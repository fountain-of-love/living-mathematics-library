# §1.7 Inequalities

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.7, `Inequalities`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Finite Sums
- Integrals
- Means
- Jensen's Inequality

### Subsections

#### 1.7(i) Finite Sums

- In this subsection $A$ and $B$ are positive constants.

Formulas:

Formula 1.7.1:

$$
\left(\sum^{n}_{j=1}a_{j}b_{j}\right)^{2}\leq\left(\sum^{n}_{j=1}a_{j}^{2}\right)\left(\sum^{n}_{j=1}b_{j}^{2}\right).
$$

Formula 1.7.2:

$$
\sum^{n}_{j=1}a_{j}b_{j}\leq\left(\sum^{n}_{j=1}a_{j}^{p}\right)^{1/p}\left(\sum^{n}_{j=1}b_{j}^{q}\right)^{1/q}.
$$

Formula 1.7.3:

$$
\left(\sum^{n}_{j=1}(a_{j}+b_{j})^{p}\right)^{1/p}\leq\left(\sum^{n}_{j=1}a_{j}^{p}\right)^{1/p}+\left(\sum^{n}_{j=1}b_{j}^{p}\right)^{1/p}.
$$


Definitions and local symbols:
- Keywords: Cauchy-Schwarz , Cauchy-Schwarz inequalities for sums and integrals , inequalities , sums and integrals
- Symbols: $j$ : integer and $n$ : nonnegative integer
- Keywords: Hlder's inequalities for sums and integrals , Hlder's , inequalities , sums and integrals
- Symbols: $j$ : integer , $n$ : nonnegative integer , $q$ : number and $p>1$
- Keywords: Minkowski's , Minkowski's inequalities for sums and series , inequalities , sums and integrals
- Symbols: $j$ : integer , $n$ : nonnegative integer and $p>1$

#### 1.7(ii) Integrals

- In this subsection $a$ and $b$ ( $>a$ ) are real constants that can be $\mp\infty$ , provided that the corresponding integrals converge. Also $A$ and $B$ are constants that are not simultaneously zero.

Formulas:

Formula 1.7.4:

$$
\left(\int_{a}^{b}f(x)g(x)\,\mathrm{d}x\right)^{2}\leq\int_{a}^{b}(f(x))^{2}\,\mathrm{d}x\int_{a}^{b}(g(x))^{2}\,\mathrm{d}x.
$$

Formula 1.7.5:

$$
\int_{a}^{b}f(x)g(x)\,\mathrm{d}x\leq\left(\int_{a}^{b}(f(x))^{p}\,\mathrm{d}x\right)^{1/p}\left(\int_{a}^{b}(g(x))^{q}\,\mathrm{d}x\right)^{1/q}.
$$

Formula 1.7.6:

$$
\left(\int_{a}^{b}(f(x)+g(x))^{p}\,\mathrm{d}x\right)^{1/p}\leq\left(\int_{a}^{b}(f(x))^{p}\,\mathrm{d}x\right)^{1/p}+\left(\int_{a}^{b}(g(x))^{p}\,\mathrm{d}x\right)^{1/p}.
$$


Definitions and local symbols:
- Keywords: Cauchy-Schwarz , Cauchy-Schwarz inequalities for sums and integrals , inequalities , sums and integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Hlder's inequalities for sums and integrals , Hlder's , inequalities , sums and integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $p>1$ and $q$ : number
- Keywords: Minkowski's , Minkowski's inequalities for sums and series , inequalities , sums and integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $p>1$

#### 1.7(iii) Means

- For the notation, see  1.2(iv) .
- with equality iff $a_{1}=a_{2}=\dots=a_{n}$ .
- with equality iff $a_{1}=a_{2}=\dots=a_{n}$ , or $r<0$ and some $a_{j}=0$ .
- with equality iff $a_{1}=a_{2}=\dots=a_{n}$ , or $s\leq 0$ and some $a_{j}=0$ .

Formulas:

Formula 1.7.7:

$$
H\leq G\leq A,
$$

Formula 1.7.8:

$$
\min(a_{1},a_{2},\dots,a_{n})\leq M(r)\leq\max(a_{1},a_{2},\dots,a_{n}),
$$

Formula 1.7.9:

$$
M(r)\leq M(s),
$$


Definitions and local symbols:
- Keywords: arithmetic mean , geometric mean , harmonic mean , inequalities , means
- Symbols: $A$ : arithmetic mean , $G$ : geometric mean and $H$ : harmonic mean
- Symbols: $n$ : nonnegative integer and $M(r)$ : weighted mean
- Symbols: $M(r)$ : weighted mean

#### 1.7(iv) Jensen's Inequality

- For $f$ integrable on $[0,1]$ , $a<f(x)<b$ , and $\phi$ convex on $(a,b)$ ( 1.4(viii) ),
- For $\exp$ and $\ln$ see  4.2 .

Formulas:

Formula 1.7.10:

$$
\phi\left(\int^{1}_{0}f(x)\,\mathrm{d}x\right)\leq\int^{1}_{0}\phi(f(x))\,\mathrm{d}x,
$$

Formula 1.7.11:

$$
\exp\left(\int^{1}_{0}\ln\left(f(x)\right)\,\mathrm{d}x\right)<\int^{1}_{0}f(x)\,\mathrm{d}x.
$$


Definitions and local symbols:
- Keywords: Jensen's , Jensen's inequality , Jensen's inequality for integrals , inequalities , integrals , sums and integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\phi(x)$ : function
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\exp z$ : exponential function , $\int$ : integral and $\ln z$ : principal branch of logarithm function

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.7](https://dlmf.nist.gov/1.7)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: Cauchy-Schwarz, Cauchy-Schwarz inequalities for sums and integrals, inequalities, sums and integrals, Hlder's inequalities for sums and integrals, Hlder's, Minkowski's, Minkowski's inequalities for sums and series, arithmetic mean, geometric mean, harmonic mean, means, Jensen's, Jensen's inequality, Jensen's inequality for integrals, integrals.

### Source Notes

- See Hardy et al. ( 1967 , pp. 1-32) .
- See Hardy et al. ( 1967 , pp. 130-147) .
- See Hardy et al. ( 1967 , pp. 14, 17, 26) .
- See Hardy et al. ( 1967 , pp. 132, 151) .
