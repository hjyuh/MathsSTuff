# Erdős #509 — Merge-height ⇒ Capacity suppression (a concrete lemma to prove/use)

This note isolates a *single* quantitative statement that matches the “crowd‑or‑crush” heuristic and is tailor‑made for a merge‑tree strategy.

It does **not** solve #509 on its own, but it gives a clean lever: *if a component stays isolated until high Green level, then it must be tiny in capacity (hence cheap to cover).*

---

## 1. Setup

Let

- \(f\) be a **monic** polynomial of degree \(d\ge 2\),
- \(E_\rho := \{z\in\mathbb C : |f(z)|\le \rho\}\) for \(\rho\ge 1\),
- \(E := E_1\) the filled lemniscate.

Let \(K\) be a connected component of \(E\) containing exactly \(k\) zeros of \(f\) (counted with multiplicity), with \(1\le k<d\).

For \(\rho\ge 1\), denote by \(U_\rho\) the connected component of \(E_\rho\) that contains \(K\).

Assume there exists \(R>1\) such that:

1. for every \(\rho\in[1,R)\), \(U_\rho\) is isolated (does not touch/merge with other components), and
2. at \(\rho=R\), the component \(U_R\) is **the first level** where the continuation of \(K\) merges with another component.

(Heuristically: \(R\) is the first “merge height” in the cluster tree above the leaf \(K\).)

---

## 2. Statement

### Lemma (merge-height capacity suppression)

Under the setup above,

\[
\operatorname{cap}(K)\ \le\ R^{\frac1d-\frac1k}.
\]

In particular, since \(k<d\), the exponent \(\frac1d-\frac1k<0\), so large \(R\) forces \(\operatorname{cap}(K)\) to be *very small*.

---

## 3. Proof skeleton (what must be made fully rigorous)

### Step 1: a clean annulus in the slab

For \(\rho\in(1,R)\), the “slab” region

\[
A := \{z\in U_R : 1<|f(z)|<R\}
\]

is (under the “first merge” / no-critical-values-in-the-slab condition) a doubly connected domain separating \(\partial U_R\) from \(\partial K\) (i.e. a ring domain with inner boundary \(\partial K\) and outer boundary in \(\partial U_R\)).

*(In a generic setting where \(|f|\) has no critical points on the intermediate level curves, the components move by holomorphic motion and the slab is a true annulus.)*

### Step 2: modulus is inherited from the base annulus

On the slab \(A\), \(f\) has no zeros and (by “first merge”) no critical points with \(|f|\in(1,R)\) inside this cluster branch. Hence

\[
f : A \to \{w: 1<|w|<R\}
\]

is an **unbranched proper holomorphic covering map** of degree \(k\) (equal to the number of zeros in the cluster).

Therefore the conformal modulus satisfies

\[
\operatorname{mod}(A)=\frac1k\operatorname{mod}\bigl(\{1<|w|<R\}\bigr)=\frac1k\cdot\frac{1}{2\pi}\log R.
\]

### Step 3: modulus controls the ratio of logarithmic capacities

A standard extremal-length/capacity comparison for ring domains implies:

> If \(K\subset U\) are continua with \(U\) simply connected and \(U\setminus K\) a ring domain of modulus \(M\), then
> \[
> \log\frac{\operatorname{cap}(U)}{\operatorname{cap}(K)}\ \ge\ 2\pi M.
> \]
> Equivalently,
> \[
> \operatorname{cap}(K)\ \le\ \operatorname{cap}(U)\,e^{-2\pi M}.
> \]

Applying this with \(U=U_R\) and \(M=\operatorname{mod}(A)=\frac{1}{2\pi k}\log R\) gives

\[
\operatorname{cap}(K)\ \le\ \operatorname{cap}(U_R)\,e^{-\frac{1}{k}\log R}
= \operatorname{cap}(U_R)\,R^{-1/k}.
\]

### Step 4: capacity monotonicity + polynomial scaling of \(E_R\)

We have \(U_R\subset E_R\), so by monotonicity

\[
\operatorname{cap}(U_R)\le \operatorname{cap}(E_R).
\]

For monic \(f\) of degree \(d\), the capacity scaling of polynomial lemniscates gives

\[
\operatorname{cap}(E_R)=R^{1/d}.
\]

Therefore

\[
\operatorname{cap}(K)\le R^{1/d}\,R^{-1/k}=R^{\frac1d-\frac1k}.
\]

That’s the desired inequality.

---

## 4. Immediate corollary for \(\tau\) (connected components)

Each component \(K\) is connected. For connected planar compact sets, Pólya’s projection/capacity inequality implies

\[
\operatorname{diam}(K)\le 4\operatorname{cap}(K)
\quad\Rightarrow\quad
\tau(K)=\frac{\operatorname{diam}(K)}{2}\le 2\operatorname{cap}(K).
\]

So the lemma yields

\[
\tau(K)\le 2\,R^{\frac1d-\frac1k}.
\]

Interpretation:

- If a leaf component must wait until huge \(R\) to merge, it is *cheap*.
- If it is expensive (large \(\tau\)), it must merge at very small \(R\approx 1\), hence must be “crowded” in a low-level equipotential cluster.

This is exactly the dichotomy we want.

---

## 5. What remains (why this isn’t already a proof of #509)

Even if you sum the separate covers of components using \(\tau(K_j)\le 2\operatorname{cap}(K_j)\), you can exceed 2 because \(\sum_j\operatorname{cap}(K_j)\) can exceed 1 (quadratic counterexamples show this).

So the missing step is:

> When many components are “expensive,” their merge heights are close to 1, which should force geometric crowding that allows a **shared cover** to beat the sum of individual covers.

Formalizing that shared-cover advantage — in a way that is *specific to polynomial lemniscates* — is the next bottleneck.

---

## 6. A clean next lemma to target (bridging to \(\tau(E)\le 2\))

Here is a concrete formulation that would combine with the suppression lemma to yield #509:

> **Bridge Lemma (crowding ⇒ shared cover).**
> Suppose two clusters \(K_1,K_2\subset E_1\) first merge at level \(R\in(1,R_0]\) where \(R_0\) is an absolute constant close to 1.
> Then \(K_1\cup K_2\) can be covered by disks with total radius
> \[
> \tau(K_1\cup K_2)\ \le\ 2\bigl(\operatorname{cap}(K_1)+\operatorname{cap}(K_2)\bigr)\ -\ \eta(R)
> \]
> for some explicit \(\eta(R)>0\) when \(R\) is close to 1.

This would quantify the *non-additivity* needed to compensate for \(\sum \operatorname{cap}(K_j)>1\).

That kind of lemma is the “first hard lemma” in a form that is crisp and testable.

