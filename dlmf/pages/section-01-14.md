# §1.14 Integral Transforms

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.14, `Integral Transforms`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Fourier Transform
- Fourier Cosine and Sine Transforms
- Laplace Transform
- Mellin Transform
- Hilbert Transform
- Stieltjes Transform
- Tables
- Compendia

### Subsections

#### 1.14(i) Fourier Transform

- The Fourier transform of a real- or complex-valued function $f(t)$ is defined by
- (Some references replace $\mathrm{i}xt$ by $-\mathrm{i}xt$ ). The same notation $\mathscr{F}$ is used for Fourier transforms of functions of several variables and for Fourier transforms of distributions; see  1.16(vii) .
- In this subsection we let $F(x)=\mathscr{F}\left(f\right)\left(x\right)$ .
- If $f(t)$ is absolutely integrable on $(-\infty,\infty)$ , then $F(x)$ is continuous, $F(x)\to 0$ as $x\to\pm\infty$ , and

Formulas:

Formula 1.14.1:

$$
\mathscr{F}\left(f\right)\left(x\right)=\mathscr{F}f\left(x\right)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}f(t){\mathrm{e}}^{\mathrm{i}xt}\,\mathrm{d}t.
$$

Formula 1.14.2:

$$
\left|F(x)\right|\leq\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}\left|f(t)\right|\,\mathrm{d}t.
$$

Formula 1.14.3:

$$
\tfrac{1}{2}(f(u+)+f(u-))=\frac{1}{\sqrt{2\pi}}\operatorname{PV}\!\int^{\infty}_{-\infty}F(x){\mathrm{e}}^{-\mathrm{i}xu}\,\mathrm{d}x,
$$

Formula 1.14.4:

$$
f(t)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}F(x){\mathrm{e}}^{-\mathrm{i}xt}\,\mathrm{d}x.
$$

Formula 1.14.5:

$$
(f*g)(t)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}f(t-s)g(s)\,\mathrm{d}s.
$$

Formula 1.14.6:

$$
(f*g)(t)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}F(x)G(x){\mathrm{e}}^{-\mathrm{i}tx}\,\mathrm{d}x,
$$

Formula 1.14.7:

$$
\int^{\infty}_{-\infty}F(x)G(x)\,\mathrm{d}x=\int^{\infty}_{-\infty}f(t)g(-t)\,\mathrm{d}t,
$$

Formula 1.14.7_5:

$$
\int^{\infty}_{-\infty}F(x)\overline{G(x)}\,\mathrm{d}x=\int^{\infty}_{-\infty}f(t)\overline{g(t)}\,\mathrm{d}t,
$$

Formula 1.14.8:

$$
\int^{\infty}_{-\infty}{\left|F(x)\right|}^{2}\,\mathrm{d}x=\int^{\infty}_{-\infty}{\left|f(t)\right|}^{2}\,\mathrm{d}t.
$$


Definitions and local symbols:
- Keywords: Fourier transform , convergence , definitions
- Defines: $\mathscr{F}\left(f\right)\left(s\right)$ : Fourier transform
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit and $\int$ : integral
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ and $\left|x\right|$ : absolute value of $x$
- Keywords: Fourier transform , inversion
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value and $F(x)$ : Fourier transform of $f(t)$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $F(x)$ : Fourier transform of $f(t)$
- Keywords: Fourier transform , convolution
- Defines: $*$ : convolution (Fourier) (locally)
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Fourier transform , Parseval's formula
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ , $*$ : convolution (Fourier) and $G(x)$ : Fourier transform of $g(t)$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ and $G(x)$ : Fourier transform of $g(t)$
- Symbols: $\overline{z}$ : complex conjugate , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ and $G(x)$ : Fourier transform of $g(t)$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F(x)$ : Fourier transform of $f(t)$ and $\left|x\right|$ : absolute value of $x$
- Keywords: Fourier transform , uniqueness

#### 1.14(ii) Fourier Cosine and Sine Transforms

- The Fourier cosine transform and Fourier sine transform are defined respectively by
- In this subsection we let $F_{c}(x)=\mathscr{F}_{c}f\left(x\right)$ , $F_{s}(x)=\mathscr{F}_{s}f\left(x\right)$ , $G_{c}(x)=\mathscr{F}_{c}g\left(x\right)$ , and $G_{s}(x)=\mathscr{F}_{s}g\left(x\right)$ .

