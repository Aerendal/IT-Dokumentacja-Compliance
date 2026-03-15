---
layer: W8
title: "Warstwa 8 — Compliance Audit (AuditEngine, NKJPBridge, EventFrame)"
phase: 8
status: planned
docs_version: 1.0.0
tags: [AuditEngine, NKJPBridge, EventFrame, StateMatrix, GapAnalysis, RISK-01, CONS-02, stress-test]
---

# Warstwa 8 — Compliance Audit (AuditEngine, NKJPBridge, EventFrame)

## Przegląd

Warstwa 8 implementuje zaawansowany audyt zgodności i analizę zdarzeń.
Rozszerza W0 (doc audit) o:
- **NKJPBridge** — mapowanie tagów morfosyntaktycznych NKJP na role w grafie
- **EventFrame** — 6-wymiarowy model zdarzenia (AGENT, ACTION, PATIENT, INSTRUMENT, LOCATION, TIME)
- **StateMatrix** — deduplikacja i "zamrażanie" wniosków compliance
- **AuditEngine** — silnik reguł RISK-01, CONS-02 + generowanie raportów luk
- **GapAnalysisGenerator** — eksport raportów luk jako REST API (W7)

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W8 istnieje bo lista `AuditFinding` z W5 to surowe wyniki — klient zarobkowy potrzebuje audytowalnego raportu: który przepis/wymóg/reguła był sprawdzany, z którym konkretnym zdaniem dokumentu to naruszenie jest związane, kto i kiedy przeprowadził audyt, jak wynik zmienił się między rewizjami dokumentu. W8 łączy `AuditFinding` z `EventFrame` (6-wymiarowy model zdarzenia), `NKJPBridge` (mapowanie na standardy NKJP) i `StateMatrix` (historia zmian stanu). Bez W8 mamy listę błędów bez kontekstu, bez historii, bez powiązania ze źródłem — nieużyteczne w sądzie lub przy roszczeniu kontraktowym.

**Co się sypie bez tej warstwy:**
- Brak audit trail: nie wiadomo "na podstawie czego" system sflagował naruszenie — klient może podważyć wynik w sporze cywilnym
- Brak historii: nie można wykazać że dokument był niezgodny PRZED poprawką i zgodny PO — traceability wymagana przez normy audytowe
- `StateMatrix` nie istnieje: ten sam dokument audytowany dwukrotnie daje zduplikowane wyniki; raport nieidempotentny = nieaudytowalny

**Zależności:**
- Wchodzi z W5: `List[AuditFinding]`
- Wchodzi z W1: morfologiczne dane zdania (przez W4) dla `NKJPBridge`
- Wchodzi z W0: `{doc_class, validation_mode}` — tryb walidacji
- Wychodzi do W7: `GapAnalysisReport` jako JSON przez REST API
- Wychodzi do klienta: `TraceabilityMatrix` — każde naruszenie powiązane z regułą, zdaniem i timestampem audytu

## Diagram przepływu danych

