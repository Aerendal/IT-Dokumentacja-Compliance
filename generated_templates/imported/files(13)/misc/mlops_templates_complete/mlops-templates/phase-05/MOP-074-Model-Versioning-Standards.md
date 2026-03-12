---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-074: Model Versioning Standards

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-074 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Versioning Scheme

### 1.1 Semantic Versioning for Models

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
- 1.0.0          - First production release
- 1.1.0          - New features, backward compatible
- 1.1.1          - Bug fix
- 2.0.0          - Breaking changes
- 2.0.0-beta.1   - Pre-release
- 2.0.0+20240115 - Build metadata
```

### 1.2 Version Increment Rules

| Change Type | Version Increment | Examples |
|-------------|-------------------|----------|
| Algorithm change | MAJOR | New model architecture |
| Feature schema change | MAJOR | Input/output schema change |
| New features added | MINOR | Additional input features |
| Performance improvement | MINOR | Better accuracy, same interface |
| Bug fix | PATCH | Fix prediction bug |
| Retraining (same data) | PATCH | Refresh with same config |
| Retraining (new data) | MINOR | Updated training data |

---

## 2. Version Metadata

### 2.1 Required Metadata

```yaml
# model_version_metadata.yaml
version: "2.1.0"
model_name: "fraud-detection"
created_at: "2024-01-15T10:30:00Z"
created_by: "user@company.com"

# Version context
previous_version: "2.0.1"
changelog: "Added new transaction velocity features"

# Training context
training:
  run_id: "abc123def456"
  experiment_id: "42"
  data_version: "v2024.01.15"
  framework: "xgboost"
  framework_version: "1.7.6"

# Performance
metrics:
  accuracy: 0.952
  precision: 0.941
  recall: 0.923
  f1: 0.932
  auc_roc: 0.978

# Schema
input_schema:
  type: "object"
  properties:
    amount:
      type: "number"
    user_age_days:
      type: "integer"
  required: ["amount", "user_age_days"]

output_schema:
  type: "object"
  properties:
    prediction:
      type: "integer"
      enum: [0, 1]
    probability:
      type: "number"

# Compatibility
compatible_with:
  min_serving_version: "1.0.0"
  max_serving_version: "2.x"
```

### 2.2 MLflow Version Tags

```python
def set_version_tags(client, model_name: str, version: str, metadata: dict):
    """Set standard version tags in MLflow."""
    
    # Core version info
    client.set_model_version_tag(model_name, version, "version.semantic", metadata['version'])
    client.set_model_version_tag(model_name, version, "version.previous", metadata['previous_version'])
    client.set_model_version_tag(model_name, version, "version.changelog", metadata['changelog'])
    
    # Training info
    client.set_model_version_tag(model_name, version, "training.run_id", metadata['training']['run_id'])
    client.set_model_version_tag(model_name, version, "training.data_version", metadata['training']['data_version'])
    client.set_model_version_tag(model_name, version, "training.framework", metadata['training']['framework'])
    
    # Performance
    for metric, value in metadata['metrics'].items():
        client.set_model_version_tag(model_name, version, f"metrics.{metric}", str(value))
```

---

## 3. Version Lifecycle

### 3.1 Lifecycle Stages

```
┌─────────────────────────────────────────────────────────────────┐
│                    Model Version Lifecycle                       │
│                                                                 │
│  ┌──────┐    ┌─────────┐    ┌────────────┐    ┌────────────┐  │
│  │ None │───►│ Staging │───►│ Production │───►│  Archived  │  │
│  └──────┘    └─────────┘    └────────────┘    └────────────┘  │
│     │             │               │                 │          │
│     │        Auto on          Requires           Auto or       │
│     │       registration      approval           manual        │
│     │                                                          │
│     └──────────────────────► Deleted (experimental only)       │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Stage Transitions

