# §1.2 Elementary Algebra

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §1.2, `Elementary Algebra`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Binomial Coefficients
- Finite Series
- Partial Fractions
- Means
- Matrices, Vectors, Scalar Products, and Norms
- Square Matrices

### Subsections

#### 1.2(i) Binomial Coefficients

- In ( 1.2.1 ) and ( 1.2.3 ) $k$ and $n$ are nonnegative integers and $k\leq n$ . In ( 1.2.2 ), ( 1.2.4 ), and ( 1.2.5 ) $n$ is a positive integer. See also  26.3(i) .
- For complex $z$ the binomial coefficient $\genfrac{(}{)}{0.0pt}{}{z}{k}$ is defined via ( 1.2.6 ).

Formulas:

Formula 1.2.1:

$$
\genfrac{(}{)}{0.0pt}{}{n}{k}=\frac{n!}{(n-k)!k!}=\genfrac{(}{)}{0.0pt}{}{n}{n-k}.
$$

Formula 1.2.2:

$$
(a+b)^{n}=a^{n}+\genfrac{(}{)}{0.0pt}{}{n}{1}a^{n-1}b+\genfrac{(}{)}{0.0pt}{}{n}{2}a^{n-2}b^{2}+\dots+\genfrac{(}{)}{0.0pt}{}{n}{n-1}ab^{n-1}+b^{n}.
$$

Formula 1.2.3:

$$
\genfrac{(}{)}{0.0pt}{}{n}{0}+\genfrac{(}{)}{0.0pt}{}{n}{1}+\dots+\genfrac{(}{)}{0.0pt}{}{n}{n}=2^{n}.
$$

Formula 1.2.4:

$$
\genfrac{(}{)}{0.0pt}{}{n}{0}-\genfrac{(}{)}{0.0pt}{}{n}{1}+\dots+(-1)^{n}\genfrac{(}{)}{0.0pt}{}{n}{n}=0.
$$

Formula 1.2.5:

$$
\genfrac{(}{)}{0.0pt}{}{n}{0}+\genfrac{(}{)}{0.0pt}{}{n}{2}+\genfrac{(}{)}{0.0pt}{}{n}{4}+\dots+\genfrac{(}{)}{0.0pt}{}{n}{\ell}=2^{n-1},
$$

Formula 1.2.6:

$$
\genfrac{(}{)}{0.0pt}{}{z}{k}=\frac{z(z-1)\cdots(z-k+1)}{k!}=\frac{(-1)^{k}{\left(-z\right)_{k}}}{k!}=(-1)^{k}\genfrac{(}{)}{0.0pt}{}{k-z-1}{k}.
$$

Formula 1.2.7:

$$
\genfrac{(}{)}{0.0pt}{}{z+1}{k}=\genfrac{(}{)}{0.0pt}{}{z}{k}+\genfrac{(}{)}{0.0pt}{}{z}{k-1}.
$$

Formula 1.2.8:

$$
\sum^{m}_{k=0}\genfrac{(}{)}{0.0pt}{}{z+k}{k}=\genfrac{(}{)}{0.0pt}{}{z+m+1}{m}.
$$

Formula 1.2.9:

$$
\genfrac{(}{)}{0.0pt}{}{z}{0}-\genfrac{(}{)}{0.0pt}{}{z}{1}+\dots+(-1)^{m}\genfrac{(}{)}{0.0pt}{}{z}{m}=(-1)^{m}\genfrac{(}{)}{0.0pt}{}{z-1}{m}.
$$


Definitions and local symbols:
- Defines: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient
- Keywords: binomial coefficients , binomials , definition
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $!$ : factorial (as in $n!$ ) , $k$ : integer and $n$ : nonnegative integer
- Keywords: binomial theorem
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $\ell$ : integer and $n$ : nonnegative integer
- Symbols: ${\left(a\right)_{n}}$ : Pochhammer's symbol (or shifted factorial) , $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $!$ : factorial (as in $n!$ ) , $z$ : variable , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $z$ : variable , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $z$ : variable , $k$ : integer , $m$ : nonnegative integer and $n$ : nonnegative integer
- Symbols: $\genfrac{(}{)}{0.0pt}{}{m}{n}$ : binomial coefficient , $z$ : variable , $m$ : nonnegative integer and $n$ : nonnegative integer

#### 1.2(ii) Finite Series

Formulas:

Formula 1.2.10:

