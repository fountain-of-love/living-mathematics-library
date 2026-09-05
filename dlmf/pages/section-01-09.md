# §1.9 Calculus of a Complex Variable

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.9, `Calculus of a Complex Variable`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Complex Numbers
- Continuity, Point Sets, and Differentiation
- Integration
- Conformal Mapping
- Infinite Sequences and Series
- Power Series
- Inversion of Limits

### Subsections

#### 1.9(i) Complex Numbers

- such that ${\mathrm{i}}^{2}=-1$ .

Formulas:

Formula 1.9.1:

$$
z=x+\mathrm{i}y,
$$

Formula:

$$
\displaystyle\Re z
$$

Formula:

$$
\displaystyle\Im z
$$

Formula:

$$
\displaystyle x
$$

Formula:

$$
\displaystyle y
$$

Formula 1.9.4:

$$
r=(x^{2}+y^{2})^{1/2},
$$

Formula 1.9.5:

$$
\theta=\omega,\quad\pi-\omega,\quad-\pi+\omega,\mathrm{or}-\omega,
$$

Formula 1.9.6:

$$
\omega=\operatorname{arctan}\left(\left|y/x\right|\right)\in\left[0,\tfrac{1}{2}\pi\right].
$$

Formula:

$$
\displaystyle\left|z\right|
$$

Formula:

$$
\displaystyle\operatorname{ph}z
$$

Formula:

$$
\displaystyle\left|\Re z\right|
$$

Formula:

$$
\displaystyle\left|\Im z\right|
$$

Formula 1.9.9:

$$
z=r{\mathrm{e}}^{\mathrm{i}\theta},
$$

Formula 1.9.10:

$$
{\mathrm{e}}^{\mathrm{i}\theta}=\cos\theta+\mathrm{i}\sin\theta;
$$

Formula 1.9.11:

$$
\displaystyle\overline{z}
$$

Formula 1.9.12:

$$
\displaystyle\left|\overline{z}\right|
$$

Formula 1.9.13:

$$
\displaystyle\operatorname{ph}\overline{z}
$$

Formula 1.9.14:

$$
z_{1}\pm z_{2}=x_{1}\pm x_{2}+\mathrm{i}(y_{1}\pm y_{2}),
$$

Formula 1.9.15:

$$
z_{1}z_{2}=x_{1}x_{2}-y_{1}y_{2}+\mathrm{i}(x_{1}y_{2}+x_{2}y_{1}),
$$

Formula 1.9.16:

$$
\frac{z_{1}}{z_{2}}=\frac{z_{1}\overline{z}_{2}}{{\left|z_{2}\right|}^{2}}=\frac{x_{1}x_{2}+y_{1}y_{2}+\mathrm{i}(x_{2}y_{1}-x_{1}y_{2})}{x_{2}^{2}+y_{2}^{2}},
$$

Formula 1.9.17:

$$
\left|z_{1}z_{2}\right|=\left|z_{1}\right|\;\left|z_{2}\right|,
$$

Formula 1.9.18:

$$
\operatorname{ph}\left(z_{1}z_{2}\right)=\operatorname{ph}z_{1}+\operatorname{ph}z_{2},
$$

Formula 1.9.19:

$$
\left|\frac{z_{1}}{z_{2}}\right|=\frac{\left|z_{1}\right|}{\left|z_{2}\right|},
$$

Formula 1.9.20:

$$
\operatorname{ph}\frac{z_{1}}{z_{2}}=\operatorname{ph}z_{1}-\operatorname{ph}z_{2}.
$$

Formula 1.9.21:

$$
z^{n}=\left(x^{n}-\genfrac{(}{)}{0.0pt}{}{n}{2}x^{n-2}y^{2}+\genfrac{(}{)}{0.0pt}{}{n}{4}x^{n-4}y^{4}-\cdots\right)+\mathrm{i}\left(\genfrac{(}{)}{0.0pt}{}{n}{1}x^{n-1}y-\genfrac{(}{)}{0.0pt}{}{n}{3}x^{n-3}y^{3}+\cdots\right),
$$

Formula 1.9.22:

$$
\cos n\theta+\mathrm{i}\sin n\theta=(\cos\theta+\mathrm{i}\sin\theta)^{n},
$$

Formula 1.9.23:

$$
\left|\left|z_{1}\right|-\left|z_{2}\right|\right|\leq\left|z_{1}+z_{2}\right|\leq\left|z_{1}\right|+\left|z_{2}\right|.
$$


