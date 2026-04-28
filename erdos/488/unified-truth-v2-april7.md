# EP-488: Unified Truth v2 — April 7, 2026 (Post-Kill #62)
## For any model. No direction imposed. Two tasks at the end.

---

## 1. THE PROBLEM

Erdős Problem 488 (1966): For a finite primitive set A (no a_i | a_j), define F_A(x) = |{n ≤ x : a|n for some a ∈ A}| and G(x) = F_A(x)/x.

Conjecture: G(m) < 2·G(n) for all m > n ≥ max(A).

Constant 2 is tight. Verified 23M+ families, zero failures.

---

## 2. WHAT'S PROVED

1. ✅ Convexity: extrema of G occur in [M, 10M]
2. ✅ Positive decomposition: F_A(x) = Σ L_j(⌊x/a_j⌋) (divisibility avoidance)
3. ✅ Weighted average: F(m)/F(n) = Σ w_j R_j, weights sum to 1
4. ✅ Single-obstruction theorem: ≤1 active obstruction → per-layer safe
5. ✅ 29-kernel classification: only 29 bad compact kernels, all ⊇ {2,3}, all prime
6. ✅ Quotient transport: q_{k,j} | 3·q_{k,i}
7. ✅ Child excess bounded: ≤ 17a_j
8. ✅ Box 1 / 3-tax bound: E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋) where C = K\{3}
9. ✅ Prime-cover rigidity: L_K(s)=1 iff all primes ≤ s are in K
10. ✅ Stock-flow identity: S_i - E_j = (2m-n)(L_i(u)+1) - n(Δ_i + Δ_j) — exact
11. ✅ Six Lean-verified foundational lemmas (Aristotle)
12. ✅ 6,659+ computational verifications of actual compensation, zero failures

---

## 3. WHAT'S BEEN KILLED (62 kills) — THE KEY LESSONS

### Every INTERMEDIATE BOUND dies.

This is the deepest lesson. Three different intermediate bounds have been tried:

**Kill #61:** Reduce to discrete inequality 2t[L_i(s')-1] ≥ (s+1)[L_i(t')+L_j(t)]
  → False at A={2,9,15,25}. Reduction too lossy.

**Kill #62:** Factor through Box 1 + Box 2 (child excess ≤ 3-tax ≤ parent slack)
  → Box 2 false at A={2,5,9,33,39,69,161,307}. Box 1 inflates child excess
    from 2 to 2092, a factor of 1046×. Parent can pay real cost but not inflated.

**Pattern:** The child excess is TINY (≤ 17a_j, typically single digits). Any upper
bound that isn't nearly tight will exceed what the parent can pay, even though the
parent trivially pays the actual cost.

### Every KERNEL COMPARISON dies.

**Kill #59:** Parent kernel = K\{3} — false (A={8,9,12}, parent kernel {8})
**Kill #60:** L_i(x) ≥ L_{B_j\{3}}(x) — false (A={2,9,15,25}, parent more obstructed)
**Your kill:** Parent sieve weaker — false (A={9,12,16}, parent obstruction 3 < child's 9)
**Kill #62:** Primitive-incompatibility of dangerous kernels — false (obstructions 11,13
  arrive through child-redundant multiples of 3 via elements 33,39)

**Pattern:** The parent kernel is UNPREDICTABLE. It can be simpler, more complex,
same, or completely unrelated. Any proof that requires the parent kernel to have
any specific relationship to the child kernel will be killed.

### Every SCALAR SUMMARY dies.

S₁, ρ, δ, k, Γ, per-layer bounds, fold orders — all killed by scaling, co-atoms,
or specific small counterexamples.

### The meta-lesson (5.4's diagnosis):

"EP-488 is a signed phase-synchronization problem on the lcm lattice. Every killed
strategy replaced phase data by a monotone or averaged scalar summary."

---

## 4. WHAT NEVER DIES: THE ACTUAL COMPENSATION

| Example | Child excess | Parent slack | Ratio |
|---------|-------------|-------------|-------|
| A={8,9,12} | 3 | 552 | 184:1 |
| A={2,9,15,25} | 22 | 554 | 25:1 |
| A={2,5,9,33,39,69,161,307} | 2 | 2090 | 1045:1 |

6,659+ instances checked. Zero failures. The phenomenon is indestructible.

---

## 5. FOUR INDEPENDENT EXPLANATIONS (all convergent)

All four models agree on WHY compensation works:

**Codex B (3-tax):** Child excess is a Buchstab derivative L_K(x) = L_C(x) - L_C(x/3).
Derivatives spike locally. Parent sees accumulated mass, not the derivative.

**Codex A (gap geometry):** Bad children are initial-gap phenomena (L_K(s)=1 means
complete small-prime cover). Parent evaluates past the gap.

**5.2 (cash-flow):** D = 2m-n > n. Every banked survivor earns D. Every new survivor
costs n. Since D > n, banked survivors are worth more. Parent has banked survivors.
Child has only new survivors.

**5.4 (stock vs flow):** Badness is flow (new survivors after n). Goodness is stock
(survivors already present at n). Stock beats flow because the coefficient 2m-n > n
amplifies stock more than n amplifies flow.

**All four say the same thing:** The child is frozen/starved/derivative. The parent
is deep/banked/accumulated. The coefficient structure (2m vs n) amplifies the
parent's advantage.

---

## 6. THE EXACT STATE OF THE GAP

