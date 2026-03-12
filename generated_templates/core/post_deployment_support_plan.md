---
title: Post-Deployment Support Plan
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Post-Deployment Support Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisuje wsparcie tuż po wdrożeniu (stabilizacja/hypercare): monitoring, obsługa incydentów, komunikacja, eskalacje, runbooki, kryteria zakończenia hypercare i przekazania do BAU.


## Zakres i granice

- Obejmuje: okres hypercare, zakres monitoringu, obsługę incydentów/problemów, kanały i SLA, eskalacje/on-call, runbooki krytycznych ścieżek, kryteria exit, raportowanie, komunikację do klientów i wewnętrzną.
- Poza zakresem: długoterminowy support BAU (opisany w Solution Support Plan); pełne playbooki IR (osobny dokument IR).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: plan wdrożenia, znane ryzyka/defekty, runbooki, monitoring/alerty, release notes, lista właścicieli komponentów, SLA/OLA, kontakt do klientów.
- Wyjścia: plan hypercare (czas, role, on-call), zakres monitoringu i alertów, drabinka eskalacji, runbooki i checklisty walidacyjne, raportowanie (status, incydenty, defekty), kryteria exit i przekazanie do BAU.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: solution_support_plan, incident_response_playbook, change_management_process, release_plan, rollback_plan, risk_register.
- Dependencies: monitoring/alerting, właściciele komponentów, znane defekty, komunikacja, SLA.
- RACI: Product/Release Owner, SRE, Support, Engineering, Security/Compliance, Comms.


## Zależności dokumentu

- Upstream: release plan, znane ryzyka/defekty, monitoring/alerting, SLA.
- Downstream: raporty hypercare, action items, przekazanie do BAU, retrospektywa.
- Zewnętrzne: klienci/partnerzy (komunikacja), dostawcy (jeśli zależności 3rd party).


## Fazy cyklu życia

- Przygotowanie: zakres hypercare, monitoring/alerty, runbooki, role/on-call, komunikacja.
- Wykonanie: aktywny hypercare, incydenty, raporty statusu.
- Zakończenie: spełnienie kryteriów exit, przekazanie BAU, retrospektywa.



## Struktura sekcji (szkielet)

1) Streszczenie i cel hypercare (czas trwania, KPI: incydenty, MTTR, błędy krytyczne)
2) Zakres hypercare (komponenty, funkcje krytyczne, klientów/regiony objęte)
3) Monitoring i alerty (metryki, progi, dashboardy, SLO)
4) Role/on-call i eskalacje (drabinka, kontakty, SLA/OLA)
5) Runbooki i checklisty walidacji powdrożeniowej (sanity checks, smoke, dane)
6) Obsługa incydentów/problemów (proces, komunikacja wew./zewn., warunki rollback)
7) Raportowanie i komunikacja (status daily, klient, stakeholderzy)
8) Kryteria exit hypercare i przekazanie do BAU (SLO/KPI, defekty otwarte, dokumentacja)
9) Ryzyka i założenia; decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- solution_support_plan, incident_response_playbook, change_management_process, release_plan, rollback_plan, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- [ ] Krytyczne ścieżki mają monitoring/alerty; runbooki powdrożeniowe wykonane.
- [ ] Incydenty/defekty obsłużone; komunikacja prowadzona; decyzje rollback/continue udokumentowane.
- [ ] Kryteria exit spełnione; przekazanie BAU i retrospektywa wykonane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Dashboardy/alerty, escalation ladder, runbooki sanity/smoke/rollback, raporty hypercare, checklisty exit, ADR log.


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

- Monitoring/alerty → obsługa incydentów → komunikacja → raportowanie → kryteria exit.
- Runbooki → walidacje powdrożeniowe → decyzje rollback/continue.


## Wymagane rozwinięcia

- Lista dashboardów/alertów i progów; drabinka eskalacji; runbooki sanity/smoke/rollback; checklisty komunikacji; kryteria exit.
- Raport template (status, incydenty, defekty, działania, ryzyka).


## Wymagane streszczenia

- Executive summary: czas hypercare, KPI, incydenty/defekty, decyzje rollback/continue, data exit.
- One-pager: kontakty/on-call, SLO, kryteria exit, linki do runbooków.


## Guidance (skrót)

- DoR: release plan, monitoring/alerty gotowe; runbooki i rollback; on-call i kontakty; komunikacja przygotowana; SLO/exit criteria uzgodnione.
- DoD: hypercare przeprowadzony; incydenty/defekty zarejestrowane; kryteria exit spełnione; przekazanie BAU i retrospektywa; metadane aktualne; dokument w linkage_index.
- Spójność: monitoring pokrywa krytyczne ścieżki; eskalacje/on-call działają; decyzje rollback mają warunki i ownerów; exit criteria są mierzalne.


## Checklisty Definition of Ready (DoR)

- [ ] Monitoring/alerty i runbooki gotowe; on-call i kontakty; SLO/exit criteria uzgodnione.
- [ ] Komunikacja (wew./zewn.) przygotowana; release/rollback plan dostępny.


## Checklisty Definition of Done (DoD)

- [ ] Hypercare zakończony; kryteria exit spełnione; incydenty/defekty zamknięte lub przekazane; przekazanie BAU; retrospektywa.
- [ ] Metadane aktualne; dokument w linkage_index.

