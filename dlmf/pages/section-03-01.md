# §3.1 Arithmetics and Error Measures

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.1, `Arithmetics and Error Measures`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Floating-Point Arithmetic
- Interval Arithmetic
- Rational Arithmetics
- Level-Index Arithmetic
- Error Measures

### Subsections

#### 3.1(i) Floating-Point Arithmetic

- Computer arithmetic is described for the binary based system with base 2; another system that has been used is the hexadecimal system with base 16.
- A nonzero normalized binary floating-point machine number $x$ is represented as
- where $s$ is equal to $1$ or $0$ , each $b_{j}$ , $j\geq 1$ , is either $0$ or $1$ , $b_{1}$ is the most significant bit , $p$ ( $\in\mathbb{N}$ ) is the number of significant bits $b_{j}$ , $b_{p-1}$ is the least significant bit , $E$ is an integer called the exponent , $b_{0}.b_{1}b_{2}\dots b_{p-1}$ is the significand , and $f=.b_{1}b_{2}\dots b_{p-1}$ is the fractional part .
- The set of machine numbers $\mathbb{R}_{{\rm fl}}$ is the union of $0$ and the set
- with $b_{0}=1$ and all allowable choices of $E$ , $p$ , $s$ , and $b_{j}$ .
- Let $E_{{\rm min}}\leq E\leq E_{{\rm max}}$ with $E_{{\rm min}}<0$ and $E_{{\rm max}}>0$ . For given values of $E_{{\rm min}}$ , $E_{{\rm max}}$ , and $p$ , the format width in bits $N$ of a computer word is the total number of bits: the sign (one bit), the significant bits $b_{1},b_{2},\dots,b_{p-1}$ ( $p-1$ bits), and the bits allocated to the exponent (the remaining $N-p$ bits). The integers $p$ , $E_{{\rm min}}$ , and $E_{{\rm max}}$ are characteristics of the machine. The machine epsilon $\epsilon_{M}$ , that is, the distance between $1$ and the next larger machine number with $E=0$ is given by $\epsilon_{M}=2^{-p+1}$ . The machine precision is $\frac{1}{2}\epsilon_{M}=2^{-p}$ . The lower and upper bounds for the absolute values of the nonzero machine numbers are given by

Formulas:

Formula 3.1.1:

$$
x=(-1)^{s}\cdot(b_{0}.b_{1}b_{2}\dots b_{p-1})\cdot 2^{E},
$$

Formula 3.1.2:

$$
(-1)^{s}2^{E}\sum_{j=0}^{p-1}b_{j}2^{-j},
$$

Formula 3.1.3:

$$
N_{{\rm min}}\equiv 2^{E_{{\rm min}}}\leq|x|\leq 2^{E_{{\rm max}}+1}\left(1-2^{-p}\right)\equiv N_{{\rm max}}.
$$

Formula 3.1.4:

$$
x=(1.b_{1}b_{2}\dots b_{p-1}b_{p}b_{p+1}\dots)\cdot 2^{E},
$$

Formula:

$$
\displaystyle x_{-}
$$

Formula:

$$
\displaystyle x_{+}
$$


Definitions and local symbols:
- Keywords: arithmetics , binary number system , bits , exponent , floating-point , floating-point arithmetic , format width , fractional part , hexadecimal number system , machine epsilon , machine number , machine precision , overflow , significand , significant , underflow
- Symbols: $b_{p}$ : bit , $s$ : sign , $p$ : number of significant bits and $E$ : exponent
- Symbols: $b_{p}$ : bit , $s$ : sign , $p$ : number of significant bits and $E$ : exponent
- Defines: $N_{{\rm min}}$ : underflow (locally) and $N_{{\rm max}}$ : overflow (locally)
- Symbols: $\equiv$ : equals by definition , $p$ : number of significant bits , $E_{{\rm min}}$ : minimum exponent and $E_{{\rm max}}$ : maximum exponent
- Keywords: IEEE standard , double precision , floating-point arithmetic , single precision
- Symbols: $s$ : sign , $p$ : number of significant bits , $E$ : exponent , $f$ : fractional part and $N$ : number of bits in floating point
- Keywords: by chopping , down , floating-point arithmetic , rounding , symmetric , to nearest machine number
- Symbols: $b_{p}$ : bit , $p$ : number of significant bits and $E$ : exponent
- Symbols: $b_{p}$ : bit , $p$ : number of significant bits , $E$ : exponent and $\epsilon_{M}$ : machine epsilon

#### 3.1(ii) Interval Arithmetic

