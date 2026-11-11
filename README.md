# Machine learning coursework

Selected exercises from my undergraduate machine learning work. I am organizing the original assignments with portable data paths, reproducible setup and clearer explanations of their limits.

## Included exercises

[Bike-sharing linear regression](notebooks/bike_sharing_linear_regression.ipynb) fits a simple model to daily rental counts using the dataset's season index. It keeps the original exercise's single-feature approach and 80/20 random split (`random_state=1`), and compares its test mean squared error with a training-mean baseline.

The season index is categorical. Treating it as a number is a deliberately limited introductory example, not a suitable demand-forecasting model. The random split also does not measure prediction on future dates.

[Forest-fire regression](notebooks/forest_fire_regression.ipynb) revisits my PS2 assignment with an explicit `area` target. The original sequence encoded month/day before selecting the final column, which could make a dummy column the target. The curated version selects the target by name before encoding and fits a categorical preprocessing pipeline on training data only. It compares raw-area test MSE with a training-mean baseline and states the limitations of this small random split.

## Setup

Use Python 3.12. From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/download_bike_sharing.py
.\.venv\Scripts\python.exe scripts/download_forest_fires.py
```

The downloader retrieves `day.csv` from UCI's published archive into `data/raw/bike-sharing/`. It validates the CSV before writing and refuses to overwrite an existing file. Raw data is ignored by Git. See [dataset notes](data/README.md) for provenance, attribution and the expected fields.

## Use a different data directory

Both downloaders and notebooks accept `ML_DATA_DIR`, an optional base directory. Absolute paths work directly; relative paths resolve from the repository root even when the notebook is opened inside `notebooks/`. Preserve the `bike-sharing/day.csv` and `forest-fires/forestfires.csv` subpaths below that base.

```powershell
$env:ML_DATA_DIR = 'C:\Data\ml-coursework'
.\.venv\Scripts\python.exe scripts/download_bike_sharing.py
.\.venv\Scripts\python.exe scripts/download_forest_fires.py
```

The path above is an example to choose deliberately; it is not created or required by the source. Unset this session's override with `Remove-Item Env:ML_DATA_DIR` to return to the ignored repository-local data directory. Raw files are not part of this source release.

## Verify without a notebook interface

After obtaining both datasets, run:

```powershell
.\.venv\Scripts\python.exe scripts/verify_notebooks.py
```

The verifier starts a separate fresh Python process per reviewed notebook, runs its code cells with a noninteractive plotting backend, checks finite evaluation values and guards the forest-fire target/input separation. It prints the resulting row counts and metrics without saving notebook outputs. It executes the three reviewed source notebooks in this repository, so review source changes before running them. This is headless code verification, not a browser/Jupyter UI test.

To open the notebook, install a notebook interface in the same environment:

```powershell
.\.venv\Scripts\python.exe -m pip install jupyterlab
.\.venv\Scripts\python.exe -m jupyterlab
```

Choose this environment's kernel and run all cells in order. The data loader locates the project from the current directory or a parent, so opening the notebook inside `notebooks/` works too. Interactive JupyterLab startup was not part of the recorded headless verification.

## Repository layout

```text
notebooks/bike_sharing_linear_regression.ipynb
notebooks/forest_fire_regression.ipynb
scripts/download_bike_sharing.py
scripts/download_forest_fires.py
data/README.md
requirements.txt
```

The dependency file pins the four direct numerical/plotting packages used for the notebook. It is not a complete transitive lockfile. Saved notebook outputs and machine-specific editor metadata have been removed; rerun the notebook to generate the figures and metrics.

## Recorded verification

On 4 November 2026, all seven code cells ran headlessly with Python 3.12.14 and the pinned packages. The input contained 731 daily records, split into 584 training and 147 test rows. Test MSE was **3,098,523.61**, compared with **3,900,177.24** for predictions using the training-set mean. MSE is measured in squared daily rental counts and applies only to this split and introductory model.

The data loader was checked from both the repository root and notebook directory. A repeated download was rejected without changing the existing CSV. Interactive notebook startup and future-date forecasting were not tested.

On 9 November 2026, the five forest-fire code cells ran headlessly on 517 rows (413 training, 104 test). Test MSE was **5,894.30 squared hectares**, versus **5,852.81** for the training-mean baseline. The linear model performed slightly worse on this split and produced 15 negative predictions. These limitations are reported rather than removed from the evaluation. No forecasting or operational-use claim follows from the exercise.

## Authorship and scope

Maintained by Carl James Poopalaretnam. The notebook was adapted from my original `PS1_Poopalaretnam_BSCS2B/Linear Regression Scikit Learn.ipynb` assignment. This first curated import adds named column selection, a portable data loader, descriptive plot labels, a mean baseline and setup/data notes while retaining the original regression exercise.

This repository is an academic learning collection. Additional assignments will be added only after review; they are not included yet. The dataset has its own license and citation, documented separately. No blanket software license has been assigned in this import.

## Spam classification

`notebooks/spam_classification.ipynb` curates my PS3 exercise with raw-row splitting followed by a train-fitted scaling/classification pipeline. Run `python scripts/download_spambase.py` first, then execute the notebook. Run `python -m unittest discover -s tests -v` for the held-out-extremes regression check. The shared verifier now executes this classifier alongside both regression notebooks in separate fresh processes. Its preprocessing regression test imports the same pipeline factory as the notebook.
