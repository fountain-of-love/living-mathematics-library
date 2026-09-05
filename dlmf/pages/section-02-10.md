# §2.10 Sums and Sequences

Source: [https://dlmf.nist.gov/2.10](https://dlmf.nist.gov/2.10)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.10. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Euler-Maclaurin Formula
- Summation by Parts
- Asymptotic Expansions of Entire Functions
- Taylor and Laurent Coefficients: Darboux's Method

## Source Notes

- See Olver ( 1997b , pp. 279-292) .
- See Olver ( 1997b , pp. 295-299) .
- See Olver ( 1997b , pp. 307-309) .
- See Olver ( 1997b , pp. 309-315) .

## Keywords

asymptotic approximations of sums and sequences, Abel-Plana formula, Euler-Maclaurin formula, Glaisher's constant, extensions, summation by parts, asymptotic expansions, entire functions, generalized hypergeometric function F 2 0, of large argument, Darboux's method, Laurent series, Taylor series, asymptotic approximations for coefficients, Legendre polynomials, large degree, generalized hypergeometric function

## Principal Formula Blocks

- Formula block (2.10.1)

```tex
\sum_{j=a}^{n}f(j)=\int_{a}^{n}f(x)\,\mathrm{d}x+\tfrac{1}{2}f(a)+\tfrac{1}{2}% f(n)+\sum_{s=1}^{m-1}\frac{B_{2s}}{(2s)!}\left(f^{(2s-1)}(n)-f^{(2s-1)}(a)% \right)+\int_{a}^{n}\frac{B_{2m}-\widetilde{B}_{2m}\left(x\right)}{(2m)!}f^{(2% m)}(x)\,\mathrm{d}x.
```

- Formula block (2.10.2)

```tex
\sum_{j=a}^{n}f(j)=\int_{a}^{n}f(x)\,\mathrm{d}x+\tfrac{1}{2}f(a)+\tfrac{1}{2}% f(n)-2\int_{0}^{\infty}\frac{\Im\left(f(a+iy)\right)}{e^{2\pi y}-1}\,\mathrm{d% }y+\sum_{s=1}^{m}\frac{B_{2s}}{(2s)!}f^{(2s-1)}(n)+2\frac{(-1)^{m}}{(2m)!}\int% _{0}^{\infty}\Im\left(f^{(2m)}(n+i\vartheta_{n}y)\right)\frac{y^{2m}\,\mathrm{% d}y}{e^{2\pi y}-1},
```

- Formula block (2.10.3)

```tex
S(n)=\sum_{j=1}^{n}j\ln j
```

- Formula block (2.10.4)

```tex
S(n)=\tfrac{1}{2}n^{2}\ln n-\tfrac{1}{4}n^{2}+\tfrac{1}{2}n\ln n+\tfrac{1}{12}% \ln n+C+\sum_{s=2}^{m-1}\frac{(-B_{2s})}{2s(2s-1)(2s-2)}\frac{1}{n^{2s-2}}+R_{% m}(n),
```

- Formula block (2.10.5)

```tex
R_{m}(n)=\int_{n}^{\infty}\frac{\widetilde{B}_{2m}\left(x\right)-B_{2m}}{2m(2m% -1)x^{2m-1}}\,\mathrm{d}x.
```

- Formula block (2.10.6)

```tex
C=\frac{\gamma+\ln\left(2\pi\right)}{12}-\frac{\zeta'\left(2\right)}{2\pi^{2}}% =\frac{1}{12}-\zeta'\left(-1\right),
```

- Formula block (2.10.7)

```tex
\sum_{j=1}^{n-1}j^{\alpha}\sim\zeta\left(-\alpha\right)+\frac{n^{\alpha+1}}{% \alpha+1}\sum_{s=0}^{\infty}\genfrac{(}{)}{0.0pt}{}{\alpha+1}{s}\frac{B_{s}}{n% ^{s}},
```

- Formula block (2.10.8)

```tex
\sum_{j=1}^{n-1}\frac{1}{j}\sim\ln n+\gamma-\frac{1}{2n}-\sum_{s=1}^{\infty}% \frac{B_{2s}}{2s}\frac{1}{n^{2s}},
```

- Formula block (2.10.9)

```tex
\sum_{j=1}^{n-1}u_{j}v_{j}=U_{n-1}v_{n}+\sum_{j=1}^{n-1}U_{j}(v_{j}-v_{j+1}),
```

- Formula block (2.10.10)

```tex
U_{j}=u_{1}+u_{2}+\dots+u_{j}.
```

- Formula block (2.10.11)

```tex
S(\alpha,\beta,n)=\sum_{j=1}^{n-1}e^{ij\beta}j^{\alpha},
```

- Formula block (2.10.12)

```tex
|S(\alpha,\beta,n)|\leq\sum_{j=1}^{n-1}j^{\alpha}=O\left(1\right),\;O\left(\ln n% \right),\text{ or }O\left(n^{\alpha+1}\right),
```

- Formula block (2.10.13)

```tex
U_{j}=e^{i\beta}(e^{ij\beta}-1)/(e^{i\beta}-1),
```

- Formula block (2.10.14)

```tex
S(\alpha,\beta,n)=\frac{e^{i\beta}}{e^{i\beta}-1}\left(e^{i(n-1)\beta}n^{% \alpha}-1+\sum_{j=1}^{n-1}e^{ij\beta}\left(j^{\alpha}-(j+1)^{\alpha}\right)% \right).
```

- Formula block (2.10.15)

```tex
j^{\alpha}-(j+1)^{\alpha}=-\alpha j^{\alpha-1}+\alpha(\alpha-1)O\left(j^{% \alpha-2}\right)
```

- Formula block (2.10.16)

```tex
S(\alpha,\beta,n)=\frac{e^{i\beta}}{e^{i\beta}-1}\left(e^{i(n-1)\beta}n^{% \alpha}-\alpha S(\alpha-1,\beta,n)+O\left(n^{\alpha-1}\right)+O\left(1\right)% \right).
```

- Formula block (2.10.17)

```tex
S(\alpha,\beta,n)=O\left(n^{\alpha}\right)+O\left(1\right).
```

- Formula block (2.10.18)

```tex
S(\alpha,\beta,n)=\frac{e^{in\beta}}{e^{i\beta}-1}n^{\alpha}+O\left(n^{\alpha-% 1}\right)+O\left(1\right),
```

- Formula block (2.10.19)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)=\sum_{j=0}^{\infty}\frac{x^{j}}{(j!)^{3}}.
```

- Formula block (2.10.20)

```tex
\sum_{j=0}^{n-1}\frac{x^{j}}{(j!)^{3}}=\frac{1}{2i}\int_{\mathscr{C}}\frac{x^{% t}}{(\Gamma\left(t+1\right))^{3}}\cot\left(\pi t\right)\,\mathrm{d}t,
```

- Formula block (2.10.21)

```tex
\frac{\cot\left(\pi t\right)}{2i}=-\frac{1}{2}-\frac{1}{e^{-2\pi it}-1}=\frac{% 1}{2}+\frac{1}{e^{2\pi it}-1},
```

- Formula block (2.10.22)

```tex
\sum_{j=0}^{n-1}\frac{x^{j}}{(j!)^{3}}=\int_{-1/2}^{n-(1/2)}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\,\mathrm{d}t-\int_{\mathscr{C}_{1}}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}{e^{-2\pi it}-1}+\int_{% \mathscr{C}_{2}}\frac{x^{t}}{(\Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}% {e^{2\pi it}-1},
```

- Formula block (2.10.23)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)=\int_{-1/2}^{\infty}\frac{x^{t}}{(\Gamma% \left(t+1\right))^{3}}\,\mathrm{d}t+2\Re\int_{-1/2}^{i\infty}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}{e^{-2\pi it}-1}=\int_{0}^{% \infty}\frac{x^{t}}{(\Gamma\left(t+1\right))^{3}}\,\mathrm{d}t+O\left(1\right),
```

- Formula block (2.10.24)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)\sim\frac{\exp\left(3x^{1/3}\right)}{2\pi 3^{% 1/2}x^{1/3}},
```

- Formula block (2.10.25)

```tex
f(z)=\sum_{n=-\infty}^{\infty}f_{n}z^{n},
```

- Formula block (2.10.26)

```tex
f_{n}=\frac{1}{2\pi i}\int_{\mathscr{C}}\frac{f(z)}{z^{n+1}}\,\mathrm{d}z,
```

- Formula block (2.10.27)

```tex
g(z)=\sum_{n=-\infty}^{\infty}g_{n}z^{n},
```

- Formula block (2.10.28)

```tex
f_{n}-g_{n}=\frac{1}{2\pi i}\int_{|z|=r}\frac{f(z)-g(z)}{z^{n+1}}\,\mathrm{d}z% =\frac{1}{2\pi r^{n}}\int_{0}^{2\pi}\left(f\left(re^{i\theta}\right)-g\left(re% ^{i\theta}\right)\right)e^{-ni\theta}\,\mathrm{d}\theta.
```

- Formula block (2.10.29)

```tex
f_{n}=g_{n}+o\left(r^{-n}\right),
```

- Formula block (2.10.30)

```tex
f(z)-g(z)=O\left((z-z_{j})^{\sigma_{j}-1}\right),
```

- Formula block (2.10.31)

```tex
f_{n}=g_{n}+o\left(r^{-n}|n|^{-m}\right),
```

- Formula block (2.10.32)

```tex
f^{(m)}(z)-g^{(m)}(z)=O\left((z-z_{j})^{\sigma_{j}-1}\right),
```

- Formula block (2.10.33)

```tex
f(z)\equiv\frac{1}{(1-2z\cos\alpha+z^{2})^{1/2}}=\sum_{n=0}^{\infty}P_{n}\left% (\cos\alpha\right)z^{n},
```

- Formula block (2.10.34)

```tex
g(z)=e^{-\pi i/4}(2\sin\alpha)^{-1/2}\left(e^{-i\alpha}-z\right)^{-1/2}+e^{\pi i% /4}(2\sin\alpha)^{-1/2}\left(e^{i\alpha}-z\right)^{-1/2}.
```

- Formula block (2.10.35)

```tex
g_{n}=\left(\frac{2}{\pi\sin\alpha}\right)^{1/2}\frac{\Gamma\left(n+\frac{1}{2% }\right)}{n!}\cos\left(n\alpha+\tfrac{1}{2}\alpha-\tfrac{1}{4}\pi\right),
```

- Formula block (2.10.36)

```tex
P_{n}\left(\cos\alpha\right)=\left(\frac{2}{\pi n\sin\alpha}\right)^{1/2}\cos% \left(n\alpha+\tfrac{1}{2}\alpha-\tfrac{1}{4}\pi\right)+o\left(n^{-1}\right).
```


## Definitions and Symbols

- Keywords: asymptotic approximations of sums and sequences
- Keywords: Abel-Plana formula , Euler-Maclaurin formula , asymptotic approximations of sums and sequences
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\int` : integral , `\widetilde{B}_{\NVar{n}}\left(\NVar{x}\right)` : periodic Bernoulli functions , `a` : integer , `m` : integer , `n` : integer and `f(x)` : integrable function
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) , `\Im` : imaginary part , `\mathrm{i}` : imaginary unit , `\int` : integral , `a` : integer , `m` : integer , `n` : integer and `f(x)` : integrable function
- Keywords: Euler-Maclaurin formula , Glaisher's constant , asymptotic approximations of sums and sequences , extensions
- Symbols: `\ln\NVar{z}` : principal branch of logarithm function , `n` : integer and `S(n)` : sum
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\ln\NVar{z}` : principal branch of logarithm function , `m` : integer , `n` : integer , `S(n)` : sum , `C` : constant and `R_{m}(n)` : remainder
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\widetilde{B}_{\NVar{n}}\left(\NVar{x}\right)` : periodic Bernoulli functions , `m` : integer , `n` : integer and `R_{m}(n)` : remainder
- Symbols: `\gamma` : Euler's constant , `\zeta\left(\NVar{s}\right)` : Riemann zeta function , `\pi` : the ratio of the circumference of a circle to its diameter , `\ln\NVar{z}` : principal branch of logarithm function and `C` : constant
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\zeta\left(\NVar{s}\right)` : Riemann zeta function , `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient and `n` : integer
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\gamma` : Euler's constant , `\sim` : Poincar asymptotic expansion , `\ln\NVar{z}` : principal branch of logarithm function and `n` : integer
- Keywords: asymptotic approximations of sums and sequences , summation by parts
- Symbols: `U_{j}` : coefficients , `u_{j}` : terms and `v_{j}` : terms
- Symbols: `U_{j}` : coefficients and `u_{j}` : terms
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\ln\NVar{z}` : principal branch of logarithm function and `S(\alpha,\beta,n)` : sum
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `U_{j}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Keywords: asymptotic approximations of sums and sequences , asymptotic expansions , entire functions
- Keywords: generalized hypergeometric function `{{}_{0}F_{2}}` , of large argument
- Symbols: `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function and `!` : factorial (as in `n!` )
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\cot\NVar{z}` : cotangent function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\mathrm{i}` : imaginary unit , `\int` : integral and `\mathscr{C}` : contour
- Symbols: `\mathscr{C}` : contour
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\cot\NVar{z}` : cotangent function , `\mathrm{e}` : base of natural logarithm and `\mathrm{i}` : imaginary unit
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) , `\mathrm{i}` : imaginary unit , `\int` : integral and `\mathscr{C}` : contour
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\Gamma\left(\NVar{z}\right)` : gamma function , `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral and `\Re` : real part
- Symbols: `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function , `\sim` : asymptotic equality , `\pi` : the ratio of the circumference of a circle to its diameter and `\exp\NVar{z}` : exponential function
- Keywords: Darboux's method , Laurent series , Taylor series , asymptotic approximations for coefficients , asymptotic approximations of sums and sequences
- Symbols: `f(x)` : analytic function , `f_{n}` : coefficients and `r` : radious of annulus
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : analytic function , `f_{n}` : coefficients and `\mathscr{C}` : simple closed contour
- Symbols: `r` : radious of annulus , `g(z)` : comparison function and `g_{n}` : coefficients
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : analytic function , `f_{n}` : coefficients , `r` : radious of annulus , `g(z)` : comparison function and `g_{n}` : coefficients
- Symbols: `o\left(\NVar{x}\right)` : order less than , `f_{n}` : coefficients , `r` : radious of annulus and `g_{n}` : coefficients
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : analytic function , `g(z)` : comparison function and `\sigma_{j}` : positive constant
- Symbols: `o\left(\NVar{x}\right)` : order less than , `f_{n}` : coefficients , `r` : radious of annulus and `g_{n}` : coefficients
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : analytic function , `g(z)` : comparison function and `\sigma_{j}` : positive constant
- Keywords: Darboux's method , Legendre polynomials , asymptotic approximations of sums and sequences , large degree
- Symbols: `P_{\NVar{n}}\left(\NVar{x}\right)` : Legendre polynomial , `\cos\NVar{z}` : cosine function , `\equiv` : equals by definition and `f(x)` : analytic function
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\sin\NVar{z}` : sine function and `g(z)` : comparison function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `!` : factorial (as in `n!` ) , `\sin\NVar{z}` : sine function and `g_{n}` : coefficients
- Symbols: `P_{\NVar{n}}\left(\NVar{x}\right)` : Legendre polynomial , `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `o\left(\NVar{x}\right)` : order less than and `\sin\NVar{z}` : sine function

