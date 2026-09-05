# §1.6 Vectors and Vector-Valued Functions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.6, `Vectors and Vector-Valued Functions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Vectors
- Vectors: Alternative Notations
- Vector-Valued Functions
- Path and Line Integrals
- Surfaces and Integrals over Surfaces

### Subsections

#### 1.6(i) Vectors

Formulas:

Formula:

$$
\displaystyle\mathbf{a}
$$

Formula:

$$
\displaystyle\mathbf{b}
$$

Formula 1.6.2:

$$
\mathbf{a}\cdot\mathbf{b}=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}.
$$

Formula 1.6.3:

$$
\left\|{\mathbf{a}}\right\|=\sqrt{\mathbf{a}\cdot\mathbf{a}},
$$

Formula 1.6.4:

$$
\cos\theta=\frac{\mathbf{a}\cdot\mathbf{b}}{\left\|{\mathbf{a}}\right\|\;\left\|{\mathbf{b}}\right\|};
$$

Formula:

$$
\displaystyle\mathbf{i}
$$

Formula:

$$
\displaystyle\mathbf{j}
$$

Formula:

$$
\displaystyle\mathbf{k}
$$

Formula 1.6.6:

$$
\mathbf{a}=a_{1}\mathbf{i}+a_{2}\mathbf{j}+a_{3}\mathbf{k}.
$$

Formula:

$$
\displaystyle\mathbf{i}\times\mathbf{j}
$$

Formula:

$$
\displaystyle\mathbf{j}\times\mathbf{k}
$$

Formula:

$$
\displaystyle\mathbf{k}\times\mathbf{i}
$$

Formula:

$$
\displaystyle\mathbf{j}\times\mathbf{i}
$$

Formula:

$$
\displaystyle\mathbf{k}\times\mathbf{j}
$$

Formula:

$$
\displaystyle\mathbf{i}\times\mathbf{k}
$$

Formula 1.6.9:

$$
\mathbf{a}\times\mathbf{b}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ a_{1}&a_{2}&a_{3}\\ b_{1}&b_{2}&b_{3}\end{vmatrix}\\ =(a_{2}b_{3}-a_{3}b_{2})\mathbf{i}+(a_{3}b_{1}-a_{1}b_{3})\mathbf{j}+(a_{1}b_{2}-a_{2}b_{1})\mathbf{k}\\ =\left\|{\mathbf{a}}\right\|\left\|{\mathbf{b}}\right\|(\sin\theta)\mathbf{n},
$$

Formula 1.6.10:

$$
\displaystyle\mathbf{a}\times(\mathbf{b}\times\mathbf{c})
$$

Formula 1.6.11:

$$
\displaystyle(\mathbf{a}\times\mathbf{b})\times\mathbf{c}
$$


Definitions and local symbols:
- Keywords: dot product , scalar product , vectors
- Keywords: angle , magnitude , vectors
- Symbols: $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Symbols: $\cos z$ : cosine function , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) and $\theta$ : angle between $\mathbf{a}$ and $\mathbf{b}$
- Keywords: unit , vectors
- Defines: $\mathbf{i}$ : unit vector (locally) , $\mathbf{j}$ : unit vector (locally) and $\mathbf{k}$ : unit vector (locally)
- Symbols: $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Keywords: area , cross product , parallelepiped , parallelogram , right-hand rule , right-hand rule for cross products , vector product , vectors , volume
- Symbols: $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Symbols: $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Symbols: $\det$ : determinant , $\sin z$ : sine function , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $\theta$ : angle between $\mathbf{a}$ and $\mathbf{b}$ , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector

#### 1.6(ii) Vectors: Alternative Notations

- The following notations are often used in the physics literature; see for example Lorentz et al. ( 1923 , pp. 122-123) .

Formulas:

Formula 1.6.12:

$$
a_{j}b_{j}=\sum_{j=1}^{3}a_{j}b_{j}=\mathbf{a}\cdot\mathbf{b}.
$$

Formula:

$$
\displaystyle\mathbf{e}_{1}
$$

Formula:

$$
\displaystyle\mathbf{e}_{2}
$$

Formula:

$$
\displaystyle\mathbf{e}_{3}
$$

Formula 1.6.14:

$$
\epsilon_{jk\ell}=\begin{cases}+1,&\mathrm{if}j,k,\ellis\,even\,permutation\,\mathrm{of}1,2,3,\\ -1,&\mathrm{if}j,k,\ellis\,odd\,permutation\,\mathrm{of}1,2,3,\\ \phantom{-}0,&\mathrm{otherwise}.\end{cases}
$$

Formula:

$$
\displaystyle\epsilon_{123}
$$

Formula:

$$
\displaystyle\epsilon_{213}
$$

Formula:

$$
\displaystyle\epsilon_{221}
$$

Formula 1.6.16:

$$
\epsilon_{jk\ell}\epsilon_{\ell mn}=\delta_{j,m}\delta_{k,n}-\delta_{j,n}\delta_{k,m},
$$

Formula 1.6.17:

$$
\mathbf{e}_{j}\times\mathbf{e}_{k}=\epsilon_{jk\ell}\mathbf{e}_{\ell};
$$

Formula 1.6.18:

$$
a_{j}\mathbf{e}_{j}\times b_{k}\mathbf{e}_{k}=\epsilon_{jk\ell}a_{j}b_{k}\mathbf{e}_{\ell};
$$


Definitions and local symbols:
- Keywords: notations , vectors
- Keywords: Einstein summation convention , Einstein summation convention for vectors , vectors
- Symbols: $j$ : integer
- Defines: $\mathbf{e}_{j}$ : unit vectors (locally)
- Symbols: $j$ : integer
- Keywords: Levi-Civita symbol , Levi-Civita symbol for vectors , vectors
- Defines: $\epsilon_{j k \ell}$ : Levi-Civita symbol
- Symbols: $j$ : integer and $k$ : integer
- Keywords: Einstein summation convention , Einstein summation convention for vectors , parallelepiped , vectors , volume
- Symbols: $\epsilon_{j k \ell}$ : Levi-Civita symbol
- Symbols: $\delta_{j,k}$ : Kronecker delta , $\epsilon_{j k \ell}$ : Levi-Civita symbol , $j$ : integer , $k$ : integer , $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $\epsilon_{j k \ell}$ : Levi-Civita symbol , $j$ : integer , $k$ : integer and $\mathbf{e}_{j}$ : unit vectors
- Symbols: $\epsilon_{j k \ell}$ : Levi-Civita symbol , $j$ : integer , $k$ : integer and $\mathbf{e}_{j}$ : unit vectors

#### 1.6(iii) Vector-Valued Functions

Formulas:

Formula 1.6.19:

$$
\nabla=\mathbf{i}\frac{\partial}{\partial x}+\mathbf{j}\frac{\partial}{\partial y}+\mathbf{k}\frac{\partial}{\partial z}.
$$

Formula 1.6.20:

$$
\operatorname{grad}f=\nabla f=\frac{\partial f}{\partial x}\mathbf{i}+\frac{\partial f}{\partial y}\mathbf{j}+\frac{\partial f}{\partial z}\mathbf{k}.
$$

Formula 1.6.21:

$$
\operatorname{div}\mathbf{F}=\nabla\cdot\mathbf{F}=\frac{\partial F_{1}}{\partial x}+\frac{\partial F_{2}}{\partial y}+\frac{\partial F_{3}}{\partial z}.
$$

Formula 1.6.22:

$$
\operatorname{curl}\mathbf{F}=\nabla\times\mathbf{F}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ \displaystyle{\frac{\partial}{\partial x}}&\displaystyle{\frac{\partial}{\partial y}}&\displaystyle{\frac{\partial}{\partial z}}\\ F_{1}&F_{2}&F_{3}\end{vmatrix}\\ =\left(\frac{\partial F_{3}}{\partial y}-\frac{\partial F_{2}}{\partial z}\right)\mathbf{i}+\left(\frac{\partial F_{1}}{\partial z}-\frac{\partial F_{3}}{\partial x}\right)\mathbf{j}+\left(\frac{\partial F_{2}}{\partial x}-\frac{\partial F_{1}}{\partial y}\right)\mathbf{k}.
$$

