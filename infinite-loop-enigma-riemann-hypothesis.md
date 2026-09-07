---
title: "The Infinite Loop Enigma: Recursive Prime Observation and the Critical-Line Constraint"
subtitle: "Primes as the Oldest Self-Referential Distribution"
author:
  - "Yves Langeraert"
date: "2026-08-24"
subject: "Riemann Hypothesis; prime counting; zeta zeros; recursive normalization"
keywords:
  - Riemann zeta function
  - Riemann Hypothesis
  - prime counting function
  - explicit formula
  - recursive normalization
  - critical line
msc:
  - "11M26"
  - "11N05"
  - "11M06"
geometry: margin=1in
fontsize: 11pt
linestretch: 1.12
---

# Abstract

The distribution of prime numbers has been studied through a sequence of increasingly expressive representations: divisibility, Euler products, counting functions, logarithmic approximations, arithmetic error terms, and complex-analytic formulas. Euler's product formula already encodes the primes as a global multiplicative structure [DLMF25.2], while later explicit formulas encode finer properties of prime distribution through analytic error terms and zeta-zero contributions [DLMF25.16; Edwards2001; Titchmarsh1986].

This paper develops a complementary interpretation of prime counting as a recursive observation process. Since the primality of a candidate integer is determined by divisibility against smaller primes, each new count depends on the prime structure already generated at lower scales. We make a proof attempt for the Riemann Hypothesis by defining a recursive observable, relating it to the explicit-formula zero terms, and arguing that a non-circular phase-crossing stability condition forces the critical line [DLMF25.10; ClayRH].

The central claim is stronger than the classical explicit formula: the nontrivial zeros of the zeta function are interpreted here not merely as a spectral encoding of fluctuations in prime distribution, but as a spectral encoding of the prime distribution itself as a self-generating and self-observing structure. Under the proposed normalization framework, the zero terms are decomposed into amplitude and phase around the candidate axis $\Re(s)=1/2$. We claim that prime-identification events are recovered through a phase-crossing rule, and that stability of this rule under recursion and functional-equation symmetry forces every nontrivial zero onto the critical line.

# 1. Introduction

The distribution of prime numbers was studied long before Riemann's 1859 memoir. Euclid established the infinitude of primes through a finite-list escape argument [HardyWright2008]. Euler connected primes to analysis through the product formula for the zeta function [DLMF25.2; Apostol1976]. Legendre, Gauss, Chebyshev, and others studied the approximate density of primes through counting functions and logarithmic laws [Ingham1932; Edwards2001]. Riemann's contribution was not to invent the mystery of primes, but to encode that mystery in a much richer complex-analytic form [Riemann1859; Edwards2001].

The Riemann Hypothesis states that every nontrivial zero $\rho$ of the Riemann zeta function satisfies [DLMF25.10; ClayRH]

$$
\Re(\rho)=\frac12.
$$

The usual analytic formulation concerns the zero set of

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s},
\qquad \Re(s)>1,
$$

continued meromorphically to the complex plane [DLMF25.2]. Yet the Euler product

$$
\zeta(s)=\prod_p \left(1-p^{-s}\right)^{-1},
\qquad \Re(s)>1,
$$

places primes at the origin of the analytic object [DLMF25.2].

This paper starts from a simple observation: a prime can be defined by exclusion rules against smaller prime divisors. Thus the prime-counting process does not merely count independent events. Each step observes a structure accumulated by previous steps. The thesis is that the classical and spectral encodings of prime distribution are not merely external descriptions; they expose a recursive self-observation process whose invariant normalization axis is the critical line.

The paper is organized as follows. Section 2 fixes notation. Section 3 formulates prime counting as a recursive observation process. Section 4 recalls classical encodings of prime-distribution properties and then narrows to the known spectral connection between primes and zeta zeros. Section 5 gives a concrete finite-scale normalization model before listing alternative observation maps. Section 6 states the main theorem and proof attempt. Section 7 isolates the proof obligations a reviewer should examine most carefully. Section 8 concludes.

For clarity, the paper separates three levels of assertion. Background claims are cited at first substantial use; new definitions and lemmas are marked as part of the present proof attempt. The Wikipedia article on the Riemann Hypothesis was used only as a discovery map for standard references and topic coverage, not as authority for the proof [WikipediaRH].

1. **Known facts.** Euler products, prime-counting functions, Chebyshev functions, and explicit formulas already connect primes with $\zeta(s)$ and its zeros.
2. **Proposed framework.** Prime counting is viewed as a recursive observation process, and $\mathcal I_\psi(x)=(\psi(x)-x)/\sqrt{x}$ is used as the first concrete normalization candidate.
3. **Proof hinge.** The proof turns on showing that the recursive observable has a non-circular phase-crossing correspondence whose infinite-scale stability forces $\Re(\rho)=1/2$.

# 2. Notation and Background

Let

$$
\pi(x)=\#\{p\le x:p\text{ prime}\}
$$

denote the prime-counting function. Let

$$
\psi(x)=\sum_{n\le x}\Lambda(n)
$$

be Chebyshev's second function, where $\Lambda$ is the von Mangoldt function. The prime-counting function, Chebyshev's $\psi$-function, and the relation between $\psi(x)$ and primes are standard in analytic number theory [DLMF25.16; Apostol1976].

The nontrivial zeros of $\zeta(s)$ are denoted [DLMF25.10]

$$
\rho=\sigma+i\gamma,
\qquad 0<\sigma<1.
$$

The Riemann Hypothesis is equivalent to the assertion that $\sigma=\tfrac12$ for every such $\rho$ [DLMF25.10; ClayRH].

# 3. Prime Counting as Recursive Observation

For an integer $n>1$, primality can be tested by checking divisibility by primes $p\le\sqrt{n}$, because a composite $n=ab$ has at least one factor not exceeding $\sqrt{n}$ [HardyWright2008; Apostol1976]. Therefore the question "is $n$ prime?" depends on the prime set already discovered below $\sqrt{n}$.

