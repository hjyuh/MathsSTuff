# EP-488: Unified Truth — April 7, 2026
## For any model. No direction imposed. Find what's true.

---

## 1. THE PROBLEM

Erdős Problem 488 (1966): For a finite primitive set A = {a_1 < ... < a_k} (no a_i | a_j), define F_A(x) = |{n ≤ x : a|n for some a ∈ A}| and G(x) = F_A(x)/x.

Conjecture: G(m) < 2·G(n) for all m > n ≥ max(A).

Constant 2 is tight (singletons approach it). Verified 23M+ families, zero failures.

---

## 2. COMPLETE PROOF CHAIN (current state)

1. ✅ Convexity reduction: extrema of G occur in [M, 10M].
2. ✅ Exact positive decomposition: F_A(x) = Σ_j L_j(⌊x/a_j⌋) where L_j counts integers avoiding the obstruction set B_j (divisibility avoidance, NOT coprimality).
3. ✅ Weighted average: F(m)/F(n) = Σ w_j R_j, weights sum to 1, w_j = L_j(⌊n/a_j⌋)/F(n).
4. ✅ Single-obstruction theorem: layers with ≤1 active obstruction satisfy per-layer EP-488.
5. ✅ Finite classification: only 29 bad compact kernels exist. All contain {2,3}, all are prime subsets of {2,3,5,7,11,13,17,19}, all have L_K(s) = 1.
6. ✅ Quotient Transport Lemma: q_{k,j} | 3·q_{k,i} (child obstructions bounded by 3× parent obstructions). Proved rigorously.
7. ✅ Child excess bounded: worst case ≤ 17·a_j across all 29 signatures.
8. ❓ **Actual-slack ancestor lemma**: for every bad compact child j, ∃ 3-ancestor i with parent actual slack ≥ child actual excess. Verified 6,658 instances, zero failures, margins enormous (worst: 554 vs 22, ratio 25:1).
9. ✅ If step 8 holds → EP-488 proved.

---

## 3. FORMALLY VERIFIED RESULTS (Lean 4, machine-checked via Aristotle)

All 6 compile cleanly with standard axioms only.

1. **Primitive Divisor Lemma**: For primitive (a,b) with a < b, gcd(a,b) ≤ a/2.
2. **Subset LCM Bound**: For primitive pairs, lcm(a,b) ≥ 2b.
3. **Floor Gap Bound**: For n ≥ a > 0: n < 2a(⌊n/a⌋ + 1).
4. **Sieve Monotonicity**: If b | b', then |{n ≤ y : b' ∤ n}| ≥ |{n ≤ y : b ∤ n}|.
5. **Single Obstruction Count**: L_{b}(y) = y - ⌊y/b⌋.
6. **EP-488 for Singletons**: ⌊m/a⌋·n < 2·⌊n/a⌋·m for m > n ≥ a > 0.

---

## 4. THE 61 KILLS — WHAT FAILED AND WHY

### Category 1: Per-layer bounds (Kills #46, 51, 54, 56)
**What:** Bound each layer's ratio R_j < 2m/n individually.
**Why it dies:** Individual layers CAN exceed 2m/n. A={2,3,5}, layer a=5, n=24, m=35 gives R_j = 3 > 2.917.
**Root cause:** Bad layers have small weights in the weighted average. The bound fails per-layer but the weighted sum is safe. Per-layer bounds throw away the weight information.
**Lesson:** Proof must be COLLECTIVE — use the weighted structure.

### Category 2: Scalar summary thresholds (Kills #45, 50, 57)
**What:** Find a parameter (S₁, ρ, δ, k) separating "easy" from "hard" sets.
**Why it dies:** Scaling A → tA preserves G ratios but moves any scalar across any threshold.
**Root cause:** EP-488 is scale-invariant. No absolute scalar can distinguish safe from dangerous.
**Lesson:** Proof must be SCALE-INVARIANT.

### Category 3: Inclusion-exclusion truncation (Kills #1-44 broadly)
**What:** Truncate the Möbius/IE expansion at order j and bound the remainder.
**Why it dies:** Co-atom sets {N/p : p prime | N} have S_j = C(k,j)/N growing binomially.
**Root cause:** The IE coefficients are not sign-definite. Truncation introduces unbounded error.
**Lesson:** Proof cannot truncate IE at any fixed order.

