# §1.4 Calculus of One Variable

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.4, `Calculus of One Variable`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Monotonicity
- Continuity
- Derivatives
- Indefinite Integrals
- Definite Integrals
- Taylor's Theorem for Real Variables
- Maxima and Minima
- Convex Functions

### Subsections

#### 1.4(i) Monotonicity

- If $f(x_{1})\leq f(x_{2})$ for every pair $x_{1}$ , $x_{2}$ in an interval $I$ such that $x_{1}<x_{2}$ , then $f(x)$ is nondecreasing on $I$ . If the $\leq$ sign is replaced by $<$ , then $f(x)$ is increasing (also called strictly increasing ) on $I$ . Similarly for nonincreasing and decreasing ( strictly decreasing ) functions. Each of the preceding four cases is classified as monotonic ; sometimes strictly monotonic is used for the strictly increasing or strictly decreasing cases.

Definitions and local symbols:
- Keywords: decreasing , functions , increasing , monotonic , monotonicity , nondecreasing , nonincreasing , strictly decreasing , strictly increasing , strictly monotonic

#### 1.4(ii) Continuity

- A function $f(x)$ is continuous on the right (or from above ) at $x=c$ if
- that is, for every arbitrarily small positive constant $\epsilon$ there exists $\delta$ ( $>0$ ) such that
- for all $\alpha$ such that $0\leq\alpha<\delta$ . Similarly, it is continuous on the left (or from below ) at $x=c$ if
- And $f(x)$ is continuous at $c$ when both ( 1.4.1 ) and ( 1.4.3 ) apply.
- If $f(x)$ is continuous at each point $c\in(a,b)$ , then $f(x)$ is continuous on the interval $(a,b)$ and we write $f\in C(a,b)$ . If also $f(x)$ is continuous on the right at $x=a$ , and continuous on the left at $x=b$ , then $f(x)$ is continuous on the interval $[a,b]$ , and we write $f(x)\in C[a,b]$ .
- A removable singularity of $f(x)$ at $x=c$ occurs when $f(c+)=f(c-)$ but $f(c)$ is undefined. For example, $f(x)=(\sin x)/x$ with $c=0$ .

Formulas:

Formula 1.4.1:

$$
f(c+)\equiv\lim_{x\to c+}f(x)=f(c),
$$

Formula 1.4.2:

$$
\left|f(c+\alpha)-f(c)\right|<\epsilon,
$$

Formula 1.4.3:

$$
f(c-)\equiv\lim_{x\to c-}f(x)=f(c).
$$


Definitions and local symbols:
- Defines: $C(I)$ or $C(a,b)$ : continuous on an interval $I$ or $(a,b)$
- Keywords: at a point , continuous , continuous function , discontinuity , functions , limits , limits of functions , notation , of one variable , on an interval , on the left (or right) , piecewise , piecewise continuous , removable , removable discontinuity , sectionally , simple discontinuity , singularity
- Symbols: $\equiv$ : equals by definition
- Symbols: $\left|x\right|$ : absolute value of $x$
- Symbols: $\equiv$ : equals by definition
- Symbols: $[a,b)$ : half-closed interval

#### 1.4(iii) Derivatives

- The derivative $f^{\prime}(x)$ of $f(x)$ is defined by
- When this limit exists $f$ is differentiable at $x$ .

Formulas:

Formula 1.4.4:

$$
f^{\prime}(x)=\frac{\mathrm{d}f}{\mathrm{d}x}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.
$$

Formula 1.4.5:

$$
(f+g)^{\prime}(x)=f^{\prime}(x)+g^{\prime}(x),
$$

Formula 1.4.6:

$$
(fg)^{\prime}(x)=f^{\prime}(x)g(x)+f(x)g^{\prime}(x),
$$

Formula 1.4.7:

$$
\left(\frac{f}{g}\right)^{\prime}(x)=\frac{f^{\prime}(x)g(x)-f(x)g^{\prime}(x)}{(g(x))^{2}}.
$$

Formula 1.4.8:

$$
f^{(2)}(x)=\frac{{\mathrm{d}}^{2}f}{{\mathrm{d}x}^{2}}=\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\mathrm{d}f}{\mathrm{d}x}\right),
$$

Formula 1.4.9:

$$
f^{(n)}=f^{(n)}(x)=\frac{\mathrm{d}}{\mathrm{d}x}f^{(n-1)}(x).
$$

