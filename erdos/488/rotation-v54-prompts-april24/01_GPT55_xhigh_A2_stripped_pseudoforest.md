# Send To: GPT 5.5 xhigh

Attach:
- `unified-truth-v53-april17.md`

Use xhigh reasoning. This is not a brainstorming task; the goal is a genuine mathematical contribution.

## Context

We are attacking Erdős Problem 488. The authoritative current state is v53 at 87%. Earlier frameworks peaked higher and died, so do not rely on older optimism.

The current open combinatorial target is A2':

For connected top-window components `C ⊂ (q/2, q]` with `n ∈ [5q/2, 3q)`, prove any equivalent form:

1. `x_3 ≤ x_1 - τ_n`
2. `ε_n ≤ 1`
3. after triple-stripping, the pair-only graph `G_n(C°)` is a pseudoforest
4. `D_C(n) ≥ Σ_{a∈C}(c_n(a)-1)`

Preferred route: the stripped pair-only graph formulation.

## Dead-Approach Warnings

Do not use:

- v52's broken run-count equality. It is false.
- `D(m)/m ≤ W_T`; this is kill #111.
- forest assumption for the n-LCM graph.
- BadBlock descent.
- direct transport `t -> t-q`.
- template finiteness without new proof.

Mandatory regression counterexample for run-count claims:

`C={24,30,36,40,45}`, `q=47`, `n=135`, `x=180`. Any formula that predicts `ε_T(180)=0` is dead; the truth is `ε_T(180)=1`.

## Your Task

Attack A2' directly.

Try to prove:

> If `C ⊂ (q/2,q]`, `n ∈ [5q/2,3q)`, and `C` is an extremal connected component after triple-stripping, then the stripped pair-only graph `G_n(C°)` is a pseudoforest.

If that statement is false or too strong, find the sharpest corrected statement that still implies A2'.

## Required Work

1. Give at least two unconditional approaches.
2. Give at least two conditional approaches, with the exact missing lemma named.
3. Search for a counterexample to the stripped pseudoforest target. If you cannot compute, give an explicit finite search design.
4. Analyze the pair-only bicyclic leafless case. Is every such component forced into a theta/shared-neighbor motif, or can a no-shared-neighbor theta survive the top-window arithmetic?
5. Produce Lean-ready theorem statements for any result you think is real.

## Output Format

Start with:

```
ERRORS OR COUNTEREXAMPLES FOUND:
```

Then:

```
PROVED RESULTS:
```

Then:

```
CONDITIONAL RESULTS:
```

Then:

```
FAILED ROUTES AND WHY:
```

Then:

```
BEST OBJECTION TO MY PROPOSED ROUTE:
```

Then:

```
LEAN-READY STATEMENTS:
```

Then:

```
NEXT ACTIONS:
```

Do not give a new percentage unless you justify it against v53's 87% anchor.

