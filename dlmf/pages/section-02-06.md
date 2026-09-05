# §2.6 Distributional Methods

Source: [https://dlmf.nist.gov/2.6](https://dlmf.nist.gov/2.6)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.6. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Divergent Integrals
- Stieltjes Transform
- Fractional Integrals
- Regularization

## Source Notes

- See Wong ( 1989 , pp. 293-294) .
- See Wong ( 1989 , pp. 295-312) .
- See Wong ( 1989 , pp. 326-333) .
- See Wong ( 1989 , pp. 333-346) .

## Keywords

asymptotic approximations of integrals, distributional methods, asymptotic approximations and expansions, asymptotic expansions, cases of failure, divergent integrals, generalized, generalized integrals, integrals, Dirac delta distribution, Stieltjes transform, Stieltjes transforms, definition, distributions, of derivatives, symmetric elliptic integrals, tempered, tempered distributions, Mellin transform, Heaviside function, convolution product, convolutions, fractional integrals, asymptotic solutions of differential equations, generalized functions, regularization

## Principal Formula Blocks

- Formula block (2.6.1)

```tex
S(x)=\int_{0}^{\infty}\frac{1}{(1+t)^{1/3}(x+t)}\,\mathrm{d}t,
```

- Formula block (2.6.2)

```tex
(1+t)^{-1/3}=\sum_{s=0}^{\infty}\genfrac{(}{)}{0.0pt}{}{-\frac{1}{3}}{s}t^{-s-% (1/3)}.
```

- Formula block (2.6.3)

```tex
\int_{0}^{\infty}\frac{t^{-s-(1/3)}}{x+t}\,\mathrm{d}t,
```

- Formula block (2.6.4)

```tex
\int_{0}^{\infty}\frac{t^{\alpha-1}}{(x+t)^{\alpha+\beta}}\,\mathrm{d}t=\frac{% \Gamma\left(\alpha\right)\Gamma\left(\beta\right)}{\Gamma\left(\alpha+\beta% \right)}\frac{1}{x^{\beta}},
```

- Formula block (2.6.5)

```tex
\int_{0}^{\infty}\frac{t^{-s-(1/3)}}{x+t}\,\mathrm{d}t=\frac{2\pi}{\sqrt{3}}% \frac{(-1)^{s}}{x^{s+(1/3)}},
```

- Formula block (2.6.6)

```tex
S(x)\sim\frac{2\pi}{\sqrt{3}}\sum_{s=0}^{\infty}(-1)^{s}{\genfrac{(}{)}{0.0pt}% {}{-\frac{1}{3}}{s}}x^{-s-(1/3)},
```

- Formula block (2.6.7)

```tex
S(x)\sim\frac{2\pi}{\sqrt{3}}\sum_{s=0}^{\infty}(-1)^{s}{\genfrac{(}{)}{0.0pt}% {}{-\frac{1}{3}}{s}}x^{-s-(1/3)}-\sum_{s=1}^{\infty}\frac{3^{s}(s-1)!}{2\cdot 5% \cdots(3s-1)}x^{-s};
```

- Formula block (2.6.8)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\int_{0}^{\infty}\frac{f(t)% }{t+z}\,\mathrm{d}t.
```

- Formula block (2.6.9)

```tex
f(t)\sim\sum_{s=0}^{\infty}a_{s}t^{-s-\alpha},
```

- Formula block (2.6.10)

```tex
f(t)=\sum_{s=0}^{n-1}a_{s}t^{-s-\alpha}+f_{n}(t).
```

- Formula block (2.6.11)

```tex
\left\langle f,\phi\right\rangle=\int_{0}^{\infty}f(t)\phi(t)\,\mathrm{d}t,
```

- Formula block (2.6.12)

```tex
\left\langle t^{-\alpha},\phi\right\rangle=\int_{0}^{\infty}t^{-\alpha}\phi(t)% \,\mathrm{d}t,
```

- Formula block (2.6.13)

```tex
\left\langle t^{-s-\alpha},\phi\right\rangle=\frac{1}{{\left(\alpha\right)_{s}% }}\int_{0}^{\infty}t^{-\alpha}\phi^{(s)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.14)

```tex
\left\langle t^{-s-1},\phi\right\rangle=-\frac{1}{s!}\int_{0}^{\infty}(\ln t)% \phi^{(s+1)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.15)

```tex
f_{n,n}(t)=\frac{(-1)^{n}}{(n-1)!}\int_{t}^{\infty}(\tau-t)^{n-1}f_{n}(\tau)\,% \mathrm{d}\tau.
```

- Formula block (2.6.16)

```tex
\left\langle f_{n},\phi\right\rangle=(-1)^{n}\int_{0}^{\infty}f_{n,n}(t)\phi^{% (n)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.17)

```tex
{\left\langle f,\phi\right\rangle}=\sum_{s=0}^{n-1}a_{s}\left\langle t^{-s-% \alpha},\phi\right\rangle-\sum_{s=1}^{n}c_{s}\left\langle{\delta}^{(s-1)},\phi% \right\rangle+\left\langle f_{n},\phi\right\rangle
```

- Formula block (2.6.18)

```tex
c_{s}=\frac{(-1)^{s}}{(s-1)!}\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(s\right),
```

- Formula block (2.6.19)

```tex
\left\langle{\delta}^{(s)},\phi\right\rangle=(-1)^{s}\phi^{(s)}(0),
```

- Formula block (2.6.20)

```tex
{\left\langle f,\phi\right\rangle}=\sum_{s=0}^{n-1}a_{s}\left\langle t^{-s-1},% \phi\right\rangle-\sum_{s=1}^{n}d_{s}\left\langle{\delta}^{(s-1)},\phi\right% \rangle+\left\langle f_{n},\phi\right\rangle
```

- Formula block (2.6.21)

```tex
(-1)^{s+1}d_{s+1}=\frac{a_{s}}{s!}\sum_{k=1}^{s}\frac{1}{k}+\frac{1}{s!}\lim_{% z\to s+1}\left(\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)+\frac{a_{s}}% {z-s-1}\right),
```

- Formula block (2.6.22)

```tex
\phi_{\varepsilon}(t)=\frac{e^{-\varepsilon t}}{t+z},
```

- Formula block (2.6.23)

```tex
\lim_{\varepsilon\to 0}\left\langle t^{-s-\alpha},\phi_{\varepsilon}\right% \rangle=\frac{\pi}{\sin\left(\pi\alpha\right)}\frac{(-1)^{s}}{z^{s+\alpha}},
```

- Formula block (2.6.24)

```tex
\lim_{\varepsilon\to 0}\left\langle t^{-s-1},\phi_{\varepsilon}\right\rangle=% \frac{(-1)^{s+1}}{z^{s+1}}\sum_{k=1}^{s}\frac{1}{k}+\frac{(-1)^{s}}{z^{s+1}}% \ln z,
```

- Formula block (2.6.25)

```tex
\lim_{\varepsilon\to 0}\left\langle f,\phi_{\varepsilon}\right\rangle=\mathcal% {S}\mskip-3.0muf\mskip 3.0mu\left(z\right),
```

- Formula block (2.6.26)

```tex
\lim_{\varepsilon\to 0}\left\langle f_{n},\phi_{\varepsilon}\right\rangle=n!% \int_{0}^{\infty}\frac{f_{n,n}(t)}{(t+z)^{n+1}}\,\mathrm{d}t.
```

- Formula block

```tex
\frac{(-1)^{n}}{z^{n}}\int_{0}^{\infty}\frac{\tau^{n}f_{n}(\tau)}{\tau+z}\,% \mathrm{d}\tau.
```

- Formula block (2.6.27)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\frac{\pi}{\sin\left(\pi% \alpha\right)}\sum_{s=0}^{n-1}(-1)^{s}\frac{a_{s}}{z^{s+\alpha}}-\sum_{s=1}^{n% }(s-1)!\frac{c_{s}}{z^{s}}+R_{n}(z),
```

- Formula block (2.6.28)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\ln z\sum_{s=0}^{n-1}(-1)^{% s}\frac{a_{s}}{z^{s+1}}+\sum_{s=0}^{n-1}(-1)^{s}\frac{\widetilde{d}_{s}}{z^{s+% 1}}+R_{n}(z),
```

- Formula block (2.6.29)

```tex
\widetilde{d}_{s}=\lim_{z\to s+1}\left(\mathscr{M}\mskip-3.0muf\mskip 3.0mu% \left(z\right)+\frac{a_{s}}{z-s-1}\right),
```

- Formula block (2.6.30)

```tex
R_{n}(z)=\frac{(-1)^{n}}{z^{n}}\int_{0}^{\infty}\frac{\tau^{n}f_{n}(\tau)}{% \tau+z}\,\mathrm{d}\tau.
```

- Formula block (2.6.31)

```tex
f(t)\sim e^{ict}\sum_{s=0}^{\infty}a_{s}t^{-s-\alpha},
```

- Formula block (2.6.32)

```tex
\int_{0}^{\infty}\frac{f(t)}{(t+z)^{\rho}}\,\mathrm{d}t,
```

- Formula block (2.6.33)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}\int_{0}^{x}(x-t)^{\mu-1}f(t)\,% \mathrm{d}t,
```

- Formula block (2.6.34)

```tex
(f\ast g)(x)=\int_{0}^{x}f(x-t)g(t)\,\mathrm{d}t
```

- Formula block (2.6.35)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}(t^{\mu-1}\ast f)(x).
```

