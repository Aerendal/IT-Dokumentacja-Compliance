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
- Jakie pola YAML front matter są obowiązkowe vs. opcjonalne dla plików dokumentacji warstwy W_x (layer, title, status, tags, version)?
- Jak zwalidować że pole `layer` w YAML front matter odpowiada jednej z zdefiniowanych wartości W0–W8?
- Jak parsować YAML front matter w Pythonie (ruamel.yaml) bez modyfikowania reszty pliku Markdown?
- Jak wyeksportować tagi YAML front matter jako właściwości węzła dokumentu w grafie Neo4j?

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
- Jak zaimplementować parser YAML front matter który toleruje brakujące pola opcjonalne bez rzucania wyjątku?
- Jak zbudować walidator schema YAML front matter oparty o jsonschema lub pydantic?
- Jak otagować pliki Markdown metadanymi YAML — pokaż przykład kompletnego front matter z polami layer, title, status, tags, version?
- Jaki parser YAML front matter wybrać dla W0 — PyYAML, ruamel.yaml, czy biblioteka python-frontmatter?
- Jak automatycznie dodać brakujące YAML metadane do istniejących plików Markdown bez nadpisywania treści?
- Jak walidować obecność obowiązkowych kluczy YAML front matter w doc_auditor.py przed przetwarzaniem dokumentu?
- Jak zaimplementować metodę GapAnalysisGenerator.add_tag_metadata(yaml_tags) — które pola YAML trafiają do sekcji metadata raportu?
- Jak filtrować raport GapAnalysisGenerator po tagach YAML — np. pokaż tylko luki w dokumentach oznaczonych [ARCH-01]?
- Jak zbudować indeks dokumentów po tagach YAML dla szybkiego filtrowania w GapAnalysisGenerator?
- Dodajmy tagi [Component:] i [ARCH-01] do plików Markdown — pokaż skrypt automatycznego dodawania tagów do YAML front matter?
- Jak zdefiniować enum dozwolonych wartości dla tagu [Component:] w schemacie JSON — skąd pobierać listę komponentów?
- Jak zautomatyzować dodawanie tagu [ARCH-01] do dokumentów warstwy W_x które opisują architekturę komponentu?
- Jak walidować że tagi [Component:] w plikach Markdown są spójne z listą komponentów w ARCHITECTURE.md?
- Jak zaprojektować tagi dla różnych stylów dokumentacji — enum: FORMAL (umowy), TECHNICAL (specyfikacje), REGULATORY (regulacje) jako wartości pola `doc_style` w YAML front matter?
- Jak zaprojektować tagi dla różnych branż — pole `industry` w YAML front matter: CIVIL_LIABILITY, FINANCE, CONSTRUCTION, IT jako enum walidowany przez JSON Schema?
- Jak zbudować system wielowymiarowych tagów — kombinacja `doc_style`, `industry`, `layer` pozwala filtrować raport audytu po wielu wymiarach jednocześnie?
- Jak pole `industry` YAML łączy się z branżowymi słownikami terminologicznymi W3 — audyt dokumentu CIVIL_LIABILITY używa słownika prawniczego z `SlowosiecAdapter(domain='LEGAL')`?
- Jak dodać nowe wartości enum industry bez przebudowy walidatora — JSON Schema `$defs/Industry` z `anyOf` zamiast sztywnego enum?
- Jak automatyczny ekstraktor terminologii branżowej zasila walidator W0 — wyekstrahowane terminy → `glossary.json` wczytywany przez LinterEngine do walidacji pola `domain` w YAML front matter?
- Uruchommy walidator Markdown jako dogfooding lintera — uruchom na plikach dokumentacji własnego projektu.
- Jak skonfigurować walidator Markdown (markdownlint, pymarkdown) jako pre-commit hook w CI/CD?
- Jak walidator W0 używa własnych reguł do weryfikacji plików W_x — przykład dogfooding z wynikiem audytu?
- Jaki jest minimalny zestaw reguł markdownlint dla plików W_x — które reguły są wymagane a które opcjonalne?
- Pokaż kompletny przykład GapAnalysisReport w JSON dla dokumentu z 3 lukami, 1 duplikatem i 2 relacjami.
- Jak renderować raport luk jako Markdown z tabelą naruszeń posortowaną po severity (CRITICAL → INFO)?
- Jakie sekcje zawiera raport luk — Executive Summary, Gaps, Duplicates, Relations, Recommendations?
- Co zawiera nagłówek raportu luk — document_id, audited_at, auditor_version, total_findings, pass/fail status?
- Uruchommy skrypt audytujący wszystkie pliki Markdown w katalogu docs/ — pokaż wywołanie z argumentami ścieżki i wyjścia.
- Jak skonfigurować skrypt audytu do rekursywnego przeszukiwania podkatalogów i filtrowania plików po *.md?
- Jak uruchomić skrypt audytujący w trybie CI/CD — exit code 0 gdy 0 błędów krytycznych, exit code 1 gdy są luki?
- Jak zbatchować wyniki audytu wielu plików Markdown do jednego zbiorczego raportu JSON?
- Jak zparallelizować audyt wielu plików Markdown — multiprocessing.Pool czy async/await?
- Jak zautomatyzować przypisanie klasy dokumentu na podstawie metadanych YAML — skrypt batch który klasyfikuje per plik po polach layer/tags?
- Stwórzmy klasę DocumentClassifier do automatycznej kategoryzacji plików — jak DocumentClassifier.classify(file_path) → DocumentType?
- Jak DocumentClassifier różni się od KlasyfikatorKontekstu — DocumentClassifier operuje na pliku/metadanych, KlasyfikatorKontekstu na zawartości semantycznej?
- Jak DocumentClassifier integruje się z Linterem W0 — klasyfikacja przed audytem aby wybrać odpowiedni zestaw reguł?
- Jak DocumentClassifier jako Krok 0 zwiększa trafność audytu W0 — klasyfikacja dokumentu przed Linterem umożliwia użycie właściwego zestawu reguł per typ dokumentu?
- Jak sequencjonować Krok 0 w run_dogfooding.py — wywołaj DocumentClassifier.classify(file) przed LinterEngine.audit(file) dla każdego pliku?
- Jak zdefiniować regułę Lintera sprawdzającą autoryzację w grafie Neo4j — `LinterRule(id='AUTH-01', query="MATCH (u:User)-[:PERFORMED]->(e:EventFrame) WHERE NOT (u)-[:HAS_ROLE]->(:Role {name:'authorized'}) RETURN e")` wywoływana przez `LinterEngine.run_cypher_rule(rule, session)` i zgłaszana jako naruszenie gdy Cypher zwraca wyniki?
- Pokaż przykład reguły Lintera dla wymiaru 'Przyczyna i intencja' — `LinterRule(id='CAUSAL-INTENT-01', query="MATCH (e:EventFrame)-[:CAUSES]->(effect) WHERE NOT (e)-[:HAS_SPEECH_ACT]->(:SpeechAct) RETURN e")` wykrywa zdarzenia kauzalne bez przypisanej intencji (brak speech_act); naruszenie wskazuje że SemanticMapper nie wydobył aktu mowy dla przyczyny?
- Jakie reguły Lintera można nałożyć na graf Neo4j — katalog: AUTH-01 (brak autoryzacji aktora), CAUSAL-INTENT-01 (przyczyna bez speech_act), ORPHAN-01 (EventFrame bez krawędzi), SYNSET-01 (predykat bez :HAS_SYNSET), ROLE-01 (EventFrame bez AGENT); każda reguła to Cypher MATCH zwracający węzły naruszające warunek?
- Jak zintegrować KnowledgeGapTracker z modułem Lintera — `LinterEngine.audit(file)` po wykryciu naruszenia wywołuje `tracker.capture_unmatched_rule(rule_id=rule.id, event=frame, doc_id=file.path)`; reguły bez dopasowania w grafie trafiają do kolejki UNMATCHED_RULE w KGT jako kandydaci do nowych reguł DRL?
- Uruchommy skrypt run_dogfooding.py na oznaczonych plikach Markdown — jakie argumenty przyjmuje: --input docs/ --filter-tags [Component:W0] --output report.json?
- Jak run_dogfooding.py filtruje pliki po tagach YAML — parsuje front matter każdego *.md i sprawdza pole tags przed audytem?
- Jak run_dogfooding.py raportuje wyniki per plik — tabela: ścieżka, status (PASS/FAIL), liczba naruszeń, lista rule_id?
- Stwórzmy punkt wejścia python -m audit dla CI/CD — plik `audit/__main__.py` z funkcją main() przyjmującą --input, --output, --format {json,markdown,html}, --exit-on-failure?
- Jak `python -m audit` zwraca exit code 1 w CI/CD gdy są naruszenia BLOCKER — sys.exit(1) gdy len(blockers) > 0?
- Jak upewnić się że audit/__main__.py i endpoint /audit (FastAPI) korzystają z tej samej klasy AuditService — DRY przez wspólną warstwę logiki?

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
- Napiszmy test RED dla `ApiAuthorizationRule` w Neo4j — `def test_auth_rule_raises_on_unauthorized(): mock_session.run.return_value = [{'e': EventFrame(id='e1')}]; result = LinterEngine([LinterRule('AUTH-01', QUERY)]).audit(mock_session); assert result.violations[0].rule_id == 'AUTH-01'`; test RED bo `LinterEngine.audit()` jeszcze nie implementuje Cypher rules?
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
- Jak obsłużyć błąd kodowania znaków (nie-UTF8) w pliku dokumentu wejściowego?
- Jak obsłużyć błąd broken link w raporcie Lintera — oflagnuj, pomiń plik, czy zatrzymaj audyt?
- Jak agregować błędy Lintera per plik do zbiorczego raportu bez duplikowania wpisów?

