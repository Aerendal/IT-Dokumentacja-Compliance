---
title: Trading Operations
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Trading Operations


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje procesy operacyjne dla handlu (rynki finansowe/crypto/energetyka): obsługa zleceń, monitoring, ryzyko operacyjne, zgodność i ciągłość działania. Ma zapewnić bezpieczne i zgodne wykonywanie transakcji oraz szybkie reagowanie na incydenty.


## Zakres i granice

- Obejmuje: lifecycle zleceń (przyjęcie, walidacja, routing, execution, post‑trade), monitoring (latencja, reject/cancel rate, fill rate), zarządzanie ryzykiem (limity, margines, fat finger, kill switch), zgodność (MiFID/Reg NMS/EMIR/Dodd‑Frank – zależnie od jurysdykcji), separacja obowiązków, dane rynkowe (integrity, feed health), obsługę wyjątków/incydentów, reconciliation, raportowanie regulacyjne, BCP/DR.
- Poza zakresem: strategia tradingowa/alpha (oddzielne dokumenty), szczegółowa architektura systemu (referencja).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: polityki ryzyka/limity, regulacje jurysdykcji, specyfikacje giełd/venue, mapy systemów (OMS/EMS/risk/market data), SLA latencji, procedury BCP/DR, rejestr wyjątków, logi/audyt, listy kontaktów.
- Wyjścia: procedury operacyjne i checklisty, konfiguracje limitów/kill switch, playbooki incydentów, raporty zgodności, harmonogramy reconciliation, metryki operacyjne, plan testów DR.


## Założenia
- Systemy bezpieczeństwa i komunikacji działają.  
- Dostępne są aktualne plany ewakuacji i A11y.  
- Dostawcy spełniają SLA.
## Otwarte pytania
- Jak często wykonywać ćwiczenia ewakuacyjne z udziałem publiczności?  
- Jakie limity gęstości tłumu przyjmujemy w danym obiekcie?  
- Jak raportować KPI do właścicieli/najemców?
## Powiązania (meta)

- Key Documents: risk_management_trading, market_data_policy, compliance_trading (MiFID/EMIR/Dodd‑Frank/NMS), bcp_drp, incident_response_trading, change_management, access_control.
- Key Document Structures: zlecenia, monitoring, ryzyko, zgodność, incydenty, BCP/DR.
- Document Dependencies: OMS/EMS, risk/limit engine, market data feed, surveillance, audit/logging, DR site, kill switch.


## Zależności dokumentu

Wymaga aktualnych limitów/ryzyk, spec giełd, polityk zgodności, konfiguracji OMS/EMS/risk, procedur BCP/DR i kontaktów. Brak = DoR otwarte.


## Fazy cyklu życia

- Przyjęcie/validacja zleceń: limity, kontrole compliance, dane rynkowe.
- Routing/execution: venue selection, latency, failover.
- Post‑trade: potwierdzenia, reconciliation, raporty regulacyjne.
- Monitoring: metryki, alerty, surveillance.
- Incydenty i wyjątki: triage, kill switch, komunikacja, postmortem.
- BCP/DR: testy, procedury, dokumentacja.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania
- venue-operations
- training-operations
- ticketing-operations
- security-operations
- scada-operations

## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **KNF-REKOM-IT** — Rekomendacje KNF dot. systemów IT w sektorze finansowym
- **MIFID2-PL** — MiFID II — Dyrektywa dot. Rynku Finansowego (implementacja PL)
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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
1. Przygotuj plan eventu/dnia, wypełnij checklisty readiness.  
2. Prowadź operacje wg ról/SOP, notuj incydenty i KPI.  
3. Po evencie wygeneruj raport, zaktualizuj DoR/DoD i linkage_index.
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
- ACS: Access Control System.  
- CMMS: Computerized Maintenance Management System.  
- Crowd management: kontrola przepływu ludzi dla bezpieczeństwa i komfortu.
## Przykłady użycia
- Koncert w arenie, mecz, targi, codzienna praca biurowca.  
- Test planu ewakuacji przy pełnej obsadzie.  
- Raport KPI po evencie (frekwencja, incydenty, przychód).
## Ryzyka i ograniczenia
- Przeciążenie wejść/Wi‑Fi → ryzyko bezpieczeństwa/UX.  
- Niespójna komunikacja między służbami → chaos.  
- Niedostępność systemów krytycznych (ACS/CCTV/AV).
## Decyzje i uzasadnienia
- Priorytety wejść/wyjść i routing tłumu.  
- Redundancje AV/IT i backup energii.  
- Standard SLA dla dostawców eventów.
## Powiązania z innymi dokumentami
- safety_plan — szczegóły ewakuacji i BHP.  
- facilities_maintenance_schedule — gotowość infrastruktury.  
- communication_plan — kanały i eskalacje.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Lokalne przepisy ppoż./BHP, normy crowd safety, wytyczne A11y.  
- Wewnętrzne standardy bezpieczeństwa obiektu.
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

## Powiązania sekcja↔sekcja

- Limity/ryzyko → Walidacja zleceń/routing → Monitoring → Incydenty/kill switch.
- Market data integrity → Walidacja → Reconciliation → Raporty.
- BCP/DR → Testy → Gotowość operacyjna.


## Struktura sekcji

1) Polityki ryzyka/limity (pre‑trade, intraday, fat finger, kill switch)  
2) Dane rynkowe i integracje (feed health, opóźnienia, integrity)  
3) Obsługa zleceń (przyjęcie, walidacja, routing, execution, cancel/reject)  
4) Monitoring i metryki (latencja, fill/reject/cancel rate, drop copy, alerty)  
5) Zgodność i raporty (MiFID/EMIR/NMS/DF, surveillance, logs/audit)  
6) Reconciliation i post‑trade kontrole  
7) Incydenty/wyjątki (playbooki, kill switch, komunikacja, postmortem)  
8) BCP/DR (procedury, testy, kontakt)

