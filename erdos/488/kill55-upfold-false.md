# EP-488: Kill #55 — Up-Fold R(A) ≤ R(C) is FALSE
## April 6, 2026

## THE KILL

R(A) ≤ R(C) where C = up_fold(A) ⊂ (M, 2M] is FALSE.

### Smallest counterexample:
A = {4,5,6,7,9}, M = 9
C = {10,12,14,18}
R(A) = 1.2765, R(C) = 1.2723
R(A) > R(C) by 0.0041

### Worst counterexample:
A = {6,8,15,17}, M = 17
C = {18,24,30,34}
R(A) = 1.4097, R(C) = 1.3056
R(A) > R(C) by 0.1042

### Statistics:
Exhaustive (M ≤ 20, k ≤ 5): 36/4673 violations (0.77%)
Random (M ≤ 50, k ≤ 8): 2/1000 violations (0.2%)

### Why it fails:
Up-fold simultaneously:
- Increases max(C) = 2M (reducing boundary oscillation)
- Changes overlap structure among progressions
- Can merge/deduplicate moduli (reducing coverage complexity)
These effects can DECREASE R, not increase it.

### 5.4's family passes:
A_N = {2p, 5p} for primes p ∈ [N, 1.1N] satisfies R(A) ≤ R(C).
So the direction IS correct for some families, just not universally.

## KILL COUNT: 55
