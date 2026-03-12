---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-099: Feature Engineering Guidelines

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-099 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Feature Engineering Principles

### 1.1 Best Practices

| Principle | Description |
|-----------|-------------|
| Reproducibility | Same inputs → same features |
| Reusability | Features shared across models |
| Freshness | Features updated appropriately |
| Documentation | Clear feature definitions |

### 1.2 Feature Categories

| Category | Examples | Update Frequency |
|----------|----------|------------------|
| Static | User demographics | Daily |
| Aggregated | Transaction counts | Hourly |
| Real-time | Current session data | Real-time |
| Derived | Ratios, differences | On-demand |

---

## 2. Naming Conventions

### 2.1 Feature Naming

```
{entity}_{metric}_{aggregation}_{window}

Examples:
- user_transaction_count_30d
- user_avg_amount_7d
- merchant_fraud_rate_90d
```

### 2.2 Feature View Naming

```
{entity}_features
{entity}_{domain}_features

Examples:
- user_features
- user_transaction_features
- merchant_risk_features
```

---

## 3. Feature Definitions

### 3.1 Feast Feature View

```python
# features/user_features.py
from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64

user = Entity(name="user", join_keys=["user_id"])

user_features = FeatureView(
    name="user_features",
    entities=[user],
    ttl=timedelta(days=1),
    schema=[
        Field(name="age", dtype=Int64, description="User age in years"),
        Field(name="tenure_days", dtype=Int64, description="Days since registration"),
        Field(name="transaction_count_30d", dtype=Int64, description="Transactions in last 30 days"),
        Field(name="avg_amount_30d", dtype=Float32, description="Average transaction amount"),
        Field(name="max_amount_30d", dtype=Float32, description="Max transaction in 30 days"),
    ],
    source=user_source,
    online=True,
    tags={"team": "fraud", "tier": "1"}
)
```

### 3.2 Feature Documentation

```yaml
# features/docs/user_transaction_count_30d.yaml
name: user_transaction_count_30d
description: Number of transactions by user in last 30 days
entity: user
dtype: int64
source: transactions table
calculation: COUNT(*) WHERE timestamp > NOW() - 30 days
update_frequency: hourly
owner: fraud-team
used_by:
  - fraud-detection-v2
  - churn-prediction
```

---

## 4. Feature Transformations

### 4.1 Common Transformations

```python
# features/transformations.py
import pandas as pd
import numpy as np

def create_time_features(df: pd.DataFrame, timestamp_col: str) -> pd.DataFrame:
    """Extract time-based features."""
    df['hour_of_day'] = df[timestamp_col].dt.hour
    df['day_of_week'] = df[timestamp_col].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_night'] = df['hour_of_day'].isin(range(22, 24)).astype(int) | \
                     df['hour_of_day'].isin(range(0, 6)).astype(int)
    return df

def create_aggregations(df: pd.DataFrame, group_col: str, 
                        value_col: str, windows: list) -> pd.DataFrame:
    """Create rolling aggregations."""
    for window in windows:
        df[f'{value_col}_sum_{window}d'] = df.groupby(group_col)[value_col] \
            .transform(lambda x: x.rolling(f'{window}D').sum())
        df[f'{value_col}_avg_{window}d'] = df.groupby(group_col)[value_col] \
            .transform(lambda x: x.rolling(f'{window}D').mean())
        df[f'{value_col}_std_{window}d'] = df.groupby(group_col)[value_col] \
            .transform(lambda x: x.rolling(f'{window}D').std())
    return df

def create_ratio_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create ratio features."""
    df['amount_to_avg_ratio'] = df['amount'] / (df['avg_amount_30d'] + 1)
    df['amount_to_max_ratio'] = df['amount'] / (df['max_amount_30d'] + 1)
    return df
```

---

## 5. Feature Quality

### 5.1 Quality Checks

```python
# features/quality.py
def validate_features(df: pd.DataFrame, feature_specs: dict) -> dict:
    """Validate feature quality."""
    results = {}
    
    for feature, spec in feature_specs.items():
        checks = {
            'null_rate': df[feature].isnull().mean(),
            'in_range': df[feature].between(spec['min'], spec['max']).mean(),
            'unique_rate': df[feature].nunique() / len(df)
        }
        
        results[feature] = {
            'passed': checks['null_rate'] < 0.05 and checks['in_range'] > 0.99,
            'checks': checks
        }
    
    return results
```

### 5.2 Feature Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Null rate | <5% | >10% |
| Value drift | <0.1 PSI | >0.2 PSI |
| Freshness | <1 hour | >2 hours |

---

## 6. Feature Checklist

```markdown
## New Feature Checklist

- [ ] Clear business justification
- [ ] Follows naming convention
- [ ] Documented in feature catalog
- [ ] Unit tested
- [ ] Quality metrics defined
- [ ] Monitoring configured
- [ ] Approved by data steward (if PII)
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial feature guidelines |
