# EP-488: Gemini Brainstorm — Lateral Connections
## April 5, 2026 — Temperature ~0.8, brainstorming mode

## TOP 3 CONNECTIONS (potentially actionable)

### 1. Pinwheel Scheduling (Chan-Chin 1992)
- k tasks, task i must execute every n_i days, one task per day
- Valid schedule exists when Σ 1/n_i ≤ 1/2
- Factor 1/2 = factor 2 barrier for periodic independent refreshes
- EP-488 IS this problem in density language
- SEARCH: Can Chan-Chin's proof technique transfer directly?
- Reference: Chan & Chin, "Schedulers for larger classes of pinwheel
  instances," Algorithmica 9 (1993), 425-462

### 2. LP Integrality Gap / Hypergraph Cover
- Treat integers as vertices, multiples of a_i as hyperedges
- Primitive = no hyperedge contains another (antichain of hyperedges)
- F(x)/x = fractional cover density
- Factor 2 = classic primal-dual integrality gap (like vertex cover)
- FORMALIZE: Write the density as LP, exhibit dual, show gap ≤ 2
- This would give a one-page proof if the formulation is correct

### 3. Sum-Free Sets / Multiplicative Freiman
- Primitive sets are multiplicatively sum-free (A ∩ A·Z_{>1} = ∅)
- Additive sum-free density barrier = 1/2 (equivalently factor 2)
- Extremal: "top half" intervals, same as EP-488 extremal (compact)
- The factor 2 in EP-488 may be the multiplicative analogue
- SEARCH: Is there a multiplicative Cameron theorem?

## OTHER CONNECTIONS (less directly applicable)

### 4. Lonely Runner Conjecture
- k runners at speeds v_i, non-resonance prevents synchronization
- Primitivity forces non-resonance (speeds can't be multiples)
- Conceptually right but technically different problem

### 5. Kruskal-Katona / Clements-Lindström
- Bounds minimum shadow size for antichains
- Extremal antichains are "lex-first" — related to adjacent pairs?
- Turán-type question for divisibility posets

### 6. Rogers' Theorem
- Density of unsieved set minimized at 0 mod n_i (multiples case)
- Already known from EP-488 forum (Alexeev cited it)
- Gives density existence, not oscillation bounds directly

### 7. Beatty / 3-Distance Theorem
- Gaps between union of APs take bounded number of distinct values
- Structural rigidity prevents anomalous gaps
- Conceptually aligned but not directly applicable

## PRIORITY FOR FOLLOW-UP
1. Pinwheel scheduling literature (closest structural match)
2. LP formulation of density oscillation (most radical, highest payoff)
3. Multiplicative sum-free barrier (deepest structural explanation)
