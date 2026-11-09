"""Download UCI Forest Fires without overwriting local input."""
from __future__ import annotations

import csv
import io
import os
import math
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

SOURCE_URL = "https://archive.ics.uci.edu/static/public/162/forest%2Bfires.zip"
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = Path(os.environ.get("ML_DATA_DIR") or REPOSITORY_ROOT / "data/raw").expanduser()
if not DATA_ROOT.is_absolute():
    DATA_ROOT = REPOSITORY_ROOT / DATA_ROOT
DESTINATION = DATA_ROOT / "forest-fires/forestfires.csv"


def main() -> None:
    if DESTINATION.exists():
        raise FileExistsError(f"Input already exists; not overwritten: {DESTINATION}")
    with urlopen(SOURCE_URL, timeout=60) as response:
        archive_bytes = response.read()
    with ZipFile(io.BytesIO(archive_bytes)) as archive:
        data = archive.read("forestfires.csv")
    reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
    expected = {"X", "Y", "month", "day", "FFMC", "DMC", "DC", "ISI", "temp", "RH", "wind", "rain", "area"}
    if not expected.issubset(reader.fieldnames or []):
        raise ValueError("The input does not have the expected Forest Fires columns.")
    rows = list(reader)
    if not rows or any(not math.isfinite(float(r["area"])) or float(r["area"]) < 0 for r in rows):
        raise ValueError("The input is empty or contains invalid burned-area values.")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("xb") as output:
        output.write(data)
    print(f"Saved {len(rows)} records to {DESTINATION}")


if __name__ == "__main__":
    main()
