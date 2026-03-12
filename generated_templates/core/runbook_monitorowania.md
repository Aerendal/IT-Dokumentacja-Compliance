---
title: Runbook monitorowania
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Runbook monitorowania


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Operacyjny opis monitorowania usług: źródła telemetryczne, alerty, on-call, triage i eskalacja, raportowanie i tuning progów.


## Zakres i granice

- Obejmuje: źródła metryk/logów/trace, konfigurację alertów (SLO/SLA, progi, deduplikacja), dyżury/on-call, triage i eskalację, przekazanie do runbooków serwisowych, raportowanie i tuning.  
- Poza zakresem: szczegółowe naprawy per serwis (są w runbookach serwisowych).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: lista usług i SLO/SLA, dashboardy/alert rules, graf kontaktów on-call, katalog runbooków serwisowych, polityka noise.  
- Wyjścia: zdefiniowane progi i routing alertów, checklisty triage, ścieżki eskalacji, raporty przeglądów, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_playbook, logging_strategy, audit_logging, runbook_monitorowania_api, backup_and_disaster_recovery.  
- Key Document Structures: źródła telemetryczne, alerty, on-call, triage/escalation, raportowanie/tuning.  
- Document Dependencies: observability stack, paging/alerting, status page, ticketing, CMDB usług.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Warunki wstępne i wymagania
- Kroki wykonania (krok po kroku)
- Weryfikacja poprawności
- Kroki rollback
- Typowe problemy i rozwiązania
- Log akcji

## Szybkie powiązania

- linkage_index.jsonl (observability/runbook_monitorowania)  
- incident_response_playbook, runbook_monitorowania_api, logging_strategy


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

1. Skonfiguruj źródła/alerty i routing; upewnij się, że on-call ma dostęp.  
2. Przy incydencie stosuj triage checklist i decision tree; eskaluj wg zasad.  
3. Po incydencie raportuj, tunuj progi, uaktualnij linkage_index i checklisty.


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

- [ ] Alerty pokrywają krytyczne SLO; routing on-call działa; noise policy wdrożona.  
- [ ] Triage ma decision tree i dane do zebrania; eskalacja i komunikacja opisana.  
- [ ] Linkage_index uzupełniony; plan przeglądów istnieje.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Alert rules, dashboardy, matryca progi→routing, checklisty triage, decision tree, raporty przeglądów, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Średni czas triage, liczba alertów szumowych, % alertów zamkniętych automatycznie, spełnienie SLO, liczba action items z przeglądów zrealizowanych on-time.

## Kryteria ukończenia

- [ ] Runbook monitorowania gotowy do użycia (alerty, triage, eskalacja, tuning) i powiązany w linkage_index.


## Struktura sekcji

1) Źródła metryk/logów/trace (systemy, dostępy, request-id/trace-id)  
2) Alerty: progi, SLO/SLA, deduplikacja/aggregation, routing do on-call, quiet hours  
3) On-call: dyżury, kontakty, kanały eskalacji, rotacje  
4) Triage alertów: klasyfikacja, timeline, decision tree, dane do zebrania, handoff do runbooków serwisowych  
5) Eskalacja i komunikacja (war room, status page, stakeholderzy)  
6) Raporty i tuning (przeglądy alertów, noise reduction, progi, action items)  
7) Załączniki (checklisty triage, matryca progi→routing, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela progów i routing per usługa/grupa SLO; definicja error budget.  
- Decision tree triage i lista danych: trace id, ostatni deploy, zmiany infrastruktury.  
- Zasady noise policy: ciche godziny, deduplikacja, auto-close, SLO-based alerts.  
- Cadence przeglądów (np. tygodniowy alert review) i właściciele action items.


## Wymagane streszczenia

- Executive: stan SLO, top źródła alertów, plan redukcji szumu.


## Guidance (skrót)

- Alerty buduj na SLO/error budget; ogranicz alert fatigue.  
- Pierwsze pytanie triage: „co się zmieniło?” (deploy, feature flag, infra).  
- Używaj trace/request-id w diagnostyce; kieruj szybko do właściwego runbooka serwisowego.  
-. Regularnie przeglądaj alerty, usuwaj szum, aktualizuj progi i linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Dashboardy/alert rules gotowe; on-call i kontakty aktualne.  
- [ ] Runbooki serwisowe zmapowane; status page i kanały komunikacji dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Progi/routing/triage/eskalacja opisane; szablony komunikacji i checklisty dołączone; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Plan przeglądów alertów (cadence, owner) zapisany; checklisty DoR/DoD odhaczone.

