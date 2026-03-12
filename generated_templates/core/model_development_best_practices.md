---
title: Model Development Best Practices
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Development Best Practices


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zbiór praktyk dla tworzenia modeli ML/AI: dane, kod, walidacja, bezpieczeństwo i operacje. Ma zmniejszyć ryzyko błędów, bias i problemów w produkcji.


## Zakres i granice

- Obejmuje: wybór problemu i metryk, przygotowanie danych (PII, quality, drift), feature engineering, eksperymenty (tracking, reproducibility), walidację (split, cross-val, bias/fairness), bezpieczeństwo (model stealing/poisoning), MLOps (CI/CD, registry, promotion), monitoring po wdrożeniu, dokumentację (model card), etykę i compliance.  
- Poza zakresem: szczegółowe guideline per framework (PyTorch/TF) – linki zewnętrzne.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe/KPI, dane i klasyfikacja PII, narzędzia eksperymentów, polityki bezpieczeństwa/fairness, standardy kodu/CI, model registry.  
- Wyjścia: checklisty praktyk, wzorce repo/pipeline, rekomendacje walidacji, wymagania monitoring/alerts, model card szablon, DoR/DoD.


## Założenia

- Dostęp do danych i narzędzi jest zapewniony.  
- Zespół zna polityki bezpieczeństwa/fairness.  
- Monitoring i registry są w użyciu.


## Otwarte pytania

- Jakie są limity kosztu inference vs metryki?  
- Jak często aktualizować feature store?  
- Jakie audyty zewnętrzne mogą być wymagane?


## Powiązania (meta)

- Key Documents: data_requirements_for_analysis, analysis_validation_plan, test_set_evaluation, bias_and_fairness_policy, security_requirements, model_promotion_process, monitoring_strategy_document.  
- Key Document Structures: problem/metryki, dane, eksperymenty, walidacja, security, MLOps, monitoring, dokumentacja.  
- Document Dependencies: data pipelines, experiment tracker, CI/CD, registry, monitoring/alerting, access control.


## Zależności dokumentu

Wymaga: zdefiniowanych KPI, klasyfikacji danych, narzędzi trackingu, standardów CI/CD, polityk security/fairness, model registry i monitoring. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja problemu i metryk.  
- Przygotowanie danych/feature’ów.  
- Eksperymenty i walidacja.  
- Promotion i deployment.  
- Monitoring, retraining, audyt.



## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (model/development/best_practices)  
- analysis_validation_plan, test_set_evaluation, model_promotion_process, monitoring_strategy_document


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Zastosuj checklisty przed startem i przed promotion.  
2. Używaj wzorca repo/CI/CD i trackingu eksperymentów.  
3. Publikuj model card; ustaw monitoring i alerts; aktualizuj DoR/DoD i linkage_index.


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

- Promotion gate: warunek publikacji modelu.  
- Drift: zmiana rozkładu danych/performance po wdrożeniu.  
- Model card: karta opisująca model, dane, metryki i ograniczenia.


## Przykłady użycia

- Tworzenie modelu rekomendacji.  
- Model detekcji fraudu z kontrolą fairness.  
- Aktualizacja modelu NLP i monitoring driftu.


## Ryzyka i ograniczenia

- Bias lub leak → błędne decyzje/ryzyka prawne.  
- Brak reproducibility → brak zaufania/ audytowalności.  
- Brak monitoringu → degradacja niewidoczna.


## Decyzje i uzasadnienia

- Metryki i progi promotion.  
- Zakres testów fairness/security.  
- Harmonogram retraining.


## Powiązania z innymi dokumentami

- bias_and_fairness_policy — zasady fairness.  
- security_requirements — bezpieczeństwo.  
- model_promotion_process — ścieżka publikacji.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne polityki ML/AI, bezpieczeństwa, danych.  
- Wytyczne etyczne i regulatorów (jeśli dotyczy).

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

## Powiązania sekcja↔sekcja

- Dane/quality → Walidacja → Promotion → Monitoring.  
- Metryki → Eksperymenty → Decyzje → Model card.  
- Security/fairness → Walidacja → Deployment guardrails.


## Struktura sekcji

1) Problem i KPI (definicja sukcesu)  
2) Dane i PII (źródła, czyszczenie, drift, privacy)  
3) Eksperymenty i reproducibility (tracking, seeds, env)  
4) Walidacja i testy (splits, cross-val, bias/fairness, leak checks)  
5) Security i etyka (poisoning, model stealing, adversarial)  
6) MLOps/CI-CD (repo, tests, packaging, registry, promotion gates)  
7) Monitoring po wdrożeniu (drift, performance, alerts, rollback)  
8) Dokumentacja (model card, lineage, dataset cards)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklista leak/bias/fairness i walidacji.  
- Wzorzec repo + CI (tests, lint, packaging).  
- Promocja i rollback gates.  
- Szablon model card i dataset card.


## Wymagane streszczenia

- One‑pager best practices + linki do repo/policy.  
- Snapshot walidacji/promotion gates.


## Guidance (skrót)

- Ustal KPI i metryki przed kodowaniem.  
- Trackuj eksperymenty i ustaw seed; unikaj nierównych splitów.  
- Waliduj bias/fairness i leak; dokumentuj wyjątki.  
- Automatyzuj testy i deployment; trzymaj modele w registry.  
- Monitoruj po wdrożeniu; zaplanuj rollback i retraining.


## Checklisty Definition of Ready (DoR)

- [ ] KPI i metryki ustalone; dane sklasyfikowane (PII).  
- [ ] Narzędzia trackingu/CI/CD dostępne; repo szablon gotowy.  
- [ ] Polityki security/fairness znane; plan walidacji ustalony.  
- [ ] Registry/monitoring dostępne.  
- [ ] Ownerzy walidacji/promotion wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Walidacja (metryki + bias/fairness + leak) zaliczona; status/wersja/data uzupełnione.  
- [ ] Model i artefakty w registry; promotion/rollback gates ustawione.  
- [ ] Monitoring/drift/alerts aktywne; exceptiony udokumentowane.  
- [ ] Model card/dataset card opublikowane; linkage_index zaktualizowany.  
- [ ] Lessons learned/decisions zapisane.

