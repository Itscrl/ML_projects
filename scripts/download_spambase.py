"""Fetch UCI's public Spambase input; preserve an existing local file."""
from pathlib import Path
import os
from urllib.request import urlopen
root = Path(__file__).resolve().parents[1]
base = Path(os.environ.get("ML_DATA_DIR") or root / "data/raw").expanduser()
if not base.is_absolute(): base = root / base
path = base / "spambase/spambase.data"
if path.exists(): raise FileExistsError(path)
with urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data", timeout=60) as response: data = response.read()
rows = data.decode("ascii").strip().splitlines()
if len(rows) != 4601 or any(len(row.split(",")) != 58 for row in rows): raise ValueError("Unexpected Spambase shape")
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("xb") as output: output.write(data)
print(f"Saved {len(rows)} rows")
