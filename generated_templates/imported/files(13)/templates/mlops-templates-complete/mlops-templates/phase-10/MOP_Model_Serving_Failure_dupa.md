---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-037: Model Serving Failure Recovery

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-037 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Failure Categories

| Category | Symptoms | Severity | RTO |
|----------|----------|----------|-----|
| Complete outage | No responses, all health checks fail | Critical | 15 min |
| Partial outage | Some models unavailable | High | 30 min |
| Degraded performance | High latency, timeouts | Medium | 1 hour |
| Data/Feature issues | Wrong predictions, stale features | Medium | 1 hour |

---

## 2. Diagnosis

### 2.1 Quick Health Check

```bash
#!/bin/bash
# recovery/serving_health_check.sh

MODEL_NAME=$1
NAMESPACE="models"

echo "=== Model Serving Health Check: $MODEL_NAME ==="

# 1. Check InferenceService status
echo -e "\n[1/5] InferenceService Status:"
kubectl get inferenceservice $MODEL_NAME -n $NAMESPACE -o yaml | grep -A 20 "status:"

# 2. Check pods
echo -e "\n[2/5] Pod Status:"
kubectl get pods -l serving.kserve.io/inferenceservice=$MODEL_NAME -n $NAMESPACE

# 3. Check endpoints
echo -e "\n[3/5] Endpoint Health:"
ENDPOINT=$(kubectl get inferenceservice $MODEL_NAME -n $NAMESPACE -o jsonpath='{.status.url}')
curl -s -o /dev/null -w "%{http_code}" ${ENDPOINT}/v2/health/ready

# 4. Check recent logs
echo -e "\n[4/5] Recent Logs:"
kubectl logs -l serving.kserve.io/inferenceservice=$MODEL_NAME -n $NAMESPACE --tail=30

# 5. Check metrics
echo -e "\n[5/5] Error Rate (last 5min):"
curl -s "http://prometheus:9090/api/v1/query?query=rate(nv_inference_request_failure_total{model=\"$MODEL_NAME\"}[5m])"
```

### 2.2 Failure Decision Tree

```
Model Serving Issue
│
├─► All requests failing?
│   ├─► Yes ──► Check pod status
│   │           ├─► Pods not running ──► See "Pod Recovery"
│   │           └─► Pods running ──► Check model loading
│   │               ├─► Model load failed ──► See "Model Recovery"
│   │               └─► Model loaded ──► Check network/ingress
│   │
│   └─► No (some failing) ──► Check error patterns
│       ├─► Specific inputs failing ──► Data validation issue
│       ├─► Random failures ──► Resource constraints
│       └─► Certain pods failing ──► Pod-specific issue
│
└─► High latency only?
    ├─► Check resources (CPU/Memory/GPU)
    ├─► Check feature store latency
    └─► Check batch size / request patterns
```

---

## 3. Recovery Procedures

### 3.1 Pod Recovery

```bash
#!/bin/bash
# recovery/recover_serving_pods.sh

MODEL_NAME=$1
NAMESPACE="models"

echo "=== Recovering Model Serving Pods ==="

# 1. Check current state
echo "[1/4] Current pod state:"
kubectl get pods -l serving.kserve.io/inferenceservice=$MODEL_NAME -n $NAMESPACE

# 2. Force restart
echo "[2/4] Restarting pods..."
kubectl rollout restart deployment/${MODEL_NAME}-predictor -n $NAMESPACE

# 3. Wait for rollout
echo "[3/4] Waiting for rollout..."
kubectl rollout status deployment/${MODEL_NAME}-predictor -n $NAMESPACE --timeout=5m

# 4. Verify health
echo "[4/4] Verifying health..."
sleep 10
kubectl exec -n $NAMESPACE deploy/${MODEL_NAME}-predictor -- curl -s localhost:8080/v2/health/ready

echo "=== Recovery Complete ==="
```

### 3.2 Model Rollback

```bash
#!/bin/bash
# recovery/rollback_model.sh

MODEL_NAME=$1
TARGET_VERSION=$2
NAMESPACE="models"

echo "=== Rolling Back Model to Version $TARGET_VERSION ==="

# 1. Get current version
CURRENT=$(kubectl get inferenceservice $MODEL_NAME -n $NAMESPACE \
  -o jsonpath='{.spec.predictor.model.storageUri}')
echo "Current: $CURRENT"

# 2. Update to previous version
echo "Rolling back to version $TARGET_VERSION..."
kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE --type='json' \
  -p="[{\"op\": \"replace\", \"path\": \"/spec/predictor/model/storageUri\", \"value\": \"s3://models/$MODEL_NAME/$TARGET_VERSION\"}]"

# 3. Wait for rollout
kubectl rollout status deployment/${MODEL_NAME}-predictor -n $NAMESPACE --timeout=10m

# 4. Verify
curl -sf "https://$MODEL_NAME.example.com/v2/health/ready" && echo "Rollback successful"

# 5. Update MLflow registry
mlflow models transition-stage --name $MODEL_NAME --version $TARGET_VERSION --stage Production
```

### 3.3 Feature Store Failover

