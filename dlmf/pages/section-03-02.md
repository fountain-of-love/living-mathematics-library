# §3.2 Linear Algebra

## Mathematical Content

### Orientation

This note explains the mathematics of DLMF §3.2, `Linear Algebra`, with formulas rendered for Obsidian and short explanations preserved from the source structure.

### Contents

- Gaussian Elimination
- Gaussian Elimination for a Tridiagonal Matrix
- Condition of Linear Systems
- Eigenvalues and Eigenvectors
- Condition of Eigenvalues
- Lanczos Tridiagonalization of a Symmetric Matrix
- Computation of Eigenvalues

### Subsections

#### 3.2(i) Gaussian Elimination

- To solve the system
- with Gaussian elimination, where $\mathbf{A}$ is a nonsingular $n\times n$ matrix and $\mathbf{b}$ is an $n\times 1$ vector, we start with the augmented matrix
- By repeatedly subtracting multiples of each row from the subsequent rows we obtain a matrix of the form
- During this reduction process we store the multipliers $\ell_{jk}$ that are used in each column to eliminate other elements in that column. This yields a lower triangular matrix of the form
- If we denote by $\mathbf{U}$ the upper triangular matrix comprising the elements $u_{jk}$ in ( 3.2.3 ), then we have the factorization, or triangular decomposition ,
- With $\mathbf{y}=[y_{1},y_{2},\dots,y_{n}]^{\rm T}$ the process of solution can then be regarded as first solving the equation $\mathbf{L}\mathbf{y}=\mathbf{b}$ for $\mathbf{y}$ ( forward elimination ), followed by the solution of $\mathbf{U}\mathbf{x}=\mathbf{y}$ for $\mathbf{x}$ ( back substitution ).

Formulas:

Formula 3.2.1:

$$
\mathbf{A}\mathbf{x}=\mathbf{b},
$$

Formula 3.2.2:

$$
\begin{bmatrix}a_{11}&\cdots&a_{1n}&b_{1}\\ \vdots&\ddots&\vdots&\vdots\\ a_{n1}&\cdots&a_{nn}&b_{n}\end{bmatrix}.
$$

Formula 3.2.3:

$$
\begin{bmatrix}u_{11}&u_{12}&\cdots&u_{1n}&y_{1}\\ 0&u_{22}&\cdots&u_{2n}&y_{2}\\ \vdots&\ddots&\ddots&\vdots&\vdots\\ 0&\cdots&0&u_{nn}&y_{n}\end{bmatrix}.
$$

Formula 3.2.4:

$$
\mathbf{L}=\begin{bmatrix}1&0&\cdots&0\\ \ell_{21}&1&\cdots&0\\ \vdots&\ddots&\ddots&\vdots\\ \ell_{n1}&\cdots&\ell_{n,n-1}&1\end{bmatrix}.
$$

Formula 3.2.5:

$$
\mathbf{A}=\mathbf{L}\mathbf{U}.
$$

Formula 3.2.6:

$$
\begin{bmatrix}1&2&3\\ 2&3&1\\ 3&1&2\end{bmatrix}=\begin{bmatrix}1&0&0\\ 2&1&0\\ 3&5&1\end{bmatrix}\begin{bmatrix}1&2&3\\ 0&-1&-5\\ 0&0&18\end{bmatrix}.
$$


Definitions and local symbols:
- Keywords: Gaussian elimination , augmented , back substitution , factorization , forward elimination , matrix , multipliers , triangular decomposition
- Symbols: $\ell_{jk}$ : multipliers
- Keywords: Gaussian elimination , multipliers , partial pivoting , pivot (or pivot element)
- Keywords: Gaussian elimination , iterative refinement , residual vector

#### 3.2(ii) Gaussian Elimination for a Tridiagonal Matrix

- Tridiagonal matrices are ones in which the only nonzero elements occur on the main diagonal and two adjacent diagonals. Thus
- Assume that $\mathbf{A}$ can be factored as in ( 3.2.5 ), but without partial pivoting. Then
- where $u_{j}=c_{j}$ , $j=1,2,\dots,n-1$ , $d_{1}=b_{1}$ , and
- Forward elimination for solving $\mathbf{A}\mathbf{x}=\mathbf{f}$ then becomes $y_{1}=f_{1}$ ,
- and back substitution is $x_{n}=y_{n}/d_{n}$ , followed by
- For more information on solving tridiagonal systems see Golub and Van Loan ( 1996 , pp. 152-160) .

