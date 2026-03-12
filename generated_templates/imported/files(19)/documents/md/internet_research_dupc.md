---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Internet Research — IT Documentation Matrix Part 5
## Specjalizacje Techniczne (Industries 37-45)
*Research conducted: 2026-02-01*

---

## 37. FinTech / RegTech Engineering

**Key Standards & Frameworks:**
- **PCI-DSS v4.0** — Payment Card Industry Data Security Standard; mandatory for any entity processing card payments. Requires 12 control domains covering network security, access control, monitoring.
- **PSD2 / Open Banking** — EU Payment Services Directive requiring Strong Customer Authentication (SCA) and open API access. Key doc: EBA Guidelines.
- **AML/KYC** — Anti-Money Laundering / Know Your Customer. FATF recommendations define the global framework. Automated screening and transaction monitoring required.
- **Basel III / IV** — Capital adequacy requirements for financial institutions. Key for risk-weighted asset calculations.
- **SOX (Sarbanes-Oxley)** — Financial reporting controls. Section 404 requires management assessment of internal controls.
- **GDPR** — EU General Data Protection Regulation. Critical for FinTech handling personal financial data.
- **ISO 27001** — Information Security Management System. Industry standard for FinTech security certification.
- **NIST CSF 2.0** — Cybersecurity Framework. Provides structured risk management approach.

**Architecture Patterns:**
- Event-driven transaction processing with exactly-once semantics
- HSM (Hardware Security Module) integration for key management
- Immutable audit trails using append-only logs (e.g., blockchain or event sourcing)
- Microservices with API gateway for regulatory isolation
- Real-time fraud detection pipelines

**Key Tools/Platforms:** Kafka for transaction streaming, Vault for secrets management, Istio for service mesh, PostgreSQL for transactional data.

---

## 38. Real-Time Systems / Stream Processing

**Key Standards & Frameworks:**
- **IEEE 1024** — Standard for real-time systems documentation
- **ITIL 4** — Service Management framework for operational excellence
- **ISO 25010** — Software quality model including performance characteristics
- **Cloud Native CNCF** — Cloud Native Computing Foundation standards for containerized real-time systems

**Architecture Patterns:**
- Lambda Architecture (batch + speed layers) vs Kappa Architecture (single streaming layer)
- RTOS (Real-Time Operating Systems) for hard real-time: FreeRTOS, Green Hills Integrity
- Soft real-time patterns: Kafka Streams, Flink, Storm
- Backpressure management and flow control
- Windowing strategies: tumbling, sliding, session windows

**Performance Benchmarks:**
- Hard real-time: < 1ms latency guarantees
- Soft real-time: < 100ms for user-facing, < 10ms for internal processing
- Throughput targets: 100K+ events/sec for high-volume systems

**Key Tools:** Apache Kafka, Apache Flink, Apache Storm, Spark Streaming, Kinesis Data Streams.

---

## 39. AR/VR/Metaverse Development

**Key Standards & Frameworks:**
- **IEEE 1840** — Standard for Augmented Reality specification
- **Meta Quest Store Requirements** — Content guidelines, privacy, age rating
- **Apple Vision Pro Guidelines** — visionOS development standards, spatial computing
- **WCAG 2.1** — Accessibility standards adapted for XR (emerging guidelines)
- **ISO 9241** — Ergonomics and human-system interaction

**Architecture Patterns:**
- Client-server for multiplayer; client-side prediction for responsiveness
- LOD (Level of Detail) systems for performance optimization
- Spatial audio and haptic feedback architecture
- Avatar and identity management in metaverse contexts
- Hand/eye tracking integration patterns

**Performance Targets:**
- VR: 90 FPS minimum (Meta Quest 3), 120 FPS preferred
- Motion-to-photon latency: < 20ms to prevent motion sickness
- Frame time budget: 11.1ms (90 FPS) or 8.3ms (120 FPS)

**Key Tools/Engines:** Unity, Unreal Engine 5, Three.js (web VR), A-Frame, Godot.
**Platforms:** Meta Quest 2/3, Apple Vision Pro, PlayStation VR2, Steam VR, Pico.

---

## 40. Conversational AI / Voice Engineering

**Key Standards & Frameworks:**
- **W3C Voice XML 2.1** — Standard for voice application markup
- **IETF Speech Standards** — Speech recognition and synthesis protocols
- **EU AI Act** — Classification of AI systems by risk; conversational AI with emotional recognition classified as high-risk
- **NIST AI RMF** — AI Risk Management Framework
- **ISO 42001** — AI Management System standard

