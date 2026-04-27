# EP617 Phase 1: No-K5 Minimum-Colour Branch

Updated 2026-04-26.

## Target Lemma

There is no graph `G` on 26 vertices satisfying all of:

- `60 <= e(G) <= 65`;
- every 6-set spans at least 1 edge of `G`;
- every 6-set spans at most 11 edges of `G`;
- `omega(G) <= 4`.

If this lemma is proved, then every valid `K_26` colouring has a minimum-colour
`K_5`, so the next global branch may anchor that `K_5`.

## Agent Partition

- A: strongest direct PySAT encoding.
- B: graph-theoretic safe cuts.
- C: local/random search for a counterexample skeleton.
- D: symmetry breaking/canonical starters.
- E: degree-sequence feasibility.
- F: non-PySAT solver alternatives.
- G: exact-edge and neighbourhood cubes.
- H: external theorem/database audit.
- I: independent model/verifier tooling.
- J: proof-log/certificate feasibility.
- K: complement-side formulation.
- L: seed repair from existing Ramsey candidates.

## Current Local Status

- Existing lazy one-colour script: `scripts/one_color_strengthened.py`.
- Endpoint strengthened runs:
  - `e=60`: `unknown`, 80 lazy rounds.
  - `e=65`: `unknown`, 80 lazy rounds.
- No valid no-K5 skeleton has been found.
- No UNSAT certificate has been produced.

## Returned Agent Signals

### Agent B: local cuts

Agent B found safe local consequences of the 6-set bounds:

- every triangle has at most 2 common neighbours;
- an independent 4-set has a common nonneighbourhood that is a clique, hence size at most 4;
- any 4-set with at least 4 internal edges has at most 1 common neighbour;
- for a `K_4`, outside pairs satisfy `deg_Q(x)+deg_Q(y)+1_xy <= 5`;
- for every nonedge `uv`, the common nonneighbourhood has size at most 20.

Most of these are compressed forms of the lower/upper 6-set constraints already
present in the lazy SAT loop. They are useful as diagnostics and potential eager
propagation, but they are not yet a new closing idea.

### Agent D: symmetry

Agent D implemented mixed-edge/nonedge anchoring and max-degree-star branches.
The mixed anchor did not improve triage. The max-degree-star starter reduced
decisions in low-degree branches but did not certify SAT/UNSAT at tested budgets.

### Agent H: external structure

Agent H found the most important strategic pivot:

- In the complement `H = complement(G)`, candidates have `260..265` edges,
  are `K_6`-free, and have `alpha(H) <= 4`.
- By near-Turan stability, such an `H` is a tiny perturbation of `T_5(26)`.
  More concretely, with `t = 270 - e(H) <= 10`, there is a 5-partition with
  at most `t` internal edges and at most `2t` missing cross-edges.
- Lyle's 2026 theorem implies any surviving complement candidate must have
  `delta(H) <= 19`, equivalently `G` must have a vertex of degree at least 6.

This suggests the next serious implementation should be complement-template
cubing around near-`T_5(26)`, not generic graph SAT.

## Integration Rules

1. A found skeleton must be verified independently before it is trusted.
2. A proposed cut must include a proof sketch before entering a shared solver.
3. UNSAT results are useful only if the assumptions/cube coverage are logged.
4. Scripts should write JSON result rows immediately, not only at completion.
