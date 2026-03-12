import click
import json
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel
from rich import box

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
@click.argument("query_text")
@click.option("--type", "-t", "type_id", default=None, help="Filtruj typ węzła np. docs:requirement")
@click.option("--layer", "-l", default=None, help="Filtruj warstwę: pm|scrum|docs|system")
@click.option("--limit", "-n", default=20)
@click.pass_context
def query(ctx, query_text, type_id, layer, limit):
    """Wyszukaj węzły (pełnotekstowe + filtr typu/warstwy)."""
    with get_conn(ctx.obj["db"]) as conn:
        results = search_nodes(conn, query_text, limit=limit * 3)
        if type_id:
            results = [r for r in results if r["type_id"] == type_id]
        if layer:
            results = [r for r in results if r["layer"] == layer]
        results = results[:limit]
        _print_nodes_table(results, f"Wyniki dla: '{query_text}'")


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
@click.option("--verbose", "-v", is_flag=True, help="Breakdown per moduł")
@click.pass_context
def graph_stats_cmd(ctx, verbose):
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

        if verbose:
            console.print("\n  [bold]Per moduł:[/bold]")
            table = Table(box=box.SIMPLE)
            table.add_column("Moduł", style="cyan")
            table.add_column("Wymagania", justify="right")
            table.add_column("Endpoints", justify="right")
            table.add_column("Story Points", justify="right")
            table.add_column("Stories", justify="right")
            for mod in conn.execute(
                "SELECT id, title FROM nodes WHERE type_id='docs:module' ORDER BY title"
            ).fetchall():
                reqs = conn.execute("""
                    SELECT count(*) FROM edges e JOIN nodes n ON e.to_node=n.id
                    WHERE e.from_node=? AND e.type_id='implements' AND n.type_id='docs:requirement'
                """, (mod['id'],)).fetchone()[0]
                eps = conn.execute(
                    "SELECT count(*) FROM edges WHERE from_node=? AND type_id='exposes'",
                    (mod['id'],)
                ).fetchone()[0]
                sp = conn.execute("""
                    SELECT coalesce(sum(ss.story_points),0) FROM scrum_stories ss
                    JOIN edges e ON ss.node_id=e.from_node
                    WHERE e.to_node=? AND e.type_id='implements'
                """, (mod['id'],)).fetchone()[0]
                stories = conn.execute("""
                    SELECT count(*) FROM scrum_stories ss
                    JOIN edges e ON ss.node_id=e.from_node
                    WHERE e.to_node=? AND e.type_id='implements'
                """, (mod['id'],)).fetchone()[0]
                table.add_row(mod['title'], str(reqs), str(eps), f"[bold]{sp}[/bold]", str(stories))
            console.print(table)


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


@graph.command("viz")
@click.option("--type", "-t", "diagram_type", default="modules",
              type=click.Choice(["modules", "sprints"]),
              help="modules — zależności modułów, sprints — Gantt timeline")
@click.option("--output", "-o", default=None, help="Plik .md do zapisu")
@click.pass_context
def graph_viz(ctx, diagram_type, output):
    """Generuj diagram Mermaid (moduły lub timeline sprintów)."""
    from metagraph.core.viz import generate_module_diagram, generate_sprint_diagram
    with get_conn(ctx.obj["db"]) as conn:
        if diagram_type == "sprints":
            diagram = generate_sprint_diagram(conn)
        else:
            diagram = generate_module_diagram(conn)

    md_output = f"```mermaid\n{diagram}\n```\n"
    if output:
        Path(output).write_text(md_output)
        console.print(f"[green]✓[/green] Diagram zapisany: {output}")
    else:
        console.print(md_output)


@cli.command()
@click.argument("node_a")
@click.argument("node_b")
@click.option("--max-depth", "-d", default=6)
@click.pass_context
def path(ctx, node_a, node_b, max_depth):
    """Znajdź najkrótszą ścieżkę między dwoma węzłami (BFS)."""
    with get_conn(ctx.obj["db"]) as conn:
        # Sprawdź czy węzły istnieją
        for nid in (node_a, node_b):
            if not conn.execute("SELECT 1 FROM nodes WHERE id=?", (nid,)).fetchone():
                console.print(f"[red]Węzeł nie istnieje: {nid}[/red]")
                return

        # BFS bidirectional
        parents = {node_a: None}
        queue = [node_a]
        found = False
        for _ in range(max_depth):
            if not queue:
                break
            nxt = []
            for nid in queue:
                neighbours = conn.execute("""
                    SELECT to_node as nb, type_id FROM edges WHERE from_node=?
                    UNION
                    SELECT from_node as nb, type_id FROM edges WHERE to_node=?
                """, (nid, nid)).fetchall()
                for nb_row in neighbours:
                    nb = nb_row['nb']
                    if nb not in parents:
                        parents[nb] = (nid, nb_row['type_id'])
                        nxt.append(nb)
                    if nb == node_b:
                        found = True
                        break
                if found:
                    break
            if found:
                break
            queue = nxt

        if not found:
            console.print(f"[yellow]Brak ścieżki (max głębokość: {max_depth})[/yellow]")
            return

        # Odtwórz ścieżkę
        path_nodes = []
        cur = node_b
        while cur != node_a:
            parent_info = parents[cur]
            path_nodes.append((cur, parent_info[1] if parent_info else None))
            cur = parent_info[0]
        path_nodes.append((node_a, None))
        path_nodes.reverse()

        console.print(f"\n[bold]Ścieżka ({len(path_nodes)} węzłów):[/bold]")
        for i, (nid, edge_type) in enumerate(path_nodes):
            n = conn.execute("SELECT title, type_id FROM nodes WHERE id=?", (nid,)).fetchone()
            prefix = "  " * i
            if edge_type:
                console.print(f"{prefix}[dim]─[{edge_type}]→[/dim]")
            console.print(f"{prefix}[cyan]{n['title'][:60]}[/cyan] [dim]({n['type_id']})[/dim]")


