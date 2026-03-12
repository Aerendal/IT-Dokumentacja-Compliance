---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-029: Model Deployment Procedures

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-029 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [ML Platform Lead / Release Manager] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-012: Model Serving Design | Infrastructure |
| MOP-008: CI/CD Design | Pipeline |
| MOP-009: Model Registry | Artifacts |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-031: Runbooks | Operations |
| MOP-034: Incident Response | Rollback |

---

## Template Content

---

# Model Deployment Procedures

## 1. Deployment Overview

### 1.1 Deployment Types

| Type | Use Case | Risk Level | Approval |
|------|----------|------------|----------|
| **Standard** | Routine updates | Low | ML Lead |
| **Expedited** | Critical fixes | Medium | ML Lead + Manager |
| **Emergency** | Production issues | High | On-call + Director |

### 1.2 Deployment Strategies

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Deployment Strategy Selection                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Model Criticality?                                           │   │
│  │     │                                                        │   │
│  │     ├── Low Risk ───────► Rolling Deployment                │   │
│  │     │                                                        │   │
│  │     ├── Medium Risk ────► Canary Deployment                 │   │
│  │     │                     (5% → 25% → 50% → 100%)          │   │
│  │     │                                                        │   │
│  │     ├── High Risk ──────► Blue/Green Deployment             │   │
│  │     │                     (Full parallel environment)       │   │
│  │     │                                                        │   │
│  │     └── New Model ──────► Shadow Deployment                 │   │
│  │                           (Parallel without serving)        │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Pre-Deployment Checklist

### 2.1 Model Validation

| Check | Requirement | Verified |
|-------|-------------|----------|
| Model registered | In MLflow registry |  |
| Model card complete | All sections filled |  |
| Tests passed | All CI tests green |  |
| Performance validated | Meets baseline |  |
| Fairness reviewed | Bias within limits |  |
| Security scan passed | No critical issues |  |

### 2.2 Infrastructure Readiness

| Check | Requirement | Verified |
|-------|-------------|----------|
| Resources allocated | CPU/GPU/Memory |  |
| Monitoring configured | Dashboards ready |  |
| Alerts configured | Thresholds set |  |
| Rollback tested | Procedure verified |  |
| Documentation updated | Runbook current |  |

### 2.3 Approval Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Approval Workflow                                 │
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐         │
│  │   ML Engineer│───►│   ML Lead    │───►│  Deployment  │         │
│  │   Submits    │    │   Reviews    │    │   Approved   │         │
│  └──────────────┘    └──────────────┘    └──────────────┘         │
│                             │                                       │
│                     ┌───────┴───────┐                              │
│                     │   High Risk?  │                              │
│                     └───────┬───────┘                              │
│                             │ Yes                                   │
│                             ▼                                       │
│                     ┌──────────────┐                               │
│                     │  Director    │                               │
│                     │  Approval    │                               │
│                     └──────────────┘                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Deployment Procedures

### 3.1 Standard Rolling Deployment

```bash
#!/bin/bash
# standard_deployment.sh

MODEL_NAME=$1
MODEL_VERSION=$2
NAMESPACE="models"

echo "=== Starting Standard Deployment ==="
echo "Model: $MODEL_NAME, Version: $MODEL_VERSION"

# Step 1: Validate model
echo "[1/6] Validating model..."
mlflow models validate \
  --model-uri "models:/$MODEL_NAME/$MODEL_VERSION" \
  --test-data "s3://mlops/test-data/$MODEL_NAME.parquet"

# Step 2: Update InferenceService
echo "[2/6] Updating InferenceService..."
kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE \
  --type='json' \
  -p="[{'op': 'replace', 'path': '/spec/predictor/triton/storageUri', 
       'value': 's3://models/$MODEL_NAME/$MODEL_VERSION'}]"

# Step 3: Wait for rollout
echo "[3/6] Waiting for rollout..."
kubectl rollout status deployment/${MODEL_NAME}-predictor -n $NAMESPACE --timeout=10m

# Step 4: Verify health
echo "[4/6] Verifying health..."
ENDPOINT=$(kubectl get inferenceservice $MODEL_NAME -n $NAMESPACE \
  -o jsonpath='{.status.url}')
curl -sf "${ENDPOINT}/v2/health/ready" || exit 1

# Step 5: Run smoke tests
echo "[5/6] Running smoke tests..."
python tests/smoke_test.py --endpoint $ENDPOINT --model $MODEL_NAME

# Step 6: Update registry
echo "[6/6] Updating model stage..."
mlflow models alias set $MODEL_NAME production $MODEL_VERSION

echo "=== Deployment Complete ==="
```

