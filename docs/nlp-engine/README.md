---
title: "NLP Engine — Mikroserwis Analizy Semantycznej"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
status: "PLANNED"
tags:
  - nlp-engine
  - microservice
  - compliance
  - semantic-analysis
audit_rules:
  - ARCH-01
related_docs:
  - "ARCHITECTURE.md"
  - "MODULES.md"
  - "IMPLEMENTATION_PLAN.md"
  - "INTEGRATION.md"
  - "TESTING.md"
  - "DOC_AUDIT_MODULE.md"
---

# NLP Engine — Mikroserwis Analizy Semantycznej

## Czym jest ten komponent?

NLP Engine to **deterministyczna warstwa analizy semantycznej** działająca jako mikroserwis na szczycie istniejącego silnika compliance (`itdoc/`, `scripts/`). Jego zadaniem jest **nie zastąpienie** obecnego pipeline'u, lecz rozszerzenie go o zdolność rozumienia **znaczenia** zdań w dokumentach IT — nie tylko ich obecności.

## Problem który rozwiązuje

Obecny engine sprawdza czy słowo kluczowe **istnieje** w dokumencie. NLP Engine rozumie **co to zdanie znaczy**:

| Obecny engine | NLP Engine |
|---|---|
| `"szyfrowanie" in text` → ✅ | `"dane NIE są szyfrowane"` → ❌ ERROR |
| `"test" in text` → ✅ | `"testy zostaną przeprowadzone"` → ⚠️ brak dowodu |
| `"autoryzacja" in text` → ✅ | `"API wymaga autoryzacji"` → wyciąga: agent=API, action=wymagać, obj=autoryzacja |

## Miejsce w architekturze projektu

```
┌─────────────────────────────────────────────────┐
│              IT Dokumentacja Compliance          │
│                                                 │
│  ┌──────────────┐    ┌──────────────────────┐   │
│  │  itdoc/      │    │  scripts/            │   │
│  │  (core lib)  │    │  pipeline_run.py     │   │
│  │  cli.py      │    │  map_standards.py    │   │
│  │  analytics   │    │  check_standards.py  │   │
│  └──────┬───────┘    └──────────┬───────────┘   │
│         │                       │               │
│         └───────────┬───────────┘               │
│                     ↓                           │
│         ┌───────────────────────┐               │
│         │   SQLite Database     │               │
│         │   doc_standard_mapping│               │
│         │   template_violations │               │
│         └───────────┬───────────┘               │
│                     │                           │
│  ════════════════ NLP LAYER ═══════════════════ │
│                     ↓                           │
│         ┌───────────────────────┐               │
│         │   scripts/nlp/        │  ← NOWY KOD  │
│         │   nlp_engine.py       │               │
│         │   plugins/            │               │
│         │   models/             │               │
│         └───────────┬───────────┘               │
│                     ↓                           │
│         ┌───────────────────────┐               │
│         │   nlp_findings        │  ← NOWE TABELE│
│         │   nlp_traceability    │               │
│         └───────────────────────┘               │
└─────────────────────────────────────────────────┘
```

## Zasady projektowe

- **Deterministyczność** — identyczne wejście = identyczny wynik, zawsze
- **Offline-first** — bez zewnętrznych API, bez LLM, bez chmury
- **Rozszerzalność** — nowy standard = nowy plugin, zero zmian w core
- **Nie niszczy istniejącego** — dodaje kolumny/tabele, nie zmienia obecnych

## Status

| Komponent | Status |
|---|---|
| Specyfikacja (ten dokument) | ✅ Gotowa |
| Architektura | ✅ Zaprojektowana |
| **Moduł audytu dokumentacji** (`scripts/nlp/`) | ✅ Zaimplementowany |
| — `text_utils.py` — normalizacja polskiego tekstu | ✅ |
| — `similarity_engine.py` — TF-IDF + cosine (pure stdlib) | ✅ |
| — `gap_detector.py` — wykrywanie luk kompletności | ✅ |
| — `duplicate_detector.py` — exact/extending/thematic/partial | ✅ |
| — `relation_mapper.py` — mapowanie powiązań między docs | ✅ |
| — `doc_auditor.py` — orkiestrator + SQLite + CLI | ✅ |
| — 89 testów jednostkowych i integracyjnych | ✅ |
| — `compliance_check.py doc-audit` subkomenda | ✅ |
| Faza 1 — ContextClassifier + NLPCore | ⬜ Do implementacji |
| Faza 2 — SemanticRoleLabeler | ⬜ Do implementacji |
| Faza 3 — Compliance Plugins | ⬜ Do implementacji |
| Faza 4 — CrossReference + Raport | ⬜ Do implementacji |
| Faza 5 — Integracja z FastAPI/CLI | ⬜ Do implementacji |

## Szybki start

### Moduł Audytu Dokumentacji (✅ działa teraz)

```bash
# Skan dokumentów — wykryj luki, duplikaty, relacje
python scripts/nlp/doc_auditor.py scan --dir dokumentacja/docs/

# Raport z ostatniego przebiegu
python scripts/nlp/doc_auditor.py report --run-id <UUID>

# Lista wszystkich przebiegów
python scripts/nlp/doc_auditor.py list-runs

# Przez centralny compliance script
python scripts/compliance_check.py doc-audit --dir dokumentacja/docs/

# Testy
python -m pytest tests/test_nlp_doc_auditor.py -v
# 89 passed in 0.47s
```

### Silnik Semantyczny (⬜ po Fazach 1–5)

```bash
# Nowe CLI command
itdoc nlp-audit docs/security_policy.md

# Nowy endpoint API
POST /nlp/audit
{"path": "docs/security_policy.md", "mode": "POST_EXECUTION"}

# Nowy skrypt standalone
python scripts/nlp/nlp_engine.py --doc docs/policy.md --mode post
```
