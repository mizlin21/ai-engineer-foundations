# log_features.py
# Goal: Read raw log lines from a file to turn them into features.

from pathlib import Path

def read_log_file(path: str) -> list[str]:
    """Read the log file and return a list of raw lines."""
    log_path = Path(path)
    lines = log_path.read_text(encoding="utf-8").splitlines()
    return lines


if __name__ == "__main__":
    logs = read_log_file("data/sample_logs.txt")
    print("Loaded", len(logs), "log entries")
    for line in logs:
        print(line)
