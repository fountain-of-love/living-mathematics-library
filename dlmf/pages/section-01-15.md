# §1.15 Summability Methods

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.15, `Summability Methods`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Definitions for Series
- Regularity
- Summability of Fourier Series
- Definitions for Integrals
- Summability of Fourier Integrals
- Fractional Integrals
- Fractional Derivatives
- Tauberian Theorems

### Subsections

#### 1.15(i) Definitions for Series

Formulas:

Formula 1.15.1:

$$
s_{n}=\sum_{k=0}^{n}a_{k}.
$$

Formula 1.15.2:

$$
\sum^{\infty}_{n=0}a_{n}=s\quad(A),
$$

Formula 1.15.3:

$$
\lim_{x\to 1-}\sum^{\infty}_{n=0}a_{n}x^{n}=s.
$$

Formula 1.15.4:

$$
\sum^{\infty}_{n=0}a_{n}=s\quad(C,1),
$$

Formula 1.15.5:

$$
\lim_{n\to\infty}\frac{s_{0}+s_{1}+\dots+s_{n}}{n+1}=s.
$$

Formula 1.15.6:

$$
\sum^{\infty}_{n=0}a_{n}=s\quad(C,\alpha),
$$

Formula 1.15.7:

$$
\lim_{n\to\infty}\frac{n!}{(\alpha+1)_{n}}\sum^{n}_{k=0}\frac{(\alpha+1)_{k}}{k!}a_{n-k}=s.
$$

Formula 1.15.8:

$$
\sum^{\infty}_{n=0}a_{n}=s\quad(B),
$$

Formula 1.15.9:

$$
\lim_{t\to\infty}{\mathrm{e}}^{-t}\sum^{\infty}_{n=0}\frac{s_{n}}{n!}t^{n}=s.
$$


Definitions and local symbols:
- Symbols: $k$ : integer and $n$ : nonnegative integer
- Keywords: Abel , Abel summability , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer
- Keywords: Cesro , Cesro summability , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer
- Keywords: Cesro , general , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $!$ : factorial (as in $n!$ ) , $k$ : integer and $n$ : nonnegative integer
- Keywords: Borel , Borel summability , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) and $n$ : nonnegative integer

#### 1.15(ii) Regularity

- Methods of summation are regular if they are consistent with conventional summation. All of the methods described in  1.15(i) are regular. For example if
- then

Formulas:

Formula 1.15.10:

$$
\sum^{\infty}_{n=0}a_{n}=s,
$$

Formula 1.15.11:

$$
\sum^{\infty}_{n=0}a_{n}=s\quad(A).
$$


Definitions and local symbols:
- Keywords: convergence , regular , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer

#### 1.15(iii) Summability of Fourier Series

Formulas:

Formula 1.15.12:

$$
P(r,\theta)=\frac{1-r^{2}}{1-2r\cos\theta+r^{2}}=\sum^{\infty}_{n=-\infty}r^{\left|n\right|}{\mathrm{e}}^{\mathrm{i}n\theta},
$$

Formula 1.15.13:

$$
\frac{1}{2\pi}\int^{2\pi}_{0}P(r,\theta)\,\mathrm{d}\theta=1.
$$

Formula 1.15.14:

$$
P(r,\theta)\to 0,
$$

Formula 1.15.15:

$$
K_{n}(\theta)=\frac{1}{n+1}\left(\frac{\sin\left(\tfrac{1}{2}(n+1)\theta\right)}{\sin\left(\tfrac{1}{2}\theta\right)}\right)^{2},
$$

Formula 1.15.16:

$$
\frac{1}{2\pi}\int^{2\pi}_{0}K_{n}(\theta)\,\mathrm{d}\theta=1.
$$

Formula 1.15.17:

$$
K_{n}(\theta)\to 0,
$$

Formula 1.15.18:

$$
A(r,\theta)=\sum^{\infty}_{n=-\infty}r^{\left|n\right|}F(n){\mathrm{e}}^{\mathrm{i}n\theta},
$$

Formula 1.15.19:

$$
F(n)=\frac{1}{2\pi}\int^{2\pi}_{0}f(t){\mathrm{e}}^{-\mathrm{i}nt}\,\mathrm{d}t.
$$

Formula 1.15.20:

$$
A(r,\theta)=\frac{1}{2\pi}\int^{2\pi}_{0}P(r,\theta-t)f(t)\,\mathrm{d}t.
$$

