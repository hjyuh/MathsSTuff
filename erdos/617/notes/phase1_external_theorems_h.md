# EP617 Phase 1 External Theorem Audit (Agent H)

Date: 2026-04-26

## Branch translated into a one-graph problem

Let `G` be the minimum-colour class in the `r=5` search branch. In the no-`K5`
subcase under discussion, the one-colour constraints become:

- `|V(G)| = 26`;
- `e(G) in {60,61,62,63,64,65}`;
- `G` is `K5`-free, so `omega(G) <= 4`;
- every 6-set contains at least one `G`-edge, equivalently the complement
  `H = \bar G` is `K6`-free;
- therefore `alpha(H) = omega(G) <= 4`.

So the external target is:

> does there exist a 26-vertex graph `H` with `e(H) in {260,...,265}`,
> `H` `K6`-free, and `alpha(H) <= 4`?

This is the cleanest complement formulation for literature lookup.

## What the existing local data already says

- The local `(6,6)` Ramsey SAT run at
  `erdos/617/results/ramsey_26_6_max64_minisat_budget2000000_summary.json`
  found a 64-edge graph with `omega, alpha <= 5`.
- I checked the corresponding model file and it has a `K5`, so it does **not**
  settle the no-`K5` branch. It only shows that the weaker `(6,6)` edge-count
  shortcut fails.

So any external theorem has to use the extra `K5`-free hypothesis, not just
`omega, alpha <= 5`.

## Results that genuinely constrain the branch

### 1. Kang-Pikhurko exact near-Turan theorem gives the correct lower edge floor

Source:

- M. Kang, O. Pikhurko, *Maximum `K_{r+1}`-free graphs which are not
  `r`-partite* (2005):
  <https://matstud.org.ua/texts/2005/24_1/24_1_012_020.html>
  and PDF
  <https://matstud.org.ua/texts/2005/24_1/24_1_012_020.pdf>

Applicability:

- `H` is `K6`-free and `alpha(H) <= 4`.
- Any 5-partite graph on 26 vertices has an independent part of size at least
  `ceil(26/5)=6`, so `H` cannot be 5-partite.
- Kang-Pikhurko determine the maximum size of a `K6`-free non-5-partite graph.
  For `n=26`, their theorem gives
  `e(H) <= t_5(26) - floor(26/5) + 1 = 270 - 5 + 1 = 266`.

Why this is slightly stronger here than the raw theorem:

- Their extremal `266`-edge examples are explicitly described. In the `n=26`,
  `r=5` case, those extremals retain a 25-vertex 5-partite Turan core, hence
  they visibly contain an independent set of size 5.
- Therefore `alpha(H) <= 4` rules out equality `e(H)=266`.

Conclusion:

- `e(H) <= 265`, hence `e(G) = 325 - e(H) >= 60`.
- This is the clean external justification for the local `60..65` minimum-colour
  window.
- It does **not** kill the branch. It only proves that `59` is impossible and
  that `60` is the first edge count worth checking.

Verdict: **sharp lower-bound input, but not a closure theorem.**

### 2. Exact stability around `T_5(26)` is the strongest usable structure theorem

Source:

- J. Balogh, F. C. Clemen, M. Lavrov, B. Lidicky, F. Pfender,
  *Making `K_{r+1}`-Free Graphs `r`-partite* (2021),
  <https://doi.org/10.1017/S0963548320000590>
  and PDF
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4B3AD0723DC446B87610E28F70A376D8/S0963548320000590a.pdf/making_kr1free_graphs_rpartite.pdf>

Why this matters:

- The paper restates the exact Furedi partition lemma for
  `K_{r+1}`-free graphs with `e = ex(n,K_{r+1}) - t`.
- Here `ex(26,K6) = t_5(26) = 270`, and `e(H) in {260,...,265}`, so
  `t = 270 - e(H) in {5,...,10}`.

Concrete consequence for our branch:

- There is a 5-partition `V(H)=V1 U ... U V5` such that
  - the total number of edges inside the five parts is at most `t <= 10`;
  - the total number of missing cross-edges is at most `2t <= 20`.

Interpretation:

- Every candidate `H` is an extremely small perturbation of `T_5(26)`.
- Equivalently, every candidate `G` is the complement of a graph that is
  almost complete 5-partite.

Usefulness:

- This is not a contradiction by itself.
- It is, however, an excellent template for SAT cubing or hand casework:
  partition sizes, internal defects, and missing cross-edge locations are all
  very tightly bounded.

Verdict: **best structural theorem I found for sharpening the branch.**

