---
title: Green IT Improvement Plan
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Green IT Improvement Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan działań obniżających ślad środowiskowy IT: cele/KPI, inicjatywy, harmonogram, monitoring i ryzyka/kompromisy.


## Zakres i granice

- Obejmuje: cele/KPI (energia/CO₂/koszt per transakcja/usługa), inicjatywy (right-sizing, hibernacja, storage lifecycle, optymalizacje danych/ML, regiony niskoemisyjne, efektywność sieci/CDN, chłodzenie), priorytety/roadmapa, monitoring/raporty, ryzyka/kompromisy (latencja vs region, koszt vs oszczędność CO₂).  
- Poza zakresem: ESG raport korporacyjny (osobny), offsety poza IT.


## Użytkownicy i interesariusze
- Streaming/Video Eng, SRE/Observability, Product, Ads/Monetization, FinOps, Security/DRM.
## Wejścia i wyjścia

- Wejścia: zużycie energii/CO₂ (cloud/on-prem), koszt, profile obciążenia, metryki perf/latencji, polityki korporacyjne ESG, mapy regionów/źródeł energii, budżet/zasoby.  
- Wyjścia: lista inicjatyw z KPI/owner/ETA, roadmapa (kwartały), dashboardy postępu, raporty do ESG/FinOps, decyzje go/conditional/no‑go dla inicjatyw.


## Założenia
- Monitoring/logi QoE i kosztów dostępne; flags/rollout kontrolowane.
## Otwarte pytania
- Jakie są progi akceptowalne QoE per region/ISP/device?
- Jak łączymy QoE i FinOps w decyzjach (np. cost/quality routing)?
## Powiązania (meta)

- Key Documents: finops_policy, capacity_planning, performance_testing_plan, data_lifecycle_policy, backup_and_retention, cloud_migration_plan, risk_register, esg_reporting_guidelines.
- Key Document Structures: cele/KPI, inicjatywy, roadmapa, monitoring, ryzyka.
- Document Dependencies: telemetry zużycia energii/CO₂ (cloud/billing/APIs), CMDB/tagging, monitoring perf, budgeting/FinOps, data lifecycle.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie: cele, zakres, założenia.
- Planowanie: sekwencja prac, zasoby, daty.
- Realizacja: monitoring postępu, decyzje go/stop.
- Zamknięcie: retrospektywa, aktualizacja planów.
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

- linkage_index.jsonl (sustainability/green_it_plan)
- finops_policy, capacity_planning, performance_testing_plan, data_lifecycle_policy, backup_and_retention, cloud_migration_plan, risk_register, esg_reporting_guidelines


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
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

1. Ustal baseline i KPI; wybierz inicjatywy i priorytety.  
2. Zbuduj roadmapę i budżet; ustaw monitoring/raporty.  
3. Wdrażaj, mierz, raportuj; aktualizuj plan i linkage_index.


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
- QoE, Rebuffer, Startup time, ABR ladder, CDN hit/miss, Canary, FinOps KPI.
## Przykłady użycia
- Redukcja rebufferu w regionie X: switch CDN, zmiana ABR, ads timeout, canary.
- Obniżenie kosztu CDN: origin shield + cache rules, przy zachowaniu QoE.
## Ryzyka i ograniczenia
- Brak danych segmentacyjnych → złe priorytety; brak rollback → regresje.
- Optymalizacje kosztowe mogą pogorszyć QoE; testuj i mierz.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Streaming Platform, Live Streaming Implementation, Observability QoE, DRM/Ads/CDN policies, Cost Optimization.
## Powiązania z sekcjami innych dokumentów
- Observability QoE → metryki; CDN Strategy → routing; Cost → optymalizacje.
## Słownik pojęć w dokumencie
- QoE, Rebuffer, Startup, ABR, CDN, Canary, FinOps.
## Wymagane odwołania do standardów
- HLS/DASH/CMAF, DRM/ads standardy, polityki QoE/SLA firmy.
## Mapa relacji sekcja→sekcja
- Problemy → Backlog → Testy/Rollout → Monitoring → Raport → Korekta.
## Mapa relacji dokument→dokument
- Improvement Plan → Platform/Live/Observability/CDN/DRM/Ads → Cost Optimization.
## Ścieżki informacji
- Metryki → Problemy → Backlog → Rollout → Monitoring → Raport → Iteracja.
## Weryfikacja spójności

- [ ] KPI/cele spójne z danymi baseline; inicjatywy mają ROI/CO₂e i właścicieli.  
- [ ] Raporty/dash działają; ryzyka/kompromisy opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Baseline/target KPI, lista inicjatyw, kalkulacje CO₂e/ROI, dashboardy, raporty ESG/FinOps, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Streaming/SRE → Product/Ads → FinOps/Security → Owner sign‑off.
## Metryki jakości

- % targetu CO₂e/koszt osiągnięty, liczba inicjatyw on-track, wpływ na perf/latencję, liczba rollbacków, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Plan zielonego IT z celami, inicjatywami, monitoringiem i roadmapą gotowy; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Cele i KPI (energia, CO₂e, koszt per usługa/txn)  
2) Inicjatywy i priorytety (right-sizing, hibernacja, storage lifecycle, dane/ML opt, regiony low-carbon, sieć/CDN, chłodzenie)  
3) Roadmapa i właściciele (kwartały, budżet, zależności)  
4) Monitoring i raportowanie (metryki, dashboardy, cadence, odbiorcy ESG/FinOps)  
5) Ryzyka i kompromisy (latencja vs region, koszt vs oszczędność, jakość usług)  
6) Załączniki (baseline zużycia, kalkulacje CO₂, decyzje, log inicjatyw)


## Wymagane rozwinięcia

- Baseline i targety KPI; metodologia liczenia CO₂e (cloud carbon/energy mix).  
- Lista inicjatyw z ROI/CO₂e saved, koszt, ryzyko; priorytetyzacja (ICE/ROI).  
- Dashboard metryk i częstotliwość raportów; wymagania tagowania/CMDB.  
- Kryteria go/conditional/no‑go i regresje perf/latencja.


## Wymagane streszczenia

- Executive: targety KPI, top inicjatywy i spodziewane oszczędności CO₂/koszt, harmonogram, ryzyka.


## Guidance (skrót)

- Zacznij od tagowania/CMDB i baseline; bez tego nie zmierzysz efektu.  
- Priorytetyzuj wg CO₂e/koszt vs wpływ na perf/UX; rób eksperymenty (A/B regionów/rozmiarów).  
- Ustal guardrails perf/latencji; rollback jeśli przekroczone.  
- Raportuj regularnie do ESG/FinOps; pilnuj sunset dla wyjątków.


## Checklisty Definition of Ready (DoR)

- [ ] Baseline zużycia/CO₂ i tagowanie/CMDB gotowe; polityki ESG/FinOps znane.  
- [ ] Wstępna lista inicjatyw i metodyka liczenia CO₂ uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] KPI/cele zapisane; roadmapa i właściciele; dashboardy/raporty działają.  
- [ ] Inicjatywy mają ROI/CO₂e, plan i status; dokument w linkage_index; metadane aktualne.

