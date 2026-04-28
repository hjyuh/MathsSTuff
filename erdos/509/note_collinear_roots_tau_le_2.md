# Erdős Problem 509 for collinear zeros (real-root polynomials)

## Problem 509 (disk-covering conjecture)

Let \(f\in\mathbb C[z]\) be monic of degree \(d\ge 1\) and define the polynomial lemniscate
\[
E(f):=\{z\in\mathbb C:\ |f(z)|\le 1\}.
\]
Define the covering functional
\[
\tau(K):=\inf\left\{\sum_j r_j:\ K\subset \bigcup_j D(c_j,r_j)\right\},
\qquad D(c,r):=\{z:\ |z-c|\le r\}.
\]
Erdős Problem 509 asks whether \(\tau(E(f))\le 2\) holds for **every** monic polynomial \(f\).

This note proves the conjectured bound \(\tau(E(f))\le 2\) when all zeros of \(f\) lie on a line.

---

## Theorem (collinear-zero case)

Let \(f\in\mathbb C[z]\) be monic of degree \(d\ge 1\).  
Assume all zeros of \(f\) lie on a line in \(\mathbb C\).  
Then
\[
\boxed{\ \tau(E(f))\le 2\ }.
\]

### Reduction to real zeros
If all zeros lie on a line, apply a rigid motion \(\Phi(z)=e^{-i\theta}(z-b)\) sending that line to \(\mathbb R\).  
Define
\[
g(z):=e^{-i\theta d}\, f(e^{i\theta}z+b).
\]
Then \(g\) is monic, \(|g(z)|=|f(e^{i\theta}z+b)|\), hence \(E(g)=\Phi(E(f))\) and \(\tau(E(g))=\tau(E(f))\).  
So it suffices to prove the theorem for monic
\[
f(z)=\prod_{k=1}^d (z-x_k),\qquad x_k\in\mathbb R.
\]

---

## Step 1: vertical monotonicity for real-root polynomials

### Lemma 1 (monotonicity in \(|\Im z|\))
Assume \(x_k\in\mathbb R\). For \(z=x+iy\),
\[
|f(x+iy)|
=\prod_{k=1}^d |x+iy-x_k|
=\prod_{k=1}^d \sqrt{(x-x_k)^2+y^2}.
\]
For fixed \(x\), each factor is increasing in \(|y|\). Hence \(|f(x+iy)|\) is increasing in \(|y|\) for fixed \(x\).

In particular, if \(|f(x+iy)|\le 1\) for some \(y\), then \(|f(x)|\le 1\).  
So the real-axis projection of \(E(f)\) is exactly
\[
P:=\{x\in\mathbb R:\ |f(x)|\le 1\}.
\]
As a closed bounded subset of \(\mathbb R\), \(P\) is a finite union of closed intervals:
\[
P=\bigcup_{j=1}^m [a_j,b_j].
\]
For each component interval \([a_j,b_j]\), by continuity and maximality, one has \(|f(a_j)|=|f(b_j)|=1\).

---

## Step 2: each vertical “slice” is trapped in a Thales disk

For an interval \(I=[a,b]\subset\mathbb R\), define the closed disk with diameter \(I\):
\[
D_I:=\left\{x+iy:\ y^2\le (x-a)(b-x)\right\}.
\]
Equivalently, \(D_I\) is the closed Euclidean disk centered at \(\frac{a+b}{2}\) of radius \(\frac{b-a}{2}\).

### Lemma 2 (Thales disk containment)
Let \(f(z)=\prod_{k=1}^d (z-x_k)\) be monic with \(x_k\in\mathbb R\).  
Let \([a,b]\) be a connected component of \(P=\{x:\ |f(x)|\le 1\}\). Then
\[
E(f)\cap\{a\le \Re z\le b\}\ \subset\ D_{[a,b]}.
\]

#### Proof
Fix \(x\in[a,b]\). Write \(x=(1-\lambda)a+\lambda b\) with \(\lambda:=\frac{x-a}{b-a}\in[0,1]\).  
Set
\[
y_0:=\sqrt{(x-a)(b-x)}=(b-a)\sqrt{\lambda(1-\lambda)}.
\]
Let \(z_0:=x+iy_0\), which lies on the upper semicircle of \(\partial D_{[a,b]}\).

