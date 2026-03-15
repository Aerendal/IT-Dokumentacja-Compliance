---
layer: W2
title: "Warstwa 2 — Role Semantyczne (SRL)"
phase: 2
status: planned
docs_version: 1.0.0
tags: [SemanticMapper, AGENT, PATIENT, INSTRUMENT, LOCATION, nsubj, SRL, koNLL-U, dep_rel]
---

# Warstwa 2 — Role Semantyczne (SRL)

## Przegląd

Warstwa 2 implementuje Semantic Role Labeling (SRL) dla języka polskiego.
Na wejściu przyjmuje `DependencyTree` z W1, na wyjściu produkuje strukturę zdarzenia z rolami:
AGENT, PATIENT, INSTRUMENT, LOCATION, TIME, CAUSE, GOAL.

Kluczowe klasy: `SemanticMapper`, `SlowosiecAdapter` (WSD dla ról).

## Diagram przepływu danych

```
DependencyTree (CoNLL-U z W1)
       │
  SemanticMapper
  ┌────────────────────────────────┐
  │ nsubj → AGENT                  │
  │ obj   → PATIENT                │
  │ obl (narzędnik) → INSTRUMENT   │
  │ obl (przyimki: w/na/przy) → LOCATION│
  │ obl (przed/po/podczas) → TIME  │
  └────────────────────────────────┘
       │
  SlowosiecAdapter   ← WSD dla polisemicznych słów
       │
       ▼
  EventRoleDict: {AGENT: "Jan", PATIENT: "zwierzę", ...}
       │
       ▼
  W4 (Neo4j) / W5 (InferenceEngine)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Jak zaprojektować model danych grafu dla relacji agent-akcja-obiekt?
- Jak zmapować relację AGENT na strukturę grafową?
- Pokaż strukturę ontologii dla ról AGENT, PATIENT i INSTRUMENT.

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_

### 3. Implementacja
- Jak stworzyć formalną ontologię dla relacji agent-akcja-obiekt?
- Pokaż implementację mapowania ról semantycznych na graf..
- Jak mapować etykiety Universal Dependencies na role semantyczne?
- Jak zaimplementować mapowanie etykiet nsubj i obj na role Agent i Patient?
- Jak powiązać tagi UDPipe z rolami Agent i Patient?
- Pokaż jak zamienić nsubj i obj na role Agent i Patient..
- Pokaż przykładowy kod ekstraktora ról semantycznych..
- Pokaż algorytm mapowania tagów UDPipe na role semantyczne..
- Jak algorytmicznie mapować tagi UDPipe na role Agent i Patient?
- Jak algorytmicznie mapować tagi nsubj i obj na role Agent i Patient?
- Jakie narzędzia polecasz do wizualizacji ról semantycznych w grafie?
- Jak UDPipe pomaga w mapowaniu ról agent-akcja-obiekt?
- Jak algorytmicznie rozwiązać konflikt między relacjami LOCATION a TIME?
- Jakie są najczęstsze błędy parsera UDPipe przy relacji INSTRUMENT?
- Stwórzmy klasę SemanticMapper dla mapowania ról AGENT i PATIENT..
- Jak rozszerzyć ontologię o relacje czasowe i przestrzenne?
- Jak dodać relacje INSTRUMENT i LOCATION do SemanticMapper?
- Jakie reguły zastosować dla relacji czasowych przed i po?
- Jak stworzyć słownik mapujący nsubj na AGENT?
- Pokaż przykład logiki mapowania przyimka na relację LOCATION..
- Czy do mapowania ról semantycznych wystarczą tylko etykiety dep?
- Pokaż kod implementacji SemanticMapper dla agenta i pacjenta..
- Jak dodać do mappera regułę dla instrumentu (np. młotkiem)?
- Jak zmapować przyimki na relacje czasowe w SemanticMapper?
- Dodajmy reguły dla relacji INSTRUMENT i LOCATION..
- Zaimplementujmy model danych grafu dla relacji AGENT-ACTION-PATIENT..
- Jak rozbudować mapowanie o relacje czasowe before i after?
- Pokaż jak zaimplementować wykrywanie relacji LOCATION na podstawie przyimków.
- Rozbudujmy metodę map_roles o analizę przyimków case dla okoliczników.
- Pokaż przykład implementacji relacji INSTRUMENT i LOCATION w kodzie.
- Pokaż jak zmapować nsubj:pass na rolę PATIENT.
- Stwórzmy listę 20 przyimków dla SemanticMapper.
- Pokaż pythonową logikę dla LOCATION i PART_OF.
- Czy Walenty obsługuje role semantyczne dla gatunków chronionych?
- Pokaż jak zamodelować relacje TIME i LOCATION w ontologii..
- Pokaż jak dodać relacje czasowe i przestrzenne do grafu..
- Jak rozbudować relacje czasowe i przestrzenne w grafie?
- Pokaż implementację relacji czasowych przed i po zdarzeniu..
- Jak zmapować przyimki 'z', 'do' na relacje source i destination?
- Jak rozbudować ontologię o relacje czasowe i przestrzenne?

### 4. Testowanie
- Zdefiniujmy test integracyjny dla relacji agent-patient w tym modelu..
- Jak rozbudować test o relacje instrument i location?
- Pokaż jak Hypothesis testuje relacje agent-akcja-obiekt..
- Stwórzmy testy jednostkowe dla klasy SemanticMapper w cyklu TDD..
- Napiszmy czerwony test dla SemanticMapper mapujący AGENT i PATIENT.
- Napiszmy testy dla klasy SemanticMapper.
- Czy do testu dodać też walidację relacji czasowych i lokalizacji?
- Pokaż testy dla roli INSTRUMENT z użyciem obl i narzędnika..
- Wdróżmy ten kod i sprawdźmy testy AGENT/PATIENT.
- Stwórzmy teraz czerwony test dla SlowosiecAdaptera..
- Jak zaprojektować testy integracyjne łączące Słowosieć z SemanticMapperem?
- Pokaż test integracyjny dla SemanticMapper i PhraseologyDetector..
- Zaprojektujmy test integracyjny łączący SemanticMapper i SlowosiecAdapter..
- Pokaż kod testu dla SemanticMapper z regułami Walentego..

### 5. Obsługa błędów
- Jak obsłużyć relacje czasowe before i after w SemanticMapperze?
- Jak obsłużyć wieloznaczność ról semantycznych przy użyciu słownika Walenty?

### 6. Integracja z innymi warstwami
- Pokaż jak zintegrować SemanticMapper z głównym pipeline przetwarzania..
- Jak zintegrować synsety Słowosieci z rolami AGENT i PATIENT?
- Jak zintegrować słownik Walenty, aby poprawnie przypisywać role semantyczne?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
## Pytania uzupełniające

### 1. Architektura

- Jak `SemanticMapper` komunikuje się z `SlowosiecAdapter` — synchronicznie czy przez interfejs?
- Czy `SemanticMapper` powinien być klasą stateless (czysta funkcja) czy stateful (słownik ról)?
- Jak podzielić mapowanie składniowe (nsubj/obj) od mapowania semantycznego (WSD)?
- Jak `SemanticMapper` obsługuje zdania wieloklauzu (zdania podrzędne, orzeczenie imienne)?
- Jaka jest granica odpowiedzialności między W2 a W3 (Słowosieć) przy ujednoznacznianiu?

### 2. Kontrakty danych

- Jaki jest schemat JSON `EventRoleDict` wychodzącego z W2 do W4/W5?
- Jak walidować, że każdy `EventRoleDict` ma przynajmniej jedno AGENT i ACTION?
- Jak kodować brak roli (np. brak INSTRUMENT w zdaniu) — null, pominięcie pola, czy pusty string?
- Jak przechowywać pewność przypisania roli (confidence score 0–1)?
- Jak reprezentować role w zdaniach wieloaktorowych (wiele AGENT)?

### 3. Implementacja

- Jak zaimplementować słownik mapowania `nsubj → AGENT`, `obj → PATIENT` w Pythonie?
- Jak zaimplementować `map_roles(dep_tree) -> dict` obsługując stronę bierną (`nsubj:pass → PATIENT`)?
- Jak rozbudować `map_roles` o analizę przyimków case (w, na, przy → LOCATION; przed, po → TIME)?
- Jak zbudować listę 20 kluczowych przyimków lokalizacyjnych i czasowych w `SemanticMapper`?
- Jak zaimplementować detekcję INSTRUMENT przez case narzędnikowy (morph feature `Case=Ins`)?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `SemanticMapper.map_roles("Jan zabił zwierzę")` → `{AGENT: "Jan", PATIENT: "zwierzę"}`?
- Jak testować stronę bierną: `map_roles("Zwierzę zostało zabite przez Jana")` → `{AGENT: "Jan", PATIENT: "zwierzę"}`?
- Jak zbudować oracle dataset 100 zdań z ręcznie annotowanymi rolami semantycznymi?
- Jak mierzyć Precision/Recall/F1 dla SRL na oracle datasecie?
- Jak testować relacje czasowe `before`/`after` w zdaniach z "przed" i "po"?

### 5. Obsługa błędów

- Co zwraca `map_roles()` gdy `DependencyTree` nie ma żadnego `nsubj`?
- Jak obsługiwać synkretyzm: `obl` może być INSTRUMENT lub LOCATION w zależności od przypadka?
- Co robić, gdy `SlowosiecAdapter` zwraca brak synsetów dla słowa?
- Jak logować nierozwiązane przypisania ról (tokeny bez roli)?
- Jak obsługiwać zdania eliptyczne (brak podmiotu wyrażonego — domyślny podmiot)?

### 6. Integracja z innymi warstwami

- Jak W2 przekazuje `EventRoleDict` do W4 (Neo4j) — bezpośrednia serializacja czy przez W5?
- Jak W3 (Słowosieć/Walenty) poprawia jakość mapowania ról w W2?
- Jak W5 (InferenceEngine) używa ról z W2 do budowania reguł wnioskowania?
- Jak W6 (koreferencja) wpływa na role — jeśli "on" → "Jan", czy W2 dostaje już rozwiązany zaimek?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Polska fleksja powoduje, że ta sama forma może być narzędnikiem (INSTRUMENT) lub nomen (AGENT) — bez `Case=Ins` z Morfeusza błąd propaguje się do W4.
- **Pułapka 2:** Mapowanie wyłącznie przez `nsubj/obj` pomija ~15% zdań z niestandardową kolejnością — konieczna analiza `feats` z W1.
- **Pułapka 3:** Walenty ma niepełne pokrycie dla nowych czasowników (neologizmy, slang techniczny) — potrzebny fallback MFS (Most Frequent Sense).

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Precision SRL na oracle datasecie | ≥ 90% |
| Recall SRL na oracle datasecie | ≥ 85% |
| F1 SRL | ≥ 87% |
| Pokrycie relacji czasowych (before/after) | ≥ 80% |
| Czas przetwarzania 1000 zdań | < 10 s |

## Pytania o idempotentność i deterministyczność

- Czy `map_roles(tree)` dla identycznego drzewa zawsze zwraca identyczny `EventRoleDict`?
- Czy `SlowosiecAdapter.get_synsets(word)` jest deterministyczny przy identycznym kontekście?
- Jak zapewnić stabliność wyników gdy Słowosieć jest aktualizowana (nowe synsety)?

## Pytania o migrację i wersjonowanie

- Jak migrować oracle dataset ról gdy dodajemy nową rolę (np. BENEFICIARY)?
- Jak wersjonować `SemanticMapper`, aby zmiany reguł mapowania nie łamały W4/W5?
- Jak zachować backwards-compatibility dla `EventRoleDict` gdy W5 już używa starszego schematu?

## Pytania o audytowalność

- Jak logować "dlaczego Jan=AGENT" — ścieżka decyzji: `nsubj → Case=Nom → brak nsubj:pass → AGENT`?
- Jak przechowywać confidence score przypisania roli dla raportu do klienta?
- Jak śledzić, który model UDPipe + która wersja Morfeusza wygenerowały dane role?

---

## Rozszerzalność i skalowanie

### Stopniowe dodawanie nowych ról semantycznych

- Jak dodać nową rolę (np. BENEFICIARY, MANNER, CAUSE) do `SemanticMapper` bez łamania istniejących testów?
- Jak zaimplementować `register_role(name, dep_labels, case_features)` — dynamiczne role?
- Jak testować regresję po dodaniu nowej roli — czy stare zdania nadal mają poprawne AGENT/PATIENT?
- Jakie są kryteria decydujące, że rola wymaga nowego pola w `EventRoleDict` vs nowej krawędzi w grafie?
- Jak stopniowo rozszerzać mapowanie: najpierw AGENT/PATIENT → potem INSTRUMENT/LOCATION → potem TIME/CAUSE?

### Skalowanie na złożone struktury zdań

- Jak `SemanticMapper` obsługuje zdania z wieloma AGENT (podmiot zbiorowy: "Jan i Maria zabili")?
- Jak mapować role dla nominalizacji ("zabójstwo Jana" — kto jest AGENT?)?
- Jak obsługiwać strony bierne wielokrotne ("Zwierzę zostało zabite i zjedzone")?
- Jak testować W2 na zdaniach prawnych (zdania wieloklauzowe, pasywne, z nominalnym orzecznikiem)?
- Jak stopniowo rozszerzać słownik przyimków z 20 do 100 (kolejne domeny: medyczna, wojskowa, prawna)?

### Inkrementalne reguły mapowania

- Jak hot-add nową regułę przyimkową do `SemanticMapper` bez restartu pipeline?
- Jak wersjonować zestaw reguł mapowania osobno od kodu (YAML/JSON reguły vs Python logika)?
- Jak mierzyć coverage reguł — ile % zdań jest pokrytych przez aktualne reguły przyimkowe?

---

## Luki zidentyfikowane przez audyt cross-warstwowy

### Kolejność W3 vs W2 w pipeline (niepodjęta decyzja architektoniczna)

- Czy W3 (WSD / Słowosieć) musi działać **przed** W2 (SemanticMapper) — czy `EnrichedToken` z synset_id jest prerequisite dla mapowania ról?
- Jeśli TAK: pipeline ma formę `W1 → W3 → W2`. Jak `SemanticMapper` przyjmuje `EnrichedToken` zamiast surowego `Token`?
- Jeśli NIE: `SemanticMapper` wywołuje W3 wewnętrznie. Jak zdefiniować tę granicę żeby nie było cyklicznej zależności W2↔W3?
- Jaka jest formalna decyzja architektoniczna i gdzie jest udokumentowana (ADR — Architecture Decision Record)?
- Jak przetestować oba scenariusze (W3-before vs W3-inside) żeby wybrać lepszy?

### Kolejność W6 vs W2 w pipeline (koreferencja przed rolami)

- Czy `CoreferenceResolver` (W6) musi działać **przed** `SemanticMapper` (W2) — decyzja: `W1 → W6 → W2` czy `W1 → W2 → W6 → aktualizacja ról`?
- Co się dzieje, gdy W2 dostaje zaimek "on" bez rozwiązania — czy mapuje AGENT="on" czy zwraca `AGENT=UNRESOLVED`?
- Jak `SemanticMapper` oznacza nieroz wiązane zaimki żeby W6 mogło je później scalić?
- Jak testować scenariusz, w którym koreferencja zmienia przypisanie roli (zaimek był PATIENT, po rozwiązaniu okazuje się tym samym bytem co AGENT)?
