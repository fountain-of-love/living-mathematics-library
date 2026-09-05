# §1.11 Zeros of Polynomials

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.11, `Zeros of Polynomials`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Division Algorithm
- Elementary Properties
- Polynomials of Degrees Two, Three, and Four
- Roots of Unity and of Other Constants
- Stable Polynomials

### Subsections

#### 1.11(i) Division Algorithm

Formulas:

Formula 1.11.1:

$$
f(z)=a_{n}z^{n}+a_{n-1}z^{n-1}+\dots+a_{0}.
$$

Formula 1.11.2:

$$
f(z)=(z-\alpha)(b_{n}z^{n-1}+b_{n-1}z^{n-2}+\dots+b_{1})+b_{0},
$$

Formula 1.11.3:

$$
b_{k}=\alpha b_{k+1}+a_{k},
$$

Formula 1.11.4:

$$
f(\alpha)=b_{0}.
$$

Formula 1.11.5:

$$
c_{k}=\alpha c_{k+1}+b_{k},
$$

Formula 1.11.6:

$$
f^{\prime}(\alpha)=c_{1}.
$$

Formula 1.11.7:

$$
f(z)=g(z)q(z)+r(z),
$$


Definitions and local symbols:
- Keywords: division algorithm , zeros of polynomials
- Keywords: Horner's scheme , Horner's scheme for polynomials , zeros of polynomials
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $k$ : integer and $n$ : nonnegative integer
- Keywords: Horner's scheme , Horner's scheme for polynomials , extended , zeros of polynomials
- Symbols: $k$ : integer and $n$ : nonnegative integer
- Symbols: $z$ : variable , $q(z)$ : polynomial and $r(z)$ : polynomial

#### 1.11(ii) Elementary Properties

- A polynomial of degree $n$ with real or complex coefficients has exactly $n$ real or complex zeros counting multiplicity. Every monic (coefficient of highest power is one) polynomial of odd degree with real coefficients has at least one real zero with sign opposite to that of the constant term. A monic polynomial of even degree with real coefficients has at least two zeros of opposite signs when the constant term is negative.

Formulas:

Formula:

$$
\displaystyle f(z)
$$

Formula:

$$
\displaystyle f(-z)
$$

Formula 1.11.9:

$$
D=a_{n}^{2n-2}\prod_{j<k}(z_{j}-z_{k})^{2},
$$

Formula:

$$
\displaystyle z_{1}+z_{2}+\dots+z_{n}
$$

Formula:

$$
\displaystyle\sum_{1\leq j<k\leq n}z_{j}z_{k}
$$

Formula:

$$
\displaystyle\mathrel{\vdots}
$$

Formula:

$$
\displaystyle z_{1}z_{2}\cdots z_{n}
$$


Definitions and local symbols:
- Keywords: distribution , elementary properties , monic , monic polynomial , polynomials , zeros of polynomials
- Keywords: Descartes' rule of signs , Descartes' rule of signs (for polynomials) , zeros of polynomials
- Keywords: discriminant , distribution , elementary symmetric functions , of a polynomial , polynomials , zeros of polynomials
- Symbols: $z$ : variable
- Defines: $D$ : discriminant of $f(z)$ (locally)
- Symbols: $z$ : variable , $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $z$ : variable , $j$ : integer , $k$ : integer and $n$ : nonnegative integer

#### 1.11(iii) Polynomials of Degrees Two, Three, and Four

Formulas:

Formula:

$$
\frac{-b\pm\sqrt{D}}{2a},
$$

Formula:

$$
\displaystyle D
$$

Formula 1.11.12:

$$
D=-4p^{3}-27q^{2}.
$$

Formula:

$$
\displaystyle A
$$

Formula:

$$
\displaystyle B
$$

Formula:

$$
\tfrac{1}{3}(A+B),
$$

Formula:

$$
\tfrac{1}{3}(\rho A+\rho^{2}B),
$$

Formula:

$$
\tfrac{1}{3}(\rho^{2}A+\rho B),
$$

Formula:

$$
\displaystyle\rho
$$

Formula:

$$
\displaystyle\rho^{2}
$$

Formula:

$$
\displaystyle g(w)
$$

Formula:

$$
\displaystyle p
$$

Formula:

$$
\displaystyle q
$$

Formula:

$$
\displaystyle r
$$

Formula 1.11.17:

$$
D=16p^{4}r-4p^{3}q^{2}-128p^{2}r^{2}+144pq^{2}r-27q^{4}+256r^{3}.
$$

Formula 1.11.18:

$$
z^{3}-2pz^{2}+(p^{2}-4r)z+q^{2}=0,
$$

Formula:

$$
\displaystyle 2\alpha_{1}
$$

Formula:

$$
\displaystyle 2\alpha_{2}
$$

Formula:

$$
\displaystyle 2\alpha_{3}
$$

Formula:

$$
\displaystyle 2\alpha_{4}
$$

Formula 1.11.20:

$$
\sqrt{-\theta_{1}}\;\sqrt{-\theta_{2}}\;\sqrt{-\theta_{3}}=-q.
$$


