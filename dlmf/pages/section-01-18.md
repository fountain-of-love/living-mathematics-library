# §1.18 Linear Second Order Differential Operators and Eigenfunction Expansions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.18, `Linear Second Order Differential Operators and Eigenfunction Expansions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Hilbert spaces
- L 2 spaces on intervals in R
- Linear Operators on a Hilbert Space
- Formally Self-adjoint Linear Second Order Differential Operators
- Point Spectra and Eigenfunction Expansions
- Continuous Spectra and Eigenfunction Expansions: Simple Cases
- Continuous Spectra: More General Cases
- Mixed Spectra and Eigenfunction Expansions
- Mathematical Background
- Literature

### Mathematical Narrative

- A survey is given of the formal spectral theory of second order differential operators, typical results being presented in  1.18(i) through  1.18(viii) . The various types of spectra and the corresponding eigenfunction expansions are illustrated by examples. These are based on the Liouville normal form of ( 1.13.29 ). A more precise mathematical discussion then follows in  1.18(ix) .

### Subsections

#### 1.18(i) Hilbert spaces

- A complex linear vector space $V$ is called an inner product space if an inner product $\left\langle u,v\right\rangle\in\mathbb{C}$ is defined for all $u,v\in V$ with the properties: (i) $\left\langle u,v\right\rangle$ is complex linear in $u$ ; (ii) $\left\langle u,v\right\rangle=\overline{\left\langle v,u\right\rangle}$ ; (iii) $\left\langle v,v\right\rangle\geq 0$ ; (iv) if $\left\langle v,v\right\rangle=0$ then $v=0$ . With norm defined by
- $V$ becomes a normed linear vector space. If $\left\|{v}\right\|=1$ then $v$ is normalized . Two elements $u$ and $v$ in $V$ are orthogonal if $\left\langle u,v\right\rangle=0$ . A (finite or countably infinite, generalizing the definition of ( 1.2.40 )) set $\{v_{n}\}$ is an orthonormal set if the $v_{n}$ are normalized and pairwise orthogonal.
- An inner product space $V$ is called a Hilbert space if every Cauchy sequence $\{v_{n}\}$ in $V$ (i.e., $\lim_{m,n\to\infty}\left\|{v_{m}-v_{n}}\right\|=0$ ) converges in norm to some $v\in V$ , i.e., $\lim_{n\to\infty}\left\|{v-v_{n}}\right\|=0$ . For an orthonormal set $\{v_{n}\}$ in a Hilbert space $V$ Bessel's inequality holds:
- where $v\in V$ and
- A Hilbert space $V$ is separable if there is an (at most countably infinite) orthonormal set $\{v_{n}\}$ in $V$ such that for every $v\in V$
- where $c_{n}$ is given by ( 1.18.3 ). Such orthonormal sets are called complete . By ( 1.18.4 )

Formulas:

Formula 1.18.1:

$$
\left\|{v}\right\|=\sqrt{\left\langle v,v\right\rangle},
$$

Formula 1.18.2:

$$
\sum_{n}{\left|c_{n}\right|}^{2}\leq{\left\|{v}\right\|}^{2},
$$

Formula 1.18.3:

$$
c_{n}=\left\langle v,v_{n}\right\rangle.
$$

Formula 1.18.4:

$$
\sum_{n}{\left|c_{n}\right|}^{2}={\left\|{v}\right\|}^{2},
$$

Formula 1.18.5:

$$
\sum_{n=0}^{\infty}{\left|c_{n}\right|}^{2}<\infty.
$$

Formula 1.18.6:

$$
v=\sum_{n=0}^{\infty}c_{n}v_{n},
$$

Formula 1.18.7:

$$
\lim_{N\to\infty}\left\|{v-\sum_{n=0}^{N}c_{n}v_{n}}\right\|=0.
$$

Formula 1.18.8:

$$
{\left\|{v}\right\|}^{2}=\sum_{n=0}^{\infty}{\left|c_{n}\right|}^{2}<\infty.
$$

Formula 1.18.9:

$$
\left\langle v,w\right\rangle=\sum_{n=0}^{\infty}c_{n}\overline{d_{n}}.
$$

Formula 1.18.10:

$$
\sum_{n=0}^{\infty}c_{n}v_{n}\mapsto(c_{0},c_{1},c_{2},\ldots)\colon V\to\ell^{2}.
$$


