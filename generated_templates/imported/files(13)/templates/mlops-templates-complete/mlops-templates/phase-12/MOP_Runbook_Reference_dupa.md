---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-042: Runbook Reference

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-042 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE Lead] |

---

## 1. Runbook Index

### 1.1 Service Runbooks

| Service | Runbook | Priority |
|---------|---------|----------|
| MLflow | RB-001 | Critical |
| Feast Feature Store | RB-002 | Critical |
| Triton/KServe | RB-003 | Critical |
| Airflow | RB-004 | High |
| Kubeflow | RB-005 | High |
| Prometheus/Grafana | RB-006 | High |

### 1.2 Procedure Runbooks

| Procedure | Runbook | Frequency |
|-----------|---------|-----------|
| Model Deployment | RB-010 | On demand |
| Feature Materialization | RB-011 | Daily |
| Backup & Restore | RB-012 | Daily |
| Scaling Operations | RB-013 | On demand |
| Certificate Renewal | RB-014 | Monthly |

---

## 2. Quick Reference: Common Operations

### 2.1 Health Checks

```bash
# All services health check
./scripts/health_check_all.sh

# Individual services
curl -sf https://mlflow.example.com/health
curl -sf https://feast.example.com/health  
curl -sf https://model.example.com/v2/health/ready
```

### 2.2 Service Restarts

```bash
# MLflow
kubectl rollout restart deployment/mlflow -n mlops

# Feature Store
kubectl rollout restart deployment/feast-server -n feast

# Model Serving (specific model)
kubectl rollout restart deployment/fraud-model-predictor -n models
```

### 2.3 Log Access

```bash
# Recent logs
kubectl logs -l app=mlflow -n mlops --tail=100

# Follow logs
kubectl logs -l app=mlflow -n mlops -f

# Logs with timestamp
kubectl logs -l app=mlflow -n mlops --timestamps
```

### 2.4 Scaling

```bash
# Scale model serving
kubectl scale deployment/fraud-model-predictor --replicas=10 -n models

# Check HPA
kubectl get hpa -n models
```

---

## 3. Alert Response Quick Reference

| Alert | First Action | Escalation |
|-------|--------------|------------|
| MLflowDown | Check pods, restart | 15 min → L2 |
| FeatureStoreDown | Check Redis, restart | 15 min → L2 |
| ModelHighLatency | Check resources, scale | 30 min → L2 |
| ModelHighErrorRate | Check logs, rollback | 15 min → L2 |
| PipelineFailure | Check Airflow UI | 1 hour → L2 |

---

## 4. Escalation Contacts

| Level | Role | Contact |
|-------|------|---------|
| L1 | On-Call Engineer | PagerDuty |
| L2 | Senior MLOps | PagerDuty |
| L3 | Platform Lead | Phone |
| L4 | Director | Phone (Critical) |

---

## 5. Emergency Procedures

### 5.1 Full Platform Outage

1. Page L2 immediately
2. Check Kubernetes cluster health
3. Check cloud provider status
4. Initiate DR if needed (see MOP-055)

### 5.2 Data Corruption

1. Stop affected pipelines
2. Identify corruption scope
3. Restore from backup (see RB-012)
4. Validate data integrity

### 5.3 Security Incident

1. Page Security team
2. Isolate affected systems
3. Preserve logs
4. Follow Security Incident Procedure

---

## 6. Maintenance Windows

| Window | Day | Time (UTC) | Type |
|--------|-----|------------|------|
| Primary | Tuesday | 02:00-06:00 | Standard |
| Secondary | Thursday | 02:00-06:00 | Standard |
| Emergency | Any | Any | Critical only |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial reference |