```
Tekst z NKJP (XML)
       |
  NKJPBridge
  (mapowanie tagów MSD -> role: case=inst -> INSTRUMENT)
       |
       v
  EventFrame (6 wymiarów: AGENT, ACTION, PATIENT, INSTRUMENT, LOCATION, TIME)
       |
       v
  StateMatrix
  (deduplikacja, zamrazanie wniosków, RISK-01, CONS-02)
       |
       v
  AuditEngine
  (reguły: brak testu, brak szyfrowania, brak dokumentacji)
       |
       v
  GapAnalysisReport
  (eksport: JSON / Markdown / REST API)
       |
       v
  W7 FastAPI /audit endpoint
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Stwórzmy moduł do wykrywania luk w analizie ryzyka (RISK-01).
- Zaimplementujmy strukturę klasy EventNode z 6 wymiarami analizy..
- Pokaż pełną implementację tej funkcji łączącej moduły audytu..
- Pokaż strukturę danych EventNode dla 6 wymiarów analizy zdarzeń.
- Pokaż strukturę Gap Analysis Report dla wykrytych luk..
- Jakie profile Złotych Standardów przypiszemy do różnych typów dokumentów — UMOWA_TEMPLATE, SRS_TEMPLATE, RAPORT_AUDYTU_TEMPLATE?
- Jak GoldenStandardProfile definiuje obowiązkowe sekcje per typ dokumentu używane przez AuditEngine do oceny kompletności?
- Jak AuditEngine porównuje audytowany dokument z GoldenStandardProfile — diff wymaganych vs. obecnych sekcji jako lista luk?

### 2. Kontrakty danych
- Jak zmapować tagi MSD z NKJP na relacje w grafie?
- Jaki jest format wejściowy AuditEngine — surowy tekst dokumentu, EventFrame z W5, czy oba jednocześnie?
- Jak wygląda schemat JSON dla raportu compliance z polami: naruszenia, pewność, uzasadnienie, identyfikator reguły?
- Jak zdefiniować kontrakt dla pola severity w naruszeniu compliance — enum (LOW/MEDIUM/HIGH/CRITICAL)?
- Jakie pola są wymagane w EventFrame przekazywanym z W5 do W8 — id, predicate, roles, timestamp, source_doc_id?
- Jak zdefiniować kontrakt dla wersjonowania raportów compliance — czy raport v2 jest kompatybilny wstecz z v1?
- Jak zdefiniować kontrakt dla GoldenStandardProfile — pola: document_type, required_sections, required_rules, version?
- Jak wersjonować GoldenStandardProfile — czy zmiana standardu UMOWA_TEMPLATE v1→v2 unieważnia historyczne raporty?
- Jak wdrożyć Klasyfikator Kontekstu i Złotych Standardów łącznie — KlasyfikatorKontekstu wybiera GoldenStandardProfile, AuditEngine waliduje dokument?
- Jak zdefiniować kontrakt AuditResponse — pola: document_type (z KlasyfikatorKontekstu), violations, knowledge_gaps, applied_golden_standard?
- Jak zintegrować document_profile z AuditResponse w FastAPI — KlasyfikatorKontekstu.classify() → document_profile → AuditEngine(profile) → AuditResponse?

### 3. Implementacja
- Pokaż jak zapisać zdarzenie „Wykonawca dostarczył dokumentację techniczną z opóźnieniem" w grafie..
- Jak wygenerować Raport Luk w formacie tabeli pokrycia?
- Pokaż model danych dla zdarzenia 'Wykonawca dostarczył dokumentację z opóźnieniem' (CONS-02)..
- Jak zaimplementować wymiar naruszenia_zobowiązania w regułach wnioskowania?
- Stwórzmy model danych dla zdarzenia kontraktowego z AGENT, ACTION, PATIENT, MANNER..
- Jak zmapować 6 wymiarów zdarzenia na graf Neo4j?
- Pokaż model danych dla zdarzenia 'Zamawiający odstąpił od umowy pismem'..
- Pokaż dokładny model danych dla zdarzenia 'Wykonawca nie dostarczył dokumentacji w terminie'..
- Jak rozbudować regułę POSSESSION o wymiar ekonomiczny i prawny?
- Jak wdrożyć regułę klasyfikacji naruszenia_terminowego (CONS-02) w InferenceEngine?
- Zaimplementujmy regułę klasyfikacji naruszenia zobowiązania kontraktowego..
- Pokaż kod reguły klasyfikacji prawnej na podstawie naruszenia terminu.
- Pokaż przykład analizy incydentu w 6 wymiarach event reasoning..
- Zaimplementujmy regułę RISK-01 dla analizy ryzyka w API..
- Zaimplementujmy regułę CONS-02 sprawdzającą opisy komponentów w grafie.
- Pokaż jak zmapować tagi NKJP na relacje w grafie.
- Zaimplementujmy 6 wymiarów analizy zdarzeń dla zdania o dostarczeniu dokumentacji.
- Zaimplementujmy Data Bridge do mapowania tagów NKJP na graf..
- Jakie jest 6 wymiarów wielowymiarowego modelu zdarzeń?
- Napiszmy Data Bridge do mapowania tagów NKJP na graf..
- Jak mapować tagi morfosyntaktyczne NKJP na relacje w grafie?
- Pokaż jak wdrożyć 6-wymiarowy Model Zdarzeń w ontologii..
- Zaktualizujmy NKJPBridge o automatyczne mapowanie ról z przypadków gramatycznych..
- Pokaż jak zamodelować 6 wymiarów zdarzenia w ontologii grafowej..
- Jak wdrożyć mechanizm 'zamrażania wniosków' w State Matrix dla NKJP?
- Jak NKJPErrorLogger pomaga w wykrywaniu luk w ontologii?
- Wygenerujmy finalny raport luk dla dokumentacji technicznej..
- Jak EventFrame wykrywa brakujące wymiary w incydentach?
- Zaprojektujmy szablon tekstowy Raportu Luk dla inżyniera..
- Jakie błędy najczęściej loguje NKJPErrorLogger w polskich tekstach?
- Czy dodajemy relację INSTRUMENT dla tagu inst w NKJPBridge?
- Jak StateMatrix deduplikuje błędy przy wielodomenowej analizie zdarzeń?
- Pokaż kod odtwarzania podmiotu z końcówki czasownika w NKJPBridge..
- Zaimplementujmy Gap Analysis Report dla brakujących wymiarów zdarzeń..
- Zaimplementujmy funkcję run_end_to_end_audit() i raport luk..
- Jak rozszerzyć EventFrame o wymiary prawne i wojskowe?
- Zastosujmy regułę odtwarzania podmiotu z końcówki czasownika..
- Zaimplementujmy Gap Analysis Report dla wykrytych luk..
- Jak rozbudować łańcuchy przyczynowe o osie czasu?
- Jak endpoint /audit w W7 wywołuje W8 (AuditEngine) — synchronicznie w request czy asynchronicznie z kolejką?
- Jak W8 serializuje wynik audytu do formatu akceptowanego przez endpoint /audit (JSON z listą naruszeń)?
- Jak reguła rekonstrukcji IMPLICIT_SUBJECT w NKJPBridge integruje się z EventFrame — podmiot staje się AGENT?
- Jak testować regułę rekonstrukcji podmiotu domyślnego na zbiorze NKJP — pokaż minimalny zestaw zdań referencyjnych?
- Jak logować każdą rekonstrukcję IMPLICIT_SUBJECT do celów audytu — co zapisać w EventFrame.metadata?
- Jak AuditEngine korzysta z KlasyfikatorKontekstu do wyboru zestawu reguł compliance per typ dokumentu?
- Jak wynik KlasyfikatorKontekstu trafia do nagłówka GapAnalysisReport — pole document_type: enum?
- Jak AuditEngine mapuje typ dokumentu z KlasyfikatorKontekstu na zestaw reguł compliance — słownik type→ruleset?
- Jak obsłużyć dokument z typem UNKNOWN w AuditEngine — zastosuj zestaw reguł bazowych czy odrzuć?
- Jak logować decyzję KlasyfikatorKontekstu w raporcie audytu dla celów traceability?
- Jak zaimplementować szablony walidacyjne per typ dokumentu w AuditEngine — klasa DocumentTemplate z listą obligatoryjnych reguł?
- Jak AuditEngine weryfikuje że audytowany dokument spełnia szablon walidacyjny — missing sections vs. required sections diff?
- Jak raport audytu compliance osadza diagram Mermaid.js łańcucha przyczynowego naruszenia CONS-02?
- Jak renderować Mermaid.js w raporcie Markdown — znacznik ```mermaid z zawartością flowchart LR?
- Stwórzmy wizualizację grafu zdarzeń w Mermaid.js dla raportu audytu — jak sekcja raportu zawiera osadzony diagram z konkretnymi EventFrame?
- Jak parametryzować wizualizację Mermaid.js w raporcie — tryb skrócony (top 5 węzłów) vs. pełny (cały łańcuch) zależnie od severity?
- Jak zaimplementować klasę KnowledgeGapTracker do logowania nieznanych zdarzeń — predykat nie pasuje do żadnego synsetu w Słowosieci?
- Jak KnowledgeGapTracker rejestruje zdarzenia bez dopasowanej reguły DRL — hook after_rule_evaluation gdy activated_rules jest puste?
- Jak KnowledgeGapTracker eksportuje listę luk wiedzy do kolejki aktywnego uczenia — format JSONL z polami: predicate, context, doc_id, timestamp?
- Pokaż przykład raportu prezentującego Wykryte Luki w Wiedzy Silnika — sekcja knowledge_gaps z polami: unknown_predicates, missing_synsets, unmatched_rules?
- Jak GapAnalysisReport odróżnia luki compliance (brakujący wymóg z GoldenStandardProfile) od luk wiedzy silnika (nieznany predykat)?
- Jak KnowledgeGapTracker dostarcza zagregowane dane do sekcji knowledge_gaps w GapAnalysisReport po zakończeniu sesji przetwarzania?
- Jak zintegrować KnowledgeGapTracker z potokiem analizy zdarzeń w AuditEngine — `tracker.check(event_frame)` przed wywołaniem reguł DRL dla każdego zdarzenia?
- Jak KnowledgeGapTracker wpływa na wynik GapAnalysisReport — zdarzenia bez dopasowania trafiają do sekcji `knowledge_gaps` a nie `violations`?
- Stwórzmy wizualizację grafu zdarzeń w Mermaid.js dla raportu — jak AuditEngine generuje pole `mermaid_diagram` w AuditResponse z flowchart LR zawierającym :EventFrame naruszenia?
- Jak filtrować węzły :EventFrame w wizualizacji raportu — pokazuj tylko zdarzenia severity CRITICAL/HIGH aby uniknąć przesłonięcia kluczowych naruszeń zbędnymi węzłami?
- Przygotujmy metodę to_html() w GapAnalysisReport — serializuje raport jako kompletny plik HTML z tabelą naruszeń i osadzonym diagramem Mermaid.js w jednym pliku?
- Jak to_html() osadza diagram Mermaid.js w raporcie HTML — inline `<div class="mermaid">` z zawartością flowchart LR wewnątrz sekcji "Łańcuch przyczynowy" raportu?

