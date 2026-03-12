---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-011: Feature Store Design

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-011 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [ML Platform Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Semi-annually) |

---

## Document Lifecycle

### When This Document Appears
-  MOP-007 Architecture Document approved
-  Multiple models sharing features identified
-  Training-serving skew issues detected
-  Feature reuse strategy needed

### When This Document Becomes Invalid
-  Feature store platform migration
-  Architecture fundamentally changes
-  New feature paradigms emerge (e.g., LLM embeddings)

### Validity Conditions
-  Supports all required feature types
-  Online/offline stores operational
-  Training-serving consistency verified
-  Latency requirements met

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-007: Architecture | Feature store placement |
| MOP-005: ML Lifecycle Requirements | Feature requirements |
| MOP-006: Scalability Requirements | Performance needs |
| MOP-003: Tool Stack Vision | Platform selection |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-020: Feature Store Setup | Implementation specs |
| MOP-008: CI/CD Pipeline | Feature pipeline integration |
| MOP-010: Experiment Tracking | Feature-experiment linkage |
| MOP-012: Model Serving | Online feature serving |

### Bidirectional Dependencies
| Document | Relationship |
|----------|--------------|
| MOP-010: Experiment Tracking | Features ↔ Experiments |
| MOP-012: Model Serving | Online features ↔ Inference |
| MOP-008: CI/CD Pipeline | Feature pipelines |

---

## Section Dependencies (Internal)

```
┌────────────────────────────────────────────────────────────────┐
│              1. Feature Store Overview                          │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 2. Data Model &  │ │ 3. Offline   │ │ 4. Online        │
│    Feature Types │ │    Store     │ │    Store         │
└──────────────────┘ └──────────────┘ └──────────────────┘
        │                   │                  │
        └───────────────────┼──────────────────┘
                            ▼
┌────────────────────────────────────────────────────────────────┐
│              5. Feature Engineering Pipelines                   │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 6. Point-in-Time │ │ 7. Feature   │ │ 8. Governance    │
│    Correctness   │ │    Serving   │ │    & Monitoring  │
└──────────────────┘ └──────────────┘ └──────────────────┘
```

---

## Template Content

---

# Feature Store Design Document

**[Organization Name]**

**Version:** [X.Y]  
**Date:** [YYYY-MM-DD]

---

## 1. Feature Store Overview

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: All other sections
> - Update trigger: Platform strategy changes

### 1.1 Purpose

The Feature Store serves as the centralized repository for ML features, providing:
- **Consistency**: Same features for training and serving (prevent skew)
- **Reusability**: Share features across models and teams
- **Point-in-Time Correctness**: Accurate historical feature retrieval
- **Low-Latency Serving**: Fast online feature retrieval
- **Governance**: Feature documentation, lineage, and access control

### 1.2 Key Problems Solved

| Problem | Without Feature Store | With Feature Store |
|---------|----------------------|-------------------|
| Training-serving skew | Different code paths | Single source of truth |
| Feature duplication | 10+ copies of same feature | One canonical version |
| Point-in-time accuracy | Data leakage in training | Correct time-travel |
| Serving latency | Minutes (recalculate) | Milliseconds (cached) |
| Feature discovery | Unknown what exists | Searchable catalog |
| Governance | Manual tracking | Automated lineage |

