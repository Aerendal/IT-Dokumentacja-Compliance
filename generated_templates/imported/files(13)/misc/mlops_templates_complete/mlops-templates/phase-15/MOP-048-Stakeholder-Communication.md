---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-048: Stakeholder Communication Templates

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-048 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead / PMO] |

---

## 1. Communication Matrix

### 1.1 Stakeholder Groups

| Group | Interest | Frequency | Channel |
|-------|----------|-----------|---------|
| Executive Leadership | ROI, strategic alignment | Monthly | Executive summary |
| Business Units | Model availability, performance | Bi-weekly | Status email |
| Engineering Teams | Technical updates, changes | Weekly | Slack/Email |
| Data Science Teams | Features, capabilities | Weekly | Team meetings |
| Security/Compliance | Risk, compliance status | Monthly | Report |

### 1.2 Communication Types

| Type | Audience | Trigger |
|------|----------|---------|
| Status Update | All stakeholders | Scheduled |
| Change Notice | Affected teams | Before changes |
| Incident Report | Leadership, affected | After incidents |
| Release Notes | Technical teams | On release |
| Announcement | All | Major milestones |

---

## 2. Status Update Template

### 2.1 Bi-Weekly Status Email

```markdown
Subject: MLOps Platform Status Update - [Date Range]

## Executive Summary
[2-3 sentence high-level summary]

## Platform Health
| Metric | Status | Trend |
|--------|--------|-------|
| Availability | 99.95% |  |
| Active Models | 47 | ↑ +3 |
| Inference Latency (P99) | 45ms | ↓ improved |

## Key Accomplishments
-  [Accomplishment 1]
-  [Accomplishment 2]

## In Progress
-  [Initiative 1] - 75% complete
-  [Initiative 2] - 50% complete

## Upcoming
-  [Upcoming item 1] - [Date]
-  [Upcoming item 2] - [Date]

## Needs Attention
-  [Issue requiring attention]

## Metrics Snapshot
- Models deployed this period: X
- Experiments run: X
- Feature store queries: X M

---
Questions? Contact #mlops-support
```

---

## 3. Change Notice Template

### 3.1 Planned Change Notice

```markdown
Subject: [CHANGE NOTICE] MLOps Platform - [Change Title]

## Change Summary
**What:** [Brief description of change]
**When:** [Date and time with timezone]
**Duration:** [Expected duration]
**Impact:** [Who/what is affected]

## Details
[Detailed description of the change]

## User Impact
| Component | Impact | Action Required |
|-----------|--------|-----------------|
| [Component] | [Impact level] | [What users need to do] |

## Timeline
| Time | Activity |
|------|----------|
| [Time] | Change begins |
| [Time] | [Milestone] |
| [Time] | Change complete |

## What You Need to Do
1. [Action item 1]
2. [Action item 2]

## Rollback Plan
If issues occur, we will [rollback procedure].

## Contact
- Questions: #mlops-support
- During change: [On-call contact]

---
This change was approved via RFC-[number]
```

### 3.2 Emergency Change Notice

```markdown
Subject: [URGENT] MLOps Platform Emergency Change - [Title]

## Emergency Change
**What:** [Brief description]
**When:** IMMEDIATELY
**Reason:** [Why this is urgent]

## Impact
[Who/what is affected and how]

## Actions Being Taken
1. [Action 1]
2. [Action 2]

## Expected Resolution
[When we expect this to be resolved]

## Updates
Updates will be posted to:
- Slack: #mlops-incidents
- Status page: status.mlops.company.com

---
Emergency contact: [Phone/Slack]
```

---

## 4. Incident Communication Template

### 4.1 Incident Notification

```markdown
Subject: [INCIDENT] MLOps Platform - [Severity] - [Brief Title]

## Incident Summary
**Status:** Investigating / Identified / Monitoring / Resolved
**Severity:** P1/P2/P3/P4
**Started:** [DateTime]
**Duration:** [Ongoing / X hours]

## Impact
[Description of user/business impact]

## Affected Services
- [Service 1]
- [Service 2]

## Current Status
[What we know and what we're doing]

## Next Update
Expected at [Time] or when status changes.

---
Follow updates: #mlops-incidents
```

### 4.2 Incident Resolution Notice

```markdown
Subject: [RESOLVED] MLOps Platform Incident - [Title]

## Resolution Summary
**Incident:** [Title]
**Duration:** [Start] to [End] ([Total time])
**Root Cause:** [Brief root cause]

## Impact Summary
- Users affected: [Number/percentage]
- Services impacted: [List]
- Data impact: [None / Description]

## Resolution
[What was done to fix the issue]

## Prevention
[What we're doing to prevent recurrence]

## Post-Mortem
Full post-mortem available: [Link]

---
Questions: Contact [ML Platform Lead]
```

---

## 5. Release Notes Template

```markdown
# MLOps Platform Release Notes - v[X.Y.Z]

**Release Date:** [Date]
**Release Type:** Major / Minor / Patch

## Highlights
[2-3 bullet points of most important changes]

## New Features
### [Feature Name]
[Description of feature and how to use it]

### [Feature Name]
[Description]

## Improvements
- [Improvement 1]
- [Improvement 2]

## Bug Fixes
- Fixed: [Bug description] (#ISSUE-123)
- Fixed: [Bug description] (#ISSUE-456)

## Breaking Changes
 **[Change description]**
- Impact: [Who is affected]
- Migration: [What users need to do]

## Deprecations
- [Feature] is deprecated and will be removed in v[X.Y]

## Known Issues
- [Issue description] - Workaround: [workaround]

## Upgrade Instructions
```bash
# Commands to upgrade
```

## Documentation
- [Link to updated docs]
- [Link to migration guide]

---
Full changelog: [Link]
```

---

## 6. Announcement Template

```markdown
Subject: [ANNOUNCEMENT] MLOps Platform - [Title]

## Announcement
[Clear, concise announcement - 2-3 sentences]

## Details
[Expanded details about the announcement]

## What This Means for You
[Specific impact on different user groups]

## Timeline
| Date | Milestone |
|------|-----------|
| [Date] | [Milestone] |

## Resources
- Documentation: [Link]
- FAQ: [Link]
- Training: [Link]

## Questions?
- Slack: #mlops-support
- Office Hours: [Day/Time]

---
[Signature]
```

---

## 7. Communication Schedule

| Communication | Frequency | Day | Owner |
|---------------|-----------|-----|-------|
| Status Update | Bi-weekly | Monday | Platform Lead |
| Release Notes | On release | - | Dev Team |
| Executive Update | Monthly | 1st Monday | Platform Lead |
| Team Newsletter | Monthly | Last Friday | PMO |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial templates |
