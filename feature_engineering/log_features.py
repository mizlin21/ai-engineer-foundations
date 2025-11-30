# log_features.py
# Goal: Read raw log lines from a file to turn them into features.

from pathlib import Path

def read_log_file(path: str) -> list[str]:
    """Read the log file and return a list of raw lines."""
    log_path = Path(path)
    lines = log_path.read_text(encoding="utf-8").splitlines()
    return lines

def parse_log_line(line: str) -> dict:
    """
    Convert a raw log line into a structured dictionary.

    Example line:
    2025-01-01 10:05:23,INFO,login,username=linda,ip=10.0.0.5,status=success
    """
    parts = line.split(",")

    # Defensive coding: skip malformed lines
    if len(parts) < 4:
        return {"raw": line, "parse_error": True}

    timestamp = parts[0]
    level = parts[1]
    event_type = parts[2]
    key_values = parts[3:]

    data = {
        "timestamp": timestamp,
        "level": level,
        "event_type": event_type,
        "parse_error": False,
    }

    for kv in key_values:
        if "=" in kv:
            key, value = kv.split("=", 1)
            data[key] = value

    return data

if __name__ == "__main__":
    logs = read_log_file("data/sample_logs.txt")
    print("Loaded", len(logs), "log entries")

    for line in logs:
        parsed = parse_log_line(line)
        print(parsed)

