# §2.11 Remainder Terms; Stokes Phenomenon

Source: [https://dlmf.nist.gov/2.11](https://dlmf.nist.gov/2.11)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Deep documentation for DLMF §2.11. This page records the mathematical structure, formulas, definitions, and local dependencies exposed in the source page.

## Contents

- Numerical Use of Asymptotic Expansions
- Connection Formulas
- Exponentially-Improved Expansions
- Stokes Phenomenon
- Exponentially-Improved Expansions (continued)
- Direct Numerical Transformations

## Source Notes

- See Olver ( 1997b , pp. 76-78) .
- See Olver ( 1991a ) .
- See Olver ( 1997b , pp. 540-543) and Weniger ( 1996 ) . The computations in the example were carried out at NIST.

## Keywords

asymptotic approximations and expansions, cases of failure, numerical use of, generalized exponential integral, of large argument, via connection formulas, exponentially-improved expansions, re-expansion of remainder terms, Stokes line, Stokes phenomenon, smoothing of, Borel transform theory, applications to asymptotic expansions, asymptotic solutions of differential equations, hyperasymptotic expansions, resurgence, terminant function, Euler's transformation, Levin's transformations, Whittaker functions, application to asymptotic expansions, applied to asymptotic expansions, improved accuracy via numerical transformations, large argument

## Principal Formula Blocks

- Formula block (2.11.1)

```tex
I(m)=\int_{0}^{\pi}\frac{\cos\left(mt\right)}{t^{2}+1}\,\mathrm{d}t,
```

- Formula block (2.11.2)

```tex
I(m)\sim(-1)^{m}\sum_{s=1}^{\infty}\frac{q_{s}(\pi)}{m^{2s}},
```

- Formula block

```tex
\displaystyle q_{1}(t)
```

- Formula block

```tex
\displaystyle q_{2}(t)
```

- Formula block

```tex
\displaystyle q_{3}(t)
```

- Formula block (2.11.4)

```tex
I(10)\approx-0.00053\;18+0.00000\;48-0.00000\;01=-0.00052\;71.
```

- Formula block (2.11.5)

```tex
E_{p}\left(z\right)=\frac{e^{-z}z^{p-1}}{\Gamma\left(p\right)}\int_{0}^{\infty% }\frac{e^{-zt}t^{p-1}}{1+t}\,\mathrm{d}t
```

- Formula block (2.11.6)

```tex
E_{p}\left(z\right)\sim\frac{e^{-z}}{z}\sum_{s=0}^{\infty}(-1)^{s}\frac{{\left% (p\right)_{s}}}{z^{s}}
```

- Formula block (2.11.7)

```tex
E_{p}\left(z\right)\sim\frac{2\pi ie^{-p\pi i}}{\Gamma\left(p\right)}z^{p-1}+% \frac{e^{-z}}{z}\sum_{s=0}^{\infty}(-1)^{s}\frac{{\left(p\right)_{s}}}{z^{s}},
```

- Formula block (2.11.8)

```tex
n=\rho-p+\alpha,
```

- Formula block (2.11.9)

```tex
\frac{1}{1+t}=\sum_{s=0}^{n-1}(-1)^{s}t^{s}+(-1)^{n}\frac{t^{n}}{1+t},
```

- Formula block (2.11.10)

```tex
E_{p}\left(z\right)=\frac{e^{-z}}{z}\sum_{s=0}^{n-1}(-1)^{s}\frac{{\left(p% \right)_{s}}}{z^{s}}+(-1)^{n}\frac{2\pi}{\Gamma\left(p\right)}z^{p-1}F_{n+p}% \left(z\right),
```

- Formula block (2.11.11)

```tex
F_{n+p}\left(z\right)=\frac{e^{-z}}{2\pi}\int_{0}^{\infty}\frac{e^{-zt}t^{n+p-% 1}}{1+t}\,\mathrm{d}t=\frac{\Gamma\left(n+p\right)}{2\pi}\frac{E_{n+p}\left(z% \right)}{z^{n+p-1}}.
```

- Formula block (2.11.12)

```tex
F_{n+p}\left(z\right)=\frac{e^{-z}}{2\pi}\int_{0}^{\infty}\exp\left(-\rho\left% (te^{i\theta}-\ln t\right)\right)\frac{t^{\alpha-1}}{1+t}\,\mathrm{d}t.
```

- Formula block (2.11.13)

```tex
F_{n+p}\left(z\right)\sim\frac{e^{-i(\rho+\alpha)\theta}}{1+e^{-i\theta}}\frac% {e^{-\rho-z}}{(2\pi\rho)^{1/2}}\sum_{s=0}^{\infty}\frac{a_{2s}(\theta,\alpha)}% {\rho^{s}},
```

- Formula block (2.11.14)

```tex
a_{2}(\theta,\alpha)=\frac{1}{12}(6\alpha^{2}-6\alpha+1)-\frac{\alpha}{1+e^{i% \theta}}+\frac{1}{(1+e^{i\theta})^{2}}.
```

- Formula block (2.11.15)

```tex
F_{n+p}\left(z\right)\sim(-1)^{n}ie^{-p\pi i}\left(\tfrac{1}{2}\operatorname{% erfc}\left(\sqrt{\tfrac{1}{2}\rho}\,c(\theta)\right)-i\frac{e^{i\rho(\pi-% \theta)}e^{-\rho-z}}{(2\pi\rho)^{1/2}}\sum_{s=0}^{\infty}\frac{h_{2s}(\theta,% \alpha)}{\rho^{s}}\right).
```

- Formula block (2.11.16)

```tex
c(\theta)=\sqrt{2(1+e^{i\theta}+i(\theta-\pi))},
```

- Formula block (2.11.17)

```tex
h_{2s}(\theta,\alpha)=\frac{e^{i\alpha(\pi-\theta)}}{1+e^{-i\theta}}a_{2s}(% \theta,\alpha)+(-1)^{s-1}i\frac{1\cdot 3\cdot 5\cdot\cdot\cdot(2s-1)}{(c(% \theta))^{2s+1}},
```

- Formula block (2.11.18)

```tex
h_{0}(\theta,\alpha)=\frac{e^{i\alpha(\pi-\theta)}}{1+e^{-i\theta}}-\frac{i}{c% (\theta)}.
```

- Formula block (2.11.19)

```tex
w_{j}(z)=e^{\lambda_{j}z}z^{\mu_{j}}\sum_{s=0}^{n-1}\frac{a_{s,j}}{z^{s}}+R_{n% }^{(j)}(z),
```

- Formula block (2.11.20)

```tex
\displaystyle R_{n}^{(1)}(z)
```

- Formula block (2.11.21)

```tex
\displaystyle R_{n}^{(2)}(z)
```

- Formula block (2.11.22)

```tex
\displaystyle R_{m,n}^{(1)}(z)
```

- Formula block (2.11.23)

```tex
\displaystyle R_{m,n}^{(2)}(z)
```

- Formula block (2.11.24)

```tex
e^{x}E_{1}\left(x\right)\sim\sum_{s=0}^{\infty}(-1)^{s}\frac{s!}{x^{s+1}},
```

- Formula block (2.11.25)

```tex
e^{5}E_{1}\left(5\right)=0.20000-0.04000+0.01600-0.00960+0.00768-0.00768+0.009% 22-0.01290+0.02064-0.03716+0.07432-\cdots.
```

- Formula block (2.11.26)

```tex
e^{5}E_{1}\left(5\right)=0.17042\dots.
```

- Formula block

```tex
\displaystyle\Delta^{0}
```

- Formula block

```tex
\displaystyle\Delta^{1}
```

- Formula block

```tex
\displaystyle\Delta^{2}
```

- Formula block

```tex
\displaystyle\Delta^{3}
```

- Formula block

```tex
\displaystyle\Delta^{4}
```

- Formula block

```tex
\displaystyle\Delta^{5}
```

- Formula block (2.11.28)

```tex
0.00384-0.00038+0.00027-0.00012+0.00009-0.00007=0.00363.
```

- Formula block (2.11.29)

```tex
W_{\kappa,\mu}\left(z\right)\sim\sum_{n=0}^{\infty}a_{n},
```

- Formula block (2.11.30)

```tex
a_{n}=\frac{e^{-z/2}}{z^{n-\kappa}n!}\left(\mu^{2}-(\kappa-\tfrac{1}{2})^{2}% \right)\*\left(\mu^{2}-(\kappa-\tfrac{3}{2})^{2}\right)\*\cdot\cdot\cdot\left(% \mu^{2}-(\kappa-n+\tfrac{1}{2})^{2}\right).
```

- Formula block (2.11.31)

```tex
W_{2.3,0.5}\left(1.0\right)=-0.83299\;50268\;27526\;\cdots
```

- Formula block (2.11.32)

```tex
d_{n}=\frac{\sum_{j=0}^{n}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{n}{j}(j+1)^{n-1}% \frac{s_{j}}{a_{j+1}}}{\sum_{j=0}^{n}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{n}{j}(j+1% )^{n-1}\frac{1}{a_{j+1}}}.
```


## Definitions and Symbols

- Keywords: asymptotic approximations and expansions , cases of failure , numerical use of
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `I(m)` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `I(m)` : integral and `q_{s}(t)` : coefficients
- Symbols: `q_{s}(t)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion and `I(m)` : integral
- Keywords: asymptotic approximations and expansions , generalized exponential integral , of large argument , via connection formulas
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\int` : integral
- Symbols: `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm and `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\mathrm{i}` : imaginary unit
- Keywords: asymptotic approximations and expansions , exponentially-improved expansions , re-expansion of remainder terms
- Symbols: `\rho` : radius
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function
- Defines: `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\int` : integral
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius and `\theta` : radius
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius , `\theta` : radius and `a_{2s}(\theta,\alpha)` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius and `a_{2s}(\theta,\alpha)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{erfc}\NVar{z}` : complementary error function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius , `\theta` : radius , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius and `c(\theta)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius , `a_{2s}(\theta,\alpha)` : coefficients , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions
- Keywords: Stokes line , Stokes phenomenon , asymptotic approximations and expansions , smoothing of
- Symbols: `\operatorname{erfc}\NVar{z}` : complementary error function , `\theta` : radius and `c(\theta)`
- Keywords: Borel transform theory , applications to asymptotic expansions , asymptotic approximations and expansions , asymptotic solutions of differential equations , exponentially-improved expansions , hyperasymptotic expansions , resurgence , terminant function
- Symbols: `\mathrm{e}` : base of natural logarithm , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\operatorname{ph}` : phase , `R_{n}^{(j)}(z)` : remainder and `\delta` : positive constant
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\operatorname{ph}` : phase , `R_{n}^{(j)}(z)` : remainder and `\delta` : positive constant
- Keywords: Euler's transformation , Levin's transformations , Whittaker functions , application to asymptotic expansions , applied to asymptotic expansions , asymptotic approximations and expansions , improved accuracy via numerical transformations , large argument , numerical use of , re-expansion of remainder terms
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `E_{1}\left(\NVar{z}\right)` : exponential integral and `!` : factorial (as in `n!` )
- Symbols: `\mathrm{e}` : base of natural logarithm and `E_{1}\left(\NVar{z}\right)` : exponential integral
- Symbols: `\mathrm{e}` : base of natural logarithm and `E_{1}\left(\NVar{z}\right)` : exponential integral
- Symbols: `\Delta^{j}` : `j` th forward difference
- Symbols: `W_{\NVar{\kappa},\NVar{\mu}}\left(\NVar{z}\right)` : Whittaker confluent hypergeometric function , `\sim` : Poincar asymptotic expansion and `a_{n}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) and `a_{n}` : coefficients
- Symbols: `a_{n}` : coefficients and `d_{n}` : coeffient
- Symbols: `W_{\NVar{\kappa},\NVar{\mu}}\left(\NVar{z}\right)` : Whittaker confluent hypergeometric function
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `a_{n}` : coefficients and `d_{n}` : coeffient

## Subsections

### 2.11(i) Numerical Use of Asymptotic Expansions

- When a rigorous bound or reliable estimate for the remainder term is unavailable, it is unsafe to judge the accuracy of an asymptotic expansion merely from the numerical rate of decrease of the terms at the point of truncation. Even when the series converges this is unwise: the tail needs to be majorized rigorously before the result can be guaranteed. For divergent expansions the situation is even more difficult. First, it is impossible to bound the tail by majorizing its terms. Secondly, the asymptotic series represents an infinite class of functions, and the remainder depends on which member we have in mind.
- As an example consider
- with `m` a large integer. By integration by parts ( 2.3(i) )
- with
- On rounding to 5D, we have `q_{1}(\pi)=-0.05318` , `q_{2}(\pi)=0.04791` , `q_{3}(\pi)=-0.08985` . Taking `m=10` in ( 2.11.2 ), the first three terms give us the approximation
- But this answer is incorrect: to 7D `I(10)=-0.00045\;58` . The error term is, in fact, approximately 700 times the last term obtained in ( 2.11.4 ). The explanation is that ( 2.11.2 ) is a more accurate expansion for the function `I(m)-\frac{1}{2}\pi e^{-m}` than it is for `I(m)` ; see Olver ( 1997b , pp. 76-78) .

Formula blocks:
- Formula block (2.11.1)

```tex
I(m)=\int_{0}^{\pi}\frac{\cos\left(mt\right)}{t^{2}+1}\,\mathrm{d}t,
```

- Formula block (2.11.2)

```tex
I(m)\sim(-1)^{m}\sum_{s=1}^{\infty}\frac{q_{s}(\pi)}{m^{2s}},
```

- Formula block

```tex
\displaystyle q_{1}(t)
```

- Formula block

```tex
\displaystyle q_{2}(t)
```

- Formula block

```tex
\displaystyle q_{3}(t)
```

- Formula block (2.11.4)

```tex
I(10)\approx-0.00053\;18+0.00000\;48-0.00000\;01=-0.00052\;71.
```


Local metadata:
- Keywords: asymptotic approximations and expansions , cases of failure , numerical use of
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\cos\NVar{z}` : cosine function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\int` : integral and `I(m)` : integral
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `I(m)` : integral and `q_{s}(t)` : coefficients
- Symbols: `q_{s}(t)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion and `I(m)` : integral

### 2.11(ii) Connection Formulas

- From  8.19(i) the generalized exponential integral is given by
- when `\Re p>0` and `|\operatorname{ph}z|<\frac{1}{2}\pi` , and by analytic continuation for other values of `p` and `z` . Application of Watson's lemma ( 2.4(i) ) yields
- when `p` is fixed and `z\to\infty` in any closed sector within `|\operatorname{ph}z|<\frac{3}{2}\pi` . As noted in  2.11(i) , poor accuracy is yielded by this expansion as `\operatorname{ph}z` approaches `\frac{3}{2}\pi` or `-\frac{3}{2}\pi` . However, on combining ( 2.11.6 ) with the connection formula ( 8.19.18 ), with `m=1` , we derive
- valid as `z\to\infty` in any closed sector within `\frac{1}{2}\pi<\operatorname{ph}z<\frac{7}{2}\pi` ; compare ( 8.20.3 ). Since the ray `\operatorname{ph}z=\frac{3}{2}\pi` is well away from the new boundaries, the compound expansion ( 2.11.7 ) yields much more accurate results when `\operatorname{ph}z\to\frac{3}{2}\pi` . In effect, ( 2.11.7 ) "corrects" ( 2.11.6 ) by introducing a term that is relatively exponentially small in the neighborhood of `\operatorname{ph}z=\pi` , is increasingly significant as `\operatorname{ph}z` passes from `\pi` to `\frac{3}{2}\pi` , and becomes the dominant contribution after `\operatorname{ph}z` passes `\frac{3}{2}\pi` . See also  2.11(iv) .

Formula blocks:
- Formula block (2.11.5)

```tex
E_{p}\left(z\right)=\frac{e^{-z}z^{p-1}}{\Gamma\left(p\right)}\int_{0}^{\infty% }\frac{e^{-zt}t^{p-1}}{1+t}\,\mathrm{d}t
```

- Formula block (2.11.6)

```tex
E_{p}\left(z\right)\sim\frac{e^{-z}}{z}\sum_{s=0}^{\infty}(-1)^{s}\frac{{\left% (p\right)_{s}}}{z^{s}}
```

- Formula block (2.11.7)

```tex
E_{p}\left(z\right)\sim\frac{2\pi ie^{-p\pi i}}{\Gamma\left(p\right)}z^{p-1}+% \frac{e^{-z}}{z}\sum_{s=0}^{\infty}(-1)^{s}\frac{{\left(p\right)_{s}}}{z^{s}},
```


Local metadata:
- Keywords: asymptotic approximations and expansions , generalized exponential integral , of large argument , via connection formulas
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\int` : integral
- Symbols: `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm and `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\mathrm{i}` : imaginary unit

### 2.11(iii) Exponentially-Improved Expansions

- The procedure followed in  2.11(ii) enabled `E_{p}\left(z\right)` to be computed with as much accuracy in the sector `\pi\leq\operatorname{ph}z\leq 3\pi` as the original expansion ( 2.11.6 ) in `|\operatorname{ph}z|\leq\pi` . We now increase substantially the accuracy of ( 2.11.6 ) in `|\operatorname{ph}z|\leq\pi` by re-expanding the remainder term.
- Optimum truncation in ( 2.11.6 ) takes place at `s=n-1` , with `|p+n-1|=|z|` , approximately. Thus
- where `z=\rho e^{i\theta}` , and `|\alpha|` is bounded as `n\to\infty` . From ( 2.11.5 ) and the identity
- we have
- where
- With `n` given by ( 2.11.8 ), we have

Formula blocks:
- Formula block (2.11.8)

```tex
n=\rho-p+\alpha,
```

- Formula block (2.11.9)

```tex
\frac{1}{1+t}=\sum_{s=0}^{n-1}(-1)^{s}t^{s}+(-1)^{n}\frac{t^{n}}{1+t},
```

- Formula block (2.11.10)

```tex
E_{p}\left(z\right)=\frac{e^{-z}}{z}\sum_{s=0}^{n-1}(-1)^{s}\frac{{\left(p% \right)_{s}}}{z^{s}}+(-1)^{n}\frac{2\pi}{\Gamma\left(p\right)}z^{p-1}F_{n+p}% \left(z\right),
```

- Formula block (2.11.11)

```tex
F_{n+p}\left(z\right)=\frac{e^{-z}}{2\pi}\int_{0}^{\infty}\frac{e^{-zt}t^{n+p-% 1}}{1+t}\,\mathrm{d}t=\frac{\Gamma\left(n+p\right)}{2\pi}\frac{E_{n+p}\left(z% \right)}{z^{n+p-1}}.
```

- Formula block (2.11.12)

```tex
F_{n+p}\left(z\right)=\frac{e^{-z}}{2\pi}\int_{0}^{\infty}\exp\left(-\rho\left% (te^{i\theta}-\ln t\right)\right)\frac{t^{\alpha-1}}{1+t}\,\mathrm{d}t.
```

- Formula block (2.11.13)

```tex
F_{n+p}\left(z\right)\sim\frac{e^{-i(\rho+\alpha)\theta}}{1+e^{-i\theta}}\frac% {e^{-\rho-z}}{(2\pi\rho)^{1/2}}\sum_{s=0}^{\infty}\frac{a_{2s}(\theta,\alpha)}% {\rho^{s}},
```

- Formula block (2.11.14)

```tex
a_{2}(\theta,\alpha)=\frac{1}{12}(6\alpha^{2}-6\alpha+1)-\frac{\alpha}{1+e^{i% \theta}}+\frac{1}{(1+e^{i\theta})^{2}}.
```

- Formula block (2.11.15)

```tex
F_{n+p}\left(z\right)\sim(-1)^{n}ie^{-p\pi i}\left(\tfrac{1}{2}\operatorname{% erfc}\left(\sqrt{\tfrac{1}{2}\rho}\,c(\theta)\right)-i\frac{e^{i\rho(\pi-% \theta)}e^{-\rho-z}}{(2\pi\rho)^{1/2}}\sum_{s=0}^{\infty}\frac{h_{2s}(\theta,% \alpha)}{\rho^{s}}\right).
```

- Formula block (2.11.16)

```tex
c(\theta)=\sqrt{2(1+e^{i\theta}+i(\theta-\pi))},
```

- Formula block (2.11.17)

```tex
h_{2s}(\theta,\alpha)=\frac{e^{i\alpha(\pi-\theta)}}{1+e^{-i\theta}}a_{2s}(% \theta,\alpha)+(-1)^{s-1}i\frac{1\cdot 3\cdot 5\cdot\cdot\cdot(2s-1)}{(c(% \theta))^{2s+1}},
```

- Formula block (2.11.18)

```tex
h_{0}(\theta,\alpha)=\frac{e^{i\alpha(\pi-\theta)}}{1+e^{-i\theta}}-\frac{i}{c% (\theta)}.
```


Local metadata:
- Keywords: asymptotic approximations and expansions , exponentially-improved expansions , re-expansion of remainder terms
- Symbols: `\rho` : radius
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `{\left(\NVar{a}\right)_{\NVar{n}}}` : Pochhammer's symbol (or shifted factorial) , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function
- Defines: `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function
- Symbols: `\Gamma\left(\NVar{z}\right)` : gamma function , `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\mathrm{e}` : base of natural logarithm , `E_{\NVar{p}}\left(\NVar{z}\right)` : generalized exponential integral and `\int` : integral
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\,\mathrm{d}\NVar{x}` : differential of `x` , `\exp\NVar{z}` : exponential function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\int` : integral , `\ln\NVar{z}` : principal branch of logarithm function , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius and `\theta` : radius
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius , `\theta` : radius and `a_{2s}(\theta,\alpha)` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius and `a_{2s}(\theta,\alpha)` : coefficients
- Symbols: `\sim` : Poincar asymptotic expansion , `\pi` : the ratio of the circumference of a circle to its diameter , `\operatorname{erfc}\NVar{z}` : complementary error function , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `\rho` : radius , `\theta` : radius , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius and `c(\theta)`
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius , `a_{2s}(\theta,\alpha)` : coefficients , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `\theta` : radius , `c(\theta)` and `h_{2s}(\theta,\alpha)` : functions

### 2.11(iv) Stokes Phenomenon

- Two different asymptotic expansions in terms of elementary functions, ( 2.11.6 ) and ( 2.11.7 ), are available for the generalized exponential integral in the sector `\frac{1}{2}\pi<\operatorname{ph}z<\frac{3}{2}\pi` . That the change in their forms is discontinuous, even though the function being approximated is analytic, is an example of the Stokes phenomenon . Where should the change-over take place? Can it be accomplished smoothly?
- Satisfactory answers to these questions were found by Berry ( 1989 ) ; see also the survey by Paris and Wood ( 1995 ) . These answers are linked to the terms involving the complementary error function in the more powerful expansions typified by the combination of ( 2.11.10 ) and ( 2.11.15 ). Thus if `0\leq\theta\leq\pi-\delta` ( `<\pi` ), then `c(\theta)` lies in the right half-plane. Hence from  7.12(i) `\operatorname{erfc}\left(\sqrt{\frac{1}{2}\rho}\;c(\theta)\right)` is of the same exponentially-small order of magnitude as the contribution from the other terms in ( 2.11.15 ) when `\rho` is large. On the other hand, when `\pi+\delta\leq\theta\leq 3\pi-\delta` , `c(\theta)` is in the left half-plane and `\operatorname{erfc}\left(\sqrt{\frac{1}{2}\rho}\;c(\theta)\right)` differs from 2 by an exponentially-small quantity. In the transition through `\theta=\pi` , `\operatorname{erfc}\left(\sqrt{\frac{1}{2}\rho}\;c(\theta)\right)` changes very rapidly, but smoothly, from one form to the other; compare the graph of its modulus in Figure 2.11.1 in the case `\rho=100` .
- In particular, on the ray `\theta=\pi` greatest accuracy is achieved by (a) taking the average of the expansions ( 2.11.6 ) and ( 2.11.7 ), followed by (b) taking account of the exponentially-small contributions arising from the terms involving `h_{2s}(\theta,\alpha)` in ( 2.11.15 ).
- Rays (or curves) on which one contribution in a compound asymptotic expansion achieves maximum dominance over another are called Stokes lines ( `\theta=\pi` in the present example). As these lines are crossed exponentially-small contributions, such as that in ( 2.11.7 ), are "switched on" smoothly, in the manner of the graph in Figure 2.11.1 .
- For higher-order Stokes phenomena see Olde Daalhuis ( 2004b ) and Howls et al. ( 2004 ) .

Local metadata:
- Keywords: Stokes line , Stokes phenomenon , asymptotic approximations and expansions , smoothing of
- Symbols: `\operatorname{erfc}\NVar{z}` : complementary error function , `\theta` : radius and `c(\theta)`

### 2.11(v) Exponentially-Improved Expansions (continued)

- Expansions similar to ( 2.11.15 ) can be constructed for many other special functions. However, to enjoy the resurgence property ( 2.7(ii) ) we often seek instead expansions in terms of the `F` -functions introduced in  2.11(iii) , leaving the connection of the error-function type behavior as an implicit consequence of this property of the `F` -functions. In this context the `F` -functions are called terminants , a name introduced by Dingle ( 1973 ) .
- For illustration, we give re-expansions of the remainder terms in the expansions ( 2.7.8 ) arising in differential-equation theory. For notational convenience assume that the original differential equation ( 2.7.1 ) is normalized so that `\lambda_{2}-\lambda_{1}=1` . (This means that, if necessary, `z` is replaced by `z/(\lambda_{2}-\lambda_{1})` .) From ( 2.7.12 ), ( 2.7.13 ) it is then seen that the optimum number of terms, `n` , in ( 2.7.14 ) is approximately `|z|` . We set
- and expand
- with `m=0,1,2,\dots` , and `C_{1},C_{2}` as in ( 2.7.17 ). Then as `z\to\infty` , with `|n-|z||` bounded and `m` fixed,
- uniformly with respect to `\operatorname{ph}z` in each case.
- The relevant Stokes lines are `\operatorname{ph}z=\pm\pi` for `w_{1}(z)` , and `\operatorname{ph}z=0,2\pi` for `w_{2}(z)` . In addition to achieving uniform exponential improvement, particularly in `|\operatorname{ph}z|\leq\pi` for `w_{1}(z)` , and `0\leq\operatorname{ph}z\leq 2\pi` for `w_{2}(z)` , the re-expansions ( 2.11.20 ), ( 2.11.21 ) are resurgent.

Formula blocks:
- Formula block (2.11.19)

```tex
w_{j}(z)=e^{\lambda_{j}z}z^{\mu_{j}}\sum_{s=0}^{n-1}\frac{a_{s,j}}{z^{s}}+R_{n% }^{(j)}(z),
```

- Formula block (2.11.20)

```tex
\displaystyle R_{n}^{(1)}(z)
```

- Formula block (2.11.21)

```tex
\displaystyle R_{n}^{(2)}(z)
```

- Formula block (2.11.22)

```tex
\displaystyle R_{m,n}^{(1)}(z)
```

- Formula block (2.11.23)

```tex
\displaystyle R_{m,n}^{(2)}(z)
```


Local metadata:
- Keywords: Borel transform theory , applications to asymptotic expansions , asymptotic approximations and expansions , asymptotic solutions of differential equations , exponentially-improved expansions , hyperasymptotic expansions , resurgence , terminant function
- Symbols: `\mathrm{e}` : base of natural logarithm , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `w_{j}(z)` : solutions
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\mathrm{i}` : imaginary unit , `F_{\NVar{p}}\left(\NVar{z}\right)` : terminant function , `R_{n}^{(j)}(z)` : remainder , `a_{s,j}` : coefficients , `\lambda_{j}` : roots , `\mu_{j}` : quantities and `C_{1}` , `C_{2}` : Stokes multipliers
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\operatorname{ph}` : phase , `R_{n}^{(j)}(z)` : remainder and `\delta` : positive constant
- Symbols: `O\left(\NVar{x}\right)` : order not exceeding , `\pi` : the ratio of the circumference of a circle to its diameter , `\mathrm{e}` : base of natural logarithm , `\operatorname{ph}` : phase , `R_{n}^{(j)}(z)` : remainder and `\delta` : positive constant

### 2.11(vi) Direct Numerical Transformations

- The transformations in  3.9 for summing slowly convergent series can also be very effective when applied to divergent asymptotic series.
- A simple example is provided by Euler's transformation ( 3.9(ii) ) applied to the asymptotic expansion for the exponential integral ( 6.12(i) ):
- Taking `x=5` and rounding to 5D, we obtain
- The numerically smallest terms are the 5th and 6th. Truncation after 5 terms yields 0.17408, compared with the correct value
- We now compute the forward differences `\Delta^{j}` , `j=0,1,2,\dots` , of the moduli of the rounded values of the first 6 neglected terms:
- Multiplying these differences by `(-1)^{j}2^{-j-1}` and summing, we obtain

Formula blocks:
- Formula block (2.11.24)

```tex
e^{x}E_{1}\left(x\right)\sim\sum_{s=0}^{\infty}(-1)^{s}\frac{s!}{x^{s+1}},
```

- Formula block (2.11.25)

```tex
e^{5}E_{1}\left(5\right)=0.20000-0.04000+0.01600-0.00960+0.00768-0.00768+0.009% 22-0.01290+0.02064-0.03716+0.07432-\cdots.
```

- Formula block (2.11.26)

```tex
e^{5}E_{1}\left(5\right)=0.17042\dots.
```

- Formula block

```tex
\displaystyle\Delta^{0}
```

- Formula block

```tex
\displaystyle\Delta^{1}
```

- Formula block

```tex
\displaystyle\Delta^{2}
```

- Formula block

```tex
\displaystyle\Delta^{3}
```

- Formula block

```tex
\displaystyle\Delta^{4}
```

- Formula block

```tex
\displaystyle\Delta^{5}
```

- Formula block (2.11.28)

```tex
0.00384-0.00038+0.00027-0.00012+0.00009-0.00007=0.00363.
```

- Formula block (2.11.29)

```tex
W_{\kappa,\mu}\left(z\right)\sim\sum_{n=0}^{\infty}a_{n},
```

- Formula block (2.11.30)

```tex
a_{n}=\frac{e^{-z/2}}{z^{n-\kappa}n!}\left(\mu^{2}-(\kappa-\tfrac{1}{2})^{2}% \right)\*\left(\mu^{2}-(\kappa-\tfrac{3}{2})^{2}\right)\*\cdot\cdot\cdot\left(% \mu^{2}-(\kappa-n+\tfrac{1}{2})^{2}\right).
```

- Formula block (2.11.31)

```tex
W_{2.3,0.5}\left(1.0\right)=-0.83299\;50268\;27526\;\cdots
```

- Formula block (2.11.32)

```tex
d_{n}=\frac{\sum_{j=0}^{n}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{n}{j}(j+1)^{n-1}% \frac{s_{j}}{a_{j+1}}}{\sum_{j=0}^{n}(-1)^{j}\genfrac{(}{)}{0.0pt}{}{n}{j}(j+1% )^{n-1}\frac{1}{a_{j+1}}}.
```


Local metadata:
- Keywords: Euler's transformation , Levin's transformations , Whittaker functions , application to asymptotic expansions , applied to asymptotic expansions , asymptotic approximations and expansions , improved accuracy via numerical transformations , large argument , numerical use of , re-expansion of remainder terms
- Symbols: `\sim` : Poincar asymptotic expansion , `\mathrm{e}` : base of natural logarithm , `E_{1}\left(\NVar{z}\right)` : exponential integral and `!` : factorial (as in `n!` )
- Symbols: `\mathrm{e}` : base of natural logarithm and `E_{1}\left(\NVar{z}\right)` : exponential integral
- Symbols: `\mathrm{e}` : base of natural logarithm and `E_{1}\left(\NVar{z}\right)` : exponential integral
- Symbols: `\Delta^{j}` : `j` th forward difference
- Symbols: `W_{\NVar{\kappa},\NVar{\mu}}\left(\NVar{z}\right)` : Whittaker confluent hypergeometric function , `\sim` : Poincar asymptotic expansion and `a_{n}` : coefficients
- Symbols: `\mathrm{e}` : base of natural logarithm , `!` : factorial (as in `n!` ) and `a_{n}` : coefficients
- Symbols: `a_{n}` : coefficients and `d_{n}` : coeffient
- Symbols: `W_{\NVar{\kappa},\NVar{\mu}}\left(\NVar{z}\right)` : Whittaker confluent hypergeometric function
- Symbols: `\genfrac{(}{)}{0.0pt}{}{\NVar{m}}{\NVar{n}}` : binomial coefficient , `a_{n}` : coefficients and `d_{n}` : coeffient
