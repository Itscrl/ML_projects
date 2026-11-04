"""Download the daily Bike Sharing input from UCI without overwriting local data."""

from __future__ import annotations

import csv
import io
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

SOURCE_URL = "https://archive.ics.uci.edu/static/public/275/bike%2Bsharing%2Bdataset.zip"
DESTINATION = Path(__file__).resolve().parents[1] / "data/raw/bike-sharing/day.csv"


def main() -> None:
    if DESTINATION.exists():
        raise FileExistsError(f"Input already exists; it was not overwritten: {DESTINATION}")

    with urlopen(SOURCE_URL, timeout=60) as response:
        archive_bytes = response.read()
    with ZipFile(io.BytesIO(archive_bytes)) as archive:
        csv_bytes = archive.read("day.csv")

    reader = csv.DictReader(io.StringIO(csv_bytes.decode("utf-8-sig")))
    required = {"dteday", "season", "cnt"}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError("The UCI CSV does not contain the expected fields.")
    rows = list(reader)
    if not rows:
        raise ValueError("The UCI CSV is empty.")
    for row in rows:
        if int(row["season"]) not in {1, 2, 3, 4} or int(row["cnt"]) < 0:
            raise ValueError("The UCI CSV contains an invalid season or rental count.")

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("xb") as output:
        output.write(csv_bytes)
    print(f"Saved {len(rows)} daily records to {DESTINATION}")
    print(f"Source: {SOURCE_URL}")


if __name__ == "__main__":
    main()
