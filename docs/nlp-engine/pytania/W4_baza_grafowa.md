---
layer: W4
title: "Warstwa 4 — Baza Grafowa (Neo4j / ArangoDB)"
phase: 4
status: planned
docs_version: 1.0.0
tags: [neo4j, arangodb, cypher, apoc, GraphDatabaseAdapter, graph, ontologia]
---

# Warstwa 4 — Baza Grafowa (Neo4j / ArangoDB)

## Przegląd

Warstwa 4 zarządza persystencją wiedzy w grafowej bazie danych.
Przyjmuje `EventRoleDict` z W2, `EnrichedToken` z W3, wyniki koreferencji z W6
i zapisuje je jako węzły i krawędzie w Neo4j (lub ArangoDB jako alternatywa).

Kluczowa klasa: `GraphDatabaseAdapter` z metodą `generate_cypher()`.

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W4 istnieje bo wnioskowanie W5 wymaga łączenia faktów z WIELU zdań i WIELU dokumentów. Relacyjna baza danych (SQL) nie obsługuje wydajnie zapytań o ścieżki: "znajdź wszystkich AGENT którzy wykonali akcję należącą do kategorii `działanie_niebezpieczne` z INSTRUMENT należącym do `narzędzie_ostre` w dowolnej liczbie zdań w dokumencie". Graf Neo4j wyraża to jednym zapytaniem Cypher. Ponadto W4 scala węzły z W6 (koreferencja) — "Jan" i "on" w różnych zdaniach to jeden węzeł, nie dwa.

**Co się sypie bez tej warstwy:**
- W5 musi trzymać całą historię zdarzeń w pamięci — brak persystencji między sesjami; duże dokumenty (1000+ zdań) powodują OOM
- Scalanie koreferencji: "Jan" w zdaniu 1 i "on" w zdaniu 15 to dwa osobne byty — W5 nie może połączyć zdarzeń tej samej osoby
- W8 nie może odpytać historii: "ile razy Jan był AGENT działania niebezpiecznego w tym dokumencie?"

**Zależności:**
- Wchodzi z W2: `EventRoleDict` — węzły zdarzeń i krawędzie semantyczne
- Wchodzi z W3: `EnrichedToken.hypernyms` — krawędzie ontologiczne `IS_A`, `HAS_SYNSET`
- Wchodzi z W6: `CoreferenceChain` — scalanie węzłów per osoba/byt
- Wychodzi do W5: grafowalny model wiedzy, odpytywalny Cypher
- Wychodzi do W8: persystentna historia zdarzeń dla `AuditEngine`

## Diagram przepływu danych

