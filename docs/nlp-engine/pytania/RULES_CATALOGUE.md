---
title: "Katalog reguł compliance — definicje i pokrycie pytaniami"
docs_version: 1.0.0
tags: [ARCH-01, ARCH-06, API-01, SEC-01, DEP-01, RISK-01, CONS-02, compliance-rules]
---

# Katalog reguł compliance

Każda reguła opisana jest jako:
1. **Oznajmienie** — formalna definicja (co reguła sprawdza, co jest naruszeniem, kryterium przejścia)
2. **Pytania implementacyjne** — co trzeba rozstrzygnąć przed kodowaniem
3. **Powiązane warstwy** — które pliki W_x dotyczą tej reguły

> **Uwaga:** Reguły ARCH-01 i ARCH-06 definiują *wymaganą strukturę projektu*, którą silnik audytu (W0, W8) weryfikuje.
> Reguły RISK-01 i CONS-02 to *wyniki audytu* — alarmy które silnik generuje.

---

## ARCH-01 — Pipeline jednokierunkowy

> **Uwaga:** W `ARCHITECTURE.md` istnieją dwie sekcje `[ARCH-01]` — "Pipeline" i "Komponenty — opisy".
> To jest kolizja nazw. Do rozstrzygnięcia w ADR-06 (patrz INDEX.md).
> Tymczasowo: ARCH-01a = pipeline, ARCH-01b = komponenty.

### ARCH-01a — Pipeline jednokierunkowy (przepływ danych)

**Oznajmienie:**
- Każdy dokument musi przejść przez pipeline w ściśle określonej kolejności: `ContextClassifier → NLPCore → CompliancePlugins → CrossReferenceEngine → ReportGenerator`.
- Żaden krok nie może ominąć poprzedniego. `CompliancePlugins` nie może działać bez `StateMatrix` z `NLPCore`.
- Naruszenie: komponent compliance odpytuje dokument bezpośrednio (np. regex na surowym tekście) zamiast przez `StateMatrix`.
- Kryterium przejścia: każdy `AuditFinding` zawiera `pipeline_step` wskazujący krok który go wygenerował.

**Pytania:**
- Jak wymusić kolejność pipeline w kodzie — dekorator, chain-of-responsibility, czy kolejność jawna w `run_pipeline()`?
- Jak testować że `CompliancePlugin` nie może ominąć `NLPCore` (guard w architekturze)?
- Co się dzieje gdy `NLPCore` zwróci pustą `StateMatrix` — czy `CompliancePlugins` działają na pustym grafie czy są przerywane?
- Jak mierzyć, że każdy `AuditFinding` ma pole `pipeline_step` wypełnione?
- Czy kolejność `CompliancePlugins` między sobą ma znaczenie — czy wyniki są od niej zależne?

### ARCH-01b — Komponenty muszą mieć opisy

**Oznajmienie:**
- Każdy komponent systemu (moduł Python, klasa, plugin) musi mieć opisany `Cel`, `Dane wejściowe`, `Dane wyjściowe` i `Tryb walidacji`.
- `ContextClassifier` musi klasyfikować dokumenty do jednego z enumerowanych typów: `SRS`, `TEST_PLAN`, `AUDIT_REPORT`, `SECURITY_POLICY` (+ inne per projekt).
- Naruszenie: komponent bez docstringa, bez `doc_class` lub bez zdefiniowanego `validation_mode`.
- Kryterium przejścia: `doc_auditor.py` nie raportuje żadnego `MISSING_DESCRIPTION` dla komponentów core.

**Pytania:**
- Jak `doc_auditor.py` (W0) wykrywa brakujące opisy komponentów — przez AST, docstring, czy YAML frontmatter?
- Jak rozszerzyć `DocumentClass` enum o nowe typy dokumentów bez łamania istniejących reguł?
- Jak reguła ARCH-01b różni się od reguły W0 `completeness_score` — czy to nie jest duplikat?
- Jak testować że klasyfikator dokumentów (`ContextClassifier`) poprawnie rozróżnia SRS od TEST_PLAN?
- Co reguła sprawdza dla dokumentów Markdown bez YAML frontmatter — automatyczna klasyfikacja czy błąd?

---

## ARCH-06 — Centralny model danych (StateMatrix)

