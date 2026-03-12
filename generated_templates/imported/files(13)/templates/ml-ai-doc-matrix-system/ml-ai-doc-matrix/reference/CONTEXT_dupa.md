---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# ML/AI Documentation Matrix - Reference Guide
## Industry #6: Machine Learning / Artificial Intelligence

### Overview
Comprehensive documentation framework for ML/AI projects covering the complete
machine learning lifecycle from problem definition through model deployment,
monitoring, and governance.

**Created:** 2025-01-31  
**Version:** 1.0  
**Total Documents:** 124  
**Lifecycle Phases:** 23  

---

## Database Statistics

| Category | Count |
|----------|-------|
| Documents | 124 |
| Phases | 23 |
| Document Types | 22 |
| DL Frameworks | 15 |
| MLOps Platforms | 15 |
| Model Serving Tools | 12 |
| Feature Stores | 10 |
| Monitoring Tools | 12 |
| Model Types | 15 |
| ML Metrics | 20 |
| AI Regulations | 8 |
| Cloud ML Platforms | 8 |
| Explainability Tools | 10 |
| Data Versioning Tools | 8 |
| Hyperparameter Methods | 8 |
| NN Architectures | 12 |
| LLMOps Tools | 10 |
| ML Maturity Levels | 5 |
| AI Risk Categories | 4 |

---

## Phases Overview

**Phase 1: CONCEPT_VISION** (4 docs)
- ML Problem Definition and Business Value Assessment

**Phase 2: REQUIREMENTS_ANALYSIS** (5 docs)
- ML Requirements, Data Needs, Success Metrics

**Phase 3: DESIGN** (6 docs)
- ML Architecture, Feature Engineering, Model Selection

**Phase 4: PLANNING** (4 docs)
- ML Project Timeline, Experiment Planning, Resources

**Phase 5: IMPLEMENTATION** (5 docs)
- Data Preparation, Feature Engineering, Model Training

**Phase 6: TESTING_QA** (5 docs)
- Model Testing, Validation, Adversarial Testing

**Phase 7: SECURITY_COMPLIANCE** (6 docs)
- AI Ethics, Bias Mitigation, Regulatory Compliance

**Phase 8: DEPLOYMENT** (5 docs)
- Model Serving, Containerization, A/B Testing

**Phase 9: OPERATIONS_MAINTENANCE** (5 docs)
- Model Monitoring, Retraining, Performance Maintenance

**Phase 10: INCIDENT_MANAGEMENT** (3 docs)
- Model Failure Recovery, Rollback Procedures

**Phase 11: MONITORING_OBSERVABILITY** (5 docs)
- Data Drift, Model Drift, Feature Monitoring

**Phase 12: REFERENCE_DOCUMENTATION** (5 docs)
- Model Documentation, Dataset Documentation, API Reference

**Phase 13: TRAINING_ONBOARDING** (4 docs)
- ML Engineer Onboarding, Framework Training

**Phase 14: STAKEHOLDER_COMMUNICATION** (4 docs)
- Model Performance Reports, Business Impact

**Phase 15: KNOWLEDGE_MANAGEMENT** (5 docs)
- ML Best Practices, Model Patterns, Feature Library

**Phase 16: POSTMORTEM_RETROSPECTIVE** (4 docs)
- ML Model Retrospective, Lessons Learned

**Phase 17: BUDGETING_COST_MANAGEMENT** (6 docs)
- ML Compute Costs, GPU Budget, Cloud Costs

**Phase 18: VENDOR_PROCUREMENT** (7 docs)
- ML Platform Evaluation, Cloud Provider Selection

**Phase 19: GOVERNANCE_COMPLIANCE_AUDITING** (7 docs)
- AI Governance, Model Audit, Compliance

**Phase 20: DECOMMISSIONING_EOL** (7 docs)
- Model Retirement, Data Archival

**Phase 21: DISASTER_RECOVERY_BCP** (8 docs)
- Model Recovery, Backup Strategies

**Phase 22: CHANGE_MANAGEMENT** (7 docs)
- Model Version Changes, Retraining Triggers

**Phase 23: CAPACITY_PLANNING** (7 docs)
- GPU Capacity, Inference Scaling, Growth Planning

---

## Critical Documents (Priority: CRITICAL)

- **ML-FEA**: Feasibility Assessment (CONCEPT_VISION)
  - Technical and data feasibility assessment for ML solution