Formulas:

Formula 1.14.9:

$$
\displaystyle\mathscr{F}_{c}\left(f\right)\left(x\right)
$$

Formula 1.14.10:

$$
\displaystyle\mathscr{F}_{s}\left(f\right)\left(x\right)
$$

Formula 1.14.11:

$$
\displaystyle\tfrac{1}{2}(f(u+)+f(u-))
$$

Formula 1.14.12:

$$
\displaystyle\tfrac{1}{2}(f(u+)+f(u-))
$$

Formula 1.14.13:

$$
\displaystyle\int^{\infty}_{0}F_{c}(x)G_{c}(x)\,\mathrm{d}x
$$

Formula 1.14.14:

$$
\displaystyle\int^{\infty}_{0}F_{s}(x)G_{s}(x)\,\mathrm{d}x
$$

Formula 1.14.15:

$$
\displaystyle\int^{\infty}_{0}(F_{c}(x))^{2}\,\mathrm{d}x
$$

Formula 1.14.16:

$$
\displaystyle\int^{\infty}_{0}(F_{s}(x))^{2}\,\mathrm{d}x
$$


Definitions and local symbols:
- Keywords: Fourier cosine and sine transforms , definition
- Defines: $\mathscr{F}_{c}\left(f\right)\left(s\right)$ : Fourier cosine transform
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $F_{c}(x)$ : cosine transformation of $f(t)$
- Defines: $\mathscr{F}_{s}\left(f\right)\left(s\right)$ : Fourier sine transform
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sin z$ : sine function and $F_{s}(x)$ : sine transformation of $f(t)$
- Keywords: Fourier cosine and sine transforms , inversion
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $F_{c}(x)$ : cosine transformation of $f(t)$
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\sin z$ : sine function and $F_{s}(x)$ : sine transformation of $f(t)$
- Keywords: Fourier cosine and sine transforms , Fourier transform , Parseval's formula
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F_{c}(x)$ : cosine transformation of $f(t)$ and $G_{c}(x)$ : cosine transformation of $g(t)$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $F_{s}(x)$ : sine transformation of $f(t)$ and $G_{s}(x)$ : sine transformation of $g(t)$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $F_{c}(x)$ : cosine transformation of $f(t)$
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral and $F_{s}(x)$ : sine transformation of $f(t)$

#### 1.14(iii) Laplace Transform

- Suppose $f(t)$ is a real- or complex-valued function and $s$ is a real or complex parameter. The Laplace transform of $f$ is defined by

Formulas:

Formula 1.14.17:

$$
\mathscr{L}\left(f\right)\left(s\right)=\mathscr{L}f\left(s\right)=\int^{\infty}_{0}{\mathrm{e}}^{-st}f(t)\,\mathrm{d}t.
$$

Formula 1.14.18:

$$
\left|f(t)\right|\leq M{\mathrm{e}}^{\alpha t},
$$

Formula 1.14.19:

$$
\mathscr{L}f\left(s\right)\to 0,
$$

Formula 1.14.20:

$$
f(t)=\frac{1}{2\pi\mathrm{i}}\lim_{T\to\infty}\int^{\sigma+\mathrm{i}T}_{\sigma-\mathrm{i}T}{\mathrm{e}}^{ts}\mathscr{L}f\left(s\right)\,\mathrm{d}s,
$$

Formula 1.14.21:

$$
\mathscr{L}f\left(s-a\right)=\mathscr{L}f_{a}\left(s\right),
$$

Formula 1.14.22:

$$
\mathscr{L}f_{a}^{+}\left(s\right)={\mathrm{e}}^{-as}\mathscr{L}f\left(s\right),
$$

Formula 1.14.23:

$$
{(-1)}^{n}\frac{{\mathrm{d}}^{n}}{{\mathrm{d}s}^{n}}\mathscr{L}f\left(s\right)=\mathscr{L}f_{n}\left(s\right),
$$

Formula 1.14.24:

$$
\int^{\infty}_{s}\mathscr{L}f\left(u\right)\,\mathrm{d}u=\mathscr{L}f_{-1}\left(s\right),
$$

Formula 1.14.25:

$$
\mathscr{L}f\left(s\right)=\frac{1}{1-{\mathrm{e}}^{-as}}\int^{a}_{0}{\mathrm{e}}^{-st}f(t)\,\mathrm{d}t.
$$

Formula 1.14.26:

$$
\mathscr{L}f\left(s\right)=\frac{1}{1+{\mathrm{e}}^{-as}}\int^{a}_{0}{\mathrm{e}}^{-st}f(t)\,\mathrm{d}t.
$$

Formula 1.14.27:

$$
\mathscr{L}\left(f^{\prime}\right)\left(s\right)=s\mathscr{L}\left(f\right)\left(s\right)-f(0+).
$$

Formula 1.14.28:

$$
\mathscr{L}\left(f^{\prime}\right)\left(s\right)=s\mathscr{L}\left(f\right)\left(s\right)-f(0+)-\sum^{n}_{k=1}{\mathrm{e}}^{-st_{k}}(f(t_{k}+)-f(t_{k}-)).
$$

Formula 1.14.29:

$$
\mathscr{L}\left(f^{(n)}\right)\left(s\right)=s^{n}\mathscr{L}\left(f\right)\left(s\right)-s^{n-1}f(0+)-s^{n-2}f^{\prime}(0+)-\dots-f^{(n-1)}(0+).
$$

Formula 1.14.30:

$$
(f*g)(t)=\int^{t}_{0}f(u)g(t-u)\,\mathrm{d}u.
$$

Formula 1.14.31:

$$
\mathscr{L}\left(f*g\right)=\mathscr{L}\left(f\right)\mathscr{L}\left(g\right).
$$


Definitions and local symbols:
- Keywords: Laplace transform , definition , notation
- Defines: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform
- Symbols: $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm and $\int$ : integral
- Keywords: Laplace transform
- Keywords: Laplace transform , analyticity , convergence , exponential growth
- Symbols: $\mathrm{e}$ : base of natural logarithm , $M$ : constant , $\alpha$ : constant and $\left|x\right|$ : absolute value of $x$
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform and $\Re$ : real part
- Keywords: Laplace transform
- Keywords: Laplace transform , inversion
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\sigma\in(a,b)$ : parameter and $\alpha$ : constant
- Keywords: Laplace transform
- Keywords: Laplace transform , translation
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform and $\mathrm{e}$ : base of natural logarithm
- Keywords: Laplace transform
- Symbols: $H\left(x\right)$ : Heaviside function , $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform and $\mathrm{e}$ : base of natural logarithm
- Keywords: Laplace transform
- Keywords: Laplace transform , differentiation , integration
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ and $n$ : nonnegative integer
- Keywords: Laplace transform
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral

#### 1.14(iv) Mellin Transform

- The Mellin transform of a real- or complex-valued function $f(x)$ is defined by
- If $x^{\sigma-1}f(x)$ is integrable on $(0,\infty)$ for all $\sigma$ in $a<\sigma<b$ , then the integral ( 1.14.32 ) converges and $\mathscr{M}f\left(s\right)$ is an analytic function of $s$ in the vertical strip $a<\Re s<b$ . Moreover, for $a<\sigma<b$ ,
- Note: If $f(x)$ is continuous and $\alpha$ and $\beta$ are real numbers such that $f(x)=O\left(x^{\alpha}\right)$ as $x\to 0+$ and $f(x)=O\left(x^{\beta}\right)$ as $x\to\infty$ , then $x^{\sigma-1}f(x)$ is integrable on $(0,\infty)$ for all $\sigma\in(-\alpha,-\beta)$ .

Formulas:

Formula 1.14.32:

$$
\mathscr{M}\left(f\right)\left(s\right)=\mathscr{M}f\left(s\right)=\int^{\infty}_{0}x^{s-1}f(x)\,\mathrm{d}x.
$$

Formula 1.14.33:

$$
\lim_{t\to\pm\infty}\mathscr{M}f\left(\sigma+\mathrm{i}t\right)=0.
$$

Formula 1.14.34:

