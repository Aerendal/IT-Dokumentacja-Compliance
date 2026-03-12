---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-015: MLOps Team Structure Plan

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-015 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [Engineering Manager / VP Engineering] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Annually) |

---

## Document Lifecycle

### When This Document Appears
-  MOP-001 MLOps Strategy approved
-  Budget for team confirmed
-  Organizational commitment secured

### When This Document Becomes Invalid
-  Major reorganization
-  Significant scope change (>30%)
-  Budget reduction (>20%)

### Validity Conditions
-  Roles aligned with strategy
-  Headcount approved
-  Career paths defined
-  Skills inventory current

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-001: MLOps Strategy | Team objectives |
| MOP-013: Implementation Roadmap | Phasing, timeline |
| MOP-014: Tool Evaluation | Skill requirements |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-045: Training Plan | Skill gaps |
| MOP-049: Budget | Personnel costs |
| MOP-013: Roadmap | Resource availability |

### Bidirectional Dependencies
| Document | Relationship |
|----------|--------------|
| MOP-013: Implementation Roadmap | Resources ↔ Timeline |
| MOP-014: Tool Evaluation | Skills ↔ Tool complexity |

---

## Section Dependencies (Internal)

```
┌────────────────────────────────────────────────────────────────┐
│              1. Organizational Context                          │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 2. Team Models   │ │ 3. Roles &   │ │ 4. Skills        │
│                  │ │    Responsibilities │    Matrix   │
└──────────────────┘ └──────────────┘ └──────────────────┘
        │                   │                  │
        └───────────────────┼──────────────────┘
                            ▼
┌────────────────────────────────────────────────────────────────┐
│              5. Team Structure                                  │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 6. Hiring &      │ │ 7. Career    │ │ 8. Operating     │
│    Onboarding    │ │    Paths     │ │    Model         │
└──────────────────┘ └──────────────┘ └──────────────────┘
```

---

## Template Content

---

# MLOps Team Structure Plan

**[Organization Name]**

**Version:** [X.Y]  
**Date:** [YYYY-MM-DD]

---

## 1. Organizational Context

> **Section Dependencies:**
> - Depends on: MOP-001 Strategy
> - Feeds into: All other sections
> - Update trigger: Org changes

### 1.1 Strategic Objectives

| Objective | Team Implication |
|-----------|------------------|
| Reduce deployment time to <1 day | Need ML Platform Engineers |
| 99.9% model availability | Need SRE/DevOps expertise |
| 50+ models in production | Need scalable team structure |
| Full compliance | Need governance/security skills |
| Self-service for ML teams | Need platform mindset |

### 1.2 Current State

| Aspect | Current | Gap |
|--------|---------|-----|
| Total ML headcount | [X] | [+Y needed] |
| MLOps specialists | [X] | [+Y needed] |
| Platform engineers | [X] | [+Y needed] |
| DevOps/SRE | [X] | [+Y needed] |

### 1.3 Organizational Placement

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Organizational Structure Options                  │
│                                                                     │
│  Option A: Centralized MLOps Team                                   │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                         CTO                                  │   │
│  │                          │                                   │   │
│  │     ┌────────────────────┼────────────────────┐             │   │
│  │     │                    │                    │             │   │
│  │  ┌──┴──┐            ┌────┴────┐          ┌───┴───┐         │   │
│  │  │ Data│            │  MLOps  │          │Product│         │   │
│  │  │Science│          │ Platform│          │  ML   │         │   │
│  │  └─────┘            └─────────┘          └───────┘         │   │
│  │                                                              │   │
│  │  Pros: Clear ownership, standardization                      │   │
│  │  Cons: Potential bottleneck, slower feature teams           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  Option B: Embedded Model (Hub-and-Spoke)                          │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                         CTO                                  │   │
│  │                          │                                   │   │
│  │              ┌───────────┼───────────┐                      │   │
│  │              │           │           │                      │   │
│  │         ┌────┴────┐ ┌────┴────┐ ┌────┴────┐                │   │
│  │         │Product A│ │Product B│ │ MLOps   │                │   │
│  │         │ + ML Eng│ │ + ML Eng│ │ Platform│                │   │
│  │         └─────────┘ └─────────┘ │  (Core) │                │   │
│  │                                  └─────────┘                │   │
│  │  Pros: Closer to products, faster iteration                 │   │
│  │  Cons: Inconsistency risk, governance challenges            │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  RECOMMENDED: Option A for Phase 1-2, transition to B in Phase 3   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Team Models

