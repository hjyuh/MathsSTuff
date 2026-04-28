# Directed switching and packing model for parity-first Erdos 689

Created: 2026-04-24

This note isolates the parity-first switching problem as an exact directed
graph/hypergraph selection problem, and then records a stronger but more
standard packing reduction to 3-uniform hypergraph matching.

The basic point is simple.  Once odd primes are placed at \(0 \pmod p\), a
prime \(p\) that is later switched to a nonzero residue does not spend one hit
on one target.  It chooses one residue class
\[
  b_p \pmod p,
\]
and thereby fires one whole arithmetic progression
\[
  b_p,\ b_p+p,\ b_p+2p,\ \ldots
\]
through the target set.  The real constraint is therefore "one residue class
per switched prime", not "one target per switched prime".

## 1. Demand vector after the parity-first baseline

Fix \(n\).  Start from the parity-first baseline
\[
  a_2\equiv 1 \pmod 2,
  \qquad
  a_p\equiv 0 \pmod p \quad (p\le n,\ p\ \text{odd prime}).
\]

It is convenient here to enlarge the hard family slightly and define
\[
  H(n)
  :=
  \{2^k q^a \le n : k\ge 0,\ a\ge 1,\ q\ \text{odd prime}\}.
\]
Thus \(H(n)\) contains:

- the odd prime powers \(q^a\) when \(k=0\);
- the even one-odd-prime targets \(2^k q^a\) when \(k\ge 1\).

Let
\[
  Z(n):=\{1\}\cup\{2^t\le n:t\ge 1\}.
\]
These are the parity-only exceptional points.

For \(u=2^k q^a\in H(n)\), write
\[
  \pi(u):=q,
  \qquad
  \kappa(u):=k.
\]

Now fix a set \(R\) of odd primes to be switched away from zero, and for each
\(p\in R\) choose a nonzero residue \(b_p \pmod p\).  Primes outside \(R\) stay
at zero.

Define the demand function on \(H(n)\cup Z(n)\) by
\[
  d_R(u):=
  \begin{cases}
    1_{\kappa(u)\ge 1}+1_{\pi(u)\in R}, & u\in H(n),\\
    1, & u=1,\\
    2, & u=2^t\in Z(n),\ t\ge 1.
  \end{cases}
\]

So:

- an unswitched odd prime power \(q^a\) has demand \(0\);
- a switched odd prime power \(q^a\) has demand \(1\);
- an even target \(2^k q^a\) with \(\pi(u)\notin R\) has demand \(1\);
- an even target \(2^k q^a\) with \(\pi(u)\in R\) has demand \(2\).

### Lemma 1.1: exact residual demands

With the parity-first baseline and switch set \(R\), the final assignment is a
2-cover on \([1,n]\) if and only if
\[
  \#\{p\in R : u\equiv b_p \pmod p\}\ge d_R(u)
  \tag{1}
\]
for every \(u\in H(n)\cup Z(n)\).

Proof.  Let \(u=2^k q^a\in H(n)\).

If \(k=0\), then \(u\) is odd.  The baseline gives one hit from \(p=2\) and
one hit from the zero residue of \(q\), so the baseline coverage is \(2\).
Switching \(q\) removes the second hit exactly when \(q\in R\).  Hence the
number of new hits needed is \(1_{q\in R}=d_R(u)\).

If \(k\ge 1\), then \(u\) is even.  The baseline gives one hit from the zero
residue of \(q\), and no hit from \(p=2\).  If \(q\notin R\), one further hit
is needed; if \(q\in R\), that baseline hit is lost and two new hits are
needed.  Hence the number of new hits needed is
\[
  1+1_{q\in R}=d_R(u).
\]

For \(u=1\), the baseline gives only the parity hit, so one further hit is
needed.  For \(u=2^t\), the baseline gives no hit, so two further hits are
needed.  This is exactly the definition of \(d_R\) on \(Z(n)\).

Finally, each switched prime \(p\in R\) contributes one new hit to \(u\) if and
only if \(u\equiv b_p \pmod p\).  Therefore (1) is exactly the condition that
the new residues supply all residual demand. \(\square\)

The main targets are still the even one-prime points, but the \(k=0\) slice of
\(H(n)\) is important because it contains the switched prime fibers that must
be repaired.

## 2. Exact directed hypergraph model

For a fixed switch set \(R\), let
\[
  V_R:=\{u\in H(n)\cup Z(n):d_R(u)>0\}.
\]

