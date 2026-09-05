# §1.16 Distributions

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.16, `Distributions`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Test Functions
- Derivatives of a Distribution
- Dirac Delta Distribution
- Heaviside Function
- Tempered Distributions
- Distributions of Several Variables
- Fourier Transforms of Tempered Distributions
- Fourier Transforms of Special Distributions
- References for Section 1.16

### Subsections

#### 1.16(i) Test Functions

- Let $\phi$ be a function defined on an open interval $I=(a,b)$ , which can be infinite. The closure of the set of points where $\phi\not=0$ is called the support of $\phi$ . If the support of $\phi$ is a compact set ( 1.9(vii) ), then $\phi$ is called a function of compact support . A test function is an infinitely differentiable function of compact support.
- A sequence $\{\phi_{n}\}$ of test functions converges to a test function $\phi$ if the support of every $\phi_{n}$ is contained in a fixed compact set $K$ and as $n\to\infty$ the sequence $\{\phi_{n}^{(k)}\}$ converges uniformly on $K$ to $\phi^{(k)}$ for $k=0,1,2,\dots$ .
- The linear space of all test functions with the above definition of convergence is called a test function space . We denote it by $\mathcal{D}(I)$ .
- A mapping $\Lambda:\mathcal{D}(I)\rightarrow\mathbb{C}$ is a linear functional if
- where $\alpha_{1}$ and $\alpha_{2}$ are real or complex constants. $\Lambda:\mathcal{D}(I)\rightarrow\mathbb{C}$ is called a distribution , or generalized function , if it is a continuous linear functional on $\mathcal{D}(I)$ , that is, it is a linear functional and for every $\phi_{n}\to\phi$ in $\mathcal{D}(I)$ ,
- From here on we write $\left\langle\Lambda,\phi\right\rangle$ for $\Lambda(\phi)$ . The space of all distributions will be denoted by $\mathcal{D}^{*}(I)$ . A distribution $\Lambda$ is called regular if there is a locally integrable function $f$ on $I$ (i.e., a function $f$ on $I$ which is absolutely Lebesgue integrable on every compact subset of $I$ ) such that

Formulas:

Formula 1.16.1:

$$
\Lambda(\alpha_{1}\phi_{1}+\alpha_{2}\phi_{2})=\alpha_{1}\Lambda(\phi_{1})+\alpha_{2}\Lambda(\phi_{2}),
$$

Formula 1.16.2:

$$
\lim_{n\to\infty}\Lambda(\phi_{n})=\Lambda(\phi).
$$

Formula 1.16.3:

$$
\left\langle\Lambda,\phi\right\rangle=\int_{I}f(x)\phi(x)\,\mathrm{d}x.
$$

Formula 1.16.3_5:

$$
\left\langle\mu_{\alpha},\phi\right\rangle=\int_{I}\phi(x)\,\mathrm{d}\alpha(x).
$$

Formula 1.16.4:

$$
\left\langle\Lambda_{1}+\Lambda_{2},\phi\right\rangle=\left\langle\Lambda_{1},\phi\right\rangle+\left\langle\Lambda_{2},\phi\right\rangle,
$$

Formula 1.16.5:

$$
\left\langle c\Lambda,\phi\right\rangle=c\left\langle\Lambda,\phi\right\rangle=\left\langle\Lambda,c\phi\right\rangle,
$$

Formula 1.16.6:

$$
\left\langle\alpha\Lambda,\phi\right\rangle=\left\langle\Lambda,\alpha\phi\right\rangle.
$$

Formula 1.16.7:

$$
\lim_{n\to\infty}\left\langle\Lambda_{n},\phi\right\rangle=\left\langle\Lambda,\phi\right\rangle
$$


