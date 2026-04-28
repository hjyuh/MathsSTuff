# Rounding without Kahn: what can be replaced?

Created: 2026-04-25

Purpose: isolate the exact fractional-rounding statement used in the EP689
route, check whether it can be proved or cited without relying on inaccessible
Kahn 1996 PDF access, and give manuscript-safe wording.

This note does not edit the posted TeX.  It is a proof-interface audit for the
rounding step only.


## 1. Exact lemma needed in the EP689 proof

The EP689 matching stage produces a sequence of finite 3-partite 3-uniform
hypergraphs
\[
  H_n=(X_n\sqcup Y_n\sqcup Z_n,E_n),
\]
where every edge has the form
\[
  e=(x,y,P)
\]
and contains exactly one label vertex \(P\in Z_n\).

After the deterministic AWN preprocessing, we have nonnegative weights
\[
  t_n:E_n\to \mathbf R_{\ge 0}
\]
such that:

1. \(t_n\) is a fractional matching:
   \[
     \sum_{e\ni v}t_n(e)\le 1
     \qquad\text{for every vertex }v.
   \]

2. Its total mass is large:
   \[
     T_n:=\sum_e t_n(e)=(1-o(1))|Z_n|,
     \qquad |Z_n|\to\infty.
   \]

3. Its atoms are small:
   \[
     \max_e t_n(e)=o(1).
   \]

4. The underlying EP689 hypergraph has pair-codegree at most \(2\):
   \[
     \Delta_2(H_n)\le 2.
   \]
   Therefore the fractional pair co-load
   \[
     \alpha(t_n):=\max_{u\ne v}\sum_{e\supset\{u,v\}}t_n(e)
   \]
   satisfies
   \[
     \alpha(t_n)\le 2\max_e t_n(e)=o(1).
   \]

The exact needed conclusion is:

### Lemma R (fractional matching rounding needed here)

Under the four hypotheses above, \(H_n\) contains a genuine matching \(M_n\)
with
\[
  |M_n|=(1-o(1))T_n=(1-o(1))|Z_n|.
\]

Since every edge contains exactly one label vertex, this matching covers
\((1-o(1))|Z_n|\) labels.

This is the only rounding statement needed for EP689.  No vertex-perfect
matching conclusion is needed.


## 2. Citation route

### 2.1 Kahn 1996 is still the best exact citation

The public Rutgers metadata for Kahn's paper states the relevant theorem in
almost exactly the form needed here:

Jeff Kahn, *A linear programming perspective on the Frankl--Rodl--Pippenger
theorem*, Random Structures and Algorithms 8 (1996), no. 2, 149--157.

The Rutgers abstract defines the pair co-load parameter
\[
  a(t)=\max_{x\ne y}\sum_{A\ni x,y}t(A)
\]
and describes Theorem 1.5 for a \(k\)-bounded hypergraph, a fractional matching
\(t\), and finitely many nonnegative statistics \(C_i\), with limits as
\(\alpha(t)\to0\).

For our application, use the single statistic
\[
  C(e)\equiv 1.
\]
Then Kahn's statistic condition, as stated in the public abstract, is
\[
  \sum_e C(e)^2t(e)
  =
  o\!\left(\left(\sum_e C(e)t(e)\right)^2\right).
\]
For \(C\equiv1\), this is just
\[
  T_n=o(T_n^2),
\]
equivalently \(T_n\to\infty\), which holds because
\[
  T_n=(1-o(1))|Z_n|\asymp n/\log n.
\]

Important correction: this is not the condition
\(\sum_e t(e)^2=o(T_n^2)\).  That stronger statement also follows from
small atoms, but Kahn's statistic condition for \(C\equiv1\), as quoted in the
metadata, is simply \(T_n=o(T_n^2)\).

Conclusion: if the printed Theorem 1.5 has no hidden hypotheses beyond the
metadata, Kahn proves Lemma R directly.

Source:
<https://www.researchwithrutgers.com/en/publications/a-linear-programming-perspective-on-the-frankl-r%C3%B6dl-pippenger-the/>


### 2.2 Keevash survey corroborates, but does not fully replace Kahn

Keevash's ICM survey *Hypergraph matchings and designs* gives an accessible
summary of a special case of Kahn:

> A special case of a theorem of Kahn is that if there is a fractional perfect
> matching on the edges of an \(r\)-graph \(G\) on \([n]\) such that for any
> pair of vertices \(x,y\) the total weight on edges containing \(\{x,y\}\) is
> \(o(1)\), then \(G\) has a matching covering all but \(o(n)\) vertices.