### 3. Andrasfai-Erdos-Sos gives a clean conditional kill at complement minimum degree 21

Convenient source with statement:

- W. Goddard, J. Lyle, *Dense Graphs with Small Clique Number* (2011),
  PDF <https://people.computing.clemson.edu/~goddard/papers/denseNoClique.pdf>

Relevant statement:

- For `K_{r+1}`-free graphs, if
  `delta > ((3r-4)/(3r-1)) n`, then the graph is `r`-partite.
- For `K6`-free graphs (`r=5`), this threshold is
  `delta(H) > (11/14) * 26 = 20.428...`, i.e. `delta(H) >= 21`.

Applicability:

- If one could prove `delta(H) >= 21`, then `H` would be 5-partite.
- But a 5-partite graph on 26 vertices has an independent set of size at least
  6, contradicting `alpha(H) <= 4`.

Translated back to `G`:

- `delta(H) >= 21` is equivalent to `Delta(G) <= 4`.

Conclusion:

- Any surviving branch candidate must violate that degree condition.
- Since `e(G) >= 60`, this is not surprising, but it is still a useful
  one-line reduction: the no-`K5` branch cannot be handled by proving only
  `Delta(G) <= 4`.

Verdict: **clean sufficient contradiction, but likely one degree too strong.**

### 4. Lyle 2026 improves the degree-kill threshold from 21 to 20

Source:

- Jeremy Lyle, *Independent sets in `K6`-free graphs with large degree*,
  Discrete Mathematics 349 (2026), DOI
  <https://doi.org/10.1016/j.disc.2025.114941>

Relevant theorem:

- Any `K6`-free graph `H` on `n` vertices with
  `delta(H) > (19/25) n` has an independent set of size at least `n/5`.

For `n=26`:

- `(19/25) * 26 = 19.76`, so `delta(H) >= 20` already implies
  `alpha(H) >= ceil(26/5) = 6`.

Applicability:

- Our branch has `alpha(H) <= 4`, so every candidate must satisfy
  `delta(H) <= 19`.
- Equivalently, every candidate `G` must have a vertex of degree at least 6.

Immediate branch consequences:

- The `e=65` case cannot be 5-regular.
- More generally, any attempt to kill the branch by showing `Delta(G) <= 5`
  would already close it.

This is strictly stronger here than Andrasfai-Erdos-Sos:

- AES needs `delta(H) >= 21`;
- Lyle only needs `delta(H) >= 20`.

Verdict: **best single-shot theorem I found for degree-sequence pruning.**

## What I did not find

### 5. No public Ramsey database seems to settle the exact `(5,6;26,260..265)` slice

Sources:

- Brendan McKay Ramsey data page:
  <https://users.cecs.anu.edu.au/~bdm/data/ramsey.html>
- Radziszowski dynamic survey:
  <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
  and PDF
  <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>

What is available:

- McKay's page has exhaustive public data for small families such as
  `(3,6)` and `(4,5)`, plus largest-known examples for `(4,6)` and `(5,5)`.

What is not available there:

- I did not find a public catalogue of all Ramsey `(5,6,26)` graphs.
- I also did not find a public table of minimum or maximum edge counts for
  26-vertex `K5`-free graphs with `alpha <= 5`, or equivalently for
  26-vertex `K6`-free graphs with `alpha <= 4`.

So:

- there is no obvious off-the-shelf database to query for the exact
  `e in {260,...,265}` complement slice;
- the literature still treats the global `R(5,6)` problem as far above this
  order, so the Ramsey number itself does not constrain `n=26`.

Verdict: **I found no external database that closes the branch for us.**

## Bottom line

My current assessment is:

1. The best exact external theorem already explains why the minimum-colour
   branch starts at `e(G)=60`.
2. The best structural theorem says every complement candidate is a
   `t`-perturbation of `T_5(26)` with `t <= 10`.
3. The best current degree theorem says:
   - if `delta(H) >= 20`, the branch is dead;
   - equivalently, every surviving `G` must have a degree-6 vertex.
4. I did **not** find a published theorem or public database that outright
   proves the no-`K5` branch impossible.

## Best next use of the literature

If this branch is attacked further, the most promising external-theorem-guided
route is:

- work in the complement `H`;
- use the Furedi/Balogh-Clemen-Lavrov-Lidicky-Pfender partition to cube by an
  almost-5-partite template;
- try to prove `delta(H) >= 20` from the remaining local constraints, which
  would finish the branch immediately by Lyle 2026.

That is the sharpest theorem-driven closure route I found.
