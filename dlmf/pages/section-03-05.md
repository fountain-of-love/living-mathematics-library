# §3.5 Quadrature

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.5, `Quadrature`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Trapezoidal Rules
- Simpson's Rule
- Romberg Integration
- Interpolatory Quadrature Rules
- Gauss Quadrature
- Eigenvalue/Eigenvector Characterization of Gauss Quadrature Formulas
- Oscillatory Integrals
- Complex Gauss Quadrature
- Other Contour Integrals
- Cubature Formulas

### Subsections

#### 3.5(i) Trapezoidal Rules

- The elementary trapezoidal rule is given by
- where $h=b-a$ , $f\in C^{2}[a,b]$ , and $a<\xi<b$ .
- The composite trapezoidal rule is
- where $h=(b-a)/n$ , $x_{k}=a+kh$ , $f_{k}=f(x_{k})$ , $k=0,1,\dots,n$ , and
- If in addition $f$ is periodic, $f\in C^{k}(\mathbb{R})$ , and the integral is taken over a period, then
- In particular, when $k=\infty$ the error term is an exponentially-small function of $1/h$ , and in these circumstances the composite trapezoidal rule is exceptionally efficient. For an example see  3.5(ix) .

Formulas:

Formula 3.5.1:

$$
\int_{a}^{b}f(x)\,\mathrm{d}x=\tfrac{1}{2}h(f(a)+f(b))-\tfrac{1}{12}h^{3}f^{\prime\prime}(\xi),
$$

Formula 3.5.2:

$$
\displaystyle\int_{a}^{b}f(x)\,\mathrm{d}x=h(\tfrac{1}{2}f_{0}+f_{1}+\dots+f_{n-1}+\tfrac{1}{2}f_{n})+E_{n}(f),
$$

Formula 3.5.3:

$$
E_{n}(f)=-\frac{b-a}{12}h^{2}f^{\prime\prime}(\xi),
$$

Formula 3.5.4:

$$
E_{n}(f)=O\left(h^{k}\right),
$$

Formula 3.5.5:

$$
\int_{-\infty}^{\infty}f(t)\,\mathrm{d}t=h\sum_{k=-\infty}^{\infty}f(kh)+E_{h}(f),
$$


Definitions and local symbols:
- Keywords: composite , elementary , improved , quadrature , trapezoidal rule
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral and $E_{n}(f)$ : error term
- Defines: $E_{n}(f)$ : error term (locally)
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $E_{n}(f)$ : error term
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral and $E_{n}(f)$ : error term

#### 3.5(ii) Simpson's Rule

- Let $h=\frac{1}{2}(b-a)$ and $f\in C^{4}[a,b]$ . Then the elementary Simpson's rule is
- where $a<\xi<b$ .
- Now let $h=(b-a)/n$ , $x_{k}=a+kh$ , and $f_{k}=f(x_{k})$ , $k=0,1,\dots,n$ . Then the composite Simpson's rule is
- where $n$ is even and
- Simpson's rule can be regarded as a combination of two trapezoidal rules, one with step size $h$ and one with step size $h/2$ to refine the error term.

Formulas:

Formula 3.5.6:

$$
\int_{a}^{b}f(x)\,\mathrm{d}x=\tfrac{1}{3}h(f(a)+4f(\tfrac{1}{2}(a+b))+f(b))-\tfrac{1}{90}h^{5}f^{(4)}(\xi),
$$

Formula 3.5.7:

$$
\int_{a}^{b}f(x)\,\mathrm{d}x=\tfrac{1}{3}h(f_{0}+4f_{1}+2f_{2}+4f_{3}+2f_{4}+\cdots+4f_{n-1}+f_{n})+E_{n}(f),
$$

Formula 3.5.8:

$$
E_{n}(f)=-\frac{b-a}{180}h^{4}f^{(4)}(\xi),
$$


Definitions and local symbols:
- Keywords: Simpson's rule , composite , elementary , quadrature
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral and $E_{n}(f)$ : error term
- Defines: $E_{n}(f)$ : error term (locally)

#### 3.5(iii) Romberg Integration

