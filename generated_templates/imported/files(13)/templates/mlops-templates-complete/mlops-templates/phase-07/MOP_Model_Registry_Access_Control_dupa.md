---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-027: Model Registry Access Control

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-027 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Security / ML Platform Lead] |

---

## 1. Access Control Model

### 1.1 RBAC Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                Model Registry RBAC                           │
│                                                             │
│  Identity Provider (Okta/Azure AD)                          │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Groups → Roles Mapping                  │   │
│  │  ml-engineers → ML_ENGINEER                         │   │
│  │  ml-leads → ML_LEAD                                 │   │
│  │  data-scientists → DATA_SCIENTIST                   │   │
│  │  platform-admins → PLATFORM_ADMIN                   │   │
│  └─────────────────────────────────────────────────────┘   │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Permissions by Role                     │   │
│  │  Role → [Create, Read, Update, Delete, Promote]     │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Role Definitions

### 2.1 Role Permission Matrix

| Permission | Viewer | Data Scientist | ML Engineer | ML Lead | Admin |
|------------|--------|----------------|-------------|---------|-------|
| List models |  |  |  |  |  |
| View model details |  |  |  |  |  |
| Download artifacts |  |  |  |  |  |
| Register model |  |  |  |  |  |
| Update model metadata |  |  |  |  |  |
| Transition to Staging |  |  |  |  |  |
| Transition to Production |  |  |  |  |  |
| Archive model |  |  |  |  |  |
| Delete model |  |  |  |  |  |
| Manage permissions |  |  |  |  |  |

### 2.2 Role Definitions

```yaml
# rbac/roles.yaml
roles:
  - name: VIEWER
    description: Read-only access to model registry
    permissions:
      - models:list
      - models:read
      - experiments:list
      - experiments:read

  - name: DATA_SCIENTIST
    description: Can register and view models
    permissions:
      - models:list
      - models:read
      - models:create
      - models:download
      - experiments:*

  - name: ML_ENGINEER
    description: Can manage models through staging
    permissions:
      - models:*
      - models:transition:staging
      - experiments:*

  - name: ML_LEAD
    description: Can promote models to production
    permissions:
      - models:*
      - models:transition:*
      - experiments:*

  - name: PLATFORM_ADMIN
    description: Full administrative access
    permissions:
      - "*"
```

---

## 3. Implementation

### 3.1 MLflow Authentication Setup

```python
# auth/mlflow_auth.py
from mlflow.server.auth import create_user, create_permission
from mlflow.server.auth.permissions import Permission

def setup_rbac():
    """Configure MLflow RBAC."""
    
    # Create permissions
    permissions = {
        'models:list': Permission.READ,
        'models:read': Permission.READ,
        'models:create': Permission.EDIT,
        'models:update': Permission.EDIT,
        'models:delete': Permission.MANAGE,
        'models:transition:staging': Permission.EDIT,
        'models:transition:production': Permission.MANAGE,
    }
    
    for perm_name, level in permissions.items():
        create_permission(
            name=perm_name,
            permission_level=level
        )
```

### 3.2 OAuth Integration

```yaml
# mlflow-config.yaml
server:
  auth:
    enabled: true
    provider: oauth2
    oauth2:
      client_id: ${OAUTH_CLIENT_ID}
      client_secret: ${OAUTH_CLIENT_SECRET}
      authorization_url: https://company.okta.com/oauth2/authorize
      token_url: https://company.okta.com/oauth2/token
      userinfo_url: https://company.okta.com/oauth2/userinfo
      scopes:
        - openid
        - profile
        - email
        - groups
```

### 3.3 Group to Role Mapping

