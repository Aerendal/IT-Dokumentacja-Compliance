---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-068: A/B Testing Framework for Models

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-068 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead / Data Science] |

---

## 1. A/B Testing Overview

### 1.1 When to Use A/B Testing

| Scenario | Use A/B Test | Use Canary |
|----------|--------------|------------|
| Compare model algorithms |  |  |
| Measure business impact |  |  |
| Validate new features |  |  |
| Safety validation only |  |  |
| Quick rollout needed |  |  |

### 1.2 A/B Test vs Canary

| Aspect | A/B Test | Canary |
|--------|----------|--------|
| Purpose | Measure effectiveness | Validate safety |
| Duration | Days to weeks | Hours to days |
| Traffic split | Fixed 50/50 | Gradual increase |
| Success metric | Business KPIs | Error rate, latency |
| Statistical rigor | Required | Not required |

---

## 2. A/B Test Design

### 2.1 Test Configuration

```yaml
# ab-test-config.yaml
apiVersion: mlops.company.com/v1
kind: ABTest
metadata:
  name: fraud-model-v2-test
  namespace: models
spec:
  # Test identification
  testId: "AB-2024-001"
  description: "Test new fraud detection algorithm"
  
  # Variants
  variants:
    - name: control
      model: fraud-model
      version: v1.2.0
      trafficPercentage: 50
    - name: treatment
      model: fraud-model
      version: v2.0.0
      trafficPercentage: 50
  
  # Targeting
  targeting:
    type: random  # random, user_id_hash, segment
    seed: 42
  
  # Duration
  duration:
    minDays: 7
    maxDays: 30
  
  # Success metrics
  primaryMetric:
    name: fraud_detection_rate
    direction: maximize
    minimumDetectableEffect: 0.05  # 5% improvement
  
  secondaryMetrics:
    - name: false_positive_rate
      direction: minimize
    - name: processing_latency_p99
      direction: minimize
  
  # Guardrail metrics
  guardrails:
    - name: error_rate
      threshold: 0.01
      action: pause
    - name: latency_p99
      threshold: 100
      action: alert
  
  # Sample size
  statistics:
    confidenceLevel: 0.95
    power: 0.8
    requiredSampleSize: 10000
```

### 2.2 Traffic Routing

```yaml
# istio-ab-test-routing.yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fraud-model-ab-test
spec:
  hosts:
    - fraud-model.models.svc.cluster.local
  http:
    - match:
        - headers:
            x-ab-test:
              exact: "treatment"
      route:
        - destination:
            host: fraud-model-v2
    - match:
        - headers:
            x-ab-test:
              exact: "control"
      route:
        - destination:
            host: fraud-model-v1
    - route:  # Default: random assignment
        - destination:
            host: fraud-model-v1
          weight: 50
        - destination:
            host: fraud-model-v2
          weight: 50
```

---

## 3. Assignment Logic

### 3.1 User Assignment

```python
# ab_testing/assignment.py
import hashlib
from typing import Optional

class ABTestAssigner:
    """Assign users to A/B test variants."""
    
    def __init__(self, test_id: str, variants: list, seed: int = 42):
        self.test_id = test_id
        self.variants = variants
        self.seed = seed
    
    def assign(self, user_id: str) -> str:
        """Deterministically assign user to variant."""
        # Create hash of user_id + test_id for consistent assignment
        hash_input = f"{self.test_id}:{user_id}:{self.seed}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
        
        # Map to variant based on traffic percentages
        bucket = hash_value % 100
        cumulative = 0
        
        for variant in self.variants:
            cumulative += variant['trafficPercentage']
            if bucket < cumulative:
                return variant['name']
        
        return self.variants[-1]['name']  # Fallback
    
    def get_model_endpoint(self, user_id: str) -> str:
        """Get model endpoint for user."""
        variant = self.assign(user_id)
        variant_config = next(v for v in self.variants if v['name'] == variant)
        return f"{variant_config['model']}-{variant_config['version']}"

# Usage in inference service
assigner = ABTestAssigner(
    test_id="AB-2024-001",
    variants=[
        {"name": "control", "model": "fraud-model", "version": "v1.2.0", "trafficPercentage": 50},
        {"name": "treatment", "model": "fraud-model", "version": "v2.0.0", "trafficPercentage": 50}
    ]
)

def predict(request):
    user_id = request.user_id
    variant = assigner.assign(user_id)
    endpoint = assigner.get_model_endpoint(user_id)
    
    # Log assignment for analysis
    log_ab_assignment(user_id, variant, request.request_id)
    
    # Route to appropriate model
    return call_model(endpoint, request.features)
```

---

## 4. Metrics Collection

### 4.1 Event Logging

```python
# ab_testing/logging.py
from datetime import datetime
import json

class ABTestLogger:
    """Log A/B test events for analysis."""
    
    def __init__(self, test_id: str):
        self.test_id = test_id
    
    def log_assignment(self, user_id: str, variant: str, request_id: str):
        """Log user assignment."""
        event = {
            "event_type": "ab_assignment",
            "test_id": self.test_id,
            "user_id": user_id,
            "variant": variant,
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        self._send_to_kafka("ab-test-events", event)
    
    def log_outcome(self, user_id: str, variant: str, 
                    metric_name: str, metric_value: float):
        """Log outcome metric."""
        event = {
            "event_type": "ab_outcome",
            "test_id": self.test_id,
            "user_id": user_id,
            "variant": variant,
            "metric_name": metric_name,
            "metric_value": metric_value,
            "timestamp": datetime.utcnow().isoformat()
        }
        self._send_to_kafka("ab-test-events", event)
```

