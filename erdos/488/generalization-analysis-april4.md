# EP-488 Generalization Analysis — April 4, 2026
## Claude Code (Opus), systematic approach analysis

---

## EXECUTIVE SUMMARY

**Goal:** Prove EP-488 for ALL primitive sets (not just one-anchor families).

**What's proved:** One-anchor families, all pairs, sparse sets (Sigma 1/a <= 2/min(A)).

**Remaining gap:** Dense primitive sets with |A| >= 3 and Sigma 1/a > 2/min(A).

**Main new results from this analysis:**

1. **Primitive Divisor Lemma (Lean-verified):** For a primitive pair (a,b) with a < b, lcm(a,b) >= 2b. Equivalently, gcd(a,b) <= a/2.

2. **IE Comparison Lemma for Triples:** For every primitive triple {a,b,c}, the quantity R = S1 - 2*S2 > 0, where S1 = sum 1/a_i and S2 = sum 1/lcm(a_i,a_j). This gives EP-488 for triples beyond an explicit horizon.

3. **Case Split Architecture:** The complete proof requires three regimes. Two are closed; the third (dense, large k) reduces to a single density claim.

4. **IE breaks down at k >= 10:** The second-order Bonferroni comparison R = S1 - 2*S2 can go negative for k >= 10. Different mechanism needed for large k.

---

## 1. PRIMITIVE DIVISOR LEMMA (LEAN-VERIFIED)

**Lemma (proper_dvd_le_half).** If d | n, d != n, and n > 0, then d <= n/2.

**Corollary (gcd_le_half_of_not_dvd).** If a > 0 and a does not divide b, then gcd(a,b) <= a/2.

**Corollary.** For a primitive pair (a,b) with a < b: lcm(a,b) = ab/gcd(a,b) >= ab/(a/2) = 2b.

More precisely: 1/lcm(a,b) <= 1/(2*max(a,b)).

**Lean proof (verified by Axle, lean-4.28.0):**
```lean
import Mathlib

theorem proper_dvd_le_half {d n : ℕ} (hn : 0 < n) (hd : d ∣ n) (hne : d ≠ n) :
    d ≤ n / 2 := by
  obtain ⟨k, hk⟩ := hd
  have hk_pos : 0 < k := by
    rcases k with _ | k
    · simp at hk; omega
    · omega
  have hk_ge2 : k ≥ 2 := by
    rcases k with _ | _ | k
    · omega
    · exfalso; exact hne (by omega)
    · omega
  have : d * 2 ≤ d * k := Nat.mul_le_mul_left d hk_ge2
  have : d * 2 ≤ n := by omega
  omega

theorem gcd_le_half_of_not_dvd {a b : ℕ} (ha : 0 < a) (hab : ¬ a ∣ b) :
    Nat.gcd a b ≤ a / 2 := by
  apply proper_dvd_le_half ha (Nat.gcd_dvd_left a b)
  intro heq
  exact hab (heq ▸ Nat.gcd_dvd_right a b)
```

---

## 2. IE COMPARISON FOR TRIPLES

### Setup
For primitive {a < b < c}: define
- S1 = 1/a + 1/b + 1/c
- S2 = 1/lcm(a,b) + 1/lcm(a,c) + 1/lcm(b,c)
- R = S1 - 2*S2

By Bonferroni:
- G(n) >= S1 - S2 - 6/n  (second-order IE lower bound)
- G(m) <= S1              (first-order IE upper bound)

So 2G(n) - G(m) >= R - 12/n. Positive for n > 12/R.

### Theorem: R > 0 for all primitive triples.

**Proof.** By the Primitive Divisor Lemma: for each primitive pair (a_i, a_j) with a_i < a_j:
  1/lcm(a_i, a_j) <= 1/(2*a_j)

Applied to the three pairs:
  1/lcm(a,b) <= 1/(2b)
  1/lcm(a,c) <= 1/(2c)
  1/lcm(b,c) <= 1/(2c)

So 2*S2 <= 1/b + 1/c + 1/c = 1/b + 2/c.

Therefore:
  R = S1 - 2*S2 >= (1/a + 1/b + 1/c) - (1/b + 2/c) = 1/a - 1/c

Since a < c: R >= 1/a - 1/c = (c - a)/(ac) > 0. QED.

### Quantitative bound
R >= (c - a)/(ac). The IE horizon is:
  n_IE = 12/R <= 12ac/(c-a)

Special cases:
- c = a+1: n_IE <= 12a(a+1) ~ 12a^2
- c = 2a:  n_IE <= 12*2a^2/a = 24a
- c >> a:  n_IE ~ 12a

### Worked examples
- {3,4,5}: R = 1/3+1/4+1/5 - 2(1/12+1/15+1/20) = 47/60 - 2(23/60) = 47/60 - 46/60 = 1/60. Wait...

