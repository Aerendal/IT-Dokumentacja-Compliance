---
title: Predictive Model Degradation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Predictive Model Degradation


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać, wykrywać i obsługiwać degradację modeli predykcyjnych (drift danych/modelu, spadek metryk biznesowych/technicznych) oraz ustalić procedury reakcji, aby utrzymać jakość predykcji i zgodność SLA.


## Zakres i granice

- Obejmuje: definicje degradacji (data drift, concept drift, performance decay), metryki i progi, monitoring on‑line/batch, alertowanie, analizy RCA, retraining, rollback, A/B lub shadow, governance modeli, wpływ na klientów.  
- Poza zakresem: projekt nowych modeli od zera (osobne dokumenty), inżynieria danych upstream (patrz data_quality_playbook).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: metryki produkcyjne (accuracy/AUC/F1, calibration), metryki biznesowe (CTR, conversion, NPS), statystyki feature’ów, rozkłady danych, logi predykcji, informacje o wersjach modeli, harmonogram retrainingu.  
- Wyjścia: plan monitoringu i progów, runbook reakcji na drift, zasady retrainingu/rollbacku, checklisty DoR/DoD, raporty degradacji, decyzje (ADR) dla zmian modeli.


## Założenia

- Dane referencyjne są reprezentatywne.  
- Monitoring ma dostęp do etykiet (gdy opóźnione – używa proxy KPI).  
- Możliwy jest szybki rollout/rollback modeli.


## Otwarte pytania

- Jak obsłużyć modele bez etykiet on‑line (proxy metryki)?  
- Jaki maksymalny czas dopuszczalny między alertem a reakcją?  
- Jakie zasady komunikacji degradacji do klientów?  
- Jak łączyć monitoring modeli z monitoringiem danych upstream?

## Powiązania (meta)

- Key Documents: ml_model_retrospective, model_tracking_metrics, data_quality_playbook, monitoring_strategy_document, rollback_runbook, bias_fairness_policy.  
- Key Document Structures: metryki, detekcja driftu, alerty, reakcja (rollback/retrain), walidacja, komunikacja.  
- Document Dependencies: feature store, model registry, monitoring/observability, CI/CD ML, A/B framework, data catalog.


## Zależności dokumentu

Wymaga: wersjonowania modeli i danych, metryk baseline, dostępnych narzędzi monitoringu (statystyki cech, predykcji, wyników), polityk retrainingu oraz możliwości szybkiego rollout/rollback. Braki = brak DoR.


## Fazy cyklu życia

- Ustalenie baseline i progów.  
- Monitoring ciągły i detekcja driftu.  
- Diagnoza i RCA.  
- Reakcja: rollback/retrain/A/B.  
- Walidacja i publikacja nowej wersji.  
- Retrospektywa i aktualizacja progów.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (ml/predictive_model_degradation)  
- model_tracking_metrics, data_quality_playbook, rollback_runbook


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

1. Skonfiguruj monitoring i progi na etapie releasu modelu.  
2. Przy alercie wykonaj checklistę RCA i wybierz reakcję (rollback/retrain).  
3. Zweryfikuj nową wersję (offline + A/B/shadow); wdroż i odhacz DoD.  
4. Zaktualizuj registry, linkage_index i raport degradacji.


## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- Data drift: zmiana rozkładu cech wejściowych.  
- Concept drift: zmiana relacji cechy→etykieta.  
- PSI (Population Stability Index): statystyka stabilności rozkładów.


## Przykłady użycia

- Spadek CTR po zmianie źródła ruchu (data drift).  
- Model detekcji fraudu zaniża precyzję po pojawieniu się nowych wzorców (concept drift).  
- Wzrost błędów predykcji przez brakujące cechy po migracji danych.


## Ryzyka i ograniczenia

- Brak alertów → cichy spadek jakości i wpływ biznesowy.  
- Fałszywe alarmy przy małej próbce → szum i wypalenie zespołu.  
- Zbyt agresywny rollback → utrata ulepszeń.  
- Brak wersjonowania danych → trudna RCA.


## Decyzje i uzasadnienia

- Wybór metryk/progów i wag alertów.  
- Kryteria wyboru reakcji (rollback vs retrain vs A/B).  
- Okresy agregacji danych monitorujących.  
- Retencja logów i próbek do RCA.


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

- Metryki ↔ Progi ↔ Alerty ↔ Reakcja.  
- Drift danych ↔ Data quality ↔ Retraining.  
- Governance ↔ Komunikacja zmian ↔ Użytkownicy/klienci.


## Struktura sekcji

1) Definicje degradacji i metryki  
2) Monitorowanie (online/batch) i alerty  
3) Analiza przyczyn (RCA) i dane pomocnicze  
4) Reakcje: rollback, retraining, A/B/shadow  
5) Walidacja i release  
6) Komunikacja i governance  
7) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Lista metryk z progami (statystyki cech, PSI/KS, metryki modelu, KPI biznesowe).  
- Procedura RCA (dane, etykiety, system, zależności).  
- Runbook dla rollbacku i aktywacji poprzedniej wersji.  
- Plan retrainingu (dane, częstotliwość, feature store).  
- Scenariusze eksperymentów (A/B, shadow, canary).  
- Polityka komunikacji zmian do interesariuszy.


## Wymagane streszczenia

- Executive summary: status modeli, alerty aktywne, plan reakcji.  
- Skrót metryk i trendów (ostatnie 7/30 dni).


## Guidance (skrót)

- Miej baseline i progi przed wejściem na produkcję.  
- Oddziel metryki danych, modelu i biznesowe; alertuj wielopoziomowo.  
- Używaj statystyk stabilności (PSI/KS) i monitoruj missing/outliers.  
- Preferuj bezpieczny rollback lub shadow przed pełnym rolloutem.  
- Dokumentuj decyzje w ADR i w model registry.  
- Weryfikuj wpływ na użytkowników; komunikuj zmiany właścicielom produktu.


## Checklisty Definition of Ready (DoR)

- [ ] Baseline metryk modelu i danych zapisany.  
- [ ] Progi i alerty skonfigurowane (PSI/KS/KPI).  
- [ ] Dostęp do feature store/logów predykcji zapewniony.  
- [ ] Plan rollback i retrainingu uzgodniony.  
- [ ] Środowisko testowe/A/B dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Degradacja zdiagnozowana; decyzja i działania wykonane.  
- [ ] Model/wersja danych zaktualizowana lub zrollbackowana.  
- [ ] Metryki po reakcji w akceptowalnych progach.  
- [ ] Dokumentacja/ADR, registry i linkage_index zaktualizowane.  
- [ ] Post‑mortem zapisane; progi/monitoring dostrojone.

