# Weighted/Fractional Matching Theorem (Averaged Nibble Form)

Created: 2026-04-25

This note isolates the **pure combinatorial** statement needed in the averaged
Green--Tao route: convert *averaged (L2) degree/load control* for a **linear**
3-partite 3-uniform hypergraph into an **integral matching** that covers
almost all "robust" labels.

The intended application is the robust prime-difference hypergraph with vertex
classes
\[
  A_1(n),\quad A_2(n),\quad \mathcal R_\beta(n),
\]
edges \((x,y,P)\) when \(|x-y|=2P\), and automatic linearity \(\Delta_2\le 1\).


## 1. Model and notations

Let \(H=(V_1\sqcup V_2\sqcup V_3,E)\) be a 3-partite 3-uniform hypergraph: every
edge \(e\in E\) meets each part in exactly one vertex.

We write \(V_1=A_1\), \(V_2=A_2\), \(V_3=R\) (labels).

**Linearity / codegree condition.** We assume
\[
  \Delta_2(H):=\max_{u\neq v}\#\{e\in E:u,v\in e\}\le 1.
  \tag{L}
\]
Equivalently, any two edges intersect in at most one vertex.

**Edge weights and loads.** Let \(\omega:E\to[0,\infty)\) be a weight function.
Define the (weighted) load at a vertex \(v\) by
\[
  L(v):=\sum_{e\ni v}\omega(e),
  \qquad
  L_i(v):=L(v)\ \ (v\in V_i).
  \tag{load}
\]
For a pair \(\{u,v\}\), define the pair-load
\[
  L(u,v):=\sum_{e\supset\{u,v\}}\omega(e).
  \tag{pair}
\]
When \(\Delta_2\le 1\), we have \(L(u,v)\le \max_e \omega(e)\).

**Interpretation.** If \(L_3(P)\approx 1\) for most labels \(P\in R\) and
\(L_1,L_2\le 1-\gamma\) on most targets, then \(\omega\) is an *approximate
fractional matching* that (almost) saturates the label class while using the
target classes with slack. The lemma below asserts that such a fractional
object can be rounded to a genuine matching covering almost all labels, using
only averaged/L2 control.


## 2. The weighted "almost-saturate labels" matching lemma

### Theorem 2.1 (Averaged Weighted Label-Saturation \(\Rightarrow\) Matching)

Fix \(\gamma>0\). Let \((H_n,\omega_n)\) be a sequence of 3-partite 3-graphs with
parts
\[
  V_1(n)\sqcup V_2(n)\sqcup V_3(n),
\]
where \(V_3(n)\) is the label class and \(|V_i(n)|\to\infty\). Assume \(H_n\) is
linear: \(\Delta_2(H_n)\le 1\).

Write \(L^{(n)}_i\) for the loads induced by \(\omega_n\).
Assume:

1. (**Small atoms**) \(\displaystyle \max_{e\in E(H_n)}\omega_n(e)=o(1)\).

2. (**Label saturation in \(L^2\)**)
   \[
     \sum_{P\in V_3(n)}\bigl(L^{(n)}_3(P)-1\bigr)^2=o(|V_3(n)|).
     \tag{LS}
   \]

3. (**Side slack outside negligible exceptional mass**)  
   There exist exceptional sets \(B_i(n)\subseteq V_i(n)\) for \(i=1,2\) such
   that
   \[
     |B_i(n)|=o(|V_i(n)|),
     \tag{B-size}
   \]
   \[
     L^{(n)}_i(v)\le 1-\gamma\qquad(v\in V_i(n)\setminus B_i(n)),
     \tag{slack}
   \]
   and the total label mass passing through the exceptional side vertices is
   negligible:
   \[
     \sum_{\substack{e\in E(H_n):\\ e\cap(B_1(n)\cup B_2(n))\neq\emptyset}}
       \omega_n(e)
     =o(|V_3(n)|).
     \tag{B-mass}
   \]

Then \(H_n\) contains a matching \(M_n\) that covers
\[
  (1-o(1))|V_3(n)|
\]
labels (i.e. all but \(o(|V_3(n)|)\) vertices of \(V_3(n)\) are saturated by
edges of \(M_n\)).

