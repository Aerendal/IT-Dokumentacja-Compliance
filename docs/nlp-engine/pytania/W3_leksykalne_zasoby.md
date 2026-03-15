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

- Zdefiniujmy testy dla synkretyzmu form takich jak słowo zamek..
- Pokaż jak rozbudować testy o przypadki synkretyzmu i wieloznaczności..
- Dopiszmy test synkretyzmu gramatycznego dla słowa „dam”..
- Zaimplementujmy logikę ujednoznaczniania w Fazie GREEN przy użyciu UDPipe..
- Zdefiniujmy testy dla synkretyzmu gramatycznego słowa dam..
- Jakie reguły ujednoznaczniania dodać do silnika disambiguation?
- Jak zintegrować Słowosieć z grafem wiedzy w Fazie 2?
- Jak wdrożyć parser zależności UDPipe do testowania synkretyzmu?
- Pokaż jak zaprojektować model danych grafu dla wieloznaczności..
- Jakie są różnice między homonimią a polisemią w testach?
- Pokaż jak zintegrować Słowosieć z ontologią grafu..
- Pokaż słownik kolokacji ułatwiający ujednoznacznianie..
- Jak wdrożyć silnik ujednoznaczniający dla polisemicznych pojęć?
- Jak uniknąć problemu eksplozji ontologii w takim systemie?
- Zbudujmy słownik kolokacji ułatwiający ujednoznacznianie..
- Czy możemy dodać warstwę ujednoznaczniania sensów (WSD) do modułu?
- Jak wdrożyć disambiguation engine dla synkretyzmu i wieloznaczności?
- Pokaż jak zbudować słownik kolokacji wspierający ujednoznacznianie..
- Jak stworzyć słownik kolokacji wspierający ujednoznacznianie wieloznaczności?
- Zbudujmy słownik kolokacji ułatwiający ujednoznacznianie semantyczne..
- Chcę zobaczyć, jak zaimplementować ten mechanizm ujednoznaczniania..
- Pokaż jak zintegrować Słowosieć z grafem w Pythonie..
- Jak algorytmicznie wybierać właściwe znaczenie wieloznacznych słów?
- Pokaż przykład kodu integrującego Słowosieć do wyboru znaczenia słowa..
- Jak zintegrować Słowosieć z grafem w Pythonie?
- W jaki sposób optymalnie ograniczyć zakres mojego systemu?
- Jak algorytmicznie wybrać właściwy synset przy wieloznaczności słowa?
- Jak zintegrować Słowosieć z tym potokiem w Fazie 2?
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
- Jak obsłużyć wieloznaczność słowa klucz w grafie?
- Jak zaimplementować mechanizm WSD dla słowa „testy jednostkowe” w grafie?
- Pokaż jak zintegrować Słowosieć w celu ujednoznaczniania pojęć..
- Jak zintegrować Słowosieć do ujednoznaczniania pojęć w grafie?
- Jak zaimplementować ujednoznacznianie pojęć dla słowa zamek?
- Jak wdrożyć prostą heurystykę szukającą przecięć kontekstu z hiperonimami?
- Zastosujmy Baseline: Najczęstszy sens (MFS) ze Słowosieci dla zamka..
- Napiszmy czerwony test dla synsetu słowa zamek.
- Stwórzmy czerwony test dla detektora idiomów w Fazie 3..
- Stwórzmy test jednostkowy dla PhraseologyDetector w Fazie 3..
- Pokaż logikę detekcji idiomów zapalającą test na zielono..
- Pokaż strukturę węzła Concept uwzględniającą synset_id i rolę.
- Jak uniknąć eksplozji ontologii przy tysiącach reguł?
- Jak zintegrować Słowosieć z naszym modelem ontologii?
- Które polskie słowniki najlepiej zintegrować z ontologią?
- Jak zintegrować Słowosieć z ontologią, by system rozumiał hiperonimy?
- Jak powiązać węzły :Concept z konkretnymi synsetami Słowosieci?
- Pokaż regułę dla Słowosieci obsługującą synonimy 'dać'..
- Jak zintegrować Słowosieć, by reguła obsługiwała synonim wręczyć?
- Jak zintegrować Słowosieć do obsługi synonimów w regułach?
- Jak rozszerzyć wyszukiwanie o synonimy ze Słowosieci?
- Jak zintegrować Słowosieć, aby obsłużyć synonimy czasownika 'dać'?
- Pokaż jak zintegrować Słowosieć do obsługi synonimów.
- Stwórzmy detektor dla idiomów i jednostek wielowyrazowych..
- Jak zaimplementować detekcję idiomów takich jak 'rzucić okiem'?
- Pokaż implementację detektora idiomów i jednostek wielowyrazowych..
- Jak zaimplementować detektor idiomów jako jednostek wielowyrazowych?
- Pokaż test dla idiomu 'odnieść sukces' w zdaniu..
- Jak rozbudować mwe_dict o idiomy?
- Czy detektor idiomów powinien działać przed lematyzacją?
- Pokaż jak dodać detektor jednostek wielowyrazowych i idiomów.

## Pytania uzupełniające

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
- Jak testować Walenty — czy "zabić" ma ramę z AGENT:NP i PATIENT:NP?

### 5. Obsługa błędów

- Co zwraca `SlowosiecAdapter` dla słów spoza Słowosieci (neologizmy, nazwy własne)?
- Jak obsługiwać `get_synsets()` gdy Słowosieć nie jest załadowana (OOM, brak pliku)?
- Co robi `PhraseologyDetector` gdy idiom jest częściowo rozgromiony przez wstawienie słowa?
- Jak obsługiwać homonimię między kategorii (rzeczownik "zamek" vs przymiotnik "zamknięty")?
- Jakie jest zachowanie WSD przy zdaniach bez kontekstu (jedno słowo)?

### 6. Integracja z innymi warstwami

- Jak W3 przekazuje `EnrichedToken` do W2 — before or after SRL (co jest prerequisite)?
- Jak W4 (Neo4j) przechowuje hiperonimię ze Słowosieci — jako krawędzie `IS_A`?
- Jak W5 (InferenceEngine) używa Słowosieci do wnioskowania o gatunkach ("wróbel IS_A ptak")?
- Jak W3 integruje się z W6 (koreferencja) — czy WSD poprawia wykrywanie zaimków?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Słowosieć 3.x ma nierówne pokrycie — czasowniki mają znacznie mniej synsetów niż rzeczowniki. Fallback MFS dla czasowników jest konieczny.
- **Pułapka 2:** Eksplozja ontologii przy ładowaniu pełnej hiperonimii Słowosieci do Neo4j (>500k relacji) — konieczne selektywne ładowanie per domena.
- **Pułapka 3:** Walenty nie pokrywa neologizmów ani anglicyzmów — brak ramy walencyjnej nie oznacza błędu, ale wymaga explicitnego fallbacku rule-based.

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