### 4. Testowanie
- Jak stworzyć wielowymiarowy test dla reguły prawnej dotyczącej kłusownictwa?
- Zbudujmy loger błędów dla stress testu na danych NKJP..
- Napiszmy test integracyjny sprawdzający wykrywanie luk w CONS-02..
- Uruchommy stress_test.py na 10 000 zdań z korpusu NKJP..
- Zróbmy Stress Test na NKJP i wykryjmy błędy..
- Pokaż skrypt stress_test.py dla tysiąca zdań z NKJP..
- Jak zintegrować wyniki stress testu z poprawkami w NKJPBridge?
- Zaimplementujmy NKJPErrorLogger i skrypt stress_test.py dla 1000 zdań.
- Stwórzmy skrypt stress_test.py i uruchommy go na danych NKJP.
- Uruchommy stress_test.py na 1000 zdań z NKJP..
- Uruchommy skrypt stress_test.py na próbce 1000 zdań..
- Jak wykorzystać logi jako testy regresyjne i dodać regułę rekonstruującą domyślny podmiot z końcówki czasownika..
- Jak uruchomić skrypt testowy CONSTRAINT_VIOLATION na pełnym zbiorze NKJP i zapisać wyniki do raportu CSV?
- Jak zweryfikować że reguła CONSTRAINT_VIOLATION nie generuje false positive dla klauzul dozwolonych w aneksie?

