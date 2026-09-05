# §1.17 Integral and Series Representations of the Dirac Delta

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.17, `Integral and Series Representations of the Dirac Delta`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Delta Sequences
- Integral Representations
- Series Representations
- Mathematical Definitions

### Subsections

#### 1.17(i) Delta Sequences

- In applications in physics, engineering, and applied mathematics, (see Friedman ( 1990 ) ), the Dirac delta distribution ( 1.16(iii) ) is historically and customarily replaced by the Dirac delta (or Dirac delta function ) $\delta\left(x\right)$ . This is a symbolic function with the properties:
- and
- subject to certain conditions on the function $\phi(x)$ . From the mathematical standpoint the left-hand side of ( 1.17.2 ) can be interpreted as a generalized integral in the sense that
- for a suitably chosen sequence of functions $\delta_{n}\left(x\right)$ , $n=1,2,\dots$ . Such a sequence is called a delta sequence and we write, symbolically,
- An example of a delta sequence is provided by
- In this case

Formulas:

Formula 1.17.1:

$$
\delta\left(x\right)=0,
$$

Formula 1.17.2:

$$
\int_{-\infty}^{\infty}\delta\left(x-a\right)\phi(x)\,\mathrm{d}x=\phi(a),
$$

Formula 1.17.3:

$$
\lim_{n\to\infty}\int_{-\infty}^{\infty}\delta_{n}\left(x-a\right)\phi(x)\,\mathrm{d}x=\phi(a),
$$

Formula 1.17.4:

$$
\lim_{n\to\infty}\delta_{n}\left(x\right)=\delta\left(x\right),
$$

Formula 1.17.5:

$$
\delta_{n}\left(x-a\right)=\sqrt{\frac{n}{\pi}}{\mathrm{e}}^{-n(x-a)^{2}}.
$$

Formula 1.17.6:

$$
\lim_{n\to\infty}\sqrt{\frac{n}{\pi}}\int_{-\infty}^{\infty}{\mathrm{e}}^{-n(x-a)^{2}}\phi(x)\,\mathrm{d}x=\phi(a),
$$

Formula 1.17.7:

$$
\lim_{n\to\infty}\sqrt{\frac{n}{\pi}}\int_{-\infty}^{\infty}{\mathrm{e}}^{-n(x-a)^{2}}\phi(x)\,\mathrm{d}x=\tfrac{1}{2}\phi(a-)+\tfrac{1}{2}\phi(a+).
$$


Definitions and local symbols:
- Defines: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) and $\delta_{n}\left(x\right)$ : Dirac delta sequence
- Keywords: Dirac delta , delta sequence , delta sequences
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\in$ : element of and $\mathbb{R}$ : real line
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $\mathbb{R}$ : real line and $\phi(x)$ : continuous function
- Symbols: $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\phi(x)$ : continuous function
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\in$ : element of , $\mathbb{R}$ : real line and $n$ : nonnegative integer
- Symbols: $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $n$ : nonnegative integer and $\phi(x)$ : continuous function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $n$ : nonnegative integer and $\phi(x)$ : continuous function

#### 1.17(ii) Integral Representations

- Formal interchange of the order of integration in the Fourier integral formula (( 1.14.1 ) and ( 1.14.4 )):
- yields
- The inner integral does not converge. However, for $n=1,2,\dots$ ,
- Hence comparison with ( 1.17.5 ) shows that ( 1.17.9 ) can be interpreted as a generalized integral ( 1.17.3 ) with
- provided that $\phi(x)$ is continuous when $x\in(-\infty,\infty)$ , and for each $a$ , $\int_{-\infty}^{\infty}{\mathrm{e}}^{-n(x-a)^{2}}\phi(x)\,\mathrm{d}x$ converges absolutely for all sufficiently large values of $n$ (as in the case of ( 1.17.6 )). Then comparison of ( 1.17.2 ) and ( 1.17.9 ) yields the formal integral representation
- Other similar integral representations of the Dirac delta that appear in the physics and applied mathematics literature include the following:

Formulas:

Formula 1.17.8:

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}{\mathrm{e}}^{-\mathrm{i}at}\left(\int_{-\infty}^{\infty}\phi(x){\mathrm{e}}^{\mathrm{i}tx}\,\mathrm{d}x\right)\,\mathrm{d}t=\phi(a)
$$

Formula 1.17.9:

$$
\int_{-\infty}^{\infty}\left(\frac{1}{2\pi}\int_{-\infty}^{\infty}{\mathrm{e}}^{\mathrm{i}(x-a)t}\,\mathrm{d}t\right)\phi(x)\,\mathrm{d}x=\phi(a).
$$

