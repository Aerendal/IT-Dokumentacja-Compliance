#!/usr/bin/env python3
"""
Fail the build if any emoji-like characters are present in text files.

Usage:
  python scripts/check_no_emoji.py [root_dir]

Exits with code 1 when at least one emoji is found; prints offending files.
Scans common text extensions; skips binary/undecodable files.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

TEXT_EXTS = {
    ".md",
    ".markdown",
    ".txt",
    ".json",
    ".jsonl",
    ".yaml",
    ".yml",
    ".csv",
    ".tsv",
    ".sql",
}

# Unicode blocks that commonly contain emoji or emoji-like pictographs.
EMOJI_RANGES = [
    (0x1F300, 0x1F6FF),
    (0x1F700, 0x1F77F),
    (0x1F780, 0x1F7FF),
    (0x1F800, 0x1F8FF),
    (0x1F900, 0x1F9FF),
    (0x1FA00, 0x1FA6F),
    (0x1FA70, 0x1FAFF),
    (0x1FB00, 0x1FBFF),
    (0x1F1E6, 0x1F1FF),  # regional indicator (flags)
    (0x2600, 0x26FF),  # misc symbols
    (0x2700, 0x27BF),  # dingbats
    (0x2300, 0x23FF),  # misc technical (clocks, etc.)
    (0x1F000, 0x1F02F),  # mahjong/domino
    (0x1F0A0, 0x1F0FF),  # playing cards
    (0xFE00, 0xFE0F),  # variation selectors
]


def is_emoji_char(ch: str) -> bool:
    cp = ord(ch)
    for start, end in EMOJI_RANGES:
        if start <= cp <= end:
            return True
    return False


SKIP_DIRS = {"reports/runs", ".git", "__pycache__", ".pytest_cache"}


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        # Skip generated pipeline run artifacts
        rel = str(path.relative_to(root) if root != Path(".") else path)
        if any(skip in rel for skip in SKIP_DIRS):
            continue
        if path.suffix.lower() not in TEXT_EXTS:
            continue
        yield path


def scan_file(path: Path) -> list[tuple[int, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    hits: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if any(is_emoji_char(ch) for ch in line):
            hits.append((lineno, line))
    return hits


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    problems = []
    for path in iter_text_files(root):
        lines = scan_file(path)
        if lines:
            problems.append((path, lines))

    if not problems:
        print("No emoji found.")
        return 0

    print("Emoji detected:")
    for path, lines in problems:
        for lineno, line in lines:
            print(f"{path}:{lineno}: {line}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