### 5. Obsługa błędów
- Jakie błędy w BRIDGE_ERROR zdarzają się najczęściej?
- Jakie błędy w BRIDGE_ERROR najczęściej pojawiają się w testach?
- Jakie błędy w BRIDGE_ERROR pojawiają się najczęściej?
- Jak obsłużyć elipsy w polskich tekstach, aby uniknąć BRIDGE_ERROR?
- Co się dzieje gdy AuditEngine otrzyma EventFrame z brakującymi polami wymaganymi przez regułę compliance?
- Jak obsłużyć timeout audytu gdy dokument ma setki EventFrame do przetworzenia — partial result czy błąd?

### 6. Integracja z innymi warstwami
- Jak zintegrować NKJPAdapter z bezstanowym silnikiem InferenceEngine?
- Pokaż jak zintegrować Słowosieć z analizą 6 wymiarów zdarzenia..
- Jak zintegrować EventFrame z wynikami StateMatrix w raporcie?
- Pokaż jak zintegrować EventFrame.missing_dimensions() z AuditReportGenerator.
- Wystawmy GapAnalysisGenerator jako REST API w FastAPI.
- Zintegrujmy pełny pipeline NKJP z GapAnalysisReport.

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Co się dzieje gdy AuditEngine generuje sprzeczne wyniki dla tego samego dokumentu przy dwóch uruchomieniach?
- Jak uniknąć false positive CONS-02 gdy opóźnienie dostawy jest explicite dozwolone w aneksie umowy?
- Jakie jest ryzyko gdy NKJPBridge zwróci null dla terminu który istnieje w bazie ale pod inną formą fleksyjną?
- Jak obsłużyć dokument gdzie ta sama klauzula jest opisana w dwóch sprzecznych paragrafach tego samego aktu?
- Czy wynik audytu compliance jest legalnie wiążący — jak opisać ograniczenia narzędzia w raporcie dla klienta?
- Jak zapewnić że EventFrame generowany przez W8 jest idempotentny przy powtórnym audycie tego samego dokumentu?
- Co się dzieje gdy dokument używa niestandardowej terminologii branżowej której brak w NKJP ani Walenty?

