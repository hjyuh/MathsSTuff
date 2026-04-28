# GTZ Moment Side: Execution Checklist (Assuming Kernel Feasibility)

Created: 2026-04-25

Goal: given a fixed finite coefficient core and feasible limiting kernels, execute the Green--Tao--Ziegler (GTZ) linear-forms-in-primes machinery to verify the averaged first/second-moment estimates needed for AWN (averaged weighted nibble / Kahn rounding).

This file is intentionally a proof-outline checklist: each box should correspond to a lemma/proposition whose hypotheses, conclusion, and parameter-dependence are explicit.

---

## 0. Nonnegotiable order of limits

- [ ] **Freeze global parameters:** fix \(S\), hence \(W_0:=\prod_{s\in S}s\); fix \(\beta\in(0,1/2)\); fix a coefficient-tail parameter \(\varepsilon>0\).
- [ ] **Freeze the finite coefficient core** \(\mathcal C_\varepsilon\): finite sets of coefficients \(a\in\mathcal A_1(\varepsilon)\) (odd) and \(b\in\mathcal A_2(\varepsilon)\) (even), and the induced finite list of admissible residue/type data (defined below).
- [ ] **Assume kernel feasibility on the core:** kernels \(g_\tau\) are fixed and bounded, and the limiting load equations hold with slack \(\gamma=\gamma(S,\beta,\varepsilon)>0\):
  \[
    L_Z^{\lim}(t,\pi)=1 \text{ a.e. on }(1/5,\beta]\times\mathcal B,
    \qquad
    L_X^{\lim}(\cdot)\le 1-2\gamma,\quad L_Y^{\lim}(\cdot)\le 1-2\gamma.
  \]
- [ ] **Choose W-trick parameter:** pick \(w\ge1\), set \(W(w):=\prod_{p\le w}p\), and let \(\widetilde W:=\mathrm{lcm}(W_0,W(w))\). Treat \(w\) as fixed during all \(n\to\infty\) arguments.
- [ ] **Choose smooth-approximation parameter(s):** pick a smoothing/approximation scale \(\eta>0\) for (i) polygonal cutoffs and (ii) bounded kernels (details in Section 4). Treat \(\eta\) as fixed during all \(n\to\infty\) arguments.
- [ ] **Execute arithmetic limits:** prove all GTZ moment asymptotics as \(n\to\infty\) with \((\varepsilon,\mathcal C_\varepsilon,w,\eta)\) fixed.
- [ ] **Remove auxiliary parameters:** after the \(n\to\infty\) estimates are in hand, pass \(w\to\infty\) (or choose a standard \(w=w(n)\to\infty\) slowly) and then \(\eta\to0\) to recover sharp cutoffs and the unsmoothed kernels.
- [ ] **Only after combinatorial rounding:** apply AWN/Kahn on the core for each fixed \(\varepsilon\); only then send \(\varepsilon\to0\) to remove the coefficient tail.

---

## 1. Fixed core/types, edge relation, and weights

- [ ] **Vertices and labels (core restriction understood):**
  \[
    X:=A_1(n),\qquad Y:=A_2(n),\qquad Z:=\mathcal R_\beta(n)=\{P\in(n/5,\beta n]: P\text{ robust}\}.
  \]
- [ ] **Coefficient-core parametrization:** within \(\mathcal C_\varepsilon\),
  \[
    x=2a q,\qquad y=2b q',\qquad P=\sigma(bq'-aq),
  \]
  where \(a\) is odd, \(b\) is even, \(\sigma\in\{\pm1\}\), and \(\gcd(a,b)=1\) is imposed (remove \(\gcd(a,b)>1\) blocks at the outset).
- [ ] **Fixed residue data modulo \(W_0\):** for each core block, fix
  \[
    q\equiv r\pmod{W_0},\qquad q'\equiv r'\pmod{W_0},\qquad P\equiv \pi\pmod{W_0},
  \]
  with \(\pi\in\mathcal B\subset(\mathbf Z/W_0\mathbf Z)^\times\) (robust classes).
