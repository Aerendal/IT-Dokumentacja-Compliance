# metagraph — Meta-Graf Wiedzy

Offline-first, SQLite-based knowledge graph for PM + Scrum + Docs layers. CLI: `mg`.

## Warstwy

| Warstwa | Typy węzłów | Opis |
|---------|-------------|------|
| `pm`    | goal, epic, risk, milestone | Zarządzanie projektami |
| `scrum` | sprint, story, task, bug | Scrum / backlog |
| `docs`  | spec, section, module, endpoint, table, finding, requirement | Dokumentacja techniczna |

## Instalacja

```bash
cd /home/jerzy/Pobrane/IT_Dokumentacja/dokumentacja
pip install -e metagraph/
```

## CLI — komendy

```bash
# Statystyki grafu
mg graph stats

# Lista węzłów
mg list
mg list --layer docs
mg list --layer pm --status active
mg list --type docs:spec --limit 10

# Szczegóły węzła (z sąsiadami)
mg show <node_id>
mg show <node_id> --depth 2
mg show <node_id> --json

# Wyszukiwanie pełnotekstowe
mg query "specyfikacja API"

# Import dokumentu Markdown
mg ingest docs/specyfikacja.md
mg ingest docs/specyfikacja.md --dry-run
mg ingest docs/specyfikacja.md --layer docs

# Węzły bez powiązań
mg graph orphans

# Migracje bazy
mg db migrate

# Statystyki bazy
mg db stats

# Własna baza danych
mg --db /ścieżka/do/custom.db graph stats
```

## Python API

```python
from metagraph.core.db import get_conn
from metagraph.core.graph import create_node, create_edge, list_nodes
from metagraph.layers.pm_layer import create_goal, create_epic, create_risk
from metagraph.layers.scrum_layer import create_sprint, create_story, create_task
from metagraph.layers.docs_layer import create_spec_doc, create_module, create_finding

with get_conn() as conn:
    # Utwórz węzły PM
    goal_id = create_goal(conn, "Uruchomienie v1.0", target_date="2024-06-01")
    epic_id = create_epic(conn, "Parser Briefów", goal_id=goal_id)

    # Utwórz sprint i historyjkę
    sprint_id = create_sprint(conn, "Sprint 1", sprint_number=1)
    story_id = create_story(conn, "Upload briefu", epic_id=epic_id, story_points=5)

    # Dokumentacja
    spec_id = create_spec_doc(conn, "Specyfikacja API", doc_number=3)
    module_id = create_module(conn, "BriefParser", module_type="service", spec_doc_id=spec_id)

    # Krawędź: task implementuje story
    create_edge(conn, story_id, epic_id, "part_of")

    # Przeszukaj
    from metagraph.core.graph import search_nodes
    results = search_nodes(conn, "brief")
```

## Schemat bazy danych

Plik: `metagraph/metagraph.db` (SQLite, WAL mode)

Kluczowe tabele: `nodes`, `edges`, `events`, `node_types`, `edge_types`  
Warstwy: `pm_goals`, `pm_epics`, `pm_risks`, `scrum_sprints`, `scrum_stories`, `scrum_tasks`, `doc_specs`, `doc_modules`, `doc_findings`

FTS5: tabela `nodes_fts` dla pełnotekstowego wyszukiwania.

## Zmienne środowiskowe

| Zmienna | Domyślna | Opis |
|---------|----------|------|
| `METAGRAPH_DB` | `metagraph/metagraph.db` | Ścieżka do bazy danych |