```python
# auth/group_mapping.py
GROUP_ROLE_MAPPING = {
    "ml-viewers": "VIEWER",
    "data-scientists": "DATA_SCIENTIST",
    "ml-engineers": "ML_ENGINEER",
    "ml-leads": "ML_LEAD",
    "platform-admins": "PLATFORM_ADMIN",
}

def get_role_from_groups(user_groups: list) -> str:
    """Get highest privilege role from user groups."""
    role_priority = ["PLATFORM_ADMIN", "ML_LEAD", "ML_ENGINEER", 
                     "DATA_SCIENTIST", "VIEWER"]
    
    for role in role_priority:
        for group, mapped_role in GROUP_ROLE_MAPPING.items():
            if group in user_groups and mapped_role == role:
                return role
    
    return "VIEWER"  # Default
```

---

## 4. Model-Level Permissions

### 4.1 Model Ownership

```python
# auth/model_permissions.py
class ModelPermissionManager:
    """Manage per-model permissions."""
    
    def __init__(self, client):
        self.client = client
    
    def set_model_owner(self, model_name: str, owner_email: str):
        """Set model owner."""
        self.client.set_registered_model_tag(
            model_name, "owner", owner_email
        )
    
    def add_model_collaborator(self, model_name: str, user_email: str, 
                                permission: str):
        """Add collaborator with specific permission."""
        collaborators = self._get_collaborators(model_name)
        collaborators[user_email] = permission
        self.client.set_registered_model_tag(
            model_name, "collaborators", json.dumps(collaborators)
        )
    
    def check_permission(self, model_name: str, user_email: str, 
                         action: str) -> bool:
        """Check if user has permission for action."""
        # Check if owner
        owner = self.client.get_registered_model(model_name).tags.get('owner')
        if user_email == owner:
            return True
        
        # Check collaborators
        collaborators = self._get_collaborators(model_name)
        user_perm = collaborators.get(user_email)
        
        return self._permission_allows(user_perm, action)
```

### 4.2 Team-Based Access

```yaml
# Model ownership by team
model_teams:
  fraud-detection-model:
    owner_team: fraud-team
    permissions:
      fraud-team: MANAGE
      risk-team: READ
      compliance-team: READ
  
  recommendation-model:
    owner_team: personalization-team
    permissions:
      personalization-team: MANAGE
      product-team: READ
```

---

## 5. Audit Logging

### 5.1 Access Events to Log

| Event | Data Captured |
|-------|---------------|
| Model viewed | user, model, timestamp |
| Model registered | user, model, version, timestamp |
| Artifact downloaded | user, model, version, timestamp |
| Stage transition | user, model, from_stage, to_stage, timestamp |
| Permission changed | admin, target_user, permission, timestamp |

### 5.2 Audit Log Implementation

```python
# auth/audit_log.py
import structlog
from datetime import datetime

logger = structlog.get_logger()

def log_access_event(event_type: str, user: str, resource: str, 
                     details: dict = None):
    """Log access event for audit."""
    logger.info(
        "model_registry_access",
        event_type=event_type,
        user=user,
        resource=resource,
        timestamp=datetime.utcnow().isoformat(),
        details=details or {}
    )

# Usage
log_access_event(
    event_type="model_stage_transition",
    user="user@company.com",
    resource="fraud-model/v5",
    details={
        "from_stage": "Staging",
        "to_stage": "Production",
        "approved_by": "lead@company.com"
    }
)
```

---

## 6. Access Review Process

### 6.1 Quarterly Review Checklist

- [ ] Export current access list
- [ ] Verify all users have appropriate roles
- [ ] Remove access for departed employees
- [ ] Review model ownership assignments
- [ ] Check for unused service accounts
- [ ] Document any exceptions

### 6.2 Access Review Report

```markdown
## Access Review Report - Q[X] [Year]

**Review Date:** [Date]
**Reviewer:** [Name]

### Summary
- Total users with access: [X]
- Users reviewed: [X]
- Access removed: [X]
- Access modified: [X]

### Findings
| User | Current Role | Action | Reason |
|------|--------------|--------|--------|
| user@co.com | ML_LEAD | Remove | Left company |

### Sign-off
- [ ] Security reviewed
- [ ] Compliance reviewed
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial access control |
