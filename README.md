# IT-Dokumentacja-Compliance

Audytowalne repo i zestaw narzędzi do walidacji, analizy i utrzymywania zgodności dokumentacji IT z jawnym kontraktem runtime, warstwą raportową i kontrolą jakości opartą o testy oraz pipeline.

## Co to jest

Projekt służy do pracy na dużych zbiorach dokumentacji IT i szablonów dokumentacyjnych.  
Repo skupia się na:

- walidacji struktury i jakości dokumentów,
- utrzymaniu zgodności z regułami i standardami,
- budowie oraz odświeżaniu warstwy danych runtime,
- kontroli poprawności przez testy, doctor checks i pipeline.

## Jaki problem rozwiązuje

W praktyce dokumentacja IT często cierpi na:
- niespójność struktury,
- brak jawnych zależności między dokumentami,
- rozjazd między szablonami, raportami i runtime,
- słabą odtwarzalność procesu walidacji,
- brak technicznej dyscypliny wokół compliance i utrzymania dokumentów.

To repo porządkuje ten obszar przez:
- jawne profile baz danych,
- walidację kontraktu runtime,
- bootstrap środowiska,
- build warstwy current-snapshot,
- testy fast / integration,
- kontrolę pipeline.

## Dla kogo jest

Repo jest przeznaczone głównie dla:
- maintainerów repozytoriów dokumentacyjnych,
- osób budujących audytowalny proces compliance dokumentacji,
- inżynierów odpowiedzialnych za walidację i kontrolę jakości dokumentów,
- zespołów technicznych, które chcą mieć powtarzalny runtime i przewidywalny proces utrzymania.

## Co działa obecnie

Aktualnie repo udostępnia i weryfikuje:

- bootstrap runtime,
- doctor checks kontraktu repo i runtime,
- build current-snapshot,
- pipeline smoke,
- fast suite,
- integration suite,
- compliance E2E,
- dokumentację operacyjną i ścieżki uruchomienia.

## Czego repo nie obiecuje

Repo nie obiecuje na dziś:
- pełnej hermetyczności danych runtime bez żadnych assets zewnętrznych,
- pełnego publicznego E2E na każdym czystym runnerze bez odpowiednich danych,
- pełnej rekonstrukcji wszystkich historycznych assets tylko z samego kodu, jeśli dany asset jest jawnie oznaczony jako zewnętrzny.

Status i zakres assets opisane są w `docs/RUNTIME_BOOTSTRAP.md`.

---

# Tryby pracy

Repo wspiera dwa poziomy użycia:

| Tryb | Doctor | Fast suite | Integration | Pipeline | Wymagane assets |
|---|---|---|---|---|---|
| **Minimal** | `doctor.py` (informacyjny, exit 0) | ✅ | ❌ | smoke | `.venv`, `it_doc_matrix_clean.db` |
| **Full runtime** | `doctor.py --strict` (exit 0 z legacy DB) | ✅ | ✅ | pełny | minimal + `it_doc_matrix.db` + `generated_templates/core/` |

> `doctor.py --strict` zakończy się kodem 1 bez `it_doc_matrix.db` — jest to **celowe i udokumentowane** (patrz `docs/RUNTIME_BOOTSTRAP.md`, `docs/TROUBLESHOOTING.md #11`).

## 1. Minimal mode
Tryb przeznaczony do:
- szybkiego uruchomienia,
- smoke validation,
- onboardingu technicznego,
- zewnętrznego przeglądu repo.

W tym trybie działają:
- bootstrap,
- `doctor.py` (informacyjny — zawsze exit 0),
- fast suite,
- podstawowy workflow narzędziowy.

## 2. Full runtime
Tryb przeznaczony do:
- integration,
- pełnej warstwy runtime,
- compliance E2E,
- pracy na pełnych assets.

W tym trybie wymagane są dodatkowe assets runtime opisane w `docs/RUNTIME_BOOTSTRAP.md`.
`doctor.py --strict` jest bramką jakości dla tego trybu.

---

# Quick start

## Minimal mode

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

