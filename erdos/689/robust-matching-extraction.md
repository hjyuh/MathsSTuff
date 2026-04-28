# Robust Matching Extraction (Combinatorial Lemma Only)

Created: 2026-04-25

This note isolates the *purely combinatorial* matching statement needed in the
robust prime-difference route (see `robust-prime-difference-route.md`) once the
arithmetic work has produced robust prime-difference edge *counts*.

The goal is: given a labelled edge set
\[
  (x,y,P),\qquad x,y\in A_S(n),\ \ |x-y|=2P,\ \ P\in\mathcal R_2(n),
  \tag{0}
\]
extract a matching of the required size under concrete degree/codegree
hypotheses, with the label set \(\mathcal R_2(n)\) treated as a genuine vertex
class.


## 0. Tripartite hypergraph model and the parity layers

Let \(A_S(n)\) be the main one-token residual set from (1) in
`robust-prime-difference-route.md`, with
\[
  N:=|A_S(n)|=(1+o(1))\frac n{\log n}.
  \tag{1}
\]
Every \(a\in A_S(n)\) is even (indeed \(a=2^k d q\) with \(k\ge 1\)).

Split \(A_S(n)\) into the two forced 2-adic layers
\[
  A_{S,1}(n):=\{a\in A_S(n):v_2(a)=1\}\quad(a\equiv 2\bmod 4),
\]
\[
  A_{S,\ge 2}(n):=\{a\in A_S(n):v_2(a)\ge 2\}\quad(a\equiv 0\bmod 4),
  \tag{2}
\]
so \(A_S(n)=A_{S,1}(n)\sqcup A_{S,\ge 2}(n)\).

Let \(\mathcal R_2(n)\) be the robust primes in \((n/5,n/2]\), as in (7) of
`robust-prime-difference-route.md`, and write
\[
  M:=|\mathcal R_2(n)|.
  \tag{3}
\]

**Parity constraint (why this is automatically tripartite).**  
If \(P\) is odd and \(|x-y|=2P\), then \(v_2(x-y)=1\). Since \(x,y\) are even,
this forces *exactly one* of \(x,y\) to lie in \(A_{S,1}(n)\) and the other to
lie in \(A_{S,\ge 2}(n)\). Equivalently, admissible edges always run between
the two parity layers \(v_2=1\) and \(v_2\ge 2\).

Define the 3-uniform 3-partite hypergraph
\[
  \mathcal H=\mathcal H(n)
  \quad\text{with vertex classes}\quad
  V_1:=A_{S,1}(n),\ V_2:=A_{S,\ge 2}(n),\ V_3:=\mathcal R_2(n),
  \tag{4}
\]
and edge set
\[
  E(\mathcal H)
  :=
  \bigl\{\{x,y,P\}:\ x\in V_1,\ y\in V_2,\ P\in V_3,\ |x-y|=2P\bigr\}.
  \tag{5}
\]

A labelled matching of triples \((x,y,P)\) with "no repeated \(x\), no repeated
\(y\), no repeated \(P\)" is exactly a matching in \(\mathcal H\): a set of
edges with pairwise disjoint vertex sets.


## 1. Automatic codegree/linearity facts for prime-difference edges

The prime-difference model has extremely strong inherent codegree control.

For \(\mathcal H\) defined by (5), for any vertices \(u\ne v\),
\[
  \codeg_{\mathcal H}(u,v):=\#\{e\in E(\mathcal H): u,v\in e\}
\]
satisfies:

1. If \(x\in V_1\) and \(P\in V_3\), then there is **at most one**
   \(y\in V_2\) with \(\{x,y,P\}\in E(\mathcal H)\), namely \(y=x\pm 2P\).
   Hence \(\codeg(x,P)\le 1\).
2. If \(y\in V_2\) and \(P\in V_3\), similarly \(\codeg(y,P)\le 1\).
3. If \(x\in V_1\) and \(y\in V_2\), there is **at most one** label \(P\) with
   \(\{x,y,P\}\in E(\mathcal H)\), namely \(P=|x-y|/2\). Hence \(\codeg(x,y)\le 1\).

Therefore
\[
  \Delta_2(\mathcal H):=\max_{u\ne v}\codeg_{\mathcal H}(u,v)\le 1.
  \tag{6}
\]
In particular, any "small codegree" hypothesis needed by a nibble/Pippenger--Spencer
matching theorem will be satisfied as soon as the relevant degrees tend to
\(\infty\).


## 2. A clean black-box matching lemma (Pippenger--Spencer / Frankl--Rodl)