### 4.2 Metrics Aggregation

```sql
-- Daily metrics aggregation query
SELECT 
    test_id,
    variant,
    DATE(timestamp) as date,
    COUNT(DISTINCT user_id) as users,
    COUNT(*) as predictions,
    AVG(CASE WHEN metric_name = 'fraud_detected' THEN metric_value END) as detection_rate,
    AVG(CASE WHEN metric_name = 'false_positive' THEN metric_value END) as false_positive_rate,
    AVG(CASE WHEN metric_name = 'latency_ms' THEN metric_value END) as avg_latency
FROM ab_test_events
WHERE test_id = 'AB-2024-001'
GROUP BY test_id, variant, DATE(timestamp)
ORDER BY date, variant;
```

---

## 5. Statistical Analysis

### 5.1 Analysis Script

```python
# ab_testing/analysis.py
import scipy.stats as stats
import numpy as np
from dataclasses import dataclass

@dataclass
class ABTestResult:
    test_id: str
    metric_name: str
    control_mean: float
    treatment_mean: float
    relative_lift: float
    p_value: float
    confidence_interval: tuple
    is_significant: bool
    recommendation: str

class ABTestAnalyzer:
    """Statistical analysis for A/B tests."""
    
    def __init__(self, confidence_level: float = 0.95):
        self.confidence_level = confidence_level
        self.alpha = 1 - confidence_level
    
    def analyze(self, control_data: np.array, treatment_data: np.array,
                metric_name: str, test_id: str) -> ABTestResult:
        """Perform statistical analysis."""
        
        # Calculate means
        control_mean = np.mean(control_data)
        treatment_mean = np.mean(treatment_data)
        
        # Relative lift
        if control_mean != 0:
            relative_lift = (treatment_mean - control_mean) / control_mean
        else:
            relative_lift = float('inf') if treatment_mean > 0 else 0
        
        # T-test
        t_stat, p_value = stats.ttest_ind(control_data, treatment_data)
        
        # Confidence interval for difference
        diff = treatment_mean - control_mean
        se = np.sqrt(np.var(control_data)/len(control_data) + 
                     np.var(treatment_data)/len(treatment_data))
        ci_margin = stats.t.ppf(1 - self.alpha/2, 
                                len(control_data) + len(treatment_data) - 2) * se
        confidence_interval = (diff - ci_margin, diff + ci_margin)
        
        # Significance
        is_significant = p_value < self.alpha
        
        # Recommendation
        if not is_significant:
            recommendation = "CONTINUE - No significant difference detected"
        elif relative_lift > 0:
            recommendation = "PROMOTE TREATMENT - Significant improvement"
        else:
            recommendation = "KEEP CONTROL - Treatment performed worse"
        
        return ABTestResult(
            test_id=test_id,
            metric_name=metric_name,
            control_mean=control_mean,
            treatment_mean=treatment_mean,
            relative_lift=relative_lift,
            p_value=p_value,
            confidence_interval=confidence_interval,
            is_significant=is_significant,
            recommendation=recommendation
        )
    
    def required_sample_size(self, baseline_rate: float, 
                             minimum_detectable_effect: float,
                             power: float = 0.8) -> int:
        """Calculate required sample size per variant."""
        effect_size = minimum_detectable_effect * baseline_rate
        
        # Using formula for two-proportion z-test
        z_alpha = stats.norm.ppf(1 - self.alpha/2)
        z_beta = stats.norm.ppf(power)
        
        p1 = baseline_rate
        p2 = baseline_rate * (1 + minimum_detectable_effect)
        p_pooled = (p1 + p2) / 2
        
        n = (2 * p_pooled * (1 - p_pooled) * (z_alpha + z_beta)**2) / effect_size**2
        
        return int(np.ceil(n))
```

---

## 6. A/B Test Dashboard

### 6.1 Grafana Queries

```promql
# Sample size by variant
sum(increase(ab_test_assignments_total{test_id="$test_id"}[24h])) by (variant)

# Primary metric by variant
sum(rate(ab_test_outcomes_total{test_id="$test_id", metric="fraud_detected"}[1h])) by (variant)
/
sum(rate(ab_test_assignments_total{test_id="$test_id"}[1h])) by (variant)

# Cumulative lift over time
# (Requires custom recording rule)
```

---

## 7. Test Lifecycle

### 7.1 Checklist

```markdown
## A/B Test Lifecycle Checklist

### Planning
- [ ] Define hypothesis
- [ ] Select primary metric
- [ ] Calculate sample size
- [ ] Set test duration
- [ ] Get stakeholder approval

### Setup
- [ ] Deploy treatment model
- [ ] Configure traffic routing
- [ ] Set up logging
- [ ] Configure dashboard
- [ ] Set up guardrail alerts

### Running
- [ ] Monitor guardrails daily
- [ ] Check sample size progress
- [ ] Document any issues

### Analysis
- [ ] Wait for required sample size
- [ ] Run statistical analysis
- [ ] Review secondary metrics
- [ ] Document findings

### Decision
- [ ] Present results to stakeholders
- [ ] Make promotion decision
- [ ] Clean up test infrastructure
- [ ] Archive test data
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial A/B testing framework |
