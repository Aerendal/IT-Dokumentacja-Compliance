---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-067: Canary Deployment Procedures

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-067 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Canary Deployment Overview

### 1.1 When to Use Canary

| Scenario | Use Canary | Rationale |
|----------|------------|-----------|
| New model version |  | Validate performance |
| Major model changes |  | Risk mitigation |
| Algorithm change |  | Compare effectiveness |
| Minor config update |  | Low risk, use rolling |
| Bug fix (tested) |  | Use rolling |

### 1.2 Canary Stages

```
┌─────────────────────────────────────────────────────────────┐
│                 Canary Deployment Stages                     │
│                                                             │
│  100% ──────────────────────────────────────────────── Old  │
│   │                                                         │
│   │    Stage 1    Stage 2    Stage 3    Stage 4            │
│   │    (5%)       (25%)      (50%)      (100%)             │
│   │      │          │          │          │                │
│   ▼      ▼          ▼          ▼          ▼                │
│   0% ─────────────────────────────────────────────── New   │
│        30min       2hr        4hr       Complete           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Canary Configuration

### 2.1 KServe Canary Setup

```yaml
# model-canary-deployment.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-model
  namespace: models
spec:
  predictor:
    # Current production version
    model:
      modelFormat:
        name: mlflow
      storageUri: "s3://models/fraud-model/v1.2.0"
    
    # Canary version
    canaryTrafficPercent: 5
    canary:
      model:
        modelFormat:
          name: mlflow
        storageUri: "s3://models/fraud-model/v1.3.0"
```

### 2.2 Istio Traffic Split

```yaml
# istio-canary-traffic.yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fraud-model-vs
  namespace: models
spec:
  hosts:
    - fraud-model.models.svc.cluster.local
  http:
    - route:
        - destination:
            host: fraud-model-stable
            port:
              number: 80
          weight: 95
        - destination:
            host: fraud-model-canary
            port:
              number: 80
          weight: 5
```

---

## 3. Canary Analysis

### 3.1 Success Criteria

| Metric | Threshold | Action if Failed |
|--------|-----------|------------------|
| Error rate | <0.5% | Auto-rollback |
| P99 latency | <100ms | Auto-rollback |
| P50 latency | <50ms | Alert, manual review |
| Prediction drift | <0.1 | Alert, manual review |

### 3.2 Automated Analysis (Flagger)

```yaml
# flagger-canary-analysis.yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: fraud-model
  namespace: models
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-model
  progressDeadlineSeconds: 3600
  
  service:
    port: 80
    targetPort: 8080
  
  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    
    metrics:
      - name: request-success-rate
        thresholdRange:
          min: 99.5
        interval: 1m
      - name: request-duration
        thresholdRange:
          max: 100
        interval: 1m
    
    webhooks:
      - name: load-test
        url: http://flagger-loadtester/
        timeout: 5s
        metadata:
          cmd: "hey -z 1m -q 10 -c 2 http://fraud-model-canary:8080/predict"
```

### 3.3 Custom Metrics Analysis

```python
# canary/analysis.py
from dataclasses import dataclass
from typing import Optional
import requests

@dataclass
class CanaryAnalysisResult:
    passed: bool
    metrics: dict
    recommendation: str

class CanaryAnalyzer:
    """Analyze canary deployment metrics."""
    
    def __init__(self, prometheus_url: str):
        self.prometheus_url = prometheus_url
    
    def analyze(self, model_name: str, duration_minutes: int = 30) -> CanaryAnalysisResult:
        """Analyze canary vs stable metrics."""
        
        metrics = {
            'canary_error_rate': self._get_error_rate(model_name, 'canary', duration_minutes),
            'stable_error_rate': self._get_error_rate(model_name, 'stable', duration_minutes),
            'canary_latency_p99': self._get_latency(model_name, 'canary', duration_minutes),
            'stable_latency_p99': self._get_latency(model_name, 'stable', duration_minutes),
        }
        
        # Compare metrics
        error_rate_ok = metrics['canary_error_rate'] <= metrics['stable_error_rate'] * 1.1
        latency_ok = metrics['canary_latency_p99'] <= metrics['stable_latency_p99'] * 1.2
        
        passed = error_rate_ok and latency_ok
        
        if passed:
            recommendation = "PROMOTE - Canary metrics within acceptable range"
        else:
            issues = []
            if not error_rate_ok:
                issues.append("Error rate elevated")
            if not latency_ok:
                issues.append("Latency increased")
            recommendation = f"ROLLBACK - {', '.join(issues)}"
        
        return CanaryAnalysisResult(
            passed=passed,
            metrics=metrics,
            recommendation=recommendation
        )
    
    def _get_error_rate(self, model: str, version: str, minutes: int) -> float:
        query = f'sum(rate(inference_requests_total{{model="{model}",version="{version}",status="error"}}[{minutes}m])) / sum(rate(inference_requests_total{{model="{model}",version="{version}"}}[{minutes}m]))'
        return self._query_prometheus(query)
    
    def _get_latency(self, model: str, version: str, minutes: int) -> float:
        query = f'histogram_quantile(0.99, sum(rate(inference_latency_bucket{{model="{model}",version="{version}"}}[{minutes}m])) by (le))'
        return self._query_prometheus(query)
