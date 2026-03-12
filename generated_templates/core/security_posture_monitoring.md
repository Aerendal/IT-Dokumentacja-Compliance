---
title: Security Posture Monitoring
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Posture Monitoring


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Monitorować postawę bezpieczeństwa (kontrolki, luki, KPI) i wykrywać degradacje w sposób ciągły.


## Zakres i granice

- Obejmuje: definicje KPI/posture, źródła danych i dowodów, alerty/degradacje, dashboardy/raporty, przeglądy i plan działań.
- Poza zakresem: implementacja konkretnych poprawek (osobne taski/backlogi).


## Użytkownicy i interesariusze
- SRE/Observability, Engineering, Product, Security/Privacy, FinOps.
## Wejścia i wyjścia
- Wejścia: buildy i wersje, device matrix, sceny referencyjne, narzędzia telemetry, SLO (FPS/frametime), zmiany assetów/kodu, dane prod i lab.
- Wyjścia: konfiguracja telemetry (sampling, eventy), dashboardy i alerty, raporty wersja→FPS, lista regresji, plan testów syntetycznych, rekomendacje optymalizacji.
## Założenia
- Stabilne źródła metryk/logów/traces i kontrola PII.  
- On‑call rota dostępna i aktualna.  
- Narzędzia wspierają etykiety/tagi i multi‑region.
## Otwarte pytania
- Czy wszystkie SLO muszą być customer‑facing czy tylko wewnętrzne?  
- Jakie synthetic tests są wymagane per krytyczna ścieżka?  
- Jakie limity kosztów są akceptowalne per usługa?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
Wskaż: device matrix, sceny referencyjne, telemetry stack, SLO, build pipeline, privacy policy (telemetry); brak – odnotuj.
## Fazy cyklu życia
Plan → Instrumentacja → Testy syntetyczne → Rollout telemetry → Monitoring/alerty → Raporty i optymalizacje.
## Struktura sekcji (szkielet)

- Kontekst i zakres monitoringu
- KPI/metryki posture i progi
- Źródła danych, dowody i jakość danych
- Alerty, degradacje i obsługa wyjątków
- Dashboardy/raporty i częstotliwość przeglądów
- Plan działań, właściciele i SLA
- Ryzyka i usprawnienia


## Szybkie powiązania
- security-monitoring-strategy
- vm-security-hardening
- vm-performance-monitoring
- transaction-monitoring
- throughput-monitoring

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

- Zdefiniuj KPI i progi, podłącz źródła danych; opisz alerty i obsługę wyjątków.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Publikuj raporty cyklicznie i aktualizuj plan działań po każdym przeglądzie.


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

- Katalog kontrolek i benchmarki zgodności.
- Źródła dowodów/logów (SIEM, scan, CMDB/IaC, ticketing).
- Raporty audytów i incydenty, rejestr ryzyk.


## Wyjścia

- Dashboard posture i alerty.
- Raporty statusu (cykliczne) i wyjątków.
- Plan działań naprawczych i właściciele.



## Szybkie powiązania (uzupełnij)

- security_compliance_matrix.md
- security_status_report.md
- security_controls_implementation.md
- logging_and_audit_trail.md
- devsecops_pipeline.md
- risk_management_framework.md


## Wymagane rozwinięcia / streszczenia

- Definicje metryk (wzory, źródła, progi) i tabela wyjątków.
- Streszczenie posture: top luki, trend KPI, kluczowe akcje.


## Wymagane powiązania

- Rejestr ryzyk, compliance matrix, incydenty i audyty.
- Plan remediacji/owners, runbook alertów.


## Kryteria DoR

- [ ] KPI/progi uzgodnione, źródła danych dostępne.
- [ ] Katalog kontrolek i mapping do źródeł gotowy.
- [ ] Ownerzy monitoringu i cykl przeglądów ustalone.


## Kryteria DoD

- [ ] Dashboard/raport wypełniony i opublikowany.
- [ ] Alerty i wyjątki opisane, action plan przypisany.
- [ ] Trendy dodane, quick-links/checklisty zaktualizowane.


## Artefakty do załączenia

- Dashboardy i raporty posture.
- Lista KPI z definicjami/progami.
- Action log i rejestr wyjątków.


## Walidacja / testy

- Sanity danych (świeżość, jakość, duplikaty/FP).
- Peer review metryk i progów; porównanie z poprzednim okresem.


## Metryki monitorowane

- % kontrolek zgodnych; liczba luk (Critical/High/Med/Low).
- Trend KPI posture (np. CIS coverage, patch compliance, MFA adoption).
- SLA reakcji na alerty posture; liczba otwartych wyjątków i ich wiek.


## Utrzymanie i aktualizacje

- Przeglądy cykliczne (np. tyg./mies.) i po incydentach/audytach.
- Aktualizuj KPI/progi przy zmianach architektury lub ryzyka.


## Zakończenie

Po spełnieniu DoD opublikuj raport, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przypisz działania właścicielom.