### 6. Integracja z innymi warstwami
- Pokaż jak zaimplementować AuditEngine do obsługi tych reguł..
- Pokaż przykład reguły w silniku AuditEngine dla ARCH-01.
- Pokaż przykład reguły w silniku AuditEngine..
- Pokaż przykład reguły w silniku AuditEngine dla weryfikacji ARCH-01..
- Zintegrujmy pełny pipeline: od XML NKJP do raportu luk.
- Jak zdefiniować klasę GapAnalysisReport — pola: document_id, gaps, duplicates, relations, generated_at, severity_summary?
- Jak pipeline NKJP → GapAnalysisReport obsługuje przypadek gdy plik XML NKJP jest niekompletny lub uszkodzony?
- Jak serializować GapAnalysisReport do JSON i Markdown jednocześnie z jednej klasy modelu?
- Jak NKJPPipeline przekazuje przetworzone tokeny do GapAnalyzer który buduje instancję GapAnalysisReport?
- Jak GapAnalysisGenerator przekazuje YAML tagi do W4 (baza grafowa) jako właściwości węzłów dokumentów?
- Jak weryfikować spójność tagów YAML między dokumentami — np. czy wszystkie W_x pliki mają tag `layer`?
- Pokaż jak zintegrować Słowosieć z Linterem W0 — W0 odpytuje W3 o synonimy terminu przed flagowaniem duplikatu.
- Jak Linter W0 używa synsetów z W3 aby odróżnić synonim (ten sam sens) od homonimii (różny sens)?
- Jak skonfigurować próg podobieństwa semantycznego (Jaccard na synsetach) dla detekcji duplikatów w Linterze?
- Jak Linter W0 obsługuje przypadek gdy W3 (Słowosieć) jest niedostępne — fallback do detekcji leksykalnej?
- Zaktualizujmy GapAnalysisGenerator o zapytania Cypher dla Neo4j — jak generator pobiera dane o lukach bezpośrednio z grafu?
- Jak GapAnalysisGenerator buduje zapytanie Cypher MATCH (d:Document)-[:HAS_GAP]->(g:Gap) RETURN g per document_id?
- Jak zdefiniować kontrakt między W0 (GapAnalysisGenerator) a W4 (Neo4j) — REST API vs. neo4j-driver Python?
- Zintegrujmy audit_cli.py z automatyzacją GitHub Actions — jakie flagi CLI obsługuje: --exit-code-on-failure, --output-format json, --input docs/?
- Jak audit_cli.py przekazuje exit code do GitHub Actions — exit(1) gdy są naruszenia BLOCKER, exit(0) gdy tylko WARNING/INFO?
- Jak przechowywać raport audit_cli.py jako artefakt GitHub Actions — krok `uses: actions/upload-artifact@v4` z plikiem report.json?
- Stwórzmy gotowy plik .github/workflows/audit.yml — jakie kroki zawiera: checkout, setup-python, pip install, run audit_cli.py --exit-code-on-failure 1?
- Jak skonfigurować wyzwalacze w audit.yml — on: push (branches: [main, fresh-main]) + on: pull_request do dowolnej gałęzi?
- Jak dodać komentarz do PR z podsumowaniem raportu audit_cli.py — GitHub Actions step z `gh pr comment` parsujący wygenerowany report.json?
- Jak skonfigurować automatyczne blokowanie Pull Requestów przy błędach audytu — branch protection rule: required status check `audit / run-audit` musi przejść?
- Jak zdefiniować job name w audit.yml tak aby pasował do required status check w ustawieniach repozytorium branch protection?
- Jak zapobiec mergowaniu PR gdy audit_cli.py zwraca exit(1) — required_status_checks.strict: true w branch protection zabezpiecza przed mergem?
- Jak zbudować kompletną strukturę audit.yml — job `run-audit` z krokami: checkout@v4, setup-python@v5, pip install -r requirements.txt, python audit_cli.py --input docs/ --exit-code-on-failure 1?
- Jak parametryzować audit.yml przez workflow_dispatch inputs — manualne uruchomienie z parametrem --filter-tags dla selektywnego audytu?
- Jak cachować zależności pip w audit.yml — actions/cache@v4 z kluczem opartym na hashFiles('requirements.txt') dla szybszego CI?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jak uniknąć fałszywych duplikatów gdy dwa dokumenty opisują ten sam temat z różnych perspektyw (różny zakres, nie ten sam tekst)?
- Co się dzieje gdy audyt wykryje lukę w dokumencie już zaakceptowanym przez klienta — jaka jest procedura powiadomienia?
- Jak zdefiniować próg podobieństwa (threshold) shingle/Jaccard tak aby nie flagować parafrazy jako duplikatu?
- Jakie są konsekwencje błędnego oznaczenia dokumentu jako kompletny gdy brakuje sekcji — kto ponosi odpowiedzialność?
- Czy moduł audytu może operować na niespójnej wersji dokumentu przy równoległym edytowaniu (race condition)?
- Jak obsłużyć dokument w formacie binarnym (PDF, DOCX) gdy audyt oczekuje płaskiego tekstu?
- Co oznacza 0 luk dla dokumentu o złożoności 500+ zdań — czy to sygnał błędu czy rzeczywistego stanu kompletności?
- Jakie kategorie błędów Markdown wykrywa Linter — broken links, brak front matter, zduplikowane nagłówki, malformed code block?
- Jak sklasyfikować błędy Lintera według krytyczności — BLOCKER (brak front matter), WARNING (brakujące pole), INFO (formatowanie)?
- Jak odróżnić błąd struktury Markdown od błędu merytorycznego (brakująca sekcja) w raporcie Lintera?
- Jak obsłużyć plik Markdown który nie jest dokumentem W_x (np. README.md) — pominąć czy audytować innym zestawem reguł?

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
- Czy W0 (doc audit) może być uruchamiany niezależnie od innych warstw jako standalone narzędzie?
- Jak W0 raportuje zidentyfikowane luki do W8 (compliance audit) — zdarzenie, callback, czy polling?
- Jak aktualizacje W1 (nowe tokenizatory) wpływają na wyniki W0 — czy audyt musi być ponownie uruchomiony?

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
