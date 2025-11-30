# This function could later clean raw input before ML processing
def clean_log_entry(log_entry):
    return log_entry.lower().strip()

# This function simulates feature extraction
def extract_features(log_entry):
    return {
        "length": len(log_entry),
        "contains_failed": "failed" in log_entry
    }
