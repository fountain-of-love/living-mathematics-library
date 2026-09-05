# §1.10 Functions of a Complex Variable

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.10, `Functions of a Complex Variable`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Taylor's Theorem for Complex Variables
- Analytic Continuation
- Laurent Series
- Residue Theorem
- Maximum-Modulus Principle
- Multivalued Functions
- Inverse Functions
- Functions Defined by Contour Integrals
- Infinite Products
- Infinite Partial Fractions
- Generating Functions

### Subsections

#### 1.10(i) Taylor's Theorem for Complex Variables

- Let $f(z)$ be analytic on the disk $\left|z-z_{0}\right|<R$ . Then
- The right-hand side is the Taylor series for $f(z)$ at $z=z_{0}$ , and its radius of convergence is at least $R$ .

Formulas:

Formula 1.10.1:

$$
f(z)=\sum^{\infty}_{n=0}\frac{f^{(n)}(z_{0})}{n!}(z-z_{0})^{n}.
$$

Formula 1.10.2:

$$
{\mathrm{e}}^{z}=1+\frac{z}{1!}+\frac{z^{2}}{2!}+\cdots,
$$

Formula 1.10.3:

$$
\ln\left(1+z\right)=z-\frac{z^{2}}{2}+\frac{z^{3}}{3}-\cdots,
$$

Formula 1.10.4:

$$
(1-z)^{-\alpha}=1+\alpha z+\frac{\alpha(\alpha+1)}{2!}z^{2}+\frac{\alpha(\alpha+1)(\alpha+2)}{3!}z^{3}+\cdots,
$$


Definitions and local symbols:
- Keywords: Taylor series , Taylor's theorem , one variable
- Symbols: $!$ : factorial (as in $n!$ ) , $z$ : variable and $n$ : nonnegative integer
- Symbols: $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) , $z$ : variable and $\left|x\right|$ : absolute value of $x$
- Symbols: $\ln z$ : principal branch of logarithm function , $z$ : variable and $\left|x\right|$ : absolute value of $x$
- Symbols: $!$ : factorial (as in $n!$ ) , $z$ : variable and $\left|x\right|$ : absolute value of $x$
- Keywords: analytic function , multiplicity , simple zero , zeros , zeros of analytic functions

#### 1.10(ii) Analytic Continuation

- Let $f_{1}(z)$ be analytic in a domain $D_{1}$ . If $f_{2}(z)$ , analytic in $D_{2}$ , equals $f_{1}(z)$ on an arc in $D=D_{1}\cap D_{2}$ , or on just an infinite number of points with a limit point in $D$ , then they are equal throughout $D$ and $f_{2}(z)$ is called an analytic continuation of $f_{1}(z)$ . We write $(f_{1},D_{1})$ , $(f_{2},D_{2})$ to signify this continuation.
- Suppose $z(t)=x(t)+\mathrm{i}y(t)$ , $a\leq t\leq b$ , is an arc and $a=t_{0}<t_{1}<\cdots<t_{n}=b$ . Suppose the subarc $z(t)$ , $t\in[t_{j-1},t_{j}]$ is contained in a domain $D_{j}$ , $j=1,\dots,n$ . The function $f_{1}(z)$ on $D_{1}$ is said to be analytically continued along the path $z(t)$ , $a\leq t\leq b$ , if there is a chain $(f_{1},D_{1})$ , $(f_{2},D_{2}),\dots,(f_{n},D_{n})$ .
- Analytic continuation is a powerful aid in establishing transformations or functional equations for complex variables, because it enables the problem to be reduced to: (a) deriving the transformation (or functional equation) with real variables; followed by (b) finding the domain on which the transformed function is analytic.

Formulas:

Formula 1.10.5:

$$
f(\overline{z})=\overline{f(z)}.
$$


Definitions and local symbols:
- Keywords: analytic continuation , analytically continued , functions
- Keywords: Schwarz reflection principle , analytic continuation , by reflection
- Symbols: $\overline{z}$ : complex conjugate

#### 1.10(iii) Laurent Series

