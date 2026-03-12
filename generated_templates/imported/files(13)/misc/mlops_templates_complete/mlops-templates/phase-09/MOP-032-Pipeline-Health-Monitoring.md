---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-032: Pipeline Health Monitoring

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-032 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Pipeline Health Overview

### 1.1 Monitored Pipelines

| Pipeline | Type | SLA | Owner |
|----------|------|-----|-------|
| Training pipelines | ML | 99% success | ML Eng |
| Feature pipelines | Data | 99.5% success | Data Eng |
| CI/CD pipelines | DevOps | 99% success | Platform |
| Monitoring pipelines | Ops | 99.9% uptime | SRE |

---

## 2. Health Metrics

### 2.1 Key Metrics

| Metric | Description | Target | Alert |
|--------|-------------|--------|-------|
| `pipeline_success_rate` | % successful runs | >95% | <90% |
| `pipeline_duration_seconds` | Run duration | <baseline×1.5 | >baseline×2 |
| `pipeline_queue_time` | Wait before start | <5 min | >15 min |
| `pipeline_failure_count` | Failures per hour | <2 | >5 |
| `task_retry_rate` | Retried tasks | <5% | >10% |

### 2.2 Prometheus Metrics

```python
# monitoring/pipeline_metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Pipeline execution metrics
pipeline_runs_total = Counter(
    'mlops_pipeline_runs_total',
    'Total pipeline runs',
    ['pipeline', 'status']  # status: success, failed, cancelled
)

pipeline_duration_seconds = Histogram(
    'mlops_pipeline_duration_seconds',
    'Pipeline execution duration',
    ['pipeline'],
    buckets=[60, 300, 600, 1800, 3600, 7200, 14400]
)

pipeline_queue_seconds = Histogram(
    'mlops_pipeline_queue_seconds',
    'Time spent in queue',
    ['pipeline'],
    buckets=[10, 30, 60, 300, 600, 1800]
)

# Current state
pipelines_running = Gauge(
    'mlops_pipelines_running',
    'Currently running pipelines',
    ['pipeline']
)

pipelines_queued = Gauge(
    'mlops_pipelines_queued',
    'Pipelines waiting in queue',
    ['pipeline']
)
```

---

## 3. Alerting Rules

### 3.1 Prometheus Alerts

```yaml
# prometheus/pipeline-alerts.yaml
groups:
  - name: pipeline-health
    rules:
      - alert: PipelineHighFailureRate
        expr: |
          sum(rate(mlops_pipeline_runs_total{status="failed"}[1h])) /
          sum(rate(mlops_pipeline_runs_total[1h])) > 0.1
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline failure rate above 10%"
          
      - alert: PipelineStuck
        expr: |
          mlops_pipeline_duration_seconds > 
          mlops_pipeline_duration_baseline_seconds * 3
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline running 3x longer than baseline"
          
      - alert: PipelineQueueBacklog
        expr: mlops_pipelines_queued > 10
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline queue backlog building"
          
      - alert: TrainingPipelineFailed
        expr: |
          increase(mlops_pipeline_runs_total{pipeline=~".*training.*",status="failed"}[1h]) > 0
        labels:
          severity: high
        annotations:
          summary: "Training pipeline failed"
```

---

## 4. Health Check Implementation

### 4.1 Airflow DAG Health

```python
# monitoring/airflow_health.py
from airflow.models import DagRun, TaskInstance
from datetime import datetime, timedelta

def check_dag_health(dag_id: str) -> dict:
    """Check health of Airflow DAG."""
    now = datetime.utcnow()
    lookback = now - timedelta(hours=24)
    
    # Get recent runs
    runs = DagRun.find(dag_id=dag_id, execution_date=lookback)
    
    total = len(runs)
    successful = len([r for r in runs if r.state == 'success'])
    failed = len([r for r in runs if r.state == 'failed'])
    running = len([r for r in runs if r.state == 'running'])
    
    # Calculate metrics
    success_rate = successful / total if total > 0 else 0
    avg_duration = sum(
        (r.end_date - r.start_date).total_seconds() 
        for r in runs if r.end_date
    ) / total if total > 0 else 0
    
    return {
        'dag_id': dag_id,
        'total_runs_24h': total,
        'success_rate': success_rate,
        'failed_count': failed,
        'running_count': running,
        'avg_duration_seconds': avg_duration,
        'healthy': success_rate >= 0.95 and failed < 3
    }
```

### 4.2 Kubeflow Pipeline Health

```python
# monitoring/kubeflow_health.py
from kfp import Client

def check_kubeflow_pipeline_health(pipeline_name: str) -> dict:
    """Check Kubeflow pipeline health."""
    client = Client()
    
    # Get recent runs
    runs = client.list_runs(
        filter=f'pipeline_name="{pipeline_name}"',
        sort_by='created_at desc',
        page_size=50
    ).runs
    
    # Analyze runs
    total = len(runs)
    succeeded = len([r for r in runs if r.status == 'Succeeded'])
    failed = len([r for r in runs if r.status == 'Failed'])
    
    return {
        'pipeline': pipeline_name,
        'success_rate': succeeded / total if total > 0 else 0,
        'failed_count': failed,
        'healthy': (succeeded / total if total > 0 else 0) >= 0.95
    }
```

---

## 5. Dashboard

### 5.1 Grafana Dashboard Panels

```json
{
  "title": "Pipeline Health Dashboard",
  "panels": [
    {
      "title": "Pipeline Success Rate (24h)",
      "type": "gauge",
      "targets": [{
        "expr": "sum(rate(mlops_pipeline_runs_total{status='success'}[24h])) / sum(rate(mlops_pipeline_runs_total[24h]))"
      }],
      "fieldConfig": {
        "defaults": {
          "thresholds": {
            "steps": [
              {"value": 0, "color": "red"},
              {"value": 0.9, "color": "yellow"},
              {"value": 0.95, "color": "green"}
            ]
          }
        }
      }
    },
    {
      "title": "Pipeline Duration Trend",
      "type": "timeseries",
      "targets": [{
        "expr": "histogram_quantile(0.95, rate(mlops_pipeline_duration_seconds_bucket[1h]))",
        "legendFormat": "P95 Duration"
      }]
    },
    {
      "title": "Failed Pipelines",
      "type": "table",
      "targets": [{
        "expr": "increase(mlops_pipeline_runs_total{status='failed'}[24h]) > 0"
      }]
    }
  ]
}
```

---

## 6. Health Check Schedule

| Check | Frequency | Action on Failure |
|-------|-----------|-------------------|
| Pipeline status | 1 min | Alert if stuck |
| Success rate | 5 min | Alert if <90% |
| Queue depth | 1 min | Scale workers |
| Resource usage | 1 min | Alert if >80% |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial monitoring |
