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

- Jak wdrożyć resolver odniesień do grafu wiedzy?
- Omówmy problem koreferencji między zdaniami w Fazie 2..
- Pokaż jak zintegrować koreferencję z grafem wiedzy w Neo4j..
- Jak zintegrować koreferencję z grafem wiedzy w Neo4j?
- Stwórzmy czerwony test dla CoreferenceResolvera.
- Jak połączyć CoreferenceResolver z grafem w Neo4j?
- Czy detekcja zaimków wymaga integracji z NKJP?
- Napiszmy logikę dopasowania rodzaju gramatycznego dla anafor..
- Jak zintegrować CoreferenceResolver z Grafem Wiedzy Neo4j?
- Stwórzmy teraz czerwony test integracyjny dla scalania węzłów grafu..
- Jak zaimplementować mechanizm Recency Heuristic w CoreferenceResolver?
- Pokaż jak GraphDatabaseAdapter powinien obsługiwać zaimki po koreferencji..
- Jak obsłużyć elipsę i brakujący podmiot w koreferencji?
- Czy system wykryje koreferencję dla imion o różnych rodzajach?
- Jak obsłużyć elipsę w CoreferenceResolverze dla języka polskiego?
- Zaimplementujmy funkcję merge_coreferences i sprawdźmy wynik w Neo4j..
- Jakie są zalety Recency Heuristic w polskim?
- Czy zintegrować CoreferenceResolver z GraphDatabaseAdapter?
- Jak testować łączenie faktów między zdaniami?
- Jak połączyć CoreferenceResolver z bazą Neo4j w pipeline?
- Pokaż implementację logiki łączenia zaimka z podmiotem..
- Jak system rozróżnia podmioty przy wielu osobach w tekście?
- Napiszmy czerwony test dla modułu koreferencji..
- Jak zintegrować moduł koreferencji w celu łączenia wątków?
- Jak zaimplementować śledzenie koreferencji między wieloma zdaniami w grafie?
- Zintegrujmy to z modułem koreferencji dla dłuższego tekstu..
- Zaimplementujmy mechanizm koreferencji dla zaimków w grafie.
- Jak wdrożyć koreferencję dla zaimków 'on' i 'ten'?
- Przejdźmy do koreferencji – jak system ma rozpoznać zaimki?
- Napiszmy test dla sekwencji zdarzeń z Janem i autem.
- Pokaż jak zintegrować Słowosieć dla synonimów w koreferencji.
- Jak wdrożyć mechanizm koreferencji dla zaimków w grafie?
- Zaimplementujmy test sekwencji zdarzeń dla mechanizmu koreferencji..
- Jak przetestować koreferencję na przykładzie Jana i auta?
- Pokaż test integracyjny sekwencji zdarzeń dla Jana.
- Pokaż przykład logu błędu dla zdania z elipsą podmiotu..

## Pytania uzupełniające

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

### 5. Obsługa błędów

- Co robi `CoreferenceResolver` gdy nie ma żadnego kandydata dla zaimka (pierwszy zaimek w dokumencie)?
- Jak obsługiwać zaimki nieokreślone ("ktoś", "coś") — brak antecedentu?
- Co gdy Morfeusz zwraca wiele interpretacji rodzaju dla kandydata?
- Jak obsługiwać długie łańcuchy koreferencji (>10 zaimków odnoszących się do tego samego bytu)?
- Co się dzieje przy sprzecznych wskaźnikach rodzaju ("Jan" ale zaimek "ona")?

### 6. Integracja z innymi warstwami

- Jak W6 dostaje tokeny z W1 — jako lista obiektów `Token` czy jako `DependencyTree`?
- Kiedy W6 działa w pipeline — przed W2 (SemanticMapper) czy po?
- Jak W4 (Neo4j) merguje węzły na podstawie `CoreferenceChain`?
- Jak W5 (InferenceEngine) korzysta z rozwiązanych zaimków — czy dostaje już zaktualizowany `EventRoleDict`?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Polska fleksja daje wiele form dla tego samego rodzaju — "on" może wskazywać na rzeczownik M1, M2 lub M3 (osobowy/nieosobowy). Bez Morfeusza błędne zmergowanie.
- **Pułapka 2:** Elipsa podmiotu jest normą w polskim (~30% zdań) — ignorowanie ellipsis_recovery = brak AGENT w 30% eventów w W5.
- **Pułapka 3:** Recency Heuristic daje ~65% accuracy — dla tekstów prawnych (gdzie precyzja ma znaczenie) potrzebne rule-based rozszerzenie (np. rola semantyczna kandydata).

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
