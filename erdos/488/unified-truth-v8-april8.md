# EP-488: Open Field v8 — Two Regimes
## April 8, 2026. Current: 80%. Move it.

---

## THE PROBLEM (5 lines)

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Verified 23M+ families. Zero failures.

---

## CRITICAL CORRECTION: TWO REGIMES, NOT ONE

Previous documents claimed "bad layers have s ∈ [4,19], m/n ∈ (1,2.5),
Δ ≤ 4." These are TRUE at compact scale (t ≤ 20) and FALSE globally.

### Compact scale (t ≤ 20): FULLY CLASSIFIED
Layers with a > M/2 evaluated in [M, 10M] always have t ≤ 20.
Here: 29 relevant kernels, Δ ≤ 4, m/n < 2.5 for positive excess.
Both extremal families proved (Codex B). Self-funding kills s ≤ 3.

### Deep scale (t >> 20): OPEN, HARDER
Layers with a ≤ M/2 can have t = 50, 100, or larger.
Here: kernel can contain ALL primes ≤ s for any s.
Δ can be arbitrarily large (= π(t) - π(s) + 1 roughly).
Bad layers exist at any m/n ratio. s can be any value ≥ 4.

EXAMPLE: A = {2,3,5,7,11,13,17,19,23,479}, layer a = 23.
B_23 = {2,3,5,7,11,13,17,19}. At n=483, m=805: s=21, t=35.
L(21) = 1, L(35) = 4. E = 322 > 0.
This is a bad layer with s = 21 — outside the "compact" range.

EXAMPLE: Same set, m = 2415 = 5n. Then t = 105, L(105) = 20.
E = 4830 > 0. Δ = 19. m/n = 5. All "compact scale bounds" violated.

INFINITE FAMILY: For any large s, take A = {primes ≤ s} ∪ {q, M}
where q is the first prime > s. Layer q has B = {primes ≤ s},
L(s) = 1, and E > 0 for suitable (n,m). s is unbounded.

---

## WHAT'S PROVED (permanent, scale-independent)

### Structural framework:
1. **Convexity:** extrema in [M, 10M]. ✅
2. **Positive decomposition:** F(x) = Σ L_j(⌊x/a_j⌋). ✅
3. **Weighted average:** F(m)/F(n) = Σ w_j R_j. ✅
4. **Self-funding:** s ≤ 3 → E_j ≤ 0. ✅
5. **First-layer theorem:** S₁ > E_j for each INDIVIDUAL bad child
   (uses: a₁ ≤ 2a_j/3 from primitivity, n ≥ 4a_j). ✅
6. **Floor Ratio Lemma:** n⌊m/a⌋ < 2m⌊n/a⌋ for a ≤ n. ✅ (Lean)
7. **Surplus Dominance:** Surplus ≥ S₁ (zero violations). Conjecture.

### Scale-independent tools:
8. **Superadditivity Lemma:** If lcm(a,b) > n for cross-component
   pairs, then B_A(n,m) ≥ Σ B_{Aᵢ}(n,m). ✅ PROVED.
9. **Component Reduction:** Counterexample to EP-488 can only live
   inside a single n-LCM connected component. ✅ PROVED.
10. **Codex B's H_A reduction:** EP-488 ⟺ 2mH_A(n) ≥ nH_A(m)
    where H_A counts non-first-layer covered integers. ✅

### Compact-scale results (VALID ONLY for t ≤ 20):
11. 29 relevant compact kernels, all ⊇ {2,3}. ✅ (compact only)
12. Bad compact range: s ∈ [4,19]. ✅ (compact only)
13. Prime Spike Lemma: Δ ≤ 4. ✅ (compact only)
14. Dangerous range: m/n < 2.5. ✅ (compact only)
15. Signature table: {2,3,5,7} at (10,19,5) is compact extremal. ✅
16. Pure {2,3} family proved, unbounded B. ✅
17. Pure {2,3,5,7} family proved, unbounded B. ✅
18. Single common-core bad band: first layer pays. ✅

### Graph-theoretic tools:
19. **Bad Layer Interaction:** Two bad elements in (n/20, n/4] with
    lcm ≤ n → gcd ≥ n/400. ✅ (for compact bad layers only)
20. **Connector Edge Classification:** c ~ b with c ≤ n/20 →
    quotient c/gcd(c,b) < 20, partitions into ≤ 18 classes. ✅
21. **Degree-Size Bound:** k bad neighbors in one class →
    c ≤ 4n/(k-1), so s_c ≥ (k-1)/4. ✅

### Lean-verified:
22. Six foundational lemmas (Aristotle). ✅

---

## THE 75 KILLS — KEY CATEGORIES

### A: Wrong function (Kill #48)
Coprimality ≠ divisibility avoidance. Use L_j correctly.

### B-F: Per-layer, scalar, IE truncation, monotone, class enlargement
All dead. Proof must be collective, scale-invariant, on original set.

### G: Kernel comparisons (Kills #59, 60, 62)
Parent kernels unpredictable. No parent-child kernel shape comparison.

### H: Intermediate bounds (Kills #61, 62)
Actual excess tiny, bounds inflate O(M). Compare directly.

