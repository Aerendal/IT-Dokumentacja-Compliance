---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-084: SLA Monitoring and Reporting

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-084 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE / Platform Lead] |

---

## 1. SLA Definitions

### 1.1 Platform SLAs

| Service | Metric | Target | Measurement |
|---------|--------|--------|-------------|
| MLflow | Availability | 99.9% | Monthly |
| Feature Store | Availability | 99.9% | Monthly |
| Model Serving | Availability | 99.95% | Monthly |
| Model Serving | Latency P99 | <100ms | Continuous |
| Training Pipelines | Success Rate | 95% | Weekly |

### 1.2 SLA Tiers

| Tier | Availability | Support Response | Use Case |
|------|--------------|------------------|----------|
| Tier 1 | 99.99% | 15 min | Business critical |
| Tier 2 | 99.9% | 1 hour | Production models |
| Tier 3 | 99.5% | 4 hours | Non-critical |
| Tier 4 | 99% | Next business day | Development |

---

## 2. SLA Metrics Collection

### 2.1 Prometheus Queries

```promql
# Availability (uptime)
avg_over_time(up{job="model-serving"}[30d]) * 100

# Error rate
sum(rate(http_requests_total{status=~"5.."}[30d]))
/
sum(rate(http_requests_total[30d])) * 100

# Latency P99
histogram_quantile(0.99, 
  sum(rate(http_request_duration_seconds_bucket[30d])) by (le)
)

# Pipeline success rate
sum(airflow_task_success_total) 
/ 
(sum(airflow_task_success_total) + sum(airflow_task_fail_total)) * 100
```

### 2.2 Recording Rules

```yaml
# prometheus/sla-recording-rules.yaml
groups:
  - name: sla-metrics
    interval: 1m
    rules:
      # 30-day rolling availability
      - record: sla:availability:30d
        expr: avg_over_time(up{job="model-serving"}[30d]) * 100
        labels:
          sla_metric: "availability"
      
      # Error budget remaining
      - record: sla:error_budget_remaining:30d
        expr: |
          (1 - (
            sum(increase(http_requests_total{status=~"5.."}[30d]))
            /
            sum(increase(http_requests_total[30d]))
          )) / 0.001 * 100
        labels:
          sla_metric: "error_budget"
      
      # Monthly P99 latency
      - record: sla:latency_p99:30d
        expr: |
          histogram_quantile(0.99,
            sum(rate(http_request_duration_seconds_bucket[30d])) by (le, service)
          )
```

---

## 3. Error Budget Tracking

### 3.1 Error Budget Calculator

```python
# sla/error_budget.py
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class ErrorBudget:
    sla_target: float  # e.g., 99.9
    period_days: int
    total_requests: int
    failed_requests: int
    
    @property
    def allowed_failures(self) -> int:
        """Calculate allowed failures for the period."""
        return int(self.total_requests * (1 - self.sla_target / 100))
    
    @property
    def budget_remaining(self) -> int:
        """Remaining error budget."""
        return max(0, self.allowed_failures - self.failed_requests)
    
    @property
    def budget_remaining_pct(self) -> float:
        """Remaining budget as percentage."""
        if self.allowed_failures == 0:
            return 0
        return (self.budget_remaining / self.allowed_failures) * 100
    
    @property
    def current_availability(self) -> float:
        """Current availability percentage."""
        if self.total_requests == 0:
            return 100
        return (1 - self.failed_requests / self.total_requests) * 100

def calculate_error_budget(service: str, sla_target: float = 99.9) -> ErrorBudget:
    """Calculate error budget from Prometheus metrics."""
    from prometheus_api_client import PrometheusConnect
    
    prom = PrometheusConnect(url="http://prometheus:9090")
    
    # Get 30-day totals
    total_query = f'sum(increase(http_requests_total{{service="{service}"}}[30d]))'
    failed_query = f'sum(increase(http_requests_total{{service="{service}",status=~"5.."}}[30d]))'
    
    total = prom.custom_query(total_query)[0]['value'][1]
    failed = prom.custom_query(failed_query)[0]['value'][1]
    
    return ErrorBudget(
        sla_target=sla_target,
        period_days=30,
        total_requests=int(float(total)),
        failed_requests=int(float(failed))
    )
```

