---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-070: MLOps Alerting Configuration

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-070 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Alerting Strategy

### 1.1 Alert Severity Levels

| Level | Response Time | Notification | Examples |
|-------|---------------|--------------|----------|
| Critical (P1) | 15 min | PagerDuty + Slack | Service down |
| High (P2) | 1 hour | PagerDuty + Slack | High error rate |
| Warning (P3) | 4 hours | Slack | Elevated latency |
| Info (P4) | Next business day | Email | Capacity warning |

### 1.2 Alert Routing

```yaml
# alertmanager/config.yaml
global:
  resolve_timeout: 5m
  slack_api_url: '${SLACK_WEBHOOK_URL}'
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

route:
  receiver: 'default'
  group_by: ['alertname', 'model', 'namespace']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true
    - match:
        severity: critical
      receiver: 'slack-critical'
    - match:
        severity: high
      receiver: 'pagerduty-high'
      continue: true
    - match:
        severity: high
      receiver: 'slack-high'
    - match:
        severity: warning
      receiver: 'slack-warning'
    - match:
        severity: info
      receiver: 'email-info'

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#mlops-alerts'
  
  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_CRITICAL_KEY}'
        severity: critical
  
  - name: 'pagerduty-high'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_HIGH_KEY}'
        severity: error
  
  - name: 'slack-critical'
    slack_configs:
      - channel: '#mlops-critical'
        title: ' CRITICAL: {{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.summary }}\n{{ end }}'
  
  - name: 'slack-high'
    slack_configs:
      - channel: '#mlops-alerts'
        title: ' HIGH: {{ .GroupLabels.alertname }}'
  
  - name: 'slack-warning'
    slack_configs:
      - channel: '#mlops-alerts'
        title: ' WARNING: {{ .GroupLabels.alertname }}'
  
  - name: 'email-info'
    email_configs:
      - to: 'mlops-team@company.com'
        send_resolved: true
```

---

## 2. Model Serving Alerts

### 2.1 Availability Alerts

```yaml
# prometheus/alerts/model-serving.yaml
groups:
  - name: model-serving-availability
    rules:
      - alert: ModelServiceDown
        expr: up{job="model-serving"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Model serving service is down"
          description: "{{ $labels.instance }} has been down for more than 1 minute"
          runbook_url: "https://runbooks.company.com/model-service-down"
      
      - alert: ModelEndpointDown
        expr: |
          sum(kserve_inferenceservice_ready{ready="true"}) by (inferenceservice_name) == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Model {{ $labels.inferenceservice_name }} is not ready"
      
      - alert: ModelPodCrashLooping
        expr: |
          increase(kube_pod_container_status_restarts_total{namespace="models"}[1h]) > 5
        labels:
          severity: high
        annotations:
          summary: "Pod {{ $labels.pod }} is crash looping"
```

### 2.2 Performance Alerts

```yaml
  - name: model-serving-performance
    rules:
      - alert: ModelHighLatency
        expr: |
          histogram_quantile(0.99, 
            sum(rate(inference_latency_seconds_bucket[5m])) by (model, le)
          ) > 0.1
        for: 5m
        labels:
          severity: high
        annotations:
          summary: "Model {{ $labels.model }} P99 latency > 100ms"
          current_value: "{{ $value | humanizeDuration }}"
      
      - alert: ModelHighErrorRate
        expr: |
          sum(rate(inference_requests_total{status="error"}[5m])) by (model)
          /
          sum(rate(inference_requests_total[5m])) by (model) > 0.01
        for: 5m
        labels:
          severity: high
        annotations:
          summary: "Model {{ $labels.model }} error rate > 1%"
          current_value: "{{ $value | humanizePercentage }}"
      
      - alert: ModelLowThroughput
        expr: |
          sum(rate(inference_requests_total[5m])) by (model) 
          < 
          sum(rate(inference_requests_total[5m] offset 1d)) by (model) * 0.5
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Model {{ $labels.model }} throughput dropped 50%"
```

---

## 3. Data & Feature Alerts

### 3.1 Feature Store Alerts

