---
title: Security Monitoring Strategy
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Monitoring Strategy


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Określić strategię monitorowania bezpieczeństwa: jakie zdarzenia i metryki zbierać, jak alertować, jak raportować i jak doskonalić.


## Zakres i granice

- Obejmuje: cele/SLO, zakres źródeł i zdarzeń, metryki/KPI/KRI, progi alertów, dashboardy/raporty, cykl przeglądów i integrację z procesami IR/SOC.
- Poza zakresem: implementacja poszczególnych fixów/zmian (oddzielne taski/runbooki).


## Użytkownicy i interesariusze
- SRE/Observability, Engineering, Product, Security/Privacy, FinOps.
## Wejścia i wyjścia
- Wejścia: katalog usług (CMDB), krytyczne ścieżki i zależności, SLO/SLA, mapa KPI biznesowych, standardy tagowania, wymagania compliance/audytu, budżet kosztów observability, narzędzia (Prometheus/Grafana/ELK/APM).
- Wyjścia: standard monitoringu (metryki/logi/traces), lista SLI/SLO z progami, macierz pokrycia (service x signal), standard alertów i eskalacji, dashboardy referencyjne, harmonogram przeglądów, plan optymalizacji kosztów i retencji.
## Założenia
- Stabilne źródła metryk/logów/traces i kontrola PII.  
- On‑call rota dostępna i aktualna.  
- Narzędzia wspierają etykiety/tagi i multi‑region.
## Otwarte pytania
- Czy wszystkie SLO muszą być customer‑facing czy tylko wewnętrzne?  
- Jakie synthetic tests są wymagane per krytyczna ścieżka?  
- Jakie limity kosztów są akceptowalne per usługa?
## Powiązania (meta)
- Key Documents: incident_response_runbook, service_level_objectives, observability_architecture, logging_standards, alerting_policy, cost_management_observability.
- Key Document Structures: sygnały (metrics/logs/traces), SLI/SLO, alerting, dashboardy, runbooki, koszt/retencja.
- Document Dependencies: CMDB/usługi, katalog zależności, narzędzia monitoringowe, system ticketowy, on‑call rota, polityki bezpieczeństwa danych.
## Zależności dokumentu
Wymaga: aktualnego CMDB/katalogu usług, zdefiniowanych SLO/SLA, przyjętych standardów tagowania i retencji, dostępów do narzędzi monitoringu/logowania/APM. Braki = DoR otwarte.
## Fazy cyklu życia
- Definicja strategii i priorytetów (services tiering).  
- Rollout standardów monitoringu i alertów.  
- Ciągłe przeglądy: coverage, fałszywe alarmy, koszty, audyty.  
- Ewolucja narzędzi/architektury observability.
## Struktura sekcji (szkielet)

- Kontekst, cele i SLO
- Źródła logów/metryk i zakres zbierania
- Metryki/KPI/KRI i definicje progów
- Alerty i procedury (triage, FP handling)
- Dashboardy/raporty i częstotliwość
- Integracja z SOC/IR i playbooki
- Przeglądy, ulepszenia i backlog


## Szybkie powiązania
- security-strategy
- system-monitoring-strategy
- sli-monitoring-strategy
- service-monitoring-strategy
- security-strategy-document

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
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

