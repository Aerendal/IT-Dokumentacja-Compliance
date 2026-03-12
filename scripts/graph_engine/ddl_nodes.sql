PRAGMA foreign_keys = ON;

-- Base tables (legacy-compatible baseline)
CREATE TABLE IF NOT EXISTS nodes (
  node_uid TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN ('doc', 'sec', 'subsec', 'section')),
  doc_uid TEXT REFERENCES docs(doc_uid),
  parent_node_uid TEXT REFERENCES nodes(node_uid),
  title TEXT,
  key_norm TEXT,
  anchor TEXT,
  ordinal INTEGER,
  start_line INTEGER,
  end_line INTEGER,
  metrics_json TEXT,
  status TEXT CHECK (status IN ('unknown', 'ok', 'needs_structure', 'needs_content', 'needs_links', 'blocked', 'active', 'inactive', 'draft', 'archived', 'placeholder')),
  node_kind TEXT CHECK (node_kind IN ('doc', 'section')),
  title_norm TEXT,
  source_table TEXT,
  created_at_utc TEXT,
  updated_at_utc TEXT
);

CREATE TABLE IF NOT EXISTS edges_manual (
  edge_uid TEXT PRIMARY KEY,
  from_node_uid TEXT NOT NULL,
  to_node_uid TEXT NOT NULL,
  link_type TEXT NOT NULL,
  direction TEXT NOT NULL DEFAULT 'forward' CHECK (direction IN ('forward', 'reverse', 'bidirectional', 'undirected')),
  strength TEXT NOT NULL DEFAULT 'navigational' CHECK (strength IN ('required', 'navigational', 'optional', 'blocking', 'informational')),
  rationale TEXT,
  impact_area TEXT,
  impact_level TEXT,
  source TEXT,
  source_row_id INTEGER,
  created_at_utc TEXT NOT NULL,
  status TEXT CHECK (status IN ('active', 'inactive', 'deprecated', 'unknown')),
  edge_manual_id TEXT UNIQUE,
  source_table TEXT,
  updated_at_utc TEXT,
  FOREIGN KEY (from_node_uid) REFERENCES nodes(node_uid),
  FOREIGN KEY (to_node_uid) REFERENCES nodes(node_uid)
);

CREATE TABLE IF NOT EXISTS edges_inferred (
  edge_uid TEXT PRIMARY KEY,
  from_node_uid TEXT NOT NULL,
  to_node_uid TEXT NOT NULL,
  link_type TEXT NOT NULL,
  direction TEXT NOT NULL DEFAULT 'forward' CHECK (direction IN ('forward', 'reverse', 'bidirectional', 'undirected')),
  strength TEXT NOT NULL DEFAULT 'navigational' CHECK (strength IN ('required', 'navigational', 'optional', 'blocking', 'informational')),
  impact_area TEXT,
  impact_level TEXT,
  confidence REAL NOT NULL CHECK (confidence >= 0.0 AND confidence <= 1.0),
  evidence_json TEXT,
  created_at_utc TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'rejected', 'deprecated', 'unknown')),
  edge_inferred_id TEXT UNIQUE,
  relation_kind TEXT,
  algorithm_version TEXT,
  updated_at_utc TEXT,
  source TEXT,
  source_row_id INTEGER,
  FOREIGN KEY (from_node_uid) REFERENCES nodes(node_uid),
  FOREIGN KEY (to_node_uid) REFERENCES nodes(node_uid)
);

CREATE TABLE IF NOT EXISTS influence (
  src_node_uid TEXT NOT NULL,
  dst_node_uid TEXT NOT NULL,
  influence_type TEXT NOT NULL,
  level TEXT CHECK (level IN ('low', 'medium', 'high', 'critical', 'unknown')),
  path_json TEXT,
  computed_at_utc TEXT NOT NULL,
  influence_id TEXT,
  source_node_uid TEXT,
  target_node_uid TEXT,
  score REAL,
  algorithm_version TEXT,
  notes TEXT,
  details_json TEXT,
  PRIMARY KEY (src_node_uid, dst_node_uid, influence_type, computed_at_utc),
  FOREIGN KEY (src_node_uid) REFERENCES nodes(node_uid),
  FOREIGN KEY (dst_node_uid) REFERENCES nodes(node_uid)
);

-- Requested additive schema for nodes
ALTER TABLE nodes ADD COLUMN kind TEXT CHECK (kind IN ('doc', 'sec', 'subsec', 'section'));
ALTER TABLE nodes ADD COLUMN parent_node_uid TEXT REFERENCES nodes(node_uid);
ALTER TABLE nodes ADD COLUMN key_norm TEXT;
ALTER TABLE nodes ADD COLUMN ordinal INTEGER;
ALTER TABLE nodes ADD COLUMN start_line INTEGER;
ALTER TABLE nodes ADD COLUMN end_line INTEGER;
ALTER TABLE nodes ADD COLUMN metrics_json TEXT;