- Suppose $f(z)$ is analytic in the annulus $r_{1}<\left|z-z_{0}\right|<r_{2}$ , $0\leq r_{1}<r_{2}\leq\infty$ , and $r\in(r_{1},r_{2})$ . Then
- where
- and the integration contour is described once in the positive sense. The series ( 1.10.6 ) converges uniformly and absolutely on compact sets in the annulus.
- Let $r_{1}=0$ , so that the annulus becomes the punctured neighborhood $N$ : $0<\left|z-z_{0}\right|<r_{2}$ , and assume that $f(z)$ is analytic in $N$ , but not at $z_{0}$ . Then $z=z_{0}$ is an isolated singularity of $f(z)$ . This singularity is removable if $a_{n}=0$ for all $n<0$ , and in this case the Laurent series becomes the Taylor series. Next, $z_{0}$ is a pole if $a_{n}\not=0$ for at least one, but only finitely many, negative $n$ . If $-n$ is the first negative integer (counting from $-\infty$ ) with $a_{-n}\not=0$ , then $z_{0}$ is a pole of order (or multiplicity ) $n$ . Lastly, if $a_{n}\not=0$ for infinitely many negative $n$ , then $z_{0}$ is an isolated essential singularity .
- The singularities of $f(z)$ at infinity are classified in the same way as the singularities of $f(1/z)$ at $z=0$ .
- An isolated singularity $z_{0}$ is always removable when $\lim_{z\to z_{0}}f(z)$ exists, for example $(\sin z)/z$ at $z=0$ .

Formulas:

Formula 1.10.6:

$$
f(z)=\sum^{\infty}_{n=-\infty}a_{n}(z-z_{0})^{n},
$$

Formula 1.10.7:

$$
a_{n}=\frac{1}{2\pi\mathrm{i}}\int_{\left|z-z_{0}\right|=r}\frac{f(z)}{(z-z_{0})^{n+1}}\,\mathrm{d}z,
$$


Definitions and local symbols:
- Defines: $\operatorname{res}$ : residue
- Keywords: Laurent series , analytic function , annulus , essential , essential singularity , functions , isolated , isolated essential , isolated essential singularity , isolated singularity , meromorphic , meromorphic function , multiplicity , neighborhood , order , pole , punctured , punctured neighborhood , removable , removable singularity , residue , singularities , singularity
- Symbols: $z$ : variable and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $z$ : variable , $n$ : nonnegative integer , $r_{1}$ , $r_{2}$ : annulus radii and $\left|x\right|$ : absolute value of $x$
- Keywords: Picard's theorem

#### 1.10(iv) Residue Theorem

- If $f(z)$ is analytic within a simple closed contour $C$ , and continuous within and on $C$ -except in both instances for a finite number of singularities within $C$ -then
- Here and elsewhere in this subsection the path $C$ is described in the positive sense.

Formulas:

Formula 1.10.8:

$$
\frac{1}{2\pi\mathrm{i}}\int_{C}f(z)\,\mathrm{d}z=\mathrm{sum}\,\mathrm{of}\,\mathrm{the}\,\mathrm{residues}\,\mathrm{of}\,f(z)\,\mathrm{within}\,C.
$$

Formula 1.10.9:

$$
N-P=\frac{1}{2\pi\mathrm{i}}\int_{C}\frac{f^{\prime}(z)}{f(z)}\,\mathrm{d}z=\frac{1}{2\pi}\Delta_{C}(\operatorname{ph}f(z)),
$$

Formula 1.10.10:

$$
\frac{1}{2\pi\mathrm{i}}\int_{C}\frac{zf^{\prime}(z)}{f(z)}\,\mathrm{d}z=(\mathrm{sum}\,\mathrm{of}\,\mathrm{locations}\,\mathrm{of}\,\mathrm{zeros})-(\mathrm{sum}\,\mathrm{of}\,\mathrm{locations}\,\mathrm{of}\,\mathrm{poles}),
$$


Definitions and local symbols:
- Keywords: residue , theorem
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $z$ : variable and $C$ : closed contour
- Keywords: argument principle , phase principle , principle of the argument
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\operatorname{ph}$ : phase , $z$ : variable , $C$ : closed contour , $N$ : number of zeros and $P$ : number of zeros
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $z$ : variable and $C$ : closed contour
- Keywords: Rouch's theorem

