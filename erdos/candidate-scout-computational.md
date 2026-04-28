# Erdos Problems: Computational/Experimental Scout

Generated: 2026-04-26.

Scope: open Erdos Problems with a concrete finite search space, exact certificate path, or formalization-friendly discrete structure. I intentionally deprioritized problems whose only visible route is deep analytic number theory or asymptotic estimates without a finite/combinatorial foothold.

Primary sources: [erdosproblems.com](https://www.erdosproblems.com/), the public [teorth/erdosproblems database](https://github.com/teorth/erdosproblems), and targeted web searches for computational/literature context.

## Selection Criteria

- Status is open, falsifiable, or verifiable on erdosproblems.com.
- A counterexample or witness, if it exists, is a finite object that can be independently checked.
- The search can be encoded as SAT/CP-SAT/ILP/exact cover, graph generation, exact rational arithmetic, or finite dynamic programming.
- A useful partial output is possible without solving the problem: bounded search certificates, near-miss databases, structural conjecture mining, or Lean-checkable certificate verifiers.

## Top 5

| Rank | Problem | Type | Why it is computationally attractive | Difficulty |
|---:|---|---|---|---:|
| 1 | [#993](https://www.erdosproblems.com/993) independent set sequence of trees | finite graph counterexample search + DP | canonical tree enumeration, independence polynomial DP, strong conjecture-mining surface | 6 |
| 2 | [#617](https://www.erdosproblems.com/617) balanced edge colorings of complete graphs | SAT/local-search finite counterexample | first unknown case is concrete; certificate is just an edge-color matrix | 7 |
| 3 | [#835](https://www.erdosproblems.com/835) Johnson graph coloring | finite witness search / coding theory bounds | highly structured coloring problem; existing partial reductions leave prime-minus-one cases | 8 |
| 4 | [#64](https://www.erdosproblems.com/64) power-of-two cycles | graph generation / SAT counterexample search | finite counterexample would settle; known computational foothold in cubic graphs | 8 |
| 5 | [#307](https://www.erdosproblems.com/307) reciprocal sums over primes | exact arithmetic witness search | verifiable finite example would prove it; meet-in-the-middle and modular filters apply | 7 |

## 1. Problem #993: Independent Set Sequence of a Tree or Forest

Source: [Erdos Problem #993](https://www.erdosproblems.com/993). Supporting literature: Basit-Galvin, [On the independent set sequence of a tree](https://arxiv.org/abs/2006.12562), and Galvin-Hilyard, [The independent set sequence of some families of trees](https://arxiv.org/abs/1701.02204).

Problem statement:

> The independent set sequence of any tree or forest is unimodal. Equivalently, if `i_k(G)` counts independent vertex sets of size `k`, then for every tree/forest `T` the sequence `i_0(T), i_1(T), ...` increases up to some point and then decreases.

What can be computed/formalized:

- Enumerate non-isomorphic trees and forests up to a size cutoff using canonical labels.
- Compute independence polynomials by rooted-tree DP:
  - `P_in(v) = x * product P_out(child)`.
  - `P_out(v) = product (P_in(child) + P_out(child))`.
- Track not just violations but "near violations": locations where `i_j - i_{j+1}` is small or sign changes are barely avoided.
- Formalize the recurrence and a certificate checker in Lean: given a tree adjacency list and polynomial coefficients, verify the coefficients count independent sets and check non-unimodality/unimodality.

Possible finite certificates or conjecture mining:

- Disproof certificate: a tree/forest adjacency list plus its independence polynomial with two separated rises after a fall.
- Bounded-search certificate: canonical enumeration log plus hash of all tree polynomials up to `n`.
- Mining targets: operations on rooted trees that preserve unimodality; finite-state reductions by polynomial-pair dominance; families where the mode is forced into a narrow interval.

Difficulty: 6/10. The computation is straightforward and falsification is cheap to verify, but a proof likely needs a structural invariant.

First concrete experiment:

Implement an unlabeled-tree enumerator pipeline using `networkx.generators.nonisomorphic_trees` or nauty, compute independence polynomials up to the largest feasible `n`, and output the 100 closest near-violations ranked by minimum normalized gap around the mode.

## 2. Problem #617: Balanced Colorings of `K_{r^2+1}`

Source: [Erdos Problem #617](https://www.erdosproblems.com/617).

Problem statement:

> Let `r >= 3`. If the edges of `K_{r^2+1}` are `r`-colored, then there exist `r+1` vertices with at least one color missing on the edges of the induced `K_{r+1}`.

The page notes this is equivalent to nonexistence of a balanced coloring; Erdos and Gyarfas proved the cases `r=3` and `r=4`, while a related `r^2`-vertex version fails for infinitely many `r`.

What can be computed/formalized:

- Encode the first unknown case `r=5` as a coloring of the 325 edges of `K_26`.
- Constraint: every 6-vertex subset must see all five colors.
- Use SAT/CP-SAT with variables `c_{ij} in {1,...,5}` and clauses forbidding any 6-set/color pair from omitting that color.
- Add symmetry breaking: fix the color pattern on edges incident to vertex 1; quotient by color permutations; test cyclic or affine-plane-inspired ansatzes.
- Formalize a checker for an explicit coloring matrix, or a bounded UNSAT certificate if a SAT solver can emit one.

Possible finite certificates or conjecture mining:

- Disproof certificate: a symmetric 26-by-26 color matrix in which every 6-set sees all 5 colors.
- Positive bounded certificate for `r=5`: DRAT/LRAT UNSAT proof for the SAT encoding, with a small independently checked translator.
- Mining targets: color-degree distributions, forbidden local types on 6/7 vertices, and whether near-colorings resemble known balanced colorings on `r^2` vertices.

Difficulty: 7/10. The first SAT instance is large but concrete; local search and symmetry breaking should produce meaningful data quickly.

First concrete experiment:

Build a CP-SAT/local-search model for `r=5`, seed it with known balanced colorings on 25 vertices if available, add the 26th vertex, and minimize the number of deficient `(6-set, color)` constraints.

## 3. Problem #835: Coloring `k`-Subsets of `[2k]`

Source: [Erdos Problem #835](https://www.erdosproblems.com/835) and its [discussion thread](https://www.erdosproblems.com/forum/thread/835).

Problem statement:

> Does there exist a `k > 2` such that the `k`-sized subsets of `{1,...,2k}` can be colored with `k+1` colors so that for every `(k+1)`-subset `A`, all `k+1` colors appear among the `k`-subsets of `A`?

The page gives the equivalent form: is `chi(J(2k,k)) = k+1` for some `k > 2`, where `J(2k,k)` is the Johnson graph. It also records that `3 <= k <= 8` are false, and Ma-Tang prove false for `k > 2` not of the form `p-1` for prime `p`.

What can be computed/formalized:

- First natural surviving cases are `k+1` prime, especially `k=10` and `k=12`.
- Encode proper `(k+1)`-coloring of `J(2k,k)` as SAT, or encode the equivalent large set/Steiner-system obstruction suggested in the discussion thread.
- Use coding-theory bounds: independent sets of `J(2k,k)` correspond to constant-weight binary codes of length `2k`, weight `k`, distance at least 4.
- Formalize the Johnson graph equivalence and exact certificate checking for either a coloring witness or a lower-bound proof from code-size inequalities.

Possible finite certificates or conjecture mining:

- Positive certificate: a coloring table for all `binom(2k,k)` vertices.
- Negative bounded certificate: an exact upper bound on `A(2k,4,k)` implying `chi(J(2k,k)) > k+1`, plus a formal proof of the bound.
- Mining targets: complement-invariance of color classes, orbit partitions under stabilizers, failed color-class designs that approximate large Steiner systems.

Difficulty: 8/10. The problem is finite and structured, but the first open SAT instances are huge and need symmetry/coding-theory reductions.

First concrete experiment:

For `k=10`, generate orbits of `10`-subsets under a stabilizer fixing one color class candidate, then run a hybrid search: greedy maximum independent sets for candidate color classes, followed by exact cover to see whether 11 such classes can partition all `10`-subsets.

## 4. Problem #64: Power-of-Two Cycles in Minimum-Degree-3 Graphs

Source: [Erdos Problem #64](https://www.erdosproblems.com/64). Related web context: searches for the Erdos-Gyarfas conjecture show prior computational work on cubic/cubic-planar cases and lower bounds on possible counterexample size.

Problem statement:

> Does every finite graph with minimum degree at least 3 contain a cycle of length `2^k` for some `k >= 2`?

The page records that this was conjectured by Erdos and Gyarfas, that they expected a negative answer in stronger minimum-degree forms, and that Liu-Montgomery proved a much stronger positive result under sufficiently large average degree.

What can be computed/formalized:

- Search cubic graphs first: a minimum counterexample can often be regularized or at least compared against cubic obstructions.
- Use graph generation (`geng -d3`, cubic graph generators) and filter out graphs containing cycles of lengths `4, 8, 16, ... <= n`.
- SAT formulation: graph edges are Boolean variables, degree constraints enforce minimum degree 3, and forbidden-cycle clauses eliminate powers of two.
- Formalize a counterexample checker: min degree, simple graph, and absence of cycles with lengths in `{4,8,16,...}`.

Possible finite certificates or conjecture mining:

- Disproof certificate: adjacency list of a finite graph with min degree at least 3 and no power-of-two cycle.
- Positive bounded certificate: exhaustive generation for all cubic graphs up to `N`, with reproducible canonical labels and hashes.
- Mining targets: unavoidable local configurations forcing 4- or 8-cycles; cycle-space constraints modulo 2; reductions from a minimal counterexample to cubic or nearly cubic graphs.

Difficulty: 8/10. It has a clean finite certificate and a history of computational footholds, but the search space grows brutally and known partial results already cover many friendly families.

First concrete experiment:

Enumerate connected cubic graphs up to the practical nauty limit, filter for no `C_4` and no `C_8`, compute the shortest power-of-two cycle present, and store extremal graphs maximizing that shortest power-of-two cycle length.

## 5. Problem #307: Product of Two Prime-Reciprocal Sums

Source: [Erdos Problem #307](https://www.erdosproblems.com/307) and its [discussion thread](https://www.erdosproblems.com/forum/thread/307).

Problem statement:

> Are there two finite sets of primes `P,Q` such that
>
> `1 = (sum_{p in P} 1/p)(sum_{q in Q} 1/q)`?

The page notes this is verifiable by a finite example, that `P` and `Q` must be disjoint, and that `sum_{p in P union Q} 1/p >= 2`, hence at least 60 primes are involved.

What can be computed/formalized:

- Exact rational search over prime subsets using meet-in-the-middle.
- Treat one side as `S(P) = a/b`; then the other side must sum to `b/a`, giving a constrained reciprocal-prime subset target.
- Use modular filters before exact rational arithmetic: denominators are squarefree products of primes, and divisibility constraints can prune many candidates.
- Formalize a witness checker in Lean: verify primality, disjointness, exact rational sums, and the product identity.

Possible finite certificates or conjecture mining:

- Positive certificate: two explicit prime lists `P,Q`.
- Search certificates: no witness below a prime cutoff, with a machine-checkable branch-and-bound transcript for a restricted model.
- Mining targets: near misses where `S(P)S(Q)-1` has small numerator, families where `P` almost determines `Q`, and weakened coprime versions that produce templates.

Difficulty: 7/10. A witness would be easy to verify, and the search is exact, but the minimum size condition suggests the first solution, if it exists, may be arithmetically large.

First concrete experiment:

Write a rational meet-in-the-middle search over the first `N` primes, but rank partial sums by closeness to intervals that could pair to product 1. Log exact near misses and factor the forced residual denominators to see whether the remaining target can plausibly be represented by unused prime reciprocals.

## Near Misses Worth Revisiting

- [#583](https://www.erdosproblems.com/583): Gallai path decomposition. Very good exact-cover target; I left it just below the top five because the likely payoff is bounded verification and structural mining rather than a plausible finite witness in the near term.
- [#743](https://www.erdosproblems.com/743): tree packing conjecture. Clean SAT/exact-cover formulation and verified for small `n`, but quickly becomes a large packing problem.
- [#167](https://www.erdosproblems.com/167): Tuza's triangle packing/covering conjecture. Excellent ILP duality surface, but heavily studied and likely needs more than raw search.
- [#723](https://www.erdosproblems.com/723): projective plane of non-prime-power order. It is finite and certificate-driven, but order 12 is a historically massive search problem.
- [#242](https://www.erdosproblems.com/242): Erdos-Straus. It has computational footholds and huge verification records, but it is too number-theoretic and famous for this particular shortlist.