- Formula block (2.6.36)

```tex
(t^{\mu-1}\ast t^{-s-\alpha})(x)=\int_{0}^{x}(x-t)^{\mu-1}t^{-s-\alpha}\,% \mathrm{d}t,
```

- Formula block (2.6.37)

```tex
F\ast G=D^{n+m}(f\ast g).
```

- Formula block (2.6.38)

```tex
t^{\mu-1}\ast{\delta}^{(s-1)}=\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu+1-% s\right)}t^{\mu-s},
```

- Formula block (2.6.39)

```tex
t^{\mu-1}\ast t^{-s-\alpha}=\frac{\Gamma\left(\mu\right)\Gamma\left(1-s-\alpha% \right)}{\Gamma\left(\mu+1-s-\alpha\right)}t^{\mu-s-\alpha},
```

- Formula block (2.6.40)

```tex
t^{\mu-1}\ast t^{-s-1}=\frac{(-1)^{s}}{\mu\cdot s!}D^{s+1}\left(t^{\mu}\left(% \ln t-\gamma-\psi\left(\mu+1\right)\right)\right),
```

- Formula block (2.6.41)

```tex
f=\sum_{s=0}^{n-1}a_{s}t^{-s-\alpha}-\sum_{s=1}^{n}c_{s}{\delta}^{(s-1)}+f_{n},
```

- Formula block (2.6.42)

```tex
f=\sum_{s=0}^{n-1}a_{s}t^{-s-1}-\sum_{s=1}^{n}d_{s}{\delta}^{(s-1)}+f_{n}.
```

- Formula block (2.6.43)

```tex
t^{\mu-1}\ast f=\sum_{s=0}^{n-1}a_{s}\frac{\Gamma\left(\mu\right)\Gamma\left(1% -s-\alpha\right)}{\Gamma\left(\mu+1-s-\alpha\right)}t^{\mu-s-\alpha}-\sum_{s=1% }^{n}c_{s}\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu-s+1\right)}t^{\mu-s}+t% ^{\mu-1}\ast f_{n}
```

- Formula block (2.6.44)

```tex
t^{\mu-1}\ast f=\sum_{s=0}^{n-1}\frac{(-1)^{s}a_{s}}{\mu\cdot s!}D^{s+1}\left(% t^{\mu}\left(\ln t-\gamma-\psi\left(\mu+1\right)\right)\right)-\sum_{s=1}^{n}d% _{s}\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu-s+1\right)}t^{\mu-s}+t^{\mu-% 1}\ast f_{n}
```

- Formula block (2.6.45)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}a_{s}\frac{\Gamma\left(1-s-\alpha\right)}{\Gamma% \left(\mu+1-s-\alpha\right)}x^{\mu-s-\alpha}-\sum_{s=1}^{n}\frac{c_{s}}{\Gamma% \left(\mu+1-s\right)}x^{\mu-s}+\frac{1}{x^{n}}\delta_{n}(x),
```

- Formula block (2.6.46)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}\frac{(-1)^{s}a_{s}}{s!\Gamma\left(\mu+1\right)}% \frac{{\mathrm{d}}^{s+1}}{{\mathrm{d}x}^{s+1}}\left(x^{\mu}\left(\ln x-\gamma-% \psi\left(\mu+1\right)\right)\right)-\sum_{s=1}^{n}\frac{d_{s}}{\Gamma\left(% \mu-s+1\right)}x^{\mu-s}+\frac{1}{x^{n}}\delta_{n}(x),
```

