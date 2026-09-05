# §3.4 Differentiation

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.4, `Differentiation`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Equally-Spaced Nodes
- Analytic Functions
- Partial Derivatives

### Subsections

#### 3.4(i) Equally-Spaced Nodes

- The Lagrange $(n+1)$ -point formula is
- and follows from the differentiated form of ( 3.3.4 ). The $B_{k}^{n}$ are the differentiated Lagrangian interpolation coefficients :
- where $A_{k}^{n}$ is as in ( 3.3.10 ).
- If $f^{(n+2)}(x)$ is continuous on the interval $I$ defined in  3.3(i) , then the remainder in ( 3.4.1 ) is given by
- where $\xi_{0}$ and $\xi_{1}\in I$ .
- For the values of $n_{0}$ and $n_{1}$ used in the formulas below

Formulas:

Formula 3.4.1:

$$
hf^{\prime}_{t}=hf^{\prime}(x_{0}+th)=\sum_{k=n_{0}}^{n_{1}}B_{k}^{n}f_{k}+hR^{\prime}_{n,t},
$$

Formula 3.4.2:

$$
B_{k}^{n}=\ifrac{\mathrm{d}A_{k}^{n}}{\mathrm{d}t},
$$

Formula 3.4.3:

$$
hR^{\prime}_{n,t}=\frac{h^{n+1}}{(n+1)!}\left(f^{(n+1)}(\xi_{0})\frac{\mathrm{d}}{\mathrm{d}t}\prod_{k=n_{0}}^{n_{1}}(t-k)+f^{(n+2)}(\xi_{1})\prod_{k=n_{0}}^{n_{1}}(t-k)\right),
$$

Formula 3.4.4:

$$
h\left|R^{\prime}_{n,t}\right|\leq h^{n+1}\left(c_{n}\left|f^{(n+2)}(\xi_{1})\right|+\frac{1}{n+1}\left|f^{(n+1)}(\xi_{0})\right|\right),
$$

Formula 3.4.5:

$$
hf^{\prime}_{t}=-f_{0}+f_{1}+hR^{\prime}_{1,t},
$$

Formula 3.4.6:

$$
hf^{\prime}_{t}=-\tfrac{1}{2}(1-2t)f_{-1}-2tf_{0}+\tfrac{1}{2}(1+2t)f_{1}+hR^{\prime}_{2,t},
$$

Formula 3.4.7:

$$
hf^{\prime}_{t}=\sum_{k=-1}^{2}B_{k}^{3}f_{k}+hR^{\prime}_{3,t},
$$

Formula:

$$
\displaystyle B_{-1}^{3}
$$

Formula:

$$
\displaystyle B_{0}^{3}
$$

Formula:

$$
\displaystyle B_{1}^{3}
$$

Formula:

$$
\displaystyle B_{2}^{3}
$$

Formula 3.4.9:

$$
hf^{\prime}_{t}=\sum_{k=-2}^{2}B_{k}^{4}f_{k}+hR^{\prime}_{4,t},
$$

Formula:

$$
\displaystyle B_{-2}^{4}
$$

Formula:

$$
\displaystyle B_{-1}^{4}
$$

Formula:

$$
\displaystyle B_{0}^{4}
$$

Formula:

$$
\displaystyle B_{1}^{4}
$$

Formula:

$$
\displaystyle B_{2}^{4}
$$

Formula 3.4.11:

$$
hf^{\prime}_{t}=\sum_{k=-2}^{3}B_{k}^{5}f_{k}+hR^{\prime}_{5,t},
$$

Formula:

$$
\displaystyle B_{-2}^{5}
$$

Formula:

$$
\displaystyle B_{-1}^{5}
$$

Formula:

$$
\displaystyle B_{0}^{5}
$$

Formula:

$$
\displaystyle B_{1}^{5}
$$

Formula:

$$
\displaystyle B_{2}^{5}
$$

Formula:

$$
\displaystyle B_{3}^{5}
$$

Formula 3.4.13:

$$
hf^{\prime}_{t}=\sum_{k=-3}^{3}B_{k}^{6}f_{k}+hR^{\prime}_{6,t},
$$

Formula:

$$
\displaystyle B_{-3}^{6}
$$

Formula:

$$
\displaystyle B_{-2}^{6}
$$

Formula:

$$
\displaystyle B_{-1}^{6}
$$

Formula:

$$
\displaystyle B_{0}^{6}
$$

Formula:

$$
\displaystyle B_{1}^{6}
$$

Formula:

