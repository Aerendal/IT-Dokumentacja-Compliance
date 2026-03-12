---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-041: Model Tracking Metrics

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-041 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Model Lifecycle Metrics

### 1.1 Registry Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `models_registered_total` | Counter | team | Total models registered |
| `model_versions_total` | Gauge | model | Versions per model |
| `models_in_production` | Gauge | tier | Production models count |
| `model_stage_transitions` | Counter | model, from, to | Stage changes |
| `model_deployment_duration` | Histogram | model | Time to deploy |

### 1.2 Implementation

```python
# metrics/model_tracking.py
from prometheus_client import Counter, Gauge, Histogram

# Registry metrics
models_registered = Counter(
    'mlops_models_registered_total',
    'Total models registered in registry',
    ['team', 'model_type']
)

model_versions = Gauge(
    'mlops_model_versions_total',
    'Number of versions per model',
    ['model_name']
)

models_by_stage = Gauge(
    'mlops_models_by_stage',
    'Number of models in each stage',
    ['stage', 'tier']
)

model_stage_transitions = Counter(
    'mlops_model_stage_transitions_total',
    'Model stage transitions',
    ['model_name', 'from_stage', 'to_stage']
)

# Deployment metrics
model_deployments = Counter(
    'mlops_model_deployments_total',
    'Total model deployments',
    ['model_name', 'environment', 'status']
)

deployment_duration = Histogram(
    'mlops_model_deployment_duration_seconds',
    'Time to deploy model',
    ['model_name', 'environment'],
    buckets=[60, 120, 300, 600, 1200, 1800, 3600]
)

# Model age in production
model_production_age = Gauge(
    'mlops_model_production_age_days',
    'Days since model deployed to production',
    ['model_name']
)
```

---

## 2. Model Performance Metrics

### 2.1 Inference Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `inference_requests_total` | Counter | model, status | Total requests |
| `inference_latency_seconds` | Histogram | model | Request latency |
| `inference_batch_size` | Histogram | model | Batch sizes |
| `model_prediction_value` | Histogram | model | Prediction distribution |

### 2.2 Implementation

```python
# metrics/inference_metrics.py
inference_requests = Counter(
    'mlops_inference_requests_total',
    'Total inference requests',
    ['model_name', 'model_version', 'status']
)

inference_latency = Histogram(
    'mlops_inference_latency_seconds',
    'Inference latency in seconds',
    ['model_name'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

inference_batch_size = Histogram(
    'mlops_inference_batch_size',
    'Number of samples per inference request',
    ['model_name'],
    buckets=[1, 5, 10, 25, 50, 100, 250, 500, 1000]
)

prediction_confidence = Histogram(
    'mlops_prediction_confidence',
    'Model prediction confidence scores',
    ['model_name', 'predicted_class'],
    buckets=[0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
)

# Track prediction distribution
prediction_distribution = Counter(
    'mlops_predictions_total',
    'Prediction class distribution',
    ['model_name', 'predicted_class']
)
```

---

## 3. Model Drift Metrics

### 3.1 Drift Detection Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `feature_drift_score` | Gauge | model, feature | Feature drift score |
| `prediction_drift_score` | Gauge | model | Output drift score |
| `data_quality_score` | Gauge | model | Input data quality |
| `drift_alerts_total` | Counter | model, type | Drift alerts fired |

### 3.2 Implementation

```python
# metrics/drift_metrics.py
from prometheus_client import Gauge, Counter

# Drift scores
feature_drift = Gauge(
    'mlops_feature_drift_score',
    'Feature drift score (0-1, higher = more drift)',
    ['model_name', 'feature_name']
)

prediction_drift = Gauge(
    'mlops_prediction_drift_score',
    'Prediction distribution drift score',
    ['model_name']
)

data_quality = Gauge(
    'mlops_input_data_quality_score',
    'Input data quality score (0-1)',
    ['model_name']
)

# Drift events
drift_detected = Counter(
    'mlops_drift_detected_total',
    'Number of drift detection events',
    ['model_name', 'drift_type', 'severity']
)

# Feature statistics
feature_null_rate = Gauge(
    'mlops_feature_null_rate',
    'Null value rate per feature',
    ['model_name', 'feature_name']
)

feature_mean = Gauge(
    'mlops_feature_mean',
    'Feature mean value',
    ['model_name', 'feature_name']
)

feature_stddev = Gauge(
    'mlops_feature_stddev',
    'Feature standard deviation',
    ['model_name', 'feature_name']
)
```

