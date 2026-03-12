---
title: Model Card
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Card


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Dostarczyć kartę modelu ML/AI opisującą przeznaczenie, dane, metryki, ograniczenia, ryzyka i odpowiedzialne użycie.


## Zakres i granice

- Obejmuje: przeznaczenie i domenę, dane treningowe/validacyjne, metryki, warunki użycia, ograniczenia/bias, ryzyka, prywatność i bezpieczeństwo, licencje, wersjonowanie, odpowiedzialne AI (fairness, safety), kontakt do właścicieli.
- Poza zakresem: szczegółowe skrypty treningowe (linkowane), polityki danych (osobne dokumenty).


## Użytkownicy i interesariusze
- ML Platform, DevOps/SRE, Security, Product/Owners modeli, FinOps.
## Wejścia i wyjścia
- Wejścia: model artifacts (onnx/pkl/pt/tf), requirements, base images, security policy, performance targets (latency/QPS), hardware profile (CPU/GPU), observability standards, cost targets, license constraints.
- Wyjścia: standard obrazu, Dockerfile/templates, checklist build/test, scan/sign SBOM, config (env/flags), runbook rollout/rollback, metrics/alerts, doc dla zespołów.
## Założenia
- Registry, scanning, signing, SBOM narzędzia dostępne; model registry działa.
## Otwarte pytania
- Jak często patchować base i rescanujemy obrazy? 
- Czy wymagane warianty CPU/GPU/AVX?
## Powiązania (meta)
- Key Documents: model_serving_architecture, observability_ml, security_baseline_containers, sbom_policy, ci_cd_pipeline_ml, cost_optimization_ml, data_privacy_policy.
- Key Document Structures: obraz, security, perf, observability, rollout.
- Document Dependencies: registry, scanner/signing, CI/CD, monitoring/logging, model registry, feature store, artifact store.
## Zależności dokumentu
Wymaga: artefaktów modeli, polityk security/observability, bazowych obrazów, celów perf i danych hardware, narzędzi scanning/signing/SBOM, CI/CD, registry. Bez tego DoR otwarte.
## Fazy cyklu życia
- Wybór base image i zależności; build szablonów.
- Security scanning/signing/SBOM; testy funkcjonalne/perf.
- Publikacja do registry; rollout/flags; monitoring.
- Utrzymanie: patching base, rescans, perf tuning.
## Struktura sekcji (szkielet)

- Przeznaczenie i zakres użycia
- Dane: źródła, skład, preprocessing, PII
- Architektura i wersjonowanie modelu
- Metryki i testy (w tym fairness/safety)
- Ograniczenia i znane problemy
- Ryzyka i mitigacje
- Warunki użycia i zakazy
- Bezpieczeństwo/prywatność/licencje
- Kontakt i odpowiedzialności


## Szybkie powiązania

- Data Governance, Responsible AI policy, Security/Privacy, Deployment guide, Monitoring/Drift.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **PCI DSS** — Standard Bezpieczeństwa Danych Przemysłu Kart Płatniczych

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
1. Wybierz base i zbuduj obraz wg szablonu; dodaj deps.
2. Dodaj security (SBOM/sign/scan) i observability; ustaw resources/perf.
3. W CI: build/test/scan/sign/push; rollout z canary; monitoruj metryki.
4. Patchuj base i rescanuj okresowo; aktualizuj dokument i linkage_index.
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
- SBOM, Signing, Rootless, Cold start, BLAS, Canary, HPA.
## Przykłady użycia
- Model fraud: base slim, onnxruntime, SBOM+sign, latency target p95<80ms, canary 10%.
- Batch inference: VPA profile, multi-stage build, SBOM, GPU image variant.
## Ryzyka i ograniczenia
- Brak scanning/signing → ryzyko supply chain; duży obraz → wolne deploy/cold start; brak observability → trudne incydenty.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Model Serving Architecture, Observability ML, Security Baseline Containers, SBOM Policy, CI/CD Pipeline ML, Cost Optimization ML, Data Privacy Policy.
## Powiązania z sekcjami innych dokumentów
- Security Baseline → rootless/scan/sign; Observability → metrics; Serving → rollout.
## Słownik pojęć w dokumencie
- SBOM, Signing, Rootless, Cold start, BLAS, Canary, HPA.
## Wymagane odwołania do standardów
- Polityki security kontenerów, SBOM i signing; licencje base/dep; privacy (PII) jeśli dane w obrazie.
## Mapa relacji sekcja→sekcja
- Base/deps → Security/size → Perf → Observability → Rollout.
## Mapa relacji dokument→dokument
- Model Containerization → Serving/Security/Observability/CI-CD → Release/Cost.
## Ścieżki informacji
- Artefakty → Build/Scan/Sign → Deploy → Monitor → Patch/Rescan.
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
- Dockerfile template, SBOM, raport scan, wyniki testów perf, config metrics/resources, rollout plan.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- ML Platform/DevOps → Security → Observability/FinOps → Owner sign‑off.
## Metryki jakości
- Rozmiar obrazu, cold start p95, liczba obrazów bez SBOM/scan, czas build/scan, liczba rollbacków z powodu obrazu, koszt storage/transfer.
## Kryteria ukończenia
- [ ] Standard obrazu wdrożony; scan/sign/SBOM; perf/observability/resource opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Wejścia

- Dane o zbiorach, pipeline treningowy, wyniki evaluacji, analizy bias/fairness, wymagania prawne/branżowe, karty poprzednich wersji.


## Wyjścia

- Kompletna karta modelu z metrykami, ograniczeniami i zaleceniami użycia.



## Jak używać (checklista)

- Wypełnij cel i zakres; opisz dane i preprocessing.
- Dodaj metryki i testy fairness/safety; wskaż ograniczenia i zakazy użycia.
- Zaktualizuj wersję i linki do artefaktów; podaj kontakt właścicieli.


## Wymagane rozwinięcia / powiązania

- Tabela metryk, wyniki fairness/safety, linki do danych/artefaktów, polityka odpowiedzialnego AI.


## Kryteria DoR

- Model wytrenowany, dane/metryki dostępne, analiza ryzyk wstępna.


## Kryteria DoD

- Karta wypełniona, metryki/fairness podane, ograniczenia/warunki użycia opisane; zatwierdzenie właściciela/AI governance.


## Artefakty

- Karta (MD/PDF), wyniki testów, linki do artefaktów, audit log.


## Walidacja

- Przegląd AI governance; weryfikacja spójności metryk i danych; kontrola ograniczeń/zakazów użycia.


## Metryki

- Pokrycie modeli kartami, czas aktualizacji po nowej wersji, liczba odchyleń wykrytych w auditach.


## Utrzymanie

- Aktualizacja przy każdej wersji modelu; przegląd okresowy ryzyk i metryk.


## Zakończenie

Karta modelu zapewnia przejrzystość i odpowiedzialne użycie; utrzymuj ją z każdą wersją i zmianą danych/regulacji.