For \(p\in R\) and a nonzero residue \(r \pmod p\), define the residue star
\[
  S_R(p,r):=\{u\in V_R : u\equiv r \pmod p\}.
\]
This is the set of demand vertices hit when \(p\) chooses residue \(r\).

Define a directed hypergraph \(\mathcal D_R\) as follows:

- the tails are the switched primes \(p\in R\);
- the head-vertex set is \(V_R\);
- for each \(p\in R\) and each nonzero \(r \pmod p\), there is one hyperarc
  \[
    e(p,r): p \to S_R(p,r).
  \]

Selecting residues \(b_p\) for \(p\in R\) is exactly the same as selecting one
outgoing hyperarc \(e(p,b_p)\) from each tail \(p\).

For a selected family \(\mathcal S=\{e(p,b_p):p\in R\}\), define
\[
  \deg^-_{\mathcal S}(u):=\#\{p\in R:u\in S_R(p,b_p)\}.
\]

### Proposition 2.1: exact hypergraph reformulation

For fixed \(R\), choosing nonzero residues \(b_p \pmod p\) is equivalent to
choosing one outgoing hyperarc from each tail of \(\mathcal D_R\).  Under this
identification, the switching is valid if and only if
\[
  \deg^-_{\mathcal S}(u)\ge d_R(u)
  \qquad (u\in V_R).
  \tag{2}
\]

Proof.  By construction, \(u\in S_R(p,b_p)\) if and only if \(u\equiv b_p \pmod
p\).  Therefore
\[
  \deg^-_{\mathcal S}(u)
  =
  \#\{p\in R:u\equiv b_p \pmod p\}.
\]
Now apply Lemma 1.1. \(\square\)

This is the exact directed-switching problem: choose one outgoing residue star
from each switched prime so that every demand vertex receives enough indegree.

## 3. Prime-repair digraph, cycles, and paths

Inside \(V_R\), the switched primes themselves appear as vertices of the form
\(u=q\) with \(q\in R\).  Their demand is \(d_R(q)=1\).  Thus every valid
switching must make each \(q\in R\) receive at least one incoming hit from some
other switched prime.

Given a valid selection \(\mathcal S\), define the prime-repair digraph
\[
  G_{\mathcal S}
\]
on vertex set \(R\) by putting a directed edge \(p\to q\) whenever
\[
  q\in S_R(p,b_p),
  \qquad\text{i.e.}\qquad
  q\equiv b_p \pmod p.
\]

Each \(q\in R\) has indegree at least \(1\) in \(G_{\mathcal S}\).

### Lemma 3.1: every solution contains cycle-with-trees structure

For every valid switching, one may choose a subdigraph \(F_{\mathcal S}\subseteq
G_{\mathcal S}\) such that every \(q\in R\) has indegree exactly \(1\).  Every
weakly connected component of \(F_{\mathcal S}\) consists of one directed cycle
with inward arborescences attached to that cycle.

Proof.  For each \(q\in R\), choose one incoming edge \(p\to q\) from
\(G_{\mathcal S}\) and retain only those chosen edges.  The resulting digraph
\(F_{\mathcal S}\) has indegree exactly \(1\) at every vertex.

In any finite digraph with indegree exactly \(1\) everywhere, following
predecessors from any starting vertex must eventually repeat a vertex, hence
encounter a directed cycle.  Since indegree is exactly \(1\), each weakly
connected component contains exactly one directed cycle, and all other vertices
lie on directed trees feeding into that cycle. \(\square\)

So cycles are not optional decoration; they are forced by the repair
requirement.  Paths appear as branches of those inward trees.  The simplest
local gadget is the special case of a 2-cycle.

## 4. Permutation and cycle-cover specialization

The previous section is exact, but still allows one residue class to repair
several switched primes at once.  A cleaner special case is to force the repair
digraph to be a permutation.

### Definition 4.1: repair permutation

A repair permutation on \(R\) is a bijection
\[
  \sigma:R\to R
\]
with \(\sigma(p)\ne p\) for all \(p\in R\).  If \(p\) chooses
\[
  b_p\equiv \sigma(p) \pmod p,
\]
then \(\sigma\) decomposes into directed cycles and automatically gives each
switched prime indegree \(1\).

For such a \(\sigma\), define the coverage count
\[
  c_\sigma(u):=\#\{p\in R:u\equiv \sigma(p)\pmod p\}.
\]

### Proposition 4.2: cycle-cover criterion