#### 1.10(v) Maximum-Modulus Principle

Formulas:

Formula 1.10.11:

$$
\left|f(z)\right|\leq\frac{M\left|z\right|}{R}\;\mathrm{and}\;\left|f^{\prime}(0)\right|\leq\frac{M}{R}.
$$


Definitions and local symbols:
- Keywords: analytic functions , maximum-modulus principle
- Keywords: harmonic functions , maximum modulus , maximum-modulus principle
- Keywords: Schwarz's lemma , maximum-modulus principle
- Symbols: $z$ : variable , $R$ : radius and $\left|x\right|$ : absolute value of $x$

#### 1.10(vi) Multivalued Functions

- Functions which have more than one value at a given point $z$ are called multivalued (or many-valued ) functions. Let $F(z)$ be a multivalued function and $D$ be a domain. If we can assign a unique value $f(z)$ to $F(z)$ at each point of $D$ , and $f(z)$ is analytic on $D$ , then $f(z)$ is a branch of $F(z)$ .

Definitions and local symbols:
- Keywords: branch , functions , many-valued , many-valued function , multivalued , multivalued function , of multivalued function
- Keywords: branch , branch point , construction , cut , domain , neighborhood , of multivalued function , singularity
- Keywords: branch , example , of multivalued function
- Symbols: $D$ : domain

#### 1.10(vii) Inverse Functions

Formulas:

Formula 1.10.12:

$$
f(z)=w
$$

Formula 1.10.13:

$$
F(w)=z_{0}+\sum^{\infty}_{n=1}F_{n}(w-w_{0})^{n}
$$

Formula 1.10.14:

$$
g(F(w))=g(z_{0})+\sum^{\infty}_{n=1}G_{n}(w-w_{0})^{n},
$$

Formula 1.10.15:

$$
f(z)=f(z_{0})+\sum^{\infty}_{n=0}f_{n}(z-z_{0})^{\mu+n},
$$

Formula 1.10.16:

$$
F(w)=z_{0}+\sum^{\infty}_{n=1}F_{n}(w-w_{0})^{n/\mu}
$$

Formula 1.10.17:

$$
g(F(w))=g(z_{0})+\sum^{\infty}_{n=1}G_{n}(w-w_{0})^{n/\mu},
$$


Definitions and local symbols:
- Keywords: functions , inverse , inverse function
- Keywords: Lagrange inversion theorem , inverse function
- Symbols: $z$ : variable and $w$ : variable
- Defines: $F(w)$ : inverse function of $f(z)$ (locally)
- Symbols: $z$ : variable , $w$ : variable , $n$ : nonnegative integer and $F_{n}$ : residue
- Symbols: $z$ : variable , $w$ : variable , $n$ : nonnegative integer , $F(w)$ : inverse function of $f(z)$ and $G_{n}$ : residue
- Keywords: Lagrange inversion theorem , extended , inverse function
- Symbols: $z$ : variable , $n$ : nonnegative integer , $f_{n}$ : residue and $\mu$ : parameter
- Symbols: $z$ : variable , $w$ : variable , $n$ : nonnegative integer , $F(w)$ : inverse function of $f(z)$ , $F_{n}$ : residue and $\mu$ : parameter
- Symbols: $z$ : variable , $w$ : variable , $n$ : nonnegative integer , $F(w)$ : inverse function of $f(z)$ , $\mu$ : parameter and $G_{n}$ : residue

#### 1.10(viii) Functions Defined by Contour Integrals

