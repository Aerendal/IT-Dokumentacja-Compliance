---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-005: Quality Metrics Definition

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-005 |
| **Version** | 1.0 |
| **Owner** | QA Manager |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Requirements phase | Strategy defined |
| **Active** | Ongoing | Metrics tracked |
| **Review** | Quarterly | Effectiveness review |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| QA-003 Quality Objectives | Objective alignment |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-028 Quality Metrics Report | Reporting |
| QA-041 Quality Metrics Tracking | Monitoring |

---

## 1. PROCESS METRICS
| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Test Execution Rate | Executed / Total | 100% | Daily |
| Test Pass Rate | Passed / Executed | >95% | Daily |
| Automation Rate | Automated / Total | >70% | Sprint |

## 2. PRODUCT METRICS
| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Defect Density | Defects / KLOC | <5 | Release |
| Defect Escape Rate | Prod / Total bugs | <5% | Release |
| MTTR | Avg fix time | <4 hrs | Monthly |

## 3. TEAM METRICS
| Metric | Target | Measurement |
|--------|--------|-------------|
| Test Productivity | >10/day | Tests created |
| Defect Find Rate | Track | Defects/day |

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Manager | | | |