**Architecture Patterns:**
- Pipeline: ASR → NLU → Dialog Manager → NLG → TTS
- Intent-entity framework for structured understanding
- Rasa Open Source / Dialogflow / Amazon Lex for dialog management
- Retrieval-Augmented Generation (RAG) for knowledge-grounded dialogs
- Multi-turn context management with session state

**Evaluation Metrics:**
- Intent Recognition Accuracy: > 95% target
- Entity Extraction F1: > 90%
- Task Completion Rate: > 80%
- Word Error Rate (ASR): < 10%
- CSAT (Customer Satisfaction): > 4.0/5.0

**Key Tools:** Rasa, Dialogflow, Amazon Lex, Azure Language Understanding, Whisper (ASR), ElevenLabs (TTS).

---

## 41. Computer Vision Engineering

### EU AI Act — High-Risk Classification for CV Systems
*Source: EU Regulation 2024/1689, entered into force 1 August 2024*

The EU AI Act classifies computer vision systems into risk tiers with binding documentation obligations:

**Prohibited AI (effective 2 February 2025):**
- Real-time biometric identification in public spaces (law enforcement exceptions require judicial approval)
- Social scoring systems using CV
- Subliminal/manipulative visual AI techniques

**High-Risk CV Systems (Annex III — rules effective August 2026):**
- Facial recognition for identity verification/authentication
- Remote biometric identification systems
- CV used in critical infrastructure monitoring
- CV for law enforcement, migration, asylum, border control
- CV components in medical devices (Annex I products)
- CV for safety assessment in automotive/aviation

**Documentation Requirements for High-Risk CV Providers (Article 16):**
1. Risk Management System (Art. 9) — Continuous lifecycle; identify/analyze/evaluate risks; measures to reduce to acceptable level
2. Technical Documentation — All info for authorities to assess compliance; demonstrate conformity
3. Data Governance (Art. 10) — Training/validation/test datasets must be relevant, representative, error-free; documented procedures
4. Record-Keeping — Auto-log events relevant for risk identification and modifications throughout lifecycle
5. Human Oversight (Art. 14) — Allow deployers to implement human oversight; humans must interpret outputs correctly
6. Accuracy & Robustness (Art. 15) — Documented performance metrics; robustness against adversarial conditions
7. EU Declaration of Conformity + CE marking before market placement
8. Registration in EU AI database (mandatory for law enforcement, migration, border control)

**Penalties:** Up to 7% of worldwide annual turnover for non-compliance.

**Phased Timeline:**
- Feb 2025: Prohibited practices enforcement
- Aug 2025: GPAI model obligations
- Aug 2026: High-risk AI system rules (most CV systems)
- Aug 2027: High-risk AI embedded in regulated products

### NIST AI RMF & Bias Testing (NIST SP 1270, FRVT/FRTE Program)

**NIST SP 1270 — Three Categories of AI Bias:**
1. Computational & Statistical Bias — Systematic errors from data/algorithms; differential performance across demographic groups
2. Human Bias — Cognitive biases in design, data collection, labeling; confirmation bias in evaluation
3. Systemic Bias — Institutional/societal patterns reproduced by AI; historical discrimination encoded in training data

**NIST Face Recognition Technology Evaluation (FRTE — renamed from FRVT in 2023):**
- Evaluates 158+ developers, 527+ algorithms (2024 report)
- Testing datasets: FBI mugshots, visa applications, DHS border crossings — 18M+ images, 8M+ subjects
- Key Metrics:
  - FNMR (False Non-Match Rate): Probability system fails to match two images of same person
  - FMR (False Match Rate): Probability system incorrectly matches different individuals
  - FNIR (False Negative Identification Rate): Incorrect rejection of legitimate user
  - FPIR (False Positive Identification Rate): Incorrect acceptance of impostor
  - APCER (Attack Presentation Classification Error Rate): Failure to detect presentation attacks
  - BPCER (Bona Fide Classification Error Rate): False alarms on genuine subjects
- Demographic Fairness Metrics: Inequity Ratios across race/gender; Fairness Discrepancy Rate (FDR); Comprehensive Equity Index (CEI)
- 2019 FRVT finding: Many algorithms 10-100x more likely to misidentify Black or East Asian faces vs white faces

**ISO/IEC 19795-10** — Standard for quantifying biometric system performance across demographic groups (published 2023)

### CV Architecture Patterns (2024-2025)

**Detection Paradigm Evolution:**