### 3.2 Canary Deployment

```bash
#!/bin/bash
# canary_deployment.sh

MODEL_NAME=$1
MODEL_VERSION=$2
NAMESPACE="models"

echo "=== Starting Canary Deployment ==="

# Step 1: Deploy canary version
cat <<EOF | kubectl apply -f -
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: ${MODEL_NAME}
  namespace: ${NAMESPACE}
spec:
  predictor:
    canaryTrafficPercent: 5
    triton:
      storageUri: "s3://models/${MODEL_NAME}/${MODEL_VERSION}"
EOF

# Step 2: Monitor canary
echo "Monitoring canary at 5% traffic..."
sleep 600  # 10 minutes

# Step 3: Check metrics
CANARY_ERROR_RATE=$(prometheus_query "model_error_rate{version='canary'}")
if (( $(echo "$CANARY_ERROR_RATE > 0.01" | bc -l) )); then
  echo "ERROR: Canary error rate too high ($CANARY_ERROR_RATE)"
  kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE \
    --type='json' -p="[{'op': 'remove', 'path': '/spec/predictor/canaryTrafficPercent'}]"
  exit 1
fi

# Step 4: Increase traffic progressively
for pct in 25 50 75 100; do
  echo "Increasing canary traffic to $pct%..."
  kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE \
    --type='json' \
    -p="[{'op': 'replace', 'path': '/spec/predictor/canaryTrafficPercent', 'value': $pct}]"
  
  sleep 600  # Monitor for 10 minutes
  
  # Verify metrics
  ERROR_RATE=$(prometheus_query "model_error_rate{model='$MODEL_NAME'}")
  LATENCY_P99=$(prometheus_query "model_latency_p99{model='$MODEL_NAME'}")
  
  if (( $(echo "$ERROR_RATE > 0.01 || $LATENCY_P99 > 100" | bc -l) )); then
    echo "ERROR: Metrics degraded. Rolling back..."
    ./rollback.sh $MODEL_NAME
    exit 1
  fi
done

echo "=== Canary Deployment Complete ==="
```

### 3.3 Blue-Green Deployment

```bash
#!/bin/bash
# blue_green_deployment.sh

MODEL_NAME=$1
MODEL_VERSION=$2

# Determine current/new color
CURRENT=$(kubectl get service ${MODEL_NAME}-production -o jsonpath='{.spec.selector.version}')
if [ "$CURRENT" == "blue" ]; then NEW="green"; else NEW="blue"; fi

echo "=== Blue-Green Deployment: $CURRENT → $NEW ==="

# Step 1: Deploy new version to inactive color
kubectl set image deployment/${MODEL_NAME}-${NEW} \
  model=s3://models/${MODEL_NAME}/${MODEL_VERSION}

# Step 2: Wait for ready
kubectl rollout status deployment/${MODEL_NAME}-${NEW} --timeout=10m

# Step 3: Run validation against new version
NEW_ENDPOINT=$(kubectl get service ${MODEL_NAME}-${NEW} -o jsonpath='{.spec.clusterIP}')
python tests/validation_test.py --endpoint $NEW_ENDPOINT

# Step 4: Switch traffic
kubectl patch service ${MODEL_NAME}-production \
  -p "{\"spec\":{\"selector\":{\"version\":\"$NEW\"}}}"

# Step 5: Verify production
sleep 30
python tests/smoke_test.py --endpoint production

# Step 6: Keep old version for quick rollback
echo "Old version ($CURRENT) retained for 1 hour"
# Cleanup scheduled via CronJob

echo "=== Blue-Green Deployment Complete ==="
```

