---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Data Engineering Research Summary 2024-2025

## Modern Data Stack Evolution

### Cloud Data Warehouses/Lakehouses
| Platform | Key Features 2024-2025 | Market Position |
|----------|------------------------|-----------------|
| **Snowflake** | Native Python & AI, Semantic Views, Cortex AI, Apache Iceberg support | Enterprise leader, Summit 2025 announcements |
| **Databricks** | Unity Catalog, Delta Lake, Lakehouse architecture, AI/ML integration | Lakehouse leader, acquired Tabular |
| **BigQuery** | Serverless, GCP integration, Iceberg support via BigLake | Google Cloud native |
| **Redshift** | AWS ecosystem, materialized views, real-time capabilities | AWS native |

### Open Table Formats (Lakehouse Foundation)
| Format | Origin | Key Features | Best For |
|--------|--------|--------------|----------|
| **Apache Iceberg** | Netflix (2017) | Vendor-neutral, multi-engine support, hidden partitioning, schema evolution | Read-heavy analytics, multi-engine environments |
| **Delta Lake** | Databricks (2017) | ACID transactions, UniForm interoperability, Deletion Vectors, tight Spark integration | Spark/Databricks ecosystems, real-time pipelines |
| **Apache Hudi** | Uber | Strong CDC support, merge-on-read/write, incremental processing | Update-heavy workloads, streaming CDC |

### Data Transformation Tools
| Tool | Type | Key Features 2024-2025 |
|------|------|------------------------|
| **dbt** | ELT Transformation | Semantic layer (MetricFlow), expanding into cataloging/orchestration/observability |
| **Dataform** | ELT | Google-owned, BigQuery focus |
| **Coalesce** | ELT | Visual transformation, Snowflake native |

### Data Integration/Ingestion
| Tool | Type | Features |
|------|------|----------|
| **Fivetran** | Managed EL | 300+ connectors, Iceberg writes, no-code |
| **Airbyte** | Open-source EL | 400+ connectors, self-hosted option |
| **Meltano** | Open-source | Singer-based, orchestration integration |

## Data Quality Frameworks 2024-2025

### Comparison Matrix
| Tool | Language | Best For | Integration |
|------|----------|----------|-------------|
| **Great Expectations (GX)** | Python | Expressive validation, CI/CD integration | Airflow, dbt, Prefect, Dagster |
| **Soda Core** | SodaCL (YAML) | Lightweight SQL checks, fast setup | 20+ data sources, Soda Cloud |
| **dbt tests** | SQL/YAML | Transformation-embedded testing | dbt ecosystem |
| **Deequ** | Spark/Scala | Large-scale Spark datasets | AWS, Spark |
| **Elementary** | dbt | dbt-native observability, anomaly detection | dbt ecosystem |

### Data Quality Dimensions
- **Completeness**: No missing required values
- **Accuracy**: Values match expected patterns/ranges
- **Consistency**: Same data across systems
- **Timeliness**: Data freshness (SLA compliance)
- **Uniqueness**: No duplicate records
- **Validity**: Conforms to business rules

## Data Orchestration 2024-2025

### Apache Airflow 3.0 (April 2025)
- **Major milestone**: Biggest update in platform history
- **Downloads**: 320M in 2024 (10x nearest competitor)
- **New Features**:
  - DAG versioning (most requested feature)
  - Multi-language Task SDKs
  - Event-driven scheduling with Data Assets
  - Python TaskSDK for backward compatibility
- **Usage**: 80,000+ organizations, 30% MLOps, 10% GenAI

### Dagster (2025)
- **Philosophy**: Asset-centric orchestration
- **Components GA**: October 2025
- **Catalog 1.7**: Enhanced asset visibility
- **Best For**: Data quality, lineage tracking, ML pipelines
- **dbt Integration**: Native asset mapping

### Prefect (2025)
- **Philosophy**: Developer-friendly, negative engineering
- **Features**:
  - Incidents for disruption management
  - Metrics-based automation triggers
  - Native Modal integration
  - Dropped Python 3.9, embraced 3.10+
