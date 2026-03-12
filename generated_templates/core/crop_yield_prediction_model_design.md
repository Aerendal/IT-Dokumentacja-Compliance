---
title: Crop Yield Prediction Model Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Crop Yield Prediction Model Design


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje projekt modelu przewidywania plonów: dane wejściowe, cechy, architekturę, wymagania jakościowe, walidację, ryzyka i zgodność (np. dane satelitarne, prywatność gospodarstw). Ma zapewnić powtarzalność, objaśnialność oraz operacyjne wdrożenie (edge/chmura).


## Zakres i granice

- Obejmuje: źródła danych (dane historyczne, meteo, gleba, satelitarne, IoT), inżynierię cech, wybór/architekturę modeli, walidację (spatio‑temporal split), metryki (RMSE/MAE/MAPE/R²), bias/regionalność, wymagania operacyjne (SLA, latencja, aktualizacje sezonowe), monitoring driftu.
- Poza zakresem: polityka ubezpieczeń, wycena CO₂, logistyka łańcucha dostaw (może być powiązana, ale nie definiowana tutaj).


## Użytkownicy i interesariusze

- Data Science/ML, Agronomia, Product, Privacy/Legal, SRE/MLOps.


## Wejścia i wyjścia

- Wejścia: katalog źródeł danych (format, częstotliwość, licencje), definicje upraw, regiony, kalendarz agronomiczny, cechy kandydackie, ograniczenia kosztowe/latency, wymagania prywatności (dane gospodarstw), standardy (GAI, ISO geospatial jeśli stosowane).
- Wyjścia: architektura modelu, pipeline feature’ów, strategia walidacji, metryki i progi, plan monitoringu, plan retrain (sezon/zdarzeniowy), plan wdrożenia (batch/near‑real‑time), wymagania danych i MLOps, ryzyka i mitigacje.


## Założenia

- Dostępne dane meteo i satelitarne w wymaganej rozdzielczości.
- Feature store/monitoring dostępne w środowisku docelowym.


## Otwarte pytania

- Czy dane gospodarskie wymagają dodatkowej anonimizacji?
- Jakie regiony mają priorytet i jaki jest cel dokładności per region?


## Powiązania (meta)

- Key Documents: data_catalog, feature_store_spec, mlops_runbook, privacy_rural_data.
- Key Document Structures: dane/cechy, model, walidacja, wdrożenie, monitoring.
- Document Dependencies: dane meteorologiczne, dane satelitarne/licencje, IoT, compliance danych rolniczych.


## Zależności dokumentu

Wymaga dostępnych i legalnych źródeł danych (licencje, zgody rolników), definicji regionów i upraw, polityki prywatności. Zależny od infrastruktury MLOps (feature store, monitoring driftu) oraz integracji z systemami agronomicznymi.


## Fazy cyklu życia

- Analiza wymagań: cele biznesowe (plon, ryzyko), KPI, ograniczenia kosztowe.
- Projekt: dane, cechy, modele, walidacja, zgodność, bezpieczeństwo danych.
- Implementacja: pipeline danych/feature store, trenowanie, eksperymenty.
- Testowanie/QA: walidacja spatio‑temporal, bias/regionalność, stress testy danych.
- Wdrożenie: batch/RT, SLA, wersjonowanie modeli, canary jeśli RT.
- Monitoring/Operations: drift danych/modelu, jakość predykcji, alerty, retrain.
- Postmortem/Retrospektywa: incydenty jakości/bias; poprawki.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (agri/ml/predykcja)
- mlops_runbook, feature_store_spec, privacy_rural_data, model_card


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
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

1. Uzupełnij dane/cechy i licencje.
2. Opisz modele, walidację i progi go/no-go.
3. Dodaj plan wdrożenia i monitoring.
4. Wypełnij DoR/DoD, zmapuj relacje cross‑doc.


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

- Spatio‑temporal split — podział danych po czasie i regionie, by uniknąć leakage.
- PSI/KS — metryki driftu danych.
- MAPE/RMSE/R² — metryki jakości regresji.


## Przykłady użycia

- Predykcja plonu pszenicy w regionie X na podstawie meteo + NDVI + gleba.
- Ocena wpływu nawadniania (IoT) na prognozowany plon kukurydzy.


## Ryzyka i ograniczenia

- Leakage czasowy/przestrzenny prowadzący do przeszacowania jakości.
- Bias regionalny (duże gospodarstwa vs. małe); ograniczenia licencyjne danych.


## Decyzje i uzasadnienia

- [Decyzja] Wybór modeli (GBM/CNN/LSTM) — uzasadnienie metryczne/kosztowe.
- [Decyzja] Kadencja retrain — powiązana z sezonem i monitoringiem driftu.


## Powiązania z innymi dokumentami

- Data Acquisition Plan, Feature Store Spec, MLOps Runbook, Privacy Policy.


