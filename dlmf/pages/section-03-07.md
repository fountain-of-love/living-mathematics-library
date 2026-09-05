# §3.7 Ordinary Differential Equations

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.7, `Ordinary Differential Equations`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Introduction
- Taylor-Series Method: Initial-Value Problems
- Taylor-Series Method: Boundary-Value Problems
- Sturm-Liouville Eigenvalue Problems
- Runge-Kutta Method

### Subsections

#### 3.7(i) Introduction

- Consideration will be limited to ordinary linear second-order differential equations
- where $f$ , $g$ , and $h$ are analytic functions in a domain $D\subset\mathbb{C}$ . If $h=0$ the differential equation is homogeneous , otherwise it is inhomogeneous . For applications to special functions $f$ , $g$ , and $h$ are often simple rational functions.
- For general information on solutions of equation ( 3.7.1 ) see  1.13 . For classification of singularities of ( 3.7.1 ) and expansions of solutions in the neighborhoods of singularities, see  2.7 . For an introduction to numerical methods for ordinary differential equations, see Ascher and Petzold ( 1998 ) , Hairer et al. ( 1993 ) , and Iserles ( 1996 ) .

Formulas:

Formula 3.7.1:

$$
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(z)\frac{\mathrm{d}w}{\mathrm{d}z}+g(z)w=h(z),
$$


Definitions and local symbols:
- Keywords: differential equations , homogeneous , inhomogeneous
- Defines: $f(z)$ : function (locally) , $g(z)$ : function (locally) and $h(z)$ : function (locally)
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ and $w(z)$ : function

#### 3.7(ii) Taylor-Series Method: Initial-Value Problems

- Assume that we wish to integrate ( 3.7.1 ) along a finite path $\mathscr{P}$ from $z=a$ to $z=b$ in a domain $D$ . The path is partitioned at $P+1$ points labeled successively $z_{0},z_{1},\dots,z_{P}$ , with $z_{0}=a$ , $z_{P}=b$ .
- By repeated differentiation of ( 3.7.1 ) all derivatives of $w(z)$ can be expressed in terms of $w(z)$ and $w^{\prime}(z)$ as follows. Write
- with
- Then for $s=2,3,\dots$ ,
- Write $\tau_{j}=z_{j+1}-z_{j}$ , $j=0,1,\dots,P$ , expand $w(z)$ and $w^{\prime}(z)$ in Taylor series ( 1.10(i) ) centered at $z=z_{j}$ , and apply ( 3.7.2 ). Then
- where $\mathbf{A}(\tau,z)$ is the matrix

Formulas:

Formula 3.7.2:

$$
w^{(s)}(z)=f_{s}(z)w(z)+g_{s}(z)w^{\prime}(z)+h_{s}(z),
$$

Formula:

$$
\displaystyle f_{0}(z)
$$

Formula:

$$
\displaystyle g_{0}(z)
$$

Formula:

$$
\displaystyle h_{0}(z)
$$

Formula:

$$
\displaystyle f_{1}(z)
$$

Formula:

$$
\displaystyle g_{1}(z)
$$

Formula:

$$
\displaystyle h_{1}(z)
$$

Formula:

$$
\displaystyle f_{s}(z)
$$

Formula:

$$
\displaystyle g_{s}(z)
$$

Formula:

$$
\displaystyle h_{s}(z)
$$

Formula 3.7.5:

$$
\begin{bmatrix}w(z_{j+1})\\ w^{\prime}(z_{j+1})\end{bmatrix}=\mathbf{A}(\tau_{j},z_{j})\begin{bmatrix}w(z_{j})\\ w^{\prime}(z_{j})\end{bmatrix}+\mathbf{b}(\tau_{j},z_{j}),
$$

Formula 3.7.6:

$$
\mathbf{A}(\tau,z)=\begin{bmatrix}A_{11}(\tau,z)&A_{12}(\tau,z)\\ A_{21}(\tau,z)&A_{22}(\tau,z)\end{bmatrix},
$$

Formula 3.7.7:

$$
\mathbf{b}(\tau,z)=\begin{bmatrix}b_{1}(\tau,z)\\ b_{2}(\tau,z)\end{bmatrix},
$$

Formula:

$$
\displaystyle A_{11}(\tau,z)
$$

Formula:

$$
\displaystyle A_{12}(\tau,z)
$$

Formula:

$$
\displaystyle A_{21}(\tau,z)
$$

Formula:

$$
\displaystyle A_{22}(\tau,z)
$$

Formula:

$$
\displaystyle b_{1}(\tau,z)
$$

Formula:

$$
\displaystyle b_{2}(\tau,z)
$$


