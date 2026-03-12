---
title: A/B Testing Guide
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# A/B Testing Guide


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przewodnik po prowadzeniu testów A/B end-to-end (planowanie, wykonanie, analiza, decyzje).


## Zakres i granice

- Obejmuje: lifecycle eksperymentu, role, dane/telemetria, monitoring anomalii, analiza, dokumentacja wyników.
- Poza zakresem: kod feature flag/experiment SDK.


## Użytkownicy i interesariusze
- QA, PM/Release, Dev, Security/Perf, Product/Business.
## Wejścia i wyjścia
- Wejścia: wymagania, ryzyka, user stories/epiki, architektura, dane testowe, środowiska, SLA/SLO, plan release, dostępność zespołu, polityki bezpieczeństwa/zgodności.
- Wyjścia: kalendarz runów, przypisania ról, matryca pokrycia, plan danych, kryteria go/conditional/no‑go, raporty cyklu, lista ryzyk i blokad.
## Założenia
- Dostępne są środowiska, dane i narzędzia testowe; zespoły mają czas na runy.
## Otwarte pytania
- Jakie dodatkowe testy wymagane przez regulatorów/klientów?  
- Czy potrzebne testy prod-shadow / canary?
## Powiązania (meta)
- Key Documents: qa_strategy, test_data_preparation, release_plan, risk_management_plan, change_management, security_testing_plan, performance_testing_plan.
- Key Document Structures: zakres, zasoby, harmonogram, kryteria, raporty.
- Document Dependencies: CI/CD, środowiska, dane testowe, feature flags, monitoring/observability.
## Zależności dokumentu
Wymaga listy wymagań/historii, ryzyk, dostępnych środowisk, danych testowych, kalendarza release, zasobów QA/dev/sec/perf oraz kryteriów jakości. Bez tego DoR pozostaje otwarte.
## Fazy cyklu życia
- Planowanie: zakres, ryzyka, zasoby, harmonogram, dane, środowiska.
- Przygotowanie: test suites, dane, środowiska, narzędzia, kryteria go/conditional/no‑go.
- Wykonanie: runy (CI/CD, manual), raporty, defekty, retesty/regresja.
- Ocena: spełnienie kryteriów go/conditional/no‑go, decyzja release.
- Zamknięcie: retrospektywa, metryki, lekcje.
## Struktura sekcji (szkielet)

- Kontekst i role
- Planowanie
- Wykonanie/monitoring
- Analiza/statystyka
- Decyzje i komunikacja
- Archiwizacja/lessons
- Ryzyka


## Szybkie powiązania
- vr-sickness-testing
- vm-performance-testing
- visualization-testing
- usability-testing
- tuning-guide

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.


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
- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria.
## Przykłady użycia
- Release: smoke → regression → perf → security smoke → UAT; decyzja go/conditional/no‑go na podstawie kryteriów.  
- Hotfix: skrócony plan (smoke + targeted regression) z klarownym go/conditional/no‑go.
## Ryzyka i ograniczenia
- Brak gotowości środowisk/danych → poślizgi; niejasne kryteria go/conditional/no‑go → spory; flakiness maskuje defekty.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- QA Strategy, Test Data Preparation, Release Plan, Risk Mgmt Plan, Change Mgmt, Security/Perf Testing Plans.
## Powiązania z sekcjami innych dokumentów
- Test Data → dane/środowiska; Release Plan → harmonogram/go-no-go; Risk → priorytety.
## Słownik pojęć w dokumencie
- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria, Regression, Smoke.
## Wymagane odwołania do standardów
- Polityki QA, bezpieczeństwa i wydajności; wymagania klienta/regulatora jeśli dotyczy.
## Mapa relacji sekcja→sekcja
- Zakres/Ryzyka → Typy testów → Harmonogram → Runy → Raporty → Decyzje → Retro.
## Mapa relacji dokument→dokument
- Testing Plan → QA/Release/Risk → Change/Incident → Lessons Learned.
## Ścieżki informacji
- Wymagania/ryzyka → Plan → Runy → Raporty → Decyzje → Retro → Aktualizacja planu.
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
- Harmonogram runów, raporty runów, metryki, defekt log, decyzje go/conditional/no‑go, retrospektywa.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- QA/PM → Security/Perf (jeśli dotyczy) → Product/Business → Release/CAB.
## Metryki jakości
- Pass rate, Defect leakage, Flake rate, Czas cyklu testów, MTTR defektów w cyklu, dotrzymanie harmonogramu.
## Kryteria ukończenia
- [ ] Plan wykonany; decyzje i raporty zapisane; retrospektywa z lekcjami.  
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.
## Wejścia

- Framework A/B
- Hipotezy i cele
- Metryki/MDE
- Narzędzia eksperymentów/telemetrii


## Wyjścia

- Przewodnik krok-po-kroku
- Checklisty DoR/DoD
- Szablony komunikacji/raportu
- Powiązania do narzędzi



## Szybkie powiązania (uzupełnij)

- [ ] a_b_testing_framework.md
- [ ] a_b_testing_plan.md
- [ ] experiment_results_documentation.md
- [ ] statistical_significance_testing.md
- [ ] api_usage_report.md
- [ ] api_monitoring_strategy.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych decyzji/ryzyk; rozwinięcia testów/polityk/macierzy.


## Wymagane powiązania

- Dokumenty security/access control/logging/testy; runbooki incydentów; compliance.


## Kryteria DoR

- [ ] Wymagania/cel zebrane
- [ ] Owner dokumentu przypisany
- [ ] Narzędzia/środowiska dostępne
- [ ] Ryzyka wstępne zidentyfikowane


## Kryteria DoD

- [ ] Sekcje wypełnione lub N/A z uzasadnieniem
- [ ] Quick-links/checklisty dodane
- [ ] Artefakty wskazane
- [ ] Metadane/DoR/DoD zaktualizowane


## Artefakty do załączenia

- Plan/ramy dokumentu
- Checklisty
- Przykłady lub macierze
- Linki do narzędzi


## Walidacja / testy

- Sanity/negative/abuse scenariusze; weryfikacja logów/alertów jeśli dotyczy.


## Metryki monitorowane

- Czas przygotowania dokumentu
- Pokrycie sekcji (%)
- Liczba otwartych TODO
- Incydenty/regresje związane z tematem


## Utrzymanie i aktualizacje

- Przegląd co release lub kwartalnie; aktualizacja quick-links/checklist/macierzy.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