This is very useful as public corroboration of the local-sparsity-to-rounding
principle.  However, it is not enough by itself for EP689:

- it assumes a fractional *perfect* matching;
- it concludes an almost vertex-covering matching;
- it does not state the statistic-preserving/non-perfect form needed to turn a
  fractional matching of total mass \(T_n\) into a matching of size
  \((1-o(1))T_n\).

One might try to reduce our non-perfect case to the perfect case by adding dummy
vertices and dummy edges to absorb slack.  The problem is that the resulting
almost-perfect matching may use many dummy edges.  To force preservation of the
number of real edges, one needs precisely a statistic-preserving conclusion
with \(C(e)=1_{\text{real edge}}\), which is Kahn's Theorem 1.5 rather than the
perfect-special-case formulation.

Conclusion: Keevash is a good secondary citation and sanity check, but not a
standalone replacement.

Source:
<https://people.maths.ox.ac.uk/keevash/papers/icm-survey-arxiv.pdf>


### 2.3 Pippenger / Frankl--Rodl / Ehard--Glock--Joos are accessible but not exact

The classical Pippenger theorem says that an almost regular uniform hypergraph
with small codegrees has an almost-perfect matching.  Ehard--Glock--Joos give an
accessible modern pseudorandom strengthening, and their paper explicitly states
Pippenger's theorem.

This is not an exact replacement for Lemma R because EP689 does not naturally
produce an unweighted almost-regular hypergraph.  It produces a weighted
fractional matching with side slack and only averaged/L2 control before
preprocessing.  Converting that weighted object into a genuinely almost-regular
unweighted hypergraph would require a discretization/regularization argument.
Such an argument is plausible, but it is essentially a re-proof of the
Kahn-style theorem rather than a one-line citation.

Potential use:

- if a referee dislikes the inaccessible Kahn paper, one possible appendix route
  is to discretize \(t\), clone capacities, and appeal to a pseudorandom
  Pippenger-style theorem;
- but the manuscript would then need to prove that the auxiliary hypergraph is
  almost regular, has small codegrees, and that a matching in the auxiliary
  object projects to \((1-o(1))T_n\) real EP689 edges.

That is extra work and introduces new places for mistakes.

Sources:

- Ehard--Glock--Joos, *Pseudorandom hypergraph matchings*:
  <https://doi.org/10.1017/S0963548320000280>
- open PDF copy via Cambridge/ETH:
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AE0DE17C95900E7DD3F221E2C17FE203/S0963548320000280a.pdf/pseudorandom_hypergraph_matchings.pdf>


## 3. Direct proof route, if we wanted to avoid Kahn

A direct proof of Lemma R should be possible by a weighted Rodl-nibble argument,
but it is not a cheap one-page proof.  The rough route is:

1. Start with the fractional matching \(t\).

2. Run a small-step random nibble.  In each round, independently sample each
   currently available edge with probability \(\theta t(e)\), where
   \(\theta>0\) is a small fixed parameter, keep only isolated sampled edges,
   and delete all vertices covered by sampled edges.

3. Track the residual fractional weights by conditioning on survival and
   renormalizing.  The pair co-load hypothesis controls dependencies between
   survival events for different vertices, while small atoms prevent one edge
   from dominating a load.

4. Prove that each round captures a \(\theta(1-o(1))\) fraction of the remaining
   fractional mass and that the residual object still has small pair co-load and
   remains a fractional matching after renormalization.

5. Iterate \(O_\theta(\log(1/\varepsilon))\) rounds to capture all but an
   \(\varepsilon\)-fraction of \(T_n\), then let \(\varepsilon\to0\).

This is exactly the philosophical proof of Kahn's theorem.  It is feasible, but
it requires a serious martingale/concentration and invariant-tracking write-up.
It should not be inserted casually into the EP689 manuscript unless Kahn becomes
unusable.


## 4. Is max edge weight plus pair co-load \(o(1)\) enough?

With the fractional matching hypothesis: yes, according to Kahn's theorem.

More precisely, the sufficient package is:

\[
  \sum_{e\ni v}t(e)\le1\quad\forall v,
\]
\[
  \alpha(t):=\max_{u\ne v}\sum_{e\supset\{u,v\}}t(e)=o(1),
\]
\[
  T:=\sum_e t(e)\to\infty.
\]

Then the \(C\equiv1\) instance of Kahn gives a matching of size
\[
  (1-o(1))T.
\]

In the EP689 hypergraph, \(\Delta_2\le2\), so
\[
  \alpha(t)\le2\max_e t(e).
\]
Thus our existing small-atom bound implies the required pair co-load bound.
Conversely, since every edge has size \(3\), any edge \(e\) contains a vertex
pair, so
\[
  t(e)\le \alpha(t).
\]
For this 3-uniform setting, small atom and small pair co-load are equivalent up
to the fixed factor \(2\).