Formula 1.4.10:

$$
h^{\prime}(x)=f^{\prime}(g(x))g^{\prime}(x).
$$

Formula 1.4.11:

$$
f(b)-f(a)=(b-a)f^{\prime}(c).
$$

Formula 1.4.12:

$$
(fg)^{(n)}=f^{(n)}g+\genfrac{(}{)}{0.0pt}{}{n}{1}f^{(n-1)}g^{\prime}+\dots+\genfrac{(}{)}{0.0pt}{}{n}{k}f^{(n-k)}g^{(k)}+\dots+fg^{(n)}.
$$

Formula 1.4.13:

$$
\frac{{\mathrm{d}}^{n}}{{\mathrm{d}x}^{n}}f(g(x))=\sum\left(\frac{n!}{m_{1}!m_{2}!\cdots m_{n}!}\right)f^{(k)}(g(x))\,\left(\frac{g^{\prime}(x)}{1!}\right)^{m_{1}}\left(\frac{g^{\prime\prime}(x)}{2!}\right)^{m_{2}}\dots\left(\frac{g^{(n)}(x)}{n!}\right)^{m_{n}},
$$

Formula 1.4.14:

$$
\lim\limits_{x\to a}f(x)=\lim\limits_{x\to a}g(x)=0\quad(\mathrm{or}\,\infty),
$$

Formula 1.4.15:

$$
\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f^{\prime}(x)}{g^{\prime}(x)}
$$


Definitions and local symbols:
- Keywords: definition , derivatives , notation
- Defines: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$
- Defines: $C^{n}(I)$ or $C^{n}(a,b)$ : continuously differentiable $n$ times on an interval $I$ or $(a,b)$
- Keywords: continuously differentiable , differentiable , differentiable functions , functions
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $n$ : nonnegative integer
- Keywords: chain rule , derivatives , for derivatives
- Keywords: local , maximum , minimum
- Keywords: derivatives , differentiable functions , mean value theorem , mean value theorems
- Keywords: Leibniz's formula , Leibniz's formula for derivatives , derivatives
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $k$ : integer and $n$ : nonnegative integer
- Keywords: Fa di Bruno's formula , derivatives , for derivatives
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $!$ : factorial (as in $n!$ ) , $k$ : integer , $m$ : nonnegative integer and $n$ : nonnegative integer
- Keywords: L'Hpital's rule , L'Hpital's rule for derivatives , derivatives

#### 1.4(iv) Indefinite Integrals

- If $F^{\prime}(x)=f(x)$ , then $\int f\,\mathrm{d}x=F(x)+C$ , where $C$ is a constant.

Formulas:

Formula 1.4.16:

$$
\int fg\,\mathrm{d}x=\left(\int f\,\mathrm{d}x\right)g-\int\left(\int f\,\mathrm{d}x\right)\frac{\mathrm{d}g}{\mathrm{d}x}\,\mathrm{d}x.
$$

Formula 1.4.17:

$$
\int x^{n}\,\mathrm{d}x=\begin{cases}\dfrac{x^{n+1}}{n+1}+C,&\quad n\not=-1,\\ \ln\left|x\right|+C,&\quad n=-1.\end{cases}
$$


Definitions and local symbols:
- Defines: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: indefinite , integrals , integration
- Keywords: by parts , integrals , integration , tables
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\ln z$ : principal branch of logarithm function , $n$ : nonnegative integer , $C$ : constant and $\left|x\right|$ : absolute value of $x$

#### 1.4(v) Definite Integrals

Formulas:

Formula 1.4.18:

$$
\int^{b}_{a}f(x)\,\mathrm{d}x=\lim\sum^{n-1}_{j=0}f(\xi_{j})(x_{j+1}-x_{j})
$$

Formula 1.4.19:

$$
\int^{b}_{a}(cf(x)+dg(x))\,\mathrm{d}x=c\int^{b}_{a}f(x)\,\mathrm{d}x+d\int^{b}_{a}g(x)\,\mathrm{d}x,
$$

Formula 1.4.20:

$$
\int^{b}_{a}f(x)\,\mathrm{d}x=-\int^{a}_{b}f(x)\,\mathrm{d}x.
$$

Formula 1.4.21:

$$
\int^{b}_{a}f(x)\,\mathrm{d}x=\int^{c}_{a}f(x)\,\mathrm{d}x+\int^{b}_{c}f(x)\,\mathrm{d}x.
$$

Formula 1.4.22:

$$
\int^{\infty}_{a}f(x)\,\mathrm{d}x=\lim_{b\to\infty}\int^{b}_{a}f(x)\,\mathrm{d}x.
$$

Formula 1.4.23:

$$
\int^{b}_{a}f(x)\,\mathrm{d}x=\lim_{c\to b-}\int^{c}_{a}f(x)\,\mathrm{d}x.
$$

Formula 1.4.23_1:

$$
\alpha(d)-\alpha(c)=\int_{c}^{d}w(x)\,\mathrm{d}x,
$$

Formula 1.4.23_2:

$$
\int_{a}^{b}f(x)\,\mathrm{d}\alpha(x)=\int_{a}^{b}f(x)w(x)\,\mathrm{d}x,
$$

Formula 1.4.23_3:

$$
\int_{a}^{b}f(x)\,\mathrm{d}\alpha(x)=\int_{a}^{b}w(x)f(x)\,\mathrm{d}x+\sum_{n=1}^{N}w_{n}f(x_{n}).
$$

Formula 1.4.24:

$$
\operatorname{PV}\!\int^{b}_{a}f(x)\,\mathrm{d}x=P\int^{b}_{a}f(x)\,\mathrm{d}x=\lim_{\epsilon\to 0+}\left(\int^{c-\epsilon}_{a}f(x)\,\mathrm{d}x+\int^{b}_{c+\epsilon}f(x)\,\mathrm{d}x\right),
$$

Formula 1.4.25:

$$
\operatorname{PV}\!\int^{\infty}_{-\infty}f(x)\,\mathrm{d}x=P\int^{\infty}_{-\infty}f(x)\,\mathrm{d}x=\lim_{b\to\infty}\int^{b}_{-b}f(x)\,\mathrm{d}x,
$$

Formula 1.4.26:

$$
\int^{b}_{a}f(x)\,\mathrm{d}x=F(b)-F(a),
$$

Formula 1.4.27:

$$
\frac{\mathrm{d}}{\mathrm{d}x}\int^{x}_{a}f(t)\,\mathrm{d}t=f(x).
$$

Formula 1.4.28:

$$
\int^{b}_{a}f(\phi(x))\phi^{\prime}(x)\,\mathrm{d}x=\int^{\phi(b)}_{\phi(a)}f(t)\,\mathrm{d}t.
$$

Formula 1.4.29:

$$
\int^{b}_{a}f(x)\phi(x)\,\mathrm{d}x=f(c)\int^{b}_{a}\phi(x)\,\mathrm{d}x.
$$

Formula 1.4.30:

$$
\int^{b}_{a}f(x)\phi(x)\,\mathrm{d}x=f(a)\int^{c}_{a}\phi(x)\,\mathrm{d}x+f(b)\int^{b}_{c}\phi(x)\,\mathrm{d}x.
$$

Formula 1.4.31:

$$
\int_{a}^{b}\,\mathrm{d}x_{n}\int_{a}^{x_{n}}\,\mathrm{d}x_{n-1}\cdots\int_{a}^{x_{2}}\,\mathrm{d}x_{1}\int_{a}^{x_{1}}f(x)\,\mathrm{d}x=\frac{1}{n!}\int_{a}^{b}(b-x)^{n}f(x)\,\mathrm{d}x.
$$

Formula 1.4.32:

$$
\|f\|^{2}_{2}\equiv\int^{b}_{a}{\left|f(x)\right|}^{2}\,\mathrm{d}x<\infty.
$$

Formula 1.4.33:

$$
\mathcal{V}_{a,b}\left(f\right)=\sup\sum^{n}_{j=1}\left|f(x_{j})-f(x_{j-1})\right|,
$$

Formula 1.4.34:

$$
\mathcal{V}_{a,b}\left(f\right)=\int^{b}_{a}\left|f^{\prime}(x)\right|\,\mathrm{d}x,
$$


