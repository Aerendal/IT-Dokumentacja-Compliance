---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-078: Bias Monitoring Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-078 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Ethics / ML Platform Lead] |

---

## 1. Bias Monitoring Overview

### 1.1 Protected Attributes

| Attribute | Legal Basis | Monitoring Required |
|-----------|-------------|---------------------|
| Race/Ethnicity | Civil Rights Act | Yes (Tier 1-2) |
| Gender | ECOA, Title VII | Yes (Tier 1-2) |
| Age | ADEA | Yes (Tier 1-2) |
| Religion | Civil Rights Act | Yes (Tier 1) |
| National Origin | Civil Rights Act | Yes (Tier 1) |
| Disability | ADA | Yes (Tier 1) |

### 1.2 Fairness Metrics

| Metric | Definition | Threshold |
|--------|------------|-----------|
| Demographic Parity | P(Ŷ=1\|A=0) ≈ P(Ŷ=1\|A=1) | Ratio ≥ 0.8 |
| Equalized Odds | Equal TPR and FPR across groups | Diff ≤ 0.1 |
| Predictive Parity | Equal PPV across groups | Ratio ≥ 0.8 |
| Disparate Impact | 80% rule (4/5ths rule) | Ratio ≥ 0.8 |

---

## 2. Bias Detection

### 2.1 Fairlearn Integration

```python
# bias/fairlearn_monitor.py
from fairlearn.metrics import MetricFrame, demographic_parity_difference, equalized_odds_difference
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pandas as pd

class BiasMonitor:
    """Monitor model predictions for bias."""
    
    def __init__(self, sensitive_features: list):
        self.sensitive_features = sensitive_features
    
    def compute_fairness_metrics(self, y_true, y_pred, sensitive_data: pd.DataFrame) -> dict:
        """Compute fairness metrics across sensitive attributes."""
        
        results = {}
        
        for feature in self.sensitive_features:
            sensitive = sensitive_data[feature]
            
            # Create metric frame
            metric_frame = MetricFrame(
                metrics={
                    'accuracy': accuracy_score,
                    'precision': precision_score,
                    'recall': recall_score,
                    'selection_rate': lambda y_t, y_p: y_p.mean()
                },
                y_true=y_true,
                y_pred=y_pred,
                sensitive_features=sensitive
            )
            
            # Compute fairness metrics
            results[feature] = {
                'demographic_parity_diff': demographic_parity_difference(
                    y_true, y_pred, sensitive_features=sensitive
                ),
                'equalized_odds_diff': equalized_odds_difference(
                    y_true, y_pred, sensitive_features=sensitive
                ),
                'metrics_by_group': metric_frame.by_group.to_dict(),
                'disparate_impact_ratio': self._compute_disparate_impact(
                    y_pred, sensitive
                )
            }
        
        return results
    
    def _compute_disparate_impact(self, y_pred, sensitive) -> float:
        """Compute disparate impact ratio (80% rule)."""
        groups = sensitive.unique()
        
        if len(groups) != 2:
            return None
        
        rates = []
        for group in groups:
            mask = sensitive == group
            rates.append(y_pred[mask].mean())
        
        return min(rates) / max(rates) if max(rates) > 0 else 1.0
    
    def check_fairness_violations(self, metrics: dict, thresholds: dict = None) -> list:
        """Check for fairness threshold violations."""
        
        if thresholds is None:
            thresholds = {
                'demographic_parity_diff': 0.1,
                'equalized_odds_diff': 0.1,
                'disparate_impact_ratio': 0.8
            }
        
        violations = []
        
        for feature, feature_metrics in metrics.items():
            # Demographic parity
            if abs(feature_metrics['demographic_parity_diff']) > thresholds['demographic_parity_diff']:
                violations.append({
                    'feature': feature,
                    'metric': 'demographic_parity',
                    'value': feature_metrics['demographic_parity_diff'],
                    'threshold': thresholds['demographic_parity_diff'],
                    'severity': 'high'
                })
            
            # Disparate impact
            if feature_metrics['disparate_impact_ratio'] and \
               feature_metrics['disparate_impact_ratio'] < thresholds['disparate_impact_ratio']:
                violations.append({
                    'feature': feature,
                    'metric': 'disparate_impact',
                    'value': feature_metrics['disparate_impact_ratio'],
                    'threshold': thresholds['disparate_impact_ratio'],
                    'severity': 'critical'
                })
        
        return violations
```

### 2.2 Continuous Monitoring