Definitions and local symbols:
- Keywords: Hilbert , Hilbert space , expansion of arbitrary vector , inner product , $\ell^{2}$ space , space
- Symbols: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $n$ : nonnegative integer
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $n$ : nonnegative integer
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) and $n$ : nonnegative integer
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\overline{z}$ : complex conjugate , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors , $w$ : variable and $n$ : nonnegative integer
- Symbols: $\ell$ : integer and $n$ : nonnegative integer

#### 1.18(ii) L 2 spaces on intervals in R

- Let $X=[a,b]$ or $[a,b)$ or $(a,b]$ or $(a,b)$ be a (possibly infinite, or semi-infinite) interval in $\mathbb{R}$ . For a Lebesgue-Stieltjes measure $\,\mathrm{d}\alpha$ on $X$ let $L^{2}\left(X,\mathrm{d}\alpha\right)$ be the space of all Lebesgue-Stieltjes measurable complex-valued functions on $X$ which are square integrable with respect to $\,\mathrm{d}\alpha$ ,
- Functions $f,g\in L^{2}\left(X,\mathrm{d}\alpha\right)$ for which $\left\langle f-g,f-g\right\rangle=0$ are identified with each other. The space $L^{2}\left(X,\mathrm{d}\alpha\right)$ becomes a separable Hilbert space with inner product
- thus generalizing the inner product of ( 1.18.9 ). When $\alpha$ is absolutely continuous, i.e. $\,\mathrm{d}\alpha(x)=w(x)\,\mathrm{d}x$ , see  1.4(v) , where the nonnegative weight function $w(x)$ is Lebesgue measurable on $X$ . In this section we will only consider the special case $w(x)=1$ , so $\,\mathrm{d}\alpha(x)=\,\mathrm{d}x$ ; in which case $L^{2}\left(X\right)\equiv L^{2}\left(X,\mathrm{d}x\right)$ .
- Assume that $\left\{\phi_{n}\right\}_{n=0}^{\infty}$ is an orthonormal basis of $L^{2}\left(X\right)$ . The formulas in  1.18(i) are then:
- where the limit has to be understood in the sense of $L^{2}$ convergence in the mean:
- Often circumstances allow rather stronger statements, such as uniform convergence, or pointwise convergence at points where $f(x)$ is continuous, with convergence to $(f(x_{0}-)+f(x_{0}+))/2$ if $x_{0}$ is an isolated point of discontinuity.

Formulas:

Formula 1.18.11:

$$
\int_{a}^{b}{\left|f(x)\right|}^{2}\,\mathrm{d}\alpha(x)<\infty.
$$

Formula 1.18.12:

$$
\left\langle f,g\right\rangle=\int_{a}^{b}f(x)\overline{g(x)}\,\mathrm{d}\alpha(x),
$$

Formula 1.18.13:

$$
c_{n}=\left\langle f,\phi_{n}\right\rangle=\int_{a}^{b}f(x)\overline{\phi_{n}(x)}\,\mathrm{d}x,
$$

Formula 1.18.14:

$$
\int_{a}^{b}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\sum_{n=0}^{\infty}{\left|c_{n}\right|}^{2},
$$

Formula 1.18.15:

$$
f(x)=\lim_{m\to\infty}\sum_{n=0}^{m}c_{n}\phi_{n}(x),
$$

Formula 1.18.16:

$$
\lim_{m\to\infty}\int_{a}^{b}{\left|f(x)-\sum_{n=0}^{m}c_{n}\phi_{n}(x)\right|}^{2}\,\mathrm{d}x=0.
$$

Formula 1.18.17:

$$
f(x)=\sum_{n=0}^{\infty}\left\langle f,\phi_{n}\right\rangle\phi_{n}(x)=\int_{a}^{b}K(x,y)f(y)\,\mathrm{d}y,
$$

Formula 1.18.18:

$$
K(x,y)=\sum_{n=0}^{\infty}\phi_{n}(x)\overline{\phi_{n}(y)}.
$$

Formula 1.18.19:

$$
\delta\left(x-y\right)=\sum_{n=0}^{\infty}\phi_{n}(x)\overline{\phi_{n}(y)},
$$

Formula 1.18.20:

$$
\delta_{n,m}=\int_{a}^{b}\phi_{n}(x)\overline{\phi_{m}(x)}\,\mathrm{d}x.
$$


