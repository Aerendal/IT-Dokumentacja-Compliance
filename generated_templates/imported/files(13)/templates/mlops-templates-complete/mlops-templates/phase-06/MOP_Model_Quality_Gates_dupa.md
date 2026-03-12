---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-024: Model Quality Gates

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-024 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML QA Lead] |

---

## 1. Quality Gate Overview

### 1.1 Gate Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Model Quality Gates                           │
│                                                                 │
│  Training ──► Gate 1 ──► Staging ──► Gate 2 ──► Production     │
│              (Auto)                   (Manual)                  │
│                                                                 │
│  Gate 1: Registration Gate    Gate 2: Production Gate          │
│  • Performance baseline       • A/B test results               │
│  • Data quality              • Fairness validation             │
│  • Schema validation         • Security review                 │
│  • Unit tests pass           • Load test pass                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Gate 1: Model Registration Gate

### 2.1 Criteria

| Criterion | Threshold | Blocking |
|-----------|-----------|----------|
| Accuracy | ≥ baseline - 2% | Yes |
| F1 Score | ≥ baseline - 2% | Yes |
| AUC-ROC | ≥ baseline - 1% | Yes |
| Unit tests | 100% pass | Yes |
| Data quality | No critical issues | Yes |
| Model size | ≤ 500MB | No |
| Inference time | ≤ 100ms | No |

### 2.2 Implementation

```python
# quality_gates/registration_gate.py
from dataclasses import dataclass
from typing import Dict, Optional
import mlflow

@dataclass
class GateResult:
    passed: bool
    criteria_results: Dict[str, bool]
    message: str

class RegistrationGate:
    """Gate 1: Model registration quality gate."""
    
    def __init__(self, model_name: str, version: str):
        self.model_name = model_name
        self.version = version
        self.client = mlflow.tracking.MlflowClient()
    
    def evaluate(self) -> GateResult:
        """Evaluate all gate criteria."""
        results = {}
        
        # Get model metrics
        model_version = self.client.get_model_version(
            self.model_name, self.version
        )
        run = self.client.get_run(model_version.run_id)
        metrics = run.data.metrics
        
        # Get baseline metrics
        baseline = self._get_baseline_metrics()
        
        # Criterion 1: Performance vs baseline
        results['accuracy'] = metrics['accuracy'] >= baseline['accuracy'] - 0.02
        results['f1'] = metrics['f1'] >= baseline['f1'] - 0.02
        results['auc_roc'] = metrics['auc_roc'] >= baseline['auc_roc'] - 0.01
        
        # Criterion 2: Unit tests
        results['unit_tests'] = self._check_unit_tests(model_version.run_id)
        
        # Criterion 3: Data quality
        results['data_quality'] = self._check_data_quality(model_version.run_id)
        
        # Determine overall pass/fail
        blocking_criteria = ['accuracy', 'f1', 'auc_roc', 'unit_tests', 'data_quality']
        passed = all(results.get(c, False) for c in blocking_criteria)
        
        message = self._generate_message(results)
        
        return GateResult(passed=passed, criteria_results=results, message=message)
    
    def _get_baseline_metrics(self) -> Dict[str, float]:
        """Get baseline from current production model."""
        try:
            prod_version = self.client.get_latest_versions(
                self.model_name, stages=["Production"]
            )[0]
            run = self.client.get_run(prod_version.run_id)
            return run.data.metrics
        except:
            # Default baseline if no production model
            return {'accuracy': 0.90, 'f1': 0.85, 'auc_roc': 0.95}
    
    def _check_unit_tests(self, run_id: str) -> bool:
        """Check if unit tests passed."""
        run = self.client.get_run(run_id)
        return run.data.tags.get('unit_tests_passed', 'false') == 'true'
    
    def _check_data_quality(self, run_id: str) -> bool:
        """Check data quality report."""
        run = self.client.get_run(run_id)
        return run.data.tags.get('data_quality_passed', 'false') == 'true'
    
    def _generate_message(self, results: Dict[str, bool]) -> str:
        """Generate human-readable message."""
        failed = [k for k, v in results.items() if not v]
        if not failed:
            return " All registration gate criteria passed"
        return f" Failed criteria: {', '.join(failed)}"
```

---

## 3. Gate 2: Production Gate

### 3.1 Criteria

| Criterion | Threshold | Blocking |
|-----------|-----------|----------|
| Staging validation | Pass | Yes |
| Fairness metrics | Demographic parity ≥ 0.8 | Yes |
| Load test | P99 < 100ms at 1000 RPS | Yes |
| Security scan | No critical vulnerabilities | Yes |
| A/B test (if applicable) | Statistically significant | No |
| Model documentation | Complete | Yes |
| Approval | Manager sign-off | Yes |

### 3.2 Implementation

