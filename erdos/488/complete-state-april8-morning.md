# EP-488: State After Kill #76 (Three Independent Confirmations)
## April 8, 2026

## THE KILL (confirmed by Codex B, 5.2, and 5.4)

Part 1 of the Closing Question is FALSE:
n-LCM connected components with bad layers, no literal {2,3}, CAN have gcd = 1.

Counterexamples:
- {8, 9, 12} (5.4, simplest, 3 elements)
- {10, 21, 35} (Codex B, 3 elements)
- {20, 63, 210} (5.2, 3 elements)
- {9, 12, 16, 40, 42} (5.2, 5 elements, two bad layers)
- {4, 6, 9, 33, 34} (5.2, coprime bad layers)
- {2p, 3q, pq} for coprime p,q (Codex B, infinite family)
- {2u, 3v, uv} for coprime u,v (5.4, infinite family)

Mechanism: "split-core" — bad hub a gets quotient 2 from one local
core g and quotient 3 from a different coprime local core h.
g and h share no prime → gcd(component) = 1.

## WHAT'S DEAD

- "Prove gcd(C) > 1 then reduce to lifted core" — DEAD
- "Prove gcd(bad layers) > 1" — DEAD (coprime bad layers exist)
- Any structural reduction requiring a global common divisor — DEAD

## WHAT'S ALIVE

The Lifted {2,3}-Core Safety theorem: STILL TRUE for sets that ARE dB.
It just doesn't apply to all components.

ALL scale-independent tools survive:
- First-layer theorem (S₁ > E_j each)
- Superadditivity + Component Reduction
- Degree-size bounds
- Window Lemma
- Surplus Dominance (zero violations)

## THE HONEST REMAINING GAP

The proof cannot close by structural reduction to lifted cores.
It must work DIRECTLY on general primitive sets — including gcd-1
components with split-core bad hubs.

The two viable closing routes:
1. SURPLUS DOMINANCE: Prove 2mH_A(n) ≥ nH_A(m) directly.
2. GLOBAL CHARGING: Window Lemma applied to general components.

Both are scale-independent and don't need gcd structure.

## PERCENTAGE: 85%

The proved theorems are worth ~50%. The tools are worth ~15%.
The specific family proofs are worth ~10%. The structural insights
(what CAN'T work) are worth ~10%. The gap is ~15%.

The gap: prove global charging or surplus dominance for arbitrary
primitive sets, including gcd-1 split-core components.