```

---

## 4. Canary Deployment Script

### 4.1 Deployment Script

```bash
#!/bin/bash
# canary/deploy_canary.sh

MODEL_NAME=$1
NEW_VERSION=$2
INITIAL_PERCENTAGE=${3:-5}

echo "=== Starting Canary Deployment ==="
echo "Model: $MODEL_NAME"
echo "New Version: $NEW_VERSION"
echo "Initial Traffic: $INITIAL_PERCENTAGE%"

# 1. Deploy canary version
echo "[1/5] Deploying canary..."
kubectl patch inferenceservice $MODEL_NAME -n models --type='json' \
  -p="[
    {\"op\": \"add\", \"path\": \"/spec/predictor/canaryTrafficPercent\", \"value\": $INITIAL_PERCENTAGE},
    {\"op\": \"add\", \"path\": \"/spec/predictor/canary\", \"value\": {\"model\": {\"storageUri\": \"s3://models/$MODEL_NAME/$NEW_VERSION\"}}}
  ]"

# 2. Wait for canary to be ready
echo "[2/5] Waiting for canary to be ready..."
kubectl wait --for=condition=Ready inferenceservice/$MODEL_NAME -n models --timeout=10m

# 3. Initial analysis (30 min)
echo "[3/5] Running initial analysis (30 min)..."
sleep 1800
python canary/analysis.py $MODEL_NAME 30

# 4. Check results
if [ $? -eq 0 ]; then
    echo "[4/5] Initial analysis passed, increasing traffic..."
    ./canary/increase_traffic.sh $MODEL_NAME 25
else
    echo "[4/5] Initial analysis failed, rolling back..."
    ./canary/rollback.sh $MODEL_NAME
    exit 1
fi

echo "[5/5] Canary deployment in progress - monitor dashboard"
echo "Dashboard: https://grafana.example.com/d/canary-$MODEL_NAME"
```

### 4.2 Traffic Increase Script

```bash
#!/bin/bash
# canary/increase_traffic.sh

MODEL_NAME=$1
NEW_PERCENTAGE=$2

echo "Increasing canary traffic to $NEW_PERCENTAGE%..."

kubectl patch inferenceservice $MODEL_NAME -n models --type='json' \
  -p="[{\"op\": \"replace\", \"path\": \"/spec/predictor/canaryTrafficPercent\", \"value\": $NEW_PERCENTAGE}]"

echo "Traffic updated. Current split:"
kubectl get inferenceservice $MODEL_NAME -n models -o jsonpath='{.status.components.predictor}'
```

### 4.3 Rollback Script

```bash
#!/bin/bash
# canary/rollback.sh

MODEL_NAME=$1

echo "=== Rolling back canary for $MODEL_NAME ==="

# Remove canary configuration
kubectl patch inferenceservice $MODEL_NAME -n models --type='json' \
  -p="[
    {\"op\": \"remove\", \"path\": \"/spec/predictor/canaryTrafficPercent\"},
    {\"op\": \"remove\", \"path\": \"/spec/predictor/canary\"}
  ]"

echo "Canary rolled back. All traffic now going to stable version."
```

---

## 5. Promotion Process

### 5.1 Promotion Checklist

```markdown
## Canary Promotion Checklist

**Model:** ___________
**Canary Version:** ___________
**Duration at 50%:** ___________

### Metrics Validation
- [ ] Error rate ≤ stable version
- [ ] Latency P99 ≤ stable version
- [ ] No prediction drift detected
- [ ] Business metrics stable

### Approval
- [ ] ML Lead approval
- [ ] On-call engineer notified

### Promotion
- [ ] Promote canary to stable
- [ ] Update model registry
- [ ] Archive old version
```

### 5.2 Promotion Script

```bash
#!/bin/bash
# canary/promote.sh

MODEL_NAME=$1

echo "=== Promoting canary to stable for $MODEL_NAME ==="

# Get canary version
CANARY_URI=$(kubectl get inferenceservice $MODEL_NAME -n models \
  -o jsonpath='{.spec.predictor.canary.model.storageUri}')

echo "Promoting $CANARY_URI to stable..."

# Update stable to canary version and remove canary config
kubectl patch inferenceservice $MODEL_NAME -n models --type='json' \
  -p="[
    {\"op\": \"replace\", \"path\": \"/spec/predictor/model/storageUri\", \"value\": \"$CANARY_URI\"},
    {\"op\": \"remove\", \"path\": \"/spec/predictor/canaryTrafficPercent\"},
    {\"op\": \"remove\", \"path\": \"/spec/predictor/canary\"}
  ]"

echo "Promotion complete. Verifying..."
kubectl get inferenceservice $MODEL_NAME -n models
```

---

## 6. Monitoring Dashboard

### 6.1 Canary Metrics Panels

```promql
# Error rate comparison
sum(rate(inference_requests_total{model="$model",status="error"}[5m])) by (version)
/
sum(rate(inference_requests_total{model="$model"}[5m])) by (version)

# Latency comparison
histogram_quantile(0.99, 
  sum(rate(inference_latency_bucket{model="$model"}[5m])) by (version, le)
)

# Traffic split
sum(rate(inference_requests_total{model="$model"}[5m])) by (version)
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial canary procedures |