### 3.3 Evidently Integration

```python
# metrics/evidently_exporter.py
from evidently.metrics import DataDriftMetric
from evidently.report import Report

def export_drift_metrics(model_name: str, reference_data, current_data):
    """Calculate and export drift metrics to Prometheus."""
    
    report = Report(metrics=[DataDriftMetric()])
    report.run(reference_data=reference_data, current_data=current_data)
    
    results = report.as_dict()
    
    # Export overall drift
    dataset_drift = results['metrics'][0]['result']['dataset_drift']
    prediction_drift.labels(model_name=model_name).set(
        1.0 if dataset_drift else 0.0
    )
    
    # Export per-feature drift
    for feature, drift_info in results['metrics'][0]['result']['drift_by_columns'].items():
        score = drift_info['drift_score']
        feature_drift.labels(
            model_name=model_name,
            feature_name=feature
        ).set(score)
        
        if drift_info['drift_detected']:
            drift_detected.labels(
                model_name=model_name,
                drift_type='feature',
                severity='warning'
            ).inc()
```

---

## 4. Business Impact Metrics

### 4.1 Business Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `model_business_value` | Gauge | model | Estimated business value |
| `model_decisions_total` | Counter | model, decision | Automated decisions |
| `model_overrides_total` | Counter | model | Human overrides |
| `model_accuracy_production` | Gauge | model | Prod accuracy (labeled) |

### 4.2 Implementation

```python
# metrics/business_metrics.py
model_decisions = Counter(
    'mlops_model_decisions_total',
    'Automated decisions made by model',
    ['model_name', 'decision_type']
)

model_overrides = Counter(
    'mlops_model_overrides_total',
    'Human overrides of model decisions',
    ['model_name', 'override_reason']
)

model_accuracy_live = Gauge(
    'mlops_model_accuracy_live',
    'Model accuracy on production labeled data',
    ['model_name']
)

model_precision_live = Gauge(
    'mlops_model_precision_live',
    'Model precision on production labeled data',
    ['model_name']
)

model_recall_live = Gauge(
    'mlops_model_recall_live',
    'Model recall on production labeled data',
    ['model_name']
)
```

---

## 5. Alerting Rules

```yaml
# prometheus/model-alerts.yaml
groups:
  - name: model-tracking-alerts
    rules:
      - alert: ModelDriftDetected
        expr: mlops_prediction_drift_score > 0.1
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "Drift detected for model {{ $labels.model_name }}"
          
      - alert: ModelAccuracyDegraded
        expr: |
          mlops_model_accuracy_live < 
          mlops_model_accuracy_baseline * 0.95
        for: 2h
        labels:
          severity: high
        annotations:
          summary: "Model {{ $labels.model_name }} accuracy degraded >5%"
          
      - alert: HighOverrideRate
        expr: |
          rate(mlops_model_overrides_total[1h]) /
          rate(mlops_model_decisions_total[1h]) > 0.1
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "High override rate (>10%) for {{ $labels.model_name }}"
          
      - alert: ModelStaleInProduction
        expr: mlops_model_production_age_days > 90
        labels:
          severity: info
        annotations:
          summary: "Model {{ $labels.model_name }} in production for >90 days"
```

---

## 6. Dashboard Panels

```promql
# Models in production by tier
mlops_models_by_stage{stage="Production"}

# Model deployment frequency
rate(mlops_model_deployments_total{status="success"}[7d])

# Average model age in production
avg(mlops_model_production_age_days)

# Drift score heatmap
mlops_feature_drift_score

# Production accuracy trend
mlops_model_accuracy_live
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial model tracking metrics |
