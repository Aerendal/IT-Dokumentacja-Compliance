---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-095: Incident Communication Templates

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-095 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE / Communications] |

---

## 1. Communication Channels

| Channel | Use For | Audience |
|---------|---------|----------|
| #mlops-incidents | Real-time updates | Technical teams |
| Status Page | Public status | All users |
| Email | Major incidents | Leadership, affected teams |
| PagerDuty | On-call notification | Responders |

---

## 2. Incident Start Notification

### 2.1 Internal (Slack)

```markdown
 **INCIDENT STARTED** 

**Incident ID:** INC-XXXX
**Severity:** P1 / P2 / P3
**Started:** YYYY-MM-DD HH:MM UTC

**Summary:**
[Brief description of the issue]

**Impact:**
[What users/services are affected]

**Status:** Investigating

**Incident Commander:** @[name]
**Bridge:** #mlops-incident-XXXX

---
Updates will be posted every [X] minutes.
```

### 2.2 Status Page Update

```markdown
**Title:** [Service] Performance Degradation

**Status:** Investigating

**Message:**
We are currently investigating reports of [issue description]. 
Users may experience [symptoms]. 
Our team is actively working on resolving this issue.

**Affected Components:**
- Model Serving API
- Feature Store

**Posted:** YYYY-MM-DD HH:MM UTC
```

---

## 3. During Incident Updates

### 3.1 Regular Update Template

```markdown
 **INCIDENT UPDATE** - INC-XXXX

**Time:** YYYY-MM-DD HH:MM UTC
**Status:** Investigating / Identified / Monitoring / Resolved

**Update:**
[What has been discovered/done since last update]

**Current Actions:**
- [Action being taken]
- [Next steps]

**ETA:** [Expected resolution time or "Assessing"]

---
Next update in [X] minutes.
```

### 3.2 Mitigation Applied

```markdown
 **MITIGATION IN PROGRESS** - INC-XXXX

**Time:** YYYY-MM-DD HH:MM UTC

**Root Cause Identified:**
[Brief description of root cause]

**Mitigation:**
[What mitigation has been applied]

**Expected Impact:**
Users should begin seeing improvement within [X] minutes.

**Status:** Monitoring

---
We will continue monitoring and provide an update in [X] minutes.
```

---

## 4. Incident Resolution

### 4.1 Resolution Notification

```markdown
 **INCIDENT RESOLVED** - INC-XXXX

**Resolved:** YYYY-MM-DD HH:MM UTC
**Duration:** X hours X minutes

**Summary:**
[Brief description of what happened]

**Root Cause:**
[What caused the incident]

**Resolution:**
[How it was fixed]

**Impact:**
- Duration: [time]
- Users affected: [estimate]
- Services impacted: [list]

**Follow-up:**
- Post-mortem scheduled for [date]
- Tracking ticket: [link]

---
Thank you for your patience. Please reach out to #mlops-support with any questions.
```

### 4.2 Status Page Resolution

```markdown
**Title:** [Service] - Resolved

**Status:** Resolved

**Message:**
This incident has been resolved. [Service] is now operating normally.

**Summary:**
Between [start time] and [end time] UTC, users experienced [issue]. 
The root cause was [brief cause]. We have implemented [fix] to resolve the issue.

A detailed post-mortem will be published within 5 business days.

We apologize for any inconvenience caused.

**Posted:** YYYY-MM-DD HH:MM UTC
```

---

## 5. Executive Communication

### 5.1 Executive Summary (P1 Only)

```markdown
## Executive Incident Summary

**Incident:** INC-XXXX
**Date:** YYYY-MM-DD
**Duration:** X hours X minutes
**Severity:** P1 - Critical

### Business Impact
- [Revenue/customer impact if applicable]
- [Number of affected customers/transactions]
- [SLA implications]

### Summary
[2-3 sentence summary for executives]

### Root Cause
[Non-technical explanation]

### Resolution
[What was done to fix it]

### Prevention
[What will prevent recurrence]

### Timeline
| Time | Event |
|------|-------|
| HH:MM | Issue detected |
| HH:MM | Team engaged |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | Resolution confirmed |
```

---

## 6. Customer Communication

### 6.1 Customer Email (If Needed)

```markdown
Subject: [Service] Incident - [Date] - Resolved

Dear Customer,

We want to inform you about a service incident that occurred on [date].

**What Happened:**
Between [time] and [time] UTC, [brief description of issue]. 
During this time, you may have experienced [symptoms].

**Impact to You:**
[Specific impact to this customer if known]

**What We Did:**
Our team identified the issue and implemented [fix]. 
The service has been restored to normal operation.

**Prevention:**
We are implementing [measures] to prevent similar incidents.

We sincerely apologize for any inconvenience this may have caused. 
If you have any questions, please contact [support channel].

Sincerely,
[Team/Company Name]
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial communication templates |