-- Fast join maps (additive)
CREATE TABLE IF NOT EXISTS node_map_docs (
  doc_uid TEXT PRIMARY KEY REFERENCES docs(doc_uid),
  node_uid TEXT NOT NULL UNIQUE REFERENCES nodes(node_uid),
  created_at_utc TEXT,
  updated_at_utc TEXT
);

CREATE TABLE IF NOT EXISTS node_map_sections (
  section_uid TEXT PRIMARY KEY REFERENCES sections(section_uid),
  node_uid TEXT NOT NULL UNIQUE REFERENCES nodes(node_uid),
  created_at_utc TEXT,
  updated_at_utc TEXT
);

-- Requested additive schema for edges_manual
ALTER TABLE edges_manual ADD COLUMN edge_uid TEXT;
ALTER TABLE edges_manual ADD COLUMN impact_area TEXT;
ALTER TABLE edges_manual ADD COLUMN impact_level TEXT;
ALTER TABLE edges_manual ADD COLUMN source TEXT;
ALTER TABLE edges_manual ADD COLUMN status TEXT CHECK (status IN ('active', 'inactive', 'deprecated', 'unknown'));

-- Requested additive schema for edges_inferred
ALTER TABLE edges_inferred ADD COLUMN edge_uid TEXT;
ALTER TABLE edges_inferred ADD COLUMN link_type TEXT;
ALTER TABLE edges_inferred ADD COLUMN direction TEXT CHECK (direction IN ('forward', 'reverse', 'bidirectional', 'undirected'));
ALTER TABLE edges_inferred ADD COLUMN strength TEXT CHECK (strength IN ('required', 'navigational', 'optional', 'blocking', 'informational'));
ALTER TABLE edges_inferred ADD COLUMN impact_area TEXT;
ALTER TABLE edges_inferred ADD COLUMN impact_level TEXT;
ALTER TABLE edges_inferred ADD COLUMN source TEXT;
ALTER TABLE edges_inferred ADD COLUMN source_row_id INTEGER;

-- Requested additive schema for influence
ALTER TABLE influence ADD COLUMN src_node_uid TEXT REFERENCES nodes(node_uid);
ALTER TABLE influence ADD COLUMN dst_node_uid TEXT REFERENCES nodes(node_uid);
ALTER TABLE influence ADD COLUMN influence_type TEXT;
ALTER TABLE influence ADD COLUMN level TEXT CHECK (level IN ('low', 'medium', 'high', 'critical', 'unknown'));
ALTER TABLE influence ADD COLUMN path_json TEXT;

-- Backfill aliases
UPDATE nodes SET kind = node_kind WHERE kind IS NULL;
UPDATE nodes SET key_norm = COALESCE(title_norm, lower(trim(title))) WHERE key_norm IS NULL;
UPDATE edges_manual SET edge_uid = edge_manual_id WHERE edge_uid IS NULL;
UPDATE edges_manual SET source = source_table WHERE source IS NULL AND source_table IS NOT NULL;
UPDATE edges_inferred SET edge_uid = edge_inferred_id WHERE edge_uid IS NULL;
UPDATE edges_inferred SET link_type = relation_kind WHERE link_type IS NULL AND relation_kind IS NOT NULL;
UPDATE influence SET src_node_uid = source_node_uid WHERE src_node_uid IS NULL;
UPDATE influence SET dst_node_uid = target_node_uid WHERE dst_node_uid IS NULL;

-- Indexes for frequent queries
CREATE INDEX IF NOT EXISTS idx_nodes_kind ON nodes(node_kind);
CREATE INDEX IF NOT EXISTS idx_nodes_kind_v2 ON nodes(kind);
CREATE INDEX IF NOT EXISTS idx_nodes_doc_uid ON nodes(doc_uid);
CREATE INDEX IF NOT EXISTS idx_nodes_key_norm ON nodes(key_norm);
CREATE INDEX IF NOT EXISTS idx_nodes_status ON nodes(status);

CREATE INDEX IF NOT EXISTS idx_node_map_docs_node_uid ON node_map_docs(node_uid);
CREATE INDEX IF NOT EXISTS idx_node_map_sections_node_uid ON node_map_sections(node_uid);

CREATE UNIQUE INDEX IF NOT EXISTS idx_edges_manual_edge_uid_uniq ON edges_manual(edge_uid);
CREATE INDEX IF NOT EXISTS idx_edges_manual_from ON edges_manual(from_node_uid);
CREATE INDEX IF NOT EXISTS idx_edges_manual_to ON edges_manual(to_node_uid);
CREATE INDEX IF NOT EXISTS idx_edges_manual_status ON edges_manual(status);
CREATE INDEX IF NOT EXISTS idx_edges_manual_source ON edges_manual(source, source_row_id);