- Formula block (2.6.47)

```tex
\delta_{n}(x)=\sum_{j=0}^{n}\genfrac{(}{)}{0.0pt}{}{n}{j}\frac{\Gamma\left(\mu% +1\right)}{\Gamma\left(\mu+1-j\right)}I^{\mu}\left(t^{n-j}f_{n,j}\right)(x),
```

- Formula block (2.6.48)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}\int_{0}^{x}(x-t)^{\mu-1}t^{1-% \alpha}(1+t)^{-1}\,\mathrm{d}t,
```

- Formula block (2.6.49)

```tex
f(t)=\sum_{s=0}^{n-1}(-1)^{s}t^{-s-\alpha}+(-1)^{n}\frac{t^{1-n-\alpha}}{1+t}.
```

- Formula block (2.6.50)

```tex
f_{n}(t)=(-1)^{n}\frac{t^{1-n-\alpha}}{1+t}.
```

- Formula block (2.6.51)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(s\right)=(-1)^{s}\pi/\sin\left(\pi% \alpha\right),
```

- Formula block (2.6.52)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}(-1)^{s}\frac{\Gamma\left(1-s-\alpha\right)}{% \Gamma\left(\mu+1-s-\alpha\right)}x^{\mu-s-\alpha}-\frac{\pi}{\sin\left(\pi% \alpha\right)}\sum_{s=1}^{n}\frac{1}{\Gamma\left(\mu+1-s\right)}\frac{x^{\mu-s% }}{(s-1)!}+\frac{1}{x^{n}}\delta_{n}(x).
```

- Formula block (2.6.53)

```tex
{\left|\delta_{n}(x)\right|}\leq\frac{\Gamma\left(\mu+1\right)\Gamma\left(1-% \alpha\right)}{\Gamma\left(\mu+1-\alpha\right)\Gamma\left(n+\alpha\right)}\*% \sum_{j=0}^{n}\dbinom{n}{j}\frac{\Gamma\left(n+\alpha-j\right)}{\left|\Gamma% \left(\mu+1-j\right)\right|}x^{\mu-\alpha}
```

- Formula block (2.6.54)

```tex
I(x)=\int_{0}^{\infty}f(t)h(xt)\,\mathrm{d}t.
```

- Formula block (2.6.55)

```tex
f(t)=\sum_{s=0}^{n-1}a_{s}t^{s+\alpha-1}+f_{n}(t),
```

- Formula block (2.6.56)

```tex
h(t)=\sum_{s=0}^{n-1}b_{s}t^{-s-\beta}+h_{n}(t),
```

- Formula block (2.6.57)

```tex
f(t)h(xt)=\sum_{j=0}^{n-1}\sum_{k=0}^{n-1}a_{j}b_{k}t^{j+\alpha-1-k-\beta}x^{-% k-\beta}+\sum_{j=0}^{n-1}a_{j}t^{j+\alpha-1}h_{n}(xt)+\sum_{k=0}^{n-1}b_{k}x^{% -k-\beta}t^{-k-\beta}f_{n}(t)+f_{n}(t)h_{n}(xt).
```

- Formula block (2.6.58)

```tex
\int_{0}^{\infty}t^{\lambda}\,\mathrm{d}t,
```

- Formula block (2.6.59)

```tex
\int_{0}^{\infty}t^{\lambda}\,\mathrm{d}t=0,
```

- Formula block (2.6.60)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf_{n% }\mskip 3.0mu\left(z\right),
```

- Formula block (2.6.61)

```tex
\mathscr{M}\mskip-3.0muh_{x}\mskip 3.0mu\left(j+\alpha\right)=x^{-j-\alpha}% \mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(j+\alpha\right),
```

- Formula block (2.6.62)

```tex
I(x)=\sum_{j=0}^{n-1}a_{j}\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(j+\alpha% \right)x^{-j-\alpha}+\sum_{k=0}^{n-1}b_{k}\mathscr{M}\mskip-3.0muf\mskip 3.0mu% \left(1-k-\beta\right)x^{-k-\beta}+\delta_{n}(x)
```

- Formula block

```tex
\delta_{n}(x)=\int_{0}^{\infty}f_{n}(t)h_{n}(xt)\,\mathrm{d}t.
```


## Definitions and Symbols

