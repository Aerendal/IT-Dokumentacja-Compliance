---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-073: Resource Allocation Plan

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-073 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead / Finance] |

---

## 1. Resource Categories

### 1.1 Resource Types

| Category | Resources | Cost Driver |
|----------|-----------|-------------|
| Compute | CPU, GPU, Memory | Instance hours |
| Storage | S3, EBS, Database | GB-months |
| Network | Data transfer, Load balancers | GB transferred |
| Services | MLflow, Feast, Monitoring | Service usage |
| Human | Engineers, Data Scientists | FTE |

---

## 2. Team Resource Allocation

### 2.1 Team Structure

| Role | Count | Allocation |
|------|-------|------------|
| ML Platform Lead | 1 | 100% MLOps |
| Sr. ML Engineer | 2 | 100% MLOps |
| ML Engineer | 3 | 100% MLOps |
| MLOps SRE | 2 | 100% MLOps |
| Data Engineer | 2 | 50% MLOps |
| **Total FTE** | **9** | |

### 2.2 Time Allocation

| Activity | % Time | Hours/Sprint |
|----------|--------|--------------|
| Development | 40% | 64h |
| Operations | 25% | 40h |
| Support | 15% | 24h |
| Planning | 10% | 16h |
| Training | 10% | 16h |

---

## 3. Compute Resource Allocation

### 3.1 Environment Allocation

| Environment | CPU (cores) | Memory (GB) | GPU | Monthly Cost |
|-------------|-------------|-------------|-----|--------------|
| Development | 100 | 400 | 2 | $5,000 |
| Staging | 50 | 200 | 1 | $3,000 |
| Production | 200 | 800 | 8 | $25,000 |
| Training | 100 | 400 | 16 | $15,000 |
| **Total** | **450** | **1,800** | **27** | **$48,000** |

### 3.2 Team Quotas

```yaml
# k8s/resource-quotas.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-fraud-quota
  namespace: fraud-team
spec:
  hard:
    requests.cpu: "50"
    requests.memory: "200Gi"
    requests.nvidia.com/gpu: "4"
    limits.cpu: "100"
    limits.memory: "400Gi"
    limits.nvidia.com/gpu: "4"
    persistentvolumeclaims: "10"
    
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-recommendation-quota
  namespace: recommendation-team
spec:
  hard:
    requests.cpu: "30"
    requests.memory: "120Gi"
    requests.nvidia.com/gpu: "2"
```

### 3.3 Priority Classes

```yaml
# k8s/priority-classes.yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: production-serving
value: 1000000
globalDefault: false
description: "Production model serving - highest priority"

---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: scheduled-training
value: 100000
description: "Scheduled training jobs"

---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: development
value: 10000
description: "Development and experimentation"
```

---

## 4. Storage Allocation

### 4.1 Storage Budget

| Storage Type | Allocated | Unit Cost | Monthly |
|--------------|-----------|-----------|---------|
| S3 Standard | 10 TB | $0.023/GB | $230 |
| S3 IA | 20 TB | $0.0125/GB | $250 |
| S3 Glacier | 50 TB | $0.004/GB | $200 |
| EBS (gp3) | 2 TB | $0.08/GB | $160 |
| RDS Storage | 500 GB | $0.115/GB | $58 |
| Redis | 50 GB | $0.10/GB | $5 |
| **Total** | | | **$903** |

### 4.2 Team Storage Quotas

| Team | S3 Quota | EBS Quota |
|------|----------|-----------|
| Fraud Detection | 5 TB | 500 GB |
| Recommendations | 3 TB | 300 GB |
| NLP | 2 TB | 200 GB |
| Shared/Platform | 20 TB | 1 TB |

---

## 5. GPU Allocation Strategy

### 5.1 GPU Pool

| GPU Type | Count | Primary Use |
|----------|-------|-------------|
| A100 (80GB) | 4 | Large model training |
| A10G (24GB) | 8 | Inference, fine-tuning |
| T4 (16GB) | 8 | Development, small training |
| **Total** | **20** | |

### 5.2 GPU Scheduling

```yaml
# GPU time allocation
scheduling:
  production_inference:
    gpus: 8
    priority: highest
    preemptible: false
    
  scheduled_training:
    gpus: 8
    priority: high
    time_window: "00:00-08:00 UTC"
    preemptible: false
    
  on_demand_training:
    gpus: 4
    priority: medium
    preemptible: true
    max_duration: 8h
```

---

## 6. Budget Allocation

### 6.1 Annual Budget

| Category | Q1 | Q2 | Q3 | Q4 | Annual |
|----------|----|----|----|----|--------|
| Compute | $144K | $150K | $156K | $162K | $612K |
| Storage | $36K | $40K | $44K | $48K | $168K |
| Services | $24K | $24K | $24K | $24K | $96K |
| Training | $12K | $12K | $12K | $12K | $48K |
| Contingency | $12K | $12K | $12K | $12K | $48K |
| **Total** | **$228K** | **$238K** | **$248K** | **$258K** | **$972K** |

### 6.2 Cost Allocation by Team

| Team | % Budget | Monthly |
|------|----------|---------|
| Platform/Shared | 40% | $32,400 |
| Fraud Detection | 25% | $20,250 |
| Recommendations | 20% | $16,200 |
| NLP/Other | 15% | $12,150 |

---

## 7. Allocation Requests

### 7.1 Request Process

```markdown
## Resource Allocation Request

**Requestor:** ___________
**Team:** ___________
**Date:** ___________

### Request Details
| Resource | Current | Requested | Duration |
|----------|---------|-----------|----------|
| CPU | 20 cores | 40 cores | 3 months |
| Memory | 80 GB | 160 GB | 3 months |
| GPU | 1 | 4 | 2 weeks |

### Justification
[Explain why additional resources are needed]

### Expected Outcome
[What will be achieved with additional resources]

### Approval
- [ ] Team Lead
- [ ] Platform Lead
- [ ] Finance (if >$5K/month)
```

---

## 8. Monitoring & Adjustment

### 8.1 Review Cycle

| Review | Frequency | Participants |
|--------|-----------|--------------|
| Usage Review | Weekly | Team Leads |
| Allocation Review | Monthly | Platform Lead |
| Budget Review | Quarterly | Finance + Leadership |

### 8.2 Adjustment Triggers

| Trigger | Action |
|---------|--------|
| Utilization <50% for 2 weeks | Reduce allocation |
| Utilization >90% for 1 week | Review for increase |
| Budget variance >10% | Finance review |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial resource plan |
