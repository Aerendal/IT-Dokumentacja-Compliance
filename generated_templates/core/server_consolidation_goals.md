---
title: Server Consolidation Goals
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Server Consolidation Goals


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określa cele i kryteria konsolidacji serwerów/środowisk: redukcja kosztów, poprawa zarządzania, bezpieczeństwa i dostępności. Ustala zakres, metryki sukcesu i ograniczenia.


## Zakres i granice

- Obejmuje: inwentaryzację serwerów/aplikacji, kryteria konsolidacji (utilization, krytyczność, zgodność), target architekturę (virtualization/container/cloud), migracje i harmonogram, ryzyka (downtime, licencje), bezpieczeństwo (patching, hardening), DR/HA, compliance (licencje/RODO), decommission, metryki (TCO, energy, MTTR).  
- Poza zakresem: refaktoryzacja aplikacji (oddzielne projekty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: CMDB/inventory, metryki wykorzystania, SLA, koszty/licencje, zależności aplikacji, polityki bezpieczeństwa/DR, ograniczenia biznesowe, okna serwisowe.  
- Wyjścia: cele konsolidacji i KPI, lista kandydatów (move/retain/decom), target architektura, plan migracji/cutover, plan testów i walidacji, raport kosztów/korzyści, checklisty DoR/DoD.


## Założenia

- Dane CMDB są w miarę aktualne.  
- Dostępne są budżety i okna serwisowe.  
- Zespoły security/DR współpracują.


## Otwarte pytania

- Jakie regulatory ograniczenia sprzętu/danych?  
- Jak mierzyć koszty energii/CO2 po konsolidacji?  
- Czy pozostawić bufory capacity na wzrost ruchu?


## Powiązania (meta)

- Key Documents: infrastructure_scaling_setup, dr_plan, security_hardening_checklist, capacity_planning, change_management_policy, finops_policy.  
- Key Document Structures: inwentaryzacja, kryteria, architektura docelowa, plan migracji, testy, ryzyka, KPI.  
- Document Dependencies: CMDB, monitoring, licencje, backup/DR, ticketing/change mgmt, cost data.


## Zależności dokumentu

Wymaga: aktualnej inwentaryzacji, metryk użycia, SLA/krytyczności, licencji/kosztów, planów DR/HA, standardów bezpieczeństwa. Braki = DoR otwarte.


## Fazy cyklu życia

- Analiza i definiowanie celów/KPI.  
- Wybór architektury docelowej i listy kandydatów.  
- Plan i wykonanie migracji/decommission.  
- Walidacja, raportowanie i optymalizacje.



## Struktura sekcji (szkielet)
- Kontekst i interesariusze.
- Zakres procesów/zjawisk.
- Scenariusze i parametry wejściowe.
- Metryki sukcesu i tolerancje błędu.
- Wydajność/czas uruchomienia i zasoby.
- Plan walidacji (benchmarks, dane referencyjne).
- Ryzyka i ograniczenia.
## Szybkie powiązania

- linkage_index.jsonl (server/consolidation/goals)  
- finops_policy, capacity_planning, security_hardening_checklist, dr_plan


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

1. Zbierz dane (CMDB, koszty, SLA), zdefiniuj kryteria i listę kandydatów.  
2. Wybierz architekturę docelową i plan migracji; wykonaj piloty.  
3. Przeprowadź migracje/decommission, waliduj, raportuj KPI; aktualizuj DoR/DoD i linkage_index.


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

- Consolidation: redukcja liczby serwerów/instancji przy zachowaniu SLO.  
- Break-even: moment, gdy oszczędności pokrywają koszt migracji.  
- Patch compliance: % systemów z aktualnymi poprawkami.


## Przykłady użycia

- Konsolidacja VM do mniejszej liczby hostów/kontenerów.  
- Migracja on-prem → cloud/hybrid w celu redukcji kosztów i zwiększenia HA.  
- Decommission serwerów po przejściu na managed services.


## Ryzyka i ograniczenia

- Niedoszacowanie zależności → downtime.  
- Koszty licencji lub storage mogą zjeść oszczędności.  
- Brak DR/HA w nowym środowisku → ryzyko dostępności.


## Decyzje i uzasadnienia

- Priorytety migracji (krytyczność vs koszt).  
- Wybór platformy docelowej (cloud/on‑prem/hybrid).  
- Zakres automatyzacji (IaC) vs ręczne migracje.


## Powiązania z innymi dokumentami

- infrastructure_scaling_setup — progi i IaC.  
- finops_policy — koszty.  
- dr_plan — odporność.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Standardy bezpieczeństwa, retencji danych, DR/BCP.  
- Licencyjne/regulacyjne wymagania sprzętu/oprogramowania.

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

- Inwentaryzacja → Kryteria → Lista kandydatów → Plan migracji.  
- Bezpieczeństwo/DR → Architektura docelowa → Testy cutover.  
- KPI/TCO → Raport koszt/korzyść → Decyzje biznesowe.


## Struktura sekcji

1) Cele i KPI (TCO, energy, MTTR, patch compliance)  
2) Inwentaryzacja i kryteria konsolidacji (utilization, zgodność, krytyczność)  
3) Architektura docelowa (virtualization/container/cloud/hybrid)  
4) Plan migracji/cutover i testy (piloty, fazy, rollback)  
5) Bezpieczeństwo i licencje (compliance, hardening, patching)  
6) DR/HA i backup (RTO/RPO)  
7) Koszt/FinOps i raportowanie (CAPEX/OPEX, oszczędności)  
8) Decommission i disposal (bezpieczne usuwanie danych)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela kandydatów z metrykami (CPU/mem/util, SLA, koszt).  
- Plan testów migracji i cutover (downtime, rollback).  
- Model oszczędności i break‑even.  
- Plan decommission (data wipe, licencje, CMDB update).


## Wymagane streszczenia

- Executive snapshot: KPI, oszczędności, ryzyka, status migracji.  
- Krótka karta pilotów i wyników.


## Guidance (skrót)

- Zacznij od low‑risk/low‑value serwerów; pilotaż przed szeroką migracją.  
- Ustal kryteria go/no‑go per migracja; miej rollback.  
- Utrzymuj aktualny CMDB i licencje podczas konsolidacji.  
- Hardening i patch compliance to must‑have przed/po migracji.  
- Mierz oszczędności vs koszt migracji; iteruj.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentaryzacja i metryki wykorzystania gotowe.  
- [ ] Kryteria i KPI uzgodnione.  
- [ ] Architektura docelowa wstępnie wybrana; standardy security/DR znane.  
- [ ] Licencje/koszty zebrane; plan finansowy wstępny.  
- [ ] Okna migracji i właściciele uzgodnieni.


## Checklisty Definition of Done (DoD)

- [ ] Migracje/decommission wykonane; CMDB/licencje zaktualizowane; status/wersja/data uzupełnione.  
- [ ] KPI osiągnięte lub wyjątki zaakceptowane; oszczędności obliczone.  
- [ ] Hardening/patch/backup/DR zweryfikowane.  
- [ ] Raport koszt/korzyść opublikowany; linkage_index uzupełniony.  
- [ ] Ryzyka i lessons learned zapisane.

