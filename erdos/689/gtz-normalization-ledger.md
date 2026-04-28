# GTZ normalization ledger (kappa/zeta/xi/eta; W0=2W)

Created: 2026-04-25

Status: working ledger.  Purpose: pin down a single normalization convention that
simultaneously matches:

- `kernel-feasibility-program.md` Section 2 (definition of the local constants
  `\kappa_\tau` and the prime-class scale),
- `typed-kernel-lift-proof.md` Lemma 7.1 (what the lift needs),
- `external-55-gtz-moment-finalization-response.md` (what the second-moment proof
  needs, and where the "local-factor caveat" sits),
- `gtz-execution-checklist.md` (where the W-trick modulus lives operationally).

This file is not a new analytic lemma.  It is a bookkeeping contract: once the
GTZ statement is phrased in the "normalized W-tricked" form below, the only
thing to verify is that every first/second moment statement is written with the
same vertex measures and the same outside scale.  If one instead phrases GTZ in
raw prime-indicator / singular-series language, then one must explicitly check
conditional Euler-factor identities (listed below).


## 1. Moduli: W, W0=2W, and the GTZ W-trick modulus

Convention used in `kernel-feasibility-program.md` and `typed-kernel-lift-proof.md`:

- Fix a finite set of odd primes `S` (the "robust-prime data") and
  `W := \prod_{s\in S} s`.

Moment-proof convention (aligning with `external-55-gtz-moment-finalization-response.md`):

- Set
  \[
    W_0 := 2W.
  \]
  This folds the prime `2` into the fixed modulus used for congruence bookkeeping
  (parity, and "excise small primes").  In the EP689 setup `W` is odd, hence
  `\varphi(W_0)=\varphi(W)` and the prime-class scale does not change when
  passing from `W` to `W_0`.

Operational GTZ modulus (as in `gtz-execution-checklist.md`):

- Choose a small-prime cutoff `w` and set `W(w):=\prod_{p\le w} p`.
- Work with
  \[
    \widetilde W := \mathrm{lcm}(W_0,W(w)).
  \]
  All affine congruence restrictions are fixed modulo `\widetilde W` while
  proving moment estimates as `n\to\infty` (with `w` fixed), and only afterwards
  one removes `w` (iterated limit or a diagonal choice `w=w(n)\to\infty`).

Translation note (to avoid notational collisions across notes):

- Some checklists use the symbol `W_0` for `\prod_{s\in S}s`.  In this ledger we
  reserve `W` for `\prod_{s\in S}s` and reserve `W_0` for `2W`.


## 2. Prime-class scale and vertex measures (zeta/xi/eta)

Fix the prime-class scale (already used in `typed-kernel-lift-proof.md`):
\[
  N_{W_0}(n):={n\over \varphi(W_0)\log n}.
\]
Interpretation: in this scale, **one fixed coprime residue class modulo `W_0`**
has density `1`.  Equivalently, for any fixed `r\in(\mathbb Z/W_0\mathbb Z)^\times`,
\[
  \sum_{\substack{q\le n\\ q\ \mathrm{prime}\\ q\equiv r\ (W_0)}} 1
  = (1+o(1))\,N_{W_0}(n).
\]

### Label measure (zeta_pi)

Labels are robust primes `P` in a fixed residue class `\pi (W_0)`, scaled by
`t:=P/n\in I:=(1/5,\beta]`.

Convention:
\[
  d\mu_Z(\pi,t) = \zeta_\pi\,dt,\qquad \zeta_\pi:=1.
\]
This matches `typed-kernel-lift-proof.md` (Section 1): we work per residue class
in the prime-class scale `N_{W_0}(n)`.

If some writeup uses the absolute scale `n/\log n` instead, then one has the
alternative convention `\zeta_\pi = 1/\varphi(W_0)`; all identities below remain
true after consistently dividing by the corresponding vertex measures.

### Side measures (xi_{a,r}, eta_{b,r'})

Side vertices are of the form
\[
  x = 2a q,\qquad y=2b q',
\]
where `q,q'` are primes and `a` is odd, `b` is even.  Fix residue classes
`q\equiv r (W_0)` and `q'\equiv r' (W_0)`.