**Oznajmienie:**
- `StateMatrix` jest jedynym obiektem przekazywanym między krokami pipeline. Żaden krok nie może przekazywać surowego tekstu zamiast `StateMatrix`.
- Schemat `StateMatrix` jest wersjonowany — pole `schema_version` jest obowiązkowe.
- `TokenNode` musi zawierać: `token_id`, `text`, `lemma`, `pos`, `dep_rel`, `head_id`. Pola opcjonalne: `tense`, `mood`, `negated`, `sem_role`.
- Naruszenie: `SentenceGraph.tokens` jest pustą listą dla niepustego zdania; `sem_role` zawiera wartość spoza dopuszczalnego zbioru (AGENT/PATIENT/INSTRUMENT/LOCATION/TIME).
- Kryterium przejścia: każdy `TokenNode` przechodzi walidację Pydantic bez błędów.

**Pytania:**
- Jak zapewnić że `StateMatrix` jest niemutowalna po wyjściu z `NLPCore` — `frozen=True` w Pydantic czy protokół?
- Jak migrować schemat `StateMatrix` gdy dodajemy nowe pole (np. `entity_type`) — backwards compatible?
- Jak testować że `StateMatrix` po przejściu przez `CompliancePlugins` jest identyczna jak przed (immutability)?
- Jak wersjonować `StateMatrix.schema_version` — semver czy hash schematu?
- Jak `CrossReferenceEngine` łączy `StateMatrix` z wielu dokumentów (cross-document analysis)?
- Gdzie w grafie `StateMatrix` przechowuje relacje koreferencyjne (W6) — dodatkowe pole w `TokenNode`?

**Powiązania z warstwami:**
- W1 wypełnia: `lemma`, `pos`, `dep_rel`, `head_id`, `tense`, `mood`
- W2 wypełnia: `sem_role`
- W6 rozszerza: koreferencja (wymaga decyzji ADR-02 z INDEX.md)
- W4 konsumuje: cały `StateMatrix` → ładuje do Neo4j

---

## API-01 — Interfejsy zewnętrzne

**Oznajmienie:**
- System musi eksponować dokładnie trzy endpointy REST: `POST /nlp/audit`, `GET /nlp/findings/{doc_path}`, `GET /nlp/traceability/{doc_path}`.
- `POST /nlp/audit` przyjmuje `{path: str, mode: "PRE_PRODUCTION"|"POST_EXECUTION"}` i zwraca `{findings: AuditFinding[], summary: dict}`.
- Naruszenie: endpoint zwraca inne kody statusu niż 200/400/422/500; brak pola `task_id` w odpowiedzi async.
- Kryterium przejścia: kontrakt OpenAPI/Swagger jest auto-generowany i walidowany w CI.

**Pytania:**
- Jak zintegrować nowy `nlp_router` z istniejącym `scripts/api/main.py` bez łamania obecnych endpointów?
- Jak obsługiwać `doc_path` — czy to ścieżka absolutna, względna do projektu, czy URL?
- Jak zaprojektować `AuditFinding` — jakie pola są obowiązkowe dla projektu zarobkowego (rule_id, severity, evidence)?
- Jak auto-generować i wersjonować OpenAPI spec (`openapi.json`) — czy zmiana kontraktu wymaga major version bump?
- Jak zaimplementować `GET /nlp/traceability/{doc_path}` — co zawiera `TraceabilityMatrix`?
- Jak rate-limitować `POST /nlp/audit` — per IP, per API key, per projekt?

**Powiązania z warstwami:** W7 implementuje endpointy; W0/W8 dostarcza logiki audytu.

---

## SEC-01 — Model zagrożeń

**Oznajmienie:**
- System musi mitigować cztery klasy zagrożeń:
  1. **YAML injection**: walidacja YAML frontmatter przez Pydantic przed parsowaniem — `yaml.safe_load()` + schema validation.
  2. **doc_class manipulation**: `DocumentClass` jest enumeracją — nie może zawierać wartości spoza listy.
  3. **Path traversal**: `doc_path` musi być znormalizowana i ograniczona do katalogu projektu (`pathlib.Path.resolve()` + prefix check).
  4. **Persystencja treści**: do SQLite trafiają tylko `findings` (rule_id, severity, evidence_snippet) — **nie pełna treść dokumentu**.
