# Asymptotic Normalization and Continuous Change

## Definition

A quantity behaves asymptotically when it approaches a limiting value as a parameter grows without bound. The value need not equal the limit at any finite stage; it only needs to become arbitrarily close.

For the recursive-removal process,

$$
\left(1-\frac{1}{n}\right)^n
$$

approaches

$$
\frac{1}{e} \approx 0.367879
$$

as \(n \to \infty\).

## Numerical Approach

| \(n\) | Value of \(\left(1-\frac{1}{n}\right)^n\) |
|---:|---:|
| \(2\) | \(0.25\) |
| \(10\) | \(\approx 0.349\) |
| \(100\) | \(\approx 0.366\) |
| \(10000\) | \(\approx 0.36786\) |

The values approach \(1/e\), but no finite row in the table is itself the limit.

## The Role of \(e\)

The constant \(e\) is not an average. It is the natural scaling constant for quantities whose rate of change is proportional to their current amount.

In the recursive-removal model, the update rule is

$$
C_{k+1} = C_k\left(1-\frac{1}{n}\right).
$$

Each step depends on the current state. The process is therefore multiplicative rather than additive.

As the individual changes become infinitesimally small while the number of changes becomes indefinitely large, the discrete product

$$
\left(1-\frac{1}{n}\right)^n
$$

converges to

$$
e^{-1}.
$$

## General Principle

Many small relative changes accumulate exponentially:

$$
\text{many small relative changes}
\quad\longrightarrow\quad
e^{\text{total relative change}}.
$$

For total relative change \(-1\), the resulting factor is

$$
e^{-1}.
$$

Thus \(e\) acts as the canonical normalization constant for continuous compounding. It appears in compound interest, radioactive decay, population growth, cooling, probability, and differential equations because all these settings involve proportional change over time.

## Course Note

The structural transition is:

$$
\underbrace{\text{local proportional step}}_{1/n}
\quad+\quad
\underbrace{\text{recursive update}}_{n\text{ times}}
\quad\xrightarrow[n\to\infty]{}\quad
\underbrace{\text{global exponential factor}}_{e^{-1}}.
$$

The constant \(e\) records how local proportional change becomes global exponential behavior in the continuous limit.