$$
a+(a+d)+(a+2d)+\dots+(a+(n-1)d)=na+\tfrac{1}{2}n(n-1)d=\tfrac{1}{2}n(a+\ell),
$$

Formula 1.2.11:

$$
a+ax+ax^{2}+\dots+ax^{n-1}=\frac{a(1-x^{n})}{1-x},
$$


Definitions and local symbols:
- Keywords: arithmetic progression
- Symbols: $n$ : nonnegative integer
- Keywords: geometric progression (or series)
- Symbols: $n$ : nonnegative integer

#### 1.2(iii) Partial Fractions

- Let $\alpha_{1},\alpha_{2},\dots,\alpha_{n}$ be distinct constants, and $f(x)$ be a polynomial of degree less than $n$ . Then
- where
- Also,
- and $f^{(k)}$ is the $k$ -th derivative of $f$ ( 1.4(iii) ).
- If $m_{1},m_{2},\dots,m_{n}$ are positive integers and $\deg f<\sum_{j=1}^{n}m_{j}$ , then there exist polynomials $f_{j}(x)$ , $\deg f_{j}<m_{j}$ , such that
- To find the polynomials $f_{j}(x)$ , $j=1,2,\dots,n$ , multiply both sides by the denominator of the left-hand side and equate coefficients. See Chrystal ( 1959a , pp. 151-159) .

Formulas:

Formula 1.2.12:

$$
\frac{f(x)}{(x-\alpha_{1})(x-\alpha_{2})\cdots(x-\alpha_{n})}=\frac{A_{1}}{x-\alpha_{1}}+\frac{A_{2}}{x-\alpha_{2}}+\dots+\frac{A_{n}}{x-\alpha_{n}},
$$

Formula 1.2.13:

$$
A_{j}=\frac{f(\alpha_{j})}{\prod\limits_{k\not=j}(\alpha_{j}-\alpha_{k})}.
$$

Formula 1.2.14:

$$
\frac{f(x)}{(x-\alpha_{1})^{n}}=\frac{B_{1}}{x-\alpha_{1}}+\frac{B_{2}}{(x-\alpha_{1})^{2}}+\dots+\frac{B_{n}}{(x-\alpha_{1})^{n}},
$$

Formula 1.2.15:

$$
B_{j}=\frac{f^{(n-j)}(\alpha_{1})}{(n-j)!},
$$

Formula 1.2.16:

$$
\frac{f(x)}{(x-\alpha_{1})^{m_{1}}(x-\alpha_{2})^{m_{2}}\cdots(x-\alpha_{n})^{m_{n}}}=\frac{f_{1}(x)}{(x-\alpha_{1})^{m_{1}}}+\frac{f_{2}(x)}{(x-\alpha_{2})^{m_{2}}}+\cdots+\frac{f_{n}(x)}{(x-\alpha_{n})^{m_{n}}}.
$$


Definitions and local symbols:
- Keywords: partial fractions
- Symbols: $n$ : nonnegative integer , $f(x)$ : polynomial of degree less than $n$ and $A_{j}$ : coefficient
- Defines: $A_{j}$ : coefficient (locally)
- Symbols: $j$ : integer , $k$ : integer and $f(x)$ : polynomial of degree less than $n$
- Symbols: $n$ : nonnegative integer , $f(x)$ : polynomial of degree less than $n$ and $B_{j}$ : coefficient
- Defines: $B_{j}$ : coefficient (locally)
- Symbols: $!$ : factorial (as in $n!$ ) , $j$ : integer , $n$ : nonnegative integer and $f(x)$ : polynomial of degree less than $n$
- Symbols: $m$ : nonnegative integer , $n$ : nonnegative integer and $f(x)$ : polynomial of degree less than $n$

#### 1.2(iv) Means

- The arithmetic mean of $n$ numbers $a_{1},a_{2},\dots,a_{n}$ is
- The geometric mean $G$ and harmonic mean $H$ of $n$ positive numbers $a_{1},a_{2},\dots,a_{n}$ are given by
- If $r$ is a nonzero real number, then the weighted mean $M(r)$ of $n$ nonnegative numbers $a_{1},a_{2},\dots,a_{n}$ , and $n$ positive numbers $p_{1},p_{2},\dots,p_{n}$ with
- is defined by
- with the exception
- For $p_{j}=1/n$ , $j=1,2,\dots,n$ ,