```yaml
  - name: feature-store
    rules:
      - alert: FeatureStoreDown
        expr: up{job="feast-server"} == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Feature store is down"
      
      - alert: FeatureMaterializationFailed
        expr: increase(feast_materialization_failures_total[1h]) > 0
        labels:
          severity: high
        annotations:
          summary: "Feature materialization failed"
      
      - alert: FeatureStaleData
        expr: |
          time() - feast_feature_freshness_seconds > 7200
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Features older than 2 hours"
      
      - alert: FeatureNullRateHigh
        expr: feast_feature_null_rate > 0.1
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "High null rate in feature {{ $labels.feature }}"
```

### 3.2 Data Quality Alerts

```yaml
  - name: data-quality
    rules:
      - alert: DataDriftDetected
        expr: mlops_prediction_drift_score > 0.15
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "Data drift detected for model {{ $labels.model }}"
      
      - alert: DataSchemaChange
        expr: increase(mlops_schema_changes_total[1h]) > 0
        labels:
          severity: warning
        annotations:
          summary: "Schema change detected in {{ $labels.table }}"
```

---

## 4. Pipeline Alerts

### 4.1 Training Pipeline Alerts

```yaml
  - name: training-pipelines
    rules:
      - alert: TrainingPipelineFailed
        expr: |
          increase(airflow_task_fail{dag_id=~".*training.*"}[1h]) > 0
        labels:
          severity: high
        annotations:
          summary: "Training pipeline {{ $labels.dag_id }} failed"
      
      - alert: TrainingPipelineStuck
        expr: |
          airflow_dag_run_duration_seconds{state="running"} > 14400
        labels:
          severity: warning
        annotations:
          summary: "Training pipeline running > 4 hours"
      
      - alert: NoRecentTraining
        expr: |
          time() - max(airflow_dag_last_success_timestamp{dag_id=~".*training.*"}) > 86400
        labels:
          severity: info
        annotations:
          summary: "No successful training in 24 hours"
```

---

## 5. Infrastructure Alerts

### 5.1 Resource Alerts

```yaml
  - name: infrastructure
    rules:
      - alert: HighCPUUsage
        expr: |
          avg by (pod) (rate(container_cpu_usage_seconds_total{namespace="models"}[5m])) 
          / 
          avg by (pod) (kube_pod_container_resource_limits{resource="cpu",namespace="models"}) 
          > 0.9
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Pod {{ $labels.pod }} CPU > 90%"
      
      - alert: HighMemoryUsage
        expr: |
          container_memory_working_set_bytes{namespace="models"}
          /
          kube_pod_container_resource_limits{resource="memory",namespace="models"}
          > 0.9
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Pod {{ $labels.pod }} memory > 90%"
      
      - alert: GPUHighUtilization
        expr: DCGM_FI_DEV_GPU_UTIL > 95
        for: 30m
        labels:
          severity: info
        annotations:
          summary: "GPU utilization consistently > 95%"
      
      - alert: DiskSpaceLow
        expr: |
          kubelet_volume_stats_available_bytes / kubelet_volume_stats_capacity_bytes < 0.15
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Disk space < 15% on {{ $labels.persistentvolumeclaim }}"
```

---

## 6. Alert Silencing

### 6.1 Silence Configuration

```yaml
# Silence during maintenance
# POST to /api/v2/silences
{
  "matchers": [
    {
      "name": "namespace",
      "value": "models",
      "isRegex": false
    }
  ],
  "startsAt": "2024-01-15T02:00:00Z",
  "endsAt": "2024-01-15T06:00:00Z",
  "createdBy": "mlops-team",
  "comment": "Scheduled maintenance window"
}
```

### 6.2 Inhibition Rules

```yaml
# alertmanager/inhibitions.yaml
inhibit_rules:
  # If service is down, inhibit performance alerts
  - source_match:
      alertname: ModelServiceDown
    target_match_re:
      alertname: Model.*
    equal: ['model']
  
  # If cluster is down, inhibit all model alerts
  - source_match:
      alertname: KubernetesClusterDown
    target_match:
      severity: warning
```

---

## 7. Alert Testing

### 7.1 Test Alert Script

```bash
#!/bin/bash
# Test alert routing

# Send test alert
curl -X POST http://alertmanager:9093/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '[{
    "labels": {
      "alertname": "TestAlert",
      "severity": "warning",
      "model": "test-model"
    },
    "annotations": {
      "summary": "This is a test alert"
    }
  }]'
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial alerting configuration |