$$
\displaystyle B_{2}^{6}
$$

Formula:

$$
\displaystyle B_{3}^{6}
$$

Formula 3.4.15:

$$
hf^{\prime}_{t}=\sum_{k=-3}^{4}B_{k}^{7}f_{k}+hR^{\prime}_{7,t},
$$

Formula:

$$
\displaystyle B_{-3}^{7}
$$

Formula:

$$
\displaystyle B_{-2}^{7}
$$

Formula:

$$
\displaystyle B_{-1}^{7}
$$

Formula:

$$
\displaystyle B_{0}^{7}
$$

Formula:

$$
\displaystyle B_{1}^{7}
$$

Formula:

$$
\displaystyle B_{2}^{7}
$$

Formula:

$$
\displaystyle B_{3}^{7}
$$

Formula:

$$
\displaystyle B_{4}^{7}
$$


Definitions and local symbols:
- Keywords: Lagrange's formula for equally-spaced nodes , differentiation , numerical
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Defines: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients (locally)
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ and $A_{k}^{n}$ : Lagrangian interpolation coefficients
- Defines: $R^{\prime}_{n,t}(x)$ : remainder (locally)
- Symbols: $\frac{\mathrm{d}\NVar{f}}{\mathrm{d}\NVar{x}}$ : derivative of $f$ with respect to $x$ and $!$ : factorial (as in $n!$ )
- Symbols: $c_{n}$ : bound coefficient and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients
- Keywords: Lagrange's formula for equally-spaced nodes , differentiation , numerical
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients and $R^{\prime}_{n,t}(x)$ : remainder
- Symbols: $B_{k}^{n}$ : differentiated Lagrangian interpolation coefficients

#### 3.4(ii) Analytic Functions

- If $f$ can be extended analytically into the complex plane, then from Cauchy's integral formula ( 1.9(iii) )
- where $C$ is a simple closed contour described in the positive rotational sense such that $C$ and its interior lie in the domain of analyticity of $f$ , and $x_{0}$ is interior to $C$ . Taking $C$ to be a circle of radius $r$ centered at $x_{0}$ , we obtain
- The integral on the right-hand side can be approximated by the composite trapezoidal rule ( 3.5.2 ).

Formulas:

Formula 3.4.17:

$$
\frac{1}{k!}\,f^{(k)}(x_{0})=\frac{1}{2\pi i}\int_{C}\frac{f(\zeta)}{(\zeta-x_{0})^{k+1}}\,\,\mathrm{d}\zeta,
$$

Formula 3.4.18:

$$
\frac{1}{k!}\,f^{(k)}(x_{0})=\frac{1}{2\pi r^{k}}\int_{0}^{2\pi}f(x_{0}+re^{i\theta})e^{-ik\theta}\,\mathrm{d}\theta.
$$

Formula 3.4.19:

$$
\frac{1}{k!}=\frac{1}{2\pi r^{k}}\int_{0}^{2\pi}e^{r\cos\theta}\cos\left(r\sin\theta-k\theta\right)\,\mathrm{d}\theta.
$$


Definitions and local symbols:
- Keywords: analytic functions , differentiation , numerical
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $!$ : factorial (as in $n!$ ) , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $C$ : simple closed contour
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $r$ : radius
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos\NVar{z}$ : cosine function , $\,\mathrm{d}\NVar{x}$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) , $\int$ : integral , $\sin\NVar{z}$ : sine function and $r$ : radius

#### 3.4(iii) Partial Derivatives

Formulas:

Formula 3.4.20:

$$
\frac{\partial u_{0,0}}{\partial x}=\frac{1}{2h}\,(u_{1,0}-u_{-1,0})+O\left(h^{2}\right),
$$

Formula 3.4.21:

$$
\frac{\partial u_{0,0}}{\partial x}=\frac{1}{4h}\,(u_{1,1}-u_{-1,1}+u_{1,-1}-u_{-1,-1})+O\left(h^{2}\right).
$$

Formula 3.4.22:

$$
\frac{{\partial}^{2}u_{0,0}}{{\partial x}^{2}}=\frac{1}{h^{2}}\,(u_{1,0}-2u_{0,0}+u_{-1,0})+O\left(h^{2}\right),
$$

Formula 3.4.23:

$$
\frac{{\partial}^{2}u_{0,0}}{{\partial x}^{2}}=\frac{1}{12h^{2}}\,(-u_{2,0}+16u_{1,0}-30u_{0,0}+16u_{-1,0}-u_{-2,0})+O\left(h^{4}\right),
$$

