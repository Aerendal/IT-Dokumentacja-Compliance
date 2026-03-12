---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-006: Cloud Cost-Benefit Analysis

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-006 |
| **Version** | 1.0 |
| **Status** | DRAFT / APPROVED |
| **Owner** | [Cloud Architect / Finance] |

---

## 1. Executive Summary

| Metric | Current (On-Prem) | Cloud (Year 3) | Savings |
|--------|-------------------|----------------|---------|
| Annual Infrastructure Cost | $X,XXX,XXX | $X,XXX,XXX | XX% |
| TCO (5 Years) | $X,XXX,XXX | $X,XXX,XXX | $X,XXX,XXX |
| Break-even Point | - | Month XX | - |
| ROI | - | XXX% | - |

---

## 2. Current State Costs (On-Premise)

### 2.1 CapEx - Capital Expenditure

| Category | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|----------|--------|--------|--------|--------|--------|
| Hardware Refresh | $500K | - | - | $500K | - |
| Network Equipment | $100K | - | - | $100K | - |
| Storage Expansion | $200K | $100K | $100K | $200K | $100K |
| Data Center Upgrades | $150K | - | - | $150K | - |
| **Total CapEx** | **$950K** | **$100K** | **$100K** | **$950K** | **$100K** |

### 2.2 OpEx - Operating Expenditure

| Category | Annual Cost | Notes |
|----------|-------------|-------|
| Data Center (Space, Power, Cooling) | $300,000 | 500 sq ft, 200 kW |
| Hardware Maintenance | $150,000 | 15% of hardware value |
| Software Licenses | $200,000 | VMware, Windows, etc. |
| Network Costs | $100,000 | Circuits, firewalls |
| Personnel (Infrastructure) | $600,000 | 4 FTEs × $150K |
| Disaster Recovery Site | $200,000 | Secondary DC costs |
| **Total Annual OpEx** | **$1,550,000** | |

### 2.3 Hidden Costs

| Category | Estimated Cost | Description |
|----------|----------------|-------------|
| Downtime Cost | $50,000/year | 10 hours × $5,000/hour |
| Opportunity Cost | $200,000/year | Delayed projects |
| Technical Debt | $100,000/year | Legacy system maintenance |
| **Total Hidden Costs** | **$350,000/year** | |

---

## 3. Cloud Costs Projection

### 3.1 Migration Costs (One-time)

| Category | Cost | Notes |
|----------|------|-------|
| Migration Services | $200,000 | Professional services |
| Training | $50,000 | Team upskilling |
| Parallel Running | $100,000 | 3 months overlap |
| Testing & Validation | $50,000 | Performance, security |
| **Total Migration** | **$400,000** | |

### 3.2 Cloud Operating Costs

| Service | Monthly | Year 1 | Year 2 | Year 3 |
|---------|---------|--------|--------|--------|
| Compute (EC2/VMs) | $30,000 | $360,000 | $340,000 | $320,000 |
| Storage (S3/EBS) | $10,000 | $120,000 | $130,000 | $140,000 |
| Database (RDS) | $15,000 | $180,000 | $180,000 | $180,000 |
| Networking | $5,000 | $60,000 | $65,000 | $70,000 |
| Security Services | $3,000 | $36,000 | $36,000 | $36,000 |
| Monitoring | $2,000 | $24,000 | $24,000 | $24,000 |
| Support (Enterprise) | $8,000 | $96,000 | $96,000 | $96,000 |
| **Total Cloud** | **$73,000** | **$876,000** | **$871,000** | **$866,000** |

### 3.3 Cost Optimization Assumptions

| Optimization | Savings | Timeline |
|--------------|---------|----------|
| Reserved Instances (1yr) | 30% on compute | Year 1 |
| Right-sizing | 15% reduction | Ongoing |
| Auto-scaling | 20% off-hours savings | Year 1 |
| Spot Instances (Dev/Test) | 70% savings | Year 1 |

---

## 4. Total Cost of Ownership (TCO)

### 4.1 5-Year TCO Comparison

| Year | On-Premise | Cloud | Difference |
|------|------------|-------|------------|
| Year 1 | $2,500,000 | $1,276,000 | -$1,224,000 |
| Year 2 | $1,650,000 | $871,000 | -$779,000 |
| Year 3 | $1,650,000 | $866,000 | -$784,000 |
| Year 4 | $2,500,000 | $860,000 | -$1,640,000 |
| Year 5 | $1,650,000 | $855,000 | -$795,000 |
| **5-Year Total** | **$9,950,000** | **$4,728,000** | **-$5,222,000** |

### 4.2 TCO Chart

```
TCO Comparison ($ thousands)
│
$3M │  ████                    ████
    │  ████                    ████
$2M │  ████  ░░░░  ░░░░        ████  ░░░░
    │  ████  ░░░░  ░░░░        ████  ░░░░
$1M │  ████  ░░░░  ░░░░  ░░░░  ████  ░░░░  ░░░░  ░░░░
    │  ████  ░░░░  ░░░░  ░░░░  ████  ░░░░  ░░░░  ░░░░
  0 └──Year1──Year2──Year3──Year4──Year5───────────────
    
    ████ On-Premise    ░░░░ Cloud
```

---

## 5. Qualitative Benefits

| Benefit | Impact | Value |
|---------|--------|-------|
| Faster Time-to-Market | Deploy in days vs weeks | Competitive advantage |
| Scalability | Handle 10x traffic spikes | Revenue protection |
| Innovation | Access to AI/ML services | New capabilities |
| Global Reach | Multi-region deployment | Market expansion |
| Reliability | 99.99% availability | Customer satisfaction |
| Security | Enterprise-grade security | Risk reduction |

---

## 6. Risk-Adjusted Analysis

| Risk | Probability | Impact | Mitigation Cost |
|------|-------------|--------|-----------------|
| Cost Overrun | 30% | +20% costs | $50K (FinOps) |
| Migration Delays | 40% | +3 months | $100K (buffer) |
| Performance Issues | 20% | $200K rework | $30K (POC) |

**Risk-Adjusted Cloud TCO:** $4,728,000 + $180,000 = **$4,908,000**

---

## 7. Recommendation

**Recommendation:**  PROCEED with cloud migration

**Justification:**
1. 5-year savings of **$5.2M** (52% reduction)
2. Break-even in **Month 8**
3. ROI of **110%** over 5 years
4. Strategic benefits (agility, innovation)

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial cost-benefit analysis |