```python
# bias/continuous_monitor.py
from prometheus_client import Gauge, Counter

# Metrics
bias_demographic_parity = Gauge(
    'mlops_bias_demographic_parity_diff',
    'Demographic parity difference',
    ['model', 'sensitive_feature']
)

bias_disparate_impact = Gauge(
    'mlops_bias_disparate_impact_ratio',
    'Disparate impact ratio',
    ['model', 'sensitive_feature']
)

bias_violations = Counter(
    'mlops_bias_violations_total',
    'Total bias violations detected',
    ['model', 'sensitive_feature', 'metric']
)

class ContinuousBiasMonitor:
    """Continuous bias monitoring in production."""
    
    def __init__(self, model_name: str, sensitive_features: list,
                 window_size: int = 10000):
        self.model_name = model_name
        self.sensitive_features = sensitive_features
        self.window_size = window_size
        self.buffer = []
    
    def record_prediction(self, prediction: dict, sensitive_data: dict):
        """Record prediction for bias analysis."""
        self.buffer.append({
            'prediction': prediction['prediction'],
            'actual': prediction.get('actual'),
            **sensitive_data
        })
        
        # Analyze when buffer is full
        if len(self.buffer) >= self.window_size:
            self.analyze_and_report()
            self.buffer = []
    
    def analyze_and_report(self):
        """Analyze buffer for bias and report metrics."""
        df = pd.DataFrame(self.buffer)
        
        monitor = BiasMonitor(self.sensitive_features)
        
        for feature in self.sensitive_features:
            if feature not in df.columns:
                continue
            
            metrics = monitor.compute_fairness_metrics(
                df['actual'].values if 'actual' in df else df['prediction'].values,
                df['prediction'].values,
                df[[feature]]
            )
            
            # Update Prometheus metrics
            feature_metrics = metrics[feature]
            
            bias_demographic_parity.labels(
                model=self.model_name,
                sensitive_feature=feature
            ).set(feature_metrics['demographic_parity_diff'])
            
            if feature_metrics['disparate_impact_ratio']:
                bias_disparate_impact.labels(
                    model=self.model_name,
                    sensitive_feature=feature
                ).set(feature_metrics['disparate_impact_ratio'])
            
            # Check violations
            violations = monitor.check_fairness_violations(metrics)
            for v in violations:
                bias_violations.labels(
                    model=self.model_name,
                    sensitive_feature=v['feature'],
                    metric=v['metric']
                ).inc()
```

---

## 3. Alerting Rules

```yaml
# prometheus/bias-alerts.yaml
groups:
  - name: bias-monitoring
    rules:
      - alert: BiasDisparateImpactViolation
        expr: mlops_bias_disparate_impact_ratio < 0.8
        for: 1h
        labels:
          severity: critical
        annotations:
          summary: "Disparate impact violation for {{ $labels.model }}"
          description: "Model {{ $labels.model }} shows disparate impact ratio of {{ $value }} for {{ $labels.sensitive_feature }}"
          
      - alert: BiasDemographicParityDrift
        expr: abs(mlops_bias_demographic_parity_diff) > 0.1
        for: 2h
        labels:
          severity: high
        annotations:
          summary: "Demographic parity drift for {{ $labels.model }}"
          
      - alert: BiasViolationsTrending
        expr: increase(mlops_bias_violations_total[24h]) > 5
        labels:
          severity: warning
        annotations:
          summary: "Multiple bias violations detected for {{ $labels.model }}"
```

---

## 4. Bias Mitigation

### 4.1 Pre-processing Techniques

```python
# bias/mitigation.py
from fairlearn.preprocessing import CorrelationRemover
from fairlearn.reductions import ExponentiatedGradient, DemographicParity

def remove_correlation(X: pd.DataFrame, sensitive_feature: str) -> pd.DataFrame:
    """Remove correlation with sensitive attribute."""
    cr = CorrelationRemover(sensitive_feature_ids=[sensitive_feature])
    return pd.DataFrame(cr.fit_transform(X), columns=X.columns)
```

### 4.2 In-processing Techniques

```python
def train_fair_model(model, X, y, sensitive_features):
    """Train model with fairness constraints."""
    mitigator = ExponentiatedGradient(
        model,
        constraints=DemographicParity()
    )
    mitigator.fit(X, y, sensitive_features=sensitive_features)
    return mitigator
```

---

## 5. Reporting

### 5.1 Bias Report Template

```markdown
# Bias Monitoring Report

**Model:** [Model Name]
**Period:** [Date Range]
**Generated:** [Timestamp]

## Summary
| Metric | Status |
|--------|--------|
| Disparate Impact |  Pass /  Fail |
| Demographic Parity |  Pass /  Fail |
| Equalized Odds |  Pass /  Fail |

## Metrics by Sensitive Attribute

### Gender
| Group | Selection Rate | Accuracy | Precision |
|-------|----------------|----------|-----------|
| Male | X% | X% | X% |
| Female | X% | X% | X% |
| **Disparity** | X | X | X |

### Age Group
[Similar table]

## Violations
| Date | Attribute | Metric | Value | Threshold |
|------|-----------|--------|-------|-----------|
| | | | | |

## Recommendations
1. [Recommendation]
2. [Recommendation]

## Sign-off
- [ ] Ethics Review
- [ ] Model Owner
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial bias monitoring guide |
