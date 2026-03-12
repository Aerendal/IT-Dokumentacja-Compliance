# 15 — Implementation Roadmap

**Status:** Draft v1.1 — zaktualizowano po weryfikacji stanu it_doc_matrix.db  
**Powiązane dokumenty:** Wszystkie dokumenty 01–16

---

## 1. Przegląd faz

Implementacja Warsztatu podzielona jest na **5 faz** (Faza 0 Pre-flight jest krytyczna). Każda faza kończy się działającym, testowalnym przyrostem funkcjonalności.

```
FAZA 0: Pre-flight                 FAZA 1: Fundament
────────────────────────           ────────────────────────
Weryfikacja itdoc DB +             Infrastruktura + DB +
OperationalError fix +             ItdocConnector + /health
Keyword fallback baseline
        │                                  │
        ▼                                  ▼
FAZA 2: Core Mapping               FAZA 3: Raportowanie
────────────────────────           ────────────────────────
Brief Parser + LLM Adapter +       EstimationEngine +
SemanticMapper + Side 2 API        Side 3 API + Raporty
        │                                  │
        ▼                                  ▼
FAZA 4: Planowanie & Side 1
────────────────────────────
WorkPlanner + Side 4 +
Ingestion + Side 1 API
```

---

## 1.5 Faza 0 — Pre-flight (OBOWIĄZKOWA przed Fazą 1)

### Cel fazy
Ustanowienie działającego baseline z faktycznym stanem bazy itdoc. Bez tej fazy **żadna implementacja nie daje użytecznych wyników** — SemanticMapper zwraca 0 kandydatów.

> Patrz **dok.16 Data Strategy** po szczegóły weryfikacji bazy i strategię długoterminową.

### Scope

| Zadanie | Opis | Dok. referencyjna |
|---------|------|------------------|
| Weryfikacja stanu it_doc_matrix.db | Które tabele istnieją, które są puste | dok. 02, dok. 16 |
| `CREATE VIEW document_phases` | Alias do tabeli `phases` (wymagany przez get_phases()) | dok. 16 §3.3 |
| Fix ItdocConnector error handling | catch `sqlite3.OperationalError` we wszystkich metodach | dok. 12 §3 |
| Keyword fallback w SemanticMapper | `find_by_keyword()` + phase fallback gdy wyniki puste | dok. 09 §3, dok. 12 §3.6-3.7 |
| Nowe tabele w PostgreSQL schema | `project_settings`, `audit_log`, `webhook_subscriptions`, `local_templates_index` | dok. 04 §2.12-2.15 |
| `brief.version` + `parent_brief_id` | Wersjonowanie briefów w schema | dok. 04 §2.2 |
| Zestaw testowy evaluation briefs | 10 briefów z ground truth dokumentów | dok. 14, dok. 16 §7 |
| Pomiar jakości baseline | Precision@10, recall, empty_rate | dok. 16 §7 |

### Kryteria go/no-go

- [ ] `CREATE VIEW document_phases` wykonany pomyślnie
- [ ] `ItdocConnector.find_by_standard("ISO/IEC 27001")` zwraca `[]` (NIE rzuca wyjątku)
- [ ] `ItdocConnector.find_by_keyword(["security", "policy"])` zwraca ≥ 5 wyników
- [ ] `ItdocConnector.get_phases()` zwraca 24 fazy
- [ ] SemanticMapper z keyword fallback: `total_items > 0` dla ≥ 8/10 testowych briefów
- [ ] `empty_rate < 20%` na zestawie testowym
- [ ] Startup lifespan handler z zombie recovery zaimplementowany i przetestowany

---

## 2. Faza 1 — Fundament

### Cel fazy
Działający serwer FastAPI z połączeniem do PostgreSQL i itdoc. Sprawdzony układ projektu, pipeline CI, konfiguracja Docker.

### Scope

| Komponent | Opis | Dok. referencyjna |
|-----------|------|------------------|
| Struktura projektu `workshop/` | Katalogi, pyproject.toml, Dockerfile | dok. 03 |
| Konfiguracja (`config.py`, `.env`) | pydantic-settings, walidacja sekretów | dok. 13 |
| PostgreSQL schema v1 | 11 tabel, Alembic migrations `0001_initial_schema` | dok. 04 |
| `ItdocConnector` (read-only) | Wszystkie metody + health_check | dok. 12 |
| `GET /health` | Status DB + itdoc | dok. 06 |
| `POST /projects` | Utwórz projekt | dok. 06 |
| `GET /projects` | Lista projektów | dok. 06 |
| `GET /projects/{project_id}` | Szczegóły projektu | dok. 06 |
| API Key authentication | Middleware `verify_api_key` | dok. 13 |
| Docker Compose | FastAPI + PostgreSQL + wolumen itdoc (read-only) | dok. — |
| Testy unit: ItdocConnector | ~15 testów | dok. 14 |
| Testy integration: /health, /projects | ~10 testów | dok. 14 |

