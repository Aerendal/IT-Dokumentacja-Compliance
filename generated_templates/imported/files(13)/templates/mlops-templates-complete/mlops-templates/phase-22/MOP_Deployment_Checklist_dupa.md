---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-096: Model Deployment Checklist

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-096 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## Pre-Deployment Checklist

### 1. Model Readiness

| Check | Required | Verified |
|-------|----------|----------|
| Model registered in MLflow |  |  |
| Model card completed |  |  |
| Version follows semantic versioning |  |  |
| All tests passing |  |  |
| Performance meets baseline |  |  |

**Model Details:**
- Name: ___________
- Version: ___________
- Tier: ___________
- MLflow Run ID: ___________

---

### 2. Code & Pipeline

| Check | Required | Verified |
|-------|----------|----------|
| Code merged to main |  |  |
| CI pipeline passed |  |  |
| No critical security findings |  |  |
| Dependencies up to date |  |  |
| Config changes documented |  |  |

---

### 3. Testing

| Check | Required | Verified |
|-------|----------|----------|
| Unit tests passing |  |  |
| Integration tests passing |  |  |
| Model accuracy validated |  |  |
| Load test completed | Tier 1-2 |  |
| Bias testing completed | Tier 1-2 |  |

**Test Results:**
- Accuracy: ___________
- Precision: ___________
- Recall: ___________
- P99 Latency: ___________

---

### 4. Infrastructure

| Check | Required | Verified |
|-------|----------|----------|
| Resource requirements defined |  |  |
| HPA configured |  |  |
| Health checks configured |  |  |
| Rollback procedure documented |  |  |

**Resources:**
- CPU Request/Limit: _____ / _____
- Memory Request/Limit: _____ / _____
- Min/Max Replicas: _____ / _____

---

### 5. Monitoring & Alerting

| Check | Required | Verified |
|-------|----------|----------|
| Dashboard configured |  |  |
| Alerts configured |  |  |
| Logging enabled |  |  |
| Drift monitoring enabled | Tier 1-2 |  |

**Dashboard:** [Link]
**Alert Channel:** ___________

---

### 6. Documentation

| Check | Required | Verified |
|-------|----------|----------|
| Runbook updated |  |  |
| API documentation current |  |  |
| Release notes prepared |  |  |
| Stakeholders notified |  |  |

---

### 7. Approvals

| Approver | Required For | Approved | Date |
|----------|--------------|----------|------|
| ML Lead | All |  | |
| QA Lead | Tier 1-2 |  | |
| Security | Tier 1 |  | |
| Product Owner | Tier 1-2 |  | |

---

## Deployment Execution

### 8. Deploy

| Step | Action | Verified |
|------|--------|----------|
| 1 | Notify #mlops-deployments |  |
| 2 | Deploy to staging |  |
| 3 | Run smoke tests |  |
| 4 | Deploy to production (canary) |  |
| 5 | Monitor canary metrics (30 min) |  |
| 6 | Promote to full production |  |

---

## Post-Deployment Verification

### 9. Verify

| Check | Verified |
|-------|----------|
| Health endpoint returns 200 |  |
| Test inference successful |  |
| Metrics appearing in dashboard |  |
| No errors in logs |  |
| Latency within SLA |  |

---

### 10. Complete

| Action | Done |
|--------|------|
| Update model stage to Production |  |
| Send release notification |  |
| Close deployment ticket |  |
| Update documentation |  |

---

## Rollback Trigger Criteria

| Condition | Action |
|-----------|--------|
| Error rate > 5% | Immediate rollback |
| P99 latency > 2x baseline | Investigate, rollback if persists |
| Health check failures | Investigate, rollback if not resolved in 15 min |

**Rollback Command:**
```bash
kubectl rollout undo deployment/<model-name> -n models
```

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Deployer | | | |
| ML Lead | | | |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial deployment checklist |