### I: S₁ alone (Kill #65, CONFIRMED)
Prime-Product Swarm: B ≈ M/log log M bad layers overwhelm S₁.
Rigorously verified with simultaneity + support constraints.

### J: Constant B (Kill #66)
B unbounded. But self-regulation: more bad → more ancestors → more slack.

### K-L: Hallucinations, directional errors
Verify claims against established facts. Check inequality directions.

### M: Naive IE factor closure (Kill #68)
Pair strands eat 5/6 of main surplus. No termwise domination.

### N: Wrong proofs (Kill #69)
Result 16 proof wrong (lcm bound), T(d) sign wrong for d > n.

### O: Kernel monotonicity global reduction (Kill #70)
{2,3} is worst at FIXED signature but MILDEST across all signatures.
{2,3,5,7} at (10,19) gives E = 17a. Cannot reduce mixed → pure.

### P: Monotone reduction from pairs (Kill #71)
Adding generators can DECREASE surplus. No monotone comparison.

### Q: Compact-scale extrapolation (Kills #72-75)
BAD LAYERS EXIST BEYOND COMPACT SCALE.
s ∈ [4,19] is compact-only. Δ ≤ 4 is compact-only.
m/n < 2.5 is compact-only. Connectors CAN be bad.
The compact classification does NOT cover the full problem.

---

## THE REMAINING GAP: TWO FRONTS

### Front 1: Compact Scale (mostly solved, ~5% remaining)
For layers with t ≤ 20: fully classified. Both extremal families proved.
Remaining: formalize the general compact-scale charging for arbitrary
primitive sets (not just specific families). The Window Lemma +
degree-size bounds + superadditivity should close this with careful
constant extraction.

### Front 2: Deep Scale (the real gap, ~15% remaining)
For layers with t >> 20 (non-compact elements with full prime-cover
kernels): essentially unexplored.

Key properties of deep-scale bad layers:
- Element a ≤ M/2 (non-compact)
- Kernel B_a = {all primes ≤ s} for some s ≥ 4
- L(s) = 1 (frozen by prime-cover)
- L(t) = 1 + (number of primes in (s,t]) + (composites with all
  factors > s that are ≤ t)
- Δ = L(t) - 1 grows with prime density in (s,t]
- E = n·L(t) - 2m can be large

The "initial prime segment" kernel B = {2,3,...,p_s} is the deep-scale
analog of the compact {2,3,5,7} kernel. For deep scale:
- Each prime p ≤ s creates a p-ancestor in A (element with quotient p)
- The ancestor count is π(s) — logarithmically many
- Each ancestor creates a good layer
- Self-regulation: more primes in kernel → more ancestors → more slack

### The deep-scale self-regulation hypothesis:
For any primitive set with a bad layer at depth s (kernel = {primes ≤ s}),
the π(s) mandatory ancestors generate enough collective slack to cover
the bad excess.

This is the SAME self-regulation mechanism as compact scale, but with
logarithmically many ancestors instead of 2-4. The Buchstab telescope
and Window Lemma should apply, but this needs verification.

---

## APPROACHES

### 1. Surplus Dominance (most direct)
Prove: 2mH_A(n) ≥ nH_A(m) for all primitive A.
Zero violations across all tested sets. Scale-independent.
A direct proof would close EP-488 at both scales simultaneously.
This bypasses the compact/deep distinction entirely.

### 2. Deep-Scale Self-Regulation
Extend the Window Lemma to deep-scale ancestors.
A bad layer with kernel {primes ≤ s} forces π(s) ancestors.
In a thin window [s, s^{1+ε}] of ancestor primes, obstructions are
thin (Mertens product ≈ log s / log p → bounded for p close to s).
Each ancestor contributes O(mn/p) slack.
Sum: O(mn · log(1+ε)) = O(M²).
Bad excess: O(M² · Δ / (stuff)) — need to bound.

### 3. Component Analysis at Deep Scale
The superadditivity lemma works at any scale. The component reduction
works at any scale. Extend the connector analysis to deep-scale
components. The degree-size bounds generalize.

### 4. Induction on |A|
Base: singletons (Lean-verified). Step: remove max element.
If Surplus Dominance holds, induction closes EP-488.
Scale-independent approach that avoids the compact/deep split.

### 5. Something entirely new
75 kills map dead territory at BOTH scales. The proof must avoid all
killed mechanisms at all scales. Fresh eyes might find a route that
works uniformly.

---

## WHAT WE BELIEVE (computational evidence)

- 23M+ families: zero EP-488 violations
- All primitive subsets of [2,20]: zero surplus dominance violations
- Random search M ≤ 500: zero violations
- Every constructed infinite family: EP-488 holds
- Worst surplus dominance ratio: 1.33
- The global budget has NEVER failed at ANY scale

---

## YOUR TASK

Push the percentage. Up or down. Any route.

The problem has TWO regimes. Compact scale is mostly solved.
Deep scale is the real frontier. But a scale-independent approach
(Surplus Dominance, induction) could close both at once.

75 kills are your map. 22 proved results are your tools.
Find the proof. Or show where it breaks.