@cli.command()
@click.option("--format", "-f", "fmt", default="console",
              type=click.Choice(["console", "md"]))
@click.option("--output", "-o", default=None, help="Plik wyjściowy (np. RAPORT.md)")
@click.pass_context
def report(ctx, fmt, output):
    """Generuj raport projektu: kosztorys, sprints, wymagania, ryzyka."""
    from metagraph.core.report import generate_project_report, render_markdown
    with get_conn(ctx.obj["db"]) as conn:
        data = generate_project_report(conn)

    if fmt == "md" or output:
        md = render_markdown(data)
        if output:
            Path(output).write_text(md)
            console.print(f"[green]✓[/green] Raport zapisany: {output}")
        else:
            console.print(md)
        return

    # Console rich output
    console.print(Panel.fit(
        f"[bold]AI Documentation Workshop[/bold]\n"
        f"[dim]Wygenerowano: {data['generated_at']}[/dim]",
        title="📋 Raport Projektu"
    ))

    # Summary
    tbl = Table(title="Podsumowanie", box=box.SIMPLE)
    tbl.add_column("Metryka"); tbl.add_column("Wartość", justify="right", style="cyan")
    tbl.add_row("Total Story Points", f"[bold]{data['total_sp']} SP[/bold]")
    tbl.add_row("User Stories", str(data["total_stories"]))
    tbl.add_row("Sprints", str(len(data["sprints"])))
    if data["sprints"]:
        tbl.add_row("Zakres", f"{data['sprints'][0]['start']} → {data['sprints'][-1]['end']}")
    tbl.add_row("Wymagania", str(data["requirements"]["total"]))
    console.print(tbl)

    # Moduły
    mtbl = Table(title="Per moduł", box=box.SIMPLE)
    for col in ("Moduł", "Wymagania", "Endpoints", "Story Points"):
        mtbl.add_column(col, justify="right" if col != "Moduł" else "left")
    for m in sorted(data["modules"], key=lambda x: -x["story_points"]):
        mtbl.add_row(m["name"], str(m["requirements"]), str(m["endpoints"]),
                     f"[bold]{m['story_points']}[/bold]")
    console.print(mtbl)

    # Sprints
    for s in data["sprints"]:
        console.print(
            f"\n[bold cyan]Sprint {s['number']}[/bold cyan] — {s['title']}"
            f" [dim]({s['start']} → {s['end']})[/dim] [yellow]{s['total_sp']} SP[/yellow]"
        )
        for st in s["stories"]:
            mod = st.get("module") or "—"
            console.print(f"  • [{st['story_points']} SP] {st['title'][:55]}  [dim]{mod}[/dim]")

    # Ryzyka
    if data["risks"]:
        console.print("\n[bold]⚠️  Ryzyka:[/bold]")
        for rk in data["risks"]:
            p, i = rk["probability"], rk["impact"]
            score = p * i
            color = "red" if score >= 9 else "yellow" if score >= 4 else "green"
            console.print(f"  [{color}]●[/{color}] {rk['title'][:55]} (P={p}×I={i}={score})")
            if rk.get("mitigation"):
                console.print(f"    [dim]↪ {rk['mitigation'][:60]}[/dim]")


@cli.command()
@click.option("--fix", is_flag=True, help="Automatycznie napraw znalezione problemy (np. FTS rebuild)")
@click.pass_context
def check(ctx, fix):
    """Sprawdź integralność grafu (orphans, dangling, FTS, schema, itp.)."""
    from metagraph.core.check import run_all_checks
    with get_conn(ctx.obj["db"]) as conn:
        results = run_all_checks(conn)

        all_ok = True
        for r in results:
            icon = "[green]✅[/green]" if r.ok else "[red]❌[/red]"
            status = "[green]OK[/green]" if r.ok else f"[red]FAIL[/red]"
            console.print(f"{icon} {r.name}: {status} — {r.detail}")
            if not r.ok:
                all_ok = False
                for item in r.items[:5]:
                    console.print(f"   [dim]• {item}[/dim]")
                if len(r.items) > 5:
                    console.print(f"   [dim]... i {len(r.items)-5} więcej[/dim]")

        if fix and not all_ok:
            console.print("\n[yellow]Uruchamiam autofiks...[/yellow]")
            # FTS rebuild
            try:
                conn.execute("INSERT INTO nodes_fts(nodes_fts) VALUES('rebuild')")
                conn.commit()
                console.print("[green]✓[/green] FTS5 przebudowany")
            except Exception as e:
                console.print(f"[red]FTS rebuild failed: {e}[/red]")
        elif all_ok:
            console.print("\n[bold green]✨ Wszystkie sprawdzenia OK[/bold green]")
        else:
            console.print(f"\n[yellow]Użyj --fix aby naprawić automatycznie naprawialne problemy[/yellow]")


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
