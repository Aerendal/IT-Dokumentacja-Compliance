---
title: Test Data Preparation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Test Data Preparation


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować proces przygotowania danych testowych: źródła, generowanie/masking, jakość, bezpieczeństwo i utrzymanie, aby testy były wiarygodne i zgodne z regulacjami.


## Zakres i granice

- Obejmuje: potrzeby danych per typ testu, źródła (prod subset/syntetyczne), maskowanie/anonimizację, generowanie, weryfikację jakości, wersjonowanie, dostęp/bezpieczeństwo, automatyzację i utrzymanie.
- Poza zakresem: implementacja konkretnych skryptów w repo (linkować zamiast kopiować).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

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

- Kontekst i wymagania danych (per typ testu)
- Źródła i tworzenie danych (subset, syntetyczne, mieszane)
- Maskowanie/anonimizacja i polityki bezpieczeństwa
- Weryfikacja jakości danych (spójność, pokrycie, brak PII)
- Dostęp i zarządzanie (wersjonowanie, rotacja, cleanup)
- Automatyzacja i integracja z CI/CD
- Utrzymanie i przeglądy


## Szybkie powiązania
- test-data-preparation-plan
- test-data-strategy
- test-data-reference
- data-preparation-procedure
- data-preparation-code

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

- Ustal wymagania danych na podstawie scenariuszy; wybierz źródła i metody; opisz maskowanie/weryfikację; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Linkuj skrypty/generatory z repo zamiast kopiować; aktualizuj plan przy zmianach testów/regulacji.


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

- Scenariusze testowe, wymagania danych i krytyczne ścieżki.
- Polityki danych/PII/GDPR, klasyfikacja danych, zgody.
- Źródła danych (prod subset, syntetyczne, katalog danych), narzędzia do maskowania/generowania.


## Wyjścia

- Plan danych testowych per typ testu (unit/integration/e2e/perf/DR).
- Zestawy danych testowych lub procedury ich tworzenia.
- Checklisty jakości i bezpieczeństwa danych.



## Szybkie powiązania (uzupełnij)

- test_data_preparation_plan.md
- security_compliance_matrix.md
- data_privacy_compliance.md
- logging_and_audit_trail.md
- devsecops_pipeline.md
- performance_testing_plan.md


## Wymagane rozwinięcia / streszczenia

- Tabela: typ testu → wymagania danych → źródło → maskowanie → weryfikacja → owner.
- Checklisty jakości/bezpieczeństwa danych.


## Wymagane powiązania

- Polityki PII/GDPR, compliance, CI/CD, katalog danych, narzędzia maskowania/generacji.


## Kryteria DoR

- [ ] Wymagania danych i scenariusze zebrane.
- [ ] Polityki PII/GDPR i źródła danych dostępne.
- [ ] Narzędzia i właściciele przygotowani.


## Kryteria DoD

- [ ] Plan danych per typ testu opisany; maskowanie/weryfikacja ujęte.
- [ ] Artefakty/skrypty podlinkowane; checklisty uzupełnione.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Plan danych (MD/CSV), checklisty jakości/bezpieczeństwa.
- Linki do skryptów/generatorów/maskowania.
- Raporty weryfikacji danych.


## Walidacja / testy

- Próbny run generacji/maskowania; sanity brak PII.
- Sprawdzenie pokrycia scenariuszy kluczowych.


## Metryki monitorowane

- Czas przygotowania danych; % testów blokowanych przez dane.
- Incydenty PII w danych testowych; pokrycie danych krytycznych ścieżek.
- Flake/defect leakage związane z danymi.


## Utrzymanie i aktualizacje

- Przeglądy co release/kwartał lub po zmianach regulacji/testów.
- Aktualizuj źródła/maskowanie przy zmianach schematów danych.


## Zakończenie

Po spełnieniu DoD opublikuj plan, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zsynchronizuj z pipeline CI/CD.