Let \(R\) be a set of switched primes and let \(\sigma\) be a repair
permutation on \(R\).  If
\[
  c_\sigma(u)\ge d_R(u)
  \qquad (u\in V_R),
  \tag{3}
\]
then the residues \(b_p\equiv \sigma(p)\pmod p\) give a valid parity-first
switching on \(R\).

Proof.  Because \(\sigma\) is bijective, each \(q\in R\) receives exactly one
incoming repair hit from \(\sigma^{-1}(q)\).  For every \(u\in V_R\),
\[
  c_\sigma(u)
  =
  \#\{p\in R:u\equiv b_p\pmod p\}
\]
by definition.  Therefore (3) is exactly Lemma 1.1. \(\square\)

This makes the scaling of the local two-prime gadget completely transparent.

### Corollary 4.3: scaling the two-prime gadget by pairing

Suppose \(R\) can be partitioned into pairs \(\{p_i,q_i\}\), and for each pair
we choose the 2-cycle
\[
  p_i\to q_i,
  \qquad
  q_i\to p_i.
\]
If every \(u\in V_R\) lies in at least \(d_R(u)\) of the directed progressions
\[
  q_i+jp_i
  \qquad\text{or}\qquad
  p_i+jq_i
  \qquad (j\ge 0),
\]
then the resulting paired 2-cycles give a valid switching.

Proof.  This is Proposition 4.2 for the involution \(\sigma\) that swaps each
\(p_i\) with \(q_i\). \(\square\)

Thus a local 2-cycle scales exactly when one can find a prime pairing whose
paired progressions cover all demands.  Longer cycles are the natural next
level of flexibility.

## 5. Bipartite matching model for the cycle-cover subproblem

Take two labeled copies of \(R\):
\[
  R_{\mathrm{out}}
  \qquad\text{and}\qquad
  R_{\mathrm{in}}.
\]
Let \(B_R\) be the bipartite graph with vertex classes \(R_{\mathrm{out}}\) and
\(R_{\mathrm{in}}\), and edge set
\[
  E(B_R)=\{(p,q):p,q\in R,\ p\ne q\}.
\]
So \(B_R\) is the complete bipartite graph on \(R\times R\) with the diagonal
removed.

An edge \((p,q)\) means: prime \(p\) chooses the residue class \(q \pmod p\).
For each demand vertex \(u\in V_R\), define the constraint set
\[
  E_u:=\{(p,q)\in E(B_R):u\equiv q\pmod p\}.
\]

### Proposition 5.1: exact matching model inside the permutation subclass

For fixed \(R\), the following are equivalent.

1. There is a repair permutation \(\sigma\) on \(R\) satisfying (3).
2. There is a perfect matching \(M\) in \(B_R\) such that
   \[
     |M\cap E_u|\ge d_R(u)
     \qquad (u\in V_R).
     \tag{4}
   \]

Proof.  A perfect matching \(M\) in \(B_R\) is exactly a bijection
\(\sigma:R\to R\) with \(\sigma(p)\ne p\), by matching \(p_{\mathrm{out}}\) to
\(\sigma(p)_{\mathrm{in}}\).  Under this identification,
\[
  |M\cap E_u|
  =
  \#\{p\in R:u\equiv \sigma(p)\pmod p\}
  =
  c_\sigma(u).
\]
Hence (4) is exactly (3). \(\square\)

So the permutation-restricted parity-first problem becomes:

- choose a perfect matching in the directed prime graph \(B_R\);
- the chosen matching must hit every target-constraint set \(E_u\) often
  enough.

This is a precise graph problem, with no further number-theoretic ambiguity.

## 6. A strong sufficient packing lemma

The cycle-cover matching model lets one selected edge \((p,q)\) help many
different targets \(u\) simultaneously.  Standard matching/nibble theorems do
not directly speak that language.  A stronger but more standard reduction is to
force each unit of demand to receive its own matched prime pair.

Form the demand-copy set
\[
  U_R:=\{(u,j):u\in V_R,\ 1\le j\le d_R(u)\}.
\]

Now define a 3-uniform hypergraph \(\mathcal K_R\) with vertex classes
\[
  R_{\mathrm{out}},\qquad R_{\mathrm{in}},\qquad U_R,
\]
and hyperedges
\[
  \{p_{\mathrm{out}},q_{\mathrm{in}},(u,j)\}
\]
whenever
\[
  p,q\in R,\ p\ne q,\ u\equiv q\pmod p.
  \tag{5}
\]

