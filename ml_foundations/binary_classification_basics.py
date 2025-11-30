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


def accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    total = tp + tn + fp + fn
    if total == 0:
        return 0.0
    return (tp + tn) / total


def precision(tp: int, fp: int) -> float:
    denom = tp + fp
    if denom == 0:
        return 0.0
    return tp / denom


def recall(tp: int, fn: int) -> float:
    denom = tp + fn
    if denom == 0:
        return 0.0
    return tp / denom


def f1_score(tp: int, fp: int, fn: int) -> float:
    p = precision(tp, fp)
    r = recall(tp, fn)
    denom = p + r
    if denom == 0:
        return 0.0
    return 2 * (p * r) / denom


if __name__ == "__main__":
    # Example scenario:
    # 1 = suspicious login, 0 = normal
    # Pretend these labels come from a security analyst.
    y_true = [0, 1, 1, 0, 1]  # ground truth labels
    y_pred = [0, 1, 0, 0, 1]  # model predictions

    tp, tn, fp, fn = count_outcomes(y_true, y_pred)

    print("True labels:     ", y_true)
    print("Predicted labels:", y_pred)
    print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)
    print("Accuracy:", accuracy(tp, tn, fp, fn))
    print("Precision:", precision(tp, fp))
    print("Recall:", recall(tp, fn))
    print("F1:", f1_score(tp, fp, fn))
