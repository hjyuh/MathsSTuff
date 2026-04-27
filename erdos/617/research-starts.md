# EP617 Research Starts

Date: 2026-04-26

## Statement and Status

For every integer `r >= 3`, every `r`-edge-coloring of `K_{r^2+1}` should contain `r+1`
vertices whose induced `K_{r+1}` misses at least one color. Equivalently, there is no
`r`-coloring of `K_{r^2+1}` in which every `K_{r+1}` is polychromatic.

Status: open/falsifiable. The official ErdosProblems page was last edited 2026-04-01,
lists no claimed partial solutions in comments, and marks the statement formalised in
Lean. The only visible forum comment is a typo correction from 2026-03-11.

First open case: `r = 5`, i.e. rule out a 5-coloring of the 325 edges of `K_26` such
that every 6-set sees all 5 colors.

## Known Results and Partials

- Erdos-Gyarfas (1999) proved the conjecture for `r = 3` and `r = 4`, observed it is
  false for `r = 2`, and gave affine-plane constructions on `K_{r^2}` for infinitely
  many `r` showing the `+1` in `r^2+1` is sharp.
- The same paper proves the relevant balanced-coloring upper construction:
  balanced `r`-colorings of `K_{r^2+r+1}` exist when a projective plane of order
  `r+1` exists. Thus EP617 would identify the exact threshold `r^2+r+1` in those
  prime-power cases.
- For any hypothetical `r=5` counterexample, each color class on 26 vertices must have
  no clique of size 6 and no independent set of size 6. Local notes record necessary
  edge bounds `56 <= e(G_c) <= 101`.
- Local SAT confirms:
  - `r=2` is SAT, matching the known exception.
  - `r=3` is UNSAT.
  - `r=5` full search is still unknown under current budgets.
  - All 15 one-vertex extensions of the affine `F_5^2` slope construction are UNSAT.
  - Cyclic distance colorings of `K_26`, cyclic `K_25` core plus arbitrary star, and
    `F_5^2` Cayley core plus arbitrary star are UNSAT.
- A tempting edge-count shortcut fails: local SAT found a 65-edge graph on 26 vertices
  with both clique number and independence number at most 5, so one cannot simply prove
  that every `(6,6)` Ramsey graph on 26 vertices has at least 66 edges.

## Latest Literature and Comments

- The original source is still the main source: Erdos-Gyarfas, "Split and balanced
  colorings of complete graphs", Discrete Math. 200 (1999), 79-86.
- Gyarfas's later "Problems and memories" notes/slides repeat the balanced-coloring
  conjecture as open and restate the `r^2+r+1` construction when `r+1` is a prime
  power.
- Related later work on split colorings, e.g. Furedi-Ramamurthi (2002) and
  Gyarfas-Kezdy-Lehel (2002), develops the split-coloring side but does not appear to
  settle this balanced clique threshold.
- Modern polychromatic-coloring papers give useful language: EP617 asks for an
  edge-coloring of `K_{r^2+1}` that is polychromatic on every `K_{r+1}`. Recent
  polychromatic work mainly treats spanning families such as matchings, 2-factors,
  cycles, Hamilton cycles, or hypercube subgraphs, not this diagonal clique-size case.
- I found no newer claimed proof, counterexample, or serious forum update beyond the
  official typo comment.

## Natural First Attack Routes

1. Finish or shrink the finite `r=5` SAT case. Add certified-safe symmetry breaking,
   cardinality/density cuts, and cube-and-conquer; aim for either a model or a DRAT/LRAT
   UNSAT certificate.
2. Reframe `r=5` as a partition problem into five 26-vertex `(6,6)` Ramsey graphs.
   Enumerate or sample candidate color-class graphs, then test whether five can partition
   `E(K_26)` while satisfying every 6-set/color coverage condition.
3. Exploit stability around the affine `K_25` construction. Exact affine-core extensions
   are ruled out; next try bounded perturbations of the affine core plus an arbitrary new
   star, looking for either a near-miss family or a structural no-extension lemma.
4. Generalize the `r=3,4` minority-color/Turan/Brooks arguments. For `r=5`, pure
   one-color edge bounds are too weak, so the target should be a coupled statement across
   the five color classes or across many 6-sets.
