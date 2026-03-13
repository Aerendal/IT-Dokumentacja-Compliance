# 19 — Glossary / Słownik Pojęć

**Wersja:** 1.0  
**Status:** Draft  
**Cel:** Ujednolicone definicje terminów używanych we wszystkich spec docs (01–18).  
**Zasada:** Jeśli termin w dokumencie nie pasuje do definicji poniżej, dokument wymaga korekty.

---

## Terminy domenowe (biznesowe)

### Brief
Dokument wejściowy dostarczany przez klienta opisujący projekt do wyceny/realizacji.  
Format: PDF, DOCX lub wypełniony formularz `18_brief_template.md`.  
**Nie mylić z:** Statement of Work (SoW) — brief poprzedza SoW.

### WorkPackage / WorkPackageV2
Jednostka pracy przypisana do agenta (AI lub człowieka) reprezentująca jeden dokument do wytworzenia.  
Zawiera: `id`, `doc_uid`, `template_name`, `status`, `context` (v2).  
**Nie mylić z:** Story (Scrum), Task (Jira) — WorkPackage jest wyżej w hierarchii.

### WorkPlan
Zbiór WorkPackage'ów dla jednego zlecenia. Powiązany z jednym briefem i jednym projektem.

### MappingResult
Wynik mapowania briefu na szablony — lista dokumentów do wytworzenia z confidence score.

### EstimationReport
Raport kosztorysowy: lista dokumentów, godziny (min/likely/max), mnożnik branżowy, total.  
Status: `draft` → `accepted` → `rejected`.

### ParsedBrief
Ustrukturyzowana reprezentacja treści briefu po parsowaniu przez `BriefParser`.  
Zawiera: `project_type`, `industry`, `detected_phases`, `constraints`.

### confidence_score
Liczba 0.0–1.0 wyrażająca pewność dopasowania szablonu do briefu.  
Progi: `HIGH≥0.70` | `MEDIUM 0.50–0.69` | `LOW 0.30–0.49` | `REJECTED<0.30`  
**Canonical source:** `settings.CONFIDENCE_THRESHOLD_*` (spec17 §3.4).

### doc_uid
Unikalny identyfikator szablonu dokumentu w bibliotece itdoc.  
Format: string, np. `"audit_plan_v2"`, `"system_spec_iso29148"`.  
**Nie mylić z:** `id` (UUID WorkPackage), `project_id`.

### phase / detected_phases
Faza projektu wykryta z briefu lub przypisana do szablonu.  
Wartości: `analysis`, `design`, `implementation`, `testing`, `deployment`, `maintenance`.

---

## Terminy techniczne (systemowe)

### BriefParser
Moduł odpowiedzialny za parsowanie i ekstrakcję struktury z surowego briefu.  
Spec: `08_brief_parser_spec.md`.  
Output: `ParsedBrief`.

### SemanticMapper
Moduł mapujący `ParsedBrief` na szablony dokumentów z biblioteki itdoc.  
Spec: `09_semantic_mapper_spec.md`.  
Output: `MappingResult[]`.

### EstimationEngine
Moduł obliczający kosztorys na podstawie `MappingResult[]`.  
Spec: `10_estimation_engine_spec.md`.  
Output: `EstimationReport`.

### WorkPlanner
Moduł tworzący `WorkPlan` z `WorkPackage[]` po akceptacji kosztorysu.  
Spec: `11_work_planner_spec.md`.

### LLMAdapter
Fasada nad różnymi providerami LLM (OpenAI, Anthropic, local).  
Spec: `07_llm_adapter_spec.md`.  
**Ważne:** Wszystkie wywołania LLM muszą przechodzić przez `LLMAdapter`, nie bezpośrednio.

### ItdocConnector
Moduł komunikujący się z zewnętrzną biblioteką szablonów itdoc.  
Spec: `12_itdoc_integration_spec.md`.  
Udostępnia: listę szablonów, strukturę sekcji, standardy.

### it_doc_matrix.db
SQLite baza danych itdoc — lokalna kopia biblioteki szablonów.  
Tabele: `documents`, `document_phases`, `rhythm_edges`, `standards`, `contracts`.  
**Ważne:** `rhythm_edges` i `standards` mogą być puste — weryfikuj przed użyciem.

