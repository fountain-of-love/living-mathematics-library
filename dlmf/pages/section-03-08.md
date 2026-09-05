# §3.8 Nonlinear Equations

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.8, `Nonlinear Equations`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Introduction
- Newton's Rule
- Other Methods
- Zeros of Polynomials
- Zeros of Analytic Functions
- Conditioning of Zeros
- Systems of Nonlinear Equations
- Fixed-Point Iterations: Fractals

### Subsections

#### 3.8(i) Introduction

- The equation to be solved is
- where $z$ is a real or complex variable and the function $f$ is nonlinear. Solutions are called roots of the equation, or zeros of $f$ . If $f(z_{0})=0$ and $f^{\prime}(z_{0})\neq 0$ , then $z_{0}$ is a simple zero of $f$ . If $f(z_{0})=f^{\prime}(z_{0})=\cdots=f^{(m-1)}(z_{0})=0$ and $f^{(m)}(z_{0})\neq 0$ , then $z_{0}$ is a zero of $f$ of multiplicity $m$ ; compare  1.10(i) .
- Sometimes the equation takes the form
- and the solutions are called fixed points of $\phi$ .
- Equations ( 3.8.1 ) and ( 3.8.2 ) are usually solved by iterative methods. Let $z_{1},z_{2},\dots$ be a sequence of approximations to a root, or fixed point, $\zeta$ . If
- for all $n$ sufficiently large, where $A$ and $p$ are independent of $n$ , then the sequence is said to have convergence of the $p$ th order . (More precisely, $p$ is the largest of the possible set of indices for ( 3.8.3 ).) If $p=1$ and $A<1$ , then the convergence is said to be linear or geometric . If $p=2$ , then the convergence is quadratic ; if $p=3$ , then the convergence is cubic , and so on.

Formulas:

Formula 3.8.1:

$$
f(z)=0,
$$

Formula 3.8.2:

$$
z=\phi(z),
$$

Formula 3.8.3:

$$
\left|z_{n+1}-\zeta\right|<A{\left|z_{n}-\zeta\right|}^{p}
$$


Definitions and local symbols:
- Keywords: acceleration , convergence , cubic , fixed point , fixed points , geometric , iterative methods , linear , local , nonlinear equations , of the $p$ th order , quadratic
- Symbols: $\zeta$ : fixed point

#### 3.8(ii) Newton's Rule

- This is an iterative method for real twice-continuously differentiable, or complex analytic, functions:
- If $\zeta$ is a simple zero, then the iteration converges locally and quadratically. For multiple zeros the convergence is linear, but if the multiplicity $m$ is known then quadratic convergence can be restored by multiplying the ratio $f(z_{n})/f^{\prime}(z_{n})$ in ( 3.8.4 ) by $m$ .
- For real functions $f(x)$ the sequence of approximations to a real zero $\xi$ will always converge (and converge quadratically) if either:

Formulas:

Formula 3.8.4:

$$
z_{n+1}=z_{n}-\frac{f(z_{n})}{f^{\prime}(z_{n})},
$$

Formula:

$$
\displaystyle x_{n+1}
$$

Formula:

$$
\displaystyle\phi(x)
$$


Definitions and local symbols:
- Keywords: Newton's rule (or method) , convergence , iterative methods
- Symbols: $\cot\NVar{z}$ : cotangent function
- Symbols: $\tan\NVar{z}$ : tangent function

#### 3.8(iii) Other Methods

Formulas:

Formula 3.8.6:

$$
x_{2}=x_{1}-\frac{x_{1}-x_{0}}{f_{1}-f_{0}}f_{1}=\frac{f_{1}x_{0}-f_{0}x_{1}}{f_{1}-f_{0}}.
$$

Formula 3.8.7:

$$
z_{n+1}=z_{n}-\frac{(\phi(z_{n})-z_{n})^{2}}{\phi(\phi(z_{n}))-2\phi(z_{n})+z_{n}},
$$


