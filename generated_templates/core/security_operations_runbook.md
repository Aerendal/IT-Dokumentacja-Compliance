---
title: Security Operations Runbook
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Operations Runbook


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Procedury operacyjne SOC: triage i eskalacja alertów, komunikacja, utrzymanie narzędzi, raportowanie i postmortem.


## Zakres i granice

- Obejmuje: oncall SOC, triage alertów, klasyfikację i eskalacje, komunikację, utrzymanie SIEM/SOAR, checklisty review i raportowanie.
- Poza zakresem: naprawy w kodzie produktu; zmiany infrastruktury spoza incydentów.


## Użytkownicy i interesariusze
- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.
## Wejścia i wyjścia
- Wejścia: inwentarz systemów i integracji (EHR/EMR/PACS/LIS/RIS), RTO/RPO, okna serwisowe, polityki bezpieczeństwa, listy kontaktów (klinika, dostawcy), dokumenty compliance (HIPAA/RODO), procedury downtime, CMDB/asset, runbooki vendorów.
- Wyjścia: harmonogramy zadań operacyjnych, procedury incydentów, checklisty backup/DR, instrukcje downtime, playbook komunikacji, lista kontaktów i eskalacji, log zmian/patchy.
## Założenia
- Dostępne są runbooki vendorów i aktualne listy kontaktów.
- Monitoring i backup są wdrożone w środowisku docelowym.
## Otwarte pytania
- Czy wszystkie integracje HL7/FHIR mają testy conformance?
- Jakie są lokalne wymagania prawne poza HIPAA/RODO?
## Powiązania (meta)
- Key Documents: incident_response, change_management, backup_dr, privacy/security policies, hl7_fhir_integration.
- Key Document Structures: harmonogram operacji, playbook incydentowy, komunikacja, checklisty.
- Document Dependencies: CMDB, IAM, monitoring/observability, compliance.
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

- Kontekst i SLO oncall
- Alerty/detekcje i triage (klasyfikacja, FP handling)
- Eskalacje, komunikacja i kanały
- Utrzymanie SIEM/SOAR/logów (health checks)
- Raportowanie/oncall handover
- Postmortem i ciągłe doskonalenie
- Ryzyka i scenariusze awaryjne


## Szybkie powiązania
- security-operations
- tournament-operations-runbook
- streaming-operations-runbook
- search-operations-runbook
- scada-operations-runbook

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Wypełnij sekcje dopasowane do Twojego SOC; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; podlinkuj playbooki i kanały komunikacji.
- Aktualizuj po zmianach źródeł logów, narzędzi lub SLO.


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

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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
- Dashboardy, harmonogramy patch/backup, szablony komunikatów, listy kontaktów, logi audytu.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- IT Ops → Security/Compliance → Klinika → CAB/Owner sign‑off.
## Metryki jakości
- Dostępność (SLA), liczba incydentów klinicznych, czas reakcji/naprawy, sukces testów DR, wskaźniki audytu (log completeness, access recertification), defekty po patchach.
## Kryteria ukończenia
- [ ] Harmonogramy, playbooki i kontakty kompletne.
- [ ] Dowody backup/DR/testów dostępne.
- [ ] Dokument powiązany w linkage_index.jsonl i checklistach.
## Wejścia

- SLO SOC, playbooki i polityki komunikacji.
- Mapa alertów/detekcji i źródła logów.
- Ownerzy/eskalacje, kanały komunikacyjne, narzędzia SIEM/SOAR/ticketing.


## Wyjścia

- Runbook SOC i checklisty triage.
- Mapa eskalacji i komunikacji.
- Raporty statusu/oncall, linki do postmortem.



## Szybkie powiązania (uzupełnij)

- security_monitoring_strategy.md
- security_incident_response.md
- security_status_report.md
- logging_and_audit_trail.md
- audit_compliance.md
- security_posture_monitoring.md


## Wymagane rozwinięcia / streszczenia

- Checklisty triage i health-check SIEM/SOAR.
- Schemat eskalacji i komunikacji (kanały, czasy, ownerzy).
- Szablon handover i raportu oncall.


## Wymagane powiązania

- Playbooki IR, postmortem, status reporty, audyty.
- CMDB/inventory log sources, change management okna.


## Kryteria DoR

- [ ] Lista alertów/detekcji i klasyfikacja dostępna.
- [ ] Kanały i właściciele eskalacji uzgodnieni.
- [ ] Narzędzia SIEM/SOAR/ticketing skonfigurowane; konta dostępne.
- [ ] SLO/SLI oncall zdefiniowane.


## Kryteria DoD

- [ ] Checklisty triage i eskalacji opisane.
- [ ] Komunikacja i handover zdefiniowane.
- [ ] Health-check i utrzymanie narzędzi opisane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Checklisty triage/health-check.
- Schemat eskalacji/komunikacji.
- Handover template i przykładowe raporty oncall.
- Linki do postmortem.


## Walidacja / testy

- Dry-run triage/eskalacji; próbny alert.
- Peer review runbooku; weryfikacja kanałów komunikacyjnych.


## Metryki monitorowane

- MTTA/MTTR, % FP, liczba eskalacji.
- SLA oncall handover i raportów.
- Dostępność źródeł logów/narzędzi SOC.


## Utrzymanie i aktualizacje

- Przegląd co sprint/msc lub po incydencie/audytach.
- Aktualizuj mapę alertów i kanały po zmianach w usługach/narzędziach.


## Zakończenie

Po spełnieniu DoD podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i poinformuj zespół SOC o zmianach.