CREATE UNIQUE INDEX IF NOT EXISTS idx_edges_inferred_edge_uid_uniq ON edges_inferred(edge_uid);
CREATE INDEX IF NOT EXISTS idx_edges_inferred_from ON edges_inferred(from_node_uid);
CREATE INDEX IF NOT EXISTS idx_edges_inferred_to ON edges_inferred(to_node_uid);
CREATE INDEX IF NOT EXISTS idx_edges_inferred_confidence ON edges_inferred(confidence);
CREATE INDEX IF NOT EXISTS idx_edges_inferred_status ON edges_inferred(status);

CREATE INDEX IF NOT EXISTS idx_influence_src ON influence(src_node_uid);
CREATE INDEX IF NOT EXISTS idx_influence_dst ON influence(dst_node_uid);
CREATE INDEX IF NOT EXISTS idx_influence_type ON influence(influence_type);
CREATE INDEX IF NOT EXISTS idx_influence_computed_at ON influence(computed_at_utc);

-- Guardrails for legacy columns where CHECK cannot be added via ALTER TABLE
CREATE TRIGGER IF NOT EXISTS trg_nodes_kind_guard_ins
BEFORE INSERT ON nodes
FOR EACH ROW
WHEN NEW.kind IS NOT NULL AND NEW.kind NOT IN ('doc', 'sec', 'subsec', 'section')
BEGIN
  SELECT RAISE(ABORT, 'nodes.kind invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_nodes_kind_guard_upd
BEFORE UPDATE OF kind ON nodes
FOR EACH ROW
WHEN NEW.kind IS NOT NULL AND NEW.kind NOT IN ('doc', 'sec', 'subsec', 'section')
BEGIN
  SELECT RAISE(ABORT, 'nodes.kind invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_nodes_status_guard_ins
BEFORE INSERT ON nodes
FOR EACH ROW
WHEN NEW.status IS NOT NULL
  AND NEW.status NOT IN ('unknown', 'ok', 'needs_structure', 'needs_content', 'needs_links', 'blocked', 'active', 'inactive', 'draft', 'archived', 'placeholder')
BEGIN
  SELECT RAISE(ABORT, 'nodes.status invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_nodes_status_guard_upd
BEFORE UPDATE OF status ON nodes
FOR EACH ROW
WHEN NEW.status IS NOT NULL
  AND NEW.status NOT IN ('unknown', 'ok', 'needs_structure', 'needs_content', 'needs_links', 'blocked', 'active', 'inactive', 'draft', 'archived', 'placeholder')
BEGIN
  SELECT RAISE(ABORT, 'nodes.status invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_edges_manual_dir_strength_ins
BEFORE INSERT ON edges_manual
FOR EACH ROW
WHEN (NEW.direction IS NOT NULL AND NEW.direction NOT IN ('forward', 'reverse', 'bidirectional', 'undirected'))
   OR (NEW.strength IS NOT NULL AND NEW.strength NOT IN ('required', 'navigational', 'optional', 'blocking', 'informational'))
BEGIN
  SELECT RAISE(ABORT, 'edges_manual direction/strength invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_edges_manual_dir_strength_upd
BEFORE UPDATE OF direction, strength ON edges_manual
FOR EACH ROW
WHEN (NEW.direction IS NOT NULL AND NEW.direction NOT IN ('forward', 'reverse', 'bidirectional', 'undirected'))
   OR (NEW.strength IS NOT NULL AND NEW.strength NOT IN ('required', 'navigational', 'optional', 'blocking', 'informational'))
BEGIN
  SELECT RAISE(ABORT, 'edges_manual direction/strength invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_edges_inferred_dir_strength_status_ins
BEFORE INSERT ON edges_inferred
FOR EACH ROW
WHEN (NEW.direction IS NOT NULL AND NEW.direction NOT IN ('forward', 'reverse', 'bidirectional', 'undirected'))
   OR (NEW.strength IS NOT NULL AND NEW.strength NOT IN ('required', 'navigational', 'optional', 'blocking', 'informational'))
   OR (NEW.status IS NOT NULL AND NEW.status NOT IN ('active', 'inactive', 'rejected', 'deprecated', 'unknown'))
BEGIN
  SELECT RAISE(ABORT, 'edges_inferred direction/strength/status invalid');
END;

CREATE TRIGGER IF NOT EXISTS trg_edges_inferred_dir_strength_status_upd
BEFORE UPDATE OF direction, strength, status ON edges_inferred
FOR EACH ROW
WHEN (NEW.direction IS NOT NULL AND NEW.direction NOT IN ('forward', 'reverse', 'bidirectional', 'undirected'))
   OR (NEW.strength IS NOT NULL AND NEW.strength NOT IN ('required', 'navigational', 'optional', 'blocking', 'informational'))
   OR (NEW.status IS NOT NULL AND NEW.status NOT IN ('active', 'inactive', 'rejected', 'deprecated', 'unknown'))
BEGIN
  SELECT RAISE(ABORT, 'edges_inferred direction/strength/status invalid');
END;