*Two-Stage Detectors (accuracy-focused):*
- R-CNN → Fast R-CNN → Faster R-CNN → Mask R-CNN progression
- Faster R-CNN: Region Proposal Network (RPN); shared convolutional features; end-to-end trainable
- Mask R-CNN: Pixel-wise segmentation mask branch; standard for instance segmentation
- Inference: ~333ms/frame baseline

*One-Stage Detectors (speed-focused):*
- YOLO family: single forward pass detection
- YOLOv7: 3.5ms/frame; feature aggregation improvements
- YOLOv9 (2024): Feedback initialization, attention-based modules; enhanced small/distant object detection
- YOLOv10 (2024): Dynamic task prioritization, transformer-based feature extraction; improved occlusion handling
- YOLOv11 (2024): Cross-domain learning, refined loss functions
- SSD: Multi-scale feature maps for different object sizes

*Transformer-Based Detectors (2020+):*
- DETR: End-to-end detection; no region proposals; set prediction via global attention; eliminates NMS
- Vision Transformers (ViTs): Images as patch sequences; self-attention; outperform CNNs on benchmarks
- Hybrid (ConvNeXt): CNN spatial strengths + transformer attention

**Edge AI / On-Device Deployment:**
- Lightweight architectures: MobileNets, EfficientNets, YOLOv5-nano
- Optimization: TensorRT, ONNX Runtime, TFLite, quantization (INT8/INT4)
- ONNX: Standardizes model export across platforms
- NAS/AutoML: Automated compact architecture design for edge

**Performance Benchmarks (COCO):**
- mAP (mean Average Precision) at IoU 0.5-0.95 = primary metric
- mAP > 50 on COCO = competitive baseline
- YOLOv7: 3.5ms/frame; Mask R-CNN: 333ms/frame
- Edge target: < 100ms inference

**Key Tools:** PyTorch, TensorFlow, YOLO (Ultralytics), OpenCV, CVAT (annotation), TensorRT, Triton (serving), Hugging Face Transformers.

---

## 42. Natural Language Processing (NLP)

### Benchmarking Standards: GLUE & SuperGLUE

**GLUE (General Language Understanding Evaluation):**
- Introduced 2018 as standardized multi-task benchmark for NLU systems
- Model-agnostic; incentivizes knowledge sharing across tasks
- 9 tasks across 3 categories:
  - Single-Sentence: CoLA (linguistic acceptability, Matthews correlation); SST-2 (sentiment analysis, accuracy)
  - Similarity/Paraphrase: MRPC (Microsoft Research Paraphrase Corpus); STS-B (semantic textual similarity, regression); QQP (Quora question pairs)
  - Inference: MNLI (multi-genre natural language inference); QNLI (question NLI); RTE (recognizing textual entailment); WNLI (Winograd schema)
- Scoring: Per-task scores + macro-average; privately-held test data prevents overfitting
- Human baseline: 87.1; Models surpassed human performance ~1 year after release
- Evaluation via gluebenchmark.com submission system

**SuperGLUE:**
- Created when models saturated GLUE (exceeded human baseline)
- 8 more challenging tasks; diverse formats (coreference resolution, QA added beyond sentence classification)
- Retains hardest GLUE tasks (RTE, Winograd Schema Challenge)
- Human baseline: 89.8; Best model (Vega v2): 91.3 — humans beaten on most tasks
- Tasks include: BoolQ, CB (CommitmentBank), COPA, MultiRC, ReCoRD, RTE, WiC, WSC
- Includes AXb (broad-coverage diagnostic) and AXg (Winogender gender bias diagnostic)

**Beyond GLUE/SuperGLUE (2024):**
- BIG-bench: 200+ tasks requiring creative/logical thinking; math, coding, real-world scenarios
- SQuAD: Reading comprehension benchmark; Exact Match metric
- LLM-specific benchmarks emerging for reasoning, factuality, hallucination detection

### Transformer Architecture & NLP Pipeline (2024-2025)

**Core Architecture (Vaswani et al., 2017 — "Attention Is All You Need"):**
- Self-attention mechanism models associations across entire input sequence
- Parallelizable (vs sequential RNNs); captures long-range dependencies
- Preprocessing pipeline: Tokenizer → Embedding layer → Positional encoding → Encoder/Decoder blocks

**Key Model Families:**

