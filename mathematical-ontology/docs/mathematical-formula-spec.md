# Mathematical Formula Spec

- **Status:** Draft 0.1
- **Purpose:** Page contract for formulas, identities, transforms, recurrences, and computational expressions.
- **Companion:** [Universal Mathematical Knowledge-Node Schema](./universal-mathematical-knowledge-node-schema.md)

## 1. Role

A formula page preserves a mathematical expression together with the conditions under which it is meaningful.

The page should make the formula usable, linkable, and auditable. It should not hide assumptions inside prose.

## 2. Contract Shape

Formula pages begin with a compact contract:

```yaml
id: formula.euler
type: formula
status: established

name: Euler's formula

source_expression: |
  e^(i theta) = cos(theta) + i sin(theta)

canonical_expression: |
  e^{i\theta} = \cos(\theta) + i\sin(\theta)

equivalence:
  status: established
  reason: notation normalization

notation_notes:
  - "theta is written canonically as \\theta."
  - "Function names are written canonically with LaTeX operators."

objects:
  - concept.complex-number
  - concept.exponential-function
  - concept.sine
  - concept.cosine

relations:
  derives:
    - formula.euler-identity
  connects:
    - concept.complex-rotation

verification:
  type: proof
  status: not-yet-developed

sources:
  - id: source.not-listed
    role: reference
    note: Not listed on source page.
```

The Markdown body may then add symbol tables, convention notes, examples, and derivations.

## 3. Formula Provenance

Do not overwrite a source expression with the library's preferred expression.

When a source writes one form and the library uses another canonical form, preserve both:

```yaml
source_expression: |
  \sum_{n=1}^{\infty}\frac{1}{n^s}

canonical_expression: |
  \zeta(s)=\sum_{n=1}^{\infty}n^{-s}

equivalence:
  status: established
  reason: algebraic rewriting

notation_notes:
  - "n^{-s} is equivalent to 1/n^s."
  - "The summation domain is unchanged."
```

If equivalence has not been checked, use `status: not-yet-verified`.

## 4. Required Fields

Every formula page should include:

- `id`;
- `type`;
- `status`;
- `name`;
- `source_expression`;
- `canonical_expression`;
- `equivalence`;
- `objects`;
- `sources` or a clear provenance note.

## 5. Recommended Fields

Use these when they clarify mathematical use:

- `conditions`;
- `symbols`;
- `relations`;
- `verification`;
- `normalization`;
- `notation_notes`;
- `used_in`;

Structured fields such as `objects`, `relations`, `prerequisites`, and `used_in` should use stable IDs. Human prose may render the same targets as Obsidian links.

## 6. Empty Field Discipline

Do not remove conditions, symbols, verification, equivalence, notation notes, or sources merely because they are unfinished.

Use explicit values from [Mathematical Process](./mathematical-process.md), such as `unknown`, `not-applicable`, `not-yet-verified`, `not-yet-developed`, `open`, and `not-known`.

## 7. Formula Types

Use one of these labels when helpful:

- identity;
- definition;
- transform;
- recurrence;
- asymptotic relation;
- approximation;
- inequality;
- computational rule.

## 8. Review Checklist

- The source expression is preserved before canonical normalization.
- Equivalence status and reason are recorded.
- Notation changes are named in `notation_notes`.
- All symbols in `canonical_expression` are explained in `symbols` or the body.
- Human-facing links use Obsidian display names while structured fields use stable IDs.
- Conditions include domain and convergence where relevant.
- Normalization conventions are stated when multiple conventions exist.
- The formula links to concepts rather than re-explaining whole domains.
- Missing information is explicit rather than silently absent.
- Sources are present for externally acquired formulas.
