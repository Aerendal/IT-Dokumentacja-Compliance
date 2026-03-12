---
title: Policy Migration Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Policy Migration Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zaplanować migrację polityk/procedur do nowego systemu/biblioteki: harmonogram, fale, zależności, ryzyka i komunikację.


## Zakres i granice

- Obejmuje: inwentarz polityk/wersji, priorytetyzację i fale, zależności (techniczne/operacyjne), okna zmian, zasoby, plan komunikacji, ryzyka i kryteria go/no-go.
- Poza zakresem: szczegółowe kroki migracji (w Migration Execution) i zmiany treści polityk.


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

- Kontekst i cele migracji
- Inwentarz i priorytetyzacja (fale)
- Zależności techniczne/operacyjne i okna zmian
- Harmonogram, zasoby i właściciele
- Ryzyka i plan mitigacji
- Plan komunikacji i go/no-go


## Szybkie powiązania
- policy-migration-execution
- vm-migration-procedure
- vm-migration-plan
- retraining-schedule
- qa-project-schedule

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)

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

- Wypełnij inwentarz, priorytety, fale i zależności; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj harmonogram po dry-runie/zmianach systemów; synchronizuj z execution.


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

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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
- Inwentarz, plan fal, test cases, narzędzia migracji, raporty, rollback plan, monitoring.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Infra/Cloud → Security → Product/Owners → Change/CAB → Owner sign‑off.
## Metryki jakości
- Sukces fal, downtime, incydenty, czas cutover, koszt migracji, czas do stabilizacji.
## Kryteria ukończenia
- [ ] Plan migracji opisany; testy/go-no-go/rollback gotowe; dokument w linkage_index; wersja/data/właściciel aktualne.
## Wejścia

- Inwentarz polityk/metadanych, wymagania regulacyjne/retencji.
- Dostępność systemów źródło/cel, okna zmian, zasoby.
- Ryzyka i ograniczenia (np. blackout dates, audyty).


## Wyjścia

- Harmonogram/fale migracji z właścicielami.
- Lista zależności i ryzyk z planem mitigacji.
- Plan komunikacji i go/no-go checklist.



## Szybkie powiązania (uzupełnij)

- policy_migration_execution.md
- policy_administration_system_implementation.md
- policy_and_procedure_library.md
- logging_and_audit_trail.md
- policy_metrics_monitoring.md
- security_compliance_matrix.md


## Wymagane rozwinięcia / streszczenia

- Tabela harmonogramu/fal: polityka → wersje → fala → data/okno → owner → status.
- Streszczenie ryzyk i decyzji go/no-go.


## Wymagane powiązania

- System źródło/cel, ograniczenia zmian, audyt/retencja, komunikacja.


## Kryteria DoR

- [ ] Inwentarz polityk/metadanych i priorytety dostępne.
- [ ] Okna zmian i zasoby uzgodnione.
- [ ] Właściciele fal i kanały komunikacji potwierdzeni.


## Kryteria DoD

- [ ] Harmonogram/fale opisane; zależności i ryzyka wpisane.
- [ ] Plan komunikacji i go/no-go checklist dodane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Harmonogram/fale (MD/CSV), inwentarz polityk.
- Lista zależności/ryzyk i plan mitigacji.
- Plan komunikacji/go-no-go.


## Walidacja / testy

- Peer review harmonogramu i zależności; sanity okien zmian.
- Dry-run planowania na próbce polityk.


## Metryki monitorowane

- % polityk zaplanowanych/zmigrowanych vs plan.
- Liczba zmian harmonogramu i przyczyny.
- Ryzyka aktywne vs zamknięte.


## Utrzymanie i aktualizacje

- Aktualizuj po dry-run, zmianach systemów lub odkryciu nowych ryzyk.
- Synchronizuj z execution i komunikacją.


## Zakończenie

Po spełnieniu DoD opublikuj harmonogram, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przekaż go interesariuszom.
