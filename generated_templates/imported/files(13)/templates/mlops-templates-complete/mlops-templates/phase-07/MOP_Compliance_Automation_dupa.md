---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-030: Compliance Automation

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-030 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Compliance / ML Platform Lead] |

---

## 1. Compliance Automation Overview

### 1.1 Automated Checks

| Check | Trigger | Frequency |
|-------|---------|-----------|
| Model documentation completeness | On registration | Every model |
| Bias/fairness testing | Before promotion | Every model |
| Data lineage validation | On training | Every run |
| Security scan | On build | Every deployment |
| Access review | Scheduled | Quarterly |
| Retention policy enforcement | Scheduled | Daily |

---

## 2. Model Documentation Compliance

### 2.1 Documentation Validator

```python
# compliance/doc_validator.py
from dataclasses import dataclass
from typing import List, Optional
import mlflow

@dataclass
class ValidationResult:
    passed: bool
    missing_fields: List[str]
    warnings: List[str]

class ModelDocumentationValidator:
    """Validate model documentation completeness."""
    
    REQUIRED_FIELDS = {
        'tier_1': [
            'model_type', 'framework', 'owner', 'tier',
            'training_data_version', 'intended_use', 'limitations',
            'fairness_metrics', 'ethical_review_date', 'approved_by'
        ],
        'tier_2': [
            'model_type', 'framework', 'owner', 'tier',
            'training_data_version', 'intended_use'
        ],
        'tier_3': [
            'model_type', 'framework', 'owner', 'tier'
        ]
    }
    
    def validate(self, model_name: str, version: str) -> ValidationResult:
        """Validate model documentation."""
        client = mlflow.tracking.MlflowClient()
        model_version = client.get_model_version(model_name, version)
        
        # Get tier
        tier = model_version.tags.get('tier', '3')
        required = self.REQUIRED_FIELDS.get(f'tier_{tier}', [])
        
        # Check fields
        missing = []
        warnings = []
        
        for field in required:
            if field not in model_version.tags:
                missing.append(field)
        
        # Check optional but recommended
        if 'performance_baseline' not in model_version.tags:
            warnings.append('performance_baseline not set')
        
        return ValidationResult(
            passed=len(missing) == 0,
            missing_fields=missing,
            warnings=warnings
        )
```

### 2.2 CI/CD Integration

```yaml
# .github/workflows/compliance-check.yml
name: Compliance Check

on:
  workflow_call:
    inputs:
      model_name:
        required: true
        type: string
      version:
        required: true
        type: string

jobs:
  documentation-check:
    runs-on: ubuntu-latest
    steps:
      - name: Validate Documentation
        run: |
          python -c "
          from compliance.doc_validator import ModelDocumentationValidator
          validator = ModelDocumentationValidator()
          result = validator.validate('${{ inputs.model_name }}', '${{ inputs.version }}')
          if not result.passed:
              print(f'Missing fields: {result.missing_fields}')
              exit(1)
          print('Documentation validation passed')
          "
```

---

## 3. Fairness Compliance Automation

### 3.1 Automated Fairness Testing

```python
# compliance/fairness_checker.py
from fairlearn.metrics import MetricFrame, demographic_parity_difference
from sklearn.metrics import accuracy_score
import pandas as pd

class FairnessComplianceChecker:
    """Automated fairness compliance checks."""
    
    THRESHOLDS = {
        'demographic_parity': 0.8,
        'equalized_odds': 0.8,
        'max_disparity': 0.2
    }
    
    def check_fairness(
        self,
        y_true: pd.Series,
        y_pred: pd.Series,
        sensitive_features: pd.DataFrame
    ) -> dict:
        """Run fairness compliance checks."""
        results = {}
        
        for feature in sensitive_features.columns:
            metric_frame = MetricFrame(
                metrics={'accuracy': accuracy_score},
                y_true=y_true,
                y_pred=y_pred,
                sensitive_features=sensitive_features[feature]
            )
            
            # Calculate metrics
            dp_diff = demographic_parity_difference(
                y_true, y_pred,
                sensitive_features=sensitive_features[feature]
            )
            
            group_metrics = metric_frame.by_group
            min_acc = group_metrics['accuracy'].min()
            max_acc = group_metrics['accuracy'].max()
            disparity = max_acc - min_acc
            
            results[feature] = {
                'demographic_parity': 1 - abs(dp_diff),
                'min_group_accuracy': min_acc,
                'max_disparity': disparity,
                'passed': (
                    1 - abs(dp_diff) >= self.THRESHOLDS['demographic_parity'] and
                    disparity <= self.THRESHOLDS['max_disparity']
                )
            }
        
        return {
            'overall_passed': all(r['passed'] for r in results.values()),
            'by_feature': results
        }
    
    def generate_report(self, results: dict) -> str:
        """Generate compliance report."""
        report = ["# Fairness Compliance Report\n"]
        report.append(f"**Overall Status:** {' PASSED' if results['overall_passed'] else ' FAILED'}\n")
        
        for feature, metrics in results['by_feature'].items():
            status = '' if metrics['passed'] else ''
            report.append(f"\n## {feature} {status}")
            report.append(f"- Demographic Parity: {metrics['demographic_parity']:.3f}")
            report.append(f"- Max Disparity: {metrics['max_disparity']:.3f}")
        
        return '\n'.join(report)
```

