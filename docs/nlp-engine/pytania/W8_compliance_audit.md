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


- Pokaż jak zapisać zdarzenie „Jan zabił zwierzę” w grafie..
- Jak wygenerować Raport Luk w formacie tabeli pokrycia?
- Jak stworzyć wielowymiarowy test dla reguły prawnej dotyczącej kłusownictwa?
- Pokaż model danych dla zdarzenia Jan zabił zwierzę..
- Jak zaimplementować wymiar kłusownictwa w regułach wnioskowania?
- Stwórzmy model danych dla zdarzenia 'Jan zabił zwierzę'..
- Jak zmapować 6 wymiarów zdarzenia na graf Neo4j?
- Pokaż model danych dla zdarzenia 'Jan zabił zwierzę'..
- Pokaż dokładny model danych dla zdarzenia Jan zabił zwierzę..
- Jak rozbudować regułę POSSESSION o wymiar ekonomiczny i prawny?
- Jak wdrożyć regułę klasyfikacji kłusownictwa w InferenceEngine?
- Zaimplementujmy regułę klasyfikacji prawnej dla kłusownictwa..
- Pokaż kod reguły klasyfikacji prawnej na podstawie kłusownictwa.
- Pokaż przykład analizy incydentu w 6 wymiarach event reasoning..
- Jak zmapować tagi MSD z NKJP na relacje w grafie?
- Zbudujmy loger błędów dla stress testu na danych NKJP..
- Zaimplementujmy regułę RISK-01 dla analizy ryzyka w API..
- Napiszmy test integracyjny sprawdzający wykrywanie luk w CONS-02..
- Zaimplementujmy regułę CONS-02 sprawdzającą opisy komponentów w grafie.
- Jak zintegrować NKJPAdapter z bezstanowym silnikiem InferenceEngine?
- Pokaż jak zmapować tagi NKJP na relacje w grafie.
- Zaimplementujmy 6 wymiarów analizy zdarzeń dla zdania o zwierzęciu.
- Stwórzmy moduł do wykrywania luk w analizie ryzyka (RISK-01).
- Zaimplementujmy Data Bridge do mapowania tagów NKJP na graf..
- Jakie jest 6 wymiarów wielowymiarowego modelu zdarzeń?
- Pokaż jak zintegrować Słowosieć z analizą 6 wymiarów zdarzenia..
- Napiszmy Data Bridge do mapowania tagów NKJP na graf..
- Jak mapować tagi morfosyntaktyczne NKJP na relacje w grafie?
- Pokaż jak wdrożyć 6-wymiarowy Model Zdarzeń w ontologii..
- Zaimplementujmy strukturę klasy EventNode z 6 wymiarami analizy..
- Zaktualizujmy NKJPBridge o automatyczne mapowanie ról z przypadków gramatycznych..
- Pokaż jak zamodelować 6 wymiarów zdarzenia w ontologii grafowej..
- Jak wdrożyć mechanizm 'zamrażania wniosków' w State Matrix dla NKJP?
- Uruchommy stress_test.py na 10 000 zdań z korpusu NKJP..
- Jakie błędy w BRIDGE_ERROR zdarzają się najczęściej?
- Jak NKJPErrorLogger pomaga w wykrywaniu luk w ontologii?
- Zróbmy Stress Test na NKJP i wykryjmy błędy..
- Wygenerujmy finalny raport luk dla dokumentacji technicznej..
- Jak EventFrame wykrywa brakujące wymiary w incydentach?
- Pokaż pełną implementację tej funkcji łączącej moduły audytu..
- Zaprojektujmy szablon tekstowy Raportu Luk dla inżyniera..
- Jak zintegrować EventFrame z wynikami StateMatrix w raporcie?
- Pokaż skrypt stress_test.py dla tysiąca zdań z NKJP..
- Jakie błędy najczęściej loguje NKJPErrorLogger w polskich tekstach?
- Jak zintegrować wyniki stress testu z poprawkami w NKJPBridge?
- Zaimplementujmy NKJPErrorLogger i skrypt stress_test.py dla 1000 zdań.
- Jakie błędy w BRIDGE_ERROR najczęściej pojawiają się w testach?
- Pokaż strukturę danych EventNode dla 6 wymiarów analizy zdarzeń.
- Czy dodajemy relację INSTRUMENT dla tagu inst w NKJPBridge?
- Jak StateMatrix deduplikuje błędy przy wielodomenowej analizie zdarzeń?
- Stwórzmy skrypt stress_test.py i uruchommy go na danych NKJP.
- Pokaż jak zintegrować EventFrame.missing_dimensions() z AuditReportGenerator.
- Uruchommy stress_test.py na 1000 zdań z NKJP..
- Jakie błędy w BRIDGE_ERROR pojawiają się najczęściej?
- Pokaż strukturę Gap Analysis Report dla wykrytych luk..
- Pokaż kod odtwarzania podmiotu z końcówki czasownika w NKJPBridge..
- Zaimplementujmy Gap Analysis Report dla brakujących wymiarów zdarzeń..
- Jak obsłużyć elipsy w polskich tekstach, aby uniknąć BRIDGE_ERROR?
- Zaimplementujmy funkcję run_end_to_end_audit() i raport luk..
- Jak rozszerzyć EventFrame o wymiary prawne i wojskowe?
- Uruchommy skrypt stress_test.py na próbce 1000 zdań..
- Zastosujmy regułę odtwarzania podmiotu z końcówki czasownika..
- Zaimplementujmy Gap Analysis Report dla wykrytych luk..
- Jak rozbudować łańcuchy przyczynowe o osie czasu?
- Jak wykorzystać logi jako testy regresyjne i dodać regułę rekonstruującą domyślny podmiot z końcówki czasownika..
- Wystawmy GapAnalysisGenerator jako REST API w FastAPI.
- Zintegrujmy pełny pipeline NKJP z GapAnalysisReport.


## Pytania uzupełniające

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

### 5. Obsługa błędów

- Co loguje NKJPBridge gdy tag MSD nie ma mapowania (BRIDGE_ERROR)?
- Co robi AuditEngine gdy EventFrame ma mniej niż 3 z 6 wymiarów?
- Jak obsłużyć elipsę podmiotu w polskich tekstach bez fałszywych alarmów RISK-01?
- Co zwrócić gdy stress_test.py wykryje >10% BRIDGE_ERROR rate?
- Jak StateMatrix zapobiega fałszywym alarmom przy wielodomenowej analizie?

### 6. Integracja z innymi warstwami

- Jak W8 dostaje EventRoleDict z W2 — przez W5 czy bezpośrednio?
- Jak W8 używa NKJPBridge do konwersji danych z W1 (Morfeusz/CoNLL-U)?
- Jak GapAnalysisReport jest eksponowany przez W7 (FastAPI /audit)?
- Jak W8 zapisuje wyniki audytu do Neo4j (W4) dla długoterminowego trackowania?
- Jak W0 i W8 kooperują — co robi W0, czego W8 nie robi?

### 7. Pułapki i ryzyka

- **Pułapka 1:** NKJPBridge bez obsługi elipsy flaguje ~30% polskich zdań jako BRIDGE_ERROR (brak AGENT) — konieczna integracja z W6 (ellipsis_recovery).
- **Pułapka 2:** StateMatrix bez "zamrażania wniosków" powoduje wielokrotne alarmy RISK-01 dla tego samego komponentu — każde nowe zdanie re-triggeruje audyt.
- **Pułapka 3:** CONS-02 (sprzeczności) wymaga porównania semantycznego między dokumentami — bez W3 (Słowosieć) false positive rate >20%.

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
