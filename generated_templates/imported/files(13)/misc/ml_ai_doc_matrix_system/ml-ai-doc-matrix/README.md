---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# ML/AI Documentation Matrix System
## Industry #6: Machine Learning / Artificial Intelligence

### Overview
A comprehensive documentation framework for Machine Learning and AI projects, covering the complete ML lifecycle from problem definition through deployment, monitoring, compliance, and governance.

**Version:** 1.0  
**Created:** 2025-01-31  
**Database:** SQLite 3  

---

## Statistics

| Metric | Count |
|--------|-------|
| **Total Documents** | 124 |
| **Lifecycle Phases** | 23 |
| **Document Types** | 22 |
| **DL Frameworks** | 15 |
| **MLOps Platforms** | 15 |
| **Model Serving Tools** | 12 |
| **Feature Stores** | 10 |
| **Monitoring Tools** | 12 |
| **Model Types** | 15 |
| **ML Metrics** | 20 |
| **AI Regulations** | 8 |
| **Cloud ML Platforms** | 8 |
| **Explainability Tools** | 10 |
| **LLMOps Tools** | 10 |
| **NN Architectures** | 12 |
| **Hyperparameter Methods** | 8 |

---

## Directory Structure

```
ml-ai-doc-matrix/
├── README.md                 # This file
├── db/
│   ├── schema.sql           # Database schema (22 tables)
│   ├── data_part1.sql       # Phases, document types, documents
│   ├── data_part2.sql       # Specialized tables (frameworks, tools)
│   ├── data_part3.sql       # Mappings and relationships
│   └── ml_ai_docs.db        # SQLite database
├── exports/
│   └── ml_ai_matrix.json    # Complete JSON export
├── reference/
│   └── CONTEXT.md           # Comprehensive reference guide
└── research/
    └── research_notes.md    # 2024-2025 research notes
```

---

## Documents by Priority

| Priority | Count | Description |
|----------|-------|-------------|
| CRITICAL | 23 | Must-have documents for any ML project |
| HIGH | 58 | Important for production ML systems |
| MEDIUM | 40 | Recommended for mature ML operations |
| LOW | 3 | Nice-to-have for comprehensive coverage |

---

## Technology Coverage

### Deep Learning Frameworks (15)
- **Low-Level:** PyTorch (55%), TensorFlow (38%), JAX, MXNet, ONNX Runtime
- **High-Level:** Keras, Hugging Face Transformers, FastAI, scikit-learn
- **Gradient Boosting:** XGBoost, LightGBM, CatBoost
- **Wrappers:** PyTorch Lightning, Detectron2

### MLOps Platforms (15)
- **Open Source:** MLflow, Kubeflow, DVC, Metaflow, ZenML, ClearML, Flyte
- **Commercial:** Weights & Biases, Neptune.ai, Comet ML, H2O.ai
- **Cloud Native:** AWS SageMaker, Google Vertex AI, Azure ML, Databricks

### Model Serving (12)
- **Framework-Specific:** TorchServe, TensorFlow Serving
- **Multi-Framework:** NVIDIA Triton, BentoML, KServe, Seldon Core, Ray Serve
- **LLM-Specific:** vLLM, TGI (Text Generation Inference), OpenLLM

### Feature Stores (10)
- **Open Source:** Feast, Hopsworks, Feathr, FeatureForm
- **Managed:** Tecton, Iguazio
- **Cloud Native:** Vertex AI Feature Store, SageMaker Feature Store, Databricks

### Model Monitoring (12)
- **Open Source:** Evidently AI, NannyML, Deepchecks, Alibi Detect
- **Commercial:** WhyLabs, Arize AI, Fiddler AI, Superwise, Aporia
- **Cloud Native:** SageMaker Monitor, Vertex AI Monitor, Azure ML Monitor

### LLMOps Tools (10) - New for 2024-2025
- **Orchestration:** LangChain, LlamaIndex, Semantic Kernel
- **Observability:** LangSmith, Helicone, Portkey
- **Safety:** Guardrails AI, NeMo Guardrails
- **Development:** Promptflow, W&B Prompts

---

## AI Regulations Covered

| Regulation | Jurisdiction | Status |
|------------|--------------|--------|
| EU AI Act | European Union | In force (phased 2024-2027) |
| GDPR (AI) | European Union | In force |
| NYC Local Law 144 | New York City | In force |
| Colorado AI Act | Colorado, USA | Effective Feb 2026 |
| NIST AI RMF | USA | Voluntary framework |
| ISO/IEC 42001 | International | Certification standard |
| UK AI Safety | United Kingdom | Advisory |
| China AI Regulations | China | In force |

---

## EU AI Act Risk Classification

