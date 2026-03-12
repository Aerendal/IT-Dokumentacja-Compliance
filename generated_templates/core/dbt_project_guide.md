---
title: dbt Project Guide
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# dbt Project Guide


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przewodnik prowadzenia projektu dbt: struktura repo, profile/targety, CI/CD, dokumentacja, governance, deployment i operacje.


## Zakres i granice

- Obejmuje: layout repo (models/macros/tests/seeds/snapshots), profiles/targets/sekrety, standardy CI/CD (tests/seed/snapshot/docs), tagging i exposures, katalog i dokumentację, strategię deploymentu i harmonogram runów, governance (code review, approvals, branch model), versioning/migrations, observability (freshness).  
- Poza zakresem: szczegółowy design modeli (w dbt_model_design), polityki dostępu danych (design_abac), monitoring platformy (osobny runbook).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe, platforma DWH, polityki bezpieczeństwa/sekretów, standardy naming, SLA świeżości, harmonogram danych upstream.  
- Wyjścia: struktura repo i konwencje, profiles.yml/targety, pipeline CI/CD, harmonogram runów, zasady review i release, mapa powiązań w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: dbt_model_design, dbt_test_specification, lineage_strategy, data_quality_policy, ci_cd_pipeline, secrets_management, cost_optimization.  
- Key Document Structures: repo layout, profile/target, CI/CD, dokumentacja/katalog, deployment, governance/operacje.  
- Document Dependencies: Git/CI tool, secrets manager, scheduler (dbt Cloud/Airflow), warehouse limits, SLA upstream, tagging/ownership conventions.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
1. Etapy pipeline (CI → CD) i minimalne kroki.
2. Budowa/artefakty i wersjonowanie (semver, SBOM).
3. Testy i jakość (unit/integration/e2e, coverage gates).
4. Bezpieczeństwo (SAST/DAST/dependency scan, secrets, signing).
5. Deploy i promotion (dev/stage/prod, canary/blue-green, approvals).
6. Observability pipeline (logi, metryki, alerty), retry/fail-fast.
7. Rollback i disaster path.
## Szybkie powiązania

- linkage_index.jsonl (data/dbt_project_guide)  
- dbt_model_design, dbt_test_specification, ci_cd_pipeline, secrets_management, data_quality_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **SCRUM Guide** — Przewodnik Scrum

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

1. Ustal strukturę repo i targety; skonfiguruj profiles.yml i sekrety.  
2. Zdefiniuj pipeline CI/CD i harmonogram runów; dodaj selectors i zestaw standardowych poleceń.  
3. Wdroż governance (review/owners/release); publikuj docs i zaktualizuj linkage_index.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

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

- [ ] Profile/targety zabezpieczone, separacja dev/stage/prod.  
- [ ] CI/CD uruchamia dbt build/tests, publikacja docs działa; selectors odzwierciedlają zakres runów.  
- [ ] Governance i rollback opisane; linkage_index zawiera dokument.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Struktura katalogów, profiles.yml przykładowe, selectors.yml, pipeline CI/CD (yaml), docs/exposures build, release notes, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Średni czas/ koszt runu, sukces rate CI/CD, pokrycie docs/exposures, liczba rollbacków, liczba nieudanych buildów z powodu brakujących testów/dokumentacji.

## Kryteria ukończenia

- [ ] Projekt dbt ma spójną strukturę, automatyzację, dokumentację i zasady operacji gotowe do produkcji.


## Struktura sekcji

1) Struktura repo i naming (models/, macros/, seeds/, snapshots/, analyses/, packages)  
2) Profile i targety (dev/stage/prod, poświadczenia, bezpieczeństwo sekretów, target-specific vars)  
3) CI/CD i jakość (pre-commit, dbt build/pr checks, seed/snapshot rules, data contracts)  
4) Dokumentacja i katalog (docs generate/serve, exposures, owners, meta tags, lineage)  
5) Deployment i harmonogram (orchestrator, run ordering, slim CI, selectors, freshness)  
6) Governance i release (branching, approvals, versioning, waivery, incident/rollback)  
7) Operacje i observability (monitoring runów, koszt/czas, alerty SLA, retry/backoff)  
8) Załączniki (przykładowe pipeline'y, selectors.yml, ADR, waiver log)


## Wymagane rozwinięcia

- Tabela konwencji katalogów i nazw (per domena/warstwa).  
- Standard profiles.yml (dev/stage/prod) z zasadami sekretów/rotacji.  
- CI checklist: dbt deps, format/lint, dbt build --select state:modified+, artifacts upload.  
- Harmonogram runów z zależnościami do upstream; polityka freshness i alertów.  
- Governance: minimalne review, code owners, release tags, rollback i incident process.


## Wymagane streszczenia

- Executive: stan CI/CD, pokrycie dokumentacji/exposures, ryzyka (sekrety, koszt, SLA).


## Guidance (skrót)

- Oddziel dev/stage/prod targety; dev zawsze w izolowanym schema z własnym prefixem.  
- Używaj slim CI (state artifacts) i selectors zamiast pełnych rebuildów; monitoruj koszt/czas.  
- Wymagaj dbt build przed merge; blokuj PR bez tests/docs i owners.  
- Publikuj docs/exposures po każdym releasie; utrzymuj lineage w linkage_index.  
- Plan utrzymania: rotacja sekrety, cleanup schematów dev, audyt kosztów i failed runów.


## Checklisty Definition of Ready (DoR)

- [ ] Platforma DWH i narzędzia CI wybrane; polityka sekretów potwierdzona.  
- [ ] Konwencje repo/naming uzgodnione; SLA świeżości znane.  
- [ ] Code owners i proces review określone.


## Checklisty Definition of Done (DoD)

- [ ] Repo ma ustaloną strukturę, profiles.yml, pipeline CI/CD i selectors; dokumentacja i exposures generują się.  
- [ ] Harmonogram runów i alerty SLA skonfigurowane; governance (review/release/rollback) opisane; linkage_index zaktualizowany.  
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.

