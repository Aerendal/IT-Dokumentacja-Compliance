---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-049: MLOps Budget & Cost Management

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-049 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [ML Platform Lead / Finance Partner] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-013: Roadmap | Timeline |
| MOP-014: Tool Evaluation | Tool costs |
| MOP-015: Team Structure | Personnel costs |
| MOP-006: Scalability | Capacity projections |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-051: Status Reports | Cost tracking |
| Executive Reports | Budget status |

---

## Template Content

---

# MLOps Budget & Cost Management Plan

## 1. Budget Overview

### 1.1 Total Budget Summary

| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| **Infrastructure** | $280,000 | $350,000 | $420,000 | $1,050,000 |
| **Personnel** | $800,000 | $1,200,000 | $1,500,000 | $3,500,000 |
| **Tools & Licensing** | $25,000 | $40,000 | $60,000 | $125,000 |
| **Training** | $50,000 | $30,000 | $20,000 | $100,000 |
| **Consulting** | $100,000 | $50,000 | $25,000 | $175,000 |
| **Contingency (10%)** | $125,500 | $167,000 | $202,500 | $495,000 |
| **TOTAL** | $1,380,500 | $1,837,000 | $2,227,500 | $5,445,000 |

### 1.2 Budget by Phase

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Budget Allocation by Phase                        │
│                                                                     │
│  Phase 1: Foundation (M1-6)                    ████████░░ $450K    │
│  Phase 2: Core Platform (M7-12)               ██████████░ $550K    │
│  Phase 3: Advanced Features (M13-18)          ████████░░░ $380K    │
│                                                                     │
│  Ongoing Operations (Annual)                  ████████████ $600K+  │
│                                                                     │
│  Legend: █ = $50K                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Infrastructure Costs

### 2.1 Compute Costs

| Resource | Specification | Monthly | Annual |
|----------|---------------|---------|--------|
| **Kubernetes (EKS)** | | | |
| Control plane | 2 clusters | $146 | $1,752 |
| Worker nodes (CPU) | 10 × m6i.xlarge | $1,400 | $16,800 |
| Worker nodes (GPU) | 4 × g5.xlarge | $4,400 | $52,800 |
| **Model Serving** | | | |
| Inference (CPU) | 20 × c6i.xlarge | $2,800 | $33,600 |
| Inference (GPU) | 8 × g5.xlarge | $8,800 | $105,600 |
| **Training** | | | |
| On-demand GPU | Variable | $3,000 | $36,000 |
| Spot instances | Variable | $1,000 | $12,000 |
| **Subtotal** | | **$21,546** | **$258,552** |

### 2.2 Storage Costs

| Service | Size | Monthly | Annual |
|---------|------|---------|--------|
| S3 (artifacts) | 10 TB | $230 | $2,760 |
| S3 (features offline) | 50 TB | $1,150 | $13,800 |
| EBS (persistent) | 5 TB | $500 | $6,000 |
| RDS PostgreSQL | db.r6g.xlarge | $500 | $6,000 |
| ElastiCache Redis | 6 nodes | $1,200 | $14,400 |
| **Subtotal** | | **$3,580** | **$42,960** |

### 2.3 Network & Data Transfer

| Service | Usage | Monthly | Annual |
|---------|-------|---------|--------|
| NAT Gateway | 2 AZs | $90 | $1,080 |
| Data transfer | 5 TB | $450 | $5,400 |
| Load Balancer | 3 ALBs | $60 | $720 |
| **Subtotal** | | **$600** | **$7,200** |

---

## 3. Personnel Costs

### 3.1 Team Costs by Role

| Role | Level | Count Y1 | Count Y2 | Count Y3 | Annual Cost/Person |
|------|-------|----------|----------|----------|-------------------|
| ML Platform Lead | L6 | 1 | 1 | 1 | $220,000 |
| Sr ML Platform Eng | L5 | 2 | 3 | 4 | $180,000 |
| ML Platform Eng | L4 | 1 | 2 | 3 | $150,000 |
| MLOps/SRE | L5 | 1 | 2 | 2 | $175,000 |
| ML Quality Eng | L4 | 1 | 1 | 2 | $155,000 |
| **Total FTE** | | **6** | **9** | **12** | |
| **Total Cost** | | **$1,010,000** | **$1,515,000** | **$2,020,000** | |

### 3.2 Hiring Timeline

| Quarter | Hires | Roles | Recruiting Cost |
|---------|-------|-------|-----------------|
| Q1 Y1 | 3 | Lead, Sr Eng, SRE | $45,000 |
| Q2 Y1 | 2 | Eng, Quality | $30,000 |
| Q3 Y1 | 1 | Sr Eng | $15,000 |
| Q1 Y2 | 2 | Sr Eng, SRE | $30,000 |
| Q3 Y2 | 1 | Eng | $15,000 |
| Y3 | 3 | Various | $45,000 |

---

## 4. Tools & Licensing

### 4.1 Open Source Tools (No License Cost)

| Tool | License | Support Option | Annual Support |
|------|---------|----------------|----------------|
| MLflow | Apache 2.0 | Community | $0 |
| Feast | Apache 2.0 | Community | $0 |
| Triton | BSD-3 | NVIDIA Enterprise | $10,000 |
| Prometheus | Apache 2.0 | Community | $0 |
| Grafana | AGPL 3.0 | Grafana Cloud | $5,000 |

