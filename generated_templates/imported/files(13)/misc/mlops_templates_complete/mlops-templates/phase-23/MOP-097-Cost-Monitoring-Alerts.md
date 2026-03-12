---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-097: Cost Monitoring and Alerts

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-097 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [FinOps / ML Platform Lead] |

---

## 1. Cost Monitoring Strategy

### 1.1 Monitoring Levels

| Level | Frequency | Alert Threshold | Action |
|-------|-----------|-----------------|--------|
| Daily | Daily | >120% of daily avg | Investigate |
| Weekly | Weekly | >110% of weekly budget | Review |
| Monthly | Monthly | >100% of monthly budget | Escalate |

### 1.2 Cost Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| team | Team allocation | fraud-detection |
| environment | Env tracking | production |
| model | Model attribution | fraud-model-v2 |
| project | Project tracking | q1-initiative |

---

## 2. Alert Configuration

### 2.1 AWS Budget Alerts

```json
{
  "BudgetName": "MLOps-Monthly",
  "BudgetLimit": {
    "Amount": "50000",
    "Unit": "USD"
  },
  "BudgetType": "COST",
  "TimeUnit": "MONTHLY",
  "NotificationsWithSubscribers": [
    {
      "Notification": {
        "NotificationType": "ACTUAL",
        "ComparisonOperator": "GREATER_THAN",
        "Threshold": 80,
        "ThresholdType": "PERCENTAGE"
      },
      "Subscribers": [
        {"SubscriptionType": "EMAIL", "Address": "mlops-team@company.com"}
      ]
    },
    {
      "Notification": {
        "NotificationType": "ACTUAL",
        "ComparisonOperator": "GREATER_THAN",
        "Threshold": 100,
        "ThresholdType": "PERCENTAGE"
      },
      "Subscribers": [
        {"SubscriptionType": "EMAIL", "Address": "platform-lead@company.com"},
        {"SubscriptionType": "SNS", "Address": "arn:aws:sns:us-west-2:xxx:cost-alerts"}
      ]
    }
  ]
}
```

### 2.2 Prometheus Cost Alerts

```yaml
# prometheus/cost-alerts.yaml
groups:
  - name: cost-alerts
    rules:
      - alert: DailyCostAnomaly
        expr: |
          sum(increase(cloud_cost_usd[24h])) 
          > 
          avg_over_time(sum(increase(cloud_cost_usd[24h]))[7d:1d]) * 1.2
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "Daily cost 20% higher than 7-day average"
          
      - alert: GPUIdleCost
        expr: |
          (sum(node_gpu_count) - sum(DCGM_FI_DEV_GPU_UTIL > 10)) 
          * 3.0  # $3/hr per idle GPU
          * 24 > 100  # > $100/day in idle GPUs
        for: 2h
        labels:
          severity: warning
        annotations:
          summary: "Significant idle GPU costs detected"
          
      - alert: StorageGrowthAnomaly
        expr: |
          delta(aws_s3_bucket_size_bytes[7d]) / 1e9 > 100  # >100GB growth
        labels:
          severity: info
        annotations:
          summary: "S3 storage grew by >100GB in 7 days"
```

---

## 3. Cost Dashboard

### 3.1 Grafana Queries

```promql
# Daily spend
sum(increase(cloud_cost_usd[24h]))

# Spend by team
sum(increase(cloud_cost_usd[24h])) by (team)

# Cost per inference (rolling 7d)
sum(increase(cloud_cost_usd{service="model-serving"}[7d]))
/
sum(increase(inference_requests_total[7d]))
* 1000  # per 1000 inferences

# GPU utilization vs cost
sum(DCGM_FI_DEV_GPU_UTIL) / count(DCGM_FI_DEV_GPU_UTIL)  # utilization
sum(rate(gpu_cost_usd[1h]))  # hourly GPU cost
```

### 3.2 Dashboard Panels

| Panel | Metric | Alert |
|-------|--------|-------|
| Daily Spend | Total $ | >120% avg |
| MTD vs Budget | % of budget | >80%, >100% |
| Cost by Team | $ per team | Anomaly |
| Cost per Inference | $/1K inferences | Increase |
| Idle Resources | Wasted $ | >$100/day |

---

## 4. Automated Cost Reports

### 4.1 Daily Cost Email

```python
# cost_monitoring/daily_report.py
def send_daily_cost_report():
    """Send daily cost summary."""
    yesterday = datetime.now() - timedelta(days=1)
    
    costs = get_daily_costs(yesterday)
    avg_7d = get_average_daily_cost(7)
    
    report = f"""
    MLOps Daily Cost Report - {yesterday.strftime('%Y-%m-%d')}
    
    Yesterday's Spend: ${costs['total']:,.2f}
    7-Day Average: ${avg_7d:,.2f}
    Variance: {((costs['total'] - avg_7d) / avg_7d * 100):+.1f}%
    
    Top Spend Categories:
    - Compute: ${costs['compute']:,.2f}
    - GPU: ${costs['gpu']:,.2f}
    - Storage: ${costs['storage']:,.2f}
    
    MTD Total: ${costs['mtd']:,.2f}
    MTD Budget: ${costs['budget']:,.2f}
    Budget Remaining: ${costs['budget'] - costs['mtd']:,.2f}
    """
    
    if costs['total'] > avg_7d * 1.2:
        report += "\n ALERT: Spend 20% above average!"
    
    send_email(
        to="mlops-team@company.com",
        subject=f"MLOps Daily Cost: ${costs['total']:,.0f}",
        body=report
    )
```

---

## 5. Cost Optimization Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| Idle GPU | GPU <10% util for 2hr | Alert + Auto-terminate |
| Over-provisioned | CPU <30% avg for 7d | Right-size recommendation |
| Storage growth | >10% growth/week | Review + cleanup |
| Budget breach | >100% MTD | Freeze non-critical |

---

## 6. Response Procedures

### 6.1 Cost Spike Investigation

```markdown
## Cost Spike Investigation

1. **Identify source**
   - Check cost by team/service
   - Compare to baseline
   - Identify anomalous resources

2. **Common causes**
   - Runaway training job
   - Misconfigured autoscaling
   - Data pipeline issue
   - Forgotten resources

3. **Remediation**
   - Terminate unnecessary resources
   - Fix configuration
   - Update alerts to prevent recurrence

4. **Document**
   - Root cause
   - Actions taken
   - Prevention measures
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial cost monitoring |
