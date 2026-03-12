---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-043: Incident Classification and Severity

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-043 |
| **Version** | 1.0 |
| **Owner** | IR Lead |
| **NIST CSF** | RS.AN |

---

## 1. SEVERITY MATRIX

| Severity | Business Impact | Data Impact | Response |
|----------|-----------------|-------------|----------|
| **SEV-1** | Critical systems down | PII/sensitive breach confirmed | 15 min |
| **SEV-2** | Major service degradation | Potential data exposure | 1 hour |
| **SEV-3** | Limited impact | Internal data only | 4 hours |
| **SEV-4** | Minimal impact | No data impact | 24 hours |

## 2. INCIDENT CATEGORIES

| Category | Examples | Typical Severity |
|----------|----------|------------------|
| Malware | Ransomware, trojan, worm | SEV-1 to SEV-3 |
| Unauthorized Access | Account compromise, intrusion | SEV-1 to SEV-2 |
| Data Breach | Exfiltration, exposure | SEV-1 to SEV-2 |
| DoS/DDoS | Service disruption | SEV-2 to SEV-3 |
| Policy Violation | Acceptable use breach | SEV-3 to SEV-4 |

## 3. ESCALATION MATRIX

| Severity | Notify Within | Stakeholders |
|----------|---------------|--------------|
| SEV-1 | 15 min | CISO, CIO, Legal, CEO |
| SEV-2 | 1 hour | CISO, IT Director |
| SEV-3 | 4 hours | Security Manager |
| SEV-4 | 24 hours | Team Lead |
