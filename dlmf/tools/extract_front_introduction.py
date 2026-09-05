#!/usr/bin/env python3
"""Extract the DLMF Mathematical Introduction into an Obsidian-oriented note."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".cache" / "html" / "front__introduction.html"
TARGET = ROOT / "pages" / "front-introduction.md"
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


def obsidian_math(value: str) -> str:
    return re.sub(r"`([^`]+)`", r"$\1$", value)


def table_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def text_with_math(node: Tag, *, math_mode: str = "obsidian") -> str:
    clone = BeautifulSoup(str(node), "html.parser")
    for math in clone.select("math"):
        alt = clean(math.get("alttext", ""))
        if math_mode == "code":
            replacement = f"`{alt}`" if alt else ""
        else:
            replacement = f"${alt}$" if alt else ""
        math.replace_with(replacement)
    return clean(clone.get_text(" "))


def title(soup: BeautifulSoup) -> str:
    heading = soup.select_one("h1.ltx_title")
    return clean(heading.get_text(" ")) if heading else "Mathematical Introduction"


def version(soup: BeautifulSoup) -> tuple[str, str]:
    footer = soup.select_one(".ltx_footer_links")
    if footer:
        match = VERSION_RE.search(clean(footer.get_text(" ")))
        if match:
            return clean(match.group(1)), clean(match.group(2))
    return "unknown", "unknown"


def sections(soup: BeautifulSoup) -> list[tuple[str, list[str]]]:
    result = []
    for heading in soup.select("h2.ltx_title_section"):
        section_title = clean(heading.get_text(" "))
        paras: list[str] = []
        for sibling in heading.find_next_siblings():
            if isinstance(sibling, Tag) and sibling.name == "h2":
                break
            if not isinstance(sibling, Tag):
                continue
            for para in sibling.select("p.ltx_p"):
                text = text_with_math(para)
                if text and text not in paras:
                    paras.append(text)
        result.append((section_title, paras))
    return result


def first_sentence(text: str) -> str:
    match = re.search(r"(.+?[.!?])(?:\s|$)", text)
    return match.group(1) if match else text


def summarize_section(section_title: str, paras: list[str]) -> str:
    joined = " ".join(paras)
    if section_title == "Organization and Objective":
        return "DLMF is positioned as a modern reference for special functions, with Chapters 1-3 supplying algebraic, analytic, asymptotic, and numerical foundations."
    if section_title == "Methodology":
        return "The page explains that DLMF chapters combine definitions, identities, approximations, graphics, applications, computation, and validation notes, with references and cross-links supporting the formulas."
    if section_title == "Notation for the Special Functions":
        return "Special-function notation is chapter-local: each relevant chapter begins with a notation section identifying adopted notations and important alternatives."
    if section_title == "Common Notations and Definitions":
        return "The introduction centralizes common symbols, set notation, operators, constants, and definitions used across the DLMF."
    if section_title == "Graphics":
        return "Graphics are part of the reference layer and are designed to support interpretation of formulas and function behavior."
    if section_title == "Applications":
        return "Application notes identify where the special functions arise in scientific and engineering contexts."
    if section_title == "Computation":
        return "Computation notes point readers toward methods, software, tables, and numerical evaluation concerns."
    if section_title == "Verification":
        return "Verification is treated as a mathematical reliability practice: formulas and results are checked by multiple methods where possible."
    if section_title == "Special Acknowledgment":
        return "The page closes with acknowledgment of major contributors to the DLMF project."
    return first_sentence(joined) if joined else "No prose summary extracted."


def table_rows(table: Tag) -> list[list[str]]:
    rows: list[list[str]] = []
    for row in table.select("tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if cells:
            rows.append([text_with_math(cell) for cell in cells])
    return rows


def common_tables(soup: BeautifulSoup) -> list[tuple[str, list[list[str]]]]:
    result = []
    common = soup.find(id="common")
    if not common:
        return result
    for index, table in enumerate(common.find_all("table", class_="ltx_tabular"), start=1):
        result.append((f"Common notation table {index}", table_rows(table)))
    return result


def special_notation_links(soup: BeautifulSoup) -> list[tuple[str, str, str]]:
    notations = soup.find(id="notations")
    if not notations:
        return []
    links = []
    for link in notations.select("a[href]"):
        label = clean(link.get_text(" "))
        href = urljoin(BASE_URL, link["href"].replace(".././", "").replace("./", ""))
        title_attr = clean(link.get("title", ""))
        if re.match(r"§?\d", label):
            links.append((label, href, title_attr))
    return links


def math_items(soup: BeautifulSoup) -> list[tuple[str, str, str]]:
    items = []
    seen = set()
    for math in soup.select("section math"):
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
    for link in soup.select("section a[href]"):
        label = clean(link.get_text(" "))
        href = urljoin(BASE_URL, link["href"].replace(".././", "").replace("./", ""))
        title_attr = clean(link.get("title", ""))
        key = (label, href, title_attr)
        if label and key not in seen:
            seen.add(key)
            links.append(key)
    return links


def render_common_table(name: str, rows: list[list[str]]) -> list[str]:
    width = max((len(row) for row in rows), default=0)
    if width == 0:
        return []
    headers = ["Notation", "Meaning"] + [f"Detail {i}" for i in range(3, width + 1)]
    lines = [f"#### {name}", "", "| " + " | ".join(headers[:width]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    for row in rows:
        padded = row + [""] * (width - len(row))
        lines.append("| " + " | ".join(table_cell(item) for item in padded) + " |")
    lines.append("")
    return lines


def render() -> str:
    soup = BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")
    page_version, release = version(soup)
    section_data = sections(soup)
    notation_links = special_notation_links(soup)
    tables = common_tables(soup)
    math = math_items(soup)
    links = related_links(soup)

    lines = [
        f"# {title(soup)}",
        "",
        "## Mathematical and Reference Content",
        "",
        "This introduction explains how to read the DLMF as a mathematical reference: what the chapters are for, how notation is assigned, how common symbols are defined, and how graphics, computation, applications, and verification support the formulas.",
        "",
        "### Reading Map",
        "",
    ]
    for section_title, paras in section_data:
        lines.append(f"- **{section_title}**: {summarize_section(section_title, paras)}")

    lines.extend(["", "### DLMF Notation Policy", ""])
    lines.extend(
        [
            "- Special-function notation is not assumed globally; relevant chapters declare their adopted notation in chapter notation sections.",
            "- Alternative notations are important because DLMF is meant to bridge mathematical, physics, engineering, and computational literature.",
            "- Common notation and definitions are centralized in the introduction and the DLMF Notations index.",
        ]
    )

    if notation_links:
        lines.extend(["", "### Special-Notation Sections Referenced", "", "| Section | URL | Source title |", "|---|---|---|"])
        for label, href, title_attr in notation_links:
            lines.append(f"| {label} | {href} | {table_cell(title_attr or '-')} |")

    if tables:
        lines.extend(["", "### Common Notations and Definitions", ""])
        for name, rows in tables:
            lines.extend(render_common_table(name, rows))

    lines.extend(
        [
            "## Rendering and Source Details",
            "",
            "### Source",
            "",
            "- Source: [https://dlmf.nist.gov/front/introduction](https://dlmf.nist.gov/front/introduction)",
            f"- Observed version: {page_version}, release date {release}.",
            "",
            "### Source Section Inventory",
            "",
            "| Section | Extracted paragraph count |",
            "|---|---:|",
        ]
    )
    for section_title, paras in section_data:
        lines.append(f"| {section_title} | {len(paras)} |")

    lines.extend(
        [
            "",
            "### Math Rendering Details",
            "",
            "| Obsidian inline math | TeX alt text | DLMF display | Semantic titles |",
            "|---|---|---|---|",
        ]
    )
    for alt, display, titles in math:
        lines.append(f"| {table_cell(f'${alt}$')} | `{table_cell(alt)}` | {display or '-'} | {table_cell(titles or '-')} |")

    lines.extend(["", "### Related Links", "", "| Label | URL | Source title |", "|---|---|---|"])
    for label, href, title_attr in links:
        lines.append(f"| {table_cell(label)} | {href} | {table_cell(title_attr or '-')} |")

    lines.extend(
        [
            "",
            "## Retrieval Coverage",
            "",
            f"- Major sections extracted: {len(section_data)}.",
            f"- Common notation tables extracted: {len(tables)}.",
            f"- Unique math elements extracted: {len(math)}.",
            f"- Related links extracted: {len(links)}.",
            "- The top section is written for Obsidian reading; rendering/source diagnostics are separated below.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    TARGET.write_text(render(), encoding="utf-8")
    print(f"Wrote processed Mathematical Introduction to {TARGET}")


if __name__ == "__main__":
    main()