Let me recompute. 1/lcm(3,4)=1/12, 1/lcm(3,5)=1/15, 1/lcm(4,5)=1/20.
S2 = 1/12+1/15+1/20 = (5+4+3)/60 = 12/60 = 1/5.
2*S2 = 2/5.
S1 = 1/3+1/4+1/5 = (20+15+12)/60 = 47/60.
R = 47/60 - 24/60 = 23/60 ~ 0.383. n_IE = 12/(23/60) = 720/23 ~ 31.

- {3,5,7}: S1=1/3+1/5+1/7=71/105, S2=1/15+1/21+1/35=(7+5+3)/105=15/105=1/7.
R = 71/105-2/7 = 71/105-30/105 = 41/105 ~ 0.390. n_IE ~ 31.

- {10,11,99}: S1=199/990, S2=1/110+1/990+1/99=9/990+1/990+10/990=20/990.
R = 199/990-40/990 = 159/990 ~ 0.161. n_IE ~ 75.

All strictly positive, confirming R > 0.

### What R > 0 gives and doesn't give

**Gives:** EP-488 for any primitive triple beyond n > 12/R. Combined with the discrepancy tail (C <= 6 for triples, horizon n_0 = 18/delta_A), this covers n > min(12/R, 18/delta_A).

**Doesn't give:** EP-488 for n in [max(A), min(12/R, 18/delta_A)]. This "early range" requires a separate argument.

### Early-range analysis for triples

For n >= max(A) = c: G(n) >= (floor(n/a) + floor(n/b) - floor(n/lcm(a,b)))/n.

The key comparison at n = c:
  2G(c) >= 2(floor(c/a) + floor(c/b) - floor(c/lcm(a,b)))/c
  G(m) <= S1 = 1/a + 1/b + 1/c

For consecutive triples {a, a+1, a+2}:
  F(c)/c = 3/c (since c = a+2, only a, a+1, a+2 themselves are counted for small a).
  But 2*3/(a+2) = 6/(a+2) and S1 ~ 3/a.
  Need 6/(a+2) > 3/a, i.e., 6a > 3(a+2), i.e., 3a > 6, i.e., a > 2. TRUE for a >= 3.

  More carefully: S1 = 1/a + 1/(a+1) + 1/(a+2) < 3/a.
  And 6/(a+2) > 3/a iff 6a > 3a + 6 iff a > 2. So for a >= 3: 2G(c) > S1 >= G(m). DONE.

For general n in [c, 2a]: F(n) = 3 (just the three elements), G(n) = 3/n >= 3/(2a).
  2G(n) >= 6/(2a) = 3/a > S1 (since S1 < 3/a for a >= 3). DONE.

For n in [2a, 3a]: F(n) >= 4 (adds one more a-multiple), G(n) >= 4/(3a).
  2G(n) >= 8/(3a). Need > S1 ~ 3/a. 8/3 > 3? NO (8/3 = 2.67 < 3).

  BUT: F(n) >= floor(n/a) + floor(n/b) + 1 - floor(n/lcm(a,b)) which for n ~ 2.5a gives
  floor(2.5) + floor(2.5a/(a+1)) + 1 ~ 2 + 2 + 1 = 5. G ~ 5/(2.5a) = 2/a.
  2G ~ 4/a > 3/a. YES for exact counting.

**Bottom line for triples:** A layer-by-layer analysis (similar to the Principal-Layer Lemma for one-anchor) should close the early range. The structure is:
- In each "layer" [ra, (r+1)a): each of a, b, c contributes ~1 new multiple
- So F grows by ~3 per a integers, keeping G ~ 3/a
- 2G ~ 6/a > 3/a ~ S1 >= G(m)

This is not fully rigorous yet — it needs the analog of the Principal-Layer argument showing the contributions are "fresh" (not overcounted).

---

## 3. IE COMPARISON BREAKS DOWN FOR LARGE k

**Key example:** First 10 primes {2,3,5,7,11,13,17,19,23,29}.
S1 ~ 1.533. S2 = (S1^2 - sum 1/p^2)/2 ~ (2.35 - 0.30)/2 = 1.025.
R = 1.533 - 2.050 = -0.517 < 0.

The second-order Bonferroni comparison FAILS. This is fundamental: for large k, the pairwise overlaps accumulate faster than the single terms.

**However:** For these large-k sets, delta_A is very close to 1 (delta ~ 0.92 for first 10 primes), so G(n) > 1/2 for all large n, giving 2G(n) > 1 >= G(m) trivially.

The IE mechanism and the density mechanism have COMPLEMENTARY ranges:
- IE works for small k (proven for k <= 3)
- Density works for large k (when delta_A > 1/2)

---

## 4. APPROACH 1: QUOTIENT-CORE REDUCTION