```
EventRoleDict (z W2)
EnrichedToken (z W3)
CoreferenceChain (z W6)
       │
  GraphDatabaseAdapter
  ┌─────────────────────────────────┐
  │  generate_cypher()              │
  │  build_document(sentences)      │
  │  merge_nodes(entity, synset_id) │
  └─────────────────────────────────┘
       │
       ▼
  Neo4j / ArangoDB
  ┌────────────────────────────────────────────────┐
  │ (:Concept {id, lemma, synset_id, pos})       │
  │ (:Event {action, tense, voice})              │
  │ (:Sentence {text, doc_id, sent_id})          │
  │ ─[:AGENT]─> ─[:PATIENT]─> ─[:INSTRUMENT]─>    │
  │ ─[:IS_A]─>  ─[:HAS_PART]─> ─[:LOCATED_IN]─>  │
  └────────────────────────────────────────────────┘
       │
       ▼
  W5 (InferenceEngine — zapytania Cypher)
  W8 (AuditEngine — raporty)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Pokaż jak zaprojektować wewnętrzny format reprezentacji znaczenia zdania.
- Pokaż jak zaprojektować wewnętrzny format reprezentacji znaczenia dla grafu..
- Jak zaprojektować ten wewnętrzny format reprezentacji znaczenia zdania?
- Jak zaprojektować wewnętrzny format reprezentacji znaczenia dla grafu?
- Jak zaprojektować format reprezentacji znaczenia, by uniknąć tych barier?
- Przejdźmy do Fazy 2: zaprojektuj strukturę węzłów Grafu Wiedzy..
- Jak zaprojektować wewnętrzny format reprezentacji znaczenia zdania?
- Pokaż strukturę tabel i indeksów dla inżynierskiej bazy grafowej..
- Przejdźmy do zamiany słownika ról na strukturę grafową..
- Jak zapisać wielowymiarowy graf zdarzenia w strukturze bazy Neo4j?
- Zaprojektuj strukturę bazy Neo4j dla grafu przyczynowego — węzły :EventFrame, :Concept, :Synset i krawędzie :CAUSES, :IS_A, :HAS_ROLE?
- Jak wygląda ontologia zdarzeń w Neo4j — jakie typy węzłów i relacji są konieczne dla compliance dokumentów prawnych?
- Jak odróżnić węzeł :EventFrame (konkretne zdarzenie z dokumentu) od :Concept (abstrakcyjna klasa) w grafie Neo4j?
- Jak zdefiniować hierarchię ontologiczną zdarzeń — :EventFrame IS_A :Concept IS_A :OntologyClass?
- Jak modelować proweniencję zdarzenia w ontologii — węzeł :Document połączony z :EventFrame przez krawędź :CONTAINS?
- Jak obsłużyć zmiany wersji ontologii (v1→v2 nowy typ węzła) bez utraty istniejących krawędzi w Neo4j?
- Jak modelować kauzalność dwukierunkową (A :CAUSES B i B :CAUSES A) — wykrycie cyklu i decyzja architektoniczna?
- Jakie indeksy (INDEX) stworzyć w Neo4j dla wydajnych zapytań compliance — po source_doc_id i predicate?
- Jak ograniczyć wykładniczy wzrost kombinacji węzłów ontologii — strategia flat hierarchy zamiast pełnego drzewa hiperonimii?
- Jak wybrać głębokość drzewa hiperonimii do importu — MAX_DEPTH=3 zamiast pełnego WordNet hierarchy?
- Podaj kompletny przykład ontologii 3-poziomowej: :OntologyClass('działanie')→:Concept('dostarczyć')→:EventFrame(id='e01')?
- Jak modelować ontologię zdarzeń by uniknąć wykładniczego wzrostu kombinacji — stosuj Event Type Hierarchy zamiast ad-hoc relacji: :EventType('naruszenie') jako nadklasa dla :EventType('niedostarczenie')?
- Jak ograniczyć liczbę typów ról per :EventFrame do stałego zestawu 6 ról (AGENT/PATIENT/INSTRUMENT/LOCATION/TIME/MANNER) zamiast nieskończonej listy relacji ad-hoc?
- Jak walidować że nowy :EventFrame nie przekracza dozwolonej liczby węzłów per zdanie — APOC constraint max_roles_per_event = 6 zamiast dowolnej liczby?

### 2. Kontrakty danych
- Jak zapisać węzeł pojęcia w formacie JSON dla grafu?
- Jak zapisać model danych grafu dla zdania o Janie w JSON?
- Pokaż schemat fizycznej bazy danych dla relacji semantycznych..
- Jak załadować takie pliki JSON bezpośrednio do bazy Neo4j?
- Jak zintegrować bibliotekę jsonschema z bazą grafową Neo4j?
- Pokaż jak zintegrować format TEI P5 z bazą Neo4j..
- Jak APOC przyspiesza import JSON do bazy Neo4j?
- Jak reprezentować relację synsetową IS_A jako krawędź w grafie Neo4j — węzeł :Concept i krawędź :IS_A z właściwościami?
- Jak zdefiniować schemat węzła :Synset w Neo4j — właściwości id, name, pos, definition, source (Słowosieć/WordNet)?
- Jak zapobiec eksplozji grafu gdy każdy token importuje pełne drzewo hiperonimii (setki węzłów per token)?
- Jaki jest schemat węzła :EventFrame w Neo4j — właściwości: id, predicate, source_doc_id, timestamp, confidence?
- Jak zdefiniować schemat krawędzi :CAUSES — właściwości: rule_id, confidence, evidence_sentence?
- Jak zdefiniować schemat węzła :Synset w grafie przyczynowym — id, name, pos, synset_id ze Słowosieci?
- Jakie ograniczenia (CONSTRAINT) założyć na węzłach :EventFrame — UNIQUE na id, NOT NULL na predicate?
- Jak zdefiniować schemat krawędzi :HAS_ROLE w Neo4j — właściwości: role_type (AGENT/PATIENT/INSTRUMENT), confidence?
- Jak reprezentować wieloznaczność tokena w schemacie — węzeł :Token połączony z wieloma :Synset przez :HAS_CANDIDATE z wagą?
- Jak zweryfikować schemat grafu przed importem — constraint validation przez APOC.meta.schema?

### 3. Implementacja
- Pokaż dokładny model danych grafu dla przykładu z Janem..
- Jakie są 40-60 relacji semantycznych do grafu wiedzy?
- Jakie są 40-60 relacji semantycznych kluczowych dla grafu wiedzy?
- Przejdźmy do Fazy 2: Jak zamienić drzewo składniowe w graf relacji?
- Przejdźmy do Fazy 2: budowa grafu relacji semantycznych..
- Jak zapisać relacje agent-pacjent w bazie Neo4j?
- Jak zarządzać eksplozją ontologii przy modelowaniu 50 relacji?
- Pokaż jak napisać regułę w Cypher do ujednoznaczniania synsetów..
- Pokaż jak zaimplementować wielowymiarowy węzeł zdarzenia w Neo4j..
- Pokaż przykład reguły ujednoznaczniającej synset w Neo4j..
- Jak zapisać regułę ujednoznaczniania synsetów w Cypher?
- Pokaż jak napisać regułę Cypher odrzucającą niepasujące synsety..
- Pokaż przykład reguły w Neo4j odrzucającej niepasujące znaczenia..
- Jakie są najczęstsze błędy przy budowie ontologii w Neo4j?
- Pokaż model relacji dla grafu wiedzy w formacie Cypher..
- Pokaż listę 50 podstawowych relacji semantycznych dla grafu..
- Jak zmapować relacje z NKJP do bazy Neo4j?
- Pokaż listę 50 relacji semantycznych dla grafu wiedzy..
- Pokaż listę 50 relacji semantycznych dla grafu zdarzeń..
- Pokaż jak zapisać ten graf semantyczny w bazie Neo4j..
- Pokaż 50 podstawowych relacji semantycznych dla grafu wiedzy..
- Przejdźmy do Fazy 2 - Jak zamienić drzewo składniowe w graf relacji.
- Jak zapisać ujednoznaczniony synset Słowosieci w bazie Neo4j?
- Ustalmy czy lepszym silnikiem dla grafu będzie Neo4j czy ArangoDB.
- Pokaż model relacji w Cypher dla AGENT i PATIENT..
- Jak połączyć WSD ze Słowosieci z modelem bazy Neo4j?
- Jak zaimplementować pętlę generującą węzły i krawędzie w Cypher?
- Jakie są różnice między Neo4j a ArangoDB w tym projekcie?
- Jak stworzyć generator zapytań Cypher dla relacji semantycznych?
- Jakie reguły MERGE zastosować w Neo4j dla synsetów?
- Zaimplementujmy metodę build_document w GraphBuilderze.
- Pokaż skrypt integrujący Słowosieć z Neo4j..
- Pokaż skrypt Python importujący synsety Słowosieci do Neo4j..
- Jak wczytać hiperonimię ze Słowosieci do grafu Neo4j?
- Jak wczytać pliki relacji semantycznych do bazy Neo4j?
- Pokaż jak zoptymalizować import miliona relacji hiperonimii do Neo4j..
- Jak w Neo4j wykrywać sprzeczne relacje w modelu zdarzenia?
- Pokaż skrypt Python mapujący synsety Słowosieci na krawędzie Cypher..
- Pokaż implementację wyszukiwarki faktów w Cypherze..
- Jak modelować wielowymiarowy kontekst zdarzenia w grafie Neo4j?
- Jak zamodelować SituationalContext w Neo4j — właściwości `temporal`, `spatial`, `speech_act` bezpośrednio na węźle :EventFrame, lub osobny węzeł :Context z krawędzią :HAS_CONTEXT?
- Jak zapytać Cypher o zdarzenia z temporal='BEFORE' i speech_act='ZOBOWIĄZANIE' — MATCH (e:EventFrame)-[:HAS_CONTEXT]->(c:Context {temporal:'BEFORE', speech_act:'ZOBOWIĄZANIE'}) RETURN e?
- Pokaż implementację wyszukiwania w Neo4j dla pytań o lokalizację..
- Jak zaimplementować wyszukiwanie wzorca z pytajnikiem w Neo4j?
- Pokaż implementację wyszukiwarki Cypher dla intencji QUESTION..
- Pokaż Cypher CREATE CONSTRAINT UNIQUE dla węzła :EventFrame(id) i :Synset(synset_id)?
- Jak stworzyć indeks pełnotekstowy (fulltext index) na właściwości predicate węzłów :EventFrame?
- Jak zaimportować ontologię zdarzeń compliance do Neo4j używając APOC.load.json z pliku seed?
- Jak napisać Cypher który zwraca pełny łańcuch przyczynowy od węzła :EventFrame do korzenia ontologii?
- Jak zapytać Neo4j o wszystkie :EventFrame połączone krawędzią :CAUSES w łańcuchu A→B→C→D?
- Pokaż skrypt Python importujący synsety Słowosieci do Neo4j — parsowanie API/XML i UNWIND MERGE Cypher?
- Jak obsłużyć aktualizację Słowosieci (nowa wersja) w Neo4j — MERGE upsert czy usunięcie i reimport?
- Jak zweryfikować kompletność importu Słowosieci — porównaj liczbę synsetów w Neo4j z liczbą w źródle?
- Jak napisać zapytanie Cypher które zwraca łańcuch :CAUSES jako listę par (source, target) do Mermaid serializacji?
- Jak zbudować Mermaid.js diagram z wyników Cypher — Python f-string template dla `flowchart LR`?
- Wygeneruj przykładowy diagram Mermaid.js dla łańcucha compliance: 'dostarcza towar' :CAUSES 'potwierdza odbiór' :CAUSES 'wystawia fakturę'?
- Jak reprezentować w Mermaid.js węzeł :EventFrame z atrybutem rule_id — etykieta węzła jako "EventFrame.id [CONS-02]"?
- Jak zaimportować plik plWordNet LMF XML do Neo4j — skrypt Python z iterparse + UNWIND + MERGE Cypher?
- Jak zmapować elementy LMF XML na węzły Neo4j — LexicalEntry→:Lemma, Synset→:Synset, SynsetRelation→:IS_A?
- Jak zweryfikować poprawność importu plWordNet — sprawdź że liczba węzłów :Synset = liczba <Synset> w XML?
- Pokaż przykład łańcucha przyczynowego w Neo4j dla zdarzenia krytycznego CONS-02 — węzły :EventFrame(predicate:'nie dostarczyć', severity:'CRITICAL') powiązane krawędziami :CAUSES?
- Jak zwizualizować pełny łańcuch przyczynowy dla zdarzenia krytycznego — Cypher: MATCH path=(e:EventFrame)-[:CAUSES*1..5]->(:EventFrame) WHERE e.severity='CRITICAL' RETURN path?
- Jak reprezentować zdarzenie krytyczne w grafie — atrybut severity:'CRITICAL' na węźle :EventFrame czy osobna etykieta :CriticalEvent?
- Pokaż jak wygenerować graf łańcuchów kauzalnych w Mermaid.js — Python skrypt pobiera wyniki Cypher MATCH path=(:EventFrame)-[:CAUSES*]->(:EventFrame) i serializuje jako flowchart LR?
- Jak obsłużyć pusty łańcuch kauzalny (brak krawędzi :CAUSES) w generatorze Mermaid — fallback: diagram z jednym węzłem i komentarzem "brak łańcucha przyczynowego"?
- Jak zmapować wymiar intencji (speech_act: ZOBOWIĄZANIE) na krawędź Neo4j — :EventFrame -[:HAS_SPEECH_ACT]-> :SpeechAct {type: 'ZOBOWIĄZANIE'}?
- Jak zintegrować `IntentClassifier` z warstwą grafu Neo4j — po `clf.classify(sentence)` wynik trafia jako `speech_act_type` do `Neo4jAdapter.save_event(frame)`; adapter tworzy `MERGE (:SpeechAct {type: $speech_act}) WITH s MERGE (e)-[:HAS_SPEECH_ACT]->(s)`; spajanie IntentClassifier→EventFrame.speech_act→Neo4j `:HAS_SPEECH_ACT` zamyka pętlę pipeline→graf?
- Jak zmapować wymiar narzędzia (INSTRUMENT) na krawędź Neo4j — :EventFrame -[:HAS_ROLE {role: 'INSTRUMENT'}]-> :Token {lemma: ...}?
- Jak modelować wymiary intencji i narzędzia łącznie w grafie zdarzeń — węzeł :EventFrame z krawędziami :HAS_SPEECH_ACT→:SpeechAct {type:'ZOBOWIĄZANIE'} i :HAS_ROLE {role:'INSTRUMENT'}→:Token; Cypher: `MATCH (e)-[:HAS_SPEECH_ACT]->(s), (e)-[:HAS_ROLE {role:'INSTRUMENT'}]->(t) WHERE s.type='ZOBOWIĄZANIE' RETURN e, t` dla audytu narzędzi zobowiązania?
- Jak modelować wymiary przyczyny i narzędzia łącznie w grafie Neo4j — węzeł :EventFrame z krawędziami :CAUSES→:EventFrame (relacja kauzalna) i :HAS_ROLE {role:'INSTRUMENT'}→:Token; Cypher: `MATCH (cause:EventFrame)-[:CAUSES]->(effect:EventFrame), (cause)-[:HAS_ROLE {role:'INSTRUMENT'}]->(t:Token) RETURN cause.predicate, t.lemma, effect.predicate` dla analizy jakim narzędziem wywołano skutek?
- Jak zapytać Cypher o wszystkie EventFrame z INSTRUMENT należącym do klasy 'narzędzie' — MATCH (e:EventFrame)-[:HAS_ROLE {role:'INSTRUMENT'}]->(t:Token)-[:HAS_SYNSET]->(:Synset)-[:IS_A*]->(:OntologyClass {name:'narzędzie'}) RETURN e?
- Jak rozszerzyć Cypher o wymiary instrumentu i lokalizacji łącznie — `MATCH (e:EventFrame)-[:HAS_ROLE {role:'INSTRUMENT'}]->(t:Token), (e)-[:HAS_ROLE {role:'LOCATION'}]->(l:Token) RETURN e.predicate, t.lemma, l.lemma`; obydwa wymiary jako `:HAS_ROLE {role:...}` dają jednolity schemat relacyjny bez mnożenia typów krawędzi?
- Jak wdrożyć warunek logiczny (CONDITION) w grafie przyczynowym — węzeł `:Condition {expr: 'termin_minął==True'}` połączony krawędzią `:REQUIRES_CONDITION`; Cypher: `MATCH (e:EventFrame)-[:CAUSES]->(eff) WHERE NOT (e)-[:REQUIRES_CONDITION]->(:Condition {satisfied:True}) RETURN eff` filtruje efekty których warunek wstępny nie jest spełniony?
- Pokaż przykład zapytania Cypher do wykrywania węzłów-orfanów :EventFrame — MATCH (e:EventFrame) WHERE NOT (e)-[:CAUSES]->() AND NOT ()-[:CAUSES]->(e) RETURN e?
- Jak wykryć orfany :Synset niepowiązane z żadnym :EventFrame — MATCH (s:Synset) WHERE NOT ()-[:HAS_SYNSET]->(s) AND NOT (s)-[:IS_A]->() RETURN s?
- Jak zaplanować cykliczne oczyszczanie orfanów w Neo4j przez APOC — `CALL apoc.periodic.iterate('MATCH (e:EventFrame) WHERE NOT (e)-[:CAUSES|HAS_SYNSET|HAS_ROLE]-() RETURN e', 'DELETE e', {batchSize:100})`?
- Jak zintegrować wykrywanie orfanów jako krok CI/CD — po każdym imporcie uruchom Cypher orphan-check w skrypcie Python i zwróć exit 1 gdy `count(orphans) > 0`?
- Jak monitorować orfany jako metrykę SLI — `MATCH (e:EventFrame) WHERE NOT (e)-[:CAUSES|HAS_SYNSET|HAS_ROLE]-() RETURN count(e)` eksportowany cyklicznie do Grafana/Prometheus?
- Czy Neo4j pozwala na constraint zapobiegający tworzeniu orfanów :EventFrame — brak natywnych relacyjnych constraints w Neo4j; alternatywa to APOC trigger `apoc.trigger.add` wywołujący rollback gdy węzeł bez krawędzi?
- Jak połączyć Słowosieć z grafem przyczynowym w Neo4j — MERGE (e:EventFrame {id: $id})-[:HAS_SYNSET]->(s:Synset {synset_id: $synset_id}) po imporcie każdego zdarzenia z SemanticMapper?
- Jak weryfikować że :EventFrame.predicate ma zmapowany :Synset — MATCH (e:EventFrame) WHERE NOT (e)-[:HAS_SYNSET]->(:Synset) RETURN e jako raport brakujących mappingów predykatów?

### 4. Testowanie
- Jak zapisać węzeł „Test jednostkowy” w formacie ontologii JSON?
- Jak zapisać węzeł „Test jednostkowy” w formacie JSON?
- Napiszmy test dla adaptera bazy grafowej w Fazie 4..
- Stwórzmy teraz testy dla Fazy 4: Baza grafowa..
- Stwórzmy czerwony test dla GraphDatabaseAdaptera w Cypher.
- Napiszmy czerwony test dla Neo4jAdapter w Fazie 4..
- Stwórzmy teraz czerwony test dla metody generate_cypher().

### 5. Obsługa błędów
_brak pytań źródłowych w tej kategorii_
- Jak obsługiwać konflikt MERGE gdy ten sam węzeł jest dodawany równolegle przez dwa procesy (race condition)?
- Jak obsłużyć błąd zapisu do Neo4j — retry, dead letter queue, czy odrzucenie dokumentu?
- Co zwrócić przy próbie odczytu węzła który nie istnieje w grafie — null, wyjątek, czy pusty wynik?
- Jak logować failed transactions do bazy grafowej bez blokowania głównego pipeline?
- Jak obsłużyć przekroczenie limitu pamięci heap Neo4j przy dużym zapytaniu APOC?

### 6. Integracja z innymi warstwami
- Pokaż jak zintegrować Słowosieć z grafem wiedzy w Neo4j..
- Jak zintegrować Słowosieć z ontologią zdarzeń w Neo4j?
- Jak zintegrować wyniki z BeautifulSoup bezpośrednio z bazą Neo4j?
- Zintegrujmy bazę Neo4j jako fundament grafu wiedzy Fazy 4..
- Jak zintegrować PhraseologyDetector z istniejącym GraphBuilderem?
- Jak zintegrować Słowosieć z GraphDatabaseAdapterem?
- Jak zintegrować ArangoDB jako alternatywną bazę grafową?
- Pokaż jak zintegrować GraphDatabaseAdapter z resztą pipeline'u..
- Jak zintegrować Słowosieć z naszym grafem w Neo4j?
- Jak zintegrować Słowosieć z naszym grafem wiedzy w Neo4j?
- Jak zintegrować Słowosieć z grafem Neo4j w Fazie 8?
- Jak zintegrować regułę posiadania z grafem Neo4j?
- Pokaż jak zintegrować Neo4j jako nową warstwę grafu wiedzy — jak W4 odbiera EventFrame z W2/W3 i zapisuje jako węzeł?
- Jak zdefiniować granicę odpowiedzialności W4 (persystencja) vs. W5 (wnioskowanie) — co zapisuje W4, co czyta W5?
- Jak W4 eksponuje API dla W5 — REST HTTP czy neo4j-driver Python z protokołem Bolt?
- Jak testować integrację W4 z W5 bez uruchomionej instancji Neo4j — neo4j-driver mock czy testcontainers?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Co się dzieje gdy baza grafowa jest niedostępna podczas zapisu EventFrame — czy dane są tracone czy buforowane?
- Jak uniknąć duplikatów węzłów gdy ten sam podmiot (np. Wykonawca ABC sp. z o.o.) pojawia się w wielu dokumentach?
- Jakie jest ryzyko nieaktywnych relacji (dangling edges) po usunięciu węzła bez kaskadowego usunięcia krawędzi?
- Czy Cypher MERGE gwarantuje atomowość przy równoległych zapisach z wielu instancji serwisu?
- Jak obsłużyć migrację schematu grafu gdy nowy EventFrame dodaje właściwość wymaganą dla istniejących węzłów?
- Jaka jest konsekwencja wyboru ArangoDB zamiast Neo4j dla schematu i zapytań zdefiniowanych w Cypher?
- Jak zapobiec nieograniczonemu wzrostowi grafu przy przetwarzaniu tysięcy dokumentów bez archiwizacji starych węzłów?
- Jaka jest pułapka wykładniczego wzrostu kombinacji w ontologii — każde :EventFrame z 6 rolami × N synsetów = 6N węzłów per zdanie?
- Jak ograniczyć kombinatoryczną eksplozję relacji hiperonimii — import tylko pierwszego poziomu hiperonimu zamiast pełnego drzewa?

## Pytania uzupełniające
- **Pułapka 4:** MERGE w Neo4j bez unikalnego indeksu tworzy duplikaty węzłów — `MERGE (n:Concept {id: x})` bez `CREATE INDEX FOR (n:Concept) ON (n.id)` jest O(n) i duplikuje dane.
- **Pułapka 5:** Neo4j Community Edition nie ma replikacji ani automatycznego failover — awaria węzła podczas zapisu to utrata danych; Commercial/AuraDB wymagane dla projektu produkcyjnego.
- **Pułapka 6:** Zapytania Cypher bez `LIMIT` na grafach >1M węzłów mogą zwrócić GB danych — `MATCH (n:Concept)-[:IS_A*]->(m)` bez limitu głębokości to pełny obchód grafu.

### 1. Architektura

- Jak `GraphDatabaseAdapter` abstrahuje różnice między Neo4j a ArangoDB (wzorzec Adapter)?
- Jak podzielić odpowiedzialność między `GraphBuilder` (budowanie grafu) a `GraphDatabaseAdapter` (persystencja)?
- Jakie są niezmienniki grafu, których nigdy nie wolno naruszyć (np. każdy Event musi mieć AGENT)?
- Jak zarządzać transakcjami w Neo4j przy batch imporcie 10000 zdań?
- Jak skonfigurować indeksy i constraints w Neo4j dla wydajnego wyszukiwania?

### 2. Kontrakty danych

- Jaki jest schemat węzła `:Concept` — pola obowiązkowe i opcjonalne?
- Jaki jest schemat węzła `:Event` — które z 6 wymiarów (AGENT, ACTION, PATIENT, INSTRUMENT, LOCATION, TIME) są required?
- Jaki format ma `CypherBatch` — lista zapytań MERGE czy jeden bulkowy UNWIND?
- Jak walidować `EventRoleDict` przed zapisem do Neo4j (JSON Schema)?
- Jak kodować pewność krawędzi (confidence) jako właściwość relacji?
- Jaki jest model danych grafu dla relacji `MITIGATED_BY` — pełny schemat: węzły `:ThreatModel {id:str, stride:List[str], mitigated:bool=False}` i `:Mitigation {id:str, control:str, status:'PLANNED'|'IMPLEMENTED'|'VERIFIED', owner:str}`; krawędź `[:MITIGATED_BY {applied_at:date, verified_by:str}]`; constraint: `CREATE CONSTRAINT ON (m:Mitigation) ASSERT m.id IS UNIQUE`; `ThreatModel.mitigated` to cache-flag dla wydajności — aktualizowany triggerem gdy wszystkie powiązane Mitigation mają `status='VERIFIED'`?

### 3. Implementacja

- Jak zaimplementować `generate_cypher(event_role_dict) -> List[str]`?
- Jak zaimplementować `MERGE` dla węzłów konceptów, żeby unikać duplikatów na synset_id?
- Jak zaimplementować `build_document(sentences)` — pętlę budującą pełny graf dokumentu?
- Jak użyć APOC (`apoc.import.json`) do szybkiego importu wielu węzłów naraz?
- Jak zoptymalizować import miliona relacji hiperonimii ze Słowosieci do Neo4j?
- Jak modelować relację `MITIGATED_BY` w grafie dla modelu zagrożeń — `:ThreatModel {stride:['SPOOFING'], mitigated:False}` + `(:ThreatModel)-[:MITIGATED_BY]->(:Mitigation {control:'rate_limiting', status:'IMPLEMENTED'})`; krawędź `MITIGATED_BY` pozwala Cypherowi na `MATCH (tm)-[:MITIGATED_BY]->(m) WHERE m.status='IMPLEMENTED' RETURN tm` jako alternatywny warunek zaspokojenia SEC-01b bez pola `mitigated` na węźle?
- Jak zdefiniować relację `MITIGATED_BY` w Cypher dla SEC-01 — pełny przepis: `MERGE (tm:ThreatModel {id:'tm_api'}) MERGE (m:Mitigation {id:'mit_rate', control:'rate_limiting', status:'IMPLEMENTED', owner:'DevOps'}) MERGE (tm)-[r:MITIGATED_BY]->(m) SET r.applied_at='2026-03-01'`; SEC-01b query: `MATCH (e)-[:HAS_THREAT_MODEL]->(tm) WHERE NOT (tm)-[:MITIGATED_BY]->(:Mitigation {status:'IMPLEMENTED'}) RETURN e, tm`; różnica względem `tm.mitigated=True`: właściwość `owner` i `applied_at` na krawędzi dają pełną historię remediacji?
- Jak stworzyć graf przyczynowy dla zdarzenia z wymiarem 6 (TIME) — `:EventFrame {id:'e_dostawa', predicate:'dostarczyć'}` z krawędziami: `:HAS_ROLE {role:'TIME'}→:Token {lemma:'2026-01-15', type:'DATE'}`; Cypher kauzalny: `MATCH (e1:EventFrame)-[:HAS_ROLE {role:'TIME'}]->(t:Token), (e1)-[:CAUSES]->(e2:EventFrame) WHERE t.lemma < date() RETURN e1, e2` wykrywa przeterminowane przyczyny aktywnych zobowiązań; wymiar TIME jako predykat warunkowy w grafie kauzalnym?
- Pokaż formalny model grafu dla zdania — zdanie `"Wykonawca dostarczył SRS dnia 2026-01-15"` → formalizacja: `(e:EventFrame {id:'e1', predicate:'dostarczyć', speech_act:'ASSERT'})-[:HAS_ROLE {role:'AGENT'}]→(:Token {lemma:'Wykonawca'}), -[:HAS_ROLE {role:'PATIENT'}]→(:Token {lemma:'SRS'}), -[:HAS_ROLE {role:'TIME'}]→(:Token {lemma:'2026-01-15', type:'DATE'}), -[:HAS_SYNSET]→(:Synset {id:'dostarczyć.1', domain:'LOGISTICS'})`; 6-wymiarowy model zamknięty przez synset domeny?
- Pokaż jak modelować relację `MITIGATED_BY` w Cypher dla SEC-01 — rozszerzony przykład: `MATCH (e:EventFrame {domain:'API'})-[:HAS_THREAT_MODEL]->(tm:ThreatModel) WHERE NOT (tm)-[:MITIGATED_BY {verified_by: $auditor}]->(:Mitigation {status:'VERIFIED'}) RETURN e, tm`; parametr `$auditor` pozwala filtrować po osobie weryfikującej; `SET tm.mitigated = (size([(tm)-[:MITIGATED_BY]->(m:Mitigation {status:'VERIFIED'}) | m]) > 0)` aktualizuje cache-flagę po każdej weryfikacji?
- Jak wdrożyć regułę `OPS-04` w grafie Neo4j jako schemat — węzeł `:BackupProcedure {id:str, frequency:'DAILY'|'WEEKLY'|'MONTHLY', tested:bool, last_test_date:date, rto_hours:int, rpo_hours:int}`; `rto_hours` (Recovery Time Objective) i `rpo_hours` (Recovery Point Objective) jako pola obowiązkowe dla compliance DORA; krawędź `:HAS_BACKUP_PROCEDURE`; OPS-04 dodatkowo może sprawdzać `rto_hours <= 4` dla systemów krytycznych?
- Jak zapisać relację `MITIGATED_BY` w modelu danych grafu Neo4j kompletnie — Cypher setup: `CREATE CONSTRAINT FOR (m:Mitigation) REQUIRE m.id IS UNIQUE; CREATE INDEX FOR ()-[r:MITIGATED_BY]-() ON (r.applied_at)`; wzorzec zapisu: `MERGE (tm:ThreatModel {id:$tm_id}) MERGE (m:Mitigation {id:$m_id}) ON CREATE SET m.control=$ctrl, m.status='PLANNED', m.owner=$owner MERGE (tm)-[r:MITIGATED_BY]->(m) ON CREATE SET r.applied_at=date() ON MATCH SET r.verified_by=$auditor, m.status='VERIFIED'`; ON MATCH aktualizuje status przy ponownym wywołaniu — wzorzec upsert?
- Jak wymiarowanie zdarzeń wpływa na kaskady błędów w grafie — EventFrame z 6 wymiarami (AGENT/ACTION/PATIENT/INSTRUMENT/LOCATION/TIME) generuje potencjalnie 6 krawędzi `:HAS_ROLE`; każdy wymiar może być źródłem kaskady: np. `INSTRUMENT='klucz'` → `HOMOGRAPH_AMBIGUITY`; `TIME < date()` → `TEMPORAL_CASCADE`; `LOCATION='system_A'` → `CROSS_DOMAIN_CASCADE` gdy system_A w domenie INFRA; więcej wymiarów = wyższe ryzyko kaskady; reguła: `cascade_risk_score = count(HAS_ROLE edges) * depth_limit`?
- Jak wyświetlić dashboard postępu mitigacji dla SEC-01 w Neo4j — query: `MATCH (e:EventFrame {domain:'API'})-[:HAS_THREAT_MODEL]->(tm:ThreatModel)-[:MITIGATED_BY]->(m:Mitigation) RETURN tm.id AS threat, m.status AS status, m.owner AS owner, tm.mitigated AS cached ORDER BY m.status`; wynik: tabela `|threat|status|owner|cached|` ze stanami PLANNED/IMPLEMENTED/VERIFIED; `cached=False` przy `status=IMPLEMENTED` sygnalizuje nieaktualną cache-flagę → `SET tm.mitigated=True`; `KnowledgeGapTracker` może raportować `MISSING_MITIGATION` gdy `tm.mitigated=False` od ponad 30 dni bazując na `r.applied_at`?
- Pokaż przykład analizy kaskadowej dla Wymiaru 6 (TIME/konsekwencje) — `(e:EventFrame {id:'e_deadline'})-[:HAS_ROLE {role:'TIME'}]->(:Token {lemma:'2025-12-31', type:'DATE'})`; query: `MATCH (e)-[:HAS_ROLE {role:'TIME'}]->(t:Token) WHERE date(t.lemma) < date() RETURN e.id AS node_id`; wynik: `Violation('TEMPORAL-01','e_deadline', cascade_type='TEMPORAL_CASCADE', severity='HIGH')`; `CrossReferenceEngine.check_cascade(v)` propaguje do dokumentów referencujących `e_deadline` → kaskada konsekwencji przez dokumenty opisujące następstwa (kary umowne, harmonogramy); Wymiar 6 = TIME jest najczęstszym źródłem kaskad w dokumentacji kontraktowej?
- Jak zaimportować dane plWordNet do Neo4j w trybie wsadowym — `LOAD CSV WITH HEADERS FROM 'file:///plWordNet_synsets.csv' AS row MERGE (:Synset {id:row.synset_id, name:row.name, pos:row.pos, domain:row.domain, source:'plWordNet'})`; krawędzie hiperonimii: `LOAD CSV FROM 'file:///plWordNet_hypernyms.csv' AS row MERGE (a:Synset {id:row.child}) MERGE (b:Synset {id:row.parent}) MERGE (a)-[:HYPERNYM]->(b)`; po imporcie: `CREATE INDEX FOR (s:Synset) ON (s.name, s.pos)` dla wydajności `is_hypernym_of()`; `WordnetAdapter.get_synsets(lemma)` używa tej lokalnej bazy zamiast zewnętrznego API?
- Napiszmy zapytanie Cypher do rezolucji zaimka "on" — model koreferencji: `(:Token {lemma:'on', pos:'ppron3:sg:nom:m1'})-[:COREFERENCE_OF]->(:Token {pos:'subst'})`; query: `MATCH (p:Token {lemma:'on', pos:'ppron3:sg:nom:m1'})-[:IN_SENTENCE]->(s:Sentence)-[:PREV]->(s2:Sentence)-[:HAS_TOKEN]->(ant:Token) WHERE ant.pos =~ 'subst.*' AND ant.gender='m1' RETURN p.id AS pronoun, last(collect(ant.lemma)) AS resolved_as`; wynik: `{pronoun:'on_47', resolved_as:'Wykonawca'}` — zaimek "on" rozwiązany do podmiotu "Wykonawca"; `CoreferenceResolver` tworzy krawędź `COREFERENCE_OF` po analizie Morfeuszem; rozwiązuje problem anonimowości aktora w zdaniach kontraktowych?
- Jak modelować hierarchię tematyczną dokumentu w Neo4j — schemat: `(:Document {id, layer:'W0'})-[:HAS_TOPIC]->(:Topic {name, level:int})`; `(:Topic)-[:SUBTOPIC_OF]->(:Topic)` mapuje sekcje Markdown: poziom 2 (`##`) → `level:2`, poziom 3 (`###`) → `level:3`; query pokrycia: `MATCH (d:Document {layer:'W0'})-[:HAS_TOPIC*1..3]->(t:Topic) RETURN t.name, count(*) AS coverage ORDER BY coverage DESC`; `CrossReferenceEngine` wykrywa nakładające się tematy między dokumentami przez `MATCH (t1:Topic)<-[:HAS_TOPIC]-(d1) MATCH (t1)<-[:HAS_TOPIC]-(d2) WHERE d1<>d2 RETURN t1.name`?
- Jak zamodelować wszystkie 6 wymiarów EventFrame jako klasy ontologiczne — `:DimensionType {name, description, required:bool}` dla `AGENT/ACTION/PATIENT/INSTRUMENT/LOCATION/TIME`; `AGENT` i `ACTION` mają `required=True` — brak `[:HAS_ROLE {role:'AGENT'}]` → `Violation('ROLE-01')`; `TIME` ma `required=False` ale gdy `date(t.lemma) < date()` → `Violation('TEMPORAL-01')`; `CREATE CONSTRAINT FOR (dt:DimensionType) REQUIRE dt.name IS UNIQUE`; query walidacyjny `MATCH (e:EventFrame) WHERE NOT (e)-[:HAS_ROLE {role:'AGENT'}]->() RETURN e.id` jako bezpośrednia implementacja ROLE-01?
- Jak zmodyfikować zapytanie Cypher by wykrywało luki w Wymiarze 6 — dwa typy: (a) brak TIME gdy wymagany: `MATCH (e:EventFrame {domain:'CONTRACT'}) WHERE NOT (e)-[:HAS_ROLE {role:'TIME'}]->() RETURN e.id AS node_id`; wynik: `Violation('TEMPORAL-02', node_id, severity='MEDIUM', details={gap:'missing_time_dimension'})`; (b) przekroczony termin: `MATCH (e)-[:HAS_ROLE {role:'TIME'}]->(t:Token) WHERE date(t.lemma) < date() RETURN e.id, t.lemma`; wynik: `Violation('TEMPORAL-01',..., severity='HIGH')`; `KnowledgeGapTracker.MISSING_TEMPORAL` jako nowy typ luki dla obu przypadków?
- Jak wersjonować stan grafu Neo4j po każdym zasilaniu z parsera Markdown — węzeł `:ExtractionRun {id:uuid, timestamp:datetime, docs_processed:int, violations_found:int, status:'COMPLETE'|'PARTIAL'|'FAILED'}`; relacja `(r:ExtractionRun)-[:PROCESSED]->(:Document)`; historia: `MATCH (r:ExtractionRun) RETURN r.timestamp, r.docs_processed, r.violations_found ORDER BY r.timestamp DESC LIMIT 10`; `MarkdownRelationExtractor.run_batch()` tworzy węzeł na początku i ustawia `status='COMPLETE'` po zakończeniu; rollback: `status='PARTIAL'` → usuń przetworzone dokumenty?
- Jak walidować kompletność wszystkich wymiarów EventFrame przez `DimensionType` — centralny query: `MATCH (e:EventFrame), (dt:DimensionType {required:true}) WHERE NOT (e)-[:HAS_ROLE {role:dt.name}]->() RETURN e.id AS frame, dt.name AS missing_dimension`; jeden MATCH zastępuje N osobnych per-reguła queries; wynik: `|frame|missing_dimension|` → brak AGENT → `Violation('ROLE-01')`; brak ACTION → nowa reguła `ACTION-01`; query jako centralny validator dla wszystkich wymaganych wymiarów?
- Jak dodać wymiar intencji (speech_act) jako 7. wymiar do grafu zdarzenia — uzupełnienie katalogu: `MERGE (:DimensionType {name:'INTENT', required:False, description:'speech act type'})`; krawędź `[:HAS_SPEECH_ACT]->(sa:SpeechAct {type:'COMMITMENT'|'ASSERTION'|'REQUIREMENT'|'DECLARATION'})` jako 7. wymiar; gdy `type='COMMITMENT'` i brak powiązanej `SpeechAct {type:'DECLARATION'}` → `Violation('CAUSAL-INTENT-01')`; query: `MATCH (e)-[:HAS_SPEECH_ACT]->(sa) WHERE sa.type='COMMITMENT' AND NOT (e)-[:HAS_SPEECH_ACT]->(:SpeechAct {type:'DECLARATION'}) RETURN e.id`; `IntentClassifier.classify()` → `MERGE (e)-[:HAS_SPEECH_ACT]->(sa)` domyka pipeline→graf?
- Pokaż kod parsera Markdown tworzącego węzły bazy danych w Neo4j — `MarkdownRelationExtractor.extract(path)`: `ast = mistune.create_markdown(renderer=ASTRenderer()).parse(text)`; iteracja: `heading→MERGE (:Topic {name:h['text']})`, `code_block→MERGE (:CodeSnippet {lang:info, body:text})`, `list_item→MERGE (:EventFrame {text:item})-[:BELONGS_TO]->(topic)`; wynik: `nodes=[{label, props}], rels=[{src,type,dst}]`; `BatchWriter.write(nodes, rels)`: `session.run("UNWIND $rows AS r MERGE (n:{label} {id:r.id}) SET n += r.props", rows=nodes)` — jeden `UNWIND` per typ etykiety, nie N osobnych `session.run()`?
- Pokaż model danych dla relacji synonimii i hiperonimii w plWordNet (Neo4j) — węzły: `(:Synset {id:'plwn-12345', lemma:'klucz', pos:'noun', domain:'SECURITY'})`; krawędzie: `(:Synset)-[:SYNONYM_OF {confidence:0.99}]->(:Synset)` (symetria: dwa `MERGE` A→B i B→A), `(:Synset)-[:HYPERNYM_OF {depth:1}]->(:Synset {lemma:'urządzenie'})` (asymetryczna), `(:Synset)-[:HYPONYM_OF]->(:Synset)` (odwrotna do HYPERNYM); indeksy: `CREATE INDEX synset_lemma FOR (s:Synset) ON (s.lemma, s.domain)`; `WordnetAdapter.get_hypernyms(lemma, depth=3)` → `MATCH (s {lemma:$l})-[:HYPERNYM_OF*1..3]->(h) RETURN h` z cache `lru_cache(maxsize=512)`?
- W jaki sposób rozwiązać problem koreferencji zaimka "on" w grafie Neo4j — `CoreferenceResolver.resolve(sentence_id, token_id)` szuka antecedent: `MATCH (s:Sentence)-[:PREV]->(prev:Sentence), (s)-[:HAS_TOKEN]->(t:Token {id:$token_id, pos:'ppron3:sg:nom:m1'}), (prev)-[:HAS_TOKEN]->(cand:Token {pos:'subst:sg:nom:m1'}) RETURN cand ORDER BY cand.offset DESC LIMIT 1`; gdy znaleziony: `MERGE (t)-[:COREFERENCE_OF]->(cand)`; gdy brak antecedent w poprzednim zdaniu — przeszukaj 2 zdania wstecz `[:PREV*1..2]`; `Violation('COREF-UNRESOLVED')` gdy >2 zdania bez antecedent m1; metryka: `CoreferenceAccuracy` = resolved / total ppron3?
- Pokaż model grafu dla zaimków w pamięci kontekstu dokumentu — `(:DocumentContext {id:doc_id})-[:HAS_SENTENCE {order:n}]->(s:Sentence)-[:HAS_TOKEN]->(t:Token)`; okno kontekstowe: `(:ContextWindow {size:3})-[:COVERS]->(s:Sentence)` łączy bieżące zdanie z 3 poprzednimi; zaimki: `(t:Token {pos:'ppron3', lemma:'on'})-[:IN_CONTEXT]->(:ContextWindow)`; lookup: `MATCH (w:ContextWindow)-[:COVERS]->(prev:Sentence)-[:HAS_TOKEN]->(cand:Token {pos:'subst:sg:nom:m1'}) WHERE prev.order < s.order RETURN cand ORDER BY prev.order DESC`; `ContextWindowManager.slide(doc_id)` przesuwa okno po `[:HAS_SENTENCE {order}]` — O(1) per zdanie dzięki indeksowi na `order`?
- Pokaż kod parsera Markdown tworzącego węzły Event (EventFrame) w Neo4j — rozszerzenie `MarkdownRelationExtractor`: `list_item` z czasownikiem modal/nakazu → `MERGE (:EventFrame {id:hash(text), text:item, domain:'CONTRACT', source_doc_id:$path})-[:BELONGS_TO]->(topic)`; wykrywanie czasownika: `re.search(r'\b(dostarczy|zapewni|zobowiązuje|musi|należy)\b', item)`; łańcuch przyczynowy: jeśli poprzedni item też EventFrame → `MERGE (prev)-[:CAUSED_BY]->(curr)`; wynik: `EventFrame` z `source_doc_id` (constraint B62 Pułapka 9) + `[:CAUSED_BY]` sieć gotowa do `DeductionRule.CAUSAL_CHAIN`?
- Pokaż jak zainstalować i skonfigurować oficjalny sterownik Neo4j — `pip install neo4j==5.18.0`; konfiguracja: `from neo4j import GraphDatabase; driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","test"), max_connection_pool_size=50, connection_timeout=5)`; zarządzanie sesją: `with driver.session(database="neo4j") as session: session.run(query, params)`; zamknięcie: `driver.close()` w `__exit__` lub `@contextmanager`; konfiguracja środowiskowa: `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD` → `GraphAdapter.from_env()` czyta `os.environ`; `driver.verify_connectivity()` jako health check w `AuditPipeline.__init__`?
- Pokaż jak zintegrować oficjalny sterownik Neo4j z `GraphDatabaseAdapter` — `class Neo4jAdapter: def __init__(self, driver:neo4j.Driver): self._driver=driver`; `def run(self, query:str, **params)->List[Record]: with self._driver.session() as s: return list(s.run(query, params))`; `def merge_event_frame(self, frame:EventFrame): self.run("MERGE (e:EventFrame {id:$id}) ON CREATE SET e+=$props", id=frame.id, props=asdict(frame))`; `GraphQueryAdapter(Neo4jAdapter)` jako warstwa wyższa z metodami domenowymi `save_violation()`, `find_cascades()`; `Neo4jAdapter` testowany przez `driver=Mock()` — oddziela sterownik od logiki domenowej?
- Jak modelować relacje w grafie zgodnie z wymiarem 6 (TIME) — `(:EventFrame)-[:HAS_ROLE {role:'TIME'}]->(t:Token {lemma:'2025-03-15', type:'DATE'})`; powiązanie przyczynowe: `(e1)-[:CAUSED_BY]->(e2)` gdy `e2.time > e1.time` i `e2.domain == e1.domain`; kolejność temporalna: `ORDER BY t.lemma` wyznacza sekwencję `e1→e2→e3` jako łańcuch OBLIGATION_TRANSFER; brakujący wymiar TIME: `TEMPORAL-02` query → `Violation(severity='MEDIUM')`; przekroczony termin: TEMPORAL-01 query → `Violation(severity='HIGH')`; `TemporalDimensionValidator.validate(session)` odpytuje oba queries i zwraca `List[Violation]` w jednym przebiegu?
- Jak modelować 'pamięć kontekstu dokumentu' w grafie Neo4j — pełny schemat: `(:Document {id, path, hash})-[:HAS_SECTION {order:n}]->(:Section {heading})-[:HAS_SENTENCE {order:m}]->(:Sentence {text, id})-[:HAS_TOKEN]->(:Token)`; okno: `(:ContextWindow {doc_id, start_order, end_order, size:3})-[:COVERS {position:k}]->(:Sentence)`; pamięć krótkotrwała: constraint `CREATE CONSTRAINT ON (w:ContextWindow) ASSERT w.doc_id IS NOT NULL`; `ContextWindowManager.slide(doc_id, current_order)`: DELETE stare okno `WHERE w.start_order < current_order-3`, CREATE nowe; `MATCH (w:ContextWindow {doc_id:$d})-[:COVERS]->(s)-[:HAS_TOKEN]->(t {pos:'ppron3'}) RETURN t` jako punkt wejścia CoreferenceResolver — pełna pamięć dokumentu w jednym podgrafie?
- Jak zmapować relacje agent-akcja-obiekt na grafie semantycznym — `DependencyParserAdapter.extract_roles(doc)→RoleSet`; mapowanie dep-rel: `nsubj→AGENT`, `obj/dobj→PATIENT`, `ROOT (verb)→ACTION`; `SemanticMapper.map(roles)`: `MERGE (e:EventFrame {id:$id}) MERGE (a:Token {lemma:$agent}) MERGE (e)-[:HAS_ROLE {role:'AGENT'}]->(a) MERGE (p:Token {lemma:$patient}) MERGE (e)-[:HAS_ROLE {role:'PATIENT'}]->(p) MERGE (v:Token {lemma:$action}) MERGE (e)-[:HAS_ROLE {role:'ACTION'}]->(v)`; zapytanie semantyczne: `MATCH (e)-[:HAS_ROLE {role:'AGENT'}]->(a), (e)-[:HAS_ROLE {role:'ACTION'}]->(v), (e)-[:HAS_ROLE {role:'PATIENT'}]->(p) RETURN a.lemma, v.lemma, p.lemma`; trójka agent-akcja-obiekt jako minimalny EventFrame?
- Pokaż model ontologii dla wielowymiarowej analizy zdarzenia — 7 węzłów `DimensionType` z flagą `required`: `MERGE (:DimensionType {name:'AGENT', required:True})`, `MERGE (:DimensionType {name:'ACTION', required:True})`, `MERGE (:DimensionType {name:'PATIENT', required:False})`, `MERGE (:DimensionType {name:'INSTRUMENT', required:False})`, `MERGE (:DimensionType {name:'LOCATION', required:False})`, `MERGE (:DimensionType {name:'TIME', required:True, default_check:'TEMPORAL-01'})`, `MERGE (:DimensionType {name:'INTENT', required:False, default_check:'CAUSAL-INTENT-01'})`; centralny validator: `MATCH (e:EventFrame),(dt:DimensionType {required:True}) WHERE NOT (e)-[:HAS_ROLE {role:dt.name}]->() AND NOT (e)-[:HAS_SPEECH_ACT]->() WHERE dt.name='INTENT' RETURN e.id, dt.name` — jeden MATCH dla 3 wymaganych wymiarów?
- Pokaż jak zintegrować parser Markdown z grafem Neo4j — wzorzec ON MATCH SET dla aktualizacji: `MERGE (d:Document {path:$path}) ON CREATE SET d.hash=$hash, d.status='NEW' ON MATCH SET d.hash=CASE WHEN d.hash<>$hash THEN $hash ELSE d.hash END, d.status=CASE WHEN d.hash<>$hash THEN 'UPDATED' ELSE 'UNCHANGED' END`; gdy `status='UPDATED'` → `MarkdownRelationExtractor` re-przetwarza plik i aktualizuje powiązane `EventFrame`/`Topic` węzły przez `MERGE ... ON MATCH SET props`; gdy `status='UNCHANGED'` → skip; wzorzec hash-based idempotent update zastępuje naiwny DELETE+CREATE — żadne istniejące relacje nie giną?
- Jak użyć spaCy do ekstrakcji ról agent-akcja-obiekt i zapisać do grafu — `doc=nlp(sentence)`; `subj=[t for t in doc if t.dep_=='nsubj']`; `verb=[t for t in doc if t.dep_=='ROOT']`; `obj=[t for t in doc if t.dep_ in('obj','dobj')]`; `MERGE (e:EventFrame {id:hash(sentence)}) MERGE (a:Token {lemma:subj[0].lemma_}) MERGE (e)-[:HAS_ROLE {role:'AGENT'}]->(a) MERGE (v:Token {lemma:verb[0].lemma_}) MERGE (e)-[:HAS_ROLE {role:'ACTION'}]->(v) MERGE (p:Token {lemma:obj[0].lemma_}) MERGE (e)-[:HAS_ROLE {role:'PATIENT'}]->(p)`; guard: `if not subj → Violation('ROLE-01')`; `if not verb → Violation('ACTION-01')`; cały blok jako `SemanticMapper.map_to_cypher(doc)→str` gotowy do `session.run()`?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `Neo4jAdapter.save_event()` bez real Neo4j (mock/stub)?
- Jak testować `generate_cypher()` — sprawdzić, czy wygenerowany Cypher jest poprawny składniowo?
- Jak napisać test integracyjny dla scalania węzłów (`MERGE`) na embedded Neo4j?
- Jak testować `build_document()` dla zdania "Wykonawca dostarczył dokumentację techniczną z opóźnieniem" — sprawdzić węzły i krawędzie?
- Zdefiniuj testy dla intencji CONDITION i jej skutków — `def test_condition_blocks_effect(): mock_session.run.return_value = [{'eff': {'id':'e2'}}]; violations = LinterRuleEngine([CONDITION_RULE], mock_session).run_all(); assert violations[0].rule_id == 'CONDITION-01'`; reguła `CONDITION-01`: `MATCH (e)-[:CAUSES]->(eff) WHERE NOT (e)-[:REQUIRES_CONDITION]->(:Condition {satisfied:True}) RETURN eff`?
- Jak testować wykrywanie sprzecznych relacji w modelu zdarzenia?
- Pokaż jak testować wykrywanie osieroconych węzłów w Neo4j — `def test_orphan_detection(): mock_session.run.return_value = [{'e': {'id':'orphan1'}}]; engine = LinterRuleEngine([ORPHAN_RULE], mock_session); violations = engine.run_all(); assert violations[0].rule_id == 'ORPHAN-01' and violations[0].node_id == 'orphan1'`?
#### Kompletna hierarchia TDD
- Zaimplementuj Fazę GREEN dla `Neo4jAdapter.save_event()` — minimalna implementacja: stwórz węzeł Event i krawędź AGENT bez walidacji typów.
- Jak zrefaktoryzować `GraphDatabaseAdapter` po GREEN — oddzielić `CypherBuilder` od `Neo4jClient` żeby można było testować generowanie Cypher bez połączenia z bazą?
- Zrefaktoryzuj `generate_cypher()` — każdy typ relacji (AGENT, PATIENT, IS_A) jako osobna metoda z testem jednostkowym.
- Jak napisać test jednostkowy dla `CypherBuilder.build_merge_query()` — bez połączenia z Neo4j, sprawdzić tylko poprawność składniową?
- Jak zbudować oracle dataset dla W4 — 20 zdań kontraktowych + oczekiwane grafy Cypher jako golden files?
- Jak zmierzyć Mutation Score dla `GraphDatabaseAdapter` — które warunki MERGE vs CREATE są najtrudniejsze do pokrycia?
- Jak napisać test własnościowy (Hypothesis) dla `save_event()` — dla każdego poprawnego `EventRoleDict` zapis powinien być idempotentny (3x MERGE = 1 węzeł)?
- Jak zapewnić że migracja Neo4j (3.x→5.x) nie zmienia semantyki zapytań Cypher — golden file z wynikami 10 kluczowych zapytań?
- Stwórz test regresyjny schematu grafu — snapshot węzłów i krawędzi dla 5 zdań testowych; CI fail gdy schemat się zmieni.
- Jak przetestować W1→W2→W3→W4 end-to-end — zdanie → sprawdź że graf zawiera węzeł IS_A z hyperonimem z W3?

