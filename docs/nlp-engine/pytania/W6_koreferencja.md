---
layer: W6
title: "Warstwa 6 — Koreferencja i Anaforyka"
phase: 6
status: planned
docs_version: 1.0.0
tags: [CoreferenceResolver, koreferencja, zaimki, elipsa, anaforyka, Recency-Heuristic]
---

# Warstwa 6 — Koreferencja i Anaforyka

## Przegląd

Warstwa 6 rozwiązuje problem koreferencji w polskich tekstach wielozdaniowych:
- Identyfikuje, do czego odnosi się zaimek ("on", "ten", "jej", "tym")
- Wykrywa elipsę podmiotu (podmiot domniemany z końcówki czasownika)
- Scala węzły grafu reprezentujące ten sam byt
- Dostarcza `CoreferenceChain` do W4 (Neo4j) i W5 (InferenceEngine)

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W6 istnieje bo dokumenty prawne, umowy i raporty techniczne używają intensywnie zaimków i elipsy — "Jan zawarł umowę. Jej przedmiotem jest..." — "Jej" odnosi się do "umowy". Bez W6 W2 przypisuje role zaimkom bez antecedensów; W4 zapisuje "jej_nierozwiązana" jako osobny węzeł; W5 wnioskuje o "jej_nierozwiązana" zamiast o "umowa". W przypadku dokumentów prawnych (które są głównym targetem projektu zarobkowego) — 30-50% zdań zawiera zaimki lub elipsę podmiotu (polskie czasowniki nie wymagają jawnego podmiotu: "zawarł umowę" = podmiot wynika z końcówki).

**Co się sypie bez tej warstwy:**
- Każde zdanie z zaimkiem ma AGENT/PATIENT "nieznany" lub błędny — precyzja W2 spada o 15-30% dla dokumentów wielozdaniowych
- W4 ma N osobnych węzłów dla tej samej osoby zamiast jednego — zapytania Cypher zwracają fragmentaryczne wyniki
- W5 nie może budować historii działań osoby/podmiotu — traci kontekst między zdaniami

**Zależności:**
- Wchodzi z W1: `DependencyNode[upos, feats, dep_rel]` dla detekcji zaimków i końcówek osobowych
- Wchodzi z W4 (poprzednie zdania): istniejące węzły w grafie jako kandydaci na antecedens
- Wychodzi do W2 (ADR-02): `CoreferenceChain` — rozwiązane zaimki przed mapowaniem ról
- Wychodzi do W4: instrukcje scalenia węzłów (MERGE zamiast CREATE dla znanych bytów)

## Diagram przepływu danych

