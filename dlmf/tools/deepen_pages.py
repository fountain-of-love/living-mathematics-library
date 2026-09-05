#!/usr/bin/env python3
"""Create deeper math-aware Markdown notes from cached DLMF HTML pages."""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup, Tag


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "html"
PAGES = ROOT / "pages"
VERSION_RE = re.compile(r"Version\s+([^;]+);\s*Release date\s+([0-9-]+)")


@dataclass(frozen=True)
class PageId:
    chapter: int
    section: int | None = None

    @property
    def dotted(self) -> str:
        if self.section is None:
            return str(self.chapter)
        return f"{self.chapter}.{self.section}"

    @property
    def filename(self) -> str:
        if self.section is None:
            return f"chapter-{self.chapter:02d}.md"
        return f"section-{self.chapter:02d}-{self.section:02d}.md"


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


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return ascii_text(value)


def clean_latex(value: str) -> str:
    value = clean_text(value)
    value = re.sub(r"%\s*", "", value)
    value = unwrap_nvar(value)
    value = unwrap_two_arg_macro(value, r"\ifrac", r"\frac")
    value = remove_one_arg_macro(value, r"\cfracstyle")
    value = unwrap_two_arg_macro(value, r"\raisebox", "")
    value = unwrap_one_arg_macro(value, r"\textit", r"\text")
    value = unwrap_one_arg_macro(value, r"\mbox", r"\text")
    value = rewrite_text_macros(value)
    value = value.replace(r"\pvint", r"\operatorname{PV}\!\int")
    value = value.replace(r"\Residue", r"\operatorname{res}")
    value = value.replace(r"\*", r"\,")
    value = re.sub(r"\\(?:m(?:skip|kern))\s*-?\d+(?:\.\d+)?mu", "", value)
    value = re.sub(r"(?:\\;){2,}", r"\\quad", value)
    value = re.sub(r"\\rm\s+([A-Za-z]+)", r"\\mathrm{\1}", value)
    value = re.sub(r"(?<!\\)\\ ", r"\\,", value)
    value = re.sub(r",\\,", ",", value)
    value = re.sub(r"\\,([),.])", r"\1", value)
    value = re.sub(r"\\(in|setminus)\\,", r"\\\1 ", value)
    return value


def find_balanced_group(value: str, start: int) -> tuple[int, int, str] | None:
    while start < len(value) and value[start].isspace():
        start += 1
    if start >= len(value) or value[start] != "{":
        return None
    depth = 1
    pos = start + 1
    while pos < len(value) and depth:
        if value[pos] == "{":
            depth += 1
        elif value[pos] == "}":
            depth -= 1
        pos += 1
    if depth:
        return None
    return start, pos, value[start + 1 : pos - 1]


def unwrap_one_arg_macro(value: str, macro: str, replacement: str) -> str:
    while macro in value:
        start = value.find(macro)
        group = find_balanced_group(value, start + len(macro))
        if not group:
            break
        group_start, group_end, content = group
        content = re.sub(r"\s+", " ", content.replace("$", " ")).strip()
        if replacement:
            rendered = f"{replacement}{{{content}}}"
        else:
            rendered = content
        value = value[:start] + rendered + value[group_end:]
    return value


def rewrite_text_macros(value: str) -> str:
    while r"\text{" in value:
        start = value.find(r"\text{")
        group = find_balanced_group(value, start + len(r"\text"))
        if not group:
            break
        _, group_end, content = group
        value = value[:start] + text_content_as_math(content) + value[group_end:]
    return value


def text_content_as_math(content: str) -> str:
    content = re.sub(r"\s+", " ", content.replace("$", " ")).strip()
    if content in {"(A)", "(B)", "(C,1)", r"(C,\alpha)", "(<0)"}:
        return content

    words = {
        "and",
        "at",
        "if",
        "locations",
        "of",
        "or",
        "otherwise",
        "poles",
        "residues",
        "sum",
        "the",
        "within",
        "zeros",
    }

    def render_word(match: re.Match[str]) -> str:
        word = match.group(0)
        if word in words:
            return rf"\mathrm{{{word}}}"
        return word

    content = re.sub(r"[A-Za-z]+", render_word, content)
    return content.replace(" ", r"\,")


def remove_one_arg_macro(value: str, macro: str) -> str:
    while macro in value:
        start = value.find(macro)
        group = find_balanced_group(value, start + len(macro))
        if not group:
            break
        _, group_end, _ = group
        value = value[:start] + value[group_end:]
    return value


