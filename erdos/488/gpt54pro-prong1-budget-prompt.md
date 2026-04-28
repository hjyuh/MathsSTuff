# EP-488: Prove V + 2U < C for Spread Primitive Sets (Prong 1)
## Self-contained prompt for GPT-5.4 Pro Extended — April 5, 2026

---

## THE PROBLEM

Erdős Problem 488: Let A = {a_1 < ... < a_k} be a finite primitive set (no a_i | a_j). Let M = max(A). Define F_A(x) = |{n ≤ x : a | n for some a ∈ A}| and G(x) = F_A(x)/x.

**Conjecture:** For all m > n ≥ M: G(m) < 2·G(n).

This is open. Computationally verified for 148,885+ primitive sets with zero failures. The constant 2 is best possible (singletons approach it).

## THE EXACT LAYER DECOMPOSITION (verified computationally)

Sort A = (a_1 < ... < a_k). Assign each multiple n to the SMALLEST a_j dividing it. Then:

**F_A(x) = Σ_j L_j(⌊x/a_j⌋)**

where:
- B_j = {a_i / gcd(a_i, a_j) : i < j, quotient > 1} (obstruction set from earlier elements)
- L_j(y) = #{n ≤ y : b ∤ n for all b ∈ B_j} (divisibility avoidance, NOT coprimality)

**IMPORTANT:** L_j counts integers avoiding DIVISIBILITY by elements of B_j, not coprimality. These are different: 4∤6 but gcd(4,6)≠1.

Properties:
- B_1 = ∅ always (principal layer has no obstructions), so L_1(y) = y
- L_j is periodic with period lcm(B_j)
- Density: d_j = lim L_j(y)/y = Σ_{S⊆B_j} (-1)^|S| / lcm(S) (exact inclusion-exclusion)
- For B_j = ∅: d_j = 1

## THE COLLECTIVE OSCILLATION BUDGET

Define normalized layers: T_j(x) = (M/x) · L_j(⌊x/a_j⌋)

Each T_j decomposes as: T_j(x) = c_j + ε_j(x) where c_j = r_j · d_j is CONSTANT.
(Here r_j = M/a_j.)

Define excursions:
- v_j = sup_x ε_j(x) (upward)
- u_j = sup_x (-ε_j(x)) (downward)
- V = Σ v_j, U = Σ u_j, C = Σ c_j

**Theorem (algebraic):** If V + 2U < C, then sup Σ T_j < 2·inf Σ T_j on [M, 10M]. ∎

(The asymmetry V + 2U comes from: upward spikes hurt the numerator once, downward dips hurt the denominator twice under the factor-2 comparison.)

## COMPUTATIONAL RESULTS (148,885 primitive sets scanned)

With the CORRECT L_j decomposition:

| Scan | Sets | V+2U<C passes | Pass rate |
|------|------|---------------|-----------|
| Exhaustive (M≤20, k≤5) | 4,673 | 4,359 | 93.3% |
| Random (M≤50, k≤8) | 1,000 | 982 | 98.2% |
| Consecutive blocks | 343 | 316 | 92.1% |
| Compact near-M | 1,000 | 1,000 | 100% |
| Prime-prefix ≤47 | 15 | 15 | 100% |

**Critical pattern:** Sets with true ratio near 2 (dangerous for EP-488) ALWAYS pass V+2U<C. Budget failures only occur for sets with true ratio ≤ 1.62.

Worst budget failure: A = {8,9,10,12,15}, budget ratio 1.186, true ratio 1.267.

## YOUR TASK: PROVE PRONG 1

**Prove that V + 2U < C holds for all primitive sets A where the true EP-488 ratio is "dangerous" (close to 2).**

More precisely, the data shows that budget failures only occur for sets with many elements clustered near M (compact-ish sets). For "spread" sets where max/min is large, the principal layer dominates and the budget holds easily.

### Suggested approach:

**Step 1: Bound the principal layer's contribution.**
For j=1 (a_1 = min(A)): B_1 = ∅, d_1 = 1, c_1 = r_1 = M/min(A).
The principal layer contributes c_1 = M/min(A) to C.
Its excursion: v_1 = sup_{x∈[M,10M]} (M/x · ⌊x/a_1⌋ - M/a_1).
Since ⌊x/a_1⌋ = x/a_1 - {x/a_1}, we get ε_1(x) = -(M/x)·{x/a_1} ∈ [-1, 0].
So v_1 = 0 and u_1 ≤ 1. The principal layer contributes 0 to V and ≤ 1 to U.

**Step 2: Bound all other layers' excursions.**
For j ≥ 2: L_j(y) is periodic with period p_j = lcm(B_j). The discrepancy
|L_j(y) - d_j·y| ≤ 2^|B_j| - 1 (from inclusion-exclusion, trivial bound).

So: v_j + u_j ≤ 2·(2^|B_j| - 1)·(M/M) + d_j = 2^|B_j+1| - 2 + d_j.
(This uses M/x ≤ 1 and the floor-term contribution.)

Actually, more carefully: |ε_j(x)| = |(M/x)(L_j(y_j) - d_j·y_j) - (M/x)·d_j·{x/a_j}|
≤ (M/x)|L_j(y_j) - d_j·y_j| + d_j ≤ |L_j(y_j) - d_j·y_j| + d_j.

For y_j ∈ [r_j/10, r_j], this is ≤ 2^|B_j| - 1 + d_j.

**Step 3: Show budget holds when M/min(A) is large.**
C ≥ c_1 = M/min(A).
V + 2U ≤ 2 + 3·Σ_{j≥2} (2^|B_j| - 1 + d_j).

Budget holds if M/min(A) > 2 + 3·Σ_{j≥2} (2^|B_j| + d_j).

**Step 4: Bound Σ 2^|B_j|.**
|B_j| = number of distinct quotients a_i/gcd(a_i, a_j) > 1 for i < j.
This is at most j-1 (one quotient per earlier element).
So 2^|B_j| ≤ 2^{j-1}.
And Σ_{j=2}^k 2^{j-1} = 2^k - 2.

This gives: budget holds if M/min(A) > 3·2^k.

**Step 5: Is M/min(A) > 3·2^k always true for "dangerous" sets?**
Not in general — compact sets have M/min(A) ≈ 2 and k can be large.
But compact sets are already proved (Theorem 6 below).

The question: is there a clean partition of primitive sets into
"spread" (M/min(A) > f(k)) where the budget works, and "compact"
(M/min(A) ≤ f(k)) where the existing proof works?

## WHAT'S ALREADY PROVED (do not re-derive)

1. EP-488 for all primitive pairs
2. EP-488 for all primitive triples
3. EP-488 for all consecutive k-tuples
4. EP-488 for all one-anchor families (a prime, plus elements in one residue class)
5. EP-488 for sparse sets (Σ 1/a ≤ 2/min)
6. EP-488 for compact sets (max ≤ 2·min - 1)
7. EP-488 for any fixed k (discrepancy + finite verification)
8. Convexity: G(x+L) is a convex combination of G(x) and δ_A
9. Extrema stabilize by 10·max(A)
10. The decomposition F_A = Σ L_j(⌊x/a_j⌋) is exact (computationally verified)
11. The collective budget V + 2U < C ⟹ sup < 2·inf (algebraic)

## CONSTRAINTS

- Proof must be SCALE-INVARIANT (scaling A → tA preserves the ratio)
- No threshold on S₁ = Σ 1/a or δ_A alone (not scale-invariant)
- Ratios like max/min, k, d_j are scale-invariant and allowed

## DELIVERABLES

1. A rigorous proof that V + 2U < C holds for all primitive sets satisfying [CONDITION], where [CONDITION] covers all sets with true ratio close to 2.

2. Explicit identification of [CONDITION] — ideally something like "max(A)/min(A) > f(k)" or "Σ 1/a_j < g(min(A))".

3. If you cannot prove this for a general [CONDITION], identify the precise obstruction and the tightest [CONDITION] you CAN prove.

4. Clearly separate proved statements from conjectures.