The only unproved step:

"For every finite primitive set A, every m > n ∈ [M, 10M], and every compact layer j
with positive excess: ∃ 3-ancestor i with parent actual slack ≥ child actual excess."

  2m·L_i(⌊n/a_i⌋) - n·L_i(⌊m/a_i⌋) ≥ n·L_j(⌊m/a_j⌋) - 2m·L_j(⌊n/a_j⌋)

This CANNOT be factored through any intermediate bound (Kills #61, 62).
This CANNOT use kernel comparisons (Kills #59, 60, 62).
This must be proved DIRECTLY.

The stock-flow identity gives the exact comparison:
  S_i - E_j = (2m-n)(L_i(u)+1) - n(Δ_i + Δ_j)

This is non-negative when (2m-n)/(n) > (Δ_i + Δ_j)/(L_i(u)+1).
Since (2m-n)/n = 2m/n - 1 > 1 (because m > n), this requires L_i(u)+1 > Δ_i + Δ_j.

---

## 7. COMPLETELY DIFFERENT APPROACHES (not yet tried)

Maybe ancestor compensation is the wrong framework entirely. Here are approaches
that don't use parent-child matching at all:

### Approach A: Direct weighted average bound

F(m)/F(n) = Σ w_j R_j where w_j = L_j(s_j)/F(n), Σw_j = 1.

Bad layers have w_j = 1/F(n) (because L_K(s) = 1).
If there are B bad layers, their total weight is B/F(n).
Their maximum ratio is R_j ≤ (some bound from 29-kernel classification).

If we can show that B/F(n) is small enough that even at maximum ratio,
the bad layers' weighted contribution is dominated by the good layers'
contribution, we're done WITHOUT matching parents to children.

Key question: how many bad compact layers can a primitive set have?
If B ≤ c·F(n) for some c < 1, the weighted average might work directly.

### Approach B: Global budget without ancestor matching

Total budget = Σ_j (2m·L_j(s_j) - n·L_j(t_j)) = 2m·F(n) - n·F(m).
We need this > 0, i.e., F(m)/F(n) < 2m/n.

Instead of matching bad layers to good layers, can we bound:
  Total bad = Σ_{bad j} (n·L_j(t_j) - 2m·L_j(s_j))
  ≤ Σ_{bad j} (n·L_j(t_j) - 2m)     (since L_K(s)=1 for all bad j)
  = n·Σ_{bad j} L_j(t_j) - 2m·B

And total good = Σ_{good j} (2m·L_j(s_j) - n·L_j(t_j)) ≥ ???

Can we bound total good from below using F(n) and F(m)?

### Approach C: The weight anti-correlation

The weighted average F(m)/F(n) = Σ w_j R_j.
We know max R_j can exceed 2m/n (Kill #56).
But we need the WEIGHTED average to be < 2m/n.

This works if weights and ratios are NEGATIVELY correlated:
bad layers (high R_j) have small weights, good layers (low R_j) have large weights.

This is exactly what we observe: bad layers have w_j = 1/F(n) (minimum weight).
Can we prove this anti-correlation DIRECTLY without identifying ancestors?

### Approach D: Convex combination + extremal analysis

F(m)/F(n) is a convex combination of R_j values.
The maximum R_j for any single layer is bounded (from the 29-kernel classification).
The weight of layers achieving near-maximum R_j is bounded (L_K(s)=1 → weight = 1/F(n)).

For the weighted average to reach 2m/n, you'd need MANY bad layers or
VERY high R_j values. The 29-kernel classification bounds R_j.
Can we bound the NUMBER of bad layers in a primitive set?

### Approach E: Use F(n) directly

F(n) counts integers ≤ n with a divisor in A. For primitive A with max(A) = M ≤ n:
  F(n) ≥ k (each element contributes at least ⌊n/M⌋ ≥ 1 hit, with overlaps)

Actually F(n) = Σ L_j(s_j) and each L_j(s_j) ≥ 1 (since L_j(1) = 1 and s_j ≥ 1).
So F(n) ≥ k. The weight of each bad layer is 1/F(n) ≤ 1/k.

With B bad layers, their total weight ≤ B/k.
If B ≤ k-1 (at least one layer is good), and the good layers' average ratio
is bounded below 2m/n, the weighted average is safe.

Is B ≤ k-1 always true? Can every layer be bad simultaneously?

---

## 8. YOUR TASKS

### Task 1: Update your understanding
Read everything above. Identify which approach — ancestor compensation (with the
direct stock-flow identity) or a completely different framework (Approaches A-E) —
is most promising given the 62 kills.

### Task 2: Push as far as you can
Either prove the actual-slack ancestor lemma directly (using the stock-flow identity
without ANY intermediate bound), or develop one of the new approaches (A-E) to the
point where it either works or gets killed.

### Important constraints:
- Do NOT use kernel comparisons (Kills #59, 60, 62)
- Do NOT factor through intermediate bounds (Kills #61, 62)
- Do NOT use scalar summaries as thresholds (scaling kills them)
- You CAN use: stock-flow identity, 29-kernel classification, quotient transport,
  prime-cover rigidity, Buchstab identity, computational evidence, primitivity constraints
- If you find a counterexample to the actual-slack lemma, STOP and report it
- If you find a counterexample to ANY of approaches A-E, report it with the kill

Find the proof or tell us why it can't be found with current tools.