### Kryteria go/no-go

- [ ] `GET /health` zwraca `{"status": "ok", "db": "ok", "itdoc": "ok"}`
- [ ] Alembic migrations przechodzą bez błędów
- [ ] `ItdocConnector.find_by_standard("ISO/IEC 27001")` zwraca niepusty wynik
- [ ] `ItdocConnector` nie ma żadnych metod zapisu (test `test_connector_is_readonly`)
- [ ] Docker Compose startuje bez błędów (`docker compose up`)
- [ ] Testy unit i integration przechodzą (0 failures)

---

## 3. Faza 2 — Core Mapping (Side 2)

### Cel fazy
Działający pipeline od wgrania briefu do `MappingResult`. To najważniejszy moduł — po Fazie 2 system jest użyteczny analitycznie.

### Scope

| Komponent | Opis | Dok. referencyjna |
|-----------|------|------------------|
| `BriefParser` | Parsowanie .txt/.md/.pdf/.docx | dok. 08 |
| `BaseLLMAdapter` + interfejs | Abstrakcja Strategy | dok. 07 |
| `OpenAIAdapter` | Implementacja OpenAI | dok. 07 |
| `AnthropicAdapter` | Implementacja Anthropic | dok. 07 |
| `OllamaAdapter` | Implementacja Ollama | dok. 07 |
| LLM Factory (`create_llm_adapter`) | Wybór dostawcy z .env | dok. 07 |
| LLM Cache (llm_calls_log) | SHA256 cache, TTL 24h | dok. 07 |
| `SemanticMapper` | Pipeline ekstrakcji → zapytania → scoring | dok. 09 |
| Normalizacja aliasów standardów | ~150 aliasów | dok. 09 |
| `POST /brief/upload` | Upload + parsowanie | dok. 06 |
| `POST /brief/{id}/map` | Uruchomienie mapowania (async) | dok. 06 |
| `GET /brief/{id}/mapping` | Pobierz wynik | dok. 06 |
| `PUT /brief/{id}/mapping/{item_id}` | Ręczna korekta | dok. 06 |
| Testy unit: Parser, Mapper, LLM Adapter | ~50 testów | dok. 14 |
| Testy integration: Side 2 API | ~15 testów | dok. 14 |

### Zależności
- ✅ Faza 1 musi być ukończona (infrastruktura, DB, ItdocConnector)

### Kryteria go/no-go

- [ ] `POST /brief/upload` akceptuje .txt, .md, .pdf, .docx — każdy format osobny test
- [ ] `ParsedBrief.text` jest zawsze UTF-8 bez null bytes
- [ ] `POST /brief/{id}/map` z mock LLM zwraca `MappingResult` z `status="done"`
- [ ] `MappingItem.confidence` ∈ [0.0, 1.0] dla wszystkich elementów
- [ ] LLM adapter podmienialny przez zmianę `LLM_PROVIDER` w .env (test fabryki)
- [ ] LLM cache działa: drugie mapowanie tego samego briefu → `response_cached=True`
- [ ] Testy unit: ≥ 80% pokrycia serwisów Parser, Mapper, LLM

---

## 4. Faza 3 — Raportowanie (Side 3)

### Cel fazy
Generowanie kosztorysu z uzasadnieniem. Po Fazie 3 system dostarcza główny produkt dla klienta — raport decyzyjny.

### Scope

| Komponent | Opis | Dok. referencyjna |
|-----------|------|------------------|
| `EstimationEngine` | Model punktów złożoności + przelicznik h | dok. 10 |
| `DOCUMENT_TYPE_POINTS` | Macierz 15 typów dokumentów | dok. 10 |
| `COMPLEXITY_MULTIPLIERS` | Mnożniki confidence, domain, required | dok. 10 |
| `PHASE_DEFAULT_CONTRACTS` | Fallback kontrakty dla 24 faz | dok. 11 |
| Klasyfikacja złożoności | low/medium/high/critical | dok. 10 |
| Budowanie `DeductionBasis` | Uzasadnienia z wagami | dok. 10 |
| `POST /reports/estimate/{brief_id}` | Generuj raport | dok. 06 |
| `GET /reports/{report_id}` | Pobierz (JSON + Markdown) | dok. 06 |
| `GET /reports/{report_id}/summary` | Skrócony widok | dok. 06 |
| `POST /reports/{report_id}/accept` | Akceptacja → odblokowanie Side 4 | dok. 06 |
| `POST /reports/{report_id}/reject` | Odrzucenie | dok. 06 |
| Testy unit: EstimationEngine | ~25 testów | dok. 14 |
| Testy integration: Side 3 API | ~10 testów | dok. 14 |

