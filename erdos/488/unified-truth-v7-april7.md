# EP-488: Open Field v7 — The Distributed-Core Gap
## April 7, 2026. Current: 86%. Move it.

---

## READ THIS FIRST

This is a FOCUSED addendum. Read v6 for full context (70 kills, 20 proved
results, complete constraint map). This document targets the ONE remaining gap.

---

## THE PROBLEM (5 lines)

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Verified 23M+ families. Zero failures.

---

## WHAT'S DONE (the 86%)

### Proved for specific families:
- Pure {2,3}-kernel family d{2,3,p₁,...,p_B}: PROVED for all B
- Pure {2,3,5,7}-kernel family d{2,3,5,7,p₁,...,p_B}: PROVED for all B
- Any single common-core bad band at any signature: PROVED
- All-compact sets (M > 40): PROVED
- Singletons, pairs: PROVED (Lean-verified)

### Proved asymptotically:
- {2,3}-distributed swarm: Window Lemma gives O(M²) slack vs O(M²/log y) excess
- {2,3,5,7}-distributed swarm: same, 2p-ancestors alone suffice
- General swarm: ancestor slack diverges vs bad excess (ratio ~ log log M)

### Key structural results:
- Self-funding: s ≤ 3 → E_j ≤ 0
- 29 relevant compact kernels, all ⊇ {2,3}
- Bad range: s ∈ [4,19], m/n ∈ (1, 2.5)
- Prime Spike Lemma: Δ_j ≤ 4
- First-layer theorem: S₁ > E_j for each individual bad child
- Signature table: {2,3,5,7} at (10,19,5) with c=17 is true extremal
- Surplus Dominance: Surplus ≥ S₁ (zero violations, all tested sets)
- Window Lemma: thin prime window [y, y^{1+ε}] of ancestors has
  O(M²) slack regardless of kernel (union bound, no sieve theory)

---

## THE ONE REMAINING GAP: DISTRIBUTED-CORE PRIMITIVES

Every proved case shares a feature: a COMMON CORE. The set has the form
d{small primes, p₁, ..., p_B} where all bad elements are multiples of d,
all ancestors are multiples of d, and the first layer 2d (or the four
base layers) pays for everything.

In a GENERAL primitive set, there is no common core d. Bad layers can
arise from DIFFERENT ancestor networks with no shared structure:

Example of what's NOT yet covered:
- Element 1001 = 7 × 11 × 13 gets kernel {2,3} from ancestors 2002, 3003
- Element 1003 = 17 × 59 gets kernel {2,3} from ancestors 2006, 3009
- These two bad layers have DIFFERENT ancestor pairs
- No common d, no shared base layer
- The first layer (smallest element, say 6) pays each INDIVIDUALLY
  (first-layer theorem) but might not pay BOTH collectively (Kill #65)
- The ancestors 2002, 3003, 2006, 3009 are good layers with slack,
  but their slack depends on THEIR obstruction sets

The question: does the global budget Σ_good S_j > Σ_bad E_j hold when
bad layers arise from distributed, non-shared ancestor networks?

---

## WHY WE BELIEVE IT'S TRUE

1. **Computational:** Zero violations across 23M+ families, 10,240 subsets
   of [2,20], and every constructed swarm. The Surplus Dominance ratio
   is ≥ 1.33 in all tested cases.

2. **Self-regulation:** Each bad layer CREATES at least 2 ancestors (for
   {2,3} kernel) or 4 ancestors (for {2,3,5,7}). These ancestors are
   good layers. More bad layers = more ancestors = more good slack.

3. **Window Lemma:** In ANY primitive set with bad layers using prime
   threshold y, there exists a thin window [y, y^{1+ε}] of ancestors
   with quasi-linear L (density ≥ c > 1/2) and combined slack O(M²).
   Bad excess is O(M²/log y). Ratio diverges.

4. **Density cancellation:** Ancestors and bad layers are sieved by the
   SAME prime threshold. Their densities are proportional to the same
   1/log y. When compared, the density cancels and pure geometry decides
   (and geometry gives 4m > n or similar, trivially true).

---

## APPROACHES TO CLOSE THE GAP

### Approach 1: The Extraction Lemma (most promising)

Prove: "From the existence of B bad layers in a general primitive set A,
extract a subset of ancestors whose combined slack exceeds Σ E_j."

The key structural fact: each bad layer with kernel K ⊇ {2,3} must have
elements in A creating quotients 2 and 3 (at minimum). These "support
elements" are good layers. The support elements might be shared across
bad layers (which is fine — their slack counts once but covers multiple
children) or independent (which is even better — more total slack).

The Window Lemma gives the quantitative tool: among the support primes
p that factor the ancestors, a thin window [y, y^{1+ε}] provides O(M²)
slack. The bad excess is O(M²/log y). For large enough M, done.

For small M: computational verification (extend from M ≤ 20 to M ≤ M₀).

### Approach 2: Induction with Surplus Dominance

Prove: Surplus(A) ≥ S₁ for all primitive A (the Surplus Dominance Conjecture).

Then induction on |A| closes EP-488:
- Base: |A| = 1, Surplus = S₁ > 0. ✓
- Step: Remove max(A). If layer M is good: Surplus grows. If bad:
  Surplus(A) = Surplus(A') - E_M ≥ S₁ - E_M > 0 (first-layer theorem). ✓

Surplus Dominance is equivalent to: "the non-first-layer net contribution
Σ_{j≥2} (2m·L_j(s_j) - n·L_j(t_j)) ≥ 0."

This has zero computational violations with worst ratio 1.33.

### Approach 3: Direct F(m)/F(n) bound

Skip layers entirely. Bound F(m)/F(n) < 2m/n directly using properties
of primitive sets (Erdős density bound Σ 1/(a log a) < ∞, or the
Behrend/Erdős structure theorem for primitive sequences).

This would bypass all layer-based kills but requires new techniques
not yet explored in the project.

### Approach 4: Finite verification + asymptotic

Show: for M ≥ M₀, the Window Lemma asymptotic works uniformly.
For M < M₀: extend computational verification.

If M₀ is reasonable (say ≤ 10⁶), this is a legitimate proof strategy.
The Window Lemma gives ratio ~ log log M, which exceeds 1 once
M > e^{e^C} for some explicit constant C.

### Approach 5: Something entirely new

70 kills map the dead territory. The proof lives outside all of it.
If you see a path nobody has tried, take it.

---

## CONSTRAINTS (what's killed)

- No per-layer bounds (Cat B)
- No scalar thresholds (Cat C)
- No kernel comparisons across signatures (Cat G + Kill #70)
- No intermediate bounds (Cat H)
- No S₁ alone for collective payment (Cat I, Kill #65)
- No constant B (Cat J, Kill #66)
- No naive IE factor gap (Cat M, Kill #68)
- Must use divisibility avoidance, not coprimality (Kill #48)

---

## YOUR TASK

Close the distributed-core gap. Or show why it can't be closed.

The proof is 86% complete. Every specific construction works. Every
computational test passes. The mechanisms are identified. The extremal
cases are handled. What remains is universality.

70 kills are your map. 20+ proved results are your tools.
Find the bridge from "every construction works" to "all primitive sets work."
