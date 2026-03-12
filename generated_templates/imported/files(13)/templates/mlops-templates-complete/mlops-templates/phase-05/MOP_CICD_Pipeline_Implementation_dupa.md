---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-017: CI/CD Pipeline Implementation

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-017 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Engineer] |

---

## 1. Pipeline Architecture

### 1.1 Overview
```
┌─────────────────────────────────────────────────────────────┐
│                    ML CI/CD Pipeline                         │
│                                                             │
│  Code Push    ┌─────────────────────────────────────────┐  │
│      │        │              CI Pipeline                 │  │
│      ▼        │  Lint → Test → Build → Validate Model   │  │
│  ┌──────┐     └─────────────────────────────────────────┘  │
│  │GitHub│                        │                          │
│  │ PR   │                        ▼                          │
│  └──────┘     ┌─────────────────────────────────────────┐  │
│               │              CD Pipeline                 │  │
│               │  Stage → Test → Canary → Production     │  │
│               └─────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. CI Pipeline Implementation

### 2.1 GitHub Actions Workflow

```yaml
# .github/workflows/ml-ci.yml
name: ML CI Pipeline

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

env:
  PYTHON_VERSION: "3.11"
  MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run: pip install ruff black isort mypy
      - name: Run linters
        run: |
          ruff check .
          black --check .
          isort --check .
          mypy src/

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run: pip install -r requirements.txt -r requirements-test.txt
      - name: Run unit tests
        run: pytest tests/unit -v --cov=src --cov-report=xml
      - name: Run integration tests
        run: pytest tests/integration -v
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: |
          docker build -t mlops/model:${{ github.sha }} .
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker push $ECR_REGISTRY/mlops/model:${{ github.sha }}

  validate-model:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
      - name: Validate model artifact
        run: |
          python scripts/validate_model.py \
            --model-uri models:/fraud-model/staging \
            --test-data s3://mlops/test-data/
      - name: Check model performance
        run: |
          python scripts/check_performance.py \
            --baseline-metrics configs/baseline_metrics.json
```

### 2.2 Model Validation Script

```python
# scripts/validate_model.py
import mlflow
import pandas as pd
import sys

def validate_model(model_uri: str, test_data_path: str) -> bool:
    """Validate model meets deployment criteria."""
    
    # Load model
    model = mlflow.pyfunc.load_model(model_uri)
    
    # Load test data
    test_df = pd.read_parquet(test_data_path)
    X_test = test_df.drop('label', axis=1)
    y_test = test_df['label']
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Validate schema
    assert len(predictions) == len(X_test), "Prediction count mismatch"
    
    # Validate performance
    from sklearn.metrics import accuracy_score, f1_score
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    
    print(f"Accuracy: {accuracy:.4f}, F1: {f1:.4f}")
    
    # Check thresholds
    if accuracy < 0.90 or f1 < 0.85:
        print("FAILED: Model below performance threshold")
        return False
    
    print("PASSED: Model validation successful")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-uri", required=True)
    parser.add_argument("--test-data", required=True)
    args = parser.parse_args()
    
    success = validate_model(args.model_uri, args.test_data)
    sys.exit(0 if success else 1)
```

---

## 3. CD Pipeline Implementation

### 3.1 Argo CD Application

```yaml
# argocd/model-serving-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: fraud-model
  namespace: argocd
spec:
  project: ml-models
  source:
    repoURL: https://github.com/company/ml-deployments
    targetRevision: HEAD
    path: models/fraud-model
  destination:
    server: https://kubernetes.default.svc
    namespace: models
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### 3.2 Deployment Manifest Template

```yaml
# models/fraud-model/inference-service.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-model
  namespace: models
spec:
  predictor:
    minReplicas: 2
    maxReplicas: 10
    triton:
      storageUri: "s3://models/fraud-model/${MODEL_VERSION}"
      runtimeVersion: "23.10-py3"
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
        limits:
          cpu: "2"
          memory: "4Gi"
```

### 3.3 Deployment Script

```bash
#!/bin/bash
# scripts/deploy.sh

MODEL_NAME=$1
MODEL_VERSION=$2
ENVIRONMENT=$3

echo "Deploying $MODEL_NAME:$MODEL_VERSION to $ENVIRONMENT"

# Update manifest
sed -i "s/\${MODEL_VERSION}/$MODEL_VERSION/g" manifests/inference-service.yaml

# Apply to cluster
if [ "$ENVIRONMENT" == "staging" ]; then
    kubectl apply -f manifests/ -n models-staging
elif [ "$ENVIRONMENT" == "production" ]; then
    # Canary deployment
    kubectl patch inferenceservice $MODEL_NAME -n models \
        --type='json' \
        -p='[{"op": "add", "path": "/spec/predictor/canaryTrafficPercent", "value": 10}]'
fi

# Wait for rollout
kubectl rollout status deployment/${MODEL_NAME}-predictor -n models --timeout=10m

echo "Deployment complete"
```

---

## 4. Pipeline Triggers

### 4.1 Trigger Configuration

| Trigger | Action | Pipeline |
|---------|--------|----------|
| PR to main | CI pipeline | Lint, Test, Build |
| Merge to main | CD to staging | Deploy staging |
| Manual approval | CD to production | Canary → Full |
| Model registered | Validation | Auto-validate |
| Schedule (daily) | Retraining | Full pipeline |

### 4.2 Webhook Setup

```yaml
# MLflow webhook for model registration
webhooks:
  - name: model-registered
    events: [MODEL_VERSION_CREATED]
    http_endpoint:
      url: https://ci.example.com/api/webhooks/model-registered
      headers:
        Authorization: Bearer ${CI_TOKEN}
```

---

## 5. Verification

### 5.1 Pipeline Health Check

```bash
# Check CI status
gh run list --workflow=ml-ci.yml --limit=5

# Check CD status
argocd app get fraud-model

# Check deployment
kubectl get inferenceservice -n models
```

### 5.2 Success Criteria

| Metric | Target |
|--------|--------|
| CI pipeline duration | <15 minutes |
| CD pipeline duration | <10 minutes |
| Pipeline success rate | >95% |
| Rollback time | <5 minutes |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation |
