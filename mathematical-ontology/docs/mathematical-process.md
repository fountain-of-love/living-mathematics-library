# Mathematical Process

- **Status:** Draft 0.1
- **Purpose:** Repeatable production process for the Living Mathematics Library.
- **Reference pattern:** Gemstones uses separate spec, process, dictionary, and proof-run files for a living knowledge base.

## 1. Principle

Use small page contracts instead of one enormous schema.

The universal schema defines the deeper data model. The page specs define how humans create, review, and grow mathematical notes without forcing every term to be complete on arrival.

The contract family is intentionally plural:

```text
dictionary
concept
formula
theorem
conjecture
proof
experiment
proof-run
```

Each contract begins with the smallest structured block that makes the artifact linkable and reviewable.

Before scaling any new contract family across a large corpus, complete the [Mathematical Knowledge Engineering Proof Run](./mathematical-proof-run.md).

Do not scale before doing this.

Schema terms and mathematical entities must stay distinct. `status`, `source`, `prerequisite`, `relationship`, `proof`, and `example` describe the knowledge record. `complex number`, `group`, `ring`, `field`, `derivative`, `integral`, and `Fourier transform` are mathematical entities represented by records.

Schema terms should usually be written as code-formatted fields, such as `status`, not as Obsidian concept links. Mathematical entities should use human-facing links and stable IDs.

## 2. Design Tensions

The mathematics repository is built around productive tensions. These tensions should be preserved rather than prematurely resolved.

### 2.1 Intuitive Vs Formal

Every concept should have both an accessible orientation and a precise mathematical formulation.

The intuitive layer helps humans enter the idea. The formal layer protects the mathematics from becoming vague or misleading.

### 2.2 Canonical Vs Plural Notation

The library normalizes notation without pretending alternative conventions are wrong.

Source notation should be preserved, canonical notation should be explicit, and the equivalence between them should be recorded when a rewrite is made.

### 2.3 Provenance Vs Synthesis

The library preserves source attribution while allowing original synthesis.

Imported claims, formulas, and definitions need provenance. Local synthesis should be marked as synthesis, not disguised as source material.

### 2.4 Local Page Vs Graph

A page should be understandable alone but become richer through links.

Each artifact should carry enough context to stand on its own while using typed relationships to connect to prerequisites, related objects, transformations, proofs, experiments, and deeper domains.

### 2.5 Established Vs Exploratory

Speculation may be connected to mathematics, but it must never masquerade as established mathematics.

Conjectures, experiments, heuristics, analogies, and failed proof attempts are welcome when their epistemic status is explicit.

### 2.6 Consistency Vs Mathematical Character

Templates should support comparison without forcing every mathematical object into identical prose.

The contracts define shared fields and review checks. The body of a page may keep the particular character of a concept, formula, theorem, proof, or experiment.

## 3. Structured Tables Plus Prose

Use structured tables for stable facts and prose for nuance.

Structured fields give humans and AI something predictable to scan, compare, validate, and link. Prose preserves mathematical intuition, historical texture, explanation, and careful distinctions that do not fit cleanly in a table.

For a mathematical concept, the page may begin with a compact facts table:

| Property | Value |
|---|---|
| Type | Concept |
| Domain | Analysis |
| Status | Established |
| Prerequisites | Real numbers |
| Related | Limits, continuity |
| Sources | Not listed on source page. |

Then the prose can explain the idea:

> Intuitively, a limit describes what a quantity approaches as its input approaches some value.

Do not force nuance into a table. Do not hide stable facts inside prose when they should be parseable.

## 4. Empty Fields Are Honest

Never silently remove missing information from a mathematical contract.

If a field matters to the meaning of a page, preserve the field and mark its current state explicitly. A missing `counterexamples` field must not be read as "there are no counterexamples." It may only mean "this page has not documented the counterexample state."

Use this absence vocabulary:

| Value | Meaning |
|---|---|
| `unknown` | The library does not currently know the value. |
| `not-applicable` | The field does not apply to this artifact. |
| `not-yet-verified` | The field has been filled or claimed but has not been checked. |
| `not-yet-developed` | The section or field is intentionally deferred. |
| `open` | The mathematical question is unresolved in the stated scope. |
| `not-known` | No example, proof, source, or counterexample is documented in this library or in the checked record. |

