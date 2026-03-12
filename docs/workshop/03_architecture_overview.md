# 03 — Architecture Overview: AI Documentation Workshop

**Status:** Draft v1.0  
**Powiązane dokumenty:** 01_vision_and_scope, 02_system_state_description, 05_module_interface_contracts, 06_openapi_specification

---

## 1. Widok C4 Poziom 1 — Kontekst systemu

```
╔══════════════════════════════════════════════════════════════════════╗
║                        KONTEKST SYSTEMU                             ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   [AI Agent / PM]                                                    ║
║        │                                                             ║
║        │ HTTP REST                                                   ║
║        ▼                                                             ║
║   ┌────────────────────────────────────────────────────────────┐    ║
║   │           AI DOCUMENTATION WORKSHOP                        │    ║
║   │           (FastAPI, Python 3.11+)                          │    ║
║   └────────────────────────────────────────────────────────────┘    ║
║        │                              │                              ║
║        │ read-only Python API         │ SQLAlchemy async             ║
║        ▼                              ▼                              ║
║   ┌──────────────────┐     ┌──────────────────────┐                ║
║   │  itdoc library   │     │  PostgreSQL           │                ║
║   │  (biblioteka     │     │  workshop.db          │                ║
║   │   istniejąca)    │     │  (stan projektów)     │                ║
║   └──────────────────┘     └──────────────────────┘                ║
║                                                                      ║
║   [LLM Provider]                                                     ║
║   OpenAI / Anthropic / Ollama (konfigurowalne przez .env)           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 2. Widok C4 Poziom 2 — Kontenery

```
┌──────────────────────────────────────────────────────────────────────┐
│                    AI DOCUMENTATION WORKSHOP                         │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    FastAPI Application                       │    │
│  │                                                              │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │    │
│  │  │ /ingestion   │  │ /brief       │  │ /reports         │  │    │
│  │  │              │  │              │  │                  │  │    │
│  │  │ Side 1       │  │ Side 2       │  │ Side 3           │  │    │
│  │  │ Template     │  │ Brief        │  │ Estimation &     │  │    │
│  │  │ Ingestion    │  │ Mapper       │  │ Report Engine    │  │    │
│  │  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘  │    │
│  │         │                 │                    │             │    │
│  │         └─────────────────┼────────────────────┘             │    │
│  │                           │                                  │    │
│  │                   ┌───────┴───────┐                          │    │
│  │                   │  /planning    │                          │    │
│  │                   │               │                          │    │
│  │                   │  Side 4       │                          │    │
│  │                   │  Work Planner │                          │    │
│  │                   └───────────────┘                          │    │
│  │                                                              │    │
│  │  ┌──────────────────────────────────────────────────────┐   │    │
│  │  │               Shared Services Layer                   │   │    │
│  │  │  ┌──────────────┐ ┌──────────────┐ ┌─────────────┐  │   │    │
│  │  │  │  LLM Adapter │ │ Brief Parser │ │  itdoc      │  │   │    │
│  │  │  │  (Strategy)  │ │ (multi-fmt)  │ │  Connector  │  │   │    │
│  │  │  └──────────────┘ └──────────────┘ └─────────────┘  │   │    │
│  │  └──────────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌──────────────────┐     ┌──────────────────────────────────────┐  │
│  │   PostgreSQL     │     │  it_doc_matrix.db (SQLite)           │  │
│  │   workshop.db    │     │  TYLKO ODCZYT przez itdoc API        │  │
│  └──────────────────┘     └──────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 3. Widok C4 Poziom 3 — Komponenty (szczegóły routerów)

### Side 1: Template Ingestion (`/ingestion`)

```
POST /ingestion/spec          ← przyjmuje spec (tekst/URL)
  │
  ├── SpecParser              ← wyciąga strukturę z oficjalnego dokumentu
  ├── LLMAdapter.extract()    ← LLM generuje szkielet szablonu
  ├── TemplateValidator       ← waliduje wg standardów itdoc (yaml frontmatter)
  └── IngestionJobRepository  ← zapisuje job + wynik w PostgreSQL

GET /ingestion/{job_id}       ← podgląd wygenerowanego szablonu
POST /ingestion/{job_id}/approve ← zatwierdza → zapisuje plik szablonu
POST /ingestion/{job_id}/reject  ← odrzuca job
```

### Side 2: Brief Mapper (`/brief`)