### Zależności
- ✅ Faza 2 musi być ukończona (MappingResult jako wejście)

### Kryteria go/no-go

- [ ] `total_h_min ≤ total_h_likely ≤ total_h_max` zawsze prawdziwe
- [ ] Każdy raport zawiera co najmniej 1 element w `deduction_basis`
- [ ] `by_phase` pokrywa wszystkie fazy z ≥ 1 dokumentem z mapowania
- [ ] Złożoność "critical" gdy `total_h_likely > 600`
- [ ] `status="accepted"` poprawnie odblokuje tworzenie planu (FK check)
- [ ] Markdown export czytelny i poprawnie sformatowany (manual review próbki)

---

## 5. Faza 4 — Planowanie & Ingestia (Side 4 + Side 1)

### Cel fazy
Dekompozycja zaakceptowanego raportu na task-units dla AI-agentów (Side 4) oraz interfejs do wgrywania nowych szablonów (Side 1).

### Scope

| Komponent | Opis | Dok. referencyjna |
|-----------|------|------------------|
| `WorkPlanner` | Topologiczne sortowanie + wzbogacenie o kontrakty | dok. 11 |
| `_build_dependency_graph` | rhythm_upstream → graf zależności | dok. 11 |
| `_topological_sort` | Kahn's algorithm + cycle detection | dok. 11 |
| RACI assignee resolver | Reguły przypisania ai_writer/reviewer/human | dok. 11 |
| `POST /planning/create/{report_id}` | Utwórz plan | dok. 06 |
| `GET /planning/{plan_id}` | Szczegóły planu | dok. 06 |
| `GET /planning/{plan_id}/packages` | Lista task-units (filtry: status, phase_id, assignee_type) | dok. 06 |
| `PATCH /planning/{plan_id}/packages/{id}/status` | Aktualizuj status | dok. 06 |
| `GET /planning/{plan_id}/gantt` | Widok sekwencji | dok. 06 |
| `IngestionJob` + `SpecParser` | Side 1: przyjmuje spec | dok. 06 |
| `POST /ingestion/spec` | Wgraj spec do wygenerowania szablonu | dok. 06 |
| `GET /ingestion/jobs` | Lista jobów ingestii | dok. 06 |
| `POST /ingestion/{job_id}/approve` | Zatwierdź i zapisz plik | dok. 06 |
| `POST /ingestion/{job_id}/reject` | Odrzuć job | dok. 06 |
| Testy unit: WorkPlanner | ~20 testów | dok. 14 |
| Testy unit: Ingestion | ~15 testów | dok. 14 |
| Testy E2E: pełny przepływ | 5 testów | dok. 14 |
| Testy integration: Side 4 + Side 1 API | ~15 testów | dok. 14 |

### Zależności
- ✅ Faza 3 musi być ukończona (EstimationReport jako wejście dla planowania)

### Kryteria go/no-go

- [ ] `WorkPackage.sequence_order` jest unikalny i monotonicznie rosnący
- [ ] `depends_on` nie tworzy cykli (test dla grafów z cyclami w rhythm_edges)
- [ ] `assignee_type` przypisany dla każdego pakietu (nie null)
- [ ] Test E2E `test_brief_to_work_plan` przechodzi (pełny przepływ, mock LLM)
- [ ] Zatwierdzony szablon z Side 1 zapisywany jako plik .md (nie do it_doc_matrix.db)
- [ ] `GET /planning/{plan_id}/gantt` zwraca czytelny Markdown z podziałem na fazy

---

## 6. Mapa zależności między fazami

```
FAZA 1 ──────────────────────────────────────────────┐
  Infrastruktura + DB + ItdocConnector                │
  [go/no-go] → /health OK, ItdocConnector read-only   │
                │                                     │
                ▼                                     │
FAZA 2 ─────────────────────────────────────────┐    │
  BriefParser + LLM Adapter + SemanticMapper     │    │
  [go/no-go] → MappingResult poprawny, LLM cache │    │
                │                                │    │
                ▼                                │    │
FAZA 3 ──────────────────────────────────┐       │    │
  EstimationEngine + Reports             │       │    │
  [go/no-go] → Raport z deduction_basis  │       │    │
                │                        │       │    │
                ▼                        │       │    │
FAZA 4 ──────────────────────────────────────────────┘
  WorkPlanner + Side 4 + Side 1
  [go/no-go] → E2E test przechodzi, read-only gwarantowane
```