Definitions and local symbols:
- Defines: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function
- Keywords: convergence , definition , distribution , distributions , functions , generalized function , linear functional , linear functionals , of a function , of compact support , regular , singular , support , support of , test function space , test functions
- Symbols: $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $n$ : nonnegative integer , $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\int$ : integral , $\phi(x)$ : test function , $I$ : interval and $\Lambda$ : mapping
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\int$ : integral , $\phi(x)$ : test function and $I$ : interval
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $n$ : nonnegative integer , $\phi(x)$ : test function and $\Lambda$ : mapping

#### 1.16(ii) Derivatives of a Distribution

- The derivative $\Lambda^{\prime}$ of a distribution is defined by
- Similarly
- If $f$ is a locally integrable function then its distributional derivative is $Df=\Lambda^{\prime}_{f}$ . In the situation of ( 1.16.3_5 ) we have
- If the measure $\mu_{\alpha}$ is absolutely continuous with density $w$ (see  1.4(v) ) then $D\alpha=\Lambda_{w}$ .

Formulas:

Formula 1.16.8:

$$
\left\langle\Lambda^{\prime},\phi\right\rangle=-\left\langle\Lambda,\phi^{\prime}\right\rangle,
$$

Formula 1.16.9:

$$
\left\langle\Lambda^{(k)},\phi\right\rangle=(-1)^{k}\left\langle\Lambda,\phi^{(k)}\right\rangle,
$$

Formula 1.16.9_5:

$$
\mu_{\alpha}=D\alpha.
$$


Definitions and local symbols:
- Keywords: derivatives , distributional , distributional derivative , distributions , of distribution
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $\phi(x)$ : test function , $I$ : interval , $\mathcal{D}(I)$ : test function space and $\Lambda$ : mapping
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $k$ : integer , $\phi(x)$ : test function and $\Lambda$ : mapping
- Symbols: $Df$ : distributional derivative

#### 1.16(iii) Dirac Delta Distribution

- The Dirac delta distribution is singular. See also  1.17(i) .

Formulas:

Formula 1.16.10:

$$
\displaystyle\left\langle\delta,\phi\right\rangle
$$

Formula 1.16.11:

$$
\displaystyle\left\langle\delta_{x_{0}},\phi\right\rangle
$$

Formula 1.16.12:

$$
\displaystyle\left\langle{\delta_{x_{0}}}^{(n)},\phi\right\rangle
$$


Definitions and local symbols:
- Defines: $\delta_{x}$ : Dirac delta distribution
- Keywords: Dirac delta distribution , distributions
- Symbols: $\delta_{x}$ : Dirac delta distribution , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $\phi(x)$ : test function , $I$ : interval and $\mathcal{D}(I)$ : test function space
- Symbols: $\delta_{x}$ : Dirac delta distribution , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $\phi(x)$ : test function , $I$ : interval and $\mathcal{D}(I)$ : test function space
- Symbols: $\delta_{x}$ : Dirac delta distribution , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $n$ : nonnegative integer , $\phi(x)$ : test function , $I$ : interval and $\mathcal{D}(I)$ : test function space

#### 1.16(iv) Heaviside Function

- Since $\delta_{x_{0}}$ is the Lebesgue-Stieltjes measure $\mu_{\alpha}$ corresponding to $\alpha(x)=H\left(x-x_{0}\right)$ (see  1.4(v) ), formula ( 1.16.16 ) is a special case of ( 1.16.3_5 ), ( 1.16.9_5 ) for that choice of $\alpha$ .
- Suppose $f(x)$ is infinitely differentiable except at $x_{0}$ , where left and right derivatives of all orders exist, and
- Then
- For $\alpha>-1$ ,
- For $\alpha>0$ ,
- For $\alpha<-1$ and $\alpha$ not an integer, define

Formulas:

Formula 1.16.13:

$$
\displaystyle H\left(x\right)
$$

Formula 1.16.14:

$$
\displaystyle H\left(x-x_{0}\right)
$$

Formula 1.16.15:

$$
\displaystyle D\!H
$$

Formula 1.16.16:

$$
\displaystyle D\!H\left(x-x_{0}\right)
$$

Formula 1.16.17:

$$
\sigma_{n}=f^{(n)}(x_{0}+)-f^{(n)}(x_{0}-).
$$

Formula 1.16.18:

$$
D^{m}f=f^{(m)}+\sigma_{0}{\delta_{x_{0}}}^{(m-1)}+\sigma_{1}{\delta_{x_{0}}}^{(m-2)}+\dots+\sigma_{m-1}\delta_{x_{0}},
$$

Formula 1.16.19:

$$
x^{\alpha}_{+}=x^{\alpha}H\left(x\right)=\begin{cases}x^{\alpha},&x>0,\\ 0,&x\leq 0.\end{cases}
$$

Formula 1.16.20:

$$
Dx^{\alpha}_{+}=\alpha x_{+}^{\alpha-1}.
$$

Formula 1.16.21:

$$
x^{\alpha}_{+}=\frac{1}{(\alpha+1)_{n}}D^{n}x_{+}^{\alpha+n},
$$

Formula 1.16.22:

$$
\ln_{+}x=H\left(x\right)\ln x=\begin{cases}\ln x,&x>0,\\ 0,&x\leq 0,\end{cases}
$$

Formula 1.16.23:

$$
(-1)^{n}n!x_{+}^{-1-n}=D^{(n+1)}\ln_{+}x,
$$


Definitions and local symbols:
- Keywords: Heaviside function , derivative , distributions
- Defines: $H\left(x\right)$ : Heaviside function
- Symbols: $H\left(x\right)$ : Heaviside function
- Symbols: $H\left(x\right)$ : Heaviside function , $\delta_{x}$ : Dirac delta distribution and $Df$ : distributional derivative
- Symbols: $H\left(x\right)$ : Heaviside function , $\delta_{x}$ : Dirac delta distribution and $Df$ : distributional derivative
- Symbols: $n$ : nonnegative integer
- Symbols: $\delta_{x}$ : Dirac delta distribution , $m$ : nonnegative integer and $Df$ : distributional derivative
- Symbols: $H\left(x\right)$ : Heaviside function
- Symbols: $Df$ : distributional derivative
- Symbols: $n$ : nonnegative integer and $Df$ : distributional derivative
- Symbols: $H\left(x\right)$ : Heaviside function and $\ln z$ : principal branch of logarithm function
- Symbols: $!$ : factorial (as in $n!$ ) , $\ln z$ : principal branch of logarithm function , $n$ : nonnegative integer and $Df$ : distributional derivative

#### 1.16(v) Tempered Distributions

- The space $\mathcal{T}(\mathbb{R})$ of test functions for tempered distributions consists of all infinitely-differentiable functions such that the function and all its derivatives are $O\left({\left|x\right|}^{-N}\right)$ as $\left|x\right|\to\infty$ for all $N$ .
- A sequence $\{\phi_{n}\}$ of functions in $\mathcal{T}$ is said to converge to a function $\phi\in\mathcal{T}$ as $n\to\infty$ if the sequence $\{\phi_{n}^{(k)}\}$ converges uniformly to $\phi^{(k)}$ on every finite interval and if the constants $c_{k,N}$ in the inequalities
- do not depend on $n$ .
- A tempered distribution is a continuous linear functional $\Lambda$ on $\mathcal{T}$ . (See the definition of a distribution in  1.16(i) .) The set of tempered distributions is denoted by $\mathcal{T}^{*}$ .
- A sequence of tempered distributions $\Lambda_{n}$ converges to $\Lambda$ in $\mathcal{T}^{*}$ if
- for all $\phi\in\mathcal{T}$ .

Formulas:

Formula 1.16.24:

$$
\left|x^{N}\phi_{n}^{(k)}\right|\leq c_{k,N}
$$

Formula 1.16.25:

$$
\lim_{n\to\infty}\left\langle\Lambda_{n},\phi\right\rangle=\left\langle\Lambda,\phi\right\rangle,
$$


