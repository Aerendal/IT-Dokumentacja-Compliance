---
layer: W0
title: "Warstwa 0 — Doc Audit Module"
phase: 0
status: implemented
docs_version: 1.0.0
tags: [gap_detector, duplicate_detector, relation_mapper, doc_auditor, ARCH-01, SEC-01, linter, raport_luk]
---

# Warstwa 0 — Doc Audit Module

## Przegląd

Warstwa 0 jest **jedyną już w pełni zaimplementowaną warstwą** (`scripts/nlp/`, 8 plików, ~900 linii, 89 testów).
Pełni rolę narzędzia audytującego dokumentację projektową: wykrywa luki, duplikaty semantyczne, relacje między dokumentami i generuje raporty.

Szczegółowa dokumentacja implementacji: [`DOC_AUDIT_MODULE.md`](../DOC_AUDIT_MODULE.md)

## Diagram przepływu danych

```
Pliki .md / .txt
       │
       ▼
  text_utils.py           ← normalizacja PL, stemming, shingles
       │
       ▼
  similarity_engine.py    ← TF-IDF + cosine (stdlib)
       │
  ┌────┴────┐
  ▼         ▼
gap_detector  duplicate_detector  relation_mapper
  │                    │                │
  └────────────────────┴────────────────┘
                        │
                        ▼
               doc_auditor.py (orchestrator)
                        │
                   SQLite (ddl_audit.sql)
                        │
                   CLI: scan / report / list-runs
```

## Pytania źródłowe — sklasyfikowane


### Architektura, reguły i integracja (z tur 1–4)

- Jak zaimplementować testy własnościowe dla reguł ARCH-01 i SEC-01?
- Jak zdefiniować testy własnościowe dla reguł ARCH-01?
- Jakie reguły ARCH-01 i SEC-01 sprawdzać w teście własnościowym?
- Jakie konkretne relacje semantyczne uwzględnić w grafie dla ARCH-01?
- Jak zaimplementować testy własnościowe dla reguły ARCH-01?
- Pokaż przykład tabeli decyzyjnej dla testowania reguł SEC-01..
- Pokaż konkretny przykład testu własnościowego dla reguły ARCH-01..
- Jak połączyć ontologię z regułami audytowymi dla dokumentacji?
- Tak, przygotuj kod testu w Hypothesis dla reguły ARCH-01..
- Stwórzmy szkielet testu hypothesis dla reguł ARCH-01 w grafie..
- Pokaż szkielet testu hypothesis dla reguł ARCH-01 i SEC-01..
- Pokaż kod testu z użyciem biblioteki hypothesis dla ARCH-01.
- Jak zdefiniować twarde niezmienniki dla reguły SEC-01?
- Zaimplementujmy AuditEngine, aby testy ARCH-01 i SEC-01 przeszły..
- Zdefiniujmy testy dla reguł API-01 oraz DEP-01..
- Pokaż jak zaimplementować AuditEngine do obsługi tych reguł..
- Jak zapisać relacje przyczynowe w grafie dla reguły SEC-01?
- Jakie są najczęstsze błędy przy budowaniu ontologii dla ARCH-01?
- Pokaż szkielet testu własnościowego ARCH-01 w bibliotece hypothesis..
- Pokaż szkielet testu ARCH-01 w bibliotece hypothesis..
- Pokaż przykład reguły w silniku AuditEngine dla ARCH-01.
- Jak napisać regułę w AuditEngine, aby zaliczyć test ARCH-01?
- Jakie reguły audytowe ARCH-01 dodać, by testy własnościowe przeszły?
- Pokaż przykład reguły w silniku AuditEngine..
- Zaprojektuj minimalną ontologię dla dokumentacji..
- Pokaż przykład reguły w silniku AuditEngine dla weryfikacji ARCH-01..
- Zaprojektuj minimalną ontologię dla analizatora dokumentacji technicznej..
- Pokaż jak zaimplementować testy architektury za pomocą import-linter..
- Pokaż przykład reguły wyłapującej brak testów integracyjnych w API..
- Jak wdrożyć regułę luki dla brakującego testu integracyjnego?
- Pokaż jak zdefiniować twarde granice modułów używając import-linter..
- Pokaż zapytanie Cypher wykrywające brak testów dla komponentów zewnętrznych..
- Pokaż regułę Drools dla luki w dokumentacji..
- Pokaż przykład raportu luk dla audytu dokumentacji..
- Jak zaimplementować regułę wykrywającą brak dowodów wykonania w raporcie?
- Pokaż zapytanie Cypher dla raportu luk.
- Zaimplementujmy Krok 1: regułę SPEECH_ACT do wykrywania słów należy i musi..
- Zdefiniujmy słownik pojęć sieciowych dla Kroku 2 analizy audytowej..
- Jak system rozpozna brak protokołu bezpieczeństwa w grafie komponentu sieciowego?
- Jak zmapować pojęcia techniczne na klasę komponent_sieciowy?
- Czy system obsłuży audyt warunków typu 'Jeśli API, to SSL'?
- Zintegrujmy pełny pipeline: od XML NKJP do raportu luk.

## Pytania uzupełniające

### 1. Architektura

- Jak `doc_auditor.py` dzieli odpowiedzialność z resztą projektu — co jest w `scripts/nlp/`, a co w `scripts/compliance_check.py`?
- Czy `DocAuditor` powinien działać jako serwis ciągły (daemon) czy wywoływany każdorazowo z CLI?
- Jak zdefiniować granicę modułu W0 wobec W8 (AuditEngine)? Co należy do W0, a co do W8?
- Jakie są niezmienniki architektury, których W0 nie może naruszać (import-linter)?
- Jak rozbudować `doc_auditor.py` o obsługę wielojęzycznych dokumentów?