Definitions and local symbols:
- Keywords: definite , integrals , integration
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $j$ : integer , $n$ : nonnegative integer and $\xi_{j}$ : point
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: absolute , convergence , infinite , integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Lebesgue , Lebesgue-Stieltjes , Stieltjes , absolute , convergence , integrals
- Keywords: Absolutely continuous integration measure , Stieltjes , absolutely convergent , measure
- Symbols: $[a,b]$ : closed interval , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\subset$ : is contained in and $w(x)$ : weight function
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $w(x)$ : weight function
- Keywords: Steiltjes , Stieltjes , Stieltjes with jumps , integral , measure , measure with jumps
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $w(x)$ : weight function
- Keywords: Cauchy principal values , integrals
- Defines: $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value
- Keywords: differentiation , fundamental theorem of calculus , integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral

#### 1.4(vi) Taylor's Theorem for Real Variables

- If $f(x)\in C^{n+1}[a,b]$ , then
- and

Formulas:

Formula 1.4.35:

$$
f(x)=\sum^{n}_{k=0}\frac{f^{(k)}(a)}{k!}(x-a)^{k}+R_{n},
$$

Formula 1.4.36:

$$
R_{n}=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1},
$$

Formula 1.4.37:

$$
R_{n}=\frac{1}{n!}\int^{x}_{a}(x-t)^{n}f^{(n+1)}(t)\,\mathrm{d}t.
$$


Definitions and local symbols:
- Keywords: Taylor's theorem , one variable
- Symbols: $!$ : factorial (as in $n!$ ) , $k$ : integer , $n$ : nonnegative integer and $R_{n}$ : remainder
- Symbols: $!$ : factorial (as in $n!$ ) , $n$ : nonnegative integer and $R_{n}$ : remainder
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $!$ : factorial (as in $n!$ ) , $\int$ : integral , $n$ : nonnegative integer and $R_{n}$ : remainder

#### 1.4(vii) Maxima and Minima

- If $f(x)$ is twice-differentiable, and if also $f^{\prime}(x_{0})=0$ and $f^{\prime\prime}(x_{0})<0$ ( $>0$ ), then $x=x_{0}$ is a local maximum (minimum) ( 1.4(iii) ) of $f(x)$ . The overall maximum (minimum) of $f(x)$ on $[a,b]$ will either be at a local maximum (minimum) or at one of the end points $a$ or $b$ .

Definitions and local symbols:
- Keywords: maximum , minimum

#### 1.4(viii) Convex Functions

- A function $f(x)$ is convex on $(a,b)$ if
- for any $c,d\in(a,b)$ , and $t\in[0,1]$ . See Figure 1.4.2 . A similar definition applies to closed intervals $[a,b]$ .
- If $f(x)$ is twice differentiable, then $f(x)$ is convex iff $f^{\prime\prime}(x)\geq 0$ on $(a,b)$ . A continuously differentiable function is convex iff the curve does not lie below its tangent at any point.

Formulas:

Formula 1.4.38:

$$
f((1-t)c+td)\leq(1-t)f(c)+tf(d)
$$


Definitions and local symbols:
- Keywords: calculus , convex , convex functions , functions , one variable
- Symbols: $\in$ : element of and $(a,b)$ : open interval

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.4](https://dlmf.nist.gov/1.4)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: calculus, one variable, decreasing, functions, increasing, monotonic, monotonicity, nondecreasing, nonincreasing, strictly decreasing, strictly increasing, strictly monotonic, at a point, continuous, continuous function, discontinuity, limits, limits of functions, notation, of one variable, on an interval, on the left (or right), piecewise, piecewise continuous, removable, removable discontinuity, sectionally, simple discontinuity, singularity, definition, derivatives, continuously differentiable, differentiable, differentiable functions, chain rule, for derivatives, local, maximum, minimum, mean value theorem.

### Source Notes

- See Hardy ( 1952 , Chapter 5) and Olver ( 1997b , p. 73) .
- See Hardy ( 1952 , Chapter 6) or Rudin ( 1976 , Chapter 5) . For ( 1.4.13 ) see Riordan ( 1958 , pp. 35-36) and Knuth ( 1968 , p. 50) .
- See Hardy ( 1952 , pp. 247-248, 258) .
- See Hardy ( 1952 , Chapters 6, 7) . For ( 1.4.31 ) integrate by parts. For ( 1.4.34 ) see Olver ( 1997b , p. 28) .
- See Hardy ( 1952 , pp. 285-292, 327-328) .
- See Hardy ( 1952 , pp. 234-235) .
- See Hardy et al. ( 1967 , pp. 70-77) .