- Keywords: asymptotic approximations of integrals , distributional methods
- Keywords: asymptotic approximations and expansions , asymptotic expansions , cases of failure , divergent integrals , generalized , generalized integrals , integrals
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `S(x)` : integral
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` and `\int` : integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `\Re` : real part
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` and `\int` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\pi` : the ratio of the circumference of a circle to its diameter and `S(x)` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\pi` : the ratio of the circumference of a circle to its diameter , `!` : factorial (as in `n!` ) and `S(x)` : integral
- Keywords: Dirac delta distribution , Stieltjes transform , Stieltjes transforms , asymptotic approximations and expansions , asymptotic approximations of integrals , asymptotic expansions , definition , distributions , generalized , of derivatives , symmetric elliptic integrals , tempered , tempered distributions
- Symbols: `\mathcal{S}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Stieltjes transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `f(t)` : locally integrable function
- Symbols: `\sim` : Poincar asymptotic expansion , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Defines: `f_{n}(t)` : remainder (locally)
- Symbols: `f(t)` : locally integrable function , `a_{n}` : coefficients and `n` : nonnegative integer
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral , `f(t)` : locally integrable function and `\mathcal{T}` : space of decreasing functions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral and `\mathcal{T}` : space of decreasing functions
- Symbols: `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral and `\mathcal{T}` : space of decreasing functions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `!` : factorial (as in `n!` ) , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function and `\mathcal{T}` : space of decreasing functions
- Defines: `f_{n,n}(t)` : `n` th repeated integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\int` : integral , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral , `n` : nonnegative integer , `f_{n}(t)` : remainder , `\mathcal{T}` : space of decreasing functions and `f_{n,n}(t)` : `n` th repeated integral
- Symbols: `\delta_{x}` : Dirac delta distribution , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `c\neq 0` : real , `f(t)` : locally integrable function , `a_{n}` : coefficients , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `!` : factorial (as in `n!` ) , `c\neq 0` : real and `f(t)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\delta_{x}` : Dirac delta distribution and `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function
- Symbols: `\delta_{x}` : Dirac delta distribution , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `d_{s}` : coefficients , `f(t)` : locally integrable function , `a_{n}` : coefficients , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `!` : factorial (as in `n!` ) , `d_{s}` : coefficients , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Keywords: Mellin transform
- Symbols: `\in` : element of , `\mathrm{e}` : base of natural logarithm , `(\NVar{a},\NVar{b})` : open interval and `\varepsilon` : small positive number
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\sin\NVar{z}` : sine function and `\varepsilon` : small positive number
- Symbols: `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\ln\NVar{z}` : principal branch of logarithm function and `\varepsilon` : small positive number
- Symbols: `\mathcal{S}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Stieltjes transform , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\varepsilon` : small positive number and `f(t)` : locally integrable function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `!` : factorial (as in `n!` ) , `\int` : integral , `\varepsilon` : small positive number , `n` : nonnegative integer , `f_{n}(t)` : remainder and `f_{n,n}(t)` : `n` th repeated integral
- Symbols: `\mathcal{S}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Stieltjes transform , `\pi` : the ratio of the circumference of a circle to its diameter , `!` : factorial (as in `n!` ) , `\sin\NVar{z}` : sine function , `R_{n}(z)` : remainder , `c\neq 0` : real , `f(t)` : locally integrable function , `a_{n}` : coefficients and `n` : nonnegative integer
- Symbols: `\mathcal{S}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Stieltjes transform , `\ln\NVar{z}` : principal branch of logarithm function , `R_{n}(z)` : remainder , `f(t)` : locally integrable function , `a_{n}` : coefficients and `n` : nonnegative integer
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Keywords: Mellin transform
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `R_{n}(z)` : remainder , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `c\neq 0` : real , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `f(t)` : locally integrable function
- Keywords: Heaviside function , asymptotic expansions , convolution product , convolutions , definition , distributions , fractional integrals , integrals
- Defines: `I^{\mu}` : fractional integral (locally)
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order and `f(t)` : locally integrable function
- Defines: `\ast` : convolution (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `g(t)` : locally integrable function and `f(t)` : locally integrable function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `I^{\mu}` : fractional integral , `\ast` : convolution and `f(t)` : locally integrable function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order and `\ast` : convolution
- Symbols: `g(t)` : locally integrable function , `\ast` : convolution , `D` : derivative of distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `F` : derivative and `G` : derivative
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\delta_{x}` : Dirac delta distribution , `\mu` : order and `\ast` : convolution
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order and `\ast` : convolution
- Symbols: `\gamma` : Euler's constant , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `\mu` : order , `\ast` : convolution and `D` : derivative of distribution
- Symbols: `\delta_{x}` : Dirac delta distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `f_{n}(t)` : remainder and `c_{s}` : coefficients
- Symbols: `\delta_{x}` : Dirac delta distribution , `d_{s}` : coefficients , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `\ast` : convolution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `f_{n}(t)` : remainder and `c_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\gamma` : Euler's constant , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `d_{s}` : coefficients , `\mu` : order , `\ast` : convolution , `D` : derivative of distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `I^{\mu}` : fractional integral , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `\delta_{n}(x)` : sum and `c_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\gamma` : Euler's constant , `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `d_{s}` : coefficients , `\mu` : order , `I^{\mu}` : fractional integral , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `\delta_{n}(x)` : sum
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\mu` : order , `I^{\mu}` : fractional integral , `n` : nonnegative integer , `\delta_{n}(x)` : sum and `f_{n,n}(t)` : `n` th repeated integral
- Keywords: asymptotic expansions , fractional integrals
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order , `I^{\mu}` : fractional integral and `f(t)` : locally integrable function
- Symbols: `f(t)` : locally integrable function and `n` : nonnegative integer
- Symbols: `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `\pi` : the ratio of the circumference of a circle to its diameter , `\sin\NVar{z}` : sine function and `f(t)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `!` : factorial (as in `n!` ) , `\sin\NVar{z}` : sine function , `\mu` : order , `I^{\mu}` : fractional integral , `f(t)` : locally integrable function , `n` : nonnegative integer and `\delta_{n}(x)` : sum
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\mu` : order , `n` : nonnegative integer and `\delta_{n}(x)` : sum
- Keywords: asymptotic approximations of integrals , asymptotic solutions of differential equations , distributional methods , distributions , divergent integrals , generalized functions , regularization
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(t)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Symbols: `f(t)` : locally integrable function , `n` : positive integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `n` : positive integer , `b_{n}` : coefficients and `h(x)` : function
- Symbols: `f(t)` : locally integrable function , `n` : positive integer , `a_{n}` : coefficients , `b_{n}` : coefficients , `h(x)` : function and `f_{n}(t)` : remainder
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\in` : element of , `\int` : integral and `\mathbb{R}` : real line
- Symbols: `\mathbb{C}` : complex plane , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\in` : element of and `\int` : integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function , `n` : positive integer and `f_{n}(t)` : remainder
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function , `I(x)` : convolution integral , `n` : positive integer , `a_{n}` : coefficients , `b_{n}` : coefficients , `h(x)` : function and `\delta_{n}(x)` : integral
- Keywords: Mellin transform

## Subsections

### 2.6(i) Divergent Integrals

- Consider the integral
- where `x>0` . For `t>1` ,
- Motivated by Watson's lemma ( 2.3(ii) ), we substitute ( 2.6.2 ) in ( 2.6.1 ), and integrate term by term. This leads to integrals of the form
- Although divergent, these integrals may be interpreted in a generalized sense. For instance, we have
- But the right-hand side is meaningful for all values of `\alpha` and `\beta` , other than nonpositive integers. We may therefore define the integral on the left-hand side of ( 2.6.4 ) by the value on the right-hand side, except when `\alpha,\beta=0,-1,-2,\dots` . With this interpretation
- Inserting ( 2.6.2 ) into ( 2.6.1 ) and integrating formally term-by-term, we obtain

Formula blocks:
- Formula block (2.6.1)

```tex
S(x)=\int_{0}^{\infty}\frac{1}{(1+t)^{1/3}(x+t)}\,\mathrm{d}t,
```

- Formula block (2.6.2)

```tex
(1+t)^{-1/3}=\sum_{s=0}^{\infty}\genfrac{(}{)}{0.0pt}{}{-\frac{1}{3}}{s}t^{-s-% (1/3)}.
```

- Formula block (2.6.3)

```tex
\int_{0}^{\infty}\frac{t^{-s-(1/3)}}{x+t}\,\mathrm{d}t,
```

- Formula block (2.6.4)

```tex
\int_{0}^{\infty}\frac{t^{\alpha-1}}{(x+t)^{\alpha+\beta}}\,\mathrm{d}t=\frac{% \Gamma\left(\alpha\right)\Gamma\left(\beta\right)}{\Gamma\left(\alpha+\beta% \right)}\frac{1}{x^{\beta}},
```

- Formula block (2.6.5)

```tex
\int_{0}^{\infty}\frac{t^{-s-(1/3)}}{x+t}\,\mathrm{d}t=\frac{2\pi}{\sqrt{3}}% \frac{(-1)^{s}}{x^{s+(1/3)}},
```

- Formula block (2.6.6)

```tex
S(x)\sim\frac{2\pi}{\sqrt{3}}\sum_{s=0}^{\infty}(-1)^{s}{\genfrac{(}{)}{0.0pt}% {}{-\frac{1}{3}}{s}}x^{-s-(1/3)},
```

- Formula block (2.6.7)

```tex
S(x)\sim\frac{2\pi}{\sqrt{3}}\sum_{s=0}^{\infty}(-1)^{s}{\genfrac{(}{)}{0.0pt}% {}{-\frac{1}{3}}{s}}x^{-s-(1/3)}-\sum_{s=1}^{\infty}\frac{3^{s}(s-1)!}{2\cdot 5% \cdots(3s-1)}x^{-s};
```


Local metadata:
- Keywords: asymptotic approximations and expansions , asymptotic expansions , cases of failure , divergent integrals , generalized , generalized integrals , integrals
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `S(x)` : integral
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` and `\int` : integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `\Re` : real part
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` and `\int` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\pi` : the ratio of the circumference of a circle to its diameter and `S(x)` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\pi` : the ratio of the circumference of a circle to its diameter , `!` : factorial (as in `n!` ) and `S(x)` : integral

### 2.6(ii) Stieltjes Transform

- Let `f(t)` be locally integrable on `[0,\infty)` . The Stieltjes transform of `f(t)` is defined by
- To derive an asymptotic expansion of `\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)` for large values of `|z|` , with `|\operatorname{ph}z|<\pi` , we assume that `f(t)` possesses an asymptotic expansion of the form
- with `0<\alpha\leq 1` . For each `n=1,2,3,\dots` , set
- To each function in this equation, we shall assign a tempered distribution (i.e., a continuous linear functional) on the space `\mathcal{T}` of rapidly decreasing functions on `\mathbb{R}` . Since `f(t)` is locally integrable on `[0,\infty)` , it defines a distribution by
- In particular,
- when `0<\alpha<1` . Since the functions `t^{-s-\alpha}` , `s=1,2,\dots` , are not locally integrable on `[0,\infty)` , we cannot assign distributions to them in a similar manner. However, they are multiples of the derivatives of `t^{-\alpha}` . Motivated by the definition of distributional derivatives, we can assign them the distributions defined by

Formula blocks:
- Formula block (2.6.8)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\int_{0}^{\infty}\frac{f(t)% }{t+z}\,\mathrm{d}t.
```