Formulas:

Formula 1.2.17:

$$
A=\frac{a_{1}+a_{2}+\dots+a_{n}}{n}.
$$

Formula 1.2.18:

$$
G=(a_{1}a_{2}\cdots a_{n})^{1/n},
$$

Formula 1.2.19:

$$
\frac{1}{H}=\frac{1}{n}\left(\frac{1}{a_{1}}+\frac{1}{a_{2}}+\dots+\frac{1}{a_{n}}\right).
$$

Formula 1.2.20:

$$
p_{1}+p_{2}+\dots+p_{n}=1,
$$

Formula 1.2.21:

$$
M(r)=(p_{1}a_{1}^{r}+p_{2}a_{2}^{r}+\dots+p_{n}a_{n}^{r})^{1/r},
$$

Formula 1.2.22:

$$
M(r)=0,
$$

Formula 1.2.23:

$$
\displaystyle\lim_{r\to\infty}M(r)
$$

Formula 1.2.24:

$$
\displaystyle\lim_{r\to-\infty}M(r)
$$

Formula:

$$
\displaystyle M(1)
$$

Formula:

$$
\displaystyle M(-1)
$$

Formula 1.2.26:

$$
\lim_{r\to 0}M(r)=G.
$$


Definitions and local symbols:
- Keywords: arithmetic mean , geometric mean , harmonic mean , means , weighted means
- Defines: $A$ : arithmetic mean (locally)
- Symbols: $n$ : nonnegative integer
- Defines: $G$ : geometric mean (locally)
- Symbols: $n$ : nonnegative integer
- Defines: $H$ : harmonic mean (locally)
- Symbols: $n$ : nonnegative integer
- Symbols: $n$ : nonnegative integer and $p_{j}$ ; positive numbers
- Defines: $M(r)$ : weighted mean (locally)
- Symbols: $n$ : nonnegative integer and $p_{j}$ ; positive numbers
- Symbols: $n$ : nonnegative integer and $M(r)$ : weighted mean
- Symbols: $n$ : nonnegative integer and $M(r)$ : weighted mean
- Symbols: $n$ : nonnegative integer and $M(r)$ : weighted mean
- Symbols: $A$ : arithmetic mean , $H$ : harmonic mean and $M(r)$ : weighted mean
- Symbols: $G$ : geometric mean and $M(r)$ : weighted mean

#### 1.2(v) Matrices, Vectors, Scalar Products, and Norms

Formulas:

Formula 1.2.27:

$$
\mathbf{A}=[a_{ij}]=\left[\begin{matrix}a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{m1}&a_{m2}&\dots&a_{mn}\end{matrix}\right],
$$

Formula 1.2.28:

$$
\mathbf{A}^{\mathrm{T}}=[a_{ji}],
$$

Formula 1.2.29:

$$
\overline{\mathbf{A}}=[\overline{a_{ij}}],
$$

Formula 1.2.30:

$$
{\mathbf{A}}^{{\mathrm{H}}}=[\overline{a_{ji}}].
$$

Formula 1.2.31:

$$
\alpha\mathbf{A}=\mathbf{A}\alpha=[\alpha a_{ij}].
$$

Formula 1.2.32:

$$
\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}=[a_{ij}+b_{ij}],
$$

Formula 1.2.33:

$$
\mathbf{A}+\mathbf{B}+\mathbf{C}=(\mathbf{A}+\mathbf{B})+\mathbf{C}=\mathbf{A}+(\mathbf{B}+\mathbf{C})=[a_{ij}+b_{ij}+c_{ij}].
$$

Formula 1.2.34:

$$
c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}.
$$

Formula 1.2.35:

$$
\mathbf{A}(\mathbf{B}\mathbf{C})=(\mathbf{A}\mathbf{B})\mathbf{C};
$$

Formula 1.2.36:

$$
\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}.
$$

Formula 1.2.37:

$$
(\mathbf{A}\mathbf{B})^{\mathrm{T}}=\mathbf{B}^{\mathrm{T}}\mathbf{A}^{\mathrm{T}}.
$$

Formula 1.2.38:

$$
\mathbf{v}=\left[\begin{matrix}v_{1}\\ v_{2}\\ \vdots\\ v_{n}\end{matrix}\right],
$$

Formula 1.2.39:

$$
\mathbf{v}^{\mathrm{T}}=\left[\begin{matrix}v_{1}&v_{2}&\dots&v_{n}\\ \end{matrix}\right].
$$