```
┌─────────────────────────────────────────────────────────────┐
│                    EU AI Act Risk Levels                     │
├─────────────────────────────────────────────────────────────┤
│ UNACCEPTABLE │ Banned: social scoring, manipulation,        │
│              │ real-time biometric in public spaces         │
│              │ Penalty: €35M or 7% turnover                 │
├──────────────┼──────────────────────────────────────────────┤
│ HIGH RISK    │ Critical infrastructure, employment,         │
│              │ education, law enforcement, healthcare       │
│              │ Requirements: conformity, oversight, docs    │
│              │ Penalty: €15M or 3% turnover                 │
├──────────────┼──────────────────────────────────────────────┤
│ LIMITED      │ Chatbots, deepfakes, emotion recognition     │
│              │ Requirements: transparency obligations       │
│              │ Penalty: €7.5M or 1.5% turnover              │
├──────────────┼──────────────────────────────────────────────┤
│ MINIMAL      │ Spam filters, AI games, recommendations      │
│              │ No specific requirements                     │
└─────────────────────────────────────────────────────────────┘
```

---

## ML Maturity Model

```
Level 4: SCALABLE ML      │ Full MLOps, auto-retraining, A/B testing
         (10+ engineers)  │ feature stores, full observability
                         │
Level 3: RELIABLE ML      │ CI/CD for ML, automated testing,
         (5-10 engineers) │ drift detection, monitoring
                         │
Level 2: REPEATABLE ML    │ Version control, experiment tracking,
         (3-5 engineers)  │ manual pipelines
                         │
Level 1: AD-HOC ML        │ Notebooks, manual deployment,
         (1-2 scientists) │ basic model training
                         │
Level 0: NO ML            │ Manual analytics only
```

---

## Framework Selection Decision Tree

```
Is this for research or production?
├── Research
│   ├── Need cutting-edge flexibility? → PyTorch
│   ├── Need TPU/HPC optimization? → JAX
│   └── Quick prototyping? → Keras + PyTorch backend
│
└── Production
    ├── Mobile/Edge deployment? → TensorFlow + TFLite
    ├── AWS infrastructure? → PyTorch + SageMaker
    ├── GCP infrastructure? → TensorFlow + Vertex AI
    └── Multi-cloud/vendor agnostic? → ONNX export
```

---

## Model Serving Selection

```
What's your primary requirement?
├── Maximum GPU performance? → NVIDIA Triton
├── PyTorch models only? → TorchServe
├── Kubernetes native? 
│   ├── Serverless scaling? → KServe
│   └── Advanced deployment? → Seldon Core
├── Quick deployment, any framework? → BentoML
└── LLM serving?
    ├── High throughput? → vLLM
    └── Hugging Face models? → TGI
```

---

## Critical Documents (23 CRITICAL priority)

### Phase 1-3: Foundation
- ML-PSD: ML Problem Statement
- ML-FEA: Feasibility Assessment
- ML-REQ: ML Requirements Specification
- ML-DRQ: Data Requirements for ML
- ML-ARC: ML Architecture Document
- ML-FEP: Feature Engineering Plan

### Phase 5-7: Development & Compliance
- ML-DPC: Data Preparation Code
- ML-MTC: Model Training Code
- ML-MTP: Model Testing Plan
- ML-FBT: Fairness and Bias Testing
- ML-EXP: Model Explainability Documentation
- ML-RCC: Regulatory Compliance Check
- ML-EUA: EU AI Act Compliance Assessment

### Phase 8-11: Deployment & Operations
- ML-MSA: Model Serving Architecture
- ML-PDG: Production Deployment Guide
- ML-MMG: Model Monitoring Guide
- ML-MDD: Model Drift Detection
- ML-MFR: Model Failure Recovery
- ML-RBP: Rollback Procedure
- ML-PMT: Model Performance Metrics

### Phase 12, 21: Documentation & DR
- ML-MDC: Model Documentation
- ML-DRP: Disaster Recovery Plan
- ML-BCP: Business Continuity Plan

---

## Related Systems

| # | Industry | Documents | Status |
|---|----------|-----------|--------|
| 1 | Backend/API Development | ~100 |  Complete |
| 2 | Frontend/Web Development | ~100 |  Complete |
| 3 | Mobile Development | ~100 |  Complete |
| 4 | Data Engineering | 171 |  Complete |
| 5 | Data Science/Analytics | 107 |  Complete |
| **6** | **ML/AI** | **124** | ** Complete** |

---

## Usage Examples

### Query Critical Documents
```sql
SELECT doc_code, doc_name, priority
FROM documents
WHERE priority = 'CRITICAL'
ORDER BY doc_code;
```

### Find MLOps Platforms with Full Features
```sql
SELECT platform_name, vendor, platform_type
FROM mlops_platforms
WHERE experiment_tracking = 1 
  AND model_registry = 1 
  AND pipeline_orchestration = 1;
```

### Get High-Risk AI Compliance Documents
```sql
SELECT d.doc_code, d.doc_name
FROM documents d
JOIN document_phases dp ON d.doc_id = dp.doc_id
WHERE dp.phase_id = 7  -- Security/Compliance phase
ORDER BY d.priority;
```

---

## License
Internal documentation framework - adapt as needed for your organization.

---

*ML/AI Documentation Matrix System v1.0*  
*Generated: 2025-01-31*