```python
# recovery/feature_failover.py
class FeatureStoreFailover:
    """Handle feature store failures during inference."""
    
    def __init__(self, primary_store, fallback_cache):
        self.primary = primary_store
        self.fallback = fallback_cache
        self.use_fallback = False
    
    def get_features(self, entity_ids: list, feature_names: list):
        """Get features with automatic failover."""
        if not self.use_fallback:
            try:
                return self.primary.get_online_features(
                    entity_rows=entity_ids,
                    features=feature_names
                )
            except Exception as e:
                logger.error(f"Primary feature store failed: {e}")
                self.use_fallback = True
                self.alert_oncall("Feature store failover activated")
        
        # Use cached/default features
        return self.fallback.get_cached_features(entity_ids, feature_names)
    
    def health_check(self):
        """Check if primary store recovered."""
        try:
            self.primary.get_online_features(
                entity_rows=[{"user_id": "health_check"}],
                features=["user_features:user_age"]
            )
            if self.use_fallback:
                logger.info("Primary feature store recovered")
                self.use_fallback = False
            return True
        except:
            return False
```

---

## 4. Failure Playbooks

### 4.1 Complete Model Outage

```markdown
## Playbook: Complete Model Outage

**Severity:** P1 Critical
**RTO:** 15 minutes

### Immediate Actions (0-5 min)
1. Acknowledge alert
2. Check if multiple models affected
3. If single model: Attempt pod restart
4. If multiple models: Check infrastructure (nodes, storage)

### Diagnosis (5-10 min)
```bash
# Check all model pods
kubectl get pods -n models

# Check node status
kubectl get nodes

# Check storage
kubectl get pv

# Check recent events
kubectl get events -n models --sort-by='.lastTimestamp' | tail -20
```

### Recovery (10-15 min)
1. If node issue: Drain and replace node
2. If storage issue: Failover to replica
3. If model issue: Rollback to last known good version

### Verification
```bash
# Test each model
for model in fraud-model rec-model; do
  curl -sf "https://$model.example.com/v2/health/ready" && echo "$model OK"
done
```
```

### 4.2 High Latency

```markdown
## Playbook: Model Serving High Latency

**Severity:** P2 High
**RTO:** 30 minutes

### Diagnosis
```bash
# Check current latency
curl -w "@curl-format.txt" -s "https://model.example.com/v2/models/fraud-model/infer" -d @test.json

# Check resource usage
kubectl top pods -n models

# Check feature store latency
curl -w "%{time_total}\n" -s "https://feast.example.com/get-online-features"
```

### Common Causes & Fixes

| Cause | Fix |
|-------|-----|
| CPU saturation | Scale horizontally |
| Memory pressure | Increase memory or scale |
| Feature store slow | Check Redis, failover if needed |
| Large batch size | Limit batch size |
| Cold start | Increase min replicas |

### Recovery
```bash
# Scale up
kubectl scale deployment/fraud-model-predictor --replicas=10 -n models

# Or adjust HPA
kubectl patch hpa fraud-model-hpa -n models -p '{"spec":{"minReplicas":5}}'
```
```

---

## 5. Automated Recovery

### 5.1 Self-Healing Configuration

```yaml
# k8s/model-serving-self-healing.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-model
spec:
  predictor:
    minReplicas: 3
    maxReplicas: 20
    scaleTarget: 10
    scaleMetric: concurrency
    
    # Liveness probe for auto-restart
    containers:
    - name: kserve-container
      livenessProbe:
        httpGet:
          path: /v2/health/live
          port: 8080
        initialDelaySeconds: 10
        periodSeconds: 10
        failureThreshold: 3
      
      # Readiness probe for traffic management
      readinessProbe:
        httpGet:
          path: /v2/health/ready
          port: 8080
        initialDelaySeconds: 20
        periodSeconds: 5
```

### 5.2 Automatic Rollback

```python
# recovery/auto_rollback.py
class AutoRollbackMonitor:
    """Monitor model serving and auto-rollback on issues."""
    
    ERROR_THRESHOLD = 0.05  # 5% error rate
    LATENCY_THRESHOLD = 200  # 200ms P99
    
    def check_and_rollback(self, model_name: str):
        """Check metrics and rollback if needed."""
        metrics = self.get_current_metrics(model_name)
        
        if metrics['error_rate'] > self.ERROR_THRESHOLD:
            logger.warning(f"Error rate {metrics['error_rate']} exceeds threshold")
            self.trigger_rollback(model_name, "high_error_rate")
            return
        
        if metrics['p99_latency'] > self.LATENCY_THRESHOLD:
            logger.warning(f"Latency {metrics['p99_latency']}ms exceeds threshold")
            # Don't auto-rollback for latency, just alert
            self.alert("high_latency", model_name, metrics)
    
    def trigger_rollback(self, model_name: str, reason: str):
        """Trigger automatic rollback."""
        previous_version = self.get_previous_version(model_name)
        
        logger.info(f"Auto-rolling back {model_name} to {previous_version}")
        
        # Execute rollback
        subprocess.run([
            "./recovery/rollback_model.sh",
            model_name,
            previous_version
        ])
        
        # Notify
        self.alert("auto_rollback", model_name, {"reason": reason})
```

---

## 6. Recovery Metrics

| Metric | Target | Current |
|--------|--------|---------|
| MTTR (P1) | <15 min | |
| MTTR (P2) | <30 min | |
| Auto-recovery success | >90% | |
| Rollback time | <5 min | |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial serving recovery |