The recursion F_A(x) = F_{A\{a}}(x) + floor(x/a) - F_{Q_a}(floor(x/a)) is excellent for bounding the discrepancy constant C:
- C_singletons = 0
- C_pairs < 2
- C_triples <= C_pair + 1 + C_{Q_a} <= 2 + 1 + 2 = 5

But it does NOT directly prove EP-488 because G(m)/(2G(n)) doesn't factor through the recursion. The ratio comparison involves both F and x, and the compression x -> floor(x/a) destroys the monotonicity structure.

**Verdict:** Essential supporting tool (bounds C), not a standalone proof route.

---

## 5. APPROACH 2: LARGE-k DENSITY ARGUMENT

### The mechanism
For delta_A > 1/2: G(n) > 1/2 for large n, so 2G(n) > 1 >= G(m).

### When is delta_A > 1/2?

**Coprime case (e.g., primes):** delta_A = 1 - prod(1 - 1/a_i).
Product < 1/2 iff sum(-log(1-1/a)) > log 2, approximately when sum 1/a > log 2 ~ 0.693.

For the first 4 primes {2,3,5,7}: prod = (1/2)(2/3)(4/5)(6/7) = 48/210 = 0.229 < 1/2.
So delta > 1/2 already at k=4 primes.

**General primitive sets:** By Bonferroni second-order:
delta_A >= S1 - S2 > S1 - S1^2/2 (since S2 < S1^2/2 for coprime).
At S1 = 1: delta > 1 - 1/2 = 1/2. Barely.

For non-coprime primitive sets: S2 could be larger (gcd > 1 increases 1/lcm). But the product formula still applies modulo prime factorization — the overlaps from shared factors don't drastically change delta_A.

### The gap in this approach

"G(n) > 1/2 for large n" requires n > 2C/(2*delta_A - 1) where C is the discrepancy. For the EARLY range [max(A), horizon], we need G(n) > 1/2 directly.

At n = max(A): G(max(A)) >= k/max(A) (each element contributes at least 1). For k > max(A)/2: this gives G > 1/2.

But primitive sets can have max(A) >> k (e.g., k primes can have max(A) ~ k*log(k)).

**What's needed:** A proof that for dense primitive sets with sum 1/a > 2/min(A), either:
(a) G(n) > 1/2 for all n >= max(A), or
(b) The discrepancy C is small enough (polynomial in k) that the early range is manageable.

The Parseval obstruction (C = Omega(2^{k/2}) for large primes) applies to SPARSE sets. For DENSE sets, empirical C values are O(k):
- {18,19,20}: C ~ 3.1
- {9,16,17,19}: C ~ 4.8
- {3,5,13,17,19}: C ~ 5.8

**Conjecture (Dense Discrepancy):** For primitive sets with sum 1/a > 2/min(A), we have C = O(k^2). If true, this closes the large-k regime.

---

## 6. APPROACH 4: CASE SPLIT (RECOMMENDED STRATEGY)

### Architecture

**Regime 1: k <= 3.**
- k=1: Trivial (G monotone decreasing, ratio < 1 always).
- k=2 (pairs): PROVED (4-line argument: 2G(n) > 2/a > 1/a + 1/b > G(m)).
- k=3 (triples): IE comparison R > 0 gives EP-488 beyond horizon 12/R. Early range needs Principal-Layer analog or discrepancy tail.

**Regime 2: k >= 4, SPARSE (sum 1/a <= 2/min(A)).**
PROVED by sparse-mass lemma.

**Regime 3: k >= 4, DENSE (sum 1/a > 2/min(A)).**
Two sub-cases:
- (3a) delta_A > 1/2: trivial for n beyond discrepancy horizon
- (3b) delta_A <= 1/2 but sum 1/a > 2/min(A): this is the critical gap

### The critical gap: Regime 3b

Does Regime 3b even exist? For delta_A <= 1/2 and sum 1/a > 2/min(A):

If min(A) = 2: sum > 1. By Bonferroni, delta >= sum - sum^2/2 > 1 - 1/2 = 1/2 (for coprime). Non-coprime could reduce delta. But A containing 2 is handled by Theorem A anyway (2G(n) > 1 trivially).

If min(A) = 3: sum > 2/3. delta >= S1(1-S1/2). At S1 = 2/3: delta >= (2/3)(2/3) = 4/9 < 1/2. So Regime 3b EXISTS for min(A) = 3.

Example: {3, 5, 7} with S1 = 71/105 ~ 0.676 > 2/3.
delta = 1 - (2/3)(4/5)(6/7) = 1 - 48/105 = 57/105 ~ 0.543 > 1/2. OK, this one is 3a.

