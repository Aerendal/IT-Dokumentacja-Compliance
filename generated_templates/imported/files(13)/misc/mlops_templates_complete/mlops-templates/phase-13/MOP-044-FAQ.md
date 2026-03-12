---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-044: MLOps Platform FAQ

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-044 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Getting Started

### Q: How do I get access to the MLOps platform?
**A:** Request access through ServiceNow ticket:
1. Go to ServiceNow → Request Access
2. Select "MLOps Platform Access"
3. Choose your role (Data Scientist, ML Engineer, etc.)
4. Manager approval required
5. Access granted within 24-48 hours

### Q: What are the prerequisites for using the platform?
**A:** 
- VPN access to corporate network
- Okta account for SSO
- Basic Python knowledge
- Completed "MLOps Platform 101" training (4 hours)

### Q: Where can I find the platform documentation?
**A:**
- Confluence: confluence.company.com/mlops
- API Docs: docs.mlops.company.com
- This Knowledge Base: kb.mlops.company.com

---

## 2. Experiment Tracking (MLflow)

### Q: How do I log my first experiment?
**A:**
```python
import mlflow

mlflow.set_tracking_uri("https://mlflow.company.com")
mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.sklearn.log_model(model, "model")
```

### Q: Why can't I see my experiments in the UI?
**A:** Common causes:
1. Wrong tracking URI - verify with `print(mlflow.get_tracking_uri())`
2. Wrong experiment name - check spelling
3. VPN not connected - ensure VPN is active
4. Permission issue - verify you have access to the experiment

### Q: How do I compare multiple runs?
**A:** In MLflow UI:
1. Go to your experiment
2. Select runs using checkboxes
3. Click "Compare" button
4. View metrics comparison charts

### Q: What's the maximum artifact size I can log?
**A:** 
- Single artifact: 5GB
- Total per run: 50GB
- Contact platform team for larger needs

---

## 3. Feature Store (Feast)

### Q: How do I access features for training?
**A:**
```python
from feast import FeatureStore

store = FeatureStore(repo_path="s3://mlops-feast/repo")

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=["user_features:age", "user_features:tenure"]
).to_df()
```

### Q: How do I access features for inference?
**A:**
```python
online_features = store.get_online_features(
    features=["user_features:age", "user_features:tenure"],
    entity_rows=[{"user_id": "123"}]
).to_dict()
```

### Q: Why are my online features returning null?
**A:** Common causes:
1. Features not materialized - run `feast materialize`
2. Entity ID not found - verify entity exists
3. Feature view not registered - check `feast feature-views list`
4. Stale materialization - check last materialization time

### Q: How often are features updated?
**A:**
- Online features: Materialized hourly
- Batch features: Updated daily at 2 AM UTC
- Streaming features: Real-time (seconds)

---

## 4. Model Registry

### Q: How do I register a model?
**A:**
```python
import mlflow

# From a run
mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="my-model"
)
```

### Q: How do I promote a model to production?
**A:**
1. Model must be in "Staging" stage first
2. Complete validation checklist
3. Request approval from ML Lead
4. Once approved:
```python
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="my-model",
    version="1",
    stage="Production"
)
```

### Q: Who can promote models to production?
**A:** Only ML Leads and Platform Admins can promote to Production. ML Engineers can promote to Staging.

---

## 5. Model Deployment

### Q: How do I deploy my model?
**A:**
1. Ensure model is in Production stage
2. Create deployment request:
```bash
kubectl apply -f my-model-deployment.yaml
```
3. Or use CI/CD pipeline (recommended)

### Q: How long does deployment take?
**A:**
- Staging: 5-10 minutes (automatic)
- Production: 15-30 minutes (with approval)

### Q: How do I rollback a bad deployment?
**A:**
```bash
# Quick rollback
kubectl rollout undo deployment/my-model -n models

# Or deploy previous version
./scripts/deploy.sh my-model v1.2 production
```

### Q: How do I test my model endpoint?
**A:**
```bash
curl -X POST https://my-model.models.company.com/v2/models/my-model/infer \
  -H "Content-Type: application/json" \
  -d '{"inputs": [{"data": [1.0, 2.0, 3.0]}]}'
```

---

## 6. Monitoring & Alerts

### Q: Where can I see my model's performance?
**A:** 
- Grafana: grafana.company.com/d/model-performance
- Select your model from dropdown

### Q: How do I set up alerts for my model?
**A:** Contact #mlops-support Slack channel with:
- Model name
- Metrics to alert on
- Threshold values
- Alert recipients

### Q: What metrics are tracked automatically?
**A:**
- Request count and rate
- Latency (P50, P95, P99)
- Error rate
- Prediction distribution
- Feature drift scores

---

## 7. Troubleshooting

### Q: My training job is stuck, what do I do?
**A:**
1. Check job status: `kubectl get pods -l job-name=<job>`
2. Check logs: `kubectl logs <pod-name>`
3. Check events: `kubectl describe pod <pod-name>`
4. Common issues: OOM, missing data, permission errors

### Q: My model inference is slow, how do I debug?
**A:**
1. Check current latency in Grafana
2. Profile your model locally
3. Check feature retrieval time
4. Consider model optimization or scaling

### Q: Who do I contact for help?
**A:**
- Slack: #mlops-support (response within 4 hours)
- Urgent issues: Page via PagerDuty
- Office hours: Tuesdays 2-3 PM

---

## 8. Best Practices

### Q: What naming conventions should I follow?
**A:**
- Experiments: `team-project-description`
- Models: `domain-model-type` (e.g., `fraud-detection-xgboost`)
- Features: `entity_attribute` (e.g., `user_lifetime_value`)

### Q: How should I version my models?
**A:**
- Use semantic versioning: MAJOR.MINOR.PATCH
- MAJOR: Breaking API changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes

### Q: What should I include in my model documentation?
**A:** At minimum:
- Model purpose and intended use
- Training data description
- Input/output schema
- Performance metrics
- Known limitations
- Owner contact

---

## 9. Policies & Compliance

### Q: What data can I use for training?
**A:**
- Only approved data sources
- PII requires special handling - contact Compliance
- Check data catalog for approved datasets

### Q: Do I need approval to deploy a model?
**A:**
- Tier 1 (high-risk): Governance Board approval
- Tier 2 (medium): ML Lead approval
- Tier 3 (low): Self-service with checklist
- Tier 4 (experimental): No approval needed

### Q: How long are model artifacts retained?
**A:**
- Production models: 7 years
- Staging models: 1 year
- Experimental: 90 days

---

## 10. Updates & Maintenance

### Q: When are maintenance windows?
**A:**
- Regular: Tuesdays 02:00-04:00 UTC
- Major: First Saturday of month 02:00-06:00 UTC

### Q: How do I get notified of platform updates?
**A:**
- Subscribe to #mlops-announcements Slack
- Check platform changelog: changelog.mlops.company.com

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial FAQ |
