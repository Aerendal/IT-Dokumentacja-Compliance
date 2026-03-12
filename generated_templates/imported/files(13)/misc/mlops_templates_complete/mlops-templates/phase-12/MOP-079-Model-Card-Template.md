---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-079: Model Card Template

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-079 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## Model Card: [Model Name]

### Model Details

| Field | Value |
|-------|-------|
| **Model Name** | [e.g., fraud-detection-xgboost] |
| **Version** | [e.g., 2.1.0] |
| **Type** | [Classification / Regression / etc.] |
| **Framework** | [XGBoost / PyTorch / etc.] |
| **Owner** | [Team / Individual] |
| **Created** | [Date] |
| **Last Updated** | [Date] |

### Model Description

**Purpose:** [What problem does this model solve?]

**Intended Use:**
- Primary use case: [Description]
- Secondary use cases: [If any]
- Out-of-scope uses: [What this model should NOT be used for]

**Input:**
```json
{
  "user_id": "string",
  "transaction_amount": "float",
  "transaction_time": "datetime",
  "merchant_category": "string"
}
```

**Output:**
```json
{
  "prediction": "int (0 or 1)",
  "probability": "float (0.0-1.0)",
  "explanation": "object (SHAP values)"
}
```

---

### Training Data

| Attribute | Value |
|-----------|-------|
| **Dataset** | [Dataset name/version] |
| **Size** | [e.g., 10M records] |
| **Date Range** | [e.g., 2023-01-01 to 2023-12-31] |
| **Features** | [Number of features] |
| **Label Distribution** | [e.g., 98% negative, 2% positive] |

**Data Sources:**
- [Source 1]
- [Source 2]

**Preprocessing:**
- [Step 1]
- [Step 2]

---

### Performance Metrics

#### Overall Performance

| Metric | Value | Baseline |
|--------|-------|----------|
| Accuracy | 0.952 | 0.940 |
| Precision | 0.891 | 0.870 |
| Recall | 0.823 | 0.800 |
| F1 Score | 0.856 | 0.834 |
| AUC-ROC | 0.978 | 0.965 |

#### Performance by Segment

| Segment | Accuracy | Precision | Recall |
|---------|----------|-----------|--------|
| Segment A | 0.96 | 0.90 | 0.85 |
| Segment B | 0.94 | 0.88 | 0.80 |
| Segment C | 0.93 | 0.87 | 0.78 |

---

### Fairness & Bias

#### Tested Attributes
- Gender
- Age group
- Geographic region

#### Fairness Metrics

| Attribute | Demographic Parity | Equalized Odds |
|-----------|-------------------|----------------|
| Gender | 0.95 | 0.92 |
| Age Group | 0.91 | 0.89 |
| Region | 0.93 | 0.90 |

**Threshold:** Demographic parity ≥ 0.8

#### Known Limitations
- [Limitation 1]
- [Limitation 2]

---

### Ethical Considerations

**Potential Risks:**
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

**Human Oversight:**
- [What decisions require human review]
- [Escalation criteria]

**Privacy:**
- PII handling: [How PII is protected]
- Data retention: [Retention period]

---

### Technical Specifications

**Model Architecture:**
```
XGBoost Classifier
- n_estimators: 500
- max_depth: 8
- learning_rate: 0.05
- subsample: 0.8
```

**Resource Requirements:**
| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 2 cores | 4 cores |
| Memory | 4 GB | 8 GB |
| GPU | Not required | Not required |

**Inference Latency:**
- P50: 15ms
- P99: 45ms

---

### Maintenance

**Monitoring:**
- Performance metrics: [Dashboard link]
- Drift detection: [Enabled/Disabled]
- Alert thresholds: [List]

**Retraining:**
- Schedule: [e.g., Monthly]
- Trigger: [e.g., Accuracy drops below 0.90]

**Dependencies:**
- Python 3.11
- XGBoost 1.7.6
- Feature Store v2.0

---

### Changelog

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2024-01-15 | Added velocity features |
| 2.0.0 | 2023-10-01 | New algorithm |
| 1.0.0 | 2023-06-01 | Initial release |

---

### References

- [Link to experiment tracking]
- [Link to training code]
- [Link to deployment config]

---

### Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Model Owner | | | |
| ML Lead | | | |
| Ethics Review | | | |
