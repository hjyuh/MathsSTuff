# Matching/no-identified-target-reuse closure

Created: 2026-04-25

This note closes the local bookkeeping issue flagged in
`robust-prime-difference-route.md` and sharpened in
`final-cleanup-theorem-draft.md`: whether the Kahn/AWN matching step must carry
an extra "no identified target reuse" condition.

Verdict: if Kahn is applied to the actual 2-adic-layered hypergraph
\[
  X=A_{S,1}(n),\qquad Y=A_{S,\ge 2}(n),
\]
then no identified-target-reuse condition is missing.  It is already part of
the ordinary matching property, because \(A_{S,1}(n)\) and
\(A_{S,\ge 2}(n)\) are disjoint subsets of the true target set \(A_S(n)\).

The projection issue exists only in the artificial two-full-copy model
\[
  A_S(n)^{\rm left}\sqcup A_S(n)^{\rm right}\sqcup \mathcal R_\beta(n).
\]
In that model, a target may be used once in each copy unless one adds an
explicit projection-injectivity condition, or first restricts the two copies to
the two disjoint 2-adic layers.

## 1. Exact hypergraph for Kahn

Keep the parity-first setup and robust primes from
`final-cleanup-theorem-draft.md`.  For \(1/5<\beta\le 1/2\), set
\[
  X_n:=A_{S,1}(n)=\{x\in A_S(n):v_2(x)=1\},
\]
\[
  Y_n:=A_{S,\ge 2}(n)=\{y\in A_S(n):v_2(y)\ge 2\},
\]
\[
  Z_n:=\mathcal R_\beta(n)
  =\{P\in(n/5,\beta n]:P\ {\rm prime,\ robust}\}.
\]

Kahn should be applied, after the GTZ/AWN preprocessing, to a subhypergraph of
the 3-partite 3-uniform hypergraph
\[
  H_{S,\beta}(n)=(X_n\sqcup Y_n\sqcup Z_n,E_n),
\]
where
\[
  (x,y,P)\in E_n
  \quad\Longleftrightarrow\quad
  x\in X_n,\ y\in Y_n,\ P\in Z_n,\ |x-y|=2P.
  \tag{1}
\]

This is the same hypergraph as the one called \(H_n\) in
`gtz-kahn-proof-chain.md`, but with the side classes identified explicitly as
the two \(v_2\)-layers of \(A_S(n)\).  The notation \(A_1(n),A_2(n)\) in the
GTZ/Kahn chain should therefore be read as
\[
  A_1(n)=A_{S,1}(n),\qquad A_2(n)=A_{S,\ge 2}(n).
\]

The parity reason for this model is forced.  If \(P\) is odd and
\(|x-y|=2P\), then \(v_2(x-y)=1\).  Since every element of \(A_S(n)\) is even,
exactly one endpoint has \(v_2=1\), and the other has \(v_2\ge 2\).

## 2. Pair-codegree bound

The exact absolute-difference edge relation (1) gives
\[
  \Delta_2(H_{S,\beta}(n))\le 2.
\]

Indeed:

1. If \(x\in X_n\) and \(y\in Y_n\), then the only possible label is
   \(P=|x-y|/2\), so \(\codeg(x,y)\le 1\).
2. If \(x\in X_n\) and \(P\in Z_n\), then any third vertex must be
   \(y=x+2P\) or \(y=x-2P\), so \(\codeg(x,P)\le 2\).
3. If \(y\in Y_n\) and \(P\in Z_n\), similarly any third vertex must be
   \(x=y+2P\) or \(x=y-2P\), so \(\codeg(y,P)\le 2\).
4. Pairs inside one part have codegree \(0\).

