---
title: Prediction Quality Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Prediction Quality Monitoring


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje monitorowanie jakości predykcji modeli ML po wdrożeniu: metryki, drift, alerty, dane referencyjne, retesty i decyzje (retrain/rollback). Ma ograniczyć degradację jakości i ryzyko biznesowe.


## Zakres i granice

- Obejmuje: metryki jakości (Accuracy/Precision/Recall/F1/AUC/MAE/MAPE itp.), dane referencyjne i okna czasowe, drift danych/modelu (PSI/KS/JS), bias/fairness (jeśli dotyczy), sampling/logging, etykietowanie zwrotne/feedback loop, alerty i progi, dashboardy, działania (retrain/rollback/threshold tuning), privacy/PII, koszty monitoringu.
- Poza zakresem: trening modeli (osobne), bezpieczeństwo modeli (oddzielny dokument – model governance/security).


## Użytkownicy i interesariusze

- Data/ML/Ops, Product, Security/Privacy, Compliance, Business Owners.


## Wejścia i wyjścia

- Wejścia: dane predykcji i cech, prawda referencyjna (labels) lub proxy, metryki SLO modelu, dane referencyjne (train/val), konfiguracje progu/thresholdów, polityka privacy, koszty logowania, release/feature flags.
- Wyjścia: dashboardy i alerty, raporty trendów, decyzje (retrain/rollback/threshold), backlog poprawek, log audytu, plan etykietowania zwrotnego.


## Założenia

- Dostępny model registry, logging, dane referencyjne; polityki privacy obowiązują.


## Otwarte pytania

- Jaki maks. delay etykiet jest akceptowalny? 
- Jak łączymy alerty jakości z alertami kosztu/latency?


## Powiązania (meta)

- Key Documents: model_card, model_governance, observability_ml, data_quality_policy, retraining_plan, incident_response_ml.
- Key Document Structures: metryki, drift, alerty, działania, audyt.
- Document Dependencies: model registry, logging/metrics, data store, labeling/feedback system, feature store, flags/rollout.


## Zależności dokumentu

Wymaga: SLO/metryk modelu, danych referencyjnych, mechanizmu logowania predykcji/cech, etykiet lub proxy, polityki privacy, narzędzi drift/bias. Bez tego DoR otwarte.


## Fazy cyklu życia

- Definicja metryk/SLO i danych referencyjnych.
- Konfiguracja logowania/sampling i drift/bias monitoringu.
- Alerty i runbooki działań (retrain/rollback/tuning).
- Raporty i przeglądy; aktualizacja progów i planów retrain.



## Struktura sekcji (szkielet)
- Kontekst i krytyczne dane
- Metryki/reguły
- Alerty/progi/sampling
- Dashboardy/raporty
- Incydenty i follow-up
- Ryzyka
## Szybkie powiązania

- linkage_index.jsonl (ml/prediction_monitoring)
- model_card, model_governance, observability_ml, data_quality_policy, retraining_plan, incident_response_ml


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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

1. Zdefiniuj metryki/SLO i dane referencyjne; ustaw logowanie/sampling.
2. Skonfiguruj drift/bias i alerty; przygotuj runbooki działań.
3. Publikuj dashboardy/raporty; audituj wersje i decyzje.
4. Aktualizuj progi i plany retrain po incydentach/przeglądach.


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

- Drift (PSI/KS/JS), Delay etykiet, SLO modelu, Threshold, Rollback.


## Przykłady użycia

- Model scoringu: alert na spadek AUC >5% i PSI cech >0.2; decyzja retrain/rollback.
- Model rekomendacji: monitor CTR, coverage i drift cech; tuning threshold.


## Ryzyka i ograniczenia

- Brak etykiet → brak walidacji; koszt logowania; fałszywe alerty driftu.


## Decyzje i uzasadnienia

- [Decyzja] Metryki/progi → uzasadnienie wpływu biznes/SLO.
- [Decyzja] Sampling/logging vs koszt/privacy → uzasadnienie ryzyka.


## Powiązania z innymi dokumentami

- Model Card, Model Governance, Observability ML, Data Quality Policy, Retraining Plan, Incident Response ML.


## Powiązania z sekcjami innych dokumentów

- Model Card → metryki; Data Quality → dane referencyjne; IR ML → runbook alertów.


## Słownik pojęć w dokumencie

- Drift, PSI, KS, JS, SLO modelu, Threshold, Rollback.


## Wymagane odwołania do standardów

- Polityki privacy/PII, standardy monitoringu ML, wewn. SLO/SLA.


## Mapa relacji sekcja→sekcja

- Metryki/SLO → Alerty → Działania → Raporty → Korekta progów.


## Mapa relacji dokument→dokument

- Prediction Monitoring → Model Governance/Observability/Retraining → Incident Response ML.


## Ścieżki informacji

- Logi/metryki → Alert → Działanie → Raport → Update progów/planów.


## Weryfikacja spójności

- [ ] Metryki/progi i drift ustawione; runbooki gotowe; privacy/koszt ujęte.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy alert ma próg, owner, runbook; każda metryka ma źródło i okno.
- [ ] Każda decyzja (retrain/rollback) ma dowód i wpis w audycie.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy, alert config, logi/metryki, model registry wpisy, runbooki, raporty.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Data/ML → Ops/SRE → Privacy/Compliance → Product/Owner sign‑off.


## Metryki jakości

- MTTA/MTTR dla degradacji, odsetek alertów uzasadnionych, czas do retrain/rollback, koszt logowania/sampling, zgodność privacy.

## Kryteria ukończenia

- [ ] Monitoring metryk/drift/bias działa; runbooki i audyt opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Metryki → Alerty → Działania (retrain/rollback/threshold) → Raporty.
- Dane referencyjne → Drift → Decyzje.


## Struktura sekcji

1) Metryki jakości i SLO (definicje, okna, progi)  
2) Dane referencyjne i prawda (labels/proxy, okna, latency)  
3) Drift i bias (metryki, progi, okna)  
4) Logging/sampling i privacy (PII, retention, koszt)  
5) Alerty i runbook działań (retrain, threshold, rollback)  
6) Dashboardy i raporty (cadence, odbiorcy)  
7) Audyt i ślad (wersje modelu, dane, decyzje)  
8) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Lista metryk i progów; okna czasowe; mapowanie do SLO biznes/technicznych.
- Dane referencyjne: źródła, opóźnienie etykiet, jakość; drift: PSI/KS/JS, progi.
- Runbook: co robić przy alertach (retrain/rollback/threshold), warunki go/no-go.


## Wymagane streszczenia

- Aktualne metryki vs SLO, drift status, otwarte alerty i działania.


## Guidance (skrót)

- Mierz to, co wpływa na decyzje biznesowe; definiuj progi na p95/p99 i trend.
- Loguj cechy/predykcje z kontrolą PII; ogranicz sampling dla kosztu.
- Włącz drift i delay etykiet w alertach; miej runbook retrain/rollback.
- Audituj wersje modeli/danych/decisions; integruj z model registry.


## Checklisty Definition of Ready (DoR)

- [ ] SLO/metryki i dane referencyjne zidentyfikowane; logowanie dostępne.
- [ ] Narzędzia drift/bias i privacy polityki gotowe; ownerzy przypisani.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/alerty/drift/bias skonfigurowane; runbooki działań opisane.
- [ ] Dashboardy/raporty dostępne; audyt wersji/danych/decyzji działa.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

