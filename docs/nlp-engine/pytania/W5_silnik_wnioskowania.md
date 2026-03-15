---
layer: W5
title: "Warstwa 5 — Silnik Wnioskowania (InferenceEngine / Drools)"
phase: 5
status: planned
docs_version: 1.0.0
tags: [InferenceEngine, Drools, DRL, wnioskowanie, dedukcja, lancuchy_przyczynowe, StateMatrix]
---

# Warstwa 5 — Silnik Wnioskowania (InferenceEngine / Drools)

## Przegląd

Warstwa 5 implementuje logiczne wnioskowanie na grafie wiedzy z W4.
Przetwarza `EventRoleDict` przez reguły IF-THEN (Python lub Drools DRL),
buduje łańcuchy przyczynowe i inferencje (stan obiektu, posiadanie, lokalizacja, naruszenie_zobowiązania).

Kluczowe klasy: `InferenceEngine`, `StateMatrix`, `IntentClassifier`.

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W5 istnieje bo compliance wymaga logiki warunkowej która kaskaduje — zdarzenie A może triggerować wniosek B który triggeruje regułę C. Tego nie da się wyrazić prostym filtrowaniem. Drools DRL pozwala deklaratywnie zapisać "IF agent EXISTS AND instrument IS_A narzędzie_ostre AND NOT policy(bezpieczeństwo) THEN flag RISK-01" — i ta reguła działa dla każdego przyszłego przypadku bez zmiany kodu. `StateMatrix` deduplicuje wnioski (ten sam fakt nie może być flagowany dwukrotnie) i "zamraża" stan po każdym przebiegu (idempotentność — krytyczna dla projektu zarobkowego).

**Co się sypie bez tej warstwy:**
- Reguły compliance muszą być zakodowane jako if-else w Pythonie — każda zmiana wymaga deploymentu nowego kodu; klient nie może edytować reguł bez programisty
- Brak kaskadowania: "RISK-01 + CONS-02 jednocześnie" nie może triggerować eskalacji severity
- Brak `StateMatrix`: ten sam dokument audytowany dwukrotnie daje zduplikowane wyniki — raport compliance jest nieaudytowalny

**Zależności:**
- Wchodzi z W4: graf wiedzy (Cypher zapytania, zwracające fakty)
- Wchodzi z W2: `EventRoleDict` (bezpośrednio lub przez W4)
- Wychodzi do W7: `List[AuditFinding]` przez REST API
- Wychodzi do W8: te same fakty jako wejście dla `AuditEngine` i `GapAnalysisReport`

## Diagram przepływu danych

