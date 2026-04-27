# EP617 Sprint Status

Updated 2026-04-26.

## Problem

For every integer `r >= 3`, every `r`-edge-colouring of `K_{r^2+1}` should contain `r+1` vertices whose induced complete graph misses at least one colour.

Equivalently, there should be no balanced `r`-colouring of `K_{r^2+1}` in which every `(r+1)`-set sees all `r` colours.

The first visibly open case is `r=5`: a 5-colouring of the 325 edges of `K_26` such that every 6-set sees all 5 colours.

## Completed Work

1. Verified live status:
   - EP617 is still listed as falsifiable/open.
   - The only visible forum comment is a typo correction.
   - Erdős-Gyárfás proved the `r=3,4` cases and gave balanced `K_{r^2}` constructions for infinitely many `r`.

2. Affine-plane construction:
   - For `r=5`, `F_5^2` with colors from affine slopes, merging two slope classes, gives a balanced `K_25`.
   - A direct line-intersection argument shows no such affine construction can be extended by adding one vertex.
   - SAT confirmed all 15 slope merges are UNSAT as one-vertex extensions.

3. Structured families ruled out by SAT:
   - no cyclic distance coloring of `K_26`;
   - no cyclic `K_25` core plus arbitrary extra star;
   - no `F_5^2` translation-invariant Cayley `K_25` core plus arbitrary extra star.

4. Solver model:
   - Full `r=5` CNF has:
     - variables: 1625
     - clauses: 1,154,726
     - coverage clauses: 1,151,150
   - `glucose4` with 1,000,000 conflict budget returned `unknown`.
   - A WalkSAT-style search reached a best near miss with 1,268 missing-color violations.

5. Useful necessary constraints:
   - For each color class `G_c` on 26 vertices:
     - `alpha(G_c) <= 5`
     - `omega(G_c) <= 5`
     - `56 <= e(G_c) <= 101`
   - For each q-set and each color, Turan lower/upper cuts apply.

6. Failed shortcut:
   - It would be enough to prove that every 26-vertex graph with both `alpha <= 5` and `omega <= 5` has at least 66 edges.
   - SAT found a 65-edge `(6,6)` Ramsey graph candidate, so this edge-count shortcut cannot prove the `r=5` case.

7. Strengthened minimum-colour route:
   - A Kang-Pikhurko extremal theorem for non-5-partite `K_6`-free graphs gives the sharper safe bound `60 <= e_c <= 85` for every colour class in a valid `K_26` colouring.
   - Since the average colour size is 65, a minimum colour may be assumed to have exact size `k` with `60 <= k <= 65`.
   - Encoded the projected K5-star rule for one colour: if `Q` is a `K_5` in the minimum colour, every outside vertex has at most one minimum-colour edge into `Q`.
   - Added `one_color_strengthened.py`, a lazy-cut SAT test for the proposed one-colour lemma: every 6-set has between 1 and 11 minimum-colour edges, and K5-star projection holds.
   - Exact sweeps for `e=60..65` with lazy upper-6 and K5-star cuts remain `unknown`, but every candidate found so far violates at least one of the new cuts.
   - Improved the lazy encoding with sequential-cardinality upper-6 cuts and short auxiliary K5 indicators.
     Endpoint runs:
     - `e=60`: 80 lazy rounds, 86,245 lazy clauses, still `unknown`.
     - `e=65`: 80 lazy rounds, 172,663 lazy clauses, still `unknown`.
   - The no-K5 minimum-colour branch did not return a first model in a 5-minute test, but this is not yet a proof.

8. Full minimum-colour profile cubes:
   - Added `mincolor_profile_sat.py`, which fixes colour 0 as a minimum colour, sets `e_0=k`, and fixes a sorted residual profile `(e_1,e_2,e_3,e_4)`.
   - Profile counts match the expected small cube list:
     - `k=60`: 185 profiles
     - `k=61`: 108 profiles
     - `k=62`: 54 profiles
     - `k=63`: 23 profiles
     - `k=64`: 6 profiles
     - `k=65`: 1 profile
   - The perfectly balanced branch `k=65`, profile `(65,65,65,65)`, is still `unknown` after 1.5M Glucose conflicts.
   - All six `k=64` profiles were touched at 100k Minisat conflicts or a 60s wall cutoff; all remain `unknown`.
   - Six sample `k=63` profiles, three low-index and three high-index, were touched at 75k Minisat conflicts or a 45s wall cutoff; all remain `unknown`.
   - No SAT certificate has been found in any minimum-colour profile branch tested so far.

## Current Estimate

Closure of the `r=5` finite case: about 49%.

Closure of full EP617: about 30%.

Why not higher:

- We have not found a counterexample for `r=5`.
- We do not have an UNSAT certificate for `r=5`.
- The full all-`r` positive statement would need theory beyond one finite case.
- The strengthened one-colour lemma is still a SAT/search target, not a theorem.
- The exact-count profile cubes are harder than expected; none closed quickly under generic CDCL.

Why not lower:

- The first open case is finite and exactly encoded.
- The natural affine `K25` extension is completely eliminated.
- The problem now has a reproducible computational pipeline.
- The minimum-colour window has been reduced to six exact edge sizes, `60..65`, with a clear one-colour lemma that would settle `r=5` if proved.
- The full SAT search now has a reproducible branch table rather than one monolithic CNF.

## Best Next Moves

1. Improve the solver encoding:
   - use the sharpened `60..85` edge-count bounds in the full SAT encoding;
   - cube by minimum-colour size `k=60..65`;
   - add residual profile cubes for the other four colour classes.

2. Attack `r=5` through color-class Ramsey graphs:
   - focus on minimum-colour skeletons with `60..65` edges;
   - require every 6-set to have `1..11` skeleton edges;
   - require the projected K5-star rule.

3. Search for non-affine structured candidates:
   - cyclic colorings on `Z/26`,
   - Cayley colorings on abelian groups of order 26 or 25 plus one special point,
   - perturbations of affine `K25` rather than fixed affine extension.

4. If the no-K5 minimum-colour branch is proved UNSAT:
   - anchor a minimum-colour `K_5`;
   - cube outside-vertex star patterns under the `S_5 x S_4` stabilizer;
   - solve the residual 4-colour problem.
