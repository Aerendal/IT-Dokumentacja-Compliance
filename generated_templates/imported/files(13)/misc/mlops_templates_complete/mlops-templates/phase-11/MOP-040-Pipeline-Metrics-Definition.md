---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-039: Pipeline Metrics Definition

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-039 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Metrics Overview

### 1.1 Metrics Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| Execution | Track pipeline runs | Duration, success rate |
| Resource | Monitor resource usage | CPU, memory, GPU |
| Data | Track data quality | Row count, schema drift |
| Business | Measure business impact | Models deployed, experiments |

---

## 2. Pipeline Execution Metrics

### 2.1 Core Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `pipeline_runs_total` | Counter | pipeline, status | Total pipeline runs |
| `pipeline_duration_seconds` | Histogram | pipeline | Execution duration |
| `pipeline_tasks_total` | Counter | pipeline, task, status | Task executions |
| `pipeline_task_duration_seconds` | Histogram | pipeline, task | Task duration |
| `pipeline_queue_time_seconds` | Histogram | pipeline | Time waiting in queue |
| `pipeline_retries_total` | Counter | pipeline, task | Retry count |

### 2.2 Prometheus Metrics Implementation

```python
# metrics/pipeline_metrics.py
from prometheus_client import Counter, Histogram, Gauge, Info

# Execution metrics
pipeline_runs = Counter(
    'mlops_pipeline_runs_total',
    'Total number of pipeline runs',
    ['pipeline_name', 'pipeline_type', 'status']
)

pipeline_duration = Histogram(
    'mlops_pipeline_duration_seconds',
    'Pipeline execution duration in seconds',
    ['pipeline_name', 'pipeline_type'],
    buckets=[60, 300, 600, 1800, 3600, 7200, 14400, 28800]
)

task_duration = Histogram(
    'mlops_task_duration_seconds',
    'Task execution duration in seconds',
    ['pipeline_name', 'task_name'],
    buckets=[10, 30, 60, 300, 600, 1800, 3600]
)

# Queue metrics
pipeline_queue_size = Gauge(
    'mlops_pipeline_queue_size',
    'Number of pipelines waiting in queue',
    ['pipeline_type']
)

pipeline_queue_time = Histogram(
    'mlops_pipeline_queue_time_seconds',
    'Time spent waiting in queue',
    ['pipeline_name'],
    buckets=[10, 30, 60, 120, 300, 600]
)

# Current state
pipelines_running = Gauge(
    'mlops_pipelines_running',
    'Number of currently running pipelines',
    ['pipeline_type']
)
```

### 2.3 Recording Rules

```yaml
# prometheus/pipeline-recording-rules.yaml
groups:
  - name: pipeline-metrics
    interval: 1m
    rules:
      # Success rate (5 min window)
      - record: mlops:pipeline_success_rate:5m
        expr: |
          sum(rate(mlops_pipeline_runs_total{status="success"}[5m])) by (pipeline_name)
          /
          sum(rate(mlops_pipeline_runs_total[5m])) by (pipeline_name)
      
      # Average duration
      - record: mlops:pipeline_duration_avg:5m
        expr: |
          sum(rate(mlops_pipeline_duration_seconds_sum[5m])) by (pipeline_name)
          /
          sum(rate(mlops_pipeline_duration_seconds_count[5m])) by (pipeline_name)
      
      # P95 duration
      - record: mlops:pipeline_duration_p95:5m
        expr: |
          histogram_quantile(0.95, 
            sum(rate(mlops_pipeline_duration_seconds_bucket[5m])) by (pipeline_name, le)
          )
      
      # Failure rate
      - record: mlops:pipeline_failure_rate:1h
        expr: |
          sum(increase(mlops_pipeline_runs_total{status="failed"}[1h])) by (pipeline_name)
          /
          sum(increase(mlops_pipeline_runs_total[1h])) by (pipeline_name)
```

---

## 3. Data Pipeline Metrics

### 3.1 Data Quality Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `data_rows_processed` | Counter | pipeline, table | Rows processed |
| `data_quality_score` | Gauge | pipeline, table | Quality score (0-1) |
| `data_null_rate` | Gauge | pipeline, column | Null value rate |
| `data_schema_changes` | Counter | pipeline, table | Schema change events |
| `data_freshness_seconds` | Gauge | pipeline, table | Age of latest data |

