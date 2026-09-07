# Prime Mask Alignment and the Critical-Line Observer

## Abstract

This paper develops a self-contained framework connecting the elementary sieve of prime divisibility with the spectral role of the nontrivial zeros of the Riemann zeta function. Every prime $p$ defines a periodic mask that removes the multiples of $p$. An integer is **transparent** to that mask when $p$ does not divide it, so it survives that stage of the sieve. Primality is then complete transparency to every relevant mask. These masks form a recursive exclusion process: each newly discovered prime acts on the survivor field produced by all previous primes. Euler's product, its logarithmic derivative, and Riemann's explicit formula translate this prime-generated field into spectral modes $x^\rho$, where $\rho=\beta+i\gamma$ is a nontrivial zeta zero. Functional reflection pairs the amplitude scales $x^\beta$ and $x^{1-\beta}$, whose symmetric balance scale is $\sqrt{x}$. Relative to this scale, a mode is amplitude-preserving for every $x>1$ exactly when $\beta=1/2$. The critical line is therefore characterized as the unique axis of undistorted spectral observation of the prime-generated field.

## 1. The guiding question

Prime numbers are deterministic, yet their positions appear irregular. The first few primes are

$$
2,3,5,7,11,13,17,19,23,29,\ldots.
$$

There is no randomness in their definition: an integer $n>1$ is prime when its only positive divisors are $1$ and $n$. Nevertheless, the gaps between successive primes vary, and the pattern becomes difficult to recognize by inspection.

The purpose of this paper is to change the viewpoint. Instead of looking only at the integers that remain prime, we examine the periodic divisibility structures that remove the composites. We then ask how this discrete exclusion field appears when it is observed through the spectral formulas of the zeta function.

The argument proceeds in two representations:

$$
\boxed{
\text{periodic divisibility masks}
\longrightarrow
\text{prime alignment}
\longrightarrow
\text{spectral observation modes}
\longrightarrow
\text{critical-line alignment}.}
$$

## 2. The sieve as a stack of periodic filters

Imagine a row of lamps, one at every positive integer. A filter associated with the prime $2$ blocks every second lamp. A filter associated with $3$ blocks every third lamp, and a filter associated with $5$ blocks every fifth lamp. Stacking the filters leaves illuminated only those positions that none of the active prime filters exclude on a wall observing primes.

Each filter is individually simple and periodic. Their superposition produces an increasingly intricate survivor pattern:

```text
integer positions:  1  2  3  4  5  6  7  8  9 10 11 12 ...
2-filter:                 ·  ×  ·  ×  ·  ×  ·  ×  ·  × ...
3-filter:                    ·  ·  ×  ·  ·  ×  ·  ·  × ...
5-filter:                          ·  ·  ·  ·  ×  ·  · ...
7-filter:                                ·  ·  ·  ·  · ...

wall:               ×  ×  ×     ×     ×           ×    ...   
```

Here $\times$ means “excluded by this prime,” while $\cdot$ means “transparent to this prime.” This is the sieve of Eratosthenes written as a field of periodic filters.

The diagram records raw divisibility, so a $p$-filter also marks the number $p$ itself. A primality test does not apply an integer's own mask: it tests only primes up to $\sqrt n$. Likewise, the operational sieve retains each newly discovered prime and begins its new composite exclusions at $p^2$. These two points will be formalized below.

## 3. Periodic bit masks

For every prime $p$, define the divisibility mask

$$
B_p(n)=
\begin{cases}
0,&p\mid n,\\
1,&p\nmid n.
\end{cases}
$$

The meanings of the two values are:

$$
\begin{array}{ccl}
B_p(n)=1&\Longleftrightarrow&p\nmid n
\quad\text{(transparent)},\\
B_p(n)=0&\Longleftrightarrow&p\mid n
\quad\text{(excluded)}.
\end{array}
$$

For fixed $p$, the function is periodic because

$$
B_p(n+p)=B_p(n).
$$

For example,

