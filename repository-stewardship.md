# Repository Stewardship

Review date: 2026-08-26

Implementation tracker: [Stewardship Progress](stewardship-progress.md)

This review treats the repository as a mathematical corpus. The goal is not to
make the material more complicated, but to make mathematical structure clearer: a primary-school student should find simple mental images, while a university student should be pushed
toward the underlying mathematical structure.

## Teaching Position

The repository should speak with the voice of a mathematics professor who can move
between two levels:

- **Primary-school level:** explain through ordinary images, simple analogies, and clear
  distinctions.
- **University level:** ask what structure is preserved, what representation changed,
  what assumptions are needed, and what has actually been proved.

The guiding rule is:

> A formula should come after the idea has become visible.

## Current Shape

The repository already has an emerging architecture:

| Area                                                                                        | Current role                                                              |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [Mathematical fundamentals](mathematical-ontology/Mathematical%20fundamentals.md)           | Ontology, vocabulary, concept map, and glossary.                          |
| [Formula Registry](notes/formula-registry.md)                                               | Workspace-wide formula index and route map.                               |
| [formulas/](formulas/README.md)                                                             | Dedicated one-formula explanation pages.                                  |
| [formula-bonds/](formula-bonds/README.md)                                                   | Teaching notes explaining why formulas belong together.                   |
| [history-of-prime-distribution-analytics](notes/history-of-prime-distribution-analytics.md) | Historical narrative spine for prime distribution and zeta ideas.         |
| [dlmf/](dlmf/index.md)                                                                      | Reference corpus from the NIST Digital Library of Mathematical Functions. |
| Local-only chat folders                                                                     | Raw research quarry and idea capture.                                     |
| CSV files and scripts                                                                       | Experimental evidence, computations, and reproducibility artifacts.       |

It is not merely a pile of notes. It's intention is to become a layered atlas of
mathematical thinking.

## Main Risk

The main risk is **conceptual drift**.

Different kinds of material are beginning to live close together due to their relations:

- mathematical vocabulary;
- mathematical concepts;
- formulas;
- formula families;
- formula bonds;
- experiments;
- conjectural models;
- cross-domain frameworks;
- raw chat captures;
- reference documentation.

These can coexist, but they should not be presented as if they have the same status.
A child, a student, or a future researcher should always be able to ask:

> What kind of truth am I reading?

## Separation Principle

Use these guidelines when adding new material:

| Layer        | Belongs here when                                                           | Example                                                   |
| ------------ | --------------------------------------------------------------------------- | --------------------------------------------------------- |
| Vocabulary   | The main need is to clarify the meaning of a word.                          | interval, spectrum, ordinal number                        |
| Concept      | The main need is to understand a mathematical object, method, or structure. | complex number, square-free integer, Mellin transform     |
| Formula      | The main need is to state a symbolic relation.                              | Euler's formula, Taylor series, Laplace transform formula |
| Formula bond | The main need is to explain why formulas belong together.                   | Binet, Euler's number, and number-system extension        |
| Experiment   | The main need is to test a proposed pattern against data.                   | zeta-zero spacing scaling                                 |
| Framework    | The main need is to record a structural metaphor or research prompt.        | Spiral Dynamics, Unified Spiral Dynamics                  |
| Reference    | The main need is source fidelity, notation, or provenance.                  | DLMF pages                                                |

No layer is "lesser" than another. They simply answer different questions.

## Recommendations

### 1. Make a root README

The repository needs a front door. A top-level `README.md` should explain:

- start with [Mathematical fundamentals](mathematical-ontology/Mathematical%20fundamentals.md);
- use [Formula Registry](notes/formula-registry.md) to navigate formulas;
- use [formulas/](formulas/README.md) for individual formula explanations;
- use [formula-bonds/](formula-bonds/README.md) for relationships between formulas;
- treat local chat folders as raw research material, not public repository content;
- treat [dlmf/](dlmf/index.md) as reference material;
- treat CSVs and scripts as evidence and reproducibility artifacts.

### 2. Split Mathematical fundamentals into companion pages

[Mathematical fundamentals](mathematical-ontology/Mathematical%20fundamentals.md) has become valuable but
large. It should eventually become a central map that links to smaller companion pages:

| Future page | Purpose |
|---|---|
| `mathematical-ontology.md` | Concept neighborhoods and topology. |
| `mathematical-vocabulary.md` | Relational vocabulary grouped by similarity, contrast, and common confusion. |
| `transform-family.md` | Fourier, Laplace, Mellin, kernels, scale, frequency, and complex variables. |
| `cross-domain-frameworks.md` | Spiral Dynamics, Unified Spiral Dynamics, and other non-mathematical frameworks with guardrails. |