*BERT (Bidirectional Encoder Representations from Transformers, Google 2018):*
- Encoder-only architecture; bidirectional understanding via Masked Language Model (MLM)
- Pre-training: MLM (predict masked tokens) + Next Sentence Prediction (NSP)
- Fine-tuning: Add classification head for downstream tasks (NER, sentiment, QA)
- BERT-base: 12 layers, 12 attention heads, 110M parameters, hidden size 768
- BERT-large: 24 layers, 16 attention heads, 340M parameters, hidden size 1024
- Variants: RoBERTa, ALBERT, DistilBERT (60% faster, 95% performance), DeBERTa

*GPT Family (OpenAI):*
- Decoder-only; autoregressive (left-to-right); generative text production
- Pre-training on large unlabeled corpora; fine-tuning or few-shot prompting
- GPT-4o (2024): Multimodal (text+image+audio); low latency
- Ideal for: Text generation, creative writing, summarization, reasoning

*T5 (Text-to-Text Transfer Transformer, Google):*
- Encoder-decoder; frames all NLP tasks as text-to-text problems
- Unified framework enables easy adaptation across tasks
- Explored 100+ design choices to find optimal configuration

*LLaMA / Open-Source Models (2024):*
- Meta's LLaMA 3.2; Mistral 7B; open-weight models for fine-tuning
- Parameter-efficient fine-tuning: LoRA (Low-Rank Adaptation), adapters
- Practical for domain-specific deployment with limited compute

**Modern NLP Pipeline Architecture:**
```
Raw Text → Preprocessing → Tokenization → Embedding → Model Inference → Post-processing → Output

Preprocessing: language detection, cleaning, normalization
Tokenization: WordPiece (BERT), BPE (GPT), SentencePiece
Embedding: Token + Position + Segment embeddings → contextual via transformer layers
Model: Pre-trained LLM (fine-tuned or prompted)
Post-processing: Decoding strategy (greedy, beam search, nucleus sampling)
```

**Transfer Learning Paradigm (dominant since 2018):**
1. Pre-train on massive unlabeled corpus (general language understanding)
2. Fine-tune on task-specific labeled data (small dataset sufficient)
- Dramatically reduced training time/compute vs training from scratch
- Foundation model + domain-specific fine-tuning = production standard

### Responsible AI Documentation: Model Cards & Datasheets

**Model Cards (Mitchell et al., 2019):**
- "Nutrition labels" for ML models; document performance across use cases, data distributions, social contexts
- Standard sections: Model summary, architecture, training procedures, parameters, evaluation results, intended uses, limitations, biases, ethical considerations
- Adopted by: Meta (with fairness dashboards), Hugging Face (mandatory on Hub), OpenAI (internal review), Stanford CRFM (HELM benchmark)
- NAACL 2024: CardBench aggregated 4.8k model cards + 1.4k data cards; automated generation via LLMs (CardGen pipeline)

**Datasheets for Datasets (Gebru et al., 2018/2021):**
- Guided questions covering dataset lifecycle stages: motivation, composition, collection, processing, intended uses, social impact
- Workflow for both creators (guide thinking) and consumers (assess suitability)
- Analogies from automotive industry, clinical trials, electronics

**Data Cards (Pushkarna et al., 2022, Google):**
- Emphasize information that shapes data but cannot be inferred from dataset directly
- Row-and-column structure; increasing detail left-to-right
- Complement Model Cards, Data Statements, FactSheets

**Data Statements for NLP (Bender & Friedman, 2018):**
- NLP-specific dataset documentation framework
- Documents language characteristics, annotator demographics, collection context
- Aims to mitigate system bias and enable better science

**CLeAR Framework (2024):**
- Comparable, Legible, Actionable, Robust documentation principles
- Addresses tradeoffs: comparability vs customization; legibility vs technical depth; actionability vs comprehensiveness
- Guides practitioners and policymakers on AI transparency documentation

**OpenDatasheets (2023):**
- Machine-readable evolution of Datasheets for Datasets
- JSON/YAML format; integrates with open platforms
- Supports GDPR compliance documentation; schema.org/Dataset metadata for discoverability

**AI Cards (APF 2024):**
- Framework for EU AI Act compliance; machine-readable risk documentation
- Bridges community documentation (Model Cards, Datasheets) with regulatory requirements
- System architecture documentation including component provenance

### EU AI Act Overlap with NLP
- NLP systems for **emotion recognition** and **biometric identification** = high-risk (Annex III)
- All GPAI model providers must: provide technical documentation, instructions for use, comply with Copyright Directive, publish training data summary
- GPAI models with **systemic risk**: model evaluations, adversarial testing, incident tracking, cybersecurity protections required

**Key Tools:** Hugging Face Transformers, spaCy, NLTK, vLLM (serving), Sentence-Transformers, LangChain, PyTorch.