### mapping_results
Tabela w głównej bazie PostgreSQL przechowująca wyniki mapowania.  
Klucz: `id`, `brief_id`, `project_id`, `status`.  
Status flow: `pending` → `running` → `done` → `error`.

### llm_calls_log
Tabela logów wszystkich wywołań LLM: model, tokeny, czas, koszt, status.  
Używana do: debugowania, monitoringu kosztów, rate limiting.

### webhook_subscriptions
Tabela subskrypcji webhooków — `target_url`, `event_type`, `project_id`.  
Event types: `mapping.done`, `estimation.ready`, `package.status_changed`, `plan.ready`.

---

## Terminy procesowe (przepływ pracy)

### DisambiguationProtocol
Procedura klasyfikacji niejednoznaczności w briefie.  
Typy: `MISSING_CRITICAL`, `MISSING_OPTIONAL`, `AMBIGUOUS`, `CONFLICTING`, `BELOW_THRESHOLD`.  
Spec: `17_ai_agent_context_spec.md` §3.

### ClarificationRequest
Pytanie blokujące do klienta gdy brief zawiera `MISSING_CRITICAL`.  
Status WorkPackage przy aktywnym ClarificationRequest: `blocked`.

### QualityGate
Mierzalne kryterium ukończenia WorkPackage'u.  
Typy: `min_length`, `required_field`, `format_match`, `cross_reference`, `human_review`.  
Severity: `blocking` (blokuje `done`) | `warning` (nie blokuje).

### assumption_flag
Flaga na WorkPackage oznaczająca że AI użył wartości domyślnej zamiast danych z briefu.  
Skutek: `status = "needs_review"` (nie `"done"`).

---

## Skróty i akronimy

| Skrót | Pełna nazwa | Kontekst |
|---|---|---|
| `AC` | Acceptance Criteria | Kryteria akceptacji wymagania/story |
| `API` | Application Programming Interface | Interfejs systemu |
| `CR` | Change Request | Wymaganie zmiany |
| `DR` | Documentation Requirement | Wymaganie dokumentacyjne |
| `FR` | Functional Requirement | Wymaganie funkcjonalne |
| `IR` | Integration Requirement | Wymaganie integracji |
| `LLM` | Large Language Model | Model językowy (GPT, Claude itp.) |
| `MVP` | Minimum Viable Product | Pierwsze wydanie |
| `NFR` | Non-Functional Requirement | Wymaganie niefunkcjonalne |
| `SP` | Story Points | Jednostka estymacji w Scrum |
| `SR` | Security Requirement | Wymaganie bezpieczeństwa |
| `TR` | Technical Requirement | Wymaganie techniczne |
| `WP` | WorkPackage | Jednostka pracy |

---

## Konwencje nazewnicze

### IDs w systemie

| Kontekst | Format | Przykład |
|---|---|---|
| WorkPackage | UUID v4 | `"3fa85f64-5717-4562-b3fc-2c963f66afa6"` |
| Project | UUID v4 | jak wyżej |
| Brief | UUID v4 | jak wyżej |
| doc_uid | string kebab-case | `"audit_plan_v2"` |
| Wymaganie | `REQ-<num>` lub `<spec>-<num>` | `"REQ-042"`, `"spec05-003"` |
| Finding (audyt) | `<litera>-<num>` | `"E-01"`, `"J-06"` |

### Status values (ujednolicone)

| Obiekt | Możliwe statusy |
|---|---|
| WorkPackage | `pending`, `in_progress`, `needs_review`, `blocked`, `done` |
| Brief | `uploaded`, `parsing`, `parsed`, `mapping`, `mapped`, `error` |
| MappingResult | `pending`, `running`, `done`, `error` |
| EstimationReport | `draft`, `accepted`, `rejected` |
| Wymaganie (graf) | `active`, `archived`, `deleted` |

---

*Glossary pokrywa terminologię z spec01–spec18. Aktualizuj przy dodawaniu nowych specyfikacji.*