### 1.3 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Feature Store                                │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Feature Definition Layer                    │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │ │
│  │  │   Entities   │  │ Feature Views│  │ Data Sources │        │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│  ┌─────────────────────────────┼─────────────────────────────────┐ │
│  │                    Transformation Layer                        │ │
│  │  ┌──────────────┐          │          ┌──────────────┐        │ │
│  │  │    Batch     │◄─────────┴─────────►│   Stream     │        │ │
│  │  │ Transformations                    │ Transformations       │ │
│  │  └──────────────┘                     └──────────────┘        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│  ┌─────────────────────────────┼─────────────────────────────────┐ │
│  │                      Storage Layer                             │ │
│  │  ┌──────────────────────┐  │  ┌──────────────────────┐       │ │
│  │  │    Offline Store     │◄─┴─►│    Online Store      │       │ │
│  │  │  (S3/BigQuery/Spark) │     │   (Redis/DynamoDB)   │       │ │
│  │  │                      │     │                      │       │ │
│  │  │  - Historical data   │     │  - Latest values     │       │ │
│  │  │  - Training datasets │     │  - Low-latency       │       │ │
│  │  │  - Batch retrieval   │     │  - Real-time serving │       │ │
│  │  └──────────────────────┘     └──────────────────────┘       │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│  ┌─────────────────────────────┼─────────────────────────────────┐ │
│  │                     Serving Layer                              │ │
│  │  ┌──────────────┐          │          ┌──────────────┐        │ │
│  │  │   Training   │◄─────────┴─────────►│   Inference  │        │ │
│  │  │   (Batch)    │                     │   (Online)   │        │ │
│  │  └──────────────┘                     └──────────────┘        │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.4 Technology Selection

| Component | Options | Selected | Rationale |
|-----------|---------|----------|-----------|
| Feature Store | Feast / Tecton / Vertex AI | [Selection] | [Rationale] |
| Offline Store | S3/GCS / BigQuery / Databricks | [Selection] | Existing data lake |
| Online Store | Redis / DynamoDB / Bigtable | [Selection] | Latency requirements |
| Orchestration | Airflow / Dagster / Prefect | [Selection] | Existing tools |

### 1.5 Platform Comparison

| Feature | Feast | Tecton | Vertex AI | Databricks |
|---------|-------|--------|-----------|------------|
| Open Source |  |  |  |  |
| Self-hosted |  |  |  |  |
| Stream features | Limited |  |  |  |
| Transformations | External | Built-in | Built-in | Built-in |
| Cost | Free | $$$ | $$ | $$ |
| Complexity | Low | Medium | Low | Medium |

---

## 2. Data Model & Feature Types

> **Section Dependencies:**
> - Depends on: Section 1 (Overview)
> - Feeds into: Sections 3-8
> - Update trigger: New feature types needed

### 2.1 Core Concepts

```
┌───────────────────────────────────────────────────────────────────┐
│                    Feature Store Data Model                        │
│                                                                   │
│  ┌─────────────────┐         ┌─────────────────┐                 │
│  │     Entity      │         │   Data Source   │                 │
│  │─────────────────│         │─────────────────│                 │
│  │ name            │         │ name            │                 │
│  │ join_keys[]     │         │ type (batch/    │                 │
│  │ description     │         │       stream)   │                 │
│  └────────┬────────┘         │ connection_info │                 │
│           │                  └────────┬────────┘                 │
│           │ 1:N                       │                          │
│           │              ┌────────────┘                          │
│           ▼              ▼                                       │
│  ┌────────────────────────────────────────────────────────┐      │
│  │                    Feature View                         │      │
│  │────────────────────────────────────────────────────────│      │
│  │ name                                                    │      │
│  │ entities[] (FK to Entity)                              │      │
│  │ source (FK to Data Source)                             │      │
│  │ schema (feature definitions)                           │      │
│  │ ttl (time-to-live)                                     │      │
│  │ online (bool)                                          │      │
│  │ tags{}                                                 │      │
│  └────────────────────────────────────────────────────────┘      │
│           │                                                       │
│           │ 1:N                                                   │
│           ▼                                                       │
│  ┌─────────────────┐                                             │
│  │     Feature     │                                             │
│  │─────────────────│                                             │
│  │ name            │                                             │
│  │ dtype           │                                             │
│  │ description     │                                             │
│  │ tags{}          │                                             │
│  └─────────────────┘                                             │
└───────────────────────────────────────────────────────────────────┘
```

### 2.2 Entity Definition

```python
from feast import Entity

# User entity - for user-level features
user = Entity(
    name="user",
    description="User identifier",
    join_keys=["user_id"],
    tags={"domain": "customer", "pii": "true"}
)

# Transaction entity - for transaction-level features
transaction = Entity(
    name="transaction",
    description="Transaction identifier",
    join_keys=["transaction_id"],
    tags={"domain": "payments"}
)

# Merchant entity - for merchant-level features
merchant = Entity(
    name="merchant",
    description="Merchant identifier",
    join_keys=["merchant_id"],
    tags={"domain": "merchant"}
)
```

