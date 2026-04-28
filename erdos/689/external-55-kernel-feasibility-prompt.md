# Prompt for 5.5 Pro: limiting kernel feasibility lemma

Created: 2026-04-25

Context: We are working on Erdos Problem 689. The current robust
prime-difference route has reached the following state.

Known framework:

1. Use the parity-first baseline \(a_2\equiv1\pmod2\).
2. Choose a large fixed set \(S\subset\{7,11,13,\ldots\}\) and nonzero residues
   \(b_s\pmod s\).  Keep \(3\) at \(0\pmod3\).
3. Define robust primes \(P>n/5\) by
   \[
     H_S(P)\ge1,\qquad H_S(2P)\ge2,\qquad H_S(4P)\ge2.
   \]
   Robust primes create no unresolved side debt.
4. Choose \(S\) so the robust density \(\delta_S>10/11\).
5. Let
   \[
     A_1(n)=\{x\in A_S(n):v_2(x)=1\},
     \qquad
     A_2(n)=\{x\in A_S(n):v_2(x)\ge2\}.
   \]
6. For fixed
   \[
     \beta\in(\delta_S^{-1}-3/5,\ 1/2),
   \]
   let
   \[
     \mathcal R_\beta(n)=\{P\in(n/5,\beta n]:P\text{ robust}\}.
   \]
7. If we match almost all labels \(P\in\mathcal R_\beta(n)\) in the hypergraph
   \[
     x\in A_1(n),\quad y\in A_2(n),\quad |y-x|=2P,
   \]
   then the pair-plus-singleton cleanup proves EP689.

Your last response clarified that:

- pointwise degrees would need Hardy-Littlewood/Bateman-Horn strength;
- averaged second moments are finite-complexity Green-Tao-Ziegler systems;
- Kahn's fractional Frankl-Rodl-Pippenger theorem should round a near-perfect
  fractional matching to an integral matching;
- the weakest remaining theorem is deterministic:

> prove a limiting fractional matching / kernel feasibility lemma for a finite
> coefficient core.

Please focus only on this deterministic kernel feasibility problem.

## Setup for the limiting problem

After truncating to a finite coefficient core, vertices have the form
\[
  x=2a q,\qquad y=2bq',
\]
where
\[
  a\in\mathcal A_1 \quad(a\text{ odd}),\qquad
  b\in\mathcal A_2 \quad(b\text{ even}),
\]
and only coefficient pairs with \(\gcd(a,b)=1\) contribute.

For each type
\[
  \tau=(a,b,\sigma,r,r',\pi),
\]
where
\[
  \sigma\in\{\pm1\},
  \quad q\equiv r\pmod W,\quad q'\equiv r'\pmod W,
  \quad P=\sigma(bq'-aq)\equiv\pi\pmod W,
  \quad \pi\in\mathcal B,
\]
we may choose a bounded nonnegative kernel
\[
  g_\tau(Q,Q')\ge0,
  \qquad Q=q/n,\quad Q'=q'/n,
\]
supported on the fixed polygon
\[
  0<Q\le\frac1{2a},\qquad
  0<Q'\le\frac1{2b},\qquad
  \frac15<\sigma(bQ'-aQ)\le\beta.
\]

The normalized edge weight is
\[
  w_e=\frac{\log^2 n}{n}g_\tau(q/n,q'/n).
\]

The desired limiting loads are:

- label load:
  \[
    L_Z(t,\pi)=1
  \]
  for almost every \(t=P/n\in(1/5,\beta]\) and robust class
  \(\pi\in\mathcal B\);
- side loads:
  \[
    L_X(z,a,r)\le1-2\gamma,\qquad
    L_Y(z,b,r')\le1-2\gamma
  \]
  for some fixed \(\gamma>0\), where \(z=x/n\) or \(z=y/n\).

## What I need from you

### 1. State the exact limiting load equations

Derive explicit integral equations for \(L_Z(t,\pi)\), \(L_X(z,a,r)\), and
\(L_Y(z,b,r')\) in terms of the kernels \(g_\tau\), including the Jacobian
factors from the linear relation
\[
  t=\sigma(bQ'-aQ).
\]

Be precise about domains, orientations, and residue/type sums.

### 2. Try to prove kernel feasibility

Either:

- construct explicit kernels \(g_\tau\) that saturate labels and keep side
  loads bounded away from \(1\); or
- reduce feasibility to a clean finite/compact max-flow or Hall condition and
  prove that condition from the density slack
  \[
    |\mathcal R_\beta|<|A_1|,\ |A_2|
  \]
  plus the geometry of the edge relation; or
- identify a genuine obstruction.

It is acceptable to first ignore residue classes and prove a model theorem,
then explain what must be added to handle \(W\)-classes and robust classes.

### 3. Check continuum Hall obstructions

For every measurable subset \(T\subset(1/5,\beta]\times\mathcal B\) of label
types, the neighbor target mass in \(A_1\) and \(A_2\) must be large enough to
route its load with slack.

Please identify the right Hall-type inequalities and check the dangerous
subsets:

- labels near \(t=1/5\);
- labels near \(t=\beta\);
- labels with restricted robust residue classes;
- coefficient pairs where \(\gcd(a,b)=1\) removes many options;
- target positions near boundaries \(z=0,1\).

### 4. Decide what moves EP689 to a proof

Give a final verdict:

1. **Kernel feasibility is provable with explicit kernels**: provide them.
2. **Kernel feasibility reduces to a finite LP / compact Hall theorem**:
   state the exact theorem left to prove.
3. **There is an obstruction**: state it precisely.

The goal is to know whether the remaining EP689 work is now a deterministic
flow problem, and if so what exact flow theorem/proof should be attacked next.
