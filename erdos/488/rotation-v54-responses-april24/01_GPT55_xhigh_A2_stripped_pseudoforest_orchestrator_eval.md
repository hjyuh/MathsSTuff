# GPT 5.5 xhigh A2 Stripped Pseudoforest — Orchestrator Evaluation

Received: April 24, 2026

Prompt intended: `01_GPT55_xhigh_A2_stripped_pseudoforest.md`

## Orchestrator Verdict

Status: **major useful correction; no closure, but A2' must be restated with a strong true-extremizer predicate.**

This response confirms that the unqualified stripped-pseudoforest target is false. This aligns with the Claude/Kimi concerns and gives the canonical theta13 as the clean regression case.

## Accepted Findings

### 1. Unqualified A2'/pseudoforest target is false

Canonical theta:

```text
q = 451
n = 1350
C = {240,243,256,270,288,300,320,324,360,384,405,432,450}
```

Claimed properties:

- pair-only, so `tau_n = 0`;
- connected;
- `|V| = 13`;
- `|E| = 14`;
- cyclomatic number `c = 2`;
- `epsilon = 2`;
- `D_C(1350) = 37`;
- `sum(c_n(a)-1) = 38`;
- thus coverage-mass A2' fails for this arbitrary top-window component.

This means A2' is not a theorem for arbitrary connected top-window components. It can only be a theorem for a strong exact EP-extremizer predicate, or it must be replaced by a cycle-absorption theorem.

### 2. True-extremizer predicate is now critical

Accepted as a core lesson:

> Any proof that treats "extremizer" as merely an event-point local maximizer of `D_C(m)/m` is too weak.

The canonical theta may be locally maximizing but below the EP-488 threshold. Therefore the predicate must encode true relevance to a potential EP violation, not just internal maximization.

### 3. Bad-core reduction is plausible and useful

In pair-only graphs:

- deleting leaves preserves cyclomatic number;
- a minimal pair-only bicyclic obstruction has a leafless 2-core;
- if `c=2`, degree accounting gives exactly two degree-3 vertices and the rest degree 2 under max-degree-3/top-window hypotheses.

This should be turned into precise Lean statements after graph definitions are pinned.

### 4. Edge alphabet lemma is a strong formalization candidate

The proposed lemma:

```text
if q/2 < a < b < q, n < 3q, lcm(a,b) <= n,
then the reduced edge ratio is in {2:3, 3:4, 3:5, 4:5}.
```

This is small, useful, and likely suitable for Gauss/Aristotle once the exact divisibility statement is stated correctly.

### 5. No-shared-neighbor search supports, but does not prove, a classification

xhigh reports:

- induced leafless bicyclic theta cores searched for `q <= 700`;
- found 29 theta cores;
- all were shared-neighbor motif `d*{8,9,12}`;
- zero no-shared-neighbor theta cores.

This is evidence only until code/certificates are provided.

## Current A2' State After xhigh

Unsafe:

```text
For arbitrary connected top-window C, epsilon <= 1.
For arbitrary connected top-window C, stripped graph is a pseudoforest.
```

Safe target:

```text
For true EP-extremizers, D_C(n) >= sum(c_n(a)-1).
```

or:

```text
For true EP-extremizers, epsilon <= 1.
```

But `TrueExtremizer` must be defined precisely and must exclude theta13.

## Missing Lemmas Identified

1. `no_shared_neighbor_theta_impossible_top_window`
2. `shared_neighbor_theta_motif_not_true_extremizer`
3. `leaf_pruning_preserves_true_extremality`
4. `TrueExtremizer` definition/regression: theta13 must not satisfy it

## Relation To Kimi Obstruction

The xhigh result and Kimi obstruction point in the same direction:

- stripped pseudoforest is not an unconditional structural fact;
- low-density/non-extremal bad cores exist;
- the final proof must either:
  - use a strong true-extremizer exclusion theorem, or
  - use cycle absorption and tolerate these cores.

## Formalization Priority Update

Good immediate targets:

1. `upperStrip_pair_edge_ratio_alphabet`
2. `theta13_pairOnly_bicyclic_counterexample`
3. exact `TrueExtremizer` predicate and proof that theta13 is not one
4. bad-core leaf-pruning graph lemmas

Defer:

- `extremizer_stripped_pseudoforest` until `TrueExtremizer` is defined.
- broad triple-stripping equivalences until the Kimi obstruction is resolved.

## Ledger Update

No theorem closed. But one false overstatement is now explicitly killed:

> A2' / stripped pseudoforest for arbitrary connected top-window components.

New regression case:

```json
{
  "name": "theta13_paironly_bicyclic_A2_failure",
  "q": 451,
  "n": 1350,
  "C": [240,243,256,270,288,300,320,324,360,384,405,432,450],
  "tau": 0,
  "vertices": 13,
  "edges": 14,
  "cyclomatic": 2,
  "D_C_n": 37,
  "sum_c_minus_1": 38
}
```