> **Section Dependencies:**
> - Depends on: Section 1 (Context)
> - Feeds into: Section 5 (Structure)
> - Update trigger: Scale changes

### 2.1 Team Model Comparison

| Model | Size | Best For | Pros | Cons |
|-------|------|----------|------|------|
| **Full-Stack MLOps** | 5-10 | Small orgs, early stage | Flexibility, low overhead | Limited specialization |
| **Specialized Teams** | 15-30 | Medium orgs | Deep expertise | Coordination overhead |
| **Platform + Embedded** | 30+ | Large orgs | Scale, ownership | Complexity |

### 2.2 Recommended Model: Specialized Teams

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MLOps Team Structure                              │
│                                                                     │
│                    ┌─────────────────────┐                         │
│                    │   ML Platform Lead   │                         │
│                    │      (Director)      │                         │
│                    └──────────┬──────────┘                         │
│                               │                                     │
│           ┌───────────────────┼───────────────────┐                │
│           │                   │                   │                │
│  ┌────────┴────────┐ ┌───────┴───────┐ ┌────────┴────────┐       │
│  │  ML Platform    │ │   ML Ops      │ │   ML Quality    │       │
│  │  Engineering    │ │   (SRE)       │ │   & Governance  │       │
│  │                 │ │               │ │                 │       │
│  │  - Infrastructure│ │ - Monitoring  │ │ - Testing       │       │
│  │  - Tools        │ │ - Reliability │ │ - Compliance    │       │
│  │  - Integration  │ │ - Incident    │ │ - Security      │       │
│  └─────────────────┘ └───────────────┘ └─────────────────┘       │
│                                                                     │
│  Supported Teams:                                                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│  │  Product A  │ │  Product B  │ │  Product C  │ │    R&D      │ │
│  │  ML Team    │ │  ML Team    │ │  ML Team    │ │  ML Team    │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 Team Sizing by Phase

| Phase | Platform Eng | ML Ops | Quality | Total MLOps | ML Teams Supported |
|-------|--------------|--------|---------|-------------|-------------------|
| Phase 1 | 2 | 1 | 1 | 4 | 2 |
| Phase 2 | 4 | 2 | 2 | 8 | 5 |
| Phase 3 | 5 | 3 | 2 | 10 | 10+ |

---

## 3. Roles & Responsibilities

> **Section Dependencies:**
> - Depends on: Section 2 (Team Models)
> - Feeds into: Section 4 (Skills), Section 6 (Hiring)
> - Update trigger: Role scope changes

### 3.1 Role Catalog

#### Leadership Roles

| Role | Level | Reports To | Direct Reports |
|------|-------|------------|----------------|
| VP of ML Platform | L8 | CTO | 3-5 |
| Director, ML Platform | L7 | VP | 3-4 |
| Senior Manager, MLOps | L6 | Director | 4-6 |

#### Individual Contributor Roles

| Role | Level | Reports To | Team |
|------|-------|------------|------|
| Staff ML Platform Engineer | L6 | Director | Platform |
| Senior ML Platform Engineer | L5 | Manager | Platform |
| ML Platform Engineer | L4 | Manager | Platform |
| Staff MLOps Engineer (SRE) | L6 | Director | Operations |
| Senior MLOps Engineer | L5 | Manager | Operations |
| MLOps Engineer | L4 | Manager | Operations |
| Senior ML Quality Engineer | L5 | Manager | Quality |
| ML Quality Engineer | L4 | Manager | Quality |