### Category 4: Monotone reductions (Kills #52, 55)
**What:** Map A to a simpler set C where EP-488 is easier, prove R(A) ≤ R(C).
**Why it dies:** No monotone map exists. Up-fold increases ratio in 36/4673 cases. Kawamura fold has no partitioning analog.
**Root cause:** The mapping changes which integers are covered in non-monotone ways.
**Lesson:** Proof must work on the ORIGINAL set.

### Category 5: Class enlargement (Kill #53)
**What:** Prove EP-488 for shifted progressions (r ≠ 0), specialize to multiples.
**Why it dies:** Shifted progressions can have ratio = ∞.
**Root cause:** Multiples (r=0) pin all phases at 0. Shifted progressions can delay their first hit arbitrarily. The r=0 structure is essential.
**Lesson:** Proof must use the MULTIPLES structure specifically.

### Category 6: Exact kernel matching (Kills #59, 60)
**What:** Show the 3-ancestor's kernel equals K\{3} or is dominated by it.
**Why it dies:** A={8,9,12}: parent kernel {8} ≠ K\{3}={2}. A={2,9,15,25}: parent kernel {2,3}, L_i(6)=2 < L_{K\{3}}(6)=3. A={9,12,16}: parent obstruction 3 < child's remaining 9.
**Root cause:** Quotient transport relates individual obstruction PAIRS (q_{k,j} | 3·q_{k,i}), but the FULL parent obstruction set can include extra obstructions from other elements. The parent can be MORE obstructed than the child's reduced set.
**Lesson:** Proof cannot assume any relationship between parent and child KERNEL shapes.

### Category 7: Discrete inequality reduction (Kill #61)
**What:** Reduce actual-slack comparison to 2t[L_i(s')-1] ≥ (s+1)[L_i(t')+L_j(t)].
**Why it dies:** A={2,9,15,25}, n=124, m=175: gives 28 ≥ 35, false. Even with idealized parent: 42 ≥ 45, false.
**Root cause:** The reduction is too lossy — it uses worst-case bounds on m and n that throw away the actual relationship between the coefficients.
**Lesson:** The actual-slack comparison cannot be reduced to a simpler inequality. It must be proved directly.

### Category 8: BAD boundedness (Kill #58)
**What:** Bound BAD(m,n) by a function of ρ alone.
**Why it dies:** A_N = {2p,3p,5p : p prime in [N,(1+δ)N]} has bounded ρ but BAD → ∞.
**Root cause:** You can have arbitrarily many bad layers at bounded aspect ratio by using many generators.
**Lesson:** The proof cannot bound BAD independently of GOOD. Compensation is inherently relational.

### Category 9: S₁ as middleman (Kill #57)
**What:** Use S₁ = Σ 1/a_i as an intermediate bound between G and δ.
**Why it dies:** 2δ > S₁ is false for primes ≤ 100 (S₁ ≈ 2.10, 2δ ≈ 1.76).
**Root cause:** For dense primitive sets, the IE terms S_j for j ≥ 2 contribute significantly to δ. S₁ alone overestimates the density.
**Lesson:** S₁ is not a useful upper bound on G for dense sets.

### THE META-LESSON (5.4 Pro's diagnosis):
"EP-488 is a signed phase-synchronization problem on the lcm lattice, not a density problem. Every killed strategy replaced phase data by a monotone or averaged scalar summary, so counterexamples could fake the summary while keeping the bad phase pattern."

---

## 5. THE CENTRAL MYSTERY

**Every proposed MECHANISM for why compensation works has been killed. But the compensation ITSELF has never failed.**

| Kill | Mechanism proposed | Counterexample | But compensation works? |
|------|-------------------|----------------|------------------------|
| #59 | Parent kernel = K\{3} | A={8,9,12} | Yes (552 vs 3) |
| #60 | L_i(x) ≥ L_{B_j\{3}}(x) | A={2,9,15,25} | Yes (554 vs 22) |
| #61 | Discrete inequality | A={2,9,15,25} | Yes (554 vs 22) |
| yours | Parent sieve weaker | A={9,12,16} | Yes (by inspection) |

6,658 instances checked across all primitive sets with M ≤ 20 (k ≤ 5) and 5,000 random sets with M ≤ 100. Zero failures. Minimum margin enormous.

The question is not WHETHER compensation works. It's WHY.

---

## 6. WHAT'S OBJECTIVELY TRUE (patterns from computation)

These are observed facts, not conjectures:

- Bad compact layers ALWAYS have L_K(s) = 1 (only integer 1 survives)
- Bad compact kernels ALWAYS contain {2,3} and ONLY primes
- The child excess is always TINY relative to a_j (worst: 17a_j)
- The 3-ancestor ALWAYS exists when 3 ∈ K (definitional)
- The 3-ancestor is ALWAYS smaller (a_i = 3g < hg = a_j since h ≥ 5)
- The 3-ancestor ALWAYS evaluates deeper (⌊n/a_i⌋ > ⌊n/a_j⌋)
- The 3-ancestor's actual slack ALWAYS exceeds child excess (6,658/6,658)
- The margins are ALWAYS large (minimum ratio ~25:1)
- The parent's kernel can be ANYTHING — same as child, simpler, more complex, unrelated
- Despite kernel unpredictability, the ACTUAL L_i values always produce enough slack

---

## 7. KEY IDENTITIES AND TOOLS

### The positive decomposition:
F_A(x) = Σ_j L_j(⌊x/a_j⌋), each L_j non-negative, non-decreasing.

### The Buchstab identity:
L_B(x) = L_{B\{p}}(x) - L_{B\{p}}(x/p)

### The quotient transport:
q_{k,j} | 3·q_{k,i} (child obstruction divides 3× parent obstruction)

### Floor bounds:
⌊n/a_i⌋ ≈ (h/3)⌊n/a_j⌋ with h ≥ 5, so parent floor ≥ (5/3)× child floor

### The floor-gap identity:
y/⌊y⌋ < 2 for y ≥ 1 (EP-488 for singletons, Lean-verified)

---

## 8. LITERATURE STATUS

- **Ahlswede-Khachatrian 1995** ("Density inequalities for sets of multiples"): ASYMPTOTIC densities only. Does not address finite oscillation. Dead end.
- **Ahlswede-Khachatrian 1997** (correlation inequality): Requires nonnegative measures. lcm-lattice coefficients μ_A(d) are signed. Cannot apply directly.
- **Granville-Soundararajan 2001**: GS integral framework reduces to signed lcm-lattice measure against smoothing kernel. Sets up the problem but doesn't close it (average ≠ pointwise).
- **Buchstab identity**: The most relevant tool. Directly relates child and parent sieve counts.
- **Friedlander-Granville-Hildebrand-Maier 1991**: Proves sieve oscillation but via continuous methods. Different framework.
- **The ancestor lemma is genuinely new mathematics** (Gemini confirmed via thorough search). Not a known theorem in any form.

---

## 9. COMPUTATIONAL EVIDENCE

- 23M+ families verified for EP-488 itself, zero violations
- Budget V+2U < C passes for 93.3% of primitive sets (M ≤ 20)
- 6,658 ancestor compensation instances, zero failures
- Tightest margin: 554 vs 22 (ratio 25:1) at A={2,9,15,25}
- Previously tightest: 552 vs 3 (ratio 184:1) at A={8,9,12}
- Clean conjecture: ratio ≤ 1 - 1/max(A), tight at adjacent pairs (800K+ verified)

---

## 10. WHAT WE'RE ASKING YOU TO DO

Do NOT try to prove the actual-slack ancestor lemma directly. Four mechanisms have been proposed and all four were killed. Instead:

**Step back and look at the data.**

The compensation works every time with enormous margins. Every mechanism we propose for WHY it works gets killed. But the PHENOMENON is indestructible.

Questions to consider:

1. What PATTERN do you see across all the counterexamples that killed mechanisms but confirmed compensation? Is there a common structural reason the compensation works that's DIFFERENT from all four killed mechanisms?

2. The parent is always smaller (a_i < a_j). The parent always evaluates deeper. The child always has L_K(s) = 1. Are these three facts ALONE sufficient? Can you show that ANY layer evaluating at floor values ≥ 6 with ANY obstruction set has enough slack to beat an excess of ≤ 17a_j?

3. The Buchstab identity connects child and parent: L_{B_j}(x) = L_{B_j\{3}}(x) - L_{B_j\{3}}(x/3). The child's count is literally the parent's reduced count minus a correction at x/3. What does this tell us about the RATIO L_{B_j}(t)/L_{B_j}(s) vs the parent's ratio?

4. Is there a proof that doesn't use kernel comparisons AT ALL? That just uses: (a) the parent is smaller, (b) the child excess is bounded by 17a_j, (c) some universal property of L_i at deep evaluation points?

5. Is the compensation phenomenon a consequence of something SIMPLER that we're overcomplicating? Every proved special case of EP-488 has a short proof. Is the general case also short, hiding behind the machinery we've built?

Find the pattern. Make the connections. Tell us what's actually going on.
