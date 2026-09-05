# Formula Registry

This registry is an index of formulas, formula families, and formula bonds that appear
across this mathematics workspace.

It deliberately does not reproduce the formulas themselves. Each entry points to the
current source note and, where useful, suggests a future one-page-per-formula location.

This means the registry has a different job from the bond pages:

| Page type | Purpose |
|---|---|
| Registry | Help the reader find a formula or choose a learning route |
| Formula page | Explain one formula in depth |
| Bond page | Explain why two or more formulas belong together |

Think of this page as the map at the entrance to a museum. It tells you which exhibits
exist, where they currently live, and which rooms should eventually become dedicated
formula pages. It is intentionally light on derivation so that the registry stays
useful as the collection grows.

If you are learning the material for the first time, start with the "Existing Bond
Pages" section near the bottom. Those pages introduce the elements and explain why the
formulas belong together. Then return here to choose an individual formula for deeper
study.

Companion pages:

- [Formula Genealogy: From Prime Counting To Zeta, And Back Again](formula-genealogy-zeta-to-primes.md)
- [Formulas Linked To Prime Numbers](formulas-linked-to-prime-numbers.md)
- [Dedicated Formula Pages](formulas/README.md)
- [Formula Bonds](formula-bonds/README.md)
- [Mathematical Fundamentals](Mathematical%20fundamentals.md)
- [Repository Stewardship Review](repository-stewardship-review.md)

---

## Registry Convention

Suggested future formula pages should live under:

```text
formulas/
```

Suggested future bond pages should live under:

```text
formula-bonds/
```

Use this registry as the table of contents, not as the place where formula derivations
accumulate. A good formula page should eventually explain:

- what the formula measures or transforms;
- which mathematical objects it connects;
- what obstacle it removes;
- what assumptions or convergence conditions it needs;
- which adjacent formulas it bonds to.

When adding to this registry, prefer the reader's path over encyclopedic completeness.
An entry is useful when it answers: "What is this object, where can I learn more, and
what page should eventually hold its dedicated explanation?"

---

## Learning Routes

Use these routes when you want a guided path rather than a full catalogue.

| Route | Start here | Then follow |
|---|---|---|
| Geometry and right triangles | [Pythagorean Theorem](formulas/pythagorean-theorem.md) | Right triangle, hypotenuse, square, square root, distance |
| Waves and circular motion | [Cosine Function](formulas/cosine-function.md) | Unit circle, period, zeros, phasor, Euler's formula |
| Local approximation | [Taylor Series](formulas/taylor-series.md) | Derivative, polynomial, Maclaurin series, asymptotic formula |
| Divergence and limits | [Divergence, Partial Sums, And Indeterminate Quotients](formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md) | Harmonic series, prime reciprocal series, partial sums, L'Hopital's rule |
| Fractions and approximation | [Farey Neighbors, Fibonacci Ratios, And The Golden Ratio](formula-bonds/farey-fibonacci-golden-ratio.md) | Farey determinant condition, Stern-Brocot mediant, golden-ratio continued fraction |
| Number-system extension | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md) | Binet's formula, square root of 5, Euler's number, Euler's formula |
| Prime distribution | [Formula Genealogy](formula-genealogy-zeta-to-primes.md) | Prime-counting function, Euler product, von Mangoldt function, Riemann explicit formula |
| Zeta experiments | [Zeta Phase Coordinate Analysis](zeta-phase-coordinate-analysis.md) | Zeta phase identity, unity-circle coordinate, unfolded zero spacing |
| Constants as process signatures | [Mathematical Constants As Process Invariants](constants-as-process-invariants-proposal.md) | Golden ratio, pi, Euler's number, square root of 5, Euler-Mascheroni constant |
| Inverse exponential forms | [Lambert W Function](formulas/lambert-w-function.md) | Lambert W function, second real branch, Omega constant |

Each route is a reading suggestion, not a dependency chain. The goal is to keep the
reader oriented: first see the story, then inspect the individual formulas.

---

