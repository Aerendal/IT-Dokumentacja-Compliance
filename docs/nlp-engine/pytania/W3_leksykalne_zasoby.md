---
layer: W3
title: "Warstwa 3 — Leksykalne Zasoby (Słowosieć, Walenty, WSD)"
phase: 3
status: planned
docs_version: 1.0.0
tags: [slowosiec, walenty, WSD, synset, polisemia, idiomy, PhraseologyDetector, kolokacje, MWE]
---

# Warstwa 3 — Leksykalne Zasoby (Słowosieć, Walenty, WSD)

## Przegląd

Warstwa 3 integruje polskie zasoby leksykalne:
- **Słowosieć** — polska sieć semantyczna (synsety, relacje hiperonimii, synonimii, derywacji)
- **Walenty** — słownik walencyjny polskich czasowników (ramy subkategoryzacyjne)
- **WSD** — Word Sense Disambiguation (ujednoznacznianie sensów)
- **PhraseologyDetector** — detekcja idiomów i jednostek wielowyrazowych (MWE)

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W3 istnieje bo W2 przypisuje role bez wiedzy o znaczeniu słów — mapuje strukturę na role, ale nie wie że "nóż" jest narzędziem niebezpiecznym, albo że "wróbel" to ptak, albo że "zwinąć" w kontekście kradzieży znaczy "ukraść" a nie "zwinąć rulon". Słowosieć dostarcza hiperonimię (`nóż IS_A narzędzie_ostre IS_A narzędzie`), Walenty dostarcza ramy walencyjne (które argumenty są obowiązkowe dla danego czasownika), WSD rozstrzyga polisemię. Bez W3 reguły W5 muszą wymieniać każde słowo z osobna zamiast operować na klasach semantycznych.

**Co się sypie bez tej warstwy:**
- W5 ma reguły "IF instrument == 'nóż' OR instrument == 'pistolet' OR instrument == 'miecz' ..." — lista musi być ręcznie utrzymywana; neologizmy nigdy nie są wykrywane
- WSD nie działa: "zamek" może być LOCATION (budowla) lub INSTRUMENT (mechanizm zamykający) — bez synsetu W2 przypisuje losowo
- Idiomy: "wziąć nogi za pas" → W2 widzi INSTRUMENT(pas) i LOCATION(nogi) zamiast całości = "uciec"

**Zależności:**
- Wchodzi z W1: `lemma` każdego tokenu
- Dostęp do: Słowosieć API, Walenty DB, WSD model
- Wychodzi do W2 (lub równolegle): `EnrichedToken[synsets, hypernyms, valency_frame, is_mwe]`
- Wychodzi do W4: krawędzie `IS_A`, `HAS_SYNSET`, `HAS_HYPONYM` w grafie ontologicznym
- Wychodzi do W5: klasy semantyczne jako warunki reguł DRL

## Diagram przepływu danych

