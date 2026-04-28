# Send To: Kimi K2.6 Agent Swarm

Attach:
- `unified-truth-v53-april17.md`

Use Agent Swarm. This is a computation/certificate task, not a prose-only reasoning task.

## Context

EP-488 v53 leaves two hard targets:

- A2': combinatorial closure via stripped pair-only pseudoforest / `ε_n≤1`.
- A4: analytic closure for unicyclic hosts at finite event points.

We need exhaustive search and reusable certificates, not just examples.

## Swarm Tasks

### Task A: A2' Census

Enumerate top-window primitive components:

- `q` up to at least 500 if feasible; report exact bound reached.
- `C ⊂ (q/2,q]`, `|C|≥3`.
- `n ∈ [2q,3q)`, especially `[5q/2,3q)`.
- q-excluded n-LCM graph edges:
  `(a,b)` is an edge iff `lcm(a,b) ≤ n` and `q ∤ lcm(a,b)`.

For each connected component:

- vertices, edges;
- collision fibers `S_l`;
- `c=|E|-|V|+1`;
- `τ_n`;
- `ε_n=c-τ_n`;
- stripped graph `C°`;
- whether stripped graph is a pseudoforest;
- any pair-only bicyclic leafless component;
- any no-shared-neighbor theta.

### Task B: Extremizer Filter

For every apparent A2' obstruction, compute:

- `D_C(n)`;
- `Σ(c_n(a)-1)`;
- whether `D_C(n) ≥ Σ(c_n(a)-1)`;
- whether the component can be extremal under the v53 finite-window extremizer conditions.

### Task C: A4 Event-Point Margins

For connected unicyclic top-window hosts:

- compute event set `J_D`;
- compute `H_U#(n)`, `H_U#(m)`, and `c_m(L_cyc)`;
- verify or refute:
  `2 H_U#(n)/n - H_U#(m)/m ≥ c_m(L_cyc)/m`.

### Task D: Regression Suite

Hard-code these regression cases:

- theta family in v53;
- v52 run-count counterexample:
  `C={24,30,36,40,45}`, `q=47`, `n=135`, `x=180`;
- one-edge simplification counterexample from v52;
- kill #108 and kill #111 examples.

## Required Output

1. Source code or clear pseudocode sufficient for independent rerun.
2. Tables of distinct `(c,τ_n,ε_n)` triples with witnesses.
3. List of all obstructions found, or a statement that none were found up to the search bound.
4. Machine-checkable JSON/CSV schema for witnesses.
5. Exact worst-case A4 margin witness.
6. Any counterexample must be printed fully, not summarized.

## Output Format

```
SUMMARY:
```

```
SEARCH BOUNDS AND METHODS:
```

```
REGRESSION RESULTS:
```

```
A2' CENSUS RESULTS:
```

```
A4 EVENT-POINT RESULTS:
```

```
COUNTEREXAMPLES OR OBSTRUCTIONS:
```

```
FILES / CODE:
```

```
NEXT COMPUTATION:
```

No mathematical claim should be presented as proved unless it is either formally proved or follows from an explicitly described exhaustive finite search.

