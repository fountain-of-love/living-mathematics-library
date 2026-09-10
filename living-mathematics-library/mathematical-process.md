# Mathematical Process

- **Status:** Starter process
- **Purpose:** Repeatable knowledge-engineering operation for mathematical artifacts.
- **Full working draft:** [mathematical-ontology/docs/mathematical-process.md](../mathematical-ontology/docs/mathematical-process.md)

## Rule

Do not scale before running and reviewing [Proof Run 5](./proof-run-5.md).

Use [Mathematical Worklist](./mathematical-worklist.md) as the production queue. Worklist presence means the object is known about; it does not mean the object has been engineered.

## Operation

1. Identify object.
2. Determine object type.
3. Capture source statement.
4. Normalize terminology.
5. Identify prerequisites.
6. Identify related objects.
7. Resolve human links to stable IDs.
8. Record source provenance.
9. Determine epistemic status.
10. Add examples.
11. Add counterexamples where relevant.
12. Add transformations and bonds.
13. Validate formulas.
14. Validate claims.
15. Run consistency checks.
16. Publish.

## Core Guardrails

- The dictionary is an interface.
- Use one-sentence definitions before deep pages.
- Use Obsidian links for humans and stable IDs for machines.
- Preserve source notation before canonical normalization.
- Empty fields are honest when explicitly marked.
- Tables carry stable facts; prose preserves nuance.
- Schema terms are not mathematical entities.
- Experiments and conjectures must not masquerade as established mathematics.

## Absence Vocabulary

Use explicit values instead of silent omission:

- `unknown`
- `not-applicable`
- `not-yet-verified`
- `not-yet-developed`
- `open`
- `not-known`

Imported aliases may appear in older notes:

- `not-yet-checked` -> `not-yet-verified`
- `not-yet-added` -> `not-yet-developed`
- `none-known` -> `not-known`