## Pytania uzupełniające
- **Pułapka 3:** `NKJPBridge` obsługuje tagi MSD ze standardu Morfeusz2 — starsze dane z NKJP używają tagów Pantery (inny standard); bridge musi rozróżniać oba formaty, bo milcząca nieprawidłowa konwersja generuje fałszywe BRIDGE_ERROR.
- **Pułapka 4:** `StateMatrix` bez "zamrażania wniosków" pozwala na cofnięcie stanu — jeśli reguła R2 cofa wniosek R1 po dodaniu nowego faktu, starsze raporty audytu są retrospektywnie błędne (problem dla dokumentacji zarobkowej).
- **Pułapka 5:** `AuditReportGenerator` produkuje raport w momencie wywołania — jeśli ten sam dokument jest analizowany dwukrotnie (np. po aktualizacji reguł), dwa raporty mogą mieć różne wyniki bez zmiany dokumentu.
- **Pułapka 6:** GDPR — jeśli analizowane dokumenty projektowe zawierają dane osobowe (imię/nazwisko autora, PESEL w przykładach), wyniki audytu w SQLite są RODO-objęte; brak mechanizmu anonimizacji przed zapisem to ryzyko prawne.

### 1. Architektura

- Jak NKJPBridge integruje się z bezstanowym InferenceEngine (W5)?
- Jak EventFrame różni się od EventRoleDict z W2 — co dodają wymiary compliance?
- Jak AuditEngine rozszerza W0 (doc_auditor) nie duplikując jego funkcji?
- Jak StateMatrix koordynuje wnioski z W5 i AuditEngine — który ma priorytet?
- Jak GapAnalysisGenerator eksponuje raporty przez FastAPI (W7)?

### 2. Kontrakty danych

- Jaki jest schemat EventNode z 6 wymiarami analizy — które pola są obowiązkowe?
- Jaki jest schemat Gap Analysis Report — fields: rule_id, severity, description, evidence?
- Jaki jest format pliku BRIDGE_ERROR log — fields: zdanie, tag_MSD, brak mapowania?
- Jak kodować RISK-01 violation — jaki jest struktura JSON alertu compliance?
- Jak EventFrame.missing_dimensions() zwraca listę brakujących wymiarów?

### 3. Implementacja

- Jak zaimplementować NKJPBridge.map_tag(msd_tag) -> role dla wszystkich przypadków gramatycznych?
- Jak zaimplementować odtwarzanie podmiotu z końcówki czasownika (elipsa) w NKJPBridge?
- Jak zaimplementować regułę RISK-01 (brak szyfrowania w API komponentu sieciowego)?
- Jak zaimplementować regułę CONS-02 (sprzeczne opisy komponentu w dwóch dokumentach)?
- Jak zaimplementować run_end_to_end_audit() łącząc NKJPBridge + EventFrame + AuditEngine?
- Jak zintegrować tagowanie YAML front matter (layer, status, tags) z `GapAnalysisGenerator` — czy metadane YAML trafiają do raportu luk?

### 4. Testowanie

