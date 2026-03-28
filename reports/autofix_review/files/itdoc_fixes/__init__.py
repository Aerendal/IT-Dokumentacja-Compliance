"""
itdoc.fixes — autofix engine for structural Markdown template violations.

Public API (V1):
    parse(path)                    -> MarkdownDoc
    analyze(doc)                   -> list[Finding]
    build_plan(root, mode)         -> FixPlan
    apply_plan(plan, ...)          -> ApplyResult
    safe_write(path, content, dir) -> WriteResult
"""
from itdoc.fixes.markdown_model import MarkdownDoc, Section, parse, section_headings
from itdoc.fixes.io_safe import WriteResult, safe_write

__all__ = [
    "MarkdownDoc",
    "Section",
    "parse",
    "section_headings",
    "WriteResult",
    "safe_write",
]
