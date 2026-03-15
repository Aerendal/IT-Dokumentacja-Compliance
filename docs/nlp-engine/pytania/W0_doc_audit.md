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
- Zaimplementujmy Silnik Reguł Lintera jako moduł — `class LinterRuleEngine: def __init__(self, rules: List[LinterRule], session): self._rules = rules; self._session = session` + metoda `run_all() → List[Violation]` iteruje `self._rules`, wywołuje `run_cypher_rule(rule)` dla każdej i zbiera naruszenia do jednej listy `[Violation(rule_id, node_id) for row in result]`?
- Zaprojektujmy regułę Lintera wykrywającą brak autoryzacji w API — reguła AUTH-01 rozszerzona o sprawdzenie wywołań API: `LinterRule(id='API-AUTH-01', query="MATCH (e:EventFrame {domain:'API'})-[:PERFORMED_BY]->(a:Actor) WHERE NOT (a)-[:HAS_TOKEN]->(:AuthToken {valid:True}) RETURN e, a")`; naruszenie = EventFrame API bez aktora z ważnym tokenem; uzupełnia AUTH-01 (Neo4j roles) o wymiar API-level?
- Pokaż wdrożenie `ApiAuthorizationRule` w fazie Green — `class ApiAuthorizationRule(LinterRule): query = "MATCH (e:EventFrame {domain:'API'}) WHERE NOT (e)-[:AUTHORIZED_BY]->(:AuthToken) RETURN e"`; `run_cypher_rule(self, session)` → `[Violation('API-AUTH-01', row['e']['id']) for row in session.run(self.query)]`; test GREEN: mock zwraca 0 wyników → `violations == []`?
- Zdefiniujmy regułę Lintera dla procedur w grafie — `LinterRule(id='PROC-01', query="MATCH (e:EventFrame {domain:'PROCEDURE'}) WHERE NOT (e)-[:HAS_ROLE {role:'RESPONSIBLE_PARTY'}]->(:Actor) RETURN e")`; wykrywa procedury bez przypisanej strony odpowiedzialnej; analogia do ROLE-01 (brak AGENT) ale ograniczona do węzłów `domain='PROCEDURE'`?
- Jak zintegrować `CauseAndIntentionRule` z nowym modelem relacji Neo4j — `class CauseAndIntentionRule(LinterRule): id='CAUSAL-INTENT-01'`; `query = "MATCH (e:EventFrame)-[:CAUSES]->(eff) WHERE NOT (e)-[:HAS_SPEECH_ACT]->(:SpeechAct) RETURN e"`; nowość: rozszerzyć o `AND NOT (e)-[:HAS_ROLE {role:'AGENT'}]->()` żeby filtrować tylko zdarzenia z kompletnym modelem; integracja z `LinterRuleEngine.run_all()` → `Violation(rule_id, node_id)`?
- Pokaż regułę `ApiAuthorizationRule` wykrywającą luki w grafie Neo4j — poza podstawowym `AUTHORIZED_BY` dodaj detekcję luk: `query = "MATCH (e:EventFrame {domain:'API'}) WHERE NOT (e)-[:AUTHORIZED_BY]->(:AuthToken) OR (e)-[:AUTHORIZED_BY]->(:AuthToken {expired:True}) RETURN e"`; reguła wykrywa oba warianty luki: brak tokenu I wygasły token w jednym MATCH?
- Jak przetestować `ApiAuthorizationRule` na grafie z mieszanymi tokenami — `def test_api_auth_detects_expired_token(): mock_session.run.return_value=[{'e':{'id':'e_expired'}}]; rule = ApiAuthorizationRule(); violations = rule.run_cypher_rule(mock_session); assert violations[0].node_id == 'e_expired'`; scenariusz: token istnieje ale `expired:True` — reguła musi zwrócić naruszenie jak przy braku tokenu?
- Jak zdefiniować regułę `SEC-01` dotyczącą modelu zagrożeń w grafie — `LinterRule(id='SEC-01', query="MATCH (e:EventFrame {domain:'API'}) WHERE NOT (e)-[:HAS_THREAT_MODEL]->(:ThreatModel) RETURN e")`; węzeł `:ThreatModel {stride: ['SPOOFING','TAMPERING'], mitigated: True}` połączony z EventFrame; naruszenie SEC-01 = brak przypisanego modelu zagrożeń do zdarzenia API?
- Pokaż pełną implementację reguły `SEC-01` w grafie — `class SEC01Rule(LinterRule): id='SEC-01'; query=SEC01_QUERY; def run_cypher_rule(self, session): rows=session.run(self.query); return [Violation('SEC-01', r['e']['id'], severity='HIGH') for r in rows]`; `Violation` ma dodatkowe pole `severity` dla priorytetyzacji w raporcie bezpieczeństwa; SEC-01 zawsze `severity='HIGH'`?
- Jakie reguły Cypher dodać do audytu bezpieczeństwa — poza AUTH-01/API-AUTH-01/SEC-01 dodaj: PRIV-01 (`MATCH (a:Actor)-[:PERFORMED]->(e:EventFrame) WHERE a.privilege_level < e.required_privilege RETURN a, e`); DATA-01 (`MATCH (e:EventFrame)-[:PROCESSES]->(:DataAsset {sensitivity:'CONFIDENTIAL'}) WHERE NOT (e)-[:HAS_ENCRYPTION]->() RETURN e`); łącznie 5 reguł bezpieczeństwa w katalogu?
- Jak sformatować raport luk w formacie TEI P5 — TEI P5 (Text Encoding Initiative) to XML dla dokumentów humanistycznych; dla dokumentacji technicznej: `<div type='audit-report'><list type='violations'><item n='AUTH-01'><ref target='#frame_e1'>brak autoryzacji</ref></item></list></div>`; `AuditReportGenerator.generate_tei()` generuje XML zatwierdzony przez `xmlschema` z TEI-all.xsd?
- Wdrożmy `AuditReportGenerator` w fazie Green z CSV — dodaj `generate_csv()`: `import csv; writer = csv.DictWriter(f, fieldnames=['rule_id','node_id','severity'])`; każdy `Violation` jako wiersz; `generate()` dispatch na format: `{'json': generate_json, 'md': generate_markdown, 'csv': generate_csv, 'tei': generate_tei}[fmt](violations, kgt)`?
- Jak rozszerzyć SEC-01 o weryfikację mitygacji — `query = "MATCH (e:EventFrame {domain:'API'})-[:HAS_THREAT_MODEL]->(t:ThreatModel) WHERE t.mitigated=False RETURN e, t.stride"`; SEC-01b wykrywa modele zagrożeń istniejące ale **niezmitigowane**; `Violation` zawiera `details={'unmitigated_stride': t.stride}` — informacja dla inżyniera bezpieczeństwa?
- Jak zintegrować `IntentClassifier` z raportem audytowym — po uruchomieniu `LinterRuleEngine.run_all()` uzupełnij `AuditReport` o pole `intent_stats: Counter({'REQUIREMENT': n, 'ASSERT': m, 'QUESTION': k})`; `AuditReport.generate()` filtruje naruszenia `REQUIREMENT` gdzie brak `AUTH_ROLE` i wypisuje jako sekcję "Wymagania bez autoryzacji" w JSON/Markdown?
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
- Napiszmy test RED dla Silnika Reguł Lintera jako całości — `def test_rule_engine_runs_all_rules(): engine = LinterRuleEngine([ORPHAN_RULE, AUTH_RULE], mock_session); violations = engine.run_all(); assert len(violations) == 2 and {v.rule_id for v in violations} == {'ORPHAN-01','AUTH-01'}`; test RED bo `run_all()` niezaimplementowane?
- Pokaż testy RED dla `LinterRuleEngine` z warunkami brzegowymi — `def test_run_all_returns_empty_when_no_violations(): mock_session.run.return_value = []; violations = LinterRuleEngine([AUTH_RULE], mock_session).run_all(); assert violations == []`; osobny RED: `def test_run_all_aggregates_from_multiple_rules(): mock_session.run.side_effect=[[row1],[row2]]; assert len(LinterRuleEngine([R1,R2], mock_session).run_all()) == 2`?
- Pokażmy czerwoną fazę testu dla Silnika Reguł Lintera — `def test_rules_engine_violation_includes_rule_id(): mock_session.run.return_value=[{'e':{'id':'e99'}}]; engine = LinterRuleEngine([CAUSAL_INTENT_RULE], mock_session); v = engine.run_all()[0]; assert v.rule_id == 'CAUSAL-INTENT-01' and v.node_id == 'e99'`; test RED bo `Violation.rule_id` i `Violation.node_id` niezdefiniowane na dataclass?
- Stwórzmy test RED dla `LinterRuleEngine` (RulesEngine) — `def test_engine_raises_on_invalid_cypher(): engine = LinterRuleEngine([LinterRule('BAD-01', 'NOT VALID CYPHER')], mock_session); mock_session.run.side_effect = CypherSyntaxError('Invalid'); with pytest.raises(LinterRuleError, match='BAD-01'): engine.run_all()`; test RED sprawdza czy silnik opakowuje błędy Cypher w `LinterRuleError` z rule_id?
- Napiszmy czerwony test dla `AuditReportGenerator` — `def test_report_contains_violations_section(): gen = AuditReportGenerator(); report = gen.generate(violations=[Violation('AUTH-01','e1')]); assert 'AUTH-01' in report['violations'] and report['summary']['total'] == 1`; test RED bo `AuditReportGenerator` i `report['violations']` niezaimplementowane?
- Napiszmy RED test `AuditReportGenerator` dla fazy Refactor — `def test_report_serializes_to_markdown(): gen = AuditReportGenerator(); md = gen.generate_markdown(violations=[Violation('AUTH-01','e1')], kgt=None); assert '| AUTH-01 |' in md and '## Raport audytowy' in md`; test RED przed dodaniem `generate_markdown()` do klasy?
- Zbudujmy test dla `CrossReferenceEngine` sprawdzający błędy kaskadowe — `def test_cascade_violation_propagates(): engine = CrossReferenceEngine([doc_A, doc_B]); doc_A_violation = Violation('SEC-01','api_frame'); violations = engine.check_cascade(doc_A_violation); assert any(v.source_doc == 'doc_B' for v in violations)`; naruszenie SEC-01 w doc_A propaguje do wszystkich dokumentów odwołujących się do tego samego węzła?
- Zdefiniujmy RED test dla `CrossReferenceEngine` (Silnik Zależności) bez kaskady — `def test_cross_ref_no_cascade_when_isolated(): engine = CrossReferenceEngine([doc_A, doc_B_isolated]); violations = engine.check_cascade(Violation('AUTH-01','node_x')); assert violations == []`; doc_B nie odwołuje się do `node_x` → brak propagacji; RED bo `check_cascade()` jeszcze nie sprawdza izolacji węzła?
- Dodajmy test RED dla reguły `SEC-01` dotyczącej modelu zagrożeń — `def test_sec01_raises_when_no_threat_model(): mock_session.run.return_value=[{'e':{'id':'api_e1'}}]; rule = LinterRule('SEC-01', SEC01_QUERY); violations = rule.run_cypher_rule(mock_session); assert violations[0].rule_id == 'SEC-01' and violations[0].node_id == 'api_e1'`; test RED przed implementacją `run_cypher_rule()`?
- Jak naprawić `ModuleNotFoundError` w testach `AuditReportGenerator` — błąd `ModuleNotFoundError: No module named 'audit_report_generator'` wskazuje brak `__init__.py` lub błędną ścieżkę importu; fix: dodaj `from compliance.audit.report_generator import AuditReportGenerator` lub upewnij się że `src/` jest w `PYTHONPATH`; wzorzec: `conftest.py` z `sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))`?
- Jak zaimplementować `AuditReportGenerator` w fazie Green — minimalna klasa: `class AuditReportGenerator: def __init__(self, kgt=None): self._kgt=kgt; def generate(self, violations): return {'violations': {v.rule_id: v.node_id for v in violations}, 'knowledge_gaps': [{'word':g.word} for g in self._kgt.get_ign_gaps()] if self._kgt else [], 'summary': {'total': len(violations)}}`; oba testy RED z B38 przechodzą?
- Jak połączyć błędy z Neo4j i `KnowledgeGapTracker` w jednym raporcie — `AuditReportGenerator.generate(violations=neo4j_violations, session=neo4j_session)` wewnętrznie: 1) `linter.run_all(session)` → `violations`; 2) `kgt.dump_jsonl()` → `knowledge_gaps`; 3) merge: `{'violations': [...], 'knowledge_gaps': [...], 'summary': {'neo4j_violations': N, 'kgt_gaps': M}}`; jednorodny JSON dla downstream raportowania?
- Wdrożmy `AuditReportGenerator` z serializacją — dodaj `generate_markdown(violations, kgt)`: nagłówek `## Raport audytowy`; sekcja `### Naruszenia` tabela `| rule_id | node_id |`; sekcja `### Luki wiedzy` tabela `| słowo | count |`; `generate_json()` jako alias do `generate()`; interfejs zgodny z `run_dogfooding.py --output report.md`?
- Jakie formaty raportów powinien obsługiwać `AuditReportGenerator` — minimum: JSON (`generate_json()`), Markdown (`generate_markdown()`); opcjonalnie CSV (`generate_csv()`) dla import do Excela/JIRA; wybór formatu przez `--output-format {json,md,csv}` w `run_dogfooding.py`; każdy format jako osobna strategia (Strategy pattern) niezależnie testowalna?
- Jak zintegrować wyniki `KnowledgeGapTracker` w końcowym raporcie — `kgt.get_summary()` zwraca `{'total_gaps': N, 'top_missing': [('słowo', count), ...], 'by_type': {'MISSING_SYNSET': n, 'UNMATCHED_RULE': m}}`; `AuditReportGenerator` embeduje `summary` KGT jako sekcję `### Podsumowanie luk` w końcowym raporcie; umożliwia priorytetyzację prac nad uzupełnieniem wiedzy?
- Stwórz RED test integracji `KnowledgeGapTracker` z `AuditReportGenerator` — `def test_kgt_gaps_appear_in_audit_report(): kgt = KnowledgeGapTracker(); kgt.capture_ign('kompilacja', context=['doc_A']); gen = AuditReportGenerator(kgt=kgt); report = gen.generate(violations=[]); assert report['knowledge_gaps'][0]['word'] == 'kompilacja'`; test RED bo `AuditReportGenerator(kgt=...)` nie przyjmuje KGT?
- Jak przetestować że `AuditReportGenerator` sortuje luki KGT po częstości — `def test_kgt_gaps_sorted_by_frequency(): kgt = KnowledgeGapTracker(); [kgt.capture_ign('API', context=[f'd{i}']) for i in range(3)]; kgt.capture_ign('moduł', context=['d0']); report = AuditReportGenerator(kgt=kgt).generate(violations=[]); assert report['knowledge_gaps'][0]['word'] == 'API'`; sortowanie `by=count desc` priorytetyzuje luki do uzupełnienia?
- Pokaż czerwony test dla `ApiAuthorizationRule` krok po kroku — `@pytest.fixture def unauth_session(): s = Mock(); s.run.return_value=[{'e':{'id':'frame_1'}}]; return s`; `def test_api_auth_unauthorized(unauth_session): rule = ApiAuthorizationRule(); violations = rule.run_cypher_rule(unauth_session); assert violations == [Violation('API-AUTH-01','frame_1')]`; RED bo `ApiAuthorizationRule` niezaimplementowane?
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
- Jak `LinterRuleEngine` wykrywa błędy kaskadowe przy braku backupu — reguła `BACKUP-01` (`MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP]->(:BackupPolicy) RETURN db`) uruchamia `CrossReferenceEngine.check_cascade(violation)` i zbiera wszystkie dokumenty referujące `db`; błąd kaskadowy = każdy dokument opisujący odtwarzanie bez potwierdzenia polityki backupu; `Violation(rule_id='BACKUP-01', node_id=db_id, severity='CRITICAL')`?
- Jak `CrossReferenceEngine` wykrywa konflikty między regułami — dwie reguły `r1, r2` są w konflikcie gdy ich Cypher MATCH pokrywa ten sam węzeł i generują sprzeczne `Violation.severity`: `class RuleConflict(NamedTuple): rule_a, rule_b, node_id, conflict_type`; `conflict_type ∈ {'DOUBLE_VIOLATION', 'SEVERITY_MISMATCH', 'MUTUAL_EXCLUSION'}`; `CrossReferenceEngine.detect_conflicts(violations_a, violations_b)→List[RuleConflict]`?
- Jak wdrożyć regułę SEC-01 w grafie Neo4j krok po kroku — (1) `MERGE (:ThreatModel {id:'tm_api', stride:['SPOOFING'], mitigated:True})` tworzy węzeł; (2) `MATCH (e:EventFrame {domain:'API'}) MERGE (e)-[:HAS_THREAT_MODEL]->(tm)` tworzy krawędź; (3) `SEC01Rule.run_cypher_rule(session)` wyszukuje EventFrame bez tej krawędzi; (4) wynik: `Violation('SEC-01', e_id, severity='HIGH')`; `:ThreatModel` bez pola `mitigated` domyślnie traktowany jako `mitigated=False` → naruszenie SEC-01b?
- Zaimplementujmy regułę `SEC-01` jako klasę — `class SEC01Rule(LinterRule): id='SEC-01'; QUERY = "MATCH (e:EventFrame {domain:'API'}) WHERE NOT (e)-[:HAS_THREAT_MODEL]->(:ThreatModel) RETURN e.id AS node_id"; def run_cypher_rule(self, session): return [Violation(self.id, row['node_id'], severity='HIGH') for row in session.run(self.QUERY)]`; klasa dziedziczy po `LinterRule` z metodą abstrakcyjną `run_cypher_rule(session)`; rejestracja w `LinterRuleEngine` przez `rules=[SEC01Rule()]`?
- Jak `CrossReferenceEngine` łączy błędy z wielu domen — każdy `Violation` ma pole `domain: str`; `CrossReferenceEngine.aggregate_by_domain(violations)→Dict[str, List[Violation]]` grupuje błędy; `aggregate_cross_domain(violations)→List[CrossDomainIssue]` wykrywa węzły naruszające reguły z co najmniej 2 różnych domen (np. `node_x` ma AUTH-01 z domeny `API` i ORPHAN-01 z domeny `GRAPH`); `CrossDomainIssue(node_id, domains, violations)` jako sygnał krytyczny?
- Jak wdrożyć regułę `TEST-01` dla weryfikacji planu testów — `TEST-01`: `MATCH (e:EventFrame {domain:'SYSTEM'}) WHERE NOT (e)-[:HAS_TEST_PLAN]->(:TestPlan {status:'APPROVED'}) RETURN e`; węzeł `:TestPlan {id, status: 'DRAFT'|'APPROVED', coverage_pct: float}`; naruszenie TEST-01 gdy system nie ma zatwierdzonego planu testów; `Violation('TEST-01', e_id, severity='MEDIUM')` — 7. reguła w katalogu; otwiera nową domenę SYSTEM dla Lintera?
- Napiszmy fazę Green dla `CrossReferenceEngine` — minimalna implementacja: `class CrossReferenceEngine: def __init__(self, docs): self.docs=docs; def check_cascade(self, violation): return [Violation(violation.rule_id, violation.node_id, source_doc=d) for d in self.docs if d.references(violation.node_id) and d != violation.source_doc]`; `doc.references(node_id)→bool` jako metoda kontraktu dokumentu; `aggregate_by_domain(violations)→defaultdict(list)`; wszystkie dotychczasowe testy (cascade/isolation/CrossDomainIssue) powinny przejść GREEN?
- Jak `CrossReferenceEngine` zarządza kaskadowymi błędami w grafie — kolejność propagacji: (1) `run_all()→violations`; (2) dla każdego `v`: `cascade=engine.check_cascade(v)→list`; (3) `detect_conflicts(violations, cascade)→conflicts`; (4) `aggregate_cross_domain(violations+cascade)→critical`; błędy CRITICAL (cross-domain) są raportowane przed HIGH i MEDIUM w `AuditReportGenerator`; strategia `depth_limit=3` zapobiega nieskończonej rekurencji?
- Jakie reguły dedukcji kontekstowej powinien implementować CrossReferenceEngine — (1) `TRANSITIVITY`: jeśli `A→B` i `B→C` naruszają tę samą regułę, `A→C` też narusza; (2) `SCOPE_INHERITANCE`: naruszenie reguły w pakiecie dziedziczy do wszystkich klas; (3) `TEMPORAL_ORDER`: naruszenie w kroku N blokuje walidację kroków N+1..M; `DeductionRule(name, apply(violations)→List[Violation])` jako interfejs strategii dedukcji?
- Pokaż przykładowy raport luki dla brakującej przyczyny w grafie — `KnowledgeGapTracker` wykrywa: `{type:'MISSING_CAUSE', predicate:'zobowiązuje', node_id:'e_47', doc_id:'W4', details:'EventFrame bez krawędzi :CAUSES — przyczyna zobowiązania nie zdefiniowana'}`; raport Markdown: `| MISSING_CAUSE | e_47 | W4 | predicate=zobowiązuje |`; priorytet wyższy od MISSING_SYNSET (bo MISSING_CAUSE blokuje wnioskowanie Lintera)?
- Czy `CrossReferenceEngine` może automatycznie budować ontologię dla nowych domen — heurystyka: `OntologyBuilder.infer_domain(violations)→domain_name` na podstawie `rule_id` prefix (SEC→SECURITY, PROC→PROCEDURE, TEST→TESTING); `MERGE (:Domain {name: domain_name}); MERGE (e)-[:BELONGS_TO_DOMAIN]->(d)` uzupełnia węzły bez domeny; nowe domeny SYSTEM/BACKUP trafiają do grafu automatycznie bez ręcznej konfiguracji; ryzyko: fałszywe przypisanie domeny przez prefix matching?
- Napiszmy pełny kod produkcyjny `CrossReferenceEngine` (Green) — `class CrossReferenceEngine: def __init__(self, docs, depth_limit=3): self.docs=docs; self._depth=depth_limit; def check_cascade(self, violation, depth=0): if depth>=self._depth: return []; refs=[Violation(violation.rule_id, violation.node_id, source_doc=d) for d in self.docs if d.references(violation.node_id)]; return refs+[v2 for r in refs for v2 in self.check_cascade(r, depth+1)]; def aggregate_by_domain(self, violations): res=defaultdict(list); [res[v.domain].append(v) for v in violations]; return res; def aggregate_cross_domain(self, violations): by_node=defaultdict(set); [by_node[v.node_id].add(v.domain) for v in violations]; return [CrossDomainIssue(n,ds,[v for v in violations if v.node_id==n]) for n,ds in by_node.items() if len(ds)>=2]`?
- Jak `CrossReferenceEngine` wykorzystuje relacje Słowosieci do dedukcji — `doc.references(node_id)` sprawdza nie tylko bezpośrednie referencje ale też synonimy i hiponimy: `wordnet_lookup(node_id)→{synonyms, hypernyms}`; jeśli `doc` zawiera hiponim węzła naruszającego regułę, naruszenie propaguje też do tego dokumentu; `DeductionRule.TRANSITIVITY` + Słowosieć = dedukcja semantyczna; przykład: naruszenie SEC-01 na `api_auth` propaguje do doc referującego `autoryzacja_api` (synonim w Słowosieci)?
- Pokaż przykład błędu kaskadowego dla wymogu SEC-01 — `EventFrame {id:'e_checkout', domain:'API'}` bez `:HAS_THREAT_MODEL`; `SEC01Rule.run_cypher_rule()→[Violation('SEC-01','e_checkout',severity='HIGH')]`; `CrossReferenceEngine.check_cascade(v)` → `doc_B` (specyfikacja płatności) i `doc_C` (SRS kasy) referencują `e_checkout` → 3 `Violation` łącznie; `aggregate_cross_domain()→CrossDomainIssue('e_checkout', {'API','PAYMENT','SYSTEM'}, 3_violations)` → severity escaluje do CRITICAL?
- Jak `CrossReferenceEngine` ocenia ważność naruszeń SEC-01 — algorytm: `_score_severity(violations)→severity`: 1 domena → HIGH; 2 domeny → CRITICAL; 3+ domeny → CRITICAL+ALERT; `ALERT` = sygnał do natychmiastowego powiadomienia (`notify_hook()`); SEC-01 startuje jako HIGH per węzeł, ale cascade do 2+ domen automatycznie eskaluje; `Violation.escalated: bool` dodatkowe pole do śledzenia czy severity zmienił się przez kaskadę?
- Pokaż implementację `analyze_cascades` dla bazy bez backupu — `def analyze_cascades(self, initial_violations): result = CascadeAnalysis(direct=initial_violations, cascaded=[], critical=[]); for v in initial_violations: cascaded = self.check_cascade(v); result.cascaded.extend(cascaded); cross = self.aggregate_cross_domain(initial_violations+cascaded); result.critical.extend(cross); return result`; `CascadeAnalysis(NamedTuple)` z polami `direct`, `cascaded`, `critical`; dla `Backup01Rule` → `direct=[BACKUP-01/db_prod]` + `cascaded=[doc_DR, doc_SLA]` + `critical=[]` (1 domena = nie CRITICAL)?
- Jakie błędy kaskadowe wykrywa Silnik Zależności w grafie Neo4j — katalog typów kaskad: (1) `SINGLE_NODE_CASCADE`: 1 węzeł narusza N reguł w tej samej domenie; (2) `CROSS_DOMAIN_CASCADE`: 1 węzeł narusza reguły w 2+ domenach → CRITICAL; (3) `TRANSITIVE_CASCADE`: A→B→C przez Słowosieć synonimy; (4) `DEPTH_EXCEEDED_CASCADE`: propagacja zatrzymana przez `depth_limit=3` → ostrzeżenie `CascadeDepthWarning`; każdy typ ma osobny `cascade_type` w `Violation.details`?
- Jak `CrossReferenceEngine` używa sąsiedztwa w grafie do rozwiązywania konfliktów — `_get_neighborhood(node_id, session, hops=2)→List[Node]` pobiera węzły w odległości ≤2 krawędzi; dwa konflikty są rozwiązywalne gdy ich węzły mają wspólnego sąsiada (`SHARED_NEIGHBOR`); `detect_conflicts()` rozszerzone: `conflict.resolution='SHARED_NEIGHBOR'` gdy sąsiedztwo nakłada się; przykład: ORPHAN-01 i AUTH-01 na tym samym `api_frame` sąsiadują z `ThreatModel` → konflikt MUTUAL_EXCLUSION rozwiązany?
- Pokaż implementację `resolve_conflicts` dla przykładu ze słowem "klucz" — homografia: `klucz` może być `INSTRUMENT` (narzędzie) lub `AUTH_TOKEN` (bezpieczeństwo); `resolve_conflicts(violations_a=[AUTH-01/klucz], violations_b=[ROLE-01/klucz])→RuleConflict(conflict_type='HOMOGRAPH_AMBIGUITY', resolution_hint='check domain of klucz node')`; rozwiązanie: `session.run("MATCH (n {id:'klucz'}) RETURN n.domain")` → `domain='SECURITY'` → zachowaj AUTH-01, odrzuć ROLE-01 jako fałszywy pozytyw?
- Jak wdrożyć regułę `OPS-04` sprawdzającą procedury backupu w Neo4j — `OPS-04`: `MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->(:BackupProcedure {tested:True, frequency:'DAILY'}) RETURN db`; węzeł `:BackupProcedure {id, frequency:'DAILY'|'WEEKLY', tested:Bool, last_test_date}`; różnica od `BACKUP-01` (brak polityki): OPS-04 sprawdza czy procedura jest **przetestowana** i **codzienna**; `Violation('OPS-04', db_id, severity='HIGH')` — 8. reguła Lintera, nowa kategoria OPS?
- Jak zaimplementować regułę `OPS-04` jako klasę — `class Ops04Rule(LinterRule): id='OPS-04'; QUERY = "MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->(:BackupProcedure {tested:True, frequency:'DAILY'}) RETURN db.id AS node_id"; def run_cypher_rule(self, session): return [Violation(self.id, row['node_id'], severity='HIGH', domain='OPS') for row in session.run(self.QUERY)]`; GREEN dla testu z B43 `test_backup01_rule_fires_on_db_without_policy` po zmianie klasy z `Backup01Rule` na `Ops04Rule`?
- Jak Słowosieć pomaga odróżnić "klucz szyfrujący" od "klucza płaskiego" — w plWordNet `klucz` ma 3 synsety: `klucz.1` (narzędzie mechaniczne, hiperonimia→INSTRUMENT), `klucz.2` (kryptograficzny, hiperonimia→AUTH_TOKEN, domain=SECURITY), `klucz.3` (muzyczny); `resolve_conflicts()` pobiera `wordnet_lookup('klucz')→{synsets:[…]}`; synset z `domain=SECURITY` → zachowaj AUTH-01; synset z domeną INSTRUMENT → `ROLE-01` → fałszywy pozytyw; Słowosieć jako arbiter semantyczny przed `_get_neighborhood()`?
- Pokaż jak `CrossReferenceEngine` wykorzystuje Słowosieć do rozwiązywania konfliktów krok po kroku — (1) `detect_conflicts(v_a, v_b)` wykrywa `HOMOGRAPH_AMBIGUITY`; (2) `wordnet_lookup(node.lemma)→synsets`; (3) dla każdego synsetu: `synset.domain` → mapuj na domenę reguły (`SECURITY→AUTH-01`, `LOGISTICS→ROLE-01`); (4) zachowaj violation której domena=domena reguły; (5) `RuleConflict.resolved=True, resolution='WORDNET_DOMAIN'`; przepływ: `klucz.2.domain=SECURITY` → `AUTH-01 wins`, `ROLE-01 dismissed`?
- Jak zintegrować Słowosieć z `CrossReferenceEngine` dla lepszej dedukcji — `class WordnetDeductionMixin: def _get_semantic_refs(self, node_id): lemma=self._node_lemma(node_id); syns=wordnet_lookup(lemma); return syns.get('hypernyms',[])+syns.get('synonyms',[])`; `CrossReferenceEngine` dziedziczy mixin i nadpisuje `doc.references()`: `doc.references(node_id) or any(doc.references(s) for s in self._get_semantic_refs(node_id))`; zwiększa recall kaskady kosztem precyzji — parametr `use_wordnet: bool` kontroluje kompromis?
- W jaki sposób `CrossReferenceEngine` wykorzystuje relacje Słowosieci w `check_cascade()` — szczegółowo: (1) `check_cascade(violation)` wywołuje `_get_semantic_refs(violation.node_id)` gdy `use_wordnet=True`; (2) dla każdego synsetu-synonim sprawdza `doc.references(syn)`; (3) jeśli doc referencuje synonim → `Violation(..., source_doc=doc, cascade_type='TRANSITIVE_WORDNET')`; (4) HAS_SYNSET krawędź w Neo4j jest źródłem synonimów; (5) nowy `cascade_type='TRANSITIVE_WORDNET'` vs `cascade_type='TRANSITIVE_CASCADE'` (grafu) — rozróżnienie pozwala filtrować w raporcie?
- Pokaż kod produkcyjny reguły `TEST-01` dla Neo4j — `class Test01Rule(LinterRule): id='TEST-01'; QUERY = "MATCH (e:EventFrame {domain:'SYSTEM'}) WHERE NOT (e)-[:HAS_TEST_PLAN]->(:TestPlan {status:'APPROVED'}) RETURN e.id AS node_id"; def run_cypher_rule(self, session): return [Violation(self.id, row['node_id'], severity='MEDIUM', domain='SYSTEM') for row in session.run(self.QUERY)]`; GREEN dla 5 testów RED z B46/B49: fires/no_violation_approved/draft/medium+domain/query_checks_approved; `'APPROVED'` w QUERY spełnia `test_test01_query_checks_approved_status()`?
- Pokaż jak zintegrować `CrossReferenceEngine` z `AuditReportGenerator` — `generator = AuditReportGenerator(kgt=kgt); engine = CrossReferenceEngine(docs); analysis = engine.analyze_cascades(linter.run_all(session)); all_violations = analysis.direct + analysis.cascaded; report = generator.generate(all_violations); report['cascade_summary'] = {'direct': len(analysis.direct), 'cascaded': len(analysis.cascaded), 'critical': len(analysis.critical)}`; `generate_markdown()` dodaje sekcję `## Błędy kaskadowe` z podziałem direct/cascaded/critical?
- Jak zintegrować `CrossReferenceEngine` z `AuditReportGenerator` rozszerzony wzorzec — `class AuditPipeline: def __init__(self, linter, engine, generator): ...; def run(self, session, docs): direct=linter.run_all(session); analysis=engine.analyze_cascades(direct); conflicts=engine.detect_conflicts(direct, analysis.cascaded); report=generator.generate(analysis.direct+analysis.cascaded); report['conflicts']=[c._asdict() for c in conflicts]; report['cascade_summary']=analysis._asdict_counts(); return report`; `AuditPipeline` jako Facade łącząca LinterRuleEngine+CrossReferenceEngine+AuditReportGenerator w jednym wywołaniu?
- Jak przetestować `AuditPipeline.run()` — `def test_audit_pipeline_run_returns_full_report(): linter=Mock(); linter.run_all.return_value=[Violation('SEC-01','e1',domain='API',severity='HIGH')]; engine=Mock(); engine.analyze_cascades.return_value=CascadeAnalysis(direct=[...],cascaded=[],critical=[]); engine.detect_conflicts.return_value=[]; generator=Mock(); generator.generate.return_value={'violations':{},'summary':{'total':1}}; pipeline=AuditPipeline(linter,engine,generator); report=pipeline.run(session,docs); assert 'cascade_summary' in report; assert 'conflicts' in report`; test weryfikuje że Facade poprawnie scala wyniki wszystkich 3 komponentów?
- Wdróżmy regułę `OPS-04` — rozszerzona implementacja z RTO/RPO: `class Ops04Rule(LinterRule): id='OPS-04'; QUERY = "MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->(:BackupProcedure {tested:True, frequency:'DAILY'}) OR (db)-[:HAS_BACKUP_PROCEDURE]->(bp) WHERE bp.rto_hours > 4 RETURN db.id AS node_id, coalesce(bp.rto_hours, null) AS rto"`; naruszenie gdy brak procedury LUB `rto_hours > 4` dla systemów DORA-critical; `Violation.details={'rto_hours': row['rto']}` przekazuje wartość do raportu?
- Jak `CrossReferenceEngine` wykorzystuje Słowosieć do rozwiązywania wieloznaczności — architektura: `CrossReferenceEngine(docs, wordnet_adapter=WordnetAdapter())` przyjmuje adapter jako dependency injection; `WordnetAdapter.get_synsets(lemma)→List[Synset]`; w `resolve_conflicts()`: dla każdego konfliktu `HOMOGRAPH_AMBIGUITY` → `synsets = wordnet_adapter.get_synsets(node.lemma)` → `best_synset = max(synsets, key=lambda s: similarity(s.domain, violation.domain))`; `similarity()` mierzy odległość domenową (SECURITY↔API=0.9; SECURITY↔INSTRUMENT=0.1); zwycięska reguła = ta z wyższym `similarity`?
- Jak Słowosieć rozwiązuje wieloznaczność w metodzie `resolve_conflicts` — algorytm wyboru synsetu: (1) `wordnet_lookup(lemma)→{synsets}`; (2) dla każdego konfliktu: `score_a = synset.similarity_to_domain(v_a.domain)`; `score_b = synset.similarity_to_domain(v_b.domain)`; (3) `winner = v_a if score_a > score_b else v_b`; (4) `RuleConflict(winner_rule=winner.rule_id, resolved=True, resolution='WORDNET_DOMAIN', confidence=abs(score_a-score_b))`; `confidence < 0.3` → `AMBIGUOUS_RESOLUTION` zamiast `WORDNET_DOMAIN` — wymaga ręcznej weryfikacji?
- Pokaż Green dla `resolve_conflicts` — `def resolve_conflicts(self, conflicts): result = []; for c in conflicts: synsets = self._wordnet.get_synsets(c.node_lemma); score_a = max((s.similarity_to_domain(c.rule_a_domain) for s in synsets), default=0); score_b = max((s.similarity_to_domain(c.rule_b_domain) for s in synsets), default=0); conf = abs(score_a - score_b); winner = c.rule_a if score_a > score_b else c.rule_b; res = 'AMBIGUOUS_RESOLUTION' if conf < 0.3 else 'WORDNET_DOMAIN'; result.append(c._replace(winner_rule=winner, resolved=conf>=0.3, resolution=res, confidence=conf)); return result`; przechodzi test RED z B52 dla `klucz` (SECURITY score=0.9, INSTRUMENT score=0.1 → conf=0.8 > 0.3)?
- Jak zintegrować kaskady z `AuditReportGenerator` przez `cascade_type` — `generate_markdown(violations, kgt)` grupuje naruszenia po `cascade_type`: sekcja `## Naruszenia bezpośrednie` (brak `cascade_type`), `## Kaskady semantyczne` (`TRANSITIVE_WORDNET`), `## Kaskady grafowe` (`TRANSITIVE_CASCADE`, `CROSS_DOMAIN_CASCADE`); każda sekcja z tabelą `|rule_id|node_id|severity|details|`; `generate_json()` zachowuje `cascade_type` jako pole w każdym naruszeniu dla downstream narzędzi?
- Jak dodać obsługę reguły API-01 i DEP-01 do istniejącego schematu SQLite?
- Jak rozbudować `relation_mapper.py` o relację `contradicts` (wykrywanie sprzeczności)?
- Jak dodać tagi YAML front matter do plików Markdown projektu (format: `layer`, `title`, `status`, `tags`)?
- Jak `doc_auditor.py` waliduje obecność i poprawność YAML front matter w plikach dokumentacji?
- Jak zintegrować tagowanie YAML z `GapAnalysisGenerator` — czy YAML tagi trafiają do raportu luk?
- Jak wpiąć `KnowledgeGapTracker` w `AuditPipeline.run()` — uzupełnienie kontraktu Facade: `def run(self, session, docs, kgt=None): direct=self.linter.run_all(session); analysis=self.engine.analyze_cascades(direct); conflicts=self.engine.detect_conflicts(direct, analysis.cascaded); report=self.generator.generate(analysis.direct+analysis.cascaded); report['conflicts']=[c._asdict() for c in conflicts]; report['cascade_summary']=analysis._asdict_counts(); report['knowledge_gaps']=kgt.get_gaps() if kgt else []; return report`; `AuditPipeline` staje się pełnym Facade z 5 kluczami: `violations, cascades, conflicts, knowledge_gaps, summary`; `KnowledgeGapTracker.get_gaps()→List[KnowledgeGap]` zawiera `{type, node_id, doc_id, details}`?
- Faza Green dla `CrossDomainIssue.severity_escalated` (zamknięcie RED z B49) — `@dataclass class CrossDomainIssue: node_id: str; domains: Set[str]; violations: List[Violation]; severity_escalated: str = field(init=False)` + `def __post_init__(self): order=['MEDIUM','HIGH','CRITICAL']; self.severity_escalated = 'CRITICAL' if len(self.domains) >= 2 else max(self.violations, key=lambda v: order.index(v.severity)).severity`; `aggregate_cross_domain()` konstruuje `CrossDomainIssue(node_id, domains, violations)` bez jawnego przekazywania `severity_escalated` — auto-obliczane przez `__post_init__`; test z B49 `assert cross[0].severity_escalated == 'CRITICAL'` przechodzi GREEN; domyka cykl TDD #9?
- Jak rozszerzyć `OPS-04` o wymóg RPO ≤1h zgodnie z DORA art.12 — trzecia gałąź UNION: `UNION MATCH (db:Database)-[:HAS_BACKUP_PROCEDURE]->(bp:BackupProcedure) WHERE bp.rpo_hours > 1 RETURN db.id AS node_id, bp.rpo_hours AS rpo`; `Violation.details={'rpo_hours': row['rpo']}` dla naruszeń RPO; pełny DORA-compliance = OPS-04 z 3 gałęziami (brak procedury + RTO > 4h + RPO > 1h); nowy RED test: `def test_ops04_fires_when_rpo_exceeds_1h(): session.run.return_value=[{'node_id':'db_prod','rto':None,'rpo':4}]; assert Ops04Rule().run_cypher_rule(session)[0].details=={'rpo_hours':4}`; czyni OPS-04 pełną implementacją DORA Pillar 4 Recovery Objectives?

