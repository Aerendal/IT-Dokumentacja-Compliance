---
title: Resource Utilization Monitoring
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Resource Utilization Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje monitorowanie wykorzystania zasobów (CPU/RAM/IO/NET/storage) dla usług/systemów: metryki, alerty, raporty i optymalizacje. Celem jest stabilność, zgodność z SLO i kontrola kosztów.


## Zakres i granice

- Obejmuje: metryki i SLO/SLA (p95/p99, saturation), limity i quotas, tagowanie kosztów, zbieranie i agregację (agent/telemetry), alerty i progi, dashboardy, raporty FinOps, anomalia/capacity planning, noise reduction, retencję danych, integrację z incident/change.  
- Poza zakresem: szczegółowe profile aplikacji (osobne dokumenty perf).


## Użytkownicy i interesariusze
- SRE/Infra, FinOps, Security/Compliance, Product/Teams właściciele danych, Leadership.
## Wejścia i wyjścia

- Wejścia: architektura usług, SLO, profile ruchu, limity dostawcy, koszty, CMDB, zdarzenia deploy/incydent.  
- Wyjścia: standard metryk, progi alertów, dashboardy, raporty wykorzystania/kosztów, rekomendacje optymalizacji, checklisty DoR/DoD.


## Założenia

- Telemetry i billing dostępne.  
- Zespoły ops/finops współpracują.  
- CMDB aktualna.


## Otwarte pytania

- Jakie SLO na resource utilization?  
- Czy potrzebne alerty per tenant/region?  
- Jak włączyć automatyczne rightsizing?


## Powiązania (meta)

- Key Documents: observability_plan, capacity_planning, finops_policy, performance_test_plan, incident_response_runbook, scaling_policies.  
- Key Document Structures: metryki, alerty, dashboardy, raporty, optymalizacje.  
- Document Dependencies: telemetry stack, CMDB, billing, CI/CD, ticketing.


## Zależności dokumentu

Wymaga: SLO i profili ruchu, CMDB, dostępu do telemetry/billing, limitów/quotas, polityk FinOps, kanałów alertów. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja metryk i progów.  
- Implementacja zbierania/alertów/dashboardów.  
- Operacje i tuning.  
- Przeglądy okresowe (koszt/SLO) i optymalizacje.



## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (resource/utilization/monitoring)  
- observability_plan, capacity_planning, finops_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Ustal metryki/progi per usługa; wdroż zbieranie i alerty.  
2. Zbuduj dashboardy/raporty; monitoruj, reaguj, optymalizuj.  
3. Przeglądaj progi/SLO/koszt kwartalnie; aktualizuj DoR/DoD i linkage_index.


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

- Saturation: poziom zbliżenia do limitu zasobu.  
- Rightsizing: dostosowanie zasobów do potrzeb.  
- Noise reduction: techniki ograniczające fałszywe/nadmierne alerty.


## Przykłady użycia

- Monitoring CPU/RAM/IO dla mikrousług; alerty SLO.  
- Raport FinOps: koszt vs wykorzystanie, rekomendacje rightsizing.  
- Tuning progów po incydencie wydajności.


## Ryzyka i ograniczenia

- Alert fatigue przy złych progach.  
- Brak retencji → zły forecast capacity.  
- Brak tagów kosztów → brak odpowiedzialności za koszty.


## Decyzje i uzasadnienia

- Zakres SLO vs koszt monitoringu.  
- Retencja danych a koszt storage.  
- Polityka alertów (saturation/SLO vs raw).


## Powiązania z innymi dokumentami

- performance_test_plan — dane do progów.  
- incident_response_runbook — reakcja na alerty.  
- scaling_policies — progi autoscaling.


## Powiązania z sekcjami innych dokumentów
- Tagging → właściciele; Lifecycle → retencja/tiering; Security → public access/szyfrowanie.
## Słownik pojęć w dokumencie
- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.
## Wymagane odwołania do standardów

- Wewnętrzne standardy observability/FinOps.  
- Ewentualne wymogi regulatorów dot. capacity/availability.

## Mapa relacji sekcja→sekcja
- Metryki/KPI → Ryzyka → Rekomendacje → Plan działań → Follow‑up.
## Mapa relacji dokument→dokument
- Storage Report → FinOps/Lifecycle/Security → Capacity/DR → Audit/Compliance.
## Ścieżki informacji
- Metryki/billing → Analiza → Rekomendacje → Plan → Follow‑up → Kolejny raport.
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
- Dashboardy storage/billing, surowe dane, listy tagów/owners, plan działań, raport PDF/BI.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Infra → FinOps → Security/Compliance → Leadership/Owner sign‑off.
## Metryki jakości
- Dokładność danych vs billing, tempo realizacji rekomendacji, zmiana kosztów/pojemności, liczba otwartych wyjątków, public exposure findings.
## Kryteria ukończenia
- [ ] Raport opublikowany; rekomendacje/owner/ETA zapisane; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Metryki → Alerty → Incident → Optymalizacje.  
- Koszt/FinOps → Raporty → Capacity planning.  
- Deploy/incydent → Anomalia → Tuning progów.


## Struktura sekcji

1) Zakres usług i SLO/SLA  
2) Metryki i progi (CPU/RAM/IO/NET/storage, saturation)  
3) Zbieranie/telemetry i retencja (agent, sampling)  
4) Alerty i eskalacje (progi, noise reduction, channels)  
5) Dashboardy i raporty (ops, finops, exec)  
6) Anomalie i capacity planning (forecast, rightsizing)  
7) Integracje (incident/change, billing, CI/CD)  
8) Optymalizacje i rekomendacje (cache, limits, tuning)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela metryk/progów per usługa/rola.  
- Szablon dashboardów i raportów (ops/exec/finops).  
- Procedura noise reduction (grouping, SLO-based alerts).  
- Plan przeglądów SLO/kosztów kwartalnie.


## Wymagane streszczenia

- Executive snapshot: wykorzystanie vs SLO, top bottlenecki, koszt.  
- Karta alertów krytycznych (progi, kanały, ownerzy).


## Guidance (skrót)

- Alerty na SLO/saturation, nie tylko surowe wykorzystanie.  
- Koreluj z deployami/incydentami; unikaj alert fatigue.  
- Używaj taggingu kosztów i raportów rightsizing.  
- Regularnie przeglądaj progi; sezonowość ma znaczenie.  
- Zapewnij retencję danych wystarczającą do capacity planning.


## Checklisty Definition of Ready (DoR)

- [ ] SLO i profil ruchu znane; usługi w CMDB.  
- [ ] Telemetry stack i billing dostępne.  
- [ ] Limity/quotas zebrane.  
- [ ] Kanały alertów ustalone; noise policy przygotowana.  
- [ ] Plan dashboardów/raportów uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/progi/alerty aktywne; status/wersja/data uzupełnione.  
- [ ] Dashboardy/raporty opublikowane; tagowanie kosztów działa.  
- [ ] Noise reduction wdrożone; wyjątki opisane.  
- [ ] Zalecenia optymalizacji zapisane; linkage_index uzupełniony.  
- [ ] Plan przeglądów okresowych zapisany.