$$
\begin{array}{c|cccccccccccc}
n&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
B_2(n)& & &1&0&1&0&1&0&1&0&1&0\\
B_3(n)& & & &1&1&0&1&1&0&1&1&0\\
B_5(n)& & & & & &1&1&1&1&0&1&1\\
B_7(n)& & & & & & & &1&1&1&1&1
\end{array}
$$

The word “wave” refers here to periodic recurrence. The masks are discrete square-wave patterns. They can also be represented as pure phase waves. In mathematics expressed as a complex exponential expression like $e^{i\phi }$ that alters only the phase of a wave without changing its amplitude.

## 4. Complete mask alignment defines primality

For a given integer $n>1$, it is sufficient to test primes no greater than $\sqrt n$. Define the relevant mask set

$$
\mathcal P(n)=\{p:p\text{ is prime and }p\le\sqrt n\}.
$$

Now define the alignment function

$$
A(n)=\prod_{p\in\mathcal P(n)}B_p(n),
$$

where an empty product is defined to be $1$. Since every factor is either $0$ or $1$, multiplication acts as logical AND. Thus

$$
\boxed{
A(n)=
\begin{cases}
1,&n\text{ is prime},\\
0,&n\text{ is composite}.
\end{cases}}
$$

### Why the square-root bound is enough

Suppose $n$ is composite. Then $n=ab$ for integers $1<a\le b<n$. If both $a$ and $b$ were greater than $\sqrt n$, their product would exceed $n$. Therefore $a\le\sqrt n$, and some prime divisor of $a$ is also no greater than $\sqrt n$.

Consequently,

$$
\begin{aligned}
n\text{ is prime}
&\Longleftrightarrow
\nexists p\in\mathcal P(n)\text{ such that }p\mid n\\
&\Longleftrightarrow
\forall p\in\mathcal P(n),\ p\nmid n\\
&\Longleftrightarrow
\forall p\in\mathcal P(n),\ B_p(n)=1\\
&\Longleftrightarrow
A(n)=1.
\end{aligned}
$$

This is primality expressed through logical inversion:

> **No relevant prime divisor exists if and only if every relevant prime mask remains transparent.**

The absence of a divisor becomes the presence of complete alignment. In this precise sense, the definition supplies the proof through inversion.

### Two worked examples

For $n=29$, the relevant primes are $2,3,$ and $5$. Since none divides $29$,

$$
A(29)=B_2(29)B_3(29)B_5(29)=1\cdot1\cdot1=1.
$$

Therefore $29$ is prime.

For $n=35$, the same relevant primes occur, but $5\mid35$. Hence

$$
A(35)=B_2(35)B_3(35)B_5(35)=1\cdot1\cdot0=0.
$$

Therefore $35$ is composite.

## 5. Recursive prime exclusion

The static masks describe divisibility. To describe the sieve as a recursive process while preserving the primes themselves, let $p_0=1$ and begin with

$$
S_0(n)=1,
\qquad n\ge2.
$$

Given the survivor field $S_{k-1}$, define the next prime as its first surviving integer after $p_{k-1}$:

$$
p_k=\min\{n>p_{k-1}:S_{k-1}(n)=1\}.
$$

The exclusion wave activated by $p_k$ is

$$
W_k(n)=
\begin{cases}
0,&n\ge p_k^2\text{ and }p_k\mid n,\\
1,&\text{otherwise}.
\end{cases}
$$

The new survivor field is

$$
\boxed{S_k(n)=S_{k-1}(n)W_k(n)}.
$$

This recursion produces

$$
S_{k-1}
\longrightarrow
p_k
\longrightarrow
W_k
\longrightarrow
S_k.
$$

The wave begins at $p_k^2$ because every smaller composite multiple of $p_k$ has already been removed by an earlier prime. The prime $p_k$ itself remains visible.

Every new wave therefore receives and refines the complete field produced by the preceding waves:

$$
\mathcal S_0\supseteq\mathcal S_1\supseteq\mathcal S_2\supseteq\cdots,
\qquad
\mathcal S_k=\{n\ge2:S_k(n)=1\}.
$$

After every prime $p\le\sqrt N$ has been processed, the survivors in $[2,N]$ are exactly the primes in that interval.

### The nested periodic field