### 3.2 Budget Alerts

```yaml
# prometheus/error-budget-alerts.yaml
groups:
  - name: error-budget
    rules:
      - alert: ErrorBudgetLow
        expr: sla:error_budget_remaining:30d < 25
        labels:
          severity: warning
        annotations:
          summary: "Error budget below 25% for {{ $labels.service }}"
          
      - alert: ErrorBudgetCritical
        expr: sla:error_budget_remaining:30d < 10
        labels:
          severity: critical
        annotations:
          summary: "Error budget below 10% - freeze deployments"
          
      - alert: ErrorBudgetExhausted
        expr: sla:error_budget_remaining:30d <= 0
        labels:
          severity: critical
        annotations:
          summary: "Error budget exhausted - SLA breach imminent"
```

---

## 4. SLA Dashboard

### 4.1 Grafana Dashboard Config

```json
{
  "title": "SLA Dashboard",
  "panels": [
    {
      "title": "Availability (30 days)",
      "type": "gauge",
      "targets": [
        {"expr": "sla:availability:30d{service=\"model-serving\"}"}
      ],
      "fieldConfig": {
        "defaults": {
          "thresholds": {
            "steps": [
              {"value": 0, "color": "red"},
              {"value": 99, "color": "yellow"},
              {"value": 99.9, "color": "green"}
            ]
          },
          "unit": "percent",
          "min": 95,
          "max": 100
        }
      }
    },
    {
      "title": "Error Budget Remaining",
      "type": "gauge",
      "targets": [
        {"expr": "sla:error_budget_remaining:30d"}
      ]
    },
    {
      "title": "Latency P99 vs SLA",
      "type": "timeseries",
      "targets": [
        {"expr": "sla:latency_p99:30d", "legendFormat": "Actual P99"},
        {"expr": "0.1", "legendFormat": "SLA Target (100ms)"}
      ]
    }
  ]
}
```

---

## 5. Monthly SLA Report

### 5.1 Report Template

```markdown
# SLA Report - [Month Year]

## Executive Summary
- Overall platform availability: XX.XX%
- SLA compliance:  Met /  Missed
- Error budget consumed: XX%

## Service Level Summary

| Service | Target | Actual | Status |
|---------|--------|--------|--------|
| MLflow | 99.9% | XX.XX% | / |
| Feature Store | 99.9% | XX.XX% | / |
| Model Serving | 99.95% | XX.XX% | / |

## Incidents Impacting SLA

| Date | Duration | Impact | Root Cause |
|------|----------|--------|------------|
| YYYY-MM-DD | Xh Xm | X.XX% availability | [Description] |

## Error Budget Status

| Service | Budget (month) | Consumed | Remaining |
|---------|----------------|----------|-----------|
| Model Serving | 0.05% | X.XX% | X.XX% |

## Actions for Next Month
1. [Action item 1]
2. [Action item 2]

## Appendix: Daily Availability
[Chart or table with daily data]
```

### 5.2 Automated Report Generation

```python
# sla/monthly_report.py
def generate_monthly_report(month: str):
    """Generate monthly SLA report."""
    
    # Collect metrics
    metrics = collect_sla_metrics(month)
    incidents = get_incidents(month)
    
    # Generate report
    report = f"""
# SLA Report - {month}

## Executive Summary
- Overall platform availability: {metrics['availability']:.2f}%
- SLA compliance: {' Met' if metrics['sla_met'] else ' Missed'}
- Error budget consumed: {metrics['budget_consumed']:.1f}%

## Service Level Summary

| Service | Target | Actual | Status |
|---------|--------|--------|--------|
"""
    
    for service in metrics['services']:
        status = '' if service['actual'] >= service['target'] else ''
        report += f"| {service['name']} | {service['target']}% | {service['actual']:.2f}% | {status} |\n"
    
    # Save report
    save_report(report, f"sla-report-{month}.md")
    
    # Send to stakeholders
    send_report_email(report, month)
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial SLA monitoring |
