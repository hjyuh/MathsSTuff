# POST-REVIEW ANALYSIS — Problem 396
## GPT + Codex Adversarial Review Results
## March 16, 2026

---

## Review Summary

### GPT (7-point review + 2 fatal errors)
- **PASS:** Point 2 (transition matrix), Point 3 (digit split)
- **FAIL:** Point 1 (digit uniformity), Point 4 (CRT), Point 5 (Gillman), Point 6 (medium primes), Point 7 (composition)
- **Fatal Error A:** Sum vs max — need Σ_j ν_p(K-j) ≤ κ_p(K)
- **Fatal Error B:** Threshold not O(1) — ν_p(K-j) unbounded

### Codex (8-claim verification)
- **PASS:** Claims 1, 2, 5, 6 (transition matrix, eigenvalues, digit split, carry decomposition)
- **FAIL:** Claims 3, 4, 7, 8 (stationary start, Gillman constant, CRT, threshold)

### Consensus
Both reviewers confirm the Markov chain STRUCTURE is correct.
Both reviewers identify the APPLICATION errors.

---

## Fatal Error A: Sum vs Max

### The Error
Step 1 stated: κ_p(K) ≥ max_j ν_p(K-j) for all p.
Correct: κ_p(K) ≥ Σ_{j=0}^n ν_p(K-j) for all p.

### Why It Matters
The sum is strictly larger than the max (in general).
For n+1 consecutive integers, Σ ν_p(K-j) ≈ n/(p-1) by Legendre.
This is a FIXED additive cost per prime p.

### The Fix
Within K = r + p^A · m with optimal r (all low digits ≥ (p+1)/2):
- κ_p^{low}(r) = A (every position carries)
- Σ_j ν_p(K-j) = S_low(r) + ν_p(m+δ) where S_low ≤ n/(p-1) + A
- Need: κ_p^{high}(m) ≥ n/(p-1) + ν_p(m+δ)
- Since κ_p^{high} ~ L/2 and n/(p-1) is O_n(1): easily satisfied for large L

### Residual Issue
Can we always find r with all low digits ≥ (p+1)/2 AND in the right Q'-class?
Yes: the set of r with all digits in [(p+1)/2, p-1] has density ((p-1)/2/p)^A ≈ (1/2)^A.
By CRT across the finitely many small primes, such r exist.
But: such r might NOT satisfy p^A | (r-j) for any j, in which case δ doesn't exist
and S_high = 0. This is the GOOD case — no unbounded term.

If p^A | (r-j*) for some j*: need r-j* ≡ 0 (mod p^A), but we also want all digits 
of r ≥ (p+1)/2. This constrains j* to have specific digits. For j* < n < p (when Y ≥ n),
this means r ≡ j* (mod p^A) and the digits of j* in base p are all < n < (p+1)/2.
The low digits of r = j* have digits < (p+1)/2. Contradiction with "all digits ≥ (p+1)/2."

Resolution: If we can't have all-high-digit r AND r ≡ j* (mod p), then there's no 
exceptional j*, so S_high = 0 and the condition simplifies to κ_p^{high} ≥ n/(p-1).
This is the easier case!

