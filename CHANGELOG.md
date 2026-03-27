# CHANGELOG — IT_Dokumentacja

Pełna historia zmian biblioteki szablonów IT. Format: `[data] Faza — opis`.

---

## [2026-03-27] Faza 8 — Public readiness, external reviewer documentation

### Tag: `phase8-public-rc1`

### Cel fazy
Doprowadzenie repo do stanu gotowego do zewnętrznego przeglądu technicznego.

### Dodane
- `README.md`: przepisany jako reviewer-ready — problem statement, tryby pracy,
  quick start, architektura, uczciwy opis ograniczeń
- `docs/EXTERNAL_REVIEW.md`: punkt wejścia dla recenzenta technicznego
  (zakres, model runtime, scenariusze weryfikacji, znane ograniczenia, kolejność czytania)
- `CONTRIBUTING.md`: zasady zmian, wymagania przed commitem, kontrakt runtime
- `SUPPORT.md`: zakres wsparcia best-effort, co warto zgłaszać, priorytety
- `SECURITY.md`: zgłaszanie problemów bezpieczeństwa, zasady pracy z assets runtime,
  zalecenia dotyczące skanowania sekretów

### Stan testów po zmianach
- `doctor --strict` → exit 0
- `pytest -m "not integration and not slow"` → exit 0
- `pytest -m "integration and not slow"` → exit 0
- `build_current.py` → exit 0
- `pipeline_run.py` → exit 0
- custom hook → exit 0

### Otwarte decyzje (pozostałe)
- OD-001: model hooków — OPEN
- OD-003: satellite/ 0 plików — OPEN
- OD-004: CI levels — OPEN
- OD-005: data hermeticity — OPEN
- skan sekretów (gitleaks) — nie wykonany (narzędzie niedostępne w środowisku)

---

## [2026-03-27] Faza 7 — Reproducibility, przekazywalność, release checkpoint

### Tag: `phase7-repro-rc1`

### Cel fazy
Utwardzenie odtwarzalności repo — świeży klon daje się uruchomić bez wiedzy ukrytej w głowie autora.

### Wykonane

#### Faza 7.0 — stan bazowy
- Zapis stanu bazowego: `reports/repro_phase/baseline/` — doctor, fast suite, integration, pipeline, pip check (wszystkie exit 0)

#### Faza 7.1 — clean-room test
- Wykonano na świeżej kopii w `/tmp/repo_clean_room_test`
- Sekwencja: venv → pip install → bootstrap → doctor → fast suite → pip check
- Wszystkie 4 checkpointy zielone (`reports/repro_phase/clean_room/`)

#### Faza 7.2 — formalizacja kontraktu runtime assets
- `docs/RUNTIME_BOOTSTRAP.md`: dodana tabela **Asset Contract** (5 assets × 6 pól: rola, wymagany, profil DB, kto tworzy, odtwarzalny, potrzebny do)
- Dodana tabela trybów pracy: minimal / local-dev / full-integration
- `scripts/doctor.py`: FAIL komunikaty wzbogacone o `Role:` i `Recovery:` dla każdego assetu