Formula 1.6.23:

$$
\nabla(fg)=f\nabla g+g\nabla f,
$$

Formula 1.6.24:

$$
\nabla(f/g)=(g\nabla f-f\nabla g)/g^{2},
$$

Formula 1.6.25:

$$
\nabla\cdot(f\mathbf{F})=f(\nabla\cdot\mathbf{F})+\mathbf{F}\cdot\nabla f,
$$

Formula 1.6.26:

$$
\nabla\cdot(\mathbf{F}\times\mathbf{G})=\mathbf{G}\cdot(\nabla\times\mathbf{F})-\mathbf{F}\cdot(\nabla\times\mathbf{G}),
$$

Formula 1.6.27:

$$
\nabla\cdot(\nabla\times\mathbf{F})=\operatorname{div}\operatorname{curl}\mathbf{F}=0,
$$

Formula 1.6.28:

$$
\nabla\times(f\mathbf{F})=f(\nabla\times\mathbf{F})+(\nabla f)\times\mathbf{F},
$$

Formula 1.6.29:

$$
\nabla\times(\nabla f)=\operatorname{curl}\operatorname{grad}f=0,
$$

Formula 1.6.30:

$$
\nabla^{2}f=\nabla\cdot(\nabla f),
$$

Formula 1.6.31:

$$
\nabla^{2}(fg)=f\nabla^{2}g+g\nabla^{2}f+2(\nabla f\cdot\nabla g),
$$

Formula 1.6.32:

$$
\nabla\cdot(\nabla f\times\nabla g)=0,
$$

Formula 1.6.33:

$$
\nabla\cdot(f\nabla g-g\nabla f)=f\nabla^{2}g-g\nabla^{2}f,
$$

Formula 1.6.34:

$$
\nabla\times(\nabla\times\mathbf{F})=\operatorname{curl}\operatorname{curl}\mathbf{F}=\nabla(\nabla\cdot\mathbf{F})-\nabla^{2}\mathbf{F}.
$$


Definitions and local symbols:
- Keywords: functions , vector-valued
- Keywords: curl , del operator , divergence , gradient , vector-valued functions
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $z$ : variable , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Defines: $\operatorname{grad}$ : gradient of differentiable scalar function
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $z$ : variable , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Defines: $\operatorname{div}$ : divergence of vector-valued function
- Symbols: $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $z$ : variable and $F_{j}$ : vector function components
- Defines: $\operatorname{curl}$ : of vector-valued function
- Symbols: $\det$ : determinant , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $z$ : variable , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector , $\mathbf{k}$ : unit vector and $F_{j}$ : vector function components
- Symbols: $\operatorname{curl}$ : of vector-valued function and $\operatorname{div}$ : divergence of vector-valued function
- Symbols: $\operatorname{curl}$ : of vector-valued function and $\operatorname{grad}$ : gradient of differentiable scalar function
- Symbols: $\operatorname{curl}$ : of vector-valued function

#### 1.6(iv) Path and Line Integrals

- Note: The terminology open and closed sets and boundary points in the $(x,y)$ plane that is used in this subsection and  1.6(v) is analogous to that introduced for the complex plane in  1.9(ii) .
- A path is defined by $\mathbf{c}(t)=(x(t),y(t),z(t))$ , with $t$ ranging over an interval and $x(t),y(t),z(t)$ differentiable. Letting
- then the length of a path for $a\leq t\leq b$ is
- The path integral of a continuous function $f(x,y,z)$ is
- The line integral of a vector-valued function $\mathbf{F}=F_{1}\mathbf{i}+F_{2}\mathbf{j}+F_{3}\mathbf{k}$ along $\mathbf{c}$ is given by
- A path $\mathbf{c}_{1}(t)$ , $t\in[a,b]$ , is a reparametrization of $\mathbf{c}(t^{\prime})$ , $t^{\prime}\in[a^{\prime},b^{\prime}]$ , if $\mathbf{c}_{1}(t)=\mathbf{c}(t^{\prime})$ and $t^{\prime}=h(t)$ with $h(t)$ differentiable and monotonic. If $h(a)=a^{\prime}$ and $h(b)=b^{\prime}$ , then the reparametrization is called orientation-preserving , and