Prefer an explicit value such as `Not listed on source page.` when extracting from a source page.

Compatibility aliases from the architecture note may appear in imported material:

| Alias | Preferred value |
|---|---|
| `not-yet-checked` | `not-yet-verified` |
| `not-yet-added` | `not-yet-developed` |
| `none-known` | `not-known` |

## 5. Production Flow

```text
mentioned
   ↓
dictionary entry
   ↓
page contract selected
   ↓
draft page
   ↓
reviewed page
   ↓
stable concept or result
   ↓
specialized sub-pages
```

Future deep links are allowed in the early stages of this flow. A page may link to a conceptual place before that place has a complete node, as long as the link is treated as a reservation for future development rather than as completed knowledge engineering.

## 6. Formula Provenance

Never collapse source notation into canonical notation without recording the transformation.

For formulas, preserve:

- `source_expression`: the expression as the source presents it;
- `canonical_expression`: the library's normalized expression;
- `equivalence`: whether and why the two forms are equivalent;
- `notation_notes`: the specific notation changes.

This prevents a source variant from being lost and prevents a canonical rewrite from pretending to be the original source text.

## 7. Obsidian Links And Stable IDs

Use Obsidian links for human-friendly navigation and stable IDs for machine-readable structure.

Markdown should render readable links:

```markdown
[[Complex Number]]
[[Real Number]]
[[Exponential Function]]
[[Euler's Formula]]
[[Fourier Transform]]
```

Structured fields should use stable IDs:

```yaml
related:
  - concept.complex-number
  - concept.exponential-function
  - formula.euler
```

The dictionary is the stable human interface. Node contracts provide the stable machine interface.

When creating or reviewing a page, check both surfaces:

- human-facing prose uses readable display names;
- machine-facing fields use stable IDs;
- aliases and renamed pages do not change stable IDs;
- future deep links may reserve conceptual places before full nodes exist.

## 8. Choose The Smallest Useful Artifact

| Need | Artifact |
|---|---|
| Shared meaning or future deep link only | [Mathematical Dictionary](./mathematical-dictionary.md) |
| Stable idea needing examples or boundaries | [Mathematical Concept Spec](./mathematical-concept-spec.md) |
| Expression with symbols and conditions | [Mathematical Formula Spec](./mathematical-formula-spec.md) |
| Established mathematical claim | [Mathematical Theorem Spec](./mathematical-theorem-spec.md) |
| Open mathematical claim | [Mathematical Conjecture Spec](./mathematical-conjecture-spec.md) |
| Argument, proof sketch, or proof audit | [Mathematical Proof Spec](./mathematical-proof-spec.md) |
| Computation, visualization, or exploration | [Mathematical Experiment Spec](./mathematical-experiment-spec.md) |
| Audit trail of the first complete run | [Mathematical Proof Run](./mathematical-proof-run.md) |

## 9. Knowledge-Engineering Operation

Use this operation whenever creating or materially revising a mathematical artifact.

The process is itself an artifact. It is meant to be followed, reviewed, improved, and eventually automated.

### 9.1 Identify Object

Name the mathematical object, claim, formula, experiment, source, person, or event being captured.

If the object is only mentioned in passing, record it as a dictionary link before creating a full page.

### 9.2 Determine Object Type

Choose the smallest fitting contract:

- dictionary;
- concept;
- formula;
- theorem;
- conjecture;
- proof;
- experiment.

Do not promote an object to a deeper contract before it needs one.

Do not treat contract labels such as `concept`, `formula`, `proof`, or `example` as mathematical entities unless the artifact is explicitly about the schema.

### 9.3 Capture Source Statement

Preserve the source's wording, formula, notation, or claim before normalization.

For formulas, this means filling `source_expression` before `canonical_expression`.

### 9.4 Normalize Terminology

Map source terminology onto the library's canonical names.

Record aliases rather than creating duplicate concepts. If the normalization changes notation or wording in a meaningful way, add notes explaining the change.

### 9.5 Identify Prerequisites