- **ML-PSD**: ML Problem Statement (CONCEPT_VISION)
  - Definition of the ML problem to solve including business context
- **ML-DRQ**: Data Requirements for ML (REQUIREMENTS_ANALYSIS)
  - Data requirements including volume, quality, and sources
- **ML-REQ**: ML Requirements Specification (REQUIREMENTS_ANALYSIS)
  - Complete ML model requirements and constraints
- **ML-ARC**: ML Architecture Document (DESIGN)
  - Complete ML system architecture design
- **ML-FEP**: Feature Engineering Plan (DESIGN)
  - Feature engineering strategy and implementation plan
- **ML-DPC**: Data Preparation Code (IMPLEMENTATION)
  - Data preparation and preprocessing code
- **ML-MTC**: Model Training Code (IMPLEMENTATION)
  - Model training implementation and scripts
- **ML-FBT**: Fairness and Bias Testing (TESTING_QA)
  - Bias detection and fairness evaluation
- **ML-MTP**: Model Testing Plan (TESTING_QA)
  - Comprehensive model testing strategy
- **ML-EUA**: EU AI Act Compliance Assessment (SECURITY_COMPLIANCE)
  - Detailed EU AI Act compliance evaluation
- **ML-EXP**: Model Explainability Documentation (SECURITY_COMPLIANCE)
  - Model explainability and interpretability docs
- **ML-RCC**: Regulatory Compliance Check (SECURITY_COMPLIANCE)
  - Compliance assessment with AI regulations
- **ML-MSA**: Model Serving Architecture (DEPLOYMENT)
  - Architecture for model deployment and serving
- **ML-PDG**: Production Deployment Guide (DEPLOYMENT)
  - Step-by-step production deployment guide
- **ML-MDD**: Model Drift Detection (OPERATIONS_MAINTENANCE)
  - Procedures for detecting model drift
- **ML-MMG**: Model Monitoring Guide (OPERATIONS_MAINTENANCE)
  - Guide for monitoring model in production
- **ML-MFR**: Model Failure Recovery (INCIDENT_MANAGEMENT)
  - Procedures for model failure recovery
- **ML-RBP**: Rollback Procedure (INCIDENT_MANAGEMENT)
  - Procedures for rolling back to previous model
- **ML-PMT**: Model Performance Metrics (MONITORING_OBSERVABILITY)
  - Production model performance metrics tracking
- **ML-MDC**: Model Documentation (REFERENCE_DOCUMENTATION)
  - Complete ML model documentation
- **ML-BCP**: Business Continuity Plan (DISASTER_RECOVERY_BCP)
  - Business continuity for ML systems
- **ML-DRP**: Disaster Recovery Plan (DISASTER_RECOVERY_BCP)
  - ML system disaster recovery plan

---

## Deep Learning Frameworks

| Framework | Vendor | Type | GPU Support | Market Share 2025 | Best For |
|-----------|--------|------|-------------|-------------------|----------|
| PyTorch | Meta AI | LOW_LEVEL | CUDA, ROCm, MPS | 55% | Research, NLP, Generative AI |
| TensorFlow | Google | LOW_LEVEL | CUDA, TPU | 38% | Production, Mobile, Enterprise |
| Keras | Google | HIGH_LEVEL | Via TensorFlow/PyTorch/JAX | N/A | Rapid prototyping, beginners |
| JAX | Google DeepMind | LOW_LEVEL | CUDA, TPU | 5% | Research, high-performance computing |
| Flax | Google | HIGH_LEVEL | Via JAX | N/A | JAX-based neural networks |
| PyTorch Lightning | Lightning AI | WRAPPER | Via PyTorch | N/A | Structured PyTorch training |
| Hugging Face Transformers | Hugging Face | HIGH_LEVEL | CUDA | N/A | NLP, LLMs, pretrained models |
| FastAI | fast.ai | HIGH_LEVEL | Via PyTorch | N/A | Education, rapid prototyping |
| MXNet | Apache/AWS | LOW_LEVEL | CUDA | <1% | AWS deployments, legacy |
| ONNX Runtime | Microsoft | LOW_LEVEL | CUDA, DirectML | N/A | Cross-framework inference |
| scikit-learn | Community | HIGH_LEVEL | CPU only | N/A | Classical ML, tabular data |
| XGBoost | DMLC | HIGH_LEVEL | CUDA | N/A | Gradient boosting, tabular |
| LightGBM | Microsoft | HIGH_LEVEL | CUDA | N/A | Gradient boosting, large datasets |
| CatBoost | Yandex | HIGH_LEVEL | CUDA | N/A | Categorical features, tabular |
| Detectron2 | Meta AI | HIGH_LEVEL | CUDA | N/A | Computer vision, object detection |