## Subsections

### 2.10(i) Euler-Maclaurin Formula

- As in  24.2 , let `B_{n}` and `B_{n}\left(x\right)` denote the `n` th Bernoulli number and polynomial, respectively, and `\widetilde{B}_{n}\left(x\right)` the `n` th Bernoulli periodic function `B_{n}\left(x-\left\lfloor x\right\rfloor\right)` .
- Assume that `a,m` , and `n` are integers such that `n>a` , `m>0` , and `f^{(2m)}(x)` is absolutely integrable over `[a,n]` . Then
- This is the Euler-Maclaurin formula . Another version is the Abel-Plana formula :
- `\vartheta_{n}` being some number in the interval `(0,1)` . Sufficient conditions for the validity of this second result are:

Formula blocks:
- Formula block (2.10.1)

```tex
\sum_{j=a}^{n}f(j)=\int_{a}^{n}f(x)\,\mathrm{d}x+\tfrac{1}{2}f(a)+\tfrac{1}{2}% f(n)+\sum_{s=1}^{m-1}\frac{B_{2s}}{(2s)!}\left(f^{(2s-1)}(n)-f^{(2s-1)}(a)% \right)+\int_{a}^{n}\frac{B_{2m}-\widetilde{B}_{2m}\left(x\right)}{(2m)!}f^{(2% m)}(x)\,\mathrm{d}x.
```