- Interval arithmetic is intended for bounding the total effect of rounding errors of calculations with machine numbers. With this arithmetic the computed result can be proved to lie in a certain interval, which leads to validated computing with guaranteed and rigorous inclusion regions for the results.
- Let $G$ be the set of closed intervals $\{[a,b]\}$ . The elementary arithmetical operations on intervals are defined as follows:
- where $*\in\{+,-,\cdot,/\}$ , with appropriate roundings of the end points of $I*J$ when machine numbers are being used. Division is possible only if the divisor interval does not contain zero.
- A basic text on interval arithmetic and analysis is Alefeld and Herzberger ( 1983 ) , and for applications and further information see Moore ( 1979 ) and Petkovi and Petkovi ( 1998 ) . The last reference includes analogs for arithmetic in the complex plane $\mathbb{C}$ . For interval arithmetic, one should refer to the IEEE Standards for Interval Arithmetic IEEE ( 2015 , 2018 ) .

Formulas:

Formula 3.1.6:

$$
I*J=\{x*y\,|\,x\in I,y\in J\},
$$


Definitions and local symbols:
- Keywords: arithmetics , interval , interval arithmetic , validated computing
- Symbols: $\in$ : element of and $G$ : set of closed intervals

#### 3.1(iii) Rational Arithmetics

- Computer algebra systems use exact rational arithmetic with rational numbers $p/q$ , where $p$ and $q$ are multi-length integers. During the calculations common divisors are removed from the rational numbers, and the final results can be converted to decimal representations of arbitrary length. For further information see Matula and Kornerup ( 1980 ) .

Definitions and local symbols:
- Keywords: arithmetics , exact , exact rational , exact rational arithmetic , rational arithmetics

#### 3.1(iv) Level-Index Arithmetic

- To eliminate overflow or underflow in finite-precision arithmetic numbers are represented by using generalized logarithms $\ln_{\ell}(x)$ given by
- with $x\geq 0$ and $\ell$ the unique nonnegative integer such that $a\equiv\ln_{\ell}(x)\in[0,1)$ . In level-index arithmetic $x$ is represented by $\ell+a$ (or $-(\ell+a)$ for negative numbers). Also in this arithmetic generalized precision can be defined, which includes absolute error and relative precision ( 3.1(v) ) as special cases.
- For further information see Clenshaw and Olver ( 1984 ) and Clenshaw et al. ( 1989 ) . For applications see Lozier ( 1993 ) .
- For further references on level-index arithmetic (and also other arithmetics) see Anuta et al. ( 1996 ) . See also Hayes ( 2009 ) .

Formulas:

Formula:

$$
\displaystyle\ln_{0}(x)
$$

Formula:

$$
\displaystyle\ln_{\ell}(x)
$$


Definitions and local symbols:
- Keywords: arithmetics , generalized logarithms , generalized precision , level-index , level-index arithmetic
- Symbols: $\ln\NVar{z}$ : principal branch of logarithm function and $\ell$ : base

#### 3.1(v) Error Measures

- If $x^{*}$ is an approximation to a real or complex number $x$ , then the absolute error is
- If $x\neq 0$ , the relative error is
- The relative precision is
- where $xx^{*}>0$ for real variables, and $xx^{*}\neq 0$ for complex variables (with the principal value of the logarithm).
- The mollified error is
- For error measures for complex arithmetic see Olver ( 1983 ) .

Formulas:

Formula 3.1.8:

$$
\epsilon_{a}=\left|x^{*}-x\right|.
$$

Formula 3.1.9:

$$
\epsilon_{r}=\left|\frac{x^{*}-x}{x}\right|=\frac{\epsilon_{a}}{\left|x\right|}.
$$

Formula 3.1.10:

$$
\epsilon_{\mathit{rp}}=\left|\ln\left(\ifrac{x^{*}}{x}\right)\right|,
$$

Formula 3.1.11:

$$
\epsilon_{m}=\frac{\left|x^{*}-x\right|}{\max(\left|x\right|,1)}.
$$


Definitions and local symbols:
- Keywords: absolute error , arithmetics , complex , complex arithmetic , error measures , mollified error , relative error , relative precision
- Defines: $\epsilon_{a}$ : absolute error (locally)
- Defines: $\epsilon_{r}$ : relative error (locally)
- Symbols: $\epsilon_{a}$ : absolute error
- Defines: $\epsilon_{\mathit{rp}}$ : relative precision (locally)
- Symbols: $\ln\NVar{z}$ : principal branch of logarithm function
- Defines: $\epsilon_{m}$ : molified error (locally)

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.1](https://dlmf.nist.gov/3.1)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: arithmetics, binary number system, bits, exponent, floating-point, floating-point arithmetic, format width, fractional part, hexadecimal number system, machine epsilon, machine number, machine precision, overflow, significand, significant, underflow, IEEE standard, double precision, single precision, by chopping, down, rounding, symmetric, to nearest machine number, interval, interval arithmetic, validated computing, exact, exact rational, exact rational arithmetic, rational arithmetics, generalized logarithms, generalized precision, level-index, level-index arithmetic, absolute error, complex, complex arithmetic, error measures, mollified error.
