# AI Engineer Foundations

Foundations and engineering mindset for building secure, reliable, and explainable AI systems.

---

## Purpose

This repository documents my structured progression toward becoming a competent AI engineer,
with an emphasis on engineering discipline, data reasoning, and model evaluation rather than
treating AI as a black box.

The goal is not just to use machine learning libraries, but to understand how AI systems are
built end-to-end — from raw data ingestion, through feature engineering, to evaluation and
decision-making — in a way that is reliable, reproducible, and security-aware.

---

## Philosophy

AI systems fail far more often due to poor data handling, unclear assumptions, and weak
evaluation practices than due to model choice alone.

This project prioritizes:
- clear code structure
- explicit reasoning embedded in code and documentation
- reproducible workflows
- understanding trade-offs before adding complexity

Each phase builds deliberately toward a production-style mindset.

---

## Week 1 – Engineering Foundations

### Goal
Establish strong software engineering fundamentals as the base for all future AI work.

### Why this exists
AI models are only as reliable as the engineering practices surrounding them.
Without clean structure, readable code, and disciplined version control, even strong
models become fragile and difficult to trust.

This phase mirrors how professional AI projects are set up before any modeling begins.

### What was built
- A clean, professional project structure
- Python core scripts written with clarity and intention
- Environment documentation for reproducibility
- Consistent Git commit practices

### Outcome
- Familiarity with organizing AI-oriented codebases
- Reusable Python building blocks
- A foundation ready for data-driven workflows

---

## Week 2 – Data Handling & Feature Engineering

### Goal
Learn how to transform raw, unstructured log-style data into structured,
machine-learning-ready numerical features.

### Why this exists
Machine learning models cannot reason directly over raw text reliably.
Feature quality directly determines model performance, interpretability, and
security relevance.

This phase mirrors real-world preprocessing pipelines used in security analytics,
fraud detection, and anomaly detection systems.

### What was built
- A synthetic security-style log dataset
- A parser that converts raw log lines into structured dictionaries
- A feature extraction pipeline that produces numerical features
- A CSV dataset suitable for supervised learning

### Outcome
- Ability to reason about what information a model actually “sees”
- Prepared dataset for downstream modeling
- Feature engineering code that can be reused and extended

---

## Week 3 – Practical ML Evaluation

### Goal
Develop hands-on understanding of how binary classification systems are evaluated,
with a focus on metrics that matter in security-related contexts.

### Why this exists
Accuracy alone is misleading for most real-world problems.
False positives can overwhelm analysts, while false negatives allow real threats
to go undetected.

Understanding precision, recall, and their trade-offs is essential before
deploying any AI system into production.

### What was built
- Custom implementations of TP, TN, FP, and FN counting
- Manual implementations of accuracy, precision, recall, and F1 score
- A rule-based detector evaluated using the same metrics as machine learning models

### Outcome
- Ability to critically evaluate model behavior instead of relying on defaults
- Understanding of evaluation trade-offs in security-sensitive systems
- Readiness to compare rule-based and learned approaches objectively

---

## Project Structure

```text
ai-engineer-foundations/
│
├── python_core/               # Python fundamentals with engineering intent
├── environment/               # Environment and dependency documentation
├── data/                      # Raw data and generated datasets
├── feature_engineering/       # Parsing and feature extraction pipelines
├── ml_foundations/            # Metrics, evaluation, and model logic
└── README.md                  # Project rationale and progression

---

## Week 4 – Training and Evaluating a First Machine Learning Model

### Objective
The goal of Week 4 was to move beyond rule-based detection and introduce a
machine learning–driven approach, while maintaining a strong engineering
and security-focused mindset. This phase emphasized not only training a model,
but understanding how and why models are evaluated, and what their outputs
mean in real-world security scenarios.

---

### What I Built
During this week, I implemented an end-to-end miniature machine learning
pipeline using engineered log features:

- Trained a **Logistic Regression** binary classifier on structured security log data
- Explicitly defined labels to simulate analyst judgment
- Generated predictions using the trained model
- Evaluated model performance using **custom-written security metrics**

All steps were implemented deliberately without hiding core logic behind
high-level abstractions, ensuring full understanding of the modeling process.

---

### Model Evaluation Approach
Rather than relying solely on library-provided evaluation methods, the model
was evaluated using previously implemented metric functions:

- **True Positives (TP)**
- **True Negatives (TN)**
- **False Positives (FP)**
- **False Negatives (FN)**

From these values, I computed:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

This reinforced a clear mental model of how evaluation metrics are constructed
and how they reflect model behavior.

---

### Why This Matters (Security Context)
In a security detection setting:

- **False Positives** increase analyst workload and contribute to alert fatigue
- **False Negatives** represent missed threats and elevated risk

This phase focused on understanding how TP, TN, FP, and FN directly influence
precision and recall, and why accuracy alone is often an insufficient metric
for evaluating detection systems.

Model performance was interpreted operationally, treating the classifier as
part of a security system rather than a purely statistical artifact.

---

### Key Takeaways
- Machine learning models must be evaluated in context, especially in security
- High accuracy does not necessarily imply an effective detection system
- Precision and recall represent trade-offs between analyst trust and threat coverage
- Small datasets can produce misleadingly strong metrics, highlighting the
  importance of data scale and validation strategy
- Machine learning complements rule-based systems rather than replacing them

---

### Engineering Mindset
This week reinforced an end-to-end engineering approach:

> data → features → labels → model → predictions → evaluation → interpretation

By the end of Week 4, both a **rule-based detector** and an **ML-based detector**
were evaluated using the same metrics, enabling meaningful comparison and
critical reasoning about when and where machine learning adds value.

---

### Lessons Learned
- Training a machine learning model is only one part of the system; data quality,
  label design, and evaluation strategy matter just as much as model choice.
- Errors encountered during training often reflect underlying data assumptions
  rather than coding mistakes, reinforcing the need to inspect inputs and labels
  before debugging algorithms.
- Small datasets can produce unstable or misleading evaluation results, especially
  when splitting into training and testing sets.
- Accuracy alone is insufficient for evaluating security systems; precision and
  recall better capture the operational impact of false positives and false negatives.
- Machine learning models complement rule-based detection systems by learning
  patterns from data, but do not replace the need for explicit rules and constraints.
- Interpreting model performance within a security context helps ensure that
  detection systems are both effective and usable by analysts.
