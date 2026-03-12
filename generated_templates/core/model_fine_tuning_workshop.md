---
title: Model Fine-Tuning Workshop
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Fine-Tuning Workshop


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan warsztatu z fine-tuningu modeli (LLM/CV/NLP/tabular): dane, metryki, hyperparametry, MLOps i bezpieczeństwo. Ma uczyć praktyk i dostarczyć działające artefakty.


## Zakres i granice

- Obejmuje: wybór bazowego modelu, dane i PII, przygotowanie datasetu (train/val/test), augmentacje, metryki, hyperparam search, regularyzację, ewaluację (offline/online), bezpieczeństwo (toxic/hallucinations, PII), deployment (registry, serving), monitoring i rollback, dokumentację (model card).  
- Poza zakresem: od podstawowego treningu modeli.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: cel biznesowy/KPI, dane i licencje, ograniczenia PII/IP, hardware/budżet, baseline model, metryki, narzędzia MLOps, polityki bezpieczeństwa.  
- Wyjścia: repo z kodem/notebookiem, skonfigurowany pipeline fine-tune, wyniki metryk, model card, checklisty DoR/DoD, rekomendacje i następne kroki.


## Założenia

- Dostęp do GPU/compute i danych.  
- Zespół zna podstawy ML i narzędzia.  
- Polityki bezpieczeństwa/fairness stosowane.


## Otwarte pytania

- Jak często retrain/fine-tune?  
- Czy wymagane audyty zewnętrzne dla modelu?  
- Jakie limity kosztu per eksperyment?


## Powiązania (meta)

- Key Documents: model_development_best_practices, analysis_validation_plan, test_set_evaluation, bias_and_fairness_policy, mlops_strategy_document, security_requirements.  
- Key Document Structures: dane, metryki, hyperparam, ewaluacja, bezpieczeństwo, deployment.  
- Document Dependencies: data platform, compute/GPU, experiment tracker, CI/CD, registry/serving, monitoring, safety filters.


## Zależności dokumentu

Wymaga: zdefiniowanych KPI/metryk, dostępu do danych (bez PII lub z maskowaniem), bazowego modelu/licencji, zasobów GPU/budżetu, narzędzi trackingu/CI/CD, polityk safety/fairness. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie danych i celów.  
- Fine-tuning/eksperymenty.  
- Ewaluacja i bezpieczeństwo.  
- Deployment i monitoring.  
- Retro i następne iteracje.



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

- linkage_index.jsonl (model/fine_tuning/workshop)  
- model_development_best_practices, test_set_evaluation, mlops_strategy_document, bias_and_fairness_policy


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

1. Ustal KPI/dane i bezpieczeństwo; przygotuj pipeline.  
2. Przeprowadź eksperymenty; zapisuj wyniki; wybierz model.  
3. Przygotuj model card, rollout/rollback, monitoring; uzupełnij DoR/DoD i linkage_index.


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

- LoRA: Low-Rank Adaptation.  
- Baseline: model referencyjny do porównań.  
- Drift: zmiana jakości po czasie/danych.


## Przykłady użycia

- Fine-tuning LLM na danych domenowych.  
- Dostosowanie modelu CV do nowych klas.  
- Warsztat zespołowy dla nowego produktu ML.


## Ryzyka i ograniczenia

- Koszty GPU, brak reprodukowalności, wycieki danych.  
- Halucynacje/toxic output.  
- Bias przy brakach danych.


## Decyzje i uzasadnienia

- Wybór bazowego modelu/licencji.  
- Kryteria go/no-go po ewaluacji.  
- Zakres monitoringu i refresh cyklu.


## Powiązania z innymi dokumentami

- mlops_strategy_document — pipeline i governance.  
- bias_and_fairness_policy — testy fairness.  
- monitoring_strategy_document — monitorowanie.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Polityki danych/PII/fairness, licencje modelu.  
- Wytyczne bezpieczeństwa/AI.

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

- Dane → Metryki → Hyperparam → Ewaluacja → Deployment.  
- Safety/fairness → Filtry → Monitorowanie.  
- Wyniki → Model card → Decyzje go/conditional/no-go.


## Struktura sekcji

1) Cel i KPI, baseline model  
2) Dane/licencje/PII (źródła, czyszczenie, podziały, augmentacje)  
3) Metryki i walidacja (offline, safety, bias)  
4) Hyperparametry i eksperymenty (search space, tracking)  
5) Wyniki i porównania (baseline vs tuned)  
6) Bezpieczeństwo/safety (toxic, hallucinations, leakage)  
7) Deployment i MLOps (registry, serving, rollout/rollback)  
8) Monitoring i drift (performance/safety)  
9) Dokumentacja (model card, dataset card)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Plan danych (etykiety, filtry, PII maskowanie).  
- Space hyperparam i liczba prób; budżet GPU.  
- Testy safety/bias i kryteria.  
- Plan rollout/rollback i monitoring.


## Wymagane streszczenia

- Executive snapshot: metryki vs baseline, koszty, ryzyka safety.  
- Karta model card (wersja, dane, metryki, ograniczenia).


## Guidance (skrót)

- Zacznij od małych prób i reprodukowalności (seed).  
- Mierz safety/bias, nie tylko metryki dokładności.  
- Kontroluj koszt (batch size, quantization, LoRA).  
- Używaj registry i CI/CD; włącz monitorowanie po deployu.  
- Dokumentuj dane/wersje/eksperymenty.


## Checklisty Definition of Ready (DoR)

- [ ] KPI/metryki i baseline znane.  
- [ ] Dane gotowe (PII maskowane); licencje/budżet ustalone.  
- [ ] Narzędzia trackingu/CI/CD/registry dostępne.  
- [ ] Kryteria safety/bias i testy ustalone.  
- [ ] Plan GPU/budżetu i harmonogram uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Fine-tuning wykonany; wyniki/eksperymenty zapisane; status/wersja/data uzupełnione.  
- [ ] Safety/bias testy zaliczone lub wyjątki opisane.  
- [ ] Model w registry; rollout/rollback i monitoring ustawione.  
- [ ] Model card/dataset card opublikowane; linkage_index zaktualizowany.  
- [ ] Lessons learned i kolejne kroki zapisane.