## Foundational Geometry

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Pythagorean theorem | Right-triangle distance law | [Pythagorean Theorem](formulas/pythagorean-theorem.md) | `formulas/pythagorean-theorem.md` |

---

## Approximation And Expansion

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Taylor series | Local polynomial expansion | [Taylor Series](formulas/taylor-series.md) | `formulas/taylor-series.md` |
| L'Hopital's rule | Indeterminate-limit method | [L'Hopital's Rule](formulas/lhopitals-rule.md) | `formulas/lhopitals-rule.md` |

---

## Series, Divergence, And Limits

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Harmonic series | Divergent reciprocal series | [Harmonic And Prime Reciprocal Series](formulas/harmonic-and-prime-reciprocal-series.md) | `formulas/harmonic-and-prime-reciprocal-series.md` |
| Prime reciprocal series | Euler divergence theorem | [Harmonic And Prime Reciprocal Series](formulas/harmonic-and-prime-reciprocal-series.md) | `formulas/harmonic-and-prime-reciprocal-series.md` |
| Series summing to one | Convergence examples | [Series That Sum To One](formulas/series-that-sum-to-one.md) | `formulas/series-that-sum-to-one.md` |
| Divergence and indeterminate quotients | Formula bond | [Divergence, Partial Sums, And Indeterminate Quotients](formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md) | `formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md` |

---

## Waves And Circular Motion

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Cosine function | Periodic wave / unit-circle coordinate | [Cosine Function](formulas/cosine-function.md) | `formulas/cosine-function.md` |

---

