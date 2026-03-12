import click
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.tree import Tree

from metagraph.core.db import get_conn
from metagraph.core.graph import (
    create_node, create_edge, get_node, list_nodes,
    get_neighbors, search_nodes, graph_stats,
)

console = Console()


@click.group()
@click.option("--db", default=None, help="Ścieżka do bazy metagraph.db")
@click.pass_context
def cli(ctx, db):
    """mg — Meta-Graf Wiedzy CLI"""
    ctx.ensure_object(dict)
    ctx.obj["db"] = Path(db) if db else None


@cli.command()
@click.argument("query")
@click.pass_context
def query(ctx, query):
    """Wyszukaj węzły (pełnotekstowe)."""
    with get_conn(ctx.obj["db"]) as conn:
        results = search_nodes(conn, query)
        _print_nodes_table(results, f"Wyniki dla: '{query}'")


@cli.command("list")
@click.option("--layer", "-l", default=None, help="pm|scrum|docs|system")
@click.option("--type", "-t", "type_id", default=None, help="np. docs:spec")
@click.option("--status", "-s", default=None, help="active|draft|blocked|done|archived")
@click.option("--limit", "-n", default=50)
@click.pass_context
def list_cmd(ctx, layer, type_id, status, limit):
    """Listuj węzły grafu."""
    with get_conn(ctx.obj["db"]) as conn:
        results = list_nodes(conn, layer=layer, type_id=type_id, status=status, limit=limit)
        _print_nodes_table(results, f"Węzły ({len(results)})")


@cli.command()
@click.argument("node_id")
@click.option("--depth", "-d", default=1)
@click.option("--json", "as_json", is_flag=True)
@click.pass_context
def show(ctx, node_id, depth, as_json):
    """Pokaż szczegóły węzła z sąsiadami."""
    with get_conn(ctx.obj["db"]) as conn:
        node = get_node(conn, node_id)
        if not node:
            console.print(f"[red]Węzeł '{node_id}' nie istnieje[/red]")
            return
        if as_json:
            console.print_json(json.dumps(dict(node)))
            return
        console.print(f"\n[bold cyan]{node['title']}[/bold cyan]")
        console.print(f"[dim]ID:[/dim] {node['id']}")
        console.print(f"[dim]Typ:[/dim] {node['type_id']}  [dim]Warstwa:[/dim] {node['layer']}")
        console.print(
            f"[dim]Status:[/dim] {node['status']}  "
            f"[dim]Priorytet:[/dim] {'⭐' * node['priority']}"
        )
        if node["source_file"]:
            console.print(
                f"[dim]Źródło:[/dim] {node['source_file']}"
                + (f" §{node['source_section']}" if node["source_section"] else "")
            )
        if node["body"]:
            body = node["body"]
            console.print(f"\n{body[:500]}{'...' if len(body) > 500 else ''}")

        if depth > 0:
            neighbors = get_neighbors(conn, node_id, depth=depth)
            if neighbors:
                tree = Tree(f"[cyan]Powiązania (głębokość={depth})[/cyan]")
                for n in neighbors[:20]:
                    tree.add(
                        f"[green]{n['edge_type']}[/green] → {n['title']} [dim]({n['id']})[/dim]"
                    )
                console.print(tree)


