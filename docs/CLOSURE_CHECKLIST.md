# CLOSURE_CHECKLIST.md

## Cel dokumentu

Ten dokument służy do formalnego zamykania faz prac technicznych w repozytorium.

Jego zadaniem jest:
- wymusić pełną weryfikację końca fazy,
- ograniczyć ryzyko pozostawienia niewidocznych zależności lokalnych,
- zapobiec sytuacji, w której repo „działa u autora", ale nie ma domkniętego kontraktu technicznego,
- zapewnić, że każdy etap można zamknąć na podstawie dowodów wykonania, a nie pamięci lub intuicji.

---

## Zasady użycia

### Zasada 1
Nie oznaczaj punktu jako zakończonego bez realnego uruchomienia komendy lub ręcznej weryfikacji pliku.

### Zasada 2
Jeżeli punkt nie jest spełniony, nie zamykaj fazy „warunkowo".
Niespełniony punkt albo wraca do wykonania, albo trafia do `OPEN_DECISIONS.md`.

### Zasada 3
Jeżeli wynik zależy od dużych artefaktów runtime, należy to wskazać jawnie.

### Zasada 4
Jeżeli check przechodzi tylko lokalnie, ale nie został jeszcze zweryfikowany na świeżym środowisku, faza nie jest domknięta.

---

# 1. RUNTIME

## 1.1. Profile baz danych są poprawnie rozpoznawane
```bash
python3 scripts/doctor.py --strict
```
- [x] exit code 0, wszystkie sekcje OK — zweryfikowano 2026-03-27 (`reports/repro_phase/baseline/10_doctor.exit = 0`)
- [x] `reports/it_doc_matrix.db` → `legacy-runtime`
- [x] `reports/it_doc_matrix_clean.db` → `current-snapshot`

## 1.2. Runtime assets mają zdefiniowany status
- [x] wiadomo, które assets są tworzone automatycznie — patrz tabela w `docs/RUNTIME_BOOTSTRAP.md`
- [x] wiadomo, które są dostarczane zewnętrznie — `it_doc_matrix.db` (Opcja C, OD-002 CLOSED)
- [x] `docs/RUNTIME_BOOTSTRAP.md`, `scripts/bootstrap_runtime.py`, `scripts/doctor.py` są spójne

## 1.3. Bootstrap runtime działa
```bash
python3 scripts/bootstrap_runtime.py
```
- [x] exit code 0, brak ukrytych wyjątków — zweryfikowano w clean-room i onboarding (`reports/repro_phase/`)

---

# 2. PIPELINE

## 2.1. `build_current.py` jest oficjalnym buildem
```bash
python3 scripts/build_current.py --db reports/it_doc_matrix_clean.db \
  --templates-root generated_templates --alignment-log reports/alignment_log.csv --mode rebuild
```
- [x] exit code 0 — zweryfikowano 2026-03-27 (`reports/repro_phase/onboarding/13_build_current_from_docs.exit = 0`)
- [x] brak `build_current_cmd: ["true"]` — zastąpione w commit `00f71af`

## 2.2. Pipeline działa end-to-end
```bash
python3 scripts/pipeline_run.py
```
- [x] exit code 0 — zweryfikowano 2026-03-27 (`reports/repro_phase/baseline/13_pipeline.exit = 0`)

---

# 3. TESTY

## 3.1. Fast suite
```bash
python3 -m pytest -q -m "not integration and not slow"
```
- [x] exit code 0 — zweryfikowano lokalnie i w clean-room 2026-03-27

## 3.2. Integration suite
```bash
python3 -m pytest -q -m "integration and not slow"
```
- [x] exit code 0 — zweryfikowano 2026-03-27 (`reports/repro_phase/baseline/12_integration_suite.exit = 0`)

## 3.3. Compliance E2E
```bash
python3 -m pytest -q tests/test_compliance_e2e.py::TestComplianceE2E
```
- [x] exit code 0 — wchodzi w skład integration suite (powyżej)

---

# 4. TOOLCHAIN I HOOKI

## 4.1. Oficjalny model hooków jest jeden
- [x] wybrany: **custom hook** (`scripts/install_hooks.sh`) — świadoma decyzja (OD-001 OPEN, zapis decyzji w OPEN_DECISIONS.md)
- [x] dokumentacja opisuje dokładnie ten model (`docs/DEV_WORKFLOW.md`)

## 4.2. Hooki używają właściwego środowiska
```bash
pip check
bash .git/hooks/pre-commit
```
- [x] exit code 0, brak `RequestsDependencyWarning` — zweryfikowano 2026-03-27 (`reports/repro_phase/baseline/14_pip_check.exit = 0`)

---

# 5. CLEAN ROOM TEST

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python3 scripts/bootstrap_runtime.py
python3 scripts/doctor.py --strict
python3 -m pytest -q -m "not integration and not slow"
```
- [x] cała sekwencja kończy się zielono — zweryfikowano 2026-03-27 w `/tmp/repo_clean_room_test` (`reports/repro_phase/clean_room/`)

---

# 6. CI

## 6.1. Smoke workflow istnieje
- [x] `.github/workflows/smoke.yml` — doctor, fast-suite, integration, pipeline-smoke
- [x] trigger: `workflow_dispatch` + nightly (Mon 03:00 UTC)

## 6.2. Poziomy CI są jawnie rozróżnione
- [x] smoke workflow nie udaje pełnego E2E — opisano w workflow YAML i OD-004
- [x] warunki skip są jawne — patrz komentarze w `smoke.yml`

---

# 7. DOKUMENTACJA

- [x] `README.md` — aktualny, bez przestarzałych poleceń — zweryfikowano 2026-03-27
- [x] `docs/RUNTIME_BOOTSTRAP.md` — kompletny, tabela asset contract, spójny z kodem
- [x] `docs/DEV_WORKFLOW.md` — opisuje realny workflow, hooki, build, testy
- [x] `docs/TROUBLESHOOTING.md` — 12 scenariuszy, odpowiada realnym komunikatom z kodu (legacy DB, clean-room, hooki)

---

# 8. CZYSTOŚĆ REPO

```bash
git status --short
git grep -n '/home/'
git grep -n 'Pobrane'
git grep -n 'TODO'
git grep -n 'FIXME'
```
- [x] `git status` czysty — zweryfikowano 2026-03-27
- [x] brak lokalnych ścieżek użytkownika w tracked code — Z12 grep-after.txt potwierdzony
- [x] brak przypadkowych markerów długu technicznego — Z12 cleanup pass wykonany

---

# 9. BRAK UKRYTYCH ZALEŻNOŚCI

- [x] brak hardcoded ścieżek lokalnych w testach i skryptach
- [x] brak `build_current_cmd: ["true"]` w konfiguracji — zastąpione commit `00f71af`
- [x] `|| true` tylko w jawnie uzasadnionych miejscach — brak w critical paths

---

# 10. FORMALNE ZAMKNIĘCIE

Faza może zostać uznana za zamkniętą dopiero gdy wszystkie powyższe punkty są odhaczone.

- **Data zamknięcia fazy:** 2026-03-27
- **Commit / tag:** `phase7-repro-rc1` (fresh-main)
- **Uwagi końcowe:** Wszystkie checkpointy zielone. OD-001 (hook model) świadomie otwarte. OD-002 (legacy DB) CLOSED — Opcja C. OD-003 (satellite) CLOSED — 2026-03-28 (satellite wycofany z kontraktu). Clean-room test przeszedł w `/tmp/repo_clean_room_test`. Runtime manifest: `reports/runtime_manifest.json`.