Formula 1.2.40:

$$
\left\langle\mathbf{u},\mathbf{v}\right\rangle=\sum_{i=1}^{n}u_{i}\overline{v_{i}}={\mathbf{v}}^{{\mathrm{H}}}\mathbf{u}.
$$

Formula 1.2.41:

$$
\left\langle\mathbf{u},\mathbf{v}\right\rangle=\overline{\left\langle\mathbf{v},\mathbf{u}\right\rangle},
$$

Formula 1.2.42:

$$
\left\langle\alpha\mathbf{u},\beta\mathbf{v}\right\rangle=\alpha\overline{\beta}\left\langle\mathbf{u},\mathbf{v}\right\rangle,
$$

Formula 1.2.43:

$$
\left\langle\mathbf{v},\mathbf{v}\right\rangle=0,
$$

Formula 1.2.44:

$$
\left\langle\mathbf{u},\mathbf{v}\right\rangle=0.
$$

Formula 1.2.45:

$$
\left\|{\mathbf{v}}\right\|_{p}=\left(\sum_{i=1}^{n}{\left|v_{i}\right|}^{p}\right)^{1/p},
$$

Formula 1.2.46:

$$
\left\|{\mathbf{v}}\right\|=\left\|{\mathbf{v}}\right\|_{2}=\sqrt{\left\langle\mathbf{v},\mathbf{v}\right\rangle},
$$

Formula 1.2.47:

$$
\left\|{\mathbf{v}}\right\|_{1}=\sum_{i=1}^{n}\left|v_{i}\right|,
$$

Formula 1.2.48:

$$
\left\|{\mathbf{v}}\right\|_{\infty}=\max(\left|v_{1}\right|,\left|v_{2}\right|,\dots,\left|v_{n}\right|).
$$

Formula 1.2.49:

$$
\frac{1}{p}+\frac{1}{q}=1
$$

Formula 1.2.50:

$$
\left|\left\langle\mathbf{u},\mathbf{v}\right\rangle\right|\leq\left\|{\mathbf{u}}\right\|_{p}\,\left\|{\mathbf{v}}\right\|_{q},
$$

Formula 1.2.51:

$$
\left|\left\langle\mathbf{u},\mathbf{v}\right\rangle\right|\leq\left\|{\mathbf{u}}\right\|\,\left\|{\mathbf{v}}\right\|,
$$

Formula 1.2.52:

$$
\left\|{\mathbf{u}+\mathbf{v}}\right\|\leq\left\|{\mathbf{u}}\right\|+\left\|{\mathbf{v}}\right\|.
$$


Definitions and local symbols:
- Keywords: matrix, index notation for m by n
- Symbols: $j$ : integer , $m$ : nonnegative integer and $n$ : nonnegative integer
- Defines: $\mathbf{A}^{\mathrm{T}}$ : transpose of matrix
- Symbols: $j$ : integer
- Symbols: $\overline{z}$ : complex conjugate and $j$ : integer
- Defines: ${\mathbf{A}}^{{\mathrm{H}}}$ : Hermitian conjugate of matrix
- Symbols: $\overline{z}$ : complex conjugate and $j$ : integer
- Symbols: $j$ : integer
- Symbols: $j$ : integer
- Symbols: $j$ : integer
- Symbols: $j$ : integer , $k$ : integer and $n$ : nonnegative integer
- Symbols: $\mathbf{A}^{\mathrm{T}}$ : transpose of matrix
- Symbols: $n$ : nonnegative integer and $\mathbf{v}$ : column vector
- Symbols: $\mathbf{A}^{\mathrm{T}}$ : transpose of matrix , $n$ : nonnegative integer and $\mathbf{v}$ : column vector
- Defines: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors
- Symbols: ${\mathbf{A}}^{{\mathrm{H}}}$ : Hermitian conjugate of matrix , $\overline{z}$ : complex conjugate , $n$ : nonnegative integer , $\mathbf{v}$ : column vector and $\mathbf{u}$ : column vector
- Symbols: $\overline{z}$ : complex conjugate , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors , $\mathbf{v}$ : column vector and $\mathbf{u}$ : column vector
- Symbols: $\overline{z}$ : complex conjugate , $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors , $\mathbf{v}$ : column vector and $\mathbf{u}$ : column vector
- Symbols: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors and $\mathbf{v}$ : column vector
- Symbols: $\left\langle \mathbf{u},\mathbf{v}\right\rangle$ : inner product over vectors , $\mathbf{v}$ : column vector and $\mathbf{u}$ : column vector

