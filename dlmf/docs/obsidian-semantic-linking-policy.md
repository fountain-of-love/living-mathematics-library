# Obsidian Semantic Linking Policy

## Classification

This document is a policy with a lightweight implementation spec.

- Policy: decides what should become an Obsidian link and what should remain plain mathematical notation.
- Spec: defines the folder layout, link style, formula anchors, and extraction rules used to build a useful graph.

The goal is an informative mathematical graph, not maximum link density.

## Purpose

The DLMF Markdown corpus should support two reading modes:

- Page reading: each DLMF page remains one local Markdown file.
- Concept navigation: Obsidian links connect formulas, definitions, named functions, named operators, and named methods across pages.

Semantic links must add mathematical meaning without changing the formula itself.

## Core Rules

1. Preserve one Markdown file per DLMF source page.
2. Do not rewrite mathematical formulas just to add links.
3. Put concept links outside formulas unless the link is part of surrounding explanatory text.
4. Link named concepts, not ordinary local variables.
5. Prefer stable concept pages over ad hoc aliases.
6. Use formula block anchors for important formulas.
7. Keep graph edges curated enough that the Obsidian graph remains readable.

## Folder Layout

```text
dlmf/
  pages/
    section-01-04.md
    section-01-15.md
  concepts/
    limit.md
    derivative.md
    integral.md
    power.md
    exponentiation.md
    exponential-function.md
    cauchy-principal-value.md
  docs/
    obsidian-semantic-linking-policy.md
```

## Link Targets

Use concept pages for stable mathematical objects:

- Concepts: `[[dlmf/concepts/limit|limit]]`, `[[dlmf/concepts/derivative|derivative]]`
- Named functions: `[[dlmf/concepts/gamma-function|gamma function]]`, `[[dlmf/concepts/bessel-function|Bessel function]]`
- Named operators: `[[dlmf/concepts/cauchy-principal-value|Cauchy principal value]]`
- Named methods and theorems: `[[dlmf/concepts/lhopital-rule|L'Hopital's rule]]`
- Transforms: `[[dlmf/concepts/fourier-transform|Fourier transform]]`

Avoid links for ordinary local variables:

- Do not link generic `x`, `n`, `z`, `a`, `b`, `k`.
- Do not link ordinary arithmetic symbols such as `+`, `=`, `<`, `\leq`.
- Do not link every occurrence of a notation token inside formulas.

## Power, Exponentiation, and Exponential Function

Distinguish these concepts:

- `$x^2$` is a power and belongs near `[[dlmf/concepts/power|power]]` or `[[dlmf/concepts/exponentiation|exponentiation]]`.
- `$a^x$` is exponentiation with variable exponent.
- `$\mathrm{e}^x$` and `$\exp x$` belong near `[[dlmf/concepts/exponential-function|exponential function]]`.

Do not call every power expression an exponential function.

## Section Page Pattern

Each deepened section may include a curated concept list near the top:

```md
### Concepts

- [[dlmf/concepts/limit|Limits]]
- [[dlmf/concepts/derivative|Derivatives]]
- [[dlmf/concepts/lhopital-rule|L'Hopital's rule]]
```

Formula entries may include concept metadata immediately before the display math:

```md
Formula 1.4.15:

Concepts: [[dlmf/concepts/limit|limit]], [[dlmf/concepts/derivative|derivative]], [[dlmf/concepts/lhopital-rule|L'Hopital's rule]]

$$
\lim\limits_{x\to a}\frac{f(x)}{g(x)}=\lim\limits_{x\to a}\frac{f^{\prime}(x)}{g^{\prime}(x)}
$$
^formula-1-4-15
```

## Formula Anchors

Use stable Obsidian block IDs for formulas:

```text
^formula-C-S-N
```

Where:

- `C` is the DLMF chapter number.
- `S` is the DLMF section number.
- `N` is the formula number within that section.

Examples:

- `^formula-1-4-15`
- `^formula-1-15-6`
- `^formula-10-2-1`

Concept pages may link back to formulas:

```md
## Examples

- [[../pages/section-01-04#^formula-1-4-15|L'Hopital's rule]]
- [[../pages/section-01-15#^formula-1-15-6|Cesaro summability label]]
```

## Concept Page Pattern

Concept pages should be short, stable, and reusable:

```md
# Limit

## Meaning

A limit describes the value approached by a function, sequence, or expression as its input approaches a point or infinity.

## DLMF Links

- [[../pages/section-01-04|§1.4 Calculus of One Variable]]
- [[../pages/section-01-09|§1.9 Calculus of a Complex Variable]]

## Formula Examples

- [[../pages/section-01-04#^formula-1-4-14|Limit setup for L'Hopital's rule]]
- [[../pages/section-01-04#^formula-1-4-15|L'Hopital's rule]]
```

## Extraction Guidance

When a script adds semantic links:

1. Preserve formula TeX exactly except for rendering-compatibility normalization already defined in the extractor.
2. Add links in concept lists and formula metadata, not inside raw display formulas.
3. Use deterministic slugs for concept files.
4. Reuse existing concept files before creating new ones.
5. Keep generated links conservative.
6. Record source DLMF page and observed version metadata as usual.

## Appropriate Automation

The first useful automation should be a conservative concept linker:

- Input: section Markdown files and a concept registry.
- Output: `### Concepts` lists and optional formula-level `Concepts:` lines.
- It should never inject wiki links inside display math.
- It should report proposed new concept pages before creating many of them.

## Anti-Patterns

Avoid:

- Linking every occurrence of `$x$`, `$n$`, or `$z$`.
- Creating multiple names for the same concept, for example both `power.md` and `powers.md`.
- Embedding `[[...]]` links inside `$$...$$` formulas.
- Turning formula preservation into formula rewriting.
- Creating a graph that is visually dense but mathematically unhelpful.

## Initial Chapter 1 Concept Candidates

- `binomial-coefficient`
- `matrix`
- `determinant`
- `inner-product`
- `norm`
- `limit`
- `continuity`
- `derivative`
- `integral`
- `cauchy-principal-value`
- `taylor-theorem`
- `fourier-series`
- `complex-variable`
- `residue`
- `differential-equation`
- `integral-transform`
- `distribution`
- `dirac-delta`
- `hilbert-space`
- `eigenfunction-expansion`

These are candidates, not a mandate to link every occurrence.
