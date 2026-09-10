# Mathematical Dictionary

- **Status:** Starter interface
- **Purpose:** Stable human-facing vocabulary for the Living Mathematics Library.
- **Full working draft:** [mathematical-ontology/docs/mathematical-dictionary.md](../mathematical-ontology/docs/mathematical-dictionary.md)

## Rule

The dictionary is an interface.

It establishes shared meanings, canonical terminology, relationship types, stable display links, and outward paths toward deeper material. It does not try to absorb the whole surrounding domain.

## Entry Shape

```markdown
## Canonical Term

One-sentence definition or orientation.

Related:
- [[Related Term]]

Future deep links:
- [[Conceptual Place Reserved For Later]]

Deeper reference:
- [Authoritative source](https://example.org)
```

## Link Philosophy

Use Obsidian links for human navigation:

```markdown
[[Complex Number]]
[[Real Number]]
[[Exponential Function]]
[[Euler's Formula]]
[[Fourier Transform]]
```

Structured node records use stable IDs behind the scenes:

```yaml
related:
  - concept.complex-number
  - concept.exponential-function
  - formula.euler
```

## Starter Entries

## Euler's Formula

An identity connecting complex exponentials with sine and cosine:

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

Type: `formula`
Domain: [[Complex Analysis]]
Status: `established`

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

## Mellin Transform

An integral transform that represents a suitable function in terms of multiplicative scale rather than additive frequency.

Related concepts:
- [[Multiplicative Structure]]
- [[Scale Invariance]]
- [[Fourier Transform]]
- [[Laplace Transform]]
- [[Dirichlet Series]]
- [[Riemann Zeta Function]]

Future deep links:
- [[Mellin Kernel]]
- [[Asymptotic Analysis]]
- [[Scale Transform]]