**Robust-label formulation.** (LS) implies that for any fixed \(\varepsilon>0\),
all but \(o(|V_3|)\) labels satisfy \(L_3(P)\in[1-\varepsilon,1+\varepsilon]\).
Discarding the remaining labels and discarding edges through \(B_1\cup B_2\),
one obtains a set \(R_{\rm rob}\subseteq V_3\) with \(|R_{\rm rob}|=(1-o(1))|V_3|\)
such that
\[
  L_3(P)=1+o(1)\ \ (P\in R_{\rm rob})
  \quad\text{and}\quad
  \omega\text{ uses }V_1,V_2\text{ with slack }1-\gamma.
\]
The conclusion can be restated as: there is a matching saturating
\((1-o(1))|R_{\rm rob}|\) robust labels.


### Remark 2.2 (Getting the exceptional-set hypothesis from \(L^2\) control)

In applications one may only have **averaged** slack on \(V_1,V_2\). A useful
trimming criterion is:

If for some \(\gamma>0\) and \(i\in\{1,2\}\) we have
\[
  \frac1{|V_i|}\sum_{v\in V_i}L_i(v)\le 1-2\gamma
  \qquad\text{and}\qquad
  \sum_{v\in V_i}\bigl(L_i(v)-(1-2\gamma)\bigr)^2=o(|V_i|),
  \tag{side-L2}
\]
then the set \(B_i:=\{v\in V_i:L_i(v)>1-\gamma\}\) satisfies
\(|B_i|=o(|V_i|)\). Moreover, if also \(\sum_{v\in V_i}L_i(v)^2=O(|V_i|)\), then
\(\sum_{v\in B_i}L_i(v)=o(|V_i|)\), which is typically \(\ll o(|V_3|)\) in the
regimes of interest.

Thus (B-size)--(B-mass) is a *standard corollary* of first and second moment
control of side loads, after discarding \(o(|V_i|)\) heavy side vertices.


## 3. Proof sketch (weighted nibble / fractional rounding)

This section is a proof outline only. It is written to clarify what needs to
be checked, not to be publication-grade.

### 3.1. Preprocessing: throw away negligible mass

By (LS), for any slowly decaying \(\varepsilon_n\to 0\), the set
\[
  R_{\rm bad}:=\{P\in V_3:|L_3(P)-1|>\varepsilon_n\}
\]
has size \(o(|V_3|)\). Discard those labels and all incident edges. Discard all
edges meeting \(B_1\cup B_2\). By (B-mass), the total removed label load is
\(o(|V_3|)\), so the surviving label set \(R_{\rm rob}\) still has
\(|R_{\rm rob}|=(1-o(1))|V_3|\) and retains label loads \(L_3(P)=1+o(1)\).

Finally, renormalize weights per label:
\[
  \omega'(e):=\frac{\omega(e)}{L_3(P)}\quad\text{for }e=\{x,y,P\},\ P\in R_{\rm rob}.
\]
Since \(L_3(P)=1+o(1)\) on \(R_{\rm rob}\), this changes each weight by a
\((1+o(1))\) factor, preserving "small atom" and preserving the target slack
provided \(\varepsilon_n\ll \gamma\). After renormalization we may assume

- \(L_3(P)=1\) for all \(P\in R_{\rm rob}\),
- \(L_1(x),L_2(y)\le 1-\gamma/2\) on the retained target vertices,
- \(\max_e\omega(e)=o(1)\).

### 3.2. One nibble round (label-driven)

Fix a small constant \(p=p(\gamma)\in(0,1)\), say \(p=\gamma/100\).

For each currently-unmatched label \(P\in R_{\rm rob}\), independently:

1. Activate \(P\) with probability \(p\).
2. If activated, choose a single incident edge \(e(P)=(x(P),y(P),P)\) with
   probability \(\omega(e)\) among its incident edges (this is a distribution
   since \(L_3(P)=1\)).

Let \(F\) be the set of chosen edges.

**Alteration to enforce matching.** Delete from \(F\) every edge that collides
in \(V_1\cup V_2\), i.e. if two chosen edges share a vertex in \(V_1\) or in
\(V_2\). Call the surviving set \(M\). Then \(M\) is a matching and it covers
exactly the labels that survived the deletion.

