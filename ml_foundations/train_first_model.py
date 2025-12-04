# train_first_model.py
# Goal: Train the first ML model using engineered features.

import csv
from pathlib import Path

def load_dataset(path: str):
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


if __name__ == "__main__":
    rows = load_dataset("data/log_features.csv")
    print("Loaded", len(rows), "rows")

    # Inspect first row
    print("Example row:", rows[0])