Without the fractional matching hypothesis, the statement is false: one could
put large total weight through a single vertex while keeping individual atoms
small, and no matching can realize that weight.  The vertex-load constraint is
essential.

Also, a naive one-shot random rounding is not enough.  Sampling edges with
probability \(t(e)\) has expected size \(T\), but can create \(\Theta(T)\)
collisions at vertices whose load is near \(1\).  The nontrivial content is the
iterative nibble/alteration that recovers almost all of \(T\), not the first
moment.


## 5. Hidden degree, regularity, and perfectness hypotheses

For the exact Kahn route, the hidden-hypothesis checklist is:

1. **Uniformity.** Kahn is stated for \(k\)-bounded hypergraphs, so our
   3-uniform hypergraph is allowed.

2. **Regularity.** No pointwise regularity should be required in Kahn's theorem.
   This is the main advantage over Pippenger--Spencer.

3. **Perfectness.** The Rutgers metadata says \(t\) is a fractional matching,
   not necessarily a fractional perfect matching.  This is exactly what we need.
   Keevash's survey only records the perfect special case, so it cannot replace
   the full theorem.

4. **Statistic preservation.** Kahn allows finitely many statistics \(C_i\).  We
   only use \(C\equiv1\).  The statistic condition becomes \(T=o(T^2)\), hence
   \(T\to\infty\).

5. **Smallness parameter.** The needed parameter is the fractional pair co-load
   \(\alpha(t)\).  Public metadata and previews identify it as
   \[
     \max_{u\ne v}\sum_{e\supset\{u,v\}}t(e).
   \]

6. **Linearity/codegree.** Kahn does not require the underlying codegree to be
   \(1\) or \(2\); it only requires \(\alpha(t)\to0\).  Our codegree bound is a
   convenient way to prove \(\alpha(t)\to0\) from \(\max_e t_e=o(1)\).

The only unresolved risk is that the printed Theorem 1.5 could contain a
condition not visible in the public metadata.  Based on the abstract and
Keevash's survey, that risk looks low, but it is exactly why a PDF check remains
valuable.


## 6. Bottom-line recommendation for manuscript wording

Do not try to replace Kahn with Pippenger--Spencer in the main proof.  The exact
weighted non-perfect fractional rounding statement is Kahn's theorem; the
alternatives either state only a perfect special case or require substantial
regularization work.

Recommended manuscript wording:

> We use Kahn's fractional Frankl--Rodl--Pippenger rounding theorem.  In the
> form needed here, if \(H\) is a \(k\)-bounded hypergraph and \(t\) is a
> fractional matching with pair co-load
> \[
>   \alpha(t)=\max_{u\ne v}\sum_{e\supset\{u,v\}}t(e)=o(1),
> \]
> then Kahn's statistic-preserving rounding theorem, applied with the single
> statistic \(C(e)\equiv1\), gives a matching \(M\) with
> \[
>   |M|\sim\sum_e t(e),
> \]
> provided \(\sum_e t(e)\to\infty\).  In our 3-partite 3-graph
> \(\Delta_2\le2\), so \(\alpha(t)\le2\max_e t(e)=o(1)\), and the AWN
> preprocessing gives \(\sum_e t(e)=(1-o(1))|Z_n|\to\infty\).

Add a reference sentence:

> Keevash's ICM survey records the corresponding fractional-perfect special case
> as a theorem of Kahn; the full statistic-preserving non-perfect form is Kahn
> [Random Structures Algorithms 8 (1996), Theorem 1.5].

If the final paper needs to avoid reliance on an inaccessible PDF, the fallback
is not to cite Pippenger--Spencer directly, but to add an appendix proving Lemma
R by a weighted nibble.  That appendix would be real work; it should be treated
as a proof project, not a cosmetic citation swap.


## 7. Status

Current status: Kahn dependency is reduced but not eliminated.

- The exact theorem we need is now isolated as Lemma R.
- Public Kahn metadata appears to prove Lemma R directly.
- Keevash provides an accessible corroborating special case.
- Pippenger-style accessible theorems do not directly match our hypotheses.
- A self-contained direct proof is plausible but essentially reproduces Kahn's
  nibble argument.

Recommendation: keep Kahn in the proof, cite Keevash as corroboration, and
continue trying to obtain the printed Kahn paper.  Do not spend proof budget on
a Kahn-free appendix unless someone finds a hidden hypothesis in Theorem 1.5.
