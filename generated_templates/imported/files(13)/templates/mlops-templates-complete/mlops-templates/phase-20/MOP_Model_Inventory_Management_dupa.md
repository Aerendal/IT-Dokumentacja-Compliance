---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-086: Model Inventory Management

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-086 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Governance] |

---

## 1. Model Inventory Overview

### 1.1 Inventory Scope

| Category | Included | Example |
|----------|----------|---------|
| Production Models |  | fraud-detection v2.1 |
| Staging Models |  | churn-prediction v3.0-beta |
| Archived Models |  | fraud-detection v1.x |
| Experimental |  | research experiments |

### 1.2 Required Metadata

| Field | Required | Description |
|-------|----------|-------------|
| Model Name |  | Unique identifier |
| Version |  | Semantic version |
| Tier |  | Risk classification (1-4) |
| Owner |  | Responsible team/individual |
| Stage |  | Current lifecycle stage |
| Created Date |  | Registration date |
| Last Updated |  | Last modification |
| Business Domain |  | Fraud, Recommendations, etc. |
| Description |  | Purpose and use case |
| Dependencies |  | Feature views, data sources |

---

## 2. Inventory System

### 2.1 MLflow-Based Inventory

```python
# inventory/model_inventory.py
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import mlflow

@dataclass
class ModelRecord:
    name: str
    version: str
    tier: int
    owner: str
    stage: str
    created_at: datetime
    description: str
    business_domain: str
    dependencies: List[str]
    metrics: dict
    
    @classmethod
    def from_mlflow_version(cls, model_name: str, version_info):
        """Create record from MLflow model version."""
        tags = version_info.tags or {}
        
        return cls(
            name=model_name,
            version=version_info.version,
            tier=int(tags.get('tier', 4)),
            owner=tags.get('owner', 'unknown'),
            stage=version_info.current_stage,
            created_at=datetime.fromtimestamp(version_info.creation_timestamp / 1000),
            description=version_info.description or '',
            business_domain=tags.get('business_domain', 'unclassified'),
            dependencies=tags.get('dependencies', '').split(','),
            metrics={k: v for k, v in tags.items() if k.startswith('metrics.')}
        )

class ModelInventory:
    """Manage model inventory."""
    
    def __init__(self):
        self.client = mlflow.tracking.MlflowClient()
    
    def get_all_models(self) -> List[ModelRecord]:
        """Get all registered models."""
        records = []
        
        for model in self.client.search_registered_models():
            for version in self.client.search_model_versions(f"name='{model.name}'"):
                records.append(ModelRecord.from_mlflow_version(model.name, version))
        
        return records
    
    def get_production_models(self) -> List[ModelRecord]:
        """Get all production models."""
        return [m for m in self.get_all_models() if m.stage == "Production"]
    
    def get_models_by_tier(self, tier: int) -> List[ModelRecord]:
        """Get models by risk tier."""
        return [m for m in self.get_all_models() if m.tier == tier]
    
    def get_models_by_owner(self, owner: str) -> List[ModelRecord]:
        """Get models by owner."""
        return [m for m in self.get_all_models() if m.owner == owner]
    
    def generate_inventory_report(self) -> str:
        """Generate inventory report."""
        models = self.get_all_models()
        
        report = "# Model Inventory Report\n\n"
        report += f"**Generated:** {datetime.now().isoformat()}\n"
        report += f"**Total Models:** {len(set(m.name for m in models))}\n"
        report += f"**Total Versions:** {len(models)}\n\n"
        
        # By stage
        report += "## By Stage\n\n"
        for stage in ["Production", "Staging", "Archived"]:
            count = len([m for m in models if m.stage == stage])
            report += f"- {stage}: {count}\n"
        
        # By tier
        report += "\n## By Tier\n\n"
        for tier in [1, 2, 3, 4]:
            count = len([m for m in models if m.tier == tier])
            report += f"- Tier {tier}: {count}\n"
        
        # Production models table
        report += "\n## Production Models\n\n"
        report += "| Model | Version | Tier | Owner | Domain |\n"
        report += "|-------|---------|------|-------|--------|\n"
        
        for m in self.get_production_models():
            report += f"| {m.name} | {m.version} | {m.tier} | {m.owner} | {m.business_domain} |\n"
        
        return report
```

### 2.2 Inventory Dashboard

```promql
# Total models by stage
count by (stage) (mlflow_model_versions)

# Models by tier
count by (tier) (mlflow_model_versions{stage="Production"})

# Models needing review (older than 90 days)
mlflow_model_versions{stage="Production"} 
unless 
mlflow_model_versions{last_reviewed_days < 90}
```

---

## 3. Inventory Compliance

### 3.1 Required Documentation Check

```python
# inventory/compliance_check.py
def check_model_compliance(model_name: str, version: str) -> dict:
    """Check if model meets inventory requirements."""
    client = mlflow.tracking.MlflowClient()
    mv = client.get_model_version(model_name, version)
    tags = mv.tags or {}
    
    checks = {
        'has_owner': 'owner' in tags and tags['owner'] != '',
        'has_tier': 'tier' in tags,
        'has_description': mv.description is not None and len(mv.description) > 10,
        'has_business_domain': 'business_domain' in tags,
        'has_model_card': 'model_card_url' in tags,
        'has_dependencies': 'dependencies' in tags,
    }
    
    return {
        'model': model_name,
        'version': version,
        'checks': checks,
        'compliant': all(checks.values()),
        'missing': [k for k, v in checks.items() if not v]
    }

def audit_inventory_compliance():
    """Audit all production models for compliance."""
    inventory = ModelInventory()
    results = []
    
    for model in inventory.get_production_models():
        result = check_model_compliance(model.name, model.version)
        results.append(result)
    
    compliant = sum(1 for r in results if r['compliant'])
    
    print(f"Compliance: {compliant}/{len(results)} ({compliant/len(results)*100:.1f}%)")
    
    for r in results:
        if not r['compliant']:
            print(f"   {r['model']} v{r['version']}: Missing {r['missing']}")
    
    return results
```

---

## 4. Quarterly Review

### 4.1 Review Checklist

```markdown
## Quarterly Model Inventory Review

**Quarter:** Q_ 20__
**Reviewer:** ___________
**Date:** ___________

### Summary
- Total production models: ___
- Models reviewed: ___
- Models archived: ___
- New models: ___

### Review Actions

| Model | Action | Reason |
|-------|--------|--------|
| |  Keep /  Archive /  Review | |

### Compliance Issues
- [ ] All models have current owners
- [ ] All Tier 1/2 models reviewed in last quarter
- [ ] No orphaned models (owner left company)
- [ ] Documentation up to date

### Sign-off
- Reviewer: ___________
- ML Lead: ___________
```

---

## 5. Automated Reports

### 5.1 Weekly Inventory Email

```python
# inventory/weekly_report.py
def send_weekly_inventory_report():
    """Send weekly inventory summary."""
    inventory = ModelInventory()
    
    production = inventory.get_production_models()
    tier1 = [m for m in production if m.tier == 1]
    
    # Check for issues
    old_models = [m for m in production 
                  if (datetime.now() - m.created_at).days > 180]
    
    email_body = f"""
    Weekly Model Inventory Summary
    ==============================
    
    Production Models: {len(production)}
    - Tier 1 (Critical): {len(tier1)}
    
    Attention Required:
    - Models > 6 months old: {len(old_models)}
    
    View full inventory: https://mlflow.example.com/models
    """
    
    send_email(
        to="ml-team@company.com",
        subject="Weekly Model Inventory Summary",
        body=email_body
    )
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial inventory management |
