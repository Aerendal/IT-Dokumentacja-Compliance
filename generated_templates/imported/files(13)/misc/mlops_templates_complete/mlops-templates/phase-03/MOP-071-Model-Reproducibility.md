---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-071: Model Reproducibility Architecture

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-071 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Reproducibility Requirements

### 1.1 Reproducibility Levels

| Level | Description | Requirements |
|-------|-------------|--------------|
| L1 - Basic | Same code, same results | Code versioning |
| L2 - Standard | Full pipeline reproducible | + Data versioning |
| L3 - Complete | Any historical state recreatable | + Environment versioning |

### 1.2 Minimum Requirements by Model Tier

| Tier | Reproducibility Level | Audit Period |
|------|----------------------|--------------|
| Tier 1 (Critical) | L3 - Complete | 7 years |
| Tier 2 (Important) | L2 - Standard | 3 years |
| Tier 3 (Standard) | L1 - Basic | 1 year |

---

## 2. Code Versioning

### 2.1 Git Strategy

```
main (production)
  │
  ├── develop (integration)
  │     │
  │     ├── feature/model-v2
  │     ├── feature/new-features
  │     └── bugfix/training-fix
  │
  └── release/v1.2.0
```

### 2.2 Commit Standards

```yaml
# .commitlintrc.yaml
rules:
  type-enum:
    - 2
    - always
    - - feat      # New feature
      - fix       # Bug fix
      - data      # Data changes
      - model     # Model changes
      - config    # Configuration
      - docs      # Documentation
      - test      # Tests
      - refactor  # Refactoring

# Example commits:
# feat(fraud-model): add new feature engineering
# data(training): update training dataset v2.1
# model(fraud): increase hidden layers
```

### 2.3 MLflow Code Tracking

```python
import mlflow
import git

def log_code_version():
    """Log code version to MLflow."""
    repo = git.Repo(search_parent_directories=True)
    
    mlflow.set_tag("git.commit", repo.head.commit.hexsha)
    mlflow.set_tag("git.branch", repo.active_branch.name)
    mlflow.set_tag("git.remote", repo.remotes.origin.url)
    mlflow.set_tag("git.dirty", repo.is_dirty())
    
    # Log diff if dirty
    if repo.is_dirty():
        diff = repo.git.diff()
        mlflow.log_text(diff, "uncommitted_changes.diff")
```

---

## 3. Data Versioning

### 3.1 DVC Configuration

```yaml
# dvc.yaml
stages:
  prepare_data:
    cmd: python src/prepare_data.py
    deps:
      - src/prepare_data.py
      - data/raw/
    outs:
      - data/processed/
    params:
      - prepare.split_ratio
      - prepare.seed

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed/
    outs:
      - models/
    params:
      - train.learning_rate
      - train.epochs
    metrics:
      - metrics.json:
          cache: false
```

### 3.2 Data Version Tracking

```python
# data_versioning.py
import hashlib
import json
from datetime import datetime

def create_data_manifest(data_path: str) -> dict:
    """Create data version manifest."""
    manifest = {
        "created_at": datetime.utcnow().isoformat(),
        "data_path": data_path,
        "files": []
    }
    
    for file in Path(data_path).rglob("*"):
        if file.is_file():
            manifest["files"].append({
                "path": str(file.relative_to(data_path)),
                "size": file.stat().st_size,
                "md5": hashlib.md5(file.read_bytes()).hexdigest(),
                "modified": datetime.fromtimestamp(file.stat().st_mtime).isoformat()
            })
    
    # Overall hash
    manifest["data_hash"] = hashlib.md5(
        json.dumps(manifest["files"], sort_keys=True).encode()
    ).hexdigest()
    
    return manifest

def log_data_version(data_path: str):
    """Log data version to MLflow."""
    manifest = create_data_manifest(data_path)
    
    mlflow.log_dict(manifest, "data_manifest.json")
    mlflow.set_tag("data.version", manifest["data_hash"][:8])
    mlflow.set_tag("data.path", data_path)
```

---

## 4. Environment Versioning

### 4.1 Docker-based Environments

```dockerfile
# Dockerfile.training
FROM python:3.11-slim

# Pin system packages
RUN apt-get update && apt-get install -y \
    libgomp1=12.2.0-14 \
    && rm -rf /var/lib/apt/lists/*

# Pin Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY src/ /app/src/
WORKDIR /app

# Set reproducibility env vars
ENV PYTHONHASHSEED=0
ENV TF_DETERMINISTIC_OPS=1
ENV CUBLAS_WORKSPACE_CONFIG=:4096:8
```