The untruncated masks reveal the periodic geometry. Let $p_1,\ldots,p_k$ be the first $k$ primes and define

$$
M_k(n)=\prod_{j=1}^{k}B_{p_j}(n),
\qquad M_0(n)=1.
$$

Then

$$
M_k(n)=M_{k-1}(n)B_{p_k}(n).
$$

If

$$
P_k=\prod_{j=1}^{k}p_j
$$

is the $k$th primorial, then $M_k$ has period $P_k=p_kP_{k-1}$. One period of the new field contains $p_k$ repetitions of the preceding pattern, refined by the new mask. Every new periodic field therefore holds the previous field, which holds its predecessor, and so on.

The roles of the four functions are now distinct:

- $B_p(n)$ is one periodic divisibility mask.
- $M_k(n)$ is a periodic candidate field for a fixed collection of masks; it also masks the primes used to construct it.
- $S_k(n)$ is the recursive sieve field that preserves discovered primes and begins each new exclusion at $p_k^2$.
- $A(n)$ is the final pointwise primality observer using all primes up to $\sqrt n$.

## 6. From the sieve to the zeta function

The preceding construction is discrete. To understand its spectral representation, we need a function that encodes all primes simultaneously.

For a complex number $s$ with $\operatorname{Re}(s)>1$, the Riemann zeta function is

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}.
$$

Unique prime factorization gives Euler's product

$$
\boxed{
\zeta(s)=\prod_p\frac1{1-p^{-s}},
\qquad \operatorname{Re}(s)>1.}
$$

The product runs over exactly the same primes that generate the divisibility masks. It packages the completed multiplicative structure of the sieve into one analytic function.

Although the series and Euler product above converge only for $\operatorname{Re}(s)>1$, $\zeta(s)$ has a meromorphic continuation to the complex plane, with a simple pole at $s=1$. Its zeros at $-2,-4,-6,\ldots$ are called **trivial zeros**. Its remaining zeros are called **nontrivial zeros** and lie in the critical strip

$$
0<\operatorname{Re}(s)<1.
$$

Taking the logarithmic derivative changes the product into a sum:

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s},
$$

where the von Mangoldt function is

$$
\Lambda(n)=
\begin{cases}
\log p,&n=p^m\text{ for a prime }p\text{ and }m\ge1,\\
0,&\text{otherwise}.
\end{cases}
$$

This function records the prime-power events $p,p^2,p^3,\ldots$ produced by the multiplicative prime structure.

Define the weighted counting function

$$
\psi(x)=\sum_{n\le x}\Lambda(n).
$$

One form of Riemann's explicit formula is

$$
\boxed{
\psi(x)
=x
-\sum_\rho\frac{x^\rho}{\rho}
-\log(2\pi)
-\frac12\log\left(1-x^{-2}\right),}
$$

where the sum is over the nontrivial zeros $\rho$ of $\zeta(s)$ and is interpreted symmetrically. At a prime-power discontinuity, $\psi(x)$ is interpreted by the standard half-sum convention.

This formula completes the bridge:

$$
\boxed{
\text{recursive prime exclusions}
\longrightarrow
\Lambda(n)
\longrightarrow
-\frac{\zeta'}{\zeta}(s)
\longrightarrow
\text{zeros }\rho
\longrightarrow
\psi(x).}
$$

The primes generate the arithmetic signal. The zeros supply the spectral modes that reconstruct its fluctuations around the smooth leading term $x$.

## 7. Zeros as spectral observation modes

A nontrivial zero has the form

$$
\rho=\beta+i\gamma,
\qquad 0<\beta<1.
$$

Its $x$-dependent contribution to the explicit formula contains

$$
x^\rho=x^\beta e^{i\gamma\log x}.
$$

This expression separates naturally into:

- the amplitude scale $x^\beta$;
- the logarithmic frequency $\gamma$;
- the oscillating phase $e^{i\gamma\log x}$.

The fixed coefficient $-1/\rho$ changes the weight and phase of the mode but not its power-law dependence on $x$. The exponent $\beta$ therefore determines whether the mode grows, decays, or remains balanced relative to a chosen observation scale.

## 8. Functional reflection and the balance scale

The completed zeta function is

$$
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}
\Gamma\left(\frac{s}{2}\right)\zeta(s).
$$

