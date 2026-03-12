#!/usr/bin/env python3
"""
ingest_workshop.py — Wczytuje dokumentację Warsztatu do Meta-Grafu.

Użycie:
    python metagraph/ingest_workshop.py
    python metagraph/ingest_workshop.py --dry-run  # pokaż co by stworzył
    python metagraph/ingest_workshop.py --reset    # wyczyść i zacznij od nowa
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from metagraph.core.db import get_conn, init_db
from metagraph.core.graph import create_node, create_edge, graph_stats

WORKSHOP_DIR = Path(__file__).parent.parent / "docs" / "workshop"
DB_PATH = Path(__file__).parent / "metagraph.db"

# ─────────────────────────────────────────────
# Konfiguracja 16 spec docs
# ─────────────────────────────────────────────
SPEC_DOCS = [
    (1,  "01 — Vision & Scope",                  "01_vision_and_scope.md"),
    (2,  "02 — System State Description",        "02_system_state_description.md"),
    (3,  "03 — Architecture Overview",           "03_architecture_overview.md"),
    (4,  "04 — Data Model PostgreSQL",           "04_data_model_postgresql.md"),
    (5,  "05 — Module Interface Contracts",      "05_module_interface_contracts.md"),
    (6,  "06 — OpenAPI Specification",           "06_openapi_specification.yaml"),
    (7,  "07 — LLM Adapter Spec",                "07_llm_adapter_spec.md"),
    (8,  "08 — Brief Parser Spec",               "08_brief_parser_spec.md"),
    (9,  "09 — Semantic Mapper Spec",            "09_semantic_mapper_spec.md"),
    (10, "10 — Estimation Engine Spec",          "10_estimation_engine_spec.md"),
    (11, "11 — Work Planner Spec",               "11_work_planner_spec.md"),
    (12, "12 — Itdoc Integration Spec",          "12_itdoc_integration_spec.md"),
    (13, "13 — Security and Config Spec",        "13_security_and_config_spec.md"),
    (14, "14 — Testing Strategy",                "14_testing_strategy.md"),
    (15, "15 — Implementation Roadmap",          "15_implementation_roadmap.md"),
    (16, "16 — Data Strategy",                   "16_data_strategy.md"),
]

# Moduły: (name, source_doc_number)
MODULES = [
    ("BriefParser",       8),
    ("SemanticMapper",    9),
    ("EstimationEngine",  10),
    ("WorkPlanner",       11),
    ("ItdocConnector",    12),
    ("LLMAdapter",        7),
    ("IngestionService",  5),
    ("WebhookService",    5),
]

# Tabele DB
DB_TABLES = [
    "projects",
    "briefs",
    "mapping_results",
    "estimation_reports",
    "work_plans",
    "work_packages",
    "llm_calls_log",
    "webhook_subscriptions",
    "ingestion_jobs",
    "custom_templates",
    "mapping_quality_snapshots",
]

# Pliki analiz z numerem rundy
ANALYSIS_FILES = [
    (2, "ANALIZA_RUNDA_2.md"),
    (3, "ANALIZA_RUNDA_3.md"),
    (4, "ANALIZA_RUNDA_4.md"),
    (5, "ANALIZA_RUNDA_5.md"),
]

# Wzorce krawędź module → tables
MODULE_STORES_IN = {
    "BriefParser":      ["briefs"],
    "SemanticMapper":   ["mapping_results"],
    "EstimationEngine": ["estimation_reports"],
    "WorkPlanner":      ["work_plans", "work_packages"],
    "LLMAdapter":       ["llm_calls_log"],
    "WebhookService":   ["webhook_subscriptions"],
    "IngestionService": ["ingestion_jobs", "custom_templates"],
}

# Krawędzie module → module (depends_on)
MODULE_DEPS = [
    ("SemanticMapper",   "ItdocConnector"),
    ("SemanticMapper",   "LLMAdapter"),
    ("BriefParser",      "LLMAdapter"),
    ("EstimationEngine", "SemanticMapper"),
    ("WorkPlanner",      "EstimationEngine"),
    ("IngestionService", "LLMAdapter"),
]

# spec → module (implements): doc_number → module_name
SPEC_IMPLEMENTS = {
    8:  "BriefParser",
    9:  "SemanticMapper",
    10: "EstimationEngine",
    11: "WorkPlanner",
    12: "ItdocConnector",
    7:  "LLMAdapter",
}

# Epiki PM
EPICS = [
    "Faza 0 — Pre-flight i infrastruktura",
    "Faza 1 — Core API i ItdocConnector",
    "Faza 2 — BriefParser i SemanticMapper",
    "Faza 3 — EstimationEngine i WorkPlanner",
    "Faza 4 — Ingestia i WebhookService",
    "Faza 5 — Hardening i production-ready",
]

# epic → spec references (epic index 0-based → doc numbers)
EPIC_REFS = {
    1: [3, 4, 5],
    2: [8, 9],
    3: [10, 11],
    4: [5, 7],
    5: [13, 14, 15],
}

GOALS = [
    "AI Documentation Workshop MVP",
    "Narzędzie AI dla inżynierów analitycznych",
]

# ─────────────────────────────────────────────
# Parsery
# ─────────────────────────────────────────────

def parse_openapi_paths(yaml_path: Path) -> list[tuple[str, str]]:
    """Zwraca listę (method, path) z pliku OpenAPI."""
    results = []
    try:
        import yaml  # PyYAML
        with open(yaml_path) as f:
            spec = yaml.safe_load(f)
        for path, methods in spec.get("paths", {}).items():
            for method in methods:
                if method.lower() in ("get", "post", "put", "patch", "delete"):
                    results.append((method.upper(), path))
    except Exception as exc:
        print(f"  ⚠️  YAML parse error ({exc}), fallback do regex")
        # Fallback regex: linie "  /path:"
        path_re = re.compile(r"^  (/[^\s:]+):")
        method_re = re.compile(r"^\s{4}(get|post|put|patch|delete):")
        current_path = None
        with open(yaml_path) as f:
            for line in f:
                pm = path_re.match(line)
                if pm:
                    current_path = pm.group(1)
                mm = method_re.match(line)
                if mm and current_path:
                    results.append((mm.group(1).upper(), current_path))
    return results


def parse_findings(md_path: Path, round_num: int) -> list[dict]:
    """Wyciąga znaleziska z pliku analizy."""
    findings = []
    content = md_path.read_text(encoding="utf-8")

    # Pattern: ### X-NN 🔴/🟡/🟢 ... — tytuł
    pattern = re.compile(
        r"^###\s+([A-Z]-\d+)\s*"
        r"(🔴|🟡|🟢)?\s*"
        r"(?:KRYTYCZNE|WAŻNE|DROBNE)?\s*[—\-–]?\s*"
        r"(.+)$",
        re.MULTILINE,
    )
    # Alternatywny pattern: #### X-NN: tytuł
    pattern2 = re.compile(
        r"^####\s+([A-Z]-\d+):\s*(.+)$",
        re.MULTILINE,
    )

    severity_map = {"🔴": "critical", "🟡": "important", "🟢": "minor"}

    for m in pattern.finditer(content):
        finding_id = m.group(1)
        emoji = (m.group(2) or "").strip()
        title = m.group(3).strip()
        # Usuń zbędne fragmenty tytułu
        title = re.sub(r"\s*(🔴|🟡|🟢)\s*", " ", title).strip()
        severity = severity_map.get(emoji, "minor")
        findings.append({
            "id": finding_id,
            "title": f"{finding_id}: {title}",
            "severity": severity,
            "round": round_num,
        })

    for m in pattern2.finditer(content):
        finding_id = m.group(1)
        title = m.group(2).strip()
        # Unikaj duplikatów
        if not any(f["id"] == finding_id for f in findings):
            # Sprawdź severity z kontekstu (szukaj emoji wokół)
            start = max(0, m.start() - 5)
            ctx = content[start: m.start() + 10]
            if "🔴" in ctx:
                severity = "critical"
            elif "🟡" in ctx:
                severity = "important"
            else:
                severity = "minor"
            findings.append({
                "id": finding_id,
                "title": f"{finding_id}: {title}",
                "severity": severity,
                "round": round_num,
            })

    return findings


def infer_finding_doc(finding_id: str, content: str) -> list[int]:
    """Próbuje znaleźć numery dok. (1-16) powiązane ze znaleziskiem."""
    docs = set()
    # Szukaj "dok.NN" w treści sekcji znaleziska
    for m in re.finditer(r"dok\.(\d+)", content):
        n = int(m.group(1))
        if 1 <= n <= 16:
            docs.add(n)
    return sorted(docs)


# ─────────────────────────────────────────────
# Główna logika ingestii
# ─────────────────────────────────────────────

class Ingester:
    def __init__(self, conn, dry_run: bool = False):
        self.conn = conn
        self.dry_run = dry_run
        self.nodes_created = 0
        self.edges_created = 0
        # Lookup: doc_number → node_id
        self.spec_nodes: dict[int, str] = {}
        # Lookup: name → node_id (modules, tables, epics, goals)
        self.module_nodes: dict[str, str] = {}
        self.table_nodes: dict[str, str] = {}
        self.epic_nodes: dict[str, str] = {}
        self.goal_nodes: dict[str, str] = {}

    def _node(self, type_id: str, title: str, **kwargs) -> str:
        if self.dry_run:
            print(f"  [DRY] węzeł {type_id} — {title}")
            self.nodes_created += 1
            return f"dry-{type_id}-{title[:20]}"
        node_id = create_node(self.conn, type_id, title, **kwargs)
        print(f"  ✓ węzeł [{type_id}] {title[:70]}")
        self.nodes_created += 1
        return node_id

    def _edge(self, from_id: str, to_id: str, edge_type: str) -> None:
        if "dry-" in (from_id + to_id):
            if self.dry_run:
                print(f"  [DRY] krawędź {from_id} --{edge_type}--> {to_id}")
            self.edges_created += 1
            return
        create_edge(self.conn, from_id, to_id, edge_type)
        self.edges_created += 1

    # ── 1. Spec docs ──────────────────────────────
    def ingest_spec_docs(self):
        print("\n📄 [1/7] Spec docs (docs:spec)")
        for doc_num, title, filename in SPEC_DOCS:
            fp = WORKSHOP_DIR / filename
            body = ""
            if fp.exists():
                try:
                    body = fp.read_text(encoding="utf-8")[:2000]
                except Exception:
                    pass
            else:
                print(f"  ⚠️  Plik nie istnieje: {fp}")

            node_id = self._node(
                "docs:spec", title,
                body=body,
                source_file=str(fp.relative_to(Path(__file__).parent.parent)),
                metadata={"doc_number": doc_num},
            )
            self.spec_nodes[doc_num] = node_id

            # Zapisz do doc_specs jeśli nie dry-run
            if not self.dry_run:
                self.conn.execute(
                    "INSERT OR IGNORE INTO doc_specs (node_id, doc_number, file_path, version) VALUES (?, ?, ?, ?)",
                    (node_id, doc_num, str(fp), "1.0"),
                )
                self.conn.commit()

    # ── 2. Moduły ─────────────────────────────────
    def ingest_modules(self):
        print("\n🔧 [2/7] Moduły (docs:module)")
        for name, src_doc_num in MODULES:
            node_id = self._node(
                "docs:module", name,
                metadata={"source_doc": src_doc_num},
            )
            self.module_nodes[name] = node_id
            if not self.dry_run:
                self.conn.execute(
                    "INSERT OR IGNORE INTO doc_modules (node_id, module_type, spec_doc_id) VALUES (?, ?, ?)",
                    (node_id, "service", self.spec_nodes.get(src_doc_num)),
                )
                self.conn.commit()

    # ── 3. Endpointy ──────────────────────────────
    def ingest_endpoints(self):
        print("\n🌐 [3/7] Endpointy (docs:endpoint)")
        yaml_path = WORKSHOP_DIR / "06_openapi_specification.yaml"
        if not yaml_path.exists():
            print(f"  ⚠️  Brak pliku: {yaml_path}")
            return
        paths = parse_openapi_paths(yaml_path)
        print(f"  Znaleziono {len(paths)} endpoint(ów)")
        for method, path in paths:
            title = f"{method} {path}"
            self._node(
                "docs:endpoint", title,
                source_file="docs/workshop/06_openapi_specification.yaml",
            )

    # ── 4. Tabele DB ──────────────────────────────
    def ingest_tables(self):
        print("\n🗄️  [4/7] Tabele DB (docs:table)")
        md_path = WORKSHOP_DIR / "04_data_model_postgresql.md"
        for table_name in DB_TABLES:
            body = ""
            if md_path.exists():
                content = md_path.read_text(encoding="utf-8")
                # Szukaj fragmentu przy nazwie tabeli
                m = re.search(
                    rf"CREATE TABLE\s+(?:IF NOT EXISTS\s+)?{re.escape(table_name)}\s*\((.+?)(?:\);|\n\n)",
                    content, re.DOTALL | re.IGNORECASE,
                )
                if m:
                    body = f"CREATE TABLE {table_name} ({m.group(1)[:500]}..."

            node_id = self._node(
                "docs:table", table_name,
                body=body,
                source_file="docs/workshop/04_data_model_postgresql.md",
            )
            self.table_nodes[table_name] = node_id

    # ── 5. Znaleziska ─────────────────────────────
    def ingest_findings(self):
        print("\n🔍 [5/7] Znaleziska (docs:finding)")
        for round_num, filename in ANALYSIS_FILES:
            md_path = WORKSHOP_DIR / filename
            if not md_path.exists():
                print(f"  ⚠️  Plik nie istnieje: {md_path}")
                continue
            findings = parse_findings(md_path, round_num)
            print(f"  Runda {round_num}: {len(findings)} znalezisk")
            content = md_path.read_text(encoding="utf-8")
            for f in findings:
                node_id = self._node(
                    "docs:finding", f["title"],
                    metadata={
                        "severity": f["severity"],
                        "round": round_num,
                        "resolved": False,
                    },
                    source_file=f"docs/workshop/{filename}",
                )
                if not self.dry_run:
                    self.conn.execute(
                        "INSERT OR IGNORE INTO doc_findings "
                        "(node_id, round, finding_id, severity, resolved) VALUES (?, ?, ?, ?, ?)",
                        (node_id, round_num, f["id"], f["severity"], 0),
                    )
                    self.conn.commit()

                # Powiązanie finding → spec doc (fixes)
                doc_nums = infer_finding_doc(f["id"], content)
                for doc_num in doc_nums:
                    if doc_num in self.spec_nodes:
                        self._edge(node_id, self.spec_nodes[doc_num], "fixes")

    # ── 6. Węzły PM ──────────────────────────────
    def ingest_pm(self):
        print("\n🎯 [6/7] Cele i epiki PM (pm:goal, pm:epic)")

        # Cele
        for goal_title in GOALS:
            node_id = self._node("pm:goal", goal_title)
            self.goal_nodes[goal_title] = node_id
            if not self.dry_run:
                self.conn.execute(
                    "INSERT OR IGNORE INTO pm_goals (node_id, target_date, okr) VALUES (?, ?, ?)",
                    (node_id, None, None),
                )
                self.conn.commit()

        # Epiki
        main_goal_id = self.goal_nodes.get(GOALS[0])
        for epic_title in EPICS:
            node_id = self._node(
                "pm:epic", epic_title,
                source_file="docs/workshop/15_implementation_roadmap.md",
            )
            self.epic_nodes[epic_title] = node_id
            if not self.dry_run:
                self.conn.execute(
                    "INSERT OR IGNORE INTO pm_epics (node_id, goal_id, start_date, end_date) VALUES (?, ?, ?, ?)",
                    (node_id, main_goal_id, None, None),
                )
                self.conn.commit()

    # ── 7. Krawędzie ─────────────────────────────
    def ingest_edges(self):
        print("\n🔗 [7/7] Krawędzie")

        # spec → module (implements)
        for doc_num, mod_name in SPEC_IMPLEMENTS.items():
            spec_id = self.spec_nodes.get(doc_num)
            mod_id = self.module_nodes.get(mod_name)
            if spec_id and mod_id:
                self._edge(spec_id, mod_id, "implements")

        # module → module (depends_on)
        for from_mod, to_mod in MODULE_DEPS:
            from_id = self.module_nodes.get(from_mod)
            to_id = self.module_nodes.get(to_mod)
            if from_id and to_id:
                self._edge(from_id, to_id, "depends_on")

        # module → table (stores_in)
        for mod_name, tables in MODULE_STORES_IN.items():
            mod_id = self.module_nodes.get(mod_name)
            if not mod_id:
                continue
            for tbl in tables:
                tbl_id = self.table_nodes.get(tbl)
                if tbl_id:
                    self._edge(mod_id, tbl_id, "stores_in")

        # epic → spec (references)
        for epic_idx, doc_nums in EPIC_REFS.items():
            epic_title = EPICS[epic_idx]
            epic_id = self.epic_nodes.get(epic_title)
            if not epic_id:
                continue
            for doc_num in doc_nums:
                spec_id = self.spec_nodes.get(doc_num)
                if spec_id:
                    self._edge(epic_id, spec_id, "references")

        # epic → epic (precedes)
        for i in range(len(EPICS) - 1):
            from_id = self.epic_nodes.get(EPICS[i])
            to_id = self.epic_nodes.get(EPICS[i + 1])
            if from_id and to_id:
                self._edge(from_id, to_id, "precedes")

        # epic → goal (part_of)
        main_goal_id = self.goal_nodes.get(GOALS[0])
        if main_goal_id:
            for epic_title in EPICS:
                epic_id = self.epic_nodes.get(epic_title)
                if epic_id:
                    self._edge(epic_id, main_goal_id, "part_of")

    def run(self):
        self.ingest_spec_docs()
        self.ingest_modules()
        self.ingest_endpoints()
        self.ingest_tables()
        self.ingest_findings()
        self.ingest_pm()
        self.ingest_edges()


# ─────────────────────────────────────────────
# Punkt wejścia
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Wczytuje dokumentację Warsztatu do Meta-Grafu."
    )
    parser.add_argument("--dry-run", action="store_true", help="Pokaż co by stworzył")
    parser.add_argument("--reset", action="store_true", help="Wyczyść węzły Warsztatu i zacznij od nowa")
    args = parser.parse_args()

    print(f"📁 Workshop dir: {WORKSHOP_DIR}")
    print(f"🗄️  DB path:      {DB_PATH}")

    with get_conn(DB_PATH) as conn:
        if args.reset:
            print("\n⚠️  Reset: usuwam węzły z warstw docs i pm...")
            conn.execute("DELETE FROM edges WHERE from_node IN (SELECT id FROM nodes WHERE layer IN ('docs','pm'))")
            conn.execute("DELETE FROM edges WHERE to_node IN (SELECT id FROM nodes WHERE layer IN ('docs','pm'))")
            conn.execute("DELETE FROM events WHERE node_id IN (SELECT id FROM nodes WHERE layer IN ('docs','pm'))")
            conn.execute("DELETE FROM doc_specs WHERE node_id IN (SELECT id FROM nodes WHERE layer='docs')")
            conn.execute("DELETE FROM doc_modules WHERE node_id IN (SELECT id FROM nodes WHERE layer='docs')")
            conn.execute("DELETE FROM doc_findings WHERE node_id IN (SELECT id FROM nodes WHERE layer='docs')")
            conn.execute("DELETE FROM pm_goals WHERE node_id IN (SELECT id FROM nodes WHERE layer='pm')")
            conn.execute("DELETE FROM pm_epics WHERE node_id IN (SELECT id FROM nodes WHERE layer='pm')")
            conn.execute("DELETE FROM nodes WHERE layer IN ('docs', 'pm')")
            conn.commit()
            print("  ✓ Reset gotowy\n")

        ingester = Ingester(conn, dry_run=args.dry_run)
        ingester.run()

        if not args.dry_run:
            stats = graph_stats(conn)
            print("\n" + "=" * 60)
            print("✅ Ingestia zakończona!")
            print(f"   Węzły stworzone w tej sesji : {ingester.nodes_created}")
            print(f"   Krawędzie stworzone          : {ingester.edges_created}")
            print(f"\n   Stan grafu (łącznie):")
            print(f"   Węzły aktywne : {stats['nodes']}")
            print(f"   Krawędzie     : {stats['edges']}")
            print(f"\n   Rozkład warstw:")
            for layer, count in sorted(stats["by_layer"].items()):
                print(f"     {layer:<12} {count:>5}")
            print("=" * 60)
        else:
            print(f"\n[DRY-RUN] Utworzyłby: {ingester.nodes_created} węzłów, {ingester.edges_created} krawędzi")


if __name__ == "__main__":
    main()
