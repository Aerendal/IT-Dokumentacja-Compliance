---
title: Green IT Operations Runbook
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Green IT Operations Runbook


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Instrukcja operacyjna codziennego utrzymania praktyk Green IT: monitoring energii/CO₂/kosztów, reakcje na alarmy, rutyny optymalizacyjne, change management i raportowanie.


## Zakres i granice

- Obejmuje: metryki operacyjne (energia/CO₂/koszt, CPU/RAM, egress, storage tiering), rutyny (hibernacja/wyłączenia, cleanup, lifecycle danych), alarmy i reakcje (progi, akcje korygujące), change management pod kątem śladu, raportowanie dzienne/tygodniowe i eskalacje.  
- Poza zakresem: wybór strategii inwestycyjnych/ESG (osobne).


## Użytkownicy i interesariusze
- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.
## Wejścia i wyjścia

- Wejścia: telemetry/billing energii/CO₂, zużycie zasobów, polityki hibernacji/lifecycle, progi kosztów/emisji, change policy, dashboardy.  
- Wyjścia: harmonogram rutyn, konfiguracje alarmów, runbook reakcji, checklisty change, raporty/dash, log akcji/eskalacji.


## Założenia
- Dostępne są runbooki vendorów i aktualne listy kontaktów.
- Monitoring i backup są wdrożone w środowisku docelowym.
## Otwarte pytania
- Czy wszystkie integracje HL7/FHIR mają testy conformance?
- Jakie są lokalne wymagania prawne poza HIPAA/RODO?
## Powiązania (meta)

- Key Documents: green_it_improvement_plan, finops_policy, capacity_planning, data_lifecycle_policy, backup_and_retention, change_management_plan, monitoring_strategy_document, risk_register.
- Key Document Structures: metryki, rutyny, alarmy/reakcje, change checks, raporty.
- Document Dependencies: telemetry/billing API, monitoring/alerting, automation scripts, CMDB/tagging, ticketing/ESG/FinOps dashboards.



## Zależności dokumentu
Wymaga aktualnych RTO/RPO, krytyczności systemów, mapy integracji (HL7/FHIR/VPN), polityk bezpieczeństwa, listy kontaktów klinicznych i dostawców, oraz procedur downtime z kliniki. Bez nich DoR niezamknięte.
## Fazy cyklu życia
- Planowanie: aktualizacja inwentarza, RTO/RPO, okna serwisowe.
- Operacje bieżące: monitorowanie, backupy, patching, service desk, access requests.
- Incydenty: triage, eskalacje, komunikacja (klinika/pacjenci/dostawcy), raporty.
- DR/BCP: failover, restore, testy DR, powroty, walidacja kliniczna.
- Zmiany: CAB/approvals, release, walidacje post‑release.
- Audyt/Compliance: logi, ścieżki dowodów, raporty okresowe.
## Struktura sekcji (szkielet)

- Warunki wstępne i wymagania
- Kroki wykonania (krok po kroku)
- Weryfikacja poprawności
- Kroki rollback
- Typowe problemy i rozwiązania
- Log akcji

## Szybkie powiązania

- linkage_index.jsonl (sustainability/green_it_ops)
- green_it_improvement_plan, finops_policy, capacity_planning, data_lifecycle_policy, backup_and_retention, change_management_plan, monitoring_strategy_document, risk_register


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