- Further refinements are achieved by Romberg integration . If $f\in C^{2m+2}[a,b]$ , then the remainder $E_{n}(f)$ in ( 3.5.2 ) can be expanded in the form
- where $h=(b-a)/n$ . As in Simpson's rule, by combining the rule for $h$ with that for $h/2$ , the first error term $c_{1}h^{2}$ in ( 3.5.9 ) can be eliminated. With the Romberg scheme successive terms $c_{1}h^{2},c_{2}h^{4},\dots$ , in ( 3.5.9 ) are eliminated, according to the formula
- beginning with
- although we may also start with the elementary rule with $G_{0}(h)=\frac{1}{2}h(f(a)+f(b))$ and $h=b-a$ . To generate $G_{k}(h)$ the quantities $G_{0}(h),G_{0}(h/2),\dots,G_{0}(h/2^{k})$ are needed. These can be found by means of the recursion
- which depends on function values computed previously.
- If $f\in C^{2k+2}(a,b)$ , then for $j,k=0,1,\dots$ ,

Formulas:

Formula 3.5.9:

$$
E_{n}(f)=c_{1}h^{2}+c_{2}h^{4}+\dots+c_{m}h^{2m}+O\left(h^{2m+2}\right),
$$

Formula 3.5.10:

$$
G_{k}(\tfrac{1}{2}h)=G_{k-1}(\tfrac{1}{2}h)+\frac{G_{k-1}(\frac{1}{2}h)-G_{k-1}(h)}{4^{k}-1},
$$

Formula 3.5.11:

$$
G_{0}(h)=h(\tfrac{1}{2}f_{0}+f_{1}+\dots+f_{n-1}+\tfrac{1}{2}f_{n}),
$$

Formula 3.5.12:

$$
G_{0}(\tfrac{1}{2}h)=\tfrac{1}{2}G_{0}(h)+\tfrac{1}{2}h\sum_{k=0}^{n-1}f\left(x_{0}+(k+\tfrac{1}{2})h\right),
$$

Formula 3.5.13:

$$
\int_{a}^{b}f(x)\,\mathrm{d}x-G_{k}\left(\frac{b-a}{2^{j}}\right)=-\frac{(b-a)^{2k+3}}{2^{k(k+1)}}\frac{4^{-j(k+1)}}{(2k+2)!}\left|B_{2k+2}\right|f^{(2k+2)}(\xi),
$$

Formula 3.5.14:

$$
\int_{0}^{\infty}e^{-pt}J_{0}\left(t\right)\,\mathrm{d}t=\frac{1}{\sqrt{p^{2}+1}}
$$


Definitions and local symbols:
- Keywords: Romberg integration , quadrature
- Defines: $c_{m}$ : coefficients (locally)
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $E_{n}(f)$ : error term
- Defines: $G_{k}(h)$ : Romberg scheme (locally)
- Symbols: $G_{k}(h)$ : Romberg scheme
- Symbols: $G_{k}(h)$ : Romberg scheme
- Symbols: $B_{\NVar{n}}$ : Bernoulli numbers , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $!$ : factorial (as in $n!$ ) , $\int$ : integral and $G_{k}(h)$ : Romberg scheme
- Symbols: $J_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the first kind , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm and $\int$ : integral

#### 3.5(iv) Interpolatory Quadrature Rules

