# §1.12 Continued Fractions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.12, `Continued Fractions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Notation
- Convergents
- Existence of Convergents
- Contraction and Extension
- Convergence
- Applications

### Subsections

#### 1.12(i) Notation

- The notation used throughout the DLMF for the continued fraction
- is

Formulas:

Formula 1.12.1:

$$
b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\ddots}}
$$

Formula 1.12.2:

$$
b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+}}\cdots.
$$


Definitions and local symbols:
- Keywords: continued fractions , notation

#### 1.12(ii) Convergents

- $C_{n}$ is called the $n$ th approximant or convergent to $C$ . $A_{n}$ and $B_{n}$ are called the $n$ th (canonical) numerator and denominator respectively.

Formulas:

Formula 1.12.3:

$$
C=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots}},
$$

Formula 1.12.4:

$$
C_{n}=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots\cfrac{a_{n}}{b_{n}}}}=\frac{A_{n}}{B_{n}}.
$$

Formula:

$$
\displaystyle A_{k}
$$

Formula:

$$
\displaystyle B_{k}
$$

Formula:

$$
\displaystyle A_{-1}
$$

Formula:

$$
\displaystyle A_{0}
$$

Formula:

$$
\displaystyle B_{-1}
$$

Formula:

$$
\displaystyle B_{0}
$$

Formula 1.12.7:

$$
A_{n}B_{n-1}-B_{n}A_{n-1}=(-1)^{n-1}\prod^{n}_{k=1}a_{k},
$$

Formula 1.12.8:

$$
C_{n}-C_{n-1}=\frac{(-1)^{n-1}\prod^{n}_{k=1}a_{k}}{B_{n-1}B_{n}},
$$

Formula 1.12.9:

$$
C_{n}=b_{0}+\frac{a_{1}}{B_{0}B_{1}}-\dots+(-1)^{n-1}\frac{\prod^{n}_{k=1}a_{k}}{B_{n-1}B_{n}}.
$$

Formula 1.12.10:

$$
\displaystyle a_{n}
$$

Formula 1.12.11:

$$
\displaystyle a_{n}
$$

Formula 1.12.12:

$$
\displaystyle b_{n}
$$

Formula 1.12.13:

$$
\displaystyle b_{n}
$$

Formula:

$$
\displaystyle b_{0}
$$

Formula:

$$
\displaystyle b_{1}
$$

Formula:

$$
\displaystyle a_{1}
$$

Formula 1.12.15:

$$
a^{\prime}_{n}=d_{n}d_{n-1}a_{n},
$$

Formula 1.12.16:

$$
b^{\prime}_{n}=d_{n}b_{n},
$$

Formula 1.12.17:

$$
b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cfrac{a_{3}}{b_{3}+\cdots}}}={b_{0}+\cfrac{a_{1}/b_{1}}{1+\cfrac{a_{2}/(b_{1}b_{2})}{1+\cfrac{a_{3}/(b_{2}b_{3})}{1+\cdots\cfrac{a_{n}/(b_{n-1}b_{n})}{1+\cdots}}}}}={b_{0}+\cfrac{1}{(\frac{1}{a_{1}})b_{1}+\cfrac{1}{(\frac{a_{1}}{a_{2}})b_{2}+\cfrac{1}{(\frac{a_{2}}{(a_{1}a_{3})})b_{3}+\cfrac{1}{(\frac{a_{1}a_{3}}{(a_{2}a_{4})})b_{4}+\cdots}}}}}.
$$

Formula 1.12.18:

$$
p_{0}+\sum^{n}_{k=1}p_{1}p_{2}\cdots p_{k}=p_{0}+\cfrac{p_{1}}{1-\cfrac{p_{2}}{1+p_{2}-\cfrac{p_{3}}{1+p_{3}-\cdots\cfrac{p_{n}}{1+p_{n}}}}},
$$

Formula 1.12.19:

$$
\sum^{n}_{k=0}c_{k}x^{k}=c_{0}+\cfrac{c_{1}x}{1-\cfrac{(\frac{c_{2}}{c_{1}})x}{1+(\frac{c_{2}}{c_{1}})x-\cfrac{(\frac{c_{3}}{c_{2}})x}{1+(\frac{c_{3}}{c_{2}})x-\cdots\cfrac{(\frac{c_{n}}{c_{n-1}})x}{1+(\frac{c_{n}}{c_{n-1}})x}}}},
$$

Formula 1.12.20:

$$
C_{n}(w)=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots\frac{a_{n}}{b_{n}+w}}}.
$$

Formula:

$$
\displaystyle C_{n}(w)
$$

Formula:

$$
\displaystyle C_{n}(0)
$$

Formula:

$$
\displaystyle C_{n}(\infty)
$$


Definitions and local symbols:
- Keywords: approximants , canonical denominator (or numerator) , continued fractions , convergents
- Defines: $C$ : continued fraction (locally)
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer , $A_{n}$ : $n$ th numerator , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Keywords: continued fractions , recurrence relations
- Symbols: $k$ : integer , $A_{n}$ : $n$ th numerator and $B_{n}$ : $n$ th denominator
- Symbols: $A_{n}$ : $n$ th numerator and $B_{n}$ : $n$ th denominator
- Keywords: continued fractions , determinant formula
- Symbols: $k$ : integer , $n$ : nonnegative integer , $A_{n}$ : $n$ th numerator and $B_{n}$ : $n$ th denominator
- Symbols: $k$ : integer , $n$ : nonnegative integer , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Symbols: $k$ : integer , $n$ : nonnegative integer , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Symbols: $n$ : nonnegative integer , $A_{n}$ : $n$ th numerator and $B_{n}$ : $n$ th denominator
- Symbols: $n$ : nonnegative integer , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Symbols: $n$ : nonnegative integer , $A_{n}$ : $n$ th numerator and $B_{n}$ : $n$ th denominator
- Symbols: $n$ : nonnegative integer , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Symbols: $A_{n}$ : $n$ th numerator , $B_{n}$ : $n$ th denominator and $C_{n}(w)$ : continued fraction
- Keywords: continued fractions , equivalent
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer

#### 1.12(iii) Existence of Convergents

- A sequence $\{C_{n}\}$ in the extended complex plane, $\mathbb{C}\cup\{\infty\}$ , can be a sequence of convergents of the continued fraction ( 1.12.3 ) iff

Formulas:

Formula:

$$
\displaystyle C_{0}
$$

Formula:

$$
\displaystyle C_{n}
$$


Definitions and local symbols:
- Keywords: continued fractions , convergents , existence of
- Symbols: $n$ : nonnegative integer and $C_{n}$ : approximant

#### 1.12(iv) Contraction and Extension

- A contraction of a continued fraction $C$ is a continued fraction $C^{\prime}$ whose convergents $\{C^{\prime}_{n}\}$ form a subsequence of the convergents $\{C_{n}\}$ of $C$ . Conversely, $C$ is called an extension of $C^{\prime}$ . If $C^{\prime}_{n}=C_{2n}$ , $n=0,1,2,\dots$ , then $C^{\prime}$ is called the even part of $C$ . The even part of $C$ exists iff $b_{2k}\not=0$ , $k=1,2,\dots$ , and up to equivalence is given by
- If $C^{\prime}_{n}=C_{2n+1}$ , $n=0,1,2,\dots$ , then $C^{\prime}$ is called the odd part of $C$ . The odd part of $C$ exists iff $b_{2k+1}\not=0$ , $k=0,1,2,\dots$ , and up to equivalence is given by

Formulas:

Formula 1.12.23:

$$
b_{0}+\cfrac{a_{1}b_{2}}{a_{2}+b_{1}b_{2}-\cfrac{a_{2}a_{3}b_{4}}{a_{3}b_{4}+b_{2}(a_{4}+b_{3}b_{4})-\cfrac{a_{4}a_{5}b_{2}b_{6}}{a_{5}b_{6}+b_{4}(a_{6}+b_{5}b_{6})-\cfrac{a_{6}a_{7}b_{4}b_{8}}{a_{7}b_{8}+b_{6}(a_{8}+b_{7}b_{8})-\cdots}}}}.
$$

Formula 1.12.24:

$$
\frac{a_{1}+b_{0}b_{1}}{b_{1}}-\cfrac{a_{1}a_{2}b_{3}/b_{1}}{a_{2}b_{3}+b_{1}(a_{3}+b_{2}b_{3})-\cfrac{a_{3}a_{4}b_{1}b_{5}}{a_{4}b_{5}+b_{3}(a_{5}+b_{4}b_{5})-\cfrac{a_{5}a_{6}b_{3}b_{7}}{a_{6}b_{7}+b_{5}(a_{7}+b_{6}b_{7})-\cdots}}}.
$$


Definitions and local symbols:
- Keywords: continued fractions , contraction , even part , extension , odd part

#### 1.12(v) Convergence

- A continued fraction converges if the convergents $C_{n}$ tend to a finite limit as $n\to\infty$ .

Formulas:

Formula 1.12.25:

$$
\left|b_{n}\right|\geq\left|a_{n}\right|+1,
$$

Formula 1.12.26:

$$
-\tfrac{1}{2}\pi+\delta<\operatorname{ph}b_{n}<\tfrac{1}{2}\pi-\delta,
$$

Formula 1.12.27:

$$
-\tfrac{1}{2}\pi+\delta<\operatorname{ph}C_{n}<\tfrac{1}{2}\pi-\delta,
$$

Formula 1.12.28:

$$
\sum^{\infty}_{n=1}\left|b_{n}\right|=\infty.
$$


Definitions and local symbols:
- Keywords: continued fractions , convergence
- Keywords: Pringsheim's theorem , Pringsheim's theorem for continued fractions , continued fractions
- Symbols: $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Keywords: Van Vleck's theorem , Van Vleck's theorem for continued fractions , continued fractions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{ph}$ : phase and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{ph}$ : phase , $n$ : nonnegative integer and $C_{n}$ : approximant
- Symbols: $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$

#### 1.12(vi) Applications

- For analytical and numerical applications of continued fractions to special functions see  3.10 .

Definitions and local symbols:
- Keywords: applications , continued fractions

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.12](https://dlmf.nist.gov/1.12)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: continued fractions, notation, approximants, canonical denominator (or numerator), convergents, recurrence relations, determinant formula, equivalent, series, fractional transformations, existence of, contraction, even part, extension, odd part, convergence, Pringsheim's theorem, Pringsheim's theorem for continued fractions, Van Vleck's theorem, Van Vleck's theorem for continued fractions, applications.

### Source Notes

- See Jones and Thron ( 1980 , pp. 20, 31-37) . For ( 1.12.20 )-( 1.12.21 ), see Lorentzen and Waadeland ( 1992 , pp. 8-9) .
- See Jones and Thron ( 1980 , p. 34) .
- See Jones and Thron ( 1980 , pp. 42-43) , or Lorentzen and Waadeland ( 1992 , p. 84-85) .
- See Jones and Thron ( 1980 , pp. 88, 92) and Lorentzen and Waadeland ( 1992 , pp. 30, 32) .