### 5. Obsługa błędów

- Co robi `GraphDatabaseAdapter` przy niedostępności Neo4j (connection refused)?
- Jak obsługiwać konflikt przy MERGE węzłów z różnymi synset_id dla tego samego lematu?
- Co zwrócić gdy zapytanie Cypher jest malformed (syntax error)?
- Pokaż przykład błędu `CypherSyntaxError` i sposób jego naprawy — błąd: `MATCH (e:EventFrame WHERE e.domain='CONTRACT')` → `SyntaxError: Invalid input 'WHERE'` (brakujący nawias zamykający przed WHERE); naprawa: `MATCH (e:EventFrame) WHERE e.domain='CONTRACT'`; drugi przypadek: `MERGE (e)-[r:HAS_ROLE]->()` bez etykiety węzła docelowego → `SyntaxError: ')'`; naprawa: `MERGE (e)-[r:HAS_ROLE {role:$role}]->(t:Token {id:$tid})`; `Neo4jAdapter.run()` łapie `neo4j.exceptions.CypherSyntaxError` i loguje `query_hash+error.message` bez ujawniania danych; `GraphQueryAdapter` posiada `validate_query(cypher:str)->bool` wywołujący `EXPLAIN {query}` przed wykonaniem — koszt: 1 extra roundtrip, ale wykrywa błędy przed produkcyjnym `session.run()`?
- Jak rollbackować częściowy import gdy część węzłów się zapisała a reszta nie?
- Jak logować błędy imporcie (które zdania zakończono, które nie)?
- Co robi system gdy Neo4j jest w trybie read-only (np. po awarii, przed recovery)?
- Jak obsługiwać race condition: ten sam węzeł MERGE-owany równolegle przez dwa procesy?