Formula 1.17.10:

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}{\mathrm{e}}^{-t^{2}/(4n)}{\mathrm{e}}^{\mathrm{i}(x-a)t}\,\mathrm{d}t=\sqrt{\frac{n}{\pi}}{\mathrm{e}}^{-n(x-a)^{2}}.
$$

Formula 1.17.11:

$$
\delta_{n}\left(x-a\right)=\frac{1}{2\pi}\int_{-\infty}^{\infty}{\mathrm{e}}^{-t^{2}/(4n)}{\mathrm{e}}^{\mathrm{i}(x-a)t}\,\mathrm{d}t,
$$

Formula 1.17.12:

$$
\delta\left(x-a\right)=\frac{1}{2\pi}\int_{-\infty}^{\infty}{\mathrm{e}}^{\mathrm{i}(x-a)t}\,\mathrm{d}t.
$$

Formula 1.17.12_1:

$$
\delta\left(x-a\right)=\frac{2}{\pi}\int_{0}^{\infty}\cos\left(xt\right)\cos\left(at\right)\,\mathrm{d}t,
$$

Formula 1.17.12_2:

$$
\delta\left(x-a\right)=\frac{2}{\pi}\int_{0}^{\infty}\sin\left(xt\right)\sin\left(at\right)\,\mathrm{d}t,
$$

Formula 1.17.13:

$$
\delta\left(x-a\right)=x\int_{0}^{\infty}tJ_{\nu}\left(xt\right)J_{\nu}\left(at\right)\,\mathrm{d}t,
$$

Formula 1.17.14:

$$
\delta\left(x-a\right)=\frac{2xa}{\pi}\int_{0}^{\infty}t^{2}\mathsf{j}_{\ell}\left(xt\right)\mathsf{j}_{\ell}\left(at\right)\,\mathrm{d}t,
$$

Formula 1.17.15:

$$
\delta\left(x-a\right)=\int_{0}^{\infty}s\left(x,\ell;r\right)s\left(a,\ell;r\right)\,\mathrm{d}r,
$$

Formula 1.17.16:

$$
\delta\left(x-a\right)=\int_{-\infty}^{\infty}\operatorname{Ai}\left(t-x\right)\operatorname{Ai}\left(t-a\right)\,\mathrm{d}t.
$$


Definitions and local symbols:
- Keywords: Dirac delta , Fourier , Fourier integral , Fourier series , integral representations
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\phi(x)$ : continuous function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\phi(x)$ : continuous function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Keywords: Cosines , Dirac delta , Sines , integral representations
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\sin z$ : sine function
- Keywords: Bessel functions , Dirac delta , integral representations , spherical Bessel functions
- Symbols: $J_{\nu}\left(z\right)$ : Bessel function of the first kind , $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\Re$ : real part
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\mathsf{j}_{n}\left(z\right)$ : spherical Bessel function of the first kind
- Keywords: Coulomb functions , Dirac delta , integral representations
- Symbols: $s\left(\epsilon,\ell;r\right)$ : regular Coulomb function , $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Airy functions , Dirac delta , integral representations
- Symbols: $\operatorname{Ai}\left(z\right)$ : Airy function , $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral

#### 1.17(iii) Series Representations

- Formal interchange of the order of summation and integration in the Fourier summation formula (( 1.8.3 ) and ( 1.8.4 )):
- yields
- The sum $\sum_{k=-\infty}^{\infty}{\mathrm{e}}^{\mathrm{i}k(x-a)}$ does not converge, but ( 1.17.18 ) can be interpreted as a generalized integral in the sense that
- where
- provided that $\phi(x)$ is continuous and of period $2\pi$ ; see  1.8(ii) .
- By analogy with  1.17(ii) we have the formal ( $2\pi$ -periodic) series representation

Formulas:

Formula 1.17.17:

$$
\frac{1}{2\pi}\sum_{k=-\infty}^{\infty}{\mathrm{e}}^{-\mathrm{i}ka}\left(\int_{-\pi}^{\pi}\phi(x){\mathrm{e}}^{\mathrm{i}kx}\,\mathrm{d}x\right)=\phi(a),
$$

Formula 1.17.18:

$$
\int_{-\pi}^{\pi}\phi(x)\left(\frac{1}{2\pi}\sum_{k=-\infty}^{\infty}{\mathrm{e}}^{\mathrm{i}k(x-a)}\right)\,\mathrm{d}x=\phi(a).
$$

Formula 1.17.19:

$$
\lim_{n\to\infty}\int_{-\pi}^{\pi}\delta_{n}\left(x-a\right)\phi(x)\,\mathrm{d}x=\phi(a),
$$

