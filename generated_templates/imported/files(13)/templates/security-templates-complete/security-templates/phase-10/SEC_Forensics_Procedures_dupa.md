---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-044: Digital Forensics Procedures

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-044 |
| **Version** | 1.0 |
| **Classification** | Restricted |
| **Owner** | Forensics Lead |
| **NIST CSF** | RS.AN |

---

## 1. EVIDENCE COLLECTION

### 1.1 Order of Volatility
1. CPU registers, cache
2. Memory (RAM)
3. Network state
4. Running processes
5. Disk storage
6. Backup media
7. Logs/printouts

### 1.2 Collection Procedures

| Evidence Type | Tool | Procedure |
|---------------|------|-----------|
| Memory | [Tool] | Full RAM capture |
| Disk | [Tool] | Forensic image (write-blocked) |
| Network | [Tool] | PCAP capture |
| Logs | SIEM | Export with timestamps |

## 2. CHAIN OF CUSTODY

| Field | Required |
|-------|----------|
| Evidence ID | Unique identifier |
| Description | What was collected |
| Collected by | Name, role |
| Date/Time | ISO format |
| Hash | SHA-256 |
| Storage location | Secure evidence locker |

## 3. ANALYSIS PROCEDURES
- Timeline analysis
- Malware analysis (sandboxed)
- Log correlation
- IOC extraction

## 4. REPORTING
[Forensic report template reference]
