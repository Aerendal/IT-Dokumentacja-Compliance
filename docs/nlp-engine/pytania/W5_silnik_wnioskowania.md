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
buduje łańcuchy przyczynowe i inferencje (stan obiektu, posiadanie, lokalizacja, kłusownictwo).

Kluczowe klasy: `InferenceEngine`, `StateMatrix`, `IntentClassifier`.

## Diagram przepływu danych

```
Graf Neo4j (W4) + EventRoleDict (W2)
       │
  InferenceEngine
  ┌────────────────────────────────────────────┐
  │  _rule_location(event) → LOCATED_AT        │
  │  _rule_possession_transfer(event) → OWNS   │
  │  _rule_state_change(event) → state=dead    │
  │  _rule_classify_legal(event) → kłusownictwo│
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

- Jak w grafie wiedzy oznaczyć intencję działania aktora?
- Jakie reguły logiczne w Drools obsłużą synkretyzm form?
- Wyjaśnij różnicę między modelem lingwistycznym a modelem zdarzenia..
- Jakie reguły logiczne wdrożyć dla automatycznej ontologii?
- Pokaż przykład implementacji reguł Drools dla grafu..
- Jak stworzyć model ontologii zdarzeń dla domeny prawnej?
- Napiszmy funkcję build_event_graph w Fazie GREEN..
- Jakie reguły weryfikacji zastosować dla ontologii zdarzeń w fazie 2?
- Jak wdrożyć model danych grafu (Neo4j) dla analizy zdarzeń?
- Czy system może sam wywnioskować intencję na podstawie narzędzia?
- Wyjaśnij barierę eksplozji reguł i ontologii w projektach symbolicznych..
- Jakie reguły w silniku Drools obsłużą relacje agent-patient?
- Pokaż przykład wnioskowania logicznego w systemie symbolicznym..
- Jak załadować Słowosieć do modułu wnioskowania w Pythonie?
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
- Jak zintegrować reguły Drools z wynikami parsera lxml?
- Pokaż przykład reguły Drools rozwiązującej synkretyzm..
- Pokaż przykład reguły Drools mapującej składnię na rolę agent..
- Pokaż przykład reguły Drools dla relacji AGENT i PATIENT..
- Jak połączyć relację HAS_TRIGGER z wnioskowaniem w silniku Drools?
- Jak w Drools połączyć rozpoznaną akcję z wymogiem testu?
- Pokaż regułę Drools dla testu integracyjnego.
- Jak zmapować relacje przyczynowe w grafie zdarzeń?
- Jak połączyć GraphDatabaseAdapter z modułem wnioskowania Drools?
- Jak rozszerzyć ontologię o relacje przyczynowe w Neo4j?
- Stwórzmy czerwony test dla nowej klasy InferenceEngine.
- Jak zdefiniować regułę dedukcji dla lokalizacji w grafie?
- Czy Drools to dobry wybór dla polskiego silnika wnioskowania?
- Pokaż pętlę dedukcji, która zapali test na zielono..
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
- Czy Drools wymaga osobnego modułu w pipeline?
- Jak zapisać regułę w pliku .drl dla Drools?
- Stwórzmy test dla reguły skutku akcji 'zabić' w InferenceEngine.
- Jak zapisać regułę lokalizacji w natywnym formacie Drools .drl?
- Pokaż jak zintegrować Słowosieć z regułami wnioskowania o gatunkach.
- Pokaż logikę pętli w natywnym pliku .drl dla Drools.
- Jak zintegrować Słowosieć z regułami wnioskowania o lokalizacji?
- Jak zintegrować Słowosieć z ontologią pojęć w silniku wnioskowania?
- Jakie reguły wnioskowania dodać dla domeny prawnej i medycznej?
- Pokaż przykład pliku .drl dla reguły lokalizacji.
- Jak połączyć Walentego z naszym modelem zdarzeń i ról?
- Jakie reguły wnioskowania najlepiej obsłużą hierarchię gatunków ze Słowosieci?
- Jak zaimplementować wykrywanie ramy subkategoryzacyjnej dla czasownika 'zabić'?
- Przetestujmy ramy walencyjne dla nowych czasowników..
- Pokaż regułę wnioskowania o posiadaniu dla Jana i Marii.
- Jakie są najtrudniejsze ramy walencyjne w języku polskim?
- Pokaż przykład złożonej ramy walencyjnej dla nowej domeny..
- Napiszmy czerwony test dla nowej reguły posiadania w InferenceEngine..
- Jak rozbudować model zdarzenia o wymiar narzędzia i intencji?
- Pokaż jak zaimplementować regułę _rule_possession_transfer w kodzie..
- Pokaż logikę wstrzymania zapisu dla intencji QUESTION w InferenceEngine..
- Pokaż regułę wnioskowania: 'Maria posiada książkę' po akcji 'dać'..
- Jak rozbudować InferenceEngine o tryb odpytywania grafu?
- Jak rozszerzyć reguły wnioskowania o wymiar intencji i przyczyny?
- Pokaż kod metody _rule_possession_transfer dla silnika..
- Jak wykryć negację dla reguły _rule_possession_transfer?
- Czy możemy rozbudować tę regułę o wymiar intencji?
- Jak obsłużyć zaprzeczenia w regule _rule_possession_transfer?
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

## Pytania uzupełniające

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
- Jak zaimplementować `_rule_classify_legal(event)` wykrywającą kłusownictwo (AGENT + zabić + gatunek chroniony)?
- Jak zaimplementować `IntentClassifier` — detekcja QUESTION przez słowa pytajne?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `InferenceEngine` — `"Jan zabił zwierzę"` → `{state: dead, legal: kłusownictwo}`?
- Jak testować wielowymiarowy model zdarzenia: AGENT + ACTION + PATIENT + INSTRUMENT + LOCATION + TIME?
- Jak testować negację: `"Jan nie dał Marii książki"` → `posiadanie=NOT_OCCURRED`?
- Jak testować łańcuch: zdanie 1 = "Jan zabrał broń", zdanie 2 = "Jan zabił" → wnioskowanie o narzędziu?
- Jak testować zapytania o lokalizację: `"Gdzie jest Jan?"` → przeszukanie grafu → odpowiedź?

### 5. Obsługa błędów

- Co robi `InferenceEngine` gdy EventRoleDict nie ma AGENT (elipsa podmiotu)?
- Jak obsługiwać sprzeczne reguły (reguła A i reguła B dają przeciwne wyniki)?
- Co gdy Drools nie może załadować pliku `.drl` (syntax error)?
- Jak obsługiwać nieskończoną pętlę dedukcji (A → B → A)?
- Jak logować, które reguły zostały aktywowane i w jakiej kolejności?

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

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Czas wnioskowania dla 1 zdania (1000 reguł) | < 100 ms |
| Czas wnioskowania batch 100 zdań | < 10 s |
| Precision klasyfikacji prawnej (kłusownictwo) | ≥ 95% |
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
- Jak wygenerować raport "dlaczego system sklasyfikował zdarzenie jako kłusownictwo"?

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
