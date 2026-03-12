---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-058: Capacity Planning

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-058 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Priority** | HIGH |
| **Owner** | [ML Platform Lead / Cloud Architect] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Template Content

---

# MLOps Capacity Planning

## 1. Current Capacity

### 1.1 Compute Resources

| Resource | Allocated | Used | Available | Utilization |
|----------|-----------|------|-----------|-------------|
| **CPU (vCPU)** | | | | |
| Model Serving | 200 | 140 | 60 | 70% |
| Training | 400 | 280 | 120 | 70% |
| Platform Services | 50 | 35 | 15 | 70% |
| **GPU** | | | | |
| Inference (T4) | 16 | 12 | 4 | 75% |
| Training (A100) | 8 | 6 | 2 | 75% |
| **Memory (GB)** | | | | |
| Model Serving | 800 | 560 | 240 | 70% |
| Training | 1,600 | 1,120 | 480 | 70% |
| Platform Services | 200 | 140 | 60 | 70% |

### 1.2 Storage Capacity

| Storage Type | Allocated | Used | Available | Utilization |
|--------------|-----------|------|-----------|-------------|
| S3 (Artifacts) | 20 TB | 12 TB | 8 TB | 60% |
| S3 (Features) | 100 TB | 65 TB | 35 TB | 65% |
| EBS (Persistent) | 10 TB | 6 TB | 4 TB | 60% |
| PostgreSQL | 500 GB | 300 GB | 200 GB | 60% |
| Redis | 200 GB | 120 GB | 80 GB | 60% |

### 1.3 Network Capacity

| Path | Bandwidth | Peak Usage | Headroom |
|------|-----------|------------|----------|
| Ingress | 10 Gbps | 6 Gbps | 40% |
| Service-to-Service | 25 Gbps | 15 Gbps | 40% |
| Storage I/O | 25 Gbps | 12 Gbps | 52% |

---

## 2. Demand Forecast

### 2.1 Growth Projections

| Metric | Current | +3 mo | +6 mo | +12 mo |
|--------|---------|-------|-------|--------|
| Models in production | 25 | 35 | 45 | 70 |
| Inference RPS | 5,000 | 8,000 | 15,000 | 30,000 |
| Active ML users | 50 | 65 | 80 | 120 |
| Experiments/month | 1,000 | 1,500 | 2,500 | 5,000 |
| Features in store | 2,000 | 3,000 | 5,000 | 10,000 |
| Training jobs/day | 50 | 80 | 120 | 200 |

### 2.2 Capacity Requirements Projection

| Resource | Current | +3 mo | +6 mo | +12 mo |
|----------|---------|-------|-------|--------|
| **Compute** | | | | |
| Serving vCPU | 200 | 320 | 600 | 1,200 |
| Serving GPU | 16 | 24 | 40 | 80 |
| Training vCPU | 400 | 640 | 1,000 | 1,600 |
| Training GPU | 8 | 12 | 20 | 40 |
| **Storage** | | | | |
| Artifacts (TB) | 20 | 30 | 50 | 100 |
| Features (TB) | 100 | 150 | 250 | 500 |
| Database (GB) | 500 | 700 | 1,000 | 2,000 |
| **Network** | | | | |
| Bandwidth (Gbps) | 10 | 15 | 25 | 50 |

---

## 3. Capacity Planning Process

### 3.1 Planning Cycle

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Quarterly Capacity Planning Cycle                 │
│                                                                     │
│  Week 1          Week 2          Week 3          Week 4            │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │ Collect │───►│ Analyze │───►│ Plan    │───►│ Execute │        │
│  │ Data    │    │ Trends  │    │ Changes │    │ & Review│        │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘        │
│                                                                     │
│  Activities:                                                        │
│  • Gather metrics  • Forecast     • Budget        • Procurement    │
│  • Survey teams    • Identify     • Prioritize    • Implement      │
│  • Review growth     gaps        • Schedule      • Validate        │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Capacity Review Checklist

