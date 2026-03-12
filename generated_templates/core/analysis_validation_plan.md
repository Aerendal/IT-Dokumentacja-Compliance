---
title: Analysis Validation Plan
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Analysis Validation Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan walidacji analizy/analityki/modelu: poprawność danych, metod, kodu i wniosków. Ma ograniczyć błędy, bias i fałszywe decyzje biznesowe.


## Zakres i granice

- Obejmuje: weryfikację danych (źródła, kompletność, PII), metodologię (założenia, testy statystyczne), kod/replikowalność, walidację wyników (sanity checks, backtesting), metryki sukcesu, niezależny przegląd, raportowanie i ścieżkę akceptacji.  
- Poza zakresem: pełny opis analizy (osobny dokument), implementacja produkcyjna modelu.


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: opis analizy/KPI, specyfikacja danych, modele/metody, kod/notebooki, założenia, ryzyka, wymagania compliance.  
- Wyjścia: plan testów i walidacji, checklisty, wyniki walidacji (pass/fail/exception), rekomendacje i decyzja go/conditional/no-go, aktualizacje repo/kodu.


## Założenia

- Dane są dostępne i zgodne z privacy.  
- Narzędzia testowe/CI są dostępne.  
- Zespół ma kompetencje statystyczne.


## Otwarte pytania

- Czy potrzebny dodatkowy audyt (np. compliance)?  
- Jak często powtarzać walidację dla żywych analiz/modeli?  
- Jak przechowywać/archiwizować artefakty walidacji?


## Powiązania (meta)

- Key Documents: data_requirements_for_analysis, metric_definitions, data_quality_playbook, model_validation_guidelines, code_review_checklist, privacy_and_pii_handling.  
- Key Document Structures: dane, metodologia, kod, testy, wyniki, akceptacja.  
- Document Dependencies: repo kodu, dane/ekstrakty, DQ narzędzia, CI/CD, monitoring modeli (jeśli dotyczy).


## Zależności dokumentu

Wymaga: zdefiniowanych KPI/pytań, specyfikacji danych, dostępu do danych i kodu, standardów walidacji i ról reviewerów. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie planu walidacji.  
- Wykonanie testów/walidacji.  
- Raport i akceptacja.  
- Retrospektywa i aktualizacje standardów.



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (analysis/validation/plan)  
- data_requirements_for_analysis, data_quality_playbook, model_validation_guidelines, code_review_checklist


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

1. Ustal KPI/zakres, dane i metody; przygotuj checklisty.  
2. Wykonaj testy/walidacje; zapisz wyniki i rekomendacje.  
3. Komunikuj wyniki, podejmij decyzję; zaktualizuj DoR/DoD i linkage_index.


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

- Sanity check: proste testy wykrywające oczywiste błędy danych/wyników.  
- Backtest: testowanie modelu na danych historycznych z symulacją.  
- Conditional go: akceptacja z warunkami/mitigacjami.


## Przykłady użycia

- Walidacja analizy wpływu ceny na konwersję.  
- Backtest modelu scoringowego.  
- Re-run analizy po aktualizacji danych źródłowych.


## Ryzyka i ograniczenia

- Bias danych → błędne wnioski.  
- Brak replikowalności → brak zaufania.  
- Niejasne progi → spory decyzyjne.


## Decyzje i uzasadnienia

- Progi istotności/efektu.  
- Zakres testów DQ/sanity vs czas.  
- Kiedy wymagany niezależny reviewer.


## Powiązania z innymi dokumentami

- model_validation_guidelines — standard walidacji modeli.  
- code_review_checklist — przegląd kodu.  
- data_quality_playbook — testy DQ.


## Powiązania z sekcjami innych dokumentów
- Monitoring → alerty/timeline; DR/BCP → reakcja; Change → przyczyny; Risk Register → wpisy; Lessons Learned → baza wiedzy.
## Słownik pojęć w dokumencie
- MTTR, SLA/SLO, Root Cause, Contributing Factors, CAPA, Waiver, Sunset, Blameless.
## Wymagane odwołania do standardów

- Polityki danych/PII, standardy analityczne firmy.  
- Wymogi regulatorów, jeśli dotyczy (np. fin/health).

## Mapa relacji sekcja→sekcja
- Timeline → Wpływ → Root cause → CAPA → Usprawnienia → Follow‑up.
## Mapa relacji dokument→dokument
- Postmortem → Incident Response/DR/BCP/Monitoring/Change/Risk → Lessons Learned.
## Ścieżki informacji
- Alert/logi → Timeline → Analiza → CAPA → Retest → Aktualizacja dokumentacji.
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
- Logi/metryki/trace, change log, komunikacja (status/update), runbooki, ticket CAPA, wykresy, lesson learned register.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Czas dostarczenia postmortem, % CAPA zamkniętych w terminie, recydywa podobnych incydentów, jakość danych (logi/metryki) w raporcie, liczba waiverów i czas ich zamknięcia.
## Kryteria ukończenia
- [ ] Raport ukończony, CAPA/waivery z planem i dowodami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Dane → Metody → Kod → Testy → Decyzja.  
- Założenia/bias → Walidacja → Rekomendacje.  
- Wyniki → Raport/komunikacja → Akceptacja.


## Struktura sekcji

1) Cel/KPI i zakres analizy  
2) Dane i założenia (źródła, jakość, PII, bias)  
3) Metody i modele (założenia, alternatywy)  
4) Kod i replikowalność (repo, seed, environment)  
5) Testy i walidacje (DQ, sanity, stat, backtest/A-B)  
6) Metryki sukcesu i progi (stat. istotność, efekt)  
7) Wyniki walidacji i rekomendacje (go/conditional/no-go)  
8) Raportowanie i komunikacja (artefakty, notebook, slide)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklista DQ i sanity per dataset.  
- Lista testów statystycznych/backtestów z progami.  
- Instrukcja replikacji (env, seed, dane).  
- Template raportu walidacyjnego.


## Wymagane streszczenia

- Executive summary: wyniki walidacji, ryzyka, rekomendacja.  
- Krótka karta „what changed” przy re-runie.


## Guidance (skrót)

- Waliduj dane zanim ocenisz model; sprawdzaj założenia metod.  
- Wymagaj replikowalności (seed/env) i peer review.  
- Dokumentuj wyjątki i kompensacje przy „conditional go”.  
- Mapuj ryzyka/bias do decyzji i komunikacji z biznesem.  
- Aktualizuj plan po zmianach danych/metod.


## Checklisty Definition of Ready (DoR)

- [ ] KPI/pytania i dane zdefiniowane; PII/bias ocenione.  
- [ ] Kod/notebook dostępny i w repo; environment opisany.  
- [ ] Testy/walidacje i progi ustalone; role reviewerów przypisane.  
- [ ] Artefakty raportowe zdefiniowane (format).  
- [ ] Narzędzia DQ/testowe dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Testy/walidacje wykonane; wyniki zapisane; status/wersja/data uzupełnione.  
- [ ] Rekomendacja go/conditional/no-go udokumentowana; wyjątki opisane.  
- [ ] Replikowalność potwierdzona (seed/env); artefakty w repo.  
- [ ] Komunikacja do interesariuszy wykonana; linkage_index zaktualizowany.  
- [ ] Ryzyka/bias i działania korygujące zapisane.

