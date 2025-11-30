# rule_based_detector.py
# Goal: Use engineered features to simulate a simple rule-based detector.

import csv
from pathlib import Path
from typing import List

from binary_classification_basics import (
    count_outcomes,
    accuracy,
    precision,
    recall,
    f1_score,
)


def load_feature_rows(path: str) -> List[dict]:
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def rule_predict(features: dict) -> int:
    """
    Very basic "rule-based model":
    - suspicious if failed login from external IP
    - otherwise normal
    """
    is_failed_login = int(features.get("is_failed_login", 0))
    is_external_ip = int(features.get("is_external_ip", 0))

    if is_failed_login == 1 and is_external_ip == 1:
        return 1
    return 0


if __name__ == "__main__":
    rows = load_feature_rows("data/log_features.csv")

    # For now, let's pretend the "true" labels are:
    # suspicious if status == failed OR user == admin with external IP
    y_true = []
    y_pred = []

    for row in rows:
        status_failed = int(row.get("is_failed_login", 0))
        is_admin_user = int(row.get("is_admin_user", 0))
        is_external_ip = int(row.get("is_external_ip", 0))

        # Fake "ground truth" label rule (simulating what a human analyst might decide)
        label = 1 if (status_failed == 1 or (is_admin_user == 1 and is_external_ip == 1)) else 0

        y_true.append(label)
        y_pred.append(rule_predict(row))

    tp, tn, fp, fn = count_outcomes(y_true, y_pred)

    print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)
    print("Accuracy:", accuracy(tp, tn, fp, fn))
    print("Precision:", precision(tp, fp))
    print("Recall:", recall(tp, fn))
    print("F1:", f1_score(tp, fp, fn))
