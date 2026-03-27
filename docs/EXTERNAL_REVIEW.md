# EXTERNAL_REVIEW.md

## Cel dokumentu

Ten dokument jest wejściem dla osoby technicznej, która chce szybko i uczciwie ocenić repo bez przekopywania całej historii zmian.

To nie jest dokument maintainerski.  
To jest dokument do:
- przeglądu technicznego,
- audytu zewnętrznego,
- rozmowy architektonicznej,
- oceny dojrzałości repo.

---

# 1. Co to jest

Repo służy do audytowalnej walidacji, analizy i utrzymywania zgodności dokumentacji IT oraz powiązanych assets runtime, z jawnym kontraktem danych, testami i pipeline.

Projekt koncentruje się na:
- spójności struktury dokumentacji,
- walidacji jakości,
- materializacji warstwy runtime,
- przewidywalności procesu utrzymania,
- odtwarzalności środowiska.

---

# 2. Zakres

Repo obejmuje:

- bootstrap runtime,
- doctor checks,
- build current-snapshot,
- walidację kontraktu baz danych,
- fast i integration tests,
- pipeline smoke,
- raportowanie compliance i kontrolę jakości.

Repo nie obejmuje jako obietnicy publicznej:
- pełnej samowystarczalności bez assets zewnętrznych,
- pełnej rekonstrukcji wszystkich historycznych danych tylko z samego kodu,
- pełnego publicznego E2E bez odpowiedniego runtime.

---

# 3. Model runtime

Repo pracuje w dwóch trybach:

## Minimal mode
Przeznaczony do:
- onboardingu,
- smoke validation,
- technicznego przeglądu repo,
- szybkiego uruchomienia na czysto.

Minimal mode pozwala na:
- bootstrap,
- doctor,
- fast suite.

## Full runtime
Przeznaczony do:
- integration,
- compliance E2E,
- pipeline z pełniejszym kontekstem danych,
- pracy na pełnych runtime assets.

Status assets i zakres ich odtwarzalności opisano w `docs/RUNTIME_BOOTSTRAP.md`.

---

# 4. Najważniejsze moduły

## `scripts/bootstrap_runtime.py`
Odpowiada za przygotowanie środowiska runtime do minimalnego lub rozszerzonego użycia.

## `scripts/doctor.py`
Waliduje kontrakt repo i runtime:
- profile DB,
- obecność katalogów i assets,
- spójność wejść runtime.

## `scripts/build_current.py`
Buduje albo odświeża warstwę current-snapshot.

## `scripts/pipeline_run.py`
Uruchamia pipeline smoke i sprawdza spójność ścieżki runtime.

## `itdoc/`
Zawiera logikę domenową, kontrakty danych i operacje powiązane z analizą / walidacją.

---

# 5. Jak zweryfikować repo

## Minimalny scenariusz
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

python3 scripts/bootstrap_runtime.py
python3 scripts/doctor.py --strict
python3 -m pytest -q -m "not integration and not slow"
```

## Rozszerzony scenariusz
```bash
python3 scripts/build_current.py \
  --db reports/it_doc_matrix_clean.db \
  --templates-root generated_templates \
  --alignment-log reports/alignment_log.csv \
  --mode rebuild

python3 -m pytest -q -m "integration and not slow"
python3 scripts/pipeline_run.py
```

---

# 6. Co zostało już ustabilizowane

Repo ma obecnie domknięte:

* kontrakt runtime,
* rozpoznawanie profili DB,
* build current-snapshot,
* bootstrap,
* doctor checks,
* fast suite,
* integration suite,
* pipeline smoke,
* dokumentację operacyjną,
* checklistę zamknięcia i listę otwartych decyzji.

---

# 7. Znane ograniczenia

Repo nadal rozróżnia:

* minimal mode,
* full runtime.

Nie wszystkie assets są publiczne lub w pełni odtwarzalne wyłącznie z samego kodu.
To nie jest ukryte ograniczenie — status tych assets opisano jawnie.

Repo używa własnego modelu hooków, opisanego w `docs/DEV_WORKFLOW.md`.

---

# 8. Otwarta warstwa decyzji

Świadomie otwarte tematy są opisane w:

* `docs/OPEN_DECISIONS.md`

To dokument kontrolowany, a nie zapomniany backlog.

---

# 9. Jak czytać to repo

Najrozsądniejsza kolejność dla recenzenta technicznego:

1. `README.md`
2. `docs/EXTERNAL_REVIEW.md`
3. `docs/RUNTIME_BOOTSTRAP.md`
4. `docs/DEV_WORKFLOW.md`
5. `scripts/doctor.py`
6. `scripts/build_current.py`
7. `scripts/pipeline_run.py`
8. `itdoc/`

---

# 10. Ocena uczciwa

Repo jest gotowe do:

* technicznego przeglądu,
* oceny architektonicznej,
* rozmowy o dalszym rozwoju.

Repo nie próbuje udawać większej kompletności, niż rzeczywiście ma.
