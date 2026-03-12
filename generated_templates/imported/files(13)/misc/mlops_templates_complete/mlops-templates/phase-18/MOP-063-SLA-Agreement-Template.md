---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-063: SLA Agreement Template

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-063 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Procurement / Legal] |

---

# Service Level Agreement (SLA)

## Agreement Information
| Field | Value |
|-------|-------|
| **Agreement ID** | SLA-[YYYY]-[XXX] |
| **Vendor** | [Vendor Name] |
| **Service** | [Service Name] |
| **Effective Date** | [Date] |
| **Term** | [Duration] |

---

## 1. Service Description

### 1.1 Services Covered
| Service | Description |
|---------|-------------|
| [Service 1] | [Description] |
| [Service 2] | [Description] |

### 1.2 Services Excluded
- [Excluded item 1]
- [Excluded item 2]

---

## 2. Service Level Objectives (SLOs)

### 2.1 Availability

| Metric | Target | Measurement |
|--------|--------|-------------|
| Monthly Uptime | 99.9% | (Total - Downtime) / Total |
| Scheduled Maintenance | <4 hours/month | Advance notice required |

**Uptime Calculation:**
```
Uptime % = ((Total Minutes - Downtime Minutes) / Total Minutes) × 100
```

### 2.2 Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| API Response Time P50 | <100ms | 50th percentile |
| API Response Time P99 | <500ms | 99th percentile |
| Throughput | >1000 RPS | Requests per second |

### 2.3 Support Response Times

| Priority | Description | Response Time | Resolution Time |
|----------|-------------|---------------|-----------------|
| P1 - Critical | Service down | 15 minutes | 4 hours |
| P2 - High | Major degradation | 1 hour | 8 hours |
| P3 - Medium | Minor issue | 4 hours | 24 hours |
| P4 - Low | General inquiry | 24 hours | 5 business days |

---

## 3. Service Credits

### 3.1 Credit Schedule

| Monthly Uptime | Service Credit |
|----------------|----------------|
| 99.9% - 99.5% | 10% of monthly fee |
| 99.5% - 99.0% | 25% of monthly fee |
| 99.0% - 95.0% | 50% of monthly fee |
| Below 95.0% | 100% of monthly fee |

### 3.2 Credit Claim Process
1. Customer must request credit within 30 days
2. Provide incident details and timestamps
3. Vendor verifies against monitoring data
4. Credit applied to next invoice

### 3.3 Credit Exclusions
- Scheduled maintenance (with advance notice)
- Customer-caused issues
- Force majeure events
- Third-party service failures

---

## 4. Monitoring & Reporting

### 4.1 Monitoring
- Vendor provides real-time status page
- Customer has access to monitoring dashboard
- Automated alerts for SLA breaches

### 4.2 Reporting

| Report | Frequency | Contents |
|--------|-----------|----------|
| Availability Report | Monthly | Uptime, incidents |
| Performance Report | Monthly | Latency, throughput |
| Incident Summary | Monthly | Incidents, RCA |
| Quarterly Review | Quarterly | Trends, improvements |

---

## 5. Incident Management

### 5.1 Incident Classification

| Priority | Impact | Examples |
|----------|--------|----------|
| P1 | Complete service unavailable | Platform down |
| P2 | Major feature unavailable | API errors >10% |
| P3 | Minor feature impacted | Slow performance |
| P4 | Minimal impact | UI bug |

### 5.2 Communication
- P1/P2: Updates every 30 minutes
- P3: Updates every 2 hours
- Post-incident RCA within 5 business days for P1/P2

---

## 6. Maintenance

### 6.1 Scheduled Maintenance
- Advance notice: 7 days (standard), 72 hours (urgent)
- Preferred window: [Day] [Time] UTC
- Maximum duration: 4 hours/month

### 6.2 Emergency Maintenance
- Notification: As soon as possible
- For critical security or stability issues only

---

## 7. Escalation Path

| Level | Contact | Timeframe |
|-------|---------|-----------|
| L1 | Support Team | Initial contact |
| L2 | Support Manager | After 2 hours (P1) |
| L3 | Account Manager | After 4 hours (P1) |
| L4 | VP Customer Success | After 8 hours (P1) |

---

## 8. Term & Termination

### 8.1 SLA Review
- Annual review of SLO targets
- Adjustments require mutual agreement

### 8.2 Termination Rights
- Customer may terminate if SLA <95% for 3 consecutive months
- 30-day notice required

---

## 9. Signatures

| Party | Name | Title | Signature | Date |
|-------|------|-------|-----------|------|
| Customer | | | | |
| Vendor | | | | |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial SLA |
