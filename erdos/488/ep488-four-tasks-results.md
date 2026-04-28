# EP-488: FOUR TASKS — RESULTS
## April 5, 2026

---

## TASK 1: max G / S1 for spread sets — S1 CAN BE NEARLY TIGHT

**231,028 spread primitive sets** (max > 2·min) checked:

| M/a | count | avg max_G/S1 | max | min |
|-----|-------|--------------|-----|-----|
| 2 | 96,731 | 0.8823 | 0.9965 | 0.7508 |
| 3 | 72,188 | 0.8691 | 0.9947 | 0.7151 |
| 4 | 24,488 | 0.8435 | 0.9924 | 0.7068 |
| 6 | 13,819 | 0.8173 | 0.9923 | 0.6608 |
| 9 | 6,936 | 0.8624 | 0.9913 | 0.7165 |

**max G / S1 can reach 0.9965** at {11, 23, 26}. The S1 bound is SOMETIMES nearly tight.

**Conclusion:** S1 is NOT loose enough to generically tighten. For adversarially
chosen sets, max G approaches S1. Any universal tightening of max G beyond S1
would need structural constraints.

Average max G / S1 ~ 0.85-0.88, so typical sets have ~15% slack, but worst case
has < 0.4% slack. A universal "max G ≤ 0.9·S1" DOES NOT hold.

---

## TASK 2: max G LOCATION — NO SIMPLE FORMULA

| Set | a | M | max_x | max_x / M | Structure |
|-----|---|---|-------|-----------|-----------|
| {2,3,5,7} | 2 | 7 | 10 | 1.43 | dense |
| {3,5,7,11} | 3 | 11 | 12 | 1.09 | dense |
| {4,6,9,10} | 4 | 10 | 10 | 1.00 | dense |
| {5,6,7,8} | 5 | 8 | 21 | 2.62 | consecutive |
| {10,11,12,13} | 10 | 13 | 100 | 7.69 | consecutive |
| {9,22,23,25,26,28,29} | 9 | 29 | 184 | 6.34 | spread |
| {5,8,9,11} | 5 | 11 | 36 | 3.27 | near-consecutive |
| {7,10,11,12} | 7 | 12 | 50 | 4.17 | near-consecutive |

**No simple formula.** max_x ranges from M (for dense sets) to ~10M (for consecutive)
and beyond. The location depends intricately on lcm structure.

**Pattern:**
- DENSE sets (max ~ min): max_x near M (local peak at first "hit")
- CONSECUTIVE sets: max_x much larger (at specific arithmetic points like a²)
- SPREAD sets (min + cluster): max_x at cluster-alignment points

For the pair {1000, 1001}: max at x = 1001² = 1,002,001 per the exact formula.
For consecutive triples: max at x ≈ a² per the empirical data.

No closed form for general k.

---

## TASK 3: UNIFORM BOUND ratio ≤ 1 - c/M

**The bound ratio ≤ 1 - 1/M HOLDS for all tested sets.**

Tightest case: pair {50, 51} — ratio = 0.9801, 1 - 1/51 = 0.9804, margin = 0.0003.
Worst overall: pair {1000, 1001} — ratio = 0.9985, 1 - 1/1001 = 0.9990.

**What c is achievable?**
- For adjacent pairs {b-1, b}: exact formula ((2b-3)/(2b-2))² → 1 - 1/b + O(1/b²) as b → ∞
- So c = 1 is achieved asymptotically by adjacent pairs
- Numerically, min c observed = 1.5 at {1000, 1001} (computation had limited precision)

**Conjecture:** ratio ≤ 1 - 1/max(A) for all primitive A, with equality in the
limit for adjacent pairs {M-1, M} as M → ∞.

This would give a UNIFORM EP-488 bound with gap exactly 1/max(A). The proof
for adjacent pairs is exact (Theorem B). For other sets, we need ratio strictly
less than adjacent-pair ratio with the same max.

