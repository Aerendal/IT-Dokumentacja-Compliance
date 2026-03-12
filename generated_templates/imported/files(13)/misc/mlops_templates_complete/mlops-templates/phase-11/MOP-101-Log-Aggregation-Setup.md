---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-101: Log Aggregation Setup

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-101 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Logging Architecture

### 1.1 Log Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Log Aggregation Flow                          │
│                                                                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │ Apps    │───►│Fluentd  │───►│  Kafka  │───►│  Loki   │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │            │
│  • MLflow       • Parse        • Buffer       • Store         │
│  • Feast        • Enrich       • Route        • Index         │
│  • KServe       • Filter       • Replicate    • Query         │
│  • Training                                                    │
│                                                                │
│                         ▼                                      │
│                  ┌─────────────┐                               │
│                  │   Grafana   │                               │
│                  └─────────────┘                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Structured Logging

### 2.1 Log Format Standard

```python
# logging_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "service": getattr(record, 'service', 'unknown'),
            "model": getattr(record, 'model', None),
            "request_id": getattr(record, 'request_id', None),
        }
        
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_record)

# Usage
logger = logging.getLogger(__name__)
logger.info("Inference completed", extra={
    "service": "model-serving",
    "model": "fraud-detection",
    "request_id": "abc-123",
    "latency_ms": 45
})
```

### 2.2 Required Fields

| Field | Required | Description |
|-------|----------|-------------|
| timestamp |  | ISO 8601 format |
| level |  | DEBUG/INFO/WARN/ERROR |
| service |  | Service name |
| message |  | Log message |
| request_id | Recommended | Trace correlation |
| model | For inference | Model name |

---

## 3. Fluentd Configuration

### 3.1 Fluentd DaemonSet

```yaml
# k8s/fluentd-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
  namespace: logging
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/containers/*mlops*.log
      pos_file /var/log/fluentd-mlops.pos
      tag kubernetes.*
      <parse>
        @type json
        time_key timestamp
        time_format %Y-%m-%dT%H:%M:%S.%NZ
      </parse>
    </source>
    
    <filter kubernetes.**>
      @type kubernetes_metadata
    </filter>
    
    <filter kubernetes.**>
      @type record_transformer
      <record>
        namespace ${record.dig("kubernetes", "namespace_name")}
        pod ${record.dig("kubernetes", "pod_name")}
        container ${record.dig("kubernetes", "container_name")}
      </record>
    </filter>
    
    <match kubernetes.**>
      @type loki
      url "http://loki:3100"
      <label>
        namespace
        pod
        container
        service
      </label>
      <buffer>
        @type file
        path /var/log/fluentd-buffer
        flush_interval 5s
      </buffer>
    </match>
```

---

## 4. Loki Queries

### 4.1 Common Queries

```logql
# Errors in last hour
{namespace="mlops"} |= "ERROR" | json | line_format "{{.message}}"

# Model inference logs
{service="model-serving", model="fraud-detection"} | json

# Slow requests (>100ms)
{service="model-serving"} | json | latency_ms > 100

# Error rate by service
sum(rate({namespace="mlops"} |= "ERROR" [5m])) by (service)
```

### 4.2 Grafana Dashboard Panels

```yaml
# Log volume by service
sum(rate({namespace="mlops"}[5m])) by (service)

# Error percentage
sum(rate({namespace="mlops"} |= "ERROR"[5m])) 
/ 
sum(rate({namespace="mlops"}[5m])) * 100

# Top errors
topk(10, sum by (message) (rate({namespace="mlops"} |= "ERROR"[1h])))
```

---

## 5. Log Retention

| Log Type | Hot Storage | Cold Storage | Total |
|----------|-------------|--------------|-------|
| Application | 7 days | 30 days | 37 days |
| Audit | 30 days | 1 year | 13 months |
| Security | 30 days | 7 years | 7 years |
| Debug | 3 days | None | 3 days |

---

## 6. Alerting on Logs

```yaml
# prometheus/log-alerts.yaml
groups:
  - name: log-alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate({namespace="mlops"} |= "ERROR"[5m])) 
          / 
          sum(rate({namespace="mlops"}[5m])) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Error rate > 5% in MLOps namespace"
          
      - alert: NoLogs
        expr: |
          absent(sum(rate({namespace="mlops"}[5m])))
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "No logs from MLOps services"
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial log aggregation setup |