#### Faza 7.3 — decyzja o legacy-runtime
- **OD-002 CLOSED**: `reports/it_doc_matrix.db` — Opcja C (external artifact + graceful degradation)
- `docs/OPEN_DECISIONS.md` — wpis OD-002 zaktualizowany do CLOSED z pełnym opisem
- `docs/TROUBLESHOOTING.md` — dwa nowe scenariusze (#11 Missing legacy DB, #12 doctor FAIL na legacy_db w CI)

#### Faza 7.4 — onboarding techniczny
- Każda komenda z docs wykonana i zapisana: `reports/repro_phase/onboarding/`
- bootstrap, doctor, fast suite, build_current, pipeline — wszystkie exit 0

#### Faza 7.5 — release checkpoint
- `reports/runtime_manifest.json` — manifest assets (ścieżka, profil, rozmiar, hash, mtime)
- `docs/CLOSURE_CHECKLIST.md` — wszystkie punkty odhaczone z datą i dowodem wykonania

### Stan testów
- `doctor --strict` → exit 0
- `pytest -m "not integration and not slow"` → exit 0
- `pytest -m "integration and not slow"` → exit 0
- `pipeline_run.py` → exit 0
- clean-room test → PASS

### Otwarte decyzje (pozostałe)
- OD-001: model hooków (custom vs standard `pre-commit`) — świadomie OPEN
- OD-003: `generated_templates/satellite/` 0 plików — świadomie OPEN
- OD-004: CI poziomy (smoke vs full-runtime gate) — świadomie OPEN
- OD-005: hermetyzacja danych runtime — świadomie OPEN

---

## [2026-03-27] Post-stabilizacja — hardening, bootstrap, dokumentacja zamknięcia

### Tag: `post-stabilization-v1`

### Dodane
- `scripts/build_current.py` — realny build `documents_current` (rebuild/incremental); zastępuje placeholder `["true"]` w pipeline
- `scripts/bootstrap_runtime.py` — jednorazowy setup świeżego klonu (katalogi, DB schema, alignment_log, hook, doctor)
- `scripts/run_in_venv.sh` — wrapper wywołujący `.venv/bin/python` z fallbackiem
- `docs/RUNTIME_BOOTSTRAP.md` — dokumentacja runtime assets i procedury bootstrapu
- `docs/DEV_WORKFLOW.md` — kompletny workflow developerski (setup, testy, pre-commit, hooki)
- `docs/TROUBLESHOOTING.md` — 10 scenariuszy awarii z remediacja
- `docs/CLOSURE_CHECKLIST.md` — formalna checklista odbioru fazy (9 sekcji: runtime, pipeline, testy, toolchain, CI, docs, czystość repo, brak ukrytych zależności, formalne zamknięcie)
- `docs/OPEN_DECISIONS.md` — 5 otwartych decyzji architektonicznych (OD-001–OD-005)
- `README.md` — przegląd repo, quick start, model runtime, structure

### Zmienione
- `scripts/install_hooks.sh` — hook używa `.venv/bin/python` z fallbackiem i ostrzeżeniem
- `scripts/doctor.py` — FAIL komunikaty z `→ run: ...` hint; `TECHNICAL DEBT NOTE` ref do OD-002
- `scripts/pipeline_run.py` — `_load_build_current_cmd()` + wykonanie realnego buildu przed emoji gate
- `config/pipeline_policy.yaml` — `build_current_cmd` wskazuje na `scripts/build_current.py`
- `.gitignore` — dodano `reports/post_stabilization_baseline/`
- `scripts/maintenance/bulk_section_patcher.py` — usunięto marker `TODO:` z argparse help
- `tests/conftest.py` — `TECHNICAL DEBT NOTE` blok w `_require_db_profile()` (cel, warunek usunięcia, OD-002)

### Dodane (infrastruktura CI)
- `.github/workflows/smoke.yml` — 4-job smoke CI (doctor, fast-suite, integration-suite, pipeline-smoke); `workflow_dispatch` + nightly schedule

### Stan testów po zmianach
- `scripts/doctor.py --strict` → exit 0
- `pytest -m "not integration and not slow"` → exit 0 (all green)
- `pytest -m "integration and not slow"` → patrz OD-002 (testy E2E z legacy DB są poza scope tej fazy)

### Otwarte decyzje (świadome, nieblokujące)
- OD-001: model hooków (custom vs standardowy `pre-commit`)
- OD-002: status legacy DB — źródło i procedura odtworzenia
- OD-003: status `generated_templates/satellite/` (0 plików)
- OD-004: poziomy CI (smoke vs full-runtime gate)
- OD-005: hermetyzacja danych runtime

---

## [2026-03-09] Faza 12 — Wartość operacyjna: standardy, powiązania, przewodniki

### Dodane
- `QUICK_START.md` — przewodnik startowy: ścieżki per typ projektu (SaaS, chmura, AI, security, compliance), mapa per rola, wskazówki wypełniania
- `CHANGELOG.md` — ten plik; historia wszystkich faz

### Zmienione
- **7 966 szablonów** — usunięto wszystkie `[Uzupełnij zgodnie z kontekstem dokumentu]`:
  - `## Mające zastosowanie standardy i normy` (2 995 plików) → realne kody standardów z `doc_standard_mapping` + keyword fallback (ISO 27001, PMBOK, ITIL 4 itd.)
  - `## Szybkie powiązania` (303 pliki) → 5 powiązanych dokumentów z title-keyword similarity
  - `## RACI i role` (81 plików) → macierz RACI z rolami DEV/PM/BA/OPS
  - `## Checklisty jakości` (890 plików) → dane z `quality_dimensions` (Kompletność/Dokładność/Spójność)
  - `## Standardy i compliance` (81 plików) → realne kody standardów
  - `## Struktura sekcji (szkielet)` (383 pliki) → guidance z donorów + fallback typologiczny
  - `## Jak używać dokumentu` (210 plików) → guidance z donorów + universal fallback
- 24 puste sekcje uzupełnione (## Ścieżka akceptacji, ## Szybkie powiązania, ## Metryki jakości)
- Pipeline PASS `2026-03-09T09-47-38Z`

---

## [2026-03-09] Faza 10+11 Rundy 2–4 — Rozszerzenie wzbogacania szablonów

### Zmienione
- **Runda 2** (próg 9 KB): 1 073 pliki wzbogacone strukturalnie, 1 484 guidance fills, 103 Fazy cyklu życia naprawione
- **Runda 3** (próg 11 KB): 2 061 pliki wzbogacone, 882 guidance fills
- **Runda 4** (próg podobieństwa 0.01): 320 fills + 17 per-section donor + 18 fallback fills
- `scripts/fill_guidance_from_similar.py` — dodano `## Struktura sekcji (szkielet)` i `## Jak używać dokumentu` do TARGET_SECTIONS
- Wynik końcowy: **7 965/7 966** kompletne z guidance, **0** brak_guidance
- Pipeline PASS `2026-03-09T08-50-35Z`

---

## [2026-03-09] Faza 10+11 Runda 1 — Uzupełnienie małych szablonów

### Dodane
- `scripts/enrich_small_templates.py` — wstrzyknięcie brakujących sekcji kanonicznych do małych szablonów (< 3.2 KB → 7–9 KB)
- `scripts/fill_guidance_from_similar.py` — klonowanie guidance z największych podobnych szablonów (Jaccard keyword similarity)

### Zmienione
- **1 066 plików** (< 3.2 KB) — uzupełnione o 15+ brakujących sekcji ze standardowym guidance
- **1 274 pliki** — guidance skopiowane od najbardziej podobnego dużego szablonu
- Naprawiono bug samomatch (plik matchuje siebie po przekroczeniu progu 8 KB)
- Naprawiono regex `## Fazy cyklu życia` (blank line po nagłówku)
- Pipeline PASS `2026-03-09T08-29-09Z`

---

## [2026-03-09] Faza 9 — Zasilenie pustych tabel metadanych DB

### Dodane
- `scripts/seed_base_dicts.py` — słowniki bazowe: roles (40), phases (23), industries (30), document_categories (15), relationship_types (10), quality_dimensions (8)
- `scripts/seed_document_types.py` — 20 typów dokumentów
- `scripts/derive_document_phase_mapping.py` — 2 323 wiersze `document_phase_mapping` + 2 500 `document_lifecycle`
- `scripts/derive_document_raci.py` — 7 941 wierszy (1 domyślny RACI per dokument)
- `scripts/derive_document_dependencies.py` — 897 wierszy `document_dependencies` z `content_links`

### Naprawione
- `scripts/seed_document_types.py` — adaptive column detection (brak kolumny `name_en` w schemacie)
- `scripts/derive_document_dependencies.py` — błąd: `to_kind='section'` zamiast `to_type='document'` → 0 wierszy; naprawiono
- Pipeline PASS `2026-03-09T08-01-39Z`

---

## [2026-03-09] Fazy 7–8B — Narzędzia utrzymania i reindeksacja

### Dodane
- `scripts/maintenance/impact_analyzer.py` — analiza wpływu zmiany regulacji/standardu
- `scripts/maintenance/bulk_section_patcher.py` — masowe aktualizacje sekcji (dry-run + log)
- `scripts/maintenance/regulation_updater.py` + `standards_updater.py` — dodawanie nowych regulacji/standardów z auto-propagacją
- `scripts/maintenance/template_auditor.py` — ocena jakości szablonów (score 0–100)
- `scripts/maintenance/changelog_tracker.py` + tabela `template_changelog` — historia zmian per szablon
- `TEMPLATE_HOWTO.md` — przewodnik tworzenia nowych szablonów
- `MAINTENANCE_HOWTO.md` — przewodnik utrzymania biblioteki

### Zmienione
- Sekcje `## Standardy i compliance` i `## RACI i role` przekształcone w pełne nagłówki `##` (wcześniej bullet-pointy) — podniesiono wskaźnik `content_links_resolved` z 19% do ~27%
- Reindeksacja sekcji: `sections` = 419 154 wierszy
- `doc_section_guidance` — 347 867 wierszy ze `standards_refs`, 88 904 z `regulations_refs`
- Pipeline PASS `2026-03-09T08-01-39Z`

---

## [2026-03-09] Fazy 4–6 — Resolucja powiązań i integracja standardów

### Dodane
- `scripts/map_standards_to_docs.py` — mapowanie standardów do szablonów (keyword matching)
- `scripts/enrich_guidance_standards.py` — wzbogacenie `doc_section_guidance` o `standards_refs` / `regulations_refs`
- `scripts/new_template_wizard.py` — interaktywny CLI do tworzenia nowego szablonu

### Zmienione
- `doc_standard_mapping`: 19 013 wierszy (19 116 po rundzie 2)
- `doc_regulation_mapping`: 2 026 wierszy
- `content_links_resolved`: 131 749 / 484 289 (27.2%) — brak_dokumentu = 0
- Pipeline PASS po każdej fazie

---

## [2026-03-09] Fazy 1–3 — Fundament: mojibake, standardy, regulacje

### Naprawione
- Mojibake w `doc_section_guidance.doc_title` — 3 rundy czyszczenia, wynik: 0 błędów (`zarzÄ…dzania` → `zarządzania`)

### Dodane
- `standards` table — 44 normy: ISO/IEC 27001/27002/27005/27017/27018/27701, ISO 9001, ISO 20000-1, ISO 22301, ISO/IEC 12207/15288/25010/42001, IEEE 829/830/1016/42010, ITIL 4, TOGAF ADM, PMBOK 7, COBIT 2019, SAFe 6.0, DORA, NIS2, SOC 2, CIS Controls v8, OWASP ASVS/MASVS, PCI DSS, NIST CSF, GDPR/RODO, HL7 FHIR
- `compliance_regulations` table — 21 polskich regulacji: KSC, UODO, PZP, KNF, CERT PL, UŚUDE, normy PN-ISO/IEC 27001:2023-PL i inne
- Pipeline PASS `2026-03-09T07-41-46Z`

---

## [przed 2026-03-09] Fazy 1–8 (inicjalne) — Generowanie biblioteki

### Zbudowane
- Biblioteka: **7 966 szablonów core** + 741 satellite w `generated_templates/`
- Baza metadanych: `reports/it_doc_matrix.db` (WAL, 484 289 `content_links`, 7 934 unikalnych tytułów)
- Schemat DB: 70+ tabel (documents, sections, content_links, doc_section_guidance, quality frameworks...)
- ISIC przypisane do wszystkich dokumentów (unassigned = 0)
- Pipeline walidacyjny: `scripts/pipeline_run.py` (hard gate: zero emoji, snapshot, snapshots pruning)
- Powiązania sekcja↔sekcja / dokument↔dokument w DB

---

## Znane ograniczenia

| # | Opis | Wpływ | Obejście |
|---|------|-------|----------|
| 1 | `content_links_resolved` = 27.2% (72.8% nieresolwowanych) | Brak pełnej mapy powiązań w DB | Sekcje `## Szybkie powiązania` w szablonach jako substytut |
| 2 | `document_raci` = generyczny (PM/BA/DEV/OPS dla każdego) | Brak ról per projekt / branżę | Użytkownik wypełnia `[rola]` w szablonie |
| 3 | `doc_standard_mapping` = keyword matching | Może dawać fałszywe dopasowania | Zweryfikuj sekcję `## Mające zastosowanie standardy` w szablonie |
| 4 | 1 szablon (`security_analyst_onboarding.md`) ma oddzielne `## Wejścia` / `## Wyjścia` | Nie spełnia kryterium `## Wejścia i wyjścia` | Celowe — stary format szablonu onboardingowego |
| 5 | Szablony satellite (741 plików) mają starszy format (< 8 KB) | Mniejsza zawartość guidance | Docelowo przejść przez enrich_small_templates.py z progiem 8 KB |
| 6 | Sekcje `[Założenie X]`, `[Ryzyko X]` itp. są intentional placeholders | Wymagają ręcznego wypełnienia | Tak ma być — to guideline dla użytkownika |

---

## Statystyki końcowe (2026-03-09)

| Metryka | Wartość |
|---------|---------|
| Szablony core | 7 966 |
| Szablony satellite | 741 |
| Szablony kompletne z guidance | 7 965 / 7 966 |
| Pipeline | PASS `2026-03-09T09-47-38Z` |
| `doc_standard_mapping` | 19 116 wierszy |
| `doc_regulation_mapping` | 2 026 wierszy |
| `standards` (tabela) | 44 normy |
| `compliance_regulations` | 21 regulacji |
| `content_links` | 484 289 |
| `content_links_resolved` | 131 749 (27.2%) |
| `document_raci` | 7 941 wierszy |
| `document_dependencies` | 897 wierszy |
| `quality_dimensions` | 8 wymiarów |
| Emoji w plikach | 0 |