This would reduce scrolling and make the document easier for students to enter. At the same time, they should have a graph-like navigation structure that supports both human readability as well as AI-navigation.

### 3. Keep the transform family as siblings, not a ladder

Fourier, Laplace, and Mellin should be taught as related representation changes:

| Transform | Simple intuition | Mathematical direction |
|---|---|---|
| Fourier | Which waves are present? | additive frequency |
| Laplace | Which waves appear with growth or decay? | complex frequency |
| Mellin | Which scale-patterns are present? | multiplicative powers |

They are connected, but should not be presented as one strict chain. A better mental
image is a family of lenses.

### 4. Add status labels to the Formula Registry

[Formula Registry](notes/formula-registry.md) lists many suggested pages, but only some exist
under [formulas/](formulas/README.md). Add a status column:

| Status | Meaning |
|---|---|
| Exists | Dedicated page already exists. |
| Planned | Worth creating soon. |
| Candidate | Useful, but needs more context before promotion. |
| Experimental | Connected to data or hypotheses and should not be read as established. |

This protects the reader from assuming every listed formula has equal maturity.

### 5. Prioritize the next formula pages

The next high-value one-page formula notes are:

1. `formulas/eulers-formula.md`
2. `formulas/fourier-transform.md`
3. `formulas/laplace-transform.md`
4. `formulas/mellin-transform.md`
5. `formulas/riemann-zeta-function.md`
6. `formulas/prime-number-theorem.md`

Each should be readable in three passes:

- first pass: ordinary analogy;
- second pass: core formula and symbols;
- third pass: what structure it preserves or transforms.

### 6. Use a standard teaching page pattern

For concept and formula pages, use this structure:

| Section | Purpose |
|---|---|
| The Ordinary Picture | A primary-school-level image or analogy. |
| The Mathematical Object | The clean definition. |
| The Formula | The simplest useful symbolic form, if there is one. |
| What Changes Representation | What becomes easier to see after using the concept. |
| Common Confusion | A nearby wrong idea and the correction. |
| University Checkpoint | A deeper reasoning question. |
| Links | Related vocabulary, concepts, formula pages, and references. |

This keeps the professor voice consistent.

### 7. Quarantine speculative material without deleting it

The cross-domain material is useful, but it must remain clearly labeled. Spiral
Dynamics and Unified Spiral Dynamics should eventually move to a companion
cross-domain page with this warning:

> This is a conceptual framework, not a mathematical theorem.

This preserves creativity while protecting mathematical truthfulness.

### 8. Curate raw chats into research notes

The chat files contain important ideas, but they mix insight, repetition, and
provisional language. Create a promotion path:

```text
chats/ -> research-inbox/ -> research-notes/ -> polished documents
```

Useful extracted notes should contain:

- the idea;
- the mathematical object it suggests;
- what is established;
- what is speculative;
- what would test it.

### 9. Normalize names over time

Some filenames are still raw captures. Rename gradually when touching related material:

| Current style | Suggested style |
|---|---|
| `Rieman chats/` | `riemann-chats/` |
| `Notes prime - RH.md` | `research-inbox/prime-rh-notes.md` |
| `Mathematical ontology/Equivalence and Gauge in Mathematical Translation.md` | Renamed from a raw capture to a descriptive course-module title. |

Do this carefully, because links may depend on current paths.

### 10. Add light validation scripts

The repository would benefit from small, non-invasive checks:

- duplicate headings in key documents;
- duplicate TOC entries;
- broken local Markdown links;
- formula registry entries whose suggested page already exists;
- formula pages missing the standard teaching sections.

This is not bureaucracy. It is mathematical hygiene.

## Priority Order

| Priority | Action | Why |
|---|---|---|
| 1 | Add root `README.md`. | Gives every reader a front door. |
| 2 | Fix duplicate TOC entries in Mathematical fundamentals. | Removes immediate navigation drift. |
| 3 | Add status labels to Formula Registry. | Separates existing, planned, candidate, and experimental material. |
| 4 | Create `transform-family.md`. | Fourier/Laplace/Mellin are now central and deserve a clean shared home. |
| 5 | Create high-priority formula pages. | Moves formulas out of glossary entries into teachable one-page notes. |
| 6 | Curate raw chats into research notes. | Converts insight into reusable mathematical material. |

## Final Judgment

This repository is strongest when it treats mathematics as a movement of representation:

```text
ordinary image -> precise vocabulary -> mathematical object -> formula -> transformation -> test
```

The next stage is not to add more complexity. It is to make the existing complexity
navigable, honest, and teachable.