Definitions and local symbols:
- Keywords: convergence , distributions , tempered , tempered distributions , test function space , test functions
- Symbols: $k$ : integer , $n$ : nonnegative integer , $\phi(x)$ : test function and $\left|x\right|$ : absolute value of $x$
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $n$ : nonnegative integer , $\Lambda$ : mapping and $\phi(x)$ : test function

#### 1.16(vi) Distributions of Several Variables

- Let $\mathcal{D}({\mathbb{R}}^{n})=\mathcal{D}_{n}$ be the set of all infinitely differentiable functions in $n$ variables, $\phi(x_{1},x_{2},\dots,x_{n})$ , with compact support in ${\mathbb{R}}^{n}$ . If $k=(k_{1},\dots,k_{n})$ is a multi-index and $x=(x_{1},\dots,x_{n})\in{\mathbb{R}}^{n}$ , then we write $x^{k}=x_{1}^{k_{1}}\cdots x_{n}^{k_{n}}$ and $\phi^{(k)}(x)=\,{\partial}^{k}\phi/(\,\partial x_{1}^{k_{1}}\cdots\,\partial x_{n}^{k_{n}})$ . A sequence $\{\phi_{m}\}$ of functions in $\mathcal{D}_{n}$ converges to a function $\phi\in\mathcal{D}_{n}$ if the supports of $\phi_{m}$ lie in a fixed compact subset $K$ of ${\mathbb{R}}^{n}$ and $\phi_{m}^{(k)}$ converges uniformly to $\phi^{(k)}$ in $K$ for every multi-index $k=(k_{1},k_{2},\dots,k_{n})$ . A distribution in ${\mathbb{R}}^{n}$ is a continuous linear functional on $\mathcal{D}_{n}$ .
- The partial derivatives of distributions in ${\mathbb{R}}^{n}$ can be defined as in  1.16(ii) . A locally integrable function $f(x)=f(x_{1},x_{2},\dots,x_{n})$ gives rise to a distribution $\Lambda_{f}$ defined by
- The distributional derivative $D^{k}f$ of $f$ is defined by
- where $k$ is a multi-index and $\left|k\right|=k_{1}+k_{2}+\dots+k_{n}$ .
- For tempered distributions the space of test functions $\mathcal{T}_{n}$ is the set of all infinitely-differentiable functions $\phi$ of $n$ variables that satisfy
- Here $m=(m_{1},m_{2},\dots,m_{n})$ and $k=(k_{1},k_{2},\dots,k_{n})$ are multi-indices, and $c_{m,k}$ are constants. Tempered distributions are continuous linear functionals on this space of test functions. The space of tempered distributions is denoted by $\mathcal{T}^{*}_{n}$ .

Formulas:

Formula 1.16.26:

$$
\left\langle\Lambda_{f},\phi\right\rangle=\int_{{\mathbb{R}}^{n}}f(x)\phi(x)\,\mathrm{d}x,
$$

Formula 1.16.27:

$$
\left\langle D^{k}f,\phi\right\rangle=(-1)^{\left|k\right|}\int_{{\mathbb{R}}^{n}}f(x)\phi^{(k)}(x)\,\mathrm{d}x,
$$

Formula 1.16.28:

$$
\left|x^{m}\phi^{(k)}(x)\right|\leq c_{m,k},
$$


Definitions and local symbols:
- Keywords: distributions , several variables , tempered distributions
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $\int$ : integral , $\mathbb{R}$ : real line , $n$ : nonnegative integer , $\mathcal{D}_{n}$ : space of test functions , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function and $\Lambda$ : mapping
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $\int$ : integral , $\mathbb{R}$ : real line , $k$ : integer , $n$ : nonnegative integer , $\mathcal{D}_{n}$ : space of test functions , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function , $Df$ : distributional derivative and $\left|x\right|$ : absolute value of $x$
- Symbols: $\in$ : element of , $\mathbb{R}$ : real line , $k$ : integer , $m$ : nonnegative integer , $n$ : nonnegative integer , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function and $\left|x\right|$ : absolute value of $x$

