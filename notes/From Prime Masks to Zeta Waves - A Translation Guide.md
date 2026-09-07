# From Prime Masks to Zeta Waves: A Translation Guide

## No secrets—only changes of representation

The Riemann zeta function is often said to hide the “fundamental secrets” of the primes. From the viewpoint of periodic prime masks, many of these supposed mysteries are less mysterious. They are familiar structures seen after a change of mathematical language.

The sieve describes primes spatially: each prime $p$ removes a periodic set of positions from the integer line. Fourier analysis describes the same periodicity through phase waves. The logarithm translates multiplication into addition. The Mellin transform translates scale into frequency. Euler's product gathers the contribution of every prime, and Riemann's explicit formula translates the resulting analytic spectrum back into prime-counting fluctuations.

The guiding path is

$$
\boxed{
\text{periodic masks}
\longrightarrow
\text{phase waves}
\longrightarrow
\text{multiplicative spectrum}
\longrightarrow
\text{zeta zeros}
\longrightarrow
\text{prime-counting oscillations}.}
$$

What looks like a secret in one representation may be intuitive in another.

## 1. The periodic prime mask

For every prime $p$, define

$$
B_p(n)=
\begin{cases}
0,&p\mid n,\\
1,&p\nmid n.
\end{cases}
$$

The mask repeats every $p$ integers:

$$
B_p(n+p)=B_p(n).
$$

Thus $B_2$ blocks every second position, $B_3$ every third position, and $B_5$ every fifth position. Combining the masks gives the familiar sieve pattern.

The word **wave** refers first to this periodic recurrence. The masks are discrete square-wave patterns: their values jump between $0$ and $1$, but their structures repeat with exact periods.

The wave language becomes more than a metaphor when the square-wave mask is expanded into complex phases.

## 2. Translation I: from a bit mask to pure phase waves

A pure phase wave has the form

$$
e^{i\phi}.
$$

Its amplitude never changes because

$$
|e^{i\phi}|=1.
$$

Changing $\phi$ rotates the phase around the unit circle without enlarging or shrinking the wave.

A periodic bit mask is not represented by one such phase wave. It is represented by a **finite superposition** of pure phase waves. For a prime $p$, the indicator of divisibility is

$$
D_p(n)
=
\mathbf 1_{p\mid n}
=
\frac1p\sum_{r=0}^{p-1}e^{2\pi i rn/p}.
$$

This formula has two possible outcomes.

### When $p$ divides $n$

If $p\mid n$, then every phase equals $1$:

$$
e^{2\pi i rn/p}=1.
$$

All $p$ waves align, so

$$
D_p(n)=\frac1p(1+1+\cdots+1)=1.
$$

### When $p$ does not divide $n$

If $p\nmid n$, the phases are distributed around the unit circle. Their vector sum cancels:

$$
\sum_{r=0}^{p-1}e^{2\pi i rn/p}=0,
$$

and therefore

$$
D_p(n)=0.
$$

The transparent mask is the complement:

$$
\boxed{
B_p(n)
=
1-D_p(n)
=
1-\frac1p\sum_{r=0}^{p-1}e^{2\pi i rn/p}.}
$$

This is an exact translation:

$$
\begin{array}{ccl}
\text{divisibility bit}
&\longleftrightarrow&
\text{phase alignment},\\
\text{nondivisibility bit}
&\longleftrightarrow&
\text{phase cancellation}.
\end{array}
$$

The zeros and ones of the sieve are therefore recoverable from interference among constant-amplitude phase waves.

## 3. A concrete example: the mask for $3$

Let

$$
\omega=e^{2\pi i/3}.
$$

The three cube roots of unity satisfy

$$
1+\omega+\omega^2=0.
$$

The divisibility indicator becomes

$$
D_3(n)=\frac13\left(1+\omega^n+\omega^{2n}\right).
$$

If $3\mid n$, then $\omega^n=\omega^{2n}=1$, so $D_3(n)=1$. Otherwise, the three phases cancel and $D_3(n)=0$. Hence

$$
B_3(n)=1-D_3(n)
$$

reproduces the periodic mask

$$
1,1,0,1,1,0,1,1,0,\ldots.
$$

The mask and the phase sum are not competing descriptions. They are the same periodic object in two coordinate systems.

## 4. Translation II: from many masks to an interference field

For the first $k$ primes, define the combined mask

$$
M_k(n)=\prod_{j=1}^{k}B_{p_j}(n).
$$

Since multiplication of zeros and ones acts as logical AND,

$$
M_k(n)=1
$$

exactly when none of the primes $p_1,\ldots,p_k$ divides $n$.

Substituting the phase representation of every mask gives

$$
M_k(n)
=
\prod_{j=1}^{k}
\left(
1-\frac1{p_j}
\sum_{r=0}^{p_j-1}e^{2\pi i rn/p_j}
\right).
$$

