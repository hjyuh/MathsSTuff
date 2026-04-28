# EP-488: Gemini Deep Dive Results — Three Breakthrough Connections
## April 5, 2026

## INSIGHT 1: y/⌊y⌋ < 2 IS THE ENTIRE PROBLEM

EP-488 for singletons A = {k}:
  G(m)/G(n) = (⌊m/k⌋/m) / (⌊n/k⌋/n) = (n/m) · (⌊m/k⌋/⌊n/k⌋)

The singleton bound is literally y/⌊y⌋ < 2 for y ≥ 1.
The general case is the MULTI-VARIABLE I-E generalization of this.

The factor 2 comes from the floor function, not from number theory.
The n ≥ max(A) condition is required because y = n/a_i < 1 gives ⌊y⌋ = 0.
Once every generator has "kicked in" (n ≥ max(A)), the floor gap is bounded.

## INSIGHT 2: KAWAMURA (2024) — FRACTIONAL FOLDING

Kawamura solved the Chan-Chin 5/6 conjecture for pinwheel scheduling at STOC 2024.
Proof technique: "fractional folding" — map arbitrary periods to a harmonic sequence
(divisibility chain) with distortion factor < 2.

DIRECTLY APPLICABLE: Map primitive set A (antichain) to a divisibility chain B
via folding. Oscillation of chain = 1 (no oscillation). Distortion of fold < 2.
Therefore oscillation of original ≤ 2 × 1 = 2.

THIS IS THE PROOF ARCHITECTURE. Must read Kawamura immediately.

Reference: Akitoshi Kawamura, STOC 2024. Search for exact title.

## INSIGHT 3: MULTIPLICATIVE KNESER INVERSE THEOREM

Proof by contradiction: assume F(m)/m ≥ 2F(n)/n.
This forces massive synchronized "deserts" in the integers.
A Kneser-type inverse theorem would force A into {M,...,2M-1} (top half).
But compact sets are already proved (Theorem 6). Contradiction.

This is the cleanest possible proof architecture:
1. Assume counterexample exists
2. Inverse theorem forces counterexample to be compact
3. But compact case is proved
4. Contradiction

## ALSO NOTED

- Aharoni-Zerbib fractional hypergraph vertex cover — factor 2 integrality gap
- "Bamboo garden trimming" — continuous pinwheel variant, same factor 2
- Holte (1992) — pinwheel density thresholds

## PRIORITY

1. READ KAWAMURA 2024 IMMEDIATELY — the folding operation may transfer directly
2. Formalize the Kneser inverse approach — "counterexample must be compact"
3. LP integrality gap formulation as backup

## STATUS: This might be the breakthrough session.
