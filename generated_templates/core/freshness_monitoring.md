---
title: Freshness Monitoring
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Freshness Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Monitorować świeżość danych w pipeline’ach/raportach i alertować na opóźnienia, z planem remediacji (retry/re-run/backfill) i właścicielami.


## Zakres i granice

- Obejmuje: zakres tabel/raportów/datasetów, definicje freshness (timestamp, watermark, event time), SLO/progi opóźnień i okna akceptacji, implementację checków (dbt/Great Expectations/custom), źródła metryk i harmonogram, alerty/escalacje, dashboardy freshnesu/historia, playbook remediacji (retry/re-run/backfill).  
- Poza zakresem: kompletne SLA danych biznesowych (osobne polityki).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: listy tabel/raportów, definicje event/ingest time, schedule pipeline, narzędzia DQ (dbt/GE), monitoring/alerting, ownerzy danych.  
- Wyjścia: SLO/progi freshnesu, konfiguracje checków, alerty/escalacje, dashboard freshnesu, playbook remediacji/backfill, raport historii opóźnień.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: data_quality_policy, data_governance_requirements, monitoring_strategy_document, incident_response_playbook, change_management_plan, data_catalog, lineage_standards.
- Key Document Structures: zakres, definicje, SLO, implementacja checków, alerty, remediacja.
- Document Dependencies: scheduler/ETL/ELT, metadata store/lineage, DQ tools (dbt/GE), monitoring/alerting, ticketing.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Definicja SLO/SLI i krytycznych ścieżek.
- Projekt metryk/logów/traces i alertów.
- Ustawienie dashboardów i testów syntetycznych.
- Przeglądy i tuning progów.
## Struktura sekcji (szkielet)
- Cel monitoringu i zakres (usługi/ścieżki)
- SLO/SLI i priorytety alertowania
- Metryki/logi/traces i źródła danych
- Alerty/reguły, progi i runbooki
- Dashboardy i testy syntetyczne
- Operacje: on-call, eskalacje, przeglądy
- Utrzymanie, budżety zdarzeń i ciągłe doskonalenie
## Szybkie powiązania

- linkage_index.jsonl (data/freshness_monitoring)
- data_quality_policy, data_governance_requirements, monitoring_strategy_document, incident_response_playbook, change_management_plan, data_catalog, lineage_standards


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

1. Zdefiniuj zakres i SLO/progi; skonfiguruj checki i alerty.  
2. Udostępnij dashboard i playbook remediacji/backfill; przypisz ownerów.  
3. Monitoruj, raportuj i aktualizuj SLO po zmianach; zamknij DoR/DoD i linkage_index.


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

- [ ] SLO/progi spójne z wymaganiami; checki i alerty aktywne; właściciele przypisani.  
- [ ] Runbook remediacji i backfill opisany; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela SLO/progów, config checków (dbt/GE/custom), dashboard freshnesu, alert log, runbook remediacji/backfill, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Coverage freshnesu, MTTA/MTTR opóźnień, liczba opóźnień > SLO, skuteczność retry/backfill, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Freshness monitoring aktywny, alerty i dashboard działają; runbook remediacji gotowy; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres tabel/raportów/datasetów i definicje freshness (timestamp/watermark/event time)  
2) SLO/progi i okna akceptacji (per tabela/raport)  
3) Implementacja checków (narzędzia, schedule, źródła metryk)  
4) Alerty i eskalacje (progi, kanały, ownerzy, SLA reakcji)  
5) Dashboardy i raporty (historia opóźnień, trend, coverage)  
6) Remediacja (retry/re-run/backfill, runbook, właściciele)  
7) Ryzyka i waivery (sunset/kompensacje)  
8) Załączniki (check configs, dashboard links, playbook, log alertów)


## Wymagane rozwinięcia

- Tabela SLO/progów per tabela/raport; definicje event time vs ingest time.  
- Konfiguracje checków (dbt/GE/custom), schedule, źródła metryk i ETL dependency.  
- Alerty z progami i SLA; runbook remediacji/backfill i ticketing.


## Wymagane streszczenia

- Executive: coverage freshnesu, liczba/MTTA/MTTR opóźnień, top źródła i plan poprawy.


## Guidance (skrót)

- Definiuj freshness per tabela i trzymaj w katalogu/lineage; wybierz właściwy czas (event vs ingest).  
- Alertuj na przekroczenia SLO; automatyzuj retry/re-run; backfill z kontrolą jakości.  
- Mierz MTTA/MTTR opóźnień i trenduj; aktualizuj SLO po zmianach pipeline.


## Checklisty Definition of Ready (DoR)

- [ ] Listy tabel/raportów i definicje event/ingest time dostępne; narzędzia DQ/monitoring gotowe.  
- [ ] Ownerzy i progi wstępnie ustalone; runbook remediacji istnieje lub planowany.


## Checklisty Definition of Done (DoD)

- [ ] SLO/progi zdefiniowane; checki/alerty działają; dashboard publikowany.  
- [ ] Playbook remediacji/backfill z owner/ETA; dokument w linkage_index; metadane aktualne.