- Formula block (2.6.9)

```tex
f(t)\sim\sum_{s=0}^{\infty}a_{s}t^{-s-\alpha},
```

- Formula block (2.6.10)

```tex
f(t)=\sum_{s=0}^{n-1}a_{s}t^{-s-\alpha}+f_{n}(t).
```

- Formula block (2.6.11)

```tex
\left\langle f,\phi\right\rangle=\int_{0}^{\infty}f(t)\phi(t)\,\mathrm{d}t,
```

- Formula block (2.6.12)

```tex
\left\langle t^{-\alpha},\phi\right\rangle=\int_{0}^{\infty}t^{-\alpha}\phi(t)% \,\mathrm{d}t,
```

- Formula block (2.6.13)

```tex
\left\langle t^{-s-\alpha},\phi\right\rangle=\frac{1}{{\left(\alpha\right)_{s}% }}\int_{0}^{\infty}t^{-\alpha}\phi^{(s)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.14)

```tex
\left\langle t^{-s-1},\phi\right\rangle=-\frac{1}{s!}\int_{0}^{\infty}(\ln t)% \phi^{(s+1)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.15)

```tex
f_{n,n}(t)=\frac{(-1)^{n}}{(n-1)!}\int_{t}^{\infty}(\tau-t)^{n-1}f_{n}(\tau)\,% \mathrm{d}\tau.
```

- Formula block (2.6.16)

```tex
\left\langle f_{n},\phi\right\rangle=(-1)^{n}\int_{0}^{\infty}f_{n,n}(t)\phi^{% (n)}(t)\,\mathrm{d}t,
```

- Formula block (2.6.17)

```tex
{\left\langle f,\phi\right\rangle}=\sum_{s=0}^{n-1}a_{s}\left\langle t^{-s-% \alpha},\phi\right\rangle-\sum_{s=1}^{n}c_{s}\left\langle{\delta}^{(s-1)},\phi% \right\rangle+\left\langle f_{n},\phi\right\rangle
```

- Formula block (2.6.18)

```tex
c_{s}=\frac{(-1)^{s}}{(s-1)!}\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(s\right),
```

- Formula block (2.6.19)

```tex
\left\langle{\delta}^{(s)},\phi\right\rangle=(-1)^{s}\phi^{(s)}(0),
```

- Formula block (2.6.20)

```tex
{\left\langle f,\phi\right\rangle}=\sum_{s=0}^{n-1}a_{s}\left\langle t^{-s-1},% \phi\right\rangle-\sum_{s=1}^{n}d_{s}\left\langle{\delta}^{(s-1)},\phi\right% \rangle+\left\langle f_{n},\phi\right\rangle
```

- Formula block (2.6.21)

```tex
(-1)^{s+1}d_{s+1}=\frac{a_{s}}{s!}\sum_{k=1}^{s}\frac{1}{k}+\frac{1}{s!}\lim_{% z\to s+1}\left(\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)+\frac{a_{s}}% {z-s-1}\right),
```

- Formula block (2.6.22)

```tex
\phi_{\varepsilon}(t)=\frac{e^{-\varepsilon t}}{t+z},
```

- Formula block (2.6.23)

