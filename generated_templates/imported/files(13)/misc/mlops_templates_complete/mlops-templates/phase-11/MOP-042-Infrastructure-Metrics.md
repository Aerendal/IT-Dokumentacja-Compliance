---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-042: MLOps Infrastructure Metrics

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-042 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Compute Metrics

### 1.1 Kubernetes Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `node_cpu_utilization` | Gauge | node | CPU usage % |
| `node_memory_utilization` | Gauge | node | Memory usage % |
| `pod_cpu_usage` | Gauge | pod, namespace | Pod CPU |
| `pod_memory_usage` | Gauge | pod, namespace | Pod memory |
| `pod_gpu_utilization` | Gauge | pod, gpu | GPU usage % |

### 1.2 Key Queries

```promql
# Node CPU utilization
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Node memory utilization
(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# Pod CPU usage by namespace
sum by (namespace) (rate(container_cpu_usage_seconds_total[5m]))

# Pod memory usage by namespace
sum by (namespace) (container_memory_working_set_bytes)

# GPU utilization (DCGM metrics)
DCGM_FI_DEV_GPU_UTIL

# GPU memory utilization
DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL * 100
```

---

## 2. Storage Metrics

### 2.1 Storage Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `s3_bucket_size_bytes` | Gauge | S3 bucket size |
| `s3_objects_total` | Gauge | Object count |
| `pv_usage_bytes` | Gauge | PV usage |
| `pv_capacity_bytes` | Gauge | PV capacity |

### 2.2 Custom S3 Metrics Exporter

```python
# metrics/s3_metrics.py
import boto3
from prometheus_client import Gauge

s3_bucket_size = Gauge(
    'mlops_s3_bucket_size_bytes',
    'S3 bucket size in bytes',
    ['bucket', 'storage_class']
)

s3_object_count = Gauge(
    'mlops_s3_object_count',
    'Number of objects in S3 bucket',
    ['bucket']
)

def collect_s3_metrics():
    """Collect S3 bucket metrics."""
    s3 = boto3.client('s3')
    cloudwatch = boto3.client('cloudwatch')
    
    for bucket in ['mlops-artifacts', 'mlops-features', 'mlops-models']:
        # Get bucket size from CloudWatch
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/S3',
            MetricName='BucketSizeBytes',
            Dimensions=[
                {'Name': 'BucketName', 'Value': bucket},
                {'Name': 'StorageType', 'Value': 'StandardStorage'}
            ],
            StartTime=datetime.utcnow() - timedelta(days=1),
            EndTime=datetime.utcnow(),
            Period=86400,
            Statistics=['Average']
        )
        
        if response['Datapoints']:
            size = response['Datapoints'][0]['Average']
            s3_bucket_size.labels(bucket=bucket, storage_class='STANDARD').set(size)
```

---

## 3. Database Metrics

### 3.1 PostgreSQL Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `pg_connections_active` | Gauge | Active connections |
| `pg_connections_max` | Gauge | Max connections |
| `pg_database_size_bytes` | Gauge | Database size |
| `pg_query_duration_seconds` | Histogram | Query latency |
| `pg_replication_lag_seconds` | Gauge | Replication lag |

### 3.2 Redis Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `redis_memory_used_bytes` | Gauge | Memory usage |
| `redis_connected_clients` | Gauge | Client connections |
| `redis_commands_processed` | Counter | Commands/sec |
| `redis_keyspace_hits_ratio` | Gauge | Cache hit ratio |

### 3.3 Key Queries

```promql
# PostgreSQL connection utilization
pg_stat_activity_count / pg_settings_max_connections * 100

# PostgreSQL slow queries
rate(pg_stat_statements_seconds_total[5m])

# Redis memory utilization
redis_memory_used_bytes / redis_memory_max_bytes * 100

# Redis hit ratio
redis_keyspace_hits_total / (redis_keyspace_hits_total + redis_keyspace_misses_total)
```

---

## 4. Network Metrics

### 4.1 Network Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `network_receive_bytes` | Counter | Bytes received |
| `network_transmit_bytes` | Counter | Bytes transmitted |
| `http_requests_total` | Counter | HTTP requests |
| `http_request_duration` | Histogram | Request latency |

### 4.2 Service Mesh Metrics (Istio)

```promql
# Request rate by service
sum(rate(istio_requests_total[5m])) by (destination_service)

# Error rate
sum(rate(istio_requests_total{response_code=~"5.."}[5m])) 
/ 
sum(rate(istio_requests_total[5m]))

# P99 latency
histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[5m])) by (le, destination_service))
```

---

## 5. Alerting Rules

```yaml
# prometheus/infrastructure-alerts.yaml
groups:
  - name: infrastructure-alerts
    rules:
      # Compute alerts
      - alert: HighCPUUtilization
        expr: |
          100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 85
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "High CPU utilization on {{ $labels.instance }}"
          
      - alert: HighMemoryUtilization
        expr: |
          (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 > 90
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High memory utilization on {{ $labels.instance }}"
          
      - alert: GPUHighUtilization
        expr: DCGM_FI_DEV_GPU_UTIL > 95
        for: 30m
        labels:
          severity: info
        annotations:
          summary: "GPU {{ $labels.gpu }} utilization above 95%"
          
      # Storage alerts
      - alert: StorageNearCapacity
        expr: |
          (kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes) > 0.85
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "PV {{ $labels.persistentvolumeclaim }} is {{ $value | humanizePercentage }} full"
          
      - alert: S3BucketGrowthAnomaly
        expr: |
          delta(mlops_s3_bucket_size_bytes[1d]) > 
          avg_over_time(delta(mlops_s3_bucket_size_bytes[1d])[7d:1d]) * 2
        for: 1h
        labels:
          severity: info
        annotations:
          summary: "Unusual growth in S3 bucket {{ $labels.bucket }}"
          
      # Database alerts
      - alert: PostgreSQLConnectionsHigh
        expr: pg_stat_activity_count / pg_settings_max_connections > 0.8
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "PostgreSQL connections at {{ $value | humanizePercentage }} of max"
          
      - alert: RedisMemoryHigh
        expr: redis_memory_used_bytes / redis_memory_max_bytes > 0.9
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Redis memory usage above 90%"
```

---

## 6. Dashboard Layout

### 6.1 Infrastructure Overview Dashboard

```json
{
  "title": "MLOps Infrastructure",
  "rows": [
    {
      "title": "Cluster Overview",
      "panels": [
        {"title": "CPU Usage", "type": "gauge"},
        {"title": "Memory Usage", "type": "gauge"},
        {"title": "GPU Usage", "type": "gauge"},
        {"title": "Node Count", "type": "stat"}
      ]
    },
    {
      "title": "Storage",
      "panels": [
        {"title": "S3 Usage", "type": "timeseries"},
        {"title": "PV Usage", "type": "bargauge"},
        {"title": "DB Size", "type": "stat"}
      ]
    },
    {
      "title": "Database",
      "panels": [
        {"title": "PostgreSQL Connections", "type": "timeseries"},
        {"title": "Redis Memory", "type": "timeseries"},
        {"title": "Query Latency", "type": "heatmap"}
      ]
    }
  ]
}
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial infrastructure metrics |
