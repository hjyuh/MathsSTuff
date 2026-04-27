# EP617 Phase 1 Graph Cuts B

Date: 2026-04-26

Setup for this branch:

- `G` has `n = 26` vertices.
- `60 <= e(G) <= 65`.
- Every 6-set `S` satisfies `1 <= e(S) <= 11`.
- `omega(G) <= 4` (the no-`K_5` minimum-colour branch).

I only record cuts that are provably implied by those hypotheses. Several of them are
not "new information" beyond the 6-set bounds; their value is that they compress many
6-set clauses into sharper local patterns that should propagate earlier in SAT.

## Notation

- `e(X)` means the number of edges induced by a vertex set `X`.
- `N(v)` is the open neighbourhood of `v`.
- For a set `A`, `N(A) = intersection_{a in A} N(a)` is its common neighbourhood.
- For a set `A`, `M(A)` denotes the vertices outside `A` adjacent to none of `A`.

## Master templates

For disjoint sets `A, B` with `|A| + |B| = 6`,

- lower template: `e(A) + e(B) + e(A,B) >= 1`,
- upper template: `e(A) + e(B) + e(A,B) <= 11`.

All cuts below are instances of those two inequalities.

## 1. Degree-side cuts: safe, but weak

### Lemma 1.1: non-isolated vertices

For every vertex `v`, let `M(v)` be the `25 - d(v)` vertices nonadjacent to `v`. Any
5-set inside `M(v)` cannot be independent, because together with `v` it would form a
6-set with 0 edges. Hence `alpha(G[M(v)]) <= 4`.

Therefore `complement(G[M(v)])` is `K_5`-free, so by Turan

`e(G[M(v)]) >= C(s,2) - t_4(s)`, where `s = 25 - d(v)`.

Since `e(G) >= d(v) + e(G[M(v)])`, we get

`e(G) >= d(v) + C(25-d(v),2) - t_4(25-d(v))`.

At `d(v) = 0` this gives `e(G) >= C(25,2) - t_4(25) = 66`, impossible because
`e(G) <= 65`. So `delta(G) >= 1`.

Comment:

- This is the clean Turan degree cut available from the hypotheses alone.
- I do not see a safe proof of `delta(G) >= 2` or any useful absolute `Delta(G)` upper
  bound from these hypotheses only. Degree cuts should stay low priority.

## 2. Upper-side common-neighbourhood cuts

### Lemma 2.1: triangle common neighbourhood is tiny

If `T` is a triangle, then `|N(T)| <= 2`.

Proof:

If `x, y, z` are three vertices adjacent to all of `T`, then on the 6-set
`T union {x,y,z}` we already have at least

- `3` edges inside `T`, and
- `9` edges between `T` and `{x,y,z}`.

So `e(T union {x,y,z}) >= 12`, contradicting the upper 6-set bound `<= 11`.

Implementation value:

- Very strong.
- Cheap to check lazily.
- Does not require any auxiliary counting gadget.

### Lemma 2.2: any 4-set with at least 4 edges has at most one common neighbour

Let `A` be a 4-set with `e(A) >= 4`. Then `|N(A)| <= 1`.

Proof:

If `x` and `y` are both adjacent to all four vertices of `A`, then on the 6-set
`A union {x,y}` we have at least

- `e(A) >= 4`, and
- `8` cross edges from `{x,y}` into `A`.

Hence `e(A union {x,y}) >= 12`, contradiction.

Important special cases:

- a diamond (`K_4` minus one edge) has at most one common neighbour;
- a `C_4` has at most one common neighbour;
- a `K_4` has at most one common neighbour from this argument, and in fact none by
  `omega(G) <= 4`.

Implementation value:

- This is a good compressed replacement for many "upper-6" checks around dense 4-sets.
- I would implement it lazily, not eagerly.

### Lemma 2.3: `K_4` pair-star inequality

Let `Q` be a `K_4`, and let `x,y` be vertices outside `Q`. Then

`deg_Q(x) + deg_Q(y) + 1_{xy in E} <= 5`.

Proof:

On the 6-set `Q union {x,y}` we have exactly

`e(Q union {x,y}) = 6 + deg_Q(x) + deg_Q(y) + 1_{xy in E}`.

The upper 6-set bound gives the claim.

Useful corollaries:

1. At most one outside vertex can send 3 edges into a fixed `K_4`.
2. If `x` sends 3 edges into `Q` and `y` sends 2 edges into `Q`, then `xy` must be
   absent.
3. If `xy` is present, then `deg_Q(x) + deg_Q(y) <= 4`.

Implementation value:

- This is the cleanest `K_4`-star surrogate in the no-`K_5` branch.
- It is stronger than merely forbidding a common neighbour of the whole `K_4`.
- High priority once a candidate graph actually contains `K_4`s.

### Lemma 2.4: the common neighbourhood of an edge is internally tiny

Let `uv` be an edge, and set `C = N(u) intersection N(v)`.

Then every 4-set `X` inside `C` satisfies `e(X) <= 2`.

Proof:

On the 6-set `{u,v} union X` we already have

- the edge `uv`, and
- `8` edges from `u,v` into `X`.

So `1 + 8 + e(X) <= 11`, hence `e(X) <= 2`.

Structural corollary:

`G[C]` is a disjoint union of isolated vertices, single edges, and `P_3` components.
Indeed, a connected 4-vertex subgraph has at least 3 edges, which is forbidden on each
4-set in `C`. Therefore every component has size at most 3, and any 3-vertex component
has at most 2 edges.

Numerical corollary:

`e(G[C]) <= floor(2|C|/3)`.

Implementation value:

- Safe and reasonably sharp.
- More expensive than the triangle and dense-4-set cuts, so I would not lead with it.

## 3. Lower-side common-nonneighbourhood cuts

### Lemma 3.1: common nonneighbourhood of a nonedge has independence number at most 3

Let `uv` be a nonedge, and let `D = M({u,v})`, the vertices adjacent to neither `u`
nor `v`.

Then every 4-set `X` inside `D` has `e(X) >= 1`. Equivalently, `alpha(G[D]) <= 3`.

Proof:

If some 4-set `X subset D` had `e(X) = 0`, then the 6-set `{u,v} union X` would have
0 edges, contradicting the lower 6-set bound.

### Lemma 3.2: a quantitative nonedge cut

With `D` as above and `t = |D|`, we have

`e(G[D]) >= C(t,2) - t_3(t)`,

because `alpha(G[D]) <= 3` means `complement(G[D])` is `K_4`-free.

Also, each of the other `24 - t` vertices outside `{u,v} union D` is adjacent to at
least one of `u,v`, so they contribute at least `24 - t` edges incident to `{u,v}`.

Hence

`e(G) >= (24 - t) + C(t,2) - t_3(t)`.

At `t = 21` the right-hand side is

`3 + (C(21,2) - t_3(21)) = 3 + (210 - 147) = 66`,

contradicting `e(G) <= 65`. Therefore every nonedge satisfies

`|M({u,v})| <= 20`.

Equivalent form:

For every nonedge `uv`,

`|N(u) union N(v)| >= 4`.

Implementation value:

- This is a real pairwise cardinality cut, not just a pattern prohibition.
- It probably needs auxiliary support if encoded eagerly, so I would place it behind
  the pure local-pattern cuts.

### Lemma 3.3: independent 4-sets force a clique on their common nonneighbours

Let `I` be an independent 4-set, and let `D = M(I)`.

Then `D` is a clique. In particular, `|D| <= 4` because `omega(G) <= 4`.

Proof:

Take any `x,y in D`. They are nonadjacent to all four vertices of `I`. If `xy` were
also absent, then `I union {x,y}` would be a 6-set with 0 edges, impossible. So every
pair in `D` is adjacent.

Implementation value:

- This is the cleanest lower-side local cut I found.
- Since graphs in this edge range should contain many independent 4-sets, this may be
  genuinely useful in the sparse minimum-colour branch.

## 4. Strongest cuts and implementation priority

### Priority 1

1. Triangle codegree cut: every triangle has at most 2 common neighbours.
2. Independent-4 dual cut: the common nonneighbourhood of an independent 4-set is a
   clique, hence has size at most 4.

Why first:

- Both are short local patterns.
- Both are easy to validate lazily from a candidate graph.
- Neither needs a global cardinality gadget.

### Priority 2

3. Dense-4-set common-neighbourhood cut: every 4-set with at least 4 edges has at most
   one common neighbour.
4. `K_4` pair-star inequality: for a `K_4`, every outside pair `x,y` satisfies
   `deg_Q(x) + deg_Q(y) + 1_{xy} <= 5`.

Why second:

- These are strong, but they want dense-seed detection.
- They should pay off mainly after the solver starts proposing actual `K_4` or diamond
  structure.

### Priority 3

5. Nonedge common-nonneighbourhood bound: for every nonedge `uv`,
   `|M({u,v})| <= 20`.
6. Edge common-neighbourhood structure: for every edge `uv`, the graph on
   `N(u) intersection N(v)` has every 4-set of edge-count at most 2, hence consists
   only of isolated vertices, edges, and `P_3`s.

Why third:

- These are safe and nontrivial.
- They are heavier to encode directly.
- I would add them only after the shorter pattern cuts are in place.

### Low priority / analytic only

7. Degree-side Turan cuts, including `delta(G) >= 1`.

Why low:

- Safe but weak.
- They do not look competitive as first SAT-side cuts.

## Bottom line

The strongest provable local cuts I see for the no-`K_5` minimum-colour branch are:

1. triangle common neighbourhood at most 2;
2. independent 4-set common nonneighbourhood is a clique of size at most 4;
3. any 4-set with at least 4 edges has at most one common neighbour;
4. `K_4` pair-star inequality;
5. for every nonedge `uv`, the common nonneighbourhood has size at most 20.

I do not recommend spending implementation time on stronger raw degree bounds unless a
new argument appears; the stated hypotheses do not seem to force much beyond
non-isolation.