Thus for any Kahn fractional matching \(t\) supported on a subhypergraph
\(H'_{S,\beta}(n)\subseteq H_{S,\beta}(n)\),
\[
  a(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_e
  \le 2\max_e t_e.
\]
So the small-atom output \(\max_e t_e=o(1)\) from AWN preprocessing implies the
pair co-load condition \(a(t)=o(1)\).

If one orients all edges, for example by requiring \(y=x+2P\), the pair-codegree
bound improves to \(1\).  The current notes use \(|x-y|=2P\), so the safe bound
to record is \(\Delta_2\le 2\).

## 3. Matching output needed for cleanup

The exact matching target from `final-cleanup-theorem-draft.md` is
\[
  |\mathcal M_n|
  \ge
  |A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|.
  \tag{2}
\]
Here \(E_S(n)\) is the exceptional residual-token count outside the main
one-token set \(A_S(n)\), and
\[
  \mathcal R_{>1/5}(n)
  =
  \{P\in(n/5,n]:P\ {\rm prime,\ robust}\}.
\]

Kahn/AWN may deliver the stronger asymptotic output
\[
  |\mathcal M_n|=(1-o(1))|Z_n|
  =(1-o(1))|\mathcal R_\beta(n)|.
  \tag{3}
\]
This implies (2) for all sufficiently large \(n\) whenever
\[
  \delta_S>\frac{1}{\beta+3/5},
\]
because
\[
  |\mathcal R_\beta(n)|
  -
  \bigl(|A_S(n)|+E_S(n)-|\mathcal R_{>1/5}(n)|\bigr)
  =
  \left((\beta+3/5)\delta_S-1+o(1)\right)\frac n{\log n}.
\]

For \(\beta=1/2\), this is the familiar \(\delta_S>10/11\) threshold.  For a
smaller explicit-kernel value of \(\beta\), the corresponding threshold is
\(\delta_S>1/(\beta+3/5)\).

## 4. Why no-reuse follows automatically

Let \(\mathcal M_n\) be an ordinary matching in \(H_{S,\beta}(n)\).  Define
\[
  V_A(\mathcal M_n)
  :=
  \{x\in X_n:x\text{ appears in }\mathcal M_n\}
  \cup
  \{y\in Y_n:y\text{ appears in }\mathcal M_n\}.
\]

Because \(X_n\) and \(Y_n\) are disjoint subsets of \(A_S(n)\), and because a
matching has pairwise disjoint hypergraph vertices,
\[
  |V_A(\mathcal M_n)|=2|\mathcal M_n|.
  \tag{4}
\]
This is exactly the no identified-target-reuse condition needed by cleanup.
There is no additional projection map to check.

Likewise,
\[
  V_R(\mathcal M_n)
  :=
  \{P\in Z_n:P\text{ appears in }\mathcal M_n\}
\]
satisfies
\[
  |V_R(\mathcal M_n)|=|\mathcal M_n|.
  \tag{5}
\]

For each edge \((x,y,P)\in\mathcal M_n\), switch \(P\) to
\[
  a_P\equiv x\equiv y\pmod P.
\]
This is well-defined by \(|x-y|=2P\).  The robust-prime side-debt lemma in
`robust-prime-difference-route.md` and `final-cleanup-theorem-draft.md` shows
that this residue is nonzero for every residual target and that the switch
creates no new residual demand elsewhere.

After the pair stage, the remaining residual-token count is
\[
  |A_S(n)|-2|\mathcal M_n|+E_S(n).
  \tag{6}
\]
The unused robust-prime reservoir has size
\[
  |\mathcal R_{>1/5}(n)|-|\mathcal M_n|.
  \tag{7}
\]
The exact threshold (2) is equivalent to
\[
  |A_S(n)|-2|\mathcal M_n|+E_S(n)
  \le
  |\mathcal R_{>1/5}(n)|-|\mathcal M_n|.
  \tag{8}
\]
So the remaining main tokens and all exceptional tokens can be injected into
unused robust primes and cleaned by singleton switches.  If one integer carries
two exceptional residual tokens, those are separate tokens and are assigned to
two distinct unused robust primes.

Thus the cleanup theorem's no-reuse hypothesis follows from applying Kahn to
the actual layered hypergraph \(H_{S,\beta}(n)\).

## 5. Copy-model caveat

If a proof is instead written using the two-full-copy vertex set
\[
  A_S(n)^{\rm left}\sqcup A_S(n)^{\rm right}\sqcup \mathcal R_\beta(n),
\]
then an ordinary matching is not enough.  The same integer \(a\in A_S(n)\) may
be used once as \(a^{\rm left}\) and once as \(a^{\rm right}\) in two different
matched triples.  That would count two hypergraph vertices but only one cleanup
target.

The copy-model version therefore needs one of the following additional
conditions:

1. restrict the left and right copies before matching to the disjoint layers
   \(A_{S,1}(n)\) and \(A_{S,\ge 2}(n)\); or
2. impose projection injectivity:
   the map from all matched left and right target vertices to \(A_S(n)\) is
   injective.

With either condition, the copy model becomes equivalent to the actual layered
hypergraph for cleanup purposes.

## 6. Remaining gaps after this closure

This note closes only the matching/no-identified-target-reuse issue.  The
remaining gaps are the external inputs already recorded elsewhere:

1. Kahn's printed theorem still needs the final citation check for the exact
   definition of \(\alpha(t)\), although the local bridge uses the exposed
   pair co-load \(a(t)\) and small atoms.
2. The GTZ moment propositions for the fixed finite core still need formal
   verification and main-term matching to the kernel feasibility program.
3. The coefficient-tail removal step must still promote the finite-core
   matching to the full robust prime-difference hypergraph.
4. A fixed robust-density witness \(S\) with
   \(\delta_S>1/(\beta+3/5)\) must be chosen or cited.
5. The residual-demand package should still record
   \(|A_S(n)|=(1+o(1))n/\log n\) and
   \(E_S(n)=o(n/\log n)\) as a clean lemma for the final writeup.

No further no-reuse condition is needed once Kahn is applied to
\(H_{S,\beta}(n)\) with \(X=A_{S,1}(n)\) and \(Y=A_{S,\ge 2}(n)\).