## Powiązania z sekcjami innych dokumentów

- Model Card → interpretowalność i metryki.
- Observability → monitoring i alerty.


## Słownik pojęć w dokumencie

- NDVI, EVI, LAI, GDD — indeksy roślinności/termiczne.


## Wymagane odwołania do standardów

- Geospatial/remote sensing (np. OGC), privacy lokalnych danych rolniczych.


## Mapa relacji sekcja→sekcja

- Dane/cechy → Model → Walidacja → Wdrożenie → Monitoring → Retrain.


## Mapa relacji dokument→dokument

- Crop Yield Model Design → MLOps Runbook → Observability → Privacy.


## Ścieżki informacji

- Źródła danych → Feature store → Trenowanie → Walidacja → Model Card → Wdrożenie → Monitoring → Retrain.


## Weryfikacja spójności

- [ ] Źródła danych/licencje zgodne z zakresem.
- [ ] Metryki/progi odpowiadają celom biznesowym.
- [ ] Monitoring i retrain powiązane z walidacją i SLA.


## Lista kontrolna spójności relacji

- [ ] Każda cecha ma źródło i częstotliwość.
- [ ] Każdy próg ma uzasadnienie i właściciela.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Notebooki eksperymentów, konfiguracje feature store, pipeline trenowania, dashboardy.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- DS/ML → Agronomia/Product → Privacy/Legal → MLOps/SRE → Owner sign‑off.


## Metryki jakości

- RMSE/MAE/MAPE/R² per uprawa/region, Drift (PSI/KS), Latencja/SLA, Koszt inference.

## Kryteria ukończenia

- [ ] Walidacja osiąga progi; bias oceniony.
- [ ] Monitoring i retrain skonfigurowane.
- [ ] Dokument powiązany w linkage_index.jsonl i checklistach.


## Powiązania sekcja↔sekcja

- Dane/cechy → Model/architektura: każda cecha musi mieć źródło, częstotliwość i koszt.
- Walidacja → Metryki/progi → Decyzje wdrożeniowe: kryteria go/conditional/no-go.
- Monitoring → Plan retrain → Operacje: spójne trigger’y i odpowiedzialności.


## Struktura sekcji

1) Kontekst biznesowy i agronomiczny
2) Źródła danych i licencje
3) Definicje upraw/regionów i kalendarz
4) Feature engineering (statyczne, czasowe, przestrzenne, satelitarne)
5) Architektura modeli (baseline, zaawansowane, ensemble)
6) Walidacja i metryki (spatio‑temporal split, progi)
7) Interpretowalność/wyjaśnialność (SHAP/feature importances)
8) Wymagania operacyjne (SLA, koszty, retrain cadence)
9) Bezpieczeństwo/prywatność danych
10) Monitoring i alerty (drift, jakość, dane brakujące)
11) Plan wdrożenia i rollback
12) Ryzyka, decyzje, załączniki


## Wymagane rozwinięcia

- Dane satelitarne: rozdzielczość, częstotliwość, chmury/licencje.
- Walidacja: strategia podziału czas/przestrzeń, sezonowość, cold start regionów.
- Monitoring: definicje driftu (PSI/KS), okna czasowe, alert thresholds.


## Wymagane streszczenia

- Prywatność: streść zasady anonimizacji/pseudonimizacji gospodarstw.
- Licencje danych: streść ograniczenia użycia/udostępniania.


## Guidance (skrót)

- Zacznij od prostych, objaśnialnych modeli i baseline geospatial.
- Waliduj przestrzennie i sezonowo; unikaj przecieku informacji (leakage).
- Zbalansuj koszty danych (satelitarne/IoT) z korzyściami metrycznymi.
- Zaplanuj monitoring driftu i retrain powiązany z kalendarzem upraw.
- Upewnij się, że dane są legalne (licencje, zgody) i bez PII w predykcjach.


## Checklisty Definition of Ready (DoR)

- [ ] Cele biznesowe/KPI i zakres upraw/regionów zdefiniowane.
- [ ] Źródła danych i licencje potwierdzone; brakujące oznaczone.
- [ ] Struktura sekcji wypełniona/N/A; ryzyka wstępne wpisane.
- [ ] Metryki i strategia walidacji uzgodnione.
- [ ] Wymagania prywatności/bezpieczeństwa zmapowane.


## Checklisty Definition of Done (DoD)

- [ ] Wszystkie sekcje wypełnione lub N/A z uzasadnieniem.
- [ ] Dane→cechy→model→walidacja spójne; progi go/no-go wpisane.
- [ ] Monitoring driftu i retrain plan zdefiniowane; właściciele przypisani.
- [ ] Ryzyka/bias i mitigacje opisane; decyzje zapisane.
- [ ] Wersja/data/właściciel zaktualizowane; linki/artefakty działają.

