## Project Proposal: Root & Shoot Colour & Morphology Analysis Across Plant Genotypes

### Background  
During my rotation in the Plant Science Lab, I worked with several tomato genotypes infected by a pathogenic fungi. To assess infection severity, we grew the plants for two weeks, then gently washed their roots and photographed both roots and shoots. Infected roots appeared noticeably darker than uninfected controls, and we wanted to quantify and compare root darkness as well as the length and width of both roots and shoots across genotypes. All images were captured using the same camera, at a fixed distance, and under consistent lighting conditions.


### Objective  
Develop a Python‐based tool that quantitatively analyzes both **colour** and **morphological** traits of roots and shoots from these images, in order to detect and compare infection-induced changes across genotypes. This will help identify genotypes that exhibit enhanced resistance or susceptibility by measuring shifts in hue, saturation, brightness, as well as root/shoot size metrics.

Root & Shoot Morphology and Color Analyzer
A professional Python-based tool to manually analyze morphological and color traits of root and shoot tissues from plant images. Developed during my MSc rotation in a Plant Science lab, this tool was used to study tomato genotypes infected with pathogenic fungi.


🔬 Project Summary
This tool enables manual image-based quantification of plant morphology and color:

Root & shoot segmentation via interactive bounding boxes.

Manual measurement of root length and width.

Color extraction (mean shoot greenness and root darkness).

Root branching detection using skeleton overlays.

Results visualization and CSV export.

📷 Use Case Background
During fungal infection experiments, infected tomato roots appeared visually darker than controls. By capturing standardized images (same lighting and distance), we aimed to:

Compare infection severity across genotypes.

Quantify root darkness, branching, and length/width.

Identify resistant vs. susceptible genotypes.

💻 Features
Feature	Description
🧭 Manual scale calibration	Draw box over a 300 mm ruler in the image.
🌱 Plant ROI selection	Draw bounding boxes over each plant manually.
🌿 Root & shoot annotation	Draw separate boxes for root and shoot areas.
🎯 Manual length/width measurement	Click to measure root length and diameter.
🎨 Color analysis	Mean shoot green (G channel) and root gray (brightness) values.
🔗 Skeleton overlay	Auto-detects root skeletons, overlays red lines and blue branch tips.
🖼️ Visual output	Saves annotated images and plots.
📊 CSV export	Per-plant metrics saved to professional_metrics.csv.

📥 Inputs
A single image file (.jpg, .png, etc.) of one or more plants.

Ruler must be included in the image (300 mm length).

Manual interaction required throughout the process.

📤 Outputs
professional_metrics.csv — summary of root/shoot traits for all plants.

Annotated images for each plant (e.g. plant1_branches.png).

Interactive matplotlib figure for each plant with measurements and overlay.

⚙️ How to Run
1. Install requirements:
bash
Copy
Edit
pip install opencv-python numpy pandas matplotlib scikit-image scipy
2. Run the script:
bash
Copy
Edit
python professional_analyzer.py <path_to_image>
🧭 User Instructions (Interactive GUI)
Step	Action
1.	Draw ruler box (300 mm known length).
2.	Draw plant boxes (one per plant).
3.	For each plant:
a) Draw root area,
b) Draw shoot area.
4.	Measure root length and width manually by clicking endpoints.
5.	View annotated figure and press ENTER to continue to next plant or Q to quit.

Keyboard controls during drawing:

Z — Undo last box or click

Enter — Confirm step

Esc — Cancel current step

Q — Quit program

📁 Folder Structure
lua
Copy
Edit
project/
├── professional_analyzer.py
├── input_image.jpg
├── professional_metrics.csv
├── output/
│   ├── plant1_branches.png
│   ├── plant2_branches.png
✅ Status
✅ Functional
🧪 Tested with multiple tomato genotypes
🛠️ Manual-only workflow ensures precision for small datasets

🎓 Course Info
This project was developed as part of the course Python Programming for Biologists at Weizmann Institute of Science, 2024–2025.
