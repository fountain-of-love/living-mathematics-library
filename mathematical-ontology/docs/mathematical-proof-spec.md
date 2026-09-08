# Mathematical Proof Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for proof notes and proof sketches.
- **Companion:** [Mathematical Proof Run](./mathematical-proof-run.md)

## 1. Role

A proof page records why a mathematical claim follows from stated assumptions.

It may be a complete proof, a proof sketch, a verification note, or an audit of a proof attempt. The proof status must be explicit.

## 2. Page Contract

```markdown
# Proof Title

> One-sentence statement of what is being proved or checked.

## Claim

Link to the theorem, formula, definition, or conjecture under discussion.

## Status

One of: complete, sketch, partial, failed, disputed, needs-review.

## Assumptions

- Assumption.

## Strategy

Short description of the proof idea.

## Proof

Step-by-step argument.

## Dependencies

- [[Theorem]]
- [[Definition]]

## Gaps And Caveats

- Known gap, limitation, or unresolved dependency.

## Sources

- [Source](https://example.org)
```

## 3. Required Sections

Every proof page should include:

- claim;
- status;
- assumptions;
- strategy;
- proof or proof sketch;
- dependencies;
- gaps and caveats.

## 4. Empty Field Discipline

Do not omit assumptions, dependencies, gaps, caveats, or sources merely because they are incomplete.

Use explicit values from [Mathematical Process](./mathematical-process.md), such as `unknown`, `not-applicable`, `not-yet-verified`, `not-yet-developed`, `open`, and `not-known`.

## 5. Proof Status

Use the weakest honest status:

- `complete`: the proof is locally complete under the stated assumptions;
- `sketch`: the main idea is present but details are omitted;
- `partial`: only part of the claim is established;
- `failed`: the argument does not prove the claim;
- `disputed`: reliable sources or reviewers disagree;
- `needs-review`: not yet checked closely;
- `not-yet-developed`: proof content has not been written locally;
- `not-yet-verified`: proof content exists but has not been checked closely.

## 6. Review Checklist

- The claim is precise and linked.
- Each dependency is named.
- Hidden assumptions are surfaced.
- The status is not stronger than the evidence.
- Missing information is explicit rather than silently absent.
- Any failed or partial proof remains useful as navigation and audit history.
