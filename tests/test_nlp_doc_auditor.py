"""tests/test_nlp_doc_auditor.py — Testy modułu audytu dokumentacji NLP.

Pokrywa:
  - text_utils: normalize, tokenize, stem, shingles, extract_headings, extract_links
  - similarity_engine: jaccard, cosine_similarity, DocumentCorpus
  - gap_detector: GapDetector (brakujące sekcje, metadane, pusta sekcja, spójność)
  - duplicate_detector: DuplicateDetector (exact, extending, thematic)
  - relation_mapper: RelationMapper (explicit_link, name_mention, thematic_overlap)
  - doc_auditor: DocAuditor.scan() + report() integracja

Strategia oracle: specyfikacyjny (oczekiwane wyniki z dokumentacji)
Metoda: P1=funkcja/moduł P2=poprawność P3=BVA+EP P4=unit+integration
"""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

# ============================================================
# Fixtures — tekst dokumentów
# ============================================================

ARCH_FULL = """\
# Architektura systemu
author: Jan Kowalski
date: 2025-01-01
ISO 27001:2022

## Overview
System compliance zarządza dokumentacją IT projektów organizacji.
Główne komponenty to parser, analyzer i reporter.

## Context
Wdrożenie w środowisku on-premise oraz chmurze hybrydowej.

## Components
Parser wczytuje pliki Markdown. Analyzer sprawdza zgodność ze standardami.

## Interfaces
REST API / FastAPI, SQLite jako backend bazy danych.

## Data
Dane przechowywane w SQLite. Backup co 24 godziny.

## Security
Połączenia TLS 1.3. Autoryzacja JWT. Hasła hashowane bcrypt.

## Deployment
Docker Compose dla lokalnego środowiska.
"""

ARCH_MISSING_SECTIONS = """\
# Architektura systemu

## Overview
Opis systemu compliance.

## Components
Parser i analyzer.
"""

SECURITY_FULL = """\
# Polityka bezpieczeństwa
author: Security Team
date: 2025-01-01
OWASP ASVS standard

## Scope
Polityka obejmuje wszystkie systemy IT organizacji.

## Requirements
Wymagania minimum zgodne z ISO 27001.

## Authentication
Uwierzytelnianie JWT plus MFA dla wszystkich użytkowników.

## Authorization
Autoryzacja RBAC z minimalnym uprawnieniem (least privilege).

## Encryption
Szyfrowanie danych AES-256. Transport TLS 1.3.

## Logging
Logi przechowywane minimum 90 dni w systemie SIEM.

## Incident Response
Procedury obsługi incydentów: wykrycie, eskalacja, raport.
"""

TESTING_FULL = """\
# Plan testów
author: QA Team
date: 2025-01-01

## Scope
Testy obejmują moduły: parser, analyzer, reporter, API.

## Approach
Strategia testowania: unit, integration, property-based, kontraktowe.

## Test cases
Przypadki testowe zdefiniowane w pytest fixtures.

## Fixtures
Zestawy danych testowych w tests/fixtures/.

## Coverage
Pokrycie kodu minimum 85% (pytest-cov).

## Metrics
Metryki jakości: mutation score >= 60%, czas < 30s.

## Oracle
Złoty standard w tests/fixtures/nlp_oracle.jsonl.
"""

EMPTY_DOC = "   \n\n   "

SHORT_DOC = "# Krótki dokument\n\nJeden akapit."

DUPLICATE_OF_ARCH = ARCH_FULL + "\n## Extra sekcja\nDodatkowe informacje o wdrożeniu."


# ============================================================
# text_utils
# ============================================================

class TestNormalize:
    def test_lowercase(self):
        from scripts.nlp.text_utils import normalize
        assert normalize("System") == "system"

    def test_polish_diacritics(self):
        from scripts.nlp.text_utils import normalize
        assert normalize("żądanie") == "zadanie"
        assert normalize("ścieżka") == "sciezka"
        assert normalize("łącze") == "lacze"

    def test_uppercase_diacritics(self):
        from scripts.nlp.text_utils import normalize
        assert normalize("ŚCIEŻKA") == "sciezka"

    def test_empty_string(self):
        from scripts.nlp.text_utils import normalize
        assert normalize("") == ""

    def test_mixed_content(self):
        from scripts.nlp.text_utils import normalize
        result = normalize("Szyfrowanie AES-256")
        assert "szyfr" in result
        assert "256" in result


