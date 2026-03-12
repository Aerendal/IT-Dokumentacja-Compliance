---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-091: Model Security Scanning

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-091 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Security / ML Platform] |

---

## 1. Security Scanning Overview

### 1.1 Scan Types

| Scan Type | What it Checks | When |
|-----------|---------------|------|
| Dependency Scan | Vulnerable packages | Every build |
| Model Artifact Scan | Pickle exploits, malicious code | Before registration |
| Container Scan | Image vulnerabilities | Before deployment |
| API Security | Input validation, auth | Before production |

### 1.2 Severity Levels

| Level | Response | Block Deployment |
|-------|----------|------------------|
| Critical | Immediate fix | Yes |
| High | Fix within 7 days | Yes |
| Medium | Fix within 30 days | No |
| Low | Fix in next release | No |

---

## 2. Dependency Scanning

### 2.1 Safety Check

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  dependency-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install safety
        run: pip install safety
      
      - name: Check dependencies
        run: |
          pip install -r requirements.txt
          safety check --full-report --output json > safety-report.json
      
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: safety-report
          path: safety-report.json
      
      - name: Fail on critical
        run: |
          if grep -q '"severity": "critical"' safety-report.json; then
            echo "Critical vulnerability found!"
            exit 1
          fi
```

### 2.2 Bandit Static Analysis

```yaml
  static-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Bandit
        run: |
          pip install bandit
          bandit -r src/ -f json -o bandit-report.json || true
      
      - name: Check for high severity
        run: |
          python -c "
          import json
          with open('bandit-report.json') as f:
              report = json.load(f)
          high_severity = [r for r in report['results'] if r['issue_severity'] == 'HIGH']
          if high_severity:
              print(f'Found {len(high_severity)} high severity issues')
              exit(1)
          "
```

---

## 3. Model Artifact Scanning

### 3.1 Pickle Safety Check

```python
# security/model_scanner.py
import pickletools
import io
from typing import Tuple, List

DANGEROUS_OPCODES = [
    'GLOBAL',  # Can import arbitrary modules
    'REDUCE',  # Can call arbitrary functions
    'BUILD',   # Can call __setstate__
    'INST',    # Creates class instances
    'OBJ',     # Creates class instances
]

def scan_pickle_file(filepath: str) -> Tuple[bool, List[str]]:
    """Scan pickle file for dangerous operations."""
    issues = []
    
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # Analyze opcodes
    ops = io.StringIO()
    pickletools.dis(io.BytesIO(content), ops)
    ops_str = ops.getvalue()
    
    for dangerous_op in DANGEROUS_OPCODES:
        if dangerous_op in ops_str:
            # Check if it's a known safe module
            if not is_safe_module(ops_str, dangerous_op):
                issues.append(f"Dangerous opcode found: {dangerous_op}")
    
    return len(issues) == 0, issues

def is_safe_module(ops_str: str, opcode: str) -> bool:
    """Check if module usage is safe."""
    safe_modules = [
        'sklearn', 'numpy', 'pandas', 'xgboost',
        'lightgbm', 'torch', 'tensorflow'
    ]
    # Implementation to check if GLOBAL loads only safe modules
    return any(module in ops_str for module in safe_modules)

def scan_model_artifact(model_path: str) -> dict:
    """Full scan of model artifact."""
    results = {
        'path': model_path,
        'passed': True,
        'issues': []
    }
    
    # Scan pickle files
    for pkl_file in Path(model_path).rglob('*.pkl'):
        safe, issues = scan_pickle_file(str(pkl_file))
        if not safe:
            results['passed'] = False
            results['issues'].extend(issues)
    
    # Scan joblib files
    for joblib_file in Path(model_path).rglob('*.joblib'):
        safe, issues = scan_pickle_file(str(joblib_file))
        if not safe:
            results['passed'] = False
            results['issues'].extend(issues)
    
    return results
```

### 3.2 Model Registration Gate

```python
# security/registration_gate.py
from mlflow.tracking import MlflowClient

def security_gate(model_name: str, version: str) -> bool:
    """Security gate before model registration."""
    client = MlflowClient()
    
    # Get model artifact path
    mv = client.get_model_version(model_name, version)
    artifact_path = mv.source
    
    # Run security scan
    scan_result = scan_model_artifact(artifact_path)
    
    # Log results
    client.set_model_version_tag(
        model_name, version,
        "security.scanned", "true"
    )
    client.set_model_version_tag(
        model_name, version,
        "security.passed", str(scan_result['passed'])
    )
    
    if not scan_result['passed']:
        client.set_model_version_tag(
            model_name, version,
            "security.issues", str(scan_result['issues'])
        )
        raise SecurityException(f"Model failed security scan: {scan_result['issues']}")
    
    return True
```

---

## 4. Container Scanning

### 4.1 Trivy Scan

```yaml
# .github/workflows/container-scan.yml
  container-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Build image
        run: docker build -t model-serving:${{ github.sha }} .
      
      - name: Run Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'model-serving:${{ github.sha }}'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'
      
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

---

## 5. API Security Testing

### 5.1 Input Validation Tests

```python
# security/api_security_tests.py
import pytest
import requests

class TestAPISecurityBasics:
    """Basic API security tests."""
    
    def test_authentication_required(self):
        """Test that auth is required."""
        response = requests.post(
            "https://model.example.com/v2/models/fraud/infer",
            json={"inputs": []}
        )
        assert response.status_code == 401
    
    def test_input_validation(self):
        """Test input validation."""
        # Oversized input
        response = requests.post(
            "https://model.example.com/v2/models/fraud/infer",
            json={"inputs": [{"data": [0] * 1000000}]},
            headers={"Authorization": "Bearer test"}
        )
        assert response.status_code == 400
    
    def test_sql_injection(self):
        """Test SQL injection protection."""
        response = requests.post(
            "https://model.example.com/v2/models/fraud/infer",
            json={"inputs": [{"user_id": "'; DROP TABLE users;--"}]},
            headers={"Authorization": "Bearer test"}
        )
        # Should not cause server error
        assert response.status_code in [200, 400]
```

---

## 6. Security Scan Report

```markdown
## Model Security Scan Report

**Model:** [Model Name]
**Version:** [Version]
**Scan Date:** [Date]

### Summary
| Check | Status |
|-------|--------|
| Dependency Scan |  /  |
| Model Artifact Scan |  /  |
| Container Scan |  /  |
| Static Analysis |  /  |

### Findings

| ID | Severity | Component | Description |
|----|----------|-----------|-------------|
| | | | |

### Recommendations
- 

### Approval
- [ ] Security scan passed
- [ ] Approved for deployment
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial security scanning |
