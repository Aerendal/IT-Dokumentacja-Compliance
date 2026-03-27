# IT-Dokumentacja

Repozytorium szablonów dokumentacji IT z automatycznym pipelinem walidacji i zarządzania.

## Struktura repozytorium

```
IT-Dokumentacja/
├── itdoc/                   # Pakiet Python: schema, DB, query helpers
├── scripts/                 # Skrypty pipeline, diagnostyki i narzędzia
│   ├── build_current.py     # Buduje documents_current z generated_templates/
│   ├── pipeline_run.py      # Główny pipeline (manifest, walidacja, snapshot)
│   ├── doctor.py            # Diagnostyka kontraktu repo (7 bram)
│   ├── bootstrap_runtime.py # Przygotowanie środowiska (świeży klon)
│   ├── install_hooks.sh     # Instaluje pre-commit hook
│   └── run_in_venv.sh       # Wrapper do uruchamiania przez .venv
├── tests/                   # Testy: unit, integracyjne, compliance
├── config/
│   └── pipeline_policy.yaml # Konfiguracja pipeline
├── docs/
│   ├── RUNTIME_BOOTSTRAP.md # Opis odtwarzania runtime assets
│   ├── DEV_WORKFLOW.md      # Workflow developera
│   └── TROUBLESHOOTING.md   # Rozwiązywanie problemów
├── generated_templates/     # ❌ gitignored — artefakty runtime
└── reports/                 # ❌ częściowo gitignored — artefakty runtime
```

## Środowisko

### Wymagania

- Python 3.10+
- SQLite 3.35+ (wbudowany w Python)
- `pyyaml`, `pytest`, `fastapi`, `httpx` (zależności devowe)

### Instalacja

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Bootstrap runtime assets

Świeży klon nie zawiera danych runtime (szablony, bazy danych).
Uruchom bootstrap aby przygotować środowisko:

```bash
python3 scripts/bootstrap_runtime.py
```

Szczegóły: [docs/RUNTIME_BOOTSTRAP.md](docs/RUNTIME_BOOTSTRAP.md)

## Smoke checks

```bash
# Kontrakt repo (7 bram)
python3 scripts/doctor.py --strict

# Szybka suita testów (< 60 s)
python3 -m pytest -q -m "not integration and not slow"

# Suita integracyjna (wymaga runtime DB)
python3 -m pytest -q -m "integration and not slow"

# Pipeline end-to-end
python3 scripts/pipeline_run.py
```

Wszystkie komendy zwracają `0` przy sukcesie.

## Common failure modes

| Objaw | Przyczyna | Naprawa |
|---|---|---|
| `doctor: FAIL generated_templates/satellite` | Brak katalogu | `python3 scripts/bootstrap_runtime.py` |
| `doctor: FAIL current_db missing` | Brak DB | `python3 scripts/bootstrap_runtime.py` |
| `doctor: FAIL legacy_db missing` | Brak symlinka do 1.7 GB DB | `ln -sf reports/it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db` |
| `No module named 'itdoc'` | Editable install nieaktywny | `pip install -e ".[dev]"` lub aktywuj `.venv` |
| `RequestsDependencyWarning` w pre-commit | Hook używa systemowego Pythona | `bash scripts/install_hooks.sh` (przepina na `.venv`) |
| `pipeline preflight FAIL: DB profile mismatch` | Stara DB po zmianie branchu | `rm reports/it_doc_matrix_clean.db && python3 scripts/bootstrap_runtime.py` |
| `build_current_cmd failed` | Brak `alignment_log.csv` lub `generated_templates/` | `python3 scripts/bootstrap_runtime.py` |

## Workflow developera

Szczegóły: [docs/DEV_WORKFLOW.md](docs/DEV_WORKFLOW.md)
