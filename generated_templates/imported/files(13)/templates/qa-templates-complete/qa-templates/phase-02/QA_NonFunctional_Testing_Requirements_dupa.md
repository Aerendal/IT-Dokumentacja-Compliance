---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-007: Non-Functional Testing Requirements

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-007 |
| **Version** | 1.0 |
| **Owner** | Performance Lead |
| **ISO 25010** | Quality Characteristics |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Requirements phase | NFR defined |
| **Active** | Project duration | NFR testing |
| **Review** | Per release | Performance changes |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| System Requirements | NFR source |
| SLA Agreements | Performance targets |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-012 Performance Approach | Test approach |
| QA-029 Security Testing | Security tests |

---

## 1. PERFORMANCE REQUIREMENTS
| Req ID | Metric | Target | Priority |
|--------|--------|--------|----------|
| NFR-001 | Page load | <2s | P1 |
| NFR-002 | API response | <500ms | P1 |
| NFR-003 | Concurrent users | 1000 | P1 |
| NFR-004 | Throughput | 100 TPS | P2 |

## 2. RELIABILITY REQUIREMENTS
| Req ID | Metric | Target |
|--------|--------|--------|
| NFR-010 | Availability | 99.9% |
| NFR-011 | MTBF | >720 hrs |
| NFR-012 | MTTR | <4 hrs |

## 3. SECURITY REQUIREMENTS
| Req ID | Requirement | Priority |
|--------|-------------|----------|
| NFR-020 | OWASP Top 10 | P1 |
| NFR-021 | Encryption at rest | P1 |
| NFR-022 | TLS 1.3 | P1 |

## 4. COMPATIBILITY
| Req ID | Requirement |
|--------|-------------|
| NFR-030 | Chrome, Firefox, Safari, Edge |
| NFR-031 | iOS 14+, Android 10+ |

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Performance Lead | | | |
| Architect | | | |
