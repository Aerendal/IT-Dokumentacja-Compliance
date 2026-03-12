---
title: Security Operations
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Operations


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Model operacyjny bezpieczeństwa (SOC/SIEM/SOAR): procesy detekcji i reakcji, role, narzędzia, KPI i komunikacja z IT/produkt.


## Zakres i granice

- Obejmuje: zakres SOC, procesy detekcja→triage→response→postmortem, role/RACI, narzędzia i integracje, KPI/SLO, komunikację i przeglądy.
- Poza zakresem: szczegółowe playbooki incydentów (oddzielne dokumenty), konfiguracja narzędzi per usługa.


## Użytkownicy i interesariusze
- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.
## Wejścia i wyjścia
- Wejścia: polityki ryzyka/limity, regulacje jurysdykcji, specyfikacje giełd/venue, mapy systemów (OMS/EMS/risk/market data), SLA latencji, procedury BCP/DR, rejestr wyjątków, logi/audyt, listy kontaktów.
- Wyjścia: procedury operacyjne i checklisty, konfiguracje limitów/kill switch, playbooki incydentów, raporty zgodności, harmonogramy reconciliation, metryki operacyjne, plan testów DR.
## Założenia
- Dostępne są runbooki vendorów i aktualne listy kontaktów.
- Monitoring i backup są wdrożone w środowisku docelowym.
## Otwarte pytania
- Czy wszystkie integracje HL7/FHIR mają testy conformance?
- Jakie są lokalne wymagania prawne poza HIPAA/RODO?
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

- Kontekst i zakres SOC
- Procesy (detect/triage/respond/recover) i RACI
- Narzędzia, źródła logów i integracje
- KPI/SLO i raportowanie
- Komunikacja i eskalacje
- Ryzyka i ciągłe doskonalenie


## Szybkie powiązania
- security-operations-runbook
- vm-security-hardening
- venue-operations
- training-operations
- trading-operations

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

- Opisz zakres i procesy, zmapuj role/RACI i źródła logów; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; podlinkuj runbooki i KPI.
- Aktualizuj po zmianach narzędzi, usług lub wnioskach z postmortem.


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

- Polityki bezpieczeństwa, wymagania regulacyjne.
- Mapa usług/assetów/danych i źródła logów.
- Narzędzia SOC (SIEM, SOAR, EDR, ticketing) i ich wersje.
- Rejestr incydentów/KPI, lessons learned.


## Wyjścia

- Model operacyjny i RACI.
- Procesy i integracje narzędzi.
- KPI/SLO, raporty statusu i cykl przeglądów.
- Powiązania do runbooków i postmortem.



## Szybkie powiązania (uzupełnij)

- security_monitoring_strategy.md
- security_incident_response.md
- security_operations_runbook.md
- security_status_report.md
- logging_and_audit_trail.md
- security_posture_monitoring.md


## Wymagane rozwinięcia / streszczenia

- Diagramy procesów i przepływów alertów.
- Tabela RACI dla kluczowych kroków (triage, eskalacja, komunikacja, zamknięcie).
- Streszczenie KPI/SLO i progów alertów.


## Wymagane powiązania

- Strategia monitoringu, runbooki incydentów, status reporty, postmortem, compliance/audyty.
- Katalog źródeł logów i kontrolki integralności/logowania.


## Kryteria DoR

- [ ] Zakres SOC i źródła logów zebrane.
- [ ] Role i eskalacje uzgodnione.
- [ ] Narzędzia/integracje dostępne.
- [ ] Wstępne KPI/SLO zdefiniowane.


## Kryteria DoD

- [ ] Procesy i RACI opisane, KPI/SLO dodane.
- [ ] Narzędzia i źródła logów podlinkowane.
- [ ] Raportowanie/przeglądy zdefiniowane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Mapy procesów i eskalacji.
- Lista źródeł logów i integracji.
- Dashboardy KPI/SLO.
- Linki do runbooków i postmortem.


## Walidacja / testy

- Próbny triage/alert end-to-end.
- Peer review procesów i RACI.


## Metryki monitorowane

- MTTA/MTTR, % alertów false-positive, coverage logów.
- SLA raportowania i przeglądów.
- Liczba eskalacji i naruszeń SLO.


## Utrzymanie i aktualizacje

- Przeglądy co sprint/msc lub po incydencie/audytach.
- Aktualizuj integracje i źródła logów; rewiduj KPI/SLO.


## Zakończenie

Po spełnieniu DoD podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zakomunikuj zmiany interesariuszom.
