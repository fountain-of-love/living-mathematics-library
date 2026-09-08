# Snippets

This folder contains stand-alone observation snippets: small knowledge units that preserve one claim, boundary, contract, translation, normalization, or caution at a time.

This is a work in progress. Personal snippets are being formalized, screened, and published gradually rather than promoted all at once.

The most important rule is epistemic discipline:

> Do not describe a normalized observation as if the repository discovered a new mathematical relationship.

The Riemann-hypothesis-facing thread in these snippets is not that a new visual or numerical pattern reveals itself. The working idea is stricter: RH-relevant structure would have to result from arithmetic boundaries and contracts that remain respected under translation into spectral, Fourier, Mellin, or other representational forms.

In that sense, the snippets collect two related kinds of material:

- prime and exclusion properties, such as binary masks, activation at \(p^2\), CRT periods, nesting, and divisor complementarity;
- normalization and translation observations, where the question is whether an invariant, boundary, or contract survives a change of representation.

## What A Snippet May Claim

A snippet may record an exact arithmetic property, a finite construction, a proposed translation contract, a numerical observation, an analogy, or a caution. It must make that status visible in metadata and in the claim boundary.

Use weaker language when the evidence is weaker:

- Say "a numerical pattern was observed under normalization \(N\)" when the result depends on data, range, transform, or plotting choice.
- Say "this contract should be preserved by a faithful translation" when the point is a proof obligation.
- Say "this is exact" only for definitions, identities, finite constructions, or established results with clear domain.

Avoid wording such as "the repository discovered a relationship" unless there is an independently justified mathematical relationship and the snippet states its proof boundary.

## Translation Principle

Many snippets here ask whether an arithmetic contract has a faithful spectral counterpart.

Typical contracts include:

- binary exclusion becoming projection or idempotence;
- periodicity becoming Fourier phase structure;
- divisor complementarity becoming a reflection involution;
- \(p^2\)-activation becoming a half-scale filtration;
- CRT composition becoming product or tensor decomposition;
- closure at \(\sqrt x\) becoming a fixed balance boundary.

The burden is always on the translation. A representation is useful only insofar as it preserves the contract it claims to carry.

## Normalization Principle

Numerical observations require special care. A pattern seen after normalization is evidence about that normalized representation, not automatically evidence about the underlying mathematical object.

When a snippet depends on normalization, include enough information to reproduce and challenge it:

```yaml
experiment:
  id: exp.prime-mask-001
  question: Does X correlate with Y under transformation Z?
  hypothesis: ...
  objects:
    - ...
  dataset:
    source: ...
    version: ...
    hash: ...
  method: ...
  controls:
    - null_model
    - randomized_baseline
    - alternative_normalization
  result:
    statistic: ...
    value: ...
    uncertainty: ...
  interpretation:
    supported: ...
    unsupported: ...
  status: empirical-observation
```

If this structure cannot yet be filled in, keep the snippet at `workflow_status: captured` or `screened` and make the missing evidence explicit.

## Files

- `index.md` is the current catalogue of formalized snippets.
- `Snippet specification.md` defines the required metadata and body sections.
- `Snippet identifier approach.md` defines stable `OBS-000000` identifiers.
- `OBS-*.md` files are the observation snippets themselves.

Each `OBS-` file should remain atomic: one identifier, one stable observational claim, one explicit claim boundary.
