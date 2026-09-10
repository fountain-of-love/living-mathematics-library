# Mathematical Dictionary

- **Status:** Draft 0.1
- **Purpose:** A compact interface ontology for shared mathematical terminology.
- **Scope:** Canonical meanings, relation types, stable links, and outward pointers.

## 1. Interface Principle

The dictionary is an interface.

Its job is not to absorb the whole surrounding domain. Its job is to make mathematical material navigable by establishing:

1. shared meanings;
2. canonical terminology;
3. relationship types;
4. stable links;
5. outward paths toward deeper material.

A dictionary entry should be small enough to read quickly and precise enough to support linking, classification, and later conversion into a formal knowledge node.

The dictionary answers:

> "When this workspace says this term, what does it mean, what should it link to, and where does deeper study begin?"

It does not answer every theorem, proof, convention, historical lineage, or domain-specific variation attached to the term.

## 2. Portal, Don't Duplicate

If another knowledge source owns a subject better, this library should link to it rather than recreate it poorly.

The mathematical dictionary should behave like a portal. It gives enough local meaning for the term to participate in the graph, then points outward to deeper references, specialist notes, or authoritative sources.

For example, this library may need `Complex Analysis` because the Riemann zeta function, Fourier transform, Mellin transform, residues, and Euler's formula all use complex-analytic ideas. That does not mean the dictionary should try to reproduce an entire complex analysis textbook.

The Living Mathematics Library should become a map of mathematics, not an attempt to become the entire internet.

## 3. Relation to the Knowledge-Node Schema

The [Universal Mathematical Knowledge-Node Schema](./universal-mathematical-knowledge-node-schema.md) is the rigorous record format.

This dictionary is the lightweight human interface in front of it. A mature dictionary entry may later become, or link to, one or more schema nodes such as:

- `concept`
- `definition`
- `formula`
- `theorem`
- `source`
- `proof`
- `analogy`

The dictionary keeps the canonical surface stable while deeper nodes carry formal detail, provenance, proofs, variants, and review state.

Schema terms such as `status`, `source`, `prerequisite`, `relationship`, `proof`, and `example` are contract vocabulary. Mathematical entities such as `complex number`, `group`, `ring`, `field`, `derivative`, `integral`, and `Fourier transform` are dictionary or concept material.

Do not turn schema terms into Obsidian concept links unless the entry is explicitly documenting the schema itself.

## 4. Entry Contract

Concepts may begin as one-sentence definitions. A term does not need a full concept page before it can participate in the graph.

Each dictionary entry should use this compact shape:

```markdown
## Canonical Term

A compact definition in one to three sentences.

Related:
- [[Term]]
- [[Term]]

Deeper domain:
- [[Domain]]
- [[Domain]]
```

Optional sections may be added only when they preserve the interface role:

```markdown
Also known as:
- Alternate term

Distinguish from:
- [[Nearby but different term]]

Used in:
- [[Topic]]
```

Use `Deeper reference` when an external or local source carries the fuller treatment:

```markdown
Deeper reference:
- [Authoritative source](https://example.org)
```

Use `Future deep links` when naming concepts that are not yet proper entries but should become stable concepts later:

```markdown
Future deep links:
- [[Future Concept]]
- [[Future Concept]]
```

Future deep links reserve conceptual places. They do not require the target concept to be finished before it can participate in the graph.

This lets the graph grow organically:

```text
mentioned link
   ↓
one-line dictionary entry
   ↓
stable concept
   ↓
deep page
```

The dictionary may point to `[[Multiplicative Structure]]`, `[[Scale Invariance]]`, or `[[Dirichlet Series]]` before those pages are fully engineered. That is a feature, not a defect.

Avoid long derivations, full proofs, extensive examples, and textbook exposition. Point to deeper material instead.

Dictionary entries may use Obsidian display links for human navigation while structured node records use stable IDs behind the scenes.

Human-facing Markdown:

```markdown
Related:
- [[Complex Number]]
- [[Exponential Function]]
- [[Euler's Formula]]
```

Machine-facing structured fields:

```yaml
related:
  - concept.complex-number
  - concept.exponential-function
  - formula.euler
```

## 5. Relationship Types

The dictionary uses a small set of human-readable relationship types. These are intentionally broader than the typed relations in the universal node schema.

Formal node records use the relation taxonomy in [Relation Vocabulary](./relation-vocabulary.md):

```text
relation
├── transformation
├── structural-property
├── equivalence
├── dependency
├── evidence
├── representation
└── analogy
```

