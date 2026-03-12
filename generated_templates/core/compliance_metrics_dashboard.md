---
title: Compliance Metrics Dashboard
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance Metrics Dashboard


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować i utrzymywać dashboard metryk compliance (exec/ops/audit): KPI/KRI, stan kontrolek, wyjątki/waivery, alerty i raporty, zasilany automatycznie z systemów źródłowych, wspierający decyzje go/conditional/no‑go, priorytety remediacji i dowody audytowe.


## Zakres i granice

- Obejmuje: zakres regulacji/standardów i systemów, definicje KPI/KRI, źródła danych i ETL, widoki (executive/operational/audit), alerting i eskalację, repo dowodów/linki do SoA, harmonogram odświeżania, RACI utrzymania, jakość danych i tuningi.  
- Poza zakresem: projektowanie nowych kontrolek (w SoA/policies) i szczegółowe runbooki remediacji (w playbookach ops/IR).


## Użytkownicy i interesariusze
- SRE/Perf, Engineering, Product, Observability, Support, Exec (raporty).
## Wejścia i wyjścia

- Wejścia: SoA/kontrolki, wyjątki/waivery (sunset), risk register, vuln scans/SLA, SIEM/SOAR, IAM recertyfikacje, ticketing CAPA, CMDB, TPRM/SLA, DR/BCP testy, CI/CD quality gates, audyty (SOC2/PCI/HIPAA).  
- Wyjścia: dashboard (exec/ops/audit), alerty (sunset waiverów, overdue recert/scan/CAPA), export CSV/API, snapshoty do raportów zarządu/audytu/regulatora, sygnały do gatingu Release/Change i Risk & Issue Report.


## Założenia
- Narzędzia APM/monitoring i RBAC dostępne.  
- Katalog usług aktualny.  
- Zespoły on-call istnieją.
## Otwarte pytania
- Jak długo przechowywać historię zmian progów?  
- Czy potrzebne dashboardy per region/tenant?  
- Jak łączyć metryki techniczne z produktowymi na jednym panelu?
## Powiązania (meta)

- Key Documents: compliance_monitoring_tools, compliance_monitoring_runbook, compliance_with_regulations, compliance_verification, compliance_audit_report, mapowanie_compliance, risk_register, change_management_plan, security_controls_reference.
- Key Document Structures: KPI/KRI, źródła/ETL, alerty, widoki, raporty, jakość danych.
- Document Dependencies: źródła telemetryczne (SIEM/SOAR, SCA, IAM), GRC/ticketing, CMDB, SoA, ETL/DB/BI, runbooki alertów.



## Zależności dokumentu
Wymaga: listy usług i SLO, źródeł metryk, polityki alertów, narzędzia dashboard/APM, ról i dostępu. Brak = brak DoR.
## Fazy cyklu życia
- Definicja metryk i SLO.  
- Projekt dashboardu i alertów.  
- Wdrożenie i walidacja.  
- Operacje i przeglądy.  
- Aktualizacje i audyty.
## Struktura sekcji (szkielet)

- Podsumowanie wykonawcze
- Kluczowe metryki i KPI
- Trendy i analiza
- Problemy i rekomendacje
- Kolejne kroki

## Szybkie powiązania

