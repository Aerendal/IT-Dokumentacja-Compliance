---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# ML/AI Documentation Matrix - Research Notes
## 2024-2025 Industry Research Summary

### Date: 2025-01-31

---

## 1. Deep Learning Frameworks Market (2024-2025)

### PyTorch Dominance
- **Market Share:** ~55% (2025), up from 50% in 2023
- **Research Papers:** 85%+ of new DL papers use PyTorch
- **Key Features:** Dynamic computation graphs, Pythonic API, torch.compile()
- **Performance:** 20-25% speedup with torch.compile() vs vanilla
- **Production:** TorchScript, TorchServe closing gap with TensorFlow

### TensorFlow Position
- **Market Share:** ~38% (2025), stable enterprise presence
- **Strengths:** TFLite for mobile, TF Serving for production, TPU support
- **TF 2.x:** Improved usability with eager execution
- **Enterprise:** Still preferred for production deployments at scale

### Emerging: JAX
- **Adoption:** ~5% and growing, especially in research
- **Backed by:** Google DeepMind
- **Key Features:** JIT compilation, automatic differentiation, XLA
- **Use Cases:** High-performance computing, TPU optimization

### Keras 3 Revolution
- **Multi-Backend:** Now supports TensorFlow, PyTorch, and JAX
- **Impact:** "Switzerland" approach may unify frameworks
- **Released:** Late 2023, gaining traction 2024-2025

---

## 2. MLOps Market Growth

### Market Size
- **2024:** $1.58-3.0 billion
- **2032 Projection:** $19.55-89.18 billion
- **CAGR:** 37-40%

### Platform Landscape

**Open Source Leaders:**
- MLflow: Most widely adopted, modular, Databricks backing
- Kubeflow: K8s-native, CNCF project, enterprise scalable
- DVC: Git-based versioning, lightweight

**Commercial Leaders:**
- Weights & Biases: Best experiment tracking, 30+ foundation model builders
- Neptune.ai: Metadata focus, collaboration features
- Comet ML: Strong visualization

**Cloud Native:**
- AWS SageMaker: Full managed, MLflow integration (2025)
- Google Vertex AI: AutoML, Gemini integration
- Azure ML: Enterprise MLOps, responsible AI focus

### Cost Considerations
- MLflow (self-hosted): $500-2,000/month small team
- W&B: Per-user subscription, enterprise pricing
- Kubeflow: $5,000-15,000/month infrastructure
- Cloud platforms: Pay-as-you-go, can be expensive at scale

---

## 3. Model Serving Evolution

### High-Performance Inference
**NVIDIA Triton:**
- Best GPU utilization
- Dynamic batching
- Multi-framework support
- Production standard for GPU workloads

**vLLM (2024-2025):**
- PagedAttention for LLMs
- 24x throughput improvement
- Becoming standard for LLM inference

### Kubernetes-Native
**KServe:**
- Serverless inference
- Scale-to-zero
- Multi-framework
- CNCF project

**Seldon Core:**
- Advanced deployment strategies
- A/B testing, canary
- Note: BSL license change in 2024

### Developer-Friendly
**BentoML:**
- Python-first
- Any framework
- OpenLLM for LLM serving
- BentoCloud managed option

---

## 4. Feature Stores

### Market Leaders

**Feast (Open Source):**
- Linux Foundation project
- Flexible backends
- Multi-cloud support
- Best for vendor independence

**Tecton (Enterprise):**
- By Uber Michelangelo creators
- Best real-time capabilities
- $5k-15k/month enterprise
- GitOps workflow

**Hopsworks:**
- Strong governance
- Regulated industries
- Data lineage focus

### Cloud Native
- Vertex AI Feature Store (GCP)
- SageMaker Feature Store (AWS)
- Databricks Feature Store

---

## 5. Model Monitoring & Drift Detection

### Open Source Options

**Evidently AI:**
- 25M+ downloads
- Best open-source option
- Data and model drift
- Interactive reports
- 24.8% market mindshare

**NannyML:**
- Performance estimation without labels
- Unique capability
- Tabular data focus

**Deepchecks:**
- ML validation
- Testing focus

### Commercial Platforms

**Arize AI:**
- Enterprise ML observability
- Embedding drift detection
- Root cause analysis
- 22% market mindshare

**WhyLabs:**
- Privacy-preserving
- SOC 2 / HIPAA compliant
- Open-sourced Jan 2025
- Best for regulated industries

**Fiddler AI:**
- Explainability focus
- Compliance features
- Regulated industries

---

## 6. EU AI Act Implementation

### Timeline
- **Aug 1, 2024:** Entered into force
- **Feb 2, 2025:** Prohibited AI banned, AI literacy required
- **Aug 2, 2025:** GPAI model rules apply
- **Aug 2, 2026:** Most obligations in force
- **Aug 2, 2027:** High-risk in regulated products

### Risk Categories
1. **Unacceptable:** Banned (social scoring, manipulation)
2. **High-Risk:** Conformity assessment required
3. **Limited:** Transparency obligations
4. **Minimal:** No requirements

### Key Requirements for High-Risk
- Risk management system
- Data governance
- Technical documentation
- Record-keeping
- Human oversight
- Accuracy, robustness, cybersecurity

### Penalties
- Prohibited AI: €35M or 7% turnover
- High-Risk violations: €15M or 3% turnover
- Other violations: €7.5M or 1.5% turnover

---

## 7. LLMOps Emergence (2024-2025)

### "Year of the AI Agent"
- 99% of AI developers exploring agents
- RAG default pattern for production
- Evaluation infrastructure critical

### Key Tools

**Orchestration:**
- LangChain: Dominant framework
- LlamaIndex: RAG specialist
- Semantic Kernel: Microsoft entry

**Observability:**
- LangSmith: LangChain's observability
- Helicone: API monitoring
- Portkey: LLM gateway

**Safety/Guardrails:**
- Guardrails AI: Output validation
- NeMo Guardrails: NVIDIA, conversational safety

### Unique Challenges
- Prompt versioning
- Hallucination detection
- Context management
- Token cost tracking
- Latency optimization

---

## 8. ML Maturity Trends

### Industry Observations
- Most companies at Level 1-2 (ad-hoc to repeatable)
- Only ~15% at Level 3+ (reliable/scalable)
- Feature stores adoption growing
- MLOps tooling maturing

### Maturity Drivers
- Regulatory pressure (EU AI Act)
- Model governance requirements
- Cost optimization needs
- Production reliability demands

---

## 9. Responsible AI

### Key Focus Areas
- Bias detection and mitigation
- Model explainability
- Fairness testing
- Audit trails
- Human oversight

### Tools
- Fairlearn (Microsoft)
- AI Fairness 360 (IBM)
- SHAP/LIME for explainability
- What-If Tool (Google)

---

## Sources

1. MLOps market reports (2024-2025)
2. Framework popularity surveys
3. EU AI Act official documentation
4. Vendor documentation and blogs
5. Academic papers on framework comparison
6. Industry analyst reports
7. GitHub stars and community metrics

---

*Research compiled: 2025-01-31*
