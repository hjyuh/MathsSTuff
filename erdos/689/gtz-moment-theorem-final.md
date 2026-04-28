# Final GTZ weighted moment theorem on a fixed finite core

Created: 2026-04-25

This note packages the GTZ arithmetic input for the EP689 averaged-nibble route
into one theorem/proof statement. It is the finished theorem-level version of
the fixed-core moment proposition behind P1--P3 of
`gtz-kahn-proof-chain.md`, written in the normalization of
`gtz-normalization-ledger.md`.

The theorem is conditional only on the standard finite-complexity
Green--Tao--Ziegler linear-forms theorem in its normalized W-tricked form for a
finite list of systems. No pointwise Hardy--Littlewood input is used.


## 1. Frozen setup and normalization

Fix:

1. a finite set \(S\subset\{7,11,13,\ldots\}\), and
   \[
     W:=\prod_{s\in S}s,\qquad W_0:=2W;
   \]
2. a parameter \(1/5<\beta<1/2\);
3. a coefficient-tail parameter \(\varepsilon>0\) and a finite core of types
   \[
     \mathcal T_\varepsilon\subset
     \{(a,b,\sigma,r,r',\pi)\};
   \]
4. the bounded feasible kernels \(g_\tau\) from
   `typed-kernel-lift-proof.md`, with limiting side profiles
   \(\lambda_X,\lambda_Y\) and fixed slack \(\gamma>0\).

All notation below uses the ledger convention:
\[
  N_{W_0}(n):={n\over \varphi(W_0)\log n},
\]
\[
  d\mu_Z(\pi,t)=\zeta_\pi\,dt,\qquad \zeta_\pi=1,
\]
\[
  d\mu_X(a,r,Q)=dQ,\qquad d\mu_Y(b,r',Q')=dQ',
\]
so
\[
  \xi_{a,r}={1\over 2a},\qquad \eta_{b,r'}={1\over 2b}.
\]
For each retained type \(\tau=(a,b,\sigma,r,r',\pi)\), the local constant
\(\kappa_\tau\) is the one defined in `gtz-normalization-ledger.md` and
`typed-kernel-lift-proof.md`:
\[
  \sum_{\substack{
        q\equiv r\ (W_0),\ q'\equiv r'\ (W_0)\\
        q,q',\ \sigma(bq'-aq)\ {\rm prime}\\
        \sigma(bq'-aq)\equiv\pi\ (W_0)
      }}
    {\log^2 n\over n}\,
    F(q/n,q'/n)
  =
  \left(N_{W_0}(n)+o(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau}F(Q,Q')\,dQ\,dQ'.
\]
If another note writes this constant as \(\lambda_\tau\), then here
\(\lambda_\tau=\kappa_\tau\).

Write \(X_n^{\rm core}\) and \(Y_n^{\rm core}\) for the side vertices coming
from the fixed finite core, and
\[
  Z_n:=\mathcal R_\beta(n).
\]
Since \(\mathcal B\) is fixed and \(\beta>1/5\), prime number theory in
residue classes gives
\[
  |Z_n|\asymp N_{W_0}(n).
\]
For an edge \(e=(x,y,P)\) of type \(\tau\), with \(x=2aq\), \(y=2bq'\), set
\[
  w_e:={\log^2 n\over n}\,g_\tau(q/n,q'/n).
\]
The discrete loads are
\[
  L_Z(P):=\sum_{e\ni P} w_e,\qquad
  L_X(x):=\sum_{e\ni x} w_e,\qquad
  L_Y(y):=\sum_{e\ni y} w_e.
\]
For \(x=2aq\in X_n^{\rm core}\) of type \((a,r)\), define
\[
  \lambda_X(x):=\lambda_X(a,r,q/n),
\]
and similarly for \(y=2bq'\in Y_n^{\rm core}\),
\[
  \lambda_Y(y):=\lambda_Y(b,r',q'/n).
\]


## 2. The exact GTZ systems

Fix a small-prime cutoff \(w\), put \(W(w):=\prod_{p\le w}p\), and define
\[
  \widetilde W:=\operatorname{lcm}(W_0,W(w)).
\]
During the \(n\to\infty\) limit, \(w\) is fixed. All residue constraints are
lifted to \(\widetilde W\), and all prime variables are written in the form
\[
  \widetilde W m+\alpha
\]
with \(\alpha\in(\mathbf Z/\widetilde W\mathbf Z)^\times\). For such \(\alpha\),
use the normalized W-tricked von Mangoldt weight
\[
  \Lambda_{\widetilde W,\alpha}(m)
  :=
  {\varphi(\widetilde W)\over \widetilde W}\,\Lambda(\widetilde Wm+\alpha).
\]

The finite-complexity systems that occur are exactly these.

### 2.1 Edge totals

For \(\tau=(a,b,\sigma,r,r',\pi)\), the three prime forms are
\[
  q,\qquad q',\qquad P=\sigma(bq'-aq).
\]
After the W-trick this is a 2-variable, 3-form system.

### 2.2 Label second moments

For \(\tau_1,\tau_2\) sharing a label \(P\), use variables \(P,q_1,q_2\) (or
equivalently \(P,t_1,t_2\)), with
\[
  q_i'={a_iq_i+\sigma_iP\over b_i}.
\]
The prime forms are
\[
  P,\qquad q_1,\qquad q_1',\qquad q_2,\qquad q_2'.
\]
After removing the identical-edge diagonal, this is a 3-variable, 5-form
finite-complexity system.

### 2.3 X-side second moments

For \(\tau_1,\tau_2\) contributing to the same \(X\)-fiber, one necessarily has
\[
  a_1=a_2=a,\qquad r_1=r_2=r,
\]
and the shared prime is \(q\). The five prime forms are
\[
  q,\qquad q_1',\qquad q_2',\qquad
  P_1=\sigma_1(b_1q_1'-aq),\qquad
  P_2=\sigma_2(b_2q_2'-aq).
\]
This is again a 3-variable, 5-form system after removing the diagonal
\(q_1'=q_2'\) when \(\tau_1=\tau_2\).

### 2.4 Y-side second moments

Symmetrically, for a shared \(Y\)-fiber one has \(b_1=b_2=b\), \(r_1'=r_2'=r'\),
and the prime forms are
\[
  q',\qquad q_1,\qquad q_2,\qquad
  P_1=\sigma_1(bq'-a_1q_1),\qquad
  P_2=\sigma_2(bq'-a_2q_2).
\]


## 3. The theorem

### Theorem 3.1 (Normalized W-tricked GTZ weighted moments on a fixed core)

Assume the normalized W-tricked Green--Tao--Ziegler linear-forms theorem holds,
uniformly over the finite type set \(\mathcal T_\varepsilon\) and all
compatible residue lifts modulo \(\widetilde W\), for the systems in Section 2
with bounded Lipschitz weights on the relevant rational polytopes.

Assume also:

1. locally obstructed residue lifts have already been discarded, so every
   retained type has \(\kappa_\tau>0\);
2. the kernels \(g_\tau\) are those from `typed-kernel-lift-proof.md`, hence
   the limiting label equation is \(L_Z^{\lim}=1\) and the limiting side
   profiles satisfy
   \[
     \lambda_X\le 1-2\gamma,\qquad \lambda_Y\le 1-2\gamma;
   \]
3. sharp polygonal cutoffs and bounded kernels are replaced by Lipschitz
   approximants \(F_{\tau,\eta}\) and \(g_{\tau,\eta}\) with the properties
   recorded in `gtz-execution-checklist.md`, and \(\eta>0\) is held fixed while
   \(n\to\infty\).

Then, with \((\varepsilon,w,\eta)\) fixed and \(n\to\infty\),

\[
  \sum_{P\in Z_n} L_Z(P)=|Z_n|+o_{w,\eta}(|Z_n|),
  \tag{3.1}
\]
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o_{w,\eta}(|Z_n|),
  \tag{3.2}
\]
\[
  \sum_{x\in X_n^{\rm core}}(L_X(x)-\lambda_X(x))^2=o_{w,\eta}(|Z_n|),
  \tag{3.3}
\]
\[
  \sum_{y\in Y_n^{\rm core}}(L_Y(y)-\lambda_Y(y))^2=o_{w,\eta}(|Z_n|).
  \tag{3.4}
\]

After first removing \(w\) by the standard iterated-limit or diagonal choice
\(w=w(n)\to\infty\), and then sending \(\eta\to0\), the same conclusions hold
with \(o(|Z_n|)\) in place of \(o_{w,\eta}(|Z_n|)\).

In particular, these are exactly the fixed-core arithmetic inputs needed by
`awn-preprocessing-mass-loss.md`, now stated on the \(|Z_n|\)-scale required
there.


## 4. Proof

Choose Lipschitz approximants \(F_{\tau,\eta}\) for \(1_{\Omega_\tau}\) and
\(g_{\tau,\eta}\) for \(g_\tau\), and write
\[
  G_{\tau,\eta}:=g_{\tau,\eta}F_{\tau,\eta}.
\]
All GTZ applications below are first made with \(G_{\tau,\eta}\); the sharp
kernel is recovered at the end of the proof.

### Step 1: smoothing and boundary reduction

For each fixed \(\tau\), the boundary \(\partial\Omega_\tau\) is polygonal, so
its \(\eta\)-neighborhood has area \(O_\tau(\eta)\). Because the kernels are
bounded and the type set is finite, replacing \(g_\tau 1_{\Omega_\tau}\) by
\(G_{\tau,\eta}\) changes every 3-form first moment and every 5-form second
moment by
\[
  O_\eta(N_{W_0}(n))
  =
  O_\eta(|Z_n|),
\]
uniformly over \(\tau,\tau_1,\tau_2\). After \(n\to\infty\), this becomes
\(o_\eta(|Z_n|)\), and then \(\eta\to0\) removes the smoothing error.

Small-prime exceptions, where one of the prime forms is \(\le w\), contribute
only \(o_w(|Z_n|)\) by the crude count already recorded in
`gtz-execution-checklist.md`: there are only \(O(w/\log w)\) such primes, and
the remaining variables still range over intervals of length \(\asymp n\).

Thus it is enough to prove the theorem for the smoothed weights
\(G_{\tau,\eta}\) on the truncated domain with all prime forms \(>w\).

### Step 2: edge totals

Fix \(\tau=(a,b,\sigma,r,r',\pi)\) and one admissible residue lift modulo
\(\widetilde W\). The W-tricked edge system is the 2-variable, 3-form system
from Section 2.1. Its coefficient vectors are
\[
  (1,0),\qquad (0,1),\qquad (-\sigma a,\sigma b),
\]
which are pairwise non-proportional because \(\gcd(a,b)=1\).

By the normalized W-tricked GTZ theorem, the weighted prime count with test
function \(G_{\tau,\eta}\) is
\[
  \left(N_{W_0}(n)+o_{w,\eta}(N_{W_0}(n))\right)
  \kappa_\tau
  \int_{\Omega_\tau} G_{\tau,\eta}(Q,Q')\,dQ\,dQ'.
\]
Summing over the finitely many residue lifts and over \(\tau\in\mathcal
T_\varepsilon\) produces the discrete first moment
\[
  \sum_{P\in Z_n}L_Z(P).
\]
Because the local constants are exactly the ledger constants \(\kappa_\tau\),
and because the limiting label equation from `typed-kernel-lift-proof.md` is
\[
  L_Z^{\lim}(\pi,t)=1
  \quad\text{for a.e. }(\pi,t)\in\mathcal B\times(1/5,\beta],
\]
the summed main term is precisely the label measure of \(Z_n\), namely
\(|Z_n|+o(|Z_n|)\). This proves (3.1).

The same 3-form theorem with any bounded test on the shared side variable gives
the first-moment identities needed later for the side cross terms. In
particular, the profiles \(\lambda_X,\lambda_Y\) are bounded and piecewise
continuous on the fixed finite core, so one more Lipschitz approximation gives
the same asymptotic with \(\lambda_X,\lambda_Y\) as test functions:
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)\lambda_X(x)
  =
  \sum_{x\in X_n^{\rm core}}\lambda_X(x)^2
  +o_{w,\eta}(|Z_n|),
  \tag{4.1}
\]
\[
  \sum_{y\in Y_n^{\rm core}}L_Y(y)\lambda_Y(y)
  =
  \sum_{y\in Y_n^{\rm core}}\lambda_Y(y)^2
  +o_{w,\eta}(|Z_n|).
  \tag{4.2}
\]

### Step 3: label second moments

Expand
\[
  \sum_{P\in Z_n}L_Z(P)^2
\]
as a sum over ordered pairs of edges with common label \(P\). For each pair of
types \((\tau_1,\tau_2)\), the off-diagonal terms are governed by the 3-variable,
5-form system in Section 2.2. After removing the identical-edge diagonal, the
five prime forms are pairwise non-proportional, so the system has finite
complexity.

Because the theorem is used in normalized W-tricked form, all one-form
densities are already normalized to mean \(1\) in their residue classes. Hence
the joint-system constant is automatic:
\[
  \kappa^Z_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \zeta_\pi}
  =
  \kappa_{\tau_1}\kappa_{\tau_2},
  \tag{4.3}
\]
since \(\zeta_\pi=1\). This is exactly the local-factor identity from
`gtz-normalization-ledger.md`, and no separate Euler-product check remains.

Summing the GTZ main terms over \(\tau_1,\tau_2\) therefore reconstructs the
quadratic label load
\[
  \int_{\mathcal B\times(1/5,\beta]} \bigl(L_Z^{\lim}(\pi,t)\bigr)^2\,dt.
\]
Since \(L_Z^{\lim}=1\), this equals the label measure of \(Z_n\), so
\[
  \sum_{P\in Z_n}L_Z(P)^2=|Z_n|+o_{w,\eta}(|Z_n|).
  \tag{4.4}
\]

The diagonal \(e_1=e_2\) contributes only at total-edge scale:
\[
  O\!\left({n^2\over(\log n)^3}\right)\cdot
  O\!\left({\log^4 n\over n^2}\right)
  =
  O(\log n)
  =
  o(|Z_n|).
\]
Any form collision or identical-form slice is contained in such a lower-
dimensional diagonal or in an empty residue block, so it is also negligible.

Combining (4.4) with the first-moment identity (3.1) gives
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2
  =
  \sum_{P\in Z_n}L_Z(P)^2
  -2\sum_{P\in Z_n}L_Z(P)
  +|Z_n|
  =
  o_{w,\eta}(|Z_n|),
\]
which is (3.2).

### Step 4: X-side second moments

Now expand
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)^2.
\]
Mixed terms can only occur inside a common fiber \((a,r)\), because distinct
\((a,r)\)-fibers are disjoint for all sufficiently large \(n\). For each
admissible \((\tau_1,\tau_2)\) with the same \(a\) and \(r\), the off-diagonal
terms are governed by the 3-variable, 5-form system from Section 2.3.

Again the normalized W-tricked theorem gives the conditional constant
automatically:
\[
  \kappa^X_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \xi_{a,r}},
  \qquad
  \xi_{a,r}={1\over 2a}.
  \tag{4.5}
\]
Therefore the summed main term is exactly the continuum quadratic side profile:
\[
  \sum_{x\in X_n^{\rm core}}L_X(x)^2
  =
  \sum_{x\in X_n^{\rm core}}\lambda_X(x)^2
  +o_{w,\eta}(|Z_n|).
  \tag{4.6}
\]

The repeated-edge diagonal \(q_1'=q_2'\) contributes only \(O(\log n)\), by the
same calculation as in the label case, hence is negligible on the \(|Z_n|\)
scale.

Now combine (4.6) with the cross-term identity (4.1):
\[
  \sum_{x\in X_n^{\rm core}}(L_X(x)-\lambda_X(x))^2
  =
  \sum_x L_X(x)^2
  -2\sum_x L_X(x)\lambda_X(x)
  +\sum_x \lambda_X(x)^2
  =
  o_{w,\eta}(|Z_n|).
\]
This proves (3.3).

### Step 5: Y-side second moments

The \(Y\)-side is symmetric. The relevant 3-variable, 5-form system is the one
from Section 2.4, and the normalized conditional constant is
\[
  \kappa^Y_{\tau_1,\tau_2}
  =
  {\kappa_{\tau_1}\kappa_{\tau_2}\over \eta_{b,r'}},
  \qquad
  \eta_{b,r'}={1\over 2b}.
  \tag{4.7}
\]
Hence
\[
  \sum_{y\in Y_n^{\rm core}}L_Y(y)^2
  =
  \sum_{y\in Y_n^{\rm core}}\lambda_Y(y)^2
  +o_{w,\eta}(|Z_n|),
\]
and together with (4.2),
\[
  \sum_{y\in Y_n^{\rm core}}(L_Y(y)-\lambda_Y(y))^2
  =
  o_{w,\eta}(|Z_n|).
\]
This is (3.4).

### Step 6: removing \(w\) and \(\eta\)

All preceding estimates hold with \((\varepsilon,w,\eta)\) fixed. Because the
type set is finite, the \(o_{w,\eta}(1)\) terms are uniform over
\(\tau,\tau_1,\tau_2\). The checklist `gtz-execution-checklist.md` already
records the standard order of limits:

1. prove the GTZ asymptotics for fixed \(w,\eta\);
2. pass \(w\to\infty\), or choose a diagonal \(w=w(n)\to\infty\) slowly;
3. then send \(\eta\to0\).

This removes the small-prime truncation and the smoothing error, and upgrades
(3.1)--(3.4) to the stated \(o(|Z_n|)\) form. The theorem follows. \(\square\)


## 5. AWN handoff

The point of Theorem 3.1 is that the moment errors are now already on the
\(|Z_n|\)-scale used in `awn-preprocessing-mass-loss.md`:

- label normalization uses (3.2);
- heavy-side deletion uses (3.3) and (3.4) together with
  \(\lambda_X,\lambda_Y\le 1-2\gamma\);
- the atom bound is immediate from
  \[
    \max_e w_e\ll {\log^2 n\over n}=o(1).
  \]

For the final proof draft, AWN is applied directly to the finite-core
hypergraph \(X_n^{\rm core}\sqcup Y_n^{\rm core}\sqcup Z_n\).  In that
formulation the non-core tail term in `awn-preprocessing-mass-loss.md` is
simply absent, i.e. \(\tau=0\).  The coefficient tails are not deleted as
weighted edges; they remain as unmatched residual targets and are absorbed
later by the singleton robust-prime cleanup.

Equivalently, if one works inside a larger full-coefficient weighted
hypergraph first, then one must also prove the old
\(\tau=o_\varepsilon(|Z_n|)\) edge-tail estimate.  The current final proof
chooses the cleaner finite-core-only route.


## 6. What remains outside this note

This note closes the fixed-core GTZ moment proposition, but it does not by
itself supply:

1. the final check of Kahn's exact smallness parameter \(\alpha(t)\);
2. the later count of coefficient-tail residual targets and the
   pair-plus-singleton cleanup steps.

Those are downstream tasks, not GTZ moment gaps.
