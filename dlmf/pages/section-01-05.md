# §1.5 Calculus of Two or More Variables

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.5, `Calculus of Two or More Variables`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Partial Derivatives
- Coordinate Systems
- Taylor's Theorem; Maxima and Minima
- Leibniz's Theorem for Differentiation of Integrals
- Multiple Integrals
- Jacobians and Change of Variables

### Subsections

#### 1.5(i) Partial Derivatives

- A function $f(x,y)$ is continuous at a point $(a,b)$ if
- that is, for every arbitrarily small positive constant $\epsilon$ there exists $\delta$ ( $>0$ ) such that
- for all $\alpha$ and $\beta$ that satisfy $\left|\alpha\right|,\left|\beta\right|<\delta$ .
- A function is continuous on a point set $D$ if it is continuous at all points of $D$ . A function $f(x,y)$ is piecewise continuous on $I_{1}\times I_{2}$ , where $I_{1}$ and $I_{2}$ are intervals, if it is piecewise continuous in $x$ for each $y\in I_{2}$ and piecewise continuous in $y$ for each $x\in I_{1}$ .
- The function $f(x,y)$ is continuously differentiable if $f$ , $\frac{\partial f}{\partial x}$ , and $\frac{\partial f}{\partial y}$ are continuous, and twice-continuously differentiable if also $\frac{{\partial}^{2}f}{{\partial x}^{2}}$ , $\frac{{\partial}^{2}f}{{\partial y}^{2}}$ , $\,{\partial}^{2}f/\,\partial x\,\partial y$ , and $\,{\partial}^{2}f/\,\partial y\,\partial x$ are continuous. In the latter event

Formulas:

Formula 1.5.1:

$$
\lim_{(x,y)\to(a,b)}f(x,y)=f(a,b),
$$

Formula 1.5.2:

$$
\left|f(a+\alpha,b+\beta)-f(a,b)\right|<\epsilon,
$$

Formula 1.5.3:

$$
\displaystyle\frac{\partial f}{\partial x}
$$

Formula 1.5.4:

$$
\displaystyle\frac{\partial f}{\partial y}
$$

Formula:

$$
\displaystyle\frac{\,{\partial}^{2}f}{\,\partial x\,\partial y}
$$

Formula:

$$
\displaystyle\frac{\,{\partial}^{2}f}{\,\partial y\,\partial x}
$$

Formula 1.5.6:

$$
\frac{\,{\partial}^{2}f}{\,\partial x\,\partial y}=\frac{\,{\partial}^{2}f}{\,\partial y\,\partial x}.
$$

Formula 1.5.7:

$$
\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}f(x(t),y(t))
$$

Formula 1.5.8:

$$
\displaystyle\frac{\partial}{\partial u}f(x(u,v),y(u,v))
$$

Formula 1.5.9:

$$
\displaystyle\frac{\partial}{\partial v}f(x(u,v),y(u,v),z(u,v))
$$


Definitions and local symbols:
- Keywords: at a point , continuous function , continuously differentiable , definition , derivatives , differentiation , functions , limits of functions , notation , of two variables , on a point set , partial , partial derivative , partial differentiation , piecewise
- Symbols: $(a,b)$ : open interval
- Symbols: $\left|x\right|$ : absolute value of $x$
- Defines: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ and $D_{x}$ : differential operator (locally)
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ and $D_{x}$ : differential operator
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $\,\partial x$ : partial differential of $x$
- Keywords: chain rule , derivatives , for derivatives
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Keywords: implicit function theorem , neighborhood

#### 1.5(ii) Coordinate Systems

Formulas:

Formula:

$$
\displaystyle x
$$

Formula:

$$
\displaystyle y
$$

Formula 1.5.11:

$$
\displaystyle\frac{\partial}{\partial x}
$$

Formula 1.5.12:

$$
\displaystyle\frac{\partial}{\partial y}
$$

Formula 1.5.13:

$$
\nabla^{2}f=\frac{{\partial}^{2}f}{{\partial x}^{2}}+\frac{{\partial}^{2}f}{{\partial y}^{2}}=\frac{{\partial}^{2}f}{{\partial r}^{2}}+\frac{1}{r}\frac{\partial f}{\partial r}+\frac{1}{r^{2}}\frac{{\partial}^{2}f}{{\partial\phi}^{2}}.
$$

Formula:

$$
\displaystyle z
$$

Formula 1.5.15:

$$
\nabla^{2}f=\frac{{\partial}^{2}f}{{\partial x}^{2}}+\frac{{\partial}^{2}f}{{\partial y}^{2}}+\frac{{\partial}^{2}f}{{\partial z}^{2}}=\frac{{\partial}^{2}f}{{\partial r}^{2}}+\frac{1}{r}\frac{\partial f}{\partial r}+\frac{1}{r^{2}}\frac{{\partial}^{2}f}{{\partial\phi}^{2}}+\frac{{\partial}^{2}f}{{\partial z}^{2}}.
$$

Formula 1.5.17:

$$
\nabla^{2}f=\frac{{\partial}^{2}f}{{\partial x}^{2}}+\frac{{\partial}^{2}f}{{\partial y}^{2}}+\frac{{\partial}^{2}f}{{\partial z}^{2}}={\frac{1}{\rho^{2}}\frac{\partial}{\partial\rho}\left(\rho^{2}\frac{\partial f}{\partial\rho}\right)+\frac{1}{\rho^{2}{\sin}^{2}\theta}\frac{{\partial}^{2}f}{{\partial\phi}^{2}}}+\frac{1}{\rho^{2}\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial f}{\partial\theta}\right).
$$


Definitions and local symbols:
- Keywords: Laplacian , coordinate systems , plane polar coordinates , polar , polar coordinates
- Symbols: $\cos z$ : cosine function , $\sin z$ : sine function , $\phi$ : longitude and $r$ : radius
- Symbols: $\cos z$ : cosine function , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\sin z$ : sine function , $\phi$ : longitude and $r$ : radius
- Symbols: $\cos z$ : cosine function , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\sin z$ : sine function , $\phi$ : longitude and $r$ : radius
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\phi$ : longitude and $r$ : radius
- Keywords: Laplacian , coordinate systems , cylindrical , cylindrical coordinates , cylindrical polar coordinates
- Symbols: $\cos z$ : cosine function , $\sin z$ : sine function , $z$ : variable , $\phi$ : longitude and $r$ : radius
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $z$ : variable , $\phi$ : longitude and $r$ : radius
- Keywords: Laplacian , coordinate systems , spherical (or spherical polar) , spherical coordinates , spherical polar coordinates
- Symbols: $\cos z$ : cosine function , $\sin z$ : sine function , $z$ : variable , $\phi$ : longitude , $\rho$ : radius and $\theta$ : azimuth
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\sin z$ : sine function , $z$ : variable , $\phi$ : longitude , $\rho$ : radius and $\theta$ : azimuth

#### 1.5(iii) Taylor's Theorem; Maxima and Minima

- If $f$ is $n+1$ times continuously differentiable, then
- where $f$ and its partial derivatives on the right-hand side are evaluated at $(a,b)$ , and $R_{n}/(\lambda^{2}+\mu^{2})^{n/2}\to 0$ as $(\lambda,\mu)\to(0,0)$ .
- $f(x,y)$ has a local minimum ( maximum ) at $(a,b)$ if
- and the second order term in ( 1.5.18 ) is positive definite (negative definite) , that is,
- and

Formulas:

Formula 1.5.18:

$$
f(a+\lambda,b+\mu)=f+\left(\lambda\frac{\partial}{\partial x}+\mu\frac{\partial}{\partial y}\right)f+\dots+\frac{1}{n!}\left(\lambda\frac{\partial}{\partial x}+\mu\frac{\partial}{\partial y}\right)^{n}f+R_{n},
$$

Formula 1.5.19:

$$
\frac{\partial f}{\partial x}=\frac{\partial f}{\partial y}=0\quad\mathrm{at}\,(a,b),
$$

Formula 1.5.20:

$$
\frac{{\partial}^{2}f}{{\partial x}^{2}}>0\quad(<0)\quad\mathrm{at}\,(a,b),
$$

Formula 1.5.21:

$$
\frac{{\partial}^{2}f}{{\partial x}^{2}}\frac{{\partial}^{2}f}{{\partial y}^{2}}-\left(\frac{\,{\partial}^{2}f}{\,\partial x\,\partial y}\right)^{2}>0\quad\mathrm{at}\,(a,b).
$$


Definitions and local symbols:
- Keywords: Taylor series , Taylor's theorem , local , maximum , minimum , negative definite , positive definite , two variables
- Symbols: $!$ : factorial (as in $n!$ ) , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $n$ : nonnegative integer and $R_{n}$ : remainder
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$

#### 1.5(iv) Leibniz's Theorem for Differentiation of Integrals

Formulas:

Formula 1.5.22:

$$
\frac{\mathrm{d}}{\mathrm{d}x}\int^{\beta(x)}_{\alpha(x)}f(x,y)\,\mathrm{d}y={f(x,\beta(x))\beta^{\prime}(x)-f(x,\alpha(x))\alpha^{\prime}(x)}+\int^{\beta(x)}_{\alpha(x)}\frac{\partial f}{\partial x}\,\mathrm{d}y.
$$

Formula 1.5.23:

$$
\left|\int_{c_{1}}^{d}(\frac{\partial f}{\partial x})\,\mathrm{d}y\right|<\epsilon,
$$

Formula 1.5.24:

$$
\frac{\mathrm{d}}{\mathrm{d}x}\int^{d}_{c}f(x,y)\,\mathrm{d}y=\int^{d}_{c}\frac{\partial f}{\partial x}\,\mathrm{d}y,
$$


Definitions and local symbols:
- Keywords: differentiation , integrals , of integrals
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Keywords: convergence , differentiation , integrals , of integrals , uniform
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\epsilon$ : positive number and $\left|x\right|$ : absolute value of $x$
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$

#### 1.5(v) Multiple Integrals

Formulas:

Formula 1.5.25:

$$
\displaystyle a
$$

Formula 1.5.26:

$$
\displaystyle c
$$

Formula 1.5.27:

$$
\iint_{R}f(x,y)\,\mathrm{d}A={\lim\sum_{j,k}f(\xi_{j},\eta_{k})(x_{j+1}-x_{j})(y_{k+1}-y_{k})}
$$

Formula 1.5.28:

$$
f^{*}(x,y)=\begin{cases}f(x,y),&\mathrm{if}\,(x,y)\in D,\\ 0,&\mathrm{if}\,(x,y)\in R\setminus D.\end{cases}
$$

Formula 1.5.29:

$$
\iint_{D}f(x,y)\,\mathrm{d}A=\iint_{R}f^{*}(x,y)\,\mathrm{d}A,
$$

Formula:

$$
\displaystyle a
$$

Formula:

$$
\displaystyle\phi_{1}(x)
$$

Formula 1.5.31:

$$
\iint_{D}f(x,y)\,\mathrm{d}A=\int^{b}_{a}\int^{\phi_{2}(x)}_{\phi_{1}(x)}f(x,y)\,\mathrm{d}y\,\mathrm{d}x,
$$

Formula 1.5.32:

$$
\int^{b}_{a}\left(\int^{\phi_{2}(x)}_{\phi_{1}(x)}f(x,y)\,\mathrm{d}y\right)\,\mathrm{d}x.
$$

Formula:

$$
\displaystyle c
$$

Formula:

$$
\displaystyle\psi_{1}(y)
$$

Formula 1.5.34:

$$
\iint_{D}f(x,y)\,\mathrm{d}A=\int^{d}_{c}\int^{\psi_{2}(y)}_{\psi_{1}(y)}f(x,y)\,\mathrm{d}x\,\mathrm{d}y.
$$

Formula 1.5.35:

$$
\int^{b}_{a}\int^{\phi_{2}(x)}_{\phi_{1}(x)}f(x,y)\,\mathrm{d}y\,\mathrm{d}x=\int^{d}_{c}\int^{\psi_{2}(y)}_{\psi_{1}(y)}f(x,y)\,\mathrm{d}x\,\mathrm{d}y.
$$

Formula 1.5.36:

$$
\int^{b}_{a}\int^{d}_{c}f(x,y)\,\mathrm{d}y\,\mathrm{d}x=\int^{d}_{c}\int^{b}_{a}f(x,y)\,\mathrm{d}x\,\mathrm{d}y,
$$

Formula:

$$
\displaystyle\psi_{1}(x,y)
$$


Definitions and local symbols:
- Keywords: double , double integrals , integrals , multiple
- Symbols: $n$ : nonnegative integer
- Symbols: $m$ : nonnegative integer
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $j$ : integer , $k$ : integer and $R$ : closed rectangle
- Symbols: $\in$ : element of , $(a,b)$ : open interval , $\setminus$ : set subtraction , $R$ : closed rectangle and $D$ : region contained in $R$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $R$ : closed rectangle and $D$ : region contained in $R$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $D$ : region contained in $R$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $D$ : region contained in $R$
- Keywords: change of order of integration , double integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: double integrals , infinite , integrals
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: triple integrals
- Symbols: $z$ : variable

#### 1.5(vi) Jacobians and Change of Variables

Formulas:

Formula 1.5.38:

$$
\displaystyle\frac{\partial(f,g)}{\partial(x,y)}
$$

Formula 1.5.39:

$$
\displaystyle\frac{\partial(x,y)}{\partial(r,\phi)}
$$

Formula 1.5.40:

$$
\displaystyle\frac{\partial(f,g,h)}{\partial(x,y,z)}
$$

Formula 1.5.41:

$$
\displaystyle\frac{\partial(x,y,z)}{\partial(\rho,\theta,\phi)}
$$

Formula 1.5.42:

$$
\iint_{D}f(x,y)\,\mathrm{d}x\,\mathrm{d}y=\iint_{D^{*}}f(x(u,v),y(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,\mathrm{d}u\,\mathrm{d}v,
$$

Formula 1.5.43:

$$
\iiint_{D}f(x,y,z)\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z=\iiint_{D^{*}}f(x(u,v,w),y(u,v,w),z(u,v,w))\,\left|\frac{\partial(x,y,z)}{\partial(u,v,w)}\right|\,\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w.
$$


Definitions and local symbols:
- Keywords: Jacobian , derivatives
- Symbols: $\det$ : determinant , $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $r$ : radius and $\phi$ : angle
- Symbols: $\det$ : determinant , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ and $\,\partial x$ : partial differential of $x$
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\sin z$ : sine function , $\phi$ : longitude , $\rho$ : radius and $\theta$ : azimuth
- Keywords: calculus , change of variables , double integrals , two or more variables
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $w$ : variable and $\left|x\right|$ : absolute value of $x$

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.5](https://dlmf.nist.gov/1.5)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: calculus, two or more variables, at a point, continuous function, continuously differentiable, definition, derivatives, differentiation, functions, limits of functions, notation, of two variables, on a point set, partial, partial derivative, partial differentiation, piecewise, chain rule, for derivatives, implicit function theorem, neighborhood, Laplacian, coordinate systems, plane polar coordinates, polar, polar coordinates, cylindrical, cylindrical coordinates, cylindrical polar coordinates, spherical (or spherical polar), spherical coordinates, spherical polar coordinates, Taylor series, Taylor's theorem, local, maximum, minimum, negative definite, positive definite, two variables.

### Source Notes

- See Marsden and Tromba ( 1996 , Chapters 2, 3) .
- See Davis and Snider ( 1987 , Chapter 5) .
- See Marsden and Tromba ( 1996 , Chapter 3) .
- See Protter and Morrey ( 1991 , pp. 288, 298) .
- See Marsden and Tromba ( 1996 , Chapters 5, 6) . For ( 1.5.36 ) see Love ( 1970 , 1972a ) .
- See Marsden and Tromba ( 1996 , pp. 358-371) .