### 2.3 Feature Types

| Type | Description | Example | Storage |
|------|-------------|---------|---------|
| **Batch** | Computed periodically | User age, lifetime value | Offline → Online |
| **Streaming** | Real-time updates | Transaction count (5m) | Stream → Online |
| **On-demand** | Computed at request time | Time since last login | Computed |
| **Pre-computed** | Static/slowly changing | User segment | Offline → Online |

### 2.4 Data Source Definitions

```python
from feast import FileSource, BigQuerySource, KafkaSource

# Batch source (data lake)
user_features_source = FileSource(
    name="user_features_source",
    path="s3://feature-store/user_features/",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
    file_format="parquet"
)

# BigQuery source
bq_source = BigQuerySource(
    name="user_transactions_bq",
    table="project.dataset.user_transactions",
    timestamp_field="event_timestamp"
)

# Streaming source
transaction_stream = KafkaSource(
    name="transaction_stream",
    kafka_bootstrap_servers="kafka:9092",
    topic="transactions",
    timestamp_field="timestamp",
    message_format=AvroFormat(schema_file="transaction.avsc")
)
```

### 2.5 Feature View Definition

```python
from feast import FeatureView, Field
from feast.types import Float32, Int64, String

# User features - batch
user_features = FeatureView(
    name="user_features",
    entities=[user],
    schema=[
        Field(name="transaction_count_30d", dtype=Int64,
              description="Number of transactions in last 30 days"),
        Field(name="avg_transaction_amount", dtype=Float32,
              description="Average transaction amount"),
        Field(name="total_spend_30d", dtype=Float32,
              description="Total spend in last 30 days"),
        Field(name="account_age_days", dtype=Int64,
              description="Days since account creation"),
        Field(name="preferred_category", dtype=String,
              description="Most frequent purchase category"),
    ],
    source=user_features_source,
    ttl=timedelta(days=1),
    online=True,
    tags={"team": "customer-analytics", "version": "v2"}
)

# Real-time transaction features
transaction_features = FeatureView(
    name="transaction_features",
    entities=[user],
    schema=[
        Field(name="transaction_count_5m", dtype=Int64),
        Field(name="transaction_count_1h", dtype=Int64),
        Field(name="unique_merchants_1h", dtype=Int64),
        Field(name="max_amount_1h", dtype=Float32),
    ],
    source=transaction_stream,
    ttl=timedelta(hours=1),
    online=True,
    tags={"team": "fraud-ml", "realtime": "true"}
)
```

---

## 3. Offline Store Design

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model)
> - Feeds into: Section 5 (Pipelines), Section 6 (Point-in-Time)
> - Update trigger: Storage requirements change

### 3.1 Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Offline Store                                │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Storage Layer (S3/GCS)                      │ │
│  │                                                                │ │
│  │  s3://feature-store/                                          │ │
│  │  ├── user_features/                                           │ │
│  │  │   ├── year=2024/                                          │ │
│  │  │   │   ├── month=01/                                       │ │
│  │  │   │   │   ├── day=15/                                     │ │
│  │  │   │   │   │   └── data.parquet                            │ │
│  │  │   │   │   └── ...                                         │ │
│  │  │   │   └── ...                                             │ │
│  │  │   └── ...                                                 │ │
│  │  ├── transaction_features/                                    │ │
│  │  │   └── ...                                                 │ │
│  │  └── registry/                                                │ │
│  │      └── registry.db                                          │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Query Layer (Spark/BigQuery)                │ │
│  │                                                                │ │
│  │  - Point-in-time joins                                        │ │
│  │  - Feature aggregations                                       │ │
│  │  - Training dataset generation                                │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Schema Design