Formulas:

Formula 1.6.35:

$$
\mathbf{c}^{\prime}(t)=(x^{\prime}(t),y^{\prime}(t),z^{\prime}(t)),
$$

Formula 1.6.36:

$$
\int_{a}^{b}\left\|{\mathbf{c}^{\prime}(t)}\right\|\,\mathrm{d}t.
$$

Formula 1.6.37:

$$
\int_{\mathbf{c}}f\,\mathrm{d}s=\int^{b}_{a}f(x(t),y(t),z(t))\left\|{\mathbf{c}^{\prime}(t)}\right\|\,\mathrm{d}t.
$$

Formula 1.6.38:

$$
\int_{\mathbf{c}}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}=\int^{b}_{a}\mathbf{F}(\mathbf{c}(t))\cdot\mathbf{c}^{\prime}(t)\,\mathrm{d}t=\int^{b}_{a}\left(F_{1}\frac{\mathrm{d}x}{\mathrm{d}t}+F_{2}\frac{\mathrm{d}y}{\mathrm{d}t}+F_{3}\frac{\mathrm{d}z}{\mathrm{d}t}\right)\,\mathrm{d}t=\int_{\mathbf{c}}F_{1}\,\mathrm{d}x+F_{2}\,\mathrm{d}y+F_{3}\,\mathrm{d}z.
$$

Formula 1.6.39:

$$
\int_{\mathbf{c}}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}=\int_{\mathbf{c}_{1}}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}.
$$

Formula 1.6.40:

$$
\int_{\mathbf{c}}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}=-\int_{\mathbf{c}_{1}}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}.
$$

Formula 1.6.41:

$$
\int_{\mathbf{c}}f\,\mathrm{d}s=\int_{\mathbf{c}_{1}}f\,\mathrm{d}s,
$$

Formula 1.6.42:

$$
\int_{\mathbf{c}}\nabla f\cdot\,\mathrm{d}\mathbf{s}=f(\mathbf{c}(b))-f(\mathbf{c}(a)),
$$

Formula 1.6.43:

$$
\mathbf{F}(x,y)=F_{1}(x,y)\mathbf{i}+F_{2}(x,y)\mathbf{j}
$$

Formula 1.6.44:

$$
\iint_{S}\left(\frac{\partial F_{2}}{\partial x}-\frac{\partial F_{1}}{\partial y}\right)\,\mathrm{d}A=\int_{C}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s}=\int_{C}F_{1}\,\mathrm{d}x+F_{2}\,\mathrm{d}y.
$$


Definitions and local symbols:
- Keywords: boundary points , closed point set , curve , integrals , integrals of vector-valued functions , length , line , line integral , open point set , orientation-preserving , orientation-reversing , path , path integral , piecewise differentiable , piecewise differentiable curve , reparametrization of integration paths , simple closed , simple closed curve , vector-valued functions
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Symbols: $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\mathbf{F}(x,y)$ : vector and $F_{j}$ : vector function components
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\mathbf{F}(x,y)$ : vector
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $\mathbf{F}(x,y)$ : vector
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Green's theorem , Green's theorem for vector-valued functions , functions , two dimensions , vector-valued , vector-valued functions
- Defines: $\mathbf{F}(x,y)$ : vector (locally)
- Symbols: $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $F_{j}$ : vector function components
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\mathbf{F}(x,y)$ : vector , $S$ : closed region , $C$ : closed curve and $F_{j}$ : vector function components

#### 1.6(v) Surfaces and Integrals over Surfaces

