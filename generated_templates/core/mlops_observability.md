---
title: MLOps Observability
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# MLOps Observability


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zdefiniować obserwowalność dla modeli/feature store/pipeline ML: jakość, drift, wydajność i koszty.


## Zakres i granice

Obejmuje: SLI/SLO modelu (jakość, latencja, koszty), monitoring feature store, drift detection, logging predykcji, trace inferencji, alerty, retencję danych treningowych/produkcyjnych. Nie obejmuje: ogólnej architektury observability (osobno) ani governance danych (osobne dokumenty).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: cele biznesowe modelu, metryki jakości (AUC/F1 itp.), profil ruchu, wymagania kosztowe i compliance danych, dane referencyjne (training/validation), polityka wersjonowania modeli/feature store.
- Wyjścia: SLI/SLO modelu, zestaw metryk (jakość, drift, latencja, koszty), alerty, dashboardy dla modeli i feature store, procedury walidacji po deploy (shadow/canary), wymagania retencji danych.



## Założenia
- Dostępne zasoby platform/FinOps.  
- Zespoły gotowe do adopcji.  
- Istnieje polityka danych i bezpieczeństwa.
## Otwarte pytania
- Jak mierzyć NPS dev/DS dot. platformy?  
- Jak często wymuszać retrain?  
- Jak obsługiwać regulatory audyt modeli?
## Powiązania (meta)
- Key Documents: model_development_best_practices, model_promotion_process, data_governance_requirements, security_requirements, monitoring_strategy_document, bias_and_fairness_policy.  
- Key Document Structures: lifecycle, platform, CI/CD, security, monitoring, governance, koszt.  
- Document Dependencies: data platform, CI/CD, registry, feature store, observability, IAM, cost/billing.
## Zależności dokumentu
Wymaga: inwentaryzacji obecnych narzędzi i modeli, klasyfikacji danych/PII, SLO/SLA modeli, polityk security/fairness, danych kosztowych, ról i RACI. Braki = DoR otwarte.
## Fazy cyklu życia
- Definicja strategii i target state.  
- Budowa/modernizacja platformy.  
- Adopcja i rollout zespołom.  
- Operacje, monitorowanie, przeglądy i iteracje.
## Struktura sekcji (szkielet)

- SLI/SLO dla modelu (jakość, latencja, koszty; akceptowalne spadki vs baseline)
- Monitoring feature store i danych (freshness, missing, skew, cardinality, null rate)
- Drift detection (data/concept), alerty i akcje (rollback, re-train, reweighting)
- Logging i trace inferencji (próbkowanie, PII, korelacja request→predykcja→etykieta gdy dostępna)
- Dashboardy i raportowanie (model + feature store, per segment klienta/rynku)
- Testy walidacyjne po deploy (shadow/canary, AB, predykcja vs ground truth), regeneracja baseline i ciągły monitoring


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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
1. Ustal cele/KPI i target state; przygotuj diagram i RACI.  
2. Zdefiniuj guardrails promotion/rollback i monitoring.  
3. Zaplanuj roadmapę i adopcję; aktualizuj DoR/DoD i linkage_index.
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
- MLOps: praktyki i narzędzia dla całego lifecycle modeli.  
- Drift: zmiana rozkładów danych/performance w czasie.  
- Promotion gate: warunek wejścia modelu do prod.
## Przykłady użycia
- Budowa platformy MLOps w organizacji multi‑product.  
- Standard guardrails dla modeli risk/fraud.  
- Roadmapa migracji modeli do centralnego registry.
## Ryzyka i ograniczenia
- Brak guardrails → ryzyko compliance/bias.  
- Silosy narzędzi → duplikacja i koszt.  
- Brak monitoringu → cichy drift.
## Decyzje i uzasadnienia
- Self‑service vs concierge dla zespołów.  
- In‑house vs managed tooling.  
- Budżety kosztowe i priorytety capabilities.
## Powiązania z innymi dokumentami
- model_development_best_practices — development.  
- model_promotion_process — release.  
- monitoring_strategy_document — obserwowalność.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne polityki ML/AI, bezpieczeństwa, danych, fairness.  
- Wymogi regulatorów (fin/health/public) jeśli dotyczy.
## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

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

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Wymagane rozwinięcia

- Definicja SLI/SLO dla jakości (AUC/F1/accuracy per segment), latencji (p50/p95), kosztu (GPU/CPU/IO), budżet driftu.
- Zestaw sygnałów driftu: PSI/JS/KL dla feature, KS-test dla target, alerty na przekroczenie progów.
- Polityka logowania inferencji: sampling %, jakie pola maskować, korelacja trace_id.
- Procedury reakcji: kto decyduje o rollback/retrain, w jakim czasie, jakie progi.


## Wymagane streszczenia

- Streszczenie SLI/SLO modeli krytycznych i akceptowanych wyjątków.
- Streszczenie polityki drift + działania naprawcze (w formie krótkiej checklisty).

