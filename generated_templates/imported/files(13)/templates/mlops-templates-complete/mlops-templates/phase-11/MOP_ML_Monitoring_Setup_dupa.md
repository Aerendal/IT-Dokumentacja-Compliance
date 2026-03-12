---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-038: ML Monitoring Setup

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-038 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [MLOps Engineer / SRE] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-012: Model Serving Design | Metrics requirements |
| MOP-007: Architecture | Infrastructure |
| MOP-004: Requirements | SLA requirements |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-034: Incident Response | Alert procedures |
| MOP-031: Runbooks | Operations |

---

## Template Content

---

# ML Monitoring Setup Guide

## 1. Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ML Monitoring Stack                               │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Data Sources                                │ │
│  │  Model Serving │ Feature Store │ Pipelines │ Infrastructure   │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                              │                                      │
│                    ┌─────────┴─────────┐                           │
│                    ▼                   ▼                           │
│  ┌─────────────────────────┐ ┌─────────────────────────┐          │
│  │      Prometheus         │ │      Evidently          │          │
│  │   (Infrastructure +     │ │   (ML-Specific:         │          │
│  │    Request Metrics)     │ │    Drift, Data Quality) │          │
│  └───────────┬─────────────┘ └───────────┬─────────────┘          │
│              │                           │                         │
│              └─────────────┬─────────────┘                         │
│                            ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                       Grafana                                │   │
│  │  (Dashboards, Visualization, Unified View)                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                            │                                        │
│                            ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    Alertmanager                              │   │
│  │  (Alerting, Routing, PagerDuty/Slack Integration)           │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Metrics Categories

### 2.1 Infrastructure Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| `cpu_usage_percent` | CPU utilization | >80% for 5m |
| `memory_usage_percent` | Memory utilization | >85% for 5m |
| `gpu_utilization` | GPU compute usage | >90% for 10m |
| `gpu_memory_used` | GPU memory usage | >90% |
| `pod_restarts_total` | Pod restart count | >3 in 1h |

### 2.2 Model Serving Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| `inference_requests_total` | Total requests | - |
| `inference_latency_seconds` | Inference latency | P99 >100ms |
| `inference_errors_total` | Error count | Rate >1% |
| `model_load_time_seconds` | Model load time | >30s |
| `batch_size_histogram` | Batch sizes | - |

### 2.3 ML-Specific Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| `data_drift_score` | Input distribution drift | >0.1 |
| `prediction_drift_score` | Output distribution drift | >0.1 |
| `feature_null_rate` | Missing feature rate | >5% |
| `feature_freshness_seconds` | Feature age | >3600s |
| `model_accuracy` | Accuracy (with labels) | <baseline -5% |

---

## 3. Prometheus Configuration

### 3.1 ServiceMonitor for Model Serving

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: model-serving-metrics
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: triton-inference
  namespaceSelector:
    matchNames:
      - models
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
```

### 3.2 Custom Metrics Recording Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ml-recording-rules
  namespace: monitoring
spec:
  groups:
  - name: ml-metrics
    interval: 30s
    rules:
    - record: model:inference_latency_p50:rate5m
      expr: histogram_quantile(0.50, sum(rate(inference_latency_seconds_bucket[5m])) by (model, le))
    
    - record: model:inference_latency_p99:rate5m
      expr: histogram_quantile(0.99, sum(rate(inference_latency_seconds_bucket[5m])) by (model, le))
    
    - record: model:error_rate:rate5m
      expr: sum(rate(inference_errors_total[5m])) by (model) / sum(rate(inference_requests_total[5m])) by (model)
    
    - record: model:requests_per_second:rate5m
      expr: sum(rate(inference_requests_total[5m])) by (model)
```

---

## 4. Alerting Configuration

### 4.1 Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ml-alerts
  namespace: monitoring
spec:
  groups:
  - name: model-serving-alerts
    rules:
    - alert: ModelHighLatency
      expr: model:inference_latency_p99:rate5m > 0.1
      for: 5m
      labels:
        severity: warning
        team: mlops
      annotations:
        summary: "High latency on model {{ $labels.model }}"
        description: "P99 latency is {{ $value | humanizeDuration }}"
    
    - alert: ModelHighErrorRate
      expr: model:error_rate:rate5m > 0.01
      for: 5m
      labels:
        severity: critical
        team: mlops
      annotations:
        summary: "High error rate on model {{ $labels.model }}"
        description: "Error rate is {{ $value | humanizePercentage }}"
    
    - alert: ModelDown
      expr: up{job="model-serving"} == 0
      for: 1m
      labels:
        severity: critical
        team: mlops
      annotations:
        summary: "Model {{ $labels.model }} is down"

  - name: ml-quality-alerts
    rules:
    - alert: DataDriftDetected
      expr: data_drift_score > 0.1
      for: 15m
      labels:
        severity: warning
        team: ml-platform
      annotations:
        summary: "Data drift detected for {{ $labels.model }}"
        description: "Drift score: {{ $value }}"
    
    - alert: PredictionDriftDetected
      expr: prediction_drift_score > 0.1
      for: 15m
      labels:
        severity: warning
        team: ml-platform
      annotations:
        summary: "Prediction drift detected for {{ $labels.model }}"
    
    - alert: FeatureStaleData
      expr: time() - feature_last_update_timestamp > 3600
      for: 5m
      labels:
        severity: warning
        team: data-platform
      annotations:
        summary: "Feature {{ $labels.feature }} is stale"
