#!/usr/bin/env python3
"""Build GSD todo files for the DLMF deep-documentation project."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
INDEX = ROOT / "index.md"
TODOS = WORKSPACE / ".planning" / "todos"
CHAPTER_ROW_RE = re.compile(r"\| Done \| \[Chapter (\d+)\]\((https://dlmf\.nist\.gov/\d+)\) \| \[pages/(chapter-\d+\.md)\]\(pages/[^)]+\) \| ([^|]+) \|")
SECTION_ROW_RE = re.compile(r"\| Done \| \[§(\d+)\.(\d+)\]\((https://dlmf\.nist\.gov/\d+\.\d+)\) \| \[pages/(section-\d+-\d+\.md)\]\(pages/[^)]+\) \| ([^|]+) \|")


def parse_index() -> tuple[dict[int, tuple[str, str, str]], dict[int, list[tuple[int, str, str, str]]]]:
    text = INDEX.read_text(encoding="utf-8")
    chapters: dict[int, tuple[str, str, str]] = {}
    sections: dict[int, list[tuple[int, str, str, str]]] = defaultdict(list)

    for match in CHAPTER_ROW_RE.finditer(text):
        chapter = int(match.group(1))
        url = match.group(2)
        file_name = match.group(3)
        title = match.group(4).strip().rstrip(".")
        chapters[chapter] = (title, url, file_name)

    for match in SECTION_ROW_RE.finditer(text):
        chapter = int(match.group(1))
        section = int(match.group(2))
        url = match.group(3)
        file_name = match.group(4)
        title = match.group(5).strip().rstrip(".")
        sections[chapter].append((section, title, url, file_name))

    for chapter in sections:
        sections[chapter].sort(key=lambda item: item[0])
    return chapters, sections


def checkbox(done: bool) -> str:
    return "x" if done else " "


def is_deepened(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if "## Mathematical Content" in text and (
        "## Source and Review Notes" in text or "## Rendering and Source Details" in text
    ):
        return True
    return "Deep documentation for DLMF" in text


def chapter_done_marker(chapter: int) -> bool:
    chapter_file = ROOT / "pages" / f"chapter-{chapter:02d}.md"
    section_files = sorted((ROOT / "pages").glob(f"section-{chapter:02d}-*.md"))
    return is_deepened(chapter_file) and bool(section_files) and all(is_deepened(path) for path in section_files)


def write_chapter_todo(chapter: int, title: str, url: str, file_name: str, section_rows: list[tuple[int, str, str, str]]) -> None:
    done = chapter_done_marker(chapter)
    lines = [
        f"# Chapter {chapter}: {title}",
        "",
        f"Source: [{url}]({url})",
        f"Local chapter file: [dlmf/pages/{file_name}](../../dlmf/pages/{file_name})",
        "",
        "## Chapter Todo",
        "",
        f"- [{checkbox(done)}] Deepen chapter overview page with mathematical narrative and page structure.",
        f"- [{checkbox(done)}] Preserve formulas as TeX-style code blocks where available from DLMF math metadata.",
        f"- [{checkbox(done)}] Reflect definitions, symbols, notes, and local dependencies without copying large source passages.",
        f"- [{checkbox(done)}] Verify one-page-one-md-file rule remains intact.",
        "",
        "## Section Todos",
        "",
    ]
    for section, section_title, section_url, section_file in section_rows:
        lines.append(
            f"- [{checkbox(done)}] §{chapter}.{section} [{section_title}]({section_url}) -> "
            f"[dlmf/pages/{section_file}](../../dlmf/pages/{section_file})"
        )
    lines.extend(
        [
            "",
            "## Completion Definition",
            "",
            "- Page contains a useful mathematical narrative.",
            "- Page records formula blocks, definitions, symbols, and source notes when present.",
            "- Page remains source-linked and cites the observed DLMF version.",
            "- Chapter todo is checked only after all listed section todos are complete.",
            "",
        ]
    )
    (TODOS / f"chapter-{chapter:02d}.md").write_text("\n".join(lines), encoding="utf-8")


def write_master_todo(chapters: dict[int, tuple[str, str, str]], sections: dict[int, list[tuple[int, str, str, str]]]) -> None:
    total_sections = sum(len(value) for value in sections.values())
    done_chapters = sum(1 for chapter in chapters if chapter_done_marker(chapter))
    lines = [
        "# DLMF Deep Documentation Todo",
        "",
        "Tracks the second pass over DLMF: each page gets content-level notes with mathematical formulas and definitions reflected.",
        "",
        "## Progress",
        "",
        f"- Chapters discovered: {len(chapters)}",
        f"- Section pages discovered: {total_sections}",
        f"- Deepened chapters: {done_chapters}",
        "",
        "## Chapter Todos",
        "",
    ]
    for chapter in sorted(chapters):
        title, _url, _file_name = chapters[chapter]
        count = len(sections.get(chapter, []))
        done = chapter_done_marker(chapter)
        lines.append(f"- [{checkbox(done)}] Chapter {chapter}: {title} ({count} section pages) -> [chapter-{chapter:02d}.md](chapter-{chapter:02d}.md)")
    lines.append("")
    (TODOS / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    TODOS.mkdir(parents=True, exist_ok=True)
    chapters, sections = parse_index()
    for chapter in sorted(chapters):
        title, url, file_name = chapters[chapter]
        write_chapter_todo(chapter, title, url, file_name, sections.get(chapter, []))
    write_master_todo(chapters, sections)
    print(f"Wrote {len(chapters)} chapter todo files and master todo.")


if __name__ == "__main__":
    main()
