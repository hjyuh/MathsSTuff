# EP-488: Prove Anti-Alignment for Compact Primitive Sets (Prong 2)
## Self-contained prompt for GPT-5.2 Pro Extended — April 5, 2026

---

## THE PROBLEM

Erdős Problem 488: For a finite primitive set A (no element divides another), M = max(A), define G(x) = F_A(x)/x where F_A(x) counts multiples of A up to x.

**Conjecture:** G(m) < 2·G(n) for all m > n ≥ M.

Open. Verified computationally for 148,885+ sets, zero failures.

## THE DECOMPOSITION AND BUDGET FRAMEWORK

**Exact layer decomposition (verified):**

F_A(x) = Σ_j L_j(⌊x/a_j⌋)

where B_j = {a_i/gcd(a_i,a_j) : i<j, >1} and L_j(y) = #{n≤y : b∤n ∀b∈B_j}.

NOTE: L_j uses DIVISIBILITY AVOIDANCE (b∤n), NOT coprimality (gcd(n,b)=1). These differ.

**Normalized layers:** T_j(x) = (M/x)·L_j(⌊x/a_j⌋) = c_j + ε_j(x)
where c_j = r_j·d_j is constant (r_j = M/a_j, d_j = density of L_j).

**Collective budget (algebraic fact):** If V + 2U < C then sup(ΣT_j) < 2·inf(ΣT_j),
where V = Σ sup(ε_j), U = Σ sup(-ε_j), C = Σ c_j.

## THE TWO-PRONGED PROOF STRATEGY

A computational scan of 148,885 primitive sets revealed:

**Prong 1:** Sets with true EP-488 ratio near 2 ALWAYS satisfy V + 2U < C. These are "spread" sets (large max/min). Someone else (5.4 Pro) is handling this prong.

**Prong 2 (YOUR TASK):** The ~7% of sets where V + 2U ≥ C have:
- True EP-488 ratio well below 2 (max observed: 1.62)
- **Strong phase mixing / error cancellation**
- Compact structure (elements clustered near M)

The key diagnostic: define the **phase mixing ratio**:

  phase_mix = sup_x |Σ_j ε_j(x)| / Σ_j sup_x |ε_j(x)|

Measured values:
- Budget-PASSING sets: phase_mix ≈ 0.45 (moderate cancellation)
- Budget-FAILING sets: phase_mix ≈ 0.32 (STRONG cancellation, 68%)

So where the budget fails, the actual sum of errors is much smaller than the sum of individual worst cases. The triangle inequality is too pessimistic exactly where it matters.

## YOUR TASK: PROVE THE ANTI-ALIGNMENT BOUND

For primitive sets where V + 2U ≥ C, prove that:

  sup_{x ∈ [M,10M]} (Σ_j ε_j(x)) + 2·sup_{x ∈ [M,10M]} (-Σ_j ε_j(x)) < C

This is WEAKER than V + 2U < C because it bounds the sum of errors directly, not the sum of bounds.

Equivalently (using 5.2's earlier reformulation): prove that for these sets, the actual oscillation of H(x) = Σ T_j(x) around its mean C satisfies the factor-2 condition.

### What you need to show:

The ε_j(x) functions oscillate at different rates as x varies. Specifically:

- ε_j(x) depends on x through y_j = ⌊x/a_j⌋ and {x/a_j}
- L_j(y_j) is periodic in y_j with period p_j = lcm(B_j)
- In x-space, this creates oscillation with effective period a_j·p_j
- Different layers have different a_j and different p_j

**The anti-alignment mechanism:** When A is compact (all a_j near M), the different layers' periodicities a_j·lcm(B_j) are generally distinct (different a_j, different B_j). So as x sweeps through [M, 10M], the layers' errors cycle at different rates and tend to cancel.

### Possible approaches:

**A) Large-sieve / mean-value theorem:**
Bound ∫_M^{10M} |Σ ε_j(x)|² dx using orthogonality of different periodicities.
Then use the fact that Σ ε_j is a "trigonometric polynomial" with bounded number of
frequencies to convert L² → L∞ via Bernstein's inequality.

