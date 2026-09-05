#!/usr/bin/env python3
"""Generate concise Markdown notes for DLMF section pages."""

from __future__ import annotations

import html
import re
import socket
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
CACHE = ROOT / ".cache" / "html"
BASE_URL = "https://dlmf.nist.gov"
VERSION_RE = re.compile(r"Version\s+([^;]+);\s*Release date\s+([0-9-]+)")
SECTION_HREF_RE = re.compile(r"^\./(\d+)\.(\d+)$")
CHAPTER_TITLE_CACHE: dict[int, str] = {}


@dataclass(frozen=True)
class SectionPage:
    chapter: int
    section: int
    title: str
    url: str
    file_name: str


def ascii_text(value: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2023": ">",
        "\u2062": "",
        "\u2102": "C",
        "\u2115": "N",
        "\u211d": "R",
        "\u2124": "Z",
        "\u2212": "-",
        "\u221e": "infinity",
        "\u1d62": "i",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value.encode("ascii", "ignore").decode("ascii")


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return ascii_text(value)


def cache_path(path: str) -> Path:
    safe = path.strip("/").replace("/", "__") or "home"
    return CACHE / f"{safe}.html"


def fetch(path: str) -> str:
    target = cache_path(path)
    if target.exists():
        return target.read_text(encoding="utf-8")

    url = f"{BASE_URL}/{path.strip('/')}"
    request = urllib.request.Request(url, headers={"User-Agent": "Codex DLMF documentation crawler"})
    last_error: Exception | None = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", errors="replace")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding="utf-8")
            time.sleep(0.15)
            return body
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last_error = exc
            time.sleep(1)
    raise RuntimeError(f"could not fetch {url}: {last_error}")


def page_title(soup: BeautifulSoup) -> str:
    heading = soup.select_one("h1.ltx_title")
    if heading:
        tag = heading.select_one(".ltx_tag")
        if tag:
            tag.extract()
        return clean_text(heading.get_text(" "))
    if soup.title:
        return clean_text(soup.title.get_text(" "))
    return "Untitled"


def observed_version(soup: BeautifulSoup) -> tuple[str, str]:
    footer = soup.select_one(".ltx_footer_links")
    if footer:
        match = VERSION_RE.search(clean_text(footer.get_text(" ")))
        if match:
            return clean_text(match.group(1)), clean_text(match.group(2))
    return "unknown", "unknown"


def chapter_title(chapter: int) -> str:
    if chapter in CHAPTER_TITLE_CACHE:
        return CHAPTER_TITLE_CACHE[chapter]
    html_text = fetch(str(chapter))
    title = page_title(BeautifulSoup(html_text, "html.parser"))
    CHAPTER_TITLE_CACHE[chapter] = title
    return title


def discover_sections(chapters: Iterable[int]) -> list[SectionPage]:
    discovered: list[SectionPage] = []
    seen: set[tuple[int, int]] = set()
    for chapter in chapters:
        soup = BeautifulSoup(fetch(str(chapter)), "html.parser")
        for link in soup.find_all("link", rel=lambda rel: rel and "section" in rel):
            href = link.get("href", "")
            match = SECTION_HREF_RE.match(href)
            if not match:
                continue
            chapter_num, section_num = int(match.group(1)), int(match.group(2))
            key = (chapter_num, section_num)
            if key in seen:
                continue
            seen.add(key)
            raw_title = link.get("title", "")
            title = clean_text(re.sub(r"^.+?\s", "", raw_title.split(" \u2038 ")[0], count=1))
            if not title:
                title = f"Section {chapter_num}.{section_num}"
            discovered.append(
                SectionPage(
                    chapter=chapter_num,
                    section=section_num,
                    title=title,
                    url=f"{BASE_URL}/{chapter_num}.{section_num}",
                    file_name=f"section-{chapter_num:02d}-{section_num:02d}.md",
                )
            )
    return sorted(discovered, key=lambda item: (item.chapter, item.section))


def collect_contents(soup: BeautifulSoup) -> list[str]:
    items: list[str] = []
    for entry in soup.select("ol.ltx_toclist_section li.ltx_tocentry"):
        text = clean_text(entry.get_text(" "))
        text = re.sub(r"^§?\d+\.\d+\([^)]+\)\s*", "", text)
        if text and text not in items:
            items.append(text)
    return items


def collect_keywords(soup: BeautifulSoup) -> list[str]:
    keywords: list[str] = []
    for node in soup.select("a.ltx_keyword"):
        text = clean_text(node.get_text(" "))
        if text and text not in keywords:
            keywords.append(text)
    meta = soup.find("meta", attrs={"name": "keywords"})
    if meta and meta.get("content"):
        for item in meta["content"].split(","):
            text = clean_text(item)
            if text and text not in keywords:
                keywords.append(text)
    return keywords[:18]


def collect_notes(soup: BeautifulSoup) -> list[str]:
    notes: list[str] = []
    for dt in soup.select("dt"):
        if clean_text(dt.get_text(" ")).rstrip(":") != "Notes":
            continue
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        text = clean_text(dd.get_text(" "))
        if text and text not in notes:
            notes.append(text)
    return notes[:5]


def count_unique(selector: str, soup: BeautifulSoup, attr: str = "id") -> int:
    values = {node.get(attr) for node in soup.select(selector) if node.get(attr)}
    return len(values)


def write_section(page: SectionPage) -> tuple[str, str]:
    soup = BeautifulSoup(fetch(f"{page.chapter}.{page.section}"), "html.parser")
    title = page_title(soup)
    version, release_date = observed_version(soup)
    contents = collect_contents(soup)
    keywords = collect_keywords(soup)
    notes = collect_notes(soup)
    equations = count_unique(".ltx_equation, .ltx_equationgroup", soup)
    tables = count_unique("table.ltx_tabular", soup)
    figures = count_unique("figure.ltx_figure", soup)
    chapter = chapter_title(page.chapter)

    lines = [
        f"# §{page.chapter}.{page.section} {title}",
        "",
        f"Source: [{page.url}]({page.url})",
        "",
        f"Observed version: {version}, release date {release_date}.",
        "",
        "## Purpose",
        "",
        f"Documents the `{page.chapter}.{page.section}` section of Chapter {page.chapter}, {chapter}. The page focuses on {title}.",
        "",
        "## Page Structure",
        "",
    ]
    if contents:
        lines.extend(f"- {item}." for item in contents)
    else:
        lines.append("- No subsection-level contents list was exposed on the page.")

    lines.extend(["", "## Signals", ""])
    if keywords:
        lines.append(f"- Keywords: {', '.join(keywords)}.")
    else:
        lines.append("- Keywords: none listed in the page metadata.")
    lines.append(f"- Formula blocks detected: {equations}.")
    lines.append(f"- Tables detected: {tables}.")
    lines.append(f"- Figures detected: {figures}.")

    if notes:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {note}" for note in notes)

    lines.append("")
    target = PAGES / page.file_name
    target.write_text("\n".join(lines), encoding="utf-8")
    return title, version


def replace_progress_table(index: str, generated_count: int) -> str:
    row = f"| 6 | Chapter section pages 1-36 | Complete | {generated_count} |"
    patterns = [
        r"\| 6\+ \| Chapter sections, one DLMF section page per Markdown file \| In progress \| \d+ \|",
        r"\| 6 \| Chapter section pages 1-36 \| Complete \| \d+ \|",
    ]
    for pattern in patterns:
        index, replaced = re.subn(pattern, row, index, count=1)
        if replaced:
            return index
    return index


def append_missing_index_rows(index: str, pages: list[SectionPage], titles: dict[str, str]) -> str:
    rows = []
    for page in pages:
        needle = f"[§{page.chapter}.{page.section}]({page.url})"
        if needle in index:
            continue
        title = titles.get(page.file_name, page.title)
        rows.append(
            f"| Done | [§{page.chapter}.{page.section}]({page.url}) | "
            f"[pages/{page.file_name}](pages/{page.file_name}) | {title}. |"
        )
    if not rows:
        return index
    marker = "\n## Discovered Top-Level Queue"
    insert = "\n".join(rows) + "\n"
    return index.replace(marker, insert + marker)


def main() -> None:
    PAGES.mkdir(parents=True, exist_ok=True)
    sections = discover_sections(range(2, 37))
    titles: dict[str, str] = {}
    for page in sections:
        title, _version = write_section(page)
        titles[page.file_name] = title

    index_path = ROOT / "index.md"
    index = index_path.read_text(encoding="utf-8")
    total_sections = 18 + len(sections)
    index = replace_progress_table(index, total_sections)
    index = append_missing_index_rows(index, sections, titles)
    index_path.write_text(index, encoding="utf-8")
    print(f"Generated {len(sections)} section files; total section pages now {total_sections}.")


if __name__ == "__main__":
    main()
