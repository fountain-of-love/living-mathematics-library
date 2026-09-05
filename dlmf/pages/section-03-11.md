# §3.11 Approximation Techniques

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.11, `Approximation Techniques`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Minimax Polynomial Approximations
- Chebyshev-Series Expansions
- Minimax Rational Approximations
- Pad Approximations
- Least Squares Approximations
- Splines

### Subsections

#### 3.11(i) Minimax Polynomial Approximations

- Let $f(x)$ be continuous on a closed interval $[a,b]$ . Then there exists a unique $n$ th degree polynomial $p_{n}(x)$ , called the minimax (or best uniform ) polynomial approximation to $f(x)$ on $[a,b]$ , that minimizes $\max_{a\leq x\leq b}\left|\epsilon_{n}(x)\right|$ , where $\epsilon_{n}(x)=f(x)-p_{n}(x)$ .
- A sufficient condition for $p_{n}(x)$ to be the minimax polynomial is that $\left|\epsilon_{n}(x)\right|$ attains its maximum at $n+2$ distinct points in $[a,b]$ and $\epsilon_{n}(x)$ changes sign at these consecutive maxima.
- If we have a sufficiently close approximation
- to $f(x)$ , then the coefficients $a_{k}$ can be computed iteratively. Assume that $f^{\prime}(x)$ is continuous on $[a,b]$ and let $x_{0}=a$ , $x_{n+1}=b$ , and $x_{1},x_{2},\dots,x_{n}$ be the zeros of $\epsilon_{n}^{\mspace{1.0mu}\prime}(x)$ in $(a,b)$ arranged so that
- Also, let
- (Thus the $m_{j}$ are approximations to $m$ , where $\pm m$ is the maximum value of $\left|\epsilon_{n}(x)\right|$ on $[a,b]$ .)

Formulas:

Formula 3.11.1:

$$
p_{n}(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{0}
$$

Formula 3.11.2:

$$
x_{0}<x_{1}<x_{2}<\cdots<x_{n}<x_{n+1}.
$$

Formula 3.11.3:

$$
m_{j}=(-1)^{j}\epsilon_{n}(x_{j}),
$$

Formula 3.11.4:

$$
\sum_{k=0}^{n}(a_{k}+\delta a_{k})x^{k},
$$

Formula 3.11.5:

$$
\sum_{k=0}^{n}x_{j}^{k}\delta a_{k}=(-1)^{j}(m_{j}-m),
$$


Definitions and local symbols:
- Keywords: approximation techniques , best uniform polynomial approximation , computation of coefficients , minimax polynomial approximations , minimax polynomials
- Symbols: $p_{n}(x)$ : minimax approximation
- Defines: $m_{j}$ : approximation (locally)
- Symbols: $\epsilon_{n}(x)$ : error
- Symbols: $m_{j}$ : approximation

#### 3.11(ii) Chebyshev-Series Expansions

- The Chebyshev polynomials $T_{n}$ are given by
- They satisfy the recurrence relation
- with initial values $T_{0}\left(x\right)=1$ , $T_{1}\left(x\right)=x$ . They enjoy an orthogonal property with respect to integrals:
- as well as an orthogonal property with respect to sums, as follows. When $n>0$ and $0\leq j\leq n$ , $0\leq k\leq n$ ,
- where $x_{\ell}=\cos\left(\pi\ell/n\right)$ and the double prime means that the first and last terms are to be halved.
- For these and further properties of Chebyshev polynomials, see Chapter 18 , Gil et al. ( 2007a , Chapter 3) , and Mason and Handscomb ( 2003 ) .

Formulas:

Formula 3.11.6:

$$
T_{n}\left(x\right)=\cos\left(n\operatorname{arccos}x\right),
$$

Formula 3.11.7:

$$
T_{n+1}\left(x\right)-2xT_{n}\left(x\right)+T_{n-1}\left(x\right)=0,
$$

Formula 3.11.8:

$$
\int_{-1}^{1}\frac{T_{j}\left(x\right)T_{k}\left(x\right)}{\sqrt{1-x^{2}}}\,\mathrm{d}x=\begin{cases}\pi,&j=k=0,\\ \frac{1}{2}\pi,&j=k\neq 0,\\ 0,&j\neq k,\end{cases}
$$

Formula 3.11.9:

$$
\sideset{}{{}^{\prime\prime}}{\sum}_{\ell=0}^{n}T_{j}\left(x_{\ell}\right)T_{k}\left(x_{\ell}\right)=\begin{cases}n,&j=k=0\text{ or }n,\\ \frac{1}{2}n,&j=k\neq 0\text{ or }n,\\ 0,&j\neq k,\end{cases}
$$

Formula 3.11.10:

$$
c_{n}=\frac{2}{\pi}\int_{0}^{\pi}f(\cos\theta)\cos\left(n\theta\right)\,\mathrm{d}\theta,
$$

Formula 3.11.11:

$$
f(x)=\sideset{}{{}^{\prime}}{\sum}_{n=0}^{\infty}c_{n}T_{n}\left(x\right),
$$

Formula 3.11.12:

$$
f(x)=\sideset{}{{}^{\prime}}{\sum}_{n=0}^{\infty}d_{n}T_{n}\left(\frac{2x-a-b}{b-a}\right).
$$

Formula 3.11.13:

$$
\epsilon_{n}(x)=d_{n+1}T_{n+1}\left(\frac{2x-a-b}{b-a}\right),
$$

Formula 3.11.14:

$$
\left|\sum_{k=n+1}^{\infty}{}d_{k}T_{k}\left(\frac{2x-a-b}{b-a}\right)\right|
$$

Formula 3.11.15:

$$
u_{k}=2xu_{k+1}-u_{k+2}+c_{k},
$$


Definitions and local symbols:
- Keywords: Chebyshev polynomials , expansions in series of , orthogonality properties , recurrence relations , with respect to integration , with respect to summation
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind , $\cos\NVar{z}$ : cosine function and $\operatorname{arccos}\NVar{z}$ : arccosine function
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ and $\int$ : integral
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind
- Keywords: Chebyshev-series expansions , Lebesgue constants , approximation techniques , relation to minimax polynomials
- Defines: $c_{n}$ : coefficients (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos\NVar{z}$ : cosine function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ and $\int$ : integral
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind and $c_{n}$ : coefficients
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind and $\epsilon_{n}(x)$ : error
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind
- Keywords: Chebyshev-series expansions , computation of coefficients
- Keywords: Chebyshev series , Chebyshev-series expansions , Clenshaw's algorithm , summation
- Symbols: $c_{n}$ : coefficients
- Keywords: Chebyshev-series expansions , complex variables

#### 3.11(iii) Minimax Rational Approximations

- Let $f$ be continuous on a closed interval $[a,b]$ and $w$ be a continuous nonvanishing function on $[a,b]$ : $w$ is called a weight function . Then the minimax (or best uniform ) rational approximation
- of type $[k,\ell]$ to $f$ on $[a,b]$ minimizes the maximum value of $\left|\epsilon_{k,\ell}(x)\right|$ on $[a,b]$ , where
- The theory of polynomial minimax approximation given in  3.11(i) can be extended to the case when $p_{n}(x)$ is replaced by a rational function $R_{k,\ell}(x)$ . There exists a unique solution of this minimax problem and there are at least $k+\ell+2$ values $x_{j}$ , $a\leq x_{0}<x_{1}<\cdots<x_{k+\ell+1}\leq b$ , such that $m_{j}=m$ , where
- and $\pm m$ is the maximum of $\left|\epsilon_{k,\ell}(x)\right|$ on $[a,b]$ .
- A collection of minimax rational approximations to elementary and special functions can be found in Hart et al. ( 1968 ) .
- A widely implemented and used algorithm for calculating the coefficients $p_{j}$ and $q_{j}$ in ( 3.11.16 ) is Remez's second algorithm . See Remez ( 1957 ) , Werner et al. ( 1967 ) , and Johnson and Blair ( 1973 ) .

Formulas:

Formula 3.11.16:

$$
R_{k,\ell}(x)=\frac{p_{0}+p_{1}x+\dots+p_{k}x^{k}}{1+q_{1}x+\dots+q_{\ell}x^{\ell}}
$$

Formula 3.11.17:

$$
\epsilon_{k,\ell}(x)=\frac{R_{k,\ell}(x)-f(x)}{w(x)}.
$$

Formula 3.11.18:

$$
m_{j}=(-1)^{j}\epsilon_{k,\ell}(x_{j}),
$$

Formula 3.11.19:

$$
R_{3,3}(x)=\frac{p_{0}+p_{1}x+p_{2}x^{2}+p_{3}x^{3}}{1+q_{1}x+q_{2}x^{2}+q_{3}x^{3}},
$$


Definitions and local symbols:
- Keywords: Remez's second algorithm , approximation techniques , best uniform rational approximation , computation of coefficients , minimax rational approximations , minimax rational functions , type , weight function , weight functions
- Defines: $R_{k,\ell}(x)$ : rational approximation (locally) , $p_{k}$ : coefficients (locally) and $q_{\ell}$ : coefficients (locally)
- Defines: $\epsilon_{k,\ell}(x)$ : error (locally)
- Symbols: $w(x)$ : function and $R_{k,\ell}(x)$ : rational approximation
- Symbols: $\epsilon_{k,\ell}(x)$ : error and $m_{j}$ : approximation
- Keywords: Bessel functions , minimax rational approximation
- Symbols: $R_{k,\ell}(x)$ : rational approximation , $p_{k}$ : coefficients and $q_{\ell}$ : coefficients
- Symbols: $R_{k,\ell}(x)$ : rational approximation , $p_{k}$ : coefficients and $q_{\ell}$ : coefficients
- Symbols: $J_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the first kind and $R_{k,\ell}(x)$ : rational approximation

#### 3.11(iv) Pad Approximations

- Let
- be a formal power series. The rational function
- is called a Pad approximant at zero of $f$ if
- It is denoted by ${[p/q]_{f}}\left(z\right)$ . Thus if $b_{0}\neq 0$ , then the Maclaurin expansion of ( 3.11.21 ) agrees with ( 3.11.20 ) up to, and including, the term in $z^{p+q}$ .
- The requirement ( 3.11.22 ) implies
- where $c_{j}=0$ if $j<0$ . With $b_{0}=1$ , the last $q$ equations give $b_{1},\dots,b_{q}$ as the solution of a system of linear equations. The first $p+1$ equations then yield $a_{0},\dots,a_{p}$ .

Formulas:

Formula 3.11.20:

$$
f(z)=c_{0}+c_{1}z+c_{2}z^{2}+\cdots
$$

Formula 3.11.21:

$$
\frac{N_{p,q}(z)}{D_{p,q}(z)}=\frac{a_{0}+a_{1}z+\dots+a_{p}z^{p}}{b_{0}+b_{1}z+\dots+b_{q}z^{q}}
$$

Formula 3.11.22:

$$
N_{p,q}(z)-f(z)D_{p,q}(z)=O\left(z^{p+q+1}\right),
$$

Formula:

$$
\displaystyle a_{0}
$$

Formula:

$$
\displaystyle a_{1}
$$

Formula:

$$
\displaystyle\vdots
$$

Formula:

$$
\displaystyle a_{p}
$$

Formula:

$$
\displaystyle 0
$$

Formula 3.11.24:

$$
\begin{array}[]{cccc}{[0/0]_{f}}&{[0/1]_{f}}&{[0/2]_{f}}&\cdots\\ {[1/0]_{f}}&{[1/1]_{f}}&{[1/2]_{f}}&\cdots\\ {[2/0]_{f}}&{[2/1]_{f}}&{[2/2]_{f}}&\cdots\\ \vdots&\vdots&\vdots&\ddots\\ \end{array}
$$

Formula 3.11.25:

$$
(N-C)^{-1}+(S-C)^{-1}=(W-C)^{-1}+(E-C)^{-1}.
$$

Formula 3.11.26:

$$
F(s)=\mathscr{L}\mskip-3.0muf\mskip 3.0mu\left(s\right)=\int_{0}^{\infty}e^{-st}f(t)\,\mathrm{d}t
$$


Definitions and local symbols:
- Defines: ${[\NVar{p}/\NVar{q}]_{\NVar{f}}}$ : Pad approximant
- Keywords: Pad , Pad approximations , Pad table , Wynn's cross rule , approximation techniques , computation of coefficients , convergence , for Pad approximations
- Defines: $c_{q}$ : coefficients (locally)
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding
- Symbols: $c_{q}$ : coefficients
- Symbols: ${[\NVar{p}/\NVar{q}]_{\NVar{f}}}$ : Pad approximant
- Keywords: Laplace transform , Pad , Pad approximations , approximation techniques , numerical inversion
- Defines: $F(s)$ : Laplace transform of $f(t)$ (locally)
- Symbols: $\mathscr{L}\left(\NVar{f}\right)\left(\NVar{s}\right)$ : Laplace transform , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm and $\int$ : integral
- Keywords: Laplace transform

#### 3.11(v) Least Squares Approximations

- Suppose a function $f(x)$ is approximated by the polynomial
- that minimizes
- Here $x_{j}$ , $j=1,2,\dots,J$ , is a given set of distinct real points and $J\geq n+1$ . From the equations $\ifrac{\partial S}{\partial a_{k}}=0$ , $k=0,1,\dots,n$ , we derive the normal equations
- where
- ( 3.11.29 ) is a system of $n+1$ linear equations for the coefficients $a_{0},a_{1},\dots,a_{n}$ . The matrix is symmetric and positive definite, but the system is ill-conditioned when $n$ is large because the lower rows of the matrix are approximately proportional to one another. If $J=n+1$ , then $p_{n}(x)$ is the Lagrange interpolation polynomial for the set $x_{1},x_{2},\dots,x_{J}$ ( 3.3(i) ).
- More generally, let $f(x)$ be approximated by a linear combination

Formulas:

Formula 3.11.27:

$$
p_{n}(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{0}
$$

Formula 3.11.28:

$$
S=\sum_{j=1}^{J}\left(f(x_{j})-p_{n}(x_{j})\right)^{2}.
$$

Formula 3.11.29:

$$
\begin{bmatrix}X_{0}&X_{1}&\cdots&X_{n}\\ X_{1}&X_{2}&\cdots&X_{n+1}\\ \vdots&\vdots&\ddots&\vdots\\ X_{n}&X_{n+1}&\cdots&X_{2n}\end{bmatrix}\begin{bmatrix}a_{0}\\ a_{1}\\ \vdots\\ a_{n}\end{bmatrix}=\begin{bmatrix}F_{0}\\ F_{1}\\ \vdots\\ F_{n}\end{bmatrix},
$$

Formula:

$$
\displaystyle X_{k}
$$

Formula:

$$
\displaystyle F_{k}
$$

Formula 3.11.31:

$$
\Phi_{n}(x)=a_{n}\phi_{n}(x)+a_{n-1}\phi_{n-1}(x)+\dots+a_{0}\phi_{0}(x)
$$

Formula 3.11.32:

$$
\sum_{j=1}^{J}w(x_{j})\left(f(x_{j})-\Phi_{n}(x_{j})\right)^{2},
$$

Formula 3.11.33:

$$
\begin{bmatrix}X_{00}&X_{01}&\cdots&X_{0n}\\ X_{10}&X_{11}&\cdots&X_{1n}\\ \vdots&\vdots&\ddots&\vdots\\ X_{n0}&X_{n1}&\cdots&X_{nn}\end{bmatrix}\begin{bmatrix}a_{0}\\ a_{1}\\ \vdots\\ a_{n}\end{bmatrix}=\begin{bmatrix}F_{0}\\ F_{1}\\ \vdots\\ F_{n}\end{bmatrix},
$$

Formula 3.11.34:

$$
X_{k\ell}=\sum_{j=1}^{J}w(x_{j})\phi_{k}(x_{j})\phi_{\ell}(x_{j}),
$$

Formula 3.11.35:

$$
F_{k}=\sum_{j=1}^{J}w(x_{j})f(x_{j})\phi_{k}(x_{j}).
$$

Formula 3.11.36:

$$
\sum_{k=0}^{n}c_{k}\phi_{k}(x_{j})=0,
$$

Formula 3.11.37:

$$
\sum_{j=0}^{n-1}\phi_{k}(x_{j})\overline{\phi_{\ell}(x_{j})}=n\delta_{k,\ell},
$$

Formula 3.11.38:

$$
f_{j}=\sum_{k=0}^{n-1}a_{k}\phi_{k}(x_{j}),
$$

Formula 3.11.39:

$$
a_{k}=\frac{1}{n}\sum_{j=0}^{n-1}f_{j}\overline{\phi_{k}(x_{j})},
$$

Formula:

$$
\displaystyle\mathbf{f}
$$

Formula:

$$
\displaystyle\mathbf{a}
$$

Formula:

$$
\displaystyle f_{j}
$$

Formula:

$$
\displaystyle\omega_{n}
$$

Formula 3.11.42:

$$
\omega_{n}^{2(k-(n/2))}=\omega_{n/2}^{k}
$$


Definitions and local symbols:
- Keywords: Gram-Schmidt procedure , approximation techniques , conditioning , for least squares approximation , least squares , least squares approximations , normal equations , orthogonal functions with respect to weighted summation , weight functions
- Defines: $p_{n}(x)$ : approximation (locally)
- Symbols: $p_{n}(x)$ : approximation and $J>n+1$ : number of points
- Symbols: $X_{k}$ : elements and $F_{k}$ : elements
- Defines: $X_{k}$ : elements (locally) and $F_{k}$ : elements (locally)
- Symbols: $J>n+1$ : number of points
- Symbols: $\Phi_{n}(x)$ : approximant and $\phi_{k}(x)$ : functions
- Symbols: $J>n+1$ : number of points , $\Phi_{n}(x)$ : approximant and $w(x)$ : weight function
- Symbols: $X_{k}$ : elements and $F_{k}$ : elements
- Symbols: $J>n+1$ : number of points , $X_{k}$ : elements , $\phi_{k}(x)$ : functions and $w(x)$ : weight function
- Symbols: $J>n+1$ : number of points , $F_{k}$ : elements , $\phi_{k}(x)$ : functions and $w(x)$ : weight function
- Defines: $c_{k}$ : coefficients (locally)
- Symbols: $J>n+1$ : number of points and $\phi_{k}(x)$ : functions
- Keywords: Fourier transform , discrete , discrete Fourier transform
- Symbols: $\delta_{\NVar{j},\NVar{k}}$ : Kronecker delta , $\overline{\NVar{z}}$ : complex conjugate and $\phi_{k}(x)$ : functions
- Symbols: $\phi_{k}(x)$ : functions
- Symbols: $\overline{\NVar{z}}$ : complex conjugate and $\phi_{k}(x)$ : functions
- Keywords: Fourier transform , approximation techniques , fast , fast Fourier transform , least squares , least squares approximations
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm and $\mathrm{i}$ : imaginary unit

#### 3.11(vi) Splines

- Splines are defined piecewise and usually by low-degree polynomials. Given $n+1$ distinct points $x_{k}$ in the real interval $[a,b]$ , with ( $a=$ ) $x_{0}<x_{1}<\cdots<x_{n-1}<x_{n}$ ( $=b$ ), on each subinterval $[x_{k},x_{k+1}]$ , $k=0,1,\ldots,n-1$ , a low-degree polynomial is defined with coefficients determined by, for example, values $f_{k}$ and $f_{k}^{\prime}$ of a function $f$ and its derivative at the nodes $x_{k}$ and $x_{k+1}$ . The set of all the polynomials defines a function, the spline , on $[a,b]$ . By taking more derivatives into account, the smoothness of the spline will increase.
- For splines based on Bernoulli and Euler polynomials, see  24.17(ii) .
- For many applications a spline function is a more adaptable approximating tool than the Lagrange interpolation polynomial involving a comparable number of parameters; see  3.3(i) , where a single polynomial is used for interpolating $f(x)$ on the complete interval $[a,b]$ . Multivariate functions can also be approximated in terms of multivariate polynomial splines. See de Boor ( 2001 ) , Chui ( 1988 ) , and Schumaker ( 1981 ) for further information.
- In computer graphics a special type of spline is used which produces a Bzier curve . A cubic Bzier curve is defined by four points. Two are endpoints: $(x_{0},y_{0})$ and $(x_{3},y_{3})$ ; the other points $(x_{1},y_{1})$ and $(x_{2},y_{2})$ are control points. The slope of the curve at $(x_{0},y_{0})$ is tangent to the line between $(x_{0},y_{0})$ and $(x_{1},y_{1})$ ; similarly the slope at $(x_{3},y_{3})$ is tangent to the line between $x_{2},y_{2}$ and $x_{3},y_{3}$ . The curve is described by $x(t)$ and $y(t)$ , which are cubic polynomials with $t\in[0,1]$ . A complete spline results by composing several Bzier curves. A special applications area of Bzier curves is mathematical typography and the design of type fonts. See Knuth ( 1986 , pp. 116-136) .

Definitions and local symbols:
- Keywords: Bzier curves , approximation techniques , definitions , splines

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.11](https://dlmf.nist.gov/3.11)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: approximation techniques, best uniform polynomial approximation, computation of coefficients, minimax polynomial approximations, minimax polynomials, Chebyshev polynomials, expansions in series of, orthogonality properties, recurrence relations, with respect to integration, with respect to summation, Chebyshev-series expansions, Lebesgue constants, relation to minimax polynomials, Chebyshev series, Clenshaw's algorithm, summation, complex variables, Remez's second algorithm, best uniform rational approximation, minimax rational approximations, minimax rational functions, type, weight function, weight functions, Bessel functions, minimax rational approximation, Pad, Pad approximations, Pad table, Wynn's cross rule, convergence, for Pad approximations, Laplace transform, numerical inversion, Gram-Schmidt procedure, conditioning, for least squares approximation, least squares, least squares approximations.

### Source Notes

- See Powell ( 1967 ) .
- See Meinardus ( 1967 , 3) .
- See Wynn ( 1966 ) .