python3 scripts/bootstrap_runtime.py
python3 scripts/doctor.py
python3 -m pytest -q -m "not integration and not slow"
```

> **Uwaga:** `doctor.py` bez flagi `--strict` wyświetla informacyjnie stan środowiska i zawsze kończy z kodem 0. `doctor.py --strict` jest przeznaczony dla full runtime i zakończy się kodem 1, jeśli brakuje `it_doc_matrix.db` (legacy DB opisana w `docs/RUNTIME_BOOTSTRAP.md`).

## Build current-snapshot

```bash
python3 scripts/build_current.py \
  --db reports/it_doc_matrix_clean.db \
  --templates-root generated_templates \
  --alignment-log reports/alignment_log.csv \
  --mode rebuild
```

## Pipeline smoke

```bash
python3 scripts/pipeline_run.py
```

---

# Weryfikacja

## Poziomy testów

### Fast suite

```bash
python3 -m pytest -q -m "not integration and not slow"
```

### Integration suite

```bash
python3 -m pytest -q -m "integration and not slow"
```

### Doctor

```bash
# Informacyjny — zawsze exit 0, pokazuje stan środowiska:
python3 scripts/doctor.py

# Strict — wymaga pełnego runtime (legacy DB), exit 1 jeśli brakuje:
python3 scripts/doctor.py --strict
```

### Pipeline

```bash
python3 scripts/pipeline_run.py
```

## Oczekiwane użycie

* **Minimal mode**: doctor + fast suite
* **Full runtime**: doctor + build current + integration + pipeline

---

# Architektura w skrócie

Najważniejsze elementy repo:

* `scripts/bootstrap_runtime.py`
  bootstrap środowiska runtime

* `scripts/doctor.py`
  walidacja kontraktu repo i runtime

* `scripts/build_current.py`
  budowa / odświeżenie warstwy current-snapshot

* `scripts/pipeline_run.py`
  pipeline smoke / runtime pipeline verification

* `itdoc/`
  logika domenowa i kontrakt danych

* `generated_templates/`
  assets dokumentacyjne / templates runtime

* `reports/`
  runtime DB, manifesty, raporty i artefakty pomocnicze

---

# Runtime assets

Repo używa assets o różnym statusie:

* generowane automatycznie,
* wymagane tylko dla full runtime,
* dostarczane zewnętrznie,
* opcjonalne dla minimal mode.

Szczegóły znajdują się w:

* `docs/RUNTIME_BOOTSTRAP.md`
* `docs/TROUBLESHOOTING.md`

---

# Dokumentacja

Punkty wejścia:

* `docs/EXTERNAL_REVIEW.md`
* `docs/RUNTIME_BOOTSTRAP.md`
* `docs/DEV_WORKFLOW.md`
* `docs/TROUBLESHOOTING.md`
* `docs/CLOSURE_CHECKLIST.md`
* `docs/OPEN_DECISIONS.md`

---

# Status projektu

Projekt jest technicznie ustabilizowany i przygotowany do:

* przeglądu technicznego,
* dalszego rozwijania,
* pracy maintainerskiej,
* ewaluacji zewnętrznej.

Jednocześnie część decyzji architektonicznych i organizacyjnych pozostaje jawnie opisana w `docs/OPEN_DECISIONS.md`.

---

# Wsparcie narzędziami AI

W pracach nad tym repozytorium wykorzystywano pomocniczo narzędzia wspomagające programowanie i redakcję dokumentacji, w tym narzędzia klasy AI coding assistant (np. GitHub Copilot).

Zakres użycia obejmował przede wszystkim:
- szkice fragmentów kodu,
- propozycje refaktoryzacji,
- warianty testów,
- robocze fragmenty dokumentacji technicznej.

Narzędzia te były traktowane jako źródło sugestii roboczych, a nie jako autonomiczny autor architektury, kontraktu repozytorium ani końcowych decyzji projektowych.

Ostateczna odpowiedzialność za:
- dobór rozwiązań,
- architekturę,
- integrację zmian,
- uruchomienie lokalne,
- walidację wyników,
- publikowaną treść dokumentacji

pozostaje po stronie autora repozytorium.

Repozytorium należy oceniać na podstawie jego aktualnego stanu: kodu, dokumentacji, testów, oraz spójności technicznej, a nie na podstawie samego faktu użycia narzędzi wspomagających.

Szczegóły dotyczące zakresu użycia narzędzi wspomagających znajdują się w `docs/AI_ASSISTANCE.md`.

---

# Wkład i współpraca

* `CONTRIBUTING.md`
* `SECURITY.md`
* `SUPPORT.md`

---

# Licencja

Zobacz plik `LICENSE`.