- Let $D$ be a domain and $[a,b]$ be a closed finite segment of the real axis. Assume that for each $t\in[a,b]$ , $f(z,t)$ is an analytic function of $z$ in $D$ , and also that $f(z,t)$ is a continuous function of both variables. Then
- is analytic in $D$ and its derivatives of all orders can be found by differentiating under the sign of integration.
- This result is also true when $b=\infty$ , or when $f(z,t)$ has a singularity at $t=b$ , with the following conditions. For each $t\in[a,b)$ , $f(z,t)$ is analytic in $D$ ; $f(z,t)$ is a continuous function of both variables when $z\in D$ and $t\in[a,b)$ ; the integral ( 1.10.18 ) converges at $b$ , and this convergence is uniform with respect to $z$ in every compact subset $S$ of $D$ .
- The last condition means that given $\epsilon$ ( $>0$ ) there exists a number $a_{0}\in[a,b)$ that is independent of $z$ and is such that
- for all $a_{1}\in[a_{0},b)$ and all $z\in S$ ; compare  1.5(iv) .

Formulas:

Formula 1.10.18:

$$
F(z)=\int^{b}_{a}f(z,t)\,\mathrm{d}t
$$

Formula 1.10.19:

$$
\left|\int_{a_{1}}^{b}f(z,t)\,\mathrm{d}t\right|<\epsilon,
$$


Definitions and local symbols:
- Keywords: convergence , defined by contour integrals , differentiation , functions , integrals , of integrals , uniform
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $z$ : variable
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $z$ : variable , $\epsilon$ : positive number and $\left|x\right|$ : absolute value of $x$

#### 1.10(ix) Infinite Products

- Let $p_{k,m}=\prod_{n=k}^{m}(1+a_{n})$ . If for some $k\geq 1$ , $p_{k,m}\to p_{k}\not=0$ as $m\to\infty$ , then we say that the infinite product $\prod^{\infty}_{n=1}(1+a_{n})$ converges . (The integer $k$ may be greater than one to allow for a finite number of zero factors.) The convergence of the product is absolute if $\prod^{\infty}_{n=1}(1+\left|a_{n}\right|)$ converges. The product $\prod^{\infty}_{n=1}(1+a_{n})$ , with $a_{n}\not=-1$ for all $n$ , converges iff $\sum^{\infty}_{n=1}\ln\left(1+a_{n}\right)$ converges; and it converges absolutely iff $\sum^{\infty}_{n=1}\left|a_{n}\right|$ converges.
- Suppose $a_{n}=a_{n}(z)$ , $z\in D$ , a domain. The convergence of the infinite product is uniform if the sequence of partial products converges uniformly.

Formulas:

Formula 1.10.20:

$$
\left|\ln\left(1+a_{n}(z)\right)\right|\leq M_{n},
$$

Formula 1.10.21:

$$
\sum^{\infty}_{n=1}M_{n}<\infty,
$$

Formula 1.10.22:

$$
P(z)=\prod^{\infty}_{n=1}\left(1-\frac{z}{z_{n}}\right){\mathrm{e}}^{z/z_{n}}
$$


Definitions and local symbols:
- Keywords: absolute , convergence , infinite products , uniform
- Keywords: $M$ -test for uniform convergence , Weierstrass $M$ -test , infinite products
- Symbols: $\ln z$ : principal branch of logarithm function , $z$ : variable , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $n$ : nonnegative integer
- Keywords: Weierstrass product , infinite products
- Symbols: $\mathrm{e}$ : base of natural logarithm , $z$ : variable and $n$ : nonnegative integer

#### 1.10(x) Infinite Partial Fractions

- Suppose $D$ is a domain, and
- where $a_{n}(z)$ is analytic for all $n\geq 1$ , and the convergence of the product is uniform in any compact subset of $D$ . Then $F(z)$ is analytic in $D$ .
- If, also, $a_{n}(z)\neq 0$ when $n\geq 1$ and $z\in D$ , then $F(z)\neq 0$ on $D$ and

Formulas:

Formula 1.10.23:

$$
F(z)=\prod^{\infty}_{n=1}a_{n}(z),
$$

Formula 1.10.24:

$$
\frac{F^{\prime}(z)}{F(z)}=\sum^{\infty}_{n=1}\frac{a_{n}^{\prime}(z)}{a_{n}(z)}.
$$

Formula 1.10.25:

$$
f(z)=\sum^{\infty}_{n=1}a_{n}\left(\frac{1}{z-z_{n}}+\frac{1}{z_{n}}\right)
$$