### 4. Testowanie

- Jak napisać test własnościowy (Hypothesis) dla `gap_detector.py`, który gwarantuje, że `completeness_score ∈ [0,1]`?
- Jak przetestować regresję po zmianie progów podobieństwa — złoty wzorzec dla 10 dokumentów?
- Jak zmierzyć pokrycie mutacyjne (Mutation Score) dla W0 — jakie są minima dla projektu zarobkowego?
- Jakie testy integracyjne należy napisać dla subkomendy `doc-audit` w `compliance_check.py`?
- Napiszmy pierwszy RED test dla `CrossReferenceEngine` na poziomie unit — `def test_cross_ref_engine_no_violations_for_empty_docs(): engine = CrossReferenceEngine([]); result = engine.check_cascade(Violation('AUTH-01','node_x')); assert result == []`; RED bo konstruktor `CrossReferenceEngine([])` nie istnieje — zakłada co najmniej jeden dokument; unit test bez fixtury Neo4j?
- Napiszmy RED test dla bazy danych bez backupu — `def test_backup01_rule_fires_on_db_without_policy(): session = Mock(); session.run.return_value = [{'db': {'id': 'db_prod'}}]; rule = Backup01Rule(); violations = rule.run_cypher_rule(session); assert violations[0].rule_id == 'BACKUP-01'; assert violations[0].severity == 'CRITICAL'`; RED bo klasa `Backup01Rule` jeszcze nie istnieje w katalogu reguł?
- Napiszmy RED test integracyjny dla reguły SEC-01 — `@pytest.mark.integration def test_sec01_rule_integration(neo4j_session): neo4j_session.run("MERGE (:EventFrame {id:'e_no_threat', domain:'API'})"); rule = SEC01Rule(); violations = rule.run_cypher_rule(neo4j_session); assert len(violations) == 1; assert violations[0].node_id == 'e_no_threat'`; RED bo `neo4j_session` fixture nie jest jeszcze zarejestrowana w `conftest.py`; test wymaga prawdziwej bazy — `@pytest.mark.integration` odseparowuje od unit testów?
- Dodajmy przypadek testowy dla reguły TEST-01 — `def test_test01_rule_fires_on_system_without_approved_plan(): session = Mock(); session.run.return_value = [{'e': {'id': 'sys_checkout'}}]; rule = Test01Rule(); violations = rule.run_cypher_rule(session); assert violations[0].rule_id == 'TEST-01'; assert violations[0].severity == 'MEDIUM'`; drugi test: `def test_test01_no_violation_when_plan_approved(): session.run.return_value = []; assert rule.run_cypher_rule(session) == []`; RED bo `Test01Rule` klasa jeszcze nie istnieje — otwiera TDD cycle dla TEST-01?
- Zdefiniujmy więcej testów RED dla reguły TEST-01 — `def test_test01_fires_when_plan_draft(): session.run.return_value = [{'e':{'id':'sys_reg'}}]; assert Test01Rule().run_cypher_rule(session)[0].rule_id == 'TEST-01'`; `def test_test01_returns_medium_severity(): v = Test01Rule().run_cypher_rule(session)[0]; assert v.severity == 'MEDIUM'; assert v.domain == 'SYSTEM'`; `def test_test01_query_checks_approved_status(): rule=Test01Rule(); assert "status:'APPROVED'" in rule.QUERY`; 3 nowe testy + 2 z B46 = kompletna specyfikacja TEST-01 przed Green?
- Pokaż test RED symulujący kaskadę bezpieczeństwa dla modułu logowania — `def test_login_module_security_cascade(): login_frame = Violation('SEC-01','e_login', domain='AUTH', severity='HIGH'); engine = CrossReferenceEngine([doc_session_mgmt, doc_sso, doc_audit_log]); analysis = engine.analyze_cascades([login_frame]); assert len(analysis.cascaded) >= 2; cross = engine.aggregate_cross_domain(analysis.direct+analysis.cascaded); assert any(c.node_id=='e_login' for c in cross); assert cross[0].severity_escalated == 'CRITICAL'`; RED bo `severity_escalated` pole nie istnieje jeszcze w `CrossDomainIssue`?
- Pokaż test RED dla `resolve_conflicts` ze słowem "klucz" — `def test_resolve_conflicts_klucz_homograph(): engine = CrossReferenceEngine(docs, use_wordnet=True); v_auth = Violation('AUTH-01','klucz', domain='SECURITY'); v_role = Violation('ROLE-01','klucz', domain='GRAPH'); conflicts = engine.detect_conflicts([v_auth], [v_role]); assert len(conflicts) == 1; resolved = engine.resolve_conflicts(conflicts); assert resolved[0].resolved == True; assert resolved[0].resolution == 'WORDNET_DOMAIN'; assert resolved[0].winner_rule == 'AUTH-01'`; RED bo `resolve_conflicts()` i `RuleConflict.winner_rule` jeszcze nie istnieją?
- Czy zaczynamy od Fazy RED dla reguły `OPS-04` w Neo4j — `def test_ops04_fires_on_db_without_backup(): session=Mock(); session.run.return_value=[{'node_id':'db_prod','rto':None}]; rule=Ops04Rule(); violations=rule.run_cypher_rule(session); assert violations[0].rule_id=='OPS-04'; assert violations[0].severity=='HIGH'`; `def test_ops04_fires_when_rto_exceeds_4h(): session.run.return_value=[{'node_id':'db_prod','rto':8}]; v=Ops04Rule().run_cypher_rule(session)[0]; assert v.details=={'rto_hours':8}`; `def test_ops04_no_violation_when_compliant(): session.run.return_value=[]; assert Ops04Rule().run_cypher_rule(session)==[]`; 3 testy RED — kompletna specyfikacja przed Green?
- Faza Green dla `OPS-04` — `class Ops04Rule(LinterRule): id='OPS-04'; QUERY="MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->(:BackupProcedure {tested:True,frequency:'DAILY'}) RETURN db.id AS node_id, null AS rto UNION MATCH (db:Database)-[:HAS_BACKUP_PROCEDURE]->(bp:BackupProcedure) WHERE bp.rto_hours > 4 RETURN db.id AS node_id, bp.rto_hours AS rto"; def run_cypher_rule(self,session): return [Violation(self.id,r['node_id'],severity='HIGH',domain='OPS',details={'rto_hours':r['rto']} if r['rto'] else {}) for r in session.run(self.QUERY)]`; UNION w Cypher obsługuje oba warunki; wszystkie 3 testy RED przechodzą?
- Jak przetestować `AMBIGUOUS_RESOLUTION` w `resolve_conflicts` — `def test_resolve_conflicts_ambiguous_when_low_confidence(): adapter=Mock(); adapter.get_synsets.return_value=[Synset(similarity_to_domain=lambda d: 0.55)]; engine=CrossReferenceEngine([], wordnet_adapter=adapter); c=RuleConflict('AUTH-01','ROLE-01','klucz',conflict_type='HOMOGRAPH_AMBIGUITY'); resolved=engine.resolve_conflicts([c]); assert resolved[0].resolution=='AMBIGUOUS_RESOLUTION'; assert resolved[0].resolved==False`; `resolved=False` oznacza że wniosek wymaga ręcznego przeglądu — nie jest usuwany z raportu, lecz oznaczony flagą `needs_review=True`?
- Uruchommy testy integracyjne dla reguły SEC-01 w Neo4j — rozbuduj fixture: `@pytest.fixture def neo4j_session(): driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j','test')); session = driver.session(); yield session; session.run("MATCH (n) DETACH DELETE n"); session.close()`; test: `def test_sec01_fires_and_clears_on_mitigated(): neo4j_session.run("MERGE (:EventFrame {id:'e_pay', domain:'API'})-[:HAS_THREAT_MODEL]->(:ThreatModel {mitigated:True})"); assert SEC01Rule().run_cypher_rule(neo4j_session) == []`; GREEN po dodaniu fixture; wymaga lokalnego Neo4j lub testcontainers?
- Jak uruchamiać testy integracyjne SEC-01 bez lokalnego Neo4j — `pip install testcontainers[neo4j]`; fixture: `@pytest.fixture(scope='session') def neo4j_session(): from testcontainers.neo4j import Neo4jContainer; c=Neo4jContainer('neo4j:5.18'); c.start(); driver=GraphDatabase.driver(c.get_connection_url(), auth=('neo4j','password')); with driver.session() as s: yield s; c.stop()`; kontener startuje w CI automatycznie, teardown usuwa dane; `pytest -m integration` uruchamia tylko testy z prawdziwą bazą; `@pytest.mark.skipif(not os.getenv('NEO4J_TESTCONTAINERS'), reason='requires docker')` jako guard dla środowisk bez Dockera?
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
- **Pułapka 7 (bariery projektowe):** 3 fundamentalne bariery które zatrzymały podobne projekty NLP+compliance: (1) **Ontologia vs. corpus drift** — ontologia projektowana na początku nie nadąża za ewolucją dokumentacji; rozwiązanie: `OntologyBuilder.infer_domain()` auto-rozszerza domenę; (2) **Skalowalność grafu** — Neo4j Community bez partycjonowania zatrzymuje się przy ~1M węzłów; rozwiązanie: domenowe podgrafy + `depth_limit`; (3) **Brak definicji done** — projekt nie ma granicy "kiedy audyt jest kompletny"; rozwiązanie: reguły z numerowanymi wersjami (`SEC-01 v1.2`) + `coverage_pct` jako metryka zamknięcia?
- **Pułapka 8 (bariery projektów lingwistycznych):** 3 bariery specyficzne dla projektów lingwistycznych: (1) **Pokrycie leksykalne** — Słowosieć plWordNet pokrywa ~150k synsetów, ale dokumentacja techniczna IT zawiera do 30% leksemów spoza korpusu; `KnowledgeGapTracker.UNKNOWN_WORD` mierzy tę lukę; (2) **Drift morfologiczny** — polskie fleksje mnożą formy (np. "dostarczylibyśmy"); Morfeusz bez aktualizacji do nowych neologizmów zwraca `ign` tag dla ~5% zdań technicznych; (3) **Konflikt standardów anotacji** — TEI P5 vs CoNLL-U vs własny EventFrame: każda zmiana wymaga migracji całego korpusu; rozwiązanie: adapterowa warstwa konwersji?
- **Pułapka 9 (lock-in grafu):** Lock-in schematu Neo4j — węzły `:EventFrame`, `:ThreatModel`, `:BackupProcedure`, `:TestPlan` zaprojektowane pod Cypher; migracja do AuraDB cloud, Amazon Neptune (Gremlin) lub Apache AGE (PostgreSQL) wymaga przepisania wszystkich reguł Lintera; rozwiązanie: `GraphQueryAdapter` jako interfejs abstrakcji `run_query(q: Query)→List[Row]`; `CypherQueryAdapter` i `GremlinQueryAdapter` jako implementacje; `LinterRule.run_query(adapter)` nie wie jakiego backendu używa — zero-cost swap bazy grafowej bez zmiany kodu reguł?

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
