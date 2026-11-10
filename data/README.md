# Bike Sharing data

Source: [Bike Sharing, UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike%2Bsharing%2Bdataset). The collection covers daily and hourly rental counts from 2011-2012. This exercise uses only `day.csv`.

Citation: Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. [doi:10.24432/C5W894](https://doi.org/10.24432/C5W894).

UCI lists the dataset under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). That license applies to the dataset; it does not assign a software license to this repository.

## Obtain the input

From the repository root, run `python scripts/download_bike_sharing.py`. It downloads UCI's published ZIP, extracts only `day.csv` and writes it to `data/raw/bike-sharing/day.csv`. Existing input is preserved; move a deliberately reviewed copy elsewhere before obtaining a replacement.

The notebook expects `season` (the dataset's category index) and `cnt` (total rental count). It selects these columns by name rather than relying on column position. The downloader also checks for `dteday`, nonempty rows, valid season codes and nonnegative numeric counts before writing. No input rows are modified.

The CSV and archive are not committed. Keep this source/citation note alongside the notebook when sharing the exercise. Do not substitute unrelated data under the same filename and report it as the UCI experiment.

## Forest Fires

Source: [Forest Fires, UCI](https://archive.ics.uci.edu/dataset/162/forest%2Bfires). Citation: Cortez, P. and Morais, A. (2007). *Forest Fires* [Dataset]. [doi:10.24432/C5D88D](https://doi.org/10.24432/C5D88D). UCI lists CC BY 4.0 for this dataset too.

Run `python scripts/download_forest_fires.py` from the repository root to obtain `data/raw/forest-fires/forestfires.csv`. Raw CSV files stay ignored. The target is the named `area` column, measured in hectares. Month and day are categorical inputs; the notebook fits their encoder on training rows only. The exercise predicts raw burned area with a simple linear baseline rather than reproducing the original paper's log-transform/cross-validation experiments.

Set `ML_DATA_DIR` to relocate both inputs without editing a notebook. It is a base directory with the same dataset subfolders; relative overrides resolve from the repository root. Only the reviewed public dataset files should be used when reproducing the recorded results. A different input is a different experiment.

## Spambase

Obtain the public UCI Spambase input with `python scripts/download_spambase.py`. It uses the same optional `ML_DATA_DIR` base and stores `spambase/spambase.data` outside Git. Source and dataset terms: https://archive.ics.uci.edu/dataset/94/spambase . The input has 4,601 rows, 57 features and one binary target. Consult UCI for attribution and reuse terms; no dataset is redistributed here.
