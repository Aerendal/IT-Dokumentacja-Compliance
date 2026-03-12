---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-069: Model Rollback Procedures

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-069 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Rollback Overview

### 1.1 Rollback Triggers

| Trigger | Severity | Auto-Rollback | Response Time |
|---------|----------|---------------|---------------|
| Error rate >5% | Critical | Yes | Immediate |
| Latency P99 >500ms | High | Yes | 5 min |
| Prediction drift >0.2 | Medium | No | 30 min |
| Business metric drop | Medium | No | Manual |
| Security vulnerability | Critical | Manual | ASAP |

### 1.2 Rollback Types

| Type | Use Case | Time | Risk |
|------|----------|------|------|
| Instant | Traffic switch | Seconds | Low |
| Rolling | Gradual revert | Minutes | Low |
| Blue-Green | Full switch | Seconds | Low |
| Database | Schema rollback | Minutes-Hours | High |

---

## 2. Instant Rollback

### 2.1 KServe Rollback

```bash
#!/bin/bash
# rollback/instant_rollback.sh

MODEL_NAME=$1
TARGET_VERSION=$2
NAMESPACE="models"

echo "=== Instant Rollback: $MODEL_NAME to $TARGET_VERSION ==="

# 1. Get current version for logging
CURRENT=$(kubectl get inferenceservice $MODEL_NAME -n $NAMESPACE \
  -o jsonpath='{.spec.predictor.model.storageUri}')
echo "Current: $CURRENT"

# 2. Update to target version
echo "Rolling back to: s3://models/$MODEL_NAME/$TARGET_VERSION"
kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE --type='json' \
  -p="[{\"op\": \"replace\", \"path\": \"/spec/predictor/model/storageUri\", \"value\": \"s3://models/$MODEL_NAME/$TARGET_VERSION\"}]"

# 3. Remove any canary configuration
kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE --type='json' \
  -p="[{\"op\": \"remove\", \"path\": \"/spec/predictor/canaryTrafficPercent\"}]" 2>/dev/null || true
kubectl patch inferenceservice $MODEL_NAME -n $NAMESPACE --type='json' \
  -p="[{\"op\": \"remove\", \"path\": \"/spec/predictor/canary\"}]" 2>/dev/null || true

# 4. Wait for rollout
echo "Waiting for rollout..."
kubectl rollout status deployment/${MODEL_NAME}-predictor -n $NAMESPACE --timeout=5m

# 5. Verify health
echo "Verifying health..."
sleep 10
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" \
  "http://${MODEL_NAME}.${NAMESPACE}.svc.cluster.local/v2/health/ready")

if [ "$HEALTH" == "200" ]; then
    echo " Rollback successful"
else
    echo " Health check failed: $HEALTH"
    exit 1
fi

# 6. Log rollback event
echo "Logging rollback..."
curl -X POST "http://audit-service/api/events" \
  -H "Content-Type: application/json" \
  -d "{\"event\": \"model_rollback\", \"model\": \"$MODEL_NAME\", \"from\": \"$CURRENT\", \"to\": \"$TARGET_VERSION\", \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

echo "=== Rollback Complete ==="
```

### 2.2 Kubernetes Deployment Rollback

```bash
#!/bin/bash
# rollback/k8s_rollback.sh

DEPLOYMENT=$1
NAMESPACE=${2:-models}
REVISION=${3:-0}  # 0 = previous revision

echo "=== Kubernetes Rollback ==="

if [ "$REVISION" == "0" ]; then
    # Rollback to previous revision
    kubectl rollout undo deployment/$DEPLOYMENT -n $NAMESPACE
else
    # Rollback to specific revision
    kubectl rollout undo deployment/$DEPLOYMENT -n $NAMESPACE --to-revision=$REVISION
fi

# Wait and verify
kubectl rollout status deployment/$DEPLOYMENT -n $NAMESPACE --timeout=5m
```

---

## 3. Automated Rollback

### 3.1 Prometheus Alert Rules

```yaml
# prometheus/rollback-alerts.yaml
groups:
  - name: auto-rollback
    rules:
      - alert: ModelHighErrorRate
        expr: |
          sum(rate(inference_requests_total{status="error"}[5m])) by (model)
          /
          sum(rate(inference_requests_total[5m])) by (model) > 0.05
        for: 2m
        labels:
          severity: critical
          action: auto_rollback
        annotations:
          summary: "Model {{ $labels.model }} error rate >5%"
          runbook: "Execute instant rollback"
          
      - alert: ModelHighLatency
        expr: |
          histogram_quantile(0.99, 
            sum(rate(inference_latency_bucket[5m])) by (model, le)
          ) > 0.5
        for: 5m
        labels:
          severity: critical
          action: auto_rollback
        annotations:
          summary: "Model {{ $labels.model }} P99 latency >500ms"
```

### 3.2 Auto-Rollback Controller

