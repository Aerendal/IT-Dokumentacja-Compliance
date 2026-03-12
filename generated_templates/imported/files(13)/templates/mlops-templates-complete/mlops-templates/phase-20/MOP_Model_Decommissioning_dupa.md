---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-053: Model Decommissioning Procedures

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-053 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Priority** | MEDIUM |
| **Owner** | [ML Platform Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Annually) |

---

## Template Content

---

# Model Decommissioning Procedures

## 1. Decommissioning Criteria

### 1.1 Triggers for Decommissioning

| Trigger | Description | Urgency |
|---------|-------------|---------|
| Model replaced | New version deployed | Standard |
| Business retired | Use case no longer needed | Standard |
| Performance degradation | Cannot maintain SLAs | High |
| Compliance issue | Regulatory/policy violation | Urgent |
| Security vulnerability | Unpatched risk | Urgent |
| Cost optimization | ROI no longer justified | Low |

### 1.2 Decommissioning Decision Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Decommissioning Decision Flow                     │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ Is there an active replacement model?                        │  │
│  │     │                                                        │  │
│  │     ├── Yes ──► Migration path exists                       │  │
│  │     │           Proceed with standard decommission          │  │
│  │     │                                                        │  │
│  │     └── No ───► Business impact assessment required          │  │
│  │                 ├── Impact acceptable ──► Proceed            │  │
│  │                 └── Impact not acceptable ──► Maintain       │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ Are there downstream dependencies?                           │  │
│  │     │                                                        │  │
│  │     ├── Yes ──► Migration plan required                     │  │
│  │     │           Notify all consumers                         │  │
│  │     │                                                        │  │
│  │     └── No ───► Proceed with decommission                   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Decommissioning Process

### 2.1 Standard Decommissioning Timeline

| Phase | Duration | Activities |
|-------|----------|------------|
| **Announcement** | T-30 days | Notify stakeholders, document plan |
| **Deprecation** | T-30 to T-7 | Add deprecation warnings, soft disable |
| **Migration** | T-30 to T-1 | Support consumer migration |
| **Retirement** | T-0 | Remove from production |
| **Archival** | T+7 | Archive artifacts, update docs |
| **Cleanup** | T+30 | Delete resources (optional) |

### 2.2 Decommissioning Checklist

```markdown
## Model Decommissioning Checklist

**Model Name:** _______________
**Model Version:** _______________
**Decommission Date:** _______________
**Owner:** _______________

### Pre-Decommission (T-30 days)
- [ ] Business approval obtained
- [ ] Stakeholders identified and notified
- [ ] Downstream dependencies mapped
- [ ] Migration path documented (if applicable)
- [ ] Data retention requirements confirmed
- [ ] Compliance/legal review (if required)

### Deprecation Phase (T-30 to T-7)
- [ ] Deprecation warning added to API responses
- [ ] Documentation updated with deprecation notice
- [ ] Monitoring for continued usage enabled
- [ ] Consumer migration support provided
- [ ] Usage metrics captured

### Migration Support (T-30 to T-1)
- [ ] Consumer migration progress tracked
- [ ] Migration issues resolved
- [ ] Final usage report generated
- [ ] Remaining consumers contacted directly

### Retirement (T-0)
- [ ] Model endpoint removed
- [ ] Traffic routing updated
- [ ] Health checks disabled
- [ ] Alerts silenced/removed

### Post-Retirement (T+7)
- [ ] Model archived in registry
- [ ] Artifacts archived
- [ ] Documentation archived
- [ ] Training data references documented
- [ ] Final report generated

### Cleanup (T+30)
- [ ] Compute resources released
- [ ] Storage cleanup (per retention policy)
- [ ] Monitoring dashboards archived
- [ ] Final documentation update
```

---

## 3. Stakeholder Communication

### 3.1 Notification Template

```markdown
# Model Deprecation Notice

**Model:** [Model Name]
**Current Version:** [Version]
**Deprecation Date:** [Date]
**Retirement Date:** [Date]

## Summary
[Model Name] will be deprecated on [deprecation date] and fully retired on [retirement date].

## Reason for Deprecation
[Explanation - e.g., replaced by newer version, business decision, etc.]

## Impact
- **Who is affected:** [Teams/Services using this model]
- **What will change:** [Description of changes]

## Migration Path
[If applicable]
- **Replacement model:** [New model name/endpoint]
- **Migration guide:** [Link to documentation]
- **Breaking changes:** [List any breaking changes]

## Timeline
| Date | Action |
|------|--------|
| [Date] | Deprecation notice (today) |
| [Date] | Deprecation warnings enabled |
| [Date] | Final migration deadline |
| [Date] | Model retired |

## Support
- **Questions:** Contact #mlops-support or @[owner]
- **Migration assistance:** [Link or contact]

## Next Steps
1. Review your usage of this model
2. Plan migration to [replacement]
3. Test with new model in staging
4. Complete migration before [deadline]

---
**Contact:** [Owner email]
**Ticket:** [Link to tracking ticket]
```