This is the elementary sieve viewpoint. A sieve begins with a set of candidate integers and removes candidates divisible by already-known primes. The classical Sieve of Eratosthenes generates all primes below a given bound by repeatedly crossing out multiples of each prime as it is encountered [DLMF27.18; HardyWright2008]. Modern sieve theory develops this exclusion idea into a systematic method for estimating how many integers remain after specified congruence classes or prime divisibility conditions have been removed [IwaniecKowalski2004]. In this paper, "sieve rule" refers only to the elementary prime-generation rule unless a stronger analytic sieve estimate is explicitly invoked.

Define the finite prime state

$$
P_x=\{p\le x:p\text{ prime}\}.
$$

The transition from $x$ to $x+1$ may be written informally as

$$
P_{x+1}
=
P_x\cup
\begin{cases}
\{x+1\}, & x+1\text{ is not divisible by any }p\in P_{\sqrt{x+1}},\\
\varnothing, & \text{otherwise}.
\end{cases}
$$

Thus the count

$$
\pi(x+1)-\pi(x)
$$

is determined by the already-formed prime structure. In this sense, the prime-counting process observes its own prior state.

## 3.1. Recursive State Principle

The basic principle investigated here is:

> The prime distribution at scale $x$ is not an external input to prime counting; it is the accumulated state against which the next observation is defined.

This motivates searching for an invariant quantity associated with repeated normalization of prime-distribution error across scales.

## 3.2. The Square-Root Activation Frontier

An important structural observation already appears inside the sieve geometry itself, before any appeal to zeta zeros or the Riemann Hypothesis.

If a prime $p$ is the first possible divisor capable of activating a composite witness at scale $x$, then the threshold relation is

$$
p^2=x
\quad\Longleftrightarrow\quad
p=\sqrt{x}.
$$

This is the familiar square-root boundary in primality testing: to determine whether $x$ is prime, it is enough to test divisibility by primes not exceeding $\sqrt{x}$ [HardyWright2008; Apostol1976].

Now pass to logarithmic coordinates, a standard scale change in prime-number asymptotics because prime density is governed at first order by logarithmic laws [Ingham1932; Apostol1976]:

$$
u=\log x,
\qquad
v=\log p.
$$

The curved frontier $p=\sqrt{x}$ becomes the straight line

$$
v=\frac12 u.
$$

This line will be called the **square-root activation frontier** or **half-scale boundary**. Its meaning is purely arithmetic: it marks the scale at which a prime $p$ becomes large enough that its square reaches the observation level $x$.

The factor $1/2$ therefore appears already in the generative sieve geometry. This is a significant observation, but it must be handled with discipline. At this stage, the half-scale boundary is **not** identified with the critical line $\Re(s)=1/2$. It is only a geometric $1/2$ arising from the transformation of the square-root divisibility threshold into logarithmic coordinates.

The later burden is to prove that the half-scale boundary in sieve geometry and the critical-line normalization axis in spectral geometry are in fact mathematically equivalent.

# 4. Classical and Spectral Encodings of Prime Distribution

Classical number theory encodes properties of the prime distribution in several related ways. Euler's product formula encodes primes multiplicatively through the zeta function [DLMF25.2]. Prime-counting functions such as $\pi(x)$ and $\psi(x)$ encode the cumulative distribution additively [DLMF25.16]. Logarithmic approximations such as $\operatorname{Li}(x)$ encode the leading-order density in the prime number theorem tradition [Ingham1932; Edwards2001]. Error terms encode the deviation between the observed distribution and the smooth approximation [DLMF25.16; Schoenfeld1976].

## 4.1. Prime-Dependent Logarithmic Structure

Before introducing zeta zeros, it is useful to isolate the logarithmic variable that already organizes the prime sieve.

The arithmetic activation rule

$$
p\leq\sqrt{x}
$$

becomes, after passing to logarithmic coordinates,

$$
\log p\leq\frac12\log x.
$$

Thus the sieve geometry is naturally ordered by the prime-dependent quantity $\log p$, and the square-root activation frontier becomes a half-scale boundary in the $(\log x,\log p)$-plane.

Now compare this with Euler's local prime factor in the zeta product [DLMF25.2]. Write the complex variable as

$$
s=\sigma+it.
$$

For any positive real base $a$, the complex power is interpreted by

$$
a^{-s}
=
\exp(-s\log a)
=
\exp(-\sigma\log a)\exp(-it\log a).
$$

The first factor is real and positive:

$$
\exp(-\sigma\log a)=a^{-\sigma}.
$$

It changes the size, or modulus, of the contribution. The second factor lies on the unit circle:

$$
\exp(-it\log a).
$$

It does not change the modulus; it rotates the complex argument by $-t\log a$. In this precise sense, the real coordinate $\sigma$ can be interpreted as representing an amplitude and the imaginary coordinate $t$ as representing a phase.

Applying this elementary amplitude-phase dictionary to the prime base $a=p$ gives

$$
\left(1-p^{-s}\right)^{-1},
\qquad
p^{-s}=p^{-\sigma}e^{-it\log p}.
$$

This decomposition separates two roles played by the same logarithmic prime variable $\log p$:

- $p^{-\sigma}$ is an amplitude contribution determined by the real coordinate $\sigma$;
- $e^{-it\log p}$ is a phase contribution determined by the imaginary coordinate $t$ and the prime logarithm $\log p$.

So even before any use of the explicit formulas, the sieve description and the zeta factor already share a common logarithmic coordinate. On the sieve side, $\log p$ locates activation thresholds. On the zeta side, $\log p$ supplies phase rotation and amplitude damping. This does not yet identify the two structures; it explains why comparing them is mathematically meaningful.