### 3.2 Detailed Role Definitions

#### ML Platform Engineer

**Mission:** Build and maintain the ML platform infrastructure that enables ML teams to develop, deploy, and manage models efficiently.

**Responsibilities:**
- Design and implement ML infrastructure components (experiment tracking, model registry, feature store)
- Develop and maintain CI/CD pipelines for ML workloads
- Create and manage Kubernetes-based ML deployment infrastructure
- Build developer tools and SDKs for ML workflows
- Integrate ML platform with data infrastructure
- Document platform capabilities and best practices

**Requirements:**
- 3+ years software engineering experience
- Strong Python and distributed systems knowledge
- Experience with Kubernetes, Docker, cloud platforms
- Familiarity with ML frameworks (PyTorch, TensorFlow, scikit-learn)
- Experience with infrastructure as code (Terraform, Pulumi)

**Success Metrics:**
- Platform uptime and reliability
- Developer satisfaction (NPS)
- Time to deploy new model (P90)
- Number of models supported

---

#### MLOps Engineer (SRE)

**Mission:** Ensure the reliability, performance, and security of production ML systems through operational excellence.

**Responsibilities:**
- Monitor and maintain production ML systems
- Develop and maintain observability infrastructure (metrics, logs, traces)
- Create and execute incident response procedures
- Implement auto-scaling and performance optimization
- Conduct chaos engineering and reliability testing
- On-call support for ML systems

**Requirements:**
- 3+ years DevOps/SRE experience
- Strong Linux, networking, and troubleshooting skills
- Experience with monitoring tools (Prometheus, Grafana, Datadog)
- Kubernetes expertise
- Scripting skills (Python, Bash)
- Experience with incident management

**Success Metrics:**
- Model availability (SLA achievement)
- Mean time to detection (MTTD)
- Mean time to recovery (MTTR)
- Incident reduction over time

---

#### ML Quality Engineer

**Mission:** Ensure ML systems meet quality, security, and compliance standards through testing, governance, and process improvement.

**Responsibilities:**
- Develop ML testing frameworks and strategies
- Implement data quality checks and validation
- Create and maintain model governance processes
- Conduct security reviews for ML systems
- Ensure compliance with regulatory requirements
- Build and maintain documentation standards

**Requirements:**
- 3+ years QA/testing experience
- Understanding of ML concepts and lifecycle
- Experience with testing frameworks and automation
- Knowledge of security best practices
- Familiarity with compliance frameworks (SOC2, GDPR, HIPAA)
- Strong documentation skills

**Success Metrics:**
- Test coverage for ML pipelines
- Compliance audit pass rate
- Documentation completeness
- Security vulnerability resolution time

---

### 3.3 RACI Matrix

| Activity | Platform Eng | MLOps (SRE) | ML Quality | ML Teams |
|----------|--------------|-------------|------------|----------|
| Platform infrastructure | R/A | C | I | I |
| CI/CD pipelines | R/A | C | C | I |
| Model deployment | C | R/A | C | R |
| Monitoring setup | C | R/A | C | I |
| Incident response | C | R/A | I | C |
| Testing frameworks | C | I | R/A | C |
| Governance policies | C | I | R/A | I |
| Model development | I | I | C | R/A |
| Feature engineering | C | I | C | R/A |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

---

## 4. Skills Matrix

> **Section Dependencies:**
> - Depends on: Section 3 (Roles), MOP-014 (Tools)
> - Feeds into: Section 6 (Hiring), MOP-045 (Training)
> - Update trigger: Tool/tech changes

### 4.1 Core Skills by Role