```python
# rollback/auto_rollback_controller.py
import subprocess
from datetime import datetime
import requests

class AutoRollbackController:
    """Automated rollback based on metrics."""
    
    def __init__(self, prometheus_url: str, mlflow_url: str):
        self.prometheus_url = prometheus_url
        self.mlflow_url = mlflow_url
    
    def check_and_rollback(self, model_name: str):
        """Check metrics and rollback if needed."""
        
        # Check error rate
        error_rate = self._get_error_rate(model_name)
        if error_rate > 0.05:
            self._execute_rollback(model_name, f"Error rate: {error_rate:.2%}")
            return
        
        # Check latency
        latency = self._get_latency_p99(model_name)
        if latency > 500:
            self._execute_rollback(model_name, f"P99 latency: {latency}ms")
            return
    
    def _execute_rollback(self, model_name: str, reason: str):
        """Execute rollback to previous version."""
        
        # Get previous version from MLflow
        previous_version = self._get_previous_production_version(model_name)
        
        if not previous_version:
            self._alert(f"Cannot rollback {model_name}: no previous version found")
            return
        
        # Log rollback initiation
        self._log_event(model_name, "rollback_initiated", {
            "reason": reason,
            "target_version": previous_version
        })
        
        # Execute rollback script
        result = subprocess.run([
            "./rollback/instant_rollback.sh",
            model_name,
            previous_version
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            self._log_event(model_name, "rollback_completed", {
                "version": previous_version
            })
            self._alert(f" Auto-rollback successful for {model_name}")
        else:
            self._log_event(model_name, "rollback_failed", {
                "error": result.stderr
            })
            self._alert(f" Auto-rollback FAILED for {model_name}: {result.stderr}")
    
    def _get_previous_production_version(self, model_name: str) -> str:
        """Get previous production version from MLflow."""
        # Query MLflow for version history
        response = requests.get(
            f"{self.mlflow_url}/api/2.0/mlflow/registered-models/get",
            params={"name": model_name}
        )
        
        versions = response.json()['registered_model']['latest_versions']
        production_versions = [v for v in versions 
                             if v['current_stage'] == 'Production' 
                             or v['current_stage'] == 'Archived']
        
        # Sort by version number and get second latest
        sorted_versions = sorted(production_versions, 
                                key=lambda x: int(x['version']), 
                                reverse=True)
        
        if len(sorted_versions) >= 2:
            return f"v{sorted_versions[1]['version']}"
        return None
```

---

## 4. MLflow Registry Rollback

### 4.1 Stage Transition Script

```python
# rollback/mlflow_rollback.py
import mlflow
from mlflow.tracking import MlflowClient

def rollback_model_registry(model_name: str, target_version: int):
    """Rollback model in MLflow registry."""
    client = MlflowClient()
    
    # Get current production version
    current_prod = client.get_latest_versions(model_name, stages=["Production"])
    
    if current_prod:
        current_version = current_prod[0].version
        
        # Archive current production
        client.transition_model_version_stage(
            name=model_name,
            version=current_version,
            stage="Archived",
            archive_existing_versions=False
        )
        print(f"Archived version {current_version}")
    
    # Promote target version to production
    client.transition_model_version_stage(
        name=model_name,
        version=target_version,
        stage="Production"
    )
    print(f"Promoted version {target_version} to Production")
    
    # Add rollback tag
    client.set_model_version_tag(
        name=model_name,
        version=target_version,
        key="rollback_from",
        value=str(current_version) if current_prod else "initial"
    )
```

---

## 5. Rollback Verification

### 5.1 Verification Checklist

```bash
#!/bin/bash
# rollback/verify_rollback.sh

MODEL_NAME=$1
EXPECTED_VERSION=$2

echo "=== Verifying Rollback ==="

# 1. Check deployed version
DEPLOYED=$(kubectl get inferenceservice $MODEL_NAME -n models \
  -o jsonpath='{.spec.predictor.model.storageUri}')
echo "Deployed version: $DEPLOYED"

if [[ "$DEPLOYED" != *"$EXPECTED_VERSION"* ]]; then
    echo " Version mismatch!"
    exit 1
fi

# 2. Check health endpoint
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" \
  "https://$MODEL_NAME.models.example.com/v2/health/ready")
echo "Health status: $HEALTH"

if [ "$HEALTH" != "200" ]; then
    echo " Health check failed!"
    exit 1
fi

# 3. Test inference
INFERENCE=$(curl -s -o /dev/null -w "%{http_code}" \
  -X POST "https://$MODEL_NAME.models.example.com/v2/models/$MODEL_NAME/infer" \
  -H "Content-Type: application/json" \
  -d '{"inputs": [{"data": [1,2,3]}]}')
echo "Inference test: $INFERENCE"

if [ "$INFERENCE" != "200" ]; then
    echo " Inference test failed!"
    exit 1
fi

# 4. Check error rate
ERROR_RATE=$(curl -s "http://prometheus:9090/api/v1/query" \
  --data-urlencode "query=sum(rate(inference_requests_total{model=\"$MODEL_NAME\",status=\"error\"}[5m]))/sum(rate(inference_requests_total{model=\"$MODEL_NAME\"}[5m]))" \
  | jq -r '.data.result[0].value[1]')
echo "Error rate: $ERROR_RATE"

echo "=== Verification Complete  ==="
```

---

## 6. Rollback Runbook

### 6.1 Quick Reference

| Scenario | Command |
|----------|---------|
| Instant rollback | `./rollback/instant_rollback.sh MODEL VERSION` |
| K8s rollback | `kubectl rollout undo deployment/MODEL -n models` |
| Registry rollback | `python rollback/mlflow_rollback.py MODEL VERSION` |
| Verify rollback | `./rollback/verify_rollback.sh MODEL VERSION` |

### 6.2 Post-Rollback Actions

1. **Immediate:**
   - Verify service health
   - Check error rates
   - Notify stakeholders

2. **Within 1 hour:**
   - Document rollback reason
   - Create incident ticket
   - Begin root cause analysis

3. **Within 24 hours:**
   - Complete post-mortem
   - Plan fix for rolled-back changes

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial rollback procedures |