Formula 3.4.24:

$$
\frac{{\partial}^{2}u_{0,0}}{{\partial x}^{2}}=\frac{1}{3h^{2}}\,(u_{1,1}-2u_{0,1}+u_{-1,1}+u_{1,0}-2u_{0,0}+u_{-1,0}+u_{1,-1}-2u_{0,-1}+u_{-1,-1})+O\left(h^{2}\right).
$$

Formula 3.4.25:

$$
\frac{\,{\partial}^{2}u_{0,0}}{\,\partial x\,\partial y}=\frac{1}{4h^{2}}\,(u_{1,1}-u_{1,-1}-u_{-1,1}+u_{-1,-1})+O\left(h^{2}\right),
$$

Formula 3.4.26:

$$
\frac{\,{\partial}^{2}u_{0,0}}{\,\partial x\,\partial y}=-\frac{1}{2h^{2}}\,(u_{1,0}+u_{-1,0}+u_{0,1}+u_{0,-1}-2u_{0,0}-u_{1,1}-u_{-1,-1})+O\left(h^{2}\right).
$$

Formula 3.4.27:

$$
\displaystyle\nabla^{2}u
$$

Formula 3.4.28:

$$
\displaystyle\nabla^{2}u_{0,0}
$$

Formula 3.4.29:

$$
\nabla^{2}u_{0,0}=\frac{1}{12h^{2}}\left(-60u_{0,0}+16(u_{1,0}+u_{0,1}+u_{-1,0}+u_{0,-1})-(u_{2,0}+u_{0,2}+u_{-2,0}+u_{0,-2})\right)+O\left(h^{4}\right).
$$

Formula 3.4.30:

$$
\displaystyle\frac{{\partial}^{4}u_{0,0}}{{\partial x}^{4}}
$$

Formula 3.4.31:

$$
\displaystyle\frac{\,{\partial}^{4}u_{0,0}}{\,{\partial}^{2}x\,{\partial}^{2}y}
$$

Formula 3.4.32:

$$
\nabla^{4}u=\frac{{\partial}^{4}u}{{\partial x}^{4}}+2\frac{\,{\partial}^{4}u}{\,{\partial}^{2}x\,{\partial}^{2}y}+\frac{{\partial}^{4}u}{{\partial y}^{4}}\,.
$$

Formula 3.4.33:

$$
\nabla^{4}u_{0,0}=\frac{1}{h^{4}}\,(20u_{0,0}-8(u_{1,0}+u_{0,1}+u_{-1,0}+u_{0,-1})+2(u_{1,1}+u_{1,-1}+u_{-1,1}+u_{-1,-1})+(u_{0,2}+u_{2,0}+u_{-2,0}+u_{0,-2}))+O\left(h^{2}\right),
$$

Formula 3.4.34:

$$
\nabla^{4}u_{0,0}=\frac{1}{6h^{4}}\,(184u_{0,0}-(u_{0,3}+u_{0,-3}+u_{3,0}+u_{-3,0})+14(u_{0,2}+u_{0,-2}+u_{2,0}+u_{-2,0})-77(u_{0,1}+u_{0,-1}+u_{1,0}+u_{-1,0})+20(u_{1,1}+u_{1,-1}+u_{-1,1}+u_{-1,-1})-(u_{1,2}+u_{2,1}+u_{1,-2}+u_{2,-1}+u_{-1,2}+u_{-2,1}+u_{-1,-2}+u_{-2,-1}))+O\left(h^{4}\right).
$$


Definitions and local symbols:
- Keywords: differentiation , numerical , partial derivatives
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Keywords: Laplacian , numerical approximations
- Symbols: $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Keywords: biharmonic operator , differentiation , numerical , numerical approximation , partial derivatives
- Symbols: $\frac{\partial\NVar{f}}{\partial\NVar{x}}$ : partial derivative of $f$ with respect to $x$ , $\,\partial\NVar{x}$ : partial differential of $x$ and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $u$ : function
- Symbols: $O\left(\NVar{x}\right)$ : order not exceeding and $u$ : function

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.4](https://dlmf.nist.gov/3.4)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: Lagrange's formula for equally-spaced nodes, differentiation, numerical, analytic functions, partial derivatives, Laplacian, numerical approximations, biharmonic operator, numerical approximation.

### Source Notes

- See Hildebrand ( 1974 , pp. 85-89) . The coefficients $B_{k}^{n}$ are obtained by differentiation of the $A_{k}^{n}$ ; compare ( 3.4.2 ).