- Formula block (2.10.2)

```tex
\sum_{j=a}^{n}f(j)=\int_{a}^{n}f(x)\,\mathrm{d}x+\tfrac{1}{2}f(a)+\tfrac{1}{2}% f(n)-2\int_{0}^{\infty}\frac{\Im\left(f(a+iy)\right)}{e^{2\pi y}-1}\,\mathrm{d% }y+\sum_{s=1}^{m}\frac{B_{2s}}{(2s)!}f^{(2s-1)}(n)+2\frac{(-1)^{m}}{(2m)!}\int% _{0}^{\infty}\Im\left(f^{(2m)}(n+i\vartheta_{n}y)\right)\frac{y^{2m}\,\mathrm{% d}y}{e^{2\pi y}-1},
```

- Formula block (2.10.3)

```tex
S(n)=\sum_{j=1}^{n}j\ln j
```

- Formula block (2.10.4)

```tex
S(n)=\tfrac{1}{2}n^{2}\ln n-\tfrac{1}{4}n^{2}+\tfrac{1}{2}n\ln n+\tfrac{1}{12}% \ln n+C+\sum_{s=2}^{m-1}\frac{(-B_{2s})}{2s(2s-1)(2s-2)}\frac{1}{n^{2s-2}}+R_{% m}(n),
```