Definitions and local symbols:
- Defines: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions
- Keywords: Hilbert space , $L^{2}$ , Stieltjes measure , completeness relation , completness relation , discrete spectrum , eigenfunctions , expansion of arbitrary function , inner product , ortho-normality relation
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Defines: $\left\langle f,g\right\rangle$ : inner product over functions
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\left\langle f,g\right\rangle$ : inner product over functions , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $m$ : nonnegative integer , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle f,g\right\rangle$ : inner product over functions , $\int$ : integral , $(a,b)$ : open interval and $n$ : nonnegative integer
- Symbols: $\overline{z}$ : complex conjugate , $(a,b)$ : open interval and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate and $n$ : nonnegative integer
- Symbols: $\delta_{j,k}$ : Kronecker delta , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $m$ : nonnegative integer and $n$ : nonnegative integer

#### 1.18(iii) Linear Operators on a Hilbert Space

Formulas:

Formula 1.18.21:

$$
T(\alpha v+\beta w)=\alpha Tv+\beta Tw,
$$

Formula 1.18.22:

$$
\left\|{T}\right\|\equiv\sup_{v\in V,\left\|{v}\right\|=1}\left\|{Tv}\right\|<\infty.
$$

Formula 1.18.23:

$$
\left\langle Tv,w\right\rangle=\left\langle v,{T}^{*}w\right\rangle.
$$

Formula 1.18.24:

$$
Tu_{\lambda}=\lambda u_{\lambda},
$$

Formula 1.18.25:

$$
T=\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}},
$$

Formula 1.18.26:

$$
\int_{a}^{b}f^{\prime\prime}(x)g(x)\,\mathrm{d}x=\left.f^{\prime}(x)g(x)\right|^{b}_{a}-\left.f(x)g^{\prime}(x)\right|^{b}_{a}+\int_{a}^{b}f(x)g^{\prime\prime}(x)\,\mathrm{d}x.
$$

Formula 1.18.27:

$$
{T}^{*}=T=\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}},
$$


Definitions and local symbols:
- Keywords: Hilbert space , linear operators
- Symbols: $\mathbb{C}$ : complex plane , $\in$ : element of and $w$ : variable
- Symbols: $\in$ : element of , $\equiv$ : equals by definition , $\left\|{\mathbf{A}}\right\|$ : matrix norm , $\sup$ : least upper bound (supremum) and $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Keywords: Hilbert space , formally self-adjoint operators , symmetric operators
- Symbols: ${\mathbf{A}}^{*}$ : adjoint of matrix , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $w$ : variable
- Keywords: Hilbert space , formally self-adjoint differential operators , self-adjoint differential operators , self-adjoint extensions of differential operators
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: ${\mathbf{A}}^{*}$ : adjoint of matrix and $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$

#### 1.18(iv) Formally Self-adjoint Linear Second Order Differential Operators

- Let $X=(a,b)$ be a finite or infinite open interval in $\mathbb{R}$ . Consider on $X$ the linear formally self-adjoint second order differential operator
- with $q(x)$ real and continuous, unless otherwise noted.
- Eigenvalues and eigenfunctions of $T$ , self-adjoint extensions of $\mathcal{L}$ with well defined boundary conditions, and utilization of such eigenfunctions for expansion of wide classes of $L^{2}$ functions, will be the focus of the remainder of this section.
- The special form of ( 1.18.28 ) is especially useful for applications in physics, as the connection to non-relativistic quantum mechanics is immediate: $-\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}$ being proportional to the kinetic energy operator for a single particle in one dimension, $q(x)$ being proportional to the potential energy, often written as $V(x)$ , of that same particle, and which is simply a multiplicative operator. The sum of the kinetic and potential energies give the quantum Hamiltonian , or energy operator; often also referred to as a Schrdinger operator . Other applications follow from the fact that $\mathcal{L}$ is suitable for describing vibrations, especially standing waves, which arise in many parts of engineering and the physical sciences, see Birkhoff and Rota ( 1989 , 10.3 and 10.16) . See  18.39(i) .
- In what follows $T$ will be taken to be a self adjoint extension of $\mathcal{L}$ following the discussion ending the prior sub-section. For $\mathcal{D}(T)$ we can take $C^{2}(X)$ , with appropriate boundary conditions, and with compact support if $X$ is bounded, which space is dense in $L^{2}\left(X\right)$ , and for $X$ unbounded require that possible non- $L^{2}$ eigenfunctions of ( 1.18.28 ), with real eigenvalues, are non-zero but bounded on open intervals, including $\pm\infty$ .
- Stated informally, the spectrum of $T$ is the set of it's eigenvalues, these being real as $T$ is self-adjoint. These sets may be discrete, continuous, or a combination of both, as discussed in the following three subsections. Should an eigenvalue correspond to more than a single linearly independent eigenfunction, namely a multiplicity greater than one, all such eigenfunctions will always be implied as being part of any sums or integrals over the spectrum.