```markdown
## Quarterly Capacity Review

**Quarter:** Q[X] [Year]
**Review Date:** [Date]
**Reviewer:** [Name]

### Data Collection
- [ ] Current utilization metrics exported
- [ ] Growth trends analyzed
- [ ] Team forecasts collected
- [ ] Business roadmap reviewed

### Analysis
- [ ] Utilization vs targets compared
- [ ] Bottlenecks identified
- [ ] Capacity gaps calculated
- [ ] Risk assessment completed

### Planning
- [ ] Capacity additions specified
- [ ] Timeline established
- [ ] Budget approved
- [ ] Procurement initiated

### Metrics Summary
| Resource | Utilization | Gap | Action |
|----------|-------------|-----|--------|
| [Resource] | [%] | [Amount] | [Action] |
```

---

## 4. Scaling Strategies

### 4.1 Scaling Thresholds

| Resource | Warning (Yellow) | Critical (Red) | Action |
|----------|------------------|----------------|--------|
| CPU utilization | >70% | >85% | Scale up |
| Memory utilization | >75% | >90% | Scale up |
| GPU utilization | >80% | >90% | Add GPUs |
| Storage utilization | >70% | >85% | Expand storage |
| Latency P99 | >75ms | >100ms | Scale serving |

### 4.2 Auto-Scaling Configuration

```yaml
# HPA for model serving
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: model-serving-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-serving
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: inference_queue_size
      target:
        type: AverageValue
        averageValue: "100"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 25
        periodSeconds: 120
```

### 4.3 Capacity Expansion Lead Times

| Resource | Lead Time | Process |
|----------|-----------|---------|
| Kubernetes nodes | 5-10 min | Auto-scaling |
| Reserved instances | 1-3 days | Procurement |
| GPU nodes | 1-7 days | Availability dependent |
| Storage expansion | 1-2 hours | Automated |
| Database scaling | 1-4 hours | Planned maintenance |
| New region | 2-4 weeks | Architecture review |

---

## 5. Cost Optimization

### 5.1 Cost by Resource

| Resource | Monthly Cost | % of Total | Optimization |
|----------|--------------|------------|--------------|
| Compute (EC2) | $45,000 | 50% | Reserved, Spot |
| Storage (S3) | $15,000 | 17% | Tiering |
| Database (RDS) | $8,000 | 9% | Right-sizing |
| Network | $5,000 | 6% | VPC endpoints |
| Other | $17,000 | 18% | Review |
| **Total** | **$90,000** | **100%** | |

### 5.2 Optimization Opportunities

| Opportunity | Estimated Savings | Effort | Priority |
|-------------|-------------------|--------|----------|
| Reserved instances (70%) | $15,000/mo | Low | High |
| Spot for training | $8,000/mo | Medium | High |
| Storage tiering | $3,000/mo | Low | Medium |
| Right-size idle resources | $5,000/mo | Medium | Medium |
| GPU sharing | $4,000/mo | High | Low |

---

## 6. Capacity Alerts

### 6.1 Alert Configuration

```yaml
# Prometheus alerts for capacity
groups:
- name: capacity-alerts
  rules:
  - alert: HighCPUUtilization
    expr: avg(node_cpu_utilization) > 0.85
    for: 15m
    labels:
      severity: warning
    annotations:
      summary: "High CPU utilization across cluster"
      
  - alert: StorageNearCapacity
    expr: (node_filesystem_size - node_filesystem_avail) / node_filesystem_size > 0.85
    for: 30m
    labels:
      severity: warning
    annotations:
      summary: "Storage utilization above 85%"
      
  - alert: CapacityPlanningThreshold
    expr: model_serving_replicas / model_serving_max_replicas > 0.8
    for: 1h
    labels:
      severity: info
    annotations:
      summary: "Model serving approaching max scale"
```

---

## 7. Reporting

### 7.1 Monthly Capacity Report Template

```markdown
## Monthly Capacity Report - [Month Year]

### Executive Summary
[Brief overview of capacity status]

### Resource Utilization

| Resource | Target | Actual | Status |
|----------|--------|--------|--------|
| Compute | 70% | [X]% | // |
| Storage | 70% | [X]% | // |
| Network | 60% | [X]% | // |

### Capacity Actions Taken
- [Action 1]
- [Action 2]

### Planned Capacity Changes
| Change | Date | Impact |
|--------|------|--------|
| [Change] | [Date] | [Impact] |

### Cost Summary
- Monthly spend: $[X]
- vs. Budget: [+/-]%
- Optimization savings: $[X]

### Risks & Recommendations
1. [Risk/Recommendation 1]
2. [Risk/Recommendation 2]
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial plan |
