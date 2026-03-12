---
title: Obsługa incydentów rate limit
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Obsługa incydentów rate limit


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Kanał war-room: [link]


## Cel dokumentu

Runbook reagowania na incydenty związane z rate limiting (spikes, abuse, błędne konfiguracje) w celu szybkiego przywrócenia dostępności i ochrony platformy przy zachowaniu ścieżki audytu.


## Zakres i granice

- Zakres: detekcja alertów 429/503 i metryk, triage klient/endpoint/tenant, legalny ruch vs abuse, akcje doraźne (tymczasowe podniesienie limitu, throttling, blokady), komunikacja (klient/status page/internal), identyfikacja przyczyn (regresja, kampania, bot), działania trwałe, postmortem.
- Poza zakresem: definiowanie polityk limitów (w `api_rate_limiting_requirements.md`), strategia długofalowa (`rate_limiting_strategy`).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

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

1. Detekcja i alerty (metryki, progi, dashboardy, sygnatury abuse).
2. Triage (klient/tenant/endpoint, legal vs abuse, wpływ biznesowy).
3. Akcje natychmiastowe (podniesienie limitu na czas, throttling, blokady, feature flags).
4. Komunikacja (status page, klient, support L1/L2, war room).
5. Przyczyna i remediacja trwała (regresja, config, kampania, bot; plan napraw).
6. Postmortem i aktualizacja runbooka (timeline, follow‑up, decyzje).
7. Załączniki (szablony komunikatów, checklisty triage, ADR/waiver log).


## Szybkie powiązania
- rate-limit-incident-handling
- wymagania-rate-limiting
- return-rate-tracking
- rate-management-procedure
- rate-management-guide

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

- Po alercie wykonaj triage (sekcja 2); zanotuj trace/token/endpoint/plan.
- W sekcji 3 wybierz akcję natychmiastową zgodnie z polityką; w sekcji 4 uruchom komunikację.
- Ustal przyczynę i plan trwały (sekcja 5); zamknij postmortem i uzupełnij quick links oraz checklisty w `reports/checklist_atomic.jsonl`.


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

- Alerty gateway/APM/SIEM, logi/trace, telemetria 429/503, profile ruchu i plany klientów, polityka wyjątków/podniesień.


## Wyjścia

- Decyzje i akcje (temp increase/deny/throttle/block), komunikaty do klientów/supportu, bilety RCA, rekomendacje trwałe, uaktualniony runbook i linkage_index.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `api_rate_limiting_requirements.md`, `konfiguracja_rate_limiting.md`
- [ ] `linkage_index.jsonl` → `incident_response_runbook.md`, `security_incident_response.md`
- [ ] `linkage_index.jsonl` → `logging_and_audit_trail.md`, `audit_logging.md`


## Wymagane rozwinięcia / streszczenia

- Matryca progów alertów (warning/critical) z eskalacją i właścicielami.
- Kryteria: kiedy podnieść limit, a kiedy blokować; wymagane approvals i czas ważności waiver.
- Streszczenie: liczba incydentów, MTTR, główne przyczyny, plan zapobiegania.


## Wymagane powiązania

- Gateway/WAF/feature flags, telemetry (APM/SIEM), CMDB klientów/planów, status page/support playbooks.
- Waiver log i polityka wyjątków; ticketing dla RCA i zadań trwałych.


## Kryteria DoR (Definition of Ready)

- [ ] Progi alertów, dashboardy i kontakty klientów/supportu dostępne.
- [ ] Narzędzia gateway/feature flags i polityka wyjątków przygotowane.


## Kryteria DoD (Definition of Done)

- [ ] Incydent opanowany; decyzje/akcje i komunikacja udokumentowane.
- [ ] RCA i działania trwałe zaplanowane; postmortem wykonany; quick links/status zaktualizowane.
- [ ] Checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Alert rules, dashboardy, logi/trace, decyzje/waivery, komunikaty, bilety RCA, postmortem, ADR/waiver log.


## Walidacja / testy

- Ćwiczenia tabletop incydentów rate limit; dry‑run komunikacji i waiver.
- Test poprawności alertów (symulacja spike/abuse); weryfikacja logów/audytu.


## Metryki monitorowane

- MTTR incydentów rate limit, liczba incydentów/kwartał, % incydentów z komunikacją on‑time.
- Recurrence rate, liczba waiverów i czas ich wygaszania.


## Utrzymanie i aktualizacje

- Przegląd kwartalny progów/waiver logu i wzorców komunikacji.
- Rejestr zmian w `reports/change_log.jsonl`; quick links po każdej aktualizacji.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, uzupełnij `linkage_index.jsonl` oraz `reports/checklist_atomic.jsonl`.
