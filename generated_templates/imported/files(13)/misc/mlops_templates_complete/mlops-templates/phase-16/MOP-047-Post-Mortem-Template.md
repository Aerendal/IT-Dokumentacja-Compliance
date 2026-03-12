---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-047: Incident Post-Mortem Template

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-047 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Priority** | HIGH |
| **Owner** | [MLOps SRE Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Annually) |

---

## Template Content

---

# Incident Post-Mortem

## Incident Information

| Field | Value |
|-------|-------|
| **Incident ID** | INC-[XXXX] |
| **Title** | [Brief descriptive title] |
| **Severity** | P[1/2/3/4] |
| **Date/Time** | [YYYY-MM-DD HH:MM UTC] |
| **Duration** | [X hours Y minutes] |
| **Author** | [Name] |
| **Post-Mortem Date** | [YYYY-MM-DD] |
| **Status** | Draft / Review / Final |

---

## Executive Summary

[2-3 paragraph summary covering: what happened, impact, root cause, and key actions]

---

## Impact Assessment

### User Impact

| Metric | Value |
|--------|-------|
| Users affected | [Number] |
| Requests failed | [Number/Percentage] |
| Error rate during incident | [Percentage] |
| Revenue impact | $[Amount] or N/A |

### Service Impact

| Service | Impact Level | Description |
|---------|--------------|-------------|
| Model Serving | Full outage / Degraded / None | [Details] |
| Feature Store | Full outage / Degraded / None | [Details] |
| Experiment Tracking | Full outage / Degraded / None | [Details] |

### Business Impact

- [Impact 1]
- [Impact 2]
- [Impact 3]

---

## Timeline

| Time (UTC) | Event | Actor |
|------------|-------|-------|
| HH:MM | [First indication of problem] | Monitoring |
| HH:MM | Alert fired: [Alert name] | PagerDuty |
| HH:MM | On-call engineer acknowledged | @engineer |
| HH:MM | Incident declared, IC assigned | @IC |
| HH:MM | [Investigation step] | @engineer |
| HH:MM | Root cause identified | @engineer |
| HH:MM | [Mitigation action taken] | @engineer |
| HH:MM | Service restored | @engineer |
| HH:MM | Incident resolved | @IC |
| HH:MM | Post-incident monitoring complete | @engineer |

---

## Root Cause Analysis

### What Happened

[Detailed technical description of what went wrong]

### Why It Happened

**5 Whys Analysis:**

1. **Why did [symptom] occur?**
   → Because [cause 1]

2. **Why did [cause 1] occur?**
   → Because [cause 2]

3. **Why did [cause 2] occur?**
   → Because [cause 3]

4. **Why did [cause 3] occur?**
   → Because [cause 4]

5. **Why did [cause 4] occur?**
   → Because [root cause]

**Root Cause:** [Clear statement of the underlying root cause]

### Contributing Factors

- [Factor 1]
- [Factor 2]
- [Factor 3]

---

## Detection & Response

### Detection

| Question | Answer |
|----------|--------|
| How was the incident detected? | [Alert/User report/Manual discovery] |
| How long before detection? | [Time from start to detection] |
| Were there earlier signals we missed? | [Yes/No - details] |

### Response

| Question | Answer |
|----------|--------|
| Time to acknowledge | [Minutes] |
| Time to mitigate | [Minutes/Hours] |
| Time to resolve | [Minutes/Hours] |
| Was the runbook followed? | [Yes/No/Partial] |
| Was escalation appropriate? | [Yes/No - details] |

---

## What Went Well

-  [Positive aspect 1]
-  [Positive aspect 2]
-  [Positive aspect 3]

---

## What Could Be Improved

-  [Improvement area 1]
-  [Improvement area 2]
-  [Improvement area 3]

---

## Action Items

### Immediate (This Sprint)

| ID | Action | Owner | Due Date | Status |
|----|--------|-------|----------|--------|
| AI-001 | [Action description] | @owner | [Date] | Open |
| AI-002 | [Action description] | @owner | [Date] | Open |

### Short-Term (This Quarter)

| ID | Action | Owner | Due Date | Status |
|----|--------|-------|----------|--------|
| AI-003 | [Action description] | @owner | [Date] | Open |
| AI-004 | [Action description] | @owner | [Date] | Open |

### Long-Term (Future Quarters)

| ID | Action | Owner | Target Quarter | Status |
|----|--------|-------|----------------|--------|
| AI-005 | [Action description] | @owner | Q[X] | Open |

---

## Prevention Measures

### Technical

- [ ] [Technical prevention measure 1]
- [ ] [Technical prevention measure 2]

### Process

- [ ] [Process improvement 1]
- [ ] [Process improvement 2]

### Monitoring

- [ ] [New alert or dashboard]
- [ ] [Improved detection]

---

## Appendix

### Relevant Logs

```
[Key log excerpts]
```

### Relevant Metrics/Graphs

[Screenshots or links to dashboards]

### Related Incidents

| Incident ID | Date | Relationship |
|-------------|------|--------------|
| INC-XXXX | [Date] | Similar root cause |

### References

- [Link to incident channel]
- [Link to runbook used]
- [Link to relevant documentation]

---

## Sign-Off

| Role | Name | Date |
|------|------|------|
| Author | | |
| Incident Commander | | |
| Engineering Manager | | |
| Stakeholder | | |

---

## Post-Mortem Meeting Notes

**Date:** [Date]
**Attendees:** [Names]

### Discussion Points

1. [Point 1]
2. [Point 2]

### Decisions Made

1. [Decision 1]
2. [Decision 2]

### Follow-Up Required

1. [Follow-up 1]
2. [Follow-up 2]