| Skill Category | Platform Eng | MLOps (SRE) | ML Quality |
|----------------|--------------|-------------|------------|
| **Programming** | | | |
| Python | Expert | Advanced | Advanced |
| Go/Rust | Advanced | Intermediate | - |
| SQL | Advanced | Intermediate | Intermediate |
| **Infrastructure** | | | |
| Kubernetes | Expert | Expert | Intermediate |
| Docker | Expert | Expert | Intermediate |
| Terraform/IaC | Expert | Advanced | - |
| Cloud (AWS/GCP) | Expert | Expert | Intermediate |
| **ML/Data** | | | |
| ML frameworks | Intermediate | Basic | Intermediate |
| Data pipelines | Advanced | Intermediate | Intermediate |
| Feature engineering | Intermediate | - | Intermediate |
| **Operations** | | | |
| Monitoring | Advanced | Expert | Intermediate |
| Incident management | Intermediate | Expert | - |
| Security | Advanced | Advanced | Expert |
| **Domain** | | | |
| MLOps tools | Expert | Advanced | Advanced |
| Testing | Intermediate | Intermediate | Expert |
| Compliance | Intermediate | Intermediate | Expert |

### 4.2 Skill Level Definitions

| Level | Definition | Expectations |
|-------|------------|--------------|
| **Expert** | Deep knowledge, teaches others | Can architect solutions, mentor team |
| **Advanced** | Strong practical experience | Can solve complex problems independently |
| **Intermediate** | Working knowledge | Can contribute with guidance |
| **Basic** | Foundational understanding | Awareness, can learn quickly |
| **-** | Not required | Not expected for role |

### 4.3 Current Skills Inventory

| Skill | Current Capacity | Required | Gap |
|-------|------------------|----------|-----|
| Kubernetes Expert | 1 | 3 | -2 |
| MLflow | 0 | 2 | -2 |
| Feature Store | 0 | 2 | -2 |
| Triton Serving | 0 | 1 | -1 |
| ML Monitoring | 0 | 2 | -2 |
| Security (ML) | 1 | 2 | -1 |

### 4.4 Skill Development Plan

| Skill Gap | Strategy | Timeline | Owner |
|-----------|----------|----------|-------|
| Kubernetes | Training + certification | Q1 | Platform Team |
| MLflow | Vendor training | Q1 | Platform Team |
| Feature Store | Internal bootcamp | Q2 | Data Eng |
| Triton | NVIDIA training | Q2 | Platform Team |
| ML Monitoring | Build as you go | Ongoing | MLOps Team |

---

## 5. Team Structure

> **Section Dependencies:**
> - Depends on: Sections 2-4
> - Feeds into: Section 6 (Hiring), Section 8 (Operating Model)
> - Update trigger: Team growth

