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

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W0 istnieje bo dokumentacja projektowa degraduje się wraz z rozwojem systemu — pojawiają się luki (brakujące sekcje), duplikaty (ta sama informacja w dwóch dokumentach, czasem sprzeczna) i zerwane relacje (dokument A powołuje się na B, ale B nie istnieje lub nie spełnia już kontraktu). Bez automatycznego audytu te defekty są wykrywane dopiero gdy deweloper implementuje coś na podstawie niekompletnej specyfikacji — co w projekcie zarobkowym przekłada się bezpośrednio na kary umowne.

W0 musi działać PRZED każdą warstwą implementacyjną (W1–W8) **po to żeby** deweloper wiedział czy spec jest kompletna przed napisaniem linii kodu. Działa też jako warstwa monitoringu ciągłego — każda zmiana dokumentu triggeruje re-audit.

**Co się sypie bez tej warstwy:**
- Luki w specyfikacji wychodzą na jaw podczas code review lub produkcji zamiast na etapie planowania
- Duplikaty powodują rozbieżność między dokumentami bez żadnego alarmu — implementacja może podążać za złą wersją

**Zależności:**
- Wchodzi: pliki `.md`, `.txt`, `.pdf` — struktura dokumentacyjna projektu
- Wychodzi do W8: `{doc_class, validation_mode}` — tryb walidacji dla `AuditEngine`
- Wychodzi do dewelopera: `GapReport`, `DuplicateReport`, `RelationGraph`

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

### 1. Architektura
- Pokaż jak zdefiniować twarde granice modułów używając import-linter..
- Jakie są granice (boundaries) modułu doc_audit — co jest jego odpowiedzialnością a co leży poza nim?
- Jaki wzorzec projektowy najlepiej opisuje doc_audit — Facade, Strategy, czy Visitor?
- Jak doc_audit komunikuje się z pozostałymi warstwami — wywołania synchroniczne, zdarzenia, czy kolejki?
- Jakie są zależności zewnętrzne doc_audit — czy zależy od W1 (tokenizacja) czy działa na surowym tekście?
- Jak wygląda diagram komponentów doc_audit z podziałem na GapAnalyzer, DuplicateDetector, RelationMapper?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest format wejściowy dokumentu do audytu — plik tekstowy, JSON z metadanymi, czy HTTP POST z body?
- Jaki jest format wyjściowy raportu luk — JSON, Markdown, CSV, czy wszystkie trzy?
- Jak zdefiniować kontrakt dla pola confidence w raporcie duplikatu — float 0.0–1.0 czy enum (low/medium/high)?
- Jakie pola są obowiązkowe w metadanych dokumentu przekazywanego do audytu (id, tytuł, wersja, data)?
- Jak wyglądają przykładowe dane wejściowe i wyjściowe audytu w formacie JSON — pokaż schemat z polami wymaganymi?

### 3. Implementacja
- Jakie reguły ARCH-01 i SEC-01 sprawdzać w teście własnościowym?
- Jakie konkretne relacje semantyczne uwzględnić w grafie dla ARCH-01?
- Jak połączyć ontologię z regułami audytowymi dla dokumentacji?
- Jak zdefiniować twarde niezmienniki dla reguły SEC-01?
- Jak zapisać relacje przyczynowe w grafie dla reguły SEC-01?
- Jakie są najczęstsze błędy przy budowaniu ontologii dla ARCH-01?
- Zaprojektuj minimalną ontologię dla dokumentacji..
- Zaprojektuj minimalną ontologię dla analizatora dokumentacji technicznej..
- Pokaż regułę Drools dla luki w dokumentacji..
- Pokaż przykład raportu luk dla audytu dokumentacji..
- Jak zaimplementować regułę wykrywającą brak dowodów wykonania w raporcie?
- Pokaż zapytanie Cypher dla raportu luk.
- Zaimplementujmy Krok 1: regułę SPEECH_ACT do wykrywania słów należy i musi..
- Zdefiniujmy słownik pojęć sieciowych dla Kroku 2 analizy audytowej..
- Jak system rozpozna brak protokołu bezpieczeństwa w grafie komponentu sieciowego?
- Jak zmapować pojęcia techniczne na klasę komponent_sieciowy?
- Czy system obsłuży audyt warunków typu 'Jeśli API, to SSL'?