### 3.3. Why a constant fraction of activated labels survive

Fix a target vertex \(x\in V_1\). For each label \(P\), the event
\(\{x(P)=x\}\) is a Bernoulli of mean \(\sum_{e\ni x,\,e\ni P}\omega(e)\), and by
linearity there is at most one edge through \(\{x,P\}\). Therefore the number
of chosen edges of \(F\) incident to \(x\) is a sum of independent Bernoullis
with mean
\[
  \mathbb E\,N_x = p\,L_1(x)\le p(1-\gamma/2).
\]
For a Poisson-binomial variable \(N_x\),
\[
  \mathbb E\binom{N_x}{2}=\sum_{i<j}p_i p_j\le \frac12\Big(\sum_i p_i\Big)^2
  =O(p^2).
\]
Hence \(\mathbb P(N_x\ge 2)\le \mathbb E\binom{N_x}{2}=O(p^2)\), and
in particular, with \(p\) chosen small, a chosen edge is deleted due to
collisions at \(x\) with probability \(O(p)\) averaged over its incident edges.
The same holds for collisions in \(V_2\).

Summing over labels, one expects that among the \(\approx p|R_{\rm rob}|\)
activated labels, a \((1-O(p))\) fraction survive the alteration step.

### 3.4. Iteration and maintaining the hypotheses

Remove from \(H\) the vertices covered by \(M\) (both targets and labels), and
delete all incident edges; restrict \(\omega\) to the remaining edges.

Key points one needs to verify (standard in nibble analyses):

1. Only an \(O(p)\) fraction of labels are matched per round, so scaling errors
   accumulate slowly.
2. Because target loads start below \(1-\gamma/2\), the random removal of
   targets deletes only an \(O(p)\) fraction of the weight adjacent to a
   typical remaining label. (Here linearity and "small atoms" control the
   dependence/covariance terms.)
3. After renormalizing per remaining label (to keep label loads \(\approx 1\)),
   the target loads increase by at most a \((1+O(p))\) factor, so they remain
   \(<1-\gamma/4\) provided \(p\ll\gamma\).
4. Exceptional side vertices created by stochastic fluctuations carry
   negligible total label mass; one can throw them away each round.

With these invariants, after \(T\asymp (1/p)\log(1/\eta)\) rounds, the number
of unmatched robust labels drops to at most \(\eta|R_{\rm rob}|\). Taking
\(\eta\to 0\) slowly with \(n\) gives coverage \(1-o(1)\).

### 3.5. Where \(L^2\) enters

The scheme does **not** need pointwise near-regular degrees on \(V_1,V_2,V_3\).
It only needs:

- the *mass* of badly-loaded labels is negligible (from (LS));
- the *mass* of badly-loaded targets is negligible (either assumed as in
  (B-size)--(B-mass), or derived from side \(L^2\) control via trimming);
- "small atoms" so that no single edge dominates a label or target load.

These are exactly the kinds of statements one can hope to obtain from
first/second moment estimates of weighted degrees.


## 4. Status / relation to known results

This lemma is morally standard "nibble technology", but the exact packaging
above (label-driven, with side slack and only \(L^2\) hypotheses) is not a
single universally-cited black box in most combinatorics papers.

What is known/standard:

- Frankl--Rodl / Pippenger--Spencer: almost-perfect matchings in *almost
  regular* uniform hypergraphs with small codegrees (pointwise degree control).
- Kahn's linear-programming/nibble viewpoint: in sparse/linear hypergraphs,
  the matching number is asymptotically close to the fractional matching number
  under suitable "small codegree / small atom / large degree" hypotheses.

What likely needs to be written (but should not require new ideas):

- a clean **weighted** statement specialized to the 3-partite linear setting,
  with **side slack** and allowing **\(L^2\)** (rather than pointwise) control
  by trimming exceptional vertices and tracking that the discarded *mass* is
  negligible.

So: **I would treat Theorem 2.1 as "known in method, but may require a
tailored writeup/citation hunt."** It is not obviously a novel phenomenon, but
it is also not something one can safely cite from memory without locating an
exact reference that matches the weighted/slack/\(L^2\) formulation.

