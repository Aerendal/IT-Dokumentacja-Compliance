# Runtime Bootstrap

## Asset Contract — formalny rejestr runtime assets

Każdy asset ma zdefiniowany status. Nie ma aktywów "nieznanych".

| Asset | Rola | Wymagany | Profil DB | Kto tworzy | Odtwarzalny z repo | Potrzebny do |
|---|---|---|---|---|---|---|
| `generated_templates/core/` | główne szablony dokumentów | TAK | — | zewnętrzny pipeline / import | ❌ (dane) | fast suite: ❌, integration: TAK, build_current: TAK |
| `generated_templates/satellite/` | dodatkowe szablony rozszerzeń | NIE (pusty OK) | — | `bootstrap_runtime.py` tworzy katalog | ✅ | fast suite: ❌, integration: ❌ |
| `generated_templates/imported/` | szablony z importu zewnętrznego | NIE | — | pipeline importu | ❌ | integracja zewnętrzna |
| `reports/it_doc_matrix_clean.db` | indeks current-snapshot dokumentów | TAK | `current-snapshot` | `bootstrap_runtime.py` (schema) + `build_current.py` (dane) | ✅ (schema); ❌ (dane bez templates) | fast suite: TAK, pipeline: TAK |
| `reports/it_doc_matrix.db` | baza legacy-runtime — pełne dane historyczne | NIE (opcjonalna) | `legacy-runtime` | **zewnętrzny artefakt** — nie jest odtwarzany z repo | ❌ (patrz OD-002) | integration suite (compliance E2E): TAK |
| `reports/alignment_log.csv` | mapowanie szablonów na dokumenty | TAK | — | `bootstrap_runtime.py` (nagłówek) + pipeline (dane) | ✅ (nagłówek) | pipeline: TAK, build_current: TAK |
| `reports/runs/` | logi przebiegów pipeline | NIE | — | `pipeline_run.py` | ✅ | logi audytowe |
| `.venv/` | środowisko Python | TAK | — | `python3 -m venv .venv && pip install -e '.[dev]'` | ✅ | wszystko |

### Tryby pracy

| Tryb | Wymagane assets | Co działa |
|---|---|---|
| **minimal** (świeży klon) | `.venv`, `it_doc_matrix_clean.db` (schema), `alignment_log.csv` | fast suite, doctor, bootstrap |
| **local-dev** | minimal + `generated_templates/core/` | build_current, pipeline smoke |
| **full-integration** | local-dev + `reports/it_doc_matrix.db` (legacy) | integration suite, compliance E2E |

> `reports/it_doc_matrix.db` (1.7 GB) jest **zewnętrznym artefaktem**. Repo działa bez niego w trybach minimal i local-dev. Patrz: `docs/OPEN_DECISIONS.md` → OD-002.

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