```python
# versioning/transitions.py
from enum import Enum
from datetime import datetime

class ModelStage(Enum):
    NONE = "None"
    STAGING = "Staging"
    PRODUCTION = "Production"
    ARCHIVED = "Archived"

ALLOWED_TRANSITIONS = {
    ModelStage.NONE: [ModelStage.STAGING, ModelStage.ARCHIVED],
    ModelStage.STAGING: [ModelStage.PRODUCTION, ModelStage.ARCHIVED],
    ModelStage.PRODUCTION: [ModelStage.ARCHIVED],
    ModelStage.ARCHIVED: [],  # Terminal state
}

def transition_model_version(
    model_name: str, 
    version: str, 
    target_stage: ModelStage,
    reason: str,
    approved_by: str = None
) -> bool:
    """Transition model version to new stage."""
    client = MlflowClient()
    
    current = client.get_model_version(model_name, version)
    current_stage = ModelStage(current.current_stage)
    
    # Validate transition
    if target_stage not in ALLOWED_TRANSITIONS[current_stage]:
        raise ValueError(f"Cannot transition from {current_stage} to {target_stage}")
    
    # Production requires approval
    if target_stage == ModelStage.PRODUCTION and not approved_by:
        raise ValueError("Production transition requires approval")
    
    # Perform transition
    client.transition_model_version_stage(
        model_name, version, target_stage.value,
        archive_existing_versions=(target_stage == ModelStage.PRODUCTION)
    )
    
    # Log transition
    client.set_model_version_tag(model_name, version, "transition.timestamp", datetime.utcnow().isoformat())
    client.set_model_version_tag(model_name, version, "transition.reason", reason)
    if approved_by:
        client.set_model_version_tag(model_name, version, "transition.approved_by", approved_by)
    
    return True
```

---

## 4. Version Comparison

### 4.1 Comparison Report

```python
# versioning/compare.py
def compare_versions(model_name: str, version_a: str, version_b: str) -> dict:
    """Compare two model versions."""
    client = MlflowClient()
    
    v_a = client.get_model_version(model_name, version_a)
    v_b = client.get_model_version(model_name, version_b)
    
    # Get metrics from runs
    run_a = client.get_run(v_a.run_id)
    run_b = client.get_run(v_b.run_id)
    
    comparison = {
        "model_name": model_name,
        "versions": [version_a, version_b],
        "metrics_comparison": {},
        "parameter_diff": {},
        "created_at": [v_a.creation_timestamp, v_b.creation_timestamp]
    }
    
    # Compare metrics
    all_metrics = set(run_a.data.metrics.keys()) | set(run_b.data.metrics.keys())
    for metric in all_metrics:
        val_a = run_a.data.metrics.get(metric)
        val_b = run_b.data.metrics.get(metric)
        
        comparison["metrics_comparison"][metric] = {
            version_a: val_a,
            version_b: val_b,
            "diff": (val_b - val_a) if val_a and val_b else None,
            "diff_pct": ((val_b - val_a) / val_a * 100) if val_a and val_b else None
        }
    
    return comparison
```

---

## 5. Deprecation Policy

### 5.1 Deprecation Timeline

| Phase | Duration | Actions |
|-------|----------|---------|
| Active | Current | Full support |
| Deprecated | 30 days | Warning in logs, no new deployments |
| Sunset | 30 days | No support, migration required |
| Archived | Permanent | Removed from serving, retained in registry |

### 5.2 Deprecation Process

```python
def deprecate_version(model_name: str, version: str, reason: str, sunset_date: str):
    """Mark version as deprecated."""
    client = MlflowClient()
    
    # Add deprecation tags
    client.set_model_version_tag(model_name, version, "deprecated", "true")
    client.set_model_version_tag(model_name, version, "deprecated.reason", reason)
    client.set_model_version_tag(model_name, version, "deprecated.date", datetime.utcnow().isoformat())
    client.set_model_version_tag(model_name, version, "deprecated.sunset_date", sunset_date)
    
    # Update description
    current_desc = client.get_model_version(model_name, version).description or ""
    client.update_model_version(
        model_name, version,
        description=f" DEPRECATED: {reason}\nSunset: {sunset_date}\n\n{current_desc}"
    )
```

---

## 6. Version Inventory

### 6.1 Active Versions Report

```sql
-- Query for active model versions
SELECT 
    model_name,
    version,
    current_stage,
    creation_timestamp,
    tags->>'metrics.accuracy' as accuracy,
    tags->>'training.data_version' as data_version,
    CASE WHEN tags->>'deprecated' = 'true' THEN 'Yes' ELSE 'No' END as deprecated
FROM model_versions
WHERE current_stage IN ('Staging', 'Production')
ORDER BY model_name, version DESC;
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial versioning standards |
