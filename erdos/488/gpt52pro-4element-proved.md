# EP-488: 5.2 Pro — |A| ≤ 4 PROVED
## April 8, 2026

## THEOREM: EP-488 holds for all primitive sets with |A| ≤ 4.

Key new lemmas:
1. Witness-count bound: π(s_j) ≤ j-1 (frozen layer needs one witness per prime)
2. Signature rigidity: {2,3}-frozen layer with s=4 → t=7 only

Proof: Layers 1,2 safe. Two bad layers forced to (4,7,3) signature.
S₁ ≥ 4m > 6n-4m = E₃+E₄ since 8m > 6n. ∎

Verified computationally. Two independent proofs (5.2 + separate confirmation).

## CONSEQUENCE: Minimal counterexample has |A| ≥ 5.