- Jak napisać stress_test.py dla 1000 zdań z NKJP — co mierzyć (czas, BRIDGE_ERROR rate)?
- Jak napisać test integracyjny dla wykrywania luki CONS-02 (dwa dokumenty + sprzeczność)?
- Jak zbudować NKJPErrorLogger zbierający błędy mapowania dla analizy regresyjnej?
- Jak pisać testy regresyjne z logów stress testu — każdy BRIDGE_ERROR = nowy test?
- Jak testować EventFrame.missing_dimensions() dla zdania bez LOCATION?
- Jak napisać skrypt testowy dla reguły CONSTRAINT_VIOLATION na danych NKJP — jakie zdania powinny tę regułę wyzwalać, a jakie nie?
#### Kompletna hierarchia TDD
- Napisz czerwony test TDD dla `AuditEngine.run(doc)` — `test_finds_cons02()`: dokument z naruszeniem terminu → `AuditFinding(rule_id='CONS-02', severity=HIGH)`.
- Zaimplementuj Fazę GREEN dla `AuditEngine` — minimalna logika: przyjmij `AuditFinding[]` z W5, dodaj `doc_ref` i `timestamp`, zwróć `GapAnalysisReport`.
- Jak zrefaktoryzować `AuditEngine` po GREEN — wydzielić `TraceabilityMapper` (łączący finding z zdaniem) i `HistoryDiff` (zmiana między rewizjami)?
- Zrefaktoryzuj `AuditEngine` — każdy wymiar `EventFrame` (AGENT, ACTION, PATIENT...) walidowany przez osobny `DimensionValidator` z testem jednostkowym.
- Jak napisać test jednostkowy dla `NKJPBridge.map_tag_to_role()` — mock tagu NKJP, sprawdzić mapowanie na rolę semantyczną?
- Jak zbudować oracle dataset dla W8 — 15 dokumentów prawnych z oczekiwanymi `GapAnalysisReport` jako golden files?
- Jak zmierzyć Mutation Score dla `StateMatrix` — które warunki deduplikacji findings są najtrudniejsze do pokrycia?
- Jak napisać test własnościowy (Hypothesis) dla `AuditEngine` — idempotentność: ten sam dokument audytowany 2× → identyczny `GapAnalysisReport` (StateMatrix działa)?
- Jak zapewnić że zmiana formatu `EventFrame` nie zmienia struktury `GapAnalysisReport` eksportowanego przez API W7?
- Stwórz test regresyjny `AuditEngine` — golden file: 5 dokumentów kontraktowych + oczekiwany raport compliance; CI fail gdy kształt się zmieni.
- Jak przetestować W0→W8 end-to-end: dokument SRS → `doc_auditor` → pipeline NLP → `AuditEngine` → sprawdź audit trail z timestampem i `doc_ref` per finding?

### 5. Obsługa błędów

- Co loguje NKJPBridge gdy tag MSD nie ma mapowania (BRIDGE_ERROR)?
- Co robi AuditEngine gdy EventFrame ma mniej niż 3 z 6 wymiarów?
- Jak obsłużyć elipsę podmiotu w polskich tekstach bez fałszywych alarmów RISK-01?
- Co zwrócić gdy stress_test.py wykryje >10% BRIDGE_ERROR rate?
- Jak StateMatrix zapobiega fałszywym alarmom przy wielodomenowej analizie?
- Co robi `run_end_to_end_audit()` gdy jeden etap pipeline zwróci `None` zamiast wyjątku (cichy błąd)?
- Jak obsługiwać dokument który zmienił się między startem a końcem audytu (audit race condition)?

### 6. Integracja z innymi warstwami

- Jak W8 dostaje EventRoleDict z W2 — przez W5 czy bezpośrednio?
- Jak W8 używa NKJPBridge do konwersji danych z W1 (Morfeusz/CoNLL-U)?
- Jak GapAnalysisReport jest eksponowany przez W7 (FastAPI /audit)?
- Jak W8 zapisuje wyniki audytu do Neo4j (W4) dla długoterminowego trackowania?
- Jak W0 i W8 kooperują — co robi W0, czego W8 nie robi?
- Jak W8 obsługuje przypadek gdy W5 (silnik wnioskowania) zwróci sprzeczne wnioski dla tej samej reguły?
- Jak W8 raportuje luki identyfikowane przez W0 (doc audit) w kontekście oceny ryzyka compliance?
- Jak weryfikować że raport compliance z W8 jest idempotentny dla tego samego zestawu EventFrame?

### 7. Pułapki i ryzyka

