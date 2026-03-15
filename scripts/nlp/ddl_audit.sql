-- scripts/nlp/ddl_audit.sql
-- Schemat tabel dla audytu dokumentacji projektowej NLP
-- Uruchamiany automatycznie przez DocAuditor._ensure_schema()

-- -------------------------------------------------------------------
-- Kompletność dokumentów — jeden wiersz per dokument per przebieg
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doc_completeness (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id            TEXT    NOT NULL,
    doc_path          TEXT    NOT NULL,
    doc_type          TEXT,                    -- wykryty typ: architecture/testing/...
    heading_count     INTEGER DEFAULT 0,
    token_count       INTEGER DEFAULT 0,
    completeness_score REAL   DEFAULT 1.0,    -- 0.0–1.0
    gap_error_count   INTEGER DEFAULT 0,
    gap_warning_count INTEGER DEFAULT 0,
    gap_info_count    INTEGER DEFAULT 0,
    analysed_at       TEXT    NOT NULL,
    UNIQUE(run_id, doc_path)
);

-- -------------------------------------------------------------------
-- Wyniki detekcji braków — jeden wiersz per brak per dokument
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doc_audit_findings (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id       TEXT    NOT NULL,
    doc_path     TEXT    NOT NULL,
    gap_type     TEXT    NOT NULL,  -- missing_section | empty_section |
                                    -- missing_metadata | shallow_structure |
                                    -- heading_depth_inconsistency
    severity     TEXT    NOT NULL,  -- ERROR | WARNING | INFO
    section      TEXT,
    description  TEXT    NOT NULL,
    weight       INTEGER DEFAULT 1,
    analysed_at  TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_findings_run_doc
    ON doc_audit_findings(run_id, doc_path);

CREATE INDEX IF NOT EXISTS idx_findings_severity
    ON doc_audit_findings(severity);

-- -------------------------------------------------------------------
-- Duplikaty — para dokumentów ze wskaźnikiem podobieństwa
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doc_duplicates (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id          TEXT    NOT NULL,
    doc_a           TEXT    NOT NULL,
    doc_b           TEXT    NOT NULL,
    similarity      REAL    NOT NULL,   -- 0.0–1.0
    method          TEXT    NOT NULL,   -- cosine_tfidf | jaccard_shingle | both
    duplicate_type  TEXT    NOT NULL,   -- exact | extending | thematic | partial
    description     TEXT,
    analysed_at     TEXT    NOT NULL,
    UNIQUE(run_id, doc_a, doc_b)
);

CREATE INDEX IF NOT EXISTS idx_duplicates_run
    ON doc_duplicates(run_id);

-- -------------------------------------------------------------------
-- Relacje między dokumentami (linki, cross-referencje, implikacje)
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doc_relations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id          TEXT    NOT NULL,
    source_doc      TEXT    NOT NULL,
    target_doc      TEXT    NOT NULL,
    relation_type   TEXT    NOT NULL,   -- explicit_link | name_mention |
                                        -- thematic_overlap | implication |
                                        -- contradiction | extends
    link_text       TEXT,               -- tekst linku lub fraza trigger
    confidence      REAL    DEFAULT 1.0,
    analysed_at     TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_relations_source
    ON doc_relations(run_id, source_doc);

CREATE INDEX IF NOT EXISTS idx_relations_target
    ON doc_relations(run_id, target_doc);

-- -------------------------------------------------------------------
-- Metadane przebiegów audytu
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doc_audit_runs (
    run_id        TEXT PRIMARY KEY,
    scanned_dir   TEXT NOT NULL,
    doc_count     INTEGER DEFAULT 0,
    started_at    TEXT NOT NULL,
    finished_at   TEXT,
    status        TEXT DEFAULT 'running',  -- running | done | failed
    config        TEXT                     -- JSON z parametrami
);