- [ ] **Type index:** let
  \[
    \tau=(a,b,\sigma,r,r',\pi),
  \]
  and let \(\mathcal T_\varepsilon\) be the finite set of admissible types after removing empty/locally-obstructed residue choices (singular series \(0\)).
- [ ] **Polygonal support (scaled variables \(Q=q/n\), \(Q'=q'/n\)):** define
  \[
    \Omega_\tau:=\Bigl\{(Q,Q'):\ 0<Q\le \frac1{2a},\ 0<Q'\le\frac1{2b},\ \frac15<\sigma(bQ'-aQ)\le \beta\Bigr\}.
  \]
- [ ] **Edge kernels and weights (assumed feasible):** each \(\tau\) has a bounded measurable kernel \(g_\tau(Q,Q')\ge0\) supported on \(\Omega_\tau\), and each edge \(e=(x,y,P)\) of type \(\tau\) receives
  \[
    w_e=\frac{\log^2 n}{n}\,g_\tau(q/n,q'/n).
  \]
  (The exact prefactor can be changed, but it must make \(\max_e w_e=o(1)\) and keep loads \(O(1)\).)
- [ ] **Loads:** for \(v\in X\cup Y\cup Z\),
  \[
    L_X(x):=\sum_{e\ni x}w_e,\qquad L_Y(y):=\sum_{e\ni y}w_e,\qquad L_Z(P):=\sum_{e\ni P}w_e.
  \]

---

## 2. W-trick and residue lifting (discrete bookkeeping)

Everything below is executed with \(\widetilde W\) fixed.

- [ ] **Excise small primes:** remove all edges where any prime variable in the relevant system satisfies \(\le w\). Verify this contributes
  \[
    o(|Z|)\quad\text{to first moments and }o(|Z|)\text{ to the second-moment sums},
  \]
  by crude bounds using \(\#\{p\le w\}=O(w/\log w)\) and that the remaining variables range \(\asymp n\).
- [ ] **Lift all fixed congruence restrictions to \(\widetilde W\):**
  choose (finite) sets of residue classes
  \[
    \mathcal R_{q}(\tau)\subset(\mathbf Z/\widetilde W\mathbf Z)^\times,\qquad
    \mathcal R_{q'}(\tau)\subset(\mathbf Z/\widetilde W\mathbf Z)^\times,\qquad
    \mathcal R_{P}(\tau)\subset(\mathbf Z/\widetilde W\mathbf Z)^\times
  \]
  so that reducing mod \(W_0\) recovers \(r,r',\pi\) and the robust restriction \(\pi\in\mathcal B\), and so that the system is locally admissible (no prime divides all forms).
- [ ] **Rewrite prime variables in fixed residues:** for each choice of residue lifts
  \[
    q=\widetilde W m+\alpha,\qquad q'=\widetilde W m'+\alpha',
  \]
  with \(\alpha\in\mathcal R_q(\tau)\), \(\alpha'\in\mathcal R_{q'}(\tau)\); similarly, for label-moment parameterizations, enforce \(P=\widetilde W M+\alpha_P\) with \(\alpha_P\in\mathcal R_P(\tau)\).
- [ ] **Use W-tricked von Mangoldt weights:** define for \((\alpha,\widetilde W)=1\)
  \[
    \Lambda_{\alpha,\widetilde W}(m):=\frac{\varphi(\widetilde W)}{\widetilde W}\,\Lambda(\widetilde W m+\alpha).
  \]
  All GTZ applications should be stated in terms of averages of products of \(\Lambda_{\alpha,\widetilde W}\) along affine-linear forms.
- [ ] **Record the local factor conventions:** decide once whether the main term is expressed as a singular series \(\mathfrak S(\Psi)\) times a singular integral, or in the normalized W-tricked form where the main term is \(1+o(1)\) and the local factor is pushed into the residue lifting. Use one convention consistently across all systems so that the continuum load equations match the discrete main terms.

---

## 3. Finite coefficient core: what must be proved uniformly

- [ ] **Finite list principle:** because \(\mathcal T_\varepsilon\) is finite, it suffices to prove each GTZ estimate with an error \(o_{w,\eta}(1)\) uniform over:
  \[
    \tau\in\mathcal T_\varepsilon,\quad (\tau_1,\tau_2)\in\mathcal T_\varepsilon^2,
  \]
  and over all lifted residue choices in Section 2.
- [ ] **Remove empty/degenerate blocks before GTZ:** verify explicitly that the following pieces are excluded from \(\mathcal T_\varepsilon\) (or are handled as negligible errors):
  - \(\gcd(a,b)>1\) (block empty for large \(n\));
  - residue lifts with local obstruction (singular series \(=0\));
  - orientations/residue choices forcing \(P\le0\) or disjoint from \((n/5,\beta n]\).
- [ ] **Complexity checks (per system):** for each linear-forms system used later, certify the GTZ finite-complexity condition (no two distinct forms are affinely dependent over \(\mathbf Q\), after discarding the diagonals listed in Section 6).

---

## 4. Smooth approximation layer (kernel + polytope)

GTZ statements are cleanest for Lipschitz weights on a box; polygonal indicators are handled by approximation.

- [ ] **Fix a smoothing model:** choose \(\eta>0\) and for each \(\tau\) construct a Lipschitz weight \(F_{\tau,\eta}(Q,Q')\) such that
  \[
    0\le F_{\tau,\eta}\le 1,\qquad
    1_{\Omega_\tau^{-\eta}}\le F_{\tau,\eta}\le 1_{\Omega_\tau^{+\eta}},
  \]
  where \(\Omega_\tau^{\pm\eta}\) are \(\eta\)-inner/outer neighborhoods of \(\Omega_\tau\) (in \(\ell^\infty\) say), and \(\|F_{\tau,\eta}\|_{\mathrm{Lip}}\ll_\tau \eta^{-1}\).
- [ ] **Approximate kernels by Lipschitz kernels:** choose \(g_{\tau,\eta}\) Lipschitz with
  \[
    0\le g_{\tau,\eta}\le \|g_\tau\|_\infty,\qquad \|g_{\tau,\eta}-g_\tau\|_{L^1(\Omega_\tau)}\le \eta,\qquad \|g_{\tau,\eta}\|_{\mathrm{Lip}}\ll_\tau \eta^{-1}.
  \]
- [ ] **Reduction statement (must be proved once):** show that replacing \(g_\tau 1_{\Omega_\tau}\) by \(g_{\tau,\eta}F_{\tau,\eta}\) changes:
  - each first-moment sum by \(o_\eta(|Z|)\) after \(n\to\infty\);
  - each second-moment sum by \(o_\eta(|Z|)\) after \(n\to\infty\);
  uniformly over \(\tau,\tau_1,\tau_2\in\mathcal T_\varepsilon\).
  (This uses only boundary-measure \(O_\tau(\eta)\) and boundedness of kernels.)

---

## 5. The exact GTZ systems to run (edge + moments)

All systems below are stated in their *post*-W-trick form: variables are the lattice variables \((m,\dots)\), and each prime form is an affine-linear form in those variables to which \(\Lambda_{\alpha,\widetilde W}\) is applied.

### 5.1 Edge totals (per type)

- [ ] **For each \(\tau=(a,b,\sigma,r,r',\pi)\):** for each choice of residue lifts \((\alpha,\alpha')\) compatible with \(\tau\), define in variables \((m,m')\)
  \[
    L_1(m,m')=\widetilde W m+\alpha,\quad
    L_2(m,m')=\widetilde W m'+\alpha',
  \]
  \[
    L_3(m,m')=\sigma\bigl(b(\widetilde W m'+\alpha')-a(\widetilde W m+\alpha)\bigr).
  \]
  Write \(L_3(m,m')=\widetilde W\cdot L_3^\#(m,m')+\alpha_3\) where
  \[
    L_3^\#(m,m'):=\sigma(bm'-am),\qquad \alpha_3:=\sigma(b\alpha'-a\alpha)\pmod{\widetilde W},
  \]
  and interpret \(\Lambda_{\alpha_3,\widetilde W}(L_3^\#(m,m'))\) as \(0\) unless \(L_3^\#(m,m')\ge1\).
  The edge-weighted prime count to estimate is
  \[
    S_\tau(n;\eta,w):=
    \sum_{(m,m')\in K_\tau(n)}
      \Lambda_{\alpha,\widetilde W}(m)\,
      \Lambda_{\alpha',\widetilde W}(m')\,
      \Lambda_{\alpha_3,\widetilde W}(L_3^\#(m,m'))\,
      \Bigl(g_{\tau,\eta}F_{\tau,\eta}\Bigr)\Bigl(\frac{L_1}{n},\frac{L_2}{n}\Bigr),
  \]
  where \(K_\tau(n)\) is the induced box/convex domain after scaling and after enforcing the \(P\)-range \(1/5< L_3/n \le \beta\).
- [ ] **GTZ invocation (2 variables, 3 forms):** apply the GTZ linear-forms theorem to get
  \[
    S_\tau(n;\eta,w)
    =
    \mathrm{MT}_\tau(\eta,w)\,n^2
    +o_{w,\eta}(n^2),
  \]
  uniformly in \(\tau\) and residue lifts, where \(\mathrm{MT}_\tau(\eta,w)\) is the singular-series/singular-integral main term consistent with the feasibility equations.

### 5.2 Label-load first and second moments (M1 ledger)

Define \(L_Z(P)\) from the discrete hypergraph weights \(w_e\).

- [ ] **First moment:** verify
  \[
    \sum_{P\in Z} L_Z(P)
    =
    \sum_{\tau\in\mathcal T_\varepsilon}\ \sum_{\text{residue lifts}} \sum_{(q,q')\in E_\tau} w_{(q,q')}
    =
    |Z|+o(|Z|),
  \]
  by reducing to the edge totals in 5.1 and using the feasibility condition \(L_Z^{\lim}=1\) (this is where the continuum equation is used).

- [ ] **Second moment expansion:**
  \[
    \sum_{P\in Z} L_Z(P)^2
    =
    \sum_{\tau_1,\tau_2\in\mathcal T_\varepsilon}
      \sum_{\substack{e_1\in E_{\tau_1},\ e_2\in E_{\tau_2}\\ \mathrm{label}(e_1)=\mathrm{label}(e_2)}}
        w_{e_1}w_{e_2}.
  \]
  Split into diagonal \(e_1=e_2\) and off-diagonal \(e_1\ne e_2\) (see Section 6).

- [ ] **Parameterize the common-label constraint (off-diagonal):** for each \(\tau=(a,b,\sigma,\dots)\), fix integers \(u_\tau,v_\tau\) with \(b v_\tau-a u_\tau=1\). Then solutions to
  \[
    P=\sigma(bq'-aq)
  \]
  are
  \[
    q=u_\tau(\sigma P)+b t,\qquad q'=v_\tau(\sigma P)+a t.
  \]
  For \((\tau_1,\tau_2)\), use variables \((P,t_1,t_2)\) and prime forms
  \[
    P,\quad
    q_1=u_{\tau_1}(\sigma_1 P)+b_1 t_1,\quad q'_1=v_{\tau_1}(\sigma_1 P)+a_1 t_1,
  \]
  \[
    q_2=u_{\tau_2}(\sigma_2 P)+b_2 t_2,\quad q'_2=v_{\tau_2}(\sigma_2 P)+a_2 t_2.
  \]
  Encode all congruence restrictions (including robust class) as residue classes of \((P,t_1,t_2)\bmod\widetilde W\), and encode interval constraints as a fixed rational polytope in \((P/n,t_1/n,t_2/n)\).

- [ ] **GTZ invocation (3 variables, 5 forms):** apply GTZ to the system above with weight
  \[
    (P,t_1,t_2)\mapsto
    \Bigl(g_{\tau_1,\eta}F_{\tau_1,\eta}\Bigr)\Bigl(\frac{q_1}{n},\frac{q'_1}{n}\Bigr)\,
    \Bigl(g_{\tau_2,\eta}F_{\tau_2,\eta}\Bigr)\Bigl(\frac{q_2}{n},\frac{q'_2}{n}\Bigr),
  \]
  after removing the diagonals in Section 6, to obtain
  \[
    \sum_{P\in Z} L_Z(P)^2
    =
    |Z|+o(|Z|)
  \]
  (the main term \(|Z|\) is exactly the feasibility equation evaluated at load \(1\)).

- [ ] **Conclude M1:** combine first and second moments:
  \[
    \sum_{P\in Z}(L_Z(P)-1)^2
    =
    \sum_P L_Z(P)^2-2\sum_P L_Z(P)+|Z|
    =
    o(|Z|).
  \]

### 5.3 Side-load second moments (M2 ledger)

For \(X\)-side, group vertices by their fixed core type \((a,r)\) where \(x=2a q\), \(q\equiv r\pmod{W_0}\).

- [ ] **Cross-terms only within the same \(a\):** show that if \(x=2a_1 q_1=2a_2 q_2\) with primes \(q_1,q_2\) and fixed \(a_1\ne a_2\), then for all sufficiently large \(n\) there are no solutions in the core range. Conclude mixed second moments between different \(a\)'s vanish for large \(n\).

- [ ] **Second moment expansion (fixed \(a\) and target residue):** for each admissible pair \((\tau_1,\tau_2)\) with the same \(a\) and the same \(r\) (so they contribute to the same target fiber),
  \[
    \sum_{x\in X_{a,r}}
      L_{X,\tau_1}(x)\,L_{X,\tau_2}(x)
  \]
  is a weighted count of triples \((q,q_1',q_2')\) with prime forms
  \[
    q,\quad q_1',\quad q_2',\quad P_1=\sigma_1(b_1 q_1'-a q),\quad P_2=\sigma_2(b_2 q_2'-a q),
  \]
  and with the induced residue restrictions and polygonal constraints from \(\Omega_{\tau_1},\Omega_{\tau_2}\).

- [ ] **GTZ invocation (3 variables, 5 forms):** after W-trick rewriting \(q=\widetilde W m+\alpha\), \(q'_i=\widetilde W m'_i+\alpha'_i\), apply GTZ to obtain the uniform asymptotic
  \[
    \sum_{x\in X_{a,r}} L_X(x)^2
    =
    \sum_{x\in X_{a,r}} \lambda_X(x)^2
    +o(|X_{a,r}|),
  \]
  where \(\lambda_X(x)\) is the deterministic limiting side-load profile induced by the feasible kernels (recorded from the feasibility equations).

- [ ] **Repeat symmetrically for \(Y\)-side:** identical with \(q'\) as the common variable and \(q_1,q_2\) varying, giving prime forms
  \[
    q',\quad q_1,\quad q_2,\quad P_1=\sigma_1(b q'-a_1 q_1),\quad P_2=\sigma_2(b q'-a_2 q_2),
  \]
  with cross-terms only within the same \(b\).

- [ ] **Conclude M2 (L2 concentration about the profile):** for each side,
  \[
    \sum_{x\in X^{\mathrm{core}}}\bigl(L_X(x)-\lambda_X(x)\bigr)^2=o(|X^{\mathrm{core}}|),
    \qquad
    \sum_{y\in Y^{\mathrm{core}}}\bigl(L_Y(y)-\lambda_Y(y)\bigr)^2=o(|Y^{\mathrm{core}}|),
  \]
  with \(\lambda_X,\lambda_Y\le 1-2\gamma\) from feasibility.

---

## 6. Diagonals, degeneracies, and what gets removed (and why it is negligible)

Maintain a single ledger of discarded sets for each moment system; every discarded set must be shown to contribute \(o(|Z|)\) (or the relevant scale) after weights are included.

- [ ] **Diagonal A (reusing the same edge):**
  - label moment: \(e_1=e_2\) (equivalently \(t_1=t_2\) in the \((P,t_1,t_2)\) parametrization when \(\tau_1=\tau_2\));
  - \(X\)-moment: \(q_1'=q_2'\) when \(\tau_1=\tau_2\);
  - \(Y\)-moment: \(q_1=q_2\) when \(\tau_1=\tau_2\).
  Show these contribute at the total-edge scale
  \[
    O\!\left(\frac{n^2}{(\log n)^3}\right)\cdot \Bigl(\frac{\log^4 n}{n^2}\Bigr)
    =
    O(\log n)
    =
    o(|Z|),
  \]
  since \(|Z|\asymp n/\log n\).

- [ ] **Diagonal B (form collisions leading to non-finite-complexity):** for each system, list all algebraic coincidences where two prime forms become identical or rational multiples (e.g. forced by \(\tau_1=\tau_2\) and the diagonal equalities above). Verify these coincide with the diagonals in A or with genuinely empty blocks (excluded in Section 3).

- [ ] **Small-prime exceptional sets:** ensure all systems exclude \(L_i(\cdot)\le w\) for every prime form \(L_i\). Bound their total contribution by \(o(|Z|)\) as in Section 2.

- [ ] **Boundary layer of polygonal cutoffs:** show the \(\eta\)-neighborhood of each \(\partial\Omega_\tau\) contributes \(o_\eta(|Z|)\) to first and second moments after \(n\to\infty\).

- [ ] **Coefficient-tail spill:** record a single estimate (used later for M3/AWN) that the total fractional mass on edges incident to vertices outside the coefficient core is \(o_\varepsilon(|Z|)\) uniformly in \(n\), and is handled only after \(n\to\infty\) and then \(\varepsilon\to0\).

---

## 7. Smooth-kernel limit passage and matching to the feasibility equations

- [ ] **Consistency check:** verify that the main terms \(\mathrm{MT}_\tau(\eta,w)\) for edge totals and the analogous main terms for the 5-form systems are exactly the singular-integral expressions used in the feasibility/load equations (same normalization, same residue lifting, same Jacobians).
- [ ] **Uniformity in \(\tau\):** because \(\mathcal T_\varepsilon\) is finite, ensure every \(o_{w,\eta}(1)\) error is uniform in \(\tau,\tau_1,\tau_2\) so that summing over types preserves \(o(1)\).
- [ ] **Let \(n\to\infty\):** conclude M1/M2 (and any auxiliary first-moment identities) with errors \(o_{w,\eta}(1)\) for fixed \(w,\eta\).
- [ ] **Let \(w\to\infty\):** upgrade the fixed-\(w\) estimates to the intended prime model (either by a standard diagonal \(w=w(n)\to\infty\) choice, or by an iterated-limit statement).
- [ ] **Let \(\eta\to0\):** remove smoothing to return to the original kernels \(g_\tau\) and sharp polygonal constraints.

---

## 8. Translating limiting load equations to AWN hypotheses (what to hand to combinatorics)

Assume kernel feasibility has produced \(\gamma>0\) and limiting load profiles with \(L_Z^{\lim}=1\) and \(\lambda_X,\lambda_Y\le 1-2\gamma\).

- [ ] **(AWN atom bound)** show
  \[
    \max_e w_e \le \frac{\log^2 n}{n}\max_\tau\|g_\tau\|_\infty=o(1).
  \]
- [ ] **(AWN codegrees)** use the pair-codegree bound \(\Delta_2\le2\) to get
  \[
    \max_{u\ne v}\sum_{e\supset\{u,v\}}w_e \le 2\max_e w_e=o(1).
  \]
- [ ] **(AWN label L2)** use M1 to obtain
  \[
    \sum_{P\in Z}(L_Z(P)-1)^2=o(|Z|).
  \]
- [ ] **(Label normalization, if AWN is stated with \(L_Z\le1\))** define
  \[
    w'_e:=\min\bigl(1, L_Z(P)^{-1}\bigr)\,w_e\quad\text{for }e\text{ labeled }P.
  \]
  Use the L2 estimate to show \(L'_Z(P)\le1\) for all \(P\) and
  \[
    \sum_{e} w'_e = |Z|-o(|Z|),
  \]
  while preserving the atom/codegree bounds and the side-load slack up to \(o(1)\).
- [ ] **(AWN side slack + L2)** from kernel feasibility \(\lambda_X,\lambda_Y\le 1-2\gamma\) and M2, deduce:
  - the average side load satisfies \(\overline L_X\le 1-\gamma\), \(\overline L_Y\le 1-\gamma\) on the core;
  - the L2 deviation hypotheses required by AWN (either around the constant mean or around the deterministic profile, depending on the AWN formulation being used).
- [ ] **(Exceptional mass / overload pruning)** define overload sets
  \[
    B_X:=\{x\in X^{\mathrm{core}}:L_X(x)>1-\gamma\},\qquad B_Y:=\{y\in Y^{\mathrm{core}}:L_Y(y)>1-\gamma\},
  \]
  and use the L2 bounds plus feasibility slack to show
  \[
    |B_X|=o(|X^{\mathrm{core}}|),\quad |B_Y|=o(|Y^{\mathrm{core}}|),
    \qquad
    \sum_{e:e\cap(B_X\cup B_Y)\ne\emptyset} w_e=o(|Z|).
  \]
- [ ] **Coefficient-tail handling:** quantify the total weight on edges incident to \(X\setminus X^{\mathrm{core}}\) or \(Y\setminus Y^{\mathrm{core}}\) as \(o_\varepsilon(|Z|)\); this is the only place where the \(\varepsilon\to0\) limit is used.
- [ ] **Conclude AWN hypotheses** for the core hypergraph; pass to Kahn rounding to get a matching covering \((1-o(1))|Z|\) labels on the core; then send \(\varepsilon\to0\).