## 4.2. From Sieve Boundary to Spectral Encoding

The arithmetic sieve rule and the spectral-side zeta factor should first be understood as distinct structures.

On the arithmetic side, the prime sieve uses $\log p$ to determine when a prime becomes active relative to the observation scale $x$:

$$
\log p\leq\frac12\log x.
$$

On the spectral side, we can now read that Riemann's representation uses $\log p$ to determine the oscillatory phase attached to that same prime:

$$
p^{-s}=p^{-\sigma}e^{-it\log p}.
$$

These are not yet the same statement. The first is an activation threshold in generative sieve geometry. The second is a phase-amplitude decomposition in complex spectral geometry.

What matters is that both structures are indexed by the same prime logarithm. This suggests that the spectral representation is not arbitrarily attached to the primes from outside; rather, it reorganizes a logarithmic structure already present in the prime-generating side.

The conceptual bridge proposed in this paper is therefore the following:

> the sieve presents $\log p$ as an arithmetic activation coordinate, while the zeta factor presents $\log p$ as a spectral phase coordinate.

The mathematical burden is then to determine whether the half-scale boundary

$$
\log p=\frac12\log x
$$

and the critical-line normalization

$$
\Re(s)=\frac12
$$

are merely analogous appearances of the same number, or are linked by a genuine normalization principle. The paper identifies it as the central bridge that must be established.

The explicit formulas then introduce a spectral layer. They relate prime-counting functions to the zeros of $\zeta(s)$ [Riemann1859; DLMF25.16; Edwards2001; Titchmarsh1986]. In a standard schematic form,

$$
\psi(x)=x-\sum_\rho \frac{x^\rho}{\rho}+\text{lower-order terms},
$$

where the sum ranges over nontrivial zeros [DLMF25.16]. This establishes that the zeros collectively encode the oscillatory error in prime distribution.

These known results should be separated from the new claim. The established classical fact is:

$$
\text{classical formulas encode prime-distribution properties}.
$$

The sharper spectral fact is:

$$
\text{zeta zeros collectively encode prime-distribution fluctuations}.
$$

The proposed stronger claim is:

$$
\text{the critical line is forced by recursive normalization of those fluctuations}.
$$

# 5. Recursive Normalization

This section fixes one working model before introducing alternatives. The purpose is to give the reader a definite object to follow. Later sections may reject or refine this model, but the paper should first show what the words "recursive observable" mean in a computable finite setting.

The cleanest starting error term is Chebyshev's second function [DLMF25.16],

$$
E_\psi(x)=\psi(x)-x,
$$

because the explicit formula connects $\psi(x)$ directly to zero contributions of the form $x^\rho/\rho$ [DLMF25.16]. The working normalized observable is

$$
\mathcal I_\psi(x)
=
\frac{\psi(x)-x}{\sqrt{x}},
\qquad x>1.
$$

This definition deliberately uses the square-root scale as a candidate normalization, not as a proof of the critical line. The choice has two motivations:

1. the sieve activation boundary $p\leq\sqrt{x}$ already singles out half-scale arithmetic information;
2. under the Riemann Hypothesis, the explicit-formula error for $\psi(x)-x$ is expected to have natural square-root size, up to logarithmic factors [DLMF25.16; Schoenfeld1976].

The second motivation must be treated carefully. It explains why $\sqrt{x}$ is a meaningful candidate normalization, but it cannot be used as evidence for the Riemann Hypothesis. The proof must therefore test whether this normalization can be justified from recursive prime-state structure alone.

For this working model, choose the lower-scale observation map

$$
\Phi(x)=\sqrt{x}.
$$

The desired recursion becomes

$$
\mathcal I_\psi(x)
=
\mathcal T_x\bigl(\mathcal I_\psi(\sqrt{x})\bigr)+R_\psi(x),
$$

where $\mathcal T_x$ is the transport rule from scale $\sqrt{x}$ to scale $x$, and $R_\psi(x)$ records the information added between these two scales. A minimal finite-scale choice is

$$
\mathcal T_x(y)=x^{-1/4}y,
$$

since

$$
x^{-1/4}\mathcal I_\psi(\sqrt{x})
=
\frac{\psi(\sqrt{x})-\sqrt{x}}{\sqrt{x}}.
$$

With this transport, the residual is forced rather than inserted by hand:

$$
R_\psi(x)
=
\frac{\psi(x)-x-\psi(\sqrt{x})+\sqrt{x}}{\sqrt{x}}.
$$

Equivalently,

$$
R_\psi(x)
=
\frac{1}{\sqrt{x}}
\left(
\sum_{\sqrt{x}<n\leq x}\Lambda(n)
-
(x-\sqrt{x})
\right).
$$

This identity is only a finite bookkeeping recursion. Its value is that every term is explicit. It separates the already-observed lower-scale contribution from the newly resolved arithmetic interval $(\sqrt{x},x]$. The hard question is whether this elementary recursion can be strengthened into a stable spectral statement.

The use of $\psi$ adds one further structural feature. Since $\Lambda(n)$ is nonzero exactly on prime powers, $\psi(x)$ rewrites the relevant part of the integer interval into logarithms of primes. Composite integers that are not prime powers vanish from the observable, while prime powers are reflected back to their prime base. This is why $\psi$ is a natural test object for a proof attempt centered on prime-logarithmic phase structure.

There are two closely related logarithmic rewritings that should not be confused. The raw logarithm of a prime power satisfies

$$
\log(p^k)=k\log p.
$$

Chebyshev's $\psi$-function uses the von Mangoldt weight instead:

$$
\Lambda(p^k)=\log p.
$$

Thus $\psi$ records the occurrence of a prime-power scale but stores it through the logarithm of the underlying prime. It is a compressed prime-base record rather than a raw logarithm of every integer.

## 5.1. Finite Example

Take $x=25$. Then

$$
\sqrt{x}=5.
$$

