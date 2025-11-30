# binary_classification_basics.py
# Goal: Understand how we evaluate yes/no (binary) predictions.

from typing import List, Tuple


def count_outcomes(
    y_true: List[int], y_pred: List[int]
) -> Tuple[int, int, int, int]:
    """
    Count:
    - TP: true positives
    - TN: true negatives
    - FP: false positives
    - FN: false negatives
    """
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have same length")

    tp = tn = fp = fn = 0

    for truth, pred in zip(y_true, y_pred):
        if truth == 1 and pred == 1:
            tp += 1
        elif truth == 0 and pred == 0:
            tn += 1
        elif truth == 0 and pred == 1:
            fp += 1
        elif truth == 1 and pred == 0:
            fn += 1

    return tp, tn, fp, fn


if __name__ == "__main__":
    # 1 = suspicious, 0 = normal
    y_true = [0, 1, 1, 0, 1]  # ground truth labels
    y_pred = [0, 1, 0, 0, 1]  # model predictions (imperfect)

    tp, tn, fp, fn = count_outcomes(y_true, y_pred)

    print("True labels:     ", y_true)
    print("Predicted labels:", y_pred)
    print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)