Formulas:

Formula 1.18.28:

$$
\mathcal{L}=-\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}+q(x),
$$


Definitions and local symbols:
- Keywords: Liouville normal form , Schrdinger operator , eigenvalue , formally self adjoint linear operator , linear second order differential operator , multiplicity , set of eigenvalues, taking multiplicities into account , spectrum of a self-adjoint extension of a linear differential operator
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$

#### 1.18(v) Point Spectra and Eigenfunction Expansions

Formulas:

Formula 1.18.29:

$$
\int_{a}^{b}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{m}}(x)}\,\mathrm{d}x=\delta_{n,m},
$$

Formula 1.18.30:

$$
\sum_{n=0}^{\infty}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{n}}(y)}=\delta\left(x-y\right).
$$

Formula 1.18.31:

$$
f(x)=\sum_{n=0}^{\infty}\phi_{\lambda_{n}}(x)\int_{a}^{b}f(y)\overline{\phi_{\lambda_{n}}(y)}\,\mathrm{d}y=\sum_{n=0}^{\infty}\widehat{f}(\lambda_{n})\phi_{\lambda_{n}}(x)
$$

Formula 1.18.32:

$$
\widehat{f}(\lambda_{n})=\left\langle f,\phi_{\lambda_{n}}\right\rangle.
$$

Formula 1.18.33:

$$
\int_{a}^{b}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\sum_{n=0}^{\infty}{\left|\widehat{f}(\lambda_{n})\right|}^{2}.
$$

Formula 1.18.34:

$$
(Tf)(x)=\sum_{n=0}^{\infty}\lambda_{n}\widehat{f}(\lambda_{n})\phi_{\lambda_{n}}(x)=\int_{a}^{b}\left(\sum_{n=0}^{\infty}\lambda_{n}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{n}}(y)}\right)f(y)\,\mathrm{d}y,
$$

Formula 1.18.35:

$$
(F(T)f)(x)=\int_{a}^{b}\left(\sum_{n=0}^{\infty}F(\lambda_{n})\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{n}}(y)}\right)f(y)\,\mathrm{d}y.
$$

Formula 1.18.36:

$$
\phi_{\mathrm{sin}}(n,x)=\sqrt{\frac{2}{\pi}}\sin\left(nx\right),
$$

Formula 1.18.37:

$$
\phi_{\mathrm{cos}}(0,x)=\frac{1}{\sqrt{\pi}},\quad\phi_{\mathrm{cos}}(n,x)=\sqrt{\frac{2}{\pi}}\cos\left(nx\right),
$$

Formula 1.18.38:

$$
\phi_{\mathrm{exp}}(\pm n,x)=\frac{1}{\sqrt{\pi}}{\mathrm{e}}^{\pm 2\mathrm{i}nx},
$$

Formula 1.18.39:

$$
\delta\left(x-y\right)=\frac{1}{\pi}\sum_{n=-\infty}^{\infty}{\mathrm{e}}^{2\mathrm{i}n(x-y)}.
$$

Formula 1.18.40:

$$
f(x)=\frac{1}{\sqrt{\pi}}\sum_{n=-\infty}^{\infty}{\mathrm{e}}^{2\mathrm{i}nx}\widehat{f}(\lambda_{n}),
$$

Formula 1.18.41:

$$
\mathcal{L}^{\mathrm{Hermite}}=-\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}+x^{2},
$$

Formula 1.18.42:

$$
\phi_{n}(x)=\frac{1}{\sqrt{{\pi}^{\frac{1}{2}}2^{n}n!}}{\mathrm{e}}^{-x^{2}/2}H_{n}\left(x\right),
$$

Formula 1.18.43:

$$
f(x)=\sum_{n=0}^{\infty}\int_{-\infty}^{\infty}\frac{{\mathrm{e}}^{-(x^{2}+y^{2})/2}}{{\pi}^{\frac{1}{2}}2^{n}n!}H_{n}\left(x\right)H_{n}\left(y\right)f(y)\,\mathrm{d}y,
$$


