---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-028: Audit Trail for ML Models

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-028 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Compliance / ML Platform Lead] |

---

## 1. Audit Trail Overview

### 1.1 Audit Scope

| Category | Events Tracked |
|----------|----------------|
| Model Lifecycle | Registration, transitions, archival, deletion |
| Data Lineage | Training data versions, feature sources |
| Access Events | Views, downloads, modifications |
| Predictions | High-risk model inferences |
| Configuration | Parameter changes, threshold updates |

### 1.2 Retention Requirements

| Data Type | Retention | Storage |
|-----------|-----------|---------|
| Model events | 7 years | S3 + Elasticsearch |
| Prediction logs | 1-7 years (risk-based) | S3 Cold |
| Access logs | 3 years | Elasticsearch |
| Configuration changes | 7 years | Git + S3 |

---

## 2. Event Schema

### 2.1 Standard Audit Event Format

```json
{
  "event_id": "uuid-v4",
  "event_type": "model.stage_transition",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "actor": {
    "user_id": "user@company.com",
    "role": "ML_LEAD",
    "ip_address": "10.0.1.50",
    "user_agent": "mlflow-client/2.10.0"
  },
  "resource": {
    "type": "registered_model_version",
    "model_name": "fraud-detection",
    "version": "5",
    "uri": "models:/fraud-detection/5"
  },
  "action": {
    "operation": "transition_stage",
    "from_state": "Staging",
    "to_state": "Production"
  },
  "context": {
    "experiment_id": "123",
    "run_id": "abc123",
    "approval_ticket": "JIRA-456",
    "reason": "Passed all quality gates"
  },
  "metadata": {
    "source_system": "mlflow",
    "environment": "production"
  }
}
```

### 2.2 Event Types

| Event Type | Description | Risk Level |
|------------|-------------|------------|
| `model.registered` | New model version created | Low |
| `model.stage_transition` | Stage changed | High |
| `model.deleted` | Model removed | Critical |
| `model.accessed` | Model viewed/downloaded | Low |
| `prediction.made` | Inference executed | Medium |
| `config.changed` | Configuration modified | Medium |
| `permission.changed` | Access modified | High |

---

## 3. Implementation

### 3.1 Audit Logger

```python
# audit/logger.py
import json
import uuid
from datetime import datetime
from typing import Dict, Any, Optional
import structlog
from elasticsearch import Elasticsearch
import boto3

class AuditLogger:
    """Centralized audit logging for ML models."""
    
    def __init__(self):
        self.es_client = Elasticsearch([ES_HOST])
        self.s3_client = boto3.client('s3')
        self.logger = structlog.get_logger()
    
    def log_event(
        self,
        event_type: str,
        actor: Dict[str, str],
        resource: Dict[str, str],
        action: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ):
        """Log audit event to all backends."""
        
        event = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "actor": actor,
            "resource": resource,
            "action": action,
            "context": context or {},
            "metadata": {
                "source_system": "mlops-platform",
                "environment": os.environ.get("ENVIRONMENT", "unknown")
            }
        }
        
        # Log to Elasticsearch (hot storage)
        self._log_to_elasticsearch(event)
        
        # Log to S3 (cold storage)
        self._log_to_s3(event)
        
        # Log to structured logger
        self.logger.info("audit_event", **event)
        
        return event["event_id"]
    
    def _log_to_elasticsearch(self, event: Dict):
        """Store in Elasticsearch for querying."""
        index = f"mlops-audit-{datetime.utcnow().strftime('%Y.%m')}"
        self.es_client.index(index=index, body=event)
    
    def _log_to_s3(self, event: Dict):
        """Store in S3 for long-term retention."""
        date = datetime.utcnow()
        key = (f"audit-logs/{date.year}/{date.month:02d}/{date.day:02d}/"
               f"{event['event_id']}.json")
        
        self.s3_client.put_object(
            Bucket=AUDIT_BUCKET,
            Key=key,
            Body=json.dumps(event),
            ContentType='application/json'
        )

# Global instance
audit_logger = AuditLogger()
```

### 3.2 MLflow Integration