Example: {3, 4, 5} with S1 = 47/60 ~ 0.783.
delta = 1 - (2/3)(3/4)(4/5) = 1 - 2/5 = 3/5 = 0.6 > 1/2. Also 3a.

For delta <= 1/2 to occur with sum > 2/3 and min=3: need heavy pairwise overlap.
{3, 6, ...}: NOT primitive (3|6).

For min(A) >= 3 with k >= 4: sum 1/a > 2/3 with delta <= 1/2 requires many non-coprime pairs. But primitivity (a_i does not divide a_j) limits this heavily.

**Conjecture:** For all primitive sets A with sum 1/a > 2/min(A) and min(A) >= 3, we have delta_A > 1/2.

If TRUE: Regime 3b is empty, and the case split reduces to:
- k <= 3: handled (pairs proved, triples need early-range closure)
- k >= 4, sparse: sparse-mass lemma
- k >= 4, dense: delta > 1/2, so 2G(n) > 1 >= G(m) for n beyond O(C/delta)

### What remains for EACH regime

| Regime | Status | Remaining work |
|--------|--------|----------------|
| k=1 | PROVED | None |
| k=2 (pairs) | PROVED | None |
| k=3 (triples) | PARTIAL | Early-range [max(A), 12/R] needs Principal-Layer analog |
| k>=4 sparse | PROVED | None (sparse-mass lemma) |
| k>=4 dense | PARTIAL | Need rigorous delta > 1/2 proof, plus early-range with bounded C |

---

## 7. RECOMMENDED NEXT STEPS (priority order)

### 7.1 Close triples (highest impact, most tractable)
Prove EP-488 for all primitive triples by closing the early range. Two routes:
(a) **Principal-Layer analog for triples:** Show that in each "layer" [ra, (r+1)a), each of b and c contributes a fresh hit, so F grows by ~3 per a integers, keeping G ~ 3/a. Need: products (r-1)*b are distinct, non-overlap with a-multiples, and fresh.
(b) **Discrepancy tail for triples:** Prove C <= 5 for all primitive triples (via quotient-core), then use analytic tail for n > 15/delta_A. Verify [max(A), 15/delta_A] uniformly.

### 7.2 Prove delta > 1/2 for dense primitive sets with min >= 3
This would kill Regime 3b. Approach: for min(A) = a1 >= 3 and sum 1/a > 2/a1:
- If all pairs coprime: delta = 1 - prod(1-1/a) and sum > 2/3 forces the product below 1/2.
- If some pairs share factors: the shared factors INCREASE delta (overlapping progressions cover MORE integers, not fewer). So coprime is actually the WORST case for delta.

Wait — that's backwards. Shared factors means 1/lcm is larger, so IE gives LOWER delta. But the exact delta (full IE) could go either way.

Actually: delta_A = P(random integer hit by some a in A). Sharing factors between elements can REDUCE this (if the same integers are hit by multiple elements). So the coprime case gives the HIGHEST delta for given sum 1/a.

This means: if the coprime case has delta > 1/2 at sum > 2/a1, and non-coprime could have delta < 1/2. The conjecture may be FALSE.

**Correction:** Need to handle the non-coprime dense case separately. The quotient-core recursion might help here — non-coprime elements peel into simpler quotient-cores.

### 7.3 Bound C for dense primitive sets
Prove C = O(k^2) for primitive sets with sum 1/a > 2/min(A). The Parseval obstruction applies only to sparse sets (large primes) which are killed by the sparse-mass lemma. So the obstruction doesn't apply to the dense regime.

### 7.4 Unify via enhanced quotient-core
The quotient-core recursion reduces |A| by 1. After k-2 peeling steps, we reach a pair (proved) or singleton (trivial). If we can show that the ratio 2G(n)/G(m) doesn't worsen at each peeling step, induction on k works.

---

## APPENDIX: VERIFIED LEAN CODE

```lean
import Mathlib

theorem proper_dvd_le_half {d n : ℕ} (hn : 0 < n) (hd : d ∣ n) (hne : d ≠ n) :
    d ≤ n / 2 := by
  obtain ⟨k, hk⟩ := hd
  have hk_pos : 0 < k := by
    rcases k with _ | k; · simp at hk; omega; · omega
  have hk_ge2 : k ≥ 2 := by
    rcases k with _ | _ | k; · omega; · exfalso; exact hne (by omega); · omega
  have : d * 2 ≤ d * k := Nat.mul_le_mul_left d hk_ge2
  have : d * 2 ≤ n := by omega
  omega

theorem gcd_le_half_of_not_dvd {a b : ℕ} (ha : 0 < a) (hab : ¬ a ∣ b) :
    Nat.gcd a b ≤ a / 2 := by
  apply proper_dvd_le_half ha (Nat.gcd_dvd_left a b)
  intro heq
  exact hab (heq ▸ Nat.gcd_dvd_right a b)
```
