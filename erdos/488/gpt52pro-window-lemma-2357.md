# EP-488: 5.2 Pro — Window Lemma for {2,3,5,7} Extremal Swarm
## April 7, 2026

## KEY RESULT: 2p-ancestors alone pay the {2,3,5,7}-swarm

Using ONLY 2p-ancestors in thin window [y, y^{1+ε}]:
- Union bound: L_{2p}(x) ≥ cx where c = 1 - C₇·log(1+ε) > 1/2
  (C₇ = 1 + 1/3 + 1/5 + 1/7 ≈ 1.676, ε = 0.2 → c ≈ 0.695)
- Each 2p contributes slack ≈ (c - 1/2)·mn/p > 0
- Window sum: Σ S_{2p} ≈ (c-1/2)·mn·log(1+ε) = O(M²) [CONSTANT]
- Bad excess: O(M²/log y) → 0

Ratio: GOOD/BAD ≈ (constant)·log y → ∞.

## WHY THIS IS THE STRONGEST VERSION

1. Uses ONLY 2p-ancestors (ignores 3p, 5p, 7p entirely)
2. Union bound on L_{2p} — no sieve theory, just counting
3. Handles {2,3,5,7} extremal case (17a excess) directly
4. Kill-resistant: no kernel comparison, no intermediate bounds
5. The "17× harder" is irrelevant — it only changes the constant c₁(α)
   while the ratio still wins by factor log y

## THE REMAINING GAP (stated precisely by 5.2)

"Extraction lemma: from the mere existence of many {2,3,5,7}-bad
children in a general primitive set, force the existence of a
sufficiently dense prime window of small ancestors."

This is the EXACT uniformity gap. In the swarm, ancestors are
constructed by design. In a general set, they exist by the
prime-cover mandate but might not form a clean window.

## KILL COUNT: 70
## PERCENTAGE: 86%