5. Use the hypergraph viewpoint: color the 325 vertices of the edge-hypergraph whose
   hyperedges are the 15-edge sets from each `K_6`; every hyperedge must contain all
   five colors. This suggests SAT, exact cover, container-style, or local-lemma diagnostics.

## Computational and Formalization Hooks

Existing local scripts/results are already useful:

- `scripts/sat_cnf_pipeline.py`: compact full `r=5` encoding with 1625 edge-color
  variables, 1,151,150 coverage clauses, and 3,575 exactly-one clauses.
- `scripts/sat_balanced.py`: older/full encoding with cardinality machinery; local
  `balanced_r5_sat_summary.json` reports unknown.
- `scripts/cube_conquer.py`: cube generation over edge prefixes or star patterns.
- `scripts/cyclic_cayley_search.py`: structured cyclic/Cayley families, all currently
  UNSAT for the tested `r=5` families.
- `scripts/ramsey_color_class_sat.py` and `scripts/pack_ramsey_template.py`: useful for
  color-class Ramsey and edge-partition attacks.
- `scripts/walksat_balanced.py`: local search; current best `r=5` near miss has 1,268
  missing-color violations over 1,258 bad 6-sets.
- FormalConjectures has a Lean statement with solved variants recorded for `r=3`,
  `r=4`, and the `K_{r^2}` counterexample family. A certified SAT/UNSAT workflow for
  `r=5` would be naturally formalizable if proof certificates are produced.

## Risks and Unknowns

- `r=5` may be SAT via a non-affine, non-cyclic construction; current structured
  exclusions do not strongly constrain the full search space.
- An UNSAT proof for `r=5` would still be only the first open finite case, not a proof
  for all `r`.
- Solver symmetry breaking is dangerous unless independently checked; any aggressive
  canonical assumptions need proof or certificate support.
- The literature trail is sparse and terminology varies between "balanced",
  "split", and "polychromatic", so an obscure partial result could be missed.
- The local computational results are reproducible artifacts, but not yet independently
  certified proof objects.

## Tractability Score

Score: 4/10 for a serious attempt over the next few days.

Reason: meaningful progress on `r=5` is plausible because the exact finite instance is
small enough for SAT, local search, and structured enumeration. Actual closure of `r=5`
in a few days is uncertain, and a full all-`r` solution looks substantially harder.

## Three Concrete Next Steps

1. Build a hardened `r=5` SAT run: compact CNF, safe color/vertex symmetry breaking,
   edge-count bounds, cube-and-conquer, and certificate-capable solvers such as Kissat or
   CaDiCaL.
2. Start the Ramsey-graph partition route: generate canonical 26-vertex graphs with
   `omega, alpha <= 5` in the plausible edge range, then encode whether five such graphs
   can edge-partition `K_26`.
3. Run affine-perturbation local search: seed from each `F_5^2` slope-merge coloring,
   allow bounded recolorings plus a free 26th-star, and record minimum violation profiles
   or UNSAT cores that might suggest a human lemma.

## Sources

- Official EP617 page: https://www.erdosproblems.com/617
- EP617 LaTeX source: https://www.erdosproblems.com/latex/617
- EP617 forum thread: https://www.erdosproblems.com/forum/thread/617
- Erdos-Gyarfas original paper PDF: https://www.renyi.hu/~gyarfas/Cikkek/92_splitandbalanced.pdf
- ScienceDirect metadata/DOI for Erdos-Gyarfas 1999:
  https://www.sciencedirect.com/science/article/pii/S0012365X98003239
- Gyarfas, "Problems and memories" notes:
  https://www.renyi.hu/~gyarfas/Cikkek/ar2erdos.pdf
- Gyarfas 2013 slides:
  https://www.renyi.hu/~gyarfas/Presentations/erdos100talk.pdf
- FormalConjectures Lean statement:
  https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/617.lean
- Furedi-Ramamurthi, "On splittable colorings of graphs and hypergraphs":
  https://dblp.org/rec/journals/jgt/FurediR02
- Goldwasser-Hansen 2022 polychromatic complete-graph paper:
  https://www.sciencedirect.com/science/article/abs/pii/S0012365X22001029
- Axenovich et al. polychromatic complete-graph paper:
  https://arxiv.org/abs/1612.03298
