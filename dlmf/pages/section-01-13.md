# §1.13 Differential Equations

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.13, `Differential Equations`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Existence of Solutions
- Equations with a Parameter
- Inhomogeneous Equations
- Change of Variables
- Products of Solutions
- Singularities
- Closed-Form Solutions
- Eigenvalues and Eigenfunctions: Sturm-Liouville and Liouville forms

### Subsections

#### 1.13(i) Existence of Solutions

- A domain in the complex plane is simply-connected if it has no "holes"; more precisely, if its complement in the extended plane $\mathbb{C}\cup\{\infty\}$ is connected.
- The equation
- where $z\in D$ , a simply-connected domain, and $f(z)$ , $g(z)$ are analytic in $D$ , has an infinite number of analytic solutions in $D$ . A solution becomes unique, for example, when $w$ and $\frac{\mathrm{d}w}{\mathrm{d}z}$ are prescribed at a point in $D$ .

Formulas:

Formula 1.13.1:

$$
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(z)\frac{\mathrm{d}w}{\mathrm{d}z}+g(z)w=0,
$$

Formula 1.13.2:

$$
w(z)=Aw_{1}(z)+Bw_{2}(z),
$$

Formula:

$$
\displaystyle w_{1}(z_{0})
$$

Formula:

$$
\displaystyle w_{1}^{\prime}(z_{0})
$$

Formula:

$$
\displaystyle w_{2}(z_{0})
$$

Formula:

$$
\displaystyle w_{2}^{\prime}(z_{0})
$$

Formula 1.13.4:

$$
\mathscr{W}\left\{w_{1}(z),w_{2}(z)\right\}=\det\begin{bmatrix}w_{1}(z)&w_{2}(z)\\ w_{1}^{\prime}(z)&w_{2}^{\prime}(z)\end{bmatrix}=w_{1}(z)w_{2}^{\prime}(z)-w_{2}(z)w_{1}^{\prime}(z).
$$

Formula 1.13.5:

$$
\mathscr{W}\left\{w_{1}(z),w_{2}(z)\right\}=c{\mathrm{e}}^{-\int f(z)\,\mathrm{d}z},
$$

Formula 1.13.6:

$$
Aw_{1}(z)+Bw_{2}(z)=0,
$$


Definitions and local symbols:
- Keywords: differential equations , domain , existence , simply-connected , simply-connected domain , solutions
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $w(z)$ : solution , $f(z)$ : analytic coefficient and $g(z)$ : analytic coefficient
- Keywords: differential equations , fundamental pair , solutions
- Symbols: $z$ : variable , $w(z)$ : solution , $w_{1}(z)$ : solution , $w_{2}(z)$ : solution , $A$ : constant and $B$ : constant
- Symbols: $z$ : variable , $w_{1}(z)$ : solution and $w_{2}(z)$ : solution
- Defines: $\mathscr{W}$ : Wronskian
- Keywords: Wronskian , differential equations , linearly independent , solutions
- Symbols: $\mathscr{W}$ : Wronskian , $\det$ : determinant , $z$ : variable , $w_{1}(z)$ : solution and $w_{2}(z)$ : solution
- Symbols: $\mathscr{W}$ : Wronskian , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $z$ : variable , $f(z)$ : analytic coefficient , $w_{1}(z)$ : solution and $w_{2}(z)$ : solution
- Symbols: $\in$ : element of , $\forall$ : for every , $z$ : variable , $D$ : simply-connected domain , $w_{1}(z)$ : solution , $w_{2}(z)$ : solution , $A$ : constant and $B$ : constant

#### 1.13(ii) Equations with a Parameter

- Assume that in the equation
- $u$ and $z$ belong to domains $U$ and $D$ respectively, the coefficients $f(u,z)$ and $g(u,z)$ are continuous functions of both variables, and for each fixed $u$ (fixed $z$ ) the two functions are analytic in $z$ (in $u$ ). Suppose also that at (a fixed) $z_{0}\in D$ , $w$ and $\frac{\partial w}{\partial z}$ are analytic functions of $u$ . Then at each $z\in D$ , $w$ , $\frac{\partial w}{\partial z}$ and $\frac{{\partial}^{2}w}{{\partial z}^{2}}$ are analytic functions of $u$ .

Formulas:

Formula 1.13.7:

$$
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(u,z)\frac{\mathrm{d}w}{\mathrm{d}z}+g(u,z)w=0,
$$


