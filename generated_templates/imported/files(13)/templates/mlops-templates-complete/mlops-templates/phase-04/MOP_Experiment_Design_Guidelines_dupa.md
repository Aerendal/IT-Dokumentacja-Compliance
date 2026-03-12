---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-100: Experiment Design Guidelines

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-100 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Experiment Planning

### 1.1 Experiment Types

| Type | Purpose | Duration |
|------|---------|----------|
| Exploratory | Initial research | Days |
| Hypothesis Testing | Validate ideas | Days-Weeks |
| Hyperparameter Tuning | Optimize model | Hours-Days |
| Architecture Search | Find best model | Days-Weeks |
| A/B Test | Production validation | Weeks |

### 1.2 Experiment Checklist

```markdown
## Experiment Planning Checklist

**Experiment Name:** ___________
**Hypothesis:** ___________
**Owner:** ___________

### Planning
- [ ] Clear hypothesis defined
- [ ] Success metrics identified
- [ ] Baseline established
- [ ] Resource requirements estimated
- [ ] Timeline defined

### Data
- [ ] Training data identified
- [ ] Test data isolated
- [ ] Data version documented

### Execution
- [ ] Reproducibility ensured (seeds set)
- [ ] All parameters logged
- [ ] Artifacts saved
```

---

## 2. MLflow Experiment Structure

### 2.1 Naming Convention

```
{team}-{project}-{experiment_type}

Examples:
- fraud-detection-baseline
- fraud-detection-hyperopt
- fraud-detection-feature-ablation
```

### 2.2 Standard Tags

```python
import mlflow

mlflow.set_tags({
    # Required
    "team": "fraud",
    "project": "detection-v2",
    "experiment_type": "hyperparameter_tuning",
    
    # Recommended
    "data.version": "v2024.01",
    "framework": "xgboost",
    "hypothesis": "Deeper trees improve recall",
    
    # Optional
    "jira_ticket": "ML-1234",
    "reviewer": "ml-lead@company.com"
})
```

---

## 3. Hyperparameter Tuning

### 3.1 Optuna Integration

```python
# experiments/hyperopt.py
import optuna
import mlflow

def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
    }
    
    with mlflow.start_run(nested=True):
        mlflow.log_params(params)
        
        model = train_model(params)
        score = evaluate_model(model)
        
        mlflow.log_metric('auc', score)
        
    return score

# Run optimization
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

# Log best results
with mlflow.start_run():
    mlflow.log_params(study.best_params)
    mlflow.log_metric('best_auc', study.best_value)
```

---

## 4. Experiment Comparison

### 4.1 Comparison Template

| Experiment | AUC | Precision | Recall | F1 | Training Time |
|------------|-----|-----------|--------|----|--------------:|
| Baseline | 0.92 | 0.85 | 0.78 | 0.81 | 10m |
| Exp-001 | 0.94 | 0.87 | 0.82 | 0.84 | 15m |
| Exp-002 | 0.93 | 0.88 | 0.80 | 0.84 | 12m |

### 4.2 Decision Criteria

| Metric | Minimum | Target | Weight |
|--------|---------|--------|--------|
| AUC | 0.90 | 0.95 | 30% |
| Precision | 0.80 | 0.90 | 25% |
| Recall | 0.75 | 0.85 | 25% |
| Latency | <50ms | <30ms | 20% |

---

## 5. Experiment Documentation

### 5.1 Experiment Report Template

```markdown
# Experiment Report: [Name]

## Summary
**Status:** Success / Failed / Inconclusive
**Hypothesis:** [What we tested]
**Conclusion:** [What we learned]

## Setup
- Dataset: [version]
- Baseline: [run_id]
- Duration: [time]

## Results
| Metric | Baseline | This Experiment | Change |
|--------|----------|-----------------|--------|
| AUC | X.XX | X.XX | +X% |

## Recommendations
- [ ] Proceed to production
- [ ] Further experimentation needed
- [ ] Abandon approach

## Next Steps
1. [Action item]
```

---

## 6. Reproducibility

### 6.1 Required Logging

```python
def log_experiment_context():
    """Log all context for reproducibility."""
    import mlflow
    import git
    
    repo = git.Repo(search_parent_directories=True)
    
    # Code version
    mlflow.set_tag("git.commit", repo.head.commit.hexsha)
    mlflow.set_tag("git.branch", repo.active_branch.name)
    
    # Environment
    mlflow.log_artifact("requirements.txt")
    
    # Random seeds
    mlflow.log_param("random_seed", 42)
    
    # Data version
    mlflow.set_tag("data.version", get_data_version())
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial experiment guidelines |