#### 1.2(vi) Square Matrices

- Square $n\times n$ matrices (said to be of order $n$ ) dominate the use of matrices in the DLMF, and they have many special properties. Unless otherwise indicated, matrices are assumed square, of order $n$ ; and, when vectors are combined with them, these are of length $n$ .

Formulas:

Formula 1.2.53:

$$
\mathbf{I}=[\delta_{i,j}].
$$

Formula 1.2.54:

$$
a_{ij}=0,
$$

Formula 1.2.55:

$$
a_{ji}=a_{ij},~~a_{ij}\in\mathbb{R},
$$

Formula 1.2.56:

$$
a_{ji}=\overline{a_{ij}},~~a_{ij}\in\mathbb{C},
$$

Formula 1.2.57:

$$
a_{ij}=0,
$$

Formula 1.2.58:

$$
\left|\mathbf{A}\right|=\det(\mathbf{A})=\left|\begin{matrix}a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{n1}&a_{n2}&\dots&a_{nn}\end{matrix}\right|,
$$

Formula 1.2.59:

$$
\det(\mathbf{A})=\sum_{\sigma\in\mathfrak{S}_{n}}\operatorname{sign}{\sigma}\prod_{i=1}^{n}a_{i,\sigma(i)}.
$$

Formula 1.2.60:

$$
\mathbf{A}{\mathbf{A}}^{-1}={\mathbf{A}}^{-1}\mathbf{A}=\mathbf{I}.
$$

Formula 1.2.61:

$$
\mathbf{A}\mathbf{b}=\mathbf{c}
$$

Formula 1.2.62:

$$
\operatorname{tr}(\mathbf{A})=\sum_{i=1}^{n}a_{ii}.
$$

Formula 1.2.63:

$$
\operatorname{tr}(\alpha\mathbf{A})=\alpha\operatorname{tr}(\mathbf{A}),
$$

Formula 1.2.64:

$$
\operatorname{tr}(\mathbf{A}+\mathbf{B})=\operatorname{tr}(\mathbf{A})+\operatorname{tr}(\mathbf{B}),
$$

Formula 1.2.65:

$$
\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A}).
$$

Formula 1.2.66:

$$
[{\mathbf{A}},{\mathbf{B}}]=-[{\mathbf{B}},{\mathbf{A}}]=\mathbf{A}\mathbf{B}-\mathbf{B}\mathbf{A}.
$$

Formula 1.2.67:

$$
\left\|{\mathbf{A}}\right\|=\max_{\mathbf{x}\in\mathbf{E}_{n}\setminus\left\{\boldsymbol{{0}}\right\}}\frac{\left\|{\mathbf{A}\mathbf{x}}\right\|}{\left\|{\mathbf{x}}\right\|}=\max_{\left\|{\mathbf{x}}\right\|=1}\left\|{\mathbf{A}\mathbf{x}}\right\|.
$$

Formula 1.2.68:

$$
\left\|{\mathbf{A}\mathbf{B}}\right\|\leq\left\|{\mathbf{A}}\right\|\,\left\|{\mathbf{B}}\right\|,
$$

Formula 1.2.69:

$$
\left\|{\mathbf{A}+\mathbf{B}}\right\|\leq\left\|{\mathbf{A}}\right\|+\left\|{\mathbf{B}}\right\|.
$$

Formula 1.2.70:

$$
\mathbf{A}\mathbf{a}=\lambda\mathbf{a}.
$$

Formula 1.2.71:

$$
\det(\mathbf{A}-\lambda\mathbf{I})=0,
$$

Formula 1.2.72:

$$
(\mathbf{A}-\lambda\mathbf{I})\mathbf{a}=\boldsymbol{{0}}.
$$

Formula 1.2.73:

$$
\boldsymbol{{\Lambda}}={\mathbf{S}}^{-1}\mathbf{A}\mathbf{S}.
$$

Formula 1.2.74:

$$
\det(\mathbf{A})=\det(\mathbf{S}{\mathbf{S}}^{-1}\mathbf{A})=\det({\mathbf{S}}^{-1}\mathbf{A}\mathbf{S})=\prod_{i=1}^{n}\lambda_{i}.
$$

