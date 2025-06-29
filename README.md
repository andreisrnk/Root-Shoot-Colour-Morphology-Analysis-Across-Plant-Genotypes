# 🌿 Root & Shoot Colour & Morphology Analysis Across Plant Genotypes

> **Quantifying root and shoot color, length, width, and branching from plant images using an interactive Python-based GUI.**

---

## Project Proposal: Root & Shoot Colour & Morphology Analysis Across Plant Genotypes

### Background  
During my rotation in the Plant Science Lab, I worked with several tomato genotypes infected by a pathogenic fungi. To assess infection severity, we grew the plants for two weeks, then gently washed their roots and photographed both roots and shoots. Infected roots appeared noticeably darker than uninfected controls, and we wanted to quantify and compare root darkness as well as the length and width of both roots and shoots across genotypes. All images were captured using the same camera, at a fixed distance, and under consistent lighting conditions.


### Objective  
Develop a Python‐based tool that quantitatively analyzes both **colour** and **morphological** traits of roots and shoots from these images, in order to detect and compare infection-induced changes across genotypes. This will help identify genotypes that exhibit enhanced resistance or susceptibility by measuring shifts in saturation, brightness, as well as root/shoot size metrics.

---

## 🔧 What This Project Does

This tool enables researchers to manually analyze plant root and shoot systems using high-quality images.

- ✅ Scale calibration using a **300 mm ruler**
- 🌱 Manual plant ROI selection
- 🌿 Manual root/shoot area annotation
- 🎯 Manual measurement of **root length** and **diameter**
- 🎨 Extract:
  - Mean **greenness** of shoot
  - Mean **brightness** (gray level) of root
- 🔗 Skeletonization of roots for **branch count**
- 📊 Export results to CSV  
- 🖼️ Save annotated overlays with plant labels

---

## 📷 Use Case Background

This project helps researchers:

- Compare infection **severity** visually and quantitatively  
- Detect **color shifts** and **morphological differences**  
- Identify genotypes with **enhanced resistance** or **susceptibility**  

---

## 💻 Features

| Feature                    | Description                                                              |
|---------------------------|--------------------------------------------------------------------------|
| 🧭 Manual scale calibration | Draw a box over the 300 mm ruler to calibrate mm/pixel scale             | 
| 🌱 Plant ROI selection      | Manually draw bounding boxes around each plant                           |
| 🌿 Root & shoot annotation  | Draw separate boxes for root and shoot areas                             |
| 🎯 Root length & width      | Click endpoints to measure manually                                      |
| 🎨 Color analysis           | Compute mean green (shoot) and gray (root) pixel values                  |
| 🔗 Skeleton overlay         | Auto-skeletonize root, show in red; blue tips = branch endpoints         |
| 🖼️ Annotated output         | Save images with overlaid skeletons, labels, and branch counts           |
| 📊 CSV export               | Save per-plant metrics in `professional_metrics.csv`                     |

---

## 📥 Inputs

- A **single image file** (`.jpg`, `.png`) containing multiple plants  
- The image must include a visible **300 mm ruler**  
- Manual interaction is required via mouse + keyboard  

---

## 📤 Outputs

- `professional_metrics.csv` — Per-plant data summary with columns:
  - `PlantIndex`
  - `MeanShootGreen`
  - `MeanRootGray`
  - `BranchCount`
  - `ManualLength_mm`
  - `ManualDiameter_mm`

- Annotated images:
  - `basename_plant<index>_branches.png`
  - Includes:
    - Root skeleton (🔴 red)
    - Branch endpoints (🔵 blue)
    - Plant label (`Plant 1`, etc.)

---

## ⚙️ Technical Details

### ✅ Requirements

Install dependencies:

```bash
pip install opencv-python numpy pandas matplotlib scikit-image scipy
```

### ▶️ How to Run

```bash
python professional_analyzer.py <path_to_image>
```
### 🧭 User Instructions

| Step	| Description                                                         |
|------ |---------------------------------------------------------------------|
| 1️⃣   |	Draw ruler box (300 mm known length)                                | ![image](https://github.com/user-attachments/assets/1962a96d-bc0d-462e-98ef-e7adac88babd) 
| 2️⃣   |	Draw bounding boxes around each plant                               | ![image](https://github.com/user-attachments/assets/63299ff0-147f-4cff-abb0-8cb9976237fa) 
| 3️⃣   |	For each plant: Draw root and shoot area                            |![image](https://github.com/user-attachments/assets/cde8c3cd-f27c-4c18-add7-3efe19af1d6b) ![image](https://github.com/user-attachments/assets/7ebfa789-888a-4540-b9b9-3d64c4899ed8) 
| 4️⃣   |	Manually measure root length and diameter by clicking two endpoints | ![image](https://github.com/user-attachments/assets/59e4002e-3a73-479b-9fa7-2c6063f9c034) ![image](https://github.com/user-attachments/assets/d4ff7faa-f94b-4aee-8105-3704a71ea38b) 
| 5️⃣   |	View results → press ENTER to continue or Q to quit                 | ![image](https://github.com/user-attachments/assets/8327cd3d-29b5-46dd-9554-25c0fd62c6a8) 


### ⌨️ Keyboard Shortcuts
- Z — Undo last box or point
- Enter — Confirm step / move to next plant
- Esc — Cancel current step
- Q — Quit the program and export partial results

## 📁 Folder Structure
```bash
project/
├── professional_analyzer.py         # Main script for image analysis
├── input_image.jpg                  # Example input image
├── professional_metrics.csv         # Summary of measurements
├── plant1_branches.png              # Annotated output images
├── plant2_branches.png
```

## ✅ Status
- Fully functional

## 🧪 Testing
- Verified on multiple **tomato genotypes**

## 🛠️ Mode
- **Manual-only** mode ensures higher accuracy for **small datasets**

## 🎓 Course Info
Developed as part of the course  
**Python Programming for Biologists**  
*Weizmann Institute of Science, 2024–2025*
