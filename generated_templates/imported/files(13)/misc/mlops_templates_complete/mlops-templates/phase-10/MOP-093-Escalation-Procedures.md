---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-093: Escalation Procedures

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-093 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Escalation Matrix

### 1.1 By Severity

| Severity | Initial Response | Escalation L1 | Escalation L2 | Escalation L3 |
|----------|------------------|---------------|---------------|---------------|
| P1 Critical | On-call (5 min) | SRE Lead (15 min) | Platform Lead (30 min) | VP Engineering (1 hr) |
| P2 High | On-call (15 min) | SRE Lead (1 hr) | Platform Lead (4 hr) | - |
| P3 Medium | On-call (1 hr) | SRE Lead (4 hr) | - | - |
| P4 Low | Next business day | - | - | - |

### 1.2 By Component

| Component | Primary | Secondary | Escalation |
|-----------|---------|-----------|------------|
| MLflow | ML Platform Team | SRE | Platform Lead |
| Feature Store | Data Engineering | ML Platform | Data Lead |
| Model Serving | SRE | ML Platform | SRE Lead |
| Training Pipelines | ML Engineering | SRE | ML Lead |

---

## 2. Escalation Triggers

### 2.1 Automatic Escalation

| Trigger | Escalation |
|---------|------------|
| No acknowledgment in 15 min (P1) | Auto-escalate to L1 |
| No resolution in 30 min (P1) | Auto-escalate to L2 |
| Multiple P1s in 24 hours | Notify VP Engineering |
| Error budget exhausted | Freeze deployments |

### 2.2 Manual Escalation Criteria

- Issue beyond responder's expertise
- Resource constraints (need more people)
- Business impact requires executive awareness
- Cross-team coordination needed
- Vendor involvement required

---

## 3. Escalation Procedures

### 3.1 P1 Escalation Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    P1 Escalation Flow                           │
│                                                                 │
│  T+0         T+5min      T+15min     T+30min      T+1hr        │
│   │            │            │           │            │          │
│   ▼            ▼            ▼           ▼            ▼          │
│ Alert ───► On-call ───► SRE Lead ───► Platform ───► VP Eng    │
│ fired     responds      escalated     Lead         notified    │
│                                       joins                     │
│                                                                │
│ Actions at each stage:                                         │
│ • On-call: Acknowledge, initial diagnosis, page if needed     │
│ • SRE Lead: Coordinate response, allocate resources           │
│ • Platform Lead: Business decisions, customer communication   │
│ • VP Eng: Executive communication, major decisions            │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Escalation Script

```bash
#!/bin/bash
# escalation/escalate.sh

INCIDENT_ID=$1
CURRENT_LEVEL=$2
REASON=$3

echo "=== Escalating Incident $INCIDENT_ID ==="

# Determine next level
case $CURRENT_LEVEL in
    "L0")
        NEXT_LEVEL="L1"
        CONTACTS="sre-lead@company.com"
        PAGERDUTY_POLICY="sre-lead-policy"
        ;;
    "L1")
        NEXT_LEVEL="L2"
        CONTACTS="platform-lead@company.com"
        PAGERDUTY_POLICY="platform-lead-policy"
        ;;
    "L2")
        NEXT_LEVEL="L3"
        CONTACTS="vp-engineering@company.com"
        PAGERDUTY_POLICY="exec-policy"
        ;;
esac

# Page via PagerDuty
curl -X POST https://events.pagerduty.com/v2/enqueue \
  -H "Content-Type: application/json" \
  -d "{
    \"routing_key\": \"$PAGERDUTY_KEY\",
    \"event_action\": \"trigger\",
    \"payload\": {
      \"summary\": \"Escalation: Incident $INCIDENT_ID - $REASON\",
      \"severity\": \"critical\",
      \"source\": \"escalation-system\"
    }
  }"

# Update incident
curl -X PUT "https://incidents.company.com/api/incidents/$INCIDENT_ID" \
  -d "{\"escalation_level\": \"$NEXT_LEVEL\", \"escalation_reason\": \"$REASON\"}"

# Notify Slack
curl -X POST $SLACK_WEBHOOK \
  -d "{\"text\": \" Incident $INCIDENT_ID escalated to $NEXT_LEVEL: $REASON\"}"

echo "Escalated to $NEXT_LEVEL"
```

---

## 4. Contact Information

### 4.1 On-Call Rotation

| Week | Primary | Secondary |
|------|---------|-----------|
| Current | [See PagerDuty] | [See PagerDuty] |

**PagerDuty Schedule:** https://company.pagerduty.com/schedules/mlops

### 4.2 Leadership Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| SRE Lead | [Name] | [Phone] | sre-lead@company.com |
| Platform Lead | [Name] | [Phone] | platform-lead@company.com |
| VP Engineering | [Name] | [Phone] | vp-eng@company.com |

---

## 5. Communication During Escalation

### 5.1 Status Update Frequency

| Severity | Update Frequency |
|----------|------------------|
| P1 | Every 15 minutes |
| P2 | Every 30 minutes |
| P3 | Every 2 hours |

### 5.2 Stakeholder Notification

```markdown
## Escalation Notification Template

**Incident:** INC-XXXX
**Severity:** P1
**Status:** Escalated to [Level]

**Summary:** [Brief description]

**Impact:** [Customer/business impact]

**Current Actions:** [What's being done]

**Next Update:** [Time]

**Incident Commander:** [Name]
**Bridge:** [Link to call/channel]
```

---

## 6. De-escalation

### 6.1 De-escalation Criteria

- Root cause identified
- Fix deployed and verified
- Monitoring confirms resolution
- No recurrence in observation period

### 6.2 De-escalation Process

1. Incident commander confirms resolution
2. Notify all escalation levels
3. Update incident status
4. Schedule post-mortem

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial escalation procedures |