Use typed coordinates
\[
  Q:=q/n,\qquad Q':=q'/n.
\]
Then the limiting side vertex measures are **Lebesgue in `Q,Q'`**:
\[
  d\mu_X(a,r,Q):=dQ,\qquad d\mu_Y(b,r',Q'):=dQ'.
\]
The total mass of each typed fiber is its interval length, which is exactly the
geometric density appearing in `typed-kernel-lift-proof.md`:
\[
  \xi_{a,r}:=\mu_X(\{(a,r)\}\times(0,1/(2a)]) = {1\over 2a},
\]
\[
  \eta_{b,r'}:=\mu_Y(\{(b,r')\}\times(0,1/(2b)]) = {1\over 2b}.
\]
Equivalently, in the prime-class scale, the number of side vertices of type
`(a,r)` is `( \xi_{a,r}+o(1) ) N_{W_0}(n)` (and similarly for `(b,r')` with
`\eta_{b,r'}`).


## 3. Types and edge polytopes (what is held fixed)

An edge type is
\[
  \tau=(a,b,\sigma,r,r',\pi),
\]
with `\sigma\in\{\pm1\}` and congruence restrictions (all fixed, and all modulo
`W_0`):
\[
  q\equiv r,\qquad q'\equiv r',\qquad P:=\sigma(bq'-aq)\equiv \pi.
\]
The scaled label is `t:=P/n\in I:=(1/5,\beta]`.

The support polytope in typed coordinates is
\[
  \Omega_\tau
  :=
  \Bigl\{(Q,Q'):
    0<Q\le {1\over 2a},\ 
    0<Q'\le {1\over 2b},\ 
    \sigma(bQ'-aQ)\in I
  \Bigr\}.
\]


## 4. The defining convention for \kappa_\tau (Lemma 7.1 normalization)

This is the one convention that must be shared by the feasibility program, the
typed-kernel lift, and the GTZ moment estimates.

For each retained type `\tau`, define `\kappa_\tau\ge 0` by the weighted prime
asymptotic: for every bounded piecewise continuous `F` supported in `\Omega_\tau`,
\[
  \sum_{\substack{
        q\equiv r\ (W_0),\ q'\equiv r'\ (W_0)\\
        q,q',\ \sigma(bq'-aq)\ \mathrm{prime}\\
        \sigma(bq'-aq)\equiv\pi\ (W_0)
      }}
    {\log^2 n\over n}\,
    F(q/n,q'/n)
  =
  \left(N_{W_0}(n)+o(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'.
  \tag{\kappa-def}
\]

Notes:

- This is exactly `kernel-feasibility-program.md` (2.1) and
  `typed-kernel-lift-proof.md` (7.1), with `W_0` written explicitly.
- The entire singular-integral/singular-series main term is packaged into the
  single positive constant `\kappa_\tau`.  Locally obstructed types have
  `\kappa_\tau=0` and are discarded.
- In the deterministic feasibility/load equations, the base edge measure is
  \[
    m_\tau := \kappa_\tau\,dQ\,dQ'\quad\text{on }\Omega_\tau.
  \]

Compatibility requirement with any GTZ moment writeup:

- If that writeup uses the symbol `\lambda_\tau`, then under this ledger's
  convention one sets
  \[
    \lambda_\tau := \kappa_\tau
  \]
  (this is the explicit identification already made in
  `typed-kernel-lift-proof.md`, around (4.3)).


## 5. Dictionary to "raw" GTZ constants (when a note uses n^2/(log n)^3)

Some GTZ formulations state unweighted counts of prime patterns.  For example,
they may define, for bounded `F`,
\[
  \mathcal N_\tau(F)
  :=
  \sum_{\substack{
        q\equiv r,\ q'\equiv r',\ P=\sigma(bq'-aq)\equiv\pi\ (W_0)\\
        q,q',P\ \mathrm{prime}
      }}
    F(q/n,q'/n),
\]
and prove an asymptotic of the form
\[
  \mathcal N_\tau(F)
  =
  \left(c_\tau\int_{\Omega_\tau}F+o(1)\right){n^2\over(\log n)^3}.
  \tag{raw}
\]

Then multiplying (raw) by `(\log^2 n)/n` gives
\[
  \sum \frac{\log^2 n}{n}F
  =
  \left(c_\tau\int_{\Omega_\tau}F+o(1)\right){n\over\log n}.
\]
Comparing to `(\kappa-def)` yields the conversion
\[
  \kappa_\tau = \varphi(W_0)\,c_\tau
  \quad\text{(when (raw) is stated in the absolute scale n/log n).}
\]

If instead the "raw" statement has already normalized per residue class (so that
`n^2/(\log n)^3` is replaced by `N_{W_0}(n)^2/(\log n)` or similar), then the
conversion changes accordingly; the invariant rule is:

- Rewrite the main term with respect to the vertex measures
  `d\mu_Z(\pi,t)=\zeta_\pi dt`, `d\mu_X=dQ`, `d\mu_Y=dQ'`.
- The coefficient of `\int_{\Omega_\tau}F` after that rewrite is, by definition,
  the `\kappa_\tau` needed by Lemma 7.1.


## 6. "Normalized W-tricked GTZ" (what removes local-factor bookkeeping)

Fix `w` and the modulus `\widetilde W` from Section 1.  For each coprime residue
class `b (\widetilde W)`, define the normalized W-tricked von Mangoldt weight
(one standard choice)
\[
  \Lambda_{\widetilde W,b}(m)
  :=
  {\varphi(\widetilde W)\over \widetilde W}\,\Lambda(\widetilde W m+b).
\]

Key property: for fixed `b` and `\widetilde W`,
\[
  \sum_{m\le M}\Lambda_{\widetilde W,b}(m) = (1+o(1))\,M,
\]
so each prime residue class has mean `1` in the same outside scale.

The "normalized W-tricked GTZ" linear-forms theorem then gives, for any fixed
finite-complexity system of affine-linear forms with fixed residue restrictions
modulo `\widetilde W`,
\[
  \sum_{\mathbf m\in K\cap\mathbb Z^d}
    \prod_{i=1}^k \Lambda_{\widetilde W,b_i}(L_i(\mathbf m))
  =
  (1+o_{w}(1))\,\mathrm{Vol}(K),
\]
with `w` treated as fixed during the `n\to\infty` limit.

Why this is the right normalization for the EP689 program:

- All first-moment constants, and all second-moment constants, are computed in
  the same "mean-1 per residue class" normalization.
- Consequently, conditional-factor identities among singular series constants
  become automatic (up to the same `o_w(1)`), because every system is already
  normalized by the corresponding one-form densities.
- After the moment bounds are proved for fixed `w`, one removes the parameter
  `w` as in `gtz-execution-checklist.md`; the limiting constants are the
  `\kappa_\tau` in `(\kappa-def)`.


## 7. Local-factor identities: what is automatic vs what must be checked

### 7.1 The identities that the moment proof uses

Let `\tau_1,\tau_2` be two types that share the relevant vertex.

In singular-series notation one introduces "joint-system" constants for the
five-form systems appearing in second moments:

- Label second moment constant `\kappa^Z_{\tau_1,\tau_2}` for the system with
  prime forms
  \[
    P,\ q_1,\ q_1',\ q_2,\ q_2',
  \]
  where `q_i'=(a_i q_i+\sigma_i P)/b_i`.
- X-side second moment constant `\kappa^X_{\tau_1,\tau_2}` for the system with
  shared `q` (hence shared `x=2aq`) and prime forms
  \[
    q,\ q_1',\ q_2',\ P_1,\ P_2.
  \]
- Y-side second moment constant `\kappa^Y_{\tau_1,\tau_2}` defined symmetrically.

The conditional-factor identities needed (verbatim from
`external-55-gtz-moment-finalization-response.md`, with `\lambda_\tau=\kappa_\tau`)
are:
\[
  \kappa^Z_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \zeta_\pi},
\]
\[
  \kappa^X_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \xi_{a,r}},
  \qquad
  \kappa^Y_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \eta_{b,r'}}.
\]
Under the EP689 prime-class convention `\zeta_\pi=1`, so the label identity is
just `\kappa^Z=\kappa_{\tau_1}\kappa_{\tau_2}`.

### 7.2 Why the identities are automatic in normalized W-tricked form

In the normalized W-tricked formulation (Section 6), every prime form is counted
with the same mean-1 normalization in its residue class.  Therefore:

- the "one-variable" densities are exactly `\zeta_\pi dt`, `dQ`, `dQ'`;
- the first-moment constant attached to any system is the same object that
  appears when you condition on a shared variable;
- so the conditional identities above reduce to the tautology that
  \[
    \mathrm{density}(A\cap B)
    =
    \frac{\mathrm{density}(A)\,\mathrm{density}(B)}{\mathrm{density}(\text{shared})},
  \]
  with all densities interpreted in the same vertex measures.

In particular, the moment argument does not need a separate "prime pairs" input;
it needs only that GTZ applies to the relevant finite-complexity systems, and
that all systems are written in the same normalized scale.

### 7.3 What must be checked in fixed-modulus singular-series language

If one insists on writing everything in raw prime-indicator or raw singular-series
language, then one must explicitly verify the Euler-factor identities behind the
conditional-factor equations above.

Concretely:

1. For each relevant linear-forms system (3-form edge totals; 5-form label/X/Y
   second moments), define its singular series as an Euler product
   `\prod_p \beta_p`.
2. For each prime `p`, show the *local* conditional identity
   \[
     \beta_p^{\mathrm{union}}
     =
     {\beta_p^{(1)}\,\beta_p^{(2)}\over \beta_p^{\mathrm{shared}}}.
   \]
3. Multiply over `p` to obtain the global identity for `\kappa^Z,\kappa^X,\kappa^Y`.

In the EP689 setup this check is routine because:

- Primes dividing the coefficients `a,b` lie in `S`, hence divide `W` and so
  divide `W_0`; the fixed residue restrictions force all prime forms to be units
  modulo those primes, making the local factors at `p|W_0` trivial.
- For `p\nmid W_0`, finite complexity (no proportional linear forms) ensures the
  local density is computed by elementary counting modulo `p` and the "union vs
  product/shared" identity holds because the two subsystems interact only through
  the shared prime form.

This singular-series bookkeeping is separate from the diagonal/collision issue:
diagonal contributions (e.g. identical edges, form collisions) are handled by the
lower-dimensional estimates already listed in the moment response and the
execution checklist (they contribute `O(\log n)=o(n/\log n)` after weighting).


## 8. Bottom line for aligning Lemma 7.1 with the moment writeup

To make `typed-kernel-lift-proof.md` Lemma 7.1 match the GTZ moment analysis:

1. Use the modulus convention `W_0=2W` (and `\widetilde W` only as a proof device).
2. Use the prime-class scale `N_{W_0}(n)=n/(\varphi(W_0)\log n)`.
3. Fix vertex measures `d\mu_Z(\pi,t)=\zeta_\pi dt` with `\zeta_\pi=1`,
   `d\mu_X=dQ`, `d\mu_Y=dQ'`, hence `\xi_{a,r}=1/(2a)`, `\eta_{b,r'}=1/(2b)`.
4. Define `\kappa_\tau` by `(\kappa-def)`; in any GTZ moment note set
   `\lambda_\tau=\kappa_\tau`.
5. Either:
   - cite/apply GTZ in the normalized W-tricked form (Section 6), in which case
     the conditional local-factor identities are automatic; or
   - in raw singular-series language, include an explicit lemma checking the
     Euler-factor identities for the relevant 5-form systems.


## 9. Remaining gaps (as of 2026-04-25)

This ledger resolves the *normalization choices*, but the following writeup tasks
remain elsewhere:

- The GTZ moment writeup must explicitly state the version of the GTZ
  linear-forms theorem being used (preferably normalized W-tricked), including
  how congruence restrictions are imposed and how the `w`-parameter is removed.
- If the moment writeup is written in fixed-modulus singular-series language, it
  must include (or cite) the Euler-factor verification corresponding to the
  conditional-factor identities in Section 7.1.
- Notational consistency: some files use `W_0` for `\prod_{s\in S}s`; this ledger
  uses `W` for that quantity and reserves `W_0` for `2W`.