Definitions and local symbols:
- Keywords: infinite partial fractions , infinite products , relation to infinite partial fractions
- Defines: $F$ : function (locally)
- Symbols: $\in$ : element of , $z$ : variable , $n$ : nonnegative integer and $D$ : domain
- Symbols: $z$ : variable , $n$ : nonnegative integer and $F$ : function
- Keywords: Mittag-Leffler's expansion , functions , infinite partial fractions , of a complex variable
- Symbols: $z$ : variable and $n$ : nonnegative integer

#### 1.10(xi) Generating Functions

- Let $F(x,z)$ have a converging power series expansion of the form
- The radius of convergence $R$ might depend on $x$ . Then $F(x;z)$ is the generating function for the functions $p_{n}(x)$ , which will automatically have an integral representation
- compare ( 1.10.7 ). Often Darboux's method can be used to study the behavior of $p_{n}(x)$ as $n\to\infty$ . Compare  2.10(iv) .

Formulas:

Formula 1.10.26:

$$
F(x;z)=\sum^{\infty}_{n=0}p_{n}(x)z^{n},
$$

Formula 1.10.27:

$$
p_{n}(x)=\frac{1}{2\pi\mathrm{i}}\int_{\left|z\right|=r}\frac{F(x;z)}{z^{n+1}}\,\mathrm{d}z,
$$

Formula 1.10.28:

$$
F(x,\lambda;z)=\left(1-2xz+z^{2}\right)^{-\lambda}=\sum_{n=0}^{\infty}C^{(\lambda)}_{n}\left(x\right)z^{n},
$$

Formula 1.10.29:

$$
\sum_{n=0}^{\infty}\frac{\mathrm{d}}{\mathrm{d}x}C^{(\lambda)}_{n}\left(x\right)z^{n}=2\lambda z\left(1-2xz+z^{2}\right)^{-\lambda-1}=\sum_{n=0}^{\infty}2\lambda C^{(\lambda+1)}_{n}\left(x\right)z^{n+1},
$$


Definitions and local symbols:
- Keywords: definition , generating function
- Symbols: $z$ : variable , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $z$ : variable , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $C^{(\lambda)}_{n}\left(x\right)$ : ultraspherical (or Gegenbauer) polynomial , $z$ : variable , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $C^{(\lambda)}_{n}\left(x\right)$ : ultraspherical (or Gegenbauer) polynomial , $z$ : variable and $n$ : nonnegative integer

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.10](https://dlmf.nist.gov/1.10)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: functions, of a complex variable, Taylor series, Taylor's theorem, one variable, analytic function, multiplicity, simple zero, zeros, zeros of analytic functions, analytic continuation, analytically continued, Schwarz reflection principle, by reflection, Laurent series, annulus, essential, essential singularity, isolated, isolated essential, isolated essential singularity, isolated singularity, meromorphic, meromorphic function, neighborhood, order, pole, punctured, punctured neighborhood, removable, removable singularity, residue, singularities, singularity, Picard's theorem, theorem, argument principle, phase principle, principle of the argument, Rouch's theorem.

### Source Notes

- See Copson ( 1935 , pp. 72-75) and Levinson and Redheffer ( 1970 , pp. 140-143) .
- See Levinson and Redheffer ( 1970 , pp. 398-402) and Copson ( 1935 , pp. 192-193) .
- See Levinson and Redheffer ( 1970 , pp. 162-170) , Copson ( 1935 , pp. 75-81, 438-440) , and Markushevich ( 1983 , pp. 234-245) .
- See Copson ( 1935 , pp. 117-120) .
- See Titchmarsh ( 1962b , pp. 165-169) .
- See Levinson and Redheffer ( 1970 , pp. 64-77) , or Markushevich ( 1983 , pp. 106-121) .
- For ( 1.10.13 ) and ( 1.10.14 ) see Copson ( 1935 , 6.23) . See also Andrews et al. ( 1999 , pp. 629-631) and Henrici ( 1974 , pp. 57-59) . The Extended Inversion Theorem is proved in a similar way.
- See Copson ( 1935 , pp. 106-113) .