Formulas:

Formula 3.2.7:

$$
\mathbf{A}=\begin{bmatrix}b_{1}&c_{1}&&&0\\ a_{2}&b_{2}&c_{2}&&\\ &\ddots&\ddots&\ddots&\\ &&a_{n-1}&b_{n-1}&c_{n-1}\\ 0&&&a_{n}&b_{n}\end{bmatrix}.
$$

Formula 3.2.8:

$$
\mathbf{L}=\begin{bmatrix}1&0&&&0\\ \ell_{2}&1&0&&\\ &\ddots&\ddots&\ddots&\\ &&\ell_{n-1}&1&0\\ 0&&&\ell_{n}&1\end{bmatrix},
$$

Formula 3.2.9:

$$
\mathbf{U}=\begin{bmatrix}d_{1}&u_{1}&&&0\\ 0&d_{2}&u_{2}&&\\ &\ddots&\ddots&\ddots&\\ &&0&d_{n-1}&u_{n-1}\\ 0&&&0&d_{n}\end{bmatrix},
$$

Formula:

$$
\displaystyle\ell_{j}
$$

Formula:

$$
\displaystyle d_{j}
$$

Formula 3.2.11:

$$
y_{j}=f_{j}-\ell_{j}y_{j-1},
$$

Formula 3.2.12:

$$
x_{j}=(y_{j}-u_{j}x_{j+1})/d_{j},
$$


Definitions and local symbols:
- Keywords: Gaussian elimination , matrix , tridiagonal , tridiagonal systems
- Defines: $\ell_{jk}$ : elements of $\mathbf{L}$ (locally)
- Defines: $u_{j}$ : elements (locally)
- Symbols: $d_{j}$ : coefficient
- Defines: $d_{j}$ : coefficient (locally)
- Symbols: $\ell_{jk}$ : elements of $\mathbf{L}$
- Symbols: $\ell_{jk}$ : elements of $\mathbf{L}$ and $f_{i}$ : element
- Symbols: $u_{j}$ : elements and $d_{j}$ : coefficient

#### 3.2(iii) Condition of Linear Systems

- The $p$ -norm of a vector $\mathbf{x}=[x_{1},\dots,x_{n}]^{\rm T}$ is given by
- The Euclidean norm is the case $p=2$ .
- The $p$ -norm of a matrix $\mathbf{A}=[a_{jk}]$ is
- The cases $p=1,2$ , and $\infty$ are the most important:
- where $\rho(\mathbf{A}\mathbf{A}^{\rm T})$ is the largest of the absolute values of the eigenvalues of the matrix $\mathbf{A}\mathbf{A}^{\rm T}$ ; see  3.2(iv) . (We are assuming that the matrix $\mathbf{A}$ is real; if not $\mathbf{A}^{\rm T}$ is replaced by $\mathbf{A}^{\rm H}$ , the transpose of the complex conjugate of $\mathbf{A}$ .)
- The sensitivity of the solution vector $\mathbf{x}$ in ( 3.2.1 ) to small perturbations in the matrix $\mathbf{A}$ and the vector $\mathbf{b}$ is measured by the condition number

Formulas:

Formula:

$$
\displaystyle\|\mathbf{x}\|_{p}
$$

Formula:

$$
\displaystyle\|\mathbf{x}\|_{\infty}
$$

Formula 3.2.14:

$$
\|\mathbf{A}\|_{p}=\max_{\mathbf{x}\neq\boldsymbol{{0}}}\frac{\|\mathbf{A}\mathbf{x}\|_{p}}{\|\mathbf{x}\|_{p}}\,.
$$

Formula:

$$
\displaystyle\|\mathbf{A}\|_{1}
$$

Formula:

$$
\displaystyle\|\mathbf{A}\|_{\infty}
$$

Formula:

$$
\displaystyle\|\mathbf{A}\|_{2}
$$

Formula 3.2.16:

$$
\kappa(\mathbf{A})=\|\mathbf{A}\|_{p}\;\|\mathbf{A}^{-1}\|_{p},
$$

Formula 3.2.17:

$$
\frac{\|\mathbf{x}^{*}-\mathbf{x}\|_{p}}{\|\mathbf{x}\|_{p}}\leq\kappa(\mathbf{A})\frac{\|\mathbf{r}\|_{p}}{\|\mathbf{b}\|_{p}}.
$$


