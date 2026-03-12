# 02 — System State Description

**Status:** Draft v1.0  
**Powiązane dokumenty:** 01_vision_and_scope, 03_architecture_overview  
**Cel dokumentu:** Opisać aktualny stan biblioteki `itdoc` jako punkt wyjścia, zidentyfikować lukę, którą wypełnia Warsztat, oraz zmapować co istnieje vs. co trzeba zbudować.

---

## 1. Istniejący system — biblioteka `itdoc`

### 1.1 Co jest

```
dokumentacja/
├── itdoc/                    # Biblioteka Python (8 modułów, ~1 200 linii)
│   ├── query.py              # find_by_standard, find_by_regulation, rhythm_*, get_contract
│   ├── template.py           # load_template, validate_template
│   ├── db.py                 # get_connection, validate_schema
│   ├── analytics.py          # coverage_by_standard, library_health_report
│   ├── anchor.py             # to_anchor (polskie znaki → URL)
│   ├── cli.py                # CLI: find, contract, validate, rhythm, db-check
│   └── exceptions.py         # ItDocError, SchemaError, QueryError, TemplateError
├── it_doc_matrix.db          # SQLite WAL, ~60 tabel
├── generated_templates/
│   ├── core/                 # 7 203 szablony Markdown
│   └── satellite/            # 741 szablonów specjalistycznych
└── scripts/
    ├── maintenance/          # 14 skryptów (audit, patch, enrich, suggest, analyze)
    └── *.py                  # Pipeline, wizard, gap analysis, derive_*
```

### 1.2 Baza wiedzy — kluczowe dane

| Zasób | Liczba |
|-------|--------|
| Szablony dokumentów | 7 941 |
| Sekcje dokumentów | 80 000+ |
| Standardy (ISO/NIST/OWASP/etc.) | 1 000+ |
| Regulacje (RODO/NIS2/KSC/AI Act/etc.) | 200+ |
| Mapowania dokument↔standard | 5 000+ |
| Mapowania dokument↔regulacja | 1 000+ |
| Krawędzie zależności (rhythm_edges) | 2 000+ |
| Linki między treściami (content_links) | 484 289 |
| Kontrakty dokumentów (inputs/outputs/gates) | 7 941 wierszy |
| Fazy cyklu życia (SDLC) | 24 |
| Wpisy RACI | per dokument |

> **Uwaga:** Biblioteka itdoc zawiera 7941 plików Markdown (7203 core + 738 satellite).
> Z nich jedynie **7205 dokumentów** jest zaindeksowanych w tabeli `documents` w `it_doc_matrix.db`
> i dostępnych dla SemanticMapper. Pozostałe ~736 szablonów satellite nie ma wpisów w DB
> i jest niedostępnych dla automatycznego mapowania w obecnym stanie bazy.

### 1.3 Możliwości API biblioteki (read-only, używane przez Warsztat)

```python
# Zapytania
find_by_standard(conn, "ISO/IEC 27001")   # → lista doc_uid + title + path
find_by_regulation(conn, "RODO")          # → lista doc_uid + title + path
get_contract(conn, doc_uid)               # → {inputs, outputs, gates, impact}
rhythm_upstream(conn, doc_uid, depth=N)   # → poprzedzające dokumenty
rhythm_downstream(conn, doc_uid, depth=N) # → następujące dokumenty
coverage_stats(conn)                      # → statystyki pokrycia
find_unmapped(conn)                       # → dokumenty bez mapowań
suggest_for_doc(conn, doc_uid)            # → sugestie powiązanych

# Walidacja
validate_schema(conn)                     # → True/False
check_link_resolution_coverage(conn)      # → % rozwiązanych linków

# Szablony
load_template(path)                       # → {frontmatter, sections, raw}
validate_template(tmpl, validators=[])    # → lista błędów
```

### 1.4 Fazy SDLC w bibliotece

```
1  Conception          9  Deployment         17 Business Continuity
2  Requirements       10  Operations         18 Governance
3  Architecture       11  Monitoring         19 Compliance
4  Design             12  Maintenance        20 Risk Management
5  Development        13  Security           21 Data Management
6  Testing/QA         14  Documentation      22 Project Management
7  Integration        15  Training           23 Decommission
8  Staging/UAT        16  Support
```

---

## 2. Luka — czego brakuje

Biblioteka `itdoc` to doskonały **magazyn wiedzy**, ale brakuje **warstwy wnioskującej od strony klienta**:

```
MAMY:                              BRAKUJE:
┌─────────────────────────┐        ┌─────────────────────────────────┐
│  7941 szablonów          │        │  Funkcja: brief → wynik         │
│  Graf zależności         │   ───► │                                 │
│  Standardy / regulacje   │  LUK   │  "Mam brief od klienta.         │
│  Fazy SDLC               │   A    │   Które z 7941 szablonów        │
│  Kontrakty (in/out/gates)│        │   są potrzebne? W jakiej        │
│  RACI                    │        │   kolejności? Ile to zajmie?    │
└─────────────────────────┘        │   Na jakiej podstawie?"         │
                                   └─────────────────────────────────┘
```

### Konkretne luki

| Luka | Obecny stan | Potrzeba |
|------|-------------|---------|
| **Intake briefów** | Brak | Parser multi-format + LLM ekstrakcja semantyczna |
| **Project instance** | Brak encji "projekt klienta" | Tabele `projects`, `briefs`, `mappings` w PostgreSQL |
| **Mapowanie brief→szablony** | Ręczne przez PM | Automatyczne z confidence score + uzasadnieniem |
| **Szacowanie nakładu** | Brak | Macierz złożoności faz × typy dokumentów |
| **Raport kosztorysowy** | Brak | Structured report z min/likely/max |
| **Work packages dla AI** | Brak | task-units z kolejnością z rhythm_edges |
| **HTTP API** | CLI + Python API tylko | REST API dla agentów AI |
| **Persystencja stanu** | Brak (stateless) | PostgreSQL dla projektów, sesji, wyników |

