---
title: Model Retraining Procedure
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Retraining Procedure


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Opisać procedurę ponownego trenowania modeli ML: dane, pipeline, kryteria startu/stopu, walidacja, bezpieczeństwo i wdrożenie.


## Zakres i granice

- Obejmuje: trigger retrain (drift/performance), przygotowanie danych (freshness/quality/PII), pipeline treningowy, walidację/benchmarki, kontrolę wersji artefaktów, bezpieczeństwo i governance, rollout (shadow/A-B/canary), monitoring po wdrożeniu.
- Poza zakresem: projekt architektury MLOps (opisany w arch docs) i definicja funkcji/feature store (osobne dokumenty).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia
- Wejścia: definicja triggera/scenariusza, wymagane uprawnienia/narzędzia, dane wejściowe, RACI i kontakty.
- Wyjścia: wykonane kroki z timestamp, dowody/artefakty, status (sukces/niepowodzenie), decyzje i eskalacje.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie runbooka: wersja, właściciel, testowane ścieżki.
- Egzekucja: krokowo z dowodami.
- Postmortem: usprawnienia runbooka i monitoringu.
## Struktura sekcji (szkielet)

- Trigger i kryteria retraining
- Dane i przygotowanie (jakość, PII, sampling)
- Pipeline treningowy i hyperparametry
- Walidacja/benchmark (offline) i kryteria akceptacji
- Kontrola wersji artefaktów i reproducibility
- Rollout (shadow/A-B/canary) i monitoring po wdrożeniu
- Bezpieczeństwo, PII i compliance
- Action log i harmonogram


## Szybkie powiązania
- model-update-procedure
- model-retraining-pipeline
- language-model-update-procedure
- vm-provisioning-procedure
- vm-migration-procedure

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

- Zdefiniuj trigger i kryteria, przygotuj dane/pipeline, opisz walidację i rollout; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Po retrain podlinkuj artefakty/raporty, zaktualizuj monitoring i action log.


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

## Wejścia

- Dane treningowe/feature store, sygnały driftu/perf, metryki SLA/KPI modelu.
- Pipeline/CI-CD, narzędzia eksperymentów, polityki danych/PII.
- Wersje modeli, konfiguracje hyperparametrów.


## Wyjścia

- Nowy artefakt modelu z wersją i metadanymi.
- Raport walidacji/benchmarku i decyzja deploy/rollback.
- Plan rollout/monitoringu i action log.



## Szybkie powiązania (uzupełnij)

- mlops_security_architecture.md
- data_security_architecture.md
- performance_testing_plan.md
- logging_and_audit_trail.md
- system_monitoring_strategy.md
- risk_management_framework.md


## Wymagane rozwinięcia / streszczenia

- Tabela runów: data → dane → parametry → metryki → decyzja.
- Streszczenie ryzyk (drift, PII, model theft) i mitigacji.


## Wymagane powiązania

- Dane/feature store, polityki PII, CI/CD, monitoring modelu, kontrola wersji artefaktów.


## Kryteria DoR

- [ ] Trigger i metryki zdefiniowane; dane dostępne.
- [ ] Pipeline/środowisko gotowe; polityki PII uzgodnione.
- [ ] Kryteria akceptacji i rollout uzgodnione.


## Kryteria DoD

- [ ] Run/artefakt z walidacją i decyzją udokumentowany.
- [ ] Rollout/monitoring zaktualizowane; action log wpisany.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Artefakt modelu (wersja, checksum), raport walidacji/benchmark.
- Konfiguracje pipeline/hyperparametrów.
- Plan rollout/monitoringu.


## Walidacja / testy

- Reprodukcja runu; sanity metryk/overfitting/bias.
- Bezpieczeństwo: sprawdzenie PII w danych, model extraction/poisoning checks.


## Metryki monitorowane

- Metryki jakości (offline/online), drift (data/model), czas retrain.
- Incydenty PII, anomalie inferencji, koszt inferencji po retrain.


## Utrzymanie i aktualizacje

- Przegląd po każdym retrain i cyklicznie (np. miesięcznie); aktualizuj progi/trigger.
- Synchronizuj z roadmapą modeli i zmianami danych.


## Zakończenie

Po spełnieniu DoD opublikuj dokument/run, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i poinformuj właścicieli modeli.
