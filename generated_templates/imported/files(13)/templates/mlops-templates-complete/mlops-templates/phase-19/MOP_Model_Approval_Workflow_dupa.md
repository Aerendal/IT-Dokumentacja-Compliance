---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-085: Model Approval Workflow

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-085 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Governance] |

---

## 1. Approval Requirements

### 1.1 Approval Matrix

| Model Tier | Staging | Production | Approvers |
|------------|---------|------------|-----------|
| Tier 1 (Critical) | ML Lead | Governance Board | ML Lead, QA, Ethics, Compliance |
| Tier 2 (Important) | ML Lead | ML Lead + QA | ML Lead, QA Lead |
| Tier 3 (Standard) | Self-service | ML Lead | ML Lead |
| Tier 4 (Experimental) | Self-service | N/A | None |

### 1.2 Required Approvals by Stage

```
┌─────────────────────────────────────────────────────────────────┐
│                 Model Approval Workflow                          │
│                                                                 │
│  Development ──► Staging ──► Production ──► Monitoring          │
│       │            │             │              │               │
│       │            │             │              │               │
│  No approval   ML Lead      Tier-based      Periodic           │
│  required      approval     approval        review             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Approval Process

### 2.1 Staging Approval Checklist

```markdown
## Staging Approval Checklist

**Model:** ___________
**Version:** ___________
**Requestor:** ___________
**Date:** ___________

### Code Quality
- [ ] Code review completed
- [ ] Unit tests passing (100%)
- [ ] Integration tests passing
- [ ] No critical code quality issues

### Model Quality
- [ ] Model card completed
- [ ] Performance metrics documented
- [ ] Meets baseline accuracy thresholds
- [ ] Bias testing completed

### Documentation
- [ ] Training data documented
- [ ] Feature dependencies documented
- [ ] Deployment runbook created

### Approval
- [ ] **ML Lead:** ___________  Date: ___________
```

### 2.2 Production Approval Checklist

```markdown
## Production Approval Checklist

**Model:** ___________
**Version:** ___________
**Tier:** ___________

### Technical Validation
- [ ] Staging validation successful
- [ ] Load testing completed
- [ ] Security scan passed
- [ ] Rollback procedure verified

### Compliance
- [ ] Model card complete (all sections)
- [ ] Fairness metrics within thresholds
- [ ] Privacy review completed (Tier 1/2)
- [ ] Regulatory requirements met

### Operational Readiness
- [ ] Monitoring configured
- [ ] Alerts set up
- [ ] On-call documentation updated
- [ ] Support team briefed

### Approvals Required
| Role | Name | Approved | Date |
|------|------|----------|------|
| ML Lead | |  | |
| QA Lead | |  | |
| Ethics (Tier 1) | |  | |
| Compliance (Tier 1) | |  | |
```

---

## 3. Automated Approval Gates

### 3.1 GitHub Actions Workflow

```yaml
# .github/workflows/model-approval.yml
name: Model Approval Workflow

on:
  workflow_dispatch:
    inputs:
      model_name:
        description: 'Model name'
        required: true
      model_version:
        description: 'Model version'
        required: true
      target_stage:
        description: 'Target stage (staging/production)'
        required: true
        default: 'staging'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate model
        run: |
          python scripts/validate_model.py \
            --model ${{ inputs.model_name }} \
            --version ${{ inputs.model_version }}
      
      - name: Check quality gates
        run: |
          python scripts/check_quality_gates.py \
            --model ${{ inputs.model_name }} \
            --version ${{ inputs.model_version }}
  
  request-approval:
    needs: validate
    runs-on: ubuntu-latest
    environment: 
      name: ${{ inputs.target_stage }}
    steps:
      - name: Request approval
        uses: trstringer/manual-approval@v1
        with:
          secret: ${{ secrets.GITHUB_TOKEN }}
          approvers: ml-leads
          minimum-approvals: 1
      
      - name: Transition model
        if: success()
        run: |
          python scripts/transition_model.py \
            --model ${{ inputs.model_name }} \
            --version ${{ inputs.model_version }} \
            --stage ${{ inputs.target_stage }}
```

### 3.2 Approval API

```python
# approval/workflow.py
from enum import Enum
from dataclasses import dataclass
from typing import List
import mlflow

class ApprovalStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
class ApprovalRequest:
    model_name: str
    model_version: str
    target_stage: str
    requestor: str
    required_approvers: List[str]
    approvals: dict = None

class ApprovalWorkflow:
    """Manage model approval workflow."""
    
    def __init__(self):
        self.client = mlflow.tracking.MlflowClient()
    
    def create_request(self, model_name: str, version: str, 
                       target_stage: str, requestor: str) -> ApprovalRequest:
        """Create approval request."""
        tier = self._get_model_tier(model_name, version)
        approvers = self._get_required_approvers(tier, target_stage)
        
        request = ApprovalRequest(
            model_name=model_name,
            model_version=version,
            target_stage=target_stage,
            requestor=requestor,
            required_approvers=approvers,
            approvals={}
        )
        
        # Store in MLflow tags
        self.client.set_model_version_tag(
            model_name, version, 
            "approval.status", ApprovalStatus.PENDING.value
        )
        self.client.set_model_version_tag(
            model_name, version,
            "approval.required_approvers", ",".join(approvers)
        )
        
        # Notify approvers
        self._notify_approvers(request)
        
        return request
    
    def approve(self, model_name: str, version: str, approver: str) -> bool:
        """Record approval."""
        request = self._get_request(model_name, version)
        
        if approver not in request.required_approvers:
            raise ValueError(f"{approver} is not an authorized approver")
        
        request.approvals[approver] = True
        
        # Update tags
        self.client.set_model_version_tag(
            model_name, version,
            f"approval.{approver}", "approved"
        )
        
        # Check if all approvals received
        if all(a in request.approvals for a in request.required_approvers):
            self._finalize_approval(request)
            return True
        
        return False
    
    def _finalize_approval(self, request: ApprovalRequest):
        """Complete the approval process."""
        self.client.transition_model_version_stage(
            request.model_name,
            request.model_version,
            request.target_stage
        )
        
        self.client.set_model_version_tag(
            request.model_name, request.model_version,
            "approval.status", ApprovalStatus.APPROVED.value
        )
        
        self.client.set_model_version_tag(
            request.model_name, request.model_version,
            "approval.completed_at", datetime.utcnow().isoformat()
        )
```

---

## 4. Governance Board Review

### 4.1 Board Meeting Template

```markdown
## Governance Board Review - [Date]

### Models for Review

| Model | Version | Tier | Requestor | Recommendation |
|-------|---------|------|-----------|----------------|
| fraud-detection | 2.0.0 | 1 | Team A | Approve |

### Review Criteria

For each Tier 1 model:
1. Business justification
2. Ethical considerations
3. Regulatory compliance
4. Technical readiness
5. Risk assessment

### Decisions

| Model | Decision | Conditions | Next Review |
|-------|----------|------------|-------------|
| fraud-detection | Approved | Monthly bias audit | 2024-04-01 |

### Action Items
- [ ] [Action 1]
- [ ] [Action 2]
```

---

## 5. Audit Trail

### 5.1 Approval Events Logged

| Event | Data Captured |
|-------|---------------|
| Request created | Model, version, requestor, timestamp |
| Approval given | Approver, timestamp, comments |
| Rejection | Rejector, reason, timestamp |
| Stage transition | From/to stage, timestamp |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial approval workflow |