Formula 1.15.21:

$$
\sigma_{n}(\theta)=\frac{s_{0}(\theta)+s_{1}(\theta)+\dots+s_{n}(\theta)}{n+1},
$$

Formula 1.15.22:

$$
s_{n}(\theta)=\sum^{n}_{k=-n}F(k){\mathrm{e}}^{\mathrm{i}k\theta}.
$$

Formula 1.15.23:

$$
\sigma_{n}(\theta)=\frac{1}{2\pi}\int^{2\pi}_{0}K_{n}(\theta-t)f(t)\,\mathrm{d}t.
$$

Formula 1.15.24:

$$
\tfrac{1}{2}(f(\theta+)+f(\theta-))
$$

Formula 1.15.25:

$$
\sum^{\infty}_{n=-\infty}F(n){\mathrm{e}}^{\mathrm{i}n\theta}
$$

Formula 1.15.26:

$$
F(0)+2\sum^{\infty}_{n=1}F(n){\mathrm{e}}^{\mathrm{i}n\theta}
$$

Formula 1.15.27:

$$
G(z)=G(x+\mathrm{i}y)=u(x,y)+\mathrm{i}v(x,y)=F(0)+2\sum^{\infty}_{n=1}F(n)z^{n}.
$$

Formula 1.15.28:

$$
-\sum^{\infty}_{n=-\infty}\mathrm{i}(\operatorname{sign}n)F(n)r^{\left|n\right|}{\mathrm{e}}^{\mathrm{i}n\theta};
$$


Definitions and local symbols:
- Keywords: Fourier series , summability
- Keywords: Fourier series , Poisson kernel , summability methods for series
- Defines: $P(r,\theta)$ : Poisson kernel (locally)
- Symbols: $\cos z$ : cosine function , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $P(r,\theta)$ : Poisson kernel
- Symbols: $P(r,\theta)$ : Poisson kernel
- Keywords: Fejr kernel , Fourier series , summability methods for series
- Defines: $K_{n}(\theta)$ : Fejr kernel (locally)
- Symbols: $\sin z$ : sine function and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $K_{n}(\theta)$ : Fejr kernel
- Symbols: $n$ : nonnegative integer and $K_{n}(\theta)$ : Fejr kernel
- Keywords: Abel means , Fourier series , summability methods for series
- Defines: $A(r,\theta)$ : Abel mean (locally)
- Symbols: $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $n$ : nonnegative integer , $F(n)$ and $\left|x\right|$ : absolute value of $x$
- Defines: $F(n)$ (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $P(r,\theta)$ : Poisson kernel and $A(r,\theta)$ : Abel mean
- Keywords: Cesro means , Fourier series , summability methods for series
- Defines: $\sigma_{n}(\theta)$ : Cesro mean (locally)
- Symbols: $n$ : nonnegative integer

#### 1.15(iv) Definitions for Integrals

Formulas:

Formula 1.15.29:

$$
\int^{\infty}_{-\infty}f(t)\,\mathrm{d}t=L\quad(A),
$$

Formula 1.15.30:

$$
\lim_{\epsilon\to 0+}\int^{\infty}_{-\infty}{\mathrm{e}}^{-\epsilon\left|t\right|}f(t)\,\mathrm{d}t=L.
$$

Formula 1.15.31:

$$
\int^{\infty}_{-\infty}f(t)\,\mathrm{d}t=L\quad(C,1),
$$

Formula 1.15.32:

$$
\lim_{R\to\infty}\int^{R}_{-R}\left(1-\frac{\left|t\right|}{R}\right)f(t)\,\mathrm{d}t=L.
$$


Definitions and local symbols:
- Keywords: integrals , summability methods
- Keywords: Abel , Abel summability , summability methods for integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Keywords: Cesro , Cesro summability , infinite series , summability methods , summability methods for integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left|x\right|$ : absolute value of $x$

#### 1.15(v) Summability of Fourier Integrals

Formulas:

Formula 1.15.33:

$$
P(x,y)=\frac{2y}{x^{2}+y^{2}},
$$

Formula 1.15.34:

$$
\frac{1}{2\pi}\int^{\infty}_{-\infty}P(x,y)\,\mathrm{d}x=1.
$$

Formula 1.15.35:

$$
\int_{\left|x\right|\geq\delta}P(x,y)\,\mathrm{d}x\to 0,
$$

Formula 1.15.36:

$$
h(x,y)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}{\mathrm{e}}^{-y\left|t\right|}{\mathrm{e}}^{-\mathrm{i}xt}F(t)\,\mathrm{d}t,
$$

Formula 1.15.37:

$$
h(x,y)=\frac{1}{2\pi}\int^{\infty}_{-\infty}f(t)P(x-t,y)\,\mathrm{d}t
$$

Formula 1.15.38:

$$
\lim_{y\to 0+}\int^{\infty}_{-\infty}\left|h(x,y)-f(x)\right|\,\mathrm{d}x=0.
$$

Formula 1.15.39:

$$
\Phi(z)=\Phi(x+\mathrm{i}y)=\frac{\mathrm{i}}{\pi}\int^{\infty}_{-\infty}f(t)\frac{1}{(x-t)+\mathrm{i}y}\,\mathrm{d}t,
$$

Formula 1.15.40:

$$
\Im\Phi(x+\mathrm{i}y)=\frac{1}{\pi}\int^{\infty}_{-\infty}f(t)\frac{x-t}{(x-t)^{2}+y^{2}}\,\mathrm{d}t
$$

Formula 1.15.41:

$$
K_{R}(s)=\frac{1}{\pi R}\frac{1-\cos\left(Rs\right)}{s^{2}},
$$

Formula 1.15.42:

$$
\int^{\infty}_{-\infty}K_{R}(s)\,\mathrm{d}s=1.
$$

Formula 1.15.43:

$$
\int_{\left|s\right|\geq\delta}K_{R}(s)\,\mathrm{d}s\to 0,
$$

Formula 1.15.44:

$$
\displaystyle\sigma_{R}(\theta)
$$

Formula 1.15.45:

$$
\displaystyle\sigma_{R}(\theta)
$$

Formula 1.15.46:

$$
\lim_{R\to\infty}\int^{\infty}_{-\infty}\left|\sigma_{R}(\theta)-f(\theta)\right|\,\mathrm{d}\theta=0.
$$