```tex
\lim_{\varepsilon\to 0}\left\langle t^{-s-\alpha},\phi_{\varepsilon}\right% \rangle=\frac{\pi}{\sin\left(\pi\alpha\right)}\frac{(-1)^{s}}{z^{s+\alpha}},
```

- Formula block (2.6.24)

```tex
\lim_{\varepsilon\to 0}\left\langle t^{-s-1},\phi_{\varepsilon}\right\rangle=% \frac{(-1)^{s+1}}{z^{s+1}}\sum_{k=1}^{s}\frac{1}{k}+\frac{(-1)^{s}}{z^{s+1}}% \ln z,
```

- Formula block (2.6.25)

```tex
\lim_{\varepsilon\to 0}\left\langle f,\phi_{\varepsilon}\right\rangle=\mathcal% {S}\mskip-3.0muf\mskip 3.0mu\left(z\right),
```

- Formula block (2.6.26)

```tex
\lim_{\varepsilon\to 0}\left\langle f_{n},\phi_{\varepsilon}\right\rangle=n!% \int_{0}^{\infty}\frac{f_{n,n}(t)}{(t+z)^{n+1}}\,\mathrm{d}t.
```

- Formula block

```tex
\frac{(-1)^{n}}{z^{n}}\int_{0}^{\infty}\frac{\tau^{n}f_{n}(\tau)}{\tau+z}\,% \mathrm{d}\tau.
```

- Formula block (2.6.27)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\frac{\pi}{\sin\left(\pi% \alpha\right)}\sum_{s=0}^{n-1}(-1)^{s}\frac{a_{s}}{z^{s+\alpha}}-\sum_{s=1}^{n% }(s-1)!\frac{c_{s}}{z^{s}}+R_{n}(z),
```

- Formula block (2.6.28)

```tex
\mathcal{S}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\ln z\sum_{s=0}^{n-1}(-1)^{% s}\frac{a_{s}}{z^{s+1}}+\sum_{s=0}^{n-1}(-1)^{s}\frac{\widetilde{d}_{s}}{z^{s+% 1}}+R_{n}(z),
```

- Formula block (2.6.29)

```tex
\widetilde{d}_{s}=\lim_{z\to s+1}\left(\mathscr{M}\mskip-3.0muf\mskip 3.0mu% \left(z\right)+\frac{a_{s}}{z-s-1}\right),
```

- Formula block (2.6.30)

```tex
R_{n}(z)=\frac{(-1)^{n}}{z^{n}}\int_{0}^{\infty}\frac{\tau^{n}f_{n}(\tau)}{% \tau+z}\,\mathrm{d}\tau.
```

- Formula block (2.6.31)

```tex
f(t)\sim e^{ict}\sum_{s=0}^{\infty}a_{s}t^{-s-\alpha},
```

- Formula block (2.6.32)

```tex
\int_{0}^{\infty}\frac{f(t)}{(t+z)^{\rho}}\,\mathrm{d}t,
```


Local metadata:
- Keywords: Dirac delta distribution , Stieltjes transform , Stieltjes transforms , asymptotic approximations and expansions , asymptotic approximations of integrals , asymptotic expansions , definition , distributions , generalized , of derivatives , symmetric elliptic integrals , tempered , tempered distributions
- Symbols: `\mathcal{S}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Stieltjes transform , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `f(t)` : locally integrable function
- Symbols: `\sim` : Poincar asymptotic expansion , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Defines: `f_{n}(t)` : remainder (locally)
- Symbols: `f(t)` : locally integrable function , `a_{n}` : coefficients and `n` : nonnegative integer
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral , `f(t)` : locally integrable function and `\mathcal{T}` : space of decreasing functions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral and `\mathcal{T}` : space of decreasing functions
- Symbols: `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral and `\mathcal{T}` : space of decreasing functions
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `!` : factorial (as in `n!` ) , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function and `\mathcal{T}` : space of decreasing functions
- Defines: `f_{n,n}(t)` : `n` th repeated integral (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `!` : factorial (as in `n!` ) , `\int` : integral , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `\in` : element of , `\int` : integral , `n` : nonnegative integer , `f_{n}(t)` : remainder , `\mathcal{T}` : space of decreasing functions and `f_{n,n}(t)` : `n` th repeated integral
- Symbols: `\delta_{x}` : Dirac delta distribution , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `c\neq 0` : real , `f(t)` : locally integrable function , `a_{n}` : coefficients , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `!` : factorial (as in `n!` ) , `c\neq 0` : real and `f(t)` : locally integrable function
- Keywords: Mellin transform
- Symbols: `\delta_{x}` : Dirac delta distribution and `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function
- Symbols: `\delta_{x}` : Dirac delta distribution , `\left\langle\NVar{\Lambda},\NVar{\phi}\right\rangle` : action of distribution on test function , `d_{s}` : coefficients , `f(t)` : locally integrable function , `a_{n}` : coefficients , `n` : nonnegative integer and `f_{n}(t)` : remainder
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `!` : factorial (as in `n!` ) , `d_{s}` : coefficients , `f(t)` : locally integrable function and `a_{n}` : coefficients
- Keywords: Mellin transform
- Symbols: `\in` : element of , `\mathrm{e}` : base of natural logarithm , `(\NVar{a},\NVar{b})` : open interval and `\varepsilon` : small positive number

### 2.6(iii) Fractional Integrals

- The Riemann-Liouville fractional integral of order `\mu` is defined by
- see  1.15(vi) . We again assume `f(t)` is locally integrable on `[0,\infty)` and satisfies ( 2.6.9 ). We now derive an asymptotic expansion of `I^{\mu}f(x)` for large positive values of `x` .
- In terms of the convolution product
- of two locally integrable functions on `[0,\infty)` , ( 2.6.33 ) can be written
- The replacement of `f(t)` by its asymptotic expansion ( 2.6.9 ), followed by term-by-term integration leads to convolution integrals of the form
- Of course, except when `s=0` and `0<\alpha<1` , none of these integrals exists in the usual sense. However, the left-hand side can be considered as the convolution of the two distributions associated with the functions `t^{\mu-1}` and `t^{-s-\alpha}` , given by ( 2.6.12 ) and ( 2.6.13 ).

Formula blocks:
- Formula block (2.6.33)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}\int_{0}^{x}(x-t)^{\mu-1}f(t)\,% \mathrm{d}t,
```

- Formula block (2.6.34)

```tex
(f\ast g)(x)=\int_{0}^{x}f(x-t)g(t)\,\mathrm{d}t
```

- Formula block (2.6.35)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}(t^{\mu-1}\ast f)(x).
```

