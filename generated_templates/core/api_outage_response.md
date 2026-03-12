---
title: API Outage Response
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# API Outage Response


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować procedurę reakcji na awarie API (latency, błędy, całkowita niedostępność) w celu szybkiego przywrócenia SLO.


## Zakres i granice

- Obejmuje: detekcję, triage, komunikację, workaround/rollback, weryfikację usług zależnych, postmortem trigger.
- Poza zakresem: szczegółowe naprawy kodu usług.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia
- Wejścia: klasyfikacja incydentów, SLO/SLI, runbooki, kontakty on-call, dane krytycznych systemów, RACI.
- Wyjścia: plan reagowania, procedury komunikacji, checklisty, raport post-incident, lista działań naprawczych.
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
- Przygotowanie i testy scenariuszy.
- Detekcja i triage.
- Reakcja/mitigacja + komunikacja.
- Odbudowa/DR i weryfikacja usług.
- Postmortem, akcje zapobiegawcze i aktualizacja runbooków.
## Struktura sekcji (szkielet)

- Detekcja i klasyfikacja
- Triage i izolacja
- Komunikacja (wewn./zewn.)
- Workaround/rollback
- Weryfikacja i monitorowanie
- Postmortem trigger


## Szybkie powiązania
- vm-outage-response
- system-outage-response
- streaming-outage-response
- server-outage-response
- search-outage-response

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

- Alerty/monitoring
- Mapa usług i zależności
- SLO/SLA
- Kanały komunikacji


## Wyjścia

- Runbook awarii
- Plan komunikacji
- Decyzje rollback/workaround
- Link do postmortem



## Szybkie powiązania (uzupełnij)

- [ ] api_gateway_operations_runbook.md
- [ ] api_monitoring_runbook.md
- [ ] api_error_rate_monitoring.md
- [ ] api_response_time_monitoring.md
- [ ] api_incident_postmortem.md
- [ ] security_incident_response.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych decyzji/ryzyk; rozwinięcia polityk/limitów/testów.


## Wymagane powiązania

- Dokumenty gateway/security/rate limiting/monitoring/testy; runbooki incydentów.


## Kryteria DoR

- [ ] Alert/incident zgłoszony
- [ ] Mapa usług i ownerów dostępna
- [ ] Kanały komunikacji ustalone
- [ ] Runbooki pomocnicze zlinkowane


## Kryteria DoD

- [ ] Runbook wypełniony
- [ ] Komunikacja przeprowadzona
- [ ] Workaround/rollback udokumentowany
- [ ] Trigger postmortem dodany


## Artefakty do załączenia

- Runbook awarii
- Timeline i decyzje
- Komunikaty status
- Link do postmortem


## Walidacja / testy

- Sanity/regresje na krytycznych endpointach; weryfikacja alertów/limitów/logów.


## Metryki monitorowane

- MTTD/MTTR
- Czas komunikatu status
- Rollback rate
- Impact (użytkownicy/SLO)


## Utrzymanie i aktualizacje

- Przegląd co release lub przy zmianie polityk/konfiguracji.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefaty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