Definitions and local symbols:
- Defines: $\mathrm{i}$ : imaginary unit
- Symbols: $\in$ : element of , $\mathbb{R}$ : real line and $z$ : variable
- Keywords: complex numbers , imaginary part , real part
- Defines: $\Im$ : imaginary part and $\Re$ : real part
- Symbols: $z$ : variable
- Keywords: complex numbers , polar representation
- Symbols: $\cos z$ : cosine function , $\sin z$ : sine function , $r$ : radius and $\theta$ : angle
- Symbols: $r$ : radius
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter and $\theta$ : angle
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $[a,b]$ : closed interval , $\in$ : element of , $\operatorname{arctan} z$ : arctangent function and $\left|x\right|$ : absolute value of $x$
- Keywords: complex numbers , modulus , phase
- Defines: $\operatorname{ph}$ : phase and $\left|x\right|$ : absolute value of $x$ (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\in$ : element of , $\mathbb{Z}$ : set of all integers , $z$ : variable , $n$ : nonnegative integer , $r$ : radius and $\theta$ : angle
- Symbols: $\Im$ : imaginary part , $\Re$ : real part , $z$ : variable and $\left|x\right|$ : absolute value of $x$
- Symbols: $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $z$ : variable , $r$ : radius and $\theta$ : angle
- Symbols: $\cos z$ : cosine function , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\sin z$ : sine function and $\theta$ : angle
- Keywords: complex conjugates , complex numbers
- Defines: $\overline{z}$ : complex conjugate
- Symbols: $\mathrm{i}$ : imaginary unit and $z$ : variable
- Symbols: $\overline{z}$ : complex conjugate , $z$ : variable and $\left|x\right|$ : absolute value of $x$

#### 1.9(ii) Continuity, Point Sets, and Differentiation

Formulas:

Formula 1.9.24:

$$
f^{\prime}(z)=\frac{\mathrm{d}f}{\mathrm{d}z}=\lim_{h\to 0}\frac{f(z+h)-f(z)}{h}.
$$

Formula:

$$
\displaystyle\frac{\partial u}{\partial x}
$$

Formula:

$$
\displaystyle\frac{\partial u}{\partial y}
$$

Formula 1.9.26:

$$
\frac{{\partial}^{2}u}{{\partial x}^{2}}+\frac{{\partial}^{2}u}{{\partial y}^{2}}=\frac{{\partial}^{2}v}{{\partial x}^{2}}+\frac{{\partial}^{2}v}{{\partial y}^{2}}=0,
$$

Formula 1.9.27:

$$
\frac{{\partial}^{2}u}{{\partial r}^{2}}+\frac{1}{r}\frac{\partial u}{\partial r}+\frac{1}{r^{2}}\frac{{\partial}^{2}u}{{\partial\theta}^{2}}=0
$$


Definitions and local symbols:
- Keywords: at a point , continuous function , disk , limits of functions , of a complex variable , of two complex variables , of two variables , open
- Keywords: accumulation , accumulation point , boundary , boundary points , closed , closed point set , closure , connected , connected point set , continuous function , domain , interior , interior points , limit (or limiting) , limit points (or limiting points) , neighborhood , of point sets in complex plane , on a region , open , open point set , point sets in complex plane , points in complex plane , region
- Keywords: differentiable functions
- Symbols: $\mathbb{C}$ : complex plane , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $z$ : variable
- Keywords: Cauchy-Riemann equations , differentiation
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $u(x,y)$ : function and $v(x,y)$ : function
- Keywords: analytic , analytic function , entire , entire functions , functions , holomorphic , holomorphic function , in a domain
- Keywords: functions , harmonic , harmonic functions
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $u(x,y)$ : function and $v(x,y)$ : function
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $r$ : radius , $\theta$ : angle and $u(x,y)$ : function

#### 1.9(iii) Integration

- An arc $C$ is given by $z(t)=x(t)+\mathrm{i}y(t)$ , $a\leq t\leq b$ , where $x$ and $y$ are continuously differentiable. If $x(t)$ and $y(t)$ are continuous and $x^{\prime}(t)$ and $y^{\prime}(t)$ are piecewise continuous, then $z(t)$ defines a contour .
- A contour is simple if it contains no multiple points, that is, for every pair of distinct values $t_{1},t_{2}$ of $t$ , $z(t_{1})\neq z(t_{2})$ . A simple closed contour is a simple contour, except that $z(a)=z(b)$ .
- Next,
- for a contour $C$ and $f(z(t))$ continuous, $a\leq t\leq b$ . If $f(z(t_{0}))=\infty$ , $a\leq t_{0}\leq b$ , then the integral is defined analogously to the infinite integrals in  1.4(v) . Similarly when $a=-\infty$ or $b=+\infty$ .

Formulas:

Formula 1.9.28:

$$
\int_{C}f(z)\,\mathrm{d}z=\int_{a}^{b}f(z(t))(x^{\prime}(t)+\mathrm{i}y^{\prime}(t))\,\mathrm{d}t,
$$

Formula 1.9.29:

$$
\int_{C}f(z)\,\mathrm{d}z=0.
$$

Formula 1.9.30:

$$
f(z_{0})=\frac{1}{2\pi\mathrm{i}}\int_{C}\frac{f(z)}{z-z_{0}}\,\mathrm{d}z,
$$

Formula 1.9.31:

$$
f^{(n)}(z_{0})=\frac{n!}{2\pi\mathrm{i}}\int_{C}\frac{f(z)}{(z-z_{0})^{n+1}}\,\mathrm{d}z,
$$

Formula 1.9.32:

$$
\frac{1}{2\pi\mathrm{i}}\int_{C}\frac{1}{z-z_{0}}\,\mathrm{d}z=\mathcal{N}(C,z_{0}),
$$

Formula 1.9.33:

$$
u(z)=\frac{1}{2\pi}\int^{2\pi}_{0}u(z+r{\mathrm{e}}^{\mathrm{i}\phi})\,\mathrm{d}\phi.
$$

Formula 1.9.34:

$$
u(r{\mathrm{e}}^{\mathrm{i}\theta})=\frac{1}{2\pi}\int^{2\pi}_{0}\frac{(R^{2}-r^{2})h(R{\mathrm{e}}^{\mathrm{i}\phi})\,\mathrm{d}\phi}{R^{2}-2Rr\cos\left(\phi-\theta\right)+r^{2}}
$$


Definitions and local symbols:
- Keywords: arc(s) , contour , infinite , integrals , integration , simple , simple closed , simple closed contour
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $C$ : closed contour
- Keywords: Jordan curve theorem , domain , exterior , interior , point sets in complex plane
- Keywords: Cauchy's theorem
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $C$ : closed contour
- Keywords: Cauchy's integral formula , for derivatives
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $C$ : closed contour
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $!$ : factorial (as in $n!$ ) , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $n$ : nonnegative integer and $C$ : closed contour
- Keywords: Liouville's theorem , Liouville's theorem for entire functions , entire functions
- Keywords: of closed contour , winding number
- Defines: $\mathcal{N}(C,z_{0})$ : winding number of $C$ (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $C$ : closed contour
- Keywords: harmonic functions , mean value property , mean value property for harmonic functions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $r$ : radius and $u(z)$ : harmonic function
- Keywords: Poisson integral , harmonic functions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $r$ : radius , $u(z)$ : harmonic function and $R$ : radius

#### 1.9(iv) Conformal Mapping

- The extended complex plane , $\mathbb{C}\,\cup\,\{\infty\}$ , consists of the points of the complex plane $\mathbb{C}$ together with an ideal point $\infty$ called the point at infinity . A system of open disks around infinity is given by
- Each $S_{r}$ is a neighborhood of $\infty$ . Also,
- A function $f(z)$ is analytic at $\infty$ if $g(z)=f(1/z)$ is analytic at $z=0$ , and we set $f^{\prime}(\infty)=g^{\prime}(0)$ .

Formulas:

Formula 1.9.35:

$$
S_{r}=\{z\mid\left|z\right|>1/r\}\cup\{\infty\},
$$

Formula 1.9.36:

$$
\infty\pm z=z\pm\infty=\infty,
$$

Formula 1.9.37:

$$
\infty\cdot z=z\cdot\infty=\infty,
$$

Formula 1.9.38:

$$
z/\infty=0,
$$

Formula 1.9.39:

$$
z/0=\infty,
$$

Formula 1.9.40:

$$
w=f(z)=\frac{az+b}{cz+d},
$$

Formula:

$$
\displaystyle f(-d/c)
$$

Formula:

$$
\displaystyle f(\infty)
$$

Formula 1.9.42:

$$
f^{\prime}(z)=\frac{ad-bc}{(cz+d)^{2}},
$$

Formula 1.9.43:

$$
f^{\prime}(\infty)=\frac{bc-ad}{c^{2}}.
$$

Formula 1.9.44:

$$
z=\frac{dw-b}{-cw+a}.
$$

Formula 1.9.45:

$$
\frac{(z_{1}-z_{2})(z_{3}-z_{4})}{(z_{1}-z_{4})(z_{3}-z_{2})},
$$


Definitions and local symbols:
- Keywords: analytic function , around infinity , at infinity , conformal mapping , disk , extended complex plane , neighborhood , of infinity , open disks around infinity , points in complex plane
- Symbols: $\cup$ : union , $z$ : variable , $r$ : radius , $S_{r}$ : neighborhood and $\left|x\right|$ : absolute value of $x$
- Symbols: $z$ : variable
- Symbols: $z$ : variable
- Symbols: $z$ : variable
- Symbols: $z$ : variable
- Keywords: angle between , angle between arcs , arc(s) , conformal mapping , linear transformation
- Keywords: Mbius transformation , bilinear transformation , cross ratio , fractional linear transformation , homographic transformation
- Symbols: $z$ : variable and $w$ : variable
- Symbols: $z$ : variable
- Symbols: $z$ : variable and $w$ : variable
- Symbols: $z$ : variable

#### 1.9(v) Infinite Sequences and Series

- A sequence $\{z_{n}\}$ converges to $z$ if $\lim\limits_{n\to\infty}z_{n}=z$ . For $z_{n}=x_{n}+\mathrm{i}y_{n}$ , the sequence $\{z_{n}\}$ converges iff the sequences $\{x_{n}\}$ and $\{y_{n}\}$ separately converge. A series $\sum^{\infty}_{n=0}z_{n}$ converges if the sequence $s_{n}=\sum^{n}_{k=0}z_{k}$ converges. The series is divergent if $s_{n}$ does not converge. The series converges absolutely if $\sum^{\infty}_{n=0}\left|z_{n}\right|$ converges. A series $\sum^{\infty}_{n=0}z_{n}$ converges (diverges) absolutely when $\lim\limits_{n\to\infty}{\left|z_{n}\right|}^{1/n}<1$ ( $>1$ ), or when $\lim\limits_{n\to\infty}\left|\frac{z_{n+1}}{z_{n}}\right|<1$ ( $>1$ ). Absolutely convergent series are also convergent.
- Let $\{f_{n}(z)\}$ be a sequence of functions defined on a set $S$ . This sequence converges pointwise to a function $f(z)$ if
- for each $z\in S$ . The sequence converges uniformly on $S$ , if for every $\epsilon>0$ there exists an integer $N$ , independent of $z$ , such that
- for all $z\in S$ and $n\geq N$ .
- A series $\sum^{\infty}_{n=0}f_{n}(z)$ converges uniformly on $S$ , if the sequence $s_{n}(z)=\sum^{n}_{k=0}f_{k}(z)$ converges uniformly on $S$ .

Formulas:

Formula 1.9.46:

$$
f(z)=\lim_{n\to\infty}f_{n}(z)
$$

Formula 1.9.47:

$$
\left|f_{n}(z)-f(z)\right|<\epsilon
$$


Definitions and local symbols:
- Keywords: absolute , convergence , divergent , infinite sequences , infinite series , pointwise , uniform
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $z$ : variable , $n$ : nonnegative integer , $\epsilon$ : positive number and $\left|x\right|$ : absolute value of $x$
- Keywords: $M$ -test for uniform convergence , Weierstrass $M$ -test , convergence , doubly-infinite , infinite series

#### 1.9(vi) Power Series

- For a series $\sum^{\infty}_{n=0}a_{n}(z-z_{0})^{n}$ there is a number $R$ , $0\leq R\leq\infty$ , such that the series converges for all $z$ in $\left|z-z_{0}\right|<R$ and diverges for $z$ in $\left|z-z_{0}\right|>R$ . The circle $\left|z-z_{0}\right|=R$ is called the circle of convergence of the series, and $R$ is the radius of convergence . Inside the circle the sum of the series is an analytic function $f(z)$ . For $z$ in $\left|z-z_{0}\right|\leq\rho$ ( $<R$ ), the convergence is absolute and uniform. Moreover,
- and
- For the converse of this result see  1.10(i) .

Formulas:

Formula 1.9.48:

$$
a_{n}=\frac{f^{(n)}(z_{0})}{n!},
$$

Formula 1.9.49:

$$
R=\liminf_{n\to\infty}{\left|a_{n}\right|}^{-1/n}.
$$

Formula 1.9.50:

$$
\sum^{\infty}_{n=0}(a_{n}\pm b_{n})z^{n}=\sum^{\infty}_{n=0}a_{n}z^{n}\pm\sum^{\infty}_{n=0}b_{n}z^{n},
$$

Formula 1.9.51:

$$
\left(\sum^{\infty}_{n=0}a_{n}z^{n}\right)\left(\sum^{\infty}_{n=0}b_{n}z^{n}\right)=\sum^{\infty}_{n=0}c_{n}z^{n},
$$

Formula 1.9.52:

$$
c_{n}=\sum^{n}_{k=0}a_{k}b_{n-k}.
$$

Formula 1.9.53:

$$
f(z)=a_{0}+a_{1}z+a_{2}z^{2}+\cdots,
$$

Formula 1.9.54:

$$
\frac{1}{f(z)}=b_{0}+b_{1}z+b_{2}z^{2}+\cdots,
$$

Formula:

$$
\displaystyle b_{0}
$$

Formula:

$$
\displaystyle b_{1}
$$

Formula:

$$
\displaystyle b_{2}
$$

Formula 1.9.56:

$$
b_{n}=-(a_{1}b_{n-1}+a_{2}b_{n-2}+\dots+a_{n}b_{0})/a_{0},
$$

Formula 1.9.57:

$$
\ln f(z)=q_{1}z+q_{2}z^{2}+q_{3}z^{3}+\cdots,
$$

Formula:

$$
\displaystyle q_{1}
$$

Formula:

$$
\displaystyle q_{2}
$$

Formula:

$$
\displaystyle q_{3}
$$

Formula 1.9.59:

$$
q_{n}=(na_{n}-(n-1)a_{1}q_{n-1}-(n-2)a_{2}q_{n-2}-\cdots-a_{n-1}q_{1})/n,
$$

Formula 1.9.60:

$$
(f(z))^{\nu}=p_{0}+p_{1}z+p_{2}z^{2}+\cdots,
$$

Formula:

$$
\displaystyle p_{0}
$$

Formula:

$$
\displaystyle p_{1}
$$

Formula:

$$
\displaystyle p_{2}
$$

Formula 1.9.62:

$$
p_{n}=((\nu-n+1)a_{1}p_{n-1}+(2\nu-n+2)a_{2}p_{n-2}+\dots+((n-1)\nu-1)a_{n-1}p_{1}+n\nu a_{n})/n,
$$

Formula 1.9.63:

$$
f^{(m)}(z)=\sum_{n=0}^{\infty}{\left(n+1\right)_{m}}a_{n+m}(z-z_{0})^{n},
$$


Definitions and local symbols:
- Keywords: circle of , convergence , power series , radius of
- Symbols: $!$ : factorial (as in $n!$ ) , $z$ : variable and $n$ : nonnegative integer
- Defines: $R$ : radius of convergence (locally)
- Symbols: $\liminf$ : least limit point , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Keywords: addition , differentiation , multiplication , of logarithms , of powers , of reciprocals , power series , subtraction
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $k$ : integer and $n$ : nonnegative integer
- Symbols: $z$ : variable
- Symbols: $z$ : variable
- Symbols: $n$ : nonnegative integer
- Symbols: $\ln z$ : principal branch of logarithm function , $z$ : variable and $q_{j}$ : coefficients
- Symbols: $q_{j}$ : coefficients
- Symbols: $n$ : nonnegative integer and $q_{j}$ : coefficients
- Symbols: $z$ : variable , $\nu$ : complex and $p_{j}$ : coefficients
- Symbols: $\nu$ : complex and $p_{j}$ : coefficients
- Symbols: $n$ : nonnegative integer , $\nu$ : complex and $p_{j}$ : coefficients
- Symbols: ${\left(a\right)_{n}}$ : Pochhammer's symbol (or shifted factorial) , $z$ : variable , $m$ : nonnegative integer , $n$ : nonnegative integer , $R$ : radius of convergence and $\left|x\right|$ : absolute value of $x$

#### 1.9(vii) Inversion of Limits

Formulas:

Formula 1.9.64:

$$
\left|z_{m,n}-z\right|<\epsilon
$$

Formula:

$$
\lim_{m\to\infty}\left(\lim_{n\to\infty}z_{m,n}\right),
$$

Formula:

$$
\lim_{n\to\infty}\left(\lim_{m\to\infty}z_{m,n}\right)
$$

Formula 1.9.66:

$$
z_{p,q}=\sum^{p}_{m=0}\sum^{q}_{n=0}\zeta_{m,n}.
$$

Formula:

$$
\sum^{\infty}_{m=0}\left(\sum^{\infty}_{n=0}\zeta_{m,n}\right),
$$

Formula:

$$
\sum^{\infty}_{n=0}\left(\sum^{\infty}_{m=0}\zeta_{m,n}\right).
$$

Formula 1.9.68:

$$
\int_{C}\sum^{\infty}_{n=0}f_{n}(z)\,\mathrm{d}z=\sum^{\infty}_{n=0}\int_{C}f_{n}(z)\,\mathrm{d}z
$$

Formula 1.9.69:

$$
\int^{b}_{a}\sum^{\infty}_{n=0}\left|f_{n}(t)\right|\,\mathrm{d}t<\infty,
$$

Formula 1.9.70:

$$
\sum^{\infty}_{n=0}\int^{b}_{a}\left|f_{n}(t)\right|\,\mathrm{d}t<\infty.
$$

Formula 1.9.71:

$$
\int^{b}_{a}\sum^{\infty}_{n=0}f_{n}(t)\,\mathrm{d}t=\sum^{\infty}_{n=0}\int^{b}_{a}f_{n}(t)\,\mathrm{d}t.
$$


Definitions and local symbols:
- Keywords: convergence , double , infinite sequences , infinite series
- Keywords: convergence , double , double sequence , double series , infinite sequences , relation to infinite double series
- Symbols: $z$ : variable , $m$ : nonnegative integer , $n$ : nonnegative integer , $\epsilon$ : positive number and $\left|x\right|$ : absolute value of $x$
- Symbols: $z$ : variable , $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $z$ : variable , $m$ : nonnegative integer , $n$ : nonnegative integer and $\zeta_{p,q}$ : sum
- Symbols: $m$ : nonnegative integer , $n$ : nonnegative integer and $\zeta_{p,q}$ : sum
- Keywords: compact , compact set , infinite series , integration , point sets in complex plane , term by term , term-by-term integration
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $z$ : variable , $n$ : nonnegative integer and $C$ : finite contour in $D$
- Keywords: calculus , complex variable , dominated convergence theorem , infinite series
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.9](https://dlmf.nist.gov/1.9)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: calculus, complex variable, complex numbers, imaginary part, real part, polar representation, modulus, phase, complex conjugates, arithmetic operations, powers, DeMoivre's theorem, triangle inequality, at a point, continuous function, disk, limits of functions, of a complex variable, of two complex variables, of two variables, open, accumulation, accumulation point, boundary, boundary points, closed, closed point set, closure, connected, connected point set, domain, interior, interior points, limit (or limiting), limit points (or limiting points), neighborhood, of point sets in complex plane, on a region, open point set, point sets in complex plane.

### Source Notes

- See Copson ( 1935 , Chapter 1) , Levinson and Redheffer ( 1970 , Chapter 1) , or Markushevich ( 1983 , pp. 14-18) .
- See Levinson and Redheffer ( 1970 , Chapters 1,2 and pp. 133-138) and Copson ( 1935 , Chapters 2,3) .
- See Levinson and Redheffer ( 1970 , Chapter 3 and p. 360) , Copson ( 1935 , pp. 56-69) , and Ahlfors ( 1966 , pp. 168-169) . For a proof of the Jordan curve theorem see, for example, Dienes ( 1931 , pp. 177-197) . The theorem is valid with less restrictive conditions than those assumed here.
- See Markushevich ( 1983 , pp. 41-46) , Markushevich ( 1985 , vol. 1, 34) , and Levinson and Redheffer ( 1970 , pp. 259-277) .
- See Copson ( 1935 , pp. 19-24, 92-98) .
- See Copson ( 1935 , pp. 37-40) , Levinson and Redheffer ( 1970 , pp. 349-351) , or Markushevich ( 1983 , pp. 131-135) . For the operations on series, see Henrici ( 1974 , Chapter 1) or Olver ( 1997b , pp. 19-22) .
- See Copson ( 1935 , pp. 27-30, 95-97) . For ( 1.9.69 )-( 1.9.71 ), see Titchmarsh ( 1962b , 1.77) .
