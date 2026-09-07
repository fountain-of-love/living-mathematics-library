# Formula Genealogy: From Prime Counting To Zeta, And Back Again

This note gives a formula genealogy for the analytic theory of prime distribution.
It has two complementary directions.

The historical motivation runs roughly as:

```text
observed prime distribution
  -> prime-counting function pi(x)
  -> asymptotic density guesses by Gauss and Legendre
  -> Euler's zeta product
  -> Riemann's complex zeta function
  -> explicit formula and zero oscillations
```

The analytic derivation usually runs in the reverse technical direction:

```text
zeta(s)
  -> -zeta'(s)/zeta(s)
  -> von Mangoldt function Lambda(n)
  -> Chebyshev function psi(x)
  -> explicit formula
  -> pi(x)
  -> Riemann-zero normalisation
```

The purpose of this genealogy is to show why each transformation is introduced.
Each new object is not merely historical decoration; it removes a specific obstacle in
understanding prime distribution.

Companion page: [Formulas Linked To Prime Numbers](formulas-linked-to-prime-numbers.md)
catalogues prime-generating, prime-counting, prime-encoding, and prime-describing
formulas, using Wikipedia's ["Formula for primes"](https://en.wikipedia.org/wiki/Formula_for_primes)
as its source spine.

Registry page: [Formula Registry](../formula-registry.md).

Related formula-bond notes live in [Formula Bonds](formula-bonds/README.md), starting
with [Farey Neighbors, Fibonacci Ratios, And The Golden Ratio](formula-bonds/farey-fibonacci-golden-ratio.md).

---

<a id="counting-primes"></a>

## 1. The Original Object: Counting Primes

The direct object of interest is the prime-counting function:

$$
\pi(x)=\#\{p\le x:p\text{ is prime}\}
$$

Here `pi(x)` is just conventional notation for the prime-counting function. It has
nothing to do with the circle constant

$$
\pi=3.14159\ldots
$$

The notation is read as "pi of x", meaning "the number of primes up to x".
Equivalently, one could define

$$
P(x)=\#\{p\le x:p\text{ is prime}\}
$$

and the mathematics would be unchanged.

Related catalogue entry:
[Prime-Counting Formula](formulas-linked-to-prime-numbers.md#1-prime-counting-formula).

Modern references define

$$
\pi(x)=\sum_{p\le x}1
$$

The historical problem was that primes look irregular locally but statistically regular
at large scale. Gauss and Legendre both studied this regularity. In modern notation,
their central asymptotic insight is:

$$
\pi(x)\sim \frac{x}{\log x}
$$

Gauss refined this toward the logarithmic integral:

$$
\pi(x)\sim \operatorname{Li}(x)
=\int_2^x\frac{dt}{\log t}
$$

Legendre proposed an approximation of the form:

$$
\pi(x)\approx \frac{x}{\log x-A}
$$

with a fitted constant near `1.08366`.

The obstacle:

`pi(x)` is natural, but it is jagged. It jumps by 1 at primes and is flat elsewhere.
It is hard to attack directly with analysis.

---

<a id="euler-product"></a>

## 2. Euler's Transformation: Primes Become A Product

Euler's decisive insight was that primes can be encoded through all integers.
In *Variae observationes circa series infinitas*, written in 1737 and published in
1744, Euler introduced product expansions connecting infinite series with primes.

Related catalogue entry:
[Euler Product Formula](formulas-linked-to-prime-numbers.md#3-euler-product-formula).

The modern Euler product is:

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}
=\prod_p\frac{1}{1-p^{-s}},
\qquad \Re(s)>1
$$

Why introduce this?

Because the left side is a smooth analytic object, while the right side remembers the
primes. The bridge is unique factorisation:

$$
n=p_1^{a_1}\cdots p_k^{a_k}
$$

For each prime,

$$
\frac{1}{1-p^{-s}}
=1+p^{-s}+p^{-2s}+p^{-3s}+\cdots
$$

Multiplying these geometric series over all primes generates every positive integer
exactly once:

$$
\prod_p(1+p^{-s}+p^{-2s}+\cdots)
=\sum_{n=1}^{\infty}\frac1{n^s}
$$

Assumptions and methods:

- The identity is justified cleanly for `Re(s)>1`, where the series and product converge absolutely.
- The arithmetic assumption is the fundamental theorem of arithmetic.
- Euler's original use was more formal by modern standards, but the core mechanism is exactly the product decomposition of integers into primes.

The obstacle removed:

Instead of counting primes one by one, encode all primes inside a single analytic
function.

---

<a id="log-derivative"></a>

## 3. From `zeta(s)` To `-zeta'/zeta`: Multiplication Becomes Addition

Starting from Euler's product:

$$
\zeta(s)=\prod_p(1-p^{-s})^{-1}
$$

take logarithms:

$$
\log\zeta(s)
=-\sum_p\log(1-p^{-s})
$$

Using

$$
-\log(1-u)=\sum_{k\ge1}\frac{u^k}{k}
$$

we obtain:

$$
\log\zeta(s)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}
$$

Differentiate:

$$
\frac{\zeta'}{\zeta}(s)
=-\sum_p\sum_{k\ge1}(\log p)p^{-ks}
$$

Therefore:

$$
-\frac{\zeta'}{\zeta}(s)
=\sum_p\sum_{k\ge1}\frac{\log p}{p^{ks}}
$$

Why introduce the logarithmic derivative?

Because products are difficult to count with directly. The logarithm turns products into
sums, and the derivative introduces the natural prime weight `log p`.

The obstacle removed:

The Euler product has primes hidden multiplicatively. The logarithmic derivative exposes
them additively.

---

<a id="von-mangoldt"></a>

## 4. From `-zeta'/zeta` To `Lambda(n)`: The Prime-Power Signal

The previous expression naturally singles out prime powers. This motivates the von
Mangoldt function:

$$
\Lambda(n)=
\begin{cases}
\log p, & n=p^k,\ k\ge1,\\
0, & \text{otherwise}.
\end{cases}
$$

Then:

$$
-\frac{\zeta'}{\zeta}(s)
=\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s},
\qquad \Re(s)>1
$$

Why introduce `Lambda(n)`?

Because zeta does not see primes alone; it sees prime powers. `Lambda(n)` is the exact
local arithmetic signal produced by the logarithmic derivative of Euler's product.

The obstacle removed:

Instead of working with a double sum over primes and powers,

$$
\sum_p\sum_{k\ge1}(\log p)p^{-ks}
$$

we package the data into one arithmetic function:

$$
\sum_n\Lambda(n)n^{-s}
$$

---

<a id="chebyshev-psi"></a>

## 5. From `Lambda(n)` To `psi(x)`: Local Signal Becomes Cumulative Mass

Define Chebyshev's function:

$$
\psi(x)=\sum_{n\le x}\Lambda(n)
$$

Equivalently:

$$
\psi(x)=\sum_{p^k\le x}\log p
$$

Why introduce `psi(x)`?

Because it is a prime-counting function adapted to the zeta function. It counts primes
and prime powers, but with logarithmic weights. This weighting is not arbitrary; it is
forced by the logarithmic derivative.

The analytic recovery is through Perron/Mellin inversion:

$$
\psi_0(x)
=
\frac{1}{2\pi i}
\int_{c-i\infty}^{c+i\infty}
-\frac{\zeta'}{\zeta}(s)\frac{x^s}{s}\,ds,
\qquad c>1
$$

Here `psi_0(x)` denotes the averaged value at jump discontinuities.

The obstacle removed:

`pi(x)` is jagged and unweighted. `psi(x)` is still a counting function, but it is
directly attached to `-zeta'/zeta`.

---

<a id="riemann-explicit-formula"></a>

## 6. Riemann's Transformation: Continue Zeta And Read Its Singularities

Riemann's 1859 memoir *Über die Anzahl der Primzahlen unter einer gegebenen Grösse*
changed the problem. Instead of treating zeta only as Euler's real series/product for
`Re(s)>1`, Riemann studied it as a complex function.

Related catalogue entry:
[Riemann Explicit Formula](formulas-linked-to-prime-numbers.md#6-riemann-explicit-formula).

Riemann's main analytic moves were:

- extend `zeta(s)` beyond `Re(s)>1` by analytic continuation;
- use the functional equation;
- study the zeros of `zeta(s)`;
- use complex integration to connect those zeros back to prime counting.

The modern explicit formula for `psi` is:

$$
\psi_0(x)
=
x
-
\sum_{\rho}\frac{x^\rho}{\rho}
-
\log(2\pi)
-
\frac12\log(1-x^{-2}),
\qquad x>1
$$

Here `rho` ranges over the non-trivial zeros of the zeta function:

$$
0<\Re(\rho)<1
$$

Interpretation:

- The pole of `zeta(s)` at `s=1` gives the main term `x`.
- The non-trivial zeros give the oscillatory error:

$$
-\sum_\rho \frac{x^\rho}{\rho}
$$

- The trivial zeros and gamma-factor terms give the correction terms:

$$
-\log(2\pi)-\frac12\log(1-x^{-2})
$$

Why introduce the explicit formula?

Because it turns the distribution of primes into a spectral problem. Prime irregularity
is explained by the zeros of `zeta(s)`.

Important historical note:

Riemann's memoir was extraordinarily compressed. Some of the claims and transformations
were not fully justified by later standards. Rigorous versions of the explicit formula
were later supplied, especially by von Mangoldt.

The obstacle removed:

The prime-counting problem becomes a problem about the analytic geometry of zeta:
its pole, zeros, and functional equation.

---

<a id="back-to-pi"></a>

## 7. From `psi(x)` Back To `pi(x)`

The function `psi(x)` counts prime powers with logarithmic weights. To return to ordinary
prime counting, introduce:

$$
\theta(x)=\sum_{p\le x}\log p
$$

Then:

$$
\psi(x)=\sum_{k\ge1}\theta(x^{1/k})
$$

By Möbius inversion:

$$
\theta(x)=\sum_{k\ge1}\mu(k)\psi(x^{1/k})
$$

Finally, recover `pi(x)` by partial summation:

$$
\pi(x)
=
\int_{2^-}^{x}\frac{d\theta(t)}{\log t}
$$

Riemann used a related weighted prime-power counting function:

$$
J(x)=\sum_{p^k\le x}\frac1k
$$

This satisfies:

$$
J(x)=\sum_{k\ge1}\frac{\pi(x^{1/k})}{k}
$$

Möbius inversion gives:

$$
\pi(x)=\sum_{k\ge1}\frac{\mu(k)}{k}J(x^{1/k})
$$

Riemann's explicit formula is often written in terms of `J(x)`:

$$
J(x)
=
\operatorname{Li}(x)
-
\sum_\rho \operatorname{Li}(x^\rho)
-
\log 2
+
\int_x^\infty
\frac{dt}{t(t^2-1)\log t}
$$

Why introduce `J(x)`?

Because the logarithm of Euler's product naturally produces prime powers with weight
`1/k`:

$$
\log\zeta(s)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}
$$

So `J(x)` is the counting function that matches `log zeta(s)`, while `psi(x)` is the
counting function that matches `-zeta'/zeta`.

The obstacle removed:

We can translate between the zeta-natural world of prime powers and the original
human question: how many primes are at most `x`?

---

## 8. Riemann-Zero Normalisation

The explicit formula shows that the error term is governed by zeros. For `psi(x)`:

$$
\psi(x)-x
\approx
-\sum_\rho\frac{x^\rho}{\rho}
$$

The Riemann Hypothesis says every non-trivial zero has the form:

$$
\rho=\frac12+i\gamma
$$

Then:

$$
x^\rho
=x^{1/2+i\gamma}
=\sqrt{x}\,e^{i\gamma\log x}
$$

So the natural zero-normalised error for `psi` is:

$$
E_\psi(x)=\frac{\psi(x)-x}{\sqrt{x}}
$$

Under the Riemann Hypothesis, this becomes heuristically:

$$
E_\psi(x)
\approx
-\sum_\gamma
\frac{e^{i\gamma\log x}}{\frac12+i\gamma}
$$

For `pi(x)`, the main approximation is `Li(x)`. Since:

$$
\operatorname{Li}(x^\rho)
\sim
\frac{x^\rho}{\rho\log x}
$$

the corresponding normalisation is:

$$
E_\pi(x)
=
\frac{\log x}{\sqrt{x}}
\bigl(\pi(x)-\operatorname{Li}(x)\bigr)
$$

Again, heuristically under the Riemann Hypothesis:

$$
E_\pi(x)
\approx
-\sum_\gamma
\frac{e^{i\gamma\log x}}{\frac12+i\gamma}
$$

Why introduce zero-normalisation?

Because it rescales the prime-counting error by the size predicted by the critical-line
zeros. If the zeros have real part `1/2`, then their contribution has natural magnitude
about `sqrt(x)`, with an additional `1/log x` factor for `pi(x)`.

The obstacle removed:

Raw prime-counting error grows with `x`. Normalisation reveals the oscillatory structure
coming from the imaginary parts of the zeros.

---

## 9. The Genealogy In One Line

Analytic direction:

$$
\boxed{
\zeta(s)
\rightarrow
-\frac{\zeta'}{\zeta}(s)
\rightarrow
\Lambda(n)
\rightarrow
\psi(x)
\rightarrow
\text{explicit formula}
\rightarrow
\pi(x)
\rightarrow
\text{zero-normalised error}
}
$$

Historical-evolutionary direction:

$$
\boxed{
\text{count primes}
\rightarrow
\pi(x)
\rightarrow
\text{density law}
\rightarrow
\text{Euler product}
\rightarrow
\text{complex zeta}
\rightarrow
\text{zeros}
\rightarrow
\text{prime fluctuations}
}
$$

The conceptual compression is:

```text
pi(x) is natural but jagged.
psi(x) is prime-counting with zeta-compatible weights.
Lambda(n) is the local prime-power signal.
-zeta'/zeta packages that signal analytically.
zeta(s) is the global object whose pole and zeros explain the signal.
```

Or, in Riemann's reversed illumination:

```text
The primes are not random noise.
Their deviations from smooth density are the shadow of zeta's zeros.
```

---

## Sources

- Bernhard Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse*,
  first published in *Monatsberichte der Berliner Akademie*, November 1859.
  English and German editions are available through D. R. Wilkins, Trinity College Dublin:
  <https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/>

- Clay Mathematics Institute historical page for Riemann's 1859 manuscript:
  <https://www.claymath.org/library/historical/riemann/templates/x>

- Leonhard Euler, *Variae observationes circa series infinitas*, written 1737,
  published 1744, Euler Archive / Scholarly Commons:
  <https://scholarlycommons.pacific.edu/euler-works/72/>

- NIST Digital Library of Mathematical Functions, section 27.2, prime-counting
  function and prime number theorem notation:
  <https://dlmf.nist.gov/27.2>

- Mathematical Association of America, *The Origin of the Prime Number Theorem*,
  for historical context on Gauss and Legendre:
  <https://old.maa.org/node/1732760>