List concepts, definitions, formulas, or assumptions needed before the artifact can be understood.

Use explicit absence values when prerequisites are unknown or not yet developed.

### 9.6 Identify Related Objects

Add typed links to nearby objects:

- related concepts;
- formulas used by or using the object;
- theorem dependencies;
- conjectures;
- experiments;
- transformations and bonds.

Links should help navigation without pretending that all related objects are equivalent.

### 9.7 Resolve Human Links To Stable IDs

For every important Obsidian link in the page, decide whether it already has or should later have a stable ID.

Readable Markdown may say `[[Complex Number]]`; structured fields should say `concept.complex-number`.

If the target is not yet developed, keep the display link and mark it as a future deep link or unresolved stable ID rather than deleting it.

This is how the graph grows organically without requiring every linked concept to be finished before it can participate.

### 9.8 Record Source Provenance

Record where the statement came from.

Use source URLs, page or section identifiers, equation numbers, version metadata, retrieval dates, and local paths where available. If a source page does not list something, preserve the field with `Not listed on source page.`

A source should eventually become its own node, such as `source.dlmf.4.2`, so provenance can participate in the graph.

### 9.9 Determine Epistemic Status

Separate the truth status of the mathematics from the maturity of the local page.

Use statuses such as:

- established;
- conditional;
- open;
- refuted;
- experimental;
- heuristic;
- disputed;
- not-yet-verified.

### 9.10 Add Examples

Add examples when they clarify meaning or use.

If examples are needed but not yet available, preserve the field with `not-yet-developed`.

### 9.11 Add Counterexamples Where Relevant

For theorem, conjecture, definition-boundary, and experiment pages, record counterexample status explicitly.

Do not infer "no counterexample" from silence. Use `not-known`, `not-applicable`, `unknown`, or scoped notes.

### 9.12 Add Transformations And Bonds

Record transformations, equivalences, dependencies, derivations, representations, invariants, and loss-of-information relationships.

Use this step to connect the artifact to the mathematical ontology without expanding the page into a full domain treatment.

### 9.13 Validate Formulas

Check formulas for:

- source expression preserved;
- canonical expression recorded;
- equivalence status and reason;
- symbol definitions;
- domains and convergence conditions;
- normalization conventions;
- source provenance.

If equivalence is not checked, use `not-yet-verified`.

### 9.14 Validate Claims

Check mathematical claims for:

- scope;
- assumptions;
- dependencies;
- proof status;
- counterexample status;
- evidence status;
- provenance.

Do not upgrade evidence, examples, or experiments into proof.

### 9.15 Run Consistency Checks

Before publishing, check:

- required contract fields are present;
- interpretation-critical empty fields have explicit absence values;
- IDs are stable and canonical;
- schema terms are not linked as mathematical concepts;
- human-facing Obsidian links have stable IDs where applicable;
- relation targets are stable links or intentionally unresolved future links;
- source notation and canonical notation are not collapsed;
- the page does not duplicate a deeper source poorly;
- the relevant spec checklist has been applied.

### 9.16 Publish

Publish only when the artifact has:

- a fitting contract;
- explicit status;
- preserved provenance;
- stable links;
- honest absence values;
- completed formula or claim validation where relevant.

If the artifact fails these checks, keep it as draft, seed, or not-yet-verified.

## 10. Boundary Rules

- Do not turn a concept page into a domain textbook.
- Do not turn a formula page into a full proof unless the proof has its own page.
- Do not turn a theorem page into a proof unless the proof has its own page.
- Do not turn a conjecture page into a proof attempt unless the proof attempt has its own page.
- Do not turn an experiment into a theorem.
- Do not duplicate a better external source.
- Do split specialized sub-concepts when definitions diverge.
- Do preserve the design tensions instead of flattening every artifact into the same voice.

## 11. Refactoring Triggers

Refactor when:

- a dictionary entry needs examples, caveats, or variants;
- a concept page accumulates multiple specialized meanings;
- a formula page depends on a proof that deserves its own audit trail;
- an experiment produces a reusable conjecture or counterexample;
- a page becomes hard to scan because it is doing more than one job.
