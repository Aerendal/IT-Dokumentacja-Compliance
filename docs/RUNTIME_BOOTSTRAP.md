# Runtime Bootstrap

## Co jest runtime assets a co nie jest w repo

| Ścieżka | W repo? | Jak odtworzyć |
|---|---|---|
| `generated_templates/core/` | ❌ (gitignored) | generuje pipeline lub zewnętrzny skrypt |
| `generated_templates/satellite/` | ❌ (gitignored) | tworzy `bootstrap_runtime.py` (pusty) |
| `generated_templates/imported/` | ❌ (gitignored) | generuje pipeline |
| `reports/it_doc_matrix_clean.db` | ❌ (gitignored) | tworzy `bootstrap_runtime.py` |
| `reports/it_doc_matrix.db` | ❌ (gitignored, 1.7 GB) | zewnętrzne repozytorium danych |
| `reports/alignment_log.csv` | ❌ (gitignored) | tworzy `bootstrap_runtime.py` |
| `reports/runs/` | ❌ | generuje `pipeline_run.py` |
| `.venv/` | ❌ | `python3 -m venv .venv && pip install -e '.[dev]'` |

## Minimalny bootstrap — świeży klon

```bash
# 1. Sklonuj repo
git clone <repo-url>
cd IT-Dokumentacja

# 2. Utwórz środowisko Python
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# 3. Uruchom bootstrap runtime
python3 scripts/bootstrap_runtime.py
```

Po tym `doctor --strict` powinien przejść, a pipeline obsługiwać pusty model (brak danych).

## Pełny bootstrap — z danymi

Jeśli masz dostęp do legacy DB (1.7 GB):

```bash
# Podstaw symlink do legacy DB
ln -sf reports/it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db

# Wypełnij current DB przez build_current (wymaga plików w generated_templates/core/)
python3 scripts/build_current.py --mode rebuild

# Uruchom pipeline
python3 scripts/pipeline_run.py
```

## Wzmocniony bootstrap krok po kroku

### 1. Sprawdź stan repo

```bash
python3 scripts/doctor.py
```

Jeśli coś brakuje, doctor wskaże dokładnie co i jak odtworzyć.

### 2. Utwórz brakujące katalogi i inicjalny DB

```bash
python3 scripts/bootstrap_runtime.py --skip-doctor
```

### 3. Opcjonalnie: zasilenie templates

Skopiuj lub wygeneruj pliki `.md` do `generated_templates/core/`,
następnie zbuduj indeks:

```bash
python3 scripts/build_current.py --mode rebuild
```

### 4. Uruchom doctor

```bash
python3 scripts/doctor.py --strict
```

### 5. Uruchom pipeline

```bash
python3 scripts/pipeline_run.py
```

## Edge cases

### Brak `generated_templates/satellite/`

```
[FAIL] generated_templates/satellite: dir missing
  → run: mkdir -p generated_templates/satellite
```

Uruchom `python3 scripts/bootstrap_runtime.py` — katalog zostanie utworzony automatycznie.

### Schema profile mismatch w `it_doc_matrix_clean.db`

```
[FAIL] current_db: profile=unknown, expected=current-snapshot
  → run: python3 scripts/bootstrap_runtime.py
```

Bootstrap `rm`uje stary plik i tworzy od nowa. Następnie uruchom `build_current.py`.

### Stara DB po poprzednim branchu

Jeśli `it_doc_matrix_clean.db` pochodzi ze starego branchu z niezgodnym schematem:

```bash
rm reports/it_doc_matrix_clean.db
python3 scripts/bootstrap_runtime.py
python3 scripts/build_current.py --mode rebuild
```

### `RequestsDependencyWarning` w pre-commit

Oznacza, że hook używa systemowego Pythona zamiast `.venv`.
Zainstaluj hook na nowo:

```bash
bash scripts/install_hooks.sh
```

Hook użyje `.venv/bin/python` jeśli `.venv` istnieje.
