# train_first_model.py
# Goal: Train the first ML model using engineered features.

import csv
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from binary_classification_basics import (
    count_outcomes,
    accuracy,
    precision,
    recall,
    f1_score,
)

def load_dataset(path: str):
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def extract_X_y(rows):
    """
    Split rows into:
    X - feature vectors
    y - labels
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

        # Learning safeguard: ensure at least two classes exist
        label = 1 if int(row["is_failed_login"]) == 1 else 0

        X.append(features)
        y.append(label)

    return X, y


if __name__ == "__main__":
    rows = load_dataset("data/log_features.csv")
    print("Loaded", len(rows), "rows")
    print("Example row:", rows[0])

    X, y = extract_X_y(rows)
    print("Label distribution:", set(y))

    # For this tiny dataset, train on all data
    X_train, y_train = X, y

    model = LogisticRegression()
    model.fit(X_train, y_train)

    print("Model trained successfully")

    # Use the model to make predictions on the same data
    y_pred = model.predict(X)

    # Convert predictions to a regular Python list (for the metric functions)
    y_pred = list(y_pred)

    tp, tn, fp, fn = count_outcomes(y, y_pred)

    print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)

    acc = accuracy(tp, tn, fp, fn)
    prec = precision(tp, fp)
    rec = recall(tp, fn)
    f1 = f1_score(tp, fp, fn)

    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1:", f1)
