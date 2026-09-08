# Mathematical Concept Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for stable mathematical concept notes.
- **Companion:** [Mathematical Dictionary](./mathematical-dictionary.md)

## 1. Role

A concept page gives a stable mathematical idea more room than a dictionary entry, without trying to become a full textbook chapter.

Use this spec when a one-sentence dictionary entry has become important enough to need examples, boundaries, notation, relations, or deeper references.

## 2. Contract Shape

Concept pages begin with a compact contract:

```yaml
id: concept.complex-number
type: concept
status: established

name: Complex number

definition: >
  A number expressible as a + bi, where a,b are real
  and i^2 = -1.

prerequisites:
  - concept.real-number

related:
  - concept.complex-plane
  - concept.imaginary-unit

used_by:
  - formula.euler

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

The Markdown body may then add explanation, examples, diagrams, or deeper references as needed.

## 3. Structured Page Shape

Concept pages should combine a structured facts table with prose.

The structured table carries stable facts:

| Property | Value |
|---|---|
| Type | Concept |
| Domain | Analysis |
| Status | Established |
| Prerequisites | [[Real Number]] |
| Related | [[Limit]], [[Continuity]] |
| Sources | Not listed on source page. |

The prose preserves orientation and nuance:

> Intuitively, a limit describes what a quantity approaches as its input approaches some value. The formal definition makes that intuition precise by controlling how close the output must be when the input is sufficiently close.

Use the table for parseable facts. Use prose for explanation, intuition, warnings, historical texture, and mathematical character.

The structured contract should use stable IDs. The prose and facts table may use Obsidian display links.

For example, a contract may use `concept.real-number` while the page renders `[[Real Number]]`.

## 4. Required Fields

Every concept page should include:

- `id`;
- `type`;
- `status`;
- `name`;
- `definition`;
- `sources` or a clear provenance note.

## 5. Recommended Fields

Use these when they clarify navigation:

- `prerequisites`;
- `related`;
- `used_by`;
- `aliases`;
- `deeper_references`;
- `future_deep_links`.

## 6. Empty Field Discipline

Do not remove recommended fields merely because they are not developed yet.

Use explicit values from [Mathematical Process](./mathematical-process.md), such as `unknown`, `not-applicable`, `not-yet-verified`, `not-yet-developed`, `open`, and `not-known`.

## 7. Scope Discipline

A concept page may explain enough to orient the reader, but it should point outward when a subject belongs to a wider domain.

Create specialized sub-concepts when a page starts carrying multiple distinct meanings. For example, `Invariant` may later lead to `Algebraic Invariant`, `Topological Invariant`, and `Conserved Quantity`.

## 8. Review Checklist

- The `definition` matches the dictionary entry or intentionally refines it.
- The `id` is stable and independent of the filename.
- The `status` describes the mathematics, not the maturity of this page.
- Stable facts are visible in a structured table or contract block.
- Prose preserves intuition and nuance without hiding required fields.
- Human-facing links use Obsidian display names while structured fields use stable IDs.
- Related concepts are links, not embedded mini-articles.
- Missing information is explicit rather than silently absent.
- External expertise is linked rather than duplicated.
