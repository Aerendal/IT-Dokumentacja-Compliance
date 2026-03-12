---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-034: ML Incident Response Procedures

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-034 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Priority** | CRITICAL |
| **Owner** | [MLOps SRE Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Template Content

---

# ML Incident Response Procedures

## 1. Incident Classification

### 1.1 Severity Levels

| Severity | Definition | Response Time | Examples |
|----------|------------|---------------|----------|
| **P1 - Critical** | Production down, revenue impact | 15 min | Model serving down, data breach |
| **P2 - High** | Degraded performance, workaround exists | 1 hour | High latency, partial outage |
| **P3 - Medium** | Minor impact, no workaround needed | 4 hours | Single model errors, monitoring gaps |
| **P4 - Low** | Minimal impact | Next business day | Documentation issues, minor bugs |

### 1.2 ML-Specific Incident Types

| Type | Description | Typical Severity |
|------|-------------|------------------|
| Model Outage | Model not serving predictions | P1 |
| Data Drift | Input distribution changed significantly | P2/P3 |
| Model Degradation | Accuracy dropped below threshold | P2 |
| Feature Store Failure | Features unavailable | P1/P2 |
| Pipeline Failure | Training/inference pipeline broken | P2/P3 |
| Security Incident | Unauthorized access, data exposure | P1 |

---

## 2. Incident Response Process

### 2.1 Response Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Incident Response Workflow                        │
│                                                                     │
│  ┌──────────────┐                                                  │
│  │   DETECT     │  Alert fired / User reported / Monitoring        │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │   TRIAGE     │  Assess severity, assign IC, create incident    │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │  CONTAIN     │  Mitigate impact (rollback, failover, disable)  │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │  INVESTIGATE │  Root cause analysis                            │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │   RESOLVE    │  Fix root cause, verify fix                     │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │  POST-MORTEM │  Document learnings, preventive actions          │
│  └──────────────┘                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Roles During Incident

| Role | Responsibility |
|------|----------------|
| **Incident Commander (IC)** | Overall coordination, decisions, communication |
| **Technical Lead** | Technical investigation, directs engineering work |
| **Communications Lead** | Stakeholder updates, status page |
| **Scribe** | Documents timeline, actions, decisions |
| **Subject Matter Expert** | Deep expertise on affected system |

---

## 3. Incident Playbooks

### 3.1 Model Serving Outage

**Symptoms:**
- Health check failing
- 5xx errors from model endpoint
- No predictions being served

**Immediate Actions (< 5 minutes):**
```bash
# 1. Check pod status
kubectl get pods -l model=fraud-model -n models

# 2. Check recent events
kubectl get events -n models --sort-by='.lastTimestamp' | tail -20

# 3. Quick rollback if recent deployment
kubectl rollout undo deployment/fraud-model-predictor -n models

# 4. Or restart pods
kubectl rollout restart deployment/fraud-model-predictor -n models
```

**Investigation:**
```bash
# Check logs
kubectl logs -l model=fraud-model -n models --tail=500 | grep -i error

# Check resource usage
kubectl top pods -l model=fraud-model -n models

# Check dependencies
curl -s http://feature-store:6566/health
curl -s http://mlflow:5000/health
```

**Resolution Options:**
1. Rollback to previous version
2. Scale up replicas
3. Failover to backup model
4. Enable fallback predictions

---

### 3.2 Data Drift Detected

**Symptoms:**
- Data drift alert triggered
- Feature distributions changed
- Model accuracy may degrade

**Assessment:**
```python
# Review drift report
from evidently.report import Report

report = Report.load("s3://reports/drift/latest.json")
print(report.as_dict()["metrics"])

# Check which features drifted
drifted = [f for f, v in report.drift_by_columns.items() if v["drift_detected"]]
print(f"Drifted features: {drifted}")
```

**Response Actions:**
1. **Low drift (<0.1):** Monitor, no immediate action
2. **Medium drift (0.1-0.2):** Investigate cause, consider retraining
3. **High drift (>0.2):** Urgent investigation, possible model retrain

**Investigation:**
- Check upstream data sources
- Review recent data pipeline changes
- Analyze business events that could explain drift
- Compare with historical drift patterns

---

### 3.3 Model Performance Degradation

**Symptoms:**
- Accuracy dropped below baseline
- Business metrics declining
- A/B test showing worse results

**Assessment:**
```python
# Compare current vs baseline metrics
from mlflow.tracking import MlflowClient

client = MlflowClient()
production_model = client.get_model_version_by_alias("fraud-model", "production")
baseline_metrics = production_model.tags

current_accuracy = calculate_current_accuracy()
baseline_accuracy = float(baseline_metrics.get("accuracy", 0.95))

degradation = baseline_accuracy - current_accuracy
print(f"Degradation: {degradation:.2%}")
```

**Response Actions:**
1. If <2% degradation: Monitor closely
2. If 2-5% degradation: Investigate, plan retrain
3. If >5% degradation: Trigger emergency retrain or rollback

---

### 3.4 Feature Store Failure

**Symptoms:**
- Feature retrieval errors
- High latency on feature fetch
- Null/stale features

**Immediate Actions:**
```bash
# Check feature server
kubectl get pods -n feast
kubectl logs -l app=feast-server -n feast --tail=100

# Check Redis
kubectl exec -it redis-0 -n feast -- redis-cli ping
kubectl exec -it redis-0 -n feast -- redis-cli info memory

# Check materialization
feast materialize-incremental $(date -u +%Y-%m-%dT%H:%M:%S)
```

**Fallback:**
```python
# Enable default features
def get_features_with_fallback(entity_ids):
    try:
        return feature_store.get_online_features(entity_ids)
    except Exception:
        logger.warning("Feature store unavailable, using defaults")
        return get_default_features(entity_ids)
```

---

## 4. Communication Templates

### 4.1 Initial Notification

```markdown
 **INCIDENT: [INC-XXXX] [Brief Description]**

**Severity:** P[1/2/3]
**Status:** Investigating
**Time Detected:** [HH:MM UTC]
**Incident Commander:** @[name]

**Impact:**
- [Description of user/business impact]

**Current Actions:**
- [What's being done right now]

**Next Update:** [HH:MM UTC] or sooner if status changes

Incident Channel: #inc-[number]
```

### 4.2 Status Update

```markdown
 **UPDATE: [INC-XXXX] [Brief Description]**

**Status:** [Investigating/Mitigating/Resolved]
**Duration:** [X hours Y minutes]

**Progress:**
-  [Completed action]
-  [In progress action]
-  [Pending action]

**Current Impact:**
- [Updated impact description]

**ETA to Resolution:** [Estimate]
**Next Update:** [HH:MM UTC]
```

### 4.3 Resolution Notification

```markdown
 **RESOLVED: [INC-XXXX] [Brief Description]**

**Duration:** [X hours Y minutes]
**Root Cause:** [Brief description]
**Resolution:** [What fixed it]

**Impact Summary:**
- [Number] users affected
- [X]% error rate during incident
- [Y] minutes of degraded service

**Follow-up Actions:**
- [ ] Post-mortem scheduled for [date]
- [ ] [Action item 1]
- [ ] [Action item 2]
```

---

## 5. Incident Documentation

### 5.1 Incident Ticket Template

```markdown
## Incident Summary
**Incident ID:** INC-XXXX
**Title:** [Brief description]
**Severity:** P[1/2/3/4]
**Status:** [Open/Resolved]

## Timeline
| Time (UTC) | Event |
|------------|-------|
| HH:MM | Alert fired |
| HH:MM | IC assigned |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | Incident resolved |

## Impact
- **Duration:** X hours Y minutes
- **Users Affected:** [Number]
- **Revenue Impact:** $[Amount] (if applicable)
- **Services Affected:** [List]

## Root Cause
[Detailed explanation of what caused the incident]

## Resolution
[What was done to fix the issue]

## Action Items
- [ ] [Follow-up action 1] - Owner: @name - Due: [date]
- [ ] [Follow-up action 2] - Owner: @name - Due: [date]

## Lessons Learned
- [Learning 1]
- [Learning 2]
```

---

## 6. Post-Incident Review

### 6.1 Post-Mortem Meeting Agenda

1. **Timeline Review** (10 min) - Walk through events
2. **Impact Assessment** (5 min) - Quantify damage
3. **Root Cause Analysis** (15 min) - 5 Whys analysis
4. **What Went Well** (5 min) - Effective responses
5. **What Could Be Improved** (10 min) - Gaps identified
6. **Action Items** (15 min) - Preventive measures

### 6.2 5 Whys Template

```markdown
**Problem:** Model serving latency increased to 500ms

1. **Why?** The model was running on CPU instead of GPU
2. **Why?** The GPU node was cordoned for maintenance
3. **Why?** Maintenance wasn't communicated to ML team
4. **Why?** No process for coordinating maintenance windows
5. **Why?** Platform and ML teams operate independently

**Root Cause:** Lack of cross-team coordination for infrastructure changes

**Corrective Action:** Establish shared maintenance calendar and notification process
```

---

## 7. Escalation Matrix

| Condition | Escalate To | Method |
|-----------|-------------|--------|
| P1 not mitigated in 30 min | Engineering Manager | Phone |
| P1 not resolved in 2 hours | Director | Phone |
| Data breach suspected | Security + Legal | Immediate |
| Customer-facing impact | Customer Success | Slack |
| Revenue impact >$10K | VP Engineering | Phone |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial procedures |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| MLOps SRE Lead | | | |
| Engineering Manager | | | |
