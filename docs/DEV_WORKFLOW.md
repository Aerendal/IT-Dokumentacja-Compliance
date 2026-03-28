# DEV_WORKFLOW

Przewodnik codziennej pracy dla developerów IT-Dokumentacja.

## 1. Pierwsze uruchomienie

```bash
git clone <repo-url>
cd IT-Dokumentacja
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python3 scripts/bootstrap_runtime.py
```

## 2. Przed każdą sesją

```bash
source .venv/bin/activate
python3 scripts/doctor.py          # sprawdź stan repo
```

## 3. Uruchamianie testów

> Wszystkie poniższe komendy zakładają aktywne środowisko `.venv` (po `source .venv/bin/activate`).  
> Alternatywnie używaj `.venv/bin/python -m pytest ...` bez aktywacji.

### Szybka suita (< 60 s)

```bash
python3 -m pytest -q -m "not integration and not slow"
```

### Suita integracyjna (wymaga legacy DB)

```bash
python3 -m pytest -q -m "integration and not slow"
```

### Konkretny test

```bash
python3 -m pytest tests/test_wizard.py -v
python3 -m pytest tests/test_compliance_report.py::TestComplianceE2E -v
```

### Wszystkie testy

```bash
python3 -m pytest -q
```

## 4. Pipeline

### Pełny przebieg

```bash
python3 scripts/pipeline_run.py
```

Pipeline automatycznie wywołuje `build_current.py` przed uruchomieniem.

### Tylko build documents_current

```bash
python3 scripts/build_current.py --mode rebuild
python3 scripts/build_current.py --mode incremental   # tylko zmienione pliki
```

## 5. Doctor — diagnostyka

```bash
python3 scripts/doctor.py           # raport (exit 0 zawsze)
python3 scripts/doctor.py --strict  # exit 1 przy pierwszym FAILu
```

## 6. Pre-commit hook

### Instalacja

```bash
bash scripts/install_hooks.sh
```

Hook uruchamia fast suite przed każdym commitem przez `.venv/bin/python`.

### Pominięcie jednorazowe

```bash
git commit --no-verify -m "..."
```

## 7. Linting i formatowanie

```bash
ruff check .
ruff format .
```

## 8. Commity — konwencja

Format: `type(scope): opis`

| Typ | Kiedy |
|---|---|
| `fix(runtime)` | naprawa kontraktu DB / schema |
| `fix(pipeline)` | naprawa pipeline, emoji gate, config |
| `fix(compliance)` | naprawa testów compliance |
| `test(repo)` | tylko zmiany testów |
| `docs(*)` | tylko dokumentacja |
| `chore(*)` | zależności, .gitignore, konfiguracja |

## 9. Workflow dla nowego szablonu

```bash
# Dodaj plik .md do generated_templates/core/
echo "# Mój Nowy Szablon" > generated_templates/core/moj_nowy_szablon.md

# Przebuduj indeks
python3 scripts/build_current.py --mode incremental

# Sprawdź pipeline
python3 scripts/pipeline_run.py
```

## Autofix V1 — zakres i ograniczenia

Narzędzie `scripts/fix_docs.py` obsługuje bezpieczne autofixy strukturalne.

### V1 naprawia automatycznie (`safe_autofix=True`)

- **`DOC.SECTION.MISSING`** — brakująca wymagana sekcja szablonu
  Wstawia placeholder na końcu dokumentu (np. `<!-- TODO: Opisz cel dokumentu -->`).
- **`DOC.EMOJI.FORBIDDEN`** — niedozwolone emoji w pliku `.md`
  Usuwa znaki emoji, zachowując całą resztę treści.

### V1 tylko raportuje (`safe_autofix=False` / `report_only`)

- **`DOC.FRONTMATTER.MISSING`** — brak bloku YAML frontmatter
- **`DOC.FRONTMATTER.NO_TITLE`** — brak pola `title:` w frontmatter

Te przypadki wymagają manualnej decyzji — nie są modyfikowane automatycznie.

### Znane ograniczenia V1

- `DOC.SECTION.MISSING`: sekcja jest dodawana na **końcu dokumentu**, bez rekonstrukcji kanonicznej kolejności.
- Autofix nie uzupełnia treści merytorycznej — wstawia tylko placeholder.
- Nie dotyczy plików poza `generated_templates/` i `reports/demo_review/files/input/`.

### Użycie

```bash
# Analiza (bez zapisu):
.venv/bin/python scripts/fix_docs.py --root DIR --mode analyze --output plan.json

# Dry-run (diff bez zapisu):
.venv/bin/python scripts/fix_docs.py --root DIR --mode dry-run --output plan.json --write-diff diff.txt

# Apply tylko bezpiecznych fixów:
.venv/bin/python scripts/apply_fix_plan.py --plan plan.json --only-safe --backup-dir reports/autofix_backups
```

## 10. Typowy cykl pracy

```bash
# 1. Aktywuj środowisko
source .venv/bin/activate

# 2. Sprawdź stan
python3 scripts/doctor.py

# 3. Wprowadź zmiany...

# 4. Uruchom testy
python3 -m pytest -q -m "not integration and not slow"

# 5. Commit (hook odpali testy automatycznie)
git add -p
git commit -m "fix(scope): opis zmiany"

# 6. Po większych zmianach — pełna suita
python3 -m pytest -q -m "integration and not slow"
python3 scripts/pipeline_run.py
```