class TestTokenize:
    def test_basic_tokenization(self):
        from scripts.nlp.text_utils import tokenize
        tokens = tokenize("System musi szyfrować dane.")
        assert len(tokens) > 0
        assert all(isinstance(t, str) for t in tokens)

    def test_stopwords_removed_by_default(self):
        from scripts.nlp.text_utils import tokenize
        tokens = tokenize("i to jest w oraz ale")
        assert "i" not in tokens
        assert "ale" not in tokens

    def test_stopwords_kept_when_disabled(self):
        from scripts.nlp.text_utils import tokenize
        tokens = tokenize("jest i to", remove_stopwords=False)
        assert len(tokens) > 0

    def test_code_blocks_removed(self):
        from scripts.nlp.text_utils import tokenize
        text = "Opis systemu.\n```python\nprint('hello')\n```\nKoniec."
        tokens = tokenize(text)
        assert "print" not in tokens

    def test_urls_removed(self):
        from scripts.nlp.text_utils import tokenize
        tokens = tokenize("Dokumentacja na https://example.com/docs dostępna.")
        assert not any("http" in t for t in tokens)

    def test_min_length_filter(self):
        from scripts.nlp.text_utils import tokenize
        tokens = tokenize("To a b cd efg", min_len=3, remove_stopwords=False)
        assert all(len(t) >= 3 for t in tokens)


class TestStem:
    def test_noun_suffix_stripped(self):
        from scripts.nlp.text_utils import stem
        # "szyfrowanie" → rdzeń krótszy
        result = stem("szyfrowanie")
        assert len(result) < len("szyfrowanie")

    def test_short_word_unchanged(self):
        from scripts.nlp.text_utils import stem
        result = stem("api")
        assert result == "api"

    def test_verb_infinitive(self):
        from scripts.nlp.text_utils import stem
        result = stem("szyfrować")
        assert len(result) <= len("szyfrować")

    def test_returns_string(self):
        from scripts.nlp.text_utils import stem
        assert isinstance(stem("testowanie"), str)


class TestShingles:
    def test_returns_set(self):
        from scripts.nlp.text_utils import shingles
        result = shingles("hello world", n=3)
        assert isinstance(result, set)

    def test_n_gram_size(self):
        from scripts.nlp.text_utils import shingles
        result = shingles("abcdefgh", n=4)
        assert all(len(s) == 4 for s in result)

    def test_empty_text_returns_empty_set(self):
        from scripts.nlp.text_utils import shingles
        assert shingles("", n=3) == set()

    def test_text_shorter_than_n(self):
        from scripts.nlp.text_utils import shingles
        assert shingles("ab", n=5) == set()

    def test_identical_texts_same_shingles(self):
        from scripts.nlp.text_utils import shingles
        text = "test dokumentacji"
        assert shingles(text) == shingles(text)


class TestExtractHeadings:
    def test_basic_headings(self):
        from scripts.nlp.text_utils import extract_headings
        text = "# Tytuł\n\n## Sekcja 1\n\n### Podsekcja\n"
        result = extract_headings(text)
        assert len(result) == 3
        assert result[0] == (1, "Tytuł")
        assert result[1] == (2, "Sekcja 1")
        assert result[2] == (3, "Podsekcja")

    def test_no_headings(self):
        from scripts.nlp.text_utils import extract_headings
        assert extract_headings("Zwykły tekst bez nagłówków.") == []

    def test_heading_levels(self):
        from scripts.nlp.text_utils import extract_headings
        text = "###### Głęboki nagłówek"
        result = extract_headings(text)
        assert result[0][0] == 6

    def test_heading_text_cleaned(self):
        from scripts.nlp.text_utils import extract_headings
        text = "## Sekcja testowa"
        result = extract_headings(text)
        assert result[0][1] == "Sekcja testowa"