Definitions and local symbols:
- Keywords: discrete spectra , eigenfunction expansions , second order differential operators
- Keywords: completeness relation , completness relation , discrete spectrum , eigenfunctions
- Symbols: $\delta_{j,k}$ : Kronecker delta , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate and $n$ : nonnegative integer
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\left\langle f,g\right\rangle$ : inner product over functions and $n$ : nonnegative integer
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $n$ : nonnegative integer
- Keywords: Fourier eigenfunction expansion , discrete spectrum
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $(a,b)$ : open interval , $\sin z$ : sine function and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $(a,b)$ : open interval and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $(a,b)$ : open interval and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $n$ : nonnegative integer
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $n$ : nonnegative integer
- Keywords: Hermite differential operator , eigenfunction expansion
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $\in$ : element of
- Symbols: $H_{n}\left(x\right)$ : Hermite polynomial , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) and $n$ : nonnegative integer
- Symbols: $H_{n}\left(x\right)$ : Hermite polynomial , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) , $\int$ : integral and $n$ : nonnegative integer

#### 1.18(vi) Continuous Spectra and Eigenfunction Expansions: Simple Cases

Formulas:

Formula 1.18.44:

$$
\int_{0}^{\infty}{\phi_{\lambda}}(x)\overline{\phi_{\lambda^{\prime}}(x)}\,\mathrm{d}x=\delta\left(\lambda-\lambda^{\prime}\right),
$$

Formula 1.18.45:

$$
\delta\left(x-y\right)=\int_{0}^{\infty}\phi_{\lambda}(x)\overline{\phi_{\lambda}(y)}\,\mathrm{d}\lambda.
$$

Formula 1.18.46:

$$
f(x)=\int_{0}^{\infty}\phi_{\lambda}(x)\widehat{f}(\lambda)\,\mathrm{d}\lambda,
$$

Formula 1.18.47:

$$
\widehat{f}(\lambda)=\left\langle f,\phi_{\lambda}\right\rangle.
$$

Formula 1.18.48:

$$
\int_{0}^{\infty}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\int_{0}^{\infty}{\left|\widehat{f}(\lambda)\right|}^{2}\,\mathrm{d}\lambda.
$$

Formula 1.18.49:

$$
(Tf)(x)=\int_{0}^{\infty}\left(\int_{0}^{\infty}\lambda\phi_{\lambda}(x)\overline{\phi_{\lambda}(y)}\,\mathrm{d}\lambda\right)f(y)\,\mathrm{d}y,
$$

Formula 1.18.50:

$$
(F(T)f)(x)=\int_{0}^{\infty}\left(\int_{0}^{\infty}F(\lambda)\phi_{\lambda}(x)\overline{\phi_{\lambda}(y)}\,\mathrm{d}\lambda\right)f(y)\,\mathrm{d}y.
$$

Formula 1.18.51:

$$
\left\langle F(T)f,f\right\rangle=\int_{0}^{\infty}F(\lambda){\left|\widehat{f}(\lambda)\right|}^{2}\,\mathrm{d}\lambda.
$$

Formula 1.18.52:

$$
\left\langle\left(z-T\right)^{-1}f,f\right\rangle=\int_{\boldsymbol{\sigma}}{\left|\widehat{f}(\lambda)\right|}^{2}\frac{\,\mathrm{d}\lambda}{z-\lambda},
$$

Formula 1.18.53:

$$
\lim_{\nu\to 0+}\frac{1}{2\pi\mathrm{i}}\left(\left\langle\left(\mu-\mathrm{i}\nu-T\right)^{-1}f,f\right\rangle-\left\langle\left(\mu+\mathrm{i}\nu-T\right)^{-1}f,f\right\rangle\right)
$$

Formula 1.18.54:

$$
\lim_{\epsilon\to 0{+}}\int_{X}\frac{f(y)}{x\pm\mathrm{i}\epsilon-y}\,\mathrm{d}y=P\operatorname{PV}\!\int_{X}\frac{f(y)}{x-y}\,\mathrm{d}y\mp\mathrm{i}\pi f(x).
$$

Formula 1.18.55:

$$
\mathcal{L}^{\mathrm{Bessel}}=-\frac{{\mathrm{d}}^{2}}{{\mathrm{d}x}^{2}}+\frac{\nu^{2}-\frac{1}{4}}{x^{2}},
$$

Formula 1.18.56:

$$
\delta\left(x-y\right)=\int_{0}^{\infty}\sqrt{xt}J_{\nu}\left(xt\right)\sqrt{yt}J_{\nu}\left(yt\right)\,\mathrm{d}t,
$$

Formula 1.18.57:

$$
\lim_{R\to\infty}\int_{0}^{\infty}f(y)\left(\int_{0}^{R}\sqrt{xt}J_{\nu}\left(xt\right)\sqrt{yt}J_{\nu}\left(yt\right)\,\mathrm{d}t\right)\,\mathrm{d}y=\tfrac{1}{2}\left(f(x+)+f(x-)\right),
$$

Formula:

$$
\displaystyle\int_{1}^{\infty}y^{-1}\left|f(y)\right|\,\mathrm{d}y
$$

Formula:

$$
\displaystyle\int_{0}^{1}\left(1+y^{\nu+\frac{1}{2}}\right)\left|f(y)\right|\,\mathrm{d}y
$$

Formula 1.18.59:

$$
f(x)=\frac{1}{\pi}\int_{-\infty}^{\infty}\left(\int_{0}^{\infty}\cos\left(xt\right)\cos\left(yt\right)\,\mathrm{d}t\right)f(y)\,\mathrm{d}y+\frac{1}{\pi}\int_{-\infty}^{\infty}\left(\int_{0}^{\infty}\sin\left(xt\right)\sin\left(yt\right)\,\mathrm{d}t\right)f(y)\,\mathrm{d}y,
$$


Definitions and local symbols:
- Keywords: continuous spectra , eigenfunction expansions , second order differential operators
- Keywords: completeness relation , continuous spectrum , eigenfunctions , ortho-normality relation
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of and $\int$ : integral
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\left\langle f,g\right\rangle$ : inner product over functions
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle f,g\right\rangle$ : inner product over functions , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\left\langle f,g\right\rangle$ : inner product over functions , $\int$ : integral , $\notin$ : not an element of , $z$ : variable and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{i}$ : imaginary unit and $\left\langle f,g\right\rangle$ : inner product over functions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value
- Keywords: Bessel eigenfunction expansion , Hankel transform
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $\in$ : element of
- Symbols: $J_{\nu}\left(z\right)$ : Bessel function of the first kind , $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\Re$ : real part
- Symbols: $J_{\nu}\left(z\right)$ : Bessel function of the first kind , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Keywords: cosine transform , eigenfunction expansion , sine transform
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $\mathbb{R}$ : real line and $\sin z$ : sine function

#### 1.18(vii) Continuous Spectra: More General Cases

- More generally, continuous spectra may occur in sets of disjoint finite intervals $[\lambda_{a},\lambda_{b}]\in(0,\infty)$ , often called bands , when $q(x)$ is periodic , see Ashcroft and Mermin ( 1976 , Ch 8) and Kittel ( 1996 , Ch 7) . Should $q(x)$ be bounded but random , leading to Anderson localization , the spectrum could range from being a dense point spectrum to being singular continuous , see Simon ( 1995 ) , Avron and Simon ( 1982 ) ; a good general reference being Cycon et al. ( 2008 , Ch. 9 and 10) . For example, replacing $2q\cos{(2z)}$ of ( 28.2.1 ) by $\lambda\cos{(2\pi\alpha n+\theta)}$ , $n\in\mathbb{Z}$ gives an almost Mathieu equation which for appropriate $\alpha$ has such properties.

Definitions and local symbols:
- Keywords: Anderson localization , almost Mathiew equation , band spectra , random potentials , second order differential operators , singular continuous spectra

#### 1.18(viii) Mixed Spectra and Eigenfunction Expansions

- In general, operators $T$ being formally self-adjoint second order differential operators of the form ( 1.18.28 ), with $X$ unbounded, will have both a continuous and a point spectrum, and thus, correspondingly, $non-L^{2}\left(X\right)$ eigenfunctions as in  1.18(vi) and $L^{2}\left(X\right)$ eigenfunctions as in  1.18(v) . We assume a continuous spectrum $\lambda\in\boldsymbol{\sigma}_{c}=[0,\infty)$ , and a finite or countably infinite point spectrum $\boldsymbol{\sigma}_{p}$ with elements $\lambda_{n}$ . In what follows, integrals over the continuous parts of the spectrum will be denoted by $\boldsymbol{\sigma}_{c}$ , and sums over the discrete spectrum by $\boldsymbol{\sigma}_{p}$ , with $\boldsymbol{\sigma}=\boldsymbol{\sigma}_{c}\cup\boldsymbol{\sigma}_{p}$ denoting the full spectrum. It is to be noted that if any of the $\lambda\in\boldsymbol{\sigma}$ have degenerate sub-spaces, that is subspaces of orthogonal eigenfunctions with identical eigenvalues, that in the expansions below all such distinct eigenfunctions are to be included. Then orthogonality and normalization relations are
- compare ( 1.18.29 ) and ( 1.18.44 ). The formal completeness relation is now
- compare ( 1.18.30 ) and ( 1.18.45 ), and the eigenfunction expansions are of the form
- Note that the notations of ( 1.18.32 ) and ( 1.18.47 ) are used to distinguish the contributions from the discrete and continuous parts of the spectrum. Then
- The analogs of ( 1.18.49 )-( 1.18.52 ) may be written in a similar fashion each now including contributions from both the discrete and continuous parts of the spectrum, as in ( 1.18.65 ). Showing one, representative, example: the analog of ( 1.18.52 ) is now
- This representation has poles with residues ${\left|\widehat{f}(\lambda_{n})\right|}^{2}$ at the discrete eigenvalues and a branch cut along $[0,\infty)$ with discontinuity, from below to above the cut, $2\pi\mathrm{i}{\left|\widehat{f}(\lambda)\right|}^{2}$ , as in ( 1.18.53 ), see Newton ( 2002 , 7.1.1) .

