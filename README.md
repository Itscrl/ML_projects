# Machine learning coursework

Selected exercises from my undergraduate machine learning work. I am organizing the original assignments with portable data paths, reproducible setup and clearer explanations of their limits.

## Included exercise

[Bike-sharing linear regression](notebooks/bike_sharing_linear_regression.ipynb) fits a simple model to daily rental counts using the dataset's season index. It keeps the original exercise's single-feature approach and 80/20 random split (`random_state=1`), and compares its test mean squared error with a training-mean baseline.

The season index is categorical. Treating it as a number is a deliberately limited introductory example, not a suitable demand-forecasting model. The random split also does not measure prediction on future dates.

## Setup

Use Python 3.12. From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/download_bike_sharing.py
```

The downloader retrieves `day.csv` from UCI's published archive into `data/raw/bike-sharing/`. It validates the CSV before writing and refuses to overwrite an existing file. Raw data is ignored by Git. See [dataset notes](data/README.md) for provenance, attribution and the expected fields.

To open the notebook, install a notebook interface in the same environment:

```powershell
.\.venv\Scripts\python.exe -m pip install jupyterlab
.\.venv\Scripts\python.exe -m jupyterlab
```

Choose this environment's kernel and run all cells in order. The data loader locates the project from the current directory or a parent, so opening the notebook inside `notebooks/` works too. Interactive JupyterLab startup was not part of the recorded headless verification.

## Repository layout

```text
notebooks/bike_sharing_linear_regression.ipynb
scripts/download_bike_sharing.py
data/README.md
requirements.txt
```

The dependency file pins the four direct numerical/plotting packages used for the notebook. It is not a complete transitive lockfile. Saved notebook outputs and machine-specific editor metadata have been removed; rerun the notebook to generate the figures and metrics.

## Recorded verification

On 4 November 2026, all seven code cells ran headlessly with Python 3.12.14 and the pinned packages. The input contained 731 daily records, split into 584 training and 147 test rows. Test MSE was **3,098,523.61**, compared with **3,900,177.24** for predictions using the training-set mean. MSE is measured in squared daily rental counts and applies only to this split and introductory model.

The data loader was checked from both the repository root and notebook directory. A repeated download was rejected without changing the existing CSV. Interactive notebook startup and future-date forecasting were not tested.

## Authorship and scope

Maintained by Carl James Poopalaretnam. The notebook was adapted from my original `PS1_Poopalaretnam_BSCS2B/Linear Regression Scikit Learn.ipynb` assignment. This first curated import adds named column selection, a portable data loader, descriptive plot labels, a mean baseline and setup/data notes while retaining the original regression exercise.

This repository is an academic learning collection. Additional assignments will be added only after review; they are not included yet. The dataset has its own license and citation, documented separately. No blanket software license has been assigned in this import.