### 3.2 Implementation

```python
# metrics/data_metrics.py
from prometheus_client import Counter, Gauge, Histogram

data_rows_processed = Counter(
    'mlops_data_rows_processed_total',
    'Total rows processed by data pipeline',
    ['pipeline_name', 'table_name', 'operation']
)

data_quality_score = Gauge(
    'mlops_data_quality_score',
    'Data quality score from 0 to 1',
    ['pipeline_name', 'table_name']
)

data_freshness = Gauge(
    'mlops_data_freshness_seconds',
    'Age of the most recent data in seconds',
    ['table_name']
)

data_validation_results = Counter(
    'mlops_data_validation_results_total',
    'Data validation check results',
    ['pipeline_name', 'check_name', 'result']
)

# Usage example
def record_data_metrics(pipeline_name: str, table_name: str, df):
    """Record data pipeline metrics."""
    # Row count
    data_rows_processed.labels(
        pipeline_name=pipeline_name,
        table_name=table_name,
        operation='load'
    ).inc(len(df))
    
    # Quality score
    quality = calculate_quality_score(df)
    data_quality_score.labels(
        pipeline_name=pipeline_name,
        table_name=table_name
    ).set(quality)
    
    # Freshness
    if 'timestamp' in df.columns:
        age = (datetime.now() - df['timestamp'].max()).total_seconds()
        data_freshness.labels(table_name=table_name).set(age)
```

---

## 4. Training Pipeline Metrics

### 4.1 ML-Specific Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `training_epochs_total` | Counter | model | Training epochs |
| `training_loss` | Gauge | model, epoch | Current loss |
| `training_gpu_utilization` | Gauge | model, gpu_id | GPU usage |
| `experiment_count` | Counter | team | Experiments run |
| `model_registered` | Counter | model | Models registered |

### 4.2 Implementation

```python
# metrics/training_metrics.py
training_runs = Counter(
    'mlops_training_runs_total',
    'Total training runs',
    ['model_name', 'framework', 'status']
)

training_duration = Histogram(
    'mlops_training_duration_seconds',
    'Training duration',
    ['model_name'],
    buckets=[300, 600, 1800, 3600, 7200, 14400, 28800, 86400]
)

training_gpu_hours = Counter(
    'mlops_training_gpu_hours_total',
    'Total GPU hours used for training',
    ['model_name', 'gpu_type']
)

model_metrics = Gauge(
    'mlops_model_metric',
    'Model performance metric',
    ['model_name', 'metric_name']
)

experiments_total = Counter(
    'mlops_experiments_total',
    'Total experiments run',
    ['team', 'experiment_type']
)
```

---

## 5. Alerting Thresholds

### 5.1 Pipeline Alerts

```yaml
# prometheus/pipeline-alerts.yaml
groups:
  - name: pipeline-alerts
    rules:
      - alert: PipelineFailureRateHigh
        expr: mlops:pipeline_failure_rate:1h > 0.1
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline {{ $labels.pipeline_name }} failure rate > 10%"
          
      - alert: PipelineDurationAnomaly
        expr: |
          mlops:pipeline_duration_p95:5m > 
          mlops:pipeline_duration_p95:5m offset 1d * 2
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline {{ $labels.pipeline_name }} running 2x slower than usual"
          
      - alert: PipelineQueueBacklog
        expr: mlops_pipeline_queue_size > 20
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Pipeline queue backlog: {{ $value }} jobs waiting"
          
      - alert: DataFreshnessStale
        expr: mlops_data_freshness_seconds > 7200
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Data for {{ $labels.table_name }} is {{ $value | humanizeDuration }} old"
```

---

## 6. Dashboard Queries

### 6.1 Key Dashboard Panels

```promql
# Pipeline success rate (24h)
sum(increase(mlops_pipeline_runs_total{status="success"}[24h])) 
/ 
sum(increase(mlops_pipeline_runs_total[24h]))

# Pipeline duration P95
histogram_quantile(0.95, sum(rate(mlops_pipeline_duration_seconds_bucket[1h])) by (pipeline_name, le))

# Failed pipelines list
sum by (pipeline_name) (increase(mlops_pipeline_runs_total{status="failed"}[24h])) > 0

# Queue depth over time
mlops_pipeline_queue_size

# Data freshness
mlops_data_freshness_seconds
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial metrics definition |