```sql
-- Offline store table schema
CREATE TABLE user_features (
    -- Entity keys
    user_id STRING NOT NULL,
    
    -- Timestamps (critical for point-in-time correctness)
    event_timestamp TIMESTAMP NOT NULL,
    created_timestamp TIMESTAMP,
    
    -- Features
    transaction_count_30d INT64,
    avg_transaction_amount FLOAT64,
    total_spend_30d FLOAT64,
    account_age_days INT64,
    preferred_category STRING,
    
    -- Metadata
    _feast_feature_view STRING,
    _feast_run_id STRING
)
PARTITION BY DATE(event_timestamp)
CLUSTER BY user_id;
```

### 3.3 Partitioning Strategy

| Partition Type | Use Case | Example |
|----------------|----------|---------|
| Time-based | Large historical data | Daily/hourly partitions |
| Entity-based | Frequent entity lookups | Hash by user_id |
| Hybrid | Both patterns | Time + entity |

```python
# Feast offline store configuration
offline_store_config = {
    "type": "file",  # or "bigquery", "redshift", "snowflake"
    "path": "s3://feature-store/",
    "file_format": "parquet",
    "partition_columns": ["year", "month", "day"],
    "compression": "snappy"
}
```

### 3.4 Data Retention

| Data Type | Hot Storage | Cold Storage | Archive |
|-----------|-------------|--------------|---------|
| Raw features | 90 days | 1 year | 7 years |
| Aggregated | 1 year | 3 years | 7 years |
| Training sets | 1 year | 2 years | 5 years |

---

## 4. Online Store Design

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model), Section 3 (Offline)
> - Feeds into: Section 7 (Serving)
> - Update trigger: Latency requirements change

### 4.1 Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Online Store                                │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Cache Layer (Redis Cluster)                 │ │
│  │                                                                │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐         │ │
│  │  │ Shard 0 │  │ Shard 1 │  │ Shard 2 │  │ Shard N │         │ │
│  │  │ (Master)│  │ (Master)│  │ (Master)│  │ (Master)│         │ │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘         │ │
│  │       │            │            │            │                │ │
│  │  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐         │ │
│  │  │ Replica │  │ Replica │  │ Replica │  │ Replica │         │ │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘         │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  Key Schema: feast:{project}:{feature_view}:{entity_key}           │
│  Value: Serialized feature values (protobuf/msgpack)               │
│                                                                     │
│  Example:                                                           │
│  Key:   feast:fraud:user_features:user_123                         │
│  Value: {transaction_count_30d: 45, avg_amount: 125.50, ...}       │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Configuration

```yaml
# Online store configuration
online_store:
  type: redis
  connection_string: "redis://redis-cluster:6379"
  
  # Redis cluster configuration
  redis_cluster:
    nodes:
      - host: redis-1.example.com
        port: 6379
      - host: redis-2.example.com
        port: 6379
      - host: redis-3.example.com
        port: 6379
    
  # Performance tuning
  key_ttl_seconds: 86400  # 24 hours
  max_connections: 100
  connection_timeout_ms: 500
  read_timeout_ms: 100
```

### 4.3 Performance Requirements

| Metric | Requirement | Typical |
|--------|-------------|---------|
| Read latency (P50) | < 5ms | 2ms |
| Read latency (P99) | < 20ms | 10ms |
| Write latency | < 10ms | 5ms |
| Throughput | > 100K QPS | 150K QPS |
| Availability | 99.99% | 99.995% |

### 4.4 Materialization Process

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Materialization Pipeline                          │
│                                                                     │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐       │
│  │   Offline    │────►│  Materialize │────►│   Online     │       │
│  │    Store     │     │    Job       │     │    Store     │       │
│  └──────────────┘     └──────────────┘     └──────────────┘       │
│                              │                                      │
│                              ▼                                      │
│                    ┌──────────────────┐                            │
│                    │  Transformations │                            │
│                    │  - Aggregations  │                            │
│                    │  - Normalization │                            │
│                    │  - Encoding      │                            │
│                    └──────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘
```

```python
# Materialization command
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo/")

# Materialize features to online store
store.materialize(
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 1, 15),
    feature_views=["user_features", "merchant_features"]
)