Formula 1.2.75:

$$
\operatorname{tr}(\mathbf{A})=\operatorname{tr}(\mathbf{S}{\mathbf{S}}^{-1}\mathbf{A})=\operatorname{tr}({\mathbf{S}}^{-1}\mathbf{A}\mathbf{S})=\sum_{i=1}^{n}\lambda_{i}.
$$

Formula 1.2.76:

$$
\exp\left(\mathbf{A}\right)=\sum_{n=0}^{\infty}\frac{1}{n!}\mathbf{A}^{n},
$$

Formula 1.2.77:

$$
\det(\exp\left(\mathbf{A}\right))=\exp\left(\operatorname{tr}(\mathbf{A})\right)=\operatorname{etr}\left(\mathbf{A}\right).
$$


Definitions and local symbols:
- Defines: $\mathbf{I}$ : identity matrix
- Symbols: $\delta_{j,k}$ : Kronecker delta and $j$ : integer
- Symbols: $j$ : integer
- Symbols: $\in$ : element of , $\mathbb{R}$ : real line and $j$ : integer
- Symbols: $\mathbb{C}$ : complex plane , $\overline{z}$ : complex conjugate , $\in$ : element of and $j$ : integer
- Symbols: $j$ : integer and $\left|x\right|$ : absolute value of $x$
- Defines: $\det$ : determinant
- Defines: $\left|\mathbf{A}\right|$ : determinant of $\mathbf{A}$ (locally)
- Symbols: $\det$ : determinant , $n$ : nonnegative integer and $\mathbf{A}$ : non-defective matrix
- Symbols: $\det$ : determinant , $\in$ : element of , $\mathfrak{S}_{n}$ : set of permutations of $\{1,2,\ldots,n\}$ , $\operatorname{sign} x$ : sign of , $n$ : nonnegative integer and $\mathbf{A}$ : non-defective matrix
- Defines: ${\mathbf{A}}^{-1}$ : matrix inverse
- Symbols: $\mathbf{I}$ : identity matrix , ${\mathbf{A}}^{-1}$ : matrix inverse and $\mathbf{A}$ : non-defective matrix
- Symbols: $\mathbf{b}$ : column vector , $\mathbf{c}$ : column vector and $\mathbf{A}$ : non-defective matrix
- Defines: $\operatorname{tr} \mathbf{A}$ : trace of matrix
- Symbols: $n$ : nonnegative integer and $\mathbf{A}$ : non-defective matrix
- Symbols: $\operatorname{tr} \mathbf{A}$ : trace of matrix and $\mathbf{A}$ : non-defective matrix
- Symbols: $\operatorname{tr} \mathbf{A}$ : trace of matrix , $\mathbf{B}$ : square matrix and $\mathbf{A}$ : non-defective matrix
- Symbols: $\operatorname{tr} \mathbf{A}$ : trace of matrix , $\mathbf{B}$ : square matrix and $\mathbf{A}$ : non-defective matrix
- Defines: $[{\mathbf{A}},{\mathbf{B}}]$ : commutator
- Symbols: $\mathbf{B}$ : square matrix and $\mathbf{A}$ : non-defective matrix

## Source and Review Notes

- Source: [https://dlmf.nist.gov/1.2](https://dlmf.nist.gov/1.2)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: binomial coefficients, binomials, definition, binomial theorem, arithmetic progression, geometric progression (or series), partial fractions, arithmetic mean, geometric mean, harmonic mean, means, weighted means, matrix, index notation for m by n, exponential of the trace, matrix exponential, matrix, index notation for m by n.

### Source Notes

- See Graham et al. ( 1994 , pp. 157-174) . For ( 1.2.1 ), see also Chrystal ( 1959b , p. 8) . For ( 1.2.2 ) and ( 1.2.7 ), see Chrystal ( 1959a , pp. 62-70) .
- See Graham et al. ( 1994 , pp. 31-34) ; see also Chrystal ( 1959a , pp. 482-483, 489) .
- See Graham et al. ( 1994 , pp. 338-345) . See also Chrystal ( 1959a , pp. 151-159) .
- See Hardy et al. ( 1967 , pp. 12-15) .
- See Axler ( 2015 , Chapters 3c, 7) and Rudin ( 1966 , Chapter 3) .
- See Axler ( 2015 , Chapters 6, 10) or Shilov ( 2013 , Chapters 1, 7) .
