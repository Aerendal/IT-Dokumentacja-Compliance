---
title: VM Migration Plan
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# VM Migration Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan migracji maszyn wirtualnych (on-prem → cloud, cloud → cloud, in-region): cele, zakres, harmonogram, ryzyka, testy i rollback. Ma zapewnić bezpieczną, przewidywalną migrację z minimalnym downtime.


## Zakres i granice

- Obejmuje: inwentarz VM (krytyczność, OS, CPU/RAM/dysk/sieć), grupowanie fal migracyjnych, architekturę docelową (region/VPC/VNet, IAM, sieć, storage), metody migracji (image/replication, warm/cold, live), zależności (DB, load balancer, DNS, certy, backup), testy (pre/post, DR), cutover plan, rollback, monitoring/observability, koszty, komunikację i change mgmt.
- Poza zakresem: refaktoryzacja aplikacji (lift&shift fokus), ale linkuj wymagania.


## Użytkownicy i interesariusze

- Infra/Cloud, SRE/Platform, Security, Product/Owners, Change/Comms, Finance/Licensing.


## Wejścia i wyjścia

- Wejścia: inwentarz VM/asset, krytyczność/SLA, architektura docelowa, polityki sieci/IAM/security, narzędzia migracji, okna serwisowe, wymagania performance, backup/DR, koszty/budżet, change requests.
- Wyjścia: plan fal, harmonogram, runbook migracji, checklisty pre/post, testy i wyniki, plan cutover/rollback, raport statusu/kosztów.


## Założenia

- Narzędzia migracji/backup dostępne; architektura docelowa gotowa; okna serwisowe uzgodnione.


## Otwarte pytania

- Jakie licencje/systemy wymagają re‑aktywacji? 
- Jakie są limity kosztów/okna dla krytycznych usług?


## Powiązania (meta)

- Key Documents: capacity_planning, system_monitoring_strategy, security_baseline, backup_and_recovery_procedure, change_management, incident_response_plan, cost_planning_and_forecasting.
- Key Document Structures: inwentarz, fale, testy, cutover/rollback, raporty.
- Document Dependencies: CMDB, tooling migracji, monitoring, DNS/LB, IAM, backup.


## Zależności dokumentu

Wymaga inwentarza i krytyczności VM, architektury docelowej, narzędzi migracji, okien serwisowych, polityk security/IAM, backup/DR, monitoring. Bez tego DoR otwarte.


## Fazy cyklu życia

- Przygotowanie: inwentarz, architektura, narzędzia, fale, testy.
- Wykonanie: migracja fal, testy pre/post, cutover, monitoring.
- Rollback (gdy potrzebne) i stabilizacja.
- Raport i retrospektywa; optymalizacje kosztów.



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

- linkage_index.jsonl (vm/migration)
- capacity_planning, system_monitoring_strategy, security_baseline, backup_and_recovery_procedure, change_management, incident_response_plan, cost_planning_and_forecasting


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Wypełnij inwentarz/krytyczność i architekturę docelową.
2. Zaplanuj fale, metody migracji, testy i kryteria go/no-go.
3. Opisz cutover/rollback, monitoring i komunikację; wykonaj i raportuj.


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

- Lift & Shift, Warm/Cold/Live migration, Cutover, Rollback, Go/No-Go.


## Przykłady użycia

- Migracja 50 VM: pilot 5 VM, potem fale wg SLA, warm replication, DNS cutover, rollback snapshot.


## Ryzyka i ograniczenia

- Brak testów → outage; brak rollback → długi downtime; koszty i prawa licencyjne po migracji.


## Decyzje i uzasadnienia

- [Decyzja] Metoda migracji (warm/live) — uzasadnienie SLA/ryzyka.
- [Decyzja] Kolejność fal — uzasadnienie zależności/krytyczności.


## Powiązania z innymi dokumentami

- Capacity Planning, System Monitoring, Security Baseline, Backup/Recovery, Change Mgmt, Incident Response, Cost Planning.


## Powiązania z sekcjami innych dokumentów

- Monitoring → obserwacja po cutover; Security → hardening w docelowej; Backup → rollback.


## Słownik pojęć w dokumencie

- Warm/Cold/Live migration, Cutover, Rollback, Go/No-Go, Pilot, Wave.


## Wymagane odwołania do standardów

- Polityki security/backup, compliance jeśli dotyczy (np. licencje, dane), procedury change.


## Mapa relacji sekcja→sekcja

- Inwentarz → Fale → Metoda → Testy → Cutover → Monitoring → Raporty.


## Mapa relacji dokument→dokument

- VM Migration → Capacity/Security/Monitoring/Backup/Change → Incident/Cost.


## Ścieżki informacji

- Inwentarz → Plan fal → Testy → Cutover/rollback → Monitor → Raport/retro.


## Weryfikacja spójności

- [ ] Fale/metody/testy/go-no-go i rollback opisane; dokument w linkage_index.
- [ ] Relacje cross‑doc opisane; wersja/data/właściciel aktualne.


## Lista kontrolna spójności relacji

- [ ] Każda fala ma zakres, metodę, testy, go/no-go, rollback.
- [ ] Każdy cutover ma monitoring i plan komunikacji.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Inwentarz, plan fal, test cases, narzędzia migracji, raporty, rollback plan, monitoring.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Infra/Cloud → Security → Product/Owners → Change/CAB → Owner sign‑off.


## Metryki jakości

- Sukces fal, downtime, incydenty, czas cutover, koszt migracji, czas do stabilizacji.

## Kryteria ukończenia

- [ ] Plan migracji opisany; testy/go-no-go/rollback gotowe; dokument w linkage_index; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Inwentarz/krytyczność → Fale → Harmonogram → Cutover/rollback.
- Testy pre/post → Decyzja go/no-go → Raporty.


## Struktura sekcji

1) Inwentarz i krytyczność VM (OS, zasoby, SLA, zależności)  
2) Architektura docelowa i polityki (VPC/VNet, IAM, sieć, storage, security)  
3) Fale migracyjne i harmonogram (grupowanie, okna, kolejność)  
4) Metoda migracji (narzędzia, warm/cold/live, dane, replika)  
5) Testy pre/post i kryteria go/no-go (func/perf/security/DR)  
6) Cutover i rollback plan (DNS/LB, certy, dane, backup)  
7) Monitoring/observability i koszty (przed/po)  
8) Komunikacja i change management  
9) Raporty statusu i retrospektywa


## Wymagane rozwinięcia

- Inwentarz/krytyczność; fale i okna; narzędzia/metody; testy i kryteria go/no-go.
- Cutover/rollback kroki; monitoring; koszty.


## Wymagane streszczenia

- Zakres/fale, harmonogram, kryteria go/no-go, plan cutover/rollback, ryzyka.


## Guidance (skrót)

- Grupuj wg krytyczności/zależności; zacznij od pilota.
- Zrób testy pre/post (func/perf/security/DR); zdefiniuj jasne go/no-go.
- Miej rollback (snapshot/backup/DNS revert); monitoruj po cutover.
- Komunikuj zmiany; kontroluj koszty i optymalizuj po migracji.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentarz i krytyczność zebrane; architektura docelowa określona.
- [ ] Narzędzia migracji/testów przygotowane; okna serwisowe uzgodnione.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Migracja fal wykonana lub zaplanowana; testy/go-no-go i raporty gotowe.
- [ ] Cutover/rollback opisane; monitoring/koszty ocenione; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