```
Graf Neo4j (W4) + EventRoleDict (W2)
       │
  InferenceEngine
  ┌────────────────────────────────────────────┐
  │  _rule_location(event) → LOCATED_AT        │
  │  _rule_possession_transfer(event) → OWNS   │
  │  _rule_state_change(event) → state=dead    │
  │  _rule_classify_legal(event) → naruszenie_zobowiązania│
  │  _rule_negation(event) → NOT_OCCURRED      │
  └────────────────────────────────────────────┘
       │
  StateMatrix         ← deduplikacja wniosków, "zamrażanie"
       │
  IntentClassifier    ← QUESTION / COMMAND / ASSERT / NEGATE
       │
       ▼
  InferenceResult {facts: [...], intents: [...], state: {...}}
       │
       ▼
  W7 (FastAPI) / W8 (AuditEngine)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Jak załadować Słowosieć do modułu wnioskowania w Pythonie?
- Jak połączyć GraphDatabaseAdapter z modułem wnioskowania Drools?
- Jaki jest podział odpowiedzialności między InferenceEngine, Drools KieSession, i StateMatrix?
- Jak wyglądają granice W5 — co dostarcza W4 (baza grafowa) a co W5 dodaje przed przekazaniem do W8?
- Jaki wzorzec stosuje W5 dla rejestrowania reguł DRL — plugin, convention-over-configuration, czy explicit register?
- Jak W5 obsługuje wiele aktywnych sesji KieSession równolegle — pool sesji, jedna sesja globalna, czy per-request?
- Jak zdefiniować architekturę DocumentClassifier w W5 — oddzielna klasa czy metoda KlasyfikatorKontekstu.classify_by_metadata()?
- Jak DocumentClassifier współpracuje z InferenceEngine — wynik klasyfikacji pliku filtruje zestaw reguł DRL przed wnioskowniem?
- Zaimplementujmy klasę DocumentClassifier jako Krok 0 pipeline — wywołanie DocumentClassifier.classify(file_path) przed W1→W8 wybiera zestaw reguł DRL dla danego typu dokumentu?
- Jak DocumentClassifier.classify(file_path) → DocumentType z confidence — następnie InferenceEngine.set_active_ruleset(document_type) aktywuje właściwe reguły?
- Jak wyeksponować wynik DocumentClassifier w logach pipeline'u — linia "Krok 0: UMOWA (confidence=0.92)" przed przetwarzaniem W1→W8?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest format wejściowy reguły DRL — plik tekstowy, JSON z metadanymi reguły, czy DSL Drools?
- Jak zdefiniować kontrakt dla wyniku wnioskowania — lista obiektów Inference z polami confidence, rule_id, evidence?
- Jakie pola są wymagane w StateMatrix przekazywanej między sesjami Drools — id, version, facts_hash?
- Jak wersjonować reguły DRL — SemVer (1.2.3), hash zawartości, czy timestamp modyfikacji?
- Jak wygląda przykładowy JSON dla wyniku InferenceEngine dla naruszenia CONS-02 — pokaż schemat?

### 3. Implementacja
- Jak w grafie wiedzy oznaczyć intencję działania aktora?
- Jakie reguły logiczne w Drools obsłużą synkretyzm form?
- Wyjaśnij różnicę między modelem lingwistycznym a modelem zdarzenia..
- Jakie reguły logiczne wdrożyć dla automatycznej ontologii?
- Pokaż przykład implementacji reguł Drools dla grafu..
- Jak stworzyć model ontologii zdarzeń dla domeny prawnej?
- Jakie reguły weryfikacji zastosować dla ontologii zdarzeń w fazie 2?
- Jak wdrożyć model danych grafu (Neo4j) dla analizy zdarzeń?
- Czy system może sam wywnioskować intencję na podstawie narzędzia?
- Wyjaśnij barierę eksplozji reguł i ontologii w projektach symbolicznych..
- Jakie reguły w silniku Drools obsłużą relacje agent-patient?
- Pokaż przykład wnioskowania logicznego w systemie symbolicznym..
- Jak wdrożyć walidację reguł w Drools dla relacji nsubj i obj?
- Pokaż przykład wnioskowania na grafie zdarzeń w Neo4j..
- Jakie reguły Drools najlepiej obsłużą synkretyzm w DRL?
- Jakie reguły Drools najlepiej obsłużą eliminację ról przy wieloznaczności?
- Jak zapisać reguły dedukcyjne IF-THEN w silniku Drools?
- Pokaż przykład reguły DRL dla wnioskowania o istnieniu obiektu..
- Jak uniknąć eksplozji ontologii przy modelowaniu zdarzeń?
- Jak stworzyć reguły Drools klasyfikujące zdarzenie prawne?
- Jak połączyć ontologię z analizą intencji (speech acts)?
- Jak w Drools zgłosić lukę w dokumentacji?
- Pokaż przykład reguły Drools rozwiązującej synkretyzm..
- Pokaż przykład reguły Drools mapującej składnię na rolę agent..
- Pokaż przykład reguły Drools dla relacji AGENT i PATIENT..
- Jak połączyć relację HAS_TRIGGER z wnioskowaniem w silniku Drools?
- Jak zmapować relacje przyczynowe w grafie zdarzeń?
- Jak rozszerzyć ontologię o relacje przyczynowe w Neo4j?
- Jak zdefiniować regułę dedukcji dla lokalizacji w grafie?
- Czy Drools to dobry wybór dla polskiego silnika wnioskowania?
- Jakie jeszcze reguły poza lokalizacją warto teraz zaimplementować?
- Czy do wnioskowania semantycznego lepiej użyć Drools czy Pythona?
- Jakie reguły dedukcji przestrzennej dodać do InferenceEngine?
- Jak połączyć reguły logiczne z ontologią Słowosieci?
- Czy silnik wnioskowania powinien obsługiwać relacje przyczynowe?
- Czy Drools obsłuży reguły oparte na cechach obiektu i środowisku?
- Jak system powinien reagować na wykrycie przestępstwa w grafie?
- Pokaż jak zapisać regułę lokalizacji w pliku .drl dla Drools.
- Jakie inne reguły przestrzenne warto dodać do silnika wnioskowania?
- Jak połączyć wnioski z Drools z bazą grafową Neo4j?
- Pokaż implementację logiki wnioskowania dla lokalizacji.
- Jak zdefiniować regułę dla wnioskowania o intencjach?
- Jak zapisać regułę w pliku .drl dla Drools?
- Jak zapisać regułę lokalizacji w natywnym formacie Drools .drl?
- Pokaż logikę pętli w natywnym pliku .drl dla Drools.
- Jakie reguły wnioskowania dodać dla domeny prawnej i medycznej?
- Pokaż przykład pliku .drl dla reguły lokalizacji.
- Jak połączyć Walentego z naszym modelem zdarzeń i ról?
- Jakie reguły wnioskowania najlepiej obsłużą hierarchię gatunków ze Słowosieci?
- Jak zaimplementować wykrywanie ramy subkategoryzacyjnej dla czasownika 'dostarczyć'?
- Pokaż regułę wnioskowania o posiadaniu dla Wykonawcy i Zamawiającego.
- Jakie są najtrudniejsze ramy walencyjne w języku polskim?
- Pokaż przykład złożonej ramy walencyjnej dla nowej domeny..
- Jak rozbudować model zdarzenia o wymiar narzędzia i intencji?
- Pokaż jak zaimplementować regułę _rule_possession_transfer w kodzie..
- Pokaż logikę wstrzymania zapisu dla intencji QUESTION w InferenceEngine..
- Pokaż regułę wnioskowania: 'Maria posiada książkę' po akcji 'dać'..
- Jak rozbudować InferenceEngine o tryb odpytywania grafu?
- Jak rozszerzyć reguły wnioskowania o wymiar intencji i przyczyny?
- Pokaż kod metody _rule_possession_transfer dla silnika..
- Jak wykryć negację dla reguły _rule_possession_transfer?
- Czy możemy rozbudować tę regułę o wymiar intencji?
- Jak wdrożyć logikę odpytywania grafu dla pytań o lokalizację?
- Pokaż implementację reguły _rule_possession_transfer z obsługą negacji..
- Jak dodać wymiar konsekwencji dla akcji sprzedaży w InferenceEngine?
- Zaimplementujmy mechanizm przeszukiwania wzorca w InferenceEngine dla pytań..
- Jak rozbudować ontologię o relacje przyczynowe i skutkowe?
- Pokaż jak dodać wymiar narzędzia do reguł wnioskowania..
- Pokaż jak rozbudować graf o łańcuchy przyczynowo-skutkowe..
- Czy system obsłuży pytania o relacje przyczynowe?
- Jak dodać relację negacji do silnika wnioskowania?
- Pokaż implementację relacji NEGATION dla zaprzeczonych faktów..
- Jak zmodyfikować _rule_possession_transfer, aby uwzględniała status NOT_OCCURRED?
- Pokaż jak wykryć relację NEGATION za pomocą parsera zależności..
- Jak zaimplementować relację NEGATION dla zaprzeczonych faktów?
- Jak wdrożyć State Matrix, by uniknąć fałszywych alarmów w audycie?
- Jak silnik powinien wnioskować na podstawie przyczyn i skutków?
- Pokaż przykładowe reguły logiczne dla domeny prawnej i medycznej..
- Jak rozszerzyć CausalChainBuilder o wnioskowanie semantyczne z użyciem synsetów z W3 (Słowosieć)?
- Jak CausalChainBuilder buduje łańcuch przyczynowy — które EventFrame stają się węzłami a które krawędziami?
- Jak wzbogacić CausalChainBuilder o synonimy — np. "dostarczyć" i "przekazać" traktowane jako ta sama akcja?
- Jakie reguły DRL sterują CausalChainBuilder przy wykrywaniu związku przyczyna→skutek w dokumentach prawnych?
- Jak CausalChainBuilder obsługuje łańcuchy wielopoziomowe — A→B→C gdy B jest pośrednim warunkiem?
- Pokaż implementację Soft Matching w CausalChainBuilder z użyciem hiperonimii — predykaty są dopasowywane semantycznie nie leksykalnie?
- Jak Soft Matching sprawdza czy :EventFrame.predicate należy do synsetu 'dostarczyć' (i synonimów) przed emisją krawędzi :CAUSES?
- Jak zdefiniować próg Soft Matching — minimalne jaccard@synsets między predykatem a wzorcem reguły (threshold = 0.5)?
- Jak testować Soft Matching — asercja że 'przekazać' pasuje do reguły zdefiniowanej dla 'dostarczyć' przez wspólny synset?
- Zintegrujmy SlowosiecAdapter z CausalChainBuilder do łączenia zdarzeń — CausalChainBuilder.link_events(e1, e2) sprawdza SlowosiecAdapter.get_synonyms(e1.predicate) zanim emituje krawędź :CAUSES?
- Jak CausalChainBuilder decyduje czy dwa EventFrame połączyć :CAUSES bazując na Słowosieci — e1.predicate ∈ get_synonym_set(rule.predicate) → MERGE (e1)-[:CAUSES]->(e2)?
- Jak wywołać SlowosiecAdapter wewnątrz CausalChainBuilder — inicjalizacja `self._lexicon = SlowosiecAdapter(db_path)` w konstruktorze, wywołanie `self._lexicon.get_synonyms(predicate)` w metodzie `link_events()`?
- Jak obsłużyć wyjątek LookupError gdy predykat nie istnieje w Słowosieci — fallback do dopasowania leksykalnego (exact match) zamiast semantycznego?
- Jak zaktualizować CausalChainBuilder._infer() o wnioskowanie semantyczne — dla każdej pary EventFrame sprawdź `_lexicon.get_synonyms(e.predicate)` i dopasuj do synsetów wzorca reguły przed emisją :CAUSES?
- Jak buforować wyniki SlowosiecAdapter w CausalChainBuilder — `@lru_cache(maxsize=512)` na metodzie `_get_synonym_set(predicate)` aby uniknąć powtórnych zapytań SQLite podczas analizy dokumentu?
- Jak skonfigurować próg semantycznego soft matchingu w CausalChainBuilder — parametr `threshold: float = 0.5` w konstruktorze, porównanie jaccard@synsets między predykatem a wzorcem?
- Jak przetestować integrację SlowosiecAdapter+CausalChainBuilder dla soft matchingu — asercja że dokument z 'przekazać' aktywuje regułę CONS-02 zdefiniowaną dla 'dostarczyć'?
- Jak rozszerzyć `_soft_match` o relacje hiperonimii — oprócz synonimów sprawdzaj `_lexicon.get_hypernyms(predicate)` i porównaj hiperonim ze wzorcem reguły (np. 'przekazać' → 'dostarczyć' → 'działanie')?
- Jak ustalić głębokość przeszukiwania hiperonimii w `_soft_match` — parametr `max_depth: int = 3` w konstruktorze, BFS po ścieżce hiperonimów do korzenia ontologii przez `get_hypernym_path()`?
- Zaimplementujmy klasę KnowledgeGapTracker do logowania nieznanych zdarzeń i słów — jakie typy luk rozróżnia (UNKNOWN_PREDICATE, MISSING_SYNSET, UNMATCHED_RULE)?
- Jak KnowledgeGapTracker rejestruje zdarzenie nierozpoznane przez żadną regułę DRL — hook after_rule_evaluation gdy activated_rules.is_empty()?
- Jak KnowledgeGapTracker eksportuje dane do kolejki aktywnego uczenia — JSONL z polami predicate, context, doc_id, timestamp?
- Jak zintegrować KnowledgeGapTracker z InferenceEngine — rejestracja jako listener Drools WorkingMemoryEventListener?
- Zaimplementujmy KnowledgeGapTracker do logowania nieznanych struktur składniowych — jak tracker wykrywa zdanie bez parsowania dep_rel (brak węzła root w CoNLL-U z UDPipe)?
- Jak KnowledgeGapTracker kategoryzuje typy luk — UNKNOWN_WORD (tag ign), UNKNOWN_STRUCTURE (brak root), UNMATCHED_PREDICATE (brak synsetu), UNMATCHED_RULE (brak reguły DRL)?
- Jak tracker loguje nieznane struktury do bazy aktywnego uczenia — wpis UNKNOWN_STRUCTURE zawiera: raw_sentence, conllu_partial, doc_id, timestamp?
- Jak zintegrować KnowledgeGapTracker z potokiem analizy zdarzeń — w EventFrame extraction loop: dla każdego EventFrame wywołaj `tracker.check_predicate(frame.predicate)` zanim trafi do InferenceEngine?
- Jak KnowledgeGapTracker wchodzi w potok W2→W5 — po SemanticMapper.extract() `tracker.check(event)` przed przekazaniem EventFrame do InferenceEngine?
- Napiszmy kod KnowledgeGapTracker — metoda `capture_ign(token)` gdy `token.tag == 'ign'`: `self._gaps.append({'type': 'UNKNOWN_WORD', 'form': token.form, 'doc_id': self._doc_id})`?
- Jak KnowledgeGapTracker przechwytuje osierocone zdarzenia — metoda `capture_orphan(event: EventFrame)` gdy event nie ma żadnej krawędzi :CAUSES w grafie?
- Jak eksportować zebrane luki do pliku JSONL — metoda `dump_jsonl(path)` iteruje `self._gaps` i zapisuje każdy wpis przez `json.dumps(gap, ensure_ascii=False)`?
- Jak wdrożyć Klasyfikator Kontekstu aby system rozumiał typ (jestestwo) dokumentu — umowa, SRS, raport, specyfikacja?
- Jak KlasyfikatorKontekstu pobiera sygnały z W3 (leksyka), W2 (role) i W6 (koreferencja) do klasyfikacji dokumentu?
- Jak zdefiniować enum klas dokumentów w KlasyfikatorKontekstu — UMOWA, SRS, RAPORT_AUDYTU, SPECYFIKACJA_TECHNICZNA?
- Jak KlasyfikatorKontekstu wpływa na InferenceEngine — czy aktywowane reguły DRL są filtrowane per typ dokumentu?
- Jak InferenceEngine odpytuje graf przyczynowy w Neo4j — Cypher query wbudowany w regułę DRL?
- Jak CausalChainBuilder tworzy krawędź :CAUSES między dwoma :EventFrame po aktywacji reguły?
- Jak InferenceEngine weryfikuje spójność grafu przyczynowego — czy krawędź :CAUSES nie tworzy cyklu?
- Jakie dane treningowe są potrzebne dla KlasyfikatorKontekstu — etykietowane przykłady per typ dokumentu?
- Jak zdefiniować próg pewności (confidence threshold) KlasyfikatorKontekstu — co zwrócić gdy wynik < 0.6?
- Jak obsłużyć fallback KlasyfikatorKontekstu gdy dokument nie pasuje do żadnej klasy — UNKNOWN czy heurystyka?
- Jak aktualizować model KlasyfikatorKontekstu bez restartu serwisu — hot reload reguł klasyfikacji?
- Jak ekstrahować cechy z nagłówków i tytułów sekcji dokumentu dla KlasyfikatorKontekstu — regex + tf-idf?
- Jak obsłużyć dokument wieloklasowy (jednocześnie UMOWA i SPECYFIKACJA_TECHNICZNA) — multi-label vs. priorytetyzacja?
- Jak wyjaśnić decyzję klasyfikatora — które cechy zadecydowały o klasie UMOWA (SHAP lub lista feature importances)?
- Jak walidować KlasyfikatorKontekstu na polskich dokumentach prawnych — stratified cross-validation, metryki F1 per klasa?
- Jak zautomatyzować klasyfikację dokumentów na podstawie YAML front matter — pola title, tags, layer jako sygnały KlasyfikatorKontekstu?
- Jak wyekstrahować cechy z tytułów sekcji (## nagłówki) dla KlasyfikatorKontekstu — TF-IDF na słowach kluczowych nagłówków?
- Jak połączyć sygnały YAML metadata (layer: W_x, tags: [ARCH-01]) z sygnałami leksykalnymi w jednym wektorze cech klasyfikatora?
- Jak klasyfikować dokument bez YAML front matter — fallback na analizę nagłówków i pierwszych 200 tokenów?
- Jak zaimplementować szablony walidacyjne per typ dokumentu — dataclass DocumentTemplate z listą wymaganych sekcji i reguł compliance?
- Jak KlasyfikatorKontekstu generuje szablony walidacyjne — mapowanie UMOWA→[CONS-02, RISK-01], SRS→[ARCH-01, SEC-01]?
- Jak wdrożyć Klasyfikator Kontekstu i Złotych Standardów łącznie — KlasyfikatorKontekstu.classify() → GoldenStandardProfile → DocumentTemplate z regułami?
- Jak przekazać wynik KlasyfikatorKontekstu do GoldenStandardProfile.get_template(document_type) w AuditEngine?
- Jak testować połączenie KlasyfikatorKontekstu z GoldenStandardProfile — mock document_type=UMOWA → oczekiwany template zawiera CONS-02?
- Jak wykryć że dokument nie spełnia szablonu walidacyjnego — diff wymaganych sekcji vs. nagłówków wykrytych przez Linter?
- Zaimplementujmy KlasyfikatorKontekstu i szablony walidacyjne dla typów dokumentów — pipeline: classify() → select_template() → validate_against_template() → lista luk?
- Jak zdefiniować dataclass DocumentTemplate z listą required_sections, mandatory_rules i optional_rules per typ dokumentu (UMOWA/SRS/RAPORT)?
- Jak DocumentTemplate.validate(document) zwraca listę ValidationGap — brakujące sekcje i niespełnione reguły jako strukturyzowane wyniki audytu?
- Jak InferenceEngine korzysta ze synsetów w Neo4j (Wariant A) do rozszerzenia reguł o synonimy?
- Jak InferenceEngine odpytuje SlowosiecAdapter on-demand (Wariant B) w regule DRL bez blokowania sesji?
- Jak porównać skuteczność Wariantu A vs. B dla reguły CONS-02 — F1 score na zbiorze testowym?
- Zaimplementujmy eksport łańcuchów kauzalnych do formatu Mermaid.js — metoda CausalChainBuilder.to_mermaid()?
- Jak zserializować graf przyczynowy jako Mermaid flowchart LR — węzły to EventFrame.id, krawędzie to :CAUSES z rule_id?
- Jak obsłużyć łańcuchy z rozgałęzieniami (jeden :EventFrame powoduje dwa skutki) w formacie Mermaid.js?
- Jak escapować znaki specjalne (cudzysłowy, polskie litery) w etykietach węzłów Mermaid.js?
- Jak testować serializer Mermaid.js — golden file test z oczekiwanym outputem dla łańcucha A→B→C?
- Jak ograniczyć głębokość wyświetlanego łańcucha kauzalnego parametrem MAX_DEPTH w to_mermaid()?
- Jak kodować kolorem węzły Mermaid.js według ważności — CRITICAL: style fill:#f66, WARNING: style fill:#fa0?
- Jak osadzić diagram Mermaid.js w raporcie PDF/HTML — inline w Markdown czy eksport do SVG przez mermaid CLI?
- Jak linkować węzeł Mermaid.js z referencją do zdania źródłowego — click callback z document_id i sentence_id?
- Wygeneruj przykładowy kompletny diagram Mermaid.js dla raportu audytu CONS-02 — flowchart LR z węzłami zdarzenia i krawędziami :CAUSES?
- Jak wybrać poziom szczegółowości przykładu Mermaid.js — 3-węzłowy dla prezentacji vs. pełny dla eksportu technicznego?
- Jak zaktualizować metodę to_mermaid() aby wyświetlała relacje semantyczne — :IS_A, :HAS_SYNSET obok :CAUSES w tym samym diagramie?
- Jak kodować typ relacji w etykiecie krawędzi Mermaid.js — A -->|IS_A| B vs. A -->|CAUSES rule_id| B?
- Jak filtrować które relacje semantyczne trafiają do to_mermaid() — parametr include_relations: List[str]?
- Jak generować oddzielne sekcje `subgraph` w Mermaid.js dla każdego typu relacji (kauzalne vs. ontologiczne)?
- Zaktualizujmy logikę CausalChainBuilder o analizę intencji aktów mowy — jak rozpoznać czy :EventFrame jest ZOBOWIĄZANIEM, OSTRZEŻENIEM czy WYKONANIEM?
- Jakie cechy morfosyntaktyczne i leksykalne wskazują na akt mowy ZOBOWIĄZANIE (shall, zobowiązuje się) vs. POTWIERDZENIE (oświadcza, potwierdza)?
- Jak CausalChainBuilder tworzy krawędź :CAUSES gdy akt mowy ZOBOWIĄZANIE nie jest spełniony — link do EventFrame naruszenia?
- Stwórzmy wizualizację grafu łańcuchów przyczynowych w Mermaid.js — flowchart LR: niedostarczenie→brak_odbioru→naruszenie_CONS02→kara_umowna z etykietami severity?
- Jak dodać etykiety identyfikatorów reguł compliance na krawędziach Mermaid.js — `A -->|CAUSES:CONS-02| B` z linkiem do definicji reguły?
- Przygotujmy metodę to_html() w CausalChainBuilder — serializuje łańcuch kauzalny jako fragment HTML z osadzonym diagramem Mermaid.js przez `<div class="mermaid">` + inicjalizację mermaid.initialize()?
- Jak to_html() różni się od to_mermaid() — to_mermaid() zwraca str z flowchart LR, to_html() opakowuje go w kompletny fragment HTML gotowy do wstawienia w raport?
- Jak testować to_html() — asercja że wynik zawiera `<div class="mermaid">flowchart LR` i wywołanie `mermaid.initialize()`?

### 4. Testowanie
- Napiszmy test jednostkowy dla soft matchingu synonimów — `@pytest.mark.parametrize` z parami ('przekazać','dostarczyć'), ('wręczyć','dostarczyć') potwierdzającymi aktywację reguły CONS-02?
- Jak przetestować próg soft matchingu — asercja że pary z jaccard@synsets < 0.5 NIE aktywują reguły, a pary z jaccard ≥ 0.5 aktywują?
- Jak testować `_soft_match` w izolacji — mock SlowosiecAdapter zwracający zdefiniowane synsets dla konkretnych lematów bez zapytania do SQLite?
- Jak w Drools połączyć rozpoznaną akcję z wymogiem testu?
- Pokaż regułę Drools dla testu integracyjnego.
- Stwórzmy czerwony test dla nowej klasy InferenceEngine.
- Pokaż pętlę dedukcji, która zapali test na zielono..
- Stwórzmy test dla reguły skutku akcji 'dostarczyć z opóźnieniem' w InferenceEngine.
- Przetestujmy ramy walencyjne dla nowych czasowników..
- Napiszmy czerwony test dla nowej reguły posiadania w InferenceEngine..
- Napiszmy funkcję build_event_graph w Fazie GREEN..
- Jak zbudować dataset testowy dla reguły CONSTRAINT_VIOLATION — 10 zdań triggering i 10 non-triggering?
- Jak napisać test własnościowy (Hypothesis) dla CONSTRAINT_VIOLATION sprawdzający że kolejność słów nie zmienia wyniku?
- Jak mierzyć Precision i Recall reguły CONSTRAINT_VIOLATION na zbiorze zdań z korpusu NKJP?
- Pokaż strukturę pliku JSONL z danymi testowymi dla CONSTRAINT_VIOLATION — pola: sentence, expected_fired, rule_id?

### 5. Obsługa błędów
- Jak obsłużyć zaprzeczenia w regule _rule_possession_transfer?
- Co się dzieje gdy żadna reguła DRL nie pasuje do faktu — pusta lista Inference czy wyjątek NoRuleMatched?
- Jak obsłużyć nieoczekiwany wyjątek Java w KieSession — izolacja sesji czy restart całego serwisu?
- Jak logować każdą decyzję wnioskowania do celów audytu i traceability dla klienta?
- Jak obsłużyć zbyt długi czas wnioskowania — czy jest zdefiniowany timeout per session?
- Jak system obsłuży brakujące pojęcia OOV w InferenceEngine — gdy predykat EventFrame nie istnieje w Słowosieci: fallback do exact match, log KnowledgeGapTracker.capture_ign(token), kontynuacja pipeline zamiast wyjątku?
- Jak propagować informację o OOV przez pipeline W1→W5 — token `ign` z Morfeusza staje się UNKNOWN_WORD w KGT, InferenceEngine traktuje go jako low-confidence event bez emisji :CAUSES?

### 6. Integracja z innymi warstwami
- Jak zintegrować reguły Drools z wynikami parsera lxml?
- Czy Drools wymaga osobnego modułu w pipeline?
- Pokaż jak zintegrować Słowosieć z regułami wnioskowania o gatunkach.
- Jak zintegrować Słowosieć z regułami wnioskowania o lokalizacji?
- Jak zintegrować Słowosieć z ontologią pojęć w silniku wnioskowania?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jak uniknąć konfliktów reguł DRL gdy dwie reguły mają tę samą salience i sprzeczne akcje dla tego samego faktu?
- Co się dzieje gdy InferenceEngine wchodzi w pętlę — cykl zależności reguła A aktywuje B aktywuje A?
- Jak obsłużyć stare reguły DRL które nie pasują do nowego schematu EventFrame po migracji struktury danych?
- Jaka jest konsekwencja gdy StateMatrix jest niespójna między dwiema instancjami serwisu za load balancerem?
- Czy KieSession Drools jest thread-safe przy równoległym przetwarzaniu wielu dokumentów?
- Jak ograniczyć czas wnioskowania gdy reguły prowadzą do rozległego forward chaining powyżej limitu czasowego?
- Jakie jest ryzyko błędnej klasyfikacji CONS-02 gdy w dokumencie brakuje daty lub strony umowy?

## Pytania uzupełniające
- **Pułapka 3:** Drools `KieSession` nie jest thread-safe — każdy wątek musi mieć własną sesję; reużycie sesji między wątkami powoduje `ConcurrentModificationException`.
- **Pułapka 4:** Reguły DRL z `salience` (priorytet) — zmiana kolejności plików `.drl` może zmienić wyniki gdy dwie reguły mają ten sam salience; wyniki są niedeterministyczne bez jawnego salience.
- **Pułapka 5:** Drools `Working Memory` akumuluje wszystkie facts — bez `retract(fact)` po przetworzeniu zdania sesja rośnie w pamięci bez ograniczeń przy batch processingu.
- **Pułapka 6:** IntentClassifier wytrenowany na jednej domenie (np. prawna) nie generalizuje na inną (wojskowa, medyczna) — F1 może spaść z 0.90 do 0.45 bez domeny-specyficznego fine-tuningu.

### 1. Architektura

- Czy `InferenceEngine` powinien używać Drools (JVM) czy natywnego Pythona — trade-off?
- Jak zarządzać eksplozją reguł przy >1000 reguł DRL — partycjonowanie, agenda groups?
- Jak podzielić `InferenceEngine` na plugins (jeden plugin = jedna domena: prawna, medyczna, techniczna)?
- Jaka jest granica odpowiedzialności między W5 (wnioskowanie) a W4 (persystencja grafu)?
- Jak `StateMatrix` deduplikuje sprzeczne fakty — first-write-wins czy last-write-wins?

### 2. Kontrakty danych

- Jaki jest schemat `InferenceResult` — pola facts, intents, state?
- Jak reprezentować łańcuch przyczynowy w JSON: lista par `(cause, effect)` czy drzewo?
- Jaki format ma plik `.drl` dla reguły lokalizacji — minimalny przykład?
- Jak kodować pewność wnioskowania (confidence) w `InferenceResult`?
- Jak przechowywać `StateMatrix` między wywołaniami (stateful vs. stateless engine)?

### 3. Implementacja

- Jak zaimplementować `_rule_location(event)` — kiedy `EventRoleDict` ma LOCATION → zapisz `LOCATED_AT`?
- Jak zaimplementować `_rule_possession_transfer(give_event)` → `Maria OWNS książka`?
- Jak wykrywać negację (`nie dał`) i zapisać `NOT_OCCURRED` w StateMatrix?
- Jak zaimplementować `_rule_classify_legal(event)` wykrywającą naruszenie_terminowe (AGENT + dostarczyć + MANNER:opóźnienie)?
- Jak zaimplementować `IntentClassifier` — detekcja QUESTION przez słowa pytajne?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `InferenceEngine` — `"Wykonawca dostarczył dokumentację z opóźnieniem"` → `{cons: CONS-02, rule: naruszenie_terminu}`?
- Jak testować wielowymiarowy model zdarzenia: AGENT + ACTION + PATIENT + INSTRUMENT + LOCATION + TIME?
- Jak testować negację: `"Wykonawca nie dostarczył dokumentacji"` → `dostawa=NOT_OCCURRED`?
- Jak testować łańcuch: zdanie 1 = "Wykonawca złożył ofertę", zdanie 2 = "Wykonawca dostarczył dokumentację z opóźnieniem" → wnioskowanie o naruszeniu?
- Jak testować zapytania o lokalizację: `"Gdzie jest dokumentacja?"` → przeszukanie grafu → odpowiedź?
#### Kompletna hierarchia TDD
- Zaimplementuj Fazę GREEN dla `InferenceEngine` — minimalna reguła: IF AGENT=Wykonawca AND action=dostarczyć AND MANNER=opóźnienie THEN AuditFinding(CONS-02).
- Jak zrefaktoryzować `InferenceEngine` po GREEN — zastąpić hardkodowaną regułę deklaratywnym Drools DRL?
- Zrefaktoryzuj `InferenceEngine` — każda reguła compliance jako osobny plik DRL załadowany przez `RuleLoader`, testowalny w izolacji.
- Jak napisać test jednostkowy dla pojedynczej reguły DRL — mock grafu W4, sprawdzić że jedna reguła odpala się na właściwych faktach?
- Jak napisać test integracyjny W4→W5: załaduj rzeczywiste fakty z Neo4j → sprawdź że `InferenceEngine` generuje `AuditFinding(CONS-02)`?
- Jak zbudować oracle dataset dla W5 — 30 zdań kontraktowych + oczekiwane `AuditFinding[]` per zdanie?
- Jak zmierzyć Mutation Score dla reguł DRL — jak mutować warunki reguły żeby sprawdzić czy testy to wykrywają?
- Jak napisać test własnościowy (Hypothesis) dla `InferenceEngine` — idempotentność: to samo zdarzenie wnioskowane 2× → 1 `AuditFinding` (nie duplikat)?
- Jak wykryć regresję reguł: zmiana hierarchii synsetów W3 może sprawić że CONS-02 przestaje odpalać — baseline snapshot wyników per corpus?
- Stwórz test regresyjny `InferenceEngine` — golden file: 20 zdarzeń kontraktowych + oczekiwane reguły które mają się odpalić; CI fail przy rozbieżności.
- Jak przetestować W1→W5 end-to-end — dokument z 3 naruszeniami → sprawdź że `AuditFinding[]` ma dokładnie 3 wyniki z właściwymi `rule_id`?

### 5. Obsługa błędów

- Co robi `InferenceEngine` gdy EventRoleDict nie ma AGENT (elipsa podmiotu)?
- Jak obsługiwać sprzeczne reguły (reguła A i reguła B dają przeciwne wyniki)?
- Co gdy Drools nie może załadować pliku `.drl` (syntax error)?
- Jak obsługiwać nieskończoną pętlę dedukcji (A → B → A)?
- Jak logować, które reguły zostały aktywowane i w jakiej kolejności?
- Co robi `InferenceEngine` gdy plik `.drl` ma błąd składni Drools — pada całe ładowanie czy tylko zepsuta reguła jest pomijana?
- Jak obsługiwać nieskończoną pętlę reguł (reguła A aktywuje B, B aktywuje A)?

### 6. Integracja z innymi warstwami

- Jak W5 pobiera dane z Neo4j (W4) — czy `InferenceEngine` ma własny `Neo4jAdapter`?
- Jak W5 dostaje `EventRoleDict` z W2 — bezpośrednio czy przez W4?
- Jak W3 (Słowosieć, hiperonimia) zasila reguły W5 — "wróbel IS_A ptak" → reguła dla ptaków?
- Jak W6 (koreferencja) rozwiązuje zaimki ZANIM W5 dostanie EventRoleDict?
- Jak W7 (FastAPI) wywołuje W5 — synchronicznie czy async?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Drools wymaga JVM — niekompatybilność z czystym Python stackiem. Alternatywa: Python rule engine (experta, nools-py) lub własny IF-THEN runner.
- **Pułapka 2:** Eksplozja reguł DRL przy >500 regułach powoduje czas kompilacji >30s. Konieczne: agenda groups, rule salience, partial evaluation.
- **Pułapka 3:** StateMatrix bez "zamrażania wniosków" powoduje wielokrotne re-inferowanie tych samych faktów — każde nowe zdanie re-triggeruje wszystkie reguły.
- **Pułapka 3:** Drools `KieSession` nie jest thread-safe — każdy wątek musi mieć własną sesję; reużycie sesji między wątkami powoduje `ConcurrentModificationException`.
- **Pułapka 4:** Reguły DRL bez jawnego `salience` — gdy dwie reguły mają ten sam priorytet, kolejność aktywacji zależy od kolejności ładowania plików `.drl`; wyniki mogą być niedeterministyczne.
- **Pułapka 5:** `Working Memory` akumuluje fakty bez `retract()` — przy batch processingu sesja rośnie w pamięci bez ograniczeń.
- **Pułapka 6:** IntentClassifier wytrenowany na jednej domenie — F1 może spaść z 0.90 do 0.45 przy zmianie domeny bez fine-tuningu.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Czas wnioskowania dla 1 zdania (1000 reguł) | < 100 ms |
| Czas wnioskowania batch 100 zdań | < 10 s |
| Precision klasyfikacji naruszenia terminowego (CONS-02) | ≥ 95% |
| F1 detekcji intencji QUESTION vs ASSERT | ≥ 90% |
| Pokrycie testów linii | ≥ 85% |

## Pytania o idempotentność i deterministyczność

- Czy `InferenceEngine.infer(event)` wywołane 3× na identycznym evencie daje identyczny `InferenceResult`?
- Czy kolejność reguł DRL ma wpływ na końcowy wynik?
- Jak zapewnić deterministyczność przy równoległym przetwarzaniu zdań?

## Pytania o migrację i wersjonowanie

- Jak aktualizować reguły `.drl` bez przerywania działania serwisu (hot reload)?
- Jak wersjonować reguły — git tag per wersja reguł, changelog zmian logiki?
- Jak zachować backwards-compatibility gdy zmienia się schemat `InferenceResult`?

## Pytania o audytowalność

- Jak logować pełny ślad wnioskowania: "reguła X aktywowana bo warunek Y spełniony przez fakt Z"?
- Jak przechowywać activation trace per zdanie dla celów dowodowych (odpowiedzialność cywilna)?
- Jak wygenerować raport "dlaczego system sklasyfikował zdarzenie jako naruszenie_zobowiązania"?

---

## Rozszerzalność i skalowanie

### Stopniowe dodawanie reguł wnioskowania

- Jak dodać nową regułę dedukcji bez recompilacji całego zbioru reguł?
- Jak hot-reload reguł Drools bez restartu serwisu (KieScanner, incremental update)?
- Jak zaimplementować `register_rule(name, condition, action)` — dynamiczne reguły Python?
- Jak testować nową regułę w izolacji, nie uruchamiając wszystkich pozostałych?
- Jak mierzyć coverage reguł — ile % zdarzeń z testowego korpusu aktywuje przynajmniej 1 regułę?

### Stopniowe dodawanie domen (prawna → medyczna → wojskowa)

- Jak zorganizować reguły DRL per domena — osobne pliki `.drl` czy jeden globalny?
- Jak zaimplementować `load_domain(name)` — lazy loading reguł domenowych?
- Jak wykrywać konflikty między regułami z różnych domen (reguła prawna vs medyczna dają sprzeczne klasyfikacje)?
- Jak testować, że dodanie domeny medycznej nie zmienia wyników dla domeny prawnej?
- Jak stopniowo rozszerzać `StateMatrix` o nowe typy stanów domenowych?

### Skalowanie liczby reguł

- Jakie są progi wydajności Drools dla 100 / 1000 / 10000 reguł — czas kompilacji i czas ewaluacji?
- Jak zarządzać eksplozją reguł przez Agenda Groups (partycjonowanie per domena)?
- Jak zaimplementować rule salience — priorytetowanie reguł bezpieczeństwa nad regułami informacyjnymi?
- Jak testować, że nowe reguły nie powodują nieskończonej pętli dedukcji?
- Jak profilować, które reguły są najczęściej aktywowane (reguła → liczba aktywacji)?

### Inkrementalne uczenie się

- Jak system uczy się nowych wzorców z corpus feedback — semi-supervised rule induction?
- Jak zaimplementować `suggest_rule(false_negative_examples)` — propozycja nowej reguły?
- Jak weryfikować automatycznie wygenerowane reguły przed wdrożeniem (human-in-the-loop)?

---

## Luki zidentyfikowane przez audyt cross-warstwowy

### Powiadamianie W5 o zmianach ontologii W3 (brak mechanizmu)

- Jak `InferenceEngine` dostaje powiadomienie o nowym synsecie dodanym do W3 bez restartu serwisu?
- Jak zaimplementować `on_lexicon_update(event)` — callback wywoływany gdy W3 dodaje nowy leksem/synset?
- Jakie reguły Drools trzeba recompilować po dodaniu nowego synset, a jakie są odporny na tę zmianę?
- Jak testować, że nowy synset ze Słowosieci (np. neologizm "hackować" IS_A "atakować") jest od razu dostępny dla reguł W5?
- Jak izolować "gorące" reguły (zależne od ontologii W3) od "zimnych" (czysto składniowych) żeby minimalizować zakres recompilacji?

### Brakująca decyzja: W3 before/inside W5

- Czy W5 wywołuje W3 bezpośrednio (np. `SlowosiecAdapter.get_hypernyms(lemma)`) czy dostaje już wzbogacony `EnrichedToken`?
- Jak zdefiniować interfejs `IOntologyProvider` który W5 przyjmuje jako dependency — niezależnie od tego czy to W3 czy wbudowana ontologia?