```python
# quality_gates/production_gate.py
class ProductionGate:
    """Gate 2: Production deployment quality gate."""
    
    REQUIRED_APPROVERS = ['ml_lead', 'qa_lead']
    
    def __init__(self, model_name: str, version: str):
        self.model_name = model_name
        self.version = version
        self.client = mlflow.tracking.MlflowClient()
    
    def evaluate(self) -> GateResult:
        """Evaluate production gate criteria."""
        results = {}
        
        # Criterion 1: Staging validation passed
        results['staging_validation'] = self._check_staging_validation()
        
        # Criterion 2: Fairness metrics
        results['fairness'] = self._check_fairness_metrics()
        
        # Criterion 3: Load test
        results['load_test'] = self._check_load_test()
        
        # Criterion 4: Security scan
        results['security'] = self._check_security_scan()
        
        # Criterion 5: Documentation
        results['documentation'] = self._check_documentation()
        
        # Criterion 6: Approvals
        results['approvals'] = self._check_approvals()
        
        blocking = ['staging_validation', 'fairness', 'load_test', 
                    'security', 'documentation', 'approvals']
        passed = all(results.get(c, False) for c in blocking)
        
        return GateResult(
            passed=passed,
            criteria_results=results,
            message=self._generate_message(results)
        )
    
    def _check_fairness_metrics(self) -> bool:
        """Check fairness metrics meet thresholds."""
        model_version = self.client.get_model_version(
            self.model_name, self.version
        )
        run = self.client.get_run(model_version.run_id)
        
        demographic_parity = float(
            run.data.metrics.get('demographic_parity', 0)
        )
        equalized_odds = float(
            run.data.metrics.get('equalized_odds', 0)
        )
        
        return demographic_parity >= 0.8 and equalized_odds >= 0.8
    
    def _check_load_test(self) -> bool:
        """Check load test results."""
        # Query load test results from test system
        load_test_results = self._get_load_test_results()
        
        return (
            load_test_results['p99_latency_ms'] < 100 and
            load_test_results['rps'] >= 1000 and
            load_test_results['error_rate'] < 0.01
        )
    
    def _check_approvals(self) -> bool:
        """Check required approvals are in place."""
        model_version = self.client.get_model_version(
            self.model_name, self.version
        )
        
        approvals = model_version.tags.get('approvals', '').split(',')
        return all(req in approvals for req in self.REQUIRED_APPROVERS)
```

---

## 4. Gate Automation

### 4.1 CI/CD Integration

```yaml
# .github/workflows/quality-gates.yml
name: Quality Gates

on:
  workflow_call:
    inputs:
      model_name:
        required: true
        type: string
      model_version:
        required: true
        type: string
      gate:
        required: true
        type: string  # 'registration' or 'production'

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Quality Gate
        id: gate
        run: |
          python -c "
          from quality_gates import ${gate}Gate
          gate = ${gate}Gate('${{ inputs.model_name }}', '${{ inputs.model_version }}')
          result = gate.evaluate()
          print(f'::set-output name=passed::{result.passed}')
          print(result.message)
          "
      
      - name: Gate Decision
        if: steps.gate.outputs.passed != 'true'
        run: |
          echo "Quality gate failed!"
          exit 1
      
      - name: Promote Model
        if: steps.gate.outputs.passed == 'true' && inputs.gate == 'registration'
        run: |
          mlflow models transition-stage \
            --name ${{ inputs.model_name }} \
            --version ${{ inputs.model_version }} \
            --stage Staging
```

### 4.2 Webhook Trigger

```python
# webhooks/model_registered.py
@app.route('/webhooks/model-registered', methods=['POST'])
def on_model_registered():
    """Trigger registration gate on model registration."""
    data = request.json
    model_name = data['model_name']
    version = data['version']
    
    # Run registration gate
    gate = RegistrationGate(model_name, version)
    result = gate.evaluate()
    
    if result.passed:
        # Auto-transition to staging
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            model_name, version, "Staging"
        )
        notify_slack(f" {model_name} v{version} passed registration gate")
    else:
        notify_slack(f" {model_name} v{version} failed: {result.message}")
    
    return jsonify(result.__dict__)
```

---

## 5. Gate Dashboard

### 5.1 Metrics to Track

| Metric | Description |
|--------|-------------|
| Gate pass rate | % of models passing each gate |
| Mean time to pass | Average time to clear gates |
| Failure reasons | Distribution of failure causes |
| Rework rate | Models requiring multiple attempts |

### 5.2 Grafana Dashboard Query

```promql
# Gate pass rate
sum(quality_gate_passed{gate="registration"}) / 
sum(quality_gate_evaluated{gate="registration"})

# Failure reasons
topk(5, sum by (reason) (quality_gate_failures))
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial gates |
