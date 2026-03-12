---
title: dbt Test Specification
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# dbt Test Specification


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Specyfikacja testów dbt (schema/data), aby zapewnić spójność, integralność i świeżość modeli w hurtowni oraz jasne raportowanie jakości.


## Zakres i granice

- Obejmuje: scope modeli/warstw, minimalny zestaw testów (not null, unique, relationships, accepted_values), testy data (anomaly, thresholds), custom tests/macro, seedy i dane wzorcowe, harmonogram/częstotliwość, raportowanie i alerty, kryteria blokowania deployu.  
- Poza zakresem: monitoring produkcyjny poza dbt (osobny runbook), polityki danych wrażliwych (design_abac).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe i SLA danych, klasyfikacja PII, model lineage, volumetria i sezonowość, definicje jakości (accuracy, completeness, timeliness), zasady kosztowe.  
- Wyjścia: katalog testów per model/kolumna, seedy referencyjne, konfiguracja harmonogramu/test selectors, zasady alertów/thresholds, raporty jakości, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: dbt_model_design, data_quality_policy, lineage_strategy, monitoring_strategy, ci_cd_pipeline, design_abac.  
- Key Document Structures: zakres modeli, testy schema/data, seedy, raporty/alerty, cykliczność, blokery release.  
- Document Dependencies: warehouse limits, CI/CD runner, selectors/state artifacts, freshness sources, incident process.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Elicytacja i warsztaty.
- Konsolidacja i priorytetyzacja.
- Walidacja z interesariuszami (biznes/arch/security/legal).
- Traceability do backlogu/testów.
## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (data/dbt_test_specification)  
- dbt_model_design, data_quality_policy, ci_cd_pipeline, monitoring_strategy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
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

1. Skataloguj modele i krytyczność; przypisz minimalne testy i progi.  
2. Zdefiniuj selectors/harmonogram; dodaj raporty/alerty do CI i kanałów zespołu.  
3. Uzupełnij linkage_index i checklisty; utrzymuj waivery i ADR przy zmianach.


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

- [ ] Krytyczne modele mają komplet minimalnych testów; progi/thresholds są zdefiniowane.  
- [ ] Harmonogram i selectors odzwierciedlają SLA; alerty trafiają do ownerów.  
- [ ] Waivery są tymczasowe, datowane, z planem usunięcia.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- schema.yml z testami, pliki custom tests/macro, seedy i ich testy, selectors.yml, raporty/alerty, waiver log, ADR.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie testami (% modeli/kolumn), liczba blokujących defektów, MTTR dla test failures, koszt testów, odsetek waiverów wygasłych/usuniętych, zgodność ze SLA jakości.

## Kryteria ukończenia

- [ ] Specyfikacja testów pozwala utrzymać jakość danych (pokrycie, progi, raporty) i jest powiązana w linkage_index.


## Struktura sekcji

1) Zakres modeli i priorytety (warstwa, krytyczność, SLA)  
2) Testy schema (unique, not null, relationships, accepted_values, contracts)  
3) Testy data/analityczne (thresholds, anomaly detection, distribution, freshness)  
4) Custom tests i makra (wspólne biblioteki, re‑use, performance)  
5) Seedy i dane referencyjne (źródła, aktualizacja, kontrola wersji)  
6) Harmonogram i selektory (state:modified+, tags, krytyczne vs pełne przebiegi)  
7) Raportowanie i alerty (CI/CD, Slack/Email, blokery, SLO jakości)  
8) Załączniki (lista testów per model, waiver log, ADR)


## Wymagane rozwinięcia

- Matryca minimalnych testów per warstwa/krytyczność; kryteria blokujące merge/release.  
- Konwencje dla custom tests (naming, folder, parametry) i zasady wydajności.  
- Definicje progów/thresholds dla kluczowych metryk (np. completeness %, duplikaty).  
- Zasady utrzymania seedów (źródło prawdy, rewizje, testy na seedy).  
- Procedura eskalacji i tworzenia waiverów na czasowe wyjątki.


## Wymagane streszczenia

- Executive: pokrycie testami, liczba krytycznych modeli, stan blokujących defektów i SLA jakości.


## Guidance (skrót)

- Ustal minimalny zestaw testów dla każdej warstwy i egzekwuj w CI; testy muszą być deterministyczne.  
- Używaj selectors/state artifacts dla szybkich przebiegów; pełne testy okresowo (np. nightly).  
- Testuj seedy tak samo jak modele; wersjonuj i dokumentuj ich źródło.  
- Zgłaszaj i śledź waivery; blokuj deploy dla krytycznych testów failing, chyba że waiver zatwierdzony.  
- Mierz koszt testów; optymalizuj ciężkie testy (sample, window, incremental).


## Checklisty Definition of Ready (DoR)

- [ ] Modele/krytyczność i SLA danych zmapowane; źródła seedów znane.  
- [ ] Wymagane minimalne testy uzgodnione; kanały raportowania/alertów dostępne.  
- [ ] Zidentyfikowano ograniczenia kosztowe/performance.


## Checklisty Definition of Done (DoD)

- [ ] Testy przypisane do modeli/kolumn; selectors/harmonogram skonfigurowany; raporty działają.  
- [ ] Waivery/ADR opisane; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Checklisty DoR/DoD odhaczone.

