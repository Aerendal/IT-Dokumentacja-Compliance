---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Internet Research - IT Documentation Matrix Part 6
## Branże 46-54 | Standards & Frameworks

### 46. Computer Graphics / 3D Rendering
- **OpenGL** (currently 4.6), **Vulkan** (1.3+), **DirectX** (12 Ultimate), **WebGPU** (W3C standard, shipping 2024+)
- **IEEE 1394** (FireWire legacy), IEEE standards for GPU computing
- **Khronos Group** - OpenGL, Vulkan, OpenCL, WebGL specifications
- **ACES** (Academy Color Encoding System) - film/VFX color standard
- Key tools: Blender (open source), Maya, 3ds Max, Unity, Unreal Engine 5
- Performance metrics: FPS, GPU utilization, draw calls, VRAM usage

### 47. Performance Engineering Extended
- **SRE Best Practices** (Google SRE book) - SLOs, error budgets, latency percentiles
- **OWASP Performance** guidelines
- **APM tools**: Datadog, New Relic, Dynatrace, OpenTelemetry (CNCF standard)
- **Load Testing**: JMeter, k6, Gatling, Locust
- **Key metrics**: p50/p95/p99 latency, throughput (req/s), error rates, saturation
- **Akamai Performance standards**, Web Vitals (Google)

### 48. Accessibility Engineering (A11y)
- **WCAG 2.2** (Oct 2023) - current official standard; Level A, AA, AAA
- **WCAG 3.0** - Working Draft (Sep 2025 update); Bronze/Silver/Gold model; 174 outcomes; NOT final standard; expected 2030+
- **WAI-ARIA 1.2** - Accessible Rich Internet Applications
- **Section 508** (US) - rehabilitation act, references WCAG 2.0 success criteria (17 criteria adopted Jan 2017)
- **ADA Title II** (US) - DOJ final rule April 2024, references WCAG 2.1 AA for state/local govts
- **European Accessibility Act (EAA)** - legally applicable June 28, 2025; requires WCAG 2.1 AA
- **EN 301 549** (European) - currently WCAG 2.1, transitioning to 2.2
- Tools: axe-core, Lighthouse, WAVE, NVDA, JAWS, VoiceOver

### 49. API Gateway / Service Mesh Engineering
- **OpenAPI 3.1** (2021) - API specification standard (Swagger)
- **gRPC** (Google) - high-performance RPC framework
- **Istio** (CNCF) - most popular service mesh; sidecar proxy pattern (Envoy)
- **Linkerd** - lightweight service mesh
- **Consul** (HashiCorp) - service discovery + mesh
- **Kong** - API Gateway (open source)
- **AWS API Gateway**, **Apigee** (Google) - managed gateways
- **mTLS** (mutual TLS) - service-to-service security
- **OAuth 2.0**, **JWT** - API authentication standards
- Patterns: circuit breaker, rate limiting, traffic splitting, canary deployment

### 50. Identity & Access Management (IAM) - Extended
- **NIST SP 800-53** Rev 5 - Security Controls (AC family: Access Control)
- **NIST SP 800-63B** - Digital Identity Guidelines (authentication)
- **OAuth 2.0** (RFC 6749) + **OIDC** (OpenID Connect)
- **SAML 2.0** - federated identity standard
- **FIDO2 / WebAuthn** - passwordless authentication (W3C standard)
- **SCIM** (RFC 7643) - System for Cross-domain Identity Management
- **ISO 27001** - information security management
- Key concerns: zero trust architecture, privileged access management (PAM), just-in-time access

### 51. E-Commerce Platform Engineering
- **PCI DSS v4.0.1** (June 2024) - Payment Card Industry Data Security Standard
  - 64 new requirements; 51 future-dated now MANDATORY since March 31, 2025
  - Key: MFA for CDE access, payment page script security (Req 6.4.3, 11.6.1), 12-char passwords
  - Anti-e-skimming: script integrity monitoring on checkout pages
- **GDPR** / **CCPA** - data privacy for customer data
- **OWASP Top 10** - web application security
- **ISO 27001** - security management for e-commerce platforms
- **PSD2** (Europe) - Payment Services Directive, Strong Customer Authentication (SCA)
- Fraud detection: ML-based, velocity checks, 3D Secure 2.0

### 52. Supply Chain IT / Logistics Systems
- **ISO 28000** - Supply chain management security
- **ISO 9001** - Quality management
- **EDI Standards**: X12 (US/Canada), UN/EDIFACT (international)
- **GS1** - global standards for supply chain identification (barcodes, GTIN)
- **RFID** standards (ISO 18000 series)
- **ISO 44001** - collaboration management
- **SCOR Model** - Supply Chain Operations Reference Model
- **Digital Twin** technology for supply chain simulation

### 53. Educational Technology (EdTech)
- **FERPA** (Family Educational Rights and Privacy Act) - US student data privacy
- **COPPA** (Children's Online Privacy Protection Act) - children under 13
- **GDPR** Article 8 - age of consent for data processing (16 in most EU states)
- **SCORM** (Sharable Content Object Reference Model) - e-learning packaging standard
- **xAPI / Tin Can API** - learning experience data exchange
- **LTI** (Learning Tools Interoperability) - IMS standard for tool integration
- **QTI** (Question and Test Interoperability) - assessment standard
- **WCAG 2.1 AA** - accessibility for educational platforms
- **PESC** - student data exchange standards
- Major LMS platforms: Moodle, Canvas, Blackboard, Google Classroom

### 54. Energy & Utilities IT
- **NERC CIP** (Critical Infrastructure Protection) - mandatory for North American BES
  - CIP-002 through CIP-015 (14 standards); covers access control, physical security, incident response
  - **CIP-015-1** (INSM - Internal Network Security Monitoring) approved by FERC June 2025
  - MFA mandate expansion, supply chain risk management (CIP-013-2)
  - 2025 Roadmap: expanding to DERs, cloud services, low-impact systems
- **IEC 62351** - Power system security (cybersecurity for SCADA/ICS)
- **IEC 61850** - Communication standard for substations
- **NERC PSEI** - Power System Engineering Infrastructure
- **FERC** (Federal Energy Regulatory Commission) - US regulator
- **ISO 55001** - Asset management for utilities
- **ICS-CERT** advisories - OT/ICS vulnerability management
- **NIST CSF 2.0** - applicable to critical infrastructure protection
