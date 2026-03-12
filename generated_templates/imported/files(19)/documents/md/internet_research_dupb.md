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

**Key Standards & Frameworks:**
- **EU AI Act** — Computer vision for facial recognition classified as high-risk AI
- **NIST AI RMF** — Risk management for AI/ML systems
- **IEEE Ethics Guidelines for AI** — Transparency and accountability in CV systems
- **GDPR Article 22** — Rights related to automated decision-making (face recognition)
- **OWASP Machine Learning Security** — Top 10 ML security risks

**Architecture Patterns:**
- Two-stage detection: Region Proposal → Classification (R-CNN family)
- Single-stage detection: YOLO v8/v9, SSD, EfficientDet
- Segmentation: U-Net (medical), Mask R-CNN (instance), SAM (foundation model)
- Edge deployment: TensorRT, ONNX Runtime, TFLite optimization
- MLOps pipeline: data versioning → training → evaluation → deployment → monitoring

**Performance Benchmarks:**
- Object Detection mAP: > 50 (COCO benchmark)
- Inference latency: < 30ms on GPU, < 100ms on edge
- Model size: < 10MB for edge deployment

**Key Tools:** PyTorch, TensorFlow, YOLO (Ultralytics), OpenCV, CVAT (annotation), TensorRT (optimization), Triton (serving).

---

## 42. Natural Language Processing (NLP)

**Key Standards & Frameworks:**
- **EU AI Act** — NLP systems for emotion recognition and biometric identification classified as high-risk
- **ACL (Association for Computational Linguistics)** — Research standards and benchmarks
- **NIST AI RMF** — Risk management framework
- **IEEE Ethics Guidelines** — Fairness and bias mitigation in language models

**Architecture Patterns:**
- Transformer-based: BERT, RoBERTa, T5, GPT family
- Fine-tuning vs RAG vs prompt engineering decision framework
- RLHF (Reinforcement Learning from Human Feedback) for alignment
- Embedding models for semantic search and similarity
- Token-level optimization: quantization (INT8/INT4), pruning, distillation

**Benchmarks (GLUE/SuperGLUE):**
- Text Classification F1: > 90% on standard benchmarks
- NER F1: > 85% for general, > 75% for specialized domains
- Question Answering: > 80% Exact Match on SQuAD

**Key Tools:** Hugging Face Transformers, spaCy, NLTK, vLLM (serving), Sentence-Transformers, LangChain.

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
