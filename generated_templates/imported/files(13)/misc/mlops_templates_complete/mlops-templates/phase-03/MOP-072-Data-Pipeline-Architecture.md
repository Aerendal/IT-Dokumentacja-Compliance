---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-072: Data Pipeline Architecture

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-072 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Data Engineering / ML Platform] |

---

## 1. Pipeline Architecture Overview

### 1.1 Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                      ML Data Pipeline Architecture                   │
│                                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐     │
│  │  Sources │───►│  Ingest  │───►│ Transform│───►│  Store   │     │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘     │
│       │              │                │               │            │
│       ▼              ▼                ▼               ▼            │
│  • Databases     • Kafka          • Spark         • S3 (Raw)      │
│  • APIs          • Airflow        • dbt           • S3 (Processed)│
│  • Files         • CDC            • Python        • Feature Store │
│  • Streams                                        • Data Lake     │
│                                                                     │
│                         ▼                                          │
│               ┌──────────────────┐                                 │
│               │  ML Consumption  │                                 │
│               └──────────────────┘                                 │
│                       │                                            │
│         ┌─────────────┼─────────────┐                             │
│         ▼             ▼             ▼                             │
│    Training      Features      Inference                          │
│     Data          Online         Batch                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Ingestion Layer

### 2.1 Batch Ingestion

```python
# pipelines/batch_ingestion.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_ingestion_daily',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    catchup=False,
) as dag:
    
    def ingest_from_source(source_config: dict, **context):
        """Generic ingestion function."""
        from data_pipeline import SourceConnector, DataLakeWriter
        
        execution_date = context['execution_date']
        
        connector = SourceConnector(source_config)
        writer = DataLakeWriter(
            bucket="data-lake-raw",
            prefix=f"{source_config['name']}/{execution_date.strftime('%Y/%m/%d')}"
        )
        
        data = connector.extract(
            start_date=execution_date - timedelta(days=1),
            end_date=execution_date
        )
        
        writer.write(data, format='parquet')
        
        return {"rows": len(data), "path": writer.path}
    
    # Define ingestion tasks
    sources = ['transactions', 'users', 'events']
    for source in sources:
        PythonOperator(
            task_id=f'ingest_{source}',
            python_callable=ingest_from_source,
            op_kwargs={'source_config': {'name': source}},
        )
```

### 2.2 Streaming Ingestion

```python
# pipelines/stream_ingestion.py
from kafka import KafkaConsumer
import json

class StreamIngestion:
    """Real-time data ingestion from Kafka."""
    
    def __init__(self, topic: str, bootstrap_servers: list):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='ml-ingestion',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    
    def process_stream(self, handler):
        """Process messages with given handler."""
        for message in self.consumer:
            try:
                handler(message.value)
            except Exception as e:
                self.handle_error(message, e)
    
    def handle_error(self, message, error):
        """Send failed messages to DLQ."""
        # Send to dead letter queue
        pass
```

---

## 3. Transformation Layer

### 3.1 dbt Models

```sql
-- models/features/user_features.sql
{{ config(
    materialized='incremental',
    unique_key='user_id',
    partition_by={'field': 'updated_at', 'data_type': 'date'}
) }}

WITH user_transactions AS (
    SELECT
        user_id,
        COUNT(*) as transaction_count_30d,
        SUM(amount) as total_amount_30d,
        AVG(amount) as avg_amount_30d,
        MAX(created_at) as last_transaction_at
    FROM {{ ref('transactions') }}
    WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
),

user_profile AS (
    SELECT
        user_id,
        account_age_days,
        verification_status,
        country
    FROM {{ ref('users') }}
)

SELECT
    up.user_id,
    up.account_age_days,
    up.verification_status,
    up.country,
    COALESCE(ut.transaction_count_30d, 0) as transaction_count_30d,
    COALESCE(ut.total_amount_30d, 0) as total_amount_30d,
    COALESCE(ut.avg_amount_30d, 0) as avg_amount_30d,
    ut.last_transaction_at,
    CURRENT_TIMESTAMP as updated_at
FROM user_profile up
LEFT JOIN user_transactions ut ON up.user_id = ut.user_id

{% if is_incremental() %}
WHERE up.user_id IN (
    SELECT DISTINCT user_id 
    FROM {{ ref('transactions') }}
    WHERE created_at >= (SELECT MAX(updated_at) FROM {{ this }})
)
{% endif %}
```

