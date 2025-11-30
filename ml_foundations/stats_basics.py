# stats_basics.py
# Goal: Build intuition for basic statistics used in ML.

from typing import List


def mean(values: List[float]) -> float:
    """Compute the average of a list of numbers."""
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def minimum(values: List[float]) -> float:
    """Return the smallest value."""
    if not values:
        raise ValueError("Cannot compute minimum of empty list")
    return min(values)


def maximum(values: List[float]) -> float:
    """Return the largest value."""
    if not values:
        raise ValueError("Cannot compute maximum of empty list")
    return max(values)


if __name__ == "__main__":
    # Example "risk scores" to simulate model outputs
    risk_scores = [0.1, 0.4, 0.9, 0.3, 0.8]

    print("Risk scores:", risk_scores)
    print("Mean risk score:", mean(risk_scores))
    print("Min risk score:", minimum(risk_scores))
    print("Max risk score:", maximum(risk_scores))