### 4. Testowanie
- Jak zaimplementować testy własnościowe dla reguł ARCH-01 i SEC-01?
- Jak zdefiniować testy własnościowe dla reguł ARCH-01?
- Jak zaimplementować testy własnościowe dla reguły ARCH-01?
- Pokaż przykład tabeli decyzyjnej dla testowania reguł SEC-01..
- Pokaż konkretny przykład testu własnościowego dla reguły ARCH-01..
- Tak, przygotuj kod testu w Hypothesis dla reguły ARCH-01..
- Stwórzmy szkielet testu hypothesis dla reguł ARCH-01 w grafie..
- Pokaż szkielet testu hypothesis dla reguł ARCH-01 i SEC-01..
- Pokaż kod testu z użyciem biblioteki hypothesis dla ARCH-01.
- Zaimplementujmy AuditEngine, aby testy ARCH-01 i SEC-01 przeszły..
- Zdefiniujmy testy dla reguł API-01 oraz DEP-01..
- Pokaż szkielet testu własnościowego ARCH-01 w bibliotece hypothesis..
- Pokaż szkielet testu ARCH-01 w bibliotece hypothesis..
- Jak napisać regułę w AuditEngine, aby zaliczyć test ARCH-01?
- Jakie reguły audytowe ARCH-01 dodać, by testy własnościowe przeszły?
- Pokaż jak zaimplementować testy architektury za pomocą import-linter..
- Pokaż przykład reguły wyłapującej brak testów integracyjnych w API..
- Jak wdrożyć regułę luki dla brakującego testu integracyjnego?
- Pokaż zapytanie Cypher wykrywające brak testów dla komponentów zewnętrznych..

### 5. Obsługa błędów
_brak pytań źródłowych w tej kategorii_
- Co zwrócić gdy dokument wejściowy jest pusty lub zawiera tylko whitespace?
- Jak logować błędy parsowania dokumentu bez ujawniania jego treści w logach systemowych?
- Jak obsłużyć przekroczenie limitu czasu audytu dla bardzo długiego dokumentu (>100 MB)?
- Co się dzieje gdy plik dokumentu jest uszkodzony (truncated) w połowie analizy?

### 6. Integracja z innymi warstwami
- Pokaż jak zaimplementować AuditEngine do obsługi tych reguł..
- Pokaż przykład reguły w silniku AuditEngine dla ARCH-01.
- Pokaż przykład reguły w silniku AuditEngine..
- Pokaż przykład reguły w silniku AuditEngine dla weryfikacji ARCH-01..
- Zintegrujmy pełny pipeline: od XML NKJP do raportu luk.

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jak uniknąć fałszywych duplikatów gdy dwa dokumenty opisują ten sam temat z różnych perspektyw (różny zakres, nie ten sam tekst)?
- Co się dzieje gdy audyt wykryje lukę w dokumencie już zaakceptowanym przez klienta — jaka jest procedura powiadomienia?
- Jak zdefiniować próg podobieństwa (threshold) shingle/Jaccard tak aby nie flagować parafrazy jako duplikatu?
- Jakie są konsekwencje błędnego oznaczenia dokumentu jako kompletny gdy brakuje sekcji — kto ponosi odpowiedzialność?
- Czy moduł audytu może operować na niespójnej wersji dokumentu przy równoległym edytowaniu (race condition)?
- Jak obsłużyć dokument w formacie binarnym (PDF, DOCX) gdy audyt oczekuje płaskiego tekstu?
- Co oznacza 0 luk dla dokumentu o złożoności 500+ zdań — czy to sygnał błędu czy rzeczywistego stanu kompletności?

## Pytania uzupełniające
- **Pułapka 3:** `completeness_score` logarytmiczny może maskować wiele małych błędów — dokument z 20 ostrzeżeniami i 0 błędami krytycznych dostanie wynik ~0.60, co wygląda jak "akceptowalny", choć nie jest.
- **Pułapka 4:** `duplicate_detector` porównuje dokumenty przez TF-IDF bez lematyzacji — "wymagania" i "wymaganie" to różne tokeny, więc duplikat może nie zostać wykryty.
- **Pułapka 5:** SQLite jako backend audytu jest single-writer — równoległe uruchomienia `doc_auditor.py` na tym samym pliku `.db` mogą prowadzić do `database is locked`.
- **Pułapka 6:** Reguły ARCH-01, SEC-01 są zdefiniowane per-projekt — bez wersjonowania zbioru reguł wyniki audytu dla tego samego dokumentu mogą być różne w różnych datach.

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
- Jak dodać tagi YAML front matter do plików Markdown projektu (format: `layer`, `title`, `status`, `tags`)?
- Jak `doc_auditor.py` waliduje obecność i poprawność YAML front matter w plikach dokumentacji?
- Jak zintegrować tagowanie YAML z `GapAnalysisGenerator` — czy YAML tagi trafiają do raportu luk?