The dictionary can stay human-facing, but when a relation becomes part of a node or graph record it should choose a category and a controlled bond type.

| Relationship | Meaning | Example |
|---|---|---|
| `Related` | Terms that are often needed nearby for understanding or use. | Fourier Transform -> Convolution |
| `Related concepts` | Concept-level neighbors that help define the local mathematical neighborhood. | Mellin Transform -> Scale Invariance |
| `Deeper domain` | Fields where the term receives a fuller theory. | Fourier Transform -> Harmonic Analysis |
| `Deeper reference` | External or local sources that carry the full treatment. | Complex Analysis -> external authoritative source |
| `Also known as` | Synonyms, abbreviations, spelling variants, or common alternate names. | Fourier Transform -> Fourier integral transform |
| `Distinguish from` | Terms that are easily confused but not identical. | Fourier Transform -> Fourier Series |
| `Used in` | Applications, methods, or larger constructions that commonly use the term. | Fourier Transform -> Signal Processing |
| `Future deep links` | Terms that are allowed to participate as links now and mature into proper concepts later. | Invariant -> Algebraic Invariant |
| `Generalizes` | A broader term or construction that extends the entry. | Fourier Transform -> Integral Transform |
| `Specializes` | A narrower term or case of the entry. | Fourier Transform -> Discrete Fourier Transform |

When an entry grows beyond these relationship types, it probably wants a formal node or a separate essay.

## 6. Production Process

Terms move through a lightweight lifecycle:

```text
mentioned
   ↓
dictionary entry
   ↓
stable concept
   ↓
deep concept page
   ↓
specialized sub-concepts
```

This is intentionally more forgiving than demanding that every concept be finished before it can participate in the graph.

Dictionary entries still use four production states:

```text
seed -> linked -> reviewed -> canonical
```

### 6.1 Mentioned

A mentioned term may appear as a link before it has its own entry.

This is useful when an entry needs to point toward nearby or future concepts without expanding into them immediately.

### 6.2 Seed

Create the smallest useful entry:

- canonical term;
- one-sentence definition;
- obvious related links;
- obvious deeper domains.

The seed should be useful even before the surrounding ontology is complete.

### 6.3 Linked

Check that links point to stable names already used or intentionally introduced in the workspace.

At this stage:

- use one canonical capitalization;
- avoid duplicate spellings unless listed under `Also known as`;
- add `Distinguish from` for likely collisions;
- prefer Obsidian-style links for concepts: `[[Term]]`.

### 6.4 Stable Concept

A stable concept has a settled canonical name and a reusable working definition.

It may still live only in the dictionary. Stability means the workspace can safely link to it and use it as shared terminology.

### 6.5 Deep Concept Page

A deep concept page is created when the dictionary entry starts needing proofs, variants, examples, formal schemas, historical notes, or domain-specific development.

The dictionary entry should remain compact and point outward to the deeper page.

### 6.6 Specialized Sub-Concepts

Specialized sub-concepts should become their own entries or pages when they have distinct definitions, relations, or mathematical behavior.

Examples include `Algebraic Invariant`, `Topological Invariant`, and `Conserved Quantity`.

### 6.7 Reviewed

Review the entry for scope discipline and mathematical accuracy.

Ask:

- Is the definition true in the intended scope?
- Is the entry compact enough to remain an interface?
- Are relationship labels doing real work?
- Does deeper material belong elsewhere?
- Is there an authoritative external source that should be linked instead of duplicated?
- Is any ambiguity better handled by a separate entry?

### 6.8 Canonical

Mark an entry as canonical only when the workspace should rely on it as the preferred surface meaning.

Canonical entries should have:

- one stable title;
- no unresolved duplicate aliases;
- relation labels that match this file's vocabulary;
- outward links for deeper treatment;
- no hidden textbook payload.

## 7. Quality Invariants

Every dictionary entry should satisfy these invariants:

1. The title is the canonical term.
2. The first paragraph gives the shared working meaning.
3. Related links are typed by section heading, not left as an unstructured list.
4. The entry points outward before it expands inward.
5. The entry avoids absorbing a whole domain.
6. Ambiguity is named explicitly.
7. Synonyms do not create duplicate canonical entries.
8. Scope limits are stated when the usual meaning is not universal.
9. Each new relationship type must be added to the vocabulary in Section 5.
10. Formal claims that require proof belong in knowledge nodes or deeper documents.
11. The dictionary remains readable as a human interface.
12. Links remain stable even if deeper files move.
13. Portal links or refactoring are preferred when an entry starts becoming a miniature textbook, and schema terms are kept out of the mathematical concept graph unless the page is explicitly documenting the schema.

