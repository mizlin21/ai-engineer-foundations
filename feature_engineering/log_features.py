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

# Potential features for each log entry:
# - is_failed_login: did the status equal "failed"?
# - is_admin_user: is the username "admin"?
# - is_external_ip: is the IP outside private ranges 10.x, 192.168.x, 172.16-31.x?
# - level_encoded: INFO=0, WARN=1, ERROR=2, etc.

def is_private_ip(ip: str) -> bool:
    """Very simple check to see if an IP is from a private range."""
    return (
        ip.startswith("10.") or
        ip.startswith("192.168.") or
        ip.startswith("172.16.") or
        ip.startswith("172.17.") or
        ip.startswith("172.18.") or
        ip.startswith("172.19.") or
        ip.startswith("172.20.") or
        ip.startswith("172.21.") or
        ip.startswith("172.22.") or
        ip.startswith("172.23.") or
        ip.startswith("172.24.") or
        ip.startswith("172.25.") or
        ip.startswith("172.26.") or
        ip.startswith("172.27.") or
        ip.startswith("172.28.") or
        ip.startswith("172.29.") or
        ip.startswith("172.30.") or
        ip.startswith("172.31.")
    )