Definitions and local symbols:
- Keywords: differential equations , with a parameter
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $f(u,z)$ : analytic function of both variables , $g(u,z)$ : analytic function of both variables and $w(u,z)$ : solution

#### 1.13(iii) Inhomogeneous Equations

- The inhomogeneous (or nonhomogeneous ) equation
- with $f(z)$ , $g(z)$ , and $r(z)$ analytic in $D$ has infinitely many analytic solutions in $D$ . If $w_{0}(z)$ is any one solution, and $w_{1}(z)$ , $w_{2}(z)$ are a fundamental pair of solutions of the corresponding homogeneous equation ( 1.13.1 ), then every solution of ( 1.13.8 ) can be expressed as
- where $A$ and $B$ are constants.

Formulas:

Formula 1.13.8:

$$
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+f(z)\frac{\mathrm{d}w}{\mathrm{d}z}+g(z)w=r(z)
$$

Formula 1.13.9:

$$
w(z)=w_{0}(z)+Aw_{1}(z)+Bw_{2}(z),
$$

Formula 1.13.10:

$$
w_{0}(z)=w_{2}(z)\int\frac{w_{1}(z)r(z)}{\mathscr{W}\left\{w_{1}(z),w_{2}(z)\right\}}\,\mathrm{d}z-w_{1}(z)\int\frac{w_{2}(z)r(z)}{\mathscr{W}\left\{w_{1}(z),w_{2}(z)\right\}}\,\mathrm{d}z.
$$


Definitions and local symbols:
- Keywords: differential equations , homogeneous , inhomogeneous , nonhomogeneous
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $w(z)$ : solution , $r(z)$ : analytic function , $f(z)$ : analytic coefficient and $g(z)$ : analytic coefficient
- Symbols: $z$ : variable , $w(z)$ : solution , $w_{0}(z)$ : solution , $A$ : constant , $B$ : constant , $w_{1}(z)$ : solution and $w_{2}(z)$ : solution
- Keywords: differential equations , inhomogeneous , inhomogeneous differential equations , solution by variation of parameters , variation of parameters
- Symbols: $\mathscr{W}$ : Wronskian , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $z$ : variable , $r(z)$ : analytic function , $w_{0}(z)$ : solution , $w_{1}(z)$ : solution and $w_{2}(z)$ : solution

#### 1.13(iv) Change of Variables

Formulas:

Formula 1.13.11:

$$
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}\xi}^{2}}+F(\xi)\frac{\mathrm{d}W}{\mathrm{d}\xi}+G(\xi)W=0,
$$

Formula:

$$
\displaystyle W(\xi)
$$

Formula:

$$
\displaystyle F(\xi)
$$

Formula:

$$
\displaystyle G(\xi)
$$

Formula 1.13.13:

$$
w(z)=W(z)\exp\left(-\tfrac{1}{2}\int f(z)\,\mathrm{d}z\right)
$$

Formula 1.13.14:

$$
\frac{{\mathrm{d}}^{2}W}{{\mathrm{d}z}^{2}}-H(z)W=0,
$$

Formula 1.13.15:

$$
H(z)=\tfrac{1}{4}f^{2}(z)+\tfrac{1}{2}f^{\prime}(z)-g(z).
$$

Formula 1.13.16:

$$
\eta=\int\exp\left(-\int f(z)\,\mathrm{d}z\right)\,\mathrm{d}z.
$$

Formula 1.13.17:

$$
\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}\eta}^{2}}+g(z)\exp\left(2\int f(z)\,\mathrm{d}z\right)w=0.
$$

Formula 1.13.18:

$$
U(z)=(\zeta^{\prime}(z))^{1/2}W(z).
$$

Formula 1.13.19:

$$
\frac{{\mathrm{d}}^{2}U}{{\mathrm{d}\zeta}^{2}}=\left(\dot{z}^{2}H(z)-\tfrac{1}{2}\left\{z,\zeta\right\}\right)U.
$$

Formula 1.13.20:

$$
\left\{z,\zeta\right\}=-2\dot{z}^{\frac{1}{2}}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}\zeta}^{2}}(\dot{z}^{-\frac{1}{2}})=\frac{\dddot{z}}{\dot{z}}-\frac{3}{2}\left(\frac{\ddot{z}}{\dot{z}}\right)^{2}.
$$

Formula 1.13.21:

$$
\displaystyle\left\{z,\zeta\right\}
$$

Formula 1.13.22:

$$
\displaystyle\left\{z,\zeta\right\}
$$


Definitions and local symbols:
- Keywords: change of variables , differential equations , point at infinity
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\xi$ : change of variable , $W(\xi)$ : solution , $F(\xi)$ : analytic coefficient and $G(\xi)$ : analytic coefficient
- Symbols: $w(z)$ : solution , $f(z)$ : analytic coefficient , $\xi$ : change of variable , $W(\xi)$ : solution , $F(\xi)$ : analytic coefficient , $G(\xi)$ : analytic coefficient and $g(z)$ : analytic coefficient
- Keywords: change of variables , differential equations , elimination of first derivative
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\exp z$ : exponential function , $\int$ : integral , $z$ : variable , $w(z)$ : solution , $f(z)$ : analytic coefficient and $W(\xi)$ : solution
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $W(\xi)$ : solution and $H(z)$
- Defines: $H(z)$ (locally)
- Symbols: $z$ : variable , $f(z)$ : analytic coefficient and $g(z)$ : analytic coefficient
- Keywords: change of variables , differential equations , elimination of first derivative
- Defines: $\eta$ : change of variable (locally)
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\exp z$ : exponential function , $\int$ : integral , $z$ : variable and $f(z)$ : analytic coefficient
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ , $\exp z$ : exponential function , $\int$ : integral , $z$ : variable , $w(z)$ : solution , $f(z)$ : analytic coefficient , $\eta$ : change of variable and $g(z)$ : analytic coefficient
- Keywords: Liouville transformation , Liouville transformation for differential equations , Schwarzian derivative , change of variables , differential equations
- Symbols: $z$ : variable , $W(\xi)$ : solution , $\zeta(z)$ : thrice-differentiable function and $U(z)$ : solution
- Symbols: $\left\{z,\zeta\right\}$ : Schwarzian derivative , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $H(z)$ , $\zeta(z)$ : thrice-differentiable function , $U(z)$ : solution and $\dot{z}$ : derivative of $z$ with respect to $\zeta$
- Defines: $\left\{z,\zeta\right\}$ : Schwarzian derivative
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $\zeta(z)$ : thrice-differentiable function , $\dot{z}$ : derivative of $z$ with respect to $\zeta$ , $\ddot{z}$ : 2nd derivative of $z$ with respect to $\zeta$ and $\dddot{z}$ : 3rd derivative of $z$ with respect to $\zeta$
- Keywords: Cayley's identity for Schwarzian derivatives
- Symbols: $\left\{z,\zeta\right\}$ : Schwarzian derivative , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $\xi$ : change of variable and $\zeta(z)$ : thrice-differentiable function
- Symbols: $\left\{z,\zeta\right\}$ : Schwarzian derivative , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable and $\zeta(z)$ : thrice-differentiable function

#### 1.13(v) Products of Solutions

- The product of any two solutions of ( 1.13.1 ) satisfies
- If $U(z)$ and $V(z)$ are respectively solutions of
- then $W=UV$ is a solution of
- For extensions of these results to linear homogeneous differential equations of arbitrary order see Spigler ( 1984 ) .

Formulas:

Formula 1.13.23:

$$
\frac{{\mathrm{d}}^{3}w}{{\mathrm{d}z}^{3}}+3f\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}+(2f^{2}+f^{\prime}+4g)\frac{\mathrm{d}w}{\mathrm{d}z}+(4fg+2g^{\prime})w=0.
$$

Formula:

$$
\displaystyle\frac{{\mathrm{d}}^{2}U}{{\mathrm{d}z}^{2}}+IU
$$

Formula:

$$
\displaystyle\frac{{\mathrm{d}}^{2}V}{{\mathrm{d}z}^{2}}+JV
$$

Formula 1.13.25:

$$
\frac{\mathrm{d}}{\mathrm{d}z}\left(\frac{W^{\prime\prime\prime}+2(I+J)W^{\prime}+(I^{\prime}+J^{\prime})W}{I-J}\right)=-(I-J)W.
$$


Definitions and local symbols:
- Keywords: differential equations , products , solutions
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $f(z)$ : analytic coefficient , $g(z)$ : analytic coefficient and $w(z)$ : solution
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $U(z)$ : solution , $V(z)$ : solution , $I$ : coefficient and $J$ : coefficient
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $z$ : variable , $I$ : coefficient , $J$ : coefficient and $W(z)$ : solution