---

## 3. Mapa: co istnieje vs. co Warsztat buduje

### 3.1 Komponenty istniejące (NIE modyfikowane)

```
[ISTNIEJĄCE — READ-ONLY]
├── itdoc/query.py          ← Warsztat wywołuje: find_by_standard, rhythm_*, get_contract
├── itdoc/template.py       ← Warsztat wywołuje: load_template (do podglądu szablonu)
├── itdoc/db.py             ← Warsztat wywołuje: get_connection (read-only context manager)
├── it_doc_matrix.db        ← Baza wiedzy, TYLKO odczyt
└── generated_templates/    ← Szablony, TYLKO odczyt
```

### 3.2 Komponenty nowe (Warsztat)

```
[NOWE — Warsztat]
workshop/
├── api/
│   ├── main.py             ← FastAPI app factory
│   ├── routers/
│   │   ├── ingestion.py    ← Side 1: /ingestion/*
│   │   ├── brief.py        ← Side 2: /brief/*
│   │   ├── reports.py      ← Side 3: /reports/*
│   │   └── planning.py     ← Side 4: /planning/*
│   ├── services/
│   │   ├── llm_adapter.py  ← Abstrakcja LLM (Strategy)
│   │   ├── brief_parser.py ← Parser multi-format
│   │   ├── mapper.py       ← Semantic mapping engine
│   │   ├── estimator.py    ← Estimation engine
│   │   └── planner.py      ← Work planning engine
│   └── db/
│       ├── postgres.py     ← Połączenie PostgreSQL (SQLAlchemy async)
│       └── migrations/     ← Alembic migrations
├── tests/                  ← pytest, spójny z istniejącą strukturą
├── .env.example            ← Konfiguracja
├── docker-compose.yml      ← FastAPI + PostgreSQL
└── pyproject.toml          ← Zależności
```

### 3.3 Relacje między komponentami

```
                    ┌─────────────────────────────────┐
                    │         WARSZTAT (nowe)          │
                    │                                  │
  Client Brief ───► │  Side 2: Brief Mapper            │
  Spec Source  ───► │  Side 1: Ingestion               │
                    │           │                      │
                    │           ▼                      │
                    │  LLM Adapter (konfigurowalny)    │
                    │           │                      │
                    │           ▼                      │
                    │  ┌─────────────────────────┐    │
                    │  │  PostgreSQL (workshop.db)│    │
                    │  │  projects, briefs,       │    │
                    │  │  mappings, reports,      │    │
                    │  │  work_plans              │    │
                    │  └─────────────────────────┘    │
                    │           │                      │
                    │           ▼                      │
                    │  Side 3: Reports ────────────────┼──► Raport kosztorysowy
                    │  Side 4: Planner ────────────────┼──► WorkPackage JSON
                    └─────────────────────────────────┘
                                │
                                │ read-only Python API calls
                                ▼
                    ┌─────────────────────────────────┐
                    │   BIBLIOTEKA itdoc (istniejąca) │
                    │   it_doc_matrix.db (SQLite)     │
                    │   find_by_standard()            │
                    │   rhythm_upstream/downstream()  │
                    │   get_contract()                │
                    │   7941 szablonów Markdown       │
                    └─────────────────────────────────┘
```

---

## 4. Zidentyfikowane ryzyka migracji/integracji

### 4.1 Wersjonowanie biblioteki
- `it_doc_matrix.db` może być aktualizowana (nowe szablony, korekty)
- **Mitygacja:** Warsztat używa wyłącznie stabilnego API (`itdoc.*`), nie zapytań SQL bezpośrednio

### 4.2 Różnica środowisk
- Biblioteka: Python 3.9+, SQLite
- Warsztat: Python 3.11+, PostgreSQL, FastAPI
- **Mitygacja:** Docker Compose izoluje środowiska; `itdoc` jako lokalny package install

### 4.3 Stub contracts
- Tabela `contracts` w `it_doc_matrix.db` jest częściowo pusta (placeholder structure)
- **Mitygacja:** Warsztat używa `contracts` gdy dostępne, fallback na `rhythm_edges` + `phases`

### 4.4 Encoding polskich znaków
- Biblioteka ma historię problemów z mojibake w importowanych danych
- **Mitygacja:** Warsztat normalizuje tekst UTF-8 w Brief Parserze przed jakimkolwiek przetwarzaniem

---

## 5. Podsumowanie delta

| Aspekt | Przed (itdoc) | Po (itdoc + Warsztat) |
|--------|---------------|----------------------|
| Przyjmowanie briefów | ❌ brak | ✅ POST /brief/upload |
| Mapowanie brief→szablony | ❌ ręczne | ✅ automatyczne + LLM + scoring |
| Kosztorys | ❌ brak | ✅ min/likely/max + fazy |
| Plan pracy dla AI | ❌ brak | ✅ WorkPackage JSON z kolejnością |
| Ingestia nowych szablonów | ⚙️ wizard CLI | ✅ REST API + LLM |
| HTTP API | ❌ brak | ✅ FastAPI |
| Persystencja projektów | ❌ brak | ✅ PostgreSQL |
| Multi-format briefy | ❌ brak | ✅ .txt/.md/.pdf/.docx |