### 3.2 Spark Transformation

```python
# pipelines/spark_transform.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def transform_for_training(spark: SparkSession, input_path: str, output_path: str):
    """Transform raw data for ML training."""
    
    # Read raw data
    df = spark.read.parquet(input_path)
    
    # Feature engineering
    df_features = df.withColumn(
        "hour_of_day", F.hour("timestamp")
    ).withColumn(
        "day_of_week", F.dayofweek("timestamp")
    ).withColumn(
        "amount_log", F.log1p("amount")
    ).withColumn(
        "is_weekend", F.when(F.col("day_of_week").isin([1, 7]), 1).otherwise(0)
    )
    
    # Handle nulls
    df_clean = df_features.fillna({
        "amount": 0,
        "category": "unknown"
    })
    
    # Write output
    df_clean.write.mode("overwrite").parquet(output_path)
    
    return df_clean.count()
```

---

## 4. Data Quality

### 4.1 Great Expectations Suite

```python
# data_quality/expectations.py
import great_expectations as gx

def create_training_data_suite():
    """Create data quality suite for training data."""
    
    context = gx.get_context()
    
    suite = context.add_expectation_suite("training_data_suite")
    
    # Schema expectations
    suite.add_expectation(
        gx.expectations.ExpectTableColumnsToMatchOrderedList(
            column_list=["user_id", "amount", "timestamp", "label"]
        )
    )
    
    # Completeness
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="user_id")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="label")
    )
    
    # Value ranges
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="amount", min_value=0, max_value=1000000
        )
    )
    
    # Distribution
    suite.add_expectation(
        gx.expectations.ExpectColumnProportionOfUniqueValuesToBeBetween(
            column="label", min_value=0.01, max_value=0.5
        )
    )
    
    return suite
```

### 4.2 Validation Pipeline

```python
# data_quality/validation.py
from airflow.operators.python import BranchPythonOperator

def validate_data(**context):
    """Validate data and decide next step."""
    import great_expectations as gx
    
    context = gx.get_context()
    result = context.run_checkpoint(
        checkpoint_name="training_data_checkpoint",
        batch_request={
            "datasource_name": "data_lake",
            "data_asset_name": "training_data",
        }
    )
    
    if result.success:
        return "continue_pipeline"
    else:
        return "alert_data_quality_failure"

validate_task = BranchPythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
)
```

---

## 5. Data Catalog

### 5.1 Schema Registry

```yaml
# schemas/training_data.yaml
name: training_data
version: "2.0"
description: "Training data for fraud detection model"

schema:
  - name: user_id
    type: string
    description: "Unique user identifier"
    nullable: false
    pii: false
    
  - name: amount
    type: float
    description: "Transaction amount in USD"
    nullable: false
    constraints:
      min: 0
      max: 1000000
      
  - name: timestamp
    type: timestamp
    description: "Transaction timestamp"
    nullable: false
    
  - name: label
    type: integer
    description: "Fraud label (0=legitimate, 1=fraud)"
    nullable: false
    constraints:
      allowed_values: [0, 1]

lineage:
  sources:
    - transactions
    - users
  transformations:
    - dbt/user_features.sql
    - spark/feature_engineering.py
```

---

## 6. Pipeline Monitoring

### 6.1 Metrics

```python
# monitoring/pipeline_metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Ingestion metrics
rows_ingested = Counter(
    'data_pipeline_rows_ingested_total',
    'Total rows ingested',
    ['source', 'pipeline']
)

ingestion_duration = Histogram(
    'data_pipeline_ingestion_duration_seconds',
    'Ingestion duration',
    ['source']
)

# Quality metrics
data_quality_score = Gauge(
    'data_pipeline_quality_score',
    'Data quality score (0-1)',
    ['dataset']
)

validation_failures = Counter(
    'data_pipeline_validation_failures_total',
    'Validation failures',
    ['dataset', 'check']
)
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial data pipeline architecture |