@cli.command()
@click.argument("file_path")
@click.option("--layer", "-l", default=None, help="Wymuś warstwę (pm|scrum|docs)")
@click.option("--dry-run", is_flag=True, help="Pokaż co zostałoby zaimportowane")
@click.pass_context
def ingest(ctx, file_path, layer, dry_run):
    """Importuj dokument Markdown do grafu."""
    from metagraph.ai.parser import parse_markdown_file
    from metagraph.layers.docs_layer import create_spec_doc, ingest_spec_doc_sections

    parsed = parse_markdown_file(file_path)
    effective_layer = layer or parsed["layer"]

    console.print(
        f"[bold]Plik:[/bold] {parsed['file_path']} "
        f"[dim]({parsed['word_count']} słów, warstwa: {effective_layer})[/dim]"
    )
    console.print(f"Sekcje: {len(parsed['sections'])}")

    if dry_run:
        for sec in parsed["sections"][:10]:
            console.print(f"  [dim]{'#' * sec['level']}[/dim] {sec['title']}")
        return

    with get_conn(ctx.obj["db"]) as conn:
        doc_title = Path(file_path).stem.replace("_", " ").replace("-", " ").title()
        spec_id = create_spec_doc(conn, doc_title, doc_number=0, file_path=file_path)
        sec_ids = ingest_spec_doc_sections(conn, spec_id, parsed["sections"])
        console.print(
            f"[green]✓[/green] Stworzono węzeł spec: {spec_id} + {len(sec_ids)} sekcji"
        )


@cli.group()
def graph():
    """Komendy zarządzania grafem."""
    pass


@graph.command("stats")
@click.pass_context
def graph_stats_cmd(ctx):
    """Statystyki grafu."""
    with get_conn(ctx.obj["db"]) as conn:
        stats = graph_stats(conn)
        console.print("\n[bold]📊 Metagraf — statystyki[/bold]")
        console.print(f"  Węzły aktywne: [cyan]{stats['nodes']}[/cyan]")
        console.print(f"  Krawędzie:     [cyan]{stats['edges']}[/cyan]")
        console.print("\n  Podział wg warstw:")
        icons = {"pm": "🎯", "scrum": "🏃", "docs": "📄", "system": "⚙️"}
        for layer, count in stats["by_layer"].items():
            console.print(f"    {icons.get(layer, '•')} {layer}: [yellow]{count}[/yellow]")


@graph.command("orphans")
@click.pass_context
def orphans(ctx):
    """Węzły bez krawędzi."""
    with get_conn(ctx.obj["db"]) as conn:
        rows = conn.execute("""
            SELECT n.* FROM nodes n
            WHERE n.id NOT IN (SELECT from_node FROM edges)
              AND n.id NOT IN (SELECT to_node FROM edges)
              AND n.status = 'active'
        """).fetchall()
        _print_nodes_table(rows, f"Węzły bez powiązań ({len(rows)})")


@cli.group("db")
def db_group():
    """Zarządzanie bazą danych."""
    pass


@db_group.command("migrate")
@click.pass_context
def migrate(ctx):
    """Uruchom migracje."""
    from metagraph.core.db import init_db
    conn = init_db(ctx.obj["db"])
    conn.close()
    console.print("[green]✓ Migracje zakończone[/green]")


@db_group.command("stats")
@click.pass_context
def db_stats(ctx):
    """Statystyki bazy danych."""
    from metagraph.core.db import get_db_path
    import os
    db_path = ctx.obj["db"] or get_db_path()
    size = os.path.getsize(db_path) if Path(db_path).exists() else 0
    console.print(f"Baza: {db_path} ({size / 1024:.1f} KB)")


def _print_nodes_table(nodes: list, title: str = ""):
    table = Table(title=title, show_header=True)
    table.add_column("ID", style="dim", max_width=30)
    table.add_column("Typ", style="cyan", max_width=15)
    table.add_column("Tytuł", max_width=50)
    table.add_column("Status", max_width=10)
    table.add_column("W-wa", max_width=6)
    status_colors = {
        "active": "green", "draft": "yellow", "blocked": "red",
        "done": "dim", "archived": "dim",
    }
    for node in nodes:
        sc = status_colors.get(str(node["status"]), "white")
        table.add_row(
            str(node["id"])[:28],
            str(node["type_id"]),
            str(node["title"])[:48],
            f"[{sc}]{node['status']}[/{sc}]",
            str(node["layer"]),
        )
    console.print(table)


if __name__ == "__main__":
    cli(obj={})
