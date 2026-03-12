---
title: Model Selection Strategy
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Selection Strategy


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić zasady wyboru modeli ML dla danego problemu: kryteria, ograniczenia, koszty i proces decyzyjny, aby zapewnić właściwy balans jakości, złożoności, interpretowalności i operacyjności.


## Zakres i granice

- Obejmuje: kryteria jakości (metryki), koszty (inference/training), interpretowalność/zgodność, wymagania danych, latency/SLA, skalowanie, ryzyka bias/fairness, dojrzałość zespołu/narzędzi, decyzje build vs buy vs fine-tune, proces POC → produkcja, dokumentowanie ADR.  
- Poza zakresem: szczegółowa implementacja i trening (osobne dokumenty), labeling pipeline.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: problem biznesowy, dane i ich jakość, ograniczenia latency/koszt, wymagania regulatora/klienta, baseline modele, doświadczenie zespołu.  
- Wyjścia: rekomendacja modelu/rodziny, tabela kryteriów z wagami, decyzja ADR, plan POC i ewaluacji, checklisty DoR/DoD, wymagania operacyjne (monitoring, retraining).


## Założenia

- Dostępne dane i narzędzia do benchmarku.  
- Zespół może utrzymać wybrany model.  
- SLA/latency są mierzalne i negocjowalne.


## Otwarte pytania

- Jak często aktualizować tabelę kryteriów?  
- Jak mierzyć TCO modelu w czasie?  
- Czy potrzebne są certyfikacje/regulacyjne approval?

## Powiązania (meta)

- Key Documents: predictive_model_degradation, model_tracking_metrics, bias_fairness_policy, data_quality_playbook, monitoring_strategy_document, rollback_runbook.  
- Key Document Structures: kryteria, kandydaci, ewaluacja, decyzje, operacje.  
- Document Dependencies: feature store, model registry, eval pipelines, cost calculators.


## Zależności dokumentu

Wymaga: jasno zdefiniowanego problemu i metryk sukcesu, danych/baseline, ograniczeń latency/koszt, wymagań compliance, narzędzi ewaluacji. Brak = brak DoR.


## Fazy cyklu życia

- Definicja problemu i kryteriów.  
- Lista kandydatów i plan ewaluacji.  
- POC/benchmark i analiza trade-off.  
- Decyzja ADR i plan wdrożenia.  
- Retrospektywa i aktualizacje strategii.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (model/selection/strategy)  
- model_tracking_metrics, bias_fairness_policy, predictive_model_degradation


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

1. Zdefiniuj problem, metryki i ograniczenia.  
2. Przygotuj listę kandydatów; zaplanuj benchmark.  
3. Przeprowadź ewaluację; wypełnij tabelę scoringu.  
4. Sporządź ADR z rekomendacją; uzgodnij rollout/operacje.  
5. Aktualizuj dokument i linkage_index po wdrożeniu.


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

- ADR: Architecture Decision Record.  
- Build vs buy: własny model vs usługa/pretrained.  
- Trade-off: kompromis pomiędzy metrykami/kosztem/latency/interpretowalnością.


## Przykłady użycia

- Wybór modelu rekomendacji (matrix factorization vs deep learning).  
- Decyzja LLM: własny fine-tune vs API dostawcy.  
- Model scoringu kredytowego: drzewo vs gradient boosting vs GLM.


## Ryzyka i ograniczenia

- Przeszacowanie jakości bez uwzględnienia kosztu/latency.  
- Bias/fairness → ryzyko regulacyjne.  
- Vendor lock-in w usługach API.  
- Brak planu operacji → szybka degradacja w produkcji.


## Decyzje i uzasadnienia

- Wagi kryteriów; próg akceptacji.  
- Wybór modelu i dostawcy.  
- Zakres interpretowalności vs dokładność.  
- Budżet na infra i inference.


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

- Kryteria ↔ Ewaluacja ↔ Decyzje ADR.  
- Koszt/latency ↔ Operacje ↔ SLA.  
- Fairness/bias ↔ Compliance ↔ Monitoring.


## Struktura sekcji

1) Problem i metryki sukcesu  
2) Kryteria (jakość, koszt, latency, interpretowalność, zgodność) z wagami  
3) Kandydaci (algorytmy/pretrained/fine-tune/build vs buy)  
4) Plan ewaluacji i dane  
5) Wyniki i trade-offy  
6) Decyzja ADR i plan POC/produkcyjny  
7) Operacje: monitoring, retraining, rollback  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Tabela kryteriów z wagami i scoringiem.  
- Plan benchmarku (dane, metryki, hardware).  
- Kosztorys inference/training i latency profile.  
- Analiza interpretowalności i wymagań compliance.  
- ADR z uzasadnieniem i planem rollout/rollback.  
- Lista ryzyk (bias, drift, vendor lock-in).


## Wymagane streszczenia

- Executive summary: rekomendacja i główne trade-offy.  
- Skrót wyników benchmarku i kosztów.


## Guidance (skrót)

- Zacznij od prostych modeli; zwiększ złożoność gdy potrzebne.  
- Ustal wagi kryteriów z interesariuszami.  
- Uwzględnij koszt i latency w równym stopniu co metryki jakości.  
- Sprawdzaj bias/fairness; dokumentuj decyzje w ADR.  
- Planuj operacje (monitoring/retrain/rollback) już przy wyborze.  
- Aktualizuj strategię po każdym większym projekcie.


## Checklisty Definition of Ready (DoR)

- [ ] Problem i metryki sukcesu zdefiniowane.  
- [ ] Dane i baseline dostępne.  
- [ ] Ograniczenia latency/koszt znane.  
- [ ] Kryteria i wagi uzgodnione.  
- [ ] Plan benchmarku przygotowany.


## Checklisty Definition of Done (DoD)

- [ ] Benchmark wykonany; tabela scoringu uzupełniona.  
- [ ] ADR z decyzją i uzasadnieniem opublikowany.  
- [ ] Plan operacyjny (monitoring/retrain/rollback) gotowy.  
- [ ] linkage_index zaktualizowany.  
- [ ] Ryzyka/otwarte pytania adresowane lub zapisane.

