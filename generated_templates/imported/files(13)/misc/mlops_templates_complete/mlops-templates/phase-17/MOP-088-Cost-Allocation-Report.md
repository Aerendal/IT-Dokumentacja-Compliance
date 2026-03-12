---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-088: Cost Allocation Report Template

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-088 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [FinOps / ML Platform Lead] |

---

## Monthly Cost Allocation Report

### Report Period: [Month Year]

---

## 1. Executive Summary

| Metric | Value | vs Budget | vs Last Month |
|--------|-------|-----------|---------------|
| Total Spend | $XX,XXX | +X% / -X% | +X% / -X% |
| Compute | $XX,XXX | | |
| Storage | $X,XXX | | |
| Services | $X,XXX | | |

**Key Highlights:**
- [Highlight 1]
- [Highlight 2]

---

## 2. Cost by Team

| Team | Compute | Storage | Services | Total | % of Total |
|------|---------|---------|----------|-------|------------|
| Fraud Detection | $X,XXX | $XXX | $XXX | $X,XXX | XX% |
| Recommendations | $X,XXX | $XXX | $XXX | $X,XXX | XX% |
| NLP | $X,XXX | $XXX | $XXX | $X,XXX | XX% |
| Platform/Shared | $X,XXX | $XXX | $XXX | $X,XXX | XX% |
| **Total** | **$XX,XXX** | **$X,XXX** | **$X,XXX** | **$XX,XXX** | **100%** |

---

## 3. Cost by Model

### Production Models

| Model | Tier | Compute | Inference/Day | Cost/1K Inferences |
|-------|------|---------|---------------|-------------------|
| fraud-detection-v2 | 1 | $X,XXX | X.XM | $X.XX |
| rec-engine-v3 | 2 | $X,XXX | X.XM | $X.XX |
| churn-predictor | 2 | $XXX | XXK | $X.XX |

### Training Costs

| Model | GPU Hours | Compute Cost | Experiments |
|-------|-----------|--------------|-------------|
| fraud-detection | XXX | $X,XXX | XX |
| rec-engine | XXX | $X,XXX | XX |

---

## 4. Resource Utilization

### Compute Efficiency

| Resource | Allocated | Used | Utilization |
|----------|-----------|------|-------------|
| CPU (cores) | XXX | XXX | XX% |
| Memory (GB) | X,XXX | XXX | XX% |
| GPU (units) | XX | XX | XX% |

### Optimization Opportunities

| Opportunity | Potential Savings | Effort |
|-------------|-------------------|--------|
| Right-size inference pods | $X,XXX/month | Low |
| Spot instances for training | $X,XXX/month | Medium |
| Storage tiering | $XXX/month | Low |

---

## 5. Cost Trends

### Month-over-Month

| Category | 3 Months Ago | 2 Months Ago | Last Month | This Month |
|----------|--------------|--------------|------------|------------|
| Compute | $XX,XXX | $XX,XXX | $XX,XXX | $XX,XXX |
| Storage | $X,XXX | $X,XXX | $X,XXX | $X,XXX |
| Total | $XX,XXX | $XX,XXX | $XX,XXX | $XX,XXX |

### Cost Growth Drivers
1. [Driver 1]
2. [Driver 2]

---

## 6. Budget Status

| Category | Annual Budget | YTD Spend | YTD Budget | Variance |
|----------|---------------|-----------|------------|----------|
| Compute | $XXX,XXX | $XX,XXX | $XX,XXX | +X% / -X% |
| Storage | $XX,XXX | $X,XXX | $X,XXX | +X% / -X% |
| Services | $XX,XXX | $X,XXX | $X,XXX | +X% / -X% |
| **Total** | **$XXX,XXX** | **$XX,XXX** | **$XX,XXX** | |

---

## 7. Recommendations

### Immediate Actions
- [ ] [Action 1]
- [ ] [Action 2]

### Next Month Focus
- [Focus area 1]
- [Focus area 2]

---

## Appendix: Detailed Breakdown

### A. Compute by Instance Type

| Instance Type | Hours | Cost | Usage |
|---------------|-------|------|-------|
| m5.xlarge | X,XXX | $X,XXX | Training |
| g4dn.xlarge | XXX | $X,XXX | GPU Training |
| c5.large | X,XXX | $X,XXX | Inference |

### B. Storage by Bucket

| Bucket | Size (GB) | Cost | Growth |
|--------|-----------|------|--------|
| mlops-artifacts | X,XXX | $XXX | +XX% |
| mlops-features | X,XXX | $XXX | +XX% |
| mlops-models | XXX | $XX | +XX% |

---

**Report Generated:** [Date]
**Next Report:** [Date]