### 3.2 Communication Timeline

| Time | Channel | Message |
|------|---------|---------|
| T-30 | Email, Slack | Initial deprecation notice |
| T-14 | Email | Migration reminder |
| T-7 | Email, Slack | Final warning |
| T-1 | Slack | Last day reminder |
| T-0 | Slack | Retirement confirmation |

---

## 4. Technical Procedures

### 4.1 Remove from Production

```bash
#!/bin/bash
# decommission_model.sh

MODEL_NAME=$1
NAMESPACE="models"

echo "=== Decommissioning Model: $MODEL_NAME ==="

# Step 1: Scale down to zero
echo "[1/5] Scaling down deployment..."
kubectl scale deployment ${MODEL_NAME}-predictor -n $NAMESPACE --replicas=0

# Step 2: Remove from load balancer
echo "[2/5] Removing from service..."
kubectl delete service ${MODEL_NAME} -n $NAMESPACE

# Step 3: Remove InferenceService
echo "[3/5] Removing InferenceService..."
kubectl delete inferenceservice ${MODEL_NAME} -n $NAMESPACE

# Step 4: Update model registry
echo "[4/5] Updating model registry..."
mlflow models update-stage --name $MODEL_NAME --stage Archived

# Step 5: Remove monitoring
echo "[5/5] Removing monitoring..."
kubectl delete servicemonitor ${MODEL_NAME}-monitor -n monitoring

echo "=== Decommission Complete ==="
```

### 4.2 Archive Model Artifacts

```bash
#!/bin/bash
# archive_model.sh

MODEL_NAME=$1
ARCHIVE_BUCKET="s3://mlops-archives"
DATE=$(date +%Y%m%d)

echo "=== Archiving Model: $MODEL_NAME ==="

# Archive from model registry
mlflow artifacts download \
  --artifact-uri "models:/$MODEL_NAME/Production" \
  --dst-path /tmp/model_archive

# Compress and upload
tar -czvf /tmp/${MODEL_NAME}_${DATE}.tar.gz /tmp/model_archive
aws s3 cp /tmp/${MODEL_NAME}_${DATE}.tar.gz \
  ${ARCHIVE_BUCKET}/models/${MODEL_NAME}/

# Archive metadata
mlflow models get $MODEL_NAME > /tmp/${MODEL_NAME}_metadata.json
aws s3 cp /tmp/${MODEL_NAME}_metadata.json \
  ${ARCHIVE_BUCKET}/models/${MODEL_NAME}/

echo "=== Archive Complete ==="
echo "Archive location: ${ARCHIVE_BUCKET}/models/${MODEL_NAME}/"
```

---

## 5. Data Retention

### 5.1 Retention Requirements

| Data Type | Retention Period | Storage |
|-----------|------------------|---------|
| Model artifacts | 7 years | Archive storage |
| Training data reference | 7 years | Metadata only |
| Inference logs | 1 year | Cold storage |
| Experiment data | 3 years | Archive storage |
| Model card | 7 years | Documentation |
| Audit logs | 7 years | Compliance storage |

### 5.2 What to Archive

| Archive | Don't Archive |
|---------|---------------|
| Model binary | Temporary files |
| Model card | Cache data |
| Training configuration | Debug logs |
| Evaluation metrics | Old checkpoints |
| Feature definitions | Duplicate artifacts |

---

## 6. Approval Workflow

### 6.1 Approval Matrix

| Model Tier | Approver |
|------------|----------|
| Tier 1 (Critical) | Governance Board |
| Tier 2 (Important) | ML Lead + Business Owner |
| Tier 3 (Standard) | ML Lead |
| Tier 4 (Experimental) | Model Owner |

### 6.2 Approval Form

```markdown
## Model Decommission Approval Form

**Model:** _______________
**Version:** _______________
**Tier:** _______________
**Requested By:** _______________
**Date:** _______________

### Justification
[Reason for decommissioning]

### Impact Assessment
- [ ] No active consumers
- [ ] Consumers migrated
- [ ] Business impact accepted

### Compliance
- [ ] Data retention requirements met
- [ ] Audit trail preserved
- [ ] Legal review (if required)

### Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Model Owner | | | |
| ML Lead | | | |
| Business Owner | | | |
| Governance (Tier 1) | | | |
```

---

## 7. Post-Decommission

### 7.1 Final Report Template

```markdown
## Model Decommission Report

**Model:** [Name]
**Decommission Date:** [Date]
**Duration in Production:** [X months/years]

### Summary
- Total predictions served: [Number]
- Peak usage: [Requests/day]
- Final consumers migrated: [List]

### Reason for Decommission
[Explanation]

### Assets Archived
- [ ] Model artifacts
- [ ] Training data references
- [ ] Model card
- [ ] Evaluation results

### Lessons Learned
- [Learning 1]
- [Learning 2]

### Archive Location
[Path to archived assets]
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial procedures |