What remains is purely a *degree/regularity* requirement: the arithmetic step
must show that most vertices have many incident edges, and that the degrees
are not wildly nonuniform.

The following is the standard form one wants to feed with the degree
estimates.

### Lemma 2.1 (Almost-Perfect Matching in a 3-Partite 3-Graph)

Let \(H\) be a 3-partite 3-uniform hypergraph with vertex partition
\(V_1\sqcup V_2\sqcup V_3\) and every edge meeting each part in exactly one
vertex. Write \(m:=\min_i |V_i|\).

Fix \(\eta>0\). Then there exist \(\varepsilon_0=\varepsilon_0(\eta)>0\) and
\(D_0=D_0(\eta)\) such that if:

1. (**Part-wise near-regular degrees.**)  
   For each \(i\in\{1,2,3\}\) there is a number \(D_i\ge D_0\) with
   \[
     \deg_H(v)\in[(1-\varepsilon_0)D_i,(1+\varepsilon_0)D_i]
     \qquad(v\in V_i),
     \tag{7}
   \]

2. (**Small codegrees.**)  
   The maximum codegree satisfies
   \[
     \Delta_2(H)\le \varepsilon_0\min_i D_i,
     \tag{8}
   \]

then \(H\) contains a matching \(M\) of size
\[
  |M|\ge (1-\eta)m.
  \tag{9}
\]

Equivalently, \(M\) leaves at most \(\eta m\) vertices unmatched in each part,
and in particular saturates \((1-\eta)\) of the smallest vertex class.

**Reference/attribution.** This is the standard Frankl--Rodl / Pippenger--Spencer
almost-perfect matching theorem for almost-regular uniform hypergraphs with
small codegrees, applied in the 3-partite setting. A convenient modern
discussion is Kahn's linear-programming perspective on the same theorem. The
3-partite restriction only simplifies the dependencies in the standard proofs.

**Asymptotic corollary.** If \(H=H_n\) is a sequence with \(m=m(n)\to\infty\),
degrees satisfying \(\deg(v)=(1\pm o(1))D_i(n)\) with \(\min_i D_i(n)\to\infty\),
and \(\Delta_2(H_n)=o(\min_i D_i(n))\), then \(|M|=(1-o(1))m(n)\).


## 3. Specialization to the robust prime-difference hypergraph

For \(\mathcal H=\mathcal H(n)\) from (4)--(5), the codegree condition (8) is
automatic: by (6), \(\Delta_2(\mathcal H)\le 1\). So the only nontrivial input
needed to invoke Lemma 2.1 is a part-wise near-regular *degree* estimate with
degrees \(D_i(n)\to\infty\).

Concretely, one wants asymptotics of the form
\[
  \deg_{\mathcal H}(P)
  =
  (1+o(1))D_3(n)
  \qquad(P\in\mathcal R_2(n)),
  \tag{10}
\]
and similarly for \(x\in A_{S,1}(n)\) and \(y\in A_{S,\ge 2}(n)\).

Once (10) and its \(V_1,V_2\) analogues are established with \(D_i(n)\to\infty\),
Lemma 2.1 yields a matching of size
\[
  (1-o(1))\min\bigl(|A_{S,1}(n)|,\ |A_{S,\ge 2}(n)|,\ |\mathcal R_2(n)|\bigr).
  \tag{11}
\]
In the robust route, \(|\mathcal R_2(n)|\asymp N\) while each parity layer has
size \(\asymp N\), so the minimum is \(|\mathcal R_2(n)|\), and the conclusion
is the desired "use almost all labels" matching.


## 4. Why this is enough for the pair-and-singleton threshold

The robust pair-and-singleton route requires a labelled matching size
\[
  t\ge N+E_S(n)-|\mathcal R_{>1/5}(n)|
  =
  \left(1-\frac45\delta_S+o(1)\right)N,
  \tag{12}
\]
where \(E_S(n)=o(N)\) is the exceptional token count outside \(A_S(n)\) and
\(|\mathcal R_{>1/5}(n)|=(4\delta_S/5+o(1))N\).

Also
\[
  |\mathcal R_2(n)|=\left(\frac3{10}\delta_S+o(1)\right)N.
  \tag{13}
\]
When \(\delta_S>10/11\), one has \((1-\tfrac45\delta_S) < \tfrac3{10}\delta_S\),
so the required \(t\) is strictly below \(|\mathcal R_2(n)|\) at first order.

Therefore, producing a matching in \(\mathcal H(n)\) of size
\[
  |\mathcal M_n|=(1-o(1))|\mathcal R_2(n)|
  \tag{14}
\]
is more than enough to meet the threshold (12) for all large \(n\).
