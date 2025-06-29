import os
import sys
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize
from scipy.ndimage import distance_transform_edt

# Set fixed window size and center
import ctypes
user32 = ctypes.windll.user32
screen_w, screen_h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
center_x, center_y = screen_w // 2 - 450, screen_h // 2 - 300  # for 900x600
WINDOW_SIZE = (900, 600)

def wait_for_enter_or_q():
    def on_key(event):
        if event.key == 'enter':
            plt.close('all')
        elif event.key == 'q':
            plt.close('all')
            print("User exited.")
            sys.exit()

    fig = plt.gcf()
    fig.canvas.mpl_connect('key_press_event', on_key)
    print("\n📌 Press ENTER to continue to next plant or Q to quit.")
    plt.show()

def draw_multiple_rois(prompt: str, image: np.ndarray) -> list:
    rois = []
    base_image = image.copy()
    window_name = "Draw ROIs"
    drawing = False
    start_x = start_y = 0

    def mouse_callback(event, x, y, flags, param):
        nonlocal drawing, start_x, start_y, base_image
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            start_x, start_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            temp = base_image.copy()
            cv2.rectangle(temp, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.putText(temp, prompt, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            cv2.putText(temp, "Z=undo  Q=quit  Enter=done  Esc=cancel", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            cv2.imshow(window_name, temp)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            x0, y0 = min(start_x, x), min(start_y, y)
            w, h = abs(x - start_x), abs(y - start_y)
            rois.append((x0, y0, w, h))
            cv2.rectangle(base_image, (x0, y0), (x0 + w, y0 + h), (0, 0, 255), 2)
            cv2.imshow(window_name, base_image)

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, *WINDOW_SIZE)
    cv2.moveWindow(window_name, center_x, center_y)
    cv2.setMouseCallback(window_name, mouse_callback)

    print(prompt)
    while True:
        display = base_image.copy()
        cv2.putText(display, prompt, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(display, "Z=undo  Q=quit  Enter=done  Esc=cancel", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        cv2.imshow(window_name, display)
        key = cv2.waitKey(1) & 0xFF
        if key in (13, 10):
            break
        elif key == 27:
            rois = []
            break
        elif key == ord("z") and rois:
            rois.pop()
            base_image = image.copy()
            for rect in rois:
                x, y, w, h = rect
                cv2.rectangle(base_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        elif key == ord("q"):
            sys.exit("User exited.")

    cv2.destroyWindow(window_name)
    return rois

def draw_single_roi(prompt: str, image: np.ndarray) -> tuple:
    rois = draw_multiple_rois(prompt, image)
    return rois[0] if rois else (0, 0, 0, 0)

def roi_mask(shape: tuple, rect: tuple) -> np.ndarray:
    height, width = shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    x, y, w, h = rect
    if w > 0 and h > 0:
        mask[y : y + h, x : x + w] = 255
    return mask

def measure_line(prompt: str, image: np.ndarray, mm_per_px: float) -> float:
    points = []
    base_image = image.copy()
    window_name = "Measure Line"

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 2:
            points.append((x, y))

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, *WINDOW_SIZE)
    cv2.moveWindow(window_name, center_x, center_y)
    cv2.setMouseCallback(window_name, mouse_callback)

    while True:
        display = base_image.copy()
        for pt in points:
            cv2.circle(display, pt, 5, (0, 0, 255), -1)
        if len(points) == 2:
            cv2.line(display, points[0], points[1], (0, 0, 255), 2)
            px = np.hypot(points[0][0] - points[1][0], points[0][1] - points[1][1])
            mm = px * mm_per_px
            cv2.putText(display, f"{mm:.1f} mm", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(display, prompt, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(display, "Z=undo  Q=quit  Enter=done  Esc=cancel", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        cv2.imshow(window_name, display)
        key = cv2.waitKey(1) & 0xFF
        if key in (13, 10) and len(points) == 2:
            break
        elif key == 27:
            points = []
            break
        elif key == ord("z") and points:
            points.pop()
        elif key == ord("q"):
            sys.exit("User exited.")

    cv2.destroyWindow(window_name)
    if len(points) == 2:
        px = np.hypot(points[0][0] - points[1][0], points[0][1] - points[1][1])
        return px * mm_per_px
    return 0.0

def calibrate_scale(ruler_rect: tuple) -> float:
    _, _, w, h = ruler_rect
    length_px = max(w, h)
    return 300.0 / length_px if length_px > 0 else 0.0

def display_results(crop, skeleton, metrics, plant_index, basename):
    kernel = np.ones((3, 3), dtype=np.uint8)
    neighbor_count = cv2.filter2D((skeleton > 0).astype(np.uint8), -1, kernel)
    endpoints = (neighbor_count == 2).astype(np.uint8)

    overlay = crop.copy()
    overlay[skeleton > 0] = (0, 0, 255)
    overlay[endpoints > 0] = (255, 0, 0)
    cv2.putText(overlay, f"Plant {plant_index}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

    out_path = f"{basename}_plant{plant_index}_branches.png"
    cv2.imwrite(out_path, cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
    axes[0].set_title(f"Plant {plant_index} Crop")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Skeleton (red) + Endpoints (blue)")
    axes[1].axis("off")

    text = (
        f"Mean shoot green : {metrics['mean_green']:.1f}\n"
        f"Mean root gray   : {metrics['mean_root']:.1f}\n"
        f"Branch count     : {metrics['branches']}\n"
        f"Manual length    : {metrics['manual_length']:.1f} mm\n"
        f"Manual diameter  : {metrics['manual_diameter']:.1f} mm"
    )
    axes[1].text(0, 0, text, color="yellow", fontsize=10, bbox={"facecolor": "black", "alpha": 0.6, "pad": 5})
    plt.tight_layout()
    wait_for_enter_or_q()

def main(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load '{image_path}'")
        return

    basename = os.path.splitext(os.path.basename(image_path))[0]
    ruler_rect = draw_single_roi("Draw RULER box (Enter=confirm, Esc=cancel)", img)
    mm_per_px = calibrate_scale(ruler_rect)
    print(f"Scale calibrated: {mm_per_px:.4f} mm/pixel")

    plant_rects = draw_multiple_rois("Draw PLANT boxes (Z=undo, Enter=done, Esc=cancel)", img)
    print(f"Selected {len(plant_rects)} plant(s).")

    results = []
    for idx, rect in enumerate(plant_rects, start=1):
        print(f"\nAnalyzing Plant {idx}")
        mask = roi_mask(img.shape, rect)
        crop = cv2.bitwise_and(img, img, mask=mask)

        root_rect = draw_single_roi(f"Draw ROOT area for Plant {idx}", crop)
        shoot_rect = draw_single_roi(f"Draw SHOOT area for Plant {idx}", crop)
        root_mask = roi_mask(crop.shape, root_rect)
        shoot_mask = roi_mask(crop.shape, shoot_rect)

        mean_green = cv2.mean(crop[:, :, 1], mask=shoot_mask)[0]
        mean_root_gray = cv2.mean(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY), mask=root_mask)[0]

        skeleton = skeletonize(root_mask > 0).astype(np.uint8) * 255
        dist = distance_transform_edt(root_mask > 0)
        radii = dist[skeleton > 0]
        diameter_mm = (2 * np.mean(radii) * mm_per_px) if radii.size else 0.0
        kernel = np.ones((3, 3), dtype=np.uint8)
        neighbor_count = cv2.filter2D((skeleton > 0).astype(np.uint8), -1, kernel)
        branch_count = int(np.count_nonzero(neighbor_count == 2))

        manual_length = measure_line(f"Measure ROOT LENGTH for Plant {idx}", crop, mm_per_px)
        manual_diameter = measure_line(f"Measure ROOT WIDTH for Plant {idx}", crop, mm_per_px)

        metrics = {
            "mean_green": mean_green,
            "mean_root": mean_root_gray,
            "branches": branch_count,
            "manual_length": manual_length,
            "manual_diameter": manual_diameter,
        }

        display_results(crop, skeleton, metrics, idx, basename)

        results.append({
            "PlantIndex": idx,
            "MeanShootGreen": mean_green,
            "MeanRootGray": mean_root_gray,
            "BranchCount": branch_count,
            "ManualLength_mm": manual_length,
            "ManualDiameter_mm": manual_diameter,
        })

    df = pd.DataFrame(results)
    df.to_csv("professional_metrics.csv", index=False)
    print("\nAll metrics saved to 'professional_metrics.csv'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python professional_analyzer.py <image_path>")
    else:
        main(sys.argv[1])