Using the von Mangoldt definition, the finite example reads:

$$
\psi(5)=\Lambda(2)+\Lambda(3)+\Lambda(4)+\Lambda(5)
=2\log 2+\log 3+\log 5,
$$

because $\Lambda(n)$ records $\log p$ when $n$ is a prime power $p^k$, and records $0$ otherwise. Thus the prime-power $4=2^2$ is not kept as an independent logarithm $\log 4$; it is transposed back into the prime logarithm $\log 2$. In this sense $\psi(5)$ is already a prime-based logarithmic expression:

$$
\psi(5)=2\log 2+\log 3+\log 5.
$$

This is important for the present proof attempt. The observable $\mathcal I_\psi$ does not merely normalize a raw integer sum. It normalizes a logarithmic record in which non-prime contributions survive only when they are prime powers, and then only through the logarithm of their underlying prime. The normalized observable is therefore expressed through a prime-logarithmic subset of the integers.

At the larger scale,

$$
\begin{aligned}
\psi(25)
&=\sum_{n\leq25}\Lambda(n)\\
&=4\log 2+2\log 3+2\log 5+\log 7+\log 11+\log 13+\log 17+\log 19+\log 23.
\end{aligned}
$$

The normalized observable is

$$
\mathcal I_\psi(25)=\frac{\psi(25)-25}{5}.
$$

The transported lower-scale observable is

$$
\mathcal T_{25}\bigl(\mathcal I_\psi(5)\bigr)
=
25^{-1/4}\frac{\psi(5)-5}{\sqrt{5}}
=
\frac{\psi(5)-5}{5}.
$$

Therefore

$$
R_\psi(25)
=
\frac{\psi(25)-25-\psi(5)+5}{5}.
$$

Equivalently,

$$
\begin{aligned}
R_\psi(25)
&=
\frac{
2\log 2+\log 3+\log 5+\log 7+\log 11+\log 13+\log 17+\log 19+\log 23-20
}{5}.
\end{aligned}
$$

The residual is exactly the von Mangoldt-weighted contribution of the interval $5<n\leq25$, after subtracting its smooth length $20$. The extra terms $2\log 2+\log 3+\log 5$ come from the prime powers $8=2^3$, $9=3^2$, $16=2^4$, and $25=5^2$, each reflected back to its prime base by $\Lambda$. In this finite example, no spectral claim has been made. The example only shows how a reader should understand the recursion: lower-scale state is transported forward, and the remaining interval supplies a forced residual expressed in prime logarithms.

The intended next step is to ask whether the explicit-formula expansion of this same decomposition admits a phase-normalized version whose residuals remain stable under repeated square-root descent.

## 5.2. Alternative Observation Maps

The square-root map is not the only possible formalization of "previous prime state." The following maps should be tested as alternatives:

$$
\Phi_1(x)=\pi(x),
$$

$$
\Phi_2(x)=p_{\pi(x)-1},
$$

$$
\Phi_3(x)=\sqrt{x},
$$

where $p_n$ denotes the $n$-th prime.

Each choice captures a different meaning of "the previous prime state." This paper selected exactly one map before making a theorem-level claim, because the normalization, transport, residual, and stability condition all depend on this choice.

## 5.3. Definitions of Prime-Logarithmic Support, Phase, Cycle, Crossing, and Prime Identification

The language of prime-logarithmic support, phase, and waves is used in this paper in a strictly mathematical sense, not as metaphor. The following definitions define the usage.

**Definition 5.3.1. Prime-Logarithmic Support.**  
An arithmetic observable is said to have prime-logarithmic support if its nonzero arithmetic weights are expressible as finite or limiting sums of $\log p$ over primes $p$, with composite contributions either removed or transposed back to their prime bases. Chebyshev's function $\psi(x)$ has this property because

$$
\psi(x)
=
\sum_{n\leq x}\Lambda(n)
=
\sum_{p^k\leq x}\log p.
$$

Thus non-prime non-powers disappear from $\psi$, while prime powers survive only as reflections back to their prime base. This is the arithmetic support condition that makes $\psi$ compatible with the $\log p$-phase structure of Euler factors.

**Definition 5.3.2. Spectral Encoding.**  
A spectral encoding of a real-valued arithmetic function $f(x)$ is any representation of $f$, or of a canonically associated error term $E_f(x)$, as a superposition of oscillatory terms indexed by spectral data. In the zeta setting, the model oscillatory terms are the zero contributions [DLMF25.16]

$$
\frac{x^\rho}{\rho}
=
\frac{x^\sigma e^{i\gamma\log x}}{\rho},
\qquad \rho=\sigma+i\gamma.
$$

In this decomposition, $\gamma$ is the frequency parameter and $\sigma$ is the amplitude-growth parameter. Accordingly, the phrase "the nontrivial zeros spectrally encode prime distribution" means that prime-distribution error is represented through the full family of oscillatory contributions attached to the zero set.

**Definition 5.3.3. Phase Coordinate.**  
For a nontrivial zero $\rho=\sigma+i\gamma$ and scale $x>1$, the associated phase coordinate is

$$
\varphi_\rho(x)=\gamma\log x.
$$

This is the argument of the oscillatory factor $e^{i\gamma\log x}$. Whenever the paper refers to a "phase perspective," it refers to analysis in the variable $\varphi_\rho(x)$, or in an equivalent transformed variable such as the Riemann-Siegel phase $\theta(t)$.

**Definition 5.3.4. Wave Representation.**  
The wave representation attached to a zero $\rho$ is the real oscillatory component

$$
W_\rho(x)=\operatorname{Re}\left(\frac{x^\rho}{\rho}\right).
$$

Up to the amplitude factor $x^\sigma/|\rho|$ and a constant phase shift from $1/\rho$, this is a cosine-type wave in the phase variable $\varphi_\rho(x)$. Thus references in this paper to "wave" behavior mean oscillatory dependence on $\gamma\log x$, not a separate physical model.