If r ≡ j* (mod p) (first digit forced to j* < (p+1)/2): κ_p^{low} = A-1 (one position
doesn't carry). Then need κ_p^{high} ≥ n/(p-1) + 1 + ν_p(m+δ). Still O_n(1) + geometric.

Bottom line: the sum vs max changes constants by n/(p-1) but the argument structure survives.

---

## Fatal Error B: Threshold Unbounded

### The Error
Claimed max_j ν_p(K-j) = O_n(1). False: ν_p(K-j) can be log_p(K).

### The Fix: Carry-Valuation Coupling

Need: κ_p^{high}(m) ≥ C + ν_p(m+δ) where C = n/(p-1) + small constant.

The two random variables are NEARLY INDEPENDENT:
- ν_p(m+δ) depends on LOW digits of m (geometric distribution, mean 1/(p-1))
- κ_p^{high}(m) depends on ALL digits (Markov chain, mean L/2)

Conditional on ν_p(m+δ) = k:
- Bottom k digits of m are determined (all 0 mod p in m+δ)
- The carry process in those k positions is deterministic
- Remaining L-k positions: Markov chain, concentration still works

P(fail) = Σ_k P(ν=k) · P(κ^{high} < C+k | ν=k)
        ≤ Σ_k (1/p^k) · 2·exp(-(L-k)(p-1)/(8p))
        = 2·exp(-L(p-1)/(8p)) · Σ_k (e^{(p-1)/(8p)}/p)^k
        = C_p · exp(-c_p · L)

where C_p = 2/(1 - e^{(p-1)/(8p)}/p) is finite (ratio < 0.37 for p=3, decreasing in p).

### Verification
- p=3: ratio = 0.362, C_3 = 3.14
- p=5: ratio = 0.221, C_5 = 2.57
- p=7: ratio = 0.159, C_7 = 2.38

All convergent. The coupled bound gives exponential decay with only a constant prefactor.

---

## Medium Primes: The New Argument

### The Problem (GPT Point 6)
For Y < p ≤ √K, number of base-p digits L_p is small (possibly 2-3).
Can't get meaningful Markov chain concentration.

### The Solution: Squarefree Sieve + Poisson

**Step 1:** Choose Y ≥ n. Restrict to K where p²∤(K-j) for all p > Y, j ∈ [0,n].
Density: 1 - (n+1)·Σ_{p>Y} 1/p² ≥ 0.98 for Y=100, n=10.

**Step 2:** For p > Y ≥ n dividing K-j*: ν_p(K-j*) = 1 (since p² ∤ (K-j*)).
So Σ_j ν_p(K-j) = 1. Need: κ_p(K) ≥ 1.

**Step 3:** κ_p(K) = 0 iff all base-p digits of K are < ⌈p/2⌉.
Given p | (K-j*) with j* < p, the first base-p digit of K equals j* < (p+1)/2.
So P(κ_p = 0 | p | (K-j*)) = P(all higher digits < ⌈p/2⌉) = (⌈p/2⌉/p)^{L_p-1} ≈ (1/2)^{L_p-1}.

**Step 4:** Events at different primes are independent by CRT.
(Base-p₁ and base-p₂ higher digits of K are independent.)

**Step 5:** Expected number of bad medium primes:
λ = Σ_{p>Y} P(p | some K-j AND κ_p=0)
  ≈ (n+1) · Σ_{k≥2} (1/2)^{k-1} · log((k+1)/k)
  = 0.323 · (n+1)

**Step 6:** By Poisson approximation (independent rare events):
P(zero bad medium primes) ≈ exp(-0.323(n+1)) > 0 for every fixed n.

### Explicit Densities
| n | Expected bad | P(all good) |
|---|---|---|
| 1 | 0.65 | 0.525 |
| 5 | 1.94 | 0.144 |
| 10 | 3.55 | 0.029 |
| 20 | 6.77 | 1.1×10⁻³ |
| 50 | 16.4 | 7.2×10⁻⁸ |

The density is POSITIVE for every fixed n, but exponentially small in n.
This is sufficient for a(n) < ∞ (existence) but gives very large bounds on a(n).

---

## Technical Repairs Needed

### 1. Replace Gillman/Lezaud with direct 2-state computation
The 2-state chain has eigenvalue 1/p. By direct diagonalization:
P(Σ c_i = κ | c_0 = c) = [explicit formula involving (1/p)^L and binomials]
This gives an exact tail bound without needing any Markov chain LDP theorems.

### 2. Digit uniformity (block truncation)
For m ∈ [1, M], the top base-p digit is biased. Fix: truncate to m ∈ [1, p^L] 
(a complete block). The number of m ∈ [1,M] \ [1, p^L] is < p^L < M, so the 
discrepancy is O(p^L/M) → 0. Use complete blocks for exact uniformity, 
then absorb the truncation error.

### 3. CRT independence formalization
For small primes: fix a finite depth D = max(L_p) across p ≤ Y. The carry event
at prime p is determined by m mod p^D. Events at different primes are EXACTLY 
independent by CRT for m uniform mod ∏_{p≤Y} p^D. The interval [1, M] gives
approximate uniformity with discrepancy O(∏p^D / M).

For medium primes: same argument but with D = L_p (small, usually 2-3).
The CRT modulus ∏_{Y<p≤√K} p^{L_p} could be huge, but we only need pairwise
independence (for the Poisson approximation), which is exact by CRT for any 
two distinct primes.

---

## Revised Completeness Assessment

| Component | Status | Confidence |
|---|---|---|
| Step 1 (Kummer, corrected) | ✅ | 95% |
| Step 2 (large primes) | ✅ | 99% |
| Step 3 (upper medium) | ✅ | 99% |
| Step 4 (depth-A + sieve) | ✅ | 90% |
| Step 5 (digit split) | ✅ | 99% |
| Step 6a (small primes, coupled) | ⚠️ | 80% |
| Step 6b (medium primes, Poisson) | ⚠️ | 70% |
| Step 7 (collapse) | ✅ | 95% |
| Overall | ⚠️ | **~75%** |

The 25% uncertainty is split between:
- 15%: CRT independence formalization (might need more work)
- 10%: medium prime argument might have a gap in the Poisson approximation

---

## What to Send for Re-Review

A revised prompt to GPT/Codex that:
1. Uses the SUM condition (not max)
2. Includes the Carry-Valuation Coupling Lemma
3. Includes the squarefree sieve + Poisson argument for medium primes
4. Uses direct 2-state diagonalization (not Gillman)
5. Addresses digit uniformity via block truncation

This should be a single consolidated "Step 6 Theorem" that GPT/Codex can review as a unit.