- linkage_index.jsonl (compliance/metrics_dashboard)
- compliance_monitoring_tools, compliance_monitoring_runbook, compliance_with_regulations, compliance_verification, compliance_audit_report, mapowanie_compliance, risk_register, change_management_plan, security_controls_reference


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zdefiniuj zakres i KPI/KRI; stwórz słownik metryk i mapę kontrola→metryka.  
2. Opisz źródła/ETL, widoki, alerty i publikację; ustaw RACI i SLA danych.  
3. Dodaj walidacje jakości danych i plan napraw; zaktualizuj linkage_index/checklisty.


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
- SLO: target poziomu usługi.  
- Error budget: tolerowany poziom błędów.  
- Apdex: wskaźnik satysfakcji z czasu odpowiedzi.
## Przykłady użycia
- Dashboard usług API z latency/error rate i budżetem błędów.  
- Panel infrastruktury (CPU/mem/IO) z alertami saturacji.  
- Web vitals dla frontendu z Apdex/Synthetic.
## Ryzyka i ograniczenia
- Zbyt wiele alertów → szum.  
- Brak wersjonowania progów → trudne RCA.  
- Niespójne definicje metryk → złe decyzje.  
- Brak RBAC → nieautoryzowane zmiany progów.
## Decyzje i uzasadnienia
- Wybór metryk/SLO na dashboardzie.  
- Progi i kanały eskalacji.  
- Layout (kolejność, grupowanie).  
- Retencja i wersjonowanie zmian.
## Powiązania z innymi dokumentami
- Observability Standards, SLA/SLO Policy, API Performance Baseline, RUM Metrics Guidelines, Capacity Planning, Incident Response Plan.
## Powiązania z sekcjami innych dokumentów
- SLO Policy → progi; Observability → narzędzia; Release → regresje; Capacity → forecast.
## Słownik pojęć w dokumencie
- p95/p99, Burn-rate, Error rate, Web Vitals, QPS, Saturation.
## Wymagane odwołania do standardów
- Organizacyjne SLO/SLA, Web Vitals, ewentualne normy branżowe SLA.
## Mapa relacji sekcja→sekcja
- Ścieżki → Metryki → Progi/alerty → Segmentacja → Raporty → Tuning.
## Mapa relacji dokument→dokument
- Performance Metrics → Observability/SLO → Incident/Capacity → Release/Change.
## Ścieżki informacji
- Krytyczne ścieżki → Metryki → Alerty → Incydenty → Raporty → Korekta progów.
## Weryfikacja spójności

- [ ] KPI/KRI mają źródło, próg, ownera; mapowanie kontrola→metryka pełne.  
- [ ] Źródła danych mają SLA i walidacje; alerty pokrywają wyjątki i overdue.  
- [ ] Dokument w linkage_index; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Słownik metryk, mapa kontrola→metryka, schemat ETL, dashboardy, alert/runbook configs, log walidacji danych, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Perf → Engineering/Product → Observability → Owner sign‑off.
## Metryki jakości

- Terminowość danych vs SLA, % kontrolek z metryką, liczba braków danych, czas zamknięcia alertów, liczba waiverów i czas sunset, adopcja dashboardu (views/raporty).

## Kryteria ukończenia

- [ ] Dashboard i alerty działają, metryki/źródła opisane, eksport dostępny; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres dashboardu (regulacje/standardy, systemy, właściciele, odbiorcy)  
2) Definicje KPI/KRI (formuła, źródło, częstotliwość, progi/kolory, owner, link do dowodu)  
3) Źródła danych i ETL (listy źródeł, schema, SLA danych, walidacje, mapowanie SoA)  
4) Widoki i wizualizacje (executive/operational/audit; top ryzyka, overdue, dowody)  
5) Alerting i eskalacja (progi, kanały, runbooki, sunset wyjątków)  
6) Publikacja i cykl (częstotliwość odświeżania, dostępność, RACI utrzymania)  
7) Jakość danych (walidacje, kompletność, drift/spójność, plan napraw)  
8) Załączniki (słownik metryk, mapowanie kontrola→metryka, schemat ETL, szablony raportów)


## Wymagane rozwinięcia

- Słownik KPI/KRI z formułami, progami i właścicielami; mapa kontrola→metryka.  
- Lista źródeł i SLA danych; walidacje i plan napraw danych.  
- Progi/alerty i runbooki; harmonogram odświeżania i RACI utrzymania.  
- Widoki (exec/ops/audit) z zakresem i odbiorcami; eksport API/CSV.


## Wymagane streszczenia

- Executive snapshot: % kontrolek compliant, liczba wyjątków i czas do sunset, recert coverage, vuln/CAPA SLA, DR/BCP test coverage, nadchodzące audyty.


## Guidance (skrót)

- Definiuj KPI/KRI z jasnym źródłem i progiem; brak danych = alert.  
- Utrzymuj jeden słownik metryk i mapę kontrola→metryka; wersjonuj.  
- Waliduj dane i SLA; alertuj na spóźnione/niekompletne feedy.  
- Sunset wyjątków i overdue recert/scans/CAPA muszą być w alertach i widokach ops.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania KPI/KRI i odbiorcy znani; SoA/kontrolki dostępne.  
- [ ] Źródła danych i dostęp potwierdzone; wstępne progi/alerty uzgodnione.  
- [ ] Owner dashboardu i cadence odświeżania ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Słownik metryk, mapowanie kontrola→metryka i widoki opisane; alerty/runbooki działają.  
- [ ] SLA danych i walidacje ustawione; eksport API/CSV dostępny; dokument w linkage_index; metadane aktualne.