- An interpolatory quadrature rule
- with weight function $w(x)$ , is one for which $E_{n}(f)=0$ whenever $f$ is a polynomial of degree $\leq n-1$ . The nodes $x_{1},x_{2},\dots,x_{n}$ are prescribed, and the weights $w_{k}$ and error term $E_{n}(f)$ are found by integrating the product of the Lagrange interpolation polynomial of degree $n-1$ and $w(x)$ .
- If the extreme members of the set of nodes $x_{1},x_{2},\dots,x_{n}$ are the endpoints $a$ and $b$ , then the quadrature rule is said to be closed . Or if the set $x_{1},x_{2},\dots,x_{n}$ lies in the open interval $(a,b)$ , then the quadrature rule is said to be open .
- Rules of closed type include the Newton-Cotes formulas such as the trapezoidal rules and Simpson's rule . Examples of open rules are the Gauss formulas ( 3.5(v) ), the midpoint rule , and Fejr's quadrature rule . For the latter $a=-1$ , $b=1$ , and the nodes $x_{k}$ are the extrema of the Chebyshev polynomial $T_{n}\left(x\right)$ ( 3.11(ii) and  18.3 ). If we add $-1$ and $1$ to this set of $x_{k}$ , then the resulting closed formula is the frequently-used Clenshaw-Curtis formula , whose weights are positive and given by
- where $x_{k}=\cos\left(k\pi/n\right),k=0,1,\ldots,n$ , and
- For further information, see Mason and Handscomb ( 2003 , Chapter 8) , Davis and Rabinowitz ( 1984 , pp. 74-92) , and Clenshaw and Curtis ( 1960 ) .

Formulas:

Formula 3.5.15:

$$
\int_{a}^{b}f(x)w(x)\,\mathrm{d}x=\sum_{k=1}^{n}w_{k}f(x_{k})+E_{n}(f),
$$

Formula 3.5.16:

$$
w_{k}=\frac{g_{k}}{n}\left(1-\sum_{j=1}^{\left\lfloor n/2\right\rfloor}\frac{b_{j}}{4j^{2}-1}\cos\left(2jk\pi/n\right)\right),
$$

Formula 3.5.17:

$$
g_{k}=\begin{cases}1,&\text{$k=0,n$},\\ 2,&\text{otherwise},\end{cases}\quad b_{j}=\begin{cases}1,&\text{$j=\frac{1}{2}n$},\\ 2,&\text{otherwise}.\end{cases}
$$


Definitions and local symbols:
- Keywords: Clenshaw-Curtis , Clenshaw-Curtis quadrature formula , Fejr's , Gauss quadrature , Newton-Cotes , Simpson's rule , closed , comparison with Clenshaw-Curtis formula , comparison with Gauss quadrature , composite , definition , elementary , error term , interpolatory rules (or formulas) , midpoint , nodes , open , quadrature , trapezoidal rule , weight function , weight functions
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral , $E_{n}(f)$ : error term , $w$ : weight and $w_{k}$ : weights
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos\NVar{z}$ : cosine function , $\left\lfloor\NVar{x}\right\rfloor$ : floor of $x$ , $w_{k}$ : weights , $g_{k}$ : coefficient and $b_{k}$ : coefficient
- Defines: $g_{k}$ : coefficient (locally) and $b_{k}$ : coefficient (locally)

#### 3.5(v) Gauss Quadrature

- Let $\{p_{n}\}$ denote the set of monic polynomials $p_{n}$ of degree $n$ (coefficient of $x^{n}$ equal to $1$ ) that are orthogonal with respect to a positive weight function $w$ on a finite or infinite interval $(a,b)$ ; compare  18.2(i) . In Gauss quadrature (also known as Gauss-Christoffel quadrature ) we use ( 3.5.15 ) with nodes $x_{k}$ the zeros of $p_{n}$ , and weights $w_{k}$ given by
- The $w_{k}$ are also known as Christoffel coefficients or Christoffel numbers and they are all positive. The remainder is given by
- where
- and $\xi$ is some point in $(a,b)$ . As a consequence, the rule is exact for any polynomial $f(x)$ of degree $\leq 2n-1$ , that is,
- In particular, with $h_{m}=\int_{a}^{b}p_{m}(x)^{2}w(x)\,\mathrm{d}x$ , we have a finite system of orthogonal polynomials $p_{m}(x)$ ( $m=0,1,\ldots,n-1$ ) on $\{x_{1},x_{2},\ldots,x_{n}\}$ with respect to the weights $w_{k}$ :
- In practical applications the weight function $w(x)$ is chosen to simulate the asymptotic behavior of the integrand as the endpoints are approached. For $C^{\infty}$ functions Gauss quadrature can be very efficient. In adaptive algorithms the evaluation of the nodes and weights may cause difficulties, unless exact values are known.

Formulas:

Formula 3.5.18:

$$
w_{k}=\int_{a}^{b}\frac{p_{n}(x)}{(x-x_{k})p^{\mspace{1.0mu}\prime}_{n}(x_{k})}\,w(x)\,\mathrm{d}x.
$$

Formula 3.5.19:

$$
E_{n}(f)=\gamma_{n}f^{(2n)}(\xi)/(2n)!,
$$

Formula 3.5.20:

$$
\gamma_{n}=\int_{a}^{b}p_{n}^{2}(x)w(x)\,\mathrm{d}x,
$$

Formula 3.5.20_1:

$$
\int_{a}^{b}f(x)w(x)\,\mathrm{d}x=\sum_{k=1}^{n}w_{k}f(x_{k}).
$$

Formula 3.5.20_2:

$$
\sum_{k=1}^{n}p_{\ell}(x_{k})p_{m}(x_{k})w_{k}=h_{m}\delta_{\ell,m},
$$

Formula:

$$
\displaystyle[a,b]
$$

Formula:

$$
\displaystyle w(x)
$$

Formula:

$$
\displaystyle\gamma_{n}
$$

Formula:

$$
\displaystyle x_{k}
$$

Formula:

$$
\displaystyle w_{k}
$$

Formula:

$$
\displaystyle[a,b)
$$

Formula:

$$
\displaystyle(a,b)
$$


Definitions and local symbols:
- Keywords: Christoffel coefficients (or numbers) , Gauss quadrature , Gauss-Christoffel quadrature , interpolatory rules (or formulas) , nodes , quadrature , remainder terms , weight functions
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral , $w$ : weight , $w_{k}$ : weights and $p_{n}$ : set of monic polynomials
- Symbols: $!$ : factorial (as in $n!$ ) , $\gamma_{n}$ : coefficients and $E_{n}(f)$ : error term
- Defines: $\gamma_{n}$ : coefficients (locally)
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral , $w$ : weight and $p_{n}$ : set of monic polynomials
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral , $w$ : weight and $w_{k}$ : weights
- Symbols: $\delta_{\NVar{j},\NVar{k}}$ : Kronecker delta , $w_{k}$ : weights and $p_{n}$ : set of monic polynomials
- Keywords: Gauss quadrature , Gauss-Legendre formula , Legendre polynomials , monic , monic polynomial , nodes , polynomials , tables , weight functions
- Symbols: $[\NVar{a},\NVar{b}]$ : closed interval , $!$ : factorial (as in $n!$ ) , $\gamma_{n}$ : coefficients and $w$ : weight
- Symbols: $w_{k}$ : weights
- Symbols: $w_{k}$ : weights
- Keywords: Legendre polynomials , of zeros , tables , zeros
- Symbols: $w_{k}$ : weights
- Keywords: Legendre polynomials , tables of zeros
- Symbols: $w_{k}$ : weights
- Keywords: Legendre polynomials , tables of zeros
- Symbols: $w_{k}$ : weights
- Keywords: Legendre polynomials , tables of zeros
- Keywords: Chebyshev polynomials , Gauss quadrature , Gauss-Chebyshev formula , zeros
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $[\NVar{a},\NVar{b}]$ : closed interval , $\gamma_{n}$ : coefficients and $w$ : weight

#### 3.5(vi) Eigenvalue/Eigenvector Characterization of Gauss Quadrature Formulas

- All the monic orthogonal polynomials $\{p_{n}\}$ used with Gauss quadrature satisfy a three-term recurrence relation ( 18.2(iv) ):
- with $\beta_{n}>0$ , $p_{-1}(x)=0$ , and $p_{0}(x)=1$ . Then $h_{n}=\int_{a}^{b}p_{n}(x)^{2}w(x)\,\mathrm{d}x=h_{0}\beta_{1}\beta_{2}\ldots% \beta_{n}$ . The corresponding orthonormal polynomials $q_{n}(x)=p_{n}(x)/\sqrt{h_{n}}$ satisfy the recurrence relation
- with $q_{-1}(x)=0$ , and $q_{0}(x)=1/\sqrt{h_{0}}$ .
- The monic and orthonormal recursion relations of this section are both closely related to the Lanczos recursion relation in  3.2(vi) .
- The Gauss nodes $x_{k}$ (the zeros of $p_{n}$ ) are the eigenvalues of the (symmetric tridiagonal) Jacobi matrix of order $n\times n$ :
- Let $\mathbf{v}_{k}$ denote the normalized eigenvector of $\mathbf{J}_{n}$ corresponding to the eigenvalue $x_{k}$ . Then the weights are given by