- Formula block (2.6.36)

```tex
(t^{\mu-1}\ast t^{-s-\alpha})(x)=\int_{0}^{x}(x-t)^{\mu-1}t^{-s-\alpha}\,% \mathrm{d}t,
```

- Formula block (2.6.37)

```tex
F\ast G=D^{n+m}(f\ast g).
```

- Formula block (2.6.38)

```tex
t^{\mu-1}\ast{\delta}^{(s-1)}=\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu+1-% s\right)}t^{\mu-s},
```

- Formula block (2.6.39)

```tex
t^{\mu-1}\ast t^{-s-\alpha}=\frac{\Gamma\left(\mu\right)\Gamma\left(1-s-\alpha% \right)}{\Gamma\left(\mu+1-s-\alpha\right)}t^{\mu-s-\alpha},
```

- Formula block (2.6.40)

```tex
t^{\mu-1}\ast t^{-s-1}=\frac{(-1)^{s}}{\mu\cdot s!}D^{s+1}\left(t^{\mu}\left(% \ln t-\gamma-\psi\left(\mu+1\right)\right)\right),
```

- Formula block (2.6.41)

```tex
f=\sum_{s=0}^{n-1}a_{s}t^{-s-\alpha}-\sum_{s=1}^{n}c_{s}{\delta}^{(s-1)}+f_{n},
```

- Formula block (2.6.42)

```tex
f=\sum_{s=0}^{n-1}a_{s}t^{-s-1}-\sum_{s=1}^{n}d_{s}{\delta}^{(s-1)}+f_{n}.
```

- Formula block (2.6.43)

```tex
t^{\mu-1}\ast f=\sum_{s=0}^{n-1}a_{s}\frac{\Gamma\left(\mu\right)\Gamma\left(1% -s-\alpha\right)}{\Gamma\left(\mu+1-s-\alpha\right)}t^{\mu-s-\alpha}-\sum_{s=1% }^{n}c_{s}\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu-s+1\right)}t^{\mu-s}+t% ^{\mu-1}\ast f_{n}
```

- Formula block (2.6.44)

```tex
t^{\mu-1}\ast f=\sum_{s=0}^{n-1}\frac{(-1)^{s}a_{s}}{\mu\cdot s!}D^{s+1}\left(% t^{\mu}\left(\ln t-\gamma-\psi\left(\mu+1\right)\right)\right)-\sum_{s=1}^{n}d% _{s}\frac{\Gamma\left(\mu\right)}{\Gamma\left(\mu-s+1\right)}t^{\mu-s}+t^{\mu-% 1}\ast f_{n}
```

- Formula block (2.6.45)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}a_{s}\frac{\Gamma\left(1-s-\alpha\right)}{\Gamma% \left(\mu+1-s-\alpha\right)}x^{\mu-s-\alpha}-\sum_{s=1}^{n}\frac{c_{s}}{\Gamma% \left(\mu+1-s\right)}x^{\mu-s}+\frac{1}{x^{n}}\delta_{n}(x),
```

- Formula block (2.6.46)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}\frac{(-1)^{s}a_{s}}{s!\Gamma\left(\mu+1\right)}% \frac{{\mathrm{d}}^{s+1}}{{\mathrm{d}x}^{s+1}}\left(x^{\mu}\left(\ln x-\gamma-% \psi\left(\mu+1\right)\right)\right)-\sum_{s=1}^{n}\frac{d_{s}}{\Gamma\left(% \mu-s+1\right)}x^{\mu-s}+\frac{1}{x^{n}}\delta_{n}(x),
```

- Formula block (2.6.47)

```tex
\delta_{n}(x)=\sum_{j=0}^{n}\genfrac{(}{)}{0.0pt}{}{n}{j}\frac{\Gamma\left(\mu% +1\right)}{\Gamma\left(\mu+1-j\right)}I^{\mu}\left(t^{n-j}f_{n,j}\right)(x),
```

- Formula block (2.6.48)

```tex
I^{\mu}f(x)=\frac{1}{\Gamma\left(\mu\right)}\int_{0}^{x}(x-t)^{\mu-1}t^{1-% \alpha}(1+t)^{-1}\,\mathrm{d}t,
```

- Formula block (2.6.49)

```tex
f(t)=\sum_{s=0}^{n-1}(-1)^{s}t^{-s-\alpha}+(-1)^{n}\frac{t^{1-n-\alpha}}{1+t}.
```

- Formula block (2.6.50)

```tex
f_{n}(t)=(-1)^{n}\frac{t^{1-n-\alpha}}{1+t}.
```