- Naruszenie: `doc_path` prowadzi poza katalog projektu; `DocumentClass` przyjmuje dowolny string; treść dokumentu jest logowana lub zapisywana.
- Kryterium przejścia: testy penetracyjne dla każdego z 4 zagrożeń przechodzą bez naruszeń.

**Pytania:**
- Jak napisać test automatyczny dla path traversal — czy `../../etc/passwd` jest blokowane?
- Jak testować YAML injection — jakie payloady powinny być zablokowane przez Pydantic?
- Jak zapewnić że `evidence_snippet` w `AuditFinding` nie zawiera danych osobowych (GDPR + SEC-01 łącznie)?
- Jak audytować w CI że `yaml.safe_load()` jest używane wszędzie, nie `yaml.load()`?
- Jak wersjonować listę zagrożeń SEC-01 — czy nowe zagrożenia wymagają bump wersji dokumentu?

**Powiązania z warstwami:** W7 (API) wymusza mitigacje na granicy systemu; W0 (doc audit) weryfikuje konfigurację.

---

## DEP-01 — Zarządzanie zależnościami zewnętrznymi

> **Status: NIEZDEFINIOWANE** — reguła DEP-01 jest wymieniana w pytaniach W0 (`W0_doc_audit.md`) ale **nie ma formalnej definicji w żadnym dokumencie architektonicznym**.
> Wymaga ADR-06 lub doprecyzowania przez autora projektu.

**Oznajmienie (propozycja do zatwierdzenia):**
- Każda biblioteka zewnętrzna (Morfeusz2, UDPipe, Neo4j driver, Drools) musi mieć: pinowaną wersję w `requirements.txt`/`pyproject.toml`, SHA hash w lockfile, zadeklarowany cel użycia i zadeklarowaną warstwę W_x która ją używa.
- Naruszenie: dependencja bez pinowanej wersji (`morfeusz2>=2.0` zamiast `morfeusz2==2.0.1`); biblioteka używana w wielu warstwach bez wspólnego adaptera.
- Kryterium przejścia: `pip-audit` nie zgłasza CVE dla żadnej zależności; wszystkie wersje są pinowane.

**Pytania:**
- Co dokładnie sprawdza DEP-01 — czy jest to reguła bezpieczeństwa (CVE), zgodności licencji, czy pinowania wersji?
- Jak `doc_auditor.py` (W0) miałby wykrywać naruszenia DEP-01 — przez parsowanie `requirements.txt` czy przez AST importów?
- Jak DEP-01 współgra z SEC-01 (bezpieczeństwo) — czy to podzbiór SEC-01 czy osobna reguła?
- Jak automatycznie sprawdzać licencje zależności (MIT/Apache/GPL) w CI?

---

## RISK-01 — Brak szyfrowania w komponencie sieciowym

**Oznajmienie:**
- `RISK-01` jest generowany gdy `AuditEngine` wykryje w dokumencie opis komponentu sieciowego (API, serwis webowy, transfer danych) **bez** deklaracji mechanizmu szyfrowania (TLS, HTTPS, mTLS, AES).
- Sygnały wyzwalające: słowa "API", "endpoint", "połączenie", "transfer", "port", "socket" w kontekście braku "szyfrowanie", "TLS", "HTTPS", "cert".
- Naruszenie (fałszywy alarm): zdanie opisuje API ale szyfrowanie jest zdefiniowane w innym dokumencie — `CrossReferenceEngine` musi to sprawdzić przed alarmem.
- Kryterium przejścia: Precision RISK-01 ≥ 95% (nie więcej niż 5% fałszywych alarmów na zestawie testowym).

**Pytania:**
- Jak `AuditEngine` rozróżnia "API wewnętrzne" (nie wymaga TLS) od "API zewnętrznego" (wymaga TLS)?
- Jak `CrossReferenceEngine` sprawdza czy szyfrowanie jest opisane w sąsiednim dokumencie przed generowaniem RISK-01?
- Jakie zdania z NKJP powinny **wyzwalać** RISK-01, a jakie **nie** (złoty wzorzec dla testu precision)?
- Jak kodować RISK-01 violation w JSON — `{rule_id, severity, evidence_snippet, doc_path, sentence_id}`?
- Jak aktualizować regułę RISK-01 bez reaudytowania wszystkich historycznych dokumentów?
- Jak elipsa podmiotowa ("Konfiguruje się port 8080.") bez podmiotu powinna być traktowana przez RISK-01?