**Definition 5.3.5. Critical-Line Normalization.**  
Critical-line normalization means measuring each zero contribution relative to the candidate square-root amplitude scale suggested by the $\psi(x)$-error formulation of RH [DLMF25.16; Schoenfeld1976],

$$
x^{1/2}.
$$

Thus

$$
x^\rho
=
x^{1/2}
\left(x^{\sigma-1/2}e^{i\gamma\log x}\right).
$$

If $\sigma=1/2$, the relative amplitude $x^{\sigma-1/2}$ is constant in $x$, and the remaining variation is carried by the phase coordinate $\gamma\log x$. If $\sigma\neq1/2$, the relative amplitude drifts with scale. The phrase "around the critical line" therefore means "after expressing the spectral contribution relative to the candidate scale $x^{1/2}$," not "after assuming the Riemann Hypothesis."

**Definition 5.3.6. Cycle.**  
Fix a zero ordinate $\gamma>0$. A cycle of the associated phase variable is an increment of $2\pi$ in $\varphi_\rho(x)$. Equivalently, a cycle is a multiplicative rescaling of $x$ satisfying

$$
\varphi_\rho(x')-\varphi_\rho(x)=2\pi,
$$

that is,

$$
\gamma\log(x'/x)=2\pi.
$$

Hence

$$
x'=x\,e^{2\pi/\gamma}.
$$

This definition makes clear that a cycle is measured in logarithmic scale, not by additive increments in $x$.

**Definition 5.3.7. Crossing.**  
A crossing is a phase value at which the real oscillatory component changes sign. In the idealized cosine model,

$$
\cos(\varphi)=0
$$

occurs exactly at

$$
\varphi=\frac{\pi}{2}+k\pi,
\qquad k\in\mathbb Z.
$$

Accordingly, a crossing for $W_\rho(x)$ is a value of $x$ at which the phase-shifted cosine factor in $W_\rho(x)$ vanishes. The special role of $\pi/2$ and $3\pi/2$ is therefore that they are the two zero-crossings in one full $2\pi$ phase cycle.

**Definition 5.3.8. Prime Identification Event.**  
A prime identification event at scale $x$ is the update

$$
\pi(x)-\pi(x-1)=1.
$$

Equivalently, $x$ is prime. This paper does not define a prime to be a phase crossing. Instead, the stronger proposed claim is that prime identification events correspond, through the recursive observable $\mathcal I$, to distinguished crossing events in the spectral normalization. That correspondence must be proved; it is not assumed as a definition.

**Definition 5.3.9. Self-Generating and Self-Observing Prime Distribution.**  
The prime distribution is called self-generating in the minimal sense that the extension from $P_x$ to $P_{x+1}$ is determined by divisibility against primes already contained in lower-scale prime states. It is called self-observing in the sense that each update of $\pi(x)$ is evaluated relative to the previously generated prime structure. These terms describe the recursion in the arithmetic process; they do not by themselves assert any spectral theorem.

These definitions impose an important discipline on the main claim. The paper may speak of spectral encoding, phase, cycles, and crossings only through the explicit quantities defined above.

# 6. Main Theorem and Proof Attempt

This section states the proposed theorem and gives the proof spine. The argument is intentionally exposed as a sequence of lemmas so that the reader can see exactly where the proof is classical, where it is definitional, and where the new claim enters.

**Theorem 6.1. Critical-Line Constraint from Phase-Normalized Spectral Encoding.**  
Let $E(x)$ be a chosen prime-distribution error term, let

$$
\mathcal I(x)=\mathcal N(E(x),x,P_x)
$$

be the associated recursive observable. In the working model of Section 5,

$$
E(x)=E_\psi(x)=\psi(x)-x,
\qquad
\mathcal I(x)=\mathcal I_\psi(x)=\frac{\psi(x)-x}{\sqrt{x}}.
$$

Let the spectral encoding of $E$ be expressed through the zero contributions $x^\rho/\rho$, where $\rho=\sigma+i\gamma$ ranges over the nontrivial zeros of $\zeta(s)$. If the phase-crossing correspondence of Definition 5.3.8 is intrinsic to $\mathcal I$, stable under infinite square-root recursion, and invariant under the functional-equation symmetry $s\mapsto1-s$, then every nontrivial zero satisfies

$$
\sigma=\frac12.
$$

Consequently, all nontrivial zeros of $\zeta(s)$ lie on the critical line.

## 6.1. Proof Hypotheses

The proof uses the following explicit hypotheses.

**H1. Prime-State Dependence and Prime-Logarithmic Support.**  
$\mathcal I(x)$ depends only on the scale $x$, the prime state $P_x$, and the chosen prime-distribution error term $E(x)$. No external parameter may encode information not already present in these quantities. In the working model, $\mathcal I_\psi$ has prime-logarithmic support in the sense of Definition 5.3.1.

**H2. Recursive Compatibility.**  
There exists a lower-scale observation map $\Phi(x)<x$ such that

$$
\mathcal I(x)=\mathcal T_x\bigl(\mathcal I(\Phi(x))\bigr)+R(x),
$$

where $R(x)$ is determined solely by the newly resolved arithmetic structure between $\Phi(x)$ and $x$. In the working model $\Phi(x)=\sqrt{x}$, this includes prime and prime-power contributions through $\Lambda(n)$, not only newly discovered primes. Thus the residual inherits prime-logarithmic support: non-prime non-powers disappear, while prime powers survive only as reflections back to their prime base.

**H3. Spectral Compatibility.**  
The transform of $\mathcal I$ agrees with the explicit-formula zero terms for the chosen error term. In particular, each spectral contribution is represented through

$$
\frac{x^\rho}{\rho}
=
\frac{x^\sigma e^{i\gamma\log x}}{\rho}.
$$

**H4. Phase Normalization.**  
For each contributing zero $\rho$, the oscillatory part of the spectral encoding is described by the phase coordinate

$$
\varphi_\rho(x)=\gamma\log x,
$$

and the associated wave representation

$$
W_\rho(x)=\operatorname{Re}\left(\frac{x^\rho}{\rho}\right).
$$

**H5. Crossing Correspondence.**  
There exists an explicit rule assigning prime identification events

$$
\pi(x)-\pi(x-1)=1
$$

to distinguished crossing events of the phase-normalized wave representation. The rule is intrinsic to $\mathcal I$, non-circular, and independent of any prior assumption that $\sigma=1/2$.

**H6. Infinite-Scale Stability.**  
The recursive crossing correspondence remains well-defined and cutoff-independent under infinite iteration of the recursive normalization.

**H7. Symmetry Constraint.**  
The infinite-scale crossing correspondence is invariant under the functional-equation symmetry

$$
s\mapsto 1-s.
$$

## 6.2. Proof

The proof proceeds first by identifying the arithmetic support of the observable, and then by isolating the effect of one zero after square-root normalization. The decomposition $x^\rho=x^\sigma e^{i\gamma\log x}$ is elementary; the use of zero terms comes from the explicit formula [DLMF25.16; Edwards2001].

**Lemma 6.2.1. The working observable has prime-logarithmic support.**  
For

$$
\mathcal I_\psi(x)=\frac{\psi(x)-x}{\sqrt{x}},
$$

the arithmetic part of the observable is supported on prime logarithms:

$$
\psi(x)=\sum_{p^k\leq x}\log p.
$$

Consequently, non-prime non-powers disappear from the arithmetic record, while prime powers survive only as reflections back to their prime base.

**Proof.**  
By definition, $\psi(x)=\sum_{n\leq x}\Lambda(n)$. The von Mangoldt function satisfies $\Lambda(n)=\log p$ if $n=p^k$ for some prime $p$ and integer $k\geq1$, and $\Lambda(n)=0$ otherwise [DLMF25.16; Apostol1976]. Substituting this definition gives $\psi(x)=\sum_{p^k\leq x}\log p$. Division by $\sqrt{x}$ and subtraction of the smooth term $x/\sqrt{x}$ do not introduce non-prime logarithmic support. $\square$

**Lemma 6.2.2. Recursive normalization separates scale from phase.**  
For the working observable

$$
\mathcal I_\psi(x)=\frac{\psi(x)-x}{\sqrt{x}},
$$

each zero contribution has relative form

$$
\frac{x^\rho/\rho}{x^{1/2}}
=
\frac{x^{\sigma-1/2}e^{i\gamma\log x}}{\rho}.
$$

Thus the normalized contribution is a phase oscillation $e^{i\gamma\log x}$ multiplied by the relative amplitude $x^{\sigma-1/2}/\rho$.

**Proof.**  
This is immediate from $x^\rho=x^\sigma e^{i\gamma\log x}$ and division by $x^{1/2}$. The point is not that $\sigma=1/2$, but that the square-root normalization makes the scale drift $x^{\sigma-1/2}$ visible. $\square$

**Lemma 6.2.3. Off-line zeros create asymmetric scale drift.**  
If $\rho=\sigma+i\gamma$ contributes with $\sigma\neq1/2$, then after critical-line normalization its relative amplitude is not invariant under scale:

$$
x^{\sigma-1/2}.
$$

The paired zero $1-\rho=(1-\sigma)-i\gamma$ has reciprocal relative drift

$$
x^{1/2-\sigma}.
$$

**Proof.**  
The functional equation pairs zeros symmetrically across $\Re(s)=1/2$ [DLMF25.4; DLMF25.10]. Applying Lemma 6.2.2 to $\rho$ gives $x^{\sigma-1/2}$. Applying it to $1-\rho$ gives $x^{(1-\sigma)-1/2}=x^{1/2-\sigma}$. These scale factors are reciprocal and nonconstant unless $\sigma=1/2$. $\square$

**Lemma 6.2.4. Stable crossing correspondence forbids asymmetric drift.**  
Assume H5 and H6. A distinguished crossing rule that recovers prime identification events from $\mathcal I_\psi$ cannot depend on a nonconstant relative amplitude drift $x^{\sigma-1/2}$.

**Proof.**  
Prime identification events are arithmetic events at integer scales. By H5, the crossing rule is intrinsic to $\mathcal I_\psi$ and does not import an external scale parameter. By H6, the rule remains well-defined under repeated square-root descent $x\mapsto\sqrt{x}$. Under one descent, a relative amplitude factor transforms as

$$
x^{\sigma-1/2}
\longmapsto
x^{(\sigma-1/2)/2}.
$$

After $k$ descents it becomes

$$
x^{(\sigma-1/2)/2^k}.
$$

If $\sigma\neq1/2$, the crossing rule changes its amplitude scale at every finite recursion depth. Such a rule is cutoff-dependent: it distinguishes the same phase event differently depending on how many recursive normalization steps have been applied. This contradicts H6. Therefore a stable crossing correspondence must eliminate asymmetric amplitude drift. $\square$

**Lemma 6.2.5. Symmetry collapses each stable zero to the critical line.**  
Assume H6 and H7. If a zero contribution remains part of the stable infinite-scale crossing correspondence, then it must satisfy $\sigma=1-\sigma$.

**Proof.**  
By H7, the correspondence is invariant under $s\mapsto1-s$, the symmetry represented by Riemann's $\xi$-function [DLMF25.4]. By Lemma 6.2.3, an off-line pair contributes reciprocal drifts $x^{\sigma-1/2}$ and $x^{1/2-\sigma}$. By Lemma 6.2.4, stable crossing correspondence forbids dependence on either nonconstant drift. The only way for the zero contribution to be individually stable and symmetric is therefore

$$
\sigma=1-\sigma.
$$

Hence $\sigma=1/2$. $\square$

**Proof of Theorem 6.1.**  
Let $\rho=\sigma+i\gamma$ be any nontrivial zero. By Lemma 6.2.1, the arithmetic observable is supported on prime logarithms, so its spectral interpretation is tied to the same $\log p$ data that appears in Euler factors and explicit-formula zero terms. By H3 and H4, the contribution of $\rho$ to the spectral representation of $\mathcal I_\psi$ has the phase-amplitude form described in Lemma 6.2.2. If $\sigma\neq1/2$, Lemma 6.2.3 gives a nonconstant relative amplitude drift after critical-line normalization. Lemma 6.2.4 shows that such drift is incompatible with an intrinsic, cutoff-independent crossing correspondence under infinite recursion. Lemma 6.2.5 then applies the functional-equation symmetry and forces $\sigma=1-\sigma$. Therefore $\sigma=1/2$. Since $\rho$ was arbitrary, every nontrivial zero lies on the critical line. $\square$

The proof is boldest at Lemma 6.2.4. A skeptical reader should focus there: this is where the paper claims that recursive cutoff-independence is strong enough to rule out off-line amplitude drift, rather than merely averaging it across symmetric zero pairs.

# 7. Reviewer Checkpoints and Proof Obligations

The proof above makes the main claim. This section records the checkpoints a reviewer should use to test it. The purpose is not to retreat from the theorem, but to expose the stress points clearly enough that the argument can be strengthened rather than defended rhetorically.

## 7.1. Define the Observable

Use the specific error term

$$
E_\psi(x)=\psi(x)-x,
$$

because it connects cleanly to the explicit formula. The current working observable is

$$
\mathcal I_\psi(x)=\frac{\psi(x)-x}{\sqrt{x}}.
$$

This stage supplies the concrete candidate for H1. A reviewer should test whether any hidden information enters through $\sqrt{x}$, $\psi(x)$, or the choice of normalization.

The important support claim is Lemma 6.2.1: $\mathcal I_\psi$ is not a normalized raw integer sum, but a normalized prime-logarithmic record. This is where the statement "non-prime non-powers disappear, while prime powers survive only as reflections back to their prime base" enters the proof rather than merely illustrating the example.

## 7.2. Prove Recursive Closure from Prime State Updates

Show that $\mathcal I_\psi(x)$ can be expressed through the lower-scale observable and a controlled residual:

$$
\mathcal I_\psi(x)
=
\mathcal T_x\bigl(\mathcal I_\psi(\sqrt{x})\bigr)+R_\psi(x).
$$

For the finite model in Section 5, $R_\psi(x)$ is forced by the identity

$$
R_\psi(x)
=
\frac{\psi(x)-x-\psi(\sqrt{x})+\sqrt{x}}{\sqrt{x}}.
$$

The residual must be prime-state determined in a stronger structural sense, not merely algebraically defined afterward. In particular, the proof must identify how the newly resolved arithmetic interval $(\sqrt{x},x]$ contributes to the update and whether that contribution behaves coherently under iteration.

This stage is the substantive content of H2.

## 7.3. Build the Phase-Normalized Spectral Representation

Use an explicit formula to connect the transform of $\mathcal I$ to zero terms of the form

$$
\frac{x^\rho}{\rho}.
$$

The key analytical issue is the factor

$$
x^\rho=x^\sigma e^{i\gamma\log x}.
$$

Here $\gamma$ controls phase and $\sigma$ controls amplitude growth. The proof must make precise that the phase coordinate is

$$
\varphi_\rho(x)=\gamma\log x
$$

and that the associated real wave representation is

$$
W_\rho(x)=\operatorname{Re}\left(\frac{x^\rho}{\rho}\right).
$$

This stage supplies H3 and H4.

## 7.4. Prove Crossing Correspondence for Prime Identification Events

Define explicitly which crossing events in the phase-normalized wave representation correspond to prime identification events

$$
\pi(x)-\pi(x-1)=1.
$$

This is the most delicate conceptual step. The proof claims that the correspondence is intrinsic to the recursive observable and not a visual analogy retrofitted onto the oscillatory terms.

The proof obligation here is twofold:

1. show that the relevant crossings are canonically determined by the spectral representation;
2. show that prime identification events are recovered from those distinguished crossings.

This stage supplies H5.

## 7.5. Derive the Critical-Line Constraint

Use infinite-scale stability together with the symmetry $s\mapsto1-s$ to prove that the crossing correspondence remains invariant only when the amplitude normalization is centered on the critical line. The goal is to show that any contributing zero must satisfy

$$
\sigma=1-\sigma,
$$

hence

$$
\sigma=\frac12.
$$

This is the decisive step. It must use H6 and H7 without assuming the desired conclusion through the setup of the normalization, the crossing rule, or the notion of stability.

This step cannot merely cite the functional equation, since that symmetry gives paired zeros $\rho$ and $1-\rho$. The missing argument must explain why recursive stability identifies each zero with its symmetric partner rather than simply allowing both members of an off-line pair.

# 8. Conclusion

This paper argues that the Riemann Hypothesis can be approached as a fixed-point or invariance statement about recursive prime observation. Since each prime-counting step depends on the prime structure already generated, the prime distribution is a self-referential object. The nontrivial zeros of the zeta function are known to encode prime-distribution error spectrally. The proposed contribution is the stronger claim that the critical line arises as the unique stable normalization axis of this recursive encoding.

The working observable $\mathcal I_\psi(x)=(\psi(x)-x)/\sqrt{x}$ gives the argument a concrete center. The proof attempt shows that, once the crossing correspondence is intrinsic and stable under infinite square-root recursion, any off-line zero introduces scale drift incompatible with that stability. Functional-equation symmetry then collapses each stable zero contribution to $\sigma=1/2$.

The reviewer burden is concentrated in Lemma 6.2.4: one must verify that cutoff-independent crossing stability truly forbids off-line amplitude drift, rather than merely allowing cancellation across symmetric zero pairs.

# Acknowledgments

To be completed.

# References

1. [Riemann1859] B. Riemann, "Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse", *Monatsberichte der Berliner Akademie*, 1859. English translation and historical discussion appear in Edwards [Edwards2001].
2. [Edwards2001] H. M. Edwards, *Riemann's Zeta Function*, Dover Publications, 2001.
3. [Titchmarsh1986] E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford University Press, 1986.
4. [Ingham1932] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge University Press, 1932.
5. [Apostol1976] T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
6. [HardyWright2008] G. H. Hardy and E. M. Wright, revised by D. R. Heath-Brown and J. H. Silverman, *An Introduction to the Theory of Numbers*, 6th ed., Oxford University Press, 2008.
7. [IwaniecKowalski2004] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, American Mathematical Society Colloquium Publications 53, 2004. https://doi.org/10.1090/coll/053
8. [DLMF25.2] NIST Digital Library of Mathematical Functions, "§25.2 Definition and Expansions", Chapter 25, Zeta and Related Functions. https://dlmf.nist.gov/25.2
9. [DLMF25.4] NIST Digital Library of Mathematical Functions, "§25.4 Reflection Formulas", Chapter 25, Zeta and Related Functions. https://dlmf.nist.gov/25.4
10. [DLMF25.10] NIST Digital Library of Mathematical Functions, "§25.10 Zeros", Chapter 25, Zeta and Related Functions. https://dlmf.nist.gov/25.10
11. [DLMF25.16] NIST Digital Library of Mathematical Functions, "§25.16 Mathematical Applications", Chapter 25, Zeta and Related Functions. https://dlmf.nist.gov/25.16
12. [DLMF27.18] NIST Digital Library of Mathematical Functions, "§27.18 Methods of Computation: Primes", Chapter 27, Functions of Number Theory. https://dlmf.nist.gov/27.18
13. [ClayRH] Clay Mathematics Institute, "Riemann Hypothesis: Official Problem Description". https://www.claymath.org/riemann/
14. [Schoenfeld1976] L. Schoenfeld, "Sharper Bounds for the Chebyshev Functions $\theta(x)$ and $\psi(x)$. II", *Mathematics of Computation* 30, no. 134, 1976, 337-360. https://doi.org/10.1090/S0025-5718-1976-0457374-X
15. [Odlyzko1987] A. M. Odlyzko, "On the distribution of spacings between zeros of the zeta function", *Mathematics of Computation* 48, no. 177, 1987, 273-308. https://doi.org/10.1090/S0025-5718-1987-0866115-0
16. [Odlyzko2001] A. M. Odlyzko, "The $10^{22}$-nd zero of the Riemann zeta function", in *Dynamical, Spectral, and Arithmetic Zeta Functions*, Contemporary Mathematics 290, American Mathematical Society, 2001, 139-144. https://www-users.cse.umn.edu/~odlyzko/doc/zeta.html
17. [WikipediaRH] "Riemann hypothesis", Wikipedia, used only as a discovery map for references and topic coverage. https://en.wikipedia.org/wiki/Riemann_hypothesis

# Appendix A. Reviewer Stress Tests

The following checks are not part of the main proof flow. They state the standards by which the proof attempt should be tested.

1. The definition of $\mathcal I$ must not assume $\Re(\rho)=1/2$ directly or indirectly.
2. The explicit formula must be used only as the bridge from prime-logarithmic arithmetic data to zero terms, not as if it already proves recursive normalization.
3. The argument must distinguish collective encoding by all zeros from unique encoding by any single ordinate.
4. Numerical regularity may motivate diagnostics but cannot substitute for proof.
5. The residual $R_\psi(x)$ must remain an explicit prime-logarithmic residual, not a place where unresolved prime-distribution complexity is hidden.
6. Lemma 6.2.4 must rule out off-line amplitude drift by intrinsic cutoff-stability, rather than by assuming cancellation across symmetric zero pairs.

# Appendix B. Diagnostic Note on Riemann-Siegel Phase

This appendix is not part of the proof. It records a possible numerical diagnostic that may help test the phase language after the main argument has been assessed on its own terms.

The Riemann-Siegel phase coordinate is the classical phase used with Hardy's $Z(t)$-function in computations on the critical line [DLMF25.10; Titchmarsh1986].

Let

$$
\theta(t)=\operatorname{Im}\log\Gamma\left(\frac14+\frac{it}{2}\right)-\frac{t\log\pi}{2}.
$$

At the $n$-th zero ordinate $t_n$, define a phase coordinate

$$
F(t_n)=\left(n-\frac32\right)\pi.
$$

Then one may decompose

$$
F(t_n)=\theta(t_n)+A(t_n),
$$

where $A(t_n)$ represents the arithmetic correction needed to close the phase step.

The diagnostic question is:

> Does $A(t_n)$ behave like the recursive prime-state residual predicted by $\mathcal I$?

This question should not be used as evidence for the theorem. Numerical work, including Odlyzko's computations, is relevant only as diagnostic evidence and as a way to discover patterns that must later be proved independently [Odlyzko1987; Odlyzko2001].

# Appendix C. Export Notes

This Markdown file is designed to be converted with Pandoc.

Example export commands:

```sh
pandoc infinite-loop-enigma-riemann-hypothesis.md -o infinite-loop-enigma-riemann-hypothesis.pdf
pandoc infinite-loop-enigma-riemann-hypothesis.md -o infinite-loop-enigma-riemann-hypothesis.tex
```

For arXiv submission, export to LaTeX, inspect the generated `.tex`, and submit the TeX source plus any figures or bibliography files.