### 4. Testowanie

- Jak napisać test własnościowy (Hypothesis) dla `gap_detector.py`, który gwarantuje, że `completeness_score ∈ [0,1]`?
- Jak przetestować regresję po zmianie progów podobieństwa — złoty wzorzec dla 10 dokumentów?
- Jak zmierzyć pokrycie mutacyjne (Mutation Score) dla W0 — jakie są minima dla projektu zarobkowego?
- Jakie testy integracyjne należy napisać dla subkomendy `doc-audit` w `compliance_check.py`?
- Jak testować wyniki audytu SQLite, żeby sprawdzić idempotentność skanowania?
#### Kompletna hierarchia TDD
- Napisz czerwony test TDD dla `GapDetector` — `detect_gaps(doc)` z brakującą sekcją → `[GapFinding(section='Wymagania', severity=HIGH)]`.
- Jak zaimplementować minimalną logikę `GapDetector` żeby przejść z fazy RED do GREEN — który warunek sprawdzać jako pierwszy?
- Jak zrefaktoryzować `GapDetector` po uzyskaniu zielonego testu — wydzielić `SectionValidator`, `RelationChecker`, `DuplicateScorer` jako osobne klasy?
- Zrefaktoryzuj `GapDetector` do strategii per-rule — każda reguła (ARCH-01, SEC-01) jako osobna klasa walidatora.
- Jak napisać test jednostkowy dla `DuplicateDetector.score_similarity()` — izolacja od zewnętrznych zależności?
- Jak zbudować oracle dataset dla W0 — 30 dokumentów z ręcznie oznaczonymi lukami, duplikatami i zerowanymi relacjami?
- Jak zapewnić że zmiana algorytmu `DuplicateDetector` nie obniży Precision poniżej 85% na corpus testowym?
- Stwórz test regresyjny dla `GapDetector` — baseline snapshot raportów luk zapisany jako golden file.
- Jak napisać test E2E: wgraj dokument SRS → przejdź przez W0 → W8 → sprawdź że `GapAnalysisReport` ma ≥ 1 naruszenie ARCH-01?

### 5. Obsługa błędów

- Co się dzieje, gdy `doc_auditor.py` napotka plik UTF-8 z niepoprawnym kodowaniem?
- Jak moduł zachowuje się, gdy baza SQLite jest zajęta (concurrent access)?
- Co zwraca `gap_detector.py` dla pustego dokumentu (0 słów)?
- Jak logować błędy parsowania bez przerywania całego skanu?
- Jakie są progi błędów, po których przekroczeniu `completeness_score = 0`?
- Jak `relation_mapper.py` obsługuje cykl w grafie relacji dokumentów (A wymaga B, B wymaga A)?
- Co się dzieje gdy plik Markdown ma niepoprawny YAML front matter (np. brakujący cudzysłów) — czy cały audyt pada czy plik jest skipowany?

### 6. Integracja z innymi warstwami

- Jak W0 będzie konsumować wyniki z W1 (tokenizacja, lematyzacja) po implementacji W1?
- Jak wyniki `relation_mapper.py` (relacje między dokumentami) zostaną przekazane do W4 (Neo4j)?
- Jak `doc_auditor.py` będzie korzystać z W3 (Słowosieć) do lepszego wykrywania synonimicznych duplikatów?
- Jak W8 (AuditEngine) rozszerza W0, nie duplikując jego funkcji?

### 7. Pułapki i ryzyka

- **Pułapka 1:** TF-IDF bez lematyzacji W1 daje fałszywe duplikaty dla fleksji polskiej (np. "testy" vs "testów") — do naprawy w W1.
- **Pułapka 2:** Progi podobieństwa (0.85/0.65/0.40) są stałe — zmiana w jednym projekcie łamie audyt innego; rozwiązanie: konfigurowalne progi per projekt.
- **Pułapka 3:** SQLite audit.db commitowany do repo ujawnia historię dokumentów — decyzja: `.gitignore` vs `audit.db` jako artefakt CI.
- **Pułapka 4:** `duplicate_detector` porównuje dokumenty przez TF-IDF bez lematyzacji — "wymagania" i "wymaganie" to różne tokeny; duplikat może nie zostać wykryty.
- **Pułapka 5:** SQLite jako backend audytu jest single-writer — równoległe uruchomienia `doc_auditor.py` na tym samym `.db` powodują `database is locked`.
- **Pułapka 6:** Reguły ARCH-01, SEC-01 są zdefiniowane per-projekt — bez wersjonowania zbioru reguł wyniki audytu dla tego samego dokumentu różnią się między datami.

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