Definitions and local symbols:
- Keywords: bisection method , iterative methods
- Keywords: interpolation , inverse linear , iterative methods , regula falsi
- Keywords: iterative methods , secant method
- Keywords: Steffensen's method , iterative methods
- Keywords: eigenvalue methods , iterative methods

#### 3.8(iv) Zeros of Polynomials

- The polynomial
- has $n$ zeros in $\mathbb{C}$ , counting each zero according to its multiplicity. Explicit formulas for the zeros are available if $n\leq 4$ ; see  1.11(iii) and 4.43 . No explicit general formulas exist when $n\geq 5$ .
- After a zero $\zeta$ has been computed, the factor $z-\zeta$ is factored out of $p(z)$ as a by-product of Horner's scheme ( 1.11(i) ) for the computation of $p(\zeta)$ . In this way polynomials of successively lower degree can be used to find the remaining zeros. (This process is called deflation .) However, to guard against the accumulation of rounding errors, a final iteration for each zero should also be performed on the original polynomial $p(z)$ .

Formulas:

Formula 3.8.8:

$$
p(z)=a_{n}z^{n}+a_{n-1}z^{n-1}+\dots+a_{0},
$$

Formula:

$$
\displaystyle z_{n+1}
$$

Formula:

$$
\displaystyle\phi(z)
$$

Formula:

$$
\displaystyle q_{j}
$$

Formula:

$$
\displaystyle r_{j}
$$

Formula:

$$
\displaystyle\Delta s
$$

Formula:

$$
\displaystyle\Delta t
$$

Formula:

$$
\displaystyle\ell
$$


Definitions and local symbols:
- Keywords: computation , deflation , explicit formulas , polynomials , zeros of polynomials
- Defines: $p(z)$ : polynomial (locally)
- Keywords: Bairstow's method (for zeros of polynomials) , iterative methods
- Defines: $r_{j}$ : sequence (locally)
- Symbols: $q(x)$ : real-valued function
- Symbols: $r_{j}$ : sequence and $q(x)$ : real-valued function
- Keywords: computation , zeros of polynomials

#### 3.8(v) Zeros of Analytic Functions

- Newton's rule is the most frequently used iterative process for accurate computation of real or complex zeros of analytic functions $f(z)$ . Another iterative method is Halley's rule :
- This is useful when $f(z)$ satisfies a second-order linear differential equation because of the ease of computing $f^{\prime\prime}(z_{n})$ . The rule converges locally and is cubically convergent.
- Initial approximations to the zeros can often be found from asymptotic or other approximations to $f(z)$ , or by application of the phase principle or Rouch's theorem; see  1.10(iv) . These results are also useful in ensuring that no zeros are overlooked when the complex plane is being searched.
- For an example involving the Airy functions, see Fabijonas and Olver ( 1999 ) .
- For fixed-point methods for computing zeros of special functions, see Segura ( 2002 ) , Gil and Segura ( 2003 ) , and Gil et al. ( 2007a , Chapter 7) . For describing the distribution of complex zeros of solutions of linear homogeneous second-order differential equations by methods based on the Liouville-Green (WKB) approximation, see Segura ( 2013 ) .

Formulas:

Formula 3.8.12:

$$
z_{n+1}=z_{n}-\frac{f(z_{n})}{f^{\prime}(z_{n})-(f^{\prime\prime}(z_{n})f(z_{n})/(2f^{\prime}(z_{n})))}.
$$


Definitions and local symbols:
- Keywords: Halley's rule , Rouch's theorem , iterative methods , phase principle

#### 3.8(vi) Conditioning of Zeros