### 5.1 Phase 1 Team (Months 1-6)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Phase 1: Foundation Team (4 FTE)                  │
│                                                                     │
│                    ┌─────────────────────┐                         │
│                    │  ML Platform Lead   │                         │
│                    │    (50% allocated)  │                         │
│                    └──────────┬──────────┘                         │
│                               │                                     │
│           ┌───────────────────┼───────────────────┐                │
│           │                   │                   │                │
│  ┌────────┴────────┐ ┌───────┴───────┐ ┌────────┴────────┐       │
│  │ Sr. ML Platform │ │    MLOps      │ │  ML Quality     │       │
│  │   Engineer      │ │   Engineer    │ │   Engineer      │       │
│  └─────────────────┘ └───────────────┘ └─────────────────┘       │
│                                                                     │
│  Focus Areas:                                                       │
│  - Infrastructure setup                                            │
│  - MLflow deployment                                               │
│  - Basic CI/CD                                                     │
│  - Pilot model migration                                           │
└─────────────────────────────────────────────────────────────────────┘
```

**Hiring Priority for Phase 1:**
1. Senior ML Platform Engineer (Week 1-4)
2. MLOps Engineer (Week 3-6)
3. ML Quality Engineer (Week 5-8)

### 5.2 Phase 2 Team (Months 6-12)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Phase 2: Expansion Team (8 FTE)                   │
│                                                                     │
│                    ┌─────────────────────┐                         │
│                    │  ML Platform Lead   │                         │
│                    │    (Director)       │                         │
│                    └──────────┬──────────┘                         │
│                               │                                     │
│     ┌─────────────────────────┼─────────────────────────┐          │
│     │                         │                         │          │
│  ┌──┴───────────────┐  ┌──────┴──────┐  ┌──────────────┴──┐      │
│  │ Platform Team(4) │  │  Ops Team(2)│  │ Quality Team(2) │      │
│  │                  │  │             │  │                 │      │
│  │ - Sr Engineer x2 │  │ - Sr MLOps  │  │ - Sr QA         │      │
│  │ - Engineer x2    │  │ - MLOps     │  │ - QA            │      │
│  └──────────────────┘  └─────────────┘  └─────────────────┘      │
│                                                                     │
│  Focus Areas:                                                       │
│  - Feature store deployment                                        │
│  - Advanced serving (Triton)                                       │
│  - Model migration at scale                                        │
│  - Monitoring & observability                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.3 Phase 3 Team (Months 12-18)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Phase 3: Mature Team (10+ FTE)                    │
│                                                                     │
│                    ┌─────────────────────┐                         │
│                    │  ML Platform Lead   │                         │
│                    │    (Director)       │                         │
│                    └──────────┬──────────┘                         │
│                               │                                     │
│     ┌─────────────────────────┼─────────────────────────┐          │
│     │                         │                         │          │
│  ┌──┴───────────────┐  ┌──────┴──────┐  ┌──────────────┴──┐      │
│  │ Platform Team(5) │  │  Ops Team(3)│  │ Quality Team(2) │      │
│  │                  │  │             │  │                 │      │
│  │ - Staff Eng x1   │  │ - Staff SRE │  │ - Sr QA         │      │
│  │ - Sr Engineer x2 │  │ - Sr MLOps  │  │ - QA            │      │
│  │ - Engineer x2    │  │ - MLOps     │  │                 │      │
│  └──────────────────┘  └─────────────┘  └─────────────────┘      │
│                                                                     │
│  Focus Areas:                                                       │
│  - Platform optimization                                           │
│  - Self-service enablement                                         │
│  - Advanced governance                                             │
│  - Cost optimization                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. Hiring & Onboarding

> **Section Dependencies:**
> - Depends on: Section 5 (Structure)
> - Feeds into: MOP-013 (Roadmap)
> - Update trigger: Hiring progress

### 6.1 Hiring Plan

| Role | Phase | Start Month | Hiring Source | Priority |
|------|-------|-------------|---------------|----------|
| Sr. ML Platform Engineer | 1 | M1 | External | P0 |
| MLOps Engineer | 1 | M2 | Internal/External | P0 |
| ML Quality Engineer | 1 | M2 | External | P1 |
| ML Platform Engineer | 2 | M5 | External | P1 |
| ML Platform Engineer | 2 | M6 | External | P1 |
| Sr. MLOps Engineer | 2 | M7 | External | P1 |
| Sr. ML Quality Engineer | 2 | M8 | Internal | P2 |
| Staff ML Platform Engineer | 3 | M12 | External | P1 |
| Staff MLOps Engineer | 3 | M13 | External | P2 |
| ML Platform Engineer | 3 | M14 | External | P2 |

### 6.2 Hiring Criteria

| Criterion | Weight | Assessment Method |
|-----------|--------|-------------------|
| Technical skills | 40% | Coding interview, system design |
| MLOps domain knowledge | 25% | Technical discussion |
| Problem-solving | 15% | Case study |
| Communication | 10% | Behavioral interview |
| Culture fit | 10% | Team interview |

### 6.3 Interview Process

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Interview Process (2 weeks)                       │
│                                                                     │
│  Day 1-3           Day 4-7           Day 8-10        Day 11-14     │
│  ┌─────────┐      ┌─────────┐       ┌─────────┐     ┌─────────┐   │
│  │ Resume  │ ───► │Technical│ ───►  │ Onsite  │ ──► │ Offer   │   │
│  │ Screen  │      │  Phone  │       │  Loop   │     │ Decision│   │
│  └─────────┘      └─────────┘       └─────────┘     └─────────┘   │
│                                           │                        │
│                                     ┌─────┴─────┐                  │
│                                     │           │                  │
│                               ┌─────┴───┐ ┌─────┴───┐              │
│                               │System   │ │Behavioral│             │
│                               │Design   │ │+ Culture │             │
│                               └─────────┘ └──────────┘             │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.4 Onboarding Plan

| Week | Focus | Activities | Deliverable |
|------|-------|------------|-------------|
| 1 | Orientation | IT setup, HR, team intros | Access to all systems |
| 2 | Platform overview | Architecture review, tool demos | Platform understanding |
| 3 | Hands-on | Shadow projects, pair programming | First PR merged |
| 4 | First project | Small feature or bug fix | Project completed |
| 5-6 | Deep dive | Own area deep-dive | Area expertise |
| 7-8 | Independence | Lead small project | Project delivered |

### 6.5 30-60-90 Day Plan

**30 Days (Learning):**
- Complete all onboarding training
- Understand platform architecture
- Meet all team members and stakeholders
- Complete first small project
- Shadow on-call rotation

**60 Days (Contributing):**
- Own a component or feature area
- Participate in code reviews
- Join on-call rotation
- Contribute to documentation
- Complete tool certifications

**90 Days (Ownership):**
- Lead a medium project end-to-end
- Mentor newer team members
- Propose improvements to processes
- Present work to broader team
- Full on-call responsibility

---

## 7. Career Paths

> **Section Dependencies:**
> - Depends on: Section 3 (Roles)
> - Feeds into: Retention strategy
> - Update trigger: Level definitions change

### 7.1 Career Ladder

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MLOps Career Ladder                               │
│                                                                     │
│  Management Track          │        Technical Track                 │
│                            │                                        │
│  ┌──────────────────┐     │     ┌──────────────────┐              │
│  │ VP of ML Platform│     │     │ Distinguished    │     L9       │
│  │     (L8)         │     │     │    Engineer      │              │
│  └────────┬─────────┘     │     └────────┬─────────┘              │
│           │               │              │                         │
│  ┌────────┴─────────┐     │     ┌────────┴─────────┐              │
│  │ Director, ML     │     │     │ Principal        │     L7       │
│  │ Platform (L7)    │     │     │   Engineer       │              │
│  └────────┬─────────┘     │     └────────┬─────────┘              │
│           │               │              │                         │
│  ┌────────┴─────────┐     │     ┌────────┴─────────┐              │
│  │ Sr. Manager      │◄────┼────►│ Staff Engineer   │     L6       │
│  │     (L6)         │     │     │                  │              │
│  └────────┬─────────┘     │     └────────┬─────────┘              │
│           │               │              │                         │
│           │               │     ┌────────┴─────────┐              │
│           │               │     │ Sr. Engineer     │     L5       │
│           │               │     │                  │              │
│           │               │     └────────┬─────────┘              │
│           │               │              │                         │
│           │               │     ┌────────┴─────────┐              │
│           └───────────────┼────►│ Engineer         │     L4       │
│                           │     │                  │              │
│                           │     └────────┬─────────┘              │
│                           │              │                         │
│                           │     ┌────────┴─────────┐              │
│                           │     │ Jr. Engineer     │     L3       │
│                           │     │                  │              │
│                           │     └──────────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 Level Expectations

| Level | Scope | Impact | Leadership |
|-------|-------|--------|------------|
| L3 | Tasks | Self | Learning |
| L4 | Features | Team | Peer mentoring |
| L5 | Projects | Team/Cross-team | Project lead |
| L6 | Programs | Organization | Technical/people lead |
| L7 | Strategy | Business unit | Director |
| L8+ | Vision | Company | Executive |

### 7.3 Promotion Criteria

**L4 → L5 (Engineer → Senior):**
- Consistently delivers projects end-to-end
- Mentors junior team members
- Strong code review contributions
- Drives technical improvements
- 2-3 years at level

**L5 → L6 (Senior → Staff):**
- Owns significant technical area
- Cross-team technical leadership
- Influences technical direction
- External visibility (talks, blogs)
- 3-4 years at level

---

## 8. Operating Model

> **Section Dependencies:**
> - Depends on: Sections 5-7
> - Feeds into: Day-to-day operations
> - Update trigger: Process changes

### 8.1 Team Rituals

| Ritual | Frequency | Duration | Purpose | Attendees |
|--------|-----------|----------|---------|-----------|
| Daily Standup | Daily | 15 min | Sync, blockers | Team |
| Sprint Planning | Bi-weekly | 2 hr | Sprint goals | Team |
| Sprint Retro | Bi-weekly | 1 hr | Process improvement | Team |
| Tech Review | Weekly | 1 hr | Technical decisions | Leads |
| All Hands | Monthly | 1 hr | Updates, recognition | All |
| Architecture Review | Monthly | 2 hr | Major decisions | Architects |
| 1:1s | Weekly | 30 min | Coaching, feedback | Manager + IC |

### 8.2 Communication Channels

| Channel | Purpose | Response Time |
|---------|---------|---------------|
| Slack #mlops-team | General discussion | 4 hours |
| Slack #mlops-incidents | Incidents | 15 minutes |
| Slack #mlops-support | User support | 4 hours |
| Email | External, formal | 24 hours |
| Jira | Task tracking | Per sprint |
| Confluence | Documentation | Async |

### 8.3 On-Call Rotation

```
┌─────────────────────────────────────────────────────────────────────┐
│                    On-Call Structure                                 │
│                                                                     │
│  Primary On-Call (Weekly Rotation)                                  │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Week 1: Engineer A → Week 2: Engineer B → Week 3: Engineer C│   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  Escalation Path:                                                   │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │ Primary │ ─► │Secondary│ ─► │  Lead   │ ─► │ Director│        │
│  │ (5 min) │    │(15 min) │    │(30 min) │    │(critical)│       │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘        │
│                                                                     │
│  Coverage: 24/7 for P1/P2, business hours for P3/P4               │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.4 Support Model