### 4.2 Requirements Pinning

```txt
# requirements.txt - fully pinned
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
xgboost==1.7.6
mlflow==2.10.0
feast==0.36.0

# Generate with:
# pip freeze > requirements.txt
```

### 4.3 Environment Logging

```python
def log_environment():
    """Log complete environment to MLflow."""
    import platform
    import pkg_resources
    
    # System info
    mlflow.set_tag("env.python_version", platform.python_version())
    mlflow.set_tag("env.platform", platform.platform())
    
    # Packages
    packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    mlflow.log_dict(packages, "environment/packages.json")
    
    # Docker image if available
    if os.environ.get("DOCKER_IMAGE"):
        mlflow.set_tag("env.docker_image", os.environ["DOCKER_IMAGE"])
```

---

## 5. Random Seed Management

### 5.1 Seed Configuration

```python
# reproducibility/seeds.py
import os
import random
import numpy as np

def set_all_seeds(seed: int = 42):
    """Set all random seeds for reproducibility."""
    
    # Python
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    
    # NumPy
    np.random.seed(seed)
    
    # TensorFlow
    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
        os.environ['TF_DETERMINISTIC_OPS'] = '1'
    except ImportError:
        pass
    
    # PyTorch
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass
    
    # XGBoost (set in params)
    # sklearn (set in model init)
    
    return seed
```

### 5.2 Logging Seeds

```python
def log_reproducibility_config(seed: int):
    """Log reproducibility configuration."""
    mlflow.log_param("random_seed", seed)
    mlflow.set_tag("reproducibility.seed", seed)
    mlflow.set_tag("reproducibility.deterministic", True)
```

---

## 6. Experiment Recreation

### 6.1 Recreation Script

```python
# recreate_experiment.py
import mlflow
from mlflow.tracking import MlflowClient

def recreate_experiment(run_id: str):
    """Recreate an experiment from MLflow run."""
    client = MlflowClient()
    run = client.get_run(run_id)
    
    # Get code version
    git_commit = run.data.tags.get("git.commit")
    print(f"Checkout code: git checkout {git_commit}")
    
    # Get data version
    data_version = run.data.tags.get("data.version")
    print(f"Checkout data: dvc checkout {data_version}")
    
    # Get environment
    artifacts_path = mlflow.artifacts.download_artifacts(run_id)
    print(f"Environment: {artifacts_path}/environment/packages.json")
    
    # Get parameters
    params = run.data.params
    print(f"Parameters: {params}")
    
    # Get seed
    seed = run.data.params.get("random_seed", 42)
    print(f"Seed: {seed}")
    
    return {
        "git_commit": git_commit,
        "data_version": data_version,
        "params": params,
        "seed": seed
    }
```

### 6.2 Automated Verification

```python
def verify_reproducibility(original_run_id: str, new_run_id: str, 
                          tolerance: float = 1e-6) -> bool:
    """Verify two runs produce same results."""
    client = MlflowClient()
    
    original = client.get_run(original_run_id)
    new = client.get_run(new_run_id)
    
    # Compare metrics
    for metric_name in original.data.metrics:
        orig_value = original.data.metrics[metric_name]
        new_value = new.data.metrics.get(metric_name)
        
        if new_value is None:
            print(f"Missing metric: {metric_name}")
            return False
        
        if abs(orig_value - new_value) > tolerance:
            print(f"Metric mismatch: {metric_name}")
            print(f"  Original: {orig_value}")
            print(f"  New: {new_value}")
            return False
    
    print(" Reproducibility verified")
    return True
```

---

## 7. Reproducibility Checklist

```markdown
## Reproducibility Checklist

### Before Training
- [ ] Code committed to Git
- [ ] Data version tracked (DVC/manifest)
- [ ] Environment pinned (requirements.txt)
- [ ] Random seeds set

### During Training
- [ ] MLflow tracking enabled
- [ ] All parameters logged
- [ ] Data version logged
- [ ] Code version logged
- [ ] Environment logged

### After Training
- [ ] Model artifact saved
- [ ] Metrics logged
- [ ] Can recreate from logs
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial reproducibility guide |