```python
# audit/mlflow_hooks.py
from mlflow.tracking import MlflowClient
from audit.logger import audit_logger

class AuditedMlflowClient(MlflowClient):
    """MLflow client with audit logging."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = self._get_current_user()
    
    def transition_model_version_stage(self, name, version, stage, **kwargs):
        """Transition with audit logging."""
        # Get current stage
        model_version = self.get_model_version(name, version)
        from_stage = model_version.current_stage
        
        # Log audit event
        audit_logger.log_event(
            event_type="model.stage_transition",
            actor={
                "user_id": self.current_user,
                "role": self._get_user_role()
            },
            resource={
                "type": "registered_model_version",
                "model_name": name,
                "version": version
            },
            action={
                "operation": "transition_stage",
                "from_state": from_stage,
                "to_state": stage
            },
            context=kwargs.get("context", {})
        )
        
        # Perform actual transition
        return super().transition_model_version_stage(name, version, stage, **kwargs)
    
    def delete_registered_model(self, name):
        """Delete with audit logging."""
        audit_logger.log_event(
            event_type="model.deleted",
            actor={"user_id": self.current_user},
            resource={"type": "registered_model", "model_name": name},
            action={"operation": "delete"}
        )
        return super().delete_registered_model(name)
```

---

## 4. Prediction Audit Trail

### 4.1 High-Risk Model Predictions

```python
# audit/prediction_logger.py
class PredictionAuditLogger:
    """Log predictions for high-risk models."""
    
    def __init__(self, model_name: str, model_tier: int):
        self.model_name = model_name
        self.model_tier = model_tier
        self.should_log = model_tier <= 2  # Tier 1 & 2 only
    
    def log_prediction(
        self,
        request_id: str,
        input_hash: str,
        output: Any,
        latency_ms: float,
        user_context: Optional[Dict] = None
    ):
        """Log prediction for audit."""
        if not self.should_log:
            return
        
        audit_logger.log_event(
            event_type="prediction.made",
            actor=user_context or {"user_id": "system"},
            resource={
                "type": "model_prediction",
                "model_name": self.model_name
            },
            action={
                "operation": "predict",
                "input_hash": input_hash,  # Hash, not raw data
                "output_summary": self._summarize_output(output),
                "latency_ms": latency_ms
            },
            context={
                "request_id": request_id
            }
        )
    
    def _summarize_output(self, output) -> Dict:
        """Summarize output without storing sensitive data."""
        return {
            "prediction_class": str(output.get("class", "N/A")),
            "confidence": float(output.get("confidence", 0))
        }
```

---

## 5. Querying Audit Logs

### 5.1 Elasticsearch Queries

```python
# audit/queries.py
def get_model_history(model_name: str, days: int = 90) -> list:
    """Get audit history for a model."""
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"resource.model_name": model_name}},
                    {"range": {"timestamp": {"gte": f"now-{days}d"}}}
                ]
            }
        },
        "sort": [{"timestamp": "desc"}]
    }
    return es_client.search(index="mlops-audit-*", body=query)

def get_user_activity(user_id: str, days: int = 30) -> list:
    """Get user's audit trail."""
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"actor.user_id": user_id}},
                    {"range": {"timestamp": {"gte": f"now-{days}d"}}}
                ]
            }
        }
    }
    return es_client.search(index="mlops-audit-*", body=query)

def get_production_deployments(days: int = 7) -> list:
    """Get recent production deployments."""
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"event_type": "model.stage_transition"}},
                    {"match": {"action.to_state": "Production"}},
                    {"range": {"timestamp": {"gte": f"now-{days}d"}}}
                ]
            }
        }
    }
    return es_client.search(index="mlops-audit-*", body=query)
```

---

## 6. Audit Reports

### 6.1 Monthly Audit Report Template

```markdown
## ML Model Audit Report - [Month Year]

### Summary
- Total audit events: [X]
- Models registered: [X]
- Production deployments: [X]
- Models archived: [X]

### Production Deployments
| Date | Model | Version | Deployed By | Approval |
|------|-------|---------|-------------|----------|
| [Date] | [Model] | [Ver] | [User] | [Ticket] |

### Access Anomalies
| Date | User | Event | Risk |
|------|------|-------|------|
| [Date] | [User] | [Event] | [Level] |

### Compliance Status
- [ ] All Tier 1 models have audit trails
- [ ] Prediction logging active for high-risk models
- [ ] Retention policies enforced
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial audit trail |