- Suppose $f(z)$ also depends on a parameter $\alpha$ , denoted by $f(z,\alpha)$ . Then the sensitivity of a simple zero $z$ to changes in $\alpha$ is given by
- Thus if $f$ is the polynomial ( 3.8.8 ) and $\alpha$ is the coefficient $a_{j}$ , say, then
- For moderate or large values of $n$ it is not uncommon for the magnitude of the right-hand side of ( 3.8.14 ) to be very large compared with unity, signifying that the computation of zeros of polynomials is often an ill-posed problem.

Formulas:

Formula 3.8.13:

$$
\frac{\mathrm{d}z}{\mathrm{d}\alpha}=-\ifrac{\frac{\partial f}{\partial\alpha}}{\frac{\partial f}{\partial z}}.
$$

Formula 3.8.14:

$$
\frac{\mathrm{d}z}{\mathrm{d}a_{j}}=-\frac{z^{j}}{f^{\prime}(z)}.
$$

Formula 3.8.15:

$$
p(x)=(x-1)(x-2)\cdots(x-20)
$$

Formula 3.8.16:

$$
\frac{\mathrm{d}x}{\mathrm{d}a_{19}}=-\frac{20^{19}}{19!}=(-4.30\dots)\times 10^{7}.
$$


Definitions and local symbols:
- Keywords: conditioning , zeros of analytic functions , zeros of polynomials
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $\alpha$ : parameter
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$
- Keywords: Wilkinson's , Wilkinson's polynomial , computation , iterative methods , nonlinear equations , numerical solutions , polynomials , zeros of analytic functions
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ and $!$ : factorial (as in $n!$ )

#### 3.8(vii) Systems of Nonlinear Equations

- For fixed-point iterations and Newton's method for solving systems of nonlinear equations, see Gautschi ( 1997a , Chapter 4, 9) and Ortega and Rheinboldt ( 1970 ) .

Definitions and local symbols:
- Keywords: fixed-point methods , iterative methods , nonlinear equations , systems

#### 3.8(viii) Fixed-Point Iterations: Fractals

- The convergence of iterative methods
- for solving fixed-point problems ( 3.8.2 ) cannot always be predicted, especially in the complex plane.
- Consider, for example, ( 3.8.9 ). Starting this iteration in the neighborhood of one of the four zeros $\pm 1,\pm\mathrm{i}$ , sequences $\{z_{n}\}$ are generated that converge to these zeros. For an arbitrary starting point $z_{0}\in\mathbb{C}$ , convergence cannot be predicted, and the boundary of the set of points $z_{0}$ that generate a sequence converging to a particular zero has a very complicated structure. It is called a Julia set . In general the Julia set of an analytic function $f(z)$ is a fractal , that is, a set that is self-similar. See Julia ( 1918 ) and Devaney ( 1986 ) .

Formulas:

Formula 3.8.17:

$$
z_{n+1}=\phi(z_{n}),
$$


Definitions and local symbols:
- Keywords: Julia sets , fixed-point methods , fractals , iterative methods

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.8](https://dlmf.nist.gov/3.8)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: computation, iterative methods, multiplicity, nonlinear equations, numerical solutions, of equations, roots, simple, zeros of analytic functions, acceleration, convergence, cubic, fixed point, fixed points, geometric, linear, local, of the p th order, quadratic, Newton's rule (or method), bisection method, interpolation, inverse linear, regula falsi, secant method, Steffensen's method, eigenvalue methods, deflation, explicit formulas, polynomials, zeros of polynomials, Bairstow's method (for zeros of polynomials), Halley's rule, Rouch's theorem, phase principle, conditioning, Wilkinson's, Wilkinson's polynomial, fixed-point methods, systems.

### Source Notes

- See Gautschi ( 1997a , pp. 230-234) .
- See Gautschi ( 1997a , pp. 217-225) , Ostrowski ( 1973 , Chapters 3-11) , and Traub ( 1964 , pp. 268-269) .
- For Bairstow's method see National Physical Laboratory ( 1961 , pp. 57-59) .
- See Hildebrand ( 1974 , p. 582) .