Formulas:

Formula 3.5.30:

$$
xp_{n}(x)=p_{n+1}(x)+\alpha_{n}p_{n}(x)+\beta_{n}p_{n-1}(x),
$$

Formula 3.5.30_5:

$$
xq_{n}(x)=\sqrt{\beta_{n+1}}\,q_{n+1}(x)+\alpha_{n}q_{n}(x)+\sqrt{\beta_{n}}q_{n-1}(x),
$$

Formula 3.5.31:

$$
\mathbf{J}_{n}=\begin{bmatrix}\alpha_{0}&\sqrt{\beta_{1}}&&&0\\ \sqrt{\beta_{1}}&\alpha_{1}&\sqrt{\beta_{2}}&&\\ &\ddots&\ddots&\ddots&\\ &&\sqrt{\beta_{n-2}}&\alpha_{n-2}&\sqrt{\beta_{n-1}}\\ 0&&&\sqrt{\beta_{n-1}}&\alpha_{n-1}\end{bmatrix}.
$$

Formula 3.5.32:

$$
w_{k}=\beta_{0}v_{k,1}^{2},
$$

Formula 3.5.33:

$$
\gamma_{n}=\beta_{0}\beta_{1}\cdots\beta_{n}.
$$

Formula:

$$
\displaystyle\alpha_{n}
$$

Formula:

$$
\displaystyle\beta_{n}
$$

Formula:

$$
\displaystyle\alpha_{0}
$$

Formula:

$$
\displaystyle\beta_{1}
$$

Formula 3.5.33_3:

$$
xq_{n}(x)=-\sqrt{\beta_{n+1}}\,q_{n+1}(x)+\alpha_{n}q_{n}(x)-\sqrt{\beta_{n}}\,q_{n-1}(x),
$$


Definitions and local symbols:
- Keywords: Gauss quadrature , Jacobi , eigenvalue/eigenvector characterization , matrix
- Symbols: $p_{n}$ : set of monic polynomials
- Symbols: $\mathbf{v}_{k}$ : normalized eigenvector and $w_{k}$ : weights
- Symbols: $\gamma_{n}$ : coefficients
- Symbols: $\alpha$ : exponent and $\beta$ : exponent
- Symbols: $\alpha$ : exponent and $\beta$ : exponent
- Symbols: $T_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the first kind , $W_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the fourth kind , $U_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the second kind , $V_{\NVar{n}}\left(\NVar{x}\right)$ : Chebyshev polynomial of the third kind , $\Gamma\left(\NVar{z}\right)$ : gamma function , $H_{\NVar{n}}\left(\NVar{x}\right)$ : Hermite polynomial , $\delta_{\NVar{j},\NVar{k}}$ : Kronecker delta , $L^{(\NVar{\alpha})}_{\NVar{n}}\left(\NVar{x}\right)$ : Laguerre (or generalized Laguerre) polynomial , $P_{\NVar{n}}\left(\NVar{x}\right)$ : Legendre polynomial , $T^{*}_{\NVar{n}}\left(\NVar{x}\right)$ : shifted Chebyshev polynomial of the first kind , $C^{(\NVar{\lambda})}_{\NVar{n}}\left(\NVar{x}\right)$ : ultraspherical (or Gegenbauer) polynomial , $\alpha$ : exponent and $p_{n}$ : set of monic polynomials

#### 3.5(vii) Oscillatory Integrals

