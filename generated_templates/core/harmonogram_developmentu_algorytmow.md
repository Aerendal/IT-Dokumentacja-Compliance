---
title: Harmonogram developmentu algorytmów
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram developmentu algorytmów


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan prac nad algorytmami/ML (EDA → baseline → eksperymenty → optymalizacja → walidacja → deploy): etapy, zadania, zasoby, kryteria sukcesu, decyzje go/conditional/no‑go, ryzyka i raportowanie.


## Zakres i granice

- Obejmuje: etapy R&D, backlog eksperymentów, dane i compute (GPU/QPU), metryki/thresholdy, walidację/offline+online, deploy/monitoring, dokumentację i decyzje.  
- Poza zakresem: szczegółowe opisy modeli/kodu (repo), polityki danych (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: problem statement, dane/DFD, wymagania jakości (metryki), budżet compute, narzędzia MLOps, ograniczenia regulacyjne/etyczne.  
- Wyjścia: harmonogram i kamienie, backlog eksperymentów z priorytetem, metryki i progi, decyzje go/conditional/no‑go, raporty walidacji, plan deploy/monitoring.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: ml_project_plan, data_requirements, model_card, experimentation_log, mlops_pipeline, deployment_schedule, monitoring_strategy_document, risk_register, ethics_and_fairness_guidelines.
- Key Document Structures: etapy, zadania, metryki, eksperymenty, decyzje, ryzyka.
- Document Dependencies: dane (źródła, wersje), compute (GPU/QPU), feature store, pipeline CI/CD, monitoring/telemetria, A/B infra, ticketing.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (ml/algorithm_schedule)
- ml_project_plan, data_requirements, model_card, experimentation_log, mlops_pipeline, deployment_schedule, monitoring_strategy_document, risk_register, ethics_and_fairness_guidelines


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Ustal etapy/kamienie, backlog eksperymentów i zasoby.  
2. Zdefiniuj metryki/progi, plan walidacji i rollout/monitoring.  
3. Aktualizuj po każdym etapie/eksperymencie; dokumentuj decyzje; utrzymuj linkage_index.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

- [ ] Etapy/kamienie spójne z backlogiem i zasobami; metryki i progi zdefiniowane.  
- [ ] Wyniki poparte dowodami; decyzje/go-no-go udokumentowane.  
- [ ] Rollout/monitoring/drift opisane; relacje cross‑doc wpisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Experiment log, model card, raporty walidacji, pipeline CI/CD config, A/B dashboards, drift/fairness raporty, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Czas od EDA do deploy, spełnienie progów metryk, liczba iteracji eksperymentów, koszt compute vs budżet, drift/fairness alerty po deploy, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Plan zrealizowany lub decyzja stop z uzasadnieniem; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Etapy i kamienie (EDA, baseline, eksperymenty, tuning, walidacja, deploy) z datami/ownerami  
2) Backlog eksperymentów (hipotezy, priorytet, metryki, ETA)  
3) Zasoby: dane (wersje, privacy), compute (GPU/QPU), narzędzia MLOps, budżet  
4) Metryki i kryteria sukcesu (offline/online, guardrails)  
5) Plan walidacji i testów (cross‑val, holdout, fairness/robustness, perf)  
6) Decyzje go/conditional/no‑go i punkty przeglądowe  
7) Deploy i monitoring (rollout, A/B, canary, alerty, drift, retrain triggers)  
8) Ryzyka i mitigacje (dane, drift, koszt, etyka, zależności)  
9) Raportowanie i komunikacja (cadence, odbiorcy, szablony)  
10) Załączniki (experiment log, model card, raporty walidacji, dashboardy)


## Wymagane rozwinięcia

- Kamienie milowe z datami; przypisanie ownerów.  
- Metryki (np. accuracy/F1/AUC/latency/cost) i progi; guardrails fairness/robustness.  
- Plan danych (wersje, privacy/maskowanie), compute budżet i limity.  
- Scenariusze walidacji (offline/online), rollout i monitoring (drift/alerty).


## Wymagane streszczenia

- Executive: status etapów, top eksperymenty i wyniki vs progi, decyzje go/conditional/no‑go, ryzyka/koszt/ETA deploy.


## Guidance (skrót)

- Zamrażaj dane/seed dla powtarzalności; loguj eksperymenty.  
- Ustal metryki główne i guardrails przed eksperymentami; unikaj p‑hacking.  
- Waliduj fairness/robustness; planuj online rollout z monitoringiem driftu.  
- Decyzje go/conditional/no‑go dokumentuj z uzasadnieniem i dowodami.


## Checklisty Definition of Ready (DoR)

- [ ] Problem statement, dane i metryki wstępne zebrane; zasoby compute dostępne.  
- [ ] Backlog eksperymentów i etapy zarysowane; struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Etapy zrealizowane; eksperymenty i wyniki zlogowane; decyzje go/conditional/no‑go zapisane.  
- [ ] Plan deploy/monitoring/drift gotowy; dokument w linkage_index; metadane aktualne.