A matching in \(\mathcal K_R\) assigns distinct ordered prime pairs to distinct
demand copies.

### Lemma 6.1: extension of partial derangements

Let \(M_0\) be a matching in \(B_R\) of size at most \(|R|-2\).  Then \(M_0\)
extends to a perfect matching of \(B_R\).

Proof.  Remove the matched vertices of \(M_0\).  Let \(S\subseteq R\) be the
unused out-vertices and \(T\subseteq R\) the unused in-vertices.  Then
\[
  |S|=|T|=:m\ge 2.
\]
The leftover graph is the complete bipartite graph on \(S\times T\), except
that edges \((p,p)\) are missing when \(p\in S\cap T\).

We verify Hall's condition.  Let \(A\subseteq S\).

- If \(|A|=1\), say \(A=\{p\}\), then \(N(A)=T\) or \(T\setminus\{p\}\), so
  \[
    |N(A)|\ge m-1\ge 1=|A|.
  \]
- If \(|A|\ge 2\), then every \(t\in T\) has a neighbor in \(A\): if
  \(t\notin A\), then every \(p\in A\) is adjacent to \(t\); if \(t\in A\),
  choose some \(p\in A\setminus\{t\}\).  Hence \(N(A)=T\), so
  \[
    |N(A)|=m\ge |A|.
  \]

Thus Hall holds, so the leftover graph has a perfect matching.  Adding it to
\(M_0\) gives a perfect matching of \(B_R\). \(\square\)

### Proposition 6.2: hypergraph packing lemma

Assume that \(\mathcal K_R\) has a matching saturating every demand copy in
\(U_R\), and that
\[
  |U_R|\le |R|-2.
  \tag{6}
\]
Then there is a valid parity-first switching on \(R\).

Proof.  Let \(\mathcal M\) be a matching in \(\mathcal K_R\) saturating \(U_R\).
Project each hyperedge
\[
  \{p_{\mathrm{out}},q_{\mathrm{in}},(u,j)\}
\]
to the bipartite edge \((p,q)\in E(B_R)\).  Because \(\mathcal M\) is a
matching, these projected edges are pairwise disjoint in \(B_R\), so they form
a matching \(M_0\) of size \(|U_R|\).

For every demand copy \((u,j)\), one edge of \(M_0\) lies in \(E_u\).  Hence
\[
  |M_0\cap E_u|\ge d_R(u)
  \qquad (u\in V_R).
  \tag{7}
\]
By (6) and Lemma 6.1, \(M_0\) extends to a perfect matching \(M\) in \(B_R\).
Then (7) still holds for \(M\), so Proposition 5.1 gives a valid switching.
\(\square\)

This is a genuine sufficient packing lemma.  It is stronger than the exact
problem, because one matched prime-pair is allowed to pay for only one demand
copy in \(\mathcal K_R\), whereas in the real switching problem one chosen edge
\((p,q)\) can simultaneously cover every target \(u\equiv q \pmod p\).

## 7. Where known matching and nibble theorems could enter

The 3-uniform hypergraph \(\mathcal K_R\) is now in standard matching
territory.  A plausible route is:

1. choose \(R\) in a dyadic prime window \(R\subseteq (P,2P]\);
2. prove near-regular degree lower bounds for the demand-copy vertices
   \((u,j)\);
3. prove codegrees are uniformly small;
4. invoke a Pippenger-Spencer/Frankl-Rodl type almost-perfect matching theorem,
   or a modern nibble theorem for sparse almost-linear 3-graphs.

Here are the exact combinatorial quantities.

For a demand copy \((u,j)\in U_R\),
\[
  \deg_{\mathcal K_R}(u,j)
  =
  \sum_{p\in R}
  \#\{q\in R:u\equiv q\pmod p\}.
  \tag{8}
\]
If \(R\subseteq (P,2P]\), then the interval length is \(<P\), so for each fixed
\(p\in R\) there is at most one \(q\in R\) with \(u\equiv q \pmod p\).  In that
case
\[
  \deg_{\mathcal K_R}(u,j)
  =
  \#\{p\in R: u\bmod p \in R\}.
  \tag{9}
\]

