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
- Napisz szkielet parsera Markdown do zasilania grafu Neo4j — `class MarkdownNeo4jParser: def __init__(self, driver, doc_path:Path): self.driver=driver; self.ast=mistune.create_markdown(renderer=mistune.ASTRenderer())(doc_path.read_text())`; metoda `parse(self)→ExtractionReport`: `sections=self._extract_sections(self.ast)`; dla każdej sekcji: `events=[self._to_event_frame(li, heading=s['heading']) for li in s['list_items']]`; `self._batch_write(events)`; `_to_event_frame(li, heading)`: `text=li['children'][0]['raw']`; zwraca `{'id':hash(text),'text':text,'domain':'CONTRACT','source_doc_id':str(doc_path),'topic':heading}`; `_batch_write(frames)`: `UNWIND $frames AS f MERGE (e:EventFrame {id:f.id}) ON CREATE SET e+=f MERGE (t:Topic {name:f.topic}) MERGE (e)-[:BELONGS_TO]->(t)`; szkielet działa dla każdego `.md` z nagłówkami `#`/`##` i listami?
- Jak wstrzyknąć łańcuch przyczynowy Wymiaru 6 do grafu — Cypher: `MERGE (e1:EventFrame {id:'e_deadline',domain:'CONTRACT'}) MERGE (t:Token {lemma:'2026-01-15',type:'DATE'}) MERGE (e1)-[:HAS_ROLE {role:'TIME'}]->(t) MERGE (e2:EventFrame {id:'e_penalty',domain:'CONTRACT'}) MERGE (e2)-[:HAS_ROLE {role:'AGENT'}]->(:Token {lemma:'Zamawiający'}) MERGE (e1)-[:CAUSES]->(e2)`; wynik: `e_deadline(TIME=2026-01-15)-[:CAUSES]->e_penalty(AGENT=Zamawiający)`; query TEMPORAL-01: `MATCH (e)-[:HAS_ROLE {role:'TIME'}]->(t) WHERE date(t.lemma)<date() MATCH (e)-[:CAUSES]->(cons) RETURN e.id, cons.id` wykrywa przeterminowany termin i propaguje kaskadę do konsekwencji; `conftest.py` fixture `causal_chain_w6` replikuje ten wzorzec z teardown `DETACH DELETE`?
- Jak modelować relacje agent-akcja-obiekt na grafie semantycznym — rozszerzone modelowanie z synonimią: `(e:EventFrame)-[:HAS_ROLE {role:'AGENT', confidence:0.95}]->(a:Token {lemma:'Wykonawca'})-[:HAS_SYNSET]->(:Synset {id:'s_legal_person', domain:'LEGAL_PERSON'})`; `confidence` na krawędzi `HAS_ROLE` = wynik dep-parse (0.0–1.0) pozwala filtrować niepewne ekstrakcje; `domain` na `Synset` umożliwia `CrossReferenceEngine.aggregate_cross_domain()` groupowanie bez osobnego lookup; query semantic graph: `MATCH (e)-[:HAS_ROLE]->(t)-[:HAS_SYNSET]->(s) WHERE s.domain='LEGAL_PERSON' RETURN e.id, t.lemma` — agent semantyczny niezależnie od formy (`Wykonawca`/`Dostawca`/`Kontrahent`)?
- Jak w Neo4j odwzorować relacje AGENT, PATIENT i THEME — trzy role SRL: `AGENT` = inicjator akcji (`nsubj`); `PATIENT` = obiekt zmieniający stan (`obj/dobj`) — np. `'dokumentacja' po 'dostarczyć'`; `THEME` = obiekt bez zmiany stanu, treść przekazu (`ccomp/xcomp`) — np. `'że system działa'` po `'potwierdza'`; Cypher: `MERGE (e)-[:HAS_ROLE {role:'AGENT'}]->(a) MERGE (e)-[:HAS_ROLE {role:'PATIENT'}]->(p) MERGE (e)-[:HAS_ROLE {role:'THEME'}]->(th:Clause {text:$clause_text})`; `THEME` jako węzeł `(:Clause)` gdy dopełnienie to zdanie podrzędne; `DependencyParserAdapter.extract_roles()` rozróżnia PATIENT (`obj`) od THEME (`ccomp`) przez `t.dep_`?
- Pokaż kod parsera Markdown tworzącego strukturę Document-Section-Paragraph — 3-poziomowa hierarchia: `MERGE (doc:Document {id:hash(path), path:$path, title:$h1}) MERGE (sec:Section {id:hash(path+h2), heading:$h2, level:2}) MERGE (doc)-[:HAS_SECTION]->(sec) MERGE (par:Paragraph {id:hash(text), text:$text, order:$idx}) MERGE (sec)-[:HAS_PARAGRAPH {order:$idx}]->(par)`; parser: nagłówek `#` → `Document`, `##` → `Section`, `###` → subsection jako `Section {level:3}`; listy: każdy `list_item` → `Paragraph {type:'LIST_ITEM'}`; `MarkdownNeo4jParser._extract_hierarchy(ast)→List[HierarchyNode]`; `doc→sec→par` jako ścieżka dla `DocumentLogicParser` i `MarkdownRelationExtractor`?
- Jak wdrożyć `spacy-pl` do `MarkdownGraphParser` — integracja: `class MarkdownGraphParser(MarkdownNeo4jParser): def __init__(self, driver, doc_path, nlp_pipeline:NLPPipeline): super().__init__(driver, doc_path); self.nlp=nlp_pipeline`; `_to_event_frame(li)` wzbogacony: `text=li['children'][0]['raw']; doc=self.nlp.enrich(text); roles=extract_aro(text, self.nlp.nlp); frame={'id':hash(text),'text':text,'agent':roles.agent,'action':roles.action,'patient':roles.patient}`; `ObligationDetector` decyduje czy `list_item` to EventFrame (`musi/należy`) czy zwykły `Paragraph`; `NLPPipeline(spacy.load('pl_core_news_lg'), SlowosiecProxy.from_neo4j(uri,auth))` wstrzykiwany przez DI — parser testowalny z `Mock(NLPPipeline)`?
- Jak zmapować intencję 'prewencja' na protokół medyczny w grafie — model ontologiczny: `MERGE (:IntentType {type:'PREVENTION', domain:'MEDICAL'})` jako węzeł taksonomii intencji rozszerzający Austin; relacja: `(e:EventFrame {intent:'PREVENTION'})-[:TRIGGERS_PROTOCOL]->(:MedicalProtocol {id:$pid, code:'ICD-10-Z29', name:$name})`; `MedicalProtocol` dziedziczy z `(:ComplianceDocument)` — ta sama infrastruktura co `LegalReference`; query walidacyjny: `MATCH (e)-[:TRIGGERS_PROTOCOL]->(p:MedicalProtocol) WHERE NOT (e)-[:HAS_AUTHORIZATION]->() RETURN e.id AS missing_auth` → `Violation('MEDICAL-01', severity:'HIGH', domain:'MEDICAL')`; `IntentClassifier` rozszerzony o `PREVENTION` gdy `token.lemma_ in {'zapobiegać','chronić','profilaktycznie'}` + `domain='MEDICAL'`; tej samej ścieżki używa `LEGAL` (Art.25 KK) i `SECURITY` (ISO 27001 control)?
- Stwórz model grafu dla zdarzenia z intencją obrony własnej — węzły: `MERGE (e:EventFrame {id:'e_self_defense', domain:'LEGAL', intent:'SELF_DEFENSE'}) MERGE (i:IntentType {type:'SELF_DEFENSE', legal_basis:'Art.25 KK'}) MERGE (e)-[:HAS_INTENT]->(i) MERGE (e)-[:HAS_ROLE {role:'AGENT'}]->(:Token {lemma:'oskarżony'}) MERGE (e)-[:HAS_ROLE {role:'PATIENT'}]->(:Token {lemma:'agresor'}) MERGE (e)-[:IS_RESPONSE_TO]->(:EventFrame {id:'e_aggression', type:'AGGRESSION'})`; relacja `IS_RESPONSE_TO` koduje proporcjonalność — query: `MATCH (e {intent:'SELF_DEFENSE'}) WHERE NOT (e)-[:HAS_INTENT]->(:IntentType {legal_basis:_}) RETURN e.id` → `Violation('LEGAL-INTENT-01', severity:'HIGH')`; każda obrona własna w grafie wymaga powiązanego węzła `IntentType` z atrybutem `legal_basis`; wzorzec reużywalny dla SELF_DEFENSE/NECESSITY/DURESS jako podtypy domeny LEGAL?
- Jak zmapować intencję warunku na relację `[:ACTIVATED_BY]` w grafie — pełny wzorzec MERGE dla `CONDITIONAL_OBLIGATION`: `MERGE (sa:SpeechAct {id:$sid, type:'CONDITIONAL_OBLIGATION', subtype:$subtype}) MERGE (cond:TriggerCondition {id:hash($cond_text), text:$cond_text}) MERGE (sa)-[:ACTIVATED_BY]->(cond) MERGE (e:EventFrame {id:$frame_id}) MERGE (e)-[:HAS_SPEECH_ACT]->(sa)`; `TriggerCondition.text` = tekst zdania podrzędnego wyciągniętego przez `mark+advcl` dep-rel; query COND-01: `MATCH (sa:SpeechAct {type:'CONDITIONAL_OBLIGATION'}) WHERE NOT (sa)-[:ACTIVATED_BY]->(:TriggerCondition) RETURN sa.id` → `Violation('COND-01', severity:'MEDIUM')`; `TriggerCondition` reużywalny — wiele `SpeechAct` może być `ACTIVATED_BY` tym samym warunkiem (np. jeden `art.5 UODO` triggeruje 3 różne obowiązki)?
- Jak stworzyć mapę relacji semantycznych jako `SemanticRelationType(Enum)` — top-20 nazwanych stałych dla spójności nazw relacji we wszystkich parserach: `HAS_ROLE`, `HAS_SPEECH_ACT`, `CAUSES`, `IS_RESPONSE_TO`, `ACTIVATED_BY`, `TRIGGERS_PROTOCOL`, `HYPERNYM_OF`, `HAS_SYNSET`, `BELONGS_TO_DOMAIN`, `HAS_LEGAL_BASIS`, `HAS_SECTION`, `HAS_PARAGRAPH`, `HAS_INTENT`, `AT_LOCATION`, `WITHIN_TIMEFRAME`, `DELEGATES_TO`, `HAS_BRIDGE_RULE`, `EXPRESSED_IN`, `HAS_AUTHORIZATION`, `HAS_BACKUP_PROCEDURE`; `SemanticRelationType.HAS_ROLE.value='HAS_ROLE'`; wszystkie parsery (`MarkdownGraphParser`, `SemanticMapper`, `DocumentLogicParser`) importują `SemanticRelationType` zamiast string literals — typo w nazwie relacji staje się `AttributeError` przy kompilacji, nie cichym błędem w runtime?
- Pokaż strukturę parsera Markdown dla dokumentacji technicznej w Neo4j — `ExtractionReport = NamedTuple('ExtractionReport', [('document_id', str), ('nodes_created', int), ('relations_created', int), ('events_extracted', int), ('errors', List[str])])`; `MarkdownNeo4jParser.parse(self)->ExtractionReport`: zlicza wszystkie `CREATE` vs `MATCH` z odpowiedzi `summary.counters.nodes_created`; `errors` = lista zdań gdzie `_to_event_frame()` wyrzucił wyjątek; `ExtractionReport.is_clean` = `len(errors)==0`; `parse()` nigdy nie rzuca wyjątku — wszystkie błędy lądują w `errors`; `AuditPipeline` logi: `if not report.is_clean: logger.warning('%d ekstrakcji nie powiodło się', len(report.errors))`?
- Jak modelować relacje przestrzenne w grafie zdarzeń — wymiar `LOCATION` jako `[:AT_LOCATION {precision:'city'|'building'|'GPS'}]`: `MERGE (e)-[:AT_LOCATION {precision:'building'}]->(:Location {name:'Centrum_DC', lat:52.23, lon:21.01})`; `precision` kontroluje granularność audytu — `city` dla umów ramowych, `GPS` dla protokołów operacyjnych; `GEO-01` reguła: `MATCH (e:EventFrame {domain:'OPERATIONAL'}) WHERE NOT (e)-[:AT_LOCATION]->() RETURN e.id` → `Violation('GEO-01', severity:'MEDIUM')`; relacja `[:WITHIN_DISTANCE {meters:500}]` między `(:Location)` węzłami umożliwia geospatial query `MATCH (e)-[:AT_LOCATION]->(l1) MATCH (l1)-[:WITHIN_DISTANCE]->(l2:Location {name:'Server_Room'}) RETURN e.id` — zdarzenia w promieniu serwerowni?
- Napiszmy zapytanie Cypher dla ścieżki pojęć w grafie hiperonimii — variable-depth traversal: `MATCH path=(s:Synset {lemma:$root})-[:HYPERNYM_OF*1..5]->(h:Domain) WITH h, min(length(path)) AS dist RETURN h.name AS domain, dist ORDER BY dist`; wersja z pamięciową kontrolą: `CALL { WITH $root AS root MATCH (s:Synset {lemma:root})-[:HYPERNYM_OF*1..3]->(h) RETURN h LIMIT 100 } RETURN h.name, h.domain`; `CREATE INDEX FOR (s:Synset) ON (s.lemma)` — warunek konieczny dla O(1) lookup root; `min(length(path))` eliminuje duplikaty przy wielu ścieżkach do tego samego węzła domenowego; `shortest_path(s, h)` przez `CALL apoc.path.spanningTree()` gdy APOC dostępny — eliminuje O(n²) przeszukiwanie przy gęstych grafach synsetowych?
- Jak rozwiązać wieloznaczność synsetów przy zapisie do grafu — konwencja nazewnicza: `[:HYPERNYM_OF]` dla ścieżek Słowosieć-derived, `[:IS_A]` dla OWL-derived ontology — jako oddzielne stałe `SemanticRelationType.HYPERNYM_OF` i `SemanticRelationType.IS_A`; WSD przy zapisie: `SemanticMapper._write_token_synset(session, token, context)` wywołuje `proxy.disambiguate(token.lemma_, ctx_lemmas)→best_synset_id`; `MERGE (:Synset {id:best_synset_id, lemma:token.lemma_})` — zapisuje tylko disambiguowany synset zamiast wszystkich kandydatów; query weryfikujący rozbieżność: `MATCH (t:Token)-[:HAS_SYNSET]->(s) WHERE count{(t)-[:HAS_SYNSET]->()} > 1 RETURN t.lemma, count(*) AS synset_count` — tokeny z >1 synsetu = niezambiguizowane; cel: po WSD `synset_count` = 1 dla wszystkich tokenów?
- Pokaż zapytanie Cypher dla wyekstrahowanych ról Agent-Akcja-Obiekt — retrieval query: `MATCH (e:EventFrame) OPTIONAL MATCH (e)-[:HAS_ROLE {role:'AGENT'}]->(a:Token) OPTIONAL MATCH (e)-[:HAS_ROLE {role:'ACTION'}]->(v:Token) OPTIONAL MATCH (e)-[:HAS_ROLE {role:'PATIENT'}]->(p:Token) RETURN e.id AS frame_id, e.domain, a.lemma AS agent, v.lemma AS action, p.lemma AS patient`; `OPTIONAL MATCH` dla PATIENT — zdania bez dopełnienia zwracają `patient=null`; filtr kontraktowy: `WHERE e.domain='CONTRACT'`; wykrywanie brakujących agentów: `WHERE a IS NULL` → te same frame_id co ROLE-01 query; paginacja: `ORDER BY e.id SKIP $offset LIMIT 50` dla dużych grafów; `Neo4jAdapter.get_aro_triples(domain=None, limit=50)->List[ARO]` jako wygodna metoda?
- Jakie są różnice między rolami Patient a Theme w grafie — PATIENT = obiekt zmieniający stan po akcji (`obj/dobj` → `'dokumentacja'` po `'dostarczyć'`); THEME = treść przekazu bez zmiany stanu (`ccomp/xcomp` → `'że system działa'` po `'potwierdza'`); w grafie: PATIENT → `(:Token {lemma:...})`, THEME → `(:Clause {text:...})`; distinguishing query: `MATCH (e)-[:HAS_ROLE {role:'PATIENT'}]->(p:Clause) RETURN e.id` → `Violation('ROLE-03')` — Clause node omyłkowo zapisany jako PATIENT zamiast THEME; `SemanticMapper.extract_roles()`: `if t.dep_ in('ccomp','xcomp'): role='THEME'; elif t.dep_ in('obj','dobj'): role='PATIENT'`; test: `'Wykonawca potwierdza że system działa'` → `THEME=Clause{text:'że system działa'}`, nie `PATIENT=Token{lemma:'system'}`; THEME nie podlega `Violation('ROLE-01')` — brak THEME jest akceptowalny?
- Jak połączyć GraphEmitter z modelem relacji w Neo4j — `@dataclass Triple(subject:str, predicate:str, object:str, role:str, doc_id:str)`; `GraphEmitter.emit(triples:List[Triple])->List[str]` generuje Cypher MERGE per trójkę: `f"MERGE (s:Token {{lemma:'{t.subject}'}})-[:HAS_ROLE {{role:'{t.role}',doc_id:'{t.doc_id}'}}]->(o:Token {{lemma:'{t.object}'}})"`; `GraphEmitter.flush(session, triples)`: `session.run("UNWIND $rows AS row MERGE (s:Token {lemma:row.subject}) MERGE (o:Token {lemma:row.object}) MERGE (s)-[:HAS_ROLE {role:row.role, doc_id:row.doc_id}]->(o)", rows=[asdict(t) for t in triples])` — jedno wywołanie zamiast N+1; `GraphEmitter.emit_from_doc(doc:Doc, doc_id:str)->List[Triple]`: `SemanticMapper.map(doc)→frames` → `[Triple(f.agent, f.predicate, f.patient, 'PATIENT', doc_id) for f in frames if f.patient]`; integracja: `MarkdownGraphParser → SemanticMapper → GraphEmitter → Neo4jAdapter.flush()`; `NLPPipeline.with_graph_emitter(emitter)` jako factory — `emitter` wstrzykiwalny w testach przez `Mock(spec=GraphEmitter)`?
- Pokaż model danych grafu dla ról semantycznych z relacją TIME — kompaktowy schemat referencyjny: węzeł centralny `(e:EventFrame {id, predicate, domain, speech_act, theme_topic, rheme_focus})`; 6 krawędzi `[:HAS_ROLE {role}]` do `(:Token {lemma, pos, type})`; kompletny przykład: `(e:EventFrame {id:'e1', predicate:'dostarczyć', domain:'CONTRACT', speech_act:'POLECENIE'})-[:HAS_ROLE {role:'AGENT'}]->(:Token {lemma:'Wykonawca'}), -[:HAS_ROLE {role:'ACTION'}]->(:Token {lemma:'dostarczyć'}), -[:HAS_ROLE {role:'PATIENT'}]->(:Token {lemma:'SRS'}), -[:HAS_ROLE {role:'INSTRUMENT'}]->(:Token {lemma:'repozytorium'}), -[:HAS_ROLE {role:'LOCATION'}]->(:Token {lemma:'serwer'}), -[:HAS_ROLE {role:'TIME'}]->(:Token {lemma:'2026-01-15', type:'DATE'})`; TIME specials: `type:'DATE'` trigger TEMPORAL-01 gdy `date(t.lemma)<date()`; `TemporalDimensionValidator.validate()` odpytuje oba queries (brak TIME + przekroczony termin) w jednym przebiegu; `SemanticRelationType` enum pokrywa wszystkie 6 ról — `SemanticRelationType.TIME='TIME'` jako stała importowana przez wszystkie parsery?
- Pokaż przykład ontologii dla relacji AGENT-AKCJA-OBIEKT w Neo4j — hierarchia 3-poziomowa: `(:OntologyClass {name:'działanie', abstract:True})-[:IS_A]->(:EventType {name:'dostarczenie'})-[:INSTANCE_OF]->(:EventFrame {id:'e1'})`; query traversujący wszystkie poziomy: `MATCH (oc:OntologyClass)-[:IS_A*1..3]->(et:EventType)-[:INSTANCE_OF]->(e:EventFrame) WHERE oc.name='działanie' RETURN oc.name, et.name, e.id, e.predicate`; role jako `DimensionType` połączone z klasą: `MERGE (oc)-[:DEFINES_ROLE]->(dt:DimensionType {name:'AGENT', required:True})`; AAO query z ontologią: `MATCH (e)-[:HAS_ROLE {role:'AGENT'}]->(a), (e)-[:HAS_ROLE {role:'ACTION'}]->(v), (e)-[:INSTANCE_OF]->(et)-[:IS_A*]->(oc:OntologyClass) RETURN oc.name AS class, a.lemma AS agent, v.lemma AS action`; `OntologyLoader.seed_from_json(path)` tworzy hierarchię jednorazowo przy starcie — query łączy dane instancyjne z ontologią bez JOIN; nowe klasy automatycznie przez `OntologyBuilder.infer_domain()`?
- Jak spaCy identyfikuje THEME w porównaniu do PATIENT przez dep-labels — kompletna tabela dep-rel → rola: `obj/dobj` → PATIENT (bezpośredni obiekt, zmieniający stan); `iobj` → PATIENT_INDIRECT (odbiorca transferu — `'Zamawiającemu'` w `'dostarczył SRS Zamawiającemu'`); `ccomp/xcomp` → THEME (zdanie dopełniające); `obl` → INSTRUMENT gdy `{NER_type:'PRODUCT'/'ORG'}` albo LOCATION gdy `{NER_type:'LOC'/'GPE'}`; `obl` bez NER → fallback MANNER; `ROLE-04` (new): `MATCH (e)-[:HAS_ROLE {role:'PATIENT'}]->(a:Token), (e)-[:HAS_ROLE {role:'PATIENT_INDIRECT'}]->(b:Token) WHERE NOT (e)-[:HAS_ROLE {role:'AGENT'}]->() RETURN e.id` — transfer bez agenta; test: `'dostarczył SRS Zamawiającemu'` → `PATIENT='SRS'` + `PATIENT_INDIRECT='Zamawiający'`; `iobj` odróżnia adresata transferu od tematu — klucz do modelowania zobowiązań kontraktowych z odbiorcą?
- Jak rozbudować ontologię o relacje czasowe TIME i przestrzenne LOCATION — `OntologyExpander.add_temporal_relations()`: `MERGE (:RelationType {name:'BEFORE', inverse:'AFTER', symmetric:False})`; `MERGE (:RelationType {name:'SIMULTANEOUS', inverse:'SIMULTANEOUS', symmetric:True})`; TIME relations między EventFrame'ami: `(e1)-[:BEFORE {certainty:0.9}]->(e2)` gdy `e1.time < e2.time` w tym samym dokumencie; LOCATION ontologia: `(:LocationType {name:'PHYSICAL'})<-[:IS_A]-(:LocationType {name:'SERVER'})<-[:IS_A]-(:Token {lemma:'serwer_produkcyjny'})`; spatial query: `MATCH (e)-[:HAS_ROLE {role:'LOCATION'}]->(l:Token)-[:IS_A*]->(lt:LocationType) RETURN lt.name, count(e) AS events_at_type`; `GEO-01` extends: `MATCH (e1)-[:BEFORE]->(e2) WHERE e1.location != e2.location RETURN e1.id` → LOCATION_INCONSISTENCY; `OntologyExpander` rejestrowany w `DeductionEngine` — rozszerza domenę bez zmiany reguł bazowych?
- Pokaż przykładowe zapytania Cypher do audytu braków w procedurach backupu — `BACKUP-01`: `MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->(:BackupProcedure) RETURN db.id AS node_id` → `Violation('BACKUP-01', severity='HIGH')`; `BACKUP-02` (nieaktualna procedura): `MATCH (db)-[:HAS_BACKUP_PROCEDURE]->(bp:BackupProcedure) WHERE NOT (bp)-[:VERIFIED_ON]->(:Date) OR bp.last_verification < date()-duration('P90D') RETURN db.id, bp.id` → MEDIUM; `BACKUP-03` (brak testu przywrócenia): `MATCH (bp:BackupProcedure) WHERE NOT (bp)-[:HAS_RESTORE_TEST]->() RETURN bp.id` → CRITICAL; seed fixture: `MERGE (:Database {id:'db_prod'})-[:HAS_BACKUP_PROCEDURE]->(bp:BackupProcedure {id:'bp_01', last_verification:date('2025-01-01')})` — trigger BACKUP-02 gdy `date()-date('2025-01-01') > 90 dni`; `BackupDomainValidator.validate(session)->List[Violation]` odpytuje BACKUP-01/02/03 w jednym przebiegu — domknięcie domeny BACKUP jak SEC-03/04/05 dla SECURITY?
- Pokaż przykład analizy wymiarowej dla zdania o awarii systemu — zdanie: `'System bazodanowy nie przetwarza żądań ponieważ moduł szyfrowania nie jest dostępny.'`; `NLPExtractor.extract(text)` → `EventFrame(id='e_fail', predicate='przetwarzać', speech_act='ASSERT', negated=True, domain='INFRA')` z wymiarami: `AGENT='System bazodanowy'`, `ACTION='przetwarzać'`, `INSTRUMENT='moduł szyfrowania'`, `cause_dimension='moduł szyfrowania nie jest dostępny'`; `EventReasoningEngine.apply(frame)`: `frame.negated AND INSTRUMENT → CAUSAL-01` (PASS — cause_dimension ustawiony przez `causal_marker_detection`); `INSTR-01` (moduł szyfrowania bez wersji → LOW); `CAUSAL-02` gdy `frame.domain='INFRA'` i `cause.domain='SEC'` → CROSS_DOMAIN_CAUSE HIGH; `[:CAUSED_BY]` krawędź: `MERGE (e_fail)-[:CAUSED_BY]->(e_encryption_unavailable)`; propagacja przez `CrossReferenceEngine` do EventFrame'ów kontraktowych referencujących system?
- Jak zaimplementować interfejs QA do odpytywania grafu wiedzy — `KnowledgeGraphQA.answer(question:str)->QAResponse`: pipeline: `QuestionParser.parse(q)→CypherIntent(query_type, entities, filters)` → `CypherBuilder.build(intent)→cypher` → `Neo4jAdapter.run(cypher)→rows` → `AnswerFormatter.format(rows)→str`; `QuestionParser` rozpoznaje 3 intenty: `FIND_AGENT` (`'kto jest agentem {X}'` → `MATCH (e:EventFrame {id:$X})-[:HAS_ROLE {role:'AGENT'}]->(a) RETURN a.lemma`), `FIND_VIOLATIONS` (`'jakie zdarzenia naruszają {RULE}'` → `MATCH (v:Violation {rule_id:$RULE})-[:FOR_EVENT]->(e) RETURN e.id`), `FIND_CAUSE` (`'dlaczego {X} nie działa'` → `MATCH (e:EventFrame {id:$X})-[:CAUSED_BY*1..3]->(c) RETURN c.predicate`); `@dataclass QAResponse(answer:str, confidence:float, cypher_used:str, nodes_matched:int)`; `QuestionParser` używa `SlowosiecProxy` do synonimizacji — `'dostarczenie'`↔`'dostawa'`; `AuditPipeline.qa` property zwraca `KnowledgeGraphQA(self.adapter)`?
- Pokaż jak zintegrować obsługę zaimków i koreferencji w grafie — end-to-end: `CorefAwareSemanticMapper.map(doc)→frames` + `PolishCoreferenceResolver.resolve(doc)→coref_map` + `GraphEmitter.emit(triples, session)`; krawędź w grafie: `MERGE (p:Token {lemma:'on',pos:'ppron3'})-[:COREFERENCE_OF]->(a:Token {lemma:'Wykonawca'})`; `[:SAME_AGENT]`: `MERGE (e1:EventFrame)-[:SAME_AGENT]->(e2:EventFrame)` gdy `e1.resolved_agent==e2.resolved_agent`; łańcuch query: `MATCH chain=(e1)-[:SAME_AGENT*1..5]->(e5) WHERE length(chain)>=3 RETURN [n IN nodes(chain) | n.predicate] AS agent_actions`; `COREREF-01`: `MATCH (e:EventFrame) WHERE e.has_pronoun=True AND e.agent IS NULL AND NOT (e)-[:SAME_AGENT]->() RETURN e.id`; test integracyjny: `def test_coref_merged_to_graph(seeded_session): frames=mapper.map(doc_with_pronoun); emit(frames, seeded_session); n=seeded_session.run('MATCH ()-[:SAME_AGENT]->() RETURN count(*) AS n').single()['n']; assert n>=1`?
- Zdefiniujmy podstawowe węzły ontologii w katalogu nlp/ z lokalną bazą Neo4j — struktura katalogów: `nlp/ontology/seed.cypher` (węzły DimensionType + OntologyClass), `nlp/models/event_frame.py` (dataclass AAO), `nlp/extractors/semantic_mapper.py`, `nlp/rules/` (LinterRule subclasses), `nlp/adapters/neo4j_adapter.py`, `nlp/conftest.py` (fixtures); `nlp/ontology/seed.cypher`: `MERGE (:DimensionType {name:'AGENT', required:True}) MERGE (:DimensionType {name:'ACTION', required:True}) MERGE (:DimensionType {name:'PATIENT', required:False}) ...` dla 6 ról + `MERGE (:OntologyClass {name:'działanie', abstract:True})`; uruchomienie: `cypher-shell -u neo4j -p test < nlp/ontology/seed.cypher`; `@pytest.fixture def seeded_session(neo4j_session_real): seed(neo4j_session_real); yield neo4j_session_real` jako base fixture; test: `assert session.run('MATCH (dt:DimensionType) RETURN count(dt) AS n').single()['n'] == 6`?
- Jak modelować łańcuchy przyczynowe CAUSE i EFFECT w ontologii Neo4j — `OntologyExpander.add_causal_relations()`: `MERGE (:RelationType {name:'CAUSES', inverse:'CAUSED_BY', transitive:True})`; `MERGE (:RelationType {name:'ENABLES', inverse:'ENABLED_BY', transitive:False})`; chain insertion: `MERGE (e1)-[:CAUSES]->(e2)-[:CAUSES]->(e3)`; traversal: `MATCH p=(e:EventFrame)-[:CAUSES*1..5]->(end) RETURN p, length(p) AS depth ORDER BY depth DESC LIMIT 10`; `EFFECT` jako derived: `end`-węzeł w ścieżce `CAUSES*` bez osobnej krawędzi; `CROSS-DOMAIN-CAUSE`: `MATCH (e1)-[:CAUSES*1..3]->(e2) WHERE e1.domain != e2.domain RETURN e1.domain, e2.domain, count(*) AS crossings`; `ENABLES` vs `CAUSES`: `CAUSES` deterministyczny (naruszenie → kara); `ENABLES` probabilistyczny (brak backupu → możliwa utrata); `RiskScoreCalculator.risk(chain:Path)->float` = `product(r.certainty for r in chain.rels())`; `chain.rels()` przez QPP `((a)-[r:CAUSES WHERE r.certainty IS NOT NULL]->{1,5}(b))`?
- Jakie zapytanie Cypher wywoła interfejs QA dla luk backupu — `KnowledgeGraphQA` intent `FIND_VIOLATIONS` z `rule_id='BACKUP-01'`: `MATCH (db:Database) WHERE NOT (db)-[:HAS_BACKUP_PROCEDURE]->() RETURN db.id AS answer`; wywołanie: `qa.answer('Które bazy danych nie mają procedury backupu?')` → `QuestionParser` rozpoznaje `FIND_VIOLATIONS` + `'backup'→rule_id='BACKUP-01'`; rozszerzone pytanie: `'Których procedur backupu nie weryfikowano ponad 90 dni?'` → BACKUP-02 query; `QAResponse(answer='db_prod, db_archive', confidence=0.9, cypher_used='MATCH...', nodes_matched=2)`; `qa.answer()` loguje do `QueryAuditLog.jsonl` — pełna historia pytań QA; `KnowledgeGraphQA.batch_answer(questions:List[str])->List[QAResponse]` dla raportów automatycznych; test: `def test_qa_backup(seeded_session): qa=KnowledgeGraphQA(adapter); resp=qa.answer('Które bazy...'); assert 'db_prod' in resp.answer`?
- Jak wdrożyć QPP w Cypher 25 dla analizy ścieżek w grafie — QPP (Quantified Path Patterns) = `MATCH p=((a)-[r:CAUSES]->{1,5}(b))` zamiast `[:CAUSES*1..5]`; QPP z filtrem węzłów: `MATCH ((e1:EventFrame)-[r:CAUSES]->{1,5}(e2:EventFrame WHERE e2.domain='CONTRACT'))` — filtruje węzły wewnątrz ścieżki bez zewnętrznego WHERE; QPP łączony: `MATCH ((a:EventFrame)-[:SAME_AGENT]->{0,1}(b)-[:CAUSES]->{1,3}(c))` — koreferencja + kauzalność w jednym wzorcu; w Neo4j 5.9+ QPP stabilne (GQL-compatible); różnica vs `*1..5`: QPP pozwala `WHERE` per węzeł/krawędź wewnątrz `()`; BACKUP chain: `MATCH ((db:Database)-[:HAS_BACKUP_PROCEDURE]->{0,1}(bp)-[:CAUSED_BY]->{1,3}(root)) WHERE db.id=$db_id`; `EXPLAIN MATCH ((a)-[r:CAUSES]->{1,5}(b)) RETURN a` → `QPP_EXPAND` w planie zapytania?
- Wyjaśnij jak QARC automatycznie kompresuje relacje w grafie wiedzy — QARC (Query-based Automatic Relation Consolidation): wzorzec eliminujący redundantne krawędzie tworzone przez wielokrotny import; problem: `GraphEmitter.flush()` z `CREATE` (nie `MERGE`) tworzy duplikaty `[:CAUSES]`; QARC dedup query: `MATCH (a)-[r1:CAUSES]->(b), (a)-[r2:CAUSES]->(b) WHERE id(r1)<id(r2) DELETE r2`; token dedup: `MATCH (a:EventFrame)-[r:HAS_ROLE {role:'AGENT'}]->(t1:Token {lemma:$l}), (a)-[s:HAS_ROLE {role:'AGENT'}]->(t2:Token {lemma:$l}) WHERE id(t1)<id(t2) DETACH DELETE t2`; `QARCRunner.run(session, edge_types=['CAUSES','HAS_ROLE','SAME_AGENT'])` jako maintenance task po bulk import; `MERGE` w `GraphEmitter.flush()` zapobiega duplikatom przy insercie — QARC jako fallback dla legacy danych importowanych CREATE; `QARCRunner.dry_run()` zwraca `{edge_type, duplicates_count}` bez DELETE — audit tryb?
- Jak rozbudować ontologię o relacje TIME i LOCATION dla łańcuchów zdarzeń — `OntologyExpander.add_temporal_chain_rules()`: `MERGE (:RelationType {name:'BEFORE', inverse:'AFTER', symmetric:False, transitive:True})` + `MERGE (:RelationType {name:'SIMULTANEOUS', inverse:'SIMULTANEOUS', symmetric:True})`; TIME relation między EventFrame'ami: `(e1)-[:BEFORE {certainty:0.9, source:'timestamp_cmp'}]->(e2)` gdy `e1.event_date < e2.event_date` w tym samym dokumencie; `DeductionEngine.add_rule(TEMPORAL_TRANS)`: `IF (A)-[:BEFORE]->(B) AND (B)-[:BEFORE]->(C) THEN MERGE (A)-[:BEFORE {inferred:True}]->(C)` — domknięcie przechodnie; LOCATION hierarchia: `(:Token {lemma:'serwer_prod'})-[:IS_A]->(:LocationType {name:'SERVER'})-[:IS_A]->(:LocationType {name:'PHYSICAL'})`; spatial query: `MATCH (e)-[:HAS_ROLE {role:'LOCATION'}]->(l)-[:IS_A*]->(lt:LocationType) RETURN lt.name, count(e) AS events_at_type`; `GEO-01`: `MATCH (e1)-[:BEFORE]->(e2) WHERE e1.location IS NOT NULL AND e1.location<>e2.location RETURN e1.id` → `Violation('GEO-01','LOCATION_SEQUENCE_INCONSISTENCY')`; `TimelineBuilder.build(doc_id)->List[Tuple[EventFrame,EventFrame,str]]` porządkuje zdarzenia według wymiarów TIME?
- Pokaż jak SłowosiećProxy zinterpretuje pojęcie 'agent AI' w grafie semantycznym — `SlowosiecProxy.disambiguate_compound(phrase:str)->SynsetResult` dla wyrażeń wielosłownych; `'agent AI'`: decompose → `'agent'` (14 synsetów w plWordNet) + `'AI'` (DomainDictionaryPL override); WSD strategia dla MWE: `MultiWordExpression.context_score(phrase, candidates)` = suma `PMI(word_i, word_j)` dla par słów w frazie × `domain_boost`; `score('agent.8_software') > score('agent.1_human')` gdy kontekst zawiera `TECH_TOOL` tokeny w oknie 5; `phrase_to_graph()`: `MERGE (:Concept {name:'agent_AI', domain:'AI'})-[:IS_A]->(:Concept {name:'agent_programowy'})-[:IS_A]->(:Concept {name:'byt_autonomiczny'})`; `MWE_PATTERNS={'agent AI':('agent.8','Concept.AI_AGENT'), 'model językowy':('model.3','Concept.LLM')}` jako override w `DomainDictionaryPL`; test: `proxy.disambiguate_compound('agent AI').synset_id == 'agent.8'`; `SlowosiecProxy.disambiguate_compound()` deleguje do `SlowosiecProxy.disambiguate()` dla OOV multi-word bez wpisu w `MWE_PATTERNS`?
- Jakie reguły Cypher 25 obsługują wnioskowanie w wymiarze przyczynowo-kontekstowym — kompletny zestaw `CausalRuleEngine` oparty na Cypher 25: (1) **CAUSAL-TRANS** domknięcie przechodnie: `MATCH (a)-[:CAUSES]->(b)-[:CAUSES]->(c) WHERE NOT (a)-[:CAUSES]->(c) MERGE (a)-[:CAUSES {inferred:True, depth:2}]->(c)`; (2) **CAUSAL-CYCLE** detekcja cyklu: `MATCH p=(e)-[:CAUSES*2..]->(e) RETURN e.id AS cycle_node` — wynik niepusty = błąd strukturalny; (3) **CAUSAL-AGENT**: `MATCH (e)-[:CAUSES]->(eff) WHERE NOT (e)-[:HAS_ROLE {role:'AGENT'}]->() RETURN e.id` → `Violation('CAUSAL-03','MISSING_AGENT_IN_CHAIN','HIGH')`; (4) **QPP CAUSAL-RISK** Cypher 25: `MATCH ((src:EventFrame)-[r:CAUSES WHERE r.certainty IS NOT NULL]->{1,5}(dst:EventFrame WHERE dst.domain='CONTRACT')) RETURN src.id, sum(r.certainty) AS risk` — filtr wewnątrz QPP + suma certainty = scoring ryzyka; `CausalRuleEngine([CAUSAL_TRANS, CAUSAL_CYCLE, CAUSAL_AGENT, CAUSAL_RISK])` jako `InferenceModule` w `DeductionEngine`?
- Jak zaimplementować wymiarowanie zdarzeń przez EventDimensionMatrix dla analizy przyczynowo-kontekstowej — `EventDimensionMatrix` jako tabela 6 wymiarów × n zdarzeń: wiersze = `EventFrame.id`, kolumny = `{AGENT, ACTION, PATIENT, TIME, LOCATION, INSTRUMENT}`; wartość komórki = `lemma|None` + `confidence:float`; `CausalContextAnalyzer.build_matrix(frames)->EventDimensionMatrix`: `MATCH (e:EventFrame)-[:HAS_ROLE]->(t:Token) RETURN e.id, t.role, t.lemma` → `matrix.fill(rows)`; `matrix.causal_chain(root_id)->List[EventFrame]` zwraca zdarzenia powiązane `[:CAUSES*1..5]` z korzeniem — pełny kontekst przyczynowy; `matrix.coverage_score()->float` = `filled_cells / total_cells` — miara kompletności dokumentacji zdarzeń; `matrix.gap_cells()->List[Tuple[str,str]]` = `(frame_id, dimension)` gdzie `None` → `Violation('ROLE-05', severity='LOW', dimension=dim)` dla opcjonalnych wymiarów; `AuditReportGenerator.generate_dimension_matrix()` wypisuje jako Markdown tabelę `| EventFrame | AGENT | ACTION | TIME | LOCATION |...`?
- Jak wdrożyć automatyczną kompresję wiedzy QARC jako krok potoku — `QARCRunner` jako standardowy krok `(4)` w `AuditPipeline.run()`: `(1) parse → (2) extract → (3) flush(MERGE) → (4) QARCRunner.run() → (5) LinterRuleEngine → (6) report`; krok (4) eliminuje krawędzie zduplikowane mimo MERGE przez race condition w bulk import; `QARCConfig(edge_types:List[str], threshold:int=0, dry_run:bool=False)` z `qarc_config.yml`; `dry_run=True` w CI — loguje `duplicates_count` bez DELETE, blokuje pipeline gdy `duplicates > threshold`; `QARCRunner.run()->QARCReport(edges_removed, time_ms, graph_density_before, graph_density_after)` — `density=edges/(nodes*(nodes-1))`; `QARCRunner.validate_post()`: `MATCH (e:EventFrame) WHERE NOT (e)-[:HAS_ROLE {role:'AGENT'}]->() RETURN count(e) AS n` — baseline test spójności grafu po deduplikacji; metryka sukcesu: `density_after <= density_before` bez naruszenia `ROLE-01/02/03` reguł?
- Zaprojektuj zapytania Cypher 25 do audytu wielowymiarowych zdarzeń — zestaw 4 zapytań `EventAuditQuerySet`: (1) **brakujące TIME**: `MATCH (e:EventFrame) WHERE NOT (e)-[:HAS_ROLE {role:'TIME'}]->() AND e.domain='CONTRACT' RETURN e.id, 'MISSING_TIME' AS gap`; (2) **QPP multi-role**: `MATCH ((e:EventFrame)-[r:HAS_ROLE WHERE r.role IN ['AGENT','ACTION']]->{2,2}(t:Token WHERE t.lemma IS NOT NULL)) RETURN e.id, collect(t.lemma) AS roles` — filtr wewnątrz QPP; (3) **QPP causal-domain**: `MATCH ((src:EventFrame)-[r:CAUSES WHERE r.inferred=False]->{1,3}(dst:EventFrame WHERE dst.domain=src.domain)) RETURN src.id, count(*) AS chain_depth ORDER BY chain_depth DESC`; (4) **gap aggregate**: `MATCH (e:EventFrame) OPTIONAL MATCH (e)-[:HAS_ROLE]->(t) WITH e, collect(t.role) AS roles RETURN e.id, [dim IN ['AGENT','ACTION','TIME'] WHERE NOT dim IN roles] AS missing_dims`; `EventAuditQuerySet(session).run_all()->EventDimensionMatrix` mapuje wyniki na macierz?
- Jakie są różnice między Cypher 5 a Cypher 25 w kontekście grafu wiedzy — kluczowe różnice dla systemu NLP: (1) **QPP** tylko C25: `((a)-[r]->{1,5}(b))` + `WHERE` per węzeł wewnątrz `()` — C5 używa `[:TYPE*1..5]` bez wewnętrznych filtrów; (2) **inline WHERE**: `(n:Label WHERE n.prop=val)` w C25 — C5 wymaga zewnętrznego WHERE klauzuli; (3) **COLLECT subquery**: `COLLECT { MATCH (e)-[:HAS_ROLE]->(t) RETURN t.lemma }` C25 — C5 potrzebuje WITH + collect() lub list comprehension; (4) **IN TRANSACTIONS**: `CALL { UNWIND $batch AS row CREATE (:EventFrame) } IN TRANSACTIONS OF 500 ROWS` C25 — efektywny bulk import; (5) **CYPHER 25 prefix**: `CYPHER 25 MATCH ((a)->{1,5}(b))` wymusza parser C25 w Neo4j 5.9+ — bez prefiksu w Neo4j 5.8 QPP syntax error; migracja: `CypherVersionChecker.check(cypher:str)->CypherVersion`: `'>{' in cypher → C25`, else `C5`; `Neo4jAdapter.__init__`: `session.run('CALL dbms.components()')['versions'][0]` → `assert version>='5.9'` dla QPP features?

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
- Kolejne przykłady błędów `CypherSyntaxError` i ich naprawa — (1) brakujące `WITH` przed `WHERE` po `UNWIND`: `UNWIND $list AS item RETURN item WHERE item.active=True` → `SyntaxError: unexpected WHERE after RETURN`; naprawa: `UNWIND $list AS item WITH item WHERE item.active=True RETURN item`; (2) duplikat aliasu w `RETURN`: `RETURN e.id AS id, count(e) AS id` → `SyntaxError: duplicate column name 'id'`; (3) `WHERE` przed pierwszym `MATCH`: `WHERE e.domain='API' MATCH (e:EventFrame) RETURN e` → `SyntaxError: WHERE unexpected`; `GraphQueryAdapter.validate_query()` z `EXPLAIN` wykrywa wszystkie 3 przypadki przed `session.run()` — zero kosztów runtime?
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
- **Pułapka 10 (błędy logiki w relacjach CAUSE):** Trzy błędy wnioskowania w sieci kauzalnej: (1) **cykl przyczynowy** — `A-[:CAUSED_BY]->B-[:CAUSED_BY]->A`; wykrycie: `MATCH p=(e)-[:CAUSED_BY*2..]->(e) RETURN e.id` → wynik niepusty = cykl; naprawa: `CAUSED_BY` musi być DAG — `CycleDetector.check_dag()` wywoływany przed każdym `MERGE (e1)-[:CAUSED_BY]->(e2)`; (2) **odwrócona kierunkowość** — `CAUSE` vs `CAUSED_BY` użyte zamiennie: `(A)-[:CAUSES]->(B)` i `(B)-[:CAUSED_BY]->(A)` to ten sam fakt, duplikat zwiększa gęstość grafu 2× i zaburza `depth` w kaskadzie; zasada: tylko `[:CAUSES]` kierunek w całym schemacie; (3) **brakujący AGENT na ogniwie** — `EventFrame` w środku łańcucha bez `HAS_ROLE {role:'AGENT'}` → kaskada nie ma podmiotu odpowiedzialności; `CrossReferenceEngine` zgłasza `Violation('CAUSAL-01', node_id, reason='MISSING_AGENT_IN_CHAIN', severity='HIGH')`?

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
