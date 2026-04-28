# EP-488: Collective Oscillation Budget Reformulation
## Source: GPT-5.2 Pro — April 5, 2026

## THE REFORMULATED INEQUALITY

Write each layer as T_j(x) = c_j + ε_j(x) where c_j = M·ρ_{Q_j}/a_j = r_j·ρ_{Q_j}.

Define excursions:
  u_j = sup_x (-ε_j(x))     (downward)
  v_j = sup_x (ε_j(x))      (upward)

Let U = Σ u_j, V = Σ v_j, C = Σ c_j.

## COLLECTIVE FACTOR-2 CRITERION (sufficient):

  V + 2U < C

⟹ sup H(x) < 2·inf H(x) on [M, 10M].

### Symmetric corollary: If |ε_j(x)| ≤ e_j for all j, then:

  3·Σ e_j < C   (equivalently, Σ e_j < C/3)

## WHY THE ASYMMETRY V + 2U

- Upward spikes (V) hurt the numerator once
- Downward dips (U) hurt the denominator TWICE (they lower inf H,
  and the factor-2 target compares against inf H)

## PRACTICAL BOUND ON u_j AND v_j

ε_j(x) = (M/x)(D_j(y_j(x)) - ρ_j·{x/a_j})

Upward: v_j ≤ sup_{y ∈ [r_j/10, r_j]} D_j^+(y)
  (floor term -ρ{x/a} only REDUCES upward spikes)

Downward: u_j ≤ sup_{y ∈ [r_j/10, r_j]} D_j^-(y) + ρ_j
  (floor term ADDS to the dip, contributing at most ρ_j)

## PURELY COLLECTIVE EXTREMA CONDITION

Define m_j = inf T_j(x), M_j = sup T_j(x) over [M, 10M].

Sufficient: Σ M_j < 2·Σ m_j

This allows individual ratios M_j/m_j to be huge, as long as layers
with huge ratios don't carry much weight.

## THREE STRATEGIES TO PROVE V + 2U < C

### A) Dominant Stable Mass
Split layers into Good (G) and Bad (B).
Show: V_G + 2U_G ≤ θ·C_G with θ < 1
And:  Σ_{B} M_j ≤ η·C_G with θ + η < 1

### B) Anti-Alignment / Low Correlation
Show: sup_x |Σ ε_j(x)| ≤ C/3
This is the "spikes don't line up" principle.
Could use large-sieve/orthogonality heuristics + trig polynomial bounds.

### C) Endpoint Control
The weight M/x is largest at x = M, so dips near x = M are most dangerous.
Strategy: prove uniform lower bound on H(x) for x ∈ [M, (1+δ)M],
and crude upper bound for H(x) on all of [M, 10M].

## STATUS: This is the reformulated bound that replaces Kill #46.
## PERCENTAGE: Still 89% — the reformulation is clean but unproved.
