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

### 2. Kontrakty danych
- Jak zapisać węzeł pojęcia w formacie JSON dla grafu?
- Jak zapisać model danych grafu dla zdania o Janie w JSON?
- Pokaż schemat fizycznej bazy danych dla relacji semantycznych..
- Jak załadować takie pliki JSON bezpośrednio do bazy Neo4j?
- Jak zintegrować bibliotekę jsonschema z bazą grafową Neo4j?
- Pokaż jak zintegrować format TEI P5 z bazą Neo4j..
- Jak APOC przyspiesza import JSON do bazy Neo4j?

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
- Pokaż implementację wyszukiwania w Neo4j dla pytań o lokalizację..
- Jak zaimplementować wyszukiwanie wzorca z pytajnikiem w Neo4j?
- Pokaż implementację wyszukiwarki Cypher dla intencji QUESTION..

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

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Co się dzieje gdy baza grafowa jest niedostępna podczas zapisu EventFrame — czy dane są tracone czy buforowane?
- Jak uniknąć duplikatów węzłów gdy ten sam podmiot (np. Wykonawca ABC sp. z o.o.) pojawia się w wielu dokumentach?
- Jakie jest ryzyko nieaktywnych relacji (dangling edges) po usunięciu węzła bez kaskadowego usunięcia krawędzi?
- Czy Cypher MERGE gwarantuje atomowość przy równoległych zapisach z wielu instancji serwisu?
- Jak obsłużyć migrację schematu grafu gdy nowy EventFrame dodaje właściwość wymaganą dla istniejących węzłów?
- Jaka jest konsekwencja wyboru ArangoDB zamiast Neo4j dla schematu i zapytań zdefiniowanych w Cypher?
- Jak zapobiec nieograniczonemu wzrostowi grafu przy przetwarzaniu tysięcy dokumentów bez archiwizacji starych węzłów?

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

### 3. Implementacja

- Jak zaimplementować `generate_cypher(event_role_dict) -> List[str]`?
- Jak zaimplementować `MERGE` dla węzłów konceptów, żeby unikać duplikatów na synset_id?
- Jak zaimplementować `build_document(sentences)` — pętlę budującą pełny graf dokumentu?
- Jak użyć APOC (`apoc.import.json`) do szybkiego importu wielu węzłów naraz?
- Jak zoptymalizować import miliona relacji hiperonimii ze Słowosieci do Neo4j?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `Neo4jAdapter.save_event()` bez real Neo4j (mock/stub)?
- Jak testować `generate_cypher()` — sprawdzić, czy wygenerowany Cypher jest poprawny składniowo?
- Jak napisać test integracyjny dla scalania węzłów (`MERGE`) na embedded Neo4j?
- Jak testować `build_document()` dla zdania "Wykonawca dostarczył dokumentację techniczną z opóźnieniem" — sprawdzić węzły i krawędzie?
- Jak testować wykrywanie sprzecznych relacji w modelu zdarzenia?
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
- Jak rollbackować częściowy import gdy część węzłów się zapisała a reszta nie?
- Jak logować błędy imporcie (które zdania zakończono, które nie)?
- Co robi system gdy Neo4j jest w trybie read-only (np. po awarii, przed recovery)?
- Jak obsługiwać race condition: ten sam węzeł MERGE-owany równolegle przez dwa procesy?

### 6. Integracja z innymi warstwami

- Jak W4 dostaje `EventRoleDict` z W2 — bezpośrednio czy przez kolejkę?
- Jak W5 (InferenceEngine) wykonuje zapytania Cypher do W4 — przez ten sam adapter?
- Jak W6 (koreferencja) dostarcza zmergowane węzły do W4 — przed czy po `generate_cypher()`?
- Jak W8 (AuditEngine) pobiera dane z W4 do generowania raportów luk?

### 7. Pułapki i ryzyka

- **Pułapka 1:** MERGE w Neo4j bez indeksu na `synset_id` jest O(n) — baza nie skaluje się przy >100k węzłów. Indeksy muszą być założone PRZED importem.
- **Pułapka 2:** ArangoDB ma inny model zapytań niż Cypher — migracja między nimi wymaga przepisania wszystkich zapytań W5. Decyzja wyboru DB musi być ostateczna.
- **Pułapka 3:** Brak transakcji ACID przy batch imporcie = niespójny stan grafu po przerwaniu. Zawsze używać `BEGIN TRANSACTION` lub APOC periodic commit.
- **Pułapka 4:** MERGE w Neo4j bez unikalnego indeksu tworzy duplikaty węzłów — `MERGE (n:Concept {id: x})` bez `CREATE INDEX` jest O(n) i duplikuje dane.
- **Pułapka 5:** Neo4j Community Edition nie ma replikacji — awaria węzła podczas zapisu to utrata danych; wymagana edycja Enterprise dla projektu produkcyjnego.
- **Pułapka 6:** Zapytania Cypher bez `LIMIT` na grafach >1M węzłów — `MATCH (n)-[:IS_A*]->(m)` bez limitu głębokości to pełny obchód grafu.

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