---

## 43. Streaming / Real-Time Data Processing

**Key Standards & Frameworks:**
- **Apache Kafka** — De-facto standard for event streaming; Confluent documentation
- **Cloud Native CNCF** — Observability standards (OpenTelemetry) for streaming
- **EIP (Enterprise Integration Patterns)** — Channel, Router, Filter patterns for event processing
- **ITIL 4** — Operational management of streaming infrastructure

**Architecture Patterns:**
- Kappa Architecture (preferred for modern streaming)
- Exactly-once semantics: idempotent producers + transactional consumers
- Schema Registry for Avro/Protobuf schema evolution
- Consumer Group balancing and rebalancing strategies
- State stores: RocksDB (Flink/Kafka Streams), Redis for fast lookups
- Outbox pattern for transactional event publishing

**Performance Benchmarks:**
- Throughput: 1M+ messages/sec per cluster (Kafka)
- Latency: < 5ms end-to-end for low-latency use cases
- Consumer lag: < 1 second target for critical systems

**Key Tools:** Apache Kafka, Apache Flink, Confluent Platform, Apache Pulsar, AWS Kinesis, Debezium (CDC).

---

## 44. Search Engineering

**Key Standards & Frameworks:**
- **Elasticsearch documentation** — Industry reference for inverted index search
- **W3C Search** — Web search standards and semantic markup
- **NIST CSF 2.0** — Security framework for search infrastructure
- **OWASP** — Web application security for search endpoints

**Architecture Patterns:**
- Inverted Index + BM25 baseline ranking
- Hybrid search: BM25 + Dense Vector (embedding-based) retrieval
- Learning-to-Rank (LTR): pairwise/listwise models for relevance
- Faceted search with aggregation buckets
- Autocomplete: prefix trie + n-gram index
- Search-as-a-Service with multi-tenancy

**Evaluation Metrics:**
- NDCG@10: > 0.7 for good relevance
- Click-Through Rate: baseline 2-5%, target > 5%
- Zero-Result Rate: < 5% target
- P95 Query Latency: < 50ms

**Key Tools:** Elasticsearch, Solr, Algolia, Meilisearch, Weaviate (vector search), Sentence-Transformers (embeddings).

---

## 45. Geographic Information Systems (GIS)

**Key Standards & Frameworks:**
- **OGC (Open Geospatial Consortium)** — WMS, WFS, WCS, WMTS standards for spatial data services
- **ISO 19115** — Geographic information metadata standard
- **ISO 19139** — Geographic metadata XML schema
- **EPSG Registry** — Coordinate Reference Systems registry (critical for spatial accuracy)
- **GDPR** — Location data as personal data; special handling required

**Architecture Patterns:**
- PostGIS for spatial database operations (ST_* functions)
- Vector tiles (Mapbox Vector Tiles) vs Raster tiles (PNG/WebP)
- Spatial indexing: R-tree, GiST (PostgreSQL), QuadTree
- Geocoding: forward (address→coordinates) and reverse (coordinates→address)
- Routing: Dijkstra's algorithm, A*, Contraction Hierarchies (OSRM)
- Map rendering: Mapbox GL JS, Leaflet, OpenLayers, Deck.gl

**Performance Targets:**
- Map tile load: < 200ms for initial view
- Spatial query: < 100ms for point-in-polygon with < 1M features
- Geocoding: < 50ms per request

**Key Tools:** PostGIS, QGIS, ArcGIS, Mapbox, OpenStreetMap, OSRM (routing), Turf.js (client-side spatial), Kepler.gl (visualization).

---

## Cross-Industry Patterns (Part 5)

### AI/ML Systems (Industries 40-42)
All three Conversational AI, Computer Vision, and NLP share:
- MLOps lifecycle: data → model → serving → monitoring → retraining
- Model drift detection as operational requirement
- EU AI Act compliance (risk classification)
- Bias and fairness evaluation pipelines
- Model versioning and A/B testing frameworks

### Streaming & Real-Time (Industries 38, 43)
- Industry 38 focuses on embedded/hard real-time; Industry 43 on data streaming
- Shared patterns: exactly-once semantics, backpressure, consumer lag monitoring
- Event-driven architecture is the unifying pattern

### Spatial + Streaming (GIS + Streaming)
- Real-time GIS: streaming spatial events (vehicle tracking, IoT sensors)
- Geofencing as streaming filter operation

---
*Research sources: Official documentation, OWASP, NIST, EU AI Act text, ISO standards summaries, industry whitepapers*