- Formula block (2.6.51)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(s\right)=(-1)^{s}\pi/\sin\left(\pi% \alpha\right),
```

- Formula block (2.6.52)

```tex
I^{\mu}f(x)=\sum_{s=0}^{n-1}(-1)^{s}\frac{\Gamma\left(1-s-\alpha\right)}{% \Gamma\left(\mu+1-s-\alpha\right)}x^{\mu-s-\alpha}-\frac{\pi}{\sin\left(\pi% \alpha\right)}\sum_{s=1}^{n}\frac{1}{\Gamma\left(\mu+1-s\right)}\frac{x^{\mu-s% }}{(s-1)!}+\frac{1}{x^{n}}\delta_{n}(x).
```

- Formula block (2.6.53)

```tex
{\left|\delta_{n}(x)\right|}\leq\frac{\Gamma\left(\mu+1\right)\Gamma\left(1-% \alpha\right)}{\Gamma\left(\mu+1-\alpha\right)\Gamma\left(n+\alpha\right)}\*% \sum_{j=0}^{n}\dbinom{n}{j}\frac{\Gamma\left(n+\alpha-j\right)}{\left|\Gamma% \left(\mu+1-j\right)\right|}x^{\mu-\alpha}
```


Local metadata:
- Keywords: Heaviside function , asymptotic expansions , convolution product , convolutions , definition , distributions , fractional integrals , integrals
- Defines: `I^{\mu}` : fractional integral (locally)
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order and `f(t)` : locally integrable function
- Defines: `\ast` : convolution (locally)
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `g(t)` : locally integrable function and `f(t)` : locally integrable function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `I^{\mu}` : fractional integral , `\ast` : convolution and `f(t)` : locally integrable function
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order and `\ast` : convolution
- Symbols: `g(t)` : locally integrable function , `\ast` : convolution , `D` : derivative of distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `F` : derivative and `G` : derivative
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\delta_{x}` : Dirac delta distribution , `\mu` : order and `\ast` : convolution
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order and `\ast` : convolution
- Symbols: `\gamma` : Euler's constant , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `\mu` : order , `\ast` : convolution and `D` : derivative of distribution
- Symbols: `\delta_{x}` : Dirac delta distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `f_{n}(t)` : remainder and `c_{s}` : coefficients
- Symbols: `\delta_{x}` : Dirac delta distribution , `d_{s}` : coefficients , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `\ast` : convolution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `f_{n}(t)` : remainder and `c_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\gamma` : Euler's constant , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `d_{s}` : coefficients , `\mu` : order , `\ast` : convolution , `D` : derivative of distribution , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\mu` : order , `I^{\mu}` : fractional integral , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients , `\delta_{n}(x)` : sum and `c_{s}` : coefficients
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\gamma` : Euler's constant , `\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}` : derivative of `f` with respect to `x` , `\psi\left(\NVar{z}\right)` : psi (or digamma) function , `!` : factorial (as in `n!` ) , `\ln\NVar{z}` : principal branch of logarithm function , `d_{s}` : coefficients , `\mu` : order , `I^{\mu}` : fractional integral , `f(t)` : locally integrable function , `n` : nonnegative integer , `a_{n}` : coefficients and `\delta_{n}(x)` : sum
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `\mu` : order , `I^{\mu}` : fractional integral , `n` : nonnegative integer , `\delta_{n}(x)` : sum and `f_{n,n}(t)` : `n` th repeated integral
- Keywords: asymptotic expansions , fractional integrals
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `\mu` : order , `I^{\mu}` : fractional integral and `f(t)` : locally integrable function

### 2.6(iv) Regularization

- The method of distributions can be further extended to derive asymptotic expansions for convolution integrals:
- We assume that for each `n=1,2,3,\dots` ,
- where `0<\alpha\leq 1` and `f_{n}(t)=O\left(t^{n+\alpha-1}\right)` as `t\to 0+` . Also,
- where `0<\beta\leq 1` , and `h_{n}(t)=O\left(t^{-n-\beta}\right)` as `t\to\infty` . Multiplication of these expansions leads to
- On inserting this identity into ( 2.6.54 ), we immediately encounter divergent integrals of the form
- However, in the theory of generalized functions (distributions), there is a method, known as "regularization", by which these integrals can be interpreted in a meaningful manner. In this sense

Formula blocks:
- Formula block (2.6.54)

```tex
I(x)=\int_{0}^{\infty}f(t)h(xt)\,\mathrm{d}t.
```

- Formula block (2.6.55)

```tex
f(t)=\sum_{s=0}^{n-1}a_{s}t^{s+\alpha-1}+f_{n}(t),
```

- Formula block (2.6.56)

```tex
h(t)=\sum_{s=0}^{n-1}b_{s}t^{-s-\beta}+h_{n}(t),
```

- Formula block (2.6.57)

```tex
f(t)h(xt)=\sum_{j=0}^{n-1}\sum_{k=0}^{n-1}a_{j}b_{k}t^{j+\alpha-1-k-\beta}x^{-% k-\beta}+\sum_{j=0}^{n-1}a_{j}t^{j+\alpha-1}h_{n}(xt)+\sum_{k=0}^{n-1}b_{k}x^{% -k-\beta}t^{-k-\beta}f_{n}(t)+f_{n}(t)h_{n}(xt).
```

- Formula block (2.6.58)

```tex
\int_{0}^{\infty}t^{\lambda}\,\mathrm{d}t,
```

- Formula block (2.6.59)

```tex
\int_{0}^{\infty}t^{\lambda}\,\mathrm{d}t=0,
```

- Formula block (2.6.60)

```tex
\mathscr{M}\mskip-3.0muf\mskip 3.0mu\left(z\right)=\mathscr{M}\mskip-3.0muf_{n% }\mskip 3.0mu\left(z\right),
```

- Formula block (2.6.61)

```tex
\mathscr{M}\mskip-3.0muh_{x}\mskip 3.0mu\left(j+\alpha\right)=x^{-j-\alpha}% \mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(j+\alpha\right),
```

- Formula block (2.6.62)

```tex
I(x)=\sum_{j=0}^{n-1}a_{j}\mathscr{M}\mskip-3.0muh\mskip 3.0mu\left(j+\alpha% \right)x^{-j-\alpha}+\sum_{k=0}^{n-1}b_{k}\mathscr{M}\mskip-3.0muf\mskip 3.0mu% \left(1-k-\beta\right)x^{-k-\beta}+\delta_{n}(x)
```

- Formula block

```tex
\delta_{n}(x)=\int_{0}^{\infty}f_{n}(t)h_{n}(xt)\,\mathrm{d}t.
```


Local metadata:
- Keywords: asymptotic approximations of integrals , asymptotic solutions of differential equations , distributional methods , distributions , divergent integrals , generalized functions , regularization
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral , `f(t)` : locally integrable function , `I(x)` : convolution integral and `h(x)` : function
- Symbols: `f(t)` : locally integrable function , `n` : positive integer , `a_{n}` : coefficients and `f_{n}(t)` : remainder
- Symbols: `n` : positive integer , `b_{n}` : coefficients and `h(x)` : function
- Symbols: `f(t)` : locally integrable function , `n` : positive integer , `a_{n}` : coefficients , `b_{n}` : coefficients , `h(x)` : function and `f_{n}(t)` : remainder
- Symbols: `\,\mathrm{d}\NVar{x}` : differential of `x` , `\in` : element of , `\int` : integral and `\mathbb{R}` : real line
- Symbols: `\mathbb{C}` : complex plane , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\in` : element of and `\int` : integral
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function , `n` : positive integer and `f_{n}(t)` : remainder
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function and `h(x)` : function
- Keywords: Mellin transform
- Symbols: `\mathscr{M}\left(\NVar{f}\right)\left(\NVar{s}\right)` : Mellin transform , `f(t)` : locally integrable function , `I(x)` : convolution integral , `n` : positive integer , `a_{n}` : coefficients , `b_{n}` : coefficients , `h(x)` : function and `\delta_{n}(x)` : integral
- Keywords: Mellin transform
