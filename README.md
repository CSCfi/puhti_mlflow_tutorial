# Instructions for Using the "Tutorial for MLflow in Puhti"
<small>By Erika Sternad / CSC
2024</small>

#### Updates:
2024-9-2: Added first version

2024-9-13: Added README with instruction for testing

2024-9-25: Added second version with updates based on feedback

2024-10-25: Typo fixes and minor modifications

## Getting Started

1. **Setup:**
   - You can either download the zip file and move it to your desired location, such as `/projappl/project_id/username/` or `/scratch/project_id/username/`, or clone this repository directly to Puhti/LUMI. To clone the repository directly, first run `module load git` to load the Git module.
   - Note that the tutorial includes images stored in the `/pics-` folder, so the `.ipynb` file alone will not function correctly without these images.

2. **Jupyter App Configuration:**
   When starting the Jupyter app, ensure the following settings:
     - Select the appropriate project.
     - For smooth execution of example codes:
         - *Puhti:* Increase the memory allocation to 5 GB
         - *LUMI:* Increase the number of cores to 10
     - In Puhti, use the `tensorflow` module and in LUMI, use `pytorch`.
     - Verify that your working directory is set to the location where you moved the repository.