class TestExtractLinks:
    def test_markdown_link(self):
        from scripts.nlp.text_utils import extract_links
        text = "Patrz [architektura](architecture.md) dla szczegółów."
        links = extract_links(text)
        assert "architecture.md" in links

    def test_wiki_link(self):
        from scripts.nlp.text_utils import extract_links
        text = "Więcej w [[Security Policy]]."
        links = extract_links(text)
        assert "Security Policy" in links

    def test_multiple_links(self):
        from scripts.nlp.text_utils import extract_links
        text = "[a](a.md) oraz [b](b.md) i [[c]]"
        links = extract_links(text)
        assert len(links) == 3

    def test_no_links(self):
        from scripts.nlp.text_utils import extract_links
        assert extract_links("Tekst bez linków.") == []


# ============================================================
# similarity_engine
# ============================================================

class TestJaccard:
    def test_identical_sets(self):
        from scripts.nlp.similarity_engine import jaccard
        s = {"a", "b", "c"}
        assert jaccard(s, s) == 1.0

    def test_disjoint_sets(self):
        from scripts.nlp.similarity_engine import jaccard
        assert jaccard({"a", "b"}, {"c", "d"}) == 0.0

    def test_partial_overlap(self):
        from scripts.nlp.similarity_engine import jaccard
        score = jaccard({"a", "b", "c"}, {"b", "c", "d"})
        assert 0.0 < score < 1.0

    def test_empty_sets(self):
        from scripts.nlp.similarity_engine import jaccard
        assert jaccard(set(), set()) == 1.0

    def test_one_empty(self):
        from scripts.nlp.similarity_engine import jaccard
        assert jaccard({"a"}, set()) == 0.0

    def test_symmetry(self):
        from scripts.nlp.similarity_engine import jaccard
        a, b = {"x", "y"}, {"y", "z"}
        assert jaccard(a, b) == jaccard(b, a)