$$
\tfrac{1}{2}(f(u+)+f(u-))=\frac{1}{2\pi\mathrm{i}}\lim_{T\to\infty}\int^{\sigma+\mathrm{i}T}_{\sigma-\mathrm{i}T}u^{-s}\mathscr{M}f\left(s\right)\,\mathrm{d}s.
$$

Formula 1.14.35:

$$
f(x)=\frac{1}{2\pi\mathrm{i}}\int^{\sigma+\mathrm{i}\infty}_{\sigma-\mathrm{i}\infty}x^{-s}\mathscr{M}f\left(s\right)\,\mathrm{d}s.
$$

Formula 1.14.36:

$$
\int^{\infty}_{0}f(x)g(yx)\,\mathrm{d}x=\frac{1}{2\pi\mathrm{i}}\,\int^{\sigma+\mathrm{i}\infty}_{\sigma-\mathrm{i}\infty}y^{-s}\mathscr{M}f\left(1-s\right)\mathscr{M}g\left(s\right)\,\mathrm{d}s,
$$

Formula 1.14.37:

$$
\int^{\infty}_{0}f(x)g(x)\,\mathrm{d}x=\frac{1}{2\pi\mathrm{i}}\,\int^{\sigma+\mathrm{i}\infty}_{\sigma-\mathrm{i}\infty}\mathscr{M}f\left(1-s\right)\mathscr{M}g\left(s\right)\,\mathrm{d}s.
$$

Formula 1.14.38:

$$
\int^{\infty}_{0}(f(x))^{2}\,\mathrm{d}x=\frac{1}{2\pi}\int^{\infty}_{-\infty}{\left|\mathscr{M}f\left(\tfrac{1}{2}+\mathrm{i}t\right)\right|}^{2}\,\mathrm{d}t.
$$

Formula 1.14.39:

$$
(f*g)(x)=\int^{\infty}_{0}f(y)g\left(\frac{x}{y}\right)\frac{\,\mathrm{d}y}{y}.
$$

Formula 1.14.40:

$$
\int^{\infty}_{0}x^{s-1}(f*g)(x)\,\mathrm{d}x=\mathscr{M}f\left(s\right)\mathscr{M}g\left(s\right).
$$


Definitions and local symbols:
- Keywords: Mellin transform , analyticity , convergence , definition , notation
- Defines: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Mellin transform
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\mathrm{i}$ : imaginary unit and $\sigma\in(a,b)$ : parameter
- Keywords: Mellin transform
- Keywords: Mellin transform , inversion
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\sigma\in(a,b)$ : parameter
- Keywords: Mellin transform
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\sigma\in(a,b)$ : parameter
- Keywords: Mellin transform
- Keywords: Mellin transform , Parseval-type formulas
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\sigma\in(a,b)$ : parameter
- Keywords: Mellin transform
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\sigma\in(a,b)$ : parameter
- Keywords: Mellin transform
- Symbols: $\mathscr{M}\left(f\right)\left(s\right)$ : Mellin transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\left|x\right|$ : absolute value of $x$
- Keywords: Mellin transform
- Keywords: Mellin transform , convolution
- Defines: $*$ : convolution (Mellin) (locally)

#### 1.14(v) Hilbert Transform

- The Hilbert transform of a real-valued function $f(t)$ is defined in the following equivalent ways:

Formulas:

Formula 1.14.41:

$$
\displaystyle\mathcal{H}\left(f\right)\left(x\right)
$$

Formula 1.14.42:

$$
\displaystyle\mathcal{H}f\left(x\right)
$$

Formula 1.14.43:

$$
\displaystyle\mathcal{H}f\left(x\right)
$$

Formula 1.14.44:

$$
f(x)=-\frac{1}{\pi}\operatorname{PV}\!\int^{\infty}_{-\infty}\frac{\mathcal{H}f\left(u\right)}{u-x}\,\mathrm{d}u.
$$

Formula 1.14.45:

$$
\int^{\infty}_{-\infty}{\left|\mathcal{H}f\left(x\right)\right|}^{p}\,\mathrm{d}x\leq A_{p}\int^{\infty}_{-\infty}{\left|f(t)\right|}^{p}\,\mathrm{d}t,
$$

