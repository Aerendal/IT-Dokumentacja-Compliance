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
| Faza 1 — ContextClassifier + NLPCore | ⬜ Do implementacji |
| Faza 2 — SemanticRoleLabeler | ⬜ Do implementacji |
| Faza 3 — Compliance Plugins | ⬜ Do implementacji |
| Faza 4 — CrossReference + Raport | ⬜ Do implementacji |
| Faza 5 — Integracja z FastAPI/CLI | ⬜ Do implementacji |

## Szybki start (po implementacji)

```bash
# Nowe CLI command
itdoc nlp-audit docs/security_policy.md

# Nowy endpoint API
POST /nlp/audit
{"path": "docs/security_policy.md", "mode": "POST_EXECUTION"}

# Nowy skrypt standalone
python scripts/nlp/nlp_engine.py --doc docs/policy.md --mode post
```