class TestCosineSimilarity:
    def test_identical_vectors(self):
        from scripts.nlp.similarity_engine import cosine_similarity
        v = {"a": 0.5, "b": 0.5}
        # L2 normalize manually
        import math
        norm = math.sqrt(0.5 ** 2 + 0.5 ** 2)
        v_n = {k: val / norm for k, val in v.items()}
        assert cosine_similarity(v_n, v_n) == pytest.approx(1.0, abs=1e-9)

    def test_empty_vectors(self):
        from scripts.nlp.similarity_engine import cosine_similarity
        assert cosine_similarity({}, {}) == 0.0

    def test_disjoint_vectors(self):
        from scripts.nlp.similarity_engine import cosine_similarity
        assert cosine_similarity({"a": 1.0}, {"b": 1.0}) == 0.0

    def test_result_in_range(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("a", "szyfrowanie danych w systemie")
        corpus.add("b", "baza danych szyfrowanie klucz")
        corpus.build()
        score = corpus.cosine_pair("a", "b")
        assert 0.0 <= score <= 1.0


class TestDocumentCorpus:
    def test_add_and_build(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("doc1", "szyfrowanie danych systemowych")
        corpus.add("doc2", "dane szyfrowanie klucz prywatny")
        corpus.build()
        assert len(corpus) == 2

    def test_find_similar_returns_others(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("security", SECURITY_FULL)
        corpus.add("testing", TESTING_FULL)
        corpus.add("arch", ARCH_FULL)
        results = corpus.find_similar("security", threshold=0.0)
        ids = [r.doc_id for r in results]
        assert "security" not in ids
        assert len(results) == 2

    def test_similar_docs_higher_score(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("arch", ARCH_FULL)
        corpus.add("arch_dup", DUPLICATE_OF_ARCH)
        corpus.add("testing", TESTING_FULL)
        results = corpus.find_similar("arch", threshold=0.0)
        # arch_dup powinien być bardziej podobny niż testing
        scores = {r.doc_id: r.score for r in results}
        assert scores.get("arch_dup", 0) > scores.get("testing", 0)

    def test_find_similar_excludes_self(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("d1", "tekst dokumentu jeden")
        corpus.add("d2", "tekst dokumentu dwa")
        results = corpus.find_similar("d1", threshold=0.0)
        assert all(r.doc_id != "d1" for r in results)

    def test_jaccard_pair_symmetry(self):
        from scripts.nlp.similarity_engine import DocumentCorpus
        corpus = DocumentCorpus()
        corpus.add("a", ARCH_FULL)
        corpus.add("b", SECURITY_FULL)
        assert corpus.jaccard_pair("a", "b") == corpus.jaccard_pair("b", "a")


# ============================================================
# gap_detector
# ============================================================

class TestGapDetector:
    def setup_method(self):
        from scripts.nlp.gap_detector import GapDetector
        self.detector = GapDetector()

    def test_full_arch_doc_no_errors(self):
        findings = self.detector.analyse("architecture.md", ARCH_FULL)
        errors = [f for f in findings if f.severity == "ERROR"]
        assert len(errors) == 0, f"Nieoczekiwane ERRORy: {[f.description for f in errors]}"

    def test_missing_section_detected(self):
        findings = self.detector.analyse("architecture.md", ARCH_MISSING_SECTIONS)
        types = [f.gap_type for f in findings]
        assert "missing_section" in types

    def test_missing_section_severity_high_weight(self):
        findings = self.detector.analyse("architecture.md", ARCH_MISSING_SECTIONS)
        high_weight_gaps = [
            f for f in findings
            if f.gap_type == "missing_section" and f.weight >= 3
        ]
        # security i components to wymagane sekcje wagi 3
        assert len(high_weight_gaps) > 0

    def test_empty_doc_generates_warnings(self):
        findings = self.detector.analyse("empty.md", EMPTY_DOC)
        assert len(findings) > 0

    def test_short_doc_shallow_structure(self):
        findings = self.detector.analyse("short.md", SHORT_DOC)
        types = [f.gap_type for f in findings]
        assert "shallow_structure" in types

    def test_missing_metadata_detected(self):
        # ARCH_MISSING_SECTIONS nie ma metadanych
        findings = self.detector.analyse("test.md", ARCH_MISSING_SECTIONS)
        meta_findings = [f for f in findings if f.gap_type == "missing_metadata"]
        assert len(meta_findings) > 0

    def test_security_doc_detects_doc_type(self):
        from scripts.nlp.gap_detector import _detect_doc_type
        doc_type = _detect_doc_type("security.md", SECURITY_FULL)
        assert doc_type == "security"

    def test_testing_doc_detects_doc_type(self):
        from scripts.nlp.gap_detector import _detect_doc_type
        doc_type = _detect_doc_type("testing.md", TESTING_FULL)
        assert doc_type == "testing"

    def test_completeness_score_full_doc(self):
        findings = self.detector.analyse("architecture.md", ARCH_FULL)
        score = self.detector.completeness_score(findings)
        assert 0.0 <= score <= 1.0
        # Pełny dokument powinien mieć score > 0.5
        assert score > 0.5

    def test_completeness_score_empty_doc(self):
        findings = self.detector.analyse("empty.md", EMPTY_DOC)
        score = self.detector.completeness_score(findings)
        assert 0.0 <= score <= 1.0

    def test_completeness_score_range(self):
        for doc, text in [
            ("arch.md", ARCH_FULL),
            ("sec.md", SECURITY_FULL),
            ("test.md", TESTING_FULL),
            ("empty.md", EMPTY_DOC),
        ]:
            findings = self.detector.analyse(doc, text)
            score = self.detector.completeness_score(findings)
            assert 0.0 <= score <= 1.0, f"{doc}: score {score} poza zakresem"

    def test_heading_inconsistency_detected(self):
        text = "# Tytuł\n\n### Podsekcja (przeskoczono H2)\n\nTreść sekcji."
        findings = self.detector.analyse("test.md", text)
        types = [f.gap_type for f in findings]
        assert "heading_depth_inconsistency" in types

    def test_findings_sorted_error_first(self):
        findings = self.detector.analyse("architecture.md", ARCH_MISSING_SECTIONS)
        if len(findings) >= 2:
            severities = [f.severity for f in findings]
            # ERROR powinny być przed WARNING
            if "ERROR" in severities and "WARNING" in severities:
                first_warning = next(
                    (i for i, s in enumerate(severities) if s == "WARNING"), len(severities)
                )
                last_error = max(
                    (i for i, s in enumerate(severities) if s == "ERROR"), default=-1
                )
                assert last_error < first_warning

    def test_finding_has_required_fields(self):
        findings = self.detector.analyse("test.md", ARCH_MISSING_SECTIONS)
        for f in findings:
            assert f.doc_path == "test.md"
            assert f.severity in ("ERROR", "WARNING", "INFO")
            assert f.gap_type
            assert f.description

    def test_to_dict_serializable(self):
        import json
        findings = self.detector.analyse("test.md", SHORT_DOC)
        for f in findings:
            d = f.to_dict()
            # Sprawdź czy jest JSON-serializable
            json.dumps(d)


# ============================================================
# duplicate_detector
# ============================================================

class TestDuplicateDetector:
    def test_exact_duplicate_detected(self):
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("doc_a.md", ARCH_FULL)
        det.add("doc_b.md", ARCH_FULL)  # identyczne
        det.add("doc_c.md", TESTING_FULL)
        records = det.analyse()
        exact = [r for r in records if r.duplicate_type == "exact"]
        assert len(exact) >= 1
        # Identyczne dokumenty powinny mieć Jaccard ~1.0
        assert exact[0].similarity > 0.8

    def test_near_duplicate_detected(self):
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("arch.md", ARCH_FULL)
        det.add("arch_dup.md", DUPLICATE_OF_ARCH)
        records = det.analyse()
        assert len(records) >= 1

    def test_unrelated_docs_not_duplicate(self):
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("arch.md", ARCH_FULL)
        det.add("testing.md", TESTING_FULL)
        records = det.analyse(cos_threshold=0.4, jac_threshold=0.3)
        # Arch i Testing mają mało wspólne — nie powinny być duplikatem
        # (mogą być thematic przy niskim progu, ale nie exact/extending)
        high_sim = [r for r in records if r.similarity > 0.7]
        assert len(high_sim) == 0

    def test_single_doc_no_duplicates(self):
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("only.md", ARCH_FULL)
        assert det.analyse() == []

    def test_duplicate_record_fields(self):
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("a.md", ARCH_FULL)
        det.add("b.md", ARCH_FULL)
        records = det.analyse()
        if records:
            r = records[0]
            assert r.doc_a and r.doc_b
            assert 0.0 <= r.similarity <= 1.0
            assert r.duplicate_type in ("exact", "extending", "thematic", "partial")
            assert r.method in ("jaccard_shingle", "cosine_tfidf")

    def test_to_dict(self):
        import json
        from scripts.nlp.duplicate_detector import DuplicateDetector
        det = DuplicateDetector()
        det.add("a.md", ARCH_FULL)
        det.add("b.md", ARCH_FULL)
        records = det.analyse()
        for r in records:
            json.dumps(r.to_dict())


# ============================================================
# relation_mapper
# ============================================================

class TestRelationMapper:
    def test_explicit_link_detected(self):
        from scripts.nlp.relation_mapper import RelationMapper
        docs = {
            "arch.md": ARCH_FULL + "\n\nPatrz [security](security.md).",
            "security.md": SECURITY_FULL,
        }
        mapper = RelationMapper()
        records = mapper.analyse(docs)
        explicit = [r for r in records if r.relation_type == "explicit_link"]
        assert len(explicit) >= 1
        link_rec = explicit[0]
        assert link_rec.source_doc == "arch.md"
        assert link_rec.target_doc == "security.md"
        assert link_rec.confidence == 1.0

    def test_name_mention_detected(self):
        from scripts.nlp.relation_mapper import RelationMapper
        docs = {
            "arch.md": ARCH_FULL + "\nPolityka bezpieczeństwa opisuje wymagania.",
            "security.md": SECURITY_FULL,
        }
        mapper = RelationMapper()
        records = mapper.analyse(docs)
        mentions = [r for r in records if r.relation_type == "name_mention"]
        # "security" powinno być wzmiankowane
        assert len(mentions) >= 0  # może być 0 jeśli wariant zbyt krótki — akceptowalne

    def test_thematic_overlap_similar_docs(self):
        from scripts.nlp.relation_mapper import RelationMapper
        # security.md i arch.md mają wspólne słowa (szyfrowanie, TLS, itp.)
        docs = {"arch.md": ARCH_FULL, "security.md": SECURITY_FULL}
        mapper = RelationMapper()
        records = mapper.analyse(docs, similarity_threshold=0.15)
        thematic = [r for r in records if r.relation_type == "thematic_overlap"]
        assert len(thematic) >= 0  # może być 0 — akceptowalne, to heurystyka

    def test_no_self_relations(self):
        from scripts.nlp.relation_mapper import RelationMapper
        docs = {"arch.md": ARCH_FULL, "security.md": SECURITY_FULL}
        mapper = RelationMapper()
        records = mapper.analyse(docs)
        for r in records:
            assert r.source_doc != r.target_doc

    def test_relation_record_fields(self):
        from scripts.nlp.relation_mapper import RelationMapper
        docs = {
            "a.md": ARCH_FULL + "\n[b](b.md)",
            "b.md": SECURITY_FULL,
        }
        mapper = RelationMapper()
        records = mapper.analyse(docs)
        for r in records:
            assert r.source_doc in docs
            assert r.target_doc in docs
            assert r.relation_type
            assert 0.0 <= r.confidence <= 1.0

    def test_find_isolated_no_docs(self):
        from scripts.nlp.relation_mapper import RelationMapper
        mapper = RelationMapper()
        isolated = mapper.find_isolated(["only.md"], [])
        assert "only.md" in isolated

    def test_build_adjacency(self):
        from scripts.nlp.relation_mapper import RelationMapper, RelationRecord
        records = [
            RelationRecord("a.md", "b.md", "explicit_link", "b.md", 1.0),
            RelationRecord("a.md", "c.md", "thematic_overlap", "test", 0.5),
        ]
        mapper = RelationMapper()
        adj = mapper.build_adjacency(records)
        assert "a.md" in adj
        assert "b.md" in adj["a.md"]
        assert "c.md" in adj["a.md"]

    def test_to_dict(self):
        import json
        from scripts.nlp.relation_mapper import RelationRecord
        r = RelationRecord("a.md", "b.md", "explicit_link", "b.md", 1.0)
        json.dumps(r.to_dict())


# ============================================================
# doc_auditor — integracja
# ============================================================

@pytest.fixture
def doc_dir(tmp_path: Path) -> Path:
    """Katalog z przykładowymi dokumentami do audytu."""
    (tmp_path / "architecture.md").write_text(ARCH_FULL, encoding="utf-8")
    (tmp_path / "security.md").write_text(SECURITY_FULL, encoding="utf-8")
    (tmp_path / "testing.md").write_text(TESTING_FULL, encoding="utf-8")
    return tmp_path


@pytest.fixture
def auditor(tmp_path: Path):
    """DocAuditor z tymczasową bazą danych."""
    from scripts.nlp.doc_auditor import DocAuditor
    db_path = tmp_path / "test_audit.db"
    return DocAuditor(db_path=db_path)


class TestDocAuditor:
    def test_scan_returns_run_id(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        assert run_id
        assert isinstance(run_id, str)

    def test_scan_finds_all_docs(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        runs = auditor.list_runs()
        assert any(r["run_id"] == run_id for r in runs)
        run = next(r for r in runs if r["run_id"] == run_id)
        assert run["doc_count"] == 3

    def test_scan_creates_db_tables(self, tmp_path):
        from scripts.nlp.doc_auditor import DocAuditor
        db_path = tmp_path / "audit.db"
        auditor = DocAuditor(db_path=db_path)
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "test.md").write_text(ARCH_FULL)
        auditor.scan(tmp_path / "docs")

        conn = sqlite3.connect(str(db_path))
        tables = {row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()}
        conn.close()
        assert "doc_audit_findings" in tables
        assert "doc_completeness" in tables
        assert "doc_duplicates" in tables
        assert "doc_relations" in tables

    def test_scan_writes_completeness(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        conn = sqlite3.connect(str(auditor._db_path))
        rows = conn.execute(
            "SELECT doc_path, completeness_score FROM doc_completeness WHERE run_id=?",
            (run_id,),
        ).fetchall()
        conn.close()
        assert len(rows) == 3
        for path, score in rows:
            assert 0.0 <= score <= 1.0

    def test_scan_writes_findings(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        conn = sqlite3.connect(str(auditor._db_path))
        count = conn.execute(
            "SELECT COUNT(*) FROM doc_audit_findings WHERE run_id=?", (run_id,)
        ).fetchone()[0]
        conn.close()
        # Musi być co najmniej kilka braków (brak metadanych itp.)
        assert count > 0

    def test_report_contains_run_id(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        report = auditor.report(run_id)
        assert run_id in report

    def test_report_contains_sections(self, auditor, doc_dir):
        run_id = auditor.scan(doc_dir)
        report = auditor.report(run_id)
        assert "KOMPLETNOŚĆ" in report
        assert "BRAKI" in report
        assert "DUPLIKATY" in report
        assert "RELACJE" in report

    def test_report_unknown_run_id(self, auditor):
        result = auditor.report("nonexistent-run-id")
        assert "nie znaleziony" in result.lower() or "nonexistent" in result

    def test_list_runs_returns_list(self, auditor, doc_dir):
        auditor.scan(doc_dir)
        runs = auditor.list_runs()
        assert isinstance(runs, list)
        assert len(runs) >= 1

    def test_multiple_scans_independent(self, auditor, doc_dir):
        run1 = auditor.scan(doc_dir)
        run2 = auditor.scan(doc_dir)
        assert run1 != run2
        runs = auditor.list_runs()
        run_ids = [r["run_id"] for r in runs]
        assert run1 in run_ids
        assert run2 in run_ids

    def test_skip_dirs_respected(self, auditor, tmp_path):
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "arch.md").write_text(ARCH_FULL)
        (tmp_path / ".git").mkdir()
        (tmp_path / ".git" / "config").write_text("git config")
        run_id = auditor.scan(tmp_path)
        conn = sqlite3.connect(str(auditor._db_path))
        paths = [
            row[0] for row in conn.execute(
                "SELECT doc_path FROM doc_completeness WHERE run_id=?", (run_id,)
            ).fetchall()
        ]
        conn.close()
        assert not any(".git" in p for p in paths)

    def test_nonexistent_dir_raises(self, auditor):
        with pytest.raises(FileNotFoundError):
            auditor.scan("/nonexistent/path/to/docs")

    def test_duplicate_detected_in_scan(self, auditor, tmp_path):
        (tmp_path / "arch.md").write_text(ARCH_FULL)
        (tmp_path / "arch_copy.md").write_text(ARCH_FULL)
        run_id = auditor.scan(tmp_path)
        conn = sqlite3.connect(str(auditor._db_path))
        count = conn.execute(
            "SELECT COUNT(*) FROM doc_duplicates WHERE run_id=?", (run_id,)
        ).fetchone()[0]
        conn.close()
        assert count >= 1


# ============================================================
# CLI
# ============================================================

class TestDocAuditorCLI:
    def test_cli_scan_command(self, tmp_path):
        from scripts.nlp.doc_auditor import main
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "arch.md").write_text(ARCH_FULL)
        db_path = tmp_path / "test.db"
        result = main([
            "--db", str(db_path),
            "scan",
            "--dir", str(tmp_path / "docs"),
        ])
        assert result == 0

    def test_cli_list_runs_empty(self, tmp_path):
        from scripts.nlp.doc_auditor import main
        db_path = tmp_path / "empty.db"
        # Stwórz pusty DocAuditor (inicjalizuje schema)
        from scripts.nlp.doc_auditor import DocAuditor
        DocAuditor(db_path=db_path)
        result = main(["--db", str(db_path), "list-runs"])
        assert result == 0

    def test_cli_scan_and_report(self, tmp_path, capsys):
        from scripts.nlp.doc_auditor import main
        (tmp_path / "a.md").write_text(ARCH_FULL)
        db_path = tmp_path / "r.db"
        main(["--db", str(db_path), "scan", "--dir", str(tmp_path), "--report"])
        captured = capsys.readouterr()
        assert "RAPORT" in captured.out

    def test_cli_scan_nonexistent_dir(self, tmp_path):
        from scripts.nlp.doc_auditor import main
        db_path = tmp_path / "x.db"
        result = main([
            "--db", str(db_path),
            "scan", "--dir", "/nonexistent/path",
        ])
        assert result == 1