def unwrap_two_arg_macro(value: str, macro: str, replacement: str) -> str:
    while macro in value:
        start = value.find(macro)
        first = find_balanced_group(value, start + len(macro))
        if not first:
            break
        second = find_balanced_group(value, first[1])
        if not second:
            break
        _, _, first_content = first
        _, second_end, second_content = second
        if replacement:
            rendered = f"{replacement}{{{first_content}}}{{{second_content}}}"
        else:
            rendered = second_content.replace("$", "")
        value = value[:start] + rendered + value[second_end:]
    return value


def unwrap_nvar(value: str) -> str:
    token = r"\NVar{"
    while token in value:
        start = value.find(token)
        content_start = start + len(token)
        depth = 1
        pos = content_start
        while pos < len(value) and depth:
            if value[pos] == "{":
                depth += 1
            elif value[pos] == "}":
                depth -= 1
            pos += 1
        if depth:
            break
        content = value[content_start : pos - 1]
        prefix = value[:start]
        suffix = value[pos:]
        if prefix and (prefix[-1].isalpha() or re.search(r"\\operatorname\{[^{}]+\}$", prefix)):
            content = " " + content
        value = prefix + content + suffix
    return value


def node_text(node: Tag) -> str:
    clone = BeautifulSoup(str(node), "html.parser")
    for math_node in clone.select("math"):
        alt = math_node.get("alttext")
        math_node.replace_with(f"${clean_latex(alt)}$" if alt else "")
    for tag in clone.select(".ltx_tag"):
        tag.unwrap()
    return clean_text(clone.get_text(" "))


def formula_lines(tag: str, formula: str) -> list[str]:
    label = f" {tag}" if tag else ""
    return [f"Formula{label}:", "", "$$", formula, "$$", ""]


def cache_file(page: PageId) -> Path:
    return CACHE / f"{page.dotted}.html"


def load_soup(page: PageId) -> BeautifulSoup:
    path = cache_file(page)
    if not path.exists():
        raise FileNotFoundError(f"Missing cached DLMF HTML: {path}")
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


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


def contents(soup: BeautifulSoup) -> list[str]:
    items: list[str] = []
    for entry in soup.select("ol.ltx_toclist_section li.ltx_tocentry, ul.ltx_toclist_chapter li.ltx_tocentry a"):
        text = clean_text(entry.get_text(" "))
        text = re.sub(r"^§?\d+(?:\.\d+)?(?:\([^)]+\))?\s*", "", text)
        if text and text not in items:
            items.append(text)
    return items


def keywords(soup: BeautifulSoup) -> list[str]:
    found: list[str] = []
    for node in soup.select("a.ltx_keyword"):
        text = clean_text(node.get_text(" "))
        if text and text not in found:
            found.append(text)
    meta = soup.find("meta", attrs={"name": "keywords"})
    if meta and meta.get("content"):
        for item in meta["content"].split(","):
            text = clean_text(item)
            if text and text not in found:
                found.append(text)
    return found


def notes(soup: BeautifulSoup) -> list[str]:
    found: list[str] = []
    for dt in soup.select("dt"):
        if clean_text(dt.get_text(" ")).rstrip(":") != "Notes":
            continue
        dd = dt.find_next_sibling("dd")
        if dd:
            text = node_text(dd)
            if text and text not in found:
                found.append(text)
    return found


def paragraphs(parent: Tag, limit: int = 6) -> list[str]:
    found: list[str] = []
    for para in parent.select(":scope > div.ltx_para > p.ltx_p, :scope > p.ltx_p"):
        text = node_text(para)
        if text and text not in found:
            found.append(text)
        if len(found) >= limit:
            break
    return found


def equation_blocks(parent: Tag) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    seen: set[str] = set()
    for table in parent.select(":scope table.ltx_equation, :scope table.ltx_equationgroup"):
        for row in table.select("tr.ltx_equation"):
            tag_node = row.select_one(".ltx_tag_equation")
            math_node = row.select_one("math")
            tag = clean_text(tag_node.get_text(" ")) if tag_node else ""
            formula = clean_latex(math_node.get("alttext", "")) if math_node else ""
            formula = re.sub(r"%\s*", "", formula)
            key = f"{tag}:{formula}"
            if formula and key not in seen:
                seen.add(key)
                blocks.append((tag, formula))
    return blocks


