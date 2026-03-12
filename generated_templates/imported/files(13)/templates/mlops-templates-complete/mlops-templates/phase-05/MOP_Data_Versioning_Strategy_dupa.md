---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-090: Data Versioning Strategy

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-090 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Data Engineering / ML Platform] |

---

## 1. Data Versioning Overview

### 1.1 What to Version

| Data Type | Version Strategy | Tool |
|-----------|-----------------|------|
| Training Data | Immutable snapshots | DVC / Delta Lake |
| Feature Definitions | Git | Git |
| Feature Data | Time-based | Feast |
| Reference Data | Git + DVC | DVC |
| Model Artifacts | MLflow | MLflow |

### 1.2 Versioning Principles

1. **Immutability:** Never modify versioned data
2. **Traceability:** Link data versions to model versions
3. **Reproducibility:** Any training run can be recreated
4. **Efficiency:** Use deduplication and incremental updates

---

## 2. DVC Implementation

### 2.1 DVC Configuration

```yaml
# .dvc/config
[core]
    remote = s3-storage
    autostage = true

[remote "s3-storage"]
    url = s3://mlops-data-versions
    
[remote "local-cache"]
    url = /data/dvc-cache
```

### 2.2 Data Pipeline Definition

```yaml
# dvc.yaml
stages:
  prepare_data:
    cmd: python src/prepare_data.py
    deps:
      - src/prepare_data.py
      - data/raw/
    params:
      - prepare.split_ratio
      - prepare.random_seed
    outs:
      - data/processed/train.parquet
      - data/processed/test.parquet
    metrics:
      - data/metrics/data_quality.json:
          cache: false
    
  create_features:
    cmd: python src/create_features.py
    deps:
      - src/create_features.py
      - data/processed/
    outs:
      - data/features/
```

### 2.3 Version Operations

```bash
# Track new data
dvc add data/raw/transactions_2024_01.parquet

# Push to remote
dvc push

# Create data version tag
git add data/raw/transactions_2024_01.parquet.dvc
git commit -m "data: add January 2024 transactions"
git tag -a data-v2024.01 -m "Data version January 2024"

# Checkout specific version
git checkout data-v2023.12
dvc checkout
```

---

## 3. Delta Lake Versioning

### 3.1 Delta Table Setup

```python
# data_versioning/delta_setup.py
from delta import DeltaTable
from pyspark.sql import SparkSession

def create_versioned_table(spark: SparkSession, path: str, df):
    """Create Delta table with versioning."""
    df.write.format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .save(path)

def append_with_version(spark: SparkSession, path: str, df, version_tag: str):
    """Append data with version metadata."""
    df_with_version = df.withColumn("_data_version", lit(version_tag))
    
    df_with_version.write.format("delta") \
        .mode("append") \
        .save(path)

def read_version(spark: SparkSession, path: str, version: int = None, timestamp: str = None):
    """Read specific version of data."""
    reader = spark.read.format("delta")
    
    if version is not None:
        reader = reader.option("versionAsOf", version)
    elif timestamp is not None:
        reader = reader.option("timestampAsOf", timestamp)
    
    return reader.load(path)
```

### 3.2 Time Travel Queries

```python
# Read data as of specific version
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load(path)

# Read data as of timestamp
df_historical = spark.read.format("delta") \
    .option("timestampAsOf", "2024-01-15 00:00:00") \
    .load(path)

# View version history
delta_table = DeltaTable.forPath(spark, path)
history = delta_table.history()
history.select("version", "timestamp", "operation").show()
```

---

## 4. Data Version Manifest

### 4.1 Manifest Schema

```yaml
# data_versions/manifest_v2024.01.yaml
version: "2024.01"
created_at: "2024-01-15T00:00:00Z"
created_by: "data-pipeline"

datasets:
  training_data:
    path: "s3://mlops-data/training/v2024.01/"
    format: "parquet"
    records: 10500000
    size_bytes: 4523456789
    schema_version: "2.0"
    checksum: "sha256:abc123..."
    
  features:
    path: "s3://mlops-features/v2024.01/"
    format: "parquet"
    feature_count: 150
    
lineage:
  sources:
    - "transactions_db.transactions"
    - "users_db.user_profiles"
  transformations:
    - "dbt/models/training_data.sql"
    - "spark/feature_engineering.py"

quality_metrics:
  null_rate: 0.001
  duplicate_rate: 0.0
  schema_valid: true
```

### 4.2 Manifest Management

```python
# data_versioning/manifest.py
import yaml
import hashlib
from dataclasses import dataclass, asdict

@dataclass
class DatasetInfo:
    path: str
    format: str
    records: int
    size_bytes: int
    checksum: str

@dataclass
class DataManifest:
    version: str
    created_at: str
    datasets: dict
    lineage: dict
    quality_metrics: dict

def create_manifest(version: str, datasets: dict) -> DataManifest:
    """Create data version manifest."""
    manifest = DataManifest(
        version=version,
        created_at=datetime.utcnow().isoformat(),
        datasets=datasets,
        lineage={},
        quality_metrics={}
    )
    return manifest

def save_manifest(manifest: DataManifest, path: str):
    """Save manifest to file."""
    with open(path, 'w') as f:
        yaml.dump(asdict(manifest), f)

def load_manifest(path: str) -> DataManifest:
    """Load manifest from file."""
    with open(path) as f:
        data = yaml.safe_load(f)
    return DataManifest(**data)
```

---

## 5. MLflow Data Tracking

### 5.1 Log Data Version

```python
# Log data version with MLflow run
import mlflow

with mlflow.start_run():
    # Log data version
    mlflow.set_tag("data.version", "v2024.01")
    mlflow.set_tag("data.path", "s3://mlops-data/training/v2024.01/")
    mlflow.set_tag("data.records", "10500000")
    mlflow.set_tag("data.checksum", "sha256:abc123...")
    
    # Log manifest as artifact
    mlflow.log_artifact("data_versions/manifest_v2024.01.yaml")
```

---

## 6. Best Practices

| Practice | Description |
|----------|-------------|
| Immutable versions | Never modify, create new version |
| Semantic naming | `v{YYYY}.{MM}` or `v{MAJOR}.{MINOR}` |
| Include checksums | Verify data integrity |
| Link to lineage | Track data sources |
| Automate versioning | CI/CD for data pipelines |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial data versioning strategy |
