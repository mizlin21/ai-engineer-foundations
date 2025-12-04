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

def extract_X_y(rows):
    """
    Split rows into:
    X = feature vectors
    y = labels
    """
    X = []
    y = []

    for row in rows:
        features = [
            int(row["is_failed_login"]),
            int(row["is_admin_user"]),
            int(row["is_external_ip"]),
            int(row["level_info"]),
            int(row["level_warn"]),
            int(row["level_error"]),
        ]

        # Label logic (simulating analyst judgment)
        label = 1 if (
            int(row["is_failed_login"]) == 1
            or (int(row["is_admin_user"]) == 1 and int(row["is_external_ip"]) == 1)
        ) else 0

        X.append(features)
        y.append(label)

    return X, y

if __name__ == "__main__":
    rows = load_dataset("data/log_features.csv")
    X, y = extract_X_y(rows)

    print("Feature vector example:", X[0])
    print("Label example:", y[0])