The nested sieve can therefore be viewed as a structured interference field. Every newly introduced prime contributes a fresh set of phases, while multiplying the entire field inherited from the preceding primes.

The combined period is the primorial

$$
P_k=\prod_{j=1}^{k}p_j.
$$

This explains why a stack of individually simple periodic masks produces a complicated-looking pattern: each new period contains and refines all the earlier periods.

The apparent irregularity of prime candidates is not the absence of structure. It is the visible trace of many exact periodic structures interacting at once.

## 5. Translation III: from multiplication to logarithmic motion

Prime structure is multiplicative. Waves are easiest to compare in an additive coordinate. The logarithm provides the translation:

$$
\log(ab)=\log a+\log b.
$$

In particular,

$$
\log(p^m)=m\log p.
$$

Thus repeated powers of a prime become equally spaced repetitions in logarithmic space:

$$
p,p^2,p^3,\ldots
\quad\longleftrightarrow\quad
\log p,2\log p,3\log p,\ldots.
$$

This translation explains why $\log p$ repeatedly appears as a frequency, length, or period in spectral descriptions of the primes. Multiplicative repetition on the integer line becomes additive recurrence after applying the logarithm.

## 6. Translation IV: from prime repetition to Euler's product

For $\operatorname{Re}(s)>1$, one prime contributes the geometric series

$$
1+p^{-s}+p^{-2s}+p^{-3s}+\cdots
=
\frac1{1-p^{-s}}.
$$

Because

$$
p^{-ms}=e^{-ms\log p},
$$

the powers $p^m$ become repeated steps of size $\log p$ in the exponential coordinate.

Multiplying over all primes gives Euler's product:

$$
\boxed{
\zeta(s)
=
\prod_p\frac1{1-p^{-s}}
=
\sum_{n=1}^{\infty}\frac1{n^s}.}
$$

Unique factorization ensures that expanding the product generates every positive integer exactly once.

From the mask viewpoint, Euler's product is not mysterious. It is another way of assembling the complete multiplicative contribution of the primes. The mask product records which positions the primes exclude; the Euler product records every multiplicative combination the primes generate.

These are complementary views:

$$
\begin{array}{ccl}
\text{sieve product}
&:&\text{remove multiples},\\
\text{Euler product}
&:&\text{generate factorizations}.
\end{array}
$$

One observes the multiplicative structure through exclusion; the other observes it through construction.

## 7. Translation V: why prime powers appear

Take the logarithmic derivative of Euler's product:

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_p\sum_{m=1}^{\infty}
\frac{\log p}{p^{ms}}.
$$

Using the von Mangoldt function

$$
\Lambda(n)=
\begin{cases}
\log p,&n=p^m,\\
0,&\text{otherwise},
\end{cases}
$$

this becomes

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s}.
$$

Prime powers are therefore not an unexplained complication. They are the repeated appearances of the same prime generator. In wave language, $p^m$ is the $m$th repetition of the fundamental logarithmic step $\log p$.

This is closely analogous to a primitive periodic orbit and its repeated traversals in a trace formula.

## 8. Translation VI: from scale to spectral frequency

Ordinary Fourier analysis is adapted to translations such as $x\mapsto x+a$. Prime structure is adapted to scaling such as $x\mapsto ax$. The Mellin transform is the Fourier-like transform for multiplicative scale:

$$
\mathcal M[f](s)
=
\int_0^\infty f(x)x^{s-1}\,dx.
$$

Writing $x=e^u$ gives

$$
x^{s-1}\,dx=e^{su}\,du.
$$

Thus Mellin analysis on $x>0$ becomes exponential or Fourier analysis in the logarithmic coordinate $u=\log x$.

This demystifies the complex variable $s$. Its two coordinates play different roles:

$$
s=\sigma+it.
$$

- The real part $\sigma$ controls growth or decay with scale.
- The imaginary part $t$ controls oscillation in $\log x$.

The complex plane is therefore a natural observation space for multiplicative arithmetic.

## 9. Translation VII: from zeta zeros to prime-counting waves

Define the weighted prime-power count

$$
\psi(x)=\sum_{n\le x}\Lambda(n).
$$

Riemann's explicit formula has the form

$$
\psi(x)
=
x
-\sum_\rho\frac{x^\rho}{\rho}
+\text{correction terms},
$$

where $\rho$ runs over the nontrivial zeros of $\zeta(s)$.

Write

$$
\rho=\beta+i\gamma.
$$

Then

$$
x^\rho=x^\beta e^{i\gamma\log x}.
$$

The translation is immediate:

$$
\begin{array}{ccl}
\beta&\longleftrightarrow&\text{amplitude exponent},\\
\gamma&\longleftrightarrow&\text{logarithmic frequency},\\
x^\rho&\longleftrightarrow&\text{one prime-counting wave mode}.
\end{array}
$$