- Integrals of the form
- can be computed by Filon's rule . See Davis and Rabinowitz ( 1984 , pp. 146-168) .
- Oscillatory integral transforms are treated in Wong ( 1982 ) by a method based on Gaussian quadrature. A comparison of several methods, including an extension of the Clenshaw-Curtis formula ( 3.5(iv) ), is given in Evans and Webster ( 1999 ) .
- For computing infinite oscillatory integrals, Longman's method may be used. The integral is written as an alternating series of positive and negative subintegrals that are computed individually; see Longman ( 1956 ) . Convergence acceleration schemes, for example Levin's transformation ( 3.9(v) ), can be used when evaluating the series. Further methods are given in Clendenin ( 1966 ) and Lyness ( 1985 ) .
- For a comprehensive survey of quadrature of highly oscillatory integrals, including multidimensional integrals, see Iserles et al. ( 2006 ) .

Formulas:

Formula:

$$
\int_{a}^{b}f(x)\cos\left(\omega x\right)\,\mathrm{d}x,
$$

Formula:

$$
\int_{a}^{b}f(x)\sin\left(\omega x\right)\,\mathrm{d}x,
$$


Definitions and local symbols:
- Keywords: Clenshaw-Curtis formula (extended) , Clenshaw-Curtis quadrature formula , Filon's rule , Longman's method , multidimensional , oscillatory integrals , quadrature
- Symbols: $\cos\NVar{z}$ : cosine function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\int$ : integral and $\sin\NVar{z}$ : sine function

#### 3.5(viii) Complex Gauss Quadrature

- For the Bromwich integral
- a complex Gauss quadrature formula is available. Here $f(\zeta)$ is assumed analytic in the half-plane $\Re\zeta>c_{0}$ and bounded as $\zeta\to\infty$ in $\left|\operatorname{ph}\zeta\right|\leq\frac{1}{2}\pi$ . The quadrature rule for ( 3.5.35 ) is
- where $E_{n}(f)=0$ if $f(\zeta)$ is a polynomial of degree $\leq 2n-1$ in $1/\zeta$ . Complex orthogonal polynomials $p_{n}(1/\zeta)$ of degree $n=0,1,2,\dots$ , in $1/\zeta$ that satisfy the orthogonality condition
- are related to Bessel polynomials ( 10.49(ii) and 18.34 ). The complex Gauss nodes $\zeta_{k}$ have positive real part for all $s>0$ .
- The nodes and weights of the 5-point complex Gauss quadrature formula ( 3.5.36 ) for $s=1$ are shown in Table 3.5.18 . Extensive tables of quadrature nodes and weights can be found in Krylov and Skoblya ( 1985 ) .

Formulas:

Formula 3.5.35:

$$
I(f)=\frac{1}{2\pi\mathrm{i}}\int_{c-\mathrm{i}\infty}^{c+\mathrm{i}\infty}e^{\zeta}\zeta^{-s}f(\zeta)\,\mathrm{d}\zeta,
$$

Formula 3.5.36:

$$
I(f)=\sum_{k=1}^{n}w_{k}f(\zeta_{k})+E_{n}(f),
$$

Formula 3.5.37:

$$
\int_{c-\mathrm{i}\infty}^{c+\mathrm{i}\infty}e^{\zeta}\zeta^{-s}p_{k}(1/\zeta)p_{\ell}(1/\zeta)\,\mathrm{d}\zeta=0,
$$

Formula 3.5.38:

$$
G(p)=\int_{0}^{\infty}e^{-pt}g(t)\,\mathrm{d}t,
$$

Formula 3.5.39:

$$
g(t)=\frac{1}{2\pi\mathrm{i}}\int_{\sigma-\mathrm{i}\infty}^{\sigma+\mathrm{i}\infty}e^{tp}G(p)\,\mathrm{d}p,
$$

Formula:

$$
\displaystyle g(t)
$$

Formula:

$$
\displaystyle G(p)
$$

Formula 3.5.41:

$$
g(t)=\sum_{k=1}^{n}\frac{w_{k}\zeta_{k}}{\sqrt{\zeta_{k}^{2}+t^{2}}},
$$