**Powiązania:** W8 implementuje; W5 (silnik Drools) może zawierać regułę DRL dla RISK-01.

---

## CONS-02 — Sprzeczne opisy komponentu w dwóch dokumentach

**Oznajmienie:**
- `CONS-02` jest generowany gdy ten sam komponent (ta sama nazwa/id) ma semantycznie sprzeczne opisy w dwóch różnych dokumentach projektu.
- Przykład naruszenia: `SRS.md` mówi "moduł X szyfruje dane AES-256", a `ARCHITECTURE.md` mówi "moduł X przesyła dane plaintext".
- Sprzeczność jest semantyczna (nie leksykalna) — wymaga W3 (Słowosieć) do ustalenia antonimów i negacji.
- Naruszenie (fałszywy alarm): dwa dokumenty opisują ten sam komponent na różnych poziomach abstrakcji — CONS-02 nie powinno być wyzwalane dla różnych granularności opisu.
- Kryterium przejścia: Recall CONS-02 ≥ 80% (wykrycie ≥80% rzeczywistych sprzeczności w zestawie testowym).

**Pytania:**
- Jak system identyfikuje "ten sam komponent" w dwóch dokumentach — po nazwie, po UUID, po embeddings?
- Jak `CrossReferenceEngine` łączy dwa `StateMatrix` z różnych dokumentów do porównania?
- Jak budować zestaw testowy dla CONS-02 — jak generować pary dokumentów ze sprzecznościami?
- Jak CONS-02 zachowuje się gdy trzeci dokument rozwiązuje sprzeczność między pierwszym a drugim?
- Jak informować użytkownika o CONS-02 — wskazać oba dokumenty, oba zdania, typ sprzeczności?
- Jak wersjonować wyniki CONS-02 — czy po aktualizacji jednego dokumentu wynik dla pary zmienia się automatycznie?

**Powiązania:** W8 implementuje; W3 (Słowosieć) dostarcza synsetów dla detekcji antonimów; W4 (Neo4j) przechowuje relacje między dokumentami.

---

## Matryca pokrycia reguł w plikach W_x

| Reguła | Oznajmienie (def.) | W0 | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |
|--------|-------------------|----|----|----|----|----|----|----|----|-----|
| ARCH-01a (pipeline) | ✓ tu | ✓ | — | — | — | — | — | — | ✓ | ✓ |
| ARCH-01b (komponenty) | ✓ tu | ✓ | — | — | — | — | — | — | — | — |
| ARCH-06 (StateMatrix) | ✓ tu | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| API-01 (endpointy) | ✓ tu | — | — | — | — | — | — | — | ✓ | — |
| SEC-01 (zagrożenia) | ✓ tu | ✓ | — | — | — | — | — | — | ✓ | — |
| DEP-01 (zależności) | ⚠️ propozycja | ✓ | — | — | — | — | — | — | — | — |
| RISK-01 (brak szyfrowania) | ✓ tu | — | — | — | — | — | ✓ | — | — | ✓ |
| CONS-02 (sprzeczności) | ✓ tu | — | — | — | ✓ | ✓ | — | — | — | ✓ |

> Komórka `—` oznacza że dana warstwa nie implementuje tej reguły bezpośrednio.
> Komórka `✓` oznacza że plik W_x ma pytania lub oznajmienia dotyczące tej reguły.

---

## Otwarte decyzje dotyczące reguł

| Problem | Decyzja | Priorytet |
|---------|---------|-----------|
| ARCH-01 ma dwie sekcje w ARCHITECTURE.md — kolizja nazw | Zmienić drugą na ARCH-02 lub podzielić ARCH-01 na a/b | **Blokujący przed implementacją** |
| DEP-01 nie jest zdefiniowane | Zdefiniować zakres lub usunąć z pytań W0 | Wysoki |
| RISK-01/CONS-02 nie są w ARCHITECTURE.md | Dodać do ARCHITECTURE.md lub do tego pliku jako kanoniczne źródło | Średni |
| Brak reguł ARCH-02 do ARCH-05 | Czy numery są zarezerwowane? Luka w schemacie numeracji | Niski |