Definitions and local symbols:
- Keywords: Fourier integral , summability
- Keywords: Fourier integral , Fourier integrals , Fourier series , Poisson integral , Poisson kernel , conjugate , conjugate Poisson integral , summability methods for integrals
- Defines: $P(x,y)$ : Poisson kernel (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $P(x,y)$ : Poisson kernel
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $P(x,y)$ : Poisson kernel and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ , $h(x,y)$ : function and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $P(x,y)$ : Poisson kernel and $h(x,y)$ : function
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $h(x,y)$ : function and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $z$ : variable and $\Phi(z)$ : function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\Im$ : imaginary part , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\Phi(z)$ : function
- Keywords: Fejr kernel , Fourier integral , Fourier integrals , summability methods for integrals
- Defines: $K_{R}(s)$ : Fejr kernel (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter and $\cos z$ : cosine function
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $K_{R}(s)$ : Fejr kernel
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $K_{R}(s)$ : Fejr kernel and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ , $\sigma_{R}(\theta)$ : function and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $K_{R}(s)$ : Fejr kernel and $\sigma_{R}(\theta)$ : function
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sigma_{R}(\theta)$ : function and $\left|x\right|$ : absolute value of $x$

#### 1.15(vi) Fractional Integrals

- For $\Re\alpha>0$ and $x\geq 0$ , the Riemann-Liouville fractional integral of order $\alpha$ is defined by
- For $\Gamma\left(\alpha\right)$ see  5.2 , and compare ( 1.4.31 ) in the case when $\alpha$ is a positive integer.
- For extensions of ( 1.15.48 ) see Love ( 1972b ) .
- If
- then
- The lower limit $0$ of the integral in ( 1.15.47 ) can be replaced by any constant $a\leq x$ . Also, we can replace the lower and upper limits of the integral by $x$ and $a$ , respectively. In that case we must also replace $(x-t)$ in the integrand by $(t-x)$ and we can even set $a=\infty$ . See ( 18.17.9 ), ( 18.17.11 ) and ( 18.17.13 ) as examples.

Formulas:

Formula 1.15.47:

$$
I^{\alpha}f(x)=\frac{1}{\Gamma\left(\alpha\right)}\int^{x}_{0}(x-t)^{\alpha-1}f(t)\,\mathrm{d}t.
$$

Formula 1.15.48:

$$
I^{\alpha}I^{\beta}=I^{\alpha+\beta},
$$

Formula 1.15.49:

$$
f(x)=\sum^{\infty}_{k=0}a_{k}x^{k},
$$

Formula 1.15.50:

$$
I^{\alpha}f(x)=\sum^{\infty}_{k=0}\frac{k!}{\Gamma\left(k+\alpha+1\right)}a_{k}x^{k+\alpha}.
$$


Definitions and local symbols:
- Keywords: fractional integrals , summability methods for integrals
- Defines: $I^{\alpha}$ : fractional integral (locally)
- Symbols: $\Gamma\left(z\right)$ : gamma function , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\Re$ : real part and $I^{\alpha}$ : fractional integral
- Symbols: $k$ : integer
- Symbols: $\Gamma\left(z\right)$ : gamma function , $!$ : factorial (as in $n!$ ) , $k$ : integer and $I^{\alpha}$ : fractional integral

#### 1.15(vii) Fractional Derivatives

- For $0<\Re\alpha<n$ , $n$ an integer, and $x\geq 0$ , the fractional derivative of order $\alpha$ is defined by
- and satisfies the property
- When none of $\alpha$ , $\beta$ , and $\alpha+\beta$ is an integer
- Note that $D^{1/2}D\not=D^{3/2}$ . See also Love ( 1972b ) .

Formulas:

Formula 1.15.51:

$$
D^{\alpha}f(x)=\frac{{\mathrm{d}}^{n}}{{\mathrm{d}x}^{n}}I^{n-\alpha}f(x),
$$

Formula 1.15.52:

$$
D^{k}I^{\alpha}=D^{n}I^{\alpha+n-k},
$$

Formula 1.15.53:

$$
D^{\alpha}D^{\beta}=D^{\alpha+\beta}.
$$


Definitions and local symbols:
- Keywords: fractional derivatives , summability methods for integrals
- Defines: $D^{\alpha}$ : fractional derivative (locally)
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $n$ : nonnegative integer and $I^{\alpha}$ : fractional integral
- Symbols: $k$ : integer , $n$ : nonnegative integer , $I^{\alpha}$ : fractional integral and $D^{\alpha}$ : fractional derivative
- Symbols: $D^{\alpha}$ : fractional derivative

#### 1.15(viii) Tauberian Theorems

- If
- then
- and either $\left|a_{n}\right|\leq K$ or $a_{n}\geq 0$ , then

Formulas:

Formula:

$$
\displaystyle\sum^{\infty}_{n=0}a_{n}
$$

Formula:

$$
\displaystyle a_{n}
$$

Formula 1.15.55:

$$
\sum^{\infty}_{n=0}a_{n}=s.
$$

Formula 1.15.56:

$$
\lim_{x\to 1-}(1-x)\sum^{\infty}_{n=0}a_{n}x^{n}=s,
$$

Formula 1.15.57:

$$
\lim_{n\to\infty}\frac{a_{0}+a_{1}+\dots+a_{n}}{n+1}=s.
$$


Definitions and local symbols:
- Keywords: Tauberian theorems , integrals , summability methods , summability methods for series
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.15](https://dlmf.nist.gov/1.15)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: infinite series, summability methods, Abel, Abel summability, summability methods for series, Cesro, Cesro summability, general, Borel, Borel summability, convergence, regular, Fourier series, summability, Poisson kernel, Fejr kernel, Abel means, Cesro means, integrals, summability methods for integrals, Fourier integral, Fourier integrals, Poisson integral, conjugate, conjugate Poisson integral, fractional integrals, fractional derivatives, Tauberian theorems.

### Source Notes

- See Hardy ( 1949 , p. 10) .
- See Weiss ( 1965 , pp. 131-135) and Andrews et al. ( 1999 , pp. 602-604) . For ( 1.15.24 ), see Krner ( 1989 , Chapters 2,27) .
- See Weiss ( 1965 , pp. 143-147) and Wong ( 1989 , pp. 197-198) .
- See Weiss ( 1965 , pp. 143-148) .
- See Miller and Ross ( 1993 ) and Andrews et al. ( 1999 , pp. 111-114, 604-607) .
- See Andrews et al. ( 1999 , pp. 606-607) . (The notation for the fractional derivative is slightly different.)
- See Hardy ( 1949 , pp. 154-155) , and Widder ( 1941 , Chapter 5) .