Definitions and local symbols:
- Keywords: Bessel polynomials , Bromwich integral , Gauss quadrature , complex , complex orthogonal polynomials , contour integrals , for contour integrals , nodes , orthogonal polynomials , quadrature , relations to other functions , tables , weight functions
- Defines: $I(f)$ : Bromwich integral (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Symbols: $I(f)$ : Bromwich integral , $\zeta_{k}$ : Gauss nodes , $E_{n}(f)$ : error term and $w_{k}$ : weights
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Symbols: $\mathrm{i}$ : imaginary unit , $\zeta_{k}$ : Gauss nodes and $w_{k}$ : weights
- Keywords: Bessel functions , Laplace transform , computation by quadrature , numerical inversion
- Defines: $G(p)$ : Laplace transform of $g(t)$ (locally)
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral and $g(t)$ : function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $g(t)$ : function , $G(p)$ : Laplace transform of $g(t)$ and $\sigma$ : parameter
- Symbols: $J_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the first kind , $g(t)$ : function and $G(p)$ : Laplace transform of $g(t)$
- Symbols: $\zeta_{k}$ : Gauss nodes , $g(t)$ : function and $w_{k}$ : weights
- Symbols: $J_{\NVar{\nu}}\left(\NVar{z}\right)$ : Bessel function of the first kind and $g(t)$ : function

#### 3.5(ix) Other Contour Integrals

- A frequent problem with contour integrals is heavy cancellation, which occurs especially when the value of the integral is exponentially small compared with the maximum absolute value of the integrand. To avoid cancellation we try to deform the path to pass through a saddle point in such a way that the maximum contribution of the integrand is derived from the neighborhood of the saddle point. For example, steepest descent paths can be used; see  2.4(iv) .

Formulas:

Formula 3.5.42:

$$
\operatorname{erfc}\lambda=\frac{1}{2\pi\mathrm{i}}\int_{c-\mathrm{i}\infty}^{c+\mathrm{i}\infty}e^{\zeta-2\lambda\sqrt{\zeta}}\frac{\,\mathrm{d}\zeta}{\zeta},
$$

Formula 3.5.43:

$$
\operatorname{erfc}\lambda\sim\frac{e^{-\lambda^{2}}}{\sqrt{\pi}\lambda},
$$

Formula 3.5.44:

$$
\operatorname{erfc}\lambda=\frac{1}{2\pi\mathrm{i}}\int_{c-\mathrm{i}\infty}^{c+\mathrm{i}\infty}e^{\lambda^{2}(t-2\sqrt{t})}\frac{\,\mathrm{d}t}{t},
$$

Formula 3.5.45:

$$
\operatorname{erfc}\lambda=\frac{e^{-\lambda^{2}}}{2\pi}\int_{-\pi}^{\pi}e^{-\lambda^{2}{\tan}^{2}\left(\frac{1}{2}\theta\right)}\,\mathrm{d}\theta.
$$

Formula 3.5.46:

$$
\mathcal{H}\mskip-3.0muf\mskip 3.0mu\left(x\right)=\frac{1}{\pi}\pvint_{-\infty}^{\infty}\frac{f(t)}{t-x}\,\mathrm{d}t,
$$


Definitions and local symbols:
- Keywords: numerical integration , quadrature , steepest-descent paths
- Keywords: Hilbert transform , Laplace transform , Scorer functions , computation , computation by quadrature , contour integrals , error functions , numerical integration , numerical inversion , quadrature , steepest-descent paths
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{erfc}\NVar{z}$ : complementary error function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\lambda$ : parameter
- Symbols: $\sim$ : asymptotic equality , $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{erfc}\NVar{z}$ : complementary error function , $\mathrm{e}$ : base of natural logarithm and $\lambda$ : parameter
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{erfc}\NVar{z}$ : complementary error function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\lambda$ : parameter
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\operatorname{erfc}\NVar{z}$ : complementary error function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $\tan\NVar{z}$ : tangent function and $\lambda$ : parameter
- Symbols: $\operatorname{erfc}\NVar{z}$ : complementary error function and $\lambda$ : parameter
- Keywords: composite , quadrature , trapezoidal rule
- Symbols: $\mathcal{H}\left(\NVar{f}\right)\left(\NVar{x}\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\in$ : element of , $\pvint_{\NVar{a}}^{\NVar{b}}$ : Cauchy principal value and $\mathbb{R}$ : real line

#### 3.5(x) Cubature Formulas

- Table 3.5.21 supplies cubature rules, including weights $w_{j}$ , for the disk $D$ , given by $x^{2}+y^{2}\leq h^{2}$ :
- and the square $S$ , given by $\left|x\right|\leq h$ , $\left|y\right|\leq h$ :
- For these results and further information on cubature formulas see Cools ( 2003 ) .
- For integrals in higher dimensions, Monte Carlo methods are another-often the only-alternative. The standard Monte Carlo method samples points uniformly from the integration region to estimate the integral and its error. In more advanced methods points are sampled from a probability distribution, so that they are concentrated in regions that make the largest contribution to the integral. With $N$ function values, the Monte Carlo method aims at an error of order $1/\sqrt{N}$ , independently of the dimension of the domain of integration. See Davis and Rabinowitz ( 1984 , pp. 384-417) and Schrer ( 2004 ) .

Formulas:

Formula 3.5.47:

$$
\frac{1}{\pi h^{2}}\iint_{D}f(x,y)\,\mathrm{d}x\,\mathrm{d}y=\sum_{j=1}^{n}w_{j}f(x_{j},y_{j})+R,
$$

Formula 3.5.48:

$$
\frac{1}{4h^{2}}\iint_{S}f(x,y)\,\mathrm{d}x\,\mathrm{d}y=\sum_{j=1}^{n}w_{j}f(x_{j},y_{j})+R.
$$


Definitions and local symbols:
- Keywords: Monte Carlo methods , cubature , for disks and squares , for multidimensional integrals , weight functions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $(\NVar{a},\NVar{b})$ : open interval , $D$ : disk , $R$ : remainder and $w_{k}$ : weights
- Symbols: $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $(\NVar{a},\NVar{b})$ : open interval , $R$ : remainder and $w_{k}$ : weights
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $(\NVar{a},\NVar{b})$ : open interval , $R$ : remainder and $w_{k}$ : weights

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.5](https://dlmf.nist.gov/3.5)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: integration, numerical, quadrature, composite, elementary, improved, trapezoidal rule, Simpson's rule, Romberg integration, Clenshaw-Curtis, Clenshaw-Curtis quadrature formula, Fejr's, Gauss quadrature, Newton-Cotes, closed, comparison with Clenshaw-Curtis formula, comparison with Gauss quadrature, definition, error term, interpolatory rules (or formulas), midpoint, nodes, open, weight function, weight functions, Christoffel coefficients (or numbers), Gauss-Christoffel quadrature, remainder terms, Gauss-Legendre formula, Legendre polynomials, monic, monic polynomial, polynomials, tables, of zeros, zeros, tables of zeros, Chebyshev polynomials, Gauss-Chebyshev formula, Gauss-Jacobi formula.

### Source Notes

- See Davis and Rabinowitz ( 1984 , pp. 54 and 137) .
- See Davis and Rabinowitz ( 1984 , pp. 57-58) .
- See Davis and Rabinowitz ( 1984 , pp. 434-436) and Bauer et al. ( 1963 ) .
- For ( 3.5.18 )-( 3.5.19 ) see Waldvogel ( 2006 ) .
- In this subsection all numerical values of the nodes $x_{k}$ and corresponding weights $w_{k}$ that appear in the tables in the text and on the website can be computed, for example, by means of the quadruple-precision analogs of the softwares recur and gauss given in Gautschi ( 1994 ) , or in the case of the tables for the logarithmic weight function with recur replaced by cheb , also provided in Gautschi ( 1994 ) . The three softwares can be used for other values of $n$ , and other values of the parameters $\alpha$ and $\beta$ that appear in some of the weight functions.
- See Davis and Rabinowitz ( 1984 , pp. 118-120) and Golub and Welsch ( 1969 ) .
- See Salzer ( 1955 ) .
- For the cubature formulas shown in Table 3.5.21 see Stroud ( 1971 , pp. 243-249) (for the square) and Stroud ( 1971 , pp. 278-279) (for the disk).