- Zmapuj źródła i metryki, zdefiniuj progi i alerty; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Uzgodnij integrację z SOC/IR i harmonogram przeglądów, podlinkuj dashboardy.


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
- SLI: mierzalny wskaźnik jakości usługi (np. availability 99.9%, latency p95).  
- SLO: cel dla SLI w okresie (np. 99.9% / 28 dni).  
- Error budget: 1 − SLO; budżet na zmiany/awarie.
## Przykłady użycia
- Zmiana architektury logowania — ocena kosztów i tagów.  
- Nowa usługa Tier1 — nadanie SLI/SLO i alertów.  
- Post‑mortem fałszywych alarmów — tuning progów i reguł.
## Ryzyka i ograniczenia
- Alert fatigue z nadmiarem reguł lub złymi progami.  
- Brak standardu tagów uniemożliwia pivotowanie danych.  
- Niekontrolowane koszty retencji/indeksów.
## Decyzje i uzasadnienia
- Zakres SLO (global vs per region) — zależnie od architektury.  
- Retencja logów/traces — kompromis koszt vs potrzeba audytu/IR.  
- Sampling/aggregation — kompromis dokładność vs koszt.
## Powiązania z innymi dokumentami
- incident_response_runbook — reakcja na alerty.  
- logging_standards — formaty i PII.  
- cost_management_observability — budżet i optymalizacje.
## Powiązania z sekcjami innych dokumentów
- SLO Policy → progi; IR → eskalacje; Privacy → logi/trace redakcja.
## Słownik pojęć w dokumencie
- Golden signals, Burn-rate, Error budget, Sampling, Retention, RUM, APM.
## Wymagane odwołania do standardów
- ISO 27001 / SOC2 (logowanie, audyt).  
- Wewnętrzne standardy PII/RODO i retencji.
## Mapa relacji sekcja→sekcja
- Ścieżki/SLO → Sygnały → Progi/alerty → Runbooki → Raporty → Tuning.
## Mapa relacji dokument→dokument
- Monitoring Strategy → Observability/SLO → Incident/Performance → Cost/Privacy.
## Ścieżki informacji
- SLO → Metryki → Alerty → Incydent → Raport → Korekta progów.
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
- Dashboardy, alert config, runbooki, testy alertów, raporty, koszt/retencja ustawienia.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Observability → Engineering/Product → Privacy/FinOps → Owner sign‑off.
## Metryki jakości
- MTTR, liczba fałszywych alertów, pokrycie ścieżek krytycznych, koszt observability, zgodność z SLO, częstotliwość testów alertów.
## Kryteria ukończenia
- [ ] Strategia opisana; alerty/dashboards/runbooki/testy zdefiniowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Wejścia

- Polityki bezpieczeństwa, SLO i apetyt na ryzyko.
- Mapa usług, źródeł logów/metryk, scenariusze zagrożeń.
- Historia incydentów/alertów i wyniki audytów.


## Wyjścia

- Plan metryk, zdarzeń i alertów.
- Dashboardy i raporty cykliczne.
- Harmonogram przeglądów i action log.



## Szybkie powiązania (uzupełnij)

- security_operations.md
- security_incident_response.md
- logging_and_audit_trail.md
- security_posture_monitoring.md
- devsecops_pipeline.md
- security_compliance_matrix.md


## Wymagane rozwinięcia / streszczenia

- Tabela: źródło → zdarzenia/metryki → progi → właściciel → kanał alertu.
- Streszczenie głównych KPI/KRI i planu przeglądów.


## Wymagane powiązania

- Runbooki SOC/IR, compliance matrix, rejestr ryzyk, polityki logowania.
- Playbooki triage/FP i katalog alertów.


## Kryteria DoR

- [ ] Lista źródeł i scenariuszy zagrożeń zebrana.
- [ ] Cele/SLO i apetyt na ryzyko uzgodnione.
- [ ] Odbiorcy alertów/raportów zidentyfikowani.


## Kryteria DoD

- [ ] Plan metryk/alertów opisany, progi zdefiniowane.
- [ ] Dashboardy/raporty podlinkowane; integracja z SOC/IR opisana.
- [ ] Przeglądy i backlog ulepszeń wpisane; quick-links/checklisty zaktualizowane.


## Artefakty do załączenia

- Katalog źródeł i zdarzeń.
- Tabela KPI/KRI i progi alertów.
- Dashboardy i harmonogram przeglądów.


## Walidacja / testy

- Test alertów/progów na próbce; sanity duplikatów/FP.
- Peer review planu z SOC/IR i właścicielami usług.


## Metryki monitorowane

- Pokrycie logowania/metryk per usługa.
- Liczba alertów FP/TP; czas triage/MTTA/MTTR.
- SLA raportowania/przeglądów; trend KPI/KRI.


## Utrzymanie i aktualizacje

- Przeglądy cykliczne (np. kwartalnie) i po incydentach/audytach.
- Aktualizuj progi i źródła po zmianach architektury/ryzyk.


## Zakończenie

Po spełnieniu DoD opublikuj plan, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zsynchronizuj z runbookami SOC/IR.