Fix any real \(t\in\mathbb R\). We claim the identity
\[
|z_0-t|^2 = (1-\lambda)|a-t|^2 + \lambda |b-t|^2. \tag{1}
\]
Indeed,
\[
|z_0-t|^2=(x-t)^2+y_0^2.
\]
Let \(A:=a-t\), \(B:=b-t\). Then \(x-t=(1-\lambda)A+\lambda B\), and \(y_0^2=\lambda(1-\lambda)(B-A)^2\). The variance identity gives
\[
((1-\lambda)A+\lambda B)^2 + \lambda(1-\lambda)(B-A)^2 = (1-\lambda)A^2+\lambda B^2,
\]
which is exactly (1).

Now apply weighted AM–GM to the nonnegative numbers \(|a-t|^2\) and \(|b-t|^2\):
\[
(1-\lambda)|a-t|^2+\lambda|b-t|^2 \ \ge\ |a-t|^{2(1-\lambda)}|b-t|^{2\lambda}.
\]
Combine with (1) and take square roots:
\[
|z_0-t|\ \ge\ |a-t|^{1-\lambda}|b-t|^\lambda. \tag{2}
\]

Apply (2) with \(t=x_k\) and take the product over \(k\):
\[
|f(z_0)|
=\prod_{k=1}^d |z_0-x_k|
\ge
\prod_{k=1}^d |a-x_k|^{1-\lambda}|b-x_k|^\lambda
=
|f(a)|^{1-\lambda}|f(b)|^\lambda.
\]
Since \([a,b]\) is a component of \(P\), we have \(|f(a)|=|f(b)|=1\). Thus \(|f(z_0)|\ge 1\).

By Lemma 1, for this fixed \(x\), the function \(|y|\mapsto |f(x+iy)|\) is increasing, so for any \(|y|\ge y_0\),
\[
|f(x+iy)|\ge |f(x+iy_0)|=|f(z_0)|\ge 1.
\]
Therefore any point \(x+iy\) with \(|f(x+iy)|\le 1\) must satisfy \(|y|\le y_0\), i.e. must lie in \(D_{[a,b]}\). This proves the containment. ∎

### Corollary 3 (explicit disk cover and a \(\tau\) bound)
By Lemma 2,
\[
E(f)\subset \bigcup_{j=1}^m D_{[a_j,b_j]}.
\]
Each disk \(D_{[a_j,b_j]}\) has radius \(\frac{b_j-a_j}{2}\). Hence
\[
\tau(E(f))\le \sum_{j=1}^m \frac{b_j-a_j}{2}
=\frac12\,|P|,
\]
where \(|P|\) denotes the total length (Lebesgue measure) of \(P\subset\mathbb R\).

So the problem reduces to bounding \(|P|\).

---

## Step 3: a general projection-length bound by capacity

Let \(\mathrm{cap}(K)\) denote logarithmic capacity.

### Lemma 4 (projection length \(\le 4\,\mathrm{cap}\))
For any compact \(K\subset\mathbb C\), let \(P:=\mathrm{proj}_{\mathbb R}(K)\subset\mathbb R\) be its orthogonal projection and let \(L:=|P|\) be its length. Then
\[
L\le 4\,\mathrm{cap}(K).
\]

#### Proof using \(n\)-diameter
Define the \(n\)-diameter of a compact set \(K\) by
\[
d_n(K)
:=
\max_{z_1,\dots,z_n\in K}
\left(\prod_{1\le i<j\le n}|z_i-z_j|\right)^{\frac{2}{n(n-1)}}.
\]
A standard theorem (Fekete–Szegő) states \(\mathrm{cap}(K)=\lim_{n\to\infty} d_n(K)\).

**Step 1: capacity does not decrease under projection.**  
Fix \(n\) and choose points \(x_1,\dots,x_n\in P\). For each \(x_j\) pick \(z_j\in K\) with \(\Re z_j=x_j\). Then for all \(i\ne j\),
\[
|z_i-z_j|\ge |\Re(z_i-z_j)|=|x_i-x_j|.
\]
Therefore
\[
\prod_{i<j}|z_i-z_j|\ \ge\ \prod_{i<j}|x_i-x_j|.
\]
Taking maxima over \((x_j)\in P^n\) and \((z_j)\in K^n\) yields
\[
d_n(K)\ge d_n(P).
\]
Passing to the limit, \(\mathrm{cap}(K)\ge \mathrm{cap}(P)\).