**B) Direct: exploit the structure of budget-failure sets.**
Budget failures have all r_j ≈ 1 (compact). So y_j = ⌊x/a_j⌋ ≈ ⌊x/M⌋ for all j.
This means all layers are "seeing" roughly the same y-range. But L_j(y) depends on
DIFFERENT B_j sets, so the outputs are different functions of the same input.
This is like evaluating k different periodic functions at the same point — their sum
has bounded oscillation if the functions are "sufficiently independent."

**C) Convexity-based:**
G(x+L) is a strict convex combination of G(x) and δ_A (proved). For compact sets,
L = lcm(A) is not too large relative to M. The contraction rate might directly force
the first-period oscillation below factor-2.

## STRUCTURAL PROPERTIES OF BUDGET-FAILURE SETS

From the worst budget failure A = {8,9,10,12,15}, M = 15:

Layer details:
- j=1: a=8, r=1.875, B=∅, d=1, c=1.875
- j=2: a=9, r=1.667, B={8}, d=0.875, c=1.458
- j=3: a=10, r=1.5, B={4,9}, d=0.667, c=1.0
- j=4: a=12, r=1.25, B={2,3,5}, d=0.267, c=0.333
- j=5: a=15, r=1.0, B={2,3}, d=0.333, c=0.333

C = 5.0, V+2U = 5.931, budget ratio = 1.186.
But true ratio sup H / inf H = 1.267 — well below 2.

Key observations:
- All r_j are between 1 and 1.875 (compact-ish)
- B_j elements are small (2,3,4,5,8,9)
- lcm(B_j) values: 1, 8, 36, 30, 6
- The periodicities are all different → phase mixing

## WHAT'S ALREADY PROVED

1. EP-488 for pairs, triples, consecutive k-tuples, one-anchor families
2. EP-488 for sparse sets (Σ 1/a ≤ 2/min(A))
3. EP-488 for compact sets (max ≤ 2·min - 1) ← NOTE: this covers some budget-failure cases
4. EP-488 for any fixed k (by discrepancy + finite verification)
5. Convexity: G(x+L) is convex combination of G(x) and δ_A
6. Layer decomposition F_A = Σ L_j(⌊x/a_j⌋) is exact
7. V + 2U < C ⟹ sup < 2·inf (algebraic)
8. Complement FKG: ρ_Q ≥ 1/(|Q|+1) for coprime sieve (may adapt to L_j)

## 48 KILLED APPROACHES (do not attempt)

Key kills:
- Per-layer discrepancy C^loc < rρ/3: FALSE (rough numbers dip)
- Any threshold on S₁ or δ alone: not scale-invariant
- Coprimality model K_Q(y) = #{gcd(n,q)=1}: WRONG function (must use L_j)
- Structural inequality Σ ρ_j(r_j - 3q_j - 2) > 0: FALSE at A={2,3,5}
- φ(q_j) periodicity bound: applies to coprime counts, not L_j

## WHAT WOULD CONSTITUTE A SOLUTION TO PRONG 2

A proof of ANY of the following for primitive sets where V + 2U ≥ C:

(a) sup_x |Σ ε_j(x)| < C/3 (symmetric version)
(b) sup(Σε) + 2·sup(-Σε) < C (asymmetric, tighter)
(c) sup H / inf H < 2 by ANY method (bypassing the budget entirely)
(d) A reduction showing these sets are already covered by existing theorems
    (e.g., showing budget failures imply max ≤ 2·min - 1, which is Theorem 6)

Option (d) would be the cleanest: if you can show V + 2U ≥ C implies the set
is compact enough to fall under Theorem 6, then Prong 2 is free.

## DELIVERABLES

1. A rigorous proof (or strong partial result) for one of (a)-(d) above.
2. If you cannot prove it, identify the precise obstruction.
3. Clearly separate proved statements from conjectures.
4. If approach (d) works, state the exact implication chain.
