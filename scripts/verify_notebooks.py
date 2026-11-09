"""Run each reviewed notebook in a fresh Python process without saving outputs."""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ("bike_sharing_linear_regression.ipynb", "forest_fire_regression.ipynb")


def worker(name: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    path = ROOT / "notebooks" / name
    notebook = json.loads(path.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        raise ValueError("Expected a version 4 notebook.")
    os.chdir(path.parent)
    namespace = {"__name__": "__main__"}
    count = 0
    plt.show = plt.close
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            count += 1
            exec(compile("".join(cell["source"]), f"{name}:cell-{count}", "exec"), namespace)
    for key in ("mse", "baseline_mse"):
        if not math.isfinite(float(namespace[key])):
            raise ValueError(f"Non-finite evaluation value: {key}")
    if name == "forest_fire_regression.ipynb":
        if namespace["y"].name != "area" or "area" in namespace["X"].columns:
            raise ValueError("Forest-fire target leaked into inputs or changed from area.")
    print(json.dumps({"notebook": name, "code_cells": count, "rows": len(namespace["dataset"]), "train": len(namespace["y_train"]), "test": len(namespace["y_test"]), "mse": float(namespace["mse"]), "baseline_mse": float(namespace["baseline_mse"])}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", choices=NOTEBOOKS, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker)
        return
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    env.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))
    for name in NOTEBOOKS:
        subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker", name], cwd=ROOT, env=env, check=True)
    print("Both reviewed notebooks passed in separate fresh Python processes. Interactive Jupyter was not tested.")


if __name__ == "__main__":
    main()
