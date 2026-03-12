-- 001_init.sql — Pełny schemat Meta-Grafu
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS node_types (
    id TEXT PRIMARY KEY,
    layer TEXT NOT NULL CHECK (layer IN ('pm', 'scrum', 'docs', 'system')),
    description TEXT
);

CREATE TABLE IF NOT EXISTS edge_types (
    id TEXT PRIMARY KEY,
    description TEXT,
    directed INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS nodes (
    id TEXT PRIMARY KEY,
    type_id TEXT NOT NULL REFERENCES node_types(id),
    title TEXT NOT NULL,
    body TEXT,
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'draft', 'blocked', 'done', 'archived')),
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    metadata TEXT DEFAULT '{}',
    layer TEXT NOT NULL CHECK (layer IN ('pm', 'scrum', 'docs', 'system')),
    source_file TEXT,
    source_section TEXT,
    tags TEXT,  -- spacja-rozdzielone stemmy (pl_stems dla FTS + filtrów)
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS edges (
    id TEXT PRIMARY KEY,
    from_node TEXT NOT NULL REFERENCES nodes(id),
    to_node TEXT NOT NULL REFERENCES nodes(id),
    type_id TEXT NOT NULL REFERENCES edge_types(id),
    weight REAL DEFAULT 1.0,
    label TEXT,
    metadata TEXT DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS pm_goals (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    target_date TEXT,
    completion_pct INTEGER DEFAULT 0,
    okr TEXT
);

CREATE TABLE IF NOT EXISTS pm_epics (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    goal_id TEXT REFERENCES nodes(id),
    story_points_total INTEGER DEFAULT 0,
    story_points_done INTEGER DEFAULT 0,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE IF NOT EXISTS pm_risks (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    probability INTEGER DEFAULT 3 CHECK (probability BETWEEN 1 AND 5),
    impact INTEGER DEFAULT 3 CHECK (impact BETWEEN 1 AND 5),
    score INTEGER GENERATED ALWAYS AS (probability * impact) STORED,
    mitigation TEXT,
    status TEXT DEFAULT 'open' CHECK (status IN ('open', 'mitigated', 'accepted', 'closed'))
);

CREATE TABLE IF NOT EXISTS scrum_sprints (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    sprint_number INTEGER,
    start_date TEXT,
    end_date TEXT,
    goal TEXT,
    velocity INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS scrum_stories (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    epic_id TEXT REFERENCES nodes(id),
    sprint_id TEXT REFERENCES nodes(id),
    story_points INTEGER DEFAULT 0,
    acceptance_criteria TEXT
);

CREATE TABLE IF NOT EXISTS scrum_tasks (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    story_id TEXT REFERENCES nodes(id),
    assignee TEXT,
    estimate_h REAL DEFAULT 0,
    actual_h REAL,
    task_type TEXT DEFAULT 'feature' CHECK (task_type IN ('feature', 'bug', 'chore', 'spike'))
);

CREATE TABLE IF NOT EXISTS doc_specs (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    doc_number INTEGER,
    file_path TEXT,
    version TEXT DEFAULT '1.0',
    total_sections INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS doc_modules (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    module_type TEXT,
    spec_doc_id TEXT REFERENCES nodes(id)
);

CREATE TABLE IF NOT EXISTS doc_findings (
    node_id TEXT PRIMARY KEY REFERENCES nodes(id),
    round INTEGER,
    finding_id TEXT,
    severity TEXT CHECK (severity IN ('critical', 'important', 'minor')),
    resolved INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    node_id TEXT,
    event_type TEXT NOT NULL,
    payload TEXT DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS ingest_queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT NOT NULL,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'done', 'failed')),
    node_ids_created TEXT DEFAULT '[]',
    error TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    processed_at TEXT
);

CREATE TABLE IF NOT EXISTS query_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_text TEXT NOT NULL,
    result_count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

INSERT OR IGNORE INTO node_types VALUES
    ('pm:goal',         'pm',     'Cel strategiczny projektu'),
    ('pm:epic',         'pm',     'Epika — skupienie pracy nad funkcjonalnością'),
    ('pm:risk',         'pm',     'Ryzyko projektowe'),
    ('pm:milestone',    'pm',     'Kamień milowy'),
    ('scrum:sprint',    'scrum',  'Sprint Scrum'),
    ('scrum:story',     'scrum',  'User Story'),
    ('scrum:task',      'scrum',  'Task implementacyjny'),
    ('scrum:bug',       'scrum',  'Bug do naprawy'),
    ('docs:spec',       'docs',   'Dokument specyfikacji (dok.01-16)'),
    ('docs:section',    'docs',   'Sekcja dokumentu specyfikacji'),
    ('docs:module',     'docs',   'Modul systemu'),
    ('docs:endpoint',   'docs',   'Endpoint API REST'),
    ('docs:table',      'docs',   'Tabela bazy danych PostgreSQL'),
    ('docs:finding',    'docs',   'Znalezisko z analizy (Runda 1-5)'),
    ('docs:requirement','docs',   'Wymaganie funkcjonalne'),
    ('system:config',   'system', 'Konfiguracja systemu');

INSERT OR IGNORE INTO edge_types VALUES
    ('implements',   'Task/Story implementuje requirement lub spec', 1),
    ('depends_on',   'Wzezel zalezy od innego wezla', 1),
    ('part_of',      'Wzezel jest czescia nadrzednego wezla', 1),
    ('references',   'Wzezel referuje inny wezel', 1),
    ('fixes',        'Finding naprawia spec lub modul', 1),
    ('exposes',      'Modul eksponuje endpoint', 1),
    ('stores_in',    'Modul przechowuje dane w tabeli', 1),
    ('blocks',       'Wzezel blokuje inny wezel', 1),
    ('related_to',   'Luzne powiazanie tematyczne', 0),
    ('precedes',     'Wzezel poprzedza inny (kolejnosc)', 1),
    ('tests',        'Test sprawdza modul/wymaganie', 1),
    ('derives_from', 'Wzezel pochodzi z innego wezla', 1);

CREATE INDEX IF NOT EXISTS idx_nodes_type   ON nodes(type_id);
CREATE INDEX IF NOT EXISTS idx_nodes_layer  ON nodes(layer);
CREATE INDEX IF NOT EXISTS idx_nodes_status ON nodes(status);
CREATE INDEX IF NOT EXISTS idx_edges_from   ON edges(from_node);
CREATE INDEX IF NOT EXISTS idx_edges_to     ON edges(to_node);
CREATE INDEX IF NOT EXISTS idx_edges_type   ON edges(type_id);
CREATE INDEX IF NOT EXISTS idx_events_node  ON events(node_id);

CREATE VIRTUAL TABLE IF NOT EXISTS nodes_fts
    USING fts5(id, title, body, content='nodes', content_rowid='rowid');