# Incremental materialization
store.materialize_incremental(
    end_date=datetime.now(),
    feature_views=["user_features"]
)
```

---

## 5. Feature Engineering Pipelines

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model), Sections 3-4 (Storage)
> - Feeds into: Section 6 (Point-in-Time)
> - Update trigger: New features needed

### 5.1 Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                Feature Engineering Pipelines                         │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    Batch Pipeline (Airflow)                   │  │
│  │                                                               │  │
│  │  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐      │  │
│  │  │ Extract │──►│Transform│──►│  Load   │──►│Materialize│     │  │
│  │  │ (Source)│   │ (Spark) │   │(Offline)│   │ (Online) │     │  │
│  │  └─────────┘   └─────────┘   └─────────┘   └─────────┘      │  │
│  │                                                               │  │
│  │  Schedule: Daily at 2 AM UTC                                 │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                  Streaming Pipeline (Flink/Spark)             │  │
│  │                                                               │  │
│  │  ┌─────────┐   ┌─────────┐   ┌─────────┐                    │  │
│  │  │  Kafka  │──►│ Process │──►│  Write  │                    │  │
│  │  │ (Source)│   │(Windows)│   │ (Online)│                    │  │
│  │  └─────────┘   └─────────┘   └─────────┘                    │  │
│  │                                                               │  │
│  │  Latency: < 1 minute                                         │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Batch Feature Pipeline

```python
# Airflow DAG for batch feature engineering
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ml-platform',
    'depends_on_past': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'feature_engineering_daily',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    catchup=False
)

def compute_user_features(ds):
    """Compute user-level features."""
    spark = get_spark_session()
    
    # Read raw data
    transactions = spark.read.parquet(f"s3://data/transactions/date={ds}")
    users = spark.read.parquet("s3://data/users/")
    
    # Compute features
    user_features = transactions.groupBy("user_id").agg(
        count("*").alias("transaction_count_30d"),
        avg("amount").alias("avg_transaction_amount"),
        sum("amount").alias("total_spend_30d"),
        countDistinct("merchant_id").alias("unique_merchants_30d")
    ).join(users, "user_id")
    
    # Add timestamps
    user_features = user_features.withColumn(
        "event_timestamp", lit(datetime.strptime(ds, "%Y-%m-%d"))
    )
    
    # Write to offline store
    user_features.write.parquet(
        f"s3://feature-store/user_features/date={ds}",
        mode="overwrite"
    )

def materialize_features(ds):
    """Materialize features to online store."""
    from feast import FeatureStore
    
    store = FeatureStore(repo_path="/opt/feast/")
    store.materialize_incremental(
        end_date=datetime.strptime(ds, "%Y-%m-%d"),
        feature_views=["user_features"]
    )

compute_task = PythonOperator(
    task_id='compute_user_features',
    python_callable=compute_user_features,
    dag=dag
)

materialize_task = PythonOperator(
    task_id='materialize_features',
    python_callable=materialize_features,
    dag=dag
)

compute_task >> materialize_task
```

### 5.3 Streaming Feature Pipeline

```python
# Flink streaming feature computation
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

# Define Kafka source
t_env.execute_sql("""
    CREATE TABLE transactions (
        user_id STRING,
        merchant_id STRING,
        amount DOUBLE,
        timestamp TIMESTAMP(3),
        WATERMARK FOR timestamp AS timestamp - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'transactions',
        'properties.bootstrap.servers' = 'kafka:9092',
        'format' = 'json'
    )
""")

# Define Redis sink
t_env.execute_sql("""
    CREATE TABLE user_realtime_features (
        user_id STRING,
        transaction_count_5m BIGINT,
        transaction_count_1h BIGINT,
        total_amount_1h DOUBLE,
        PRIMARY KEY (user_id) NOT ENFORCED
    ) WITH (
        'connector' = 'redis',
        'host' = 'redis-cluster',
        'port' = '6379'
    )
""")

