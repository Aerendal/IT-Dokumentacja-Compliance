# graph_engine scaffold

Moduł przygotowuje warstwę grafową nad istniejącą bazą `reports/it_doc_matrix.db` bez destrukcyjnych zmian w obecnych tabelach.

## Założenia
- Python stdlib + `sqlite3` (brak zewnętrznych zależności).
- Migracje wyłącznie additive (`CREATE TABLE IF NOT EXISTS`).
- Każdy skrypt przyjmuje `--db` (domyślnie `reports/it_doc_matrix.db`).
- Każdy skrypt zapisuje wpis do `sync_runs` (`kind`, `status`, `notes`).
- Do DB nie są zapisywane pełne treści dokumentów.

## Pliki
- `ddl_nodes.sql`: tabele `nodes`, `edges_manual`, `edges_inferred`, `influence` + indeksy.
- `build_nodes.py`: buduje `nodes` z `docs` i `sections`.
- `migrate_edges_manual.py`: migruje `edges` do `edges_manual` (tylko dla istniejących node UID).
- `infer_edges.py`: stub inferencji krawędzi.
- `compute_influence.py`: stub wyliczania wpływu.

## Uruchomienie
Z katalogu `dokumentacja/`:

```bash
python3 scripts/graph_engine/build_nodes.py --db reports/it_doc_matrix.db
python3 scripts/graph_engine/migrate_edges_manual.py --db reports/it_doc_matrix.db
python3 scripts/graph_engine/infer_edges.py --db reports/it_doc_matrix.db
python3 scripts/graph_engine/compute_influence.py --db reports/it_doc_matrix.db
```

Szybki smoke test:

```bash
python3 -m unittest discover -s tests -p "test_graph_engine*.py"
```
