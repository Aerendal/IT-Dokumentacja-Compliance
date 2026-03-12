---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-094: On-Call Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-094 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. On-Call Overview

### 1.1 Rotation Schedule

| Rotation | Duration | Coverage |
|----------|----------|----------|
| Primary | 1 week | 24/7 |
| Secondary | 1 week | 24/7 backup |
| Handoff | Monday 9 AM | 30 min overlap |

### 1.2 Expectations

| Expectation | Requirement |
|-------------|-------------|
| Response time (P1) | 5 minutes |
| Response time (P2) | 15 minutes |
| Availability | Reachable at all times |
| Laptop access | Within 30 min if needed |

---

## 2. Getting Started

### 2.1 Pre-On-Call Checklist

```markdown
## Before Your Shift

- [ ] PagerDuty app installed and configured
- [ ] Slack notifications enabled for #mlops-incidents
- [ ] VPN access verified
- [ ] kubectl context configured
- [ ] Runbooks bookmarked
- [ ] Phone charged and volume on
- [ ] Review recent incidents from last week
```

### 2.2 Essential Access

| System | URL | Purpose |
|--------|-----|---------|
| PagerDuty | pagerduty.com/company | Alerts |
| Grafana | grafana.company.com | Dashboards |
| Prometheus | prometheus.company.com | Metrics/queries |
| MLflow | mlflow.company.com | Model registry |
| ArgoCD | argocd.company.com | Deployments |

### 2.3 Quick Commands

```bash
# Check platform health
kubectl get pods -n mlops
kubectl get pods -n models
kubectl get pods -n feast

# View recent logs
kubectl logs -n mlops -l app=mlflow --tail=100 --since=1h

# Check alerts
curl -s http://alertmanager:9093/api/v2/alerts | jq '.[] | select(.status.state=="active")'

# Restart a service
kubectl rollout restart deployment/<name> -n <namespace>
```

---

## 3. Alert Response

### 3.1 When Paged

1. **Acknowledge** the alert in PagerDuty (stops escalation)
2. **Assess** severity and impact
3. **Investigate** using runbooks and dashboards
4. **Communicate** in #mlops-incidents
5. **Resolve** or **Escalate** if needed

### 3.2 First Response Template

```markdown
## Alert: [Alert Name]
**Acknowledged:** [Time]
**On-call:** [Your name]

**Initial Assessment:**
- Severity: P1/P2/P3
- Impact: [Describe user/business impact]
- Components: [Affected services]

**Investigation:**
- [ ] Checked dashboard
- [ ] Reviewed logs
- [ ] Identified potential cause

**Status:** Investigating / Mitigating / Resolved
**ETA:** [Estimated time to resolution]
```

---

## 4. Common Scenarios

### 4.1 Model Serving Down

```bash
# Check pods
kubectl get pods -n models -l app=model-serving

# Check events
kubectl describe pod <pod-name> -n models

# Check logs
kubectl logs <pod-name> -n models --tail=100

# Restart if needed
kubectl rollout restart deployment/model-serving -n models
```

**Runbook:** [MOP-037](./MOP-037-Model-Serving-Failure.md)

### 4.2 MLflow Unavailable

```bash
# Check MLflow pods
kubectl get pods -n mlops -l app=mlflow

# Check database connection
kubectl exec -n mlops deploy/mlflow -- pg_isready -h mlflow-db

# Restart MLflow
kubectl rollout restart deployment/mlflow -n mlops
```

**Runbook:** [MOP-082](./MOP-082-Troubleshooting-Guide.md)

### 4.3 High Latency

```bash
# Check current latency
curl -s "http://prometheus:9090/api/v1/query?query=histogram_quantile(0.99,sum(rate(inference_latency_bucket[5m]))by(le))"

# Check resource usage
kubectl top pods -n models

# Check HPA
kubectl get hpa -n models
```

---

## 5. Handoff Procedure

### 5.1 End of Shift

1. Document any open issues
2. Update incident tickets
3. Post handoff summary in #mlops-oncall
4. Join handoff call with incoming on-call

### 5.2 Handoff Template

```markdown
## On-Call Handoff - [Date]

**Outgoing:** [Name]
**Incoming:** [Name]

### Open Issues
- [Issue 1]: Status, next steps
- [Issue 2]: Status, next steps

### Resolved This Week
- INC-XXX: [Brief description]

### Upcoming
- Maintenance window: [Date/time]
- Deployments planned: [List]

### Notes
- [Anything incoming on-call should know]
```

---

## 6. Self-Care

- Take breaks when not actively responding
- Hand off if you're impaired or exhausted
- Post-incident: take comp time if needed
- Escalate early if overwhelmed

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial on-call guide |