# Compute streaming features
t_env.execute_sql("""
    INSERT INTO user_realtime_features
    SELECT 
        user_id,
        COUNT(*) OVER (
            PARTITION BY user_id 
            ORDER BY timestamp 
            RANGE BETWEEN INTERVAL '5' MINUTE PRECEDING AND CURRENT ROW
        ) as transaction_count_5m,
        COUNT(*) OVER (
            PARTITION BY user_id 
            ORDER BY timestamp 
            RANGE BETWEEN INTERVAL '1' HOUR PRECEDING AND CURRENT ROW
        ) as transaction_count_1h,
        SUM(amount) OVER (
            PARTITION BY user_id 
            ORDER BY timestamp 
            RANGE BETWEEN INTERVAL '1' HOUR PRECEDING AND CURRENT ROW
        ) as total_amount_1h
    FROM transactions
""")
```

---

## 6. Point-in-Time Correctness

> **Section Dependencies:**
> - Depends on: Sections 2-5
> - Feeds into: Training pipelines, MOP-010 (Experiments)
> - Update trigger: Data leakage issues discovered

### 6.1 The Problem

```
┌─────────────────────────────────────────────────────────────────────┐
│              Point-in-Time Correctness Problem                       │
│                                                                     │
│  Training Data Generation WITHOUT Point-in-Time:                    │
│                                                                     │
│  Labels:     Transaction at T1 ──── Transaction at T2              │
│              (Fraud: Yes)          (Fraud: No)                      │
│                    │                      │                         │
│                    │    WRONG! Uses       │                         │
│                    │    future data       │                         │
│                    ▼                      ▼                         │
│  Features:  User features at T3 ─── User features at T3            │
│             (includes T2 data!)     (includes T2 data!)            │
│                                                                     │
│  Result: Data leakage, inflated metrics, poor production perf      │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────│
│                                                                     │
│  Training Data Generation WITH Point-in-Time:                       │
│                                                                     │
│  Labels:     Transaction at T1 ──── Transaction at T2              │
│              (Fraud: Yes)          (Fraud: No)                      │
│                    │                      │                         │
│                    │    CORRECT! Uses     │                         │
│                    │    only past data    │                         │
│                    ▼                      ▼                         │
│  Features:  User features at T1 ─── User features at T2            │
│             (only data < T1)        (only data < T2)               │
│                                                                     │
│  Result: Accurate evaluation, reliable production performance      │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 Point-in-Time Join

```python
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="feature_repo/")

# Entity dataframe with timestamps
entity_df = pd.DataFrame({
    "user_id": ["user_1", "user_2", "user_3", "user_1"],
    "event_timestamp": [
        datetime(2024, 1, 10, 10, 0),  # T1
        datetime(2024, 1, 10, 11, 0),  # T2
        datetime(2024, 1, 10, 12, 0),  # T3
        datetime(2024, 1, 11, 10, 0),  # T4 (same user, different time)
    ],
    "label": [1, 0, 0, 1]
})

# Get historical features with point-in-time correctness
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_features:transaction_count_30d",
        "user_features:avg_transaction_amount",
        "user_features:total_spend_30d",
        "merchant_features:fraud_rate"
    ]
).to_df()

# Result: Each row gets features as they were at that timestamp
# user_1 at T1 gets features computed with data < T1
# user_1 at T4 gets features computed with data < T4 (different values!)
```

### 6.3 TTL and Staleness

```python
from feast import FeatureView
from datetime import timedelta

# Feature view with TTL
user_features = FeatureView(
    name="user_features",
    entities=[user],
    schema=[...],
    source=user_features_source,
    ttl=timedelta(days=1),  # Features older than 1 day are stale
    online=True
)

# During point-in-time join:
# If event_timestamp - feature_timestamp > ttl:
#   Feature value = NULL (or default)
```

---

## 7. Feature Serving

> **Section Dependencies:**
> - Depends on: Section 4 (Online Store)
> - Feeds into: MOP-012 (Model Serving)
> - Update trigger: Latency requirements change

