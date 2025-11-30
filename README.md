# ai-engineer-foundations
Foundations and engineering mindset for AI systems

# AI Engineer Foundations

## Purpose
This repository establishes engineering foundations required to build secure and reliable AI systems.

## Week 1 Focus
- Python fundamentals with engineering mindset
- Clean project structure
- Version control discipline

## Why This Matters
AI systems fail without strong foundations. This project prioritizes clarity, reproducibility, and scalability.

## Next Steps
- Feature engineering
- Machine learning models
- Secure AI system design


## Week 2 – Data Handling & Feature Engineering

### Goals
- Turn raw security-style logs into structured, machine-readable features.
- Think like a model: what information helps detect suspicious activity?

### What I built
- `data/sample_logs.txt` – synthetic log dataset.
- `feature_engineering/log_features.py` – pipeline that:
  - reads raw logs
  - parses them into dictionaries
  - extracts numerical features (failed login, admin user, external IP, log level)
  - exports a CSV dataset (`data/log_features.csv`)

### Why this matters
Real-world AI systems depend on high-quality features.
By designing and extracting these features myself, I’m preparing for later steps
where a machine learning model will use this dataset to classify risky events.