1. Ustal metryki/progi i rutyny; skonfiguruj alarmy.  
2. Opisz akcje korygujące i checklisty change; uruchom raporty.  
3. Prowadź log akcji/eskalacji; aktualizuj linkage_index/checklisty.


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
- Downtime clinical — praca offline; kroki powrotu i walidacja kliniczna.
- RTO/RPO — czas przywrócenia / utrata danych akceptowalna.
## Przykłady użycia
- Awaria EHR: przełączenie na tryb downtime, komunikaty do kliniki, powrót i rekonsyliacja.
- Patch krytyczny: CAB, okno serwisowe, test po wdrożeniu, walidacja kliniczna.
## Ryzyka i ograniczenia
- Naruszenie HIPAA/RODO (logi, dostęp, dane w komunikatach).
- Brak walidacji klinicznej po incydencie/patchu → ryzyko kliniczne.
## Decyzje i uzasadnienia
- Kadencja raportów (tydzień/kwartał).  
- Kryteria go/no-go i required evidence.  
- Standard kanałów komunikacji (statuspage, e-mail, in-app).
## Powiązania z innymi dokumentami
- Incident Response Playbook (kliniczny/IT), Change Management, Backup & DR.
- IAM/Privileged Access Policy, Audit/Compliance plan.
## Powiązania z sekcjami innych dokumentów
- Privacy/Security → IAM/logi/szyfrowanie.
- HL7/FHIR Integration → Monitoring i testy interface’ów.
## Słownik pojęć w dokumencie
- EHR/EMR, PACS, LIS, RIS, HL7, FHIR, CAB, RTO/RPO.
## Wymagane odwołania do standardów
- HIPAA/RODO, lokalne przepisy zdrowotne, HL7/FHIR conformance, ISO 27799 (health infosec).
## Mapa relacji sekcja→sekcja
- Inwentarz → Monitoring/Backup/DR → Incydenty/Downtime → Audyt.
## Mapa relacji dokument→dokument
- Healthcare IT Ops Runbook → Incident Response → Change Mgmt → Audit/Compliance.
## Ścieżki informacji
- Alert/Incydent → Triage/Eskalacja → Komunikacja → Mitigacja → Walidacja kliniczna → Postmortem.
- Zmiana/Patch → CAB → Wdrożenie → Walidacja → Dokumentacja/audyt.
## Weryfikacja spójności

- [ ] Metryki/progi spójne z celami green IT; alarmy mają akcje i ownerów.  
- [ ] Rutyny mają harmonogram i dowody; log akcji prowadzony; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Skrypty automatyzacji, dashboardy, konfiguracje alarmów, checklisty change, raporty, log akcji/eskalacji, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- IT Ops → Security/Compliance → Klinika → CAB/Owner sign‑off.
## Metryki jakości

- Trend energii/CO₂/kosztów, liczba alarmów i MTTA/MTTR, skuteczność rutyn (oszczędności), liczba waiverów i czas sunset, adopcja raportów.

## Kryteria ukończenia

- [ ] Runbook operacyjny kompletny: metryki, rutyny, alarmy, raporty, change checks; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Metryki operacyjne (energia/CO₂/koszt, CPU/RAM, egress/storage tiering) i progi  
2) Rutyny: hibernacja/wyłączenia, cleanup, lifecycle danych, optymalizacje infra/app  
3) Alarmy i reakcje (progi, kto, akcje korygujące, eskalacje)  
4) Change management (checklisty śladu, approval, testy/regresja perf)  
5) Raportowanie (cadence dzienny/tygodniowy, dashboardy, odbiorcy, log akcji)  
6) Ryzyka i waivery (sunset/kompensacje)  
7) Załączniki (skrypty, dashboardy, checklisty change, log eskalacji)


## Wymagane rozwinięcia

- Progi energii/CO₂/kosztów i akcje; harmonogram rutyn (hibernacja, cleanup, tiering).  
- Runbook reakcji na alarmy; checklisty change z oceną śladu; raporty/dash.  
- Automatyzacje (skrypty/cron/lambda) i rollbacks; log akcji i eskalacji.


## Wymagane streszczenia

- Executive: ostatnie alarmy/akcje, trend CO₂/koszt, skuteczność rutyn, otwarte waivery.


## Guidance (skrót)

- Tagowanie/CMDB to podstawa; bez tagów nie liczysz.  
- Automatyzuj hibernację/cleanup/tiering; weryfikuj wpływ na perf/UX.  
- Alarm = akcja + log; miej ścieżkę eskalacji i rollback.  
- Change: sprawdzaj ślad (energia/CO₂/koszt) przed wdrożeniem; raportuj regularnie.


## Checklisty Definition of Ready (DoR)

- [ ] Telemetry/billing i tagowanie dostępne; progi wstępne ustalone.  
- [ ] Narzędzia/automatyzacje i ownerzy rutyn wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/progi/alarmy ustawione; rutyny działają; log akcji prowadzony.  
- [ ] Raporty publikowane wg cadence; waivery (jeśli) z sunset; dokument w linkage_index; metadane aktualne.