- **Best For**: Dynamic/event-driven workflows, cloud-native teams

## Data Governance & Catalogs 2024-2025

### Enterprise Platforms
| Platform | Strength | Best For |
|----------|----------|----------|
| **Collibra** | Enterprise governance, compliance workflows | Regulated industries (finance, healthcare) |
| **Alation** | AI-powered discovery, data literacy | Data democratization |
| **Atlan** | Modern workspace, automation, AI | Modern data teams |
| **Informatica IDMC** | Full data management suite | Existing Informatica customers |

### Open-Source Catalogs
| Tool | Origin | Key Features |
|------|--------|--------------|
| **DataHub** | LinkedIn | Real-time metadata, graph-based, extensible |
| **OpenMetadata** | Collate | Modular, real-time ingestion, federated governance |
| **Apache Atlas** | Hortonworks | Hadoop ecosystem, strong lineage |
| **Amundsen** | Lyft | Simple discovery, PageRank search |
| **Marquez** | WeWork | Lineage-focused, OpenLineage foundation |

## Streaming & Real-Time Data

### Stream Processing Stack
| Tool | Purpose | Features 2024-2025 |
|------|---------|-------------------|
| **Apache Kafka** | Event streaming | Confluent Cloud, KSQL, Connect |
| **Apache Flink** | Stream processing | Stateful processing, exactly-once |
| **Apache Pulsar** | Event streaming | Multi-tenancy, geo-replication |
| **Amazon Kinesis** | AWS streaming | Serverless, AWS integration |

## Key Data Engineering Metrics

### Pipeline Performance
| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Pipeline SLA compliance | >99% | 95-99% | <95% |
| Data freshness (latency) | <5min | 5-30min | >30min |
| Pipeline success rate | >98% | 95-98% | <95% |
| Mean time to recovery | <15min | 15-60min | >60min |

### Data Quality Metrics
| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Data completeness | >99.5% | 98-99.5% | <98% |
| Schema drift incidents | 0/month | 1-2/month | >2/month |
| Data quality test coverage | >80% | 50-80% | <50% |
| Anomaly detection rate | >95% | 80-95% | <80% |

## Data Engineering Standards & Certifications

### Industry Standards
- **DMBOK** (Data Management Body of Knowledge)
- **DAMA-DMBOK2**: Data management framework
- **CDMP**: Certified Data Management Professional
- **ISO 8000**: Data quality standards

### Cloud Certifications
- **AWS**: Data Analytics Specialty, Database Specialty
- **GCP**: Professional Data Engineer
- **Azure**: Data Engineer Associate (DP-203)
- **Snowflake**: SnowPro Core, SnowPro Advanced
- **Databricks**: Data Engineer Associate/Professional

## Compliance & Regulations

### Data Privacy
- **GDPR** (EU): Data subject rights, consent, DPO requirement
- **CCPA/CPRA** (California): Consumer data rights
- **LGPD** (Brazil): Similar to GDPR
- **PIPEDA** (Canada): Personal information protection

### Industry-Specific
- **HIPAA**: Healthcare data protection
- **PCI DSS**: Payment card data
- **SOX**: Financial data controls
- **SOC 2**: Service organization controls

## Architecture Patterns 2024-2025

### Lakehouse Architecture
- Combines data lake flexibility with warehouse reliability
- Open table formats (Iceberg/Delta Lake) as foundation
- Single storage layer for analytics and ML
- ACID transactions on object storage

### Data Mesh
- Domain-oriented decentralized ownership
- Data as a product
- Self-serve data infrastructure
- Federated computational governance

### Modern Data Stack (MDS)
- Cloud-native, modular architecture
- ELT over ETL (transform in warehouse)
- Composable tools (Fivetran + dbt + Snowflake + Looker)
- Pay-as-you-go pricing model

### Real-Time Data Architecture
- Event-driven pipelines (Kafka/Flink)
- Streaming into lakehouse (Iceberg/Delta)
- Real-time analytics and dashboards
- CDC (Change Data Capture) integration
