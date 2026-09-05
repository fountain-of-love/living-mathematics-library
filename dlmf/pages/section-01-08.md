# §1.8 Fourier Series

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.8, `Fourier Series`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Definitions and Elementary Properties
- Convergence
- Integration and Differentiation
- Poisson's Summation Formula
- Examples

### Subsections

#### 1.8(i) Definitions and Elementary Properties

- Formally, if $f(x)$ is a real- or complex-valued $2\pi$ -periodic function,
- The series ( 1.8.1 ) is called the Fourier series of $f(x)$ , and $a_{n},b_{n}$ are the Fourier coefficients of $f(x)$ .
- If $f(-x)=f(x)$ , then $b_{n}=0$ for all $n$ .
- If $f(-x)=-f(x)$ , then $a_{n}=0$ for all $n$ .

Formulas:

Formula 1.8.1:

$$
f(x)=\tfrac{1}{2}a_{0}+\sum^{\infty}_{n=1}(a_{n}\cos\left(nx\right)+b_{n}\sin\left(nx\right)),
$$

Formula:

$$
\displaystyle a_{n}
$$

Formula:

$$
\displaystyle b_{n}
$$

Formula 1.8.3:

$$
f(x)=\sum^{\infty}_{n=-\infty}c_{n}{\mathrm{e}}^{\mathrm{i}nx},
$$

Formula 1.8.4:

$$
c_{n}=\frac{1}{2\pi}\int^{\pi}_{-\pi}f(x){\mathrm{e}}^{-\mathrm{i}nx}\,\mathrm{d}x.
$$

Formula 1.8.5:

$$
\frac{1}{\pi}\int^{\pi}_{-\pi}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\tfrac{1}{2}{\left|a_{0}\right|}^{2}+\sum^{\infty}_{n=1}({\left|a_{n}\right|}^{2}+{\left|b_{n}\right|}^{2}),
$$

Formula 1.8.6:

$$
\frac{1}{2\pi}\int^{\pi}_{-\pi}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\sum^{\infty}_{n=-\infty}{\left|c_{n}\right|}^{2},
$$

Formula 1.8.6_1:

$$
\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\overline{g(x)}\,\mathrm{d}x=\tfrac{1}{2}a_{0}\overline{a_{0}^{\prime}}+\sum^{\infty}_{n=1}(a_{n}\overline{a^{\prime}_{n}}+b_{n}\overline{b^{\prime}_{n}}),
$$

Formula 1.8.6_2:

$$
\frac{1}{2\pi}\int^{\pi}_{-\pi}f(x)\overline{g(x)}\,\mathrm{d}x=\sum^{\infty}_{n=-\infty}c_{n}\overline{c_{n}^{\prime}}.
$$

Formula 1.8.7:

$$
a_{n},b_{n},c_{n}=o\left(n^{-m}\right),
$$

Formula 1.8.8:

$$
L_{n}=\frac{1}{\pi}\int^{\pi}_{0}\frac{\left|\sin\left(n+\frac{1}{2}\right)t\right|}{\sin\left(\frac{1}{2}t\right)}\,\mathrm{d}t,
$$

Formula 1.8.9:

$$
L_{n}\sim(4/{\pi}^{2})\ln n;
$$

Formula 1.8.10:

$$
\int^{b}_{a}f(x){\mathrm{e}}^{\mathrm{i}\lambda x}\,\mathrm{d}x\to 0,
$$


