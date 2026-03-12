---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-083: MLOps Platform Onboarding Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-083 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Welcome to MLOps Platform

### 1.1 Platform Overview

The MLOps platform provides end-to-end infrastructure for:
- Experiment tracking and model registry
- Feature engineering and storage
- Model training and deployment
- Monitoring and observability

### 1.2 Key Components

| Component | Purpose | URL |
|-----------|---------|-----|
| MLflow | Experiment tracking, model registry | mlflow.company.com |
| Feast | Feature store | feast.company.com |
| KServe | Model serving | models.company.com |
| Grafana | Monitoring dashboards | grafana.company.com |

---

## 2. Getting Started

### 2.1 Prerequisites

- [ ] Corporate laptop with VPN access
- [ ] Okta account activated
- [ ] GitHub access to ml-platform repositories
- [ ] AWS SSO configured

### 2.2 Access Request

1. Submit ServiceNow ticket: "MLOps Platform Access"
2. Select your role: Data Scientist / ML Engineer / Other
3. Request approval from your manager
4. Wait for provisioning (24-48 hours)

### 2.3 Environment Setup

```bash
# 1. Clone the starter repository
git clone https://github.com/company/mlops-starter.git
cd mlops-starter

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure credentials
cp .env.example .env
# Edit .env with your credentials

# 5. Verify setup
python scripts/verify_setup.py
```

---

## 3. First Week Checklist

### Day 1: Access & Environment

- [ ] Complete access requests
- [ ] Set up development environment
- [ ] Join Slack channels: #mlops-support, #mlops-announcements
- [ ] Review platform documentation

### Day 2: MLflow Basics

- [ ] Complete MLflow tutorial (1 hour)
- [ ] Run your first experiment
- [ ] Log parameters, metrics, and artifacts
- [ ] View results in MLflow UI

```python
# Quick start: Your first MLflow experiment
import mlflow

mlflow.set_tracking_uri("https://mlflow.company.com")
mlflow.set_experiment("onboarding-test")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    print("Success! Check MLflow UI")
```

### Day 3: Feature Store

- [ ] Complete Feast tutorial (1 hour)
- [ ] Browse existing feature views
- [ ] Retrieve features for a sample entity

```python
# Quick start: Retrieve features
from feast import FeatureStore

store = FeatureStore(repo_path="s3://mlops-feast/repo")

features = store.get_online_features(
    features=["user_features:age", "user_features:tenure"],
    entity_rows=[{"user_id": "sample_user"}]
).to_dict()

print(features)
```

### Day 4: Model Deployment

- [ ] Understand deployment process
- [ ] Review existing deployed models
- [ ] Walk through deployment checklist

### Day 5: Monitoring & Support

- [ ] Explore Grafana dashboards
- [ ] Set up personal alerts
- [ ] Know how to get help

---

## 4. Training Path

### 4.1 Required Training

| Course | Duration | Deadline |
|--------|----------|----------|
| MLOps Platform 101 | 4 hours | Week 1 |
| Security & Compliance | 2 hours | Week 2 |
| Data Handling Guidelines | 1 hour | Week 2 |

### 4.2 Role-Specific Training

**Data Scientists:**
- Advanced experiment tracking (2h)
- Feature engineering best practices (2h)

**ML Engineers:**
- CI/CD for ML (4h)
- Model serving deep dive (2h)
- Infrastructure overview (2h)

### 4.3 Certifications

- Bronze: MLOps Practitioner (Month 1)
- Silver: MLOps Engineer (Month 3)
- Gold: MLOps Expert (Month 6+)

---

## 5. Best Practices

### 5.1 Naming Conventions

| Entity | Convention | Example |
|--------|------------|---------|
| Experiment | team-project-description | fraud-detection-v2 |
| Model | domain-type | fraud-xgboost |
| Feature View | entity_features | user_transaction_features |
| Branch | type/description | feature/add-velocity |

### 5.2 Code Standards

```python
# Always log experiments
with mlflow.start_run():
    mlflow.log_params(config)
    mlflow.log_metrics(metrics)
    mlflow.log_artifact("config.yaml")

# Always version your data
mlflow.set_tag("data.version", "v2024.01.15")

# Always set random seeds
random.seed(42)
np.random.seed(42)
```

### 5.3 Documentation Requirements

Every model needs:
- Model card (MOP-079)
- Training code in Git
- MLflow experiment link
- Deployment runbook

---

## 6. Getting Help

### 6.1 Support Channels

| Channel | Use For | Response |
|---------|---------|----------|
| #mlops-support | Questions, issues | <4 hours |
| Office Hours | Complex discussions | Tues 2-3 PM |
| Documentation | Self-service | Immediate |
| PagerDuty | Production critical | <15 min |

### 6.2 Useful Links

- Documentation: docs.mlops.company.com
- FAQ: [MOP-044](./MOP-044-FAQ.md)
- Troubleshooting: [MOP-082](./MOP-082-Troubleshooting-Guide.md)

---

## 7. Onboarding Completion

### 7.1 Checklist Sign-off

| Item | Completed | Date |
|------|-----------|------|
| Environment setup | [ ] | |
| MLflow tutorial | [ ] | |
| Feature store tutorial | [ ] | |
| Required training | [ ] | |
| First experiment logged | [ ] | |

### 7.2 Feedback

Please provide feedback on your onboarding experience:
[Onboarding Feedback Form](https://forms.company.com/mlops-onboarding)

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial onboarding guide |
