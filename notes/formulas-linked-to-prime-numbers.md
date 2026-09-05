# Formulas Linked To Prime Numbers

Source spine: Wikipedia, ["Formula for primes"](https://en.wikipedia.org/wiki/Formula_for_primes),
accessed 2026-08-25.

This page is a companion to [Formula Genealogy: From Prime Counting To Zeta, And Back Again](formula-genealogy-zeta-to-primes.md).
For a repo-wide navigation layer without reproducing formulas, see the
[Formula Registry](formula-registry.md).
The genealogy explains why analytic number theory transforms

$$
\pi(x)\rightarrow \zeta(s)\rightarrow -\frac{\zeta'}{\zeta}(s)\rightarrow \Lambda(n)\rightarrow \psi(x)
$$

and then returns to prime counting through Riemann's explicit formula. This page collects
formulas that are directly linked to primes: formulas that generate primes, define primes,
count primes, encode primes, or describe their distribution.

The key distinction is:

- Some formulas are useful analytic structure, such as the Euler product or explicit formula.
- Some formulas are exact but computationally inefficient, such as Wilson/Willans formulas.
- Some formulas generate primes only after hiding prime information inside a constant.
- Some formulas are existential or logical characterisations rather than practical generators.

---

## 1. Prime-Counting Formula

The basic counting function is:

$$
\pi(x)=\#\{p\le x:p\text{ is prime}\}.
$$

It counts primes directly. It is the original object behind the prime number theorem and
Riemann's paper.

Genealogy link: [The Original Object: Counting Primes](formula-genealogy-zeta-to-primes.md#counting-primes).

---

## 2. Prime Number Theorem And Density Formulas

The coarse density law is:

$$
\pi(x)\sim \frac{x}{\log x}.
$$

The logarithmic-integral approximation is:

$$
\pi(x)\sim \operatorname{Li}(x)
=\int_2^x\frac{dt}{\log t}.
$$

Legendre's approximation was of the form:

$$
\pi(x)\approx \frac{x}{\log x-A},
$$

with a fitted constant near `1.08366`.

These are not prime-generating formulas. They describe the large-scale density of primes.

Genealogy link: [Riemann's Transformation](formula-genealogy-zeta-to-primes.md#riemann-explicit-formula).

---

## 3. Euler Product Formula

Euler's product connects primes to the zeta function:

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}
=\prod_p\frac1{1-p^{-s}},
\qquad \Re(s)>1.
$$

This is one of the most important prime formulas, even though it does not output primes
one by one. It encodes all primes inside an analytic object.

Genealogy link: [Euler's Transformation: Primes Become A Product](formula-genealogy-zeta-to-primes.md#euler-product).

---

## 4. Logarithmic Derivative Formula

From the Euler product:

$$
-\frac{\zeta'}{\zeta}(s)
=\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s},
\qquad \Re(s)>1.
$$

where

$$
\Lambda(n)=
\begin{cases}
\log p, & n=p^k,\ k\ge1,\\
0, & \text{otherwise}.
\end{cases}
$$

This is a prime-power detector in Dirichlet-series form.

Genealogy links:

- [From zeta(s) To -zeta'/zeta](formula-genealogy-zeta-to-primes.md#log-derivative)
- [From -zeta'/zeta To Lambda(n)](formula-genealogy-zeta-to-primes.md#von-mangoldt)

---

## 5. Chebyshev Prime-Power Formula

Chebyshev's function is:

$$
\psi(x)=\sum_{n\le x}\Lambda(n)
=\sum_{p^k\le x}\log p.
$$

It counts prime powers with logarithmic weight. It is not the same as `pi(x)`, but it is
far better adapted to zeta.

Genealogy link: [From Lambda(n) To psi(x)](formula-genealogy-zeta-to-primes.md#chebyshev-psi).

---

## 6. Riemann Explicit Formula

A modern explicit formula for `psi` is:

$$
\psi_0(x)
=
x
-
\sum_\rho\frac{x^\rho}{\rho}
-
\log(2\pi)
-
\frac12\log(1-x^{-2}),
\qquad x>1.
$$

Here `rho` runs over the non-trivial zeros of `zeta(s)`.

Riemann's related formula for the weighted prime-power counting function is:

$$
J(x)
=
\operatorname{Li}(x)
-
\sum_\rho\operatorname{Li}(x^\rho)
-
\log 2
+
\int_x^\infty
\frac{dt}{t(t^2-1)\log t}.
$$

This is not a generator in the elementary sense. It is a structural formula: prime
distribution is expressed through zeta's pole and zeros.

Genealogy link: [From psi(x) Back To pi(x)](formula-genealogy-zeta-to-primes.md#back-to-pi).

---

## 7. Wilson-Theorem Prime Formula

Wikipedia's first elementary example is based on Wilson's theorem:

$$
f(n)=
\left\lfloor
\frac{n!\bmod(n+1)}{n}
\right\rfloor(n-1)+2.
$$

For positive integers `n`, this outputs primes, mostly `2`, with `n+1` appearing when
`n+1` is prime.

The reason is Wilson's theorem:

$$
n+1\text{ is prime}
\iff
n!\equiv n\pmod{n+1}.
$$

What kind of formula is this?

It is an exact primality-test formula disguised as a generator. It is not efficient,
because factorials modulo `n+1` are expensive compared with ordinary prime tests.

Wikipedia deep link:
[Formulas based on Wilson's theorem](https://en.wikipedia.org/wiki/Formula_for_primes#Formulas_based_on_Wilson's_theorem).

---

## 8. Willans' Formula For The nth Prime

Willans gave the exact formula:

$$
p_n
=1+\sum_{i=1}^{2^n}
\left\lfloor
\left(
\frac{n}{
\sum_{j=1}^{i}
\left\lfloor
\left(
\cos\frac{(j-1)!+1}{j}\pi
\right)^2
\right\rfloor}
\right)^{1/n}
\right\rfloor.
$$

This formula uses Wilson's theorem inside a cosine/floor expression to detect primes.
Wikipedia notes that it reduces to the tautological form:

$$
p_n=1+\sum_{i=1}^{2^n}[\pi(i)<n].
$$

What kind of formula is this?

It is exact, but it depends on a hidden primality detector and is computationally poor.
It is valuable as a logical construction, not as a practical generator.

Wikipedia deep link:
[Formulas based on Wilson's theorem](https://en.wikipedia.org/wiki/Formula_for_primes#Formulas_based_on_Wilson's_theorem).

---

## 9. J. P. Jones' Shorter Wilson-Based Formula

Jones gave a shorter nth-prime formula using the monus operation:

$$
p_n=
\sum_{i=0}^{n^2}
\left(
1\dotminus
\left(
\left(\sum_{j=0}^{i}(j\dotminus1)!^2\bmod j\right)
\dotminus n
\right)
\right).
$$

Here

$$
a\dotminus b=\max(a-b,0).
$$

What kind of formula is this?

It is another exact arithmetic construction. Like Willans' formula, it is more a
demonstration of definability than an efficient computational method.

Wikipedia deep link:
[Formulas based on Wilson's theorem](https://en.wikipedia.org/wiki/Formula_for_primes#Formulas_based_on_Wilson's_theorem).

---

## 10. Gandhi's Recurrence Formula

Gandhi's formula is:

$$
p_n=
\left\lfloor
1-\log_2\left(s_{n-1}-\frac12\right)
\right\rfloor,
$$

where

$$
s_n=
\sum_{d\mid p_n\#}
\frac{\mu(d)}{2^d-1}.
$$

Here `p_n#` is the primorial:

$$
p_n\#=p_1p_2\cdots p_n.
$$

What kind of formula is this?

It is a recurrence: it gives `p_n` using earlier primes. It depends on sieve logic and
the Möbius function.

Wikipedia deep link:
[Gandhi's formula](https://en.wikipedia.org/wiki/Formula_for_primes#Gandhi's_formula).

---

## 11. Golomb's Zeta Recurrence

Golomb's formula is:

$$
p_n=
\lim_{s\to\infty}
\left(
\zeta(s)
\prod_{k=1}^{n-1}(1-p_k^{-s})
-1
\right)^{-1/s}.
$$

What kind of formula is this?

It is a recurrence for the next prime using zeta and the previously known primes. It is
directly based on the Euler product. After removing the known prime factors from zeta,
the first remaining term is controlled by the next prime.

Genealogy link:
[Euler Product Formula](#3-euler-product-formula).

Wikipedia deep link:
[Golomb's formula](https://en.wikipedia.org/wiki/Formula_for_primes#Golomb's_formula).

---

## 12. Continued-Fraction Prime-Representing Constant

Define:

$$
u_1=[p_1,p_2,p_3,\ldots].
$$

Then recursively:

$$
u_{n+1}=(u_n-\lfloor u_n\rfloor)^{-1},
$$

and:

$$
p_n=\lfloor u_n\rfloor.
$$

What kind of formula is this?

It stores the entire prime sequence inside one real number. The formula can recover
primes only because the constant was built from the primes.

Wikipedia deep link:
[Prime-representing constants](https://en.wikipedia.org/wiki/Formula_for_primes#Prime-representing_constants).

---

## 13. Fridman-Type Prime-Representing Constant

Another constant construction uses:

$$
f_n=
\lfloor f_{n-1}\rfloor
\left(f_{n-1}-\lfloor f_{n-1}\rfloor+1\right),
\qquad n\ge2,
$$

with:

$$
p_n=\lfloor f_n\rfloor.
$$

The exact initial value can be represented by a rapidly converging series:

$$
f_1=
\sum_{n=1}^{\infty}
\frac{p_n-1}{p_{n-1}\#}.
$$

What kind of formula is this?

It is another encoding formula. It is exact only when the initial constant is known with
enough precision, and the constant itself is defined using the prime sequence.

Wikipedia deep link:
[Prime-representing constants](https://en.wikipedia.org/wiki/Formula_for_primes#Prime-representing_constants).

---

## 14. Mills' Formula

Mills proved that there exists a real number `A` such that:

$$
\left\lfloor A^{3^n}\right\rfloor
$$

is prime for every positive integer `n`.

What kind of formula is this?

It is an existence formula. The constant `A` depends on deep information about primes.
The smallest such constant is connected to assumptions about prime gaps; Wikipedia notes
that its commonly cited value relies on the Riemann Hypothesis.

Wikipedia deep link:
[Mills' formula](https://en.wikipedia.org/wiki/Formula_for_primes#Mills'_formula).

---

## 15. Wright's Formula

Wright proved the existence of a real number `alpha` such that the sequence:

$$
g_0=\alpha,\qquad g_{n+1}=2^{g_n}
$$

has prime integer parts:

$$
\lfloor g_n\rfloor
=
\left\lfloor 2^{\cdots^{2^{2^\alpha}}}\right\rfloor
$$

for the relevant terms.

What kind of formula is this?

Like Mills' formula, it is existential and constant-dependent. It demonstrates that prime
sequences can be encoded in analytic growth processes, but the useful information is
hidden in the constant.

Wikipedia deep link:
[Wright's formula](https://en.wikipedia.org/wiki/Formula_for_primes#Wright's_formula).

---

## 16. Plouffe's Formulas

Plouffe proposed formulas that generate primes using constants and floor operations.
They belong to the prime-representing-constant family.

What kind of formula is this?

They are encoding formulas: the prime sequence is compressed into numerical constants
and then extracted by arithmetic operations.

Wikipedia deep link:
[Plouffe's formulas](https://en.wikipedia.org/wiki/Formula_for_primes#Plouffe's_formulas).

---

## 17. Polynomial Formulas Producing Many Primes

Euler's famous quadratic is:

$$
n^2+n+41.
$$

It produces primes for:

$$
n=0,1,\ldots,39.
$$

Other polynomials can produce many primes over finite ranges, but no nonconstant
polynomial with integer coefficients can produce only primes for all integer inputs.

What kind of formula is this?

It is a finite-run phenomenon. The polynomial is impressive locally but cannot be a
universal prime generator.

Wikipedia deep link:
[Prime formulas and polynomial functions](https://en.wikipedia.org/wiki/Formula_for_primes#Prime_formulas_and_polynomial_functions).

---

## 18. Arithmetic Progression Prime Runs

Wikipedia gives examples of linear formulas that are prime for long finite stretches,
such as:

$$
224584605939537911+18135696597948930n
$$

for a finite range of `n`.

What kind of formula is this?

It is a finite prime-rich arithmetic progression. Dirichlet's theorem explains that
some arithmetic progressions contain infinitely many primes, but not that every term in
a long interval is prime.

Wikipedia deep link:
[Prime formulas and polynomial functions](https://en.wikipedia.org/wiki/Formula_for_primes#Prime_formulas_and_polynomial_functions).

---

## 19. Rowland's Prime-Generating Sequence

Rowland's recurrence is:

$$
a_n=a_{n-1}+\gcd(n,a_{n-1}),
\qquad a_1=7.
$$

The differences

$$
a_{n+1}-a_n
$$

are always `1` or prime.

What kind of formula is this?

It is a recurrence whose increments reveal primes. It does not list all primes in order,
and Wikipedia notes that it is inefficient compared with direct prime-generating
algorithms.

Wikipedia deep link:
[Rowland's prime-generating sequence](https://en.wikipedia.org/wiki/Formula_for_primes#Rowland's_prime-generating_sequence).

---

## 20. Diophantine Prime-Describing System

By Matiyasevich's theorem, computably enumerable sets can be represented
Diophantinely. Jones and collaborators gave an explicit system of 14 Diophantine
equations in 26 variables such that `k+2` is prime exactly when the system has a
solution in nonnegative integers.

The associated polynomial inequality has the form:

$$
(k+2)(1-\alpha_0^2-\alpha_1^2-\cdots-\alpha_{13}^2)>0.
$$

As the variables range over nonnegative integers, the positive values taken by this
expression are exactly the primes.

What kind of formula is this?

It is a logical/Diophantine characterisation of the set of primes. It is exact, profound,
and wildly impractical as a way to compute primes.

Wikipedia deep link:
[Prime-describing system of Diophantine equations](https://en.wikipedia.org/wiki/Formula_for_primes#Prime-describing_system_of_Diophantine_equations).

---

## 21. Comparison Table

| Formula family | Main expression | Produces primes? | Depends on previous primes? | Practical? | Conceptual role |
|---|---:|---:|---:|---:|---|
| `pi(x)` | `# {p <= x}` | Counts | No | Yes, as definition | Original counting problem |
| PNT | `x/log x`, `Li(x)` | Estimates | No | Yes | Density law |
| Euler product | `zeta(s)=prod_p(1-p^-s)^-1` | Encodes | No | Yes | Prime-to-analysis bridge |
| Log derivative | `-zeta'/zeta=sum Lambda(n)n^-s` | Detects prime powers | No | Yes | Local prime signal |
| `psi(x)` | `sum_{n<=x} Lambda(n)` | Counts weighted prime powers | No | Yes | Zeta-compatible counting |
| Explicit formula | `x - sum_rho x^rho/rho + ...` | Describes distribution | No | Analytic | Zeros explain fluctuations |
| Wilson | factorial congruence | Yes, with many repeats | No | No | Exact primality detector |
| Willans | floor/cos/factorial sum | nth prime | No | No | Exact but tautological |
| Jones | monus/factorial/mod sum | nth prime | No | No | Short exact construction |
| Gandhi | Möbius/primorial recurrence | nth prime | Yes | No | Sieve recurrence |
| Golomb | zeta limit recurrence | nth prime | Yes | No | Euler-product recurrence |
| Prime constants | continued fraction / series | Yes | Encoded in constant | No | Information storage |
| Mills/Wright | floor of fast powers | Yes | Hidden in constant | No | Existence/encoding |
| Polynomials | e.g. `n^2+n+41` | Finite runs | No | Limited | Prime-rich patterns |
| Rowland | `a_n=a_{n-1}+gcd(n,a_{n-1})` | Some prime increments | No | No | Recurrence curiosity |
| Diophantine | polynomial inequality | Exact set | No | No | Definability of primes |

---

## 22. Map Back To The Formula Genealogy

The prime formulas fall into three evolutionary layers:

1. Direct counting and density:

```text
pi(x), x/log x, Li(x)
```

These belong to the original prime-distribution question.

2. Analytic encoding:

```text
Euler product, -zeta'/zeta, Lambda(n), psi(x), explicit formula
```

These are the main genealogy from primes to zeta and back.

3. Exact generators and encodings:

```text
Wilson, Willans, Jones, Gandhi, Golomb, Mills, Wright, Plouffe, Rowland, Diophantine systems
```

These show that "a formula for primes" can mean many different things. Some are exact
but computationally useless; some are elegant encodings; some are logical existence
theorems. The Riemann-zeta genealogy is different because it explains the structure of
prime distribution rather than merely outputting primes.