---

## MLOps Platforms

| Platform | Vendor | Type | Exp Track | Registry | Pipeline | Best For |
|----------|--------|------|-----------|----------|----------|----------|
| MLflow | Databricks | OPEN_SOURCE | Y | Y | N | Flexible, vendor-independent teams |
| Kubeflow | Google/CNCF | OPEN_SOURCE | Y | Y | Y | Kubernetes-native enterprise deployments |
| Weights & Biases | W&B Inc | COMMERCIAL | Y | Y | N | Research teams, experiment tracking |
| Neptune.ai | Neptune Labs | COMMERCIAL | Y | Y | N | Research organizations, metadata tracking |
| Comet ML | Comet | COMMERCIAL | Y | Y | N | Experiment tracking, model comparison |
| DVC | Iterative | OPEN_SOURCE | Y | Y | N | Data and model versioning |
| Metaflow | Netflix/Outerbounds | OPEN_SOURCE | Y | N | Y | Data science workflows |
| ZenML | ZenML | OPEN_SOURCE | Y | Y | Y | Modular MLOps stacks |
| ClearML | ClearML | OPEN_SOURCE | Y | Y | Y | All-in-one MLOps |
| Flyte | Union.ai | OPEN_SOURCE | Y | Y | Y | Scalable ML pipelines |
| Databricks MLflow | Databricks | COMMERCIAL | Y | Y | Y | Databricks ecosystem |
| AWS SageMaker | Amazon | CLOUD_NATIVE | Y | Y | Y | AWS-centric organizations |
| Google Vertex AI | Google | CLOUD_NATIVE | Y | Y | Y | GCP-centric organizations |
| Azure Machine Learning | Microsoft | CLOUD_NATIVE | Y | Y | Y | Azure-centric enterprises |
| H2O.ai | H2O.ai | COMMERCIAL | Y | Y | Y | AutoML, enterprise AI |

---

## Model Serving Tools

| Tool | Vendor | Framework Support | K8s | Batch | RT | Best For |
|------|--------|-------------------|-----|-------|----|---------|
| TorchServe | AWS/Meta | PyTorch | N | Y | Y | PyTorch model deployment |
| TensorFlow Serving | Google | TensorFlow | N | Y | Y | TensorFlow model deployment |
| NVIDIA Triton | NVIDIA | Multi-framework | Y | Y | Y | GPU-optimized high-performance inference |
| BentoML | BentoML | Multi-framework | N | Y | Y | Framework-agnostic, developer-friendly |
| KServe | Kubeflow/CNCF | Multi-framework | Y | Y | Y | Kubernetes-native serverless inference |
| Seldon Core | Seldon | Multi-framework | Y | Y | Y | Advanced deployment strategies on K8s |
| Ray Serve | Anyscale | Multi-framework | N | Y | Y | Distributed AI applications |
| MLflow Model Serving | Databricks | Multi-framework | N | Y | Y | MLflow ecosystem integration |
| vLLM | vLLM | LLMs | Y | N | Y | High-throughput LLM inference |
| TGI | Hugging Face | Transformers | Y | N | Y | Text generation, LLM serving |
| OpenLLM | BentoML | LLMs | Y | N | Y | Open-source LLM deployment |
| SageMaker Endpoints | AWS | Multi-framework | N | Y | Y | AWS managed inference |

---

## Feature Stores

| Store | Vendor | Type | Online | Offline | Stream | Best For |
|-------|--------|------|--------|---------|--------|---------|
| Feast | Linux Foundation | OPEN_SOURCE | Y | Y | Y | Flexible, multi-backend feature store |
| Tecton | Tecton | MANAGED | Y | Y | Y | Enterprise real-time ML |
| Hopsworks | Hopsworks | OPEN_SOURCE | Y | Y | Y | Regulated industries, governance |
| Vertex AI Feature Store | Google | CLOUD_NATIVE | Y | Y | Y | GCP-native ML workloads |
| SageMaker Feature Store | AWS | CLOUD_NATIVE | Y | Y | Y | AWS-native ML workloads |
| Databricks Feature Store | Databricks | MANAGED | Y | Y | Y | Databricks ecosystem |
| Feathr | LinkedIn/Microsoft | OPEN_SOURCE | Y | Y | Y | Large-scale feature engineering |
| Iguazio | Iguazio/McKinsey | MANAGED | Y | Y | Y | Real-time ML at scale |
| FeatureForm | FeatureForm | OPEN_SOURCE | Y | Y | Y | Virtual feature store |
| ByteHub | ByteHub | OPEN_SOURCE | Y | Y | N | Lightweight feature management |