**Step 2: among real sets of fixed length, the interval has minimal capacity.**  
Let \(P\subset\mathbb R\) be compact with length \(L\). Define the (right-continuous) distribution function
\(F(x)=|P\cap(-\infty,x]|\) and its quantile function
\[
Q(t):=\inf\{x:\ F(x)\ge t\},\qquad t\in[0,L].
\]
Then \(Q:[0,L]\to P\) is nondecreasing and satisfies the “expansion” property
\[
Q(t)-Q(s)\ \ge\ t-s\qquad(0\le s<t\le L),
\]
because \(t-s\le |P\cap[Q(s),Q(t)]|\le Q(t)-Q(s)\).

Now for any \(0\le t_1<\dots<t_n\le L\) and \(x_j:=Q(t_j)\in P\), we have
\[
|x_i-x_j|\ge |t_i-t_j|.
\]
Thus
\[
\prod_{i<j}|x_i-x_j|\ \ge\ \prod_{i<j}|t_i-t_j|.
\]
Taking the maximum over \((t_j)\in[0,L]\) shows \(d_n(P)\ge d_n([0,L])\). Hence
\[
\mathrm{cap}(P)\ge \mathrm{cap}([0,L]).
\]

**Step 3: capacity of an interval.**  
It is classical that \(\mathrm{cap}([-1,1])=\tfrac12\), and capacity scales linearly under dilations on \(\mathbb R\), so
\[
\mathrm{cap}([0,L])=\frac{L}{4}.
\]
(Indeed, \([0,L]=\tfrac{L}{2}\cdot[-1,1]+\tfrac{L}{2}\), and translations do not change capacity.)

Combining steps:
\[
\mathrm{cap}(K)\ge \mathrm{cap}(P)\ge \frac{L}{4}
\quad\Rightarrow\quad
L\le 4\,\mathrm{cap}(K).
\]
∎

---

## Step 4: capacity of a monic lemniscate

### Lemma 5 (\(\mathrm{cap}(E(f))=1\) for monic \(f\))
Let \(f\) be monic of degree \(d\). Then \(\mathrm{cap}(E(f))=1\).

#### Proof (Green-function normalization)
On \(\Omega:=\{z:\ |f(z)|>1\}\), define
\[
g(z):=\frac{1}{d}\log|f(z)|.
\]
This is harmonic on \(\Omega\), vanishes on \(\partial E(f)=\{|f|=1\}\), and satisfies
\[
g(z)=\log|z|+o(1)\qquad(z\to\infty),
\]
because \(f(z)=z^d+O(z^{d-1})\). Thus \(g\) is the Green function of \(\Omega\) with pole at \(\infty\), whose Robin constant is \(-\log\mathrm{cap}(E(f))\). The asymptotic shows this constant is 0, so \(\mathrm{cap}(E(f))=1\). ∎

---

## Finish the proof of the theorem

Let \(f\) be monic with real zeros. Let \(K=E(f)\) and \(P=\mathrm{proj}_{\mathbb R}(K)\).

From Corollary 3,
\[
\tau(E(f))\le \frac{|P|}{2}.
\]
From Lemma 4,
\[
|P|\le 4\,\mathrm{cap}(K).
\]
From Lemma 5, \(\mathrm{cap}(K)=1\). Therefore,
\[
\tau(E(f))\le \frac{|P|}{2}\le \frac{4}{2}=2.
\]
This completes the proof in the real-zero case, hence in the collinear-zero case by rigid motion invariance. ∎

---

## Remarks

1. **Why numerics point to “Chebyshev-like collinear roots.”**  
   The proof reduces \(\tau(E(f))\) to half the real projection length \(|P|\), and \(|P|\) is bounded by \(4\) purely from \(\mathrm{cap}(E(f))=1\).  
   Large \(\tau\) therefore comes from configurations that make \(|P|\) close to \(4\), i.e. push the real sublevel set \(\{|f(x)|\le 1\}\) to near-maximal length. This is consistent with numerics showing near-extremals are long, thin bands with almost collinear roots.

2. **A plausible global route for Erdős 509.**  
   If one could show that, for fixed degree \(d\), the supremum of \(\tau(E(f))\) over monic \(f\) is attained (or approximated) by collinear-root polynomials, the general conjecture \(\tau(E(f))\le 2\) would follow immediately from this theorem.