### 2. Kontrakty danych

- Jaki jest dokładny schemat JSON wyjścia z `gap_detector.py` — które pola są obowiązkowe?
- Jak zdefiniować formalny schemat JSON Schema dla wyników audytu (gaps, duplicates, relations)?
- Jaka jest struktura rekordu SQLite w tabeli `audit_runs` i `gaps`?
- Jak kontrakt danych między `similarity_engine.py` a `duplicate_detector.py` jest zawarty w typach Pythona?
- Jakie formaty wejściowe W0 akceptuje (.md, .txt, .rst, .adoc)?

### 3. Implementacja

- Jak rozbudować `gap_detector.py` o nowe typy dokumentów (poza 9 istniejącymi szablonami)?
- Jak dostroić progi podobieństwa w `duplicate_detector.py` (exact/extending/thematic/partial)?
- Jak zaimplementować regułę ARCH-01 i SEC-01 jako formalne predykaty w `doc_auditor.py`?
- Jak dodać obsługę reguły API-01 i DEP-01 do istniejącego schematu SQLite?
- Jak rozbudować `relation_mapper.py` o relację `contradicts` (wykrywanie sprzeczności)?

### 4. Testowanie

- Jak napisać test własnościowy (Hypothesis) dla `gap_detector.py`, który gwarantuje, że `completeness_score ∈ [0,1]`?
- Jak przetestować regresję po zmianie progów podobieństwa — złoty wzorzec dla 10 dokumentów?
- Jak zmierzyć pokrycie mutacyjne (Mutation Score) dla W0 — jakie są minima dla projektu zarobkowego?
- Jakie testy integracyjne należy napisać dla subkomendy `doc-audit` w `compliance_check.py`?
- Jak testować wyniki audytu SQLite, żeby sprawdzić idempotentność skanowania?

### 5. Obsługa błędów

- Co się dzieje, gdy `doc_auditor.py` napotka plik UTF-8 z niepoprawnym kodowaniem?
- Jak moduł zachowuje się, gdy baza SQLite jest zajęta (concurrent access)?
- Co zwraca `gap_detector.py` dla pustego dokumentu (0 słów)?
- Jak logować błędy parsowania bez przerywania całego skanu?
- Jakie są progi błędów, po których przekroczeniu `completeness_score = 0`?

### 6. Integracja z innymi warstwami

- Jak W0 będzie konsumować wyniki z W1 (tokenizacja, lematyzacja) po implementacji W1?
- Jak wyniki `relation_mapper.py` (relacje między dokumentami) zostaną przekazane do W4 (Neo4j)?
- Jak `doc_auditor.py` będzie korzystać z W3 (Słowosieć) do lepszego wykrywania synonimicznych duplikatów?
- Jak W8 (AuditEngine) rozszerza W0, nie duplikując jego funkcji?

### 7. Pułapki i ryzyka

- **Pułapka 1:** TF-IDF bez lematyzacji W1 daje fałszywe duplikaty dla fleksji polskiej (np. "testy" vs "testów") — do naprawy w W1.
- **Pułapka 2:** Progi podobieństwa (0.85/0.65/0.40) są stałe — zmiana w jednym projekcie łamie audyt innego; rozwiązanie: konfigurowalne progi per projekt.
- **Pułapka 3:** SQLite audit.db commitowany do repo ujawnia historię dokumentów — decyzja: `.gitignore` vs `audit.db` jako artefakt CI.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Completeness Score dla wzorcowego doc-zestawu 10 plików | ≥ 0.7 |
| False Positive Rate dla duplikatów | ≤ 5% |
| Czas skanowania 50 plików .md | < 5 s |
| Mutation Score (testy jednostkowe) | ≥ 60% |
| Pokrycie testów linii | ≥ 90% |

## Pytania o idempotentność i deterministyczność

- Czy `doc_auditor.py scan` na tych samych plikach dwukrotnie daje identyczny wynik w SQLite?
- Czy `similarity_engine.py` daje identyczny cosine score dla identycznych wejść niezależnie od kolejności wywołań?
- Jak zapewnić, że zmiana kolejności plików wejściowych nie zmienia wyników?

## Pytania o migrację i wersjonowanie

- Jak migrować schemat SQLite (`ddl_audit.sql`) po dodaniu nowej kolumny bez utraty historii audytów?
- Jak wersjonować szablony gap-detektora, gdy zmienia się standard dokumentacji projektu?
- Jak obsłużyć backwards-compatibility dla CLI `doc-audit`, gdy dodajemy nowe flagi?

## Pytania o audytowalność

- Jak każde wykrycie luki jest powiązane z konkretnym plikiem, linią i regułą w SQLite?
- Jak wygenerować raport "dlaczego dokument X dostał score 0.6?" z szczegółowym uzasadnieniem?
- Jak przechowywać historię audytów (który commit = jaki wynik) dla celów dowodowych?

---

## Rozszerzalność i skalowanie

### Stopniowe rozszerzanie analizy dokumentów

- Jak W0 obsługuje dokumenty w nowych formatach (DOCX, PDF, RST) bez zmiany kontraktu `AuditResult`?
- Jak dodać nową regułę audytu (np. wykrywanie duplikatów między plikami) bez modyfikacji istniejących reguł?
- Jak skalować W0 do analizy repo z 1000+ plikami — limit czasu, paginacja, cache wyników?
- Jak testować, że dodanie nowej reguły nie zmienia wyników dla dokumentów niepodlegających tej regule?
- Jak wersjonować zbiór reguł audytu — żeby wynik z reguła v1.0 i v1.1 był porównywalny historycznie?
- Jak W0 obsługuje dokumenty wielojęzyczne gdy W1 (Morfeusz) jest dostępny tylko dla polskiego?