Definitions and local symbols:
- Keywords: Euclidean , a posteriori , condition number , condition numbers , conditioning of linear systems , error bounds , linear algebra , matrix , norms , of arbitrary order , of matrices , of vectors , vector
- Defines: $\kappa(\mathbf{A})$ : condition number (locally)
- Symbols: $\kappa(\mathbf{A})$ : condition number

#### 3.2(iv) Eigenvalues and Eigenvectors

- If $\mathbf{A}$ is an $n\times n$ matrix, then a real or complex number $\lambda$ is called an eigenvalue of $\mathbf{A}$ , and a nonzero vector $\mathbf{x}$ a corresponding ( right ) eigenvector , if
- A nonzero vector $\mathbf{y}$ is called a left eigenvector of $\mathbf{A}$ corresponding to the eigenvalue $\lambda$ if $\mathbf{y}^{\rm T}\mathbf{A}=\lambda\mathbf{y}^{\rm T}$ or, equivalently, $\mathbf{A}^{\rm T}\mathbf{y}=\lambda\mathbf{y}$ . A normalized eigenvector has Euclidean norm 1; compare ( 3.2.13 ) with $p=2$ .
- The polynomial
- is called the characteristic polynomial of $\mathbf{A}$ and its zeros are the eigenvalues of $\mathbf{A}$ . The multiplicity of an eigenvalue is its multiplicity as a zero of the characteristic polynomial ( 3.8(i) ). To an eigenvalue of multiplicity $m$ , there correspond $m$ linearly independent eigenvectors provided that $\mathbf{A}$ is nondefective , that is, $\mathbf{A}$ has a complete set of $n$ linearly independent eigenvectors.

Formulas:

Formula 3.2.18:

$$
\mathbf{A}\mathbf{x}=\lambda\mathbf{x}.
$$

Formula 3.2.19:

$$
p_{n}(\lambda)=\det[\lambda\mathbf{I}-\mathbf{A}]
$$


Definitions and local symbols:
- Keywords: characteristic , characteristic polynomial , eigenvalues , eigenvectors , left , matrix , multiplicity , nondefective , normalized , polynomials , right
- Symbols: $\lambda$ : eigenvalue
- Symbols: $\det$ : determinant and $\lambda$ : eigenvalue

#### 3.2(v) Condition of Eigenvalues

- If $\mathbf{A}$ is nondefective and $\lambda$ is a simple zero of $p_{n}(\lambda)$ , then the sensitivity of $\lambda$ to small perturbations in the matrix $\mathbf{A}$ is measured by the condition number
- where $\mathbf{x}$ and $\mathbf{y}$ are the normalized right and left eigenvectors of $\mathbf{A}$ corresponding to the eigenvalue $\lambda$ . Because $\left|\mathbf{y}^{\rm T}\mathbf{x}\right|=\left|\cos\theta\right|$ , where $\theta$ is the angle between $\mathbf{y}^{\rm T}$ and $\mathbf{x}$ we always have $\kappa(\lambda)\geq 1$ . When $\mathbf{A}$ is a symmetric matrix, the left and right eigenvectors coincide, yielding $\kappa(\lambda)=1$ , and the calculation of its eigenvalues is a well-conditioned problem.

Formulas:

Formula 3.2.20:

$$
\kappa(\lambda)=\frac{1}{\left|\mathbf{y}^{\rm T}\mathbf{x}\right|},
$$


Definitions and local symbols:
- Keywords: condition numbers , conditioning , eigenvalues , linear algebra , matrix
- Symbols: $\kappa(\mathbf{A})$ : condition number and $\lambda$ : eigenvalue

#### 3.2(vi) Lanczos Tridiagonalization of a Symmetric Matrix