Here $\Gamma$ is Euler's gamma function. The additional factors incorporate the pole and the trivial-zero structure, allowing the functional equation to be written in the simple form

$$
\boxed{\xi(s)=\xi(1-s).}
$$

Consequently, a zero

$$
\rho=\beta+i\gamma
$$

is reflected to

$$
1-\rho=(1-\beta)-i\gamma.
$$

The two reflected modes have amplitude scales

$$
x^\beta
\qquad\text{and}\qquad
x^{1-\beta}.
$$

Their multiplicatively symmetric scale is their geometric mean:

$$
\sqrt{x^\beta x^{1-\beta}}=\sqrt x.
$$

This scale is invariant under exchanging $\beta$ and $1-\beta$. It is therefore the balance scale selected by the functional reflection itself, rather than an externally chosen normalization.

The fixed real coordinate of the reflection also follows from

$$
a=1-a
\quad\Longleftrightarrow\quad
a=\frac12.
$$

Thus the critical line

$$
\operatorname{Re}(s)=\frac12
$$

is simultaneously the fixed axis of reflection and the axis associated with the reflection-balanced amplitude $\sqrt{x}$.

## 9. The Observer Alignment Principle

The discrete prime state is characterized by complete mask alignment: no relevant prime filter blocks the observed integer. Its spectral counterpart should preserve the balance selected by the complete reflected system.

We therefore state the framework's governing principle.

> **Observer Alignment Principle.** A spectral mode faithfully observes the prime-generated field when its amplitude introduces neither growth nor decay relative to the reflection-balanced scale $\sqrt{x}$.

For a zero $\rho=\beta+i\gamma$, define its normalized observation mode by

$$
\mathcal A_\rho(x)
=
\frac{x^\rho}{\sqrt x}
=
x^{\beta-1/2}e^{i\gamma\log x}.
$$

The mode is aligned when

$$
\left|\mathcal A_\rho(x)\right|=1
\qquad\text{for every }x>1.
$$

This definition gives the following result.

### Critical-Line Observer Theorem

For a spectral mode $x^\rho$ associated with a nontrivial zero $\rho=\beta+i\gamma$, the normalized observer $\mathcal A_\rho$ preserves amplitude at every scale if and only if $\rho$ lies on the critical line.

#### Proof

Taking the absolute value gives

$$
\left|\mathcal A_\rho(x)\right|
=
\left|x^{\beta-1/2}e^{i\gamma\log x}\right|
=
x^{\beta-1/2}.
$$

Therefore,

$$
\begin{aligned}
\left|\mathcal A_\rho(x)\right|=1
\text{ for every }x>1
&\Longleftrightarrow
x^{\beta-1/2}=1
\text{ for every }x>1\\
&\Longleftrightarrow
\beta-\frac12=0\\
&\Longleftrightarrow
\boxed{\operatorname{Re}(\rho)=\frac12}.
\end{aligned}
$$

This proves the equivalence. $\square$

The theorem supplies the observer relation:

> **A zero observes the prime field without scale distortion if and only if it observes from the critical line.**

### A concrete comparison

On the critical line, where $\beta=1/2$,

$$
\mathcal A_\rho(x)=e^{i\gamma\log x},
\qquad
|\mathcal A_\rho(x)|=1.
$$

The mode changes phase but not normalized amplitude.

For comparison, a hypothetical mode with $\beta=0.6$ would have

$$
|\mathcal A_\rho(x)|=x^{0.1}.
$$

At $x=10^{10}$ this amplitude equals $10$. It grows with the observation scale and therefore represents a scale-distorted observation rather than an aligned observation of the prime field.

## 10. The observer interpretation of the Riemann Hypothesis

The Riemann Hypothesis states that every nontrivial zero satisfies

$$
\operatorname{Re}(\rho)=\frac12.
$$