### 6. Integracja z innymi warstwami

- Jak W4 dostaje `EventRoleDict` z W2 — bezpośrednio czy przez kolejkę?
- Jak W5 (InferenceEngine) wykonuje zapytania Cypher do W4 — przez ten sam adapter?
- Jak W6 (koreferencja) dostarcza zmergowane węzły do W4 — przed czy po `generate_cypher()`?
- Jak W8 (AuditEngine) pobiera dane z W4 do generowania raportów luk?
- Jak W4 informuje W5 (silnik wnioskowania) gdy nowy węzeł EventFrame jest dostępny w grafie?
- Jak weryfikować spójność grafu po wsadowym imporcie wielu dokumentów jednocześnie?
- Jak W4 obsługuje zapytania z W8 (compliance audit) o historię zmian węzła?

### 7. Pułapki i ryzyka

- **Pułapka 1:** MERGE w Neo4j bez indeksu na `synset_id` jest O(n) — baza nie skaluje się przy >100k węzłów. Indeksy muszą być założone PRZED importem.
- **Pułapka 2:** ArangoDB ma inny model zapytań niż Cypher — migracja między nimi wymaga przepisania wszystkich zapytań W5. Decyzja wyboru DB musi być ostateczna.
- **Pułapka 3:** Brak transakcji ACID przy batch imporcie = niespójny stan grafu po przerwaniu. Zawsze używać `BEGIN TRANSACTION` lub APOC periodic commit.
- **Pułapka 4:** MERGE w Neo4j bez unikalnego indeksu tworzy duplikaty węzłów — `MERGE (n:Concept {id: x})` bez `CREATE INDEX` jest O(n) i duplikuje dane.
- **Pułapka 5:** Neo4j Community Edition nie ma replikacji — awaria węzła podczas zapisu to utrata danych; wymagana edycja Enterprise dla projektu produkcyjnego.
- **Pułapka 6:** Zapytania Cypher bez `LIMIT` na grafach >1M węzłów — `MATCH (n)-[:IS_A*]->(m)` bez limitu głębokości to pełny obchód grafu.
- **Pułapka 7 (eksplozja ontologii):** Automatyczna budowa grafu przez `OntologyBuilder.infer_domain()` bez ograniczeń tworzy niekontrolowane domeny; strategie hamowania: (1) `DOMAIN_WHITELIST` — dozwolone domeny SECURITY/OPS/SYSTEM/GRAPH/API/AUTH; domeny spoza listy → `Violation('ONTOLOGY-01')`; (2) `merge_threshold: float=0.8` — nowa domena z similarity > 0.8 do istniejącej → fuzja zamiast tworzenia; (3) `max_domains_per_document=5` — limit ontologiczny per dokument; `OntologyDriftMetric` ostrzega gdy przekroczony?
- **Pułapka 8 (błędy logiczne w Cypher):** Trzy najczęstsze pułapki: (1) `MATCH` bez `WHERE` na pustym grafie zwraca pusty wynik zamiast błędu — `OPTIONAL MATCH` ujawnia brak węzła przez `null`; (2) `CREATE` zamiast `MERGE` tworzy duplikaty przy ponownym uruchomieniu — każda relacja `HAS_ROLE`/`HAS_SPEECH_ACT` powinna używać `MERGE ON CREATE SET`; (3) ścieżka gwiazdkowa bez limitu głębokości `[:CAUSES*]` → pętla nieskończona gdy graf zawiera cykl; remedium: zawsze `[:CAUSES*1..5]` + constraint `CREATE CONSTRAINT ON (e:EventFrame) ASSERT e.id IS UNIQUE` blokuje duplikaty na poziomie bazy?
- **Pułapka 9 (błędy przy budowaniu ontologii zdarzeń):** Trzy błędy konstrukcji EventFrame: (1) **over-segmentacja** — każde zdanie jako osobny EventFrame bez `[:CAUSED_BY]`/`[:PREV]` łańcucha → graf acykliczny zamiast sekwencji; test: `MATCH (e:EventFrame) WHERE NOT (e)-[:CAUSED_BY|PREV]->() RETURN count(e)` > 30% → sygnał over-segmentacji; (2) **brak identyfikatora źródła** — `EventFrame.source_doc_id` NULL → niemożność delta-extraction; constraint: `ASSERT e.source_doc_id IS NOT NULL`; (3) **mieszanie warstw** — `SpeechAct.type` kopiowane do `EventFrame.intent` zamiast krawędzi `HAS_SPEECH_ACT` → redundancja vs. niekoherencja; invariant: `MATCH (e:EventFrame) WHERE e.intent IS NOT NULL RETURN count(e)` powinno być 0?

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Czas importu 1000 węzłów + relacji | < 5 s |
| Poprawność Cypher (parse test) | 100% |
| Test integracyjny save_event → query_event | PASS |
| Brak duplikatów węzłów po 3× MERGE tego samego entity | Verified |
| Pokrycie testów linii | ≥ 85% |

