# Erdős Problem 509 — Bridge Lemma Status
# March 20, 2026

## BRIDGE LEMMA Σ cap(E_j) ≤ 1: FALSE

Huang (2025) constructs monic polynomials whose lemniscate has arbitrarily many
components, each with diameter ≈ 4. Since cap(K) ≥ diam(K)/4 for continua,
each component has cap ≈ 1. So Σ cap(E_j) ≈ N while cap(E(f)) = 1.

Logarithmic capacity is NOT subadditive (Pyrih).

## DEGREE-WEIGHTED cap(E_j) ≤ k_j/d: ALSO FALSE
Same counterexample. Components can have cap ≈ 1 while k_j/d ≈ 1/n.

## WHAT IS TRUE: Walsh lemniscatic domain exponents
Schiefermayr-Sète prove: the Walsh exponents are EXACTLY m_j = k_j/d.
This controls HARMONIC MEASURE, not capacity.

## THE CORRECT BRIDGE (from factorization):
For f = f₁·f₂ with deg(f₁) = k:
- If min_{E₁} |f₂| ≥ M, then E₁ ⊆ {|f₁| ≤ 1/M}
- Therefore cap(E₁) ≤ M^{-1/k}
- The ENTIRE problem reduces to: bound min_{E_j} |f_{other}| from below

## THE REAL OBSTRUCTION:
In "barely disconnected" configurations (near pinch-off), |f₂| stays close
to 1 on E₁, giving M ≈ 1 and no gain. This is the hard case.

In well-separated clusters, M >> 1 and the argument is powerful.

## NEXT MOVE:
Use harmonic measure / Walsh exponents (m_j = k_j/d) instead of capacity.
The natural additive invariant is harmonic measure mass, not capacity.

Need: a covering theorem that uses harmonic measure weights directly.
Something like: τ(f) ≤ Σ_j g(m_j) where g is subadditive with Σ g(k_j/d) ≤ 2.