For two distinct demand copies \((u,i)\ne (v,j)\), a common hyperedge must use
some \(p\in R\) and \(q\in R\) with
\[
  u\equiv q\equiv v\pmod p,
\]
so \(p\mid (u-v)\).  In a dyadic window \(R\subseteq (P,2P]\), this gives the
codegree bound
\[
  \codeg_{\mathcal K_R}((u,i),(v,j))
  \le
  \#\{p\in R:p\mid (u-v)\}.
  \tag{10}
\]
Since \(|u-v|\le n\), the right side is at most
\[
  \frac{\log n}{\log P}
\]
and is often \(0\) or \(1\).  So the codegree side is plausible.

The missing arithmetic input is the degree side.  One needs a lower bound of
the shape
\[
  \deg_{\mathcal K_R}(u,j)\ge (1+\eta)D
  \tag{11}
\]
for all, or almost all, demand copies, with \(D\) large and \(\eta>0\).
Concretely, this means:

> for each hard target \(u=2^k q^a\), there should be many primes \(p\in R\)
> for which the least positive residue of \(u \pmod p\) is itself a prime of
> \(R\).

That is the exact arithmetic statement needed to feed \(\mathcal K_R\) into a
nibble theorem.

## 8. Exact gaps between the models

There are three different gaps, and they should not be confused.

### Gap A: arithmetic degree lower bounds

Even for the permutation-matching model of Proposition 5.1, one needs many
candidate successor primes \(q\) for each target \(u\).  In a dyadic window
this is the count
\[
  D_R(u):=\#\{p\in R:u\bmod p \in R\}.
  \tag{12}
\]
Nothing in the graph reformulation proves that \(D_R(u)\) is large.  This is a
distribution problem for the special set \(H(n)=\{2^k q^a\}\) in prime-labeled
residue classes.

### Gap B: prime-side branching

The exact directed hypergraph model from Proposition 2.1 allows one residue
class of one prime \(p\) to repair several switched primes at once.  On the
prime side this creates the inward trees from Lemma 3.1.  The permutation model
of Proposition 4.2 discards that possibility by forcing each switched prime to
have exactly one designated successor and exactly one designated predecessor.

So Proposition 5.1 captures a clean and tractable subclass, but not every
possible switching configuration.  Any proof based on perfect matchings in
\(B_R\) must therefore justify the loss of this extra branching power, or prove
that a near-optimal solution can be replaced by a cycle cover.

### Gap C: edge reuse

The permutation-matching model of Proposition 5.1 is weaker than the packing model of
Proposition 6.2, because one matched edge \((p,q)\) may simultaneously cover
many targets \(u\equiv q \pmod p\).  The 3-uniform packing lemma discards that
multiplicity and is therefore only sufficient, not equivalent.

So there are really two possible proof routes:

1. Prove the strong packing lemma by applying a known hypergraph matching or
   nibble theorem to \(\mathcal K_R\).
2. Work directly with the cycle-cover side-constrained matching problem in
   \(B_R\), where one selected edge is allowed to satisfy many target
   constraints at once.

Route 1 is more standard.  Route 2 is closer to the true switching problem.

## 9. Final formulation of the directed switching problem

For parity-first Erdos 689, the clean exact formulation is Proposition 2.1:

1. choose a switch set \(R\) of odd primes;
2. for each \(p\in R\), choose one nonzero residue class \(b_p \pmod p\);
3. regard this as choosing one outgoing star \(e(p,b_p)\) in the directed
   hypergraph \(\mathcal D_R\);
4. require every target vertex \(u\in H(n)\cup Z(n)\) to receive indegree at
   least \(d_R(u)\).

Inside that exact model, the cycle-cover reduction is:

1. restrict to repair permutations \(\sigma:R\to R\);
2. equivalently choose a perfect matching in the bipartite graph \(B_R\);
3. require the selected matching to hit each target-constraint set \(E_u\)
   often enough.

The prime-repair part of the problem is encoded by the fact that switched
primes are themselves vertices \(u=q\in H(n)\), so they require indegree one.
The hard even targets \(2^k q^a\) require indegree one or two according to
whether \(q\) is kept at zero or switched.  Cycles are forced because any
repair digraph with indegree at least one contains directed cycles, and the
local two-prime gadget is just the 2-cycle case of the cycle-cover reduction.

The best unconditional statement obtained here is Proposition 6.2: a matching
that saturates the 3-uniform demand-copy hypergraph \(\mathcal K_R\) is enough.
The remaining gap is arithmetic, not definitional: prove degree lower bounds
for \(u=2^k q^a\) in prime windows, and then either invoke a standard nibble on
\(\mathcal K_R\) or attack the exact side-constrained perfect matching problem
in \(B_R\), while keeping track of the extra branching power available in the
full directed-star model.