## Pytania o idempotentność i deterministyczność

- Czy `save_event(event)` wywołane 3× z identycznym eventem tworzy 1 węzeł czy 3?
- Czy `generate_cypher(event_role_dict)` jest deterministyczny — identyczna kolejność zapytań?
- Jak zapewnić, że import równoległy (wiele wątków) nie tworzy duplikatów węzłów?

## Pytania o migrację i wersjonowanie

- Jak migrować schemat Neo4j gdy dodajemy nowy wymiar zdarzenia (np. MANNER)?
- Jak wersjonować `GraphDatabaseAdapter` API gdy W5 jest już zaimplementowane?
- Jak eksportować i reimportować cały graf przy zmianie wersji Neo4j (4.x → 5.x)?

## Pytania o audytowalność

- Jak każdy węzeł w Neo4j przechowuje metadane: źródłowy dokument, zdanie, data importu?
- Jak wygenerować raport "skąd pochodzi ta krawędź AGENT" — tracking do oryginalnego zdania?
- Jak Neo4j loguje zapytania Cypher dla celów debugowania i audytu compliance?

---

## Rozszerzalność i skalowanie

### Stopniowe skalowanie grafu

- Jak Neo4j zachowuje się przy 10k / 100k / 1M / 10M węzłów — gdzie są progi degradacji?
- Jakie indeksy są obowiązkowe przy każdym progu skali (pełnotekstowy, composite, point)?
- Jak zaimplementować pagination dla zapytań Cypher zwracających >10k wyników?
- Jak monitorować fragment heap Neo4j (Page Cache Hit Ratio) i kiedy zwiększyć pamięć?
- Jak testować wydajność `build_document()` dla dokumentu 10 zdań / 100 zdań / 1000 zdań?