Formula 1.14.46:

$$
\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\mathcal{H}f\left(u\right){\mathrm{e}}^{\mathrm{i}ux}\,\mathrm{d}u=-\mathrm{i}(\operatorname{sign}x)\mathscr{F}f\left(x\right),
$$


Definitions and local symbols:
- Defines: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform
- Keywords: Hilbert transform , definition
- Symbols: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ and $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value
- Symbols: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Keywords: Hilbert transform , inversion
- Symbols: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ and $\operatorname{PV}\!\int_{a}^{b}$ : Cauchy principal value
- Keywords: Hilbert transform , inequalities
- Symbols: $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $A_{p}$ : coefficient and $\left|x\right|$ : absolute value of $x$
- Keywords: Fourier transform of , Hilbert transform
- Symbols: $\mathscr{F}\left(f\right)\left(s\right)$ : Fourier transform , $\mathcal{H}\left(f\right)\left(x\right)$ : Hilbert transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\mathrm{i}$ : imaginary unit , $\int$ : integral and $\operatorname{sign} x$ : sign of

#### 1.14(vi) Stieltjes Transform

- The Stieltjes transform of a real-valued function $f(t)$ is defined by
- Sufficient conditions for the integral to converge are that $s$ is a positive real number, and $f(t)=O\left(t^{-\delta}\right)$ as $t\to\infty$ , where $\delta>0$ .
- If the integral converges, then it converges uniformly in any compact domain in the complex $s$ -plane not containing any point of the interval $(-\infty,0]$ . In this case, $\mathcal{S}f\left(s\right)$ represents an analytic function in the $s$ -plane cut along the negative real axis, and

Formulas:

Formula 1.14.47:

$$
\mathcal{S}\left(f\right)\left(s\right)=\mathcal{S}f\left(s\right)=\int^{\infty}_{0}\frac{f(t)}{s+t}\,\mathrm{d}t.
$$

Formula 1.14.48:

$$
\frac{{\mathrm{d}}^{m}}{{\mathrm{d}s}^{m}}\mathcal{S}f\left(s\right)=(-1)^{m}m!\int^{\infty}_{0}\frac{f(t)\,\mathrm{d}t}{(s+t)^{m+1}},
$$

Formula 1.14.49:

$$
\lim_{t\to 0+}\frac{\mathcal{S}f\left(-\sigma-\mathrm{i}t\right)-\mathcal{S}f\left(-\sigma+\mathrm{i}t\right)}{2\pi\mathrm{i}}=\tfrac{1}{2}(f(\sigma+)+f(\sigma-)),
$$

Formula 1.14.50:

$$
\mathcal{S}\left(f\right)=\mathscr{L}\left(\mathscr{L}\left(f\right)\right).
$$


Definitions and local symbols:
- Keywords: Stieltjes transform , analyticity , convergence , definition , derivatives
- Defines: $\mathcal{S}\left(f\right)\left(s\right)$ : Stieltjes transform
- Symbols: $\,\mathrm{d}x$ : differential of $x$ and $\int$ : integral
- Symbols: $\mathcal{S}\left(f\right)\left(s\right)$ : Stieltjes transform , $\frac{\mathrm{d}f}{\mathrm{d}x}$ : derivative of $f$ with respect to $x$ , $\,\mathrm{d}x$ : differential of $x$ , $!$ : factorial (as in $n!$ ) , $\int$ : integral and $m$ : nonnegative integer
- Keywords: Stieltjes transform , inversion
- Symbols: $\mathcal{S}\left(f\right)\left(s\right)$ : Stieltjes transform , $\pi$ : the ratio of the circumference of a circle to its diameter , $\mathrm{i}$ : imaginary unit and $\sigma\in(a,b)$ : parameter
- Keywords: Stieltjes transform , representation as double Laplace transform
- Symbols: $\mathscr{L}\left(f\right)\left(s\right)$ : Laplace transform and $\mathcal{S}\left(f\right)\left(s\right)$ : Stieltjes transform

#### 1.14(vii) Tables