Definitions and local symbols:
- Keywords: degrees two, three, four , zeros of polynomials
- Keywords: quadratic equations
- Symbols: $D$ : discriminant
- Keywords: cubic equation
- Defines: $D$ : discriminant (locally)
- Symbols: $p$ and $q$
- Defines: $A$ (locally) and $B$ (locally)
- Symbols: $p$ , $q$ and $D$ : discriminant
- Symbols: $\rho$ , $A$ and $B$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\rho$
- Keywords: cubic equation , quartic equations , resolvent , resolvent cubic , resolvent cubic equation , zeros of polynomials
- Symbols: $w$ : variable , $p$ , $q$ and $r$
- Defines: $D$ : discriminant (locally)
- Symbols: $p$ , $q$ and $r$
- Symbols: $z$ : variable , $p$ , $q$ and $r$
- Defines: $\theta_{j}$ : cubic roots (locally)
- Symbols: $j$ : integer
- Symbols: $q$ and $\theta_{j}$ : cubic roots

#### 1.11(iv) Roots of Unity and of Other Constants

- The roots of
- are $1$ , ${\mathrm{e}}^{2\pi\mathrm{i}/n}$ , ${\mathrm{e}}^{4\pi\mathrm{i}/n},\dots,{\mathrm{e}}^{(2n-2)\pi\mathrm{i}/n}$ , and of $z^{n}+1=0$ they are ${\mathrm{e}}^{\pi\mathrm{i}/n},{\mathrm{e}}^{3\pi\mathrm{i}/n},\dots,{\mathrm{e}}^{(2n-1)\pi\mathrm{i}/n}$ .
- are
- where $R=(a^{2}+b^{2})^{1/2}$ , $\alpha=\operatorname{ph}\left(a+\mathrm{i}b\right)$ , with the principal value of phase ( 1.9(i) ), and $k=0,1,\dots,n-1$ .

Formulas:

Formula 1.11.21:

$$
z^{n}-1=(z-1)(z^{n-1}+z^{n-2}+\dots+z+1)=0
$$

Formula 1.11.22:

$$
z^{n}=a+\mathrm{i}b,
$$

Formula 1.11.23:

$$
\sqrt[n]{R}\left(\cos\left(\frac{\alpha+2k\pi}{n}\right)+\mathrm{i}\sin\left(\frac{\alpha+2k\pi}{n}\right)\right),
$$


Definitions and local symbols:
- Keywords: constants , roots of , roots of constants , roots of unity , unity , zeros of polynomials
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $\mathrm{i}$ : imaginary unit , $z$ : variable and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\mathrm{i}$ : imaginary unit , $\sin z$ : sine function , $k$ : integer , $n$ : nonnegative integer and $R$ : radius

#### 1.11(v) Stable Polynomials

- with real coefficients, is called stable if the real parts of all the zeros are strictly negative.

Formulas:

Formula 1.11.24:

$$
f(z)=a_{0}+a_{1}z+\dots+a_{n}z^{n},
$$

Formula:

$$
\displaystyle D_{1}
$$

Formula:

$$
\displaystyle D_{2}
$$

Formula:

$$
\displaystyle D_{3}
$$

Formula 1.11.26:

$$
D_{k}=\det[h_{k}^{(1)},h_{k}^{(3)},\dots,h_{k}^{(2k-1)}],
$$


Definitions and local symbols:
- Keywords: polynomials , stable , stable polynomials
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Keywords: Hurwitz criterion , Hurwitz criterion for stable polynomials , stable polynomials
- Symbols: $\det$ : determinant and $D_{j}$ : quantities
- Symbols: $\det$ : determinant , $k$ : integer and $D_{j}$ : quantities

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.11](https://dlmf.nist.gov/1.11)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: polynomials, zeros, zeros of polynomials, division algorithm, Horner's scheme, Horner's scheme for polynomials, extended, distribution, elementary properties, monic, monic polynomial, Descartes' rule of signs, Descartes' rule of signs (for polynomials), discriminant, elementary symmetric functions, of a polynomial, degrees two, three, four, quadratic equations, cubic equation, quartic equations, resolvent, resolvent cubic, resolvent cubic equation, constants, roots of, roots of constants, roots of unity, unity, stable, stable polynomials, Hurwitz criterion, Hurwitz criterion for stable polynomials, degrees two, three, four.

### Source Notes

- For the Horner scheme, see Burnside and Panton ( 1960 , pp. 8-9) . The double Horner scheme is derived similarly. For ( 1.11.7 ), see Dummit and Foote ( 1999 , pp. 300-301) .
- See Burnside and Panton ( 1960 , Chapter 2) . For ( 1.11.9 ) see Dummit and Foote ( 1999 , p. 591) .
- See Dummit and Foote ( 1999 , pp. 592-595, 611-616) .
- See Burnside and Panton ( 1960 , pp. 80-81) .
- See Henrici ( 1977 , vol. 2, pp. 555-559) .