### Inkrementalne dodawanie wiedzy

- Jak dodać nową domenę (np. medyczna) do grafu bez przebudowywania istniejącej (prawna)?
- Jak zaimplementować `add_domain(name, ontology_path)` — dodanie nowej ontologii domenowej?
- Jak wykrywać konflikty po dodaniu nowej ontologii (nowe węzły IS_A naruszające istniejącą hierarchię)?
- Jak inkrementalnie importować nowe hiperonimie ze Słowosieci po aktualizacji do nowej wersji?
- Jak zaimplementować `diff_graph(snapshot_1, snapshot_2)` — porównanie stanu grafu między wersjami?

### Skalowanie importu i batch operations

- Jak zoptymalizować import 1M relacji — APOC periodic.commit vs UNWIND batch vs CSV bulk import?
- Jak obsłużyć import równoległy (4 workerów) bez race condition na MERGE?
- Jak zaimplementować idempotentny import — uruchomienie dwa razy daje ten sam stan grafu?
- Jak testować skalowalność: `stress_test_neo4j(nodes=10k, rels=50k)` — czas + błędy?

### Rozszerzanie schematu grafu

- Jak dodać nową właściwość do istniejącego węzła `:Event` bez migracji wszystkich węzłów?
- Jak wersjonować schemat grafu — gdy `:Concept` dostaje nowe pole `domain`, co ze starymi węzłami?
- Jak zaimplementować schema migrations dla Neo4j (analogicznie do Alembic dla SQL)?
