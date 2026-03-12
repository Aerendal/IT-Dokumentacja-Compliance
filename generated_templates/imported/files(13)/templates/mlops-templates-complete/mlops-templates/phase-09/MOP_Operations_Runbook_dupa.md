---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-031: MLOps Operations Runbook

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-031 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [MLOps SRE Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Monthly) |

---

## Template Content

---

# MLOps Operations Runbook

## 1. On-Call Information

### 1.1 Escalation Path

| Level | Role | Contact | Response Time |
|-------|------|---------|---------------|
| L1 | On-Call Engineer | PagerDuty | 5 min |
| L2 | Senior MLOps | PagerDuty | 15 min |
| L3 | Platform Lead | Phone | 30 min |
| L4 | Director | Phone | Critical only |

### 1.2 Key Contacts

| System | Team | Slack | Email |
|--------|------|-------|-------|
| MLflow | ML Platform | #mlops-support | mlops@company.com |
| Feature Store | Data Platform | #data-platform | data@company.com |
| Model Serving | ML Platform | #mlops-support | mlops@company.com |
| Kubernetes | Platform Eng | #platform-eng | platform@company.com |

---

## 2. Common Procedures

### 2.1 Check System Health

```bash
#!/bin/bash
# health_check.sh

echo "=== MLOps Platform Health Check ==="

# MLflow
echo -n "MLflow: "
curl -sf https://mlflow.example.com/health && echo "OK" || echo "FAILED"

# Feature Store
echo -n "Feature Store: "
curl -sf https://feast.example.com/health && echo "OK" || echo "FAILED"

# Model Serving
echo -n "Model Serving: "
for model in fraud-model rec-model nlp-model; do
  echo -n "  $model: "
  curl -sf "https://$model.models.example.com/v2/health/ready" && echo "OK" || echo "FAILED"
done

# Kubernetes pods
echo "=== Pod Status ==="
kubectl get pods -n mlops --field-selector status.phase!=Running
kubectl get pods -n models --field-selector status.phase!=Running

# Resource usage
echo "=== Resource Usage ==="
kubectl top nodes
kubectl top pods -n mlops --sort-by=memory | head -10
```

### 2.2 View Logs

```bash
# MLflow logs
kubectl logs -l app=mlflow -n mlops --tail=100 -f

# Model serving logs
kubectl logs -l serving.kserve.io/inferenceservice=fraud-model -n models --tail=100 -f

# All pods with errors
kubectl logs -l app.kubernetes.io/part-of=mlops -n mlops --tail=50 | grep -i error
```

### 2.3 Restart Services

```bash
# Restart MLflow
kubectl rollout restart deployment/mlflow-server -n mlops

# Restart model serving
kubectl rollout restart deployment/fraud-model-predictor -n models

# Restart feature server
kubectl rollout restart deployment/feast-feature-server -n feast
```

---

## 3. Alert Response Procedures

### 3.1 High Model Latency

**Alert:** `ModelLatencyHigh - P99 > 100ms for 5 minutes`

**Diagnosis:**
```bash
# Check current latency
curl -s "http://prometheus:9090/api/v1/query?query=histogram_quantile(0.99,model_inference_duration_seconds_bucket)" | jq

# Check pod resources
kubectl top pods -n models -l model=fraud-model

# Check for throttling
kubectl describe pod -l model=fraud-model -n models | grep -A5 "Last State"

# Check request queue
kubectl exec -it $(kubectl get pod -l model=fraud-model -n models -o name | head -1) \
  -- curl localhost:8002/metrics | grep queue
```

**Resolution:**
1. If CPU throttled → Scale up replicas
2. If memory pressure → Increase memory limits
3. If queue buildup → Enable/tune dynamic batching
4. If upstream slow → Check feature store latency

### 3.2 Model Serving Errors

**Alert:** `ModelErrorRateHigh - Error rate > 1%`

**Diagnosis:**
```bash
# Check error logs
kubectl logs -l model=fraud-model -n models --tail=200 | grep -i error

# Check recent changes
kubectl rollout history deployment/fraud-model-predictor -n models

# Test inference manually
curl -X POST https://fraud-model.example.com/v2/models/fraud_model/infer \
  -H "Content-Type: application/json" \
  -d '{"inputs": [{"name": "input", "shape": [1, 50], "datatype": "FP32", "data": [[0.1]*50]}]}'
```

**Resolution:**
1. If input validation errors → Check client data quality
2. If model errors → Rollback to previous version
3. If resource errors → Scale up or fix OOM
4. If dependency errors → Check upstream services

### 3.3 Feature Store Unavailable

**Alert:** `FeatureStoreDown - Health check failed`

**Diagnosis:**
```bash
# Check feast server
kubectl get pods -n feast
kubectl logs -l app=feast-server -n feast --tail=100

# Check Redis
kubectl exec -it redis-0 -n feast -- redis-cli ping

# Check PostgreSQL (registry)
kubectl exec -it $(kubectl get pod -l app=postgres -n feast -o name) -- pg_isready
```

**Resolution:**
1. Restart feast server if crashed
2. Check Redis cluster health
3. Verify network connectivity
4. Failover to backup if needed