Definitions and local symbols:
- Keywords: Taylor-series methods , differential equations , initial-value problems , numerical solution , stability
- Symbols: $w(z)$ : function , $g_{s}(z)$ : coefficient , $h(z)$ : function and $f_{s}(z)$ : coefficient
- Defines: $g_{s}(z)$ : coefficient (locally) and $f_{s}(z)$ : coefficient (locally)
- Symbols: $h(z)$ : function
- Symbols: $g_{s}(z)$ : coefficient , $f(z)$ : function , $g(z)$ : function , $h(z)$ : function and $f_{s}(z)$ : coefficient
- Symbols: $w(z)$ : function , $\mathbf{A}(\NVar{\tau},\NVar{z})$ : matrix and $\mathbf{b}(\NVar{\tau},\NVar{z})$ : vector
- Defines: $\mathbf{A}(\NVar{\tau},\NVar{z})$ : matrix (locally) and $A_{\NVar{j}\NVar{k}}(\NVar{\tau},\NVar{z})$ : matrix entry (locally)
- Defines: $\mathbf{b}(\NVar{\tau},\NVar{z})$ : vector (locally) and $b_{\NVar{j}}(\NVar{\tau},\NVar{z})$ : vector (locally)
- Symbols: $!$ : factorial (as in $n!$ ) , $g_{s}(z)$ : coefficient , $A_{\NVar{j}\NVar{k}}(\NVar{\tau},\NVar{z})$ : matrix entry and $f_{s}(z)$ : coefficient
- Symbols: $!$ : factorial (as in $n!$ ) , $b_{\NVar{j}}(\NVar{\tau},\NVar{z})$ : vector and $h(z)$ : function

#### 3.7(iii) Taylor-Series Method: Boundary-Value Problems

- Now suppose the path $\mathscr{P}$ is such that the rate of growth of $w(z)$ along $\mathscr{P}$ is intermediate to that of two other solutions. (This can happen only for inhomogeneous equations.) Then to compute $w(z)$ in a stable manner we solve the set of equations ( 3.7.5 ) simultaneously for $j=0,1,\dots,P$ , as follows. Let $\mathbf{A}_{P}$ be the $(2P)\times(2P+2)$ band matrix
- ( $\mathbf{I}$ and $\boldsymbol{{0}}$ being the identity and zero matrices of order $2\times 2$ .) Also let $\mathbf{w}$ denote the $(2P+2)\times 1$ vector
- and $\mathbf{b}$ the $(2P)\times 1$ vector
- Then
- This is a set of $2P$ equations for the $2P+2$ unknowns, $w(z_{j})$ and $w^{\prime}(z_{j})$ , $j=0,1,\dots,P$ . The remaining two equations are supplied by boundary conditions of the form
- where the $\alpha$ 's, $\beta$ 's, and $\gamma$ 's are constants.

Formulas:

Formula 3.7.10:

$$
\mathbf{A}_{P}=\begin{bmatrix}-\mathbf{A}(\tau_{0},z_{0})&\mathbf{I}&\boldsymbol{{0}}&\cdots&\boldsymbol{{0}}&\boldsymbol{{0}}\\ \boldsymbol{{0}}&-\mathbf{A}(\tau_{1},z_{1})&\mathbf{I}&\cdots&\boldsymbol{{0}}&\boldsymbol{{0}}\\ \vdots&\vdots&\ddots&\ddots&\vdots&\vdots\\ \boldsymbol{{0}}&\boldsymbol{{0}}&\cdots&-\mathbf{A}(\tau_{P-2},z_{P-2})&\mathbf{I}&\boldsymbol{{0}}\\ \boldsymbol{{0}}&\boldsymbol{{0}}&\cdots&\boldsymbol{{0}}&-\mathbf{A}(\tau_{P-1},z_{P-1})&\mathbf{I}\end{bmatrix}
$$

Formula 3.7.11:

$$
\mathbf{w}=\left[w(z_{0}),w^{\prime}(z_{0}),w(z_{1}),w^{\prime}(z_{1}),\dots,w(z_{P}),w^{\prime}(z_{P})\right]^{\rm T},
$$

Formula 3.7.12:

$$
\mathbf{b}=\left[b_{1}(\tau_{0},z_{0}),b_{2}(\tau_{0},z_{0}),b_{1}(\tau_{1},z_{1}),b_{2}(\tau_{1},z_{1}),\ldots,b_{1}(\tau_{P-1},z_{P-1}),b_{2}(\tau_{P-1},z_{P-1})\right]^{\rm T}.
$$

Formula 3.7.13:

$$
\mathbf{A}_{P}\mathbf{w}=\mathbf{b}.
$$

Formula:

$$
\displaystyle\alpha_{0}w(z_{0})+\beta_{0}w^{\prime}(z_{0})
$$

Formula:

$$
\displaystyle\alpha_{1}w(z_{P})+\beta_{1}w^{\prime}(z_{P})
$$