```
Sekwencja zdań (z W1) + DependencyTree
       │
  CoreferenceResolver
  ┌─────────────────────────────────────────────────┐
  │  mention_detection()  → lista NP + zaimków      │
  │  gender_number_match() → filtrowanie Morfeuszem │
  │  recency_heuristic()  → wybór najbliższego ante  │
  │  ellipsis_recovery()  → podmiot z końcówki czas │
  └─────────────────────────────────────────────────┘
       │
  CoreferenceChain: [("on" → "Jan"), ("ten" → "Jan")]
       │
       ▼
  GraphDatabaseAdapter.merge_coreferences() (W4)
  InferenceEngine.resolve_pronouns() (W5)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Pokaż jak GraphDatabaseAdapter powinien obsługiwać zaimki po koreferencji..
- Jaki jest podział odpowiedzialności między CoreferenceResolver a modułem anafory i elipsy?
- Jak wyglądają granice W6 — co otrzymuje z W1 (parse tree) a co przekazuje do W5 (enriched facts)?
- Jaki wzorzec stosuje W6 dla rozwiązywania łańcuchów koreferencyjnych — grafowy BFS/DFS czy sekwencyjny?
- Jak W6 integruje się z W2 (role semantyczne) gdy antecedent posiada przypisaną rolę AGENT lub PATIENT?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest format wyjściowy CoreferenceResolver — lista par (anaphor_id, antecedent_id) w JSON?
- Jak zdefiniować kontrakt dla łańcucha koreferencyjnego (chain) gdy anaphor wskazuje na klaster podmiotów?
- Jakie pola są wymagane w strukturze przekazywanej z W6 do W5 (silnik wnioskowania)?
- Jak obsłużyć brak antecedenta w kontrakcie — null w polu antecedent_id, pusta lista, czy wyjątek ValidationError?
- Jak wygląda przykładowy obiekt koreferencji dla "Wykonawca dostarczył dokumentację. On opóźnił dostawę" — pokaż JSON?

### 3. Implementacja
- Jak wdrożyć resolver odniesień do grafu wiedzy?
- Omówmy problem koreferencji między zdaniami w Fazie 2..
- Jak połączyć CoreferenceResolver z grafem w Neo4j?
- Czy detekcja zaimków wymaga integracji z NKJP?
- Napiszmy logikę dopasowania rodzaju gramatycznego dla anafor..
- Jak zaimplementować mechanizm Recency Heuristic w CoreferenceResolver?
- Czy system wykryje koreferencję dla imion o różnych rodzajach?
- Zaimplementujmy funkcję merge_coreferences i sprawdźmy wynik w Neo4j..
- Jakie są zalety Recency Heuristic w polskim?
- Pokaż implementację logiki łączenia zaimka z podmiotem..
- Jak system rozróżnia podmioty przy wielu osobach w tekście?
- Jak zaimplementować śledzenie koreferencji między wieloma zdaniami w grafie?
- Zaimplementujmy mechanizm koreferencji dla zaimków w grafie.
- Jak wdrożyć koreferencję dla zaimków 'on' i 'ten'?
- Przejdźmy do koreferencji – jak system ma rozpoznać zaimki?
- Jak wdrożyć mechanizm koreferencji dla zaimków w grafie?
- Pokaż przykład logu błędu dla zdania z elipsą podmiotu..

### 4. Testowanie
- Stwórzmy czerwony test dla CoreferenceResolvera.
- Stwórzmy teraz czerwony test integracyjny dla scalania węzłów grafu..
- Jak testować łączenie faktów między zdaniami?
- Napiszmy czerwony test dla modułu koreferencji..
- Napiszmy test dla sekwencji zdarzeń z Janem i autem.
- Zaimplementujmy test sekwencji zdarzeń dla mechanizmu koreferencji..
- Jak przetestować koreferencję na przykładzie Jana i auta?
- Pokaż test integracyjny sekwencji zdarzeń dla Jana.

### 5. Obsługa błędów
- Jak obsłużyć elipsę i brakujący podmiot w koreferencji?
- Jak obsłużyć elipsę w CoreferenceResolverze dla języka polskiego?
- Jak obsługiwać dokument gdzie ta sama osoba jest nazywana trzema różnymi sposóbami ("Jan", "Kowalski", "powód") — czy trzy odrębne łańcuchy czy jeden?

### 6. Integracja z innymi warstwami
- Pokaż jak zintegrować koreferencję z grafem wiedzy w Neo4j..
- Jak zintegrować koreferencję z grafem wiedzy w Neo4j?
- Jak zintegrować CoreferenceResolver z Grafem Wiedzy Neo4j?
- Czy zintegrować CoreferenceResolver z GraphDatabaseAdapter?
- Jak połączyć CoreferenceResolver z bazą Neo4j w pipeline?
- Jak zintegrować moduł koreferencji w celu łączenia wątków?
- Zintegrujmy to z modułem koreferencji dla dłuższego tekstu..
- Pokaż jak zintegrować Słowosieć dla synonimów w koreferencji.

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jakie jest ryzyko gdy CoreferenceResolver tworzy fałszywe łańcuchy dla różnych osób o tym samym imieniu lub tytule?
- Jak obsłużyć zaimek dzierżawczy (jego dokumentacja, jej oferta) gdy antecedent jest w poprzednim akapicie?
- Co się dzieje gdy zdanie zawiera trzy anaforyczne pronominale bez jednoznacznego antecedenta?
- Jak uniknąć propagacji błędów koreferencji z W6 do W5 (silnik wnioskowania operuje na błędnie złączonych podmiotach)?
- Czy elipsa werbalna jest odróżnialna od opuszczonego czasownika bez głębokiej analizy kontekstu składniowego?
- Jakie są konsekwencje błędu w koreferencji dla identyfikacji strony umowy — pomylenie Wykonawcy z Podwykonawcą?
- Jak obsłużyć długi dokument (1000+ zdań) gdzie antecedent jest 50 zdań wcześniej niż anaphor?

## Pytania uzupełniające
- **Pułapka 3:** `CoreferenceResolver` zakłada że antecedent jest w tym samym lub poprzednim zdaniu — w polskich tekstach prawnych antecedens może być 5+ zdań wcześniej (definicja na początku umowy).
- **Pułapka 4:** Zaimki "jej" i "jego" są polisemiczne: "jej" to G.sg.f LUB D.sg.f — bez Morfeusza (W1) `gender_number_match` nie może rozróżnić płci antecedensa.
- **Pułapka 5:** Elipsa podmiotu w ~30% polskich zdań — `IMPLICIT_SUBJECT` jest normą, ale błędna rekonstrukcja podmiotu z końcówki czasownika przy nieregularnych formach (np. "bywał") może dać błędną osobę.
- **Pułapka 6:** Merge węzłów koreferencyjnych w Neo4j (W4) jest nieodwracalny — jeśli `CoreferenceResolver` błędnie połączy dwie różne osoby "Jan Kowalski" i "Jan Nowak", błąd propaguje się do wszystkich zapytań.

### 1. Architektura

- Jak `CoreferenceResolver` integruje się z pipeline — czy działa jako pre-processing przed W2 czy post-processing?
- Czy `CoreferenceResolver` jest stateful (pamięta dokument) czy stateless (tylko jedno zdanie)?
- Jak zarządzać pamięcią przy rozwiązywaniu koreferencji w długich dokumentach (>1000 zdań)?
- Jak podzielić detekcję wzmianek (mention detection) od rozwiązywania koreferencji?
- Jaka jest granica odpowiedzialności między W6 (koreferencja) a W5 (wnioskowanie o bytach)?

### 2. Kontrakty danych

- Jaki jest schemat `CoreferenceChain` — lista par `(pronoun, antecedent)` czy graph struktura?
- Jak kodować pewność rozwiązania (confidence) dla każdego powiązania zaimek → antecedens?
- Jak `CoreferenceChain` jest przekazywany do W4 — lista par czy słownik zaimek → entity_id?
- Jak kodować elipsę — pustą wartość AGENT z flagą `IMPLICIT_SUBJECT: true`?
- Jak W5 otrzymuje rozwiązane zaimki — czy W6 modyfikuje `EventRoleDict` z W2?

### 3. Implementacja

- Jak zaimplementować `gender_number_match(pronoun, candidates) -> List[Candidate]` z Morfeuszem?
- Jak zaimplementować `recency_heuristic` — wybierz najbliższy antecedens pasujący rodzajem/liczbą?
- Jak zaimplementować `ellipsis_recovery` — odczytaj osobę z końcówki czasownika (`-m → 1sg`, `-ł → 3sg.m`)?
- Jak zbudować `mention_detector` — lista NP z drzewa zależności + lista zaimków?
- Jak zaimplementować `merge_coreferences(chain, graph)` scalający węzły Neo4j?
- Jak wdrożyć regułę rekonstrukcji podmiotu domyślnego w `NKJPBridge` — wykrywanie elipsy podmiotowej z końcówki fleksyjnej czasownika?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `CoreferenceResolver` — "Jan wyszedł. On był zmęczony." → `on → Jan`?
- Jak testować elipsę: "Wyszedł." (bez podmiotu) → `IMPLICIT_SUBJECT: Jan` (z poprzedniego zdania)?
- Jak testować rozróżnienie płci: "Jan i Maria wyszli. Ona była zmęczona." → `Ona → Maria`?
- Jak przetestować `merge_coreferences` — czy Neo4j ma 1 węzeł dla "Jan" po zmergowaniu?
- Jak zbudować oracle dataset koreferencji polskiej (50 par zdań z annotowanymi łańcuchami)?
#### Kompletna hierarchia TDD
- Zaimplementuj Fazę GREEN dla `CoreferenceResolver` — heurystyka Recency: dla 'on' znajdź najbliższy Masc.Sing noun w poprzednim zdaniu.
- Jak zrefaktoryzować `CoreferenceResolver` po GREEN — zastąpić Recency-Heuristic modelowym MentionPairClassifier?
- Zrefaktoryzuj `CoreferenceResolver` — metoda `resolve()` powinna być chain of responsibility: Recency → Agreement → Model, zatrzymać się na pierwszym pewnym dopasowaniu.
- Jak napisać test jednostkowy dla `_agreement_check(mention, candidate)` — izolacja od parsera, mock `CoreferenceChain`?
- Jak napisać test integracyjny W1→W6→W2: zdanie z elipsą podmiotu → sprawdź że W2 dostaje rozwiązany AGENT?
- Jak zmierzyć Mutation Score dla algorytmu Recency-Heuristic — które warunki zgodności (Gender, Number) są najtrudniejsze do pokrycia?
- Jak zapewnić że zmiana modelu koreferencji nie obniży F1 poniżej 0.75 na corpus polskich dokumentów prawnych?
- Stwórz test regresyjny: 20 par zdań z zaimkami + oczekiwane antecedenty jako golden file; CI fail gdy chain się zmieni.
- Jak przetestować W1→W6→W2→W4 end-to-end — zdanie z elipsą → sprawdź że w grafie Neo4j AGENT jest właściwym podmiotem a nie 'unknown'?

### 5. Obsługa błędów

- Co robi `CoreferenceResolver` gdy nie ma żadnego kandydata dla zaimka (pierwszy zaimek w dokumencie)?
- Jak obsługiwać zaimki nieokreślone ("ktoś", "coś") — brak antecedentu?
- Co gdy Morfeusz zwraca wiele interpretacji rodzaju dla kandydata?
- Jak obsługiwać długie łańcuchy koreferencji (>10 zaimków odnoszących się do tego samego bytu)?
- Co się dzieje przy sprzecznych wskaźnikach rodzaju ("Jan" ale zaimek "ona")?
- Co robi `CoreferenceResolver` gdy W1 zwróci zdanie z zerową liczbą tokenów (puste zdanie)?
- Jak obsługiwać osobę nazwaną trzema sposobami ("Jan", "Kowalski", "powód") — trzy łańcuchy czy jeden?

### 6. Integracja z innymi warstwami

- Jak W6 dostaje tokeny z W1 — jako lista obiektów `Token` czy jako `DependencyTree`?
- Kiedy W6 działa w pipeline — przed W2 (SemanticMapper) czy po?
- Jak W4 (Neo4j) merguje węzły na podstawie `CoreferenceChain`?
- Jak W5 (InferenceEngine) korzysta z rozwiązanych zaimków — czy dostaje już zaktualizowany `EventRoleDict`?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Polska fleksja daje wiele form dla tego samego rodzaju — "on" może wskazywać na rzeczownik M1, M2 lub M3 (osobowy/nieosobowy). Bez Morfeusza błędne zmergowanie.
- **Pułapka 2:** Elipsa podmiotu jest normą w polskim (~30% zdań) — ignorowanie ellipsis_recovery = brak AGENT w 30% eventów w W5.
- **Pułapka 3:** Recency Heuristic daje ~65% accuracy — dla tekstów prawnych (gdzie precyzja ma znaczenie) potrzebne rule-based rozszerzenie (np. rola semantyczna kandydata).
- **Pułapka 3:** `CoreferenceResolver` zakłada antecedens w bliskim oknie — w dokumentach prawnych definicja może być 10+ zdań wcześniej.
- **Pułapka 4:** "jej" i "jego" są polisemiczne (G.sg.f / D.sg.f) — bez Morfeusza (W1) `gender_number_match` nie rozróżnia płci antecedensa.
- **Pułapka 5:** Elipsa podmiotu w ~30% polskich zdań — błędna rekonstrukcja przy nieregularnych formach czasownika może dać błędną osobę.
- **Pułapka 6:** Merge węzłów koreferencyjnych w Neo4j jest nieodwracalny — błędne połączenie "Jan Kowalski" z "Jan Nowak" propaguje się do wszystkich zapytań grafu.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Precision koreferencji zaimków osobowych | ≥ 75% |
| Recall wykrywania elipsy podmiotu | ≥ 80% |
| F1 `gender_number_match` | ≥ 85% |
| Czas przetwarzania dokumentu 100 zdań | < 2 s |
| Pokrycie testów linii | ≥ 85% |

## Pytania o idempotentność i deterministyczność

- Czy `resolve("on", context)` dla identycznego kontekstu zawsze daje ten sam antecedens?
- Czy kolejność zdań w dokumencie determinuje wynik (czy Recency Heuristic jest order-sensitive)?
- Jak zapewnić stabliność wyników gdy Morfeusz jest aktualizowany?

## Pytania o migrację i wersjonowanie

- Jak migrować `CoreferenceChain` format gdy W4 zmienia schemat węzłów?
- Jak wersjonować `ellipsis_recovery` rules gdy dodajemy nowe czasowniki nieregularne?
- Jak backwards-compatible rozszerzyć schema o nowe rodzaje zaimków (np. zaimki wzajemne)?

## Pytania o audytowalność

- Jak logować "dlaczego 'on' zostało zmergowane z 'Jan'" — ścieżka: recency + gender match?
- Jak przechowywać łańcuch koreferencji per dokument dla celów dowodowych?
- Jak śledzić, które zdanie dostarczyło antecedentu dla danego zaimka?

---

## Rozszerzalność i skalowanie

### Stopniowe rozszerzanie koreferencji

- Jak `CoreferenceResolver` rozszerzyć na rozwiązywanie zaimków w tekstach wieloakapitowych (okno kontekstu > 1 zdanie)?
- Jak dodać obsługę nowych typów wyrażeń koreferencyjnych (np. elipsa, zero-anafora) bez przepisywania silnika?
- Jak testować poprawność koreferencji na korpusie z rosnącą liczbą zdań — czy precision/recall nie spada?
- Jak W6 skaluje się na długie dokumenty (>10 000 tokenów) — algorytm O(n²) vs O(n log n)?
- Jak stopniowo dodawać nowe strategie rozwiązywania (ML → rule-based → hybrid) nie łamiąc istniejących?
- Jak wersjonować model koreferencji — żeby móc odtworzyć wyniki z konkretnej wersji modelu?