```
Token (z W1) + DependencyTree
       │
  ┌────┴────────────────────────┐
  ▼                             ▼
SlowosiecAdapter           WalentyAdapter
(synsety, hiperonimy)      (ramy walencyjne)
  │                             │
  └────────┬────────────────────┘
           ▼
      WSD Engine
   (wybór właściwego sensu)
           │
           ▼
    PhraseologyDetector
    (idiomy, kolokacje, MWE)
           │
           ▼
  EnrichedToken {synset_id, sense, lemma, mwe_flag}
           │
           ▼
     W2 (role semantyczne)
     W4 (Neo4j — hiperonimia)
     W5 (InferenceEngine — ontologia)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Pokaż jak zaprojektować model danych grafu dla wieloznaczności..
- Pokaż strukturę węzła Concept uwzględniającą synset_id i rolę.
- Jaki wzorzec projektowy stosuje W3 dla dostępu do zasobów zewnętrznych — Adapter, Proxy, czy Repository?
- Jak wyglądają granice W3 — co dostarcza W2 (role semantyczne) a co W3 dodaje przed przekazaniem do W4?
- Jak W3 obsługuje wiele zasobów leksykalnych jednocześnie (Słowosieć + Walenty) — czy są priorytetyzowane?
- Jakie wzorce cache stosuje W3 dla wyników Słowosieci — LRU, TTL, czy trwały cache na dysku?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest format odpowiedzi Słowosieci API — obiekt JSON z listą synonimów, hiperonimów i hiponimów?
- Jak zdefiniować kontrakt dla brakującego wpisu leksykalnego — null, pusta lista, czy wyjątek NotFound?
- Jakie pola zwraca PhraseologyDetector dla wykrytej frazy idiomatycznej — id, canonical_form, confidence?
- Jak zdefiniować format przekazywania informacji leksykalnych z W3 do W2 (SemanticMapper)?
- Jak wygląda schemat JSON dla wzbogaconego tokena po przejściu przez W3 — pokaż przykładowy obiekt?
- Pokaż model danych dla relacji bazujących na synsetach — Synset(id, name, pos, lemmas) i SynsetRelation(source_id, type, target_id)?
- Jak zdefiniować kontrakt dla relacji IS_A, HAS_SYNSET, SIMILAR_TO w formacie JSON — pokaż przykładowy obiekt?
- Jak EnrichedToken z W3 reprezentuje listę synsetów — pole synsets: List[SynsetRef] z id, confidence, pos?
- Jaki jest format plWordNet (LMF XML) — struktura pliku, elementy LexicalEntry, Sense, Synset, SynsetRelation?
- Jak odróżnić plWordNet (format LMF XML) od API Słowosieci (REST/SOAP) — kiedy używać którego źródła?
- Jak parsować plik plWordNet LMF XML w Pythonie — lxml, iterparse dla pliku 500 MB bez ładowania do RAM?
- Jak mapować elementy plWordNet LMF (LexicalEntry→:Token, Synset→:Synset, SynsetRelation→:IS_A) w Neo4j?
- Jak synchronizować wersję plWordNet (4.2→5.0) z grafem Neo4j — delta import i usuwanie przestarzałych węzłów?
- Jak obsłużyć synsety plWordNet bez odpowiednika w angielskim WordNet — węzeł :Synset z flagą pl_only=true?

### 3. Implementacja
- Jakie reguły ujednoznaczniania dodać do silnika disambiguation?
- Pokaż słownik kolokacji ułatwiający ujednoznacznianie..
- Jak wdrożyć silnik ujednoznaczniający dla polisemicznych pojęć?
- Jak uniknąć problemu eksplozji ontologii w takim systemie?
- Zbudujmy słownik kolokacji ułatwiający ujednoznacznianie..
- Jak wdrożyć disambiguation engine dla synkretyzmu i wieloznaczności?
- Pokaż jak zbudować słownik kolokacji wspierający ujednoznacznianie..
- Jak stworzyć słownik kolokacji wspierający ujednoznacznianie wieloznaczności?
- Zbudujmy słownik kolokacji ułatwiający ujednoznacznianie semantyczne..
- Chcę zobaczyć, jak zaimplementować ten mechanizm ujednoznaczniania..
- Jak algorytmicznie wybierać właściwe znaczenie wieloznacznych słów?
- Pokaż przykład kodu integrującego Słowosieć do wyboru znaczenia słowa..
- W jaki sposób optymalnie ograniczyć zakres mojego systemu?
- Jak algorytmicznie wybrać właściwy synset przy wieloznaczności słowa?
- Omów 3 bariery: eksplozję reguł, ontologii i brak kontekstu..
- Jakie są ryzyka związane z eksplozją ontologii w grafie?
- Jakie są największe trudności przy tworzeniu grafowej ontologii polszczyzny?
- Pokaż jak Słowosieć pomaga w mapowaniu drzew pojęć..
- Pokaż jak algorytmicznie wybierać właściwy synset przy wieloznaczności..
- Jakie są najczęstsze błędy przy budowaniu reguł ujednoznaczniających?
- Jak uodpornić system na synkretyzm przy użyciu Morfeusza?
- Jakie są największe wyzwania przy tworzeniu reguł eliminacji polisemii?
- W jaki sposób silnik ujednoznaczniający zarządza subgrafami wariantowymi?
- Pokaż jak Słowosieć definiuje relacje derywacyjne dla grafu..
- Jak zaimplementować ujednoznacznianie pojęć dla słowa zamek?
- Jak wdrożyć prostą heurystykę szukającą przecięć kontekstu z hiperonimami?
- Zastosujmy Baseline: Najczęstszy sens (MFS) ze Słowosieci dla zamka..
- Jak uniknąć eksplozji ontologii przy tysiącach reguł?
- Jak powiązać węzły :Concept z konkretnymi synsetami Słowosieci?
- Pokaż regułę dla Słowosieci obsługującą synonimy 'dać'..
- Jak rozszerzyć wyszukiwanie o synonimy ze Słowosieci?
- Stwórzmy detektor dla idiomów i jednostek wielowyrazowych..
- Jak zaimplementować detekcję idiomów takich jak 'rzucić okiem'?
- Pokaż implementację detektora idiomów i jednostek wielowyrazowych..
- Jak zaimplementować detektor idiomów jako jednostek wielowyrazowych?
- Jak rozbudować mwe_dict o idiomy?
- Czy detektor idiomów powinien działać przed lematyzacją?
- Pokaż jak dodać detektor jednostek wielowyrazowych i idiomów.
- Napiszmy SlowosiecAdapter dla synonimów i hiperonimów — pokaż kod klasy z get_synonyms(lemma) i get_hypernyms(lemma)?
- Jak SlowosiecAdapter obsługuje polisemię — zwraca wszystkie synsety dla lematu czy tylko najbardziej prawdopodobny?
- Jak zaimplementować lazy loading w SlowosiecAdapter aby uniknąć ładowania 2 GB Słowosieci przy starcie serwisu?
- Jak testować SlowosiecAdapter — test używa prawdziwej Słowosieci czy mocka z kilkoma synsetami testowymi?
- Jak SlowosiecAdapter cachuje wyniki zapytań — LRU cache per sesja czy trwały cache na dysku?
- Jak stworzyć SlowosiecAdapter do wczytywania pliku `jednostki.txt` — jaki jest format linii (id TAB lemma TAB pos)?
- Jak parsować plik `synsety.txt` Słowosieci — jaki jest format rekordu synsetu (synset_id TAB lista lematów oddzielona przecinkami)?
- Jak zaimplementować `SlowosiecAdapter._load_from_files(units_path, synsets_path)` — inicjalizacja słownika lematów i synsetów?
- Jak walidować integralność pliku `jednostki.txt` — czy każde id jednostki z `synsety.txt` ma odpowiadający wpis w `jednostki.txt`?
- Napiszmy SlowosiecAdapter do obsługi synonimów w grafie Neo4j — jak adapter zapisuje wyniki get_synonyms() jako węzły :Synset z krawędziami :SYNONYM?
- Jak SlowosiecAdapter.enrich_graph(lemma, neo4j_session) dodaje węzeł :Synset i krawędzie :IS_SYNONYM do istniejącego :EventFrame?
- Jak uniknąć duplikatów węzłów :Synset w grafie gdy wielu AGENT używa tego samego synonimów — MERGE zamiast CREATE?
- Napiszmy kod SlowosiecAdapter do obsługi synonimów — metoda get_synonyms(lemma) → List[str] przeszukuje słownik synsetów i zwraca wszystkie lematy ze wspólnego synsetu?
- Jak SlowosiecAdapter obsługuje relacje pojęć — metody get_hypernyms(lemma) i get_hyponyms(lemma) traversując graf IS_A w Słowosieci?
- Jak SlowosiecAdapter.get_related_concepts(lemma, relation_type) zwraca powiązane pojęcia — parametr relation_type: Literal['synonym', 'hypernym', 'hyponym', 'meronym']?
- Stwórzmy skrypt kompilujący plWordNet do zoptymalizowanej bazy SQLite — skrypt parsuje plik LMF XML i wstawia synsets, lemmas i relations do plwordnet.db przez iterparse + batch INSERT?
- Jak zaindeksować bazę SQLite plWordNet dla wydajności — indeks na kolumnach `lemma` i `synset_id` dla szybkich zapytań get_synonyms(lemma)?
- Jakie złożone indeksy SQLite przyspieszą zapytania relacji semantycznych — `CREATE INDEX idx_rel_compound ON relation(synset_id, relation_type, target_id)` dla get_hyponyms()?
- Jak użyć COVERING INDEX w SQLite dla get_synonyms(lemma) — indeks na `(lemma, synset_id)` pokrywa zapytanie SELECT bez odczytu tabeli głównej?
- Jak sprawdzić plan zapytania w SQLite — `EXPLAIN QUERY PLAN SELECT ... FROM relation WHERE synset_id=?` aby zweryfikować czy indeks jest używany?
- Jak SlowosiecAdapter korzysta ze skompilowanej bazy SQLite zamiast pliku tekstowego — connection pool, parametryczne zapytania SELECT, LRU cache wyników?
- Jak weryfikować kompletność skompilowanej bazy SQLite — SELECT COUNT(*) z każdej tabeli i porównanie z liczbą `<Synset>` w źródłowym LMF XML?
- Jak wygląda główna funkcja compile_plwordnet.py — `if __name__ == '__main__': compile(src_xml, dest_db, batch_size=1000)` z argparse dla --src i --dest?
- Jak obsłużyć błąd parsowania LMF XML podczas kompilacji — try/except na iterparse, logowanie elementu, rollback transakcji przez `conn.rollback()`?
- Jak zdefiniować granice transakcji w compile_plwordnet.py — commit co batch_size wierszy, BEGIN TRANSACTION i COMMIT zawijają każdy blok batch INSERT?
- Jak zaprojektować strukturę tagów dla branżowych słowników terminologicznych — dodatkowe pole `domain` w tabeli SQLite: LEGAL, CONSTRUCTION, IT, FINANCE mapowane na branżowy synset?
- Jak tagi branżowe integrują się z SlowosiecAdapter — `get_synonyms(lemma, domain='LEGAL')` filtruje synonimy tylko z terminologii prawniczej danej branży?
- Jak wersjonować branżowe słowniki terminologiczne — osobna tabela `domain_overrides` w plwordnet.db nadpisująca relacje dla konkretnej domeny?
- Jak stworzyć słownik terminologiczny dla branży CONSTRUCTION — tabele: `domain_lemma(lemma, domain, synset_id)` + `domain_relation(synset_id, relation_type, target_synset_id, domain)`?
- Jak zasilić `domain_overrides` terminami z zewnętrznego glosariusza branżowego — import CSV: `parse(glossary.csv)` → `INSERT INTO domain_overrides(lemma, synset_id, domain)` z rollbackiem przy konflikcie?
- Jak przetestować kompletność słownika terminologicznego dla branży LEGAL — `SELECT COUNT(*) FROM domain_lemma WHERE domain='LEGAL'` vs liczba terminów w glosariuszu źródłowym?
- Jak uruchomić ETL dla Słowosieci jako pipeline trzech kroków — extract (parsuj LMF XML przez iterparse), transform (mapuj LexicalEntry→lemma, Synset→synset_id), load (batch INSERT z transakcjami)?
- Jak zmierzyć wydajność wyszukiwania synsetów po ETL — `timeit get_synonyms('dostarczyć')` < 10 ms przy włączonym COVERING INDEX na `(lemma, synset_id)` jako kryterium akceptacji?
- Jak zapewnić idempotentność skryptu compile_wordnet.py — `CREATE TABLE IF NOT EXISTS` i `INSERT OR REPLACE` aby wielokrotne uruchomienie nie duplikowało danych?
- Jak logować postęp kompilacji plWordNet w compile_wordnet.py — `tqdm` progress bar wypisujący liczbę wstawionych synsetów co 1000 wierszy batch?
- Jak stworzyć automatyczny ekstraktor terminologii branżowej — skrypt TF-IDF na korpusie prawnym: termin = leksem o TF-IDF > threshold, IDF z korpusu NKJP jako baseline?
- Jak ekstraktor filtruje fałszywe pozytywy — lista wykluczeń POS: pomijaj VERB bez branżowego frame walencyjnego i PRON; zachowaj NOUN i ADJ z wysokim TF-IDF?
- Jak zintegrować ekstraktor z `domain_overrides` — wyniki ekstraktora → CSV → `INSERT INTO domain_lemma(lemma, domain, synset_id)` w plwordnet.db jako wejście dla `SlowosiecAdapter(domain='LEGAL')`?

### 4. Testowanie
- Zdefiniujmy testy dla synkretyzmu form takich jak słowo zamek..
- Pokaż jak rozbudować testy o przypadki synkretyzmu i wieloznaczności..
- Dopiszmy test synkretyzmu gramatycznego dla słowa „dam”..
- Zdefiniujmy testy dla synkretyzmu gramatycznego słowa dam..
- Jak wdrożyć parser zależności UDPipe do testowania synkretyzmu?
- Jakie są różnice między homonimią a polisemią w testach?
- Jak zaimplementować mechanizm WSD dla słowa „testy jednostkowe” w grafie?
- Napiszmy czerwony test dla synsetu słowa zamek.
- Stwórzmy czerwony test dla detektora idiomów w Fazie 3..
- Stwórzmy test jednostkowy dla PhraseologyDetector w Fazie 3..
- Pokaż logikę detekcji idiomów zapalającą test na zielono..
- Pokaż test dla idiomu 'odnieść sukces' w zdaniu..
- Zaimplementujmy logikę ujednoznaczniania w Fazie GREEN przy użyciu UDPipe..

### 5. Obsługa błędów
- Jak obsłużyć wieloznaczność słowa klucz w grafie?
- Jak obsłużyć niedostępność Słowosieci API — fallback do lokalnego cache czy zwrócenie pustej listy synonimów?
- Co się dzieje gdy Walenty nie zawiera wpisu dla danego lematu — wyjątek, null, czy domyślna struktura?
- Jak logować brakujące wpisy leksykalne do późniejszego uzupełnienia zasobów?
- Jak obsłużyć timeout przy odpytywaniu zewnętrznego zasobu leksykalnego?

### 6. Integracja z innymi warstwami
- Jak zintegrować Słowosieć z grafem wiedzy w Fazie 2?
- Pokaż jak zintegrować Słowosieć z ontologią grafu..
- Czy możemy dodać warstwę ujednoznaczniania sensów (WSD) do modułu?
- Pokaż jak zintegrować Słowosieć z grafem w Pythonie..
- Jak zintegrować Słowosieć z grafem w Pythonie?
- Jak zintegrować Słowosieć z tym potokiem w Fazie 2?
- Pokaż jak zintegrować Słowosieć w celu ujednoznaczniania pojęć..
- Jak zintegrować Słowosieć do ujednoznaczniania pojęć w grafie?
- Jak zintegrować Słowosieć z naszym modelem ontologii?
- Które polskie słowniki najlepiej zintegrować z ontologią?
- Jak zintegrować Słowosieć z ontologią, by system rozumiał hiperonimy?
- Jak zintegrować Słowosieć, by reguła obsługiwała synonim wręczyć?
- Jak zintegrować Słowosieć do obsługi synonimów w regułach?
- Jak zintegrować Słowosieć, aby obsłużyć synonimy czasownika 'dać'?
- Pokaż jak zintegrować Słowosieć do obsługi synonimów.
- Jak W3 obsługuje żądania z W0 (Linter) o synonimy terminu — synchroniczne wywołanie czy pre-loaded cache?
- Jak W3 informuje W0 gdy wykryty "synonim" jest faktycznie hiperonimem — relacja generalizacji, nie równoznaczność?
- Jak W3 eksponuje API dla W0 do sprawdzenia czy dwa terminy należą do tego samego synsetu?
- Wariant A — pełny import synsetów Słowosieci do Neo4j jako :Synset węzły: jak przeprowadzić import offline i jak często odświeżać?
- Wariant B — odpytywanie SlowosiecAdapter on-demand dla każdego tokena: jakie są trade-offy latency vs. aktualność danych?
- Wariant C — pre-built subgraf synsetów dla domeny prawnej (filtr: lematy z NKJP-Legal): jak budować i weryfikować pokrycie?
- Kiedy wybrać Wariant A vs. B vs. C — kryteria: rozmiar korpusu, latency SLA, częstotliwość aktualizacji Słowosieci?
- Jak migrować z Wariantu B (on-demand) do Wariantu A (import) bez przerwy w działaniu serwisu?
- Jak zintegrować plWordNet z grafem przyczynowym — synsety z plWordNet stają się węzłami :Synset w Neo4j?
- Jak plWordNet definiuje relacje hiperonimii (hyperonymy) i jak mapują się na krawędź :IS_A w grafie?
- Jak połączyć węzły :EventFrame z :Synset z plWordNet — zapytanie Cypher MATCH i MERGE relacji HAS_SYNSET?
- Jak testować poprawność importu Słowosieci — asercja że węzeł :Synset('nóż') ma krawędź :IS_A do :Synset('narzędzie')?
- Jak obsłużyć rozejście między relacjami Słowosieci (hiperonimia, meronimia) a krawędziami grafu (:IS_A, :PART_OF)?
- Jak mierzyć pokrycie Wariantu C (subgraf prawny) — % lematów z NKJP-Legal z co najmniej jednym węzłem :Synset?
- Jak zintegrować Słowosieć z istniejącym grafem przyczynowo-skutkowym — węzły :Synset wzbogacają :EventFrame o semantykę predykatu?
- Jak zapytanie Cypher łączy :EventFrame z :Synset Słowosieci — MATCH (e:EventFrame)-[:HAS_SYNSET]->(s:Synset) WHERE s.hypernym = 'działanie'?
- Jak Słowosieć rozszerza reguły inferencyjne — synonim 'wręczyć' do 'dostarczyć' aktywuje tę samą regułę CONS-02 w DRL?
- Jak hiperonimia Słowosieci wspiera Soft Matching w CausalChainBuilder — predykat 'przekazać' dopasowuje regułę dla 'dostarczyć' przez wspólny hiperonim 'działanie'?
- Jak SlowosiecAdapter.get_hypernym_path(lemma) zwraca ścieżkę do korzenia ontologii — używana przez Soft Matching do ustalenia semantycznej odległości?
- Zintegrujmy Słowosieć z grafem, aby lepiej rozumieć synonimy — jak węzły :Synset w Neo4j rozszerzają dopasowanie predykatów w regułach DRL?
- Zintegrujmy SlowosiecAdapter z CausalChainBuilder do łączenia zdarzeń — wywołanie `get_synonyms(predicate)` w logice `link_events()` CausalChainBuilder decyduje o emisji krawędzi :CAUSES?
- Jak SlowosiecAdapter.get_synonym_set(lemma) zasila mapowanie predykatów w CausalChainBuilder.link_events() — sprawdzenie czy predykat zdarzenia należy do synsetu wzorca reguły?
- Jak skonfigurować semantyczny soft matching w CausalChainBuilder od strony W3 — adapter zwraca `Set[str]` synonimów; builder porównuje ze zbiorem wzorców reguły przez `intersection / union ≥ threshold`?
- Jak testować integrację SlowosiecAdapter+CausalChainBuilder od strony W3 — fixture z mock SQLite wypełnionym synsetnymi parami dla 'dostarczyć'↔'przekazać'?
- Jak połączyć Słowosieć z grafem przyczynowym w Neo4j — po `SlowosiecAdapter.enrich_graph(lemma, session)` wywołaj MERGE (e:EventFrame)-[:HAS_SYNSET]->(s:Synset {synset_id: $id}) dla każdego dopasowanego synsetu?
- Jak zoptymalizować łączenie Słowosieci z grafem przyczynowym — batch UNWIND zamiast pojedynczych MERGE: `UNWIND $synsets AS s MERGE (:Synset {id: s.id})` przy imporcie?
- Jak graf synsetów Słowosieci pozwala regule dopasować "wręczyć" gdy oczekuje "dostarczyć" — ścieżka przez wspólny hiperonim 'działanie transferu'?
- Jak testować integrację Słowosieci z grafem dla synonimów — asercja MATCH(:Synset)-[:IS_SYNONYM]->(:Synset) dla pary 'dostarczyć'/'przekazać'?
- Jak zintegrować DeepER NER z lokalną bazą Słowosieci (SQLite wordnet.db) — dla każdej encji rozpoznanej przez NERAdapter: `SlowosiecAdapter.get_synsets(entity.lemma, pos='n')`, jeśli pusta lista → `KGT.capture_ign(entity.form)`, jeśli ≥1 → `entity.synset_id = synsets[0].id` i wzbogać EventFrame.PATIENT o synset?
- Jak DeepER wykorzystuje Słowosieć do kategoryzacji bytów — etykieta NER (ORGANIZACJA) jest punktem wejścia do `SlowosiecAdapter.get_synsets(lemma, pos='n')`; synset zwęża semantyczną klasę encji (np. ORGANIZACJA + synset 'instytucja_finansowa' → kontekst audytu vs synset 'wykonawca_budowlany' → kontekst umowy budowlanej)?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jaka jest konsekwencja gdy słowo nie istnieje w Słowosieci i brak jest fallbacku — czy pipeline zatrzymuje się?
- Jak uniknąć eksplozji kombinatorycznej przy wyszukiwaniu synonimów w zdaniach wieloklausulowych?
- Co się dzieje gdy Walenty i Słowosieć dają sprzeczne informacje o selekcji dla tego samego leksemu?
- Jak obsłużyć neologizmy prawne (nowe pojęcia z ustaw) których brak w istniejących zasobach leksykalnych?
- Jakie jest ryzyko błędnego WSD dla terminów wieloznacznych w prawie (np. "strona" = strona umowy vs. strona dokumentu)?
- Czy Walenty zawiera pełne pokrycie dla czasowników prawnych: odstąpić, zobowiązać, naruszać, dostarczyć, odebrać?
- Jak zidentyfikować czy fraza idiomatyczna pokrywa się z użyciem literalnym tego samego słowa w tej samej sekcji?

## Pytania uzupełniające
- **Pułapka 3:** Słowosieć nie pokrywa neologizmów technicznych ("konteneryzacja", "mikroserwis") — `get_synsets("docker")` zwróci pusty wynik, a system milcząco pominie wzbogacenie semantyczne.
- **Pułapka 4:** Walenty ma luki dla czasowników niekonwencjonalnych i frazeologizmów — `get_valency_frame("kłaść do głowy")` zwróci `None`, co może wywołać `NullPointerException` w `SemanticMapper`.
- **Pułapka 5:** Pełne ładowanie Słowosieci do RAM zajmuje ~2 GB — w środowiskach z limitem 1 GB (containers, serverless) `SlowosiecAdapter` uruchomi się, ale spowolni do nieużywalności przez swapping.
- Jaki jest faktyczny rozmiar plwordnet.db — plik SQLite ~200 MB, z page cache OS ~500 MB; ładowanie do słownika Python to ~2 GB; na maszynach ≥4 GB RAM SQLite z lazy load wystarcza?
- Kiedy SQLite wystarczy zamiast Neo4j dla plWordNet — jeśli zapytania to tylko get_synonyms/get_hypernyms bez grafowych przeszukiwań transytywnych, SQLite jest szybszym i prostszym wyborem?
- Jak uruchomić SlowosiecAdapter w trybie lazy przez SQLite mmap — `PRAGMA mmap_size=536870912` zamiast pełnego ładowania do pamięci Python?
- **Pułapka 6:** Homografy ("zamek" = budowla / mechanizm) — `get_synsets("zamek")` zwróci oba synsets bez wskazania który; bez WSD (W3) downstream W2 dostanie losowy synset.

### 1. Architektura

- Jak podzielić `SlowosiecAdapter` od `WalentyAdapter` — osobne klasy czy jeden `LexicalResourceManager`?
- Jak załadować Słowosieć z pliku tekstowego do pamięci — słownik Python, SQLite, czy Neo4j?
- Jak podzielić odpowiedzialność WSD między W3 (wybór sensu) a W2 (kontekst roli)?
- Jaki algorytm WSD wybrać: MFS (Most Frequent Sense), Lesk, Simplified Lesk, kontekstowy?
- Jak `PhraseologyDetector` działa na tokenach z W1 — sekwencja sliding window czy drzewna?

### 2. Kontrakty danych

- Jaki jest schemat JSON dla `EnrichedToken` — które pola synset_id, sense, confidence są obowiązkowe?
- Jak Walenty przekazuje ramę walencyjną (listę ról z ograniczeniami selekcyjnymi) do W2?
- Jak kodować flagę `mwe_flag` dla jednostek wielowyrazowych ("rzucić okiem" → `mwe=idiom`)?
- Jaki jest format słownika kolokacji wejściowego dla `PhraseologyDetector`?
- Jak Słowosieć eksponuje relacje hiperonimii — jako lista ścieżek czy pełny DAG?

### 3. Implementacja

- Jak zaimplementować `SlowosiecAdapter.get_synsets(lemma, pos) -> List[Synset]`?
- Jak zaimplementować Simplified Lesk WSD: porównanie definicji synsetu z kontekstem zdania?
- Jak zaimplementować `PhraseologyDetector.detect_mwe(tokens) -> List[MWESpan]`?
- Jak załadować plik relacji Słowosieci (format TXT) do słownika Python z hiperonimią?
- Jak wdrożyć regułę "Najczęstszy Sens" (MFS) jako baseline WSD dla nieznanych kontekstów?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `SlowosiecAdapter` — `get_synsets("zamek")` zwraca ≥ 2 synsety?
- Jak testować WSD dla klasycznego przykładu "zamek" — kontekst "klucz" → "zamek do drzwi" vs "budowla"?
- Jak testować idiom "rzucić okiem" — `detect_mwe` musi zwrócić `MWESpan` zamiast 2 tokenów?
- Jak zbudować oracle dataset dla WSD polskiego (50 polisemicznych słów × 5 kontekstów)?
- Jak testować Walenty — czy "dostarczyć" ma ramę z AGENT:NP, PATIENT:NP i RECIPIENT:NP?
#### Kompletna hierarchia TDD
- Zaimplementuj Fazę GREEN dla `SlowosiecAdapter` — minimalna logika `get_synsets(lemma)` zwracająca [] dla nieznanych lematów zamiast rzucania wyjątku.
- Jak zrefaktoryzować `SlowosiecAdapter` po GREEN — dodać cache LRU żeby nie odpytywać API przy każdym wywołaniu?
- Zrefaktoryzuj `SlowosiecAdapter` — strategia fallback: Słowosieć → morfologiczny heurystyk → [] bez propagacji wyjątku do wyższych warstw.
- Jak napisać test jednostkowy dla `_resolve_polysemy()` — mock wywołania Słowosieci, testować tylko logikę WSD na fiksowanych danych?
- Jak napisać test integracyjny W3→W2: wzbogacony token z synsetem → sprawdź że `SemanticMapper` wybiera poprawną rolę dla polisemicznego słowa?
- Jak zmierzyć Mutation Score dla `WSDResolver` — które gałęzie decyzyjne są najtrudniejsze do mutacji?
- Jak napisać test własnościowy (Hypothesis) dla `SlowosiecAdapter` — dla każdego lematu z NKJP wynik powinien być listą lub pustą listą, nigdy None?
- Jak zapewnić że aktualizacja Słowosieci (nowa wersja) nie usuwa synsetów używanych przez reguły W5 — diff synsetów jako test regresyjny?
- Stwórz snapshot test: 20 kluczowych lematów (dostarczyć, odstąpić, odmówić...) + oczekiwane hypernimy — alarm gdy Słowosieć zwróci inne IS_A.
- Jak przetestować W1→W3→W5 end-to-end: zdanie z neologizmem → sprawdź że W5 loguje WARNING zamiast rzucać wyjątek?

### 5. Obsługa błędów

- Co zwraca `SlowosiecAdapter` dla słów spoza Słowosieci (neologizmy, nazwy własne)?
- Jak obsługiwać `get_synsets()` gdy Słowosieć nie jest załadowana (OOM, brak pliku)?
- Co robi `PhraseologyDetector` gdy idiom jest częściowo rozgromiony przez wstawienie słowa?
- Jak obsługiwać homonimię między kategorii (rzeczownik "zamek" vs przymiotnik "zamknięty")?
- Jakie jest zachowanie WSD przy zdaniach bez kontekstu (jedno słowo)?
- Co robi `SlowosiecAdapter` gdy plik Słowosieci jest w trakcie aktualizacji (partially written)?
- Jak obsługiwać `get_valency_frame()` gdy Walenty zwraca ramę z nieznanym typem roli (nowy standard po aktualizacji)?

### 6. Integracja z innymi warstwami

- Jak W3 przekazuje `EnrichedToken` do W2 — before or after SRL (co jest prerequisite)?
- Jak W4 (Neo4j) przechowuje hiperonimię ze Słowosieci — jako krawędzie `IS_A`?
- Jak W5 (InferenceEngine) używa Słowosieci do wnioskowania o gatunkach ("wróbel IS_A ptak")?
- Jak W3 integruje się z W6 (koreferencja) — czy WSD poprawia wykrywanie zaimków?
- Jak W3 informuje W2 gdy znaleziony synonim zmienia interpretację roli semantycznej predykatu?
- Jak weryfikować spójność między Słowosiecią a Walenty dla tego samego leksemu?
- Jak W3 obsługuje żądania z W5 (silnik wnioskowania) o synonimach terminów w regułach DRL?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Słowosieć 3.x ma nierówne pokrycie — czasowniki mają znacznie mniej synsetów niż rzeczowniki. Fallback MFS dla czasowników jest konieczny.
- **Pułapka 2:** Eksplozja ontologii przy ładowaniu pełnej hiperonimii Słowosieci do Neo4j (>500k relacji) — konieczne selektywne ładowanie per domena.
- **Pułapka 3:** Walenty nie pokrywa neologizmów ani anglicyzmów — brak ramy walencyjnej nie oznacza błędu, ale wymaga explicitnego fallbacku rule-based.
- **Pułapka 4:** Słowosieć nie pokrywa neologizmów technicznych ("konteneryzacja", "mikroserwis") — `get_synsets()` milcząco zwróci pusty wynik zamiast sygnalizować brak.
- **Pułapka 5:** Pełne ładowanie Słowosieci zajmuje ~2 GB RAM — w środowiskach z limitem 1 GB (containers) system uruchomi się ale spowolni przez swapping.
- **Pułapka 6:** Homografy ("zamek" = budowla/mechanizm) — bez WSD downstream W2 dostaje losowy synset zamiast właściwego.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| WSD Accuracy na oracle datasecie | ≥ 75% |
| MFS Baseline (górna granica prostego WSD) | ≥ 65% |
| MWE detection F1 dla idiomów | ≥ 80% |
| Czas ładowania Słowosieci do pamięci | < 10 s |
| Coverage Walenty dla 100 najczęstszych czasowników | ≥ 90% |

## Pytania o idempotentność i deterministyczność

- Czy `get_synsets("zamek", "n", context)` zawsze zwraca ten sam synset dla identycznego kontekstu?
- Czy załadowanie Słowosieci z pliku daje identyczny słownik niezależnie od systemu operacyjnego?
- Jak zapewnić stabliność WSD gdy Słowosieć jest aktualizowana do nowej wersji?

## Pytania o migrację i wersjonowanie

- Jak migrować powiązania synset_id gdy Słowosieć zmienia numery synsetów między wersjami?
- Jak wersjonować `PhraseologyDetector.mwe_dict` — dodanie nowych idiomów nie może łamać testów?
- Jak zapewnić, że stary `EnrichedToken` z synset_id v3.2 jest kompatybilny z Słowosiecia v4.0?

## Pytania o audytowalność

- Jak logować "dlaczego synset X został wybrany" — ścieżka: MFS / kontekst / Walenty?
- Jak przechowywać confidence WSD dla każdego tokenu w raporcie?
- Jak śledzić wersję Słowosieci użytą w danym przebiegu (hash pliku relacji)?

---

## Rozszerzalność i skalowanie (kluczowe dla projektu zarobkowego)

### Stopniowe dodawanie słów i zbitek wyrazowych

- Jak dodać nowy leksem do systemu (neologizm, termin branżowy) bez przeładowania całej Słowosieci?
- Jak hot-add nowy synset do `SlowosiecAdapter` w czasie działania serwisu?
- Jak system wykryje, że słowo pojawia się wystarczająco często w korpusie, żeby zasłużyć na nowy synset?
- Jak dodać nową kolokację (zbitkę wyrazową) do `PhraseologyDetector.mwe_dict` bez restartu?
- Jak mierzyć siłę kolokacji (Pointwise Mutual Information, t-score) dla nowo dodanych par słów?
- Jak zaimplementować `add_lemma(form, synset_id, pos)` — inkrementalne rozszerzenie słownika?
- Jakie testy regresyjne uruchomić po każdym dodaniu nowego leksemu?
- Jak walidować, że nowy leksem nie łamie istniejących reguł WSD?

### Stopniowe skalowanie zasobu

- Jakie jest zachowanie `SlowosiecAdapter` przy 10k / 100k / 1M synsetów — gdzie jest punkt krytyczny?
- Jak cachować wyniki `get_synsets()` żeby unikać powtarzanych lookupów przy 1000 zdań?
- Jak lazy-load domeny tematyczne Słowosieci (załaduj prawnicze tylko gdy domena=prawna)?
- Jak wersjonować przyrostowe dodawanie słów — git tag per "stan słownika" danego projektu?
- Jak zaimplementować `diff_lexicon(v1, v2)` pokazujący co się zmieniło między wersjami słownika?

### Stopniowe rozszerzanie MWE i idiomów

- Jak zaimplementować `learn_mwe(corpus)` — automatyczne wykrywanie nowych MWE z korpusu?
- Jak mierzyć pokrycie idiomów: ile % zdań w korpusie testowym zawiera przynajmniej 1 MWE?
- Jak stopniowo rozszerzać `mwe_dict` od najprostszych (bigrams) do złożonych (trigrams, idiomy)?
- Jak testować regresję po dodaniu nowego idiom — czy stare zdania nadal są poprawnie parseowane?
- Jak PhraseologyDetector obsługuje nakładające się MWE ("wziąć pod uwagę wzgląd" — 2 idiomy jednocześnie)?

### Inkrementalne aktualizacje bez restartu

- Jak Walenty obsługuje nowe czasowniki — czy reload ramy walencyjnej wymaga restartu silnika?
- Jak zaimplementować `register_verb_frame(verb, roles)` — dynamiczne dodawanie ram walencyjnych?
- Jak powiadomić W5 (InferenceEngine) o nowych synsetach bez recompilacji reguł Drools?
- Jak inkrementalnie aktualizować graf synonimów w Neo4j (W4) po dodaniu nowego synset?

### Obsługa złożoności zdań (skalowanie lingwistyczne)

- Jak WSD zachowuje się dla zdań złożonych podrzędnie — czy kontekst z zdania podrzędnego liczy się?
- Jak PhraseologyDetector radzi sobie ze zdaniami o długości >50 tokenów (nested MWE)?
- Jak `SlowosiecAdapter` obsługuje sfrazeologizowane całości ("pies ogrodnika") w kontekście całego akapitu?
- Czy Lesk WSD działa lepiej przy akapicie (więcej kontekstu) niż przy jednym zdaniu?