### 7.1 Online Serving Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Feature Serving Architecture                      │
│                                                                     │
│  ┌──────────────┐                                                   │
│  │   Client     │                                                   │
│  │ (Model Server)│                                                  │
│  └──────┬───────┘                                                   │
│         │ Request: {user_id: "123"}                                 │
│         ▼                                                           │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                   Feature Server                              │  │
│  │                                                               │  │
│  │  ┌─────────────────────────────────────────────────────────┐ │  │
│  │  │                   Request Handler                        │ │  │
│  │  │  - Parse feature requests                                │ │  │
│  │  │  - Validate entity keys                                  │ │  │
│  │  │  - Route to appropriate stores                           │ │  │
│  │  └─────────────────────────────────────────────────────────┘ │  │
│  │                          │                                    │  │
│  │         ┌────────────────┼────────────────┐                  │  │
│  │         ▼                ▼                ▼                  │  │
│  │  ┌───────────┐    ┌───────────┐    ┌───────────┐           │  │
│  │  │  Redis    │    │ DynamoDB  │    │ On-Demand │           │  │
│  │  │  Lookup   │    │  Lookup   │    │  Compute  │           │  │
│  │  └───────────┘    └───────────┘    └───────────┘           │  │
│  │         │                │                │                  │  │
│  │         └────────────────┼────────────────┘                  │  │
│  │                          ▼                                    │  │
│  │  ┌─────────────────────────────────────────────────────────┐ │  │
│  │  │                Response Assembler                        │ │  │
│  │  │  - Merge features from stores                            │ │  │
│  │  │  - Apply default values                                  │ │  │
│  │  │  - Format response                                       │ │  │
│  │  └─────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────┘  │
│         │                                                           │
│         ▼ Response: {features: {...}}                              │
│  ┌──────────────┐                                                   │
│  │   Client     │                                                   │
│  └──────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 Online Feature Retrieval

```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo/")

# Single entity lookup
features = store.get_online_features(
    features=[
        "user_features:transaction_count_30d",
        "user_features:avg_transaction_amount",
        "merchant_features:fraud_rate"
    ],
    entity_rows=[
        {"user_id": "user_123", "merchant_id": "merchant_456"}
    ]
).to_dict()

# Result
# {
#     "user_id": ["user_123"],
#     "merchant_id": ["merchant_456"],
#     "transaction_count_30d": [45],
#     "avg_transaction_amount": [125.50],
#     "fraud_rate": [0.02]
# }

# Batch lookup for multiple entities
features = store.get_online_features(
    features=[...],
    entity_rows=[
        {"user_id": "user_1", "merchant_id": "merchant_1"},
        {"user_id": "user_2", "merchant_id": "merchant_2"},
        {"user_id": "user_3", "merchant_id": "merchant_3"},
    ]
)
```

### 7.3 Feature Server Deployment

```yaml
# Kubernetes deployment for Feast feature server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: feast-feature-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: feast-feature-server
  template:
    metadata:
      labels:
        app: feast-feature-server
    spec:
      containers:
      - name: feature-server
        image: feast-feature-server:latest
        ports:
        - containerPort: 6566
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        env:
        - name: FEAST_REPO_PATH
          value: "/feast"
        - name: FEAST_ONLINE_STORE_TYPE
          value: "redis"
        livenessProbe:
          httpGet:
            path: /health
            port: 6566
        readinessProbe:
          httpGet:
            path: /ready
            port: 6566

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: feast-feature-server-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: feast-feature-server
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 7.4 REST API Specification

```http
POST /get-online-features
Content-Type: application/json

{
  "features": [
    "user_features:transaction_count_30d",
    "user_features:avg_transaction_amount"
  ],
  "entities": {
    "user_id": ["user_123", "user_456"]
  }
}

Response:
{
  "metadata": {
    "feature_names": [
      "user_id",
      "transaction_count_30d",
      "avg_transaction_amount"
    ]
  },
  "results": [
    {
      "values": ["user_123", 45, 125.50],
      "statuses": ["PRESENT", "PRESENT", "PRESENT"],
      "event_timestamps": ["2024-01-15T10:00:00Z", ...]
    },
    {
      "values": ["user_456", 23, 89.99],
      "statuses": ["PRESENT", "PRESENT", "PRESENT"],
      "event_timestamps": ["2024-01-15T10:00:00Z", ...]
    }
  ]
}
```

---

## 8. Governance & Monitoring

> **Section Dependencies:**
> - Depends on: All sections
> - Feeds into: Compliance, Operations
> - Update trigger: Policy changes

### 8.1 Feature Discovery & Catalog

```yaml
# Feature catalog metadata
feature_catalog:
  user_features:
    description: "User-level behavioral features"
    owner: "customer-analytics@company.com"
    team: "Customer Analytics"
    tags:
      domain: "customer"
      pii: "false"
      sensitivity: "internal"
    
    features:
      transaction_count_30d:
        description: "Number of transactions in the last 30 days"
        dtype: INT64
        example: 45
        compute_frequency: "daily"
        freshness_sla: "24 hours"
        
      avg_transaction_amount:
        description: "Average transaction amount over 30 days"
        dtype: FLOAT64
        example: 125.50
        unit: "USD"
        
    consumers:
      - "fraud-detection-model-v2"
      - "customer-segmentation"
      - "churn-prediction"
