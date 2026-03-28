# DATA_LAYERS.md

## Cel dokumentu

Ten dokument opisuje warstwy danych w repo — co jest kodem, co jest assetem runtime, a co jest surowym inputem.

Służy do odróżnienia:
- **core code** (kontrakt kodu, logika, testy),
- **runtime assets** (pliki wymagane do uruchomienia),
- **imported data** (surowe dane wejściowe).

---

# Warstwy danych

## Warstwa 1: Core code

**Katalogi:**
- `itdoc/` — logika domenowa, kontrakt danych
- `scripts/` — narzędzia operacyjne i pipeline
- `tests/` — testy kontraktu i weryfikacja
- `config/` — konfiguracja pipeline i polityk

**Właściwości:**
- Jest częścią kontraktu publicznego repo.
- Musi być czyste z sekretów i prywatnych ścieżek.
- Podlega testom i CI.
- Jest audytowane przez `detect-secrets` (baseline: `.secrets.baseline`).

---

## Warstwa 2: Runtime assets

**Katalogi:**
- `generated_templates/core/` — szablony core runtime

**Pliki:**
- `reports/it_doc_matrix_clean.db` — current-snapshot DB (wersjonowana schema, dane runtime)
- `reports/alignment_log.csv` — log wyrównania szablonów

**Właściwości:**
- Są wymagane do minimalnego lub pełnego trybu pracy.
- Mogą być generowane automatycznie przez `bootstrap_runtime.py`.
- Status każdego assetem opisany w `docs/RUNTIME_BOOTSTRAP.md` §Asset Contract.

**Zewnętrzny asset (poza repo):**
- `reports/it_doc_matrix.db` — legacy-runtime DB (1.9 GB, zewnętrzny artefakt)
- Wymagany tylko do `full-integration` mode.
- Szczegóły: `docs/OPEN_DECISIONS.md` → OD-002.

---

## Warstwa 3: Imported data (historyczna — przeniesiona do repozytorium semantycznego)

Katalog `generated_templates/imported/` zawierał surowe dane wejściowe z zewnętrznego procesu importu.
Został przeniesiony do repozytorium `it-doc-semantic-lab` jako materiał referencyjny
(`corpora/imported_reference_material/`). Nie jest częścią kontraktu repo stabilnego.

---

# Mapa warstw

```
repo root/
├── itdoc/                    ← core code (kontrakt, logika)
├── scripts/                  ← core code (narzędzia, pipeline)
├── tests/                    ← core code (weryfikacja)
├── config/                   ← core code (konfiguracja)
│
├── generated_templates/
│   └── core/                 ← runtime assets (wymagane: local-dev+)
│
├── reports/
│   ├── it_doc_matrix_clean.db ← runtime asset (current-snapshot)
│   ├── it_doc_matrix.db      ← zewnętrzny asset (legacy, OD-002)
│   └── alignment_log.csv     ← runtime asset
│
└── docs/                     ← dokumentacja operacyjna i procesowa
```

---

# Gdzie czytać dalej

- Asset Contract: `docs/RUNTIME_BOOTSTRAP.md` §Asset Contract
- Tryby pracy: `README.md` §Tryby pracy
- Otwarte decyzje: `docs/OPEN_DECISIONS.md`
- Weryfikacja sekretów: `SECURITY.md` §5