---

## 7. Priorytety w przypadku ograniczenia zasobów

Jeśli nie wszystko z Fazy 4 może być dostarczone, priorytety:

| Priorytet | Komponent | Uzasadnienie |
|-----------|-----------|-------------|
| 🔴 MUST | **Faza 0** (Pre-flight) | Bez tego system nie daje użytecznych wyników |
| 🔴 MUST | Side 4 WorkPlanner + /planning/packages | Główny produkt dla AI-agentów |
| 🟡 SHOULD | Side 1 Ingestion + local_templates_index | Zarządzanie wiedzą |
| 🟡 SHOULD | Wersjonowanie briefów (brief.version) | Historia briefów |
| 🟡 SHOULD | Audit log + webhooks | Produkcyjne compliance |
| 🟢 COULD | /planning/gantt Markdown view | Nice-to-have dla PM |
| 🟢 COULD | Embeddings Layer (ENABLED=false → true) | Lepsza jakość mapowania |
| ⚪ WON'T (v1) | LLM Reranking | Może być dodane w v2 |
| ⚪ WON'T (v1) | Multi-tenant API keys | v2 feature |

---

## 8. Decyzje do podjęcia przed implementacją

| # | Decyzja | Opcje | Rekomendacja |
|---|---------|-------|--------------|
| D1 | Czy Side 4 działa synchronicznie czy async (background task)? | sync (prosty) / async (skalowalne) | **sync v1** — plan < 3s dla 200 dokumentów |
| D2 | Gdzie zapisywać wygenerowane szablony z Side 1? | `generated_templates/sandbox/` / osobny katalog | **`workshop/data/generated_templates/`** — izolacja od biblioteki |
| D3 | Jak obsługiwać LLM timeout podczas mapowania? | Zwróć częściowe wyniki / rzuć błąd | **Częściowe wyniki** z `status="partial"` |
| D4 | Cache LLM — przechowywać response_content czy tylko hash? | Hash tylko / pełna odpowiedź | **Pełna odpowiedź** — umożliwia replay bez LLM |
| D5 | Strategia danych itdoc — populate DB czy embeddings? | populate_itdoc_db.py / embeddings / oba | **Oba incremenalnie** — patrz dok.16 §6 |
| D6 | Embedding model — lokalny czy API? | `paraphrase-multilingual-MiniLM-L12-v2` / `text-embedding-3-small` | **Lokalny MiniLM** — bez zależności od zewnętrznego API |

---

## 9. Zależności zewnętrzne

| Zależność | Wersja minimalna | Krytyczna? | Fallback |
|-----------|-----------------|-----------|---------|
| FastAPI | ≥ 0.115 | Tak | — |
| SQLAlchemy (async) | ≥ 2.0 | Tak | — |
| PostgreSQL | ≥ 15 | Tak | — |
| pdfplumber | ≥ 0.11 | Nie | .pdf nie obsługiwane |
| python-docx | ≥ 1.1 | Nie | .docx nie obsługiwane |
| python-magic | ≥ 0.4 | Nie | Wykrywanie po rozszerzeniu |
| openai SDK | ≥ 1.0 | Warunkowa | Jeśli LLM_PROVIDER=openai |
| anthropic SDK | ≥ 0.40 | Warunkowa | Jeśli LLM_PROVIDER=anthropic |
| testcontainers | ≥ 4.0 | Tylko testy | — |
| itdoc (local) | bieżąca | Tak | — |

---

## 10. Indeks dokumentów specyfikacyjnych

| # | Dokument | Faza implementacji |
|---|----------|--------------------|
| 01 | Vision & Scope | — (pre-implementation) |
| 02 | System State Description | — (pre-implementation) |
| 03 | Architecture Overview | Faza 1 |
| 04 | PostgreSQL Data Model | Faza 0 + Faza 1 |
| 05 | Module Interface Contracts | Faza 0-4 |
| 06 | OpenAPI Specification | Faza 0-4 |
| 07 | LLM Adapter Spec | Faza 2 |
| 08 | Brief Parser Spec | Faza 2 |
| 09 | Semantic Mapper Spec | Faza 0 + Faza 2 |
| 10 | Estimation Engine Spec | Faza 3 |
| 11 | Work Planner Spec | Faza 4 |
| 12 | itdoc Integration Spec | Faza 0 + Faza 1 |
| 13 | Security & Config Spec | Faza 1 |
| 14 | Testing Strategy | Faza 0-4 |
| 15 | Implementation Roadmap | Ten dokument |
| **16** | **Data Strategy** | **Faza 0 — KRYTYCZNE** |