#### 1.16(vii) Fourier Transforms of Tempered Distributions

- Suppose $\phi$ is a test function in $\mathcal{T}_{n}$ . Then its Fourier transform is
- where $\mathbf{x}=(x_{1},x_{2},\dots,x_{n})$ and $\mathbf{x}\cdot\mathbf{t}=x_{1}t_{1}+\dots+x_{n}t_{n}$ . $\mathscr{F}\phi(\mathbf{x})$ is also in $\mathcal{T}_{n}$ .
- Let
- For a multi-index $\boldsymbol{{\alpha}}=(\alpha_{1},\alpha_{2},\dots,\alpha_{n})$ , define
- and
- Here $\boldsymbol{{\alpha}}$ ranges over a finite set of multi-indices, $P(\mathbf{x})$ is a multivariate polynomial, and $P(\mathbf{D})$ is a partial differential operator. Then

Formulas:

Formula 1.16.29:

$$
\mathscr{F}(\phi)(\mathbf{x})=\mathscr{F}\phi(\mathbf{x})=\frac{1}{(2\pi)^{n/2}}\int_{{\mathbb{R}}^{n}}\phi(\mathbf{t}){\mathrm{e}}^{\mathrm{i}\mathbf{x}\cdot\mathbf{t}}\,\mathrm{d}\mathbf{t},
$$

Formula:

$$
F(\mathbf{x})=F=\frac{1}{(2\pi)^{n/2}}\int_{{\mathbb{R}}^{n}}\phi(\mathbf{t}){\mathrm{e}}^{\mathrm{i}\mathbf{x}\cdot\mathbf{t}}\,\mathrm{d}\mathbf{t}.
$$

Formula 1.16.30:

$$
\mathbf{D}=\left(\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{1}},\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{2}},\ldots,\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{n}}\right).
$$

Formula:

$$
D_{\boldsymbol{{\alpha}}}={\mathrm{i}}^{-\left|\boldsymbol{{\alpha}}\right|}D^{\boldsymbol{{\alpha}}}=\left(\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{1}}\right)^{\alpha_{1}}\cdots\left(\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{n}}\right)^{\alpha_{n}}.
$$

Formula 1.16.31:

$$
P(\mathbf{x})=\sum_{\boldsymbol{{\alpha}}}c_{\boldsymbol{{\alpha}}}\mathbf{x}^{\boldsymbol{{\alpha}}}=\sum_{\boldsymbol{{\alpha}}}c_{\boldsymbol{{\alpha}}}x_{1}^{\alpha_{1}}\cdots x_{n}^{\alpha_{n}},
$$

Formula 1.16.32:

$$
P(\mathbf{D})=\sum_{\boldsymbol{{\alpha}}}c_{\boldsymbol{{\alpha}}}\mathbf{D}^{\alpha}=\sum_{\boldsymbol{{\alpha}}}c_{\boldsymbol{{\alpha}}}\left(\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{1}}\right)^{\alpha_{1}}\dots\left(\frac{1}{\mathrm{i}}\frac{\partial}{\partial x_{n}}\right)^{\alpha_{n}}.
$$

Formula:

$$
P(D)=\sum_{\boldsymbol{{\alpha}}}c_{\boldsymbol{{\alpha}}}D_{\boldsymbol{{\alpha}}}
$$

Formula 1.16.33:

$$
\mathscr{F}(P(\mathbf{D})\phi)(\mathbf{x})=P(-\mathbf{x})\mathscr{F}\phi(\mathbf{x}),
$$

Formula:

$$
\frac{1}{(2\pi)^{n/2}}\int_{{\mathbb{R}}^{n}}(P(D)\phi)(\mathbf{t}){\mathrm{e}}^{\mathrm{i}\mathbf{x}\cdot\mathbf{t}}\,\mathrm{d}\mathbf{t}=P(-\mathbf{x})F(\mathbf{x}).
$$

Formula 1.16.34:

$$
\mathscr{F}(P\phi)(\mathbf{x})=P(\mathbf{D})\mathscr{F}\phi(\mathbf{x}).
$$

Formula:

$$
\frac{1}{(2\pi)^{n/2}}\int_{{\mathbb{R}}^{n}}P(\mathbf{t})\phi(\mathbf{t}){\mathrm{e}}^{\mathrm{i}\mathbf{x}\cdot\mathbf{t}}\,\mathrm{d}\mathbf{t}=P(D)F(\mathbf{x}).
$$

Formula 1.16.35:

$$
\left\langle\mathscr{F}\left(u\right),\phi\right\rangle=\left\langle u,\mathscr{F}(\phi)\right\rangle,
$$

Formula:

$$
\left\langle\mathscr{F}\left(u\right),\phi\right\rangle=\left\langle u,F\right\rangle,
$$

Formula 1.16.36:

$$
\left\langle\mathscr{F}\left(P(\mathbf{D})u\right),\phi\right\rangle=\left\langle P_{-}\mathscr{F}\left(u\right),\phi\right\rangle=\left\langle\mathscr{F}\left(u\right),P_{-}\phi\right\rangle,
$$

Formula:

$$
\mathcal{F}(P(D)u)=P(-\mathbf{x})\mathcal{F}(u).
$$

Formula 1.16.37:

$$
\left\langle\mathscr{F}\left(Pu\right),\phi\right\rangle=\left\langle P(\mathbf{D})\mathscr{F}\left(u\right),\phi\right\rangle,
$$

Formula:

$$
\mathcal{F}(Pu)=P(D)\mathcal{F}(u).
$$


Definitions and local symbols:
- Keywords: Fourier transform , Fourier transforms , distributions , several variables , tempered distributions
- Defines: $\mathscr{F}(\phi)$ : Fourier transform of a test function (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\mathbb{R}$ : real line , $n$ : nonnegative integer and $\phi(x_{1},x_{2},\dots,x_{n})$ : test function
- Defines: $\mathbf{D}$ : vector differential operator (locally)
- Symbols: $\mathrm{i}$ : imaginary unit , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $n$ : nonnegative integer , $Df$ : distributional derivative and $\left|x\right|$ : absolute value of $x$
- Symbols: $n$ : nonnegative integer and $P$ : polynomial of several variables
- Symbols: $\mathrm{i}$ : imaginary unit , $\frac{\partial f}{\partial x}$ : partial derivative of $f$ with respect to $x$ , $\,\partial x$ : partial differential of $x$ , $n$ : nonnegative integer , $\mathbf{D}$ : vector differential operator , $P$ : polynomial of several variables and $Df$ : distributional derivative
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\mathbb{R}$ : real line , $n$ : nonnegative integer , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function , $\mathscr{F}(\phi)$ : Fourier transform of a test function , $\mathbf{D}$ : vector differential operator , $P$ : polynomial of several variables and $Df$ : distributional derivative
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\mathbb{R}$ : real line , $n$ : nonnegative integer , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function , $\mathscr{F}(\phi)$ : Fourier transform of a test function , $\mathbf{D}$ : vector differential operator , $P$ : polynomial of several variables and $Df$ : distributional derivative
- Defines: $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\in$ : element of , $n$ : nonnegative integer , $\mathcal{T}$ : space of test functions , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function and $\mathscr{F}(\phi)$ : Fourier transform of a test function
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function , $\mathbf{D}$ : vector differential operator , $P$ : polynomial of several variables and $Df$ : distributional derivative
- Symbols: $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\phi(x_{1},x_{2},\dots,x_{n})$ : test function , $\mathbf{D}$ : vector differential operator , $P$ : polynomial of several variables and $Df$ : distributional derivative

#### 1.16(viii) Fourier Transforms of Special Distributions

- We use the notation of the previous subsection and take $n=1$ and $u=\delta$ in ( 1.16.35 ). We obtain
- As distributions, the last equation reads
- which is often written conventionally as
- see also ( 1.17.2 ).
- Since $\sqrt{2\pi}\mathscr{F}\left(\delta\right)=1$ , we have
- in which $\phi_{-}(x)=\phi(-x)$ . The second to last equality follows from the Fourier integral formula ( 1.17.8 ). Since the quantity on the extreme right of ( 1.16.41 ) is equal to $\sqrt{2\pi}\left\langle\delta,\phi\right\rangle$ , as distributions, the result in this equation can be stated as

Formulas:

Formula 1.16.38:

$$
\left\langle\mathscr{F}\left(\delta\right),\phi\right\rangle=\left\langle\delta,\mathscr{F}(\phi)\right\rangle=\left\langle\delta,\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}\phi(t){\mathrm{e}}^{\mathrm{i}xt}\,\mathrm{d}t\right\rangle=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(t)\,\mathrm{d}t=\frac{1}{\sqrt{2\pi}}\left\langle 1,\phi\right\rangle,
$$