- Formula block (2.10.5)

```tex
R_{m}(n)=\int_{n}^{\infty}\frac{\widetilde{B}_{2m}\left(x\right)-B_{2m}}{2m(2m% -1)x^{2m-1}}\,\mathrm{d}x.
```

- Formula block (2.10.6)

```tex
C=\frac{\gamma+\ln\left(2\pi\right)}{12}-\frac{\zeta'\left(2\right)}{2\pi^{2}}% =\frac{1}{12}-\zeta'\left(-1\right),
```

- Formula block (2.10.7)

```tex
\sum_{j=1}^{n-1}j^{\alpha}\sim\zeta\left(-\alpha\right)+\frac{n^{\alpha+1}}{% \alpha+1}\sum_{s=0}^{\infty}\genfrac{(}{)}{0.0pt}{}{\alpha+1}{s}\frac{B_{s}}{n% ^{s}},
```

- Formula block (2.10.8)

```tex
\sum_{j=1}^{n-1}\frac{1}{j}\sim\ln n+\gamma-\frac{1}{2n}-\sum_{s=1}^{\infty}% \frac{B_{2s}}{2s}\frac{1}{n^{2s}},
```


Local metadata:
- Keywords: Abel-Plana formula , Euler-Maclaurin formula , asymptotic approximations of sums and sequences
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\int` : integral , `\widetilde{B}_{\NVar{n}}\left(\NVar{x}\right)` : periodic Bernoulli functions , `a` : integer , `m` : integer , `n` : integer and `f(x)` : integrable function
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) , `\Im` : imaginary part , `\mathrm{i}` : imaginary unit , `\int` : integral , `a` : integer , `m` : integer , `n` : integer and `f(x)` : integrable function
- Keywords: Euler-Maclaurin formula , Glaisher's constant , asymptotic approximations of sums and sequences , extensions
- Symbols: `\ln\NVar{z}` : principal branch of logarithm function , `n` : integer and `S(n)` : sum
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\ln\NVar{z}` : principal branch of logarithm function , `m` : integer , `n` : integer , `S(n)` : sum , `C` : constant and `R_{m}(n)` : remainder
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\widetilde{B}_{\NVar{n}}\left(\NVar{x}\right)` : periodic Bernoulli functions , `m` : integer , `n` : integer and `R_{m}(n)` : remainder
- Symbols: `\gamma` : Euler's constant , `\zeta\left(\NVar{s}\right)` : Riemann zeta function , `\pi` : the ratio of the circumference of a circle to its diameter , `\ln\NVar{z}` : principal branch of logarithm function and `C` : constant
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\zeta\left(\NVar{s}\right)` : Riemann zeta function , `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient and `n` : integer
- Symbols: `B_{\NVar{n}}` : Bernoulli numbers , `\gamma` : Euler's constant , `\sim` : Poincar asymptotic expansion , `\ln\NVar{z}` : principal branch of logarithm function and `n` : integer

### 2.10(ii) Summation by Parts

- The formula for summation by parts is
- where
- This identity can be used to find asymptotic approximations for large `n` when the factor `v_{j}` changes slowly with `j` , and `u_{j}` is oscillatory; compare the approximation of Fourier integrals by integration by parts in  2.3(i) .

Formula blocks:
- Formula block (2.10.9)

```tex
\sum_{j=1}^{n-1}u_{j}v_{j}=U_{n-1}v_{n}+\sum_{j=1}^{n-1}U_{j}(v_{j}-v_{j+1}),
```

- Formula block (2.10.10)

```tex
U_{j}=u_{1}+u_{2}+\dots+u_{j}.
```

- Formula block (2.10.11)

```tex
S(\alpha,\beta,n)=\sum_{j=1}^{n-1}e^{ij\beta}j^{\alpha},
```

- Formula block (2.10.12)

```tex
|S(\alpha,\beta,n)|\leq\sum_{j=1}^{n-1}j^{\alpha}=O\left(1\right),\;O\left(\ln n% \right),\text{ or }O\left(n^{\alpha+1}\right),
```

- Formula block (2.10.13)

```tex
U_{j}=e^{i\beta}(e^{ij\beta}-1)/(e^{i\beta}-1),
```

- Formula block (2.10.14)

```tex
S(\alpha,\beta,n)=\frac{e^{i\beta}}{e^{i\beta}-1}\left(e^{i(n-1)\beta}n^{% \alpha}-1+\sum_{j=1}^{n-1}e^{ij\beta}\left(j^{\alpha}-(j+1)^{\alpha}\right)% \right).
```

- Formula block (2.10.15)

```tex
j^{\alpha}-(j+1)^{\alpha}=-\alpha j^{\alpha-1}+\alpha(\alpha-1)O\left(j^{% \alpha-2}\right)
```

- Formula block (2.10.16)

```tex
S(\alpha,\beta,n)=\frac{e^{i\beta}}{e^{i\beta}-1}\left(e^{i(n-1)\beta}n^{% \alpha}-\alpha S(\alpha-1,\beta,n)+O\left(n^{\alpha-1}\right)+O\left(1\right)% \right).
```

- Formula block (2.10.17)

```tex
S(\alpha,\beta,n)=O\left(n^{\alpha}\right)+O\left(1\right).
```

- Formula block (2.10.18)

```tex
S(\alpha,\beta,n)=\frac{e^{in\beta}}{e^{i\beta}-1}n^{\alpha}+O\left(n^{\alpha-% 1}\right)+O\left(1\right),
```


Local metadata:
- Keywords: asymptotic approximations of sums and sequences , summation by parts
- Symbols: `U_{j}` : coefficients , `u_{j}` : terms and `v_{j}` : terms
- Symbols: `U_{j}` : coefficients and `u_{j}` : terms
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\ln\NVar{z}` : principal branch of logarithm function and `S(\alpha,\beta,n)` : sum
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `U_{j}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding and `S(\alpha,\beta,n)` : sum
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit and `S(\alpha,\beta,n)` : sum

### 2.10(iii) Asymptotic Expansions of Entire Functions

- The asymptotic behavior of entire functions defined by Maclaurin series can be approached by converting the sum into a contour integral by use of the residue theorem and applying the methods of  2.4 and 2.5 .

Formula blocks:
- Formula block (2.10.19)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)=\sum_{j=0}^{\infty}\frac{x^{j}}{(j!)^{3}}.
```