## Prime Distribution Core

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Prime-counting function | Counting object | [Prime-Counting Formula](formulas-linked-to-prime-numbers.md#1-prime-counting-formula) | `formulas/prime-counting-function.md` |
| Prime number theorem density law | Asymptotic law | [Prime Number Theorem And Density Formulas](formulas-linked-to-prime-numbers.md#2-prime-number-theorem-and-density-formulas) | `formulas/prime-number-theorem-density.md` |
| Logarithmic integral approximation | Analytic approximation | [Prime Number Theorem And Density Formulas](formulas-linked-to-prime-numbers.md#2-prime-number-theorem-and-density-formulas) | `formulas/logarithmic-integral-prime-approximation.md` |
| Legendre prime-counting approximation | Historical approximation | [Prime Number Theorem And Density Formulas](formulas-linked-to-prime-numbers.md#2-prime-number-theorem-and-density-formulas) | `formulas/legendre-prime-counting-approximation.md` |
| Chebyshev prime-power function | Weighted counting object | [Chebyshev Prime-Power Formula](formulas-linked-to-prime-numbers.md#5-chebyshev-prime-power-formula) | `formulas/chebyshev-prime-power-function.md` |
| Riemann explicit formula | Structural formula | [Riemann Explicit Formula](formulas-linked-to-prime-numbers.md#6-riemann-explicit-formula) | `formulas/riemann-explicit-formula.md` |
| Riemann Hypothesis error-bound form | Normalisation principle | [Riemann Hypothesis as an Error-Bound Normalisation](history-of-prime-distribution-analytics.md#22-riemann-hypothesis-as-an-error-bound-normalisation) | `formulas/riemann-hypothesis-error-bound.md` |

---

## Zeta And Transform Machinery

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Riemann zeta function | Analytic encoding | [Zeta function](Mathematical%20fundamentals.md#zeta-function) | `formulas/riemann-zeta-function.md` |
| Euler product | Prime encoding | [Euler Product Formula](formulas-linked-to-prime-numbers.md#3-euler-product-formula) | `formulas/euler-product.md` |
| Logarithmic derivative of zeta | Transform | [Logarithmic Derivative Formula](formulas-linked-to-prime-numbers.md#4-logarithmic-derivative-formula) | `formulas/zeta-logarithmic-derivative.md` |
| Von Mangoldt function | Prime-power signal | [From -zeta'/zeta To Lambda(n)](formula-genealogy-zeta-to-primes.md#von-mangoldt) | `formulas/von-mangoldt-function.md` |
| Dirichlet L-function | Arithmetic progression encoding | [Dirichlet L-function](Mathematical%20fundamentals.md#dirichlet-l-function) | `formulas/dirichlet-l-function.md` |
| Euler totient normalisation | Residue-class normalisation | [History of Prime Distribution Analytics](history-of-prime-distribution-analytics.md) | `formulas/euler-totient-normalisation.md` |

---

## Prime-Generating And Prime-Representing Formulas

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Wilson-theorem prime formula | Exact generator/test hybrid | [Wilson-Theorem Prime Formula](formulas-linked-to-prime-numbers.md#7-wilson-theorem-prime-formula) | `formulas/wilson-theorem-prime-formula.md` |
| Willans formula for the nth prime | Exact nth-prime formula | [Willans' Formula For The nth Prime](formulas-linked-to-prime-numbers.md#8-willans-formula-for-the-nth-prime) | `formulas/willans-nth-prime-formula.md` |
| J. P. Jones Wilson-based formula | Exact Wilson-derived formula | [J. P. Jones' Shorter Wilson-Based Formula](formulas-linked-to-prime-numbers.md#9-j-p-jones-shorter-wilson-based-formula) | `formulas/jones-wilson-prime-formula.md` |
| Gandhi recurrence | Recursive prime formula | [Gandhi's Recurrence Formula](formulas-linked-to-prime-numbers.md#10-gandhis-recurrence-formula) | `formulas/gandhi-prime-recurrence.md` |
| Golomb zeta recurrence | Recursive prime formula | [Golomb's Zeta Recurrence](formulas-linked-to-prime-numbers.md#11-golombs-zeta-recurrence) | `formulas/golomb-zeta-recurrence.md` |
| Continued-fraction prime-representing constant | Encoded prime constant | [Continued-Fraction Prime-Representing Constant](formulas-linked-to-prime-numbers.md#12-continued-fraction-prime-representing-constant) | `formulas/continued-fraction-prime-constant.md` |
| Fridman-type prime-representing constant | Encoded prime constant | [Fridman-Type Prime-Representing Constant](formulas-linked-to-prime-numbers.md#13-fridman-type-prime-representing-constant) | `formulas/fridman-type-prime-constant.md` |
| Mills formula | Conditional prime generator | [Mills' Formula](formulas-linked-to-prime-numbers.md#14-mills-formula) | `formulas/mills-prime-formula.md` |
| Wright formula | Prime-representing formula | [Wright's Formula](formulas-linked-to-prime-numbers.md#15-wrights-formula) | `formulas/wright-prime-formula.md` |
| Plouffe formulas | Digit/constant-based prime encodings | [Plouffe's Formulas](formulas-linked-to-prime-numbers.md#16-plouffes-formulas) | `formulas/plouffe-prime-formulas.md` |
| Polynomial prime-producing formulas | Finite-run generators | [Polynomial Formulas Producing Many Primes](formulas-linked-to-prime-numbers.md#17-polynomial-formulas-producing-many-primes) | `formulas/polynomial-prime-producers.md` |
| Arithmetic progression prime runs | Structured prime runs | [Arithmetic Progression Prime Runs](formulas-linked-to-prime-numbers.md#18-arithmetic-progression-prime-runs) | `formulas/arithmetic-progression-prime-runs.md` |
| Rowland sequence | Prime-generating sequence | [Rowland's Prime-Generating Sequence](formulas-linked-to-prime-numbers.md#19-rowlands-prime-generating-sequence) | `formulas/rowland-prime-generating-sequence.md` |
| Diophantine prime-describing system | Logical/arithmetic encoding | [Diophantine Prime-Describing System](formulas-linked-to-prime-numbers.md#20-diophantine-prime-describing-system) | `formulas/diophantine-prime-system.md` |

---

## Prime Gaps, Correlations, And Statistics

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Mean prime gap estimate | Statistical scale | [Prime gaps](history-of-prime-distribution-analytics.md#xi-prime-gaps) | `formulas/mean-prime-gap.md` |
| Extreme prime gap estimate | Statistical scale | [Prime gaps](history-of-prime-distribution-analytics.md#xi-prime-gaps) | `formulas/extreme-prime-gap.md` |
| Hardy-Littlewood prime tuple heuristic | Correlation model | [Hardy-Littlewood](history-of-prime-distribution-analytics.md#xii-hardylittlewood) | `formulas/hardy-littlewood-prime-tuple-heuristic.md` |
| Cramer model | Probabilistic model | [History of Prime Distribution Analytics](history-of-prime-distribution-analytics.md) | `formulas/cramer-prime-model.md` |
| Singular series | Local correction factor | [Singular series](Mathematical%20fundamentals.md#singular-series) | `formulas/singular-series.md` |
| Pair correlation | Zero statistics | [Pair correlation](Mathematical%20fundamentals.md#pair-correlation) | `formulas/pair-correlation.md` |
| Unfolded zero spacing | Normalised statistic | [Zero ordinates to unfolded zero spacings](history-of-prime-distribution-analytics.md#10-zero-ordinates--unfolded-zero-spacings) | `formulas/unfolded-zero-spacing.md` |

---

## Zeta Zero Experiments

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Zeta phase identity | Experimental coordinate formula | [Phase Identity](zeta-phase-coordinate-analysis.md#phase-identity) | `formulas/zeta-phase-identity.md` |
| Unity-circle coordinate | Coordinate mapping | [Unity-Circle Coordinate](zeta-phase-coordinate-analysis.md#unity-circle-coordinate) | `formulas/zeta-unity-circle-coordinate.md` |
| Smoothness diagnostics | Diagnostic family | [Smoothness Diagnostics](zeta-phase-coordinate-analysis.md#smoothness-diagnostics) | `formulas/zeta-smoothness-diagnostics.md` |
| Riemann-Siegel prime geometry | Interpretive geometry | [Riemann-Siegel Prime Geometry](zeta-phase-coordinate-analysis.md#riemann-siegel-prime-geometry) | `formulas/riemann-siegel-prime-geometry.md` |
| Zeta zero spacing baseline trend | Statistical baseline | [Known Baseline Trend](zeta-zero-spacing-scaling-analysis-context.md#3-known-baseline-trend) | `formulas/zeta-zero-spacing-baseline-trend.md` |
| Zeta spacing phase structures | Candidate model family | [Candidate Phase Structures](zeta-zero-spacing-scaling-analysis-context.md#5-candidate-phase-structures) | `formulas/zeta-spacing-phase-structures.md` |
| Zeta spacing amplitude envelopes | Candidate model family | [Candidate Amplitude Envelopes](zeta-zero-spacing-scaling-analysis-context.md#6-candidate-amplitude-envelopes) | `formulas/zeta-spacing-amplitude-envelopes.md` |
| `sqrt(2) pi^2` scale | Experimental scale constant | [Zeta Zero Spacing Scaling Analysis Context](zeta-zero-spacing-scaling-analysis-context.md) | `formulas/sqrt2-pi2-zeta-spacing-scale.md` |

---

## Constants And Process Invariants

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Golden ratio | Recurrence invariant | [phi: self-similar recurrence](constants-as-process-invariants-proposal.md#phi-self-similar-recurrence) | `formulas/golden-ratio.md` |
| Pi | Rotational invariant | [pi: circular proportion and rotational closure](constants-as-process-invariants-proposal.md#pi-circular-proportion-and-rotational-closure) | `formulas/pi-rotational-invariant.md` |
| Euler's number | Continuous-change invariant | [e: self-consistent continuous change](constants-as-process-invariants-proposal.md#e-self-consistent-continuous-change) | `formulas/e-continuous-change-invariant.md` |
| Natural logarithm | Inverse exponential / growth measure | [Natural logarithm](Mathematical%20fundamentals.md#natural-logarithm) | `formulas/natural-logarithm.md` |
| Euler's formula | Rotation/complex bridge | [Euler's formula](Mathematical%20fundamentals.md#eulers-formula) | `formulas/eulers-formula.md` |
| Euler's identity | Constant unification | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md#8-eulers-formula-extends-the-pattern) | `formulas/eulers-identity.md` |
| Imaginary unit rotation | Orthogonal transformation | [Multiplication by i](Mathematical%20fundamentals.md#multiplication-by-i) | `formulas/imaginary-unit-rotation.md` |
| Square root of 2 | Incommensurability signature | [sqrt(2): incommensurability](constants-as-process-invariants-proposal.md#sqrt2-incommensurability) | `formulas/sqrt2-incommensurability.md` |
| Square root of one half | Exact radical value | [Square Root Of One Half](formulas/sqrt-one-half.md) | `formulas/sqrt-one-half.md` |
| Square root of 5 | Fibonacci mode separator | [sqrt(5): separation of Fibonacci modes](constants-as-process-invariants-proposal.md#sqrt5-separation-of-fibonacci-modes) | `formulas/sqrt5-fibonacci-mode-separation.md` |
| Apéry's constant | Infinite aggregation signature | [zeta(3): infinite aggregation under cubic decay](constants-as-process-invariants-proposal.md#zeta3-infinite-aggregation-under-cubic-decay) | `formulas/aperys-constant-zeta3.md` |
| Euler-Mascheroni constant | Residual growth constant | [gamma: residual between harmonic accumulation and logarithmic growth](constants-as-process-invariants-proposal.md#gamma-residual-between-harmonic-accumulation-and-logarithmic-growth) | `formulas/euler-mascheroni-constant.md` |
| Natural logarithm of 2 | Doubling threshold | [ln(2): doubling threshold under continuous change](constants-as-process-invariants-proposal.md#ln2-doubling-threshold-under-continuous-change) | `formulas/ln2-doubling-threshold.md` |
| Omega constant | Fixed point of exponential multiplication | [Lambert W Function](formulas/lambert-w-function.md#omega-constant) | `formulas/omega-constant.md` |

---

## Inverse Exponential Forms

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Lambert W function | Inverse special function | [Lambert W Function](formulas/lambert-w-function.md) | `formulas/lambert-w-function.md` |
| Lambert W principal branch | Principal branch | [Lambert W Function](formulas/lambert-w-function.md#lambert-w-real-branches) | `formulas/lambert-w-principal-branch.md` |
| Lambert W second real branch | Lower real branch | [Lambert W Function](formulas/lambert-w-function.md#lambert-w-second-real-branch) | `formulas/lambert-w-second-real-branch.md` |
| Lambert W parametric example | Branch-safe exact example | [Lambert W Function](formulas/lambert-w-function.md#lambert-w-parametric-example) | `formulas/lambert-w-parametric-example.md` |
| Lambert W branch point | Real branch meeting point | [Lambert W Function](formulas/lambert-w-function.md#lambert-w-branch-point) | `formulas/lambert-w-branch-point.md` |

---

## Fibonacci, Farey, And Rational Approximation

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Fibonacci recurrence | Recurrence relation | [Fibonacci: Recursive, Iterative, Accumulative, Stateful](constants-as-process-invariants-proposal.md#fibonacci-recursive-iterative-accumulative-stateful) | `formulas/fibonacci-recurrence.md` |
| Binet's formula | Closed form for recurrence | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md#4-binets-formula) | `formulas/binets-formula.md` |
| Fibonacci matrix | State transformation | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md#6-a-second-view-the-fibonacci-matrix) | `formulas/fibonacci-matrix.md` |
| Fibonacci nearest-integer formula | Dominant-mode approximation | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md#5-where-the-irrational-numbers-come-from) | `formulas/fibonacci-nearest-integer-formula.md` |
| Fibonacci ratio limit | Convergence relation | [Why phi emerges from the transition](constants-as-process-invariants-proposal.md#why-phi-emerges-from-the-transition) | `formulas/fibonacci-ratio-limit.md` |
| Farey determinant condition | Neighbor invariant | [The Farey Bond](formula-bonds/farey-fibonacci-golden-ratio.md#4-the-farey-bond) | `formulas/farey-determinant-condition.md` |
| Stern-Brocot mediant | Rational construction | [Stern-Brocot And Continued Fractions](formula-bonds/farey-fibonacci-golden-ratio.md#6-stern-brocot-and-continued-fractions) | `formulas/stern-brocot-mediant.md` |
| Golden-ratio continued fraction | Continued fraction | [Stern-Brocot And Continued Fractions](formula-bonds/farey-fibonacci-golden-ratio.md#6-stern-brocot-and-continued-fractions) | `formulas/golden-ratio-continued-fraction.md` |

---

## Geometry, Phase, And Vortex Proposals

| Entry | Kind | Current source | Suggested page |
|---|---|---|---|
| Circle radius formulas | Elementary geometry | [Radius](Mathematical%20fundamentals.md#radius) | `formulas/circle-radius.md` |
| Phasor representation | Complex signal encoding | [Phasor](Mathematical%20fundamentals.md#phasor) | `formulas/phasor-representation.md` |
| Five-coordinate vortex kernel | Coordinate model | [Five-Coordinate Kernel](vortex-discrete-continuous-mapping-proposal.md#five-coordinate-kernel) | `formulas/five-coordinate-vortex-kernel.md` |
| Continuous dual-helix expression | Continuous geometry | [Continuous Dual-Helix Expression](vortex-discrete-continuous-mapping-proposal.md#continuous-dual-helix-expression) | `formulas/continuous-dual-helix-expression.md` |
| Discrete dual-helix expression | Discrete geometry | [Discrete Dual-Helix Expression](vortex-discrete-continuous-mapping-proposal.md#discrete-dual-helix-expression) | `formulas/discrete-dual-helix-expression.md` |
| Mediator transform table | Translation structure | [Mediator Transform Table](vortex-discrete-continuous-mapping-proposal.md#mediator-transform-table) | `formulas/mediator-transform-table.md` |
| 5x5 function matrix | Relationship matrix | [The 5x5 Function Matrix](vortex-discrete-continuous-mapping-proposal.md#the-5x5-function-matrix) | `formulas/5x5-function-matrix.md` |
| Phase-indexed radial walk | Sequence visualisation | [Phase-indexed radial walk](chats/phase-indexed%20radial%20walk%20mathematical%20object.md#1-one-coordinate-system-for-both-sequences) | `formulas/phase-indexed-radial-walk.md` |
| Sequence residual comparison | Diagnostic relation | [Define the residual](chats/fibo-prime%20relationship.md#4-now-define-the-residual) | `formulas/sequence-residual-comparison.md` |

---

## Existing Bond Pages

| Bond | Current page |
|---|---|
| Binet's formula, Euler's number, and number-system extension | [Binet's Formula, Euler's Number, And Number-System Extension](formula-bonds/binet-euler-number-systems.md) |
| Divergence, partial sums, and indeterminate quotients | [Divergence, Partial Sums, And Indeterminate Quotients](formula-bonds/divergence-partial-sums-and-indeterminate-quotients.md) |
| Farey neighbors, Fibonacci ratios, and the golden ratio | [Farey Neighbors, Fibonacci Ratios, And The Golden Ratio](formula-bonds/farey-fibonacci-golden-ratio.md) |

---

## Candidate Next Formula Pages

These are good first candidates because they are central, repeated across the repo, and
already have enough source material for dedicated pages:

| Priority | Formula page |
|---|---|
| 1 | `formulas/prime-counting-function.md` |
| 2 | `formulas/euler-product.md` |
| 3 | `formulas/zeta-logarithmic-derivative.md` |
| 4 | `formulas/von-mangoldt-function.md` |
| 5 | `formulas/riemann-explicit-formula.md` |
| 6 | `formulas/fibonacci-ratio-limit.md` |
| 7 | `formulas/farey-determinant-condition.md` |
| 8 | `formulas/binets-formula.md` |
| 9 | `formulas/fibonacci-matrix.md` |
| 10 | `formulas/fibonacci-nearest-integer-formula.md` |
| 11 | `formulas/lambert-w-second-real-branch.md` |
| 12 | `formulas/lambert-w-branch-point.md` |
