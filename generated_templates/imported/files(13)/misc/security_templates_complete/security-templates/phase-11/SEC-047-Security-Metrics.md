---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-047: Security Metrics

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-047 |
| **Version** | 1.0 |
| **Owner** | CISO |
| **NIST CSF** | GV.OC |

---

## 1. EXECUTIVE METRICS

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Risk Score | Weighted avg of risks | <3.0 | Monthly |
| Compliance % | Controls met / total | >95% | Quarterly |
| Incident Rate | Incidents / month | <5 | Monthly |
| MTTR | Avg resolution time | <4h | Monthly |

## 2. OPERATIONAL METRICS

| Category | Metric | Target |
|----------|--------|--------|
| Vulnerability | Critical vuln count | 0 |
| Vulnerability | Patch compliance % | >98% |
| Access | Orphan accounts | 0 |
| Training | Completion rate | 100% |
| Phishing | Click rate | <5% |

## 3. TECHNICAL METRICS

| Metric | Source | Target |
|--------|--------|--------|
| EDR coverage | EDR console | 100% |
| MFA adoption | IdP | 100% |
| Encryption coverage | Scan results | 100% |
| Log ingestion | SIEM | 100% sources |