def definitions(parent: Tag) -> list[str]:
    found: list[str] = []
    for dt in parent.select("dt"):
        label = clean_text(dt.get_text(" ")).rstrip(":")
        if label not in {"Defines", "Symbols", "Keywords"}:
            continue
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        text = node_text(dd)
        if text and text not in found:
            found.append(f"{label}: {text}")
    return found


def subsection_blocks(soup: BeautifulSoup) -> list[tuple[str, list[str], list[tuple[str, str]], list[str]]]:
    blocks = []
    for section in soup.select("section.ltx_subsection"):
        heading = section.select_one("h2.ltx_title")
        if not heading:
            continue
        title = clean_text(heading.get_text(" "))
        blocks.append((title, paragraphs(section), equation_blocks(section), definitions(section)))
    return blocks


def render(page: PageId) -> str:
    soup = load_soup(page)
    title = page_title(soup)
    version, release_date = observed_version(soup)
    source = f"https://dlmf.nist.gov/{page.dotted}"
    page_kind = "Chapter" if page.section is None else f"§{page.dotted}"

    lines = [
        f"# Chapter {page.chapter} {title}" if page.section is None else f"# §{page.dotted} {title}",
        "",
        "## Mathematical Content",
        "",
        "### Orientation",
        "",
        f"This note explains the mathematics of DLMF {page_kind}, `{title}`, with formulas rendered for Obsidian and short explanations preserved from the source structure.",
        "",
    ]

    page_contents = contents(soup)
    if page_contents:
        lines.extend(["### Contents", ""])
        lines.extend(f"- {item}" for item in page_contents)
        lines.append("")

    section_data = subsection_blocks(soup)
    root_section = soup.select_one("section.ltx_section, section.ltx_chapter")
    if root_section:
        root_paras = paragraphs(root_section, limit=8)
        if root_paras:
            lines.extend(["### Mathematical Narrative", ""])
            lines.extend(f"- {item}" for item in root_paras)
            lines.append("")

        root_equations = equation_blocks(root_section)
        if root_equations and not section_data:
            lines.extend(["### Principal Formulas", ""])
            for tag, formula in root_equations:
                lines.extend(formula_lines(tag, formula))
            lines.append("")

        root_defs = definitions(root_section)
        if root_defs and not section_data:
            lines.extend(["### Definitions and Symbols", ""])
            lines.extend(f"- {item}" for item in root_defs[:80])
            lines.append("")

    if section_data:
        lines.extend(["### Subsections", ""])
        for title, paras, equations, defs in section_data:
            lines.extend([f"#### {title}", ""])
            if paras:
                lines.extend(f"- {item}" for item in paras)
                lines.append("")
            if equations:
                lines.append("Formulas:")
                lines.append("")
                for tag, formula in equations:
                    lines.extend(formula_lines(tag, formula))
                lines.append("")
            if defs:
                lines.append("Definitions and local symbols:")
                lines.extend(f"- {item}" for item in defs[:20])
                lines.append("")

    page_notes = notes(soup)
    page_keywords = keywords(soup)
    lines.extend(
        [
            "## Source and Review Notes",
            "",
            f"- Source: [{source}]({source})",
            f"- Observed version: {version}, release date {release_date}.",
        ]
    )
    if page_keywords:
        lines.append(f"- Keywords: {', '.join(page_keywords[:40])}.")
    if page_notes:
        lines.extend(["", "### Source Notes", ""])
        lines.extend(f"- {item}" for item in page_notes[:8])
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def page_ids_for_chapter(chapter: int) -> list[PageId]:
    ids = [PageId(chapter)]
    for path in sorted(CACHE.glob(f"{chapter}.*.html"), key=lambda item: [int(part) for part in item.stem.split(".")]):
        parts = path.stem.split(".")
        if len(parts) == 2 and parts[0] == str(chapter):
            ids.append(PageId(chapter, int(parts[1])))
    return ids


def write_page(page: PageId) -> None:
    target = PAGES / page.filename
    target.write_text(render(page), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--section", type=int)
    args = parser.parse_args()

    if args.section is not None:
        write_page(PageId(args.chapter, args.section))
        print(f"Deepened section {args.chapter}.{args.section}.")
        return

    pages = page_ids_for_chapter(args.chapter)
    for page in pages:
        write_page(page)
    print(f"Deepened {len(pages)} pages for chapter {args.chapter}.")


if __name__ == "__main__":
    main()