Definitions and local symbols:
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\cosh z$ : hyperbolic cosine function , $\sinh z$ : hyperbolic sine function , $\mathrm{i}$ : imaginary unit , $\int$ : integral , $\sin z$ : sine function and $\left|x\right|$ : absolute value of $x$
- Keywords: Fourier transform , tables
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $\ln z$ : principal branch of logarithm function , $\Re$ : real part and $\sin z$ : sine function
- Keywords: Fourier cosine and sine transforms , tables
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $\int$ : integral , $\operatorname{arctan} z$ : arctangent function , $\ln z$ : principal branch of logarithm function , $\operatorname{ph}$ : phase , $\Re$ : real part , $\sin z$ : sine function and $\left|x\right|$ : absolute value of $x$
- Keywords: Fourier cosine and sine transforms , tables
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\cos z$ : cosine function , $\,\mathrm{d}x$ : differential of $x$ , $\mathrm{e}$ : base of natural logarithm , $!$ : factorial (as in $n!$ ) , $\cosh z$ : hyperbolic cosine function , $\sinh z$ : hyperbolic sine function , $\Im$ : imaginary part , $\int$ : integral , $\operatorname{arctan} z$ : arctangent function , $\ln z$ : principal branch of logarithm function , $\Re$ : real part , $\sin z$ : sine function , $n$ : nonnegative integer and $\left|x\right|$ : absolute value of $x$
- Keywords: Laplace transform , tables
- Symbols: $\pi$ : the ratio of the circumference of a circle to its diameter , $\csc z$ : cosecant function , $\cos z$ : cosine function , $\cot z$ : cotangent function , $\,\mathrm{d}x$ : differential of $x$ , $\int$ : integral , $\operatorname{arccot} z$ : arccotangent function , $\operatorname{arctan} z$ : arctangent function , $\ln z$ : principal branch of logarithm function , $\operatorname{ph}$ : phase , $\Re$ : real part , $\sec z$ : secant function , $\sin z$ : sine function , $\tan z$ : tangent function and $\left|x\right|$ : absolute value of $x$
- Keywords: Mellin transform , tables

#### 1.14(viii) Compendia

- For more extensive tables of the integral transforms of this section and tables of other integral transforms, see Erdlyi et al. ( 1954a , b ) , Gradshteyn and Ryzhik ( 2015 ) , Marichev ( 1983 ) , Oberhettinger ( 1972 , 1974 , 1990 ) , Oberhettinger and Badii ( 1973 ) , Oberhettinger and Higgins ( 1961 ) , Prudnikov et al. ( 1986a , b , 1990 , 1992a , 1992b ) .

Definitions and local symbols:
- Keywords: Fourier cosine and sine transforms , Fourier transform , Laplace transform , Mellin transform , compendia , integral transforms , tables

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.14](https://dlmf.nist.gov/1.14)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: integral transforms, Fourier transform, convergence, definitions, inversion, convolution, Parseval's formula, uniqueness, Fourier cosine and sine transforms, definition, Laplace transform, notation, analyticity, exponential growth, translation, differentiation, integration, of periodic functions, derivatives, Mellin transform, Parseval-type formulas, Hilbert transform, inequalities, Fourier transform of, Stieltjes transform, representation as double Laplace transform, tables, compendia.

### Source Notes

- See Titchmarsh ( 1986a , pp. 3-15, 42, 50-59) .
- See Titchmarsh ( 1986a , pp. 3-15, 50-59) .
- See Schiff ( 1999 , pp. 12-57, 91-93, 151-157) .
- See Paris and Kaminski ( 2001 , pp. 79-89) , Titchmarsh ( 1986a , pp. 51-53, 60) , and Wong ( 1989 , pp. 147-152) .
- See Titchmarsh ( 1986a , pp. 119-132) and Henrici ( 1986 , vol. 3, pp. 197-202) . For ( 1.14.46 ) see Sneddon ( 1972 , p. 234) .
- See Widder ( 1941 , pp. 325-328, 340-341) .
- See Davies ( 1984 , pp. 11-13, 103-108, 152-153, 209-211) , Pinkus and Zafrany ( 1997 , pp. 147-149) , Schiff ( 1999 , pp. 209-218) , Titchmarsh ( 1986a , pp. 176-210) , and Wong ( 1989 , pp. 192-194) .