---

## Model Monitoring Tools

| Tool | Type | Data Drift | Model Drift | Explain | RT | Best For |
|------|------|------------|-------------|---------|----|---------|
| Evidently AI | OPEN_SOURCE | Y | Y | Y | Y | Open-source ML monitoring |
| WhyLabs | COMMERCIAL | Y | Y | N | Y | Privacy-preserving monitoring |
| Arize AI | COMMERCIAL | Y | Y | Y | Y | Enterprise ML observability |
| Fiddler AI | COMMERCIAL | Y | Y | Y | Y | Explainable AI, regulated industries |
| NannyML | OPEN_SOURCE | Y | Y | N | N | Performance estimation without labels |
| Deepchecks | OPEN_SOURCE | Y | Y | N | N | ML validation and testing |
| Alibi Detect | OPEN_SOURCE | Y | Y | N | N | Drift and outlier detection |
| Superwise | COMMERCIAL | Y | Y | Y | Y | Automated model monitoring |
| Aporia | COMMERCIAL | Y | Y | Y | Y | Production ML monitoring |
| SageMaker Model Monitor | CLOUD_NATIVE | Y | Y | N | Y | AWS-native monitoring |
| Vertex AI Model Monitoring | CLOUD_NATIVE | Y | Y | N | Y | GCP-native monitoring |
| Azure ML Monitoring | CLOUD_NATIVE | Y | Y | N | Y | Azure-native monitoring |

---

## ML Metrics

| Metric | Type | Description | Threshold |
|--------|------|-------------|----------|
| Accuracy | CLASSIFICATION | (TP + TN) / Total | >0.90 for production |
| Precision | CLASSIFICATION | TP / (TP + FP) | >0.85 for fraud detection |
| Recall | CLASSIFICATION | TP / (TP + FN) | >0.95 for medical diagnosis |
| F1 Score | CLASSIFICATION | 2 * (Precision * Recall) / (Precision + Recall) | >0.80 balanced |
| AUC-ROC | CLASSIFICATION | Area under ROC curve | >0.85 for production |
| Log Loss | CLASSIFICATION | Cross-entropy loss | <0.3 for production |
| MSE | REGRESSION | Mean Squared Error | Domain-specific |
| RMSE | REGRESSION | Root Mean Squared Error | Domain-specific |
| MAE | REGRESSION | Mean Absolute Error | Domain-specific |
| R-squared | REGRESSION | Coefficient of determination | >0.80 for good fit |
| MAPE | REGRESSION | Mean Absolute Percentage Error | <10% for forecasting |
| Silhouette Score | CLUSTERING | Cohesion vs separation | >0.5 for good clusters |
| NDCG | RANKING | Normalized Discounted Cumulative Gain | >0.7 for recommendations |
| MRR | RANKING | Mean Reciprocal Rank | >0.5 for search |
| BLEU | GENERATIVE | Bilingual Evaluation Understudy | >0.4 for translation |
| ROUGE | GENERATIVE | Recall-Oriented Understudy for Gisting Evaluation | >0.4 for summarization |
| Perplexity | GENERATIVE | Exponentiated average log-likelihood | <20 for LLMs |
| Latency P50 | OPERATIONAL | 50th percentile response time | <100ms for real-time |
| Latency P99 | OPERATIONAL | 99th percentile response time | <500ms for production |
| Throughput | OPERATIONAL | Requests per second | >1000 RPS for production |

---

## AI Regulations

**EU AI Act** (European Union)
- Effective: 2024-08-01 (phased)
- Requirements: Risk assessment, conformity, transparency, human oversight
- Penalties: Up to €35M or 7% global turnover

**GDPR (AI provisions)** (European Union)
- Effective: 2018-05-25
- Requirements: Data protection, automated decision-making rights
- Penalties: Up to €20M or 4% global turnover

**NYC Local Law 144** (New York City)
- Effective: 2023-07-05
- Requirements: Bias audits for automated employment decisions
- Penalties: $500-1500 per violation

