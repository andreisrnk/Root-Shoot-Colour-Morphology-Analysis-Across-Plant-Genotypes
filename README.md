🌿 Root & Shoot Colour & Morphology Analysis Across Plant Genotypes
Quantifying root and shoot color, length, width, and branching from plant images using an interactive Python-based GUI.

📚 Background
During my rotation in a Plant Science Lab, I worked with several tomato genotypes infected by a pathogenic fungus. To assess infection severity:

Plants were grown for 2 weeks

Roots were gently washed and photographed (along with shoots)

Infected roots appeared darker than healthy controls

All images were taken with a fixed camera setup under standard lighting to enable consistent comparisons.

🎯 Objective
Develop a Python-based tool to quantitatively analyze both colour and morphological traits of roots and shoots from images. This enables detection of infection-induced changes across genotypes by tracking:

🌈 Changes in saturation and brightness

📏 Morphological traits like root/shoot length and diameter

🔧 What This Project Does
✅ Scale calibration using a 300 mm ruler

🌱 Manual plant ROI selection

🌿 Manual root/shoot area annotation

🎯 Manual measurement of root length and diameter

🎨 Extracts:

Mean greenness of shoot

Mean brightness (gray level) of root

🔗 Root skeletonization and branch count

📊 Exports to CSV and saves annotated overlays

📷 Use Case Background
This project helps researchers:

Compare infection severity visually and quantitatively

Detect color shifts and morphological differences

Identify genotypes with enhanced resistance or susceptibility

💻 Features
Feature	Description
🧭 Manual scale calibration	Draw box over the 300 mm ruler in the image
🌱 Plant ROI selection	Manually draw boxes around each plant
🌿 Root & shoot annotation	Draw separate boxes for root and shoot areas
🎯 Root length & width	Manually measure length and diameter
🎨 Color analysis	Extract mean green (shoot) & gray (root) values
🔗 Root skeleton overlay	Auto-skeleton with red root lines and blue branch tips
🖼️ Annotated output	Save processed images with overlaid metrics
📊 CSV export	Per-plant metrics saved to professional_metrics.csv

📥 Inputs
A single image (JPG or PNG) containing one or more plants

Each image must include a 300 mm ruler

User provides manual interaction to draw bounding boxes and measure distances

📤 Outputs
professional_metrics.csv:

PlantIndex	MeanShootGreen	MeanRootGray	BranchCount	ManualLength_mm	ManualDiameter_mm
1	145.2	103.4	4	87.3	3.5

Annotated images:

basename_plant<index>_branches.png

Overlays include:

📏 Skeleton (red)

🔵 Branch endpoints (blue)

🏷️ Plant ID (white text)

⚙️ Technical Details
✅ Requirements
Install with:

bash
Copy
Edit
pip install opencv-python numpy pandas matplotlib scikit-image scipy
▶️ How to Run
bash
Copy
Edit
python professional_analyzer.py <path_to_image>
🧭 User Instructions (Interactive GUI)
Step	Description
1️⃣	Draw ruler box (300 mm known length)
2️⃣	Draw bounding boxes around each plant
3️⃣	For each plant: Draw root & shoot areas
4️⃣	Manually click to measure root length and diameter
5️⃣	View results → press ENTER to continue or Q to quit

⌨️ Keyboard Shortcuts
Z — Undo last action

Enter — Confirm / next step

Esc — Cancel step

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
✅ Fully Functional

🧪 Tested on tomato genotypes

🛠️ Precision ensured via manual control

📊 Suitable for low-throughput, high-quality data acquisition

🎓 Course Info
This project was developed as part of the course
Python Programming for Biologists
at the Weizmann Institute of Science, 2024–2025.