## Invariant

A property of a mathematical object or system that remains unchanged under a specified transformation.

Future deep links:
- [[Algebraic Invariant]]
- [[Topological Invariant]]
- [[Conserved Quantity]]
- [[Group Action]]
- [[Symmetry]]

## Complex Analysis

The study of complex-valued functions and their analytic, geometric, and transformational properties.

This library uses complex analysis in:
- [[Riemann Zeta Function]]
- [[Fourier Transform]]
- [[Mellin Transform]]
- [[Residue]]
- [[Euler's Formula]]

Deeper reference:
- [external authoritative source]

## Euler's Formula

An identity connecting complex exponentials with sine and cosine:

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

Type: [[Formula]]
Domain: [[Complex Analysis]]
Status: [[Established]]

Related:
- [[Complex Number]]
- [[Exponential Function]]
- [[Imaginary Unit]]
- [[Angle]]
- [[Sine Function]]
- [[Cosine Function]]
- [[Unit Circle]]
- [[Rotation]]
- [[Euler's Identity]]
- [[Fourier Transform]]

Future deep links:
- [[Complex Exponential]]
- [[Lie Group]]

## Exponential Function

A function whose values change multiplicatively with additive changes in the input.

Related:
- [[Complex Exponential]]
- [[Euler's Formula]]

Deeper reference:
- [[DLMF §4.2 Definitions]]

## Imaginary Unit

A number \(i\) satisfying \(i^2=-1\).

Related:
- [[Complex Number]]
- [[Euler's Formula]]

## Unit Circle

The circle of radius 1 centered at the origin.

Related:
- [[Angle]]
- [[Sine Function]]
- [[Cosine Function]]
- [[Rotation]]
- [[Euler's Formula]]

## Angle

A measure of rotation or separation between directions, commonly expressed in radians in analytic formulas.

Related:
- [[Unit Circle]]
- [[Rotation]]
- [[Euler's Formula]]

## Sine Function

The trigonometric function giving the vertical coordinate of a point on the unit circle at a given angle.

Related:
- [[Cosine Function]]
- [[Unit Circle]]
- [[Euler's Formula]]

Deeper reference:
- [[DLMF §4.14 Definitions and Periodicity]]

## Cosine Function

The trigonometric function giving the horizontal coordinate of a point on the unit circle at a given angle.

Related:
- [[Sine Function]]
- [[Unit Circle]]
- [[Euler's Formula]]

Deeper reference:
- [[DLMF §4.14 Definitions and Periodicity]]

## Rotation

A transformation that turns an object around a fixed point or axis while preserving relevant distances.

Related:
- [[Angle]]
- [[Unit Circle]]
- [[Euler's Formula]]

## Euler's Identity

The special case of Euler's formula at \(\theta=\pi\), commonly written \(e^{i\pi}+1=0\).

Related:
- [[Euler's Formula]]
- [[Complex Number]]
- [[Unit Circle]]

## Complex Exponential

The exponential function extended to complex inputs.

Related:
- [[Exponential Function]]
- [[Complex Number]]
- [[Euler's Formula]]

Deeper reference:
- [[DLMF §4.2 Definitions]]

## Fourier Transform

A transformation that represents a suitable function in terms of its frequency components.

It translates a function from its original variable, often time or space, into a frequency-domain representation where oscillatory structure becomes explicit.

Related:
- [[Integral]]
- [[Complex Number]]
- [[Frequency]]
- [[Convolution]]
- [[Laplace Transform]]
- [[Mellin Transform]]

Deeper domain:
- [[Harmonic Analysis]]
- [[Functional Analysis]]

Distinguish from:
- [[Fourier Series]]
- [[Discrete Fourier Transform]]
- [[Fast Fourier Transform]]

Used in:
- [[Signal Processing]]
- [[Partial Differential Equation]]
- [[Spectral Analysis]]

## Mellin Transform

An integral transform that represents a suitable function in terms of multiplicative scale rather than additive frequency.

Related concepts:
- [[Multiplicative Structure]]
- [[Scale Invariance]]
- [[Fourier Transform]]
- [[Laplace Transform]]
- [[Dirichlet Series]]
- [[Riemann Zeta Function]]

Deeper domain:
- [[Complex Analysis]]
- [[Analytic Number Theory]]

Future deep links:
- [[Mellin Kernel]]
- [[Asymptotic Analysis]]
- [[Scale Transform]]