Formula 1.17.20:

$$
\delta_{n}\left(x-a\right)=\frac{1}{2\pi}\sum_{k=-n}^{n}{\mathrm{e}}^{\mathrm{i}k(x-a)}\left(=\frac{\sin\left((n+\frac{1}{2})(x-a)\right)}{2\pi\sin\left(\frac{1}{2}(x-a)\right)}\right),
$$

Formula 1.17.21:

$$
\delta\left(x-a\right)=\frac{1}{2\pi}\sum_{k=-\infty}^{\infty}{\mathrm{e}}^{\mathrm{i}k(x-a)}.
$$

Formula 1.17.22:

$$
\delta\left(x-a\right)=\sum_{k=0}^{\infty}(k+\tfrac{1}{2})P_{k}\left(x\right)P_{k}\left(a\right).
$$

Formula 1.17.23:

$$
\delta\left(x-a\right)={\mathrm{e}}^{-(x+a)/2}\sum_{k=0}^{\infty}L_{k}\left(x\right)L_{k}\left(a\right).
$$

Formula 1.17.24:

$$
\delta\left(x-a\right)=\frac{{\mathrm{e}}^{-(x^{2}+a^{2})/2}}{\sqrt{\pi}}\sum_{k=0}^{\infty}\frac{H_{k}\left(x\right)H_{k}\left(a\right)}{2^{k}k!}.
$$

Formula 1.17.25:

$$
\delta\left(\cos\theta_{1}-\cos\theta_{2}\right)\delta\left(\phi_{1}-\phi_{2}\right)=\sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell}Y_{{\ell},{m}}\left(\theta_{1},\phi_{1}\right)\overline{Y_{{\ell},{m}}\left(\theta_{2},\phi_{2}\right)}.
$$


Definitions and local symbols:
- Keywords: Dirac delta , Fourier , series representations
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $k$ : integer and $\phi(x)$ : continuous function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $k$ : integer and $\phi(x)$ : continuous function
- Symbols: $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\phi(x)$ : continuous function
- Symbols: $\delta_{n}\left(x\right)$ : Dirac delta sequence , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\sin z$ : sine function , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $k$ : integer
- Keywords: Dirac delta , Legendre polynomials , series representations
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $P_{n}\left(x\right)$ : Legendre polynomial and $k$ : integer
- Keywords: Dirac delta , Laguerre polynomials , series representations
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\mathrm{e}$ : base of natural logarithm , $L_{n}\left(x\right)=L^{(0)}_{n}\left(x\right)$ : Laguerre polynomial and $k$ : integer
- Keywords: Dirac delta , Hermite polynomials , series representations
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $H_{n}\left(x\right)$ : Hermite polynomial , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) and $k$ : integer
- Keywords: Dirac delta , series representations , spherical harmonics
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate , $\cos z$ : cosine function , $Y_{{l},{m}}\left(\theta,\phi\right)$ : spherical harmonic and $m$ : nonnegative integer

#### 1.17(iv) Mathematical Definitions

- The references given in  1.17(ii) - 1.17(iii) are from the physics and applied mathematics literature. A comprehensive and detailed applied mathematics approach is that of Friedman ( 1990 , Ch. 3 and 4 ) .
- For mathematical derivations of the many of the results of  1.17(ii) and  1.17(iii) see Li and Wong ( 2008 ) . Lebedev ( 1965 ) gives an expanded discussion of derivations of ( 1.17.22 )-( 1.17.24 ).

Definitions and local symbols:
- Keywords: Dirac delta , mathematical definitions

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.17](https://dlmf.nist.gov/1.17)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: Dirac delta, Dirac delta function, delta sequence, delta sequences, Fourier, Fourier integral, Fourier series, integral representations, Cosines, Sines, Bessel functions, spherical Bessel functions, Coulomb functions, Airy functions, series representations, Legendre polynomials, Laguerre polynomials, Hermite polynomials, spherical harmonics, mathematical definitions.

### Source Notes

- ( 1.17.6 ) is a special case of Theorem 7.1 of Olver ( 1997b , Chapter 3) when $\phi(a)\neq 0$ . This theorem also extends straightforwardly to cover $\phi(a)=0$ . ( 1.17.7 ) is proved in a similar manner.
- For ( 1.17.10 ) complete the square in the total power of $\mathrm{e}$ , make the change of variable $\tau=(t/(2\sqrt{n}))-\mathrm{i}(x-a)\sqrt{n}$ , and use $\int_{-\infty}^{\infty}{\mathrm{e}}^{-\tau^{2}}\,\mathrm{d}\tau=\sqrt{\pi}$ .