- A parametrized surface $S$ is defined by
- with $(u,v)\in D$ , an open set in the plane.
- For $x$ , $y$ , and $z$ continuously differentiable, the vectors
- and
- are tangent to the surface at $\boldsymbol{{\Phi}}(u_{0},v_{0})$ . The surface is smooth at this point if $\mathbf{T}_{u}\times\mathbf{T}_{v}\not=0$ . A surface is smooth if it is smooth at every point. The vector $\mathbf{T}_{u}\times\mathbf{T}_{v}$ at $(u_{0},v_{0})$ is normal to the surface at $\boldsymbol{{\Phi}}(u_{0},v_{0})$ .
- The area $A(S)$ of a parametrized smooth surface is given by

Formulas:

Formula 1.6.45:

$$
\boldsymbol{{\Phi}}(u,v)=(x(u,v),y(u,v),z(u,v))
$$

Formula 1.6.46:

$$
\mathbf{T}_{u}=\frac{\partial x}{\partial u}(u_{0},v_{0})\mathbf{i}+\frac{\partial y}{\partial u}(u_{0},v_{0})\mathbf{j}+\frac{\partial z}{\partial u}(u_{0},v_{0})\mathbf{k}
$$

Formula 1.6.47:

$$
\mathbf{T}_{v}=\frac{\partial x}{\partial v}(u_{0},v_{0})\mathbf{i}+\frac{\partial y}{\partial v}(u_{0},v_{0})\mathbf{j}+\frac{\partial z}{\partial v}(u_{0},v_{0})\mathbf{k}
$$

Formula 1.6.48:

$$
A(S)=\iint_{D}\left\|{\mathbf{T}_{u}\times\mathbf{T}_{v}}\right\|\,\mathrm{d}u\,\mathrm{d}v,
$$

Formula 1.6.49:

$$
\left\|{\mathbf{T}_{u}\times\mathbf{T}_{v}}\right\|=\sqrt{\left(\frac{\partial(x,y)}{\partial(u,v)}\right)^{2}+\left(\frac{\partial(y,z)}{\partial(u,v)}\right)^{2}+\left(\frac{\partial(x,z)}{\partial(u,v)}\right)^{2}}.
$$

Formula 1.6.50:

$$
\left\|{\mathbf{T}_{\theta}\times\mathbf{T}_{\phi}}\right\|=\rho^{2}\left|\sin\theta\right|.
$$

Formula 1.6.51:

$$
A(S)=\iint_{D}\sqrt{1+\left(\frac{\partial f}{\partial x}\right)^{2}+\left(\frac{\partial f}{\partial y}\right)^{2}}\,\mathrm{d}A.
$$

Formula 1.6.52:

$$
A(S)=2\pi\int^{b}_{a}\left|f(x)\right|\sqrt{1+(f^{\prime}(x))^{2}}\,\mathrm{d}x,
$$

Formula 1.6.53:

$$
A(S)=2\pi\int^{b}_{a}\left|x\right|\sqrt{1+(f^{\prime}(x))^{2}}\,\mathrm{d}x.
$$

Formula 1.6.54:

$$
\iint_{S}f(x,y,z)\,\mathrm{d}S=\iint_{D}f(\boldsymbol{{\Phi}}(u,v))\left\|{\mathbf{T}_{u}\times\mathbf{T}_{v}}\right\|\,\mathrm{d}u\,\mathrm{d}v.
$$

Formula 1.6.55:

$$
\iint_{S}\mathbf{F}\cdot\,\mathrm{d}\mathbf{S}=\iint_{D}\mathbf{F}\cdot(\mathbf{T}_{u}\times\mathbf{T}_{v})\,\mathrm{d}u\,\mathrm{d}v,
$$

Formula 1.6.56:

$$
\iint_{\boldsymbol{{\Phi}}_{1}(D_{1})}\mathbf{F}\cdot\,\mathrm{d}\mathbf{S}=\iint_{\boldsymbol{{\Phi}}_{2}(D_{2})}\mathbf{F}\cdot\,\mathrm{d}\mathbf{S};
$$

Formula 1.6.57:

$$
\iint_{S}(\nabla\times\mathbf{F})\cdot\,\mathrm{d}\mathbf{S}=\int_{\,\partial S}\mathbf{F}\cdot\,\mathrm{d}\mathbf{s},
$$

Formula 1.6.58:

$$
\iiint_{V}(\nabla\cdot\mathbf{F})\,\mathrm{d}V=\iint_{S}\mathbf{F}\cdot\,\mathrm{d}\mathbf{S},
$$

Formula 1.6.59:

$$
\iiint_{V}(f\nabla^{2}g+\nabla f\cdot\nabla g)\,\mathrm{d}V=\iint_{S}f\frac{\partial g}{\partial n}\,\mathrm{d}A,
$$

Formula 1.6.60:

$$
\iiint_{V}(f\nabla^{2}g-g\nabla^{2}f)\,\mathrm{d}V=\iint_{S}\left(f\frac{\partial g}{\partial n}-g\frac{\partial f}{\partial n}\right)\,\mathrm{d}A,
$$


Definitions and local symbols:
- Keywords: area , integral over , integrals , of revolution , orientation , over parametrized surface , parametrized surfaces , smooth , sphere , surface , tangent vector
- Defines: $\boldsymbol{{\Phi}}(x,y,z)$ : parameterization (locally)
- Symbols: $(a,b)$ : open interval
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $\mathbf{i}$ : unit vector , $\mathbf{j}$ : unit vector and $\mathbf{k}$ : unit vector
- Defines: $A(S)$ : area of a parameterized smooth surface $S$ (locally)
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $S$ : parameterized surface and $D$ : open set in the plane
- Symbols: $(a,b)$ : open interval , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ and $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ )
- Symbols: $\sin z$ : sine function , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $\rho$ : radius , $\theta$ : angle , $\phi$ : angle and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $S$ : parameterized surface , $D$ : open set in the plane and $A(S)$ : area of a parameterized smooth surface $S$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $S$ : parameterized surface , $A(S)$ : area of a parameterized smooth surface $S$ and $\left|x\right|$ : absolute value of $x$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $S$ : parameterized surface , $A(S)$ : area of a parameterized smooth surface $S$ and $\left|x\right|$ : absolute value of $x$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\|{\mathbf{v}}\right\|$ : vector norm ( $l$ ) , $S$ : parameterized surface , $\boldsymbol{{\Phi}}(x,y,z)$ : parameterization and $D$ : open set in the plane
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $S$ : parameterized surface and $D$ : open set in the plane
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\boldsymbol{{\Phi}}(x,y,z)$ : parameterization and $D$ : open set in the plane
- Keywords: Stokes' theorem , Stokes' theorem for vector-valued functions , vector-valued functions
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\,\partial x$ : partial differential of $x$ and $S$ : parameterized surface
- Keywords: Gauss's theorem for vector-valued functions , divergence (or Gauss's) theorem , divergence theorem , vector-valued functions
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $S$ : parameterized surface and $V$ : closed region
- Keywords: Green's theorem , Green's theorem for vector-valued functions , three dimensions , vector-valued functions

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.6](https://dlmf.nist.gov/1.6)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: notations, vector-valued functions, vectors, dot product, scalar product, angle, magnitude, unit, area, cross product, parallelepiped, parallelogram, right-hand rule, right-hand rule for cross products, vector product, volume, Einstein summation convention, Einstein summation convention for vectors, Levi-Civita symbol, Levi-Civita symbol for vectors, functions, vector-valued, curl, del operator, divergence, gradient, boundary points, closed point set, curve, integrals, integrals of vector-valued functions, length, line, line integral, open point set, orientation-preserving, orientation-reversing, path, path integral, piecewise differentiable.

### Source Notes

- See Marsden and Tromba ( 1996 , Chapter 1) . For ( 1.6.9 ) see Hubbard and Hubbard ( 2002 , pp. 82-84) .
- See Marsden and Tromba ( 1996 , pp. 144-147, 273-283) .
- See Marsden and Tromba ( 1996 , pp. 396-417, 470) .
- See Marsden and Tromba ( 1996 , pp. 421-459, 485, 506) .
