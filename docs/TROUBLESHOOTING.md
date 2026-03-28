# TROUBLESHOOTING

## 1. Schema profile mismatch

**Objaw:**
```
[FAIL] current_db: profile=unknown, expected=current-snapshot
  → run: python3 scripts/bootstrap_runtime.py
```

**Przyczyna:** DB pochodzi ze starego branchu lub inna wersja schematu.

**Naprawa:**
```bash
rm reports/it_doc_matrix_clean.db
python3 scripts/bootstrap_runtime.py
python3 scripts/build_current.py --mode rebuild
```

---

## 3. Brak `reports/alignment_log.csv`

**Objaw:**
```
[FAIL] alignment_log: file missing: .../reports/alignment_log.csv
  → run: python3 scripts/bootstrap_runtime.py
```

**Naprawa:**
```bash
python3 scripts/bootstrap_runtime.py
```

Bootstrap tworzy plik z samym nagłówkiem (pusty). Wypełnia się automatycznie przy pracy z pipeline.

---

## 4. `pre-commit` używa systemowego Pythona (`RequestsDependencyWarning`)

**Objaw:**
```
▶ pre-commit: pytest -m 'not slow and not integration' -q ...
/.../lib/python3/dist-packages/urllib3/__init__.py:...: RequestsDependencyWarning
```

**Przyczyna:** Hook wygenerowany przez starą wersję `install_hooks.sh` — używał `python3` (system).

**Naprawa:**
```bash
bash scripts/install_hooks.sh
```

Nowy hook używa `.venv/bin/python` gdy dostępny.

---

## 5. `No module named 'scripts'` lub `No module named 'itdoc'`

**Objaw:**
```
ModuleNotFoundError: No module named 'scripts'
ModuleNotFoundError: No module named 'itdoc'
```

**Przyczyna:** Repo nie jest zainstalowane jako editable package, albo `.venv` nie jest aktywny.

**Naprawa:**
```bash
source .venv/bin/activate
pip install -e ".[dev]"
```

---

## 6. `build_current_cmd` failed w pipeline

**Objaw:**
```
FAIL: build_current_cmd exited with 1
```

**Przyczyna:** Brak `generated_templates/` lub `reports/alignment_log.csv`.

**Naprawa:**
```bash
python3 scripts/bootstrap_runtime.py
python3 scripts/build_current.py --mode rebuild
python3 scripts/pipeline_run.py
```

---

## 7. Pipeline preflight fail: `DB profile mismatch`

**Objaw:**
```
PREFLIGHT FAIL: DB profile mismatch: expected=current-snapshot, got=unknown
```

**Naprawa:**
```bash
rm reports/it_doc_matrix_clean.db
python3 scripts/bootstrap_runtime.py
python3 scripts/build_current.py --mode rebuild
```

---

## 8. Brak legacy DB (`it_doc_matrix.db`)

**Objaw:**
```
[FAIL] legacy_db: missing: .../reports/it_doc_matrix.db
  → restore symlink: ln -s reports/it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db
```

**Przyczyna:** Plik `it_doc_matrix_before_auto_approve.db` (1.7 GB) nie jest w repo.

**Naprawa (gdy plik jest dostępny lokalnie):**
```bash
ln -sf reports/it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db
```

Testy integracyjne wymagają tej bazy. Na CI runner bez pliku — testy są automatycznie skipowane.

---

## 9. `pytest` nie widzi testów po zmianie branchu

**Objaw:**
```
collected 0 items
```

**Możliwa przyczyna:** `.pytest_cache/` wskazuje na stary stan.

**Naprawa:**
```bash
rm -rf .pytest_cache __pycache__
python3 -m pytest -q -m "not integration and not slow"
```

---

## 10. Duża liczba `skipped` w suitach integracyjnych

**Objaw:**
```
61 passed, 120 skipped
```

**To jest normalne** — wiele testów integracyjnych sprawdza profil DB (`legacy-runtime`) i jest skipowane gdy:
- używana jest inna DB,
- brak wymaganych tabel,
- profil nie zgadza się z oczekiwanym.

Uruchom `doctor.py` aby sprawdzić aktualny profil DB.

---

## 11. Missing legacy DB — integration suite nie może być wykonany

**Objaw:**
```
[FAIL] legacy_db: missing: reports/it_doc_matrix.db
  Role: legacy-runtime historical database (integration suite / compliance E2E)
  Recovery (Option A — external artifact): restore symlink:
    ln -s reports/it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db
  Note: fast suite and pipeline smoke work without this asset.
```

**Przyczyna:**
`reports/it_doc_matrix.db` (1.7 GB) jest zewnętrznym artefaktem organizacyjnym. Nie jest odtwarzany automatycznie przez bootstrap.

**Tryb minimal (bez legacy DB):**
Fast suite, doctor (bez `legacy_db`), pipeline smoke — działają poprawnie.

**Tryb full-integration (z legacy DB):**
```bash
# Jeśli plik it_doc_matrix_before_auto_approve.db istnieje w katalogu reports/:
ln -sf it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db
python3 scripts/doctor.py --strict
```

**Komenda kontrolna:**
```bash
ls -lh reports/it_doc_matrix*.db
python3 scripts/doctor.py
```

**Patrz też:** `docs/OPEN_DECISIONS.md` → OD-002

---

## 12. `doctor --strict` FAIL na `legacy_db` w clean-room / CI smoke

**To jest oczekiwane** — w trybie minimal legacy DB nie jest wymagana.

**Jeśli chcesz uruchomić doctor bez blokowania na legacy_db**, uruchom bez `--strict`:
```bash
python3 scripts/doctor.py   # raport, exit 0 nawet przy FAIL
```

CI smoke workflow celowo nie używa `--strict` jeśli legacy DB nie jest dostarczona.

---

## 13. Warningi `RequestsDependencyWarning` / `PytestConfigWarning` przy `python3 -m pytest`

**Przyczyna:**
Uruchomienie `python3 -m pytest` poza aktywnym `.venv` używa systemowego lub user-site Pythona,
który może mieć zainstalowane pakiety z innych projektów — np. `requests` z niezgodną wersją
`urllib3`, albo konflikty z `docschema` / `PyNaCl`.

**To nie jest problem repo** — hook i oficjalne środowisko pracy są czyste.

**Jeśli widzisz ten warning:**

1. Sprawdź, czy `.venv` jest aktywne:
   ```bash
   which python3   # powinno wskazywać na .venv/bin/python3
   ```

2. Jeśli nie — aktywuj:
   ```bash
   source .venv/bin/activate
   python3 -m pytest -q -m "not integration and not slow"
   ```

3. Alternatywnie bez aktywacji:
   ```bash
   .venv/bin/python -m pytest -q -m "not integration and not slow"
   ```

**Hook zawsze używa `.venv/bin/python`** (linia 8 w `.git/hooks/pre-commit`) — jest odporny na to.

**Weryfikacja środowiska:**
```bash
.venv/bin/pip check   # powinno zwracać "No broken requirements found."
```