```
POST /brief/upload            ← wgrywa plik (.txt/.md/.pdf/.docx)
  │
  └── BriefParser.parse()     ← → ParsedBrief {text, metadata, chunks}

POST /brief/{id}/map          ← uruchamia mapowanie semantyczne
  │
  ├── LLMAdapter.extract_entities()  ← wyciąga: domeny, standardy, fazy, słowa kluczowe
  ├── itdocConnector                 ← find_by_standard, find_by_regulation, rhythm_*
  ├── ConfidenceScorer               ← Jaccard + LLM confidence → 0.0–1.0 per szablon
  └── MappingRepository              ← zapisuje MappingResult w PostgreSQL

GET /brief/{id}/mapping       ← pobiera wynik mapowania
PUT /brief/{id}/mapping/{uid} ← ręczna korekta confidence (przez P3)
```

### Side 3: Report Engine (`/reports`)

```
POST /reports/estimate/{brief_id}  ← generuje kosztorys
  │
  ├── MappingRepository.get()       ← pobiera MappingResult
  ├── EstimationEngine              ← macierz złożoności faz × typy
  ├── PhaseOrganizer                ← grupuje po 24 fazach SDLC
  └── ReportRepository              ← zapisuje EstimationReport w PostgreSQL

GET /reports/{report_id}           ← pobiera raport (JSON lub Markdown)
GET /reports/{report_id}/summary   ← skrócony widok (dla klienta)
```

### Side 4: Work Planner (`/planning`)

```
POST /planning/create/{report_id}  ← inicjuje plan pracy
  │
  ├── ReportRepository.get()        ← pobiera zatwierdzone szablony
  ├── itdocConnector.rhythm_*()     ← sekwencjonowanie z rhythm_edges
  ├── itdocConnector.get_contract() ← inputs/outputs/gates per dokument
  ├── RACIResolver                  ← mapuje role → typy AI-agentów
  └── WorkPlanRepository            ← zapisuje WorkPackage[] w PostgreSQL

GET /planning/{plan_id}/packages   ← lista task-units gotowa dla AI-agentów
GET /planning/{plan_id}/gantt      ← widok sekwencji (Markdown table / JSON)
```

---

## 4. Przepływ danych end-to-end

```
WEJŚCIE                   PRZETWARZANIE                    WYJŚCIE
──────────────────────────────────────────────────────────────────────

Brief klienta (.pdf)
      │
      ▼
[S2] BriefParser ──────► ParsedBrief
                              │
                              ▼
                   [S2] LLMAdapter.extract_entities()
                              │
                              ├─► domains: ["fintech", "cloud"]
                              ├─► standards: ["PCI DSS", "ISO 27001"]
                              ├─► phases: [3, 5, 6, 13]
                              └─► keywords: ["payment", "API", "audit"]
                                        │
                                        ▼
                   [S2] itdocConnector
                         find_by_standard("PCI DSS")     ──► 47 szablonów
                         find_by_regulation("RODO")      ──► 23 szablony
                         rhythm_downstream(root_uid, 2)  ──► 12 zależności
                                        │
                                        ▼
                   [S2] ConfidenceScorer                 ──► MappingResult
                         (Jaccard + LLM rerank)               {doc_uid, confidence,
                                        │                      reason, phase}
                                        ▼
                   [S3] EstimationEngine
                         macierz faz × złożoność         ──► EstimationReport
                                        │                     {total_h_min: 120,
                                        │                      total_h_likely: 200,
                                        │                      total_h_max: 320,
                                        │                      by_phase: [...],
                                        │                      basis: [...]}
                                        ▼
                         [Klient akceptuje]
                                        │
                                        ▼
                   [S4] WorkPlanner
                         rhythm_* + contracts + RACI     ──► WorkPackage[]
                                                              [{id, title,
                                                                inputs, outputs,
                                                                gates, assignee,
                                                                order, depends_on}]
```

---

## 5. Struktura katalogów — Warsztat