```

### 8.2 Feature Lineage

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Feature Lineage                                 │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐            │
│  │   Source    │───►│   Feature   │───►│    Model    │            │
│  │   Tables    │    │    View     │    │   (Consumer)│            │
│  └─────────────┘    └─────────────┘    └─────────────┘            │
│                                                                     │
│  transactions ──┬──► user_features ──┬──► fraud-detection-v2       │
│                 │                    │                              │
│  users ─────────┘                    ├──► customer-segmentation    │
│                                      │                              │
│                                      └──► churn-prediction         │
│                                                                     │
│  Lineage captures:                                                  │
│  - Data sources                                                     │
│  - Transformations applied                                          │
│  - Downstream consumers                                             │
│  - Version history                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.3 Monitoring Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Freshness** | Time since last update | > SLA |
| **Null rate** | % of null values | > 5% |
| **Serving latency** | P99 retrieval time | > 20ms |
| **Error rate** | Failed feature lookups | > 0.1% |
| **Drift** | Feature distribution shift | KL > 0.1 |
| **Coverage** | % entities with features | < 95% |

### 8.4 Feature Validation

```python
import great_expectations as ge

# Define feature expectations
expectation_suite = ge.core.ExpectationSuite(
    expectation_suite_name="user_features_validation"
)

# Column expectations
expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "transaction_count_30d"}
    )
)

expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_between",
        kwargs={
            "column": "avg_transaction_amount",
            "min_value": 0,
            "max_value": 100000
        }
    )
)

expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_mean_to_be_between",
        kwargs={
            "column": "transaction_count_30d",
            "min_value": 10,  # Expected range based on historical data
            "max_value": 100
        }
    )
)

# Run validation after feature computation
results = ge.validate(feature_df, expectation_suite)
if not results.success:
    raise FeatureValidationError(results)
```

### 8.5 Access Control

| Role | Read Features | Create Features | Modify Features | Admin |
|------|---------------|-----------------|-----------------|-------|
| Viewer |  |  |  |  |
| Data Scientist |  |  (own team) |  (own) |  |
| ML Engineer |  |  |  (own team) |  |
| Platform Admin |  |  |  |  |

---

## Appendices

### Appendix A: Feature Store Repository Structure

```
feature_repo/
├── feature_repo.yaml         # Feast configuration
├── entities.py               # Entity definitions
├── sources.py                # Data source definitions
├── features/
│   ├── user_features.py      # User feature views
│   ├── merchant_features.py  # Merchant feature views
│   └── transaction_features.py
├── pipelines/
│   ├── batch_pipeline.py     # Batch feature computation
│   └── streaming_pipeline.py # Streaming computation
├── tests/
│   ├── test_features.py      # Feature unit tests
│   └── test_serving.py       # Serving tests
└── README.md
```

### Appendix B: Feast CLI Quick Reference

```bash
# Apply feature definitions
feast apply

# Materialize features to online store
feast materialize 2024-01-01 2024-01-15

# Incremental materialization
feast materialize-incremental $(date +%Y-%m-%d)

# Serve features
feast serve --port 6566

# View feature registry
feast registry-dump

# Teardown
feast teardown
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Author] | Initial draft |
| 1.0 | [Date] | [Author] | Approved version |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Lead | | | |
| Data Engineering Lead | | | |
| Data Governance | | | |
