#!/usr/bin/env python3
"""Extract a DLMF notation section into a detailed Markdown page."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".cache" / "html" / "1.1.html"
TARGET = ROOT / "pages" / "section-01-01.md"
BASE_URL = "https://dlmf.nist.gov/"
VERSION_RE = re.compile(r"Version\s+([^;]+);\s*Release date\s+([0-9-]+)")


def ascii_text(value: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "\u2038": ">",
        "\u2062": "",
        "\u2102": "C",
        "\u2115": "N",
        "\u211d": "R",
        "\u2124": "Z",
        "\u2212": "-",
        "\u221e": "infinity",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value.encode("ascii", "ignore").decode("ascii")


def clean(value: str) -> str:
    return ascii_text(re.sub(r"\s+", " ", html.unescape(value)).strip())


def text_with_math(node: Tag) -> str:
    clone = BeautifulSoup(str(node), "html.parser")
    for math in clone.select("math"):
        alt = clean(math.get("alttext", ""))
        math.replace_with(f"`{alt}`" if alt else "")
    return clean(clone.get_text(" "))


def obsidian_math(value: str) -> str:
    """Convert extracted TeX code spans into Obsidian inline math."""
    return re.sub(r"`([^`]+)`", r"$\1$", value)


def table_cell(value: str) -> str:
    return value.replace("|", r"\|")


def title(soup: BeautifulSoup) -> str:
    heading = soup.select_one("h1.ltx_title")
    if not heading:
        return "Special Notation"
    tag = heading.select_one(".ltx_tag")
    if tag:
        tag.extract()
    return clean(heading.get_text(" "))


def version(soup: BeautifulSoup) -> tuple[str, str]:
    footer = soup.select_one(".ltx_footer_links")
    if footer:
        match = VERSION_RE.search(clean(footer.get_text(" ")))
        if match:
            return clean(match.group(1)), clean(match.group(2))
    return "unknown", "unknown"


def metadata(soup: BeautifulSoup) -> list[tuple[str, str]]:
    rows = []
    info = soup.select_one("#info dl")
    if not info:
        return rows
    for dt in info.select("dt"):
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        rows.append((clean(dt.get_text(" ")).rstrip(":"), text_with_math(dd)))
    return rows


def notation_rows(soup: BeautifulSoup) -> list[tuple[str, str, str, str]]:
    rows = []
    for row in soup.select("table.ltx_tabular tr.ltx_tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if len(cells) < 2:
            continue
        symbol_cell, meaning_cell = cells[0], cells[1]
        symbol = text_with_math(symbol_cell)
        meaning = text_with_math(meaning_cell)
        math_titles = []
        for math in symbol_cell.select("math"):
            alt = clean(math.get("alttext", ""))
            titles = sorted({clean(node.get("title", "")) for node in math.select("[title]") if node.get("title")})
            if alt and titles:
                math_titles.append(f"`{alt}`: {', '.join(titles)}")
        refs = []
        for link in meaning_cell.select("a[href]"):
            href = urljoin(BASE_URL, link["href"].replace("./", ""))
            label = clean(link.get_text(" "))
            title_attr = clean(link.get("title", ""))
            if label:
                refs.append(f"[{label}]({href})" + (f" - {title_attr}" if title_attr else ""))
        rows.append((symbol, meaning, "; ".join(math_titles), "; ".join(refs)))
    return rows


def all_math_items(soup: BeautifulSoup) -> list[tuple[str, str, str]]:
    items = []
    seen = set()
    for math in soup.select("section.ltx_section math"):
        alt = clean(math.get("alttext", ""))
        display = clean(math.get("display", ""))
        titles = sorted({clean(node.get("title", "")) for node in math.select("[title]") if node.get("title")})
        key = (alt, display, tuple(titles))
        if alt and key not in seen:
            seen.add(key)
            items.append((alt, display, ", ".join(titles)))
    return items


def related_links(soup: BeautifulSoup) -> list[tuple[str, str, str]]:
    links = []
    seen = set()
    content = soup.select_one("section.ltx_section")
    if not content:
        return links
    for link in content.select("a[href]"):
        label = clean(link.get_text(" "))
        href = urljoin(BASE_URL, link["href"].replace("./", ""))
        title_attr = clean(link.get("title", ""))
        key = (label, href, title_attr)
        if label and key not in seen:
            seen.add(key)
            links.append(key)
    return links


def render() -> str:
    soup = BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")
    page_version, release = version(soup)
    rows = notation_rows(soup)
    math_items = all_math_items(soup)
    links = related_links(soup)

    lines = [
        f"# §1.1 {title(soup)}",
        "",
        "## Mathematical Content",
        "",
        "This section defines the default meanings of variables, integer indices, scalar products, vector and matrix operations, adjoints, traces, and operator notation used throughout Chapter 1.",
        "",
        "### Mathematical Narrative",
        "",
        "- For notation outside this local Chapter 1 convention table, DLMF points to its global notation section for special functions.",
        "- Variables and indices are scoped by mathematical role: real variables, complex variables, integers, nonnegative integers, vectors, matrices, distributions, and linear operators.",
        "- Matrix notation distinguishes inverse, identity, determinant, trace, exponential trace, adjoint, complex conjugate, transpose, and Hermitian conjugate.",
        "- The source notes that physics, applied mathematics, and engineering literature often write complex conjugation with a star and Hermitian conjugation with a dagger.",
        "",
        "### Notation Table",
        "",
        "| Symbol | Mathematical Meaning |",
        "|---|---|",
    ]
    for symbol, meaning, _titles, _refs in rows:
        lines.append(f"| {table_cell(obsidian_math(symbol))} | {table_cell(obsidian_math(meaning))} |")

    lines.extend(
        [
            "",
            "## Rendering and Source Details",
            "",
            "### Source",
            "",
            "- Source: [https://dlmf.nist.gov/1.1](https://dlmf.nist.gov/1.1)",
            f"- Observed version: {page_version}, release date {release}.",
            "",
            "### Source Metadata",
            "",
        ]
    )
    for label, value in metadata(soup):
        lines.append(f"- {label}: {value}")

    lines.extend(
        [
            "",
            "### Notation Rendering Details",
            "",
            "This table separates DLMF's HTML/math metadata from the mathematical meaning above. `Obsidian inline math` is the Markdown rendering form to use in notes; `DLMF display` is the source page's HTML display mode.",
            "",
            "| Obsidian inline math | TeX alt text | DLMF display | Semantic titles |",
            "|---|---|---|---|",
        ]
    )
    for alt, display, titles in math_items:
        lines.append(f"| {table_cell(f'${alt}$')} | `{table_cell(alt)}` | {display or '-'} | {table_cell(titles or '-')} |")

    lines.extend(
        [
            "",
            "### Semantic Titles and Cross References",
            "",
            "| Symbol | Encoded semantic titles | Cross references in meaning |",
            "|---|---|---|",
        ]
    )
    for symbol, _meaning, titles, refs in rows:
        lines.append(f"| {table_cell(obsidian_math(symbol))} | {table_cell(obsidian_math(titles or '-'))} | {table_cell(refs or '-')} |")

    lines.extend(
        [
            "",
            "### Related Links",
            "",
            "| Label | URL | Source title |",
            "|---|---|---|",
        ]
    )
    for label, href, title_attr in links:
        lines.append(f"| {label} | {href} | {title_attr or '-'} |")

    lines.extend(
        [
            "",
            "## Retrieval Coverage",
            "",
            f"- Notation rows extracted: {len(rows)}.",
            f"- Unique math elements extracted: {len(math_items)}.",
            f"- Related links extracted: {len(links)}.",
            "- Prose was summarized rather than mirrored verbatim; mathematical symbols, meanings, semantic titles, and links were extracted structurally.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    TARGET.write_text(render(), encoding="utf-8")
    print(f"Wrote detailed §1.1 retrieval to {TARGET}")


if __name__ == "__main__":
    main()