```
workshop/
├── api/
│   ├── main.py                   # App factory, CORS, middleware, health check
│   ├── routers/
│   │   ├── ingestion.py          # Side 1 router
│   │   ├── brief.py              # Side 2 router
│   │   ├── reports.py            # Side 3 router
│   │   └── planning.py           # Side 4 router
│   ├── services/
│   │   ├── llm_adapter.py        # Strategy: BaseLLMAdapter + OpenAI/Anthropic/Ollama
│   │   ├── brief_parser.py       # BriefParser: detect_format + parse_*
│   │   ├── mapper.py             # SemanticMapper: extract_entities + score
│   │   ├── estimator.py          # EstimationEngine: complexity_matrix + report
│   │   ├── planner.py            # WorkPlanner: sequence + raci_resolve
│   │   └── itdoc_connector.py    # Wrapper read-only na itdoc Python API
│   ├── models/
│   │   ├── brief.py              # ParsedBrief, MappingResult, MappingItem
│   │   ├── report.py             # EstimationReport, PhaseEstimate
│   │   ├── planning.py           # WorkPackage, WorkPlan
│   │   └── ingestion.py          # IngestionJob, IngestionSpec
│   ├── db/
│   │   ├── postgres.py           # AsyncSession factory (SQLAlchemy 2.x)
│   │   ├── models_orm.py         # SQLAlchemy ORM modele
│   │   └── migrations/           # Alembic env.py + versions/
│   └── config.py                 # Settings z pydantic-settings + .env
├── tests/
│   ├── unit/                     # Testy bez DB/LLM
│   ├── integration/              # Testy z PostgreSQL (testcontainers)
│   └── fixtures/                 # Przykładowe briefy, mock LLM responses
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

---

## 6. Zależności technologiczne

| Komponent | Technologia | Wersja |
|-----------|------------|--------|
| Framework API | FastAPI | ≥ 0.115 |
| ASGI Server | uvicorn | ≥ 0.34 |
| ORM | SQLAlchemy (async) | ≥ 2.0 |
| Migracje | Alembic | ≥ 1.14 |
| Walidacja danych | Pydantic v2 | ≥ 2.10 |
| PostgreSQL driver | asyncpg | ≥ 0.30 |
| LLM — OpenAI | openai | ≥ 1.0 |
| LLM — Anthropic | anthropic | ≥ 0.40 |
| LLM — Ollama | ollama | ≥ 0.4 |
| PDF parsing | pdfplumber | ≥ 0.11 |
| DOCX parsing | python-docx | ≥ 1.1 |
| Konfiguracja | pydantic-settings | ≥ 2.7 |
| Testy | pytest + pytest-asyncio | ≥ 9.0 |
| Konteneryzacja | Docker + Compose v2 | latest |
| itdoc (biblioteka) | itdoc (local package) | bieżąca |

---

## 7. Kluczowe decyzje architektoniczne (ADR)

### ADR-01: Read-only dostęp do itdoc
**Decyzja:** Warsztat nigdy nie pisze do `it_doc_matrix.db` ani nie modyfikuje plików szablonów.  
**Uzasadnienie:** Izolacja ryzyka; biblioteka może być aktualizowana niezależnie.  
**Konsekwencja:** Wymagany stabilny Python API `itdoc.*` jako kontrakt integracyjny.

**Wyjątek — offline maintenance:** Skrypt `populate_itdoc_db.py` (opisany w dok.16)
może wykonywać `INSERT OR IGNORE` do pustych tabel (`standards`, `contracts`, etc.)
jako jednorazowa operacja maintenance poza runtime aplikacji. Nigdy `UPDATE` ani `DELETE`.
Skrypt nie jest częścią aplikacji — uruchamiany ręcznie przez administratora.

### ADR-02: PostgreSQL zamiast SQLite
**Decyzja:** Osobna baza PostgreSQL dla stanu Warsztatu.  
**Uzasadnienie:** Multi-user readiness, ACID transactions, async support (asyncpg).  
**Konsekwencja:** Wymaga Docker Compose; dev setup jest cięższy niż SQLite.

### ADR-03: Strategy pattern dla LLM
**Decyzja:** Abstrakcja `BaseLLMAdapter` z podmiennymi implementacjami.  
**Uzasadnienie:** Unikamy lock-in na jednego dostawcę; Ollama dla środowisk bez dostępu do API.  
**Konsekwencja:** Wspólny format `LLMResponse`; prompt templates muszą być provider-agnostic.

### ADR-04: Asynchroniczny FastAPI
**Decyzja:** Pełny async stack (FastAPI + SQLAlchemy async + asyncpg).  
**Uzasadnienie:** LLM calls i DB queries mogą być długie; async pozwala obsługiwać wiele żądań równolegle.  
**Konsekwencja:** Wszystkie serwisy muszą być `async def`; synchroniczne biblioteki (itdoc) wymagają `run_in_executor`.

### ADR-05: Każdy Side = osobny router, wspólna aplikacja
**Decyzja:** 4 routery w jednej aplikacji FastAPI, nie 4 osobne procesy.  
**Uzasadnienie:** Mniejsza złożoność deployment dla v1; można rozdzielić w v2 bez zmiany API.  
**Konsekwencja:** Współdzielone zasoby (DB pool, LLM adapter); awaria jednego routera nie izoluje pozostałych.
