---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-046: MLOps Certification Program

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-046 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead / L&D] |

---

## 1. Certification Overview

### 1.1 Certification Levels

| Level | Name | Target Audience | Prerequisites |
|-------|------|-----------------|---------------|
| Bronze | MLOps Practitioner | All ML users | Platform 101 |
| Silver | MLOps Engineer | ML Engineers | Bronze + 3 months |
| Gold | MLOps Expert | Sr. Engineers, Leads | Silver + 6 months |

### 1.2 Benefits

| Level | Benefits |
|-------|----------|
| Bronze | Platform access, basic support |
| Silver | Priority support, deploy to staging |
| Gold | Deploy to production, architecture reviews |

---

## 2. Bronze Certification: MLOps Practitioner

### 2.1 Requirements

| Requirement | Details |
|-------------|---------|
| Training | MLOps Platform 101 (4 hours) |
| Hands-on | Complete 3 guided labs |
| Assessment | 30-question quiz (70% to pass) |
| Time to complete | 1-2 weeks |

### 2.2 Curriculum

| Module | Duration | Topics |
|--------|----------|--------|
| 1. Platform Overview | 1 hour | Architecture, components, access |
| 2. Experiment Tracking | 1 hour | MLflow basics, logging, UI |
| 3. Feature Store Basics | 1 hour | Feast concepts, feature retrieval |
| 4. Model Registry | 1 hour | Registration, versioning, stages |

### 2.3 Labs

| Lab | Duration | Objective |
|-----|----------|-----------|
| Lab 1 | 30 min | Log experiment to MLflow |
| Lab 2 | 30 min | Retrieve features from Feast |
| Lab 3 | 30 min | Register model to registry |

### 2.4 Assessment Topics

- Platform architecture (20%)
- Experiment tracking (25%)
- Feature store basics (25%)
- Model registry (20%)
- Best practices (10%)

---

## 3. Silver Certification: MLOps Engineer

### 3.1 Requirements

| Requirement | Details |
|-------------|---------|
| Prerequisites | Bronze certification |
| Experience | 3+ months using platform |
| Training | Advanced MLOps (8 hours) |
| Project | Deploy model to staging |
| Assessment | Practical exam (80% to pass) |
| Time to complete | 1-2 months |

### 3.2 Curriculum

| Module | Duration | Topics |
|--------|----------|--------|
| 1. CI/CD for ML | 2 hours | Pipelines, testing, automation |
| 2. Advanced Features | 2 hours | Feature engineering, streaming |
| 3. Model Serving | 2 hours | KServe, Triton, optimization |
| 4. Monitoring | 2 hours | Metrics, drift, alerting |

### 3.3 Project Requirements

**Deploy a Model to Staging:**
1. Train model with proper experiment tracking
2. Create feature definitions in Feast
3. Register model with full documentation
4. Deploy to staging via CI/CD
5. Set up basic monitoring

**Evaluation Criteria:**
- Code quality and organization
- Proper experiment logging
- Complete model documentation
- Successful deployment
- Monitoring configured

### 3.4 Practical Exam

| Section | Duration | Weight |
|---------|----------|--------|
| Troubleshooting | 30 min | 30% |
| Pipeline creation | 45 min | 40% |
| Architecture Q&A | 15 min | 30% |

---

## 4. Gold Certification: MLOps Expert

### 4.1 Requirements

| Requirement | Details |
|-------------|---------|
| Prerequisites | Silver certification |
| Experience | 6+ months, 3+ production models |
| Training | Expert MLOps (16 hours) |
| Project | End-to-end production system |
| Assessment | Architecture review + oral exam |
| Time to complete | 3-6 months |

### 4.2 Curriculum

| Module | Duration | Topics |
|--------|----------|--------|
| 1. Platform Architecture | 4 hours | Deep dive, customization |
| 2. Advanced Pipelines | 4 hours | Kubeflow, complex DAGs |
| 3. Production Excellence | 4 hours | HA, DR, performance |
| 4. Governance & Compliance | 4 hours | Regulations, auditing |

### 4.3 Project Requirements

**Production ML System:**
1. Design and document architecture
2. Implement complete ML pipeline
3. Deploy to production with approvals
4. Configure comprehensive monitoring
5. Document runbooks and procedures
6. Present to review board

**Evaluation Criteria:**
- Architecture quality
- Production readiness
- Monitoring completeness
- Documentation quality
- Knowledge demonstration

### 4.4 Oral Examination

| Topic | Duration | Focus |
|-------|----------|-------|
| Architecture decisions | 20 min | Design tradeoffs |
| Troubleshooting scenarios | 20 min | Problem solving |
| Best practices | 20 min | Recommendations |

---

## 5. Certification Process

### 5.1 Registration

1. Log into Learning Portal
2. Select certification level
3. Review requirements
4. Register for training sessions
5. Begin curriculum

### 5.2 Assessment Scheduling

- Bronze: Self-service, any time
- Silver: Schedule with L&D (2 weeks notice)
- Gold: Schedule review board (1 month notice)

### 5.3 Retake Policy

| Level | Wait Period | Attempts |
|-------|-------------|----------|
| Bronze | 1 week | Unlimited |
| Silver | 2 weeks | 3 per year |
| Gold | 1 month | 2 per year |

---

## 6. Certification Maintenance

### 6.1 Renewal Requirements

| Level | Validity | Renewal |
|-------|----------|---------|
| Bronze | 2 years | Complete refresher (2 hours) |
| Silver | 2 years | 20 hours continuing education |
| Gold | 2 years | 30 hours + contribution |

### 6.2 Continuing Education Options

- Platform training sessions
- Conference attendance
- Writing documentation
- Mentoring others
- Contributing to platform tools

---

## 7. Recognition

### 7.1 Digital Badges

Badges issued via Credly:
- Display on LinkedIn
- Include in email signature
- Verify via public URL

### 7.2 Internal Recognition

| Level | Recognition |
|-------|-------------|
| Bronze | Certificate, Slack badge |
| Silver | Certificate, LinkedIn badge, swag |
| Gold | Certificate, all badges, annual award eligibility |

---

## 8. Metrics

| Metric | Target |
|--------|--------|
| Bronze completion rate | >90% of ML users |
| Silver completion rate | >50% of ML Engineers |
| Gold certified | 2-3 per team |
| Certification NPS | >50 |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial certification program |
