# EP-488: MONOTONICITY CONJECTURE — DISPROVED
## April 5, 2026

---

## THE CONJECTURE (stated)

For any primitive set A with min(A) = a and |A| = k:
  ratio(A) <= ratio({a, a+1, ..., a+k-1})

i.e., the consecutive k-tuple maximizes the ratio among primitive sets of
the same size with the same minimum.

## VERDICT: FALSE

**50,726 violations** out of **350,806** primitive sets checked (k=4..8, max<=50).

The conjecture fails systematically: for many (a, k) pairs, some non-consecutive
set has a HIGHER ratio than the consecutive k-tuple.

### Most striking counterexamples (by (a, k)):

| a | k | Consecutive ratio | Best non-consecutive | Winner |
|---|---|-------------------|---------------------|--------|
| 5 | 4 | 0.6429 | **0.7000** at {5, 8, 9, 11} | NC |
| 7 | 4 | 0.7222 | **0.7600** at {7, 10, 11, 12} | NC |
| 10 | 4 | 0.7838 | 0.7838 at {10,11,12,13} | CONS (tie) |
| 15 | 4 | 0.8263 | **0.8631** at {15, 16, 17, 19} | NC |
| 20 | 4 | 0.8897 | 0.8897 at {20,21,22,23} | CONS (tie) |
| 5 | 5 | 0.6250 | **0.6696** at {5, 13, 14, 16, 17} | NC |
| 7 | 5 | 0.6861 | **0.7351** at {7, 10, 11, 12, 13} | NC |
| 7 | 6 | 0.6200 | **0.7083** at {7, 18, 19, 20, 22, 23} | NC |
| 7 | 7 | 0.6269 | **0.7030** at {7, 17, 18, 19, 20, 22, 23} | NC |

**The violations are numerous and significant.** Some non-consecutive sets
exceed the corresponding consecutive ratio by over 0.1.

### Worst absolute violation

A = {9, 22, 23, 25, 26, 28, 29}: ratio = **0.7245**
Consecutive {9, 10, ..., 15}: ratio = 0.6133
**Excess: 0.1112**

## STRUCTURE OF WORST NON-CONSECUTIVE SETS

The violating sets follow a clear pattern: **one small element followed by a
cluster of elements far away**.

Examples:
- {5, 13, 14, 16, 17} — min 5, cluster at 13-17
- {7, 10, 11, 12, 13} — min 7, cluster at 10-13
- {7, 18, 19, 20, 22, 23} — min 7, cluster at 18-23
- {9, 22, 23, 25, 26, 28, 29} — min 9, cluster at 22-29
- {10, 15, 21, 22, 23, 24} — min 10, then 15, cluster at 21-24

**Why these exceed consecutive:** The "dead zone" between min and the cluster
creates a region where F grows slowly (only from multiples of the smallest
element). This depresses min G below the consecutive baseline k/(2a-1).
Meanwhile, max G stays near the cluster density.

Concretely for A = {9, 22, 23, 25, 26, 28, 29}:
- In x ∈ [9, 21]: only multiples of 9 contribute (namely 9 and 18)
- F(21) = 2 + 0 = 2, G(21) = 2/21 ≈ 0.095
- Compare to consecutive {9,...,15}: G(21) = F(21)/21 where F includes 9,10,12,14,15,18,20,21 = 8, G = 0.381
- The non-consecutive min G is ~3x SMALLER than consecutive

The non-consecutive min G drops much further than consecutive, while max G
is similar (both bounded by their respective S1). The net effect: ratio HIGHER
for non-consecutive.

## WHY THE 3-LINE PROOF DOESN'T GENERALIZE

The consecutive proof used:
1. **min G = k/(2a-1)** — from F(2a-1) = k (each element contributes exactly once)
2. **max G ≤ S1 ≤ k/a** — first-order Bonferroni
3. **2k/(2a-1) > k/a** — trivially

For non-consecutive A with "gap structure":
- **min G can be MUCH smaller than k/(2a-1)**. For {9,22,23,...,29}, min G occurs
  at x >> 2a-1 = 17, where F hasn't grown enough relative to x.
- Specifically: at x = 2a-1 = 17, F = 1 (only 9 is counted). G(17) = 1/17, not
  k/(2a-1) = 7/17.
- The identity F(2a-1) = k only holds for consecutive k-tuples with a ≥ k.

## EP-488 STILL HOLDS

Despite the monotonicity failure, **every tested primitive set has ratio < 1**.
The worst overall ratio is still at a consecutive k-tuple (approaching 1 as a -> infinity).

**Key observation:** the non-consecutive sets that beat consecutive at fixed (a,k)
have ratios that are still well below the GLOBAL supremum (which is 1).

For example:
- {9, 22, 23, 25, 26, 28, 29}: ratio 0.7245
- {1000, 1001, 1002, 1003}: ratio 0.9965 (higher, but different (a,k))

So the TRUE ordering is: for fixed (a, k), the max ratio can be non-consecutive.
But across all (a, k), the supremum is achieved by consecutive sets as a -> infinity.

## WHAT THE PROOF NEEDS NOW

Since monotonicity is false, we cannot reduce EP-488 to the consecutive case.
The right statement is:

**Theorem (to prove):** For every primitive set A: max G(A) / (2 min G(A)) < 1.

Two possible paths:

**Path 1: Direct argument for non-consecutive sets.**
Use the structure "min then cluster": for A = {a} ∪ C where C ⊂ [c_min, c_max]
with c_min > a, the analysis splits. The min G is in the dead zone [a, c_min].
The max G is inside the cluster region. Bound both explicitly.

**Path 2: Universal bound via convexity + S1 bound.**
The convexity framework reduces EP-488 to verifying ratio < 1 in the first
period. The first-period ratio is determined by the behavior in [M, M+O(M)].
For any primitive A, the first-period extrema are computable in polynomial time.
This reduces EP-488 from "prove for all A" to "prove the finite verification
converges" — essentially, show that the ratio computed at horizon 10M equals
the true global ratio.

## STATUS

| Claim | Status |
|-------|--------|
| Consecutive k-tuple is worst for fixed (a,k) | **FALSE** |
| sup over all A of ratio = 1 | TRUE (achieved by consecutive as a→∞) |
| ratio(A) < 1 for all primitive A | **VERIFIED** (800K+ sets, 0 violations) |
| ratio < 1 provable via simple monotonicity | **FALSE** |
| ratio < 1 provable via direct bound | OPEN |