Definitions and local symbols:
- Keywords: Fourier series , coefficients , definition , properties
- Symbols: $\cos z$ : cosine function , $\sin z$ : sine function and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sin z$ : sine function and $n$ : nonnegative integer
- Symbols: $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $n$ : nonnegative integer
- Keywords: Fourier series , Parseval's Formula
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $o\left(x\right)$ : order less than , $m$ : nonnegative integer and $n$ : nonnegative integer
- Keywords: Fourier series , uniqueness
- Keywords: Lebesgue constants , asymptotic behavior
- Defines: $L_{n}$ : Lebesgue constants (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sin z$ : sine function , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\sim$ : asymptotic equality , $\pi$ : the ratio of the circumference of a circle to its diameter , $\ln z$ : principal branch of logarithm function , $n$ : nonnegative integer and $L_{n}$ : Lebesgue constants
- Keywords: Riemann-Lebesgue lemma
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\lambda$ : real

#### 1.8(ii) Convergence

- Let $f(x)$ be an absolutely integrable function of period $2\pi$ , and continuous except at a finite number of points in any bounded interval. Then the series ( 1.8.1 ) converges to the sum
- at every point at which $f(x)$ has both a left-hand derivative (that is, ( 1.4.4 ) applies when $h\to 0-$ ) and a right-hand derivative (that is, ( 1.4.4 ) applies when $h\to 0+$ ). The convergence is non-uniform, however, at points where $f(x-)\neq f(x+)$ ; see  6.16(i) .
- For other tests for convergence see Titchmarsh ( 1962b , pp. 405-410) .

Formulas:

Formula 1.8.11:

$$
\tfrac{1}{2}f(x-)+\tfrac{1}{2}f(x+)
$$


Definitions and local symbols:
- Keywords: Fourier series , convergence , derivatives , left-hand , right-hand

#### 1.8(iii) Integration and Differentiation

- If $a_{n}$ and $b_{n}$ are the Fourier coefficients of a piecewise continuous function $f(x)$ on $[0,2\pi]$ , then
- If a function $f(x)\in C^{2}[0,2\pi]$ is periodic, with period $2\pi$ , then the series obtained by differentiating the Fourier series for $f(x)$ term by term converges at every point to $f^{\prime}(x)$ .

Formulas:

Formula 1.8.12:

$$
\int^{x}_{0}(f(t)-\tfrac{1}{2}a_{0})\,\mathrm{d}t=\sum^{\infty}_{n=1}\frac{a_{n}\sin\left(nx\right)+b_{n}(1-\cos\left(nx\right))}{n},
$$


Definitions and local symbols:
- Keywords: Fourier series , differentiation , integration
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sin z$ : sine function and $n$ : nonnegative integer

#### 1.8(iv) Poisson's Summation Formula

- Suppose that $f(x)$ is twice continuously differentiable and $f(x)$ and $\left|f^{\prime\prime}(x)\right|$ are integrable over $(-\infty,\infty)$ . Then
- It follows from definition ( 1.14.1 ) that the integral in ( 1.8.14 ) is equal to $\sqrt{2\pi}\mathscr{F}\left(f\right)\left(-2\pi n\right)$ .
- An alternative formulation is as follows. Suppose that $f(x)$ is continuous and of bounded variation on $[0,\infty)$ . Suppose also that $f(x)$ is integrable on $[0,\infty)$ and $f(x)\to 0$ as $x\to\infty$ . Then
- As a special case

Formulas:

Formula 1.8.14:

$$
\sum^{\infty}_{n=-\infty}f(x+n)=\sum^{\infty}_{n=-\infty}{\mathrm{e}}^{2\pi\mathrm{i}nx}\int^{\infty}_{-\infty}f(t){\mathrm{e}}^{-2\pi\mathrm{i}nt}\,\mathrm{d}t.
$$

Formula 1.8.15:

$$
\tfrac{1}{2}f(0)+\sum^{\infty}_{n=1}f(n)=\int^{\infty}_{0}f(x)\,\mathrm{d}x+2\sum^{\infty}_{n=1}\int^{\infty}_{0}f(x)\cos\left(2\pi nx\right)\,\mathrm{d}x.
$$

Formula 1.8.16:

$$
\sum_{n=-\infty}^{\infty}{\mathrm{e}}^{-(n+x)^{2}\omega}={\sqrt{\frac{\pi}{\omega}}\,\left(1+2\sum_{n=1}^{\infty}{\mathrm{e}}^{-n^{2}{\pi}^{2}/\omega}\cos\left(2n\pi x\right)\right)},
$$


Definitions and local symbols:
- Keywords: Fourier series , Poisson's summation formula
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\mathrm{e}$ : base of natural logarithm , $\Re$ : real part and $n$ : nonnegative integer

#### 1.8(v) Examples

- For collections of Fourier-series expansions see Prudnikov et al. ( 1986a , v. 1, pp. 725-740) , Gradshteyn and Ryzhik ( 2015 , 1.44-1.45) , and Oberhettinger ( 1973 ) .

Definitions and local symbols:
- Keywords: Fourier series , compendia

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.8](https://dlmf.nist.gov/1.8)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: Fourier series, coefficients, definition, properties, Parseval's Formula, uniqueness, Lebesgue constants, asymptotic behavior, Riemann-Lebesgue lemma, convergence, derivatives, left-hand, right-hand, differentiation, integration, Poisson's summation formula, compendia.

### Source Notes

- See Protter and Morrey ( 1991 , Chapter 10) , Tolstov ( 1962 , Chapter 1) , or Titchmarsh ( 1962b , Chapter 13) . For the Riemann-Lebesgue lemma, see Olver ( 1997b , p. 73) .
- See Tolstov ( 1962 , p. 77) .
- See Titchmarsh ( 1962b , p. 419) .
- For Poisson's summation formula see Rademacher ( 1973 , pp. 71-75) and Titchmarsh ( 1986a , p. 61) . For ( 1.8.16 ) set $f(x)={\mathrm{e}}^{-\omega x^{2}}$ in ( 1.8.14 ).