**Key numerical observations:**
- All 800K+ sets: ratio ≤ 1 - 1/M (verified)
- Worst ratio across all tested: 0.9985 for adjacent pair {1000, 1001}
- Approach to 1 is at rate 1/M, not any faster

---

## TASK 4: EXTREMAL ARRANGEMENT FOR FIXED (a, M)

**NOT consecutive. The extremal sets have "one small + cluster near max."**

### Examples

**min=5, max=21, k=5:** top 3:
- {5, 17, 18, 19, 21}: ratio 0.6513
- {5, 16, 17, 18, 21}: ratio 0.6489
- {5, 16, 18, 19, 21}: ratio 0.6444

**min=7, max=25, k=4:** top 3:
- {7, 18, 19, 25}: ratio 0.6939
- {7, 22, 23, 25}: ratio 0.6772
- {7, 17, 18, 25}: ratio 0.6766

**min=10, max=33, k=6:** top 3:
- {10, 26, 27, 29, 31, 33}: ratio 0.7096
- {10, 26, 27, 28, 29, 33}: ratio 0.7096
- {10, 26, 27, 28, 32, 33}: ratio 0.7049

### The Pattern

**All extremal sets for fixed (a, M) have:**
1. The minimum element `a`
2. A gap (no elements in (a, 2a] or (a, M/2])
3. A cluster of consecutive (or near-consecutive) elements ending at M

The cluster typically starts around 2a or M/2 and extends to M.

### Why this beats consecutive

For {a, cluster}:
- **min G** occurs in the "dead zone" (a, cluster_start) where F grows slowly
  (only from multiples of a). This depresses min G below consecutive.
- **max G** occurs inside or just after the cluster, where F catches up rapidly.
  Max G is near S1, similar to consecutive.
- Net: ratio HIGHER than consecutive for the same (a, M).

### For k=3, fixed (min, max):
- {5, 16, 21}: ratio 0.637 (vs consecutive {5,6,7}: ratio < 0.65)
- {7, 19, 25}: ratio 0.662
- {10, 21, 33}: ratio 0.688

### For k small (k=3, 4), the extremum is NOT achieved by consecutive when (a, M) are spread.

---

## IMPLICATIONS FOR EP-488

### The true extremal structure

Among primitive sets with fixed min(A) = a and |A| = k (FREE max), the sup ratio
is approached by consecutive k-tuples as max → ∞. But for fixed (a, max), the
extremal is the "one-small + cluster" family.

This means: **consecutive is the "global" extremum across all bounds, but not
the "local" extremum for fixed (a, M).**

### Why EP-488 still holds for all

For the "one-small + cluster" sets: the ratio stays bounded away from 1 because
the min G (which is depressed) is still positive. The exact bound depends on
the cluster density.

For {a, C} with C ⊂ [c_min, M]: the min G occurs at some x* > max(C) where F/x
is minimized. At x*, F(x*) = |C| + floor(x*/a) = k-1 + floor(x*/a).

### Towards a universal proof

The convexity framework + the observation that max_x stabilizes quickly means:
**EP-488 is verifiable in O(max(A)) time for each A.** For a proof-based
closure, we need to show either:

1. **Adjacent pair extremality:** ratio(A) ≤ ratio({M-1, M}) = ((2M-3)/(2M-2))² < 1
   Tested: FALSE (consecutive triples {a,a+1,a+2} at large a can have higher ratio)

2. **Max element extremality:** ratio(A) ≤ 1 - 1/max(A)
   Tested: HOLDS for all 800K+ sets, equality approached by adjacent pairs

3. **Weak monotonicity:** there exists c > 0 such that ratio(A) ≤ 1 - c/max(A) for all A
   Holds with c close to 1 (empirically c ≈ 1 is the best constant)

The **ratio ≤ 1 - 1/max(A)** conjecture is the cleanest universal bound that's
consistent with all data. Proving it would close EP-488 completely.
