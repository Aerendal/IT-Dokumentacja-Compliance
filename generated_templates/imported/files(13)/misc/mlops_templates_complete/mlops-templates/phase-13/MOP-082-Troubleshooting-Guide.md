---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-082: MLOps Troubleshooting Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-082 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Quick Diagnosis

### 1.1 Health Check Commands

```bash
# Platform health overview
kubectl get pods -n mlops
kubectl get pods -n models
kubectl get pods -n feast

# Service endpoints
curl -s https://mlflow.example.com/health
curl -s https://feast.example.com/health
curl -s https://model.example.com/v2/health/ready

# Recent errors
kubectl logs -n mlops -l app=mlflow --tail=50 | grep -i error
```

### 1.2 Common Issues Matrix

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| 502 Bad Gateway | Pod not ready | Check pod status, restart |
| Slow inference | Resource limits | Scale up replicas |
| Model not found | Registry issue | Check MLflow connection |
| Features null | Materialization failed | Run feast materialize |
| Training stuck | Resource quota | Check node capacity |

---

## 2. MLflow Issues

### 2.1 Cannot Connect to MLflow

**Symptoms:** Connection timeout, "tracking server not responding"

**Diagnosis:**
```bash
# Check MLflow pods
kubectl get pods -n mlops -l app=mlflow

# Check service
kubectl get svc mlflow -n mlops

# Check logs
kubectl logs -n mlops deploy/mlflow --tail=100
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| Pod crashed | `kubectl rollout restart deploy/mlflow -n mlops` |
| Database down | Check PostgreSQL connection |
| Network policy | Verify ingress configuration |
| DNS issue | Check CoreDNS logs |

### 2.2 Cannot Register Model

**Symptoms:** "Failed to register model", timeout during registration

**Diagnosis:**
```python
import mlflow
client = mlflow.tracking.MlflowClient()

# Check connection
try:
    client.search_experiments()
    print("Connection OK")
except Exception as e:
    print(f"Connection failed: {e}")

# Check permissions
try:
    client.create_registered_model("test-model")
    client.delete_registered_model("test-model")
    print("Permissions OK")
except Exception as e:
    print(f"Permission denied: {e}")
```

**Solutions:**
- Check S3/artifact storage permissions
- Verify database connection
- Check model size limits

---

## 3. Feature Store Issues

### 3.1 Online Features Returning Null

**Symptoms:** `get_online_features` returns None values

**Diagnosis:**
```python
from feast import FeatureStore
store = FeatureStore(repo_path=".")

# Check materialization status
for fv in store.list_feature_views():
    print(f"{fv.name}: {fv.materialization_intervals}")

# Check specific entity
features = store.get_online_features(
    features=["user_features:age"],
    entity_rows=[{"user_id": "test_user"}]
).to_dict()
print(features)
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| Not materialized | `feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)` |
| Entity not found | Verify entity exists in offline store |
| Redis connection | Check Redis connectivity |
| TTL expired | Re-materialize or increase TTL |

### 3.2 Materialization Failed

**Diagnosis:**
```bash
# Check Feast logs
kubectl logs -n feast deploy/feast-server --tail=100

# Manual materialization test
feast materialize-incremental --dry-run $(date -u +%Y-%m-%dT%H:%M:%S)
```

**Solutions:**
- Check offline store connectivity
- Verify data exists for date range
- Check Redis memory

---

## 4. Model Serving Issues

### 4.1 Model Returns 500 Error

**Symptoms:** Inference requests return HTTP 500

**Diagnosis:**
```bash
# Check model pod
kubectl get pods -n models -l model=fraud-model

# Check logs
kubectl logs -n models -l model=fraud-model --tail=100

# Check model loading
kubectl exec -n models deploy/fraud-model -- curl localhost:8080/v2/health/ready
```

**Common Causes:**
1. Model file corrupted → Re-deploy model
2. OOM during inference → Increase memory limits
3. Feature mismatch → Check input schema
4. Dependency issue → Check container image

### 4.2 High Latency

**Diagnosis:**
```bash
# Check resource usage
kubectl top pods -n models -l model=fraud-model

# Check HPA status
kubectl get hpa -n models

# Profile inference
curl -w "@curl-format.txt" -X POST https://model.example.com/v2/models/fraud-model/infer -d @test.json
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| CPU saturation | Scale horizontally |
| Memory pressure | Increase limits |
| Cold start | Increase min replicas |
| Feature latency | Check feature store |

---

## 5. Training Pipeline Issues

### 5.1 Training Job Stuck

**Diagnosis:**
```bash
# Check Airflow task
airflow tasks state training_dag task_name 2024-01-15

# Check pod
kubectl get pods -n training -l dag=training_dag

# Check events
kubectl describe pod <training-pod> -n training
```

**Common Causes:**
1. Waiting for resources → Check quotas
2. Data not available → Check data pipeline
3. Deadlock → Check distributed training config

### 5.2 OOM During Training

**Solutions:**
```python
# Reduce batch size
model.fit(X, y, batch_size=32)  # Reduced from 128

# Use gradient checkpointing
model.gradient_checkpointing_enable()

# Use mixed precision
from torch.cuda.amp import autocast
with autocast():
    output = model(input)
```

---

## 6. Data Pipeline Issues

### 6.1 Data Validation Failed

**Diagnosis:**
```python
# Check Great Expectations results
ge_context = gx.get_context()
result = ge_context.run_checkpoint("training_data_checkpoint")

print(f"Success: {result.success}")
for res in result.run_results.values():
    for exp_result in res['validation_result']['results']:
        if not exp_result['success']:
            print(f"Failed: {exp_result['expectation_config']}")
```

### 6.2 Schema Mismatch

**Diagnosis:**
```python
# Compare schemas
expected = load_schema("expected_schema.json")
actual = infer_schema(data_path)

for col in expected:
    if col not in actual:
        print(f"Missing: {col}")
    elif expected[col] != actual[col]:
        print(f"Type mismatch: {col}")
```

---

## 7. Escalation Path

| Level | Response Time | Contact |
|-------|---------------|---------|
| L1 - Self-service | Immediate | This guide + FAQ |
| L2 - Team support | <4 hours | #mlops-support Slack |
| L3 - Platform team | <1 hour | PagerDuty (critical) |
| L4 - Vendor support | Varies | Support tickets |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial troubleshooting guide |