The zeros do not create isolated spikes only at primes. More precisely, their combined modes reconstruct the fluctuations of the weighted prime-power counting function around its smooth main term.

What is often described as the zeros “controlling the primes” is therefore a translation statement: the discrete irregularities of prime counting become a superposition of oscillatory modes in logarithmic scale.

## 10. Translation VIII: why the critical line is balanced

The completed zeta function satisfies

$$
\xi(s)=\xi(1-s).
$$

If a zero has real part $\beta$, reflection pairs it with a mode whose real part is $1-\beta$. Their amplitude scales are

$$
x^\beta
\qquad\text{and}\qquad
x^{1-\beta}.
$$

Their geometric mean is

$$
\sqrt{x^\beta x^{1-\beta}}=\sqrt{x}.
$$

Normalize one mode by this reflection-balanced scale:

$$
\frac{x^\rho}{\sqrt{x}}
=
x^{\beta-1/2}e^{i\gamma\log x}.
$$

On the critical line, where $\beta=1/2$, this becomes the pure phase wave

$$
e^{i\gamma\log x},
$$

whose amplitude is always $1$. The critical-line mode changes only its phase; it does not grow or decay relative to the balanced scale.

This makes the critical line intuitive in the translation language:

> **The critical line is where a multiplicative prime-counting mode becomes a pure phase after reflection-balanced normalization.**

The Riemann Hypothesis is the claim that every nontrivial zero has this balanced real part. The translation explains what the claim means geometrically; proving that every zero obeys it remains the deeper question.

## 11. A translation table for the “mysteries”

| What appears mysterious | Translation from the mask viewpoint |
|---|---|
| Why do waves appear in prime theory? | Every periodic mask has an exact finite Fourier expansion into pure phases. |
| Why do complex numbers appear? | Complex exponentials record phase and make cancellation algebraic. |
| Why does $\log p$ appear? | The logarithm turns multiplication by primes into additive motion. |
| Why do prime powers appear? | They are repeated applications of the same prime generator. |
| Why does Euler's product encode all integers? | Unique factorization expands the prime factors into every integer exactly once. |
| Why do zeros affect prime counts? | Mellin inversion and residue contributions translate analytic singularities into counting oscillations. |
| Why is $\gamma$ frequency-like? | $e^{i\gamma\log x}$ oscillates with frequency $\gamma$ in logarithmic space. |
| Why does $\beta$ control amplitude? | $|x^\rho|=x^\beta$. |
| Why is $1/2$ a balance point? | Reflection pairs $\beta$ with $1-\beta$, whose symmetric scale is $\sqrt{x}$. |
| Why does quantum-chaos language arise? | Prime powers resemble repeated periodic orbits, while zeros resemble spectral levels in trace formulas. |

## 12. What has—and has not—been demystified

The translations above explain why the principal objects have the forms they do:

- periodic exclusion naturally admits a wave representation;
- roots of unity naturally encode divisibility;
- logarithms naturally linearize prime multiplication;
- Euler factors naturally collect repeated prime powers;
- Mellin analysis naturally converts scale into frequency;
- zeta zeros naturally appear as modes in explicit prime-counting formulas;
- the critical line naturally supplies reflection-balanced pure phases.

This removes much of the conceptual mystery. It does not remove every mathematical difficulty. In particular, the translations do not by themselves prove that all nontrivial zeros lie on the critical line. They show why that line is the uniquely balanced observation axis and why the Riemann Hypothesis is naturally expressed there.

The distinction is useful:

> **The mystery of why these structures belong together can be reduced by translation, even while the theorem governing all of their zeros remains open.**

## Closing perspective

The prime masks begin as simple binary recurrences. Fourier expansion reveals that each one is already composed of pure phase waves. Their multiplication creates a nested interference field. The logarithm unfolds multiplicative repetition into additive motion, the Mellin transform reads that motion spectrally, and the zeta function assembles the complete prime-generated structure.

From this viewpoint, the zeta function does not hide inaccessible secrets. It changes the representation. Its apparent mysteries arise because the observer encounters the spectral image before seeing the elementary periodic structures from which that image originates.

Once the translations are made visible, the route becomes intuitive:

$$
\boxed{
\text{bits}
\longleftrightarrow
\text{phases}
\longleftrightarrow
\text{periodic masks}
\longleftrightarrow
\text{prime powers}
\longleftrightarrow
\text{zeta spectrum}.}
$$

The “secrets” are relations between representations. Translation turns them into structure.

## Related notes

- [[A Wave-Based Framework for Prime Exclusion]]
- [[The Critical-Line Observer - A Quantum-Chaos Exploration|The Critical-Line Observer: A Quantum-Chaos Exploration]]
- [[../Prime Mask Alignment and the Critical-Line Observer|Prime Mask Alignment and the Critical-Line Observer]]