#### 1.13(vi) Singularities

- For classification of singularities of ( 1.13.1 ) and expansions of solutions in the neighborhoods of singularities, see  2.7 .

#### 1.13(vii) Closed-Form Solutions

- For an extensive collection of solutions of differential equations of the first, second, and higher orders see Kamke ( 1977 ) .

Definitions and local symbols:
- Keywords: closed-form solutions , differential equations

#### 1.13(viii) Eigenvalues and Eigenfunctions: Sturm-Liouville and Liouville forms

- A standard form for second order ordinary differential equations with $x\in\mathbb{R}$ , and with a real parameter $\lambda$ , and real valued functions $p(x),q(x),$ and $\rho(x)$ , with $p(x)$ and $\rho(x)$ positive, is
- This is the Sturm-Liouville form of a second order differential equation, where  denotes $\frac{\mathrm{d}}{\mathrm{d}x}$ . Assuming that $u(x)$ satisfies un-mixed boundary conditions of the form
- or periodic boundary conditions
- on a finite interval $[a,b]\subset\mathbb{R}$ , this is then a regular Sturm-Liouville system .

Formulas:

Formula 1.13.26:

$$
\left(p(x)u^{\prime}(x)\right)^{\prime}+\left(\lambda\rho(x)-q(x)\right)u(x)=0.
$$

Formula:

$$
\displaystyle\alpha u(a)+\alpha^{\prime}u^{\prime}(a)
$$

Formula:

$$
\displaystyle\beta u(b)+\beta^{\prime}u^{\prime}(b)
$$

Formula:

$$
\displaystyle u(a)
$$

Formula:

$$
\displaystyle u^{\prime}(a)
$$

Formula 1.13.29:

$$
\ddot{w}(t)+\left(\lambda-\widehat{q}(t)\right)w(t)=0,
$$

Formula:

$$
\displaystyle w(t)
$$

Formula:

$$
\displaystyle t
$$

Formula 1.13.31:

$$
\widehat{q}(t)=q/\rho+\left(p\rho\right)^{-1/4}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}t}^{2}}\left(p\rho\right)^{1/4}.
$$


Definitions and local symbols:
- Keywords: Sturm-Liouville form , Sturm-Liouville theory , definition , eigenfunctions , eigenvalue
- Symbols: $p(x)$ : function , $q(x)$ : function , $\rho(x)$ : function , $u(x)$ : solution , $\lambda$ : real parameter and $x$ : real variable
- Symbols: $u(x)$ : solution , $\alpha$ : variable , $\beta$ : variable , $\alpha^{\prime}$ : variable , $\beta^{\prime}$ : variable , $a$ : real variable and $b$ : real variable
- Symbols: $u(x)$ : solution , $a$ : real variable and $b$ : real variable
- Symbols: $[a,b]$ : closed interval , $\in$ : element of , $\widehat{q}(t)$ : function , $w(t)$ : solution , $\lambda$ : real parameter , $t$ : real variable , $c$ : real variable and $\ddot{z}$ : 2nd derivative of $w$ with respect to $t$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $p(x)$ : function , $\rho(x)$ : function , $u(x)$ : solution , $w(t)$ : solution , $x$ : real variable , $t$ : real variable and $a$ : real variable
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $p(x)$ : function , $q(x)$ : function , $\rho(x)$ : function , $\widehat{q}(t)$ : function and $t$ : real variable

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.13](https://dlmf.nist.gov/1.13)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: differential equations, domain, existence, simply-connected, simply-connected domain, solutions, fundamental pair, Wronskian, linearly independent, with a parameter, homogeneous, inhomogeneous, nonhomogeneous, inhomogeneous differential equations, solution by variation of parameters, variation of parameters, change of variables, point at infinity, elimination of first derivative, Liouville transformation, Liouville transformation for differential equations, Schwarzian derivative, Cayley's identity for Schwarzian derivatives, products, closed-form solutions, Sturm-Liouville form, Sturm-Liouville theory, definition, eigenfunctions, eigenvalue.

### Source Notes

- See Olver ( 1997b , pp. 141-142, 145-146) and Ince ( 1926 , 5.2) .
- See Olver ( 1997b , pp. 146-147) .
- For ( 1.13.10 ) see Simmons ( 1972 , pp. 90-92) .
- See Temme ( 1996b , pp. 84, 103) , or Olver ( 1997b , pp. 190-191) .
- See Watson ( 1944 , pp. 145-146) .