Formulas:

Formula 1.18.60:

$$
\int_{X}\phi_{\lambda}(x)\overline{\phi_{\lambda^{\prime}}(x)}\,\mathrm{d}x=\delta\left(\lambda-\lambda^{\prime}\right),
$$

Formula 1.18.61:

$$
\int_{X}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{m}}(x)}\,\mathrm{d}x=\delta_{n,m},
$$

Formula 1.18.62:

$$
\int_{X}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda}(x)}\,\mathrm{d}x=0,
$$

Formula 1.18.63:

$$
\delta\left(x-x^{\prime}\right)=\sum_{\boldsymbol{\sigma}_{p}}\phi_{\lambda_{n}}(x)\overline{\phi_{\lambda_{n}}(x^{\prime})}+\int_{\boldsymbol{\sigma}_{c}}\phi_{\lambda}(x)\overline{\phi_{\lambda}(x^{\prime})}\,\mathrm{d}\lambda,
$$

Formula 1.18.64:

$$
f(x)=\int_{\boldsymbol{\sigma}_{c}}\widehat{f}(\lambda)\phi_{\lambda}(x)\,\mathrm{d}\lambda+\sum_{\boldsymbol{\sigma}_{p}}\widehat{f}(\lambda_{n})\phi_{\lambda_{n}}(x),
$$

Formula 1.18.65:

$$
\int_{X}{\left|f(x)\right|}^{2}\,\mathrm{d}x=\int_{\boldsymbol{\sigma}_{c}}{\left|\widehat{f}(\lambda)\right|}^{2}\,\mathrm{d}\lambda+\sum_{\boldsymbol{\sigma}_{p}}{\left|\widehat{f}(\lambda_{n})\right|}^{2},
$$

Formula 1.18.66:

$$
\left\langle\left(z-T\right)^{-1}f,f\right\rangle=\sum_{\boldsymbol{\sigma}_{p}}\frac{{\left|\widehat{f}(\lambda_{n})\right|}^{2}}{z-\lambda_{n}}+\int_{\boldsymbol{\sigma}_{c}}{\left|\widehat{f}(\lambda)\right|}^{2}\frac{\,\mathrm{d}\lambda}{z-\lambda},
$$

Formula 1.18.67:

$$
\mathcal{L}_{\ell}=-\frac{1}{2}\frac{{\mathrm{d}}^{2}}{{\mathrm{d}r}^{2}}+\frac{\ell(\ell+1)}{2r^{2}}+V(r),
$$


Definitions and local symbols:
- Keywords: analytic continuation of matrix elements of the resolvent onto higher Riemann sheets , analytic continuation onto higher Riemann sheets , completeness relation , completness relation , dilatation transformations , eigenfunction expansions , eigenfunctions , matrix elements of the resolvent , mixed spectra , ortho-normality relation
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of and $\int$ : integral
- Symbols: $\delta_{j,k}$ : Kronecker delta , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral and $n$ : nonnegative integer
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $\cap$ : intersection , $C(I)$ or $C(a,b)$ : continuous on an interval $I$ or $(a,b)$ and $n$ : nonnegative integer
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\int$ : integral , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Symbols: $L^{2}\left(X,\mathrm{d}x\right)$ : Lebesgue-Stieltjes measurable, square integrable, complex-valued functions , $\,\mathrm{d}x$ : differential of $x$ , $\in$ : element of , $\left\langle f,g\right\rangle$ : inner product over functions , $\int$ : integral , $\notin$ : not an element of , $z$ : variable , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Keywords: discrete spectra , in one and two dimensions
- Keywords: Schrdinger Operators , Schrdinger-Coulomb problem , mixed spectra
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $\ell$ : integer

#### 1.18(ix) Mathematical Background

Formulas:

Formula 1.18.68:

$$
\mathcal{D}({T}^{*})=\left\{w\in V\,\Big|\,\sup_{v\in\mathcal{D}(T),\left\|{v}\right\|=1}\left|\left\langle Tv,w\right\rangle\right|<\infty\right\},
$$

Formula 1.18.69:

$$
\left\langle Tv,w\right\rangle=\left\langle v,{T}^{*}w\right\rangle,
$$

Formula 1.18.70:

$$
\left\langle Tv,w\right\rangle=\left\langle v,Tw\right\rangle,
$$

Formula 1.18.71:

$$
\mathcal{B}(f)=\lim_{x\to a+}\left(\alpha(x)f(x)+\beta(x)f^{\prime}(x)\right),
$$


Definitions and local symbols:
- Keywords: essentially self-adjoint operator , mathematical background , range and domain , self-adjoint operator
- Symbols: ${\mathbf{A}}^{*}$ : adjoint of matrix , $\in$ : element of , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors , $\sup$ : least upper bound (supremum) , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $w$ : variable and $\left|x\right|$ : absolute value of $x$
- Symbols: ${\mathbf{A}}^{*}$ : adjoint of matrix , $\in$ : element of , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $w$ : variable
- Symbols: $\in$ : element of , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $w$ : variable
- Keywords: mathematical background , spectrum of an operator
- Keywords: deficiency indices , mathematical background , self-adjoint extensions of a symmetric operator
- Keywords: boundary conditions , boundary conditions and the Weyl alternative , limit circle , limit point , limit point and limit circle boundary conditions , mathematical background , second order linear differential operator
- Symbols: ${\mathbf{A}}^{*}$ : adjoint of matrix and $\in$ : element of

#### 1.18(x) Literature

- The materials developed here follow from the extensions of the Sturm-Liouville theory of second order ODEs as developed by Weyl, to include the limit point and limit circle singular cases. This work is well overviewed by Coddington and Levinson ( 1955 , Ch. 9) , and then applied in detail by Titchmarsh ( 1946 ) , Titchmarsh ( 1962a ) , Titchmarsh ( 1958 ) , and Levitan and Sargsjan ( 1975 ) which also connects the Weyl theory to the relevant functional analysis. In parallel, similar, and more general formulations have grown out of functional analysis itself, as in the work of Stone ( 1990 ) , Rudin ( 1973 ) , Reed and Simon ( 1980 ) , Reed and Simon ( 1975 ) , Reed and Simon ( 1978 ) , Reed and Simon ( 1979 ) , Cycon et al. ( 2008 ) , Dunford and Schwartz ( 1988 , Ch. XIII) , Hall ( 2013 , pp. 127-223) . Friedman ( 1990 ) provides a useful introduction to both approaches; as does the conference proceeding Amrein et al. ( 2005 ) , overviewing the combination of Sturm-Liouville theory and Hilbert space theory. See, in particular, the overview Everitt ( 2005b , pp. 45-74) , and the uniformly annotated listing of $51$ solved Sturm-Liouville problems in Everitt ( 2005a , pp. 272-331) , each with their limit point, or circle, boundary behaviors categorized.

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.18](https://dlmf.nist.gov/1.18)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: differential operators, eigenfunction expansions, linear, second order, Hilbert, Hilbert space, expansion of arbitrary vector, inner product,  2 space, space, L 2, Stieltjes measure, completeness relation, completness relation, discrete spectrum, eigenfunctions, expansion of arbitrary function, ortho-normality relation, linear operators, formally self-adjoint operators, symmetric operators, formally self-adjoint differential operators, self-adjoint differential operators, self-adjoint extensions of differential operators, Liouville normal form, Schrdinger operator, eigenvalue, formally self adjoint linear operator, linear second order differential operator, multiplicity, set of eigenvalues, taking multiplicities into account, spectrum of a self-adjoint extension of a linear differential operator, discrete spectra, second order differential operators, Fourier eigenfunction expansion, Hermite differential operator, eigenfunction expansion, continuous spectra, continuous spectrum, Bessel eigenfunction expansion.

### Source Notes

- See https://www.physicsoverflow.org/27488/physical-interpretation-application-residual-spectrum-operator for a sketch of proof that the residual spectrum of a selfadjoint operator is empty.
- See Dunford and Schwartz ( 1988 , XII.1.4) .
- See Dunford and Schwartz ( 1988 , XII.1.1) for the spectrum of an operator.
- For self-adjoint extensions of a symmetric operator see Dunford and Schwartz ( 1988 , XII.4.1-19) .
- For the Weyl alternative see Dunford and Schwartz ( 1988 , p. 1306) .