```

### 4.2 Alertmanager Configuration

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  receiver: 'default'
  group_by: ['alertname', 'model']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
  - match:
      severity: critical
    receiver: 'pagerduty-critical'
  - match:
      severity: warning
      team: mlops
    receiver: 'slack-mlops'

receivers:
- name: 'default'
  slack_configs:
  - api_url: '${SLACK_WEBHOOK_URL}'
    channel: '#mlops-alerts'

- name: 'pagerduty-critical'
  pagerduty_configs:
  - service_key: '${PAGERDUTY_SERVICE_KEY}'
    severity: critical

- name: 'slack-mlops'
  slack_configs:
  - api_url: '${SLACK_WEBHOOK_URL}'
    channel: '#mlops-alerts'
    title: '{{ .GroupLabels.alertname }}'
    text: '{{ .CommonAnnotations.description }}'
```

---

## 5. Evidently ML Monitoring

### 5.1 Drift Detection Setup

```python
# drift_monitoring.py
from evidently.metrics import DataDriftMetric, DatasetDriftMetric
from evidently.report import Report
from evidently.test_suite import TestSuite
from evidently.tests import TestColumnDrift
import pandas as pd

def run_drift_analysis(reference_data: pd.DataFrame, current_data: pd.DataFrame, model_name: str):
    """Run drift analysis and export metrics."""
    
    # Create drift report
    report = Report(metrics=[
        DataDriftMetric(),
        DatasetDriftMetric(),
    ])
    
    report.run(reference_data=reference_data, current_data=current_data)
    
    # Extract metrics
    result = report.as_dict()
    drift_share = result["metrics"][0]["result"]["drift_share"]
    dataset_drift = result["metrics"][1]["result"]["dataset_drift"]
    
    # Export to Prometheus
    from prometheus_client import Gauge
    
    data_drift_gauge = Gauge('data_drift_score', 'Data drift score', ['model'])
    data_drift_gauge.labels(model=model_name).set(drift_share)
    
    return {
        "drift_share": drift_share,
        "dataset_drift": dataset_drift,
        "drifted_features": [
            col for col, info in result["metrics"][0]["result"]["drift_by_columns"].items()
            if info["drift_detected"]
        ]
    }
```

### 5.2 Scheduled Drift Monitoring

```yaml
# drift-monitoring-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: drift-monitoring
  namespace: mlops
spec:
  schedule: "0 * * * *"  # Every hour
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: drift-monitor
            image: mlops/drift-monitor:latest
            env:
            - name: MODEL_NAME
              value: "fraud-model"
            - name: REFERENCE_DATA_PATH
              value: "s3://mlops/reference-data/fraud-model.parquet"
            - name: PROMETHEUS_PUSHGATEWAY
              value: "prometheus-pushgateway:9091"
          restartPolicy: OnFailure
```

---

## 6. Grafana Dashboards

### 6.1 Model Performance Dashboard

```json
{
  "dashboard": {
    "title": "ML Model Performance",
    "panels": [
      {
        "title": "Request Rate",
        "type": "stat",
        "targets": [{
          "expr": "sum(rate(inference_requests_total[5m])) by (model)"
        }]
      },
      {
        "title": "Latency P50/P95/P99",
        "type": "timeseries",
        "targets": [
          {"expr": "model:inference_latency_p50:rate5m", "legendFormat": "P50"},
          {"expr": "histogram_quantile(0.95, sum(rate(inference_latency_seconds_bucket[5m])) by (le))", "legendFormat": "P95"},
          {"expr": "model:inference_latency_p99:rate5m", "legendFormat": "P99"}
        ]
      },
      {
        "title": "Error Rate",
        "type": "timeseries",
        "targets": [{
          "expr": "model:error_rate:rate5m * 100",
          "legendFormat": "Error %"
        }],
        "thresholds": [{"value": 1, "color": "red"}]
      },
      {
        "title": "Data Drift Score",
        "type": "gauge",
        "targets": [{
          "expr": "data_drift_score"
        }],
        "thresholds": [
          {"value": 0.05, "color": "green"},
          {"value": 0.1, "color": "yellow"},
          {"value": 0.2, "color": "red"}
        ]
      }
    ]
  }
}
```

### 6.2 Import Dashboard

```bash
# Import via API
curl -X POST http://grafana:3000/api/dashboards/db \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GRAFANA_API_KEY" \
  -d @dashboard.json
```

---

## 7. Log Aggregation

### 7.1 Structured Logging

```python
# structured_logging.py
import structlog
import json

logger = structlog.get_logger()

def log_prediction(model_name: str, request_id: str, features: dict, prediction: float, latency_ms: float):
    """Log prediction with structured format."""
    logger.info(
        "prediction_completed",
        model=model_name,
        request_id=request_id,
        feature_count=len(features),
        prediction=prediction,
        latency_ms=latency_ms,
        event_type="inference"
    )
```

### 7.2 Log Queries (Loki/Elasticsearch)

```promql
# Find slow predictions
{namespace="models"} |= "prediction_completed" | json | latency_ms > 100

# Find errors by model
{namespace="models", model="fraud-model"} |= "error"

# Prediction distribution
sum by (prediction_bucket) (
  count_over_time({namespace="models"} |= "prediction_completed" | json [1h])
)
```

---

## 8. Verification

### 8.1 Monitoring Checklist

| Component | Check | Status |
|-----------|-------|--------|
| Prometheus | Targets healthy |  |
| Alertmanager | Alerts routing |  |
| Grafana | Dashboards loading |  |
| Evidently | Drift reports generating |  |
| Alerts | Test alert received |  |

### 8.2 Test Alerts

```bash
# Send test alert
curl -X POST http://alertmanager:9093/api/v2/alerts \
  -H "Content-Type: application/json" \
  -d '[{
    "labels": {"alertname": "TestAlert", "severity": "warning"},
    "annotations": {"summary": "Test alert from setup verification"}
  }]'
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial setup guide |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| MLOps Engineer | | | |
| SRE Lead | | | |
