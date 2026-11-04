# Bike Sharing data

Source: [Bike Sharing, UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike%2Bsharing%2Bdataset). The collection covers daily and hourly rental counts from 2011-2012. This exercise uses only `day.csv`.

Citation: Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. [doi:10.24432/C5W894](https://doi.org/10.24432/C5W894).

UCI lists the dataset under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). That license applies to the dataset; it does not assign a software license to this repository.

## Obtain the input

From the repository root, run `python scripts/download_bike_sharing.py`. It downloads UCI's published ZIP, extracts only `day.csv` and writes it to `data/raw/bike-sharing/day.csv`. Existing input is preserved; move a deliberately reviewed copy elsewhere before obtaining a replacement.

The notebook expects `season` (the dataset's category index) and `cnt` (total rental count). It selects these columns by name rather than relying on column position. The downloader also checks for `dteday`, nonempty rows, valid season codes and nonnegative numeric counts before writing. No input rows are modified.

The CSV and archive are not committed. Keep this source/citation note alongside the notebook when sharing the exercise. Do not substitute unrelated data under the same filename and report it as the UCI experiment.
