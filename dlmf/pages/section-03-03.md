# §3.3 Interpolation

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.3, `Interpolation`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Lagrange Interpolation
- Lagrange Interpolation with Equally-Spaced Nodes
- Divided Differences
- Newton's Interpolation Formula
- Inverse Interpolation
- Other Interpolation Methods

### Subsections

#### 3.3(i) Lagrange Interpolation

- The nodes or abscissas $z_{k}$ are real or complex; function values are $f_{k}=f(z_{k})$ . Given $n+1$ distinct points $z_{k}$ and $n+1$ corresponding function values $f_{k}$ , the Lagrange interpolation polynomial is the unique polynomial $P_{n}(z)$ of degree not exceeding $n$ such that $P_{n}(z_{k})=f_{k}$ , $k=0,1,\dots,n$ . It is given by
- where
- Here the prime signifies that the factor for $j=k$ is to be omitted, $\delta_{k,j}$ is the Kronecker symbol, and $\omega_{n+1}(z)$ is the nodal polynomial
- and the weights $\widetilde{\omega}_{k}$ are
- The final expression in ( 3.3.1 ) is the Barycentric form of the Lagrange interpolation formula. It is a direct consequence of the identity
- and according to Berrut and Trefethen ( 2004 ) it is the most efficient representation of $P_{n}(z)$ .

Formulas:

Formula 3.3.1:

$$
P_{n}(z)=\sum_{k=0}^{n}\ell_{k}(z)f_{k}=\omega_{n+1}(z)\sum_{k=0}^{n}\frac{\widetilde{\omega}_{k}}{z-z_{k}}f_{k}=\ifrac{\sum_{k=0}^{n}\frac{\widetilde{\omega}_{k}f_{k}}{z-z_{k}}}{\sum_{k=0}^{n}\frac{\widetilde{\omega}_{k}}{z-z_{k}}},
$$

Formula:

$$
\displaystyle\ell_{k}(z)
$$

Formula:

$$
\displaystyle\ell_{k}(z_{j})
$$

Formula 3.3.3:

$$
\omega_{n+1}(z)=\prod_{k=0}^{n}(z-z_{k}),
$$

Formula 3.3.3_1:

$$
\widetilde{\omega}_{k}=\frac{1}{\omega_{n+1}^{\prime}(z_{k})}={\sideset{}{{}^{\prime}}{\prod}_{j=0}^{n}}\frac{1}{z_{k}-z_{j}}.
$$

Formula 3.3.3_2:

$$
1=\sum_{k=0}^{n}\ell_{k}(z)=\omega_{n+1}(z)\sum_{k=0}^{n}\frac{\widetilde{\omega}_{k}}{z-z_{k}},
$$

Formula 3.3.4:

$$
f(z)=\sum_{k=0}^{n}\ell_{k}(z)f_{k}+R_{n}(z).
$$

Formula 3.3.5:

$$
R_{n}(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\,\omega_{n+1}(x),
$$

Formula 3.3.6:

$$
R_{n}(z)=\frac{\omega_{n+1}(z)}{2\pi\mathrm{i}}\int_{C}\frac{f(\zeta)}{(\zeta-z)\omega_{n+1}(\zeta)}\,\mathrm{d}\zeta,
$$


Definitions and local symbols:
- Keywords: Barycentric form , Barycentric form of Lagrange interpolation , Lagrange interpolation , abscissas , error term , formula , nodal , nodal polynomials , nodes , polynomial , polynomials , remainder terms
- Symbols: $f_{\NVar{t}}$ : function values , $z_{\NVar{k}}$ : nodes of function , $\ell_{k}(z)$ : Lagrange interpolation polynomial and $\omega_{n+1}(z)$ : nodal polynomial
- Defines: $\ell_{k}(z)$ : Lagrange interpolation polynomial (locally)
- Symbols: $\delta_{\NVar{j},\NVar{k}}$ : Kronecker delta and $z_{\NVar{k}}$ : nodes of function
- Defines: $\omega_{n+1}(z)$ : nodal polynomial (locally)
- Symbols: $z_{\NVar{k}}$ : nodes of function
- Symbols: $z_{\NVar{k}}$ : nodes of function and $\omega_{n+1}(z)$ : nodal polynomial
- Symbols: $z_{\NVar{k}}$ : nodes of function , $\ell_{k}(z)$ : Lagrange interpolation polynomial and $\omega_{n+1}(z)$ : nodal polynomial
- Symbols: $f(z)$ : function , $f_{\NVar{t}}$ : function values , $\ell_{k}(z)$ : Lagrange interpolation polynomial and $R_{n}(x)$ : remainder
- Defines: $R_{n}(x)$ : remainder (locally)
- Symbols: $!$ : factorial (as in $n!$ ) , $f(z)$ : function and $\omega_{n+1}(z)$ : nodal polynomial
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $f(z)$ : function , $\omega_{n+1}(z)$ : nodal polynomial , $R_{n}(x)$ : remainder and $C$ : simple closed contour in $D$

#### 3.3(ii) Lagrange Interpolation with Equally-Spaced Nodes

- The $(n+1)$ -point formula ( 3.3.4 ) can be written in the form
- where the nodes $x_{k}=x_{0}+kh$ ( $h>0$ ) and function $f$ are real,
- and $A_{k}^{n}$ are the Lagrangian interpolation coefficients defined by
- The remainder is given by
- where $\xi$ is as in  3.3(i) .
- Let $c_{n}$ be defined by

Formulas:

Formula 3.3.7:

$$
f_{t}=f(x_{0}+th)=\sum_{k=n_{0}}^{n_{1}}A_{k}^{n}f_{k}+R_{n,t},
$$

Formula:

$$
\displaystyle n_{0}
$$

Formula:

$$
\displaystyle n_{1}
$$

Formula 3.3.9:

$$
\sigma=\tfrac{1}{2}(1-(-1)^{n}),
$$

Formula 3.3.10:

$$
A_{k}^{n}=\frac{(-1)^{n_{1}+k}}{(k-n_{0})!\,(n_{1}-k)!(t-k)}\,\prod_{m=n_{0}}^{n_{1}}(t-m).
$$

Formula 3.3.11:

$$
R_{n,t}=R_{n}(x_{0}+th)=\frac{h^{n+1}}{(n+1)!}f^{(n+1)}(\xi)\prod_{k=n_{0}}^{n_{1}}(t-k),
$$

Formula 3.3.12:

$$
c_{n}=\frac{1}{(n+1)!}\max\prod_{k=n_{0}}^{n_{1}}\left|t-k\right|,
$$

Formula 3.3.13:

$$
\left|R_{n,t}\right|\leq c_{n}h^{n+1}\left|f^{(n+1)}(\xi)\right|.
$$

Formula 3.3.14:

$$
\displaystyle f_{t}
$$

Formula 3.3.15:

$$
\displaystyle c_{1}
$$

Formula 3.3.16:

$$
f_{t}=\sum_{k=-1}^{1}A_{k}^{2}f_{k}+R_{2,t},
$$

Formula:

$$
\displaystyle A_{-1}^{2}
$$

Formula:

$$
\displaystyle A_{0}^{2}
$$

Formula:

$$
\displaystyle A_{1}^{2}
$$

Formula 3.3.18:

$$
c_{2}=1/(9\sqrt{3})=0.0641\ldots,
$$

Formula 3.3.19:

$$
f_{t}=\sum_{k=-1}^{2}A_{k}^{3}f_{k}+R_{3,t},
$$

Formula:

$$
\displaystyle A_{-1}^{3}
$$

Formula:

$$
\displaystyle A_{0}^{3}
$$

Formula:

$$
\displaystyle A_{1}^{3}
$$

Formula:

$$
\displaystyle A_{2}^{3}
$$

Formula 3.3.21:

$$
c_{3}=\begin{cases}\tfrac{3}{128}=0.0234\ldots,&0<t<1,\\ \tfrac{1}{24}=0.0416\ldots,&-1<t<0\mbox{ or }1<t<2.\\ \end{cases}
$$

Formula 3.3.22:

$$
f_{t}=\sum_{k=-2}^{2}A_{k}^{4}f_{k}+R_{4,t},
$$

Formula:

$$
\displaystyle A_{-2}^{4}
$$

Formula:

$$
\displaystyle A_{-1}^{4}
$$

Formula:

$$
\displaystyle A_{0}^{4}
$$

Formula:

$$
\displaystyle A_{1}^{4}
$$

Formula:

$$
\displaystyle A_{2}^{4}
$$

Formula 3.3.24:

$$
c_{4}=\begin{cases}0.0118\ldots,&\left|t\right|<1,\\ 0.0302\ldots,&1<\left|t\right|<2.\\ \end{cases}
$$

Formula 3.3.25:

$$
f_{t}=\sum_{k=-2}^{3}A_{k}^{5}f_{k}+R_{5,t},
$$

Formula:

$$
\displaystyle A_{-2}^{5}
$$

Formula:

$$
\displaystyle A_{-1}^{5}
$$

Formula:

$$
\displaystyle A_{0}^{5}
$$

Formula:

$$
\displaystyle A_{1}^{5}
$$

Formula:

$$
\displaystyle A_{2}^{5}
$$

Formula:

$$
\displaystyle A_{3}^{5}
$$

Formula 3.3.27:

$$
c_{5}=\begin{cases}0.00488\ldots,&0<t<1,\\ 0.00701\ldots,&-1<t<0\mbox{ or }1<t<2,\\ 0.0234\ldots,&-2<t<-1\mbox{ or }2<t<3.\end{cases}
$$

Formula 3.3.28:

$$
f_{t}=\sum_{k=-3}^{3}A_{k}^{6}f_{k}+R_{6,t},
$$

Formula:

$$
\displaystyle A_{-3}^{6}
$$

Formula:

$$
\displaystyle A_{-2}^{6}
$$

Formula:

$$
\displaystyle A_{-1}^{6}
$$

Formula:

$$
\displaystyle A_{0}^{6}
$$

Formula:

$$
\displaystyle A_{1}^{6}
$$

Formula:

$$
\displaystyle A_{2}^{6}
$$

Formula:

$$
\displaystyle A_{3}^{6}
$$

Formula 3.3.30:

$$
c_{6}=\begin{cases}0.00245\ldots,&\left|t\right|<1,\\ 0.00459\ldots,&1<\left|t\right|<2,\\ 0.0190\ldots,&2<\left|t\right|<3.\\ \end{cases}
$$

Formula 3.3.31:

$$
f_{t}=\sum_{k=-3}^{4}A_{k}^{7}f_{k}+R_{7,t},
$$

Formula:

$$
\displaystyle A_{-3}^{7}
$$

Formula:

$$
\displaystyle A_{-2}^{7}
$$

Formula:

$$
\displaystyle A_{-1}^{7}
$$

Formula:

$$
\displaystyle A_{0}^{7}
$$

Formula:

$$
\displaystyle A_{1}^{7}
$$

Formula:

$$
\displaystyle A_{2}^{7}
$$

Formula:

$$
\displaystyle A_{3}^{7}
$$

Formula:

$$
\displaystyle A_{4}^{7}
$$

Formula 3.3.33:

$$
c_{7}=\begin{cases}0.00106\ldots,&0<t<1,\\ 0.00139\ldots,&-1<t<0\mbox{ or }1<t<2,\\ 0.00321\ldots,&-2<t<-1\mbox{ or }2<t<3,\\ 0.0158\ldots,&-3<t<-2\mbox{ or }3<t<4.\\ \end{cases}
$$


Definitions and local symbols:
- Keywords: Lagrange interpolation , coefficients , equally-spaced nodes
- Symbols: $f(z)$ : function , $A_{k}^{n}$ : Lagrangian interpolation coefficients , $R_{n,t}(x)$ : remainder and $f_{\NVar{t}}$ : function values
- Defines: $A_{k}^{n}$ : Lagrangian interpolation coefficients (locally)
- Symbols: $!$ : factorial (as in $n!$ )
- Defines: $R_{n,t}(x)$ : remainder (locally)
- Symbols: $!$ : factorial (as in $n!$ ) and $f(z)$ : function
- Defines: $c_{n}$ : bound coefficient (locally)
- Symbols: $!$ : factorial (as in $n!$ )
- Symbols: $f(z)$ : function , $R_{n,t}(x)$ : remainder and $c_{n}$ : bound coefficient
- Keywords: interpolation , linear
- Symbols: $R_{n,t}(x)$ : remainder and $f_{\NVar{t}}$ : function values
- Symbols: $c_{n}$ : bound coefficient
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients , $R_{n,t}(x)$ : remainder and $f_{\NVar{t}}$ : function values
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients
- Symbols: $c_{n}$ : bound coefficient
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients , $R_{n,t}(x)$ : remainder and $f_{\NVar{t}}$ : function values
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients
- Symbols: $c_{n}$ : bound coefficient
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients , $R_{n,t}(x)$ : remainder and $f_{\NVar{t}}$ : function values
- Symbols: $A_{k}^{n}$ : Lagrangian interpolation coefficients

#### 3.3(iii) Divided Differences

- The divided differences of $f$ relative to a sequence of distinct points $z_{0},z_{1},z_{2},\dots$ are defined by
- and so on. Explicitly, the divided difference of order $n$ is given by
- If $f$ and the $z_{k}$ ( $=x_{k}$ ) are real, and $f$ is $n$ times continuously differentiable on a closed interval containing the $x_{k}$ , then
- and again $\xi$ is as in  3.3(i) . If $f$ is analytic in a simply-connected domain $D$ , then for $z\in{D}$ ,
- where $\omega_{n+1}(\zeta)$ is given by ( 3.3.3 ), and $C$ is a simple closed contour in ${D}$ described in the positive rotational sense and enclosing $z_{0},z_{1},\dots,z_{n}$ .

Formulas:

Formula:

$$
\displaystyle\left[z_{0}\right]f
$$

Formula:

$$
\displaystyle\left[z_{0},z_{1}\right]f
$$

Formula:

$$
\displaystyle\left[z_{0},z_{1},z_{2}\right]f
$$

Formula 3.3.35:

$$
\left[z_{0},z_{1},\dots,z_{n}\right]f=\sum_{k=0}^{n}\left(\ifrac{f(z_{k})}{\prod_{\begin{subarray}{c}0\leq j\leq n\\ j\neq k\end{subarray}}(z_{k}-z_{j})}\right).
$$

Formula 3.3.36:

$$
\left[x_{0},x_{1},\dots,x_{n}\right]f=\frac{f^{(n)}(\xi)}{n!}
$$

Formula 3.3.37:

$$
\left[z_{0},z_{1},\dots,z_{n}\right]f=\frac{1}{2\pi\mathrm{i}}\int_{C}\frac{f(\zeta)}{\omega_{n+1}(\zeta)}\,\mathrm{d}\zeta,
$$


Definitions and local symbols:
- Keywords: Lagrange interpolation , definition , divided differences , integral representation , via divided differences
- Defines: $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference
- Symbols: $f(z)$ : function , $f_{\NVar{t}}$ : function values and $z_{\NVar{k}}$ : nodes of function
- Symbols: $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference , $f(z)$ : function and $z_{\NVar{k}}$ : nodes of function
- Symbols: $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference , $!$ : factorial (as in $n!$ ) and $f(z)$ : function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $f(z)$ : function , $C$ : simple closed contour in $D$ , $z_{\NVar{k}}$ : nodes of function and $\omega_{n+1}(z)$ : nodal polynomial

#### 3.3(iv) Newton's Interpolation Formula

- This represents the Lagrange interpolation polynomial in terms of divided differences:
- The interpolation error $R_{n}(z)$ is as in  3.3(i) . Newton's formula has the advantage of allowing easy updating: incorporation of a new point $z_{n+1}$ requires only addition of the term with $\left[z_{0},z_{1},\dots,z_{n+1}\right]f$ to ( 3.3.38 ), plus the computation of this divided difference. Another advantage is its robustness with respect to confluence of the set of points $z_{0},z_{1},\dots,z_{n}$ . For example, for $k+1$ coincident points the limiting form is given by $\left[z_{0},z_{0},\dots,z_{0}\right]f=f^{(k)}(z_{0})/k!$ .

Formulas:

Formula 3.3.38:

$$
f(z)=\left[z_{0}\right]f+(z-z_{0})\left[z_{0},z_{1}\right]f+(z-z_{0})(z-z_{1})\left[z_{0},z_{1},z_{2}\right]f+\cdots+(z-z_{0})(z-z_{1})\cdots(z-z_{n-1})\left[z_{0},z_{1},\dots,z_{n}\right]f+R_{n}(z).
$$


Definitions and local symbols:
- Keywords: Lagrange interpolation , Newton's interpolation formula
- Symbols: $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference , $f(z)$ : function , $z_{\NVar{k}}$ : nodes of function and $R_{n}(x)$ : remainder

#### 3.3(v) Inverse Interpolation

- In this method we interchange the roles of the points $z_{k}$ and the function values $f_{k}$ . It can be used for solving a nonlinear scalar equation $f(z)=0$ approximately. Another approach is to combine the methods of  3.8 with direct interpolation and  3.4 .

Formulas:

Formula 3.3.39:

$$
x(f)=\left[f_{0}\right]x+(f-f_{0})\left[f_{0},f_{1}\right]x+(f-f_{0})(f-f_{1})\left[f_{0},f_{1},f_{2}\right]x;
$$

Formula 3.3.40:

$$
x=-2.2+1.44011\;1973(f-0.09614\;53780)+0.08865\;85832\*(f-0.09614\;53780)(f-0.02670\;63331),
$$

Formula 3.3.41:

$$
f(x)=0.09614\;53780+0.69439\;04495(x+2.1)-0.03007\;14275(x+2.2)(x+2.3),
$$

Formula 3.3.42:

$$
f^{\prime}(x)=0.55906\;90257-0.06014\;28550x,
$$


Definitions and local symbols:
- Keywords: interpolation , inverse
- Keywords: Airy functions , computation , zeros
- Symbols: $\left[\NVar{z_{0},z_{1},\dots,z_{n}}\right]\NVar{f}$ : divided difference , $f(z)$ : function and $f_{\NVar{t}}$ : function values
- Symbols: $f(z)$ : function
- Symbols: $f(z)$ : function
- Symbols: $f(z)$ : function

#### 3.3(vi) Other Interpolation Methods

- For Hermite interpolation, trigonometric interpolation, spline interpolation, rational interpolation (by using continued fractions), interpolation based on Chebyshev points, and bivariate interpolation, see Bulirsch and Rutishauser ( 1968 ) , Davis ( 1975 , pp. 27-31) , and Mason and Handscomb ( 2003 , Chapter 6) . These references also describe convergence properties of the interpolation formulas.
- For interpolation of a bounded function $f$ on $\mathbb{R}$ the cardinal function of $f$ is defined by
- where
- is called the Sinc function . For theory and applications see Stenger ( 1993 , Chapter 3) .

Formulas:

Formula 3.3.43:

$$
C(f,h)(x)=\sum_{k=-\infty}^{\infty}f(kh)S(k,h)(x),
$$

Formula 3.3.44:

$$
S(k,h)(x)=\frac{\sin\left(\pi(x-kh)/h\right)}{\pi(x-kh)/h},
$$


Definitions and local symbols:
- Keywords: Hermite , Sinc function , based on Chebyshev points , based on Sinc functions , bivariate , cardinal function , convergence properties , interpolation , numerical differentiation , rational , spline , trigonometric
- Defines: $C(f,h)$ : cardinal function of $f$ (locally)
- Symbols: $f(z)$ : function and $S(k,h)(x)$ : Sinc function
- Defines: $S(k,h)(x)$ : Sinc function (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter and $\sin\NVar{z}$ : sine function

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.3](https://dlmf.nist.gov/3.3)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: interpolation, Barycentric form, Barycentric form of Lagrange interpolation, Lagrange interpolation, abscissas, error term, formula, nodal, nodal polynomials, nodes, polynomial, polynomials, remainder terms, coefficients, equally-spaced nodes, linear, definition, divided differences, integral representation, via divided differences, Newton's interpolation formula, inverse, Airy functions, computation, zeros, Hermite, Sinc function, based on Chebyshev points, based on Sinc functions, bivariate, cardinal function, convergence properties, numerical differentiation, rational, spline, trigonometric.

### Source Notes

- See Davis ( 1975 , pp. 56 and 67-68) .
- See National Bureau of Standards ( 1944 , pp. xv-xvii) .
- See Davis ( 1975 , p. 65) and Hildebrand ( 1974 , Chapter 2) .
- See Davis ( 1975 , pp. 39-49) and Hildebrand ( 1974 , pp. 60-66) .
- See Ostrowski ( 1973 , pp. 18-26) and Hildebrand ( 1974 , pp. 68-70) .