| Tier | Response | Resolution | Handled By |
|------|----------|------------|------------|
| Tier 1 | 15 min | 1 hr | On-call |
| Tier 2 | 1 hr | 4 hr | Specialist |
| Tier 3 | 4 hr | 24 hr | Senior/Staff |

### 8.5 Key Metrics

| Metric | Target | Tracking |
|--------|--------|----------|
| Sprint velocity | Stable +/- 10% | Jira |
| On-time delivery | > 80% | Project tracker |
| MTTR | < 30 min | Incident tracker |
| NPS (internal) | > 50 | Quarterly survey |
| Attrition | < 10% | HR |

---

## Appendices

### Appendix A: Job Descriptions

[Include full job descriptions for each role]

### Appendix B: Interview Questions

[Include sample interview questions by role]

### Appendix C: Compensation Benchmarks

| Role | Level | Market 50th | Market 75th | Target |
|------|-------|-------------|-------------|--------|
| ML Platform Engineer | L4 | $150K | $175K | 60th |
| Sr. ML Platform Engineer | L5 | $180K | $210K | 60th |
| Staff ML Platform Engineer | L6 | $220K | $260K | 60th |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Author] | Initial draft |
| 0.9 | [Date] | [Author] | HR review |
| 1.0 | [Date] | [Author] | Approved version |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| VP Engineering | | | |
| HR Business Partner | | | |
| Finance | | | |
