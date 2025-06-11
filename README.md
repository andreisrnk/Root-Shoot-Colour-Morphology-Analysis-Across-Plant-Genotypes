## Project Proposal: Root & Shoot Colour & Morphology Analysis Across Plant Genotypes

### Background  
During my rotation in the Plant Science Lab, I worked with several tomato genotypes infected by a pathogenic fungi. To assess infection severity, we grew the plants for two weeks, then gently washed their roots and photographed both roots and shoots. Infected roots appeared noticeably darker than uninfected controls, and we wanted to quantify and compare root darkness as well as the length and width of both roots and shoots across genotypes. All images were captured using the same camera, at a fixed distance, and under consistent lighting conditions.


### Objective  
Develop a Python‐based tool that quantitatively analyzes both **colour** and **morphological** traits of roots and shoots from these images, in order to detect and compare infection-induced changes across genotypes. This will help identify genotypes that exhibit enhanced resistance or susceptibility by measuring shifts in hue, saturation, brightness, as well as root/shoot size metrics.

### What the Project Does  
1. **Image ingestion**:  
   - Load sets of TIFF/JPG images organized by genotype and treatment (infected vs. control).  
2. **Scale calibration**:  
   - Automatically detect or allow user to specify a reference object (ruler) for consistent scaling.  
3. **Region segmentation**:  
   - Identify and separate root and shoot regions—either via manual ROI selection or by applying simple colour-threshold masks.  
4. **Colour analysis**:  
   - Compute per-region colour statistics (mean & variance of HSV channels), generate heat maps of hue shift, and track temporal changes if a time series is available.  
5. **Morphological measurements**:  
   - **Root metrics**  
     - Total root length (mm) via skeletonization.  
     - Mean root width (mm) via distance transform.  
     - Count of individual root branches.  
   - **Shoot metrics**  
     - Total shoot length (mm) via user‐guided or automated skeleton tracing.  
6. **Reporting**:  
   - Export results as CSV tables and annotated overlays (e.g. false-colour maps, skeleton overlays) for downstream statistical analysis.

### Inputs & Outputs  
- **Inputs**:  
  - A directory of raw images (by genotype and treatment).  
  - (Optional) A YAML config file specifying folder structure, reference-object dimensions, and analysis parameters.  
- **Outputs**:  
  - CSV summaries (`<genotype>_<treatment>_metrics.csv`) with per-image HSV and morphological statistics.  
  - Annotated images saved under `output/heatmaps/`, `output/overlays/`, and `output/skeletons/`.  
  - Time-course plots (PNG) for each genotype showing colour and size changes over days post-inoculation.
