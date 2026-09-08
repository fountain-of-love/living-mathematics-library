# Mathematics Workspace

This repository is a layered atlas of mathematical thinking. It collects fundamentals,
formula explanations, formula relationships, historical notes, experiments, raw
conversation material, and reference documentation.

The aim is teaching clarity: a young learner should find a simple picture, and a
university student should find the deeper structure behind the picture.

## Ambition

The ambition is to bring this mathematics workspace toward a standard similar to
[Gemstones](https://github.com/fountain-of-love/gemstones), especially in terms of knowledge engineering: clear concept boundaries, durable provenance, navigable relationships, and material that can support both human study and machine-assisted reasoning.

A strongest foundation has been made visible: the repository separates formulas,
formula bonds, mathematical ontology, historical notes, experiments, and DLMF-derived
reference material. The main missing part is not more raw material. The main missing
part is more accessible dual-usage content: pages that are readable as lessons by
people and structured enough to become reliable knowledge nodes for tools. Making it accessible and distributed for everyone.

The next level is graph-based exploration and navigation. Mathematical ideas should be
easy to traverse by relation: definition, example, formula, transformation, invariant,
analogy, source, evidence, limitation, and open question. A reader should be able to
move from an ordinary image to a formal object, then sideways into related formulas,
historical context, and verified reference material without losing the type of claim
being made.

## Current Architecture

The Living Mathematics Library is currently built around a formal, machine-readable
**math-node/0.1** knowledge model.

The repository is no longer only a collection of mathematical Markdown pages. Each
canonical knowledge object is intended to be representable as a typed mathematical
node with:

- a stable identity;
- a declared node type;
- epistemic status;
- governance/page maturity;
- typed semantic relationships;
- structured provenance;
- type-specific attributes;
- validation invariants.

The human-readable Markdown layer and the machine-readable knowledge layer are
designed to coexist:

```text
Markdown
   ↓
math-node/0.1 frontmatter + content
   ↓
validated node records
   ↓
knowledge graph / indexes
   ↓
AI retrieval, navigation, visualization
```

### Canonical Specification

The normative specification currently lives in:

- [Knowledge Node Spec](mathematical-ontology/docs/knowledge-node-spec.md)
- [Universal Mathematical Knowledge-Node Schema](mathematical-ontology/docs/universal-mathematical-knowledge-node-schema.md)
- [Relation Vocabulary](mathematical-ontology/docs/relation-vocabulary.md)

The current schema version is **math-node/0.1**.

### Architectural Status

Implemented:

- universal mathematical knowledge-node envelope;
- stable node identities;
- typed node classes;
- typed semantic relations with relation categories and bond types;
- epistemic status;
- governance/page maturity;
- provenance model;
- formula, theorem, conjecture, proof, and experiment contracts;
- proof and counterexample structures;
- analogy constraints;
- validation invariants;
- one Euler's formula vertical slice with concepts, formula pages, teaching page,
  example, source nodes, and graph record.

In progress:

- migrating existing corpus material into the canonical node model;
- automated validation;
- graph extraction and indexing;
- completing high-priority canonical formula and concept pages;
- selecting precise source statements for canonical formulas;
- completing the controlled bond vocabulary within each relation category.

### Design Principle

The schema is the contract. Markdown explains the mathematics; structured metadata
makes the mathematical knowledge explicit, linkable, auditable, and machine-readable.

## Where To Start

| Reader need | Start here | Why |
|---|---|---|
| I want the conceptual map. | [Mathematical Fundamentals](mathematical-ontology/Mathematical%20fundamentals.md) | Ontology, vocabulary, topology, and core concept entries. |
| I want to find a formula. | [Formula Registry](formula-registry.md) | Workspace-wide index of formulas and learning routes. |
| I want one formula explained. | [Dedicated Formula Pages](formulas/README.md) | Focused pages for individual formulas and named functions. |
| I want to understand relationships between formulas. | [Formula Bonds](formula-bonds/README.md) | Teaching notes about why formulas belong together. |
| I want the prime/zeta story. | [Formula Genealogy](notes/03-03-formula-genealogy-zeta-to-primes.md) | Narrative path from prime counting to zeta and back. |
| I want to review emerging observations. | [Brain-Dump Observation Index](brain-dumps/README.md) | Context-first registry of raw observations, translations, status, scope, and promotion readiness. |
| I want the historical prime-distribution account. | [History of Prime Distribution Analytics](notes/01-03-history-of-prime-distribution-analytics.md) | Historical spine for primes, zeta, zeros, and statistical structure. |
| I want reference material. | [DLMF Documentation Index](dlmf/index.md) | Local map of the NIST Digital Library of Mathematical Functions notes. |
| I want the Living Mathematics Library starter contract. | [Living Mathematics Library](living-mathematics-library/knowledge-node-spec.md) | Minimal dictionary, node spec, process, and proof-run gate before scaling. |

## Reading Principle

Move from image to structure:

```text
ordinary picture -> precise vocabulary -> mathematical object -> formula -> transformation -> test
```

A formula should come after the idea has become visible.

## Repository Layers

| Layer | Purpose | Examples |
|---|---|---|
| Vocabulary | Clarify words and common confusions. | interval, spectrum, ordinal number |
| Concept | Explain mathematical objects, methods, or structures. | complex number, square-free integer, Mellin transform |
| Formula | State and explain symbolic relations. | Euler's formula, Taylor series, Laplace transform |
| Formula bond | Explain why formulas belong together. | Binet, Euler's number, and number-system extension |
| Experiment | Test a proposed pattern against data. | zeta-zero spacing scaling |
| Cross-domain framework | Preserve structural metaphors with guardrails. | Vortex Math and Trading, Spiral Dynamics, Unified Spiral Dynamics |
| Reference | Preserve source fidelity and notation. | DLMF pages |
| Raw research | Capture ideas before curation. | local-only chat transcripts and rough notes |

These layers should not drift into each other. The reader should always be able to ask:

> What kind of truth am I reading?

## Main Navigation

- [Mathematical Fundamentals](mathematical-ontology/Mathematical%20fundamentals.md)
- [Formula Registry](formula-registry.md)
- [Formulas](formulas/README.md)
- [Formula Bonds](formula-bonds/README.md)
- [Formulas Linked To Prime Numbers](notes/03-04-formulas-linked-to-prime-numbers.md)
- [Formula Genealogy: From Prime Counting To Zeta, And Back Again](notes/03-03-formula-genealogy-zeta-to-primes.md)
- [Brain-Dump Observation Index](brain-dumps/README.md)
- [Repository Stewardship Review](repository-stewardship.md)
- [Stewardship Progress](stewardship-progress.md)

## Current Stewardship Work

The current improvement plan is tracked in [Stewardship Progress](stewardship-progress.md).

The first stewardship review is documented in
[Repository Stewardship Review](repository-stewardship.md).

## Source And Evidence Notes

The repository mixes exposition with experiments. Experimental claims should remain
separate from established mathematical facts unless they have been proved or verified
against appropriate controls.

CSV files and scripts are part of the evidence layer. They should be kept close to the
documents that interpret them, but the documents should state clearly what the data
supports and what remains conjectural.