Definitions and local symbols:
- Keywords: Taylor-series methods , boundary-value methods or problems , boundary-value problems , differential equations , numerical solution , ordinary differential equations
- Defines: $\mathbf{A}(\NVar{\tau},\NVar{z})$ : matrix (locally)
- Symbols: $\tau_{j}$ : change of variable and $P$ : partitioning point
- Symbols: $w(z)$ : function and $P$ : partitioning point
- Defines: $\mathbf{b}(\NVar{\tau},\NVar{z})$ : vector (locally) and $\mathbf{b}(\NVar{\tau},\NVar{z})$ : vector (locally)
- Symbols: $\tau_{j}$ : change of variable and $P$ : partitioning point
- Symbols: $\mathbf{A}(\NVar{\tau},\NVar{z})$ : matrix , $\mathbf{b}(\NVar{\tau},\NVar{z})$ : vector and $P$ : partitioning point
- Symbols: $w(z)$ : function , $\alpha$ : constant , $\beta$ : constant , $\gamma$ : constant and $P$ : partitioning point

#### 3.7(iv) Sturm-Liouville Eigenvalue Problems

- Let $(a,b)$ be a finite or infinite interval and $q(x)$ be a real-valued continuous (or piecewise continuous) function on the closure of $(a,b)$ . The Sturm-Liouville eigenvalue problem is the construction of a nontrivial solution of the system
- with limits taken in ( 3.7.16 ) when $a$ or $b$ , or both, are infinite. The values $\lambda_{k}$ are the eigenvalues and the corresponding solutions $w_{k}$ of the differential equation are the eigenfunctions . The eigenvalues $\lambda_{k}$ are simple, that is, there is only one corresponding eigenfunction (apart from a normalization factor), and when ordered increasingly the eigenvalues satisfy
- If $q(x)$ is $C^{\infty}$ on the closure of $(a,b)$ , then the discretized form ( 3.7.13 ) of the differential equation can be used. This converts the problem into a tridiagonal matrix problem in which the elements of the matrix are polynomials in $\lambda$ ; compare  3.2(vi) . The larger the absolute values of the eigenvalues $\lambda_{k}$ that are being sought, the smaller the integration steps $\left|\tau_{j}\right|$ need to be.
- For further information, including other methods and examples, see Pryce ( 1993 , 2.5.1) .

Formulas:

Formula 3.7.15:

$$
\frac{{\mathrm{d}}^{2}w_{k}}{{\mathrm{d}x}^{2}}+(\lambda_{k}-q(x))w_{k}=0,
$$

Formula 3.7.16:

$$
w_{k}(a)=w_{k}(b)=0,
$$

Formula 3.7.17:

$$
\lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots,
$$


Definitions and local symbols:
- Keywords: Sturm-Liouville eigenvalue problems , differential equations , eigenfunctions , eigenvalues , numerical solution , ordinary differential equations
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ , $w(z)$ : function , $q(x)$ : real-valued function and $\lambda_{k}$ : eigenvalues
- Symbols: $w(z)$ : function
- Symbols: $\lambda_{k}$ : eigenvalues

#### 3.7(v) Runge-Kutta Method

- The Runge-Kutta method applies to linear or nonlinear differential equations. The method consists of a set of rules each of which is equivalent to a truncated Taylor-series expansion, but the rules avoid the need for analytic differentiations of the differential equation.

Formulas:

Formula 3.7.18:

$$
w_{n+1}=w_{n}+\tfrac{1}{6}(k_{1}+2k_{2}+2k_{3}+k_{4})+O\left(h^{5}\right),
$$

Formula:

$$
\displaystyle k_{1}
$$

Formula:

$$
\displaystyle k_{2}
$$

Formula:

$$
\displaystyle k_{3}
$$

Formula:

$$
\displaystyle k_{4}
$$

Formula:

$$
\displaystyle w_{n+1}
$$

Formula:

$$
\displaystyle w^{\prime}_{n+1}
$$


Definitions and local symbols:
- Keywords: Runge-Kutta method , Runge-Kutta methods , differential equations , numerical solution , ordinary differential equations
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $w(z)$ : function and $h(z)$ : function
- Symbols: $w(z)$ : function , $f(z)$ : function and $h(z)$ : function
- Keywords: Runge-Kutta method , Runge-Kutta methods , differential equations , numerical solution , ordinary differential equations
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $w(z)$ : function and $h(z)$ : function
- Symbols: $w(z)$ : function , $f(z)$ : function and $h(z)$ : function

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.7](https://dlmf.nist.gov/3.7)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: differential equations, homogeneous, inhomogeneous, Taylor-series methods, initial-value problems, numerical solution, stability, boundary-value methods or problems, boundary-value problems, ordinary differential equations, Sturm-Liouville eigenvalue problems, eigenfunctions, eigenvalues, Runge-Kutta method, Runge-Kutta methods.