- **Pułapka 1:** NKJPBridge bez obsługi elipsy flaguje ~30% polskich zdań jako BRIDGE_ERROR (brak AGENT) — konieczna integracja z W6 (ellipsis_recovery).
- **Pułapka 2:** StateMatrix bez "zamrażania wniosków" powoduje wielokrotne alarmy RISK-01 dla tego samego komponentu — każde nowe zdanie re-triggeruje audyt.
- **Pułapka 3:** CONS-02 (sprzeczności) wymaga porównania semantycznego między dokumentami — bez W3 (Słowosieć) false positive rate >20%.
- **Pułapka 4:** Starsze dane NKJP używają tagów Pantery (inny standard niż Morfeusz2) — bridge musi rozróżniać oba formaty; milcząca zła konwersja generuje fałszywe BRIDGE_ERROR.
- **Pułapka 5:** `StateMatrix` bez "zamrażania wniosków" — reguła może cofnąć wcześniejszy wniosek po dodaniu nowego faktu; starsze raporty audytu stają się retrospektywnie błędne.
- **Pułapka 6:** GDPR — jeśli dokumenty projektowe zawierają dane osobowe (PESEL w przykładach), wyniki audytu w SQLite są RODO-objęte; brak anonimizacji to ryzyko prawne w projekcie zarobkowym.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| BRIDGE_ERROR rate na stress test 1000 zdań NKJP | < 5% |
| Precision RISK-01 (brak fałszywych alarmów) | >= 95% |
| Recall CONS-02 (wykrycie sprzeczności) | >= 80% |
| Czas generowania Gap Analysis Report (100 dokumentów) | < 30 s |
| Pokrycie testów linii | >= 85% |

## Pytania o idempotentność i deterministyczność

- Czy run_end_to_end_audit() na identycznym zestawie dokumentów daje identyczny raport?
- Czy NKJPBridge.map_tag(tag) jest deterministyczny dla identycznego wejścia?
- Jak StateMatrix zapewnia, że te same fakty nie są dodawane dwukrotnie?

## Pytania o migrację i wersjonowanie

- Jak aktualizować reguły RISK-01/CONS-02 bez reaudytowania wszystkich historycznych dokumentów?
- Jak wersjonować EventFrame schema gdy dodajemy nowy wymiar (np. MANNER)?
- Jak migrować NKJPBridge gdy NKJP wypuszcza nowy format tagowania?

## Pytania o audytowalność

- Jak każdy alarm compliance (RISK-01, CONS-02) jest powiązany z konkretnym dokumentem, zdaniem, regułą?
- Jak przechowywać historię audytów per projekt dla celów dowodowych (odpowiedzialność cywilna)?
- Jak wygenerować raport "co system wykrył w projekcie X, kiedy, przez kogo zatwierdzony"?

---

## Rozszerzalność i skalowanie

### Stopniowe rozszerzanie reguł audytu

- Jak dodać nową regułę compliance (RISK-02, RISK-03) bez modyfikowania istniejących reguł?
- Jak zaimplementować `register_compliance_rule(id, condition, severity)` — dynamiczne reguły?
- Jak testować nową regułę compliance na historycznych danych bez re-audytowania wszystkiego?
- Jak stopniowo rozszerzać NKJPBridge o nowe mapowania tagów MSD bez naruszania istniejących?
- Jak wersjonować reguły audytu — changelog per projekt z opisem co reguła sprawdza i dlaczego?

### Skalowanie na duże korpusy

- Jak stress_test.py zachowuje się dla 1k / 10k / 100k zdań — czas, BRIDGE_ERROR rate, zużycie RAM?
- Jak zaimplementować streaming audit — przetwarzanie zdań po jednym bez ładowania całego korpusu?
- Jak EventFrame radzi sobie ze zdaniami wielokrotnie złożonymi (>5 klauzul)?
- Jak StateMatrix skaluje się przy tysiącach równoległych wniosków (thread-safe deduplikacja)?
- Jak zaimplementować incremental audit — audytuj tylko nowe dokumenty, nie cały projekt?

### Stopniowe rozszerzanie na nowe domeny

- Jak NKJPBridge obsługuje dokumenty z nowej domeny (np. medycznej) — czy wymaga nowych mapowań?
- Jak dodać nowy słownik domenowy do AuditEngine (np. terminy prawne → nowe reguły RISK)?
- Jak wykrywać, że nowa domena wymaga nowych reguł — analiza BRIDGE_ERROR rate per domena?
- Jak testować, że reguły compliance dla domeny prawnej nie generują false positive w medycznej?
- Jak zaimplementować `audit_domain(documents, domain='legal')` — audyt z filtrowaniem domenowym?

### Audyt przyrostowy (incremental audit trail)

- Jak śledzić zmiany w projekcie między audytami — "w wersji v2 pojawiły się 3 nowe luki vs v1"?
- Jak zaimplementować diff raportów luk między dwoma datami?
- Jak przechowywać pełną historię audytów (100 audytów × 1000 dokumentów) efektywnie?