- Formula block (2.10.20)

```tex
\sum_{j=0}^{n-1}\frac{x^{j}}{(j!)^{3}}=\frac{1}{2i}\int_{\mathscr{C}}\frac{x^{% t}}{(\Gamma\left(t+1\right))^{3}}\cot\left(\pi t\right)\,\mathrm{d}t,
```

- Formula block (2.10.21)

```tex
\frac{\cot\left(\pi t\right)}{2i}=-\frac{1}{2}-\frac{1}{e^{-2\pi it}-1}=\frac{% 1}{2}+\frac{1}{e^{2\pi it}-1},
```

- Formula block (2.10.22)

```tex
\sum_{j=0}^{n-1}\frac{x^{j}}{(j!)^{3}}=\int_{-1/2}^{n-(1/2)}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\,\mathrm{d}t-\int_{\mathscr{C}_{1}}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}{e^{-2\pi it}-1}+\int_{% \mathscr{C}_{2}}\frac{x^{t}}{(\Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}% {e^{2\pi it}-1},
```

- Formula block (2.10.23)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)=\int_{-1/2}^{\infty}\frac{x^{t}}{(\Gamma% \left(t+1\right))^{3}}\,\mathrm{d}t+2\Re\int_{-1/2}^{i\infty}\frac{x^{t}}{(% \Gamma\left(t+1\right))^{3}}\frac{\,\mathrm{d}t}{e^{-2\pi it}-1}=\int_{0}^{% \infty}\frac{x^{t}}{(\Gamma\left(t+1\right))^{3}}\,\mathrm{d}t+O\left(1\right),
```

- Formula block (2.10.24)

```tex
{{}_{0}F_{2}}\left(-;1,1;x\right)\sim\frac{\exp\left(3x^{1/3}\right)}{2\pi 3^{% 1/2}x^{1/3}},
```


Local metadata:
- Keywords: asymptotic approximations of sums and sequences , asymptotic expansions , entire functions
- Keywords: generalized hypergeometric function `{{}_{0}F_{2}}` , of large argument
- Symbols: `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function and `!` : factorial (as in `n!` )
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\cot\NVar{z}` : cotangent function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\mathrm{i}` : imaginary unit , `\int` : integral and `\mathscr{C}` : contour
- Symbols: `\mathscr{C}` : contour
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\cot\NVar{z}` : cotangent function , `\mathrm{e}` : base of natural logarithm and `\mathrm{i}` : imaginary unit
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) , `\mathrm{i}` : imaginary unit , `\int` : integral and `\mathscr{C}` : contour
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\Gamma\left(\NVar{z}\right)` : gamma function , `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral and `\Re` : real part
- Symbols: `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{a_{1},\dots,a_{p}};\NVar{b_{1},\dots,b_% {q}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{a_{1},\dots,a_{p}}\atop\NVar{b_{1},% \dots,b_{q}}};\NVar{z}\right)` : alternatively `{{}_{\NVar{p}}F_{\NVar{q}}}\left(\NVar{\mathbf{a}};\NVar{\mathbf{b}};\NVar{z}\right)` or `{{}_{\NVar{p}}F_{\NVar{q}}}\left({\NVar{\mathbf{a}}\atop\NVar{\mathbf{b}}};% \NVar{z}\right)` generalized hypergeometric function , `\sim` : asymptotic equality , `\pi` : the ratio of the circumference of a circle to its diameter and `\exp\NVar{z}` : exponential function

### 2.10(iv) Taylor and Laurent Coefficients: Darboux's Method

- Let `f(z)` be analytic on the annulus `0<|z|<r` , with Laurent expansion
- What is the asymptotic behavior of `f_{n}` as `n\to\infty` or `n\to-\infty` ? More specially, what is the behavior of the higher coefficients in a Taylor-series expansion?
- These problems can be brought within the scope of  2.4 by means of Cauchy's integral formula
- where `\mathscr{C}` is a simple closed contour in the annulus that encloses `z=0` . For examples see Olver ( 1997b , Chapters 8, 9) .
- However, if `r` is finite and `f(z)` has algebraic or logarithmic singularities on `|z|=r` , then Darboux's method is usually easier to apply. We need a "comparison function" `g(z)` with the properties:
- By allowing the contour in Cauchy's formula to expand, we find that

Formula blocks:
- Formula block (2.10.25)

```tex
f(z)=\sum_{n=-\infty}^{\infty}f_{n}z^{n},
```

- Formula block (2.10.26)

```tex
f_{n}=\frac{1}{2\pi i}\int_{\mathscr{C}}\frac{f(z)}{z^{n+1}}\,\mathrm{d}z,
```

- Formula block (2.10.27)

```tex
g(z)=\sum_{n=-\infty}^{\infty}g_{n}z^{n},
```

- Formula block (2.10.28)

```tex
f_{n}-g_{n}=\frac{1}{2\pi i}\int_{|z|=r}\frac{f(z)-g(z)}{z^{n+1}}\,\mathrm{d}z% =\frac{1}{2\pi r^{n}}\int_{0}^{2\pi}\left(f\left(re^{i\theta}\right)-g\left(re% ^{i\theta}\right)\right)e^{-ni\theta}\,\mathrm{d}\theta.
```

- Formula block (2.10.29)

```tex
f_{n}=g_{n}+o\left(r^{-n}\right),
```

- Formula block (2.10.30)

```tex
f(z)-g(z)=O\left((z-z_{j})^{\sigma_{j}-1}\right),
```

- Formula block (2.10.31)

```tex
f_{n}=g_{n}+o\left(r^{-n}|n|^{-m}\right),
```

- Formula block (2.10.32)

```tex
f^{(m)}(z)-g^{(m)}(z)=O\left((z-z_{j})^{\sigma_{j}-1}\right),
```

- Formula block (2.10.33)

```tex
f(z)\equiv\frac{1}{(1-2z\cos\alpha+z^{2})^{1/2}}=\sum_{n=0}^{\infty}P_{n}\left% (\cos\alpha\right)z^{n},
```

- Formula block (2.10.34)

```tex
g(z)=e^{-\pi i/4}(2\sin\alpha)^{-1/2}\left(e^{-i\alpha}-z\right)^{-1/2}+e^{\pi i% /4}(2\sin\alpha)^{-1/2}\left(e^{i\alpha}-z\right)^{-1/2}.
```

- Formula block (2.10.35)

```tex
g_{n}=\left(\frac{2}{\pi\sin\alpha}\right)^{1/2}\frac{\Gamma\left(n+\frac{1}{2% }\right)}{n!}\cos\left(n\alpha+\tfrac{1}{2}\alpha-\tfrac{1}{4}\pi\right),
```

- Formula block (2.10.36)

```tex
P_{n}\left(\cos\alpha\right)=\left(\frac{2}{\pi n\sin\alpha}\right)^{1/2}\cos% \left(n\alpha+\tfrac{1}{2}\alpha-\tfrac{1}{4}\pi\right)+o\left(n^{-1}\right).
```


Local metadata:
- Keywords: Darboux's method , Laurent series , Taylor series , asymptotic approximations for coefficients , asymptotic approximations of sums and sequences
- Symbols: `f(x)` : analytic function , `f_{n}` : coefficients and `r` : radious of annulus
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : analytic function , `f_{n}` : coefficients and `\mathscr{C}` : simple closed contour
- Symbols: `r` : radious of annulus , `g(z)` : comparison function and `g_{n}` : coefficients
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `f(x)` : analytic function , `f_{n}` : coefficients , `r` : radious of annulus , `g(z)` : comparison function and `g_{n}` : coefficients
- Symbols: `o\left(\NVar{x}\right)` : order less than , `f_{n}` : coefficients , `r` : radious of annulus and `g_{n}` : coefficients
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : analytic function , `g(z)` : comparison function and `\sigma_{j}` : positive constant
- Symbols: `o\left(\NVar{x}\right)` : order less than , `f_{n}` : coefficients , `r` : radious of annulus and `g_{n}` : coefficients
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `f(x)` : analytic function , `g(z)` : comparison function and `\sigma_{j}` : positive constant
- Keywords: Darboux's method , Legendre polynomials , asymptotic approximations of sums and sequences , large degree
- Symbols: `P_{\NVar{n}}\left(\NVar{x}\right)` : Legendre polynomial , `\cos\NVar{z}` : cosine function , `\equiv` : equals by definition and `f(x)` : analytic function
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\sin\NVar{z}` : sine function and `g(z)` : comparison function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `!` : factorial (as in `n!` ) , `\sin\NVar{z}` : sine function and `g_{n}` : coefficients
- Symbols: `P_{\NVar{n}}\left(\NVar{x}\right)` : Legendre polynomial , `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `o\left(\NVar{x}\right)` : order less than and `\sin\NVar{z}` : sine function