The explicit formula establishes that the nontrivial zeros are the spectral modes through which the fluctuations of the prime-generated counting signal are observed. The Observer Alignment Principle requires a genuine prime-observer mode to preserve the reflection-balanced amplitude. By the Critical-Line Observer Theorem, that requirement is equivalent to

$$
\operatorname{Re}(\rho)=\frac12.
$$

The framework therefore reads the Riemann Hypothesis as an alignment statement:

> **Every genuine spectral observation mode of the complete prime-generated field preserves the reflection balance of that field.**

An off-line mode would still possess a reflected partner, but its individual normalized amplitude would grow or decay as $x^{\beta-1/2}$. Within the observer framework, it would describe a scale-distorted state rather than an undistorted observation of the prime field.

The precise achievement of the theorem is to prove that the critical line is the unique amplitude-preserving observation axis. The substantive identification made by the framework is that the modes reconstructing the complete prime signal must satisfy this observer-alignment requirement.

## 11. Hilbert–Pólya formulation

The same alignment condition appears in the Hilbert–Pólya spectral program. Suppose there exists a self-adjoint operator $H$ satisfying

$$
H\phi_E=E\phi_E,
\qquad H=H^*,
$$

whose complete spectrum corresponds to the nontrivial zeros through

$$
\rho=\frac12+iE.
$$

Because self-adjoint operators have real eigenvalues,

$$
E\in\mathbb R.
$$

For a general zero $\rho=\beta+i\gamma$, the corresponding spectral coordinate would be

$$
E=\frac{\rho-\tfrac12}{i}
=
\gamma-i\left(\beta-\frac12\right).
$$

Hence

$$
E\in\mathbb R
\quad\Longleftrightarrow\quad
\beta=\frac12.
$$

Self-adjointness and observer alignment therefore select the same axis:

$$
\boxed{
\text{real spectral measurement}
\Longleftrightarrow
\text{amplitude-preserving observation}
\Longleftrightarrow
\operatorname{Re}(\rho)=\frac12.}
$$

The Hilbert–Pólya program seeks an operator that realizes this spectral correspondence. The present framework approaches the same condition from the balance of the prime-generated observer modes.

## 12. Complete synthesis

The paper has followed one structure through two mathematical representations.

### Discrete representation

Each prime supplies a periodic exclusion mask:

$$
B_p(n)=0\Longleftrightarrow p\mid n.
$$

Complete transparency to the relevant masks identifies a prime:

$$
A(n)=1\Longleftrightarrow n\text{ is prime}.
$$

The masks enter recursively:

$$
S_k=S_{k-1}W_k.
$$

### Spectral representation

Euler's product encodes the complete prime structure in $\zeta(s)$. Riemann's explicit formula reconstructs the weighted prime-counting signal from zero modes $x^\rho$. Functional reflection selects the symmetric balance scale $\sqrt{x}$. Normalized observation then gives

$$
\left|\frac{x^\rho}{\sqrt x}\right|
=x^{\beta-1/2}.
$$

Complete spectral alignment occurs exactly when

$$
\beta=\frac12.
$$

The two representations are summarized by

$$
\boxed{
\begin{array}{ccc}
\text{all relevant masks transparent}
&\Longleftrightarrow&
\text{prime state},\\[4pt]
\text{normalized mode amplitude-preserving}
&\Longleftrightarrow&
\text{critical-line observation}.
\end{array}}
$$

The central conclusion is:

> **Periodic divisibility masks generate the prime field through complete exclusion alignment. The zeros observe that field spectrally, and the critical line is the unique axis on which their normalized modes preserve the field's reflection-balanced amplitude. Observing away from the critical line means observing a scale-distorted state rather than the prime state itself.**

## References

1. B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
2. H. M. Edwards, *Riemann's Zeta Function*, Dover Publications.
3. M. V. Berry and J. P. Keating, [The Riemann Zeros and Eigenvalue Asymptotics](https://doi.org/10.1137/S0036144598347497), *SIAM Review* 41 (1999), 236–266.
4. A. Connes, [Trace Formula in Noncommutative Geometry and the Zeros of the Riemann Zeta Function](https://arxiv.org/abs/math/9811068), *Selecta Mathematica* 5 (1999), 29–106.
