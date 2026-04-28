# GTZ/Kahn downstream proposition chain (after explicit kernel feasibility)

Created: 2026-04-25

This file is a clean proposition stack for the route

\[
  \text{explicit kernel feasibility}
  \Longrightarrow
  \text{GTZ edge + moment estimates on a fixed finite core}
  \Longrightarrow
  \text{preprocessing to a fractional matching (AWN)}
  \Longrightarrow
  \text{Kahn rounding}
  \Longrightarrow
  \text{coefficient-tail removal}
  \Longrightarrow
  \text{pair-plus-singleton cleanup (Erdos 689)}.
\]

It is a roadmap, not a completed proof: each proposition below is conditional
and should be treated as a named obligation. The two main ledgers are:

- [gtz-execution-checklist.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-execution-checklist.md)
- [kahn-awn-bridge.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-awn-bridge.md)

The final cleanup reduction is recorded in:

- [robust-prime-difference-route.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\robust-prime-difference-route.md)

---

## 0. Frozen setup and order of limits (standing convention)

Fix once and for all:

1. A finite switching set \(S\subset\{7,11,13,\ldots\}\) and \(W_0:=\prod_{s\in S}s\).
2. A robustness parameter \(\beta\in(0,1/2)\).
3. A coefficient-tail parameter \(\varepsilon>0\) and a corresponding finite coefficient core \(\mathcal C_\varepsilon\).
4. A finite type set \(\mathcal T_\varepsilon\) (types \(\tau=(a,b,\sigma,r,r',\pi)\) on the core, \(\gcd(a,b)=1\)).
5. Bounded measurable kernels \(g_\tau\ge 0\) supported on the polygons \(\Omega_\tau\).
6. A fixed \(W\)-trick modulus \(\widetilde W\) (built from \(W_0\) and small primes \(\le w\)), and a fixed smoothing scale \(\eta>0\).

Then:

- all GTZ moment arguments are for \(n\to\infty\) with \((\varepsilon,\mathcal C_\varepsilon,\widetilde W,\eta)\) fixed;
- only after the \(n\to\infty\) asymptotics are proved do we send \(\widetilde W\) large (or \(w\to\infty\)) and \(\eta\to 0\);
- only after combinatorial rounding on the \(\varepsilon\)-core do we send \(\varepsilon\to 0\).

Define the 3-partite 3-uniform hypergraph
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
\]
with
\[
  X_n=A_1(n),\qquad Y_n=A_2(n),\qquad Z_n=\mathcal R_\beta(n),
\]
and edges \(e=(x,y,P)\) when \(|y-x|=2P\). (The exact definitions are as in
the checklist; what matters downstream is that \(H_n\) is 3-uniform,
3-partite, and has pair-codegree at most \(2\).)

Edge weights are of the form
\[
  w_e=\frac{\log^2 n}{n}\,g_\tau(q/n,q'/n)
\]
for the corresponding core type \(\tau\). Loads are
\[
  L_X(x)=\sum_{e\ni x}w_e,\qquad L_Y(y)=\sum_{e\ni y}w_e,\qquad L_Z(P)=\sum_{e\ni P}w_e.
\]

---

## 1. Standing input: finite-core kernel feasibility (already handled elsewhere)

**Assumption KF(\(\varepsilon\)).** For the fixed core \(\mathcal C_\varepsilon\), the kernels \(g_\tau\) solve the
limiting load equations with slack \(\gamma=\gamma(S,\beta,\varepsilon)>0\):

1. label-load equation \(L_Z^{\lim}(t,\pi)=1\) a.e. on \((1/5,\beta]\times\mathcal B\);
2. side profiles \(\lambda_X,\lambda_Y\) (induced by \(g_\tau\)) satisfy
   \(\lambda_X\le 1-2\gamma\) and \(\lambda_Y\le 1-2\gamma\).

(The feasibility program and explicit-kernel audit are in the kernel-feasibility notes; this file starts after that point.)

---

## 2. Proposition chain: GTZ moments \(\Rightarrow\) Kahn matching

### Proposition P1 (Finite-core GTZ edge totals)

Assume:

1. KF(\(\varepsilon\)).
2. For each \(\tau\in\mathcal T_\varepsilon\) and each compatible residue lift mod \(\widetilde W\), the post-\(W\)-trick
   2-variable 3-form system in [gtz-execution-checklist.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\gtz-execution-checklist.md)
   Section 5.1 satisfies the Green--Tao--Ziegler linear-forms asymptotic with the expected main term, uniformly in \(\tau\).
3. Consistency: after summing over types/lifts and undoing smoothing, the GTZ main terms match the continuum load equation \(L_Z^{\lim}=1\).

Conclusion (for \(n\to\infty\) with fixed \(\widetilde W,\eta\)):
\[
  \sum_{P\in Z_n} L_Z(P)=|Z_n|+o(|Z_n|).
\]

This is the "first-moment / edge-total" ledger item (M1 first moment).

---

### Proposition P2 (Label \(L^2\) concentration)

Assume:

1. P1.
2. For each \((\tau_1,\tau_2)\in\mathcal T_\varepsilon^2\), the post-\(W\)-trick 3-variable 5-form system for the common-label second moment
   in the checklist Section 5.2 satisfies GTZ after removal of diagonals/degeneracies (Section 6), with main term matching feasibility.

Conclusion:
\[
  \sum_{P\in Z_n}(L_Z(P)-1)^2=o(|Z_n|).
\]

Equivalently, \(\sum_{P\in Z_n}L_Z(P)^2=|Z_n|+o(|Z_n|)\).

---

### Proposition P3 (Side \(L^2\) concentration about the feasibility profile)

Assume:

1. KF(\(\varepsilon\)).
2. For each admissible side-moment system in checklist Section 5.3 (3 variables, 5 prime forms after \(W\)-trick),
   GTZ applies uniformly after removing diagonals/degeneracies.

Conclusion (with \(\lambda_X,\lambda_Y\) induced from the feasible kernels):
\[
  \sum_{x\in X_n^{\rm core}}(L_X(x)-\lambda_X(x))^2=o(|X_n^{\rm core}|),
  \qquad
  \sum_{y\in Y_n^{\rm core}}(L_Y(y)-\lambda_Y(y))^2=o(|Y_n^{\rm core}|),
\]
and in particular, since \(\lambda_X,\lambda_Y\le 1-2\gamma\),
the average side loads satisfy \(\overline L_X\le 1-\gamma\) and \(\overline L_Y\le 1-\gamma\) on the core.

---

### Proposition P4 (AWN preprocessing: from \(L^2\) loads to a large fractional matching)

This is the corrected role of "AWN" as in [kahn-awn-bridge.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\kahn-awn-bridge.md):
produce a Kahn-eligible fractional matching \(t\), not a matching.

Assume:

1. P2 (label \(L^2\)).
2. P3 (side \(L^2\) plus feasibility slack).
3. Atom bound: \(\max_e w_e=o(1)\). (With \(w_e\asymp (\log^2 n)/n\), this is expected, but it must be checked that later trimming preserves it.)
4. Pair-codegree bound: any vertex-pair lies in at most two edges, hence
   \[
     a(w):=\max_{u\ne v}\sum_{e\supset\{u,v\}}w_e \le 2\max_e w_e.
   \]
5. Coefficient-tail bound (fixed \(\varepsilon\)): total weight incident to non-core side vertices is \(o_\varepsilon(|Z_n|)\).

Conclusion: after the following deterministic preprocessing, we obtain a subhypergraph \(H_n'\subseteq H_n\) and weights \(t\) on \(E(H_n')\) such that:

1. (Fractional matching inequalities) \(\sum_{e\ni v}t_e\le 1\) for every vertex \(v\in V(H_n')\).
2. (Large total mass) \(\sum_e t_e = |Z_n|-o(|Z_n|)-o_\varepsilon(|Z_n|)\).
3. (Small atoms) \(\max_e t_e=o(1)\).
4. (Small pair co-load) \(a(t)=o(1)\) (automatic from \(\Delta_2\le2\) + small atoms).

Preprocessing steps (the point is that each step loses only \(o(|Z_n|)\) mass):

1. **Label normalization.** Replace
   \[
     w_e \mapsto t^{(0)}_e := \min(1,L_Z(P)^{-1})w_e\qquad (e\cap Z_n=\{P\}).
   \]
   Then \(L_{t^{(0)}}(P)\le 1\) for all labels.
   From P2 one expects
   \[
     \sum_e t^{(0)}_e = \sum_{P\in Z_n}\min(L_Z(P),1) = |Z_n|-o(|Z_n|),
   \]
   but this mass-loss estimate still needs to be written cleanly (it should be a one-line Cauchy--Schwarz argument).

2. **Side overload pruning.** Define overload sets (for some fixed slack parameter, e.g. \(1-\gamma\)):
   \[
     B_X:=\{x\in X_n^{\rm core}:L_{t^{(0)}}(x)>1-\gamma\},\qquad
     B_Y:=\{y\in Y_n^{\rm core}:L_{t^{(0)}}(y)>1-\gamma\}.
   \]
   Delete \(B_X\cup B_Y\) and all incident edges, producing \(t^{(1)}\) on a subhypergraph.
   Using P3 + \(\lambda_X,\lambda_Y\le 1-2\gamma\), one expects both
   \(|B_X|,|B_Y|=o(|X_n^{\rm core}|),o(|Y_n^{\rm core}|)\) and the stronger **bad-set mass** bound
   \[
     \sum_{e:\,e\cap(B_X\cup B_Y)\ne\emptyset} t^{(0)}_e = o(|Z_n|).
   \]
   The size bound alone is not enough; the mass bound is an explicit obligation.

3. **Coefficient-tail deletion.** Delete all edges incident to \(X_n\setminus X_n^{\rm core}\) or \(Y_n\setminus Y_n^{\rm core}\),
   losing \(o_\varepsilon(|Z_n|)\) mass by assumption.

Set \(t:=t^{(1)}\) restricted to the final vertex set. Then all vertex loads are \(\le 1\) by construction.

---

### Proposition P5 (Kahn rounding: fractional matching \(\Rightarrow\) matching)

Assume:

1. Proposition P4 outputs a fractional matching \(t\) on a \(k\)-bounded hypergraph \(H_n'\) (here \(k=3\)).
2. Kahn's theorem applies to \((H_n',t)\) with statistic \(C\equiv 1\) and yields
   \[
     |M_n| = (1-o(1))\sum_e t_e
   \]
   as \(\alpha(t)\to 0\).
3. The smallness parameter \(\alpha(t)\) is implied by the checks available from P4, namely:
   \[
     \max_e t_e=o(1),\qquad a(t)=o(1).
   \]
   (This is the key uncertainty: the abstract exposes \(a(t)\) but not the full definition of \(\alpha(t)\).)

Conclusion: there exists a matching \(M_n\) in \(H_n'\) with
\[
  |M_n|=(1-o(1)-o_\varepsilon(1))|Z_n|.
\]
Since each matching edge contains exactly one label \(P\in Z_n\), this matching covers the same number of labels.

---

### Proposition P6 (Coefficient-tail removal)

Assume: for every fixed \(\varepsilon>0\), the chain P1--P5 holds on the \(\varepsilon\)-core and yields a matching covering
\((1-o(1)-o_\varepsilon(1))|Z_n|\) labels.

Conclusion: after taking \(n\to\infty\) first and then \(\varepsilon\to 0\),
we obtain matchings covering \((1-o(1))|Z_n|\) labels in the full (untruncated) robust prime-difference hypergraph.

This is the only step where \(\varepsilon\to 0\) is used.

---

## 3. Final step: matching \(\Rightarrow\) Erdos 689 via pair-plus-singleton cleanup

### Proposition P7 (Pair-plus-singleton cleanup)

Assume:

1. The robust switching bookkeeping for some \(S\) produces a robust density \(\delta_S>10/11\) and a parameter \(\beta\in(\delta_S^{-1}-3/5,1/2)\) satisfying the pair-plus-singleton capacity inequality (see the constants discussion in [robust-prime-difference-route.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\robust-prime-difference-route.md) and [averaged-nibble-route.md](C:\Users\z20ma\OneDrive\Documents\!math\erdos\689\averaged-nibble-route.md)).
2. For all large \(n\), the robust prime-difference hypergraph contains a labelled matching \(\mathcal M_n\) on labels \(P\in(n/5,\beta n]\) that covers \((1-o(1))|Z_n|\) labels (or at least meets the explicit size threshold in the "Conditional robust pair theorem" in robust-prime-difference-route.md).

Conclusion: the pair-plus-singleton cleanup converts \(\mathcal M_n\) into a full switching assignment satisfying the Erdos 689 requirement for all sufficiently large \(n\).

This is a reduction step: it depends on the combinatorial cleanup proof, not on GTZ/Kahn.

---

## 4. Explicit gaps / citations still required

This list is intentionally specific (it is the "do not overclaim" ledger).

1. **Exact Kahn hypothesis (\(\alpha(t)\)).** The definition of \(\alpha(t)\) in the published paper must be checked and cited.
   At present, it is only safe to claim: "if Kahn's \(\alpha(t)\) is controlled by \(\max_e t_e\) and \(a(t)\), then P5 holds."

2. **AWN preprocessing mass bounds.** The two nontrivial deterministic inequalities in P4 must be written (and checked) in full:
   \[
     \sum_{P\in Z_n}\min(L_Z(P),1)=|Z_n|-o(|Z_n|),
   \]
   \[
     \sum_{e:\,e\cap(B_X\cup B_Y)\ne\emptyset} t_e=o(|Z_n|).
   \]
   The second is the key one: it uses \(L^2\) control plus feasibility slack to show *bad-set mass*, not just bad-set size.

3. **GTZ moment verification for each fixed core.** For P1--P3, the GTZ linear-forms-in-primes theorem must be invoked in a form that:
   - handles the fixed modulus \(\widetilde W\) and residue restrictions;
   - allows bounded (smoothed) weights \(g_{\tau,\eta}F_{\tau,\eta}\) on rational polytopes;
   - is uniform over the finite type set \(\mathcal T_\varepsilon\);
   - controls/justifies the removal of diagonals, degeneracies, small-prime exceptions, and boundary layers (checklist Sections 2, 4, 6).

4. **Main-term consistency with kernel feasibility.** Each GTZ main term has to be matched to the same singular-integral expressions used in the feasibility program (checklist Section 7).

5. **Coefficient-tail bound.** The statement "total non-core mass is \(o_\varepsilon(|Z_n|)\) uniformly in \(n\)" must be proved/cited (it should reduce to the summability of the \(S\)-smooth coefficient tails, but it still needs a clean lemma).

6. **Cleanup theorem writeup.** The pair-plus-singleton cleanup is currently a conditional theorem with a proof skeleton.
   It needs a finished writeup with explicit error terms (exceptional token count \(E_S(n)=o(n/\log n)\) and the exact matching-size threshold).