---

## 4. Rollback Procedures

### 4.1 Automatic Rollback Triggers

| Condition | Threshold | Action |
|-----------|-----------|--------|
| Error rate | >1% for 5 min | Auto rollback |
| Latency P99 | >200ms for 5 min | Auto rollback |
| Health check | 3 failures | Auto rollback |
| Memory OOM | Any | Auto rollback |

### 4.2 Manual Rollback

```bash
#!/bin/bash
# rollback.sh

MODEL_NAME=$1
PREVIOUS_VERSION=${2:-"previous"}

echo "=== Rolling Back $MODEL_NAME ==="

# Get previous version from registry
if [ "$PREVIOUS_VERSION" == "previous" ]; then
  PREVIOUS_VERSION=$(mlflow models get-latest-versions $MODEL_NAME --stages Production \
    | jq -r '.[-2].version')
fi

echo "Rolling back to version: $PREVIOUS_VERSION"

# Rollback InferenceService
kubectl rollout undo deployment/${MODEL_NAME}-predictor -n models

# Or specify version
kubectl patch inferenceservice $MODEL_NAME -n models \
  --type='json' \
  -p="[{'op': 'replace', 'path': '/spec/predictor/triton/storageUri', 
       'value': 's3://models/$MODEL_NAME/$PREVIOUS_VERSION'}]"

# Verify
kubectl rollout status deployment/${MODEL_NAME}-predictor -n models

# Update registry
mlflow models alias set $MODEL_NAME production $PREVIOUS_VERSION

# Create incident ticket
./create_incident.sh "Rollback: $MODEL_NAME to $PREVIOUS_VERSION"

echo "=== Rollback Complete ==="
```

---

## 5. Post-Deployment Verification

### 5.1 Verification Checklist

| Check | Command | Expected |
|-------|---------|----------|
| Pod status | `kubectl get pods -l model=$MODEL` | Running |
| Health check | `curl $ENDPOINT/health` | 200 OK |
| Inference test | `curl $ENDPOINT/infer -d @test.json` | Valid response |
| Latency | Grafana dashboard | <100ms P99 |
| Error rate | Grafana dashboard | <0.1% |

### 5.2 Monitoring Period

| Duration | Activity |
|----------|----------|
| 0-15 min | Active monitoring, ready to rollback |
| 15-60 min | Watch key metrics |
| 1-24 hours | Standard monitoring |
| 24-72 hours | Extended validation |

---

## 6. Deployment Templates

### 6.1 Deployment Request Form

```markdown
## Model Deployment Request

**Model Name:** _______________
**Model Version:** _______________
**Deployment Type:** [ ] Standard [ ] Expedited [ ] Emergency
**Deployment Strategy:** [ ] Rolling [ ] Canary [ ] Blue-Green

### Pre-Deployment Checklist
- [ ] Model registered in MLflow
- [ ] Model card complete
- [ ] All tests passing
- [ ] Performance validated
- [ ] Rollback plan ready

### Approvals
- [ ] ML Engineer: _______________
- [ ] ML Lead: _______________
- [ ] Director (if required): _______________

### Deployment Window
**Date:** _______________
**Time:** _______________
**Duration:** _______________

### Rollback Plan
If deployment fails:
1. _______________
2. _______________
```

### 6.2 Deployment Notification Template

```markdown
## Model Deployment Notification

**Status:** [STARTED/COMPLETED/FAILED]
**Model:** {model_name} v{version}
**Environment:** Production
**Time:** {timestamp}

### Details
- Deployment ID: {deployment_id}
- Strategy: {strategy}
- Duration: {duration}

### Metrics (Post-Deployment)
- Latency P50: {latency_p50}ms
- Latency P99: {latency_p99}ms
- Error Rate: {error_rate}%
- Success: {success_rate}%

### Next Steps
- {action_items}
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial procedures |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Lead | | | |
| Release Manager | | | |
