"""scripts.nlp — Moduł audytu dokumentacji projektowej NLP.

Publiczne API:
    from scripts.nlp.doc_auditor import DocAuditor
    from scripts.nlp.similarity_engine import cosine_similarity, jaccard
    from scripts.nlp.gap_detector import GapDetector
    from scripts.nlp.duplicate_detector import DuplicateDetector
    from scripts.nlp.relation_mapper import RelationMapper
"""
from scripts.nlp.doc_auditor import DocAuditor
from scripts.nlp.gap_detector import GapDetector
from scripts.nlp.duplicate_detector import DuplicateDetector
from scripts.nlp.relation_mapper import RelationMapper
from scripts.nlp.similarity_engine import cosine_similarity, jaccard

__all__ = [
    "DocAuditor",
    "GapDetector",
    "DuplicateDetector",
    "RelationMapper",
    "cosine_similarity",
    "jaccard",
]