**Colorado AI Act** (Colorado, USA)
- Effective: 2026-02-01
- Requirements: Impact assessments, consumer disclosures
- Penalties: Civil penalties

**NIST AI RMF** (USA (voluntary))
- Effective: 2023-01-26
- Requirements: Risk management framework, voluntary guidelines
- Penalties: N/A (voluntary)

**ISO/IEC 42001** (International)
- Effective: 2023-12-01
- Requirements: AI management system certification
- Penalties: N/A (certification)

**UK AI Safety Institute** (United Kingdom)
- Effective: 2023-11-01
- Requirements: Frontier AI safety evaluation
- Penalties: N/A (advisory)

**China AI Regulations** (China)
- Effective: 2023-08-15
- Requirements: Content moderation, algorithm registration
- Penalties: Fines, license revocation

---

## EU AI Act Risk Categories

**Prohibited AI** (Risk: UNACCEPTABLE)
- Examples: Social scoring, subliminal manipulation, real-time biometric in public
- Compliance: Banned entirely
- Penalties: €35M or 7% turnover

**High-Risk AI** (Risk: HIGH)
- Examples: Critical infrastructure, employment, education, law enforcement
- Compliance: Conformity assessment, human oversight, documentation
- Penalties: €15M or 3% turnover

**Limited Risk AI** (Risk: LIMITED)
- Examples: Chatbots, deepfakes, emotion recognition
- Compliance: Transparency obligations
- Penalties: €7.5M or 1.5% turnover

**Minimal Risk AI** (Risk: MINIMAL)
- Examples: Spam filters, AI games, recommendations
- Compliance: No specific requirements
- Penalties: N/A

---

## LLMOps Tools (2024-2025)

| Tool | Vendor | Prompt | Fine-tune | RAG | Guards | Best For |
|------|--------|--------|-----------|-----|--------|---------|
| LangChain | LangChain | Y | N | Y | Y | LLM application development |
| LlamaIndex | LlamaIndex | Y | N | Y | N | RAG, data indexing |
| LangSmith | LangChain | Y | N | Y | Y | LLM observability, debugging |
| Weights & Biases Prompts | W&B | Y | Y | N | N | Prompt versioning and tracking |
| Guardrails AI | Guardrails | N | N | N | Y | LLM output validation |
| NeMo Guardrails | NVIDIA | N | N | N | Y | Conversational AI safety |
| Helicone | Helicone | Y | N | N | N | LLM API monitoring |
| Portkey | Portkey | Y | N | Y | Y | LLM gateway, observability |
| Promptflow | Microsoft | Y | Y | Y | N | LLM workflow development |
| Semantic Kernel | Microsoft | Y | N | Y | N | AI orchestration, plugins |

---

## ML Maturity Levels

**Level 0: No ML** - No ML capabilities
- Capabilities: Manual analytics only
- Team: N/A

**Level 1: Ad-hoc ML** - Experimental ML, notebooks
- Capabilities: Basic model training, manual deployment
- Team: 1-2 data scientists

**Level 2: Repeatable ML** - Standardized training, basic MLOps
- Capabilities: Version control, experiment tracking, manual pipelines
- Team: 3-5 ML engineers

**Level 3: Reliable ML** - Automated ML pipelines, monitoring
- Capabilities: CI/CD for ML, automated testing, drift detection
- Team: 5-10 ML engineers

**Level 4: Scalable ML** - Full MLOps maturity
- Capabilities: Auto-retraining, A/B testing, feature stores, full observability
- Team: 10+ ML engineers

---

## Usage Notes

### Framework Selection
- **Research**: PyTorch (55% share, dominant in academia)
- **Production**: TensorFlow (38% share, better production tooling)
- **HPC**: JAX (Google research, TPU optimized)
- **Rapid Dev**: Keras 3 (multi-backend)

### MLOps Platform Selection
- **Starting**: MLflow (open-source, flexible)
- **Research**: Weights & Biases (best tracking)
- **Kubernetes**: Kubeflow (K8s-native)
- **Cloud**: SageMaker/Vertex AI/Azure ML

### EU AI Act Timeline
- Feb 2025: Prohibited AI banned, AI literacy required
- Aug 2025: GPAI model rules apply
- Aug 2026: Most obligations in force
- Aug 2027: High-risk in regulated products

---
*Generated: 2025-01-31 | ML/AI Doc Matrix v1.0*