### 3.4 MLflow Unavailable

**Alert:** `MLflowDown - API not responding`

**Diagnosis:**
```bash
# Check pods
kubectl get pods -l app=mlflow -n mlops

# Check database connectivity
kubectl exec -it $(kubectl get pod -l app=mlflow -n mlops -o name | head -1) \
  -- python -c "import psycopg2; conn = psycopg2.connect('$DB_URI'); print('DB OK')"

# Check storage
kubectl exec -it $(kubectl get pod -l app=mlflow -n mlops -o name | head -1) \
  -- aws s3 ls s3://mlflow-artifacts/
```

**Resolution:**
1. Restart MLflow pods
2. Check PostgreSQL connection
3. Verify S3 permissions
4. Scale up if resource constrained

---

## 4. Maintenance Procedures

### 4.1 Scheduled Maintenance Window

**Pre-Maintenance:**
```bash
# Notify stakeholders
./notify.sh "Scheduled maintenance starting in 30 minutes"

# Create maintenance window in monitoring
curl -X POST "http://alertmanager:9093/api/v2/silences" \
  -H "Content-Type: application/json" \
  -d '{"matchers":[{"name":"namespace","value":"mlops"}],"startsAt":"...","endsAt":"..."}'

# Backup databases
./backup_databases.sh
```

**Post-Maintenance:**
```bash
# Run health checks
./health_check.sh

# Remove maintenance window
curl -X DELETE "http://alertmanager:9093/api/v2/silence/{silence_id}"

# Notify completion
./notify.sh "Scheduled maintenance completed"
```

### 4.2 Database Maintenance

```bash
# PostgreSQL vacuum
kubectl exec -it postgres-0 -n mlops -- psql -U postgres -d mlflow -c "VACUUM ANALYZE;"

# Check table sizes
kubectl exec -it postgres-0 -n mlops -- psql -U postgres -d mlflow -c \
  "SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) FROM pg_catalog.pg_statio_user_tables ORDER BY pg_total_relation_size(relid) DESC LIMIT 10;"
```

### 4.3 Log Rotation & Cleanup

```bash
# Clean old experiment runs (>90 days, not production)
mlflow gc --backend-store-uri $MLFLOW_TRACKING_URI --older-than 90d

# Clean orphaned artifacts
./cleanup_orphan_artifacts.sh

# Compress old logs
kubectl exec -it $(kubectl get pod -l app=mlflow -o name) -- \
  find /var/log -name "*.log" -mtime +7 -exec gzip {} \;
```

---

## 5. Capacity Management

### 5.1 Check Capacity

```bash
# Node capacity
kubectl describe nodes | grep -A5 "Allocated resources"

# Namespace quotas
kubectl get resourcequotas -A

# PVC usage
kubectl get pvc -A -o custom-columns='NAMESPACE:.metadata.namespace,NAME:.metadata.name,CAPACITY:.spec.resources.requests.storage,USED:.status.capacity.storage'
```

### 5.2 Scale Operations

```bash
# Scale model serving
kubectl scale deployment fraud-model-predictor -n models --replicas=10

# Or use HPA
kubectl patch hpa fraud-model-hpa -n models -p '{"spec":{"maxReplicas":20}}'

# Add node (EKS)
eksctl scale nodegroup --cluster=mlops-cluster --name=ml-workers --nodes=5
```

---

## 6. Disaster Recovery

### 6.1 Backup Verification

```bash
# List backups
aws s3 ls s3://mlops-backups/daily/ --recursive | tail -10

# Test restore (to staging)
./restore_to_staging.sh --backup-date 2024-01-15

# Verify restore
./health_check.sh --environment staging
```

### 6.2 Failover Procedure

```bash
# Check DR readiness
./check_dr_status.sh

# Initiate failover
./failover_to_dr.sh --confirm

# Update DNS
aws route53 change-resource-record-sets --hosted-zone-id Z123 \
  --change-batch file://failover-dns.json

# Verify
curl -sf https://mlflow.example.com/health
```

---

## 7. Troubleshooting Guide

### 7.1 Decision Tree

```
Issue: Model prediction incorrect
├── Check: Input data format correct?
│   └── No → Fix client input serialization
├── Check: Feature values reasonable?
│   └── No → Check feature store freshness
├── Check: Model version expected?
│   └── No → Verify deployment, check registry
└── Check: Model behaving as trained?
    └── No → Compare with offline predictions
```

### 7.2 Common Issues

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Pods OOMKilled | Memory limit too low | Increase limits |
| Slow cold start | Large model | Use model caching |
| Connection refused | Service down | Restart pods |
| 429 errors | Rate limited | Scale up, add caching |
| Stale predictions | Old model | Check deployment |

---

## 8. Emergency Contacts

| Severity | Contact Method | SLA |
|----------|---------------|-----|
| P1 Critical | PagerDuty + Phone | 15 min |
| P2 High | PagerDuty | 30 min |
| P3 Medium | Slack #mlops-oncall | 4 hours |
| P4 Low | Jira ticket | Next sprint |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial runbook |