Formula 1.16.39:

$$
\mathscr{F}\left(\delta\right)=\frac{1}{\sqrt{2\pi}},
$$

Formula 1.16.40:

$$
\int^{\infty}_{-\infty}\delta\left(t\right){\mathrm{e}}^{\mathrm{i}xt}\,\mathrm{d}t=1;
$$

Formula 1.16.41:

$$
\left\langle\mathscr{F}\left(1\right),\phi\right\rangle=\sqrt{2\pi}\left\langle\mathscr{F}\left(\mathscr{F}\left(\delta\right)\right),\phi\right\rangle=\sqrt{2\pi}\left\langle\mathscr{F}\left(\delta\right),\mathscr{F}(\phi)\right\rangle=\sqrt{2\pi}\left\langle\delta,\mathscr{F}(\mathscr{F}(\phi))\right\rangle=\sqrt{2\pi}\left\langle\delta,\phi_{-}\right\rangle=\sqrt{2\pi}\phi(0),
$$

Formula 1.16.42:

$$
\mathscr{F}\left(1\right)=\sqrt{2\pi}\delta,
$$

Formula 1.16.43:

$$
\frac{1}{2\pi}\int^{\infty}_{-\infty}{\mathrm{e}}^{\mathrm{i}xt}\,\mathrm{d}t=\delta\left(x\right);
$$

Formula 1.16.44:

$$
\operatorname{sign}\left(x\right)=2H\left(x\right)-1,
$$

Formula 1.16.45:

$$
{\operatorname{sign}}^{\prime}=2H'=2\delta,
$$

Formula 1.16.46:

$$
\mathscr{F}\left({\operatorname{sign}}^{\prime}\right)=\mathscr{F}\left(2H'\right)=2\mathscr{F}\left(\delta\right)=\sqrt{\frac{2}{\pi}},
$$

Formula 1.16.47:

$$
\mathscr{F}\left({\operatorname{sign}}^{\prime}\right)=\frac{x}{\mathrm{i}}\mathscr{F}\left(\operatorname{sign}\right).
$$

Formula 1.16.48:

$$
\mathscr{F}\left(\operatorname{sign}\right)=\sqrt{\frac{2}{\pi}}\,\frac{\mathrm{i}}{x},
$$

Formula 1.16.49:

$$
\left\langle\mathscr{F}\left(\operatorname{sign}\right),\phi\right\rangle=\mathrm{i}\sqrt{\frac{2}{\pi}}\operatorname{PV}\!\int^{\infty}_{-\infty}\frac{\phi(x)}{x}\,\mathrm{d}x.
$$

Formula 1.16.50:

$$
\mathscr{F}\left(H\right)=\frac{1}{2}\mathscr{F}\left(1+\operatorname{sign}\right)=\frac{1}{2}\left[\mathscr{F}\left(1\right)+\mathscr{F}\left(\operatorname{sign}\right)\right]=\sqrt{\frac{\pi}{2}}\left(\delta+\frac{\mathrm{i}}{\pi x}\right),
$$

Formula 1.16.51:

$$
\left\langle\mathscr{F}\left(H\right),\phi\right\rangle=\sqrt{\frac{\pi}{2}}\phi(0)+\frac{\mathrm{i}}{\sqrt{2\pi}}\operatorname{PV}\!\int^{\infty}_{-\infty}\frac{\phi(x)}{x}\,\mathrm{d}x.
$$


Definitions and local symbols:
- Keywords: Dirac delta distribution , Fourier transform , Fourier transforms , Heaviside function , distributions , sign function , special distributions
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution , $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\in$ : element of , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\mathcal{T}$ : space of test functions , $\mathscr{F}(\phi)$ : Fourier transform of a test function and $\phi(x)$ : test function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution and $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathscr{F}(\phi)$ : Fourier transform of a test function and $\phi(x)$ : test function
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution and $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution
- Symbols: $\delta\left(x-a\right)$ : Dirac delta (or Dirac delta function) , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Symbols: $H\left(x\right)$ : Heaviside function and $\operatorname{sign} x$ : sign of
- Symbols: $H\left(x\right)$ : Heaviside function , $\delta_{x}$ : Dirac delta distribution and $\operatorname{sign} x$ : sign of
- Symbols: $H\left(x\right)$ : Heaviside function , $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution and $\operatorname{sign} x$ : sign of
- Symbols: $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathrm{i}$ : imaginary unit and $\operatorname{sign} x$ : sign of
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathrm{i}$ : imaginary unit and $\operatorname{sign} x$ : sign of
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathrm{i}$ : imaginary unit , $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value , $\operatorname{sign} x$ : sign of and $\phi(x)$ : test function
- Symbols: $H\left(x\right)$ : Heaviside function , $\pi$ : the ratio of the circumference of a circle to its diameter , $\delta_{x}$ : Dirac delta distribution , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathrm{i}$ : imaginary unit and $\operatorname{sign} x$ : sign of
- Symbols: $H\left(x\right)$ : Heaviside function , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\left\langle \Lambda,\phi\right\rangle$ : action of distribution on test function , $\mathscr{F}\left(u\right)$ : Fourier transform of a tempered distribution , $\mathrm{i}$ : imaginary unit , $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value and $\phi(x)$ : test function

#### 1.16(ix) References for Section 1.16

- See Hildebrandt ( 1938 ) and Chihara ( 1978 , Chapter II) for Stieltjes measures which are used in  18.39(iii) ; see also Shohat and Tamarkin ( 1970 , Chapter II) . Friedman ( 1990 ) gives an overview of generalized functions and their relation to distributions. See also Lighthill ( 1958 ) , and Zemanian ( 1987 ) .

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.16](https://dlmf.nist.gov/1.16)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: convergence, definition, distribution, distributions, functions, generalized function, linear functional, linear functionals, of a function, of compact support, regular, singular, support, support of, test function space, test functions, derivatives, distributional, distributional derivative, of distribution, Dirac delta distribution, Heaviside function, derivative, tempered, tempered distributions, several variables, Fourier transform, Fourier transforms, sign function, special distributions.

### Source Notes

- See Wong ( 1989 , pp. 241-248) .
- See Wong ( 1989 , pp. 249-251) .
- See Wong ( 1989 , pp. 243-244, 252) .
- See Wong ( 1989 , pp. 252-254) .
- See Wong ( 1989 , pp. 261-265) .
- See Wong ( 1989 , pp. 265-274) .
- See Wong ( 1989 , pp. 274-279) .
