---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-049: Threat Intelligence Integration

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-049 |
| **Version** | 1.0 |
| **Owner** | Threat Intel Analyst |
| **NIST CSF** | ID.RA, DE.CM |

---

## 1. INTELLIGENCE SOURCES

| Source | Type | Frequency | Integration |
|--------|------|-----------|-------------|
| [Commercial feed] | IOC feed | Real-time | SIEM |
| MITRE ATT&CK | TTPs | Quarterly | Detection rules |
| CISA alerts | Threat advisories | As published | Manual review |
| ISACs | Sector-specific | Daily | Email + SIEM |
| Open source | OSINT | Continuous | TIP |

## 2. IOC LIFECYCLE

| Stage | Action | Tool |
|-------|--------|------|
| Collection | Ingest feeds | TIP |
| Enrichment | Add context | TIP |
| Analysis | Relevance check | Analyst |
| Dissemination | Push to controls | SIEM, FW, EDR |
| Review | Effectiveness | Monthly |

## 3. INTEGRATION POINTS

| Destination | IOC Types | Action |
|-------------|-----------|--------|
| SIEM | IP, domain, hash | Alert |
| Firewall | IP, domain | Block |
| EDR | Hash, behavior | Block/Alert |
| Email gateway | Domain, sender | Block |
