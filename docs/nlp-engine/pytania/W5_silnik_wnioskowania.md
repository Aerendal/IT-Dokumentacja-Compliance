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
- Jak wpiąć DependencyParserAdapter do CausalChainBuilder — `CausalChainBuilder.__init__(self, parser: DependencyParser, lexicon: SlowosiecAdapter)` umożliwia re-parsowanie zdania źródłowego gdy EventFrame.agent jest None przy budowaniu łańcucha?
- Jak CausalChainBuilder używa DependencyParser gdy EventFrame nie ma wypełnionych ról — fallback `parser.parse(event.raw_sentence)` wydobywa nsubj i uzupełnia EventFrame.agent zamiast odrzucania zdarzenia z łańcucha?
- Jak CausalChainBuilder propaguje SituationalContext przez łańcuch kauzalny — węzeł B dziedziczy `context.temporal` od A gdy zdarzenie B następuje bezpośrednio po A (AFTER); `context.causal.cause_id = e_prev.id` ustawiany automatycznie po emisji krawędzi :CAUSES?
- Jak modelować wielowymiarowy kontekst zdarzenia w grafie przyczynowym — każdy EventFrame w CausalChainBuilder nosi `context.causal: {cause_id, effect_id}` aktualizowany po MERGE :CAUSES; `context.temporal` dziedziczony z relacji temporalnych wnioskowanych przez parser?
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
- Jak KnowledgeGapTracker loguje nieznane lematy z tagiem ign — pełny wpis: `{'type':'UNKNOWN_WORD', 'form': token.form, 'context': [prev.form, next.form], 'pos_in_sentence': token.id, 'doc_id': self._doc_id, 'timestamp': datetime.utcnow().isoformat()}`; kontekst sąsiednich tokenów ułatwia ręczne etykietowanie w kolejce aktywnego uczenia?
- Jak KnowledgeGapTracker przechwytuje osierocone zdarzenia — metoda `capture_orphan(event: EventFrame)` gdy event nie ma żadnej krawędzi :CAUSES w grafie?
- Jak eksportować zebrane luki do pliku JSONL — metoda `dump_jsonl(path)` iteruje `self._gaps` i zapisuje każdy wpis przez `json.dumps(gap, ensure_ascii=False)`?
- Wdróżmy pętlę KnowledgeGapTracker w pipeline W2→W5 — `for event in event_frames: tracker.check_predicate(event.predicate); tracker.capture_orphan(event) if not graph.has_edges(event); inference_engine.run(event)`?
- Jak pętla KnowledgeGapTracker obsługuje wyjątki na poziomie zdarzenia — try/except per event: wyjątek → `tracker.capture_error(event, exc)`, pipeline kontynuuje następne zdarzenie zamiast przerywać sesję?
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
- Napiszmy minimalny kod klasy `IntentClassifier` aby testy przeszły — `class IntentClassifier: QUESTION_WORDS = {'jak','czy','kiedy','gdzie','co','kto'}; def classify(self, sentence: str) → str: return 'QUESTION' if sentence.split()[0].lower() in self.QUESTION_WORDS else 'ASSERT'`; faza GREEN dla testu `assert clf.classify('Jak działa system') == 'QUESTION'`?
- Pokaż przykład klasyfikacji intencji dla dokumentacji technicznej w Pythonie — `clf = IntentClassifier(); clf.classify('Wykonawca dostarczył SRS')` → `'ASSERT'`; `clf.classify('Czy SRS spełnia wymagania?')` → `'QUESTION'`; `clf.classify('Należy dostarczyć dokumentację')` → `'REQUIREMENT'` (rozszerzony klasyfikator z listą leksemów modalnych)?
- Jakie są najczęstsze luki wykrywane przez KnowledgeGapTracker w tekstach — typ UNMATCHED_RULE (brak reguły DRL dla predykatu) dominuje (~60%), UNKNOWN_WORD/ign (~25% dla neologizmów i skrótów technicznych), UNKNOWN_STRUCTURE/brak root (~10% dla zdań eliptycznych), UNMATCHED_PREDICATE/brak synsetu (~5%); proporcje wskazują że priorytetem ML jest uzupełnianie reguł DRL?
- Wdróżmy klasę `IntentClassifier` w Fazie Green — po napisaniu czerwonego testu `assert clf.classify('Jak działa system') == 'QUESTION'`, implementacja z `QUESTION_WORDS` przechodzi; następny krok: dodaj `MODAL_WORDS = {'musi','powinien','należy'}` i test `'Należy dostarczyć' → 'REQUIREMENT'` jako kolejna iteracja RED→GREEN?
- Pokaż implementację fazy Green dla `IntentClassifier` — minimalna klasa: `class IntentClassifier: QUESTION_WORDS={'jak','czy','kiedy','co','kto'}; MODAL_WORDS={'musi','powinien','należy','wymaga'}; def classify(self, s): words=s.lower().split(); return 'REQUIREMENT' if any(w in self.MODAL_WORDS for w in words) else 'QUESTION' if words[0] in self.QUESTION_WORDS else 'ASSERT'`; wszystkie 3 testy RED przechodzą?
- Jak wdrożyć logikę FACT/REQUIREMENT w metodzie `classify()` — `if any(w in sentence for w in self.MODAL_WORDS): return 'REQUIREMENT'`; `elif sentence.split()[0].lower() in self.QUESTION_WORDS: return 'QUESTION'`; `else: return 'ASSERT'`; kolejność warunków ważna: modal check przed pytajnym?
- Jak zrefaktoryzować `IntentClassifier.classify()` z użyciem tagów morfologicznych Morfeusza — zamiast leksykalnych list słów kluczowych: `morfeusz.analyse(sentence)` → sprawdź `feats['Mood']=='Imp'` lub predykat w MODAL_LEMMAS → REQUIREMENT; `feats['Tense']=='Past'` → ASSERT; dodaj fallback do leksykalnego klasyfikatora gdy `feats` niedostępne?
- Jak rozbudować `IntentClassifier` o obsługę trybu przypuszczającego — tag Morfeusza `Mood=Cond` (np. "dostarczyłby", "mógłby") → nowa kategoria `'HYPOTHESIS'`; dodaj `elif verb and verb.feats.get('Mood')=='Cond': return 'HYPOTHESIS'` po REQUIREMENT; HYPOTHESIS pozwala Linterowi flagować warunki hipotetyczne jako potencjalne luki w wymaganiach?
- Jak rozbudować `IntentClassifier` o kolejne tagi Morfeusza — poza `Imp`/`Past`/`imps` dodaj: `Mood=Ind + Tense=Pres` → stan aktualny → `'ASSERT'`; `'qub' in t.tag` (partykuła pytajna: "czy") → `'QUESTION'`; `Aspect=Perf + Tense=Fut` → zobowiązanie przyszłe → `'REQUIREMENT'`; każdy tag mapuje na jeden z 4 typów intencji bez regex?
- Pokaż logikę Refactor dla `IntentClassifier` — wydziel prywatną metodę `_morph_classify(tokens) → Optional[str]`: zwraca klasę gdy feats jednoznaczne, `None` gdy brak pewności; `classify()` staje się `_morph_classify(tokens) or _lexical_fallback(sentence)`; metoda `_morph_classify` jest niezależnie testowalna z gotowymi listami tokenów-stubów?
- Zrefaktoryzujmy `IntentClassifier` strukturalnie: wydziel `MorphClassifier(MorphAnalyser)` + `LexicalClassifier` jako dwie strategii; `IntentClassifier.__init__(primary: MorphClassifier, fallback: LexicalClassifier)`; `classify()` próbuje `primary.classify()` — jeśli zwróci `None` (brak feats) → `fallback.classify()`; wzorzec Strategy umożliwia niezależne testowanie obu warstw?
- Zaktualizujmy metodę `classify()` o tagi `praet` i `imps` z Morfeusza — `praet` = czas przeszły (Tense=Past, Aspect=Perf/Imp) → ASSERT; `imps` = forma bezosobowa (`'imps' in t.tag`) → często REQUIREMENT (np. "dostarcza się", "podaje się"); dodaj `elif any('imps' in t.tag for t in tokens): return 'REQUIREMENT'` przed fallback lexical?
- Jak zintegrować `IntentClassifier` z modelem DeepER — po rozpoznaniu przez DeepER encji `TECHNOLOGIA` lub `ORGANIZACJA`, wzbogać `context_hint` dla `classify()`: `clf.classify(sentence, context_hint=ner_label)` → jeśli `ner_label=='TECHNOLOGIA'` i `speech_act=='REQUIREMENT'` → dodaj `domain='technical_requirement'` do EventFrame; NER wzbogaca klasyfikację intencji o domenę?
- Zaktualizujmy kod `IntentClassifier` o morfologię Morfeusza — pełna implementacja: `tokens = self._morph.analyse(sentence)`; `verb = next((t for t in tokens if 'verb' in t.pos), None)`; `if verb and verb.feats.get('Mood')=='Imp' or verb and verb.lemma in MODAL_LEMMAS: return 'REQUIREMENT'`; `elif verb and verb.feats.get('Tense')=='Past': return 'ASSERT'`; `else: return self._lexical_fallback(sentence)`?
- Czy implementujemy `IntentClassifier` z analizą tagów Morfeusza — tak: kolejność implementacji: 1) `MorphClassifier._classify_by_mood()` (Imp/Cond/Ind), 2) `._classify_by_tense()` (Past/Fut), 3) `._classify_by_pos()` (imps/qub), 4) `LexicalClassifier` jako fallback; każda sub-metoda testowana oddzielnie z `Token`-stubami bez rzeczywistego Morfeusza?
- Czy zrefaktoryzować `IntentClassifier` pod tagi Morfeusza — tak, dodaj `_classify_by_aspect(tokens)`: `Aspect=Perf+Tense=Past` → silny ASSERT (zakończony fakt); `Aspect=Imp+Tense=Pres` → stan trwający → ASSERT; `Aspect=Perf+Tense=Fut` → przyszłe zobowiązanie → REQUIREMENT; aspekt jako czwarty wymiar klasyfikacji po Mood/Tense/POS?
- Jak testować `_classify_by_aspect()` niezależnie — `def test_perf_fut_is_requirement(): tokens = [Token(lemma='dostarczyć', feats={'Aspect':'Perf','Tense':'Fut'})]; clf = MorphClassifier(None); assert clf._classify_by_aspect(tokens) == 'REQUIREMENT'`; stub tokena bez Morfeusza — izolowany test jednotkowy sub-metody?
- Jak zrefaktoryzować `IntentClassifier`, aby uniknąć fałszywych dopasowań — dodaj `confidence_threshold=0.7`; `_morph_classify()` zwraca `(label, confidence)`; gdy `confidence < threshold` → fallback do LexicalClassifier; fałszywe dopasy często: słowo `musi` w nazwie własnej (np. "firma Musi-Tech") → sprawdź POS: `label=='verb'` przed MODAL_LEMMAS check?
- Zrefaktoryzujmy `IntentClassifier` krok po kroku z tagami Morfeusza — Refactor phase po GREEN: 1) wydziel `_classify_by_mood()`, `_classify_by_tense()`, `_classify_by_aspect()`, `_classify_by_pos()` jako prywatne metody; 2) `_morph_classify()` wywołuje je w łańcuchu z `or`; 3) każda metoda zwraca `Optional[str]` — None gdy tag niedostępny; 4) `classify()` = `_morph_classify(tokens) or _lexical_fallback(sent)`?
- Jak zintegrować `IntentClassifier` z głównym pipeline'em — `SemanticMapper.__init__(intent_clf: IntentClassifier)`, po `map_roles()` wywołaj `event.speech_act = intent_clf.classify(sentence)` zanim EventFrame trafi do InferenceEngine; klasyfikator operuje na surowym zdaniu przed parsowaniem dep_rel?
- Jak KnowledgeGapTracker raportuje braki w Słowosieci — `dump_jsonl()` filtruje wpisy `type=='MISSING_SYNSET'` i eksportuje do `wordnet_gaps.jsonl`; format: `{predicate, pos, doc_id, sentence_fragment}`; plik stanowi wkład do procesu rozszerzania plWordNet o nowe leksemy techniczne?
- Jak sformatować raport luk dla błędów `MISSING_SENSE` — różnica: `MISSING_SYNSET` = brak całego synsetu dla lematu; `MISSING_SENSE` = synset istnieje ale brakuje konkretnego sensu (znaczenia) w danym kontekście domenowym; format wpisu: `{predicate, synset_id, missing_sense_gloss, domain_hint, doc_id}`; wyeksportuj jako `sense_gaps.jsonl` osobno od `wordnet_gaps.jsonl`?
- W jaki sposób silnik zamraża wniosek w macierzy stanu — `StateMatrix.freeze(fact_hash)` oznacza wniosek jako rozliczony: `self._frozen: Set[str]`; przed każdym `InferenceEngine.run()`: `if fact_hash in state_matrix._frozen: skip`; `freeze()` wywoływany po pomyślnym zapisie `AuditFinding` do Neo4j; gwarancja idempotentności — ten sam dokument audytowany dwukrotnie nie generuje duplikatów; `fact_hash = sha256(agent+action+patient+speech_act)` jako klucz deduplikacji?
- Jak zmapować taksonomię Austina na klasy `IntentClassifier` — 5 typów aktów mowy: ASSERTIVE (opis stanu → `'ASSERT'`), DIRECTIVE (nakaz → `'REQUIREMENT'`), COMMISSIVE (zobowiązanie → `'COMMITMENT'`), EXPRESSIVE (ocena → `'OPINION'`), DECLARATIVE (zmiana stanu prawnego → `'DECLARATION'`); `COMMITMENT_LEMMAS={'zobowiązuje się','dostarczy','zapewni'}`; `DECLARATIVE` gdy predykat `'niniejszym'` + orzeczenie w Pres; `COMMITMENT` kluczowy w dokumentach kontraktowych — Linter wykrywa brak `DECLARATION` potwierdzającej `COMMITMENT`?
- Jakie reguły składniowe są kluczowe dla polskiej dokumentacji technicznej — 5 wzorców dep-rel istotnych dla `DependencyParserAdapter`: (1) **nsubj** — podmiot wykonawcy (`Wykonawca dostarczył`); (2) **obj** — dopełnienie bliższe (`dostarczył dokumentację`); (3) **nmod** — modyfikator rzeczownika (`dokumentacja z opóźnieniem`); (4) **mark+advcl** — zdanie podrzędne warunkowe (`jeżeli Zamawiający potwierdzi`); (5) **aux:pass** — strona bierna (`dokumentacja została dostarczona` → agent niejawny → `Violation('ROLE-01')` gdy brak AGENT); `DepRelExtractor.extract_passive(doc)` wykrywa aux:pass i emituje `Violation` gdy `EventFrame.agent IS NULL`?
- W jaki sposób graf znaczeń rozwiązuje problem elastycznego szyku zdania — w polszczyźnie `Dokumentację dostarczył Wykonawca` ≡ `Wykonawca dostarczył dokumentację` — różny szyk, to samo znaczenie; graf koduje relacje przez etykiety krawędzi (HAS_ROLE {role:'AGENT'/'PATIENT'}) niezależnie od pozycji tokenu w zdaniu; `DependencyParserAdapter` wyciąga dep-rel (nsubj, obj) przez spaCy — pozycja nieistotna; wynik: `EventFrame.agent='Wykonawca', patient='dokumentacja'` dla obu wariantów szyku; porównaj z modelem bag-of-words: `TF-IDF('Wykonawca','dostarczył','dokumentację')` identyczny dla obu zdań, ale bez ról; graf > BoW dla tekstu prawno-kontraktowego gdzie podmiot=odpowiedzialność?
- Jakie reguły weryfikacji domenowej dodać do silnika wnioskowania — `DomainVerificationRule` jako kategoria równoległa do katalogu Lintera: `DOMAIN-01` (`MATCH (e:EventFrame) WHERE NOT e.domain IN ['API','CONTRACT','SYSTEM','INFRA','AUTH','OPS','GRAPH'] RETURN e.id`) — nieznana domena; `DOMAIN-02` (`MATCH (e1)-[:CAUSES]->(e2) WHERE e1.domain <> e2.domain AND NOT exists((e1)-[:HAS_BRIDGE_RULE]->()) RETURN e1.id, e2.id`) — cross-domain CAUSE bez reguły mostu; `DOMAIN-03` wykrywa `EventFrame.domain=NULL`; `DomainValidator(rules=[DOMAIN-01,DOMAIN-02,DOMAIN-03]).validate(session)→List[DomainViolation]`; każda nowa domena wymaga wpisu w `DOMAIN_WHITELIST` i nowego `DOMAIN-0N` testu — zamknięty katalog domen?
- Pokaż przykład reguły Freeze dla wnioskowania w `CrossReferenceEngine` — circuit-breaker dla kaskad: `@dataclass class FreezeRule: condition: Callable[[CascadeState], bool]; reason: str`; dwie gotowe instancje: `depth_freeze = FreezeRule(lambda s: s.depth >= s.depth_limit, 'DEPTH_LIMIT_REACHED')` i `cycle_freeze = FreezeRule(lambda s: s.current_node in s.visited, 'CYCLE_DETECTED')`; `CascadeEngine.step(state)` sprawdza `any(r.condition(state) for r in self.freeze_rules)` → gdy True: `state.frozen=True; Violation(cascade_type='FROZEN_CASCADE', reason=r.reason, node_id=state.current_node, severity='LOW')`; Frozen violations trafiają do osobnej sekcji raportu — nie blokują HIGH/CRITICAL; `FreezeRule` serializowalny do YAML → konfiguracja `depth_limit` i `cycle_detection` bez zmiany kodu?
- Jak zdefiniować klasy intencji dla modelu mowy — taksonomia Austin: (1) `ASSERTIVE` — opis stanu: `'Wykonawca dostarczył SRS'` → `SpeechAct.type='ASSERT'`; (2) `DIRECTIVE` — nakaz/wymóg: `'Należy dostarczyć SRS do 30.06'` → `SpeechAct.type='REQUIREMENT'`; (3) `INTERROGATIVE` — pytanie: `'Jak działa system?'` → `SpeechAct.type='QUESTION'`; (4) `COMMISSIVE` — zobowiązanie: `'Zamawiający zapewni dostęp'` → `SpeechAct.type='COMMITMENT'`; `IntentClassifier.MODAL_WORDS={'należy','musi','zobowiązuje','zapewni'}→DIRECTIVE`; fallback `'UNKNOWN'` gdy żaden wzorzec nie pasuje; `SpeechAct(type, speaker, sentence_id)` jako węzeł `(:SpeechAct)` połączony `[:HAS_SPEECH_ACT]` z `EventFrame` — rozdziela intencję od treści zdarzenia?
- Jakie reguły wnioskowania dodać do Silnika Zależności — 4 kategorie `DeductionRule`: (1) `CAUSAL_CHAIN`: `MATCH (e1)-[:CAUSES]->(e2) WHERE e1.domain=e2.domain RETURN e2.id AS derived` — propagacja naruszeń po łańcuchu przyczynowym; (2) `TEMPORAL_CONSTRAINT`: `MATCH (e)-[:HAS_ROLE {role:'TIME'}]->(t) WHERE date(t.lemma)<date() RETURN e.id` — przeterminowane zobowiązania; (3) `ROLE_COMPLETENESS`: `MATCH (e:EventFrame) WHERE NOT (e)-[:HAS_ROLE {role:'AGENT'}]->() RETURN e.id` — brak aktora; (4) `DOMAIN_CONSISTENCY`: `MATCH (e1)-[:CAUSES]->(e2) WHERE e1.domain<>e2.domain RETURN e1.id` — cross-domain bez bridge; `DeductionEngine.register(rule)→chain`; kolejność wykonania: ROLE→TEMPORAL→CAUSAL→DOMAIN?
- Jak zbudować `DeductionEngine` z metodą `register()` i łańcuchowym wykonaniem — `class DeductionEngine: def __init__(self): self._rules:List[DeductionRule]=[]; def register(self, rule:DeductionRule)->'DeductionEngine': self._rules.append(rule); return self`; metoda `apply(session)->List[Violation]`: `return [v for rule in self._rules for v in rule.run(session)]`; builder pattern: `engine = (DeductionEngine().register(RoleCompletenessRule()).register(TemporalConstraintRule()).register(CausalChainRule()).register(DomainConsistencyRule()))`; `AuditPipeline` wstrzykuje `DeductionEngine` obok `LinterRuleEngine` — osobny runner, ten sam `session`; `rule.run(session)→List[Violation]` jako interfejs — każda reguła to 1 Cypher query?
- Jak zdefiniować regułę `COMPLIANCE-01` dla zakazów bez podstawy prawnej — `class Compliance01Rule(LinterRule): id='COMPLIANCE-01'; QUERY="MATCH (s:SpeechAct {subtype:'ZAKAZ'}) WHERE NOT (s)-[:HAS_LEGAL_BASIS]->(:LegalReference) RETURN s.id AS node_id"`; `Violation('COMPLIANCE-01', node_id, severity='HIGH', domain='LEGAL')`; `(:LegalReference {id, article, act})` jako węzeł podstawy prawnej; `MERGE (s)-[:HAS_LEGAL_BASIS]->(ref)` wstawiany przez `DocumentLogicParser` gdy parser wykryje `'zgodnie z art.'` w kontekście zakazu; `COMPLIANCE-01` zamyka pętlę: `classify_directive_subtype()→ZAKAZ → COMPLIANCE-01 sprawdza podstawę → AuditReport`?
- Pokaż regułę Freezing dla `CrossReferenceEngine` w Pythonie — integracja w konstruktorze: `class CrossReferenceEngine: def __init__(self, docs, depth_limit=3, freeze_rules=None): self.freeze_rules=freeze_rules or [FreezeRule(lambda s: s.depth>=depth_limit,'DEPTH_LIMIT'),FreezeRule(lambda s: s.current_node in s.visited,'CYCLE_DETECTED')]`; użycie w `check_cascade`: `state=CascadeState(current_node=v.node_id,depth=0,visited=set()); while not state.frozen: fr=next((r for r in self.freeze_rules if r.condition(state)),None); if fr: state.frozen=True; violations.append(Violation(cascade_type='FROZEN',reason=fr.reason,severity='LOW')); break; state.visited.add(state.current_node); self._propagate(state)`; `CascadeState(current_node,depth,visited,frozen=False)` jako mutable `@dataclass`?
- Jak zdefiniować klasy intencji dla polskiego modelu mowy — polskie markery leksykalne per klasa: `DIRECTIVE` → `{'należy','musi','powinien','wymaga się','zakazuje się'}`; `COMMISSIVE` → `{'zobowiązuje się','dostarczy','zapewni','gwarantuje'}`; `DECLARATIVE` → `{'niniejszym','stwierdza się','postanawia'}`; `ASSERTIVE` → brak markera modalnego — czysty orzecznik przeszły lub teraźniejszy; wykrywanie: `IntentClassifier._match_polish(sent:str)->SpeechActType`: `for marker in DIRECTIVE_MARKERS: if marker in sent.lower(): return DIRECTIVE`; kolejność sprawdzania: DECLARATIVE → DIRECTIVE → COMMISSIVE → ASSERTIVE (malejący priorytet); `pl_core_news_lg` morfologia `Mood=Imp` jako dodatkowy sygnał DIRECTIVE?
- Jakie są 4 kluczowe reguły Event Reasoning dla grafu — reguły operujące na wzorcach `EventFrame`: (1) `OBLIGATION_CHAIN`: gdy `(e1 {type:'OBLIGATION'})-[:CAUSES]->(e2)` i `e2` bez `AGENT` → `Violation('CAUSAL-01')`; (2) `DEADLINE_PROPAGATION`: gdy `e1` ma TIME przeterminowany i `[:CAUSES]->e2` → `e2.severity` eskaluje do `HIGH`; (3) `ACTOR_CONSISTENCY`: gdy dwa `EventFrame` w tym samym łańcuchu mają różny `AGENT` bez relacji `[:DELEGATES_TO]` → `Violation('ROLE-02')`; (4) `DOMAIN_BRIDGE_CHECK`: gdy `e1.domain != e2.domain` i `(e1)-[:CAUSES]->(e2)` bez `[:HAS_BRIDGE_RULE]` → `Violation('DOMAIN-02')`; `EventReasoningEngine(rules).apply(session)→List[Violation]` — oddzielny runner od `LinterRuleEngine`?
- Stwórzmy klasyfikator intencji dla poleceń i zakazów — sub-klasyfikacja w ramach `DIRECTIVE`: `POLECENIE` gdy `Mood=Imp` lub marker `{'należy','musi','powinien'}` + brak negacji; `ZAKAZ` gdy marker `{'zakazuje się','nie wolno','zabrania się'}` lub `Mood=Imp` + `negation_token=True`; implementacja: `def classify_directive_subtype(sent:Span)->str: neg=[t for t in sent if t.dep_=='neg']; imp=[t for t in sent if t.morph.get('Mood')==['Imp']]; prohib=[t for t in sent if t.lemma_ in {'zakazywać','zabraniać','zabroniać'}]; return 'ZAKAZ' if (neg and imp) or prohib else 'POLECENIE'`; wynik wzbogaca `SpeechAct.subtype`; `ZAKAZ` generuje `Violation('COMPLIANCE-01')` gdy brak dokumentu wyjaśniającego podstawę zakazu?
- Jak zapisać intencję zdania jako węzeł `(:SpeechAct)` w Neo4j — pełny wzorzec Cypher: `MERGE (sa:SpeechAct {id:$sentence_id}) ON CREATE SET sa.type=$type, sa.subtype=$subtype, sa.speaker=$speaker, sa.confidence=$conf MERGE (e:EventFrame {id:$frame_id}) MERGE (e)-[:HAS_SPEECH_ACT]->(sa) MERGE (s:Sentence {id:$sentence_id, text:$text}) MERGE (sa)-[:EXPRESSED_IN]->(s)`; `IntentClassifier.save_to_neo4j(session, frame_id, sentence_id)` wywołuje powyższe z `{'type': self._last_type, 'subtype': self._last_subtype, 'confidence': self._last_conf}`; `confidence` = wynik `_morph_classify()` (0.0–1.0), dla leksykalnego fallback = 0.6; query agregujący: `MATCH (sa:SpeechAct) RETURN sa.type, count(*) AS n ORDER BY n DESC` — rozkład intencji w dokumencie jako metryka pokrycia klasyfikatorem?
- Jak przekazać zamrożone wnioski `FreezeRule` do `AuditReportGenerator` — `AuditReportGenerator.add_frozen_section(frozen:List[Violation])` zbiera `Violation(cascade_type='FROZEN', reason=...)` w osobną listę; `generate_markdown()` dodaje sekcję `## Wnioski zamrożone (LOW)` pod sekcją `## Kaskady grafowe`, format: tabela `|node_id|reason|depth_at_freeze|`; `generate_json()` zwraca `report['frozen_violations']` oddzielnie od `report['violations']` i `report['cascades']`; `AuditPipeline.run()` aktualizowany: `frozen=[v for v in all_violations if v.cascade_type=='FROZEN']; generator.add_frozen_section(frozen)` przed `generate_markdown()`; operatorzy widzą gdzie silnik zatrzymał kaskadę i dlaczego (`DEPTH_LIMIT_REACHED` vs `CYCLE_DETECTED`) — przezroczystość zamrażania jako audit trail?
- Pokaż kod klasyfikatora intencji dla zdań trybu warunkowego — `Mood=Cond` (`'dostarczyłby'`) + leksykalne markery `{'jeżeli','o ile','pod warunkiem','w przypadku gdy'}` → klasa `CONDITIONAL_OBLIGATION`; implementacja: `def _classify_conditional(sent:Span)->Optional[str]: markers=['jeżeli','o ile','pod warunkiem','w przypadku gdy']; has_marker=any(m in sent.text.lower() for m in markers); has_cond_mood=any(t.morph.get('Mood')==['Cond'] for t in sent); return 'CONDITIONAL_OBLIGATION' if has_marker or has_cond_mood else None`; wywołanie w łańcuchu PRZED `DIRECTIVE` — `'musi dostarczyć o ile...'` → CONDITIONAL, nie DIRECTIVE; `SpeechAct(type='CONDITIONAL_OBLIGATION', condition_text=subclause_span.text)` gdzie `subclause_span` to `mark+advcl` zależność; Linter reguła `COND-01`: każdy `CONDITIONAL_OBLIGATION` musi mieć węzeł `(:TriggerCondition)` powiązany relacją `[:ACTIVATED_BY]`?
- Jak zmapować intencję 'prewencja' na regułę walidacyjną w silniku wnioskowania — reguła `MEDICAL-01`: `class Medical01Rule(LinterRule): id='MEDICAL-01'; QUERY="MATCH (e:EventFrame {intent:'PREVENTION'})-[:TRIGGERS_PROTOCOL]->(p:MedicalProtocol) WHERE NOT (e)-[:HAS_AUTHORIZATION]->(:AuthorizationDocument) RETURN e.id AS node_id"`; `Violation('MEDICAL-01', node_id, severity='HIGH', domain='MEDICAL')`; `(:AuthorizationDocument {type:'MEDICAL_APPROVAL', issuer:$issuer})` analogiczne do `LegalReference`; wzorzec reużywalny: każda dziedzina (MEDICAL/LEGAL/SECURITY) ma własny `(:ComplianceDocument)` subtype i regułę `{DOMAIN}-01` sprawdzającą obecność autoryzacji; `DeductionEngine.register(Medical01Rule())` dodaje nową domenę bez zmiany rdzenia silnika?
- Czy klasyfikator intencji obsługuje polskie formy trybu rozkazującego — tak, ale wymagane 3 wzorce poza `Mood=Imp`: (1) `niech + 3p verb` (np. "niech Wykonawca dostarczy") — `t.lemma_=='niech'` + następny token `Mood=Ind, Tense=Pres, Person=3` → `DIRECTIVE`; (2) `proszę + infinitiv` (np. "proszę dostarczyć SRS") — `t.lemma_=='proszić'` + następny `Verbform=Inf` → `DIRECTIVE` (polite imperative, wyższy formalizm); (3) `precz z + noun` → `EXPRESSIVE_COMMAND`; `_classify_by_mood()` sprawdza te wzorce PRZED leksykalnym fallbackiem; fałszywy alarm: "musi-Tech dostarcza" — POS guard `t.pos_=='VERB'` przed sprawdzeniem `Mood=Imp` odfiltruje `'musi-'` w nazwie własnej?
- Jak zmniejszyć złożoność analizy polszczyzny o 80% przez dekompozycję pipeline'u — strategia 3-poziomowa: (1) **Poziom fast** (`fast_mode`): `disable=['ner','senter','attribute_ruler']` + `SlowosiecProxy(None)` (brak wordnet) — dla wstępnej klasyfikacji DIRECTIVE/ASSERTIVE, ~3000 zdań/s; (2) **Poziom standard**: pełne `pl_core_news_lg` + `SlowosiecProxy(Neo4jAdapter)` z TTL cache — dla EventFrame extraction, ~800 zdań/s; (3) **Poziom deep**: standard + `Neo4jWordnetAdapter([:HYPERNYM*1..3])` + `DeductionEngine.register(4 reguły)` — dla pełnego audytu, ~150 zdań/s; `NLPPipeline.select_level(doc_complexity)` automatycznie wybiera poziom na podstawie liczby zdań i domeny dokumentu; eliminuje zbędne wywołania Słowosieci dla prostych dokumentów operacyjnych?
- Pokaż jak zdefiniować regułę SEC-03 dla wymogu szyfrowania bazy — `class Sec03Rule(LinterRule): id='SEC-03'; SEVERITY='CRITICAL'; QUERY="MATCH (db:Database) WHERE NOT (db)-[:ENCRYPTED_WITH]->(:EncryptionConfig) OR (db)-[:ENCRYPTED_WITH]->(c:EncryptionConfig) WHERE NOT c.algorithm IN ['AES-256','ChaCha20-Poly1305'] RETURN db.id AS node_id"`; `Violation('SEC-03', node_id, severity='CRITICAL', domain='SECURITY')`; `(:EncryptionConfig {algorithm, key_length:int, rotation_days:int})` jako węzeł konfiguracji szyfrowania; seed fixture: `MERGE (:Database {id:'db_prod'})-[:ENCRYPTED_WITH]->(:EncryptionConfig {algorithm:'AES-256', key_length:256, rotation_days:90})`; SEC-03 `CRITICAL` blokuje release — `AuditPipeline.run()` ustawia `report['release_blocked']=True` gdy violation `severity=='CRITICAL'`?
- Jakie reguły wnioskowania dodać dla domeny bezpieczeństwa — triadę SEC-03/04/05: `SEC-03` (baza nieszyfrowana — CRITICAL); `SEC-04`: `MATCH (e:EventFrame {domain:'SECURITY'})-[:HAS_ROLE {role:'INSTRUMENT'}]->(t:Token) WHERE t.lemma_ IN ['HTTP','FTP','Telnet'] RETURN e.id` — nieszyfrowany kanał transmisji → `Violation('SEC-04', severity='HIGH')`; `SEC-05`: `MATCH (e:EventFrame) WHERE e.domain='SENSITIVE_DATA' AND NOT (e)-[:HAS_AUDIT_LOG]->() RETURN e.id` — brak logu audytu dla danych wrażliwych → `Violation('SEC-05', severity='HIGH')`; `DeductionEngine.register(Sec03Rule()).register(Sec04Rule()).register(Sec05Rule())` zamyka domenę SEC; SEC-06 proaktywnie: brak `[:ROLE_BASED_ACCESS]` na węźle `(:Database {classification:'SENSITIVE'})` → CRITICAL?
- Stwórzmy listę reguł dla klasy intencji Polecenie z priorytetami — `POL_RULES: OrderedDict = {'Mood=Imp+no_neg': ('POLECENIE', 1.0), 'modal_pos+no_neg': ('POLECENIE', 0.8), 'niech_3p': ('POLECENIE', 0.7), 'proszę_inf': ('POLECENIE', 0.6), 'Mood=Imp+neg': ('ZAKAZ', 1.0), 'zakaz_marker': ('ZAKAZ', 0.95), 'prohib_verb': ('ZAKAZ', 0.9)}`; `classify_directive_subtype(sent)`: iteruje od najwyższego priorytetu, zwraca pierwszy match z confidence; macierz testowa: 7 reguł × 2 wyniki = 14 przypadków testowych; priorytet MORFOLOGICZNY przed LEKSYKALNYM — `Mood=Imp` zawsze wygrywa z markerem `'należy'`; `SpeechAct(subtype='POLECENIE', confidence=0.8)` gdy `modal_pos` — raport wyróżnia pewne polecenia (conf≥0.9) od probabilistycznych (conf<0.9)?
- Pokaż przykład analizy tematyzacji temat-rema w grafie semantycznym — `SemanticMapper` po ekstrakcji AAO dołącza `EventFrame.cohesion_score: float = 0.0`; algorytm: sekwencja `[e1, e2, e3, ...]` — gdy `e_i.theme_topic == e_{i+1}.theme_topic` → `e_{i+1}.cohesion_score += 0.1`; `CohesionAnalyzer.analyze(frames:List[EventFrame])->float` = `mean(f.cohesion_score for f in frames)`; `Violation('COHESION-01', severity='LOW')` gdy `mean_score < 0.3` dla sekwencji ≥5 ramek — dokument bez ciągłości tematycznej; `TOPICALLY_RELATED` chain: `MATCH (e1)-[:TOPICALLY_RELATED*1..5]->(e5) RETURN count(e5) AS chain_length` — długie łańcuchy = spójny dyskurs; `AuditReport` nowa sekcja `## Spójność Dyskursu`: `{chain_count:int, mean_cohesion:float, violations_cohesion_01:int}`; polskie cleft `'To Wykonawca dostarczył SRS'` odwraca tema/remat ale zachowuje spójność dyskursu — `TOPICALLY_RELATED` wykrywa ciągłość nawet przy inwersji tematycznej?
- Jakie reguły wnioskowania dodać dla wymiarów przyczyna i narzędzie — `INSTR-01`: `MATCH (e:EventFrame)-[:HAS_ROLE {role:'INSTRUMENT'}]->(t:Token) WHERE t.ent_type IN ['TECH_TOOL','TECH_DB'] AND NOT (t)-[:HAS_VERSION]->() RETURN t.lemma AS node_id` → `Violation('INSTR-01', severity='LOW', details={'reason':'tool_without_version'})` — narzędzie techniczne bez wersji w dokumentacji; `CAUSAL-01`: `MATCH (e:EventFrame) WHERE e.speech_act='ASSERT' AND e.predicate IN ['awaria','nie działać','nie przetwarza'] AND NOT (e)-[:CAUSED_BY]->() RETURN e.id` → `Violation('CAUSAL-01', severity='MEDIUM')` — zdarzenie awaryjne bez przyczyny w grafie; `CAUSAL-02`: `MATCH (e1)-[:CAUSED_BY]->(e2) WHERE e1.domain != e2.domain RETURN e1.id` → CROSS_DOMAIN_CAUSE → `severity='HIGH'` gdy przyczyna z domeny INFRA dla zdarzenia CONTRACT; `DeductionEngine.register(Instr01Rule()).register(Causal01Rule()).register(Causal02Rule())`; `e.cause_dimension = causal_marker_detection(sent, ['ponieważ','bo','dlatego że'])` w `SemanticMapper` ustawia `[:CAUSED_BY]` przy zapisie?
- Jakie reguły w spaCy pomogą wykrywać tryb rozkazujący i zakazy — `DIRECTIVE_MATCHER = Matcher(nlp.vocab)`; wzorzec rozkazujący: `DIRECTIVE_MATCHER.add('POLECENIE_IMP', [[{'MORPH': {'IN': ['Mood=Imp']}}]])`; wzorzec modalny: `DIRECTIVE_MATCHER.add('POLECENIE_MODAL', [[{'LEMMA': {'IN': ['należeć','musieć','powinien']}}, {'DEP':'xcomp', 'MORPH':{'IN':['VerbForm=Inf']}}]])`; wzorzec zakazu: `DIRECTIVE_MATCHER.add('ZAKAZ', [[{'LEMMA': {'IN': ['zakazywać','zabraniać']}}, {'OP':'?'}], [{'LOWER':'nie'},{'LOWER':'wolno'}]])`; `DirectiveMatcher.match(doc)->List[SpeechAct]` = `DIRECTIVE_MATCHER(doc)` → `SpeechAct(subtype=match_id, confidence=POL_RULES[match_id][1])`; `@Language.component('directive_matcher') def apply_dm(doc): doc._.speech_acts.extend(dm.match(doc)); return doc`; `nlp.add_pipe('directive_matcher', after='intent_clf')` — Matcher + morfologia = dwa niezależne sygnały potwierdzające tę samą intencję; `confidence = max(morph_conf, pattern_conf)` gdy oba matchują?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `InferenceEngine` — `"Wykonawca dostarczył dokumentację z opóźnieniem"` → `{cons: CONS-02, rule: naruszenie_terminu}`?
- Zdefiniujmy testy RED dla Klasyfikatora Intencji — `def test_question_detected(): assert IntentClassifier().classify('Jak działa system?') == 'QUESTION'`; `def test_requirement_detected(): assert IntentClassifier().classify('Należy dostarczyć SRS') == 'REQUIREMENT'`; `def test_fact_detected(): assert IntentClassifier().classify('Wykonawca dostarczył dokumentację') == 'ASSERT'`; wszystkie RED przed implementacją MODAL_WORDS?
- Jak testować wielowymiarowy model zdarzenia: AGENT + ACTION + PATIENT + INSTRUMENT + LOCATION + TIME?
- Jak testować negację: `"Wykonawca nie dostarczył dokumentacji"` → `dostawa=NOT_OCCURRED`?
- Jak testować łańcuch: zdanie 1 = "Wykonawca złożył ofertę", zdanie 2 = "Wykonawca dostarczył dokumentację z opóźnieniem" → wnioskowanie o naruszeniu?
- Uruchommy testy integracyjne dla całego pipeline'u z klasyfikatorem — `def test_full_pipeline_with_intent_classifier(): clf = IntentClassifier(MorphClassifier(morph_stub), LexicalClassifier()); mapper = SemanticMapper(intent_clf=clf); frame = mapper.process('Wykonawca musi dostarczyć SRS'); assert frame.speech_act == 'REQUIREMENT'`; test integracyjny łączy Morfeusz→IntentClassifier→SemanticMapper→EventFrame w jednym call?
- Uruchommy testy integracyjne dla warstwy pragmatycznej — `@pytest.mark.integration def test_pragmatic_layer_pipeline(): clf = IntentClassifier(MorphClassifier(morph_real), LexicalClassifier()); speech_acts = [clf.classify(s) for s in PRAGMATIC_CORPUS]; assert speech_acts.count('REQUIREMENT') >= 3; assert speech_acts.count('QUESTION') >= 2`; `PRAGMATIC_CORPUS` = 10 zdań kontraktowych + pytań; walidacja rozkładu intencji jako test własnościowy warstwy pragmatycznej; RED bo `morph_real` wymaga uruchomionego Morfeusza?
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