### 4.2 Commercial Tools

| Tool | Purpose | Annual Cost |
|------|---------|-------------|
| Evidently (Cloud) | ML Monitoring | $12,000 |
| PagerDuty | Alerting | $3,000 |
| Datadog (optional) | APM | $15,000 |
| GitHub Enterprise | CI/CD | Existing |
| **Total** | | **$25,000-$45,000** |

---

## 5. Cost Optimization Strategies

### 5.1 Infrastructure Optimization

| Strategy | Potential Savings | Implementation |
|----------|-------------------|----------------|
| Reserved Instances (1yr) | 30-40% | Commit to baseline |
| Spot Instances (training) | 60-70% | Fault-tolerant workloads |
| Right-sizing | 20-30% | Quarterly review |
| Auto-scaling | 15-25% | Scale to zero when idle |
| Storage tiering | 10-20% | Move old data to Glacier |

### 5.2 Savings Projections

| Optimization | Year 1 | Year 2 | Year 3 |
|--------------|--------|--------|--------|
| Reserved instances | $30,000 | $50,000 | $70,000 |
| Spot instances | $20,000 | $35,000 | $50,000 |
| Right-sizing | $10,000 | $20,000 | $30,000 |
| **Total Savings** | **$60,000** | **$105,000** | **$150,000** |

---

## 6. Cost Allocation

### 6.1 Chargeback Model

| Cost Type | Allocation Method | Metric |
|-----------|-------------------|--------|
| Shared platform | Per team headcount | % of ML users |
| Model serving | Per model | Inference requests |
| Training compute | Direct | GPU hours used |
| Storage | Direct | GB stored |
| Feature store | Per feature | Feature retrieval calls |

### 6.2 Team Cost Breakdown Template

```markdown
## Monthly Cost Report - [Team Name]

| Category | Usage | Rate | Cost |
|----------|-------|------|------|
| Platform share | 10% of 50 users | $500/user | $500 |
| Model serving | 1M requests | $0.50/1K | $500 |
| Training | 100 GPU hours | $2/hour | $200 |
| Storage | 500 GB | $0.10/GB | $50 |
| **Total** | | | **$1,250** |
```

---

## 7. Budget Tracking

### 7.1 Monthly Tracking Template

| Category | Budget | Actual | Variance | YTD Budget | YTD Actual |
|----------|--------|--------|----------|------------|------------|
| Infrastructure | $25,000 | $24,500 | +$500 | $150,000 | $147,000 |
| Personnel | $85,000 | $85,000 | $0 | $510,000 | $510,000 |
| Tools | $3,000 | $2,800 | +$200 | $18,000 | $16,800 |
| Training | $5,000 | $6,500 | -$1,500 | $30,000 | $31,000 |
| **Total** | **$118,000** | **$118,800** | **-$800** | **$708,000** | **$704,800** |

### 7.2 Alerting Thresholds

| Threshold | Action |
|-----------|--------|
| >90% monthly budget | Alert to team lead |
| >100% monthly budget | Escalate to manager |
| >110% monthly budget | Escalate to director |
| Projected overage >5% | Quarterly review trigger |

---

## 8. ROI Analysis

### 8.1 Expected Benefits

| Benefit | Metric | Before | After | Value |
|---------|--------|--------|-------|-------|
| Deployment time | Days | 14 | 1 | Save 13 days/model |
| Model failures | % | 15% | 2% | Reduce incidents |
| Engineer productivity | Models/quarter | 2 | 8 | 4x improvement |
| Infrastructure utilization | % | 30% | 70% | 2.3x efficiency |

### 8.2 ROI Calculation

```
Investment (3 years): $5,445,000

Benefits:
- Reduced deployment time: 50 models × 13 days × $500/day = $325,000/year
- Fewer incidents: 100 incidents × $5,000/incident × 80% reduction = $400,000/year
- Productivity gains: 10 engineers × $50,000 value/year = $500,000/year
- Infrastructure savings: $150,000/year (Year 3)

Total Annual Benefits (Year 3): $1,375,000

Payback Period: ~3.5 years
3-Year ROI: (($1,375,000 × 3) - $5,445,000) / $5,445,000 = -24%
5-Year ROI: (($1,375,000 × 5) - $5,445,000) / $5,445,000 = +26%
```

---

## 9. Approval & Governance

### 9.1 Approval Matrix

| Spend Type | Amount | Approver |
|------------|--------|----------|
| Within budget | Any | Team Lead |
| Over budget <10% | <$10K | Manager |
| Over budget >10% | Any | Director |
| New tool/vendor | Any | Director + Procurement |
| Headcount | Any | VP + HR |

### 9.2 Review Cadence

| Review | Frequency | Participants |
|--------|-----------|--------------|
| Spend review | Weekly | Team lead |
| Budget review | Monthly | Manager + Finance |
| Forecast update | Quarterly | Director + Finance |
| Annual planning | Yearly | VP + Finance |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial budget plan |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Lead | | | |
| Finance Partner | | | |
| Engineering Director | | | |