- Let $\mathbf{A}$ be an $n\times n$ symmetric matrix. Define the Lanczos vectors $\mathbf{v}_{j}$ and coefficients $\alpha_{j}$ and $\beta_{j}$ by $\mathbf{v}_{0}=\boldsymbol{{0}}$ , a normalized vector $\mathbf{v}_{1}$ (perhaps chosen randomly), $\alpha_{1}=\mathbf{v}_{1}^{\rm T}\mathbf{A}\mathbf{v}_{1}$ , $\beta_{1}=0$ , and for $j=1,2,\ldots,n-1$ by the recursive scheme
- Then $\mathbf{v}_{j}^{\rm T}\mathbf{v}_{k}=\delta_{j,k}$ , $j,k=1,2,\ldots,n$ . The tridiagonal matrix
- has the same eigenvalues as $\mathbf{A}$ . Its characteristic polynomial can be obtained from the recursion
- with $p_{-1}(\lambda)=0$ , $p_{0}(\lambda)=1$ .
- In the case that the orthogonality condition is replaced by $\mathbf{S}$ -orthogonality, that is, $\mathbf{v}_{j}^{\rm T}\mathbf{S}\mathbf{v}_{k}=\delta_{j,k}$ , $j,k=1,2,\ldots,n$ , for some positive definite matrix $\mathbf{S}$ with Cholesky decomposition $\mathbf{S}=\mathbf{L}^{\rm T}\mathbf{L}$ , then the details change as follows. Start with $\mathbf{v}_{0}=\boldsymbol{{0}}$ , vector $\mathbf{v}_{1}$ such that $\mathbf{v}_{1}^{\rm T}\mathbf{S}\mathbf{v}_{1}=1$ , $\alpha_{1}=\mathbf{v}_{1}^{\rm T}\mathbf{A}\mathbf{v}_{1}$ , $\beta_{1}=0$ . Then for $j=1,2,\dots,n-1$
- For more details see Guan et al. ( 2007 ) .

Formulas:

Formula:

$$
\displaystyle\mathbf{u}
$$

Formula:

$$
\displaystyle\beta_{j+1}
$$

Formula:

$$
\displaystyle\mathbf{v}_{j+1}
$$

Formula:

$$
\displaystyle\alpha_{j+1}
$$

Formula 3.2.22:

$$
\mathbf{B}=\begin{bmatrix}\alpha_{1}&\beta_{2}&&&0\\ \beta_{2}&\alpha_{2}&\beta_{3}&&\\ &\ddots&\ddots&\ddots&\\ &&\beta_{n-1}&\alpha_{n-1}&\beta_{n}\\ 0&&&\beta_{n}&\alpha_{n}\end{bmatrix}
$$

Formula 3.2.23:

$$
p_{k+1}(\lambda)=(\lambda-\alpha_{k+1})p_{k}(\lambda)-\beta_{k+1}^{2}p_{k-1}(\lambda),
$$


Definitions and local symbols:
- Keywords: Lanczos tridiagonalization of a symmetric matrix , Lanczos vectors , matrix , symmetric , tridiagonalization
- Symbols: $\alpha_{j}$ : matrix and $\beta_{j}$ : matrix
- Symbols: $\alpha_{j}$ : matrix and $\beta_{j}$ : matrix
- Defines: $p_{k}(\lambda)$ : characteristic polynomial (locally)
- Symbols: $\alpha_{j}$ : matrix , $\beta_{j}$ : matrix and $\lambda$ : eigenvalue
- Defines: $\alpha_{j}$ : matrix (locally) and $\beta_{j}$ : matrix (locally)

#### 3.2(vii) Computation of Eigenvalues

- Many methods are available for computing eigenvalues; see Golub and Van Loan ( 1996 , Chapters 7, 8) , Trefethen and Bau ( 1997 , Chapter 5) , and Wilkinson ( 1988 , Chapters 8, 9) .

Definitions and local symbols:
- Keywords: computation , eigenvalues , linear algebra , matrix

## Source and Review Notes

- Source: [https://dlmf.nist.gov/3.2](https://dlmf.nist.gov/3.2)
- Observed version: 1.2.7, release date 2026-06-15.
- Keywords: linear algebra, matrix, Gaussian elimination, augmented, back substitution, factorization, forward elimination, multipliers, triangular decomposition, partial pivoting, pivot (or pivot element), iterative refinement, residual vector, tridiagonal, tridiagonal systems, Euclidean, a posteriori, condition number, condition numbers, conditioning of linear systems, error bounds, norms, of arbitrary order, of matrices, of vectors, vector, characteristic, characteristic polynomial, eigenvalues, eigenvectors, left, multiplicity, nondefective, normalized, polynomials, right, conditioning, Lanczos tridiagonalization of a symmetric matrix, Lanczos vectors, symmetric.

### Source Notes

- See Young and Gregory ( 1988 , pp. 741-743) .
- See Wilkinson ( 1988 , Chapter 2, 8-10) .
- See Wilkinson ( 1988 , pp. 394-395 and 423) .
