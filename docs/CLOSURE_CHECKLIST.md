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
- [ ] exit code 0, wszystkie sekcje OK
- [ ] `reports/it_doc_matrix.db` → `legacy-runtime`
- [ ] `reports/it_doc_matrix_clean.db` → `current-snapshot`

## 1.2. Runtime assets mają zdefiniowany status
- [ ] wiadomo, które assets są tworzone automatycznie
- [ ] wiadomo, które są dostarczane zewnętrznie
- [ ] `docs/RUNTIME_BOOTSTRAP.md`, `scripts/bootstrap_runtime.py`, `scripts/doctor.py` są spójne

## 1.3. Bootstrap runtime działa
```bash
python3 scripts/bootstrap_runtime.py
```
- [ ] exit code 0, brak ukrytych wyjątków

---

# 2. PIPELINE

## 2.1. `build_current.py` jest oficjalnym buildem
```bash
python3 scripts/build_current.py --db reports/it_doc_matrix_clean.db \
  --templates-root generated_templates --alignment-log reports/alignment_log.csv --mode rebuild
```
- [ ] exit code 0
- [ ] brak `build_current_cmd: ["true"]`

## 2.2. Pipeline działa end-to-end
```bash
python3 scripts/pipeline_run.py
```
- [ ] exit code 0, status PASS, brak ukrytych fallbacków

---

# 3. TESTY

## 3.1. Fast suite
```bash
python3 -m pytest -q -m "not integration and not slow"
```
- [ ] exit code 0

## 3.2. Integration suite
```bash
python3 -m pytest -q -m "integration and not slow"
```
- [ ] exit code 0

## 3.3. Compliance E2E
```bash
python3 -m pytest -q tests/test_compliance_e2e.py::TestComplianceE2E
```
- [ ] exit code 0

---

# 4. TOOLCHAIN I HOOKI

## 4.1. Oficjalny model hooków jest jeden
- [ ] wybrany: custom hook (`scripts/install_hooks.sh`) lub standardowy `pre-commit`
- [ ] dokumentacja opisuje dokładnie ten model
- [ ] patrz OD-001 w `docs/OPEN_DECISIONS.md`

## 4.2. Hooki używają właściwego środowiska
```bash
pip check
bash .git/hooks/pre-commit
```
- [ ] exit code 0, brak `RequestsDependencyWarning`

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
- [ ] cała sekwencja kończy się zielono

---

# 6. CI

## 6.1. Smoke workflow istnieje
- [ ] `.github/workflows/smoke.yml` — doctor, fast-suite, integration, pipeline-smoke
- [ ] trigger: `workflow_dispatch` + nightly

## 6.2. Poziomy CI są jawnie rozróżnione
- [ ] smoke workflow nie udaje pełnego E2E
- [ ] warunki skip są jawne i uzasadnione

---

# 7. DOKUMENTACJA

- [ ] `README.md` — aktualny, bez przestarzałych poleceń
- [ ] `docs/RUNTIME_BOOTSTRAP.md` — kompletny, spójny z kodem
- [ ] `docs/DEV_WORKFLOW.md` — opisuje realny workflow
- [ ] `docs/TROUBLESHOOTING.md` — odpowiada realnym komunikatom z kodu

---

# 8. CZYSTOŚĆ REPO

```bash
git status --short
git grep -n '/home/'
git grep -n 'Pobrane'
git grep -n 'TODO'
git grep -n 'FIXME'
```
- [ ] `git status` czysty
- [ ] brak lokalnych ścieżek użytkownika w tracked code
- [ ] brak przypadkowych markerów długu technicznego

---

# 9. BRAK UKRYTYCH ZALEŻNOŚCI

- [ ] brak hardcoded ścieżek lokalnych w testach i skryptach
- [ ] brak `build_current_cmd: ["true"]` w konfiguracji
- [ ] `|| true` tylko w jawnie uzasadnionych miejscach

---

# 10. FORMALNE ZAMKNIĘCIE

Faza może zostać uznana za zamkniętą dopiero gdy wszystkie powyższe punkty są odhaczone:

- Data zamknięcia fazy: `________________________________`
- Commit / tag: `________________________________`
- Uwagi końcowe: `________________________________`