### 3.2 Fairness Gate Integration

```python
# compliance/fairness_gate.py
def fairness_quality_gate(model_uri: str, test_data_path: str) -> bool:
    """Quality gate for fairness compliance."""
    import mlflow
    
    # Load model and test data
    model = mlflow.pyfunc.load_model(model_uri)
    test_df = pd.read_parquet(test_data_path)
    
    # Get predictions
    X = test_df.drop(['label', 'gender', 'age_group'], axis=1)
    y_true = test_df['label']
    y_pred = model.predict(X)
    
    # Run fairness check
    checker = FairnessComplianceChecker()
    results = checker.check_fairness(
        y_true, y_pred,
        test_df[['gender', 'age_group']]
    )
    
    # Log results to MLflow
    mlflow.log_dict(results, "fairness_compliance.json")
    mlflow.log_text(checker.generate_report(results), "fairness_report.md")
    
    return results['overall_passed']
```

---

## 4. Data Lineage Compliance

### 4.1 Lineage Validator

```python
# compliance/lineage_validator.py
class DataLineageValidator:
    """Validate data lineage for compliance."""
    
    def validate_training_lineage(self, run_id: str) -> dict:
        """Validate training data lineage is documented."""
        client = mlflow.tracking.MlflowClient()
        run = client.get_run(run_id)
        
        required_lineage = [
            'data_source',
            'data_version',
            'data_hash',
            'feature_store_version',
            'preprocessing_version'
        ]
        
        missing = []
        for field in required_lineage:
            if field not in run.data.params:
                missing.append(field)
        
        return {
            'passed': len(missing) == 0,
            'missing': missing,
            'lineage': {k: v for k, v in run.data.params.items() 
                       if k in required_lineage}
        }
```

---

## 5. Retention Policy Automation

### 5.1 Retention Enforcer

```python
# compliance/retention_enforcer.py
from datetime import datetime, timedelta

class RetentionPolicyEnforcer:
    """Automate data retention policy enforcement."""
    
    RETENTION_POLICIES = {
        'model_artifacts': timedelta(days=7*365),  # 7 years
        'experiment_data': timedelta(days=3*365),  # 3 years
        'inference_logs': timedelta(days=365),     # 1 year
        'temp_data': timedelta(days=30),           # 30 days
    }
    
    def enforce_policies(self, dry_run: bool = True) -> dict:
        """Enforce retention policies."""
        results = {'deleted': [], 'archived': [], 'errors': []}
        
        for data_type, retention in self.RETENTION_POLICIES.items():
            cutoff = datetime.now() - retention
            
            if data_type == 'experiment_data':
                self._process_experiments(cutoff, results, dry_run)
            elif data_type == 'inference_logs':
                self._process_inference_logs(cutoff, results, dry_run)
        
        return results
    
    def _process_experiments(self, cutoff: datetime, results: dict, 
                             dry_run: bool):
        """Archive old experiments."""
        client = mlflow.tracking.MlflowClient()
        
        for exp in client.search_experiments():
            # Check last activity
            runs = client.search_runs(
                exp.experiment_id,
                order_by=["start_time DESC"],
                max_results=1
            )
            
            if runs and runs[0].info.start_time < cutoff.timestamp() * 1000:
                if not dry_run:
                    # Archive experiment
                    self._archive_experiment(exp.experiment_id)
                results['archived'].append(exp.name)
```

### 5.2 Retention Cron Job

```yaml
# k8s/retention-enforcer-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: retention-policy-enforcer
  namespace: mlops
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: enforcer
            image: mlops/compliance-tools:latest
            command:
              - python
              - -m
              - compliance.retention_enforcer
            env:
            - name: DRY_RUN
              value: "false"
          restartPolicy: OnFailure
```

---

## 6. Compliance Dashboard

### 6.1 Metrics

```yaml
# prometheus/compliance-metrics.yaml
groups:
  - name: compliance
    rules:
      - record: compliance_models_documented_ratio
        expr: |
          sum(model_documentation_complete{tier="1"}) / 
          count(model_documentation_complete{tier="1"})
      
      - record: compliance_fairness_passing_ratio
        expr: |
          sum(fairness_check_passed) / count(fairness_check_passed)
      
      - alert: ComplianceViolation
        expr: compliance_models_documented_ratio < 1
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "Tier 1 models missing documentation"
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial automation |
