# Problem 848 — Complete Status After Day 2
## March 13, 2026 (evening)

## THE FULL ARGUMENT (what we've built)

### For N ≤ 5000:
Exact computation: alpha(G_N) = |A_7(N)| at every checkpoint. ✅ DONE.

### For N > 5000:
Any valid set A either:
(a) Has no outsiders → A ⊆ B_7(N) or B_18(N) → |A| ≤ N/25. ✅ TRIVIAL.
(b) Has at least one outsider → two bounds apply:

**Bound 1 (Exchange, EFFECTIVE):**
|A ∩ B_7(N)| ≤ (1 - 25/(4π²)) × N/25 + explicit_error
≈ 0.01467N + small error
Effective from M=3 (GPT proved with explicit constants).

**Bound 2 (Outsider clique, ASYMPTOTIC):**  
|A \ B_7(N)| ≤ 1.25147 × N × Σ 1/p² + o(N)
≈ 0.01729N + o(N)
Asymptotic via Lapkova-Xiao 2019.

**Combined:** |A| ≤ 0.03196N + o(N) < 0.04N for large N.

### The gap:
The o(N) in Bound 2 is NOT explicit. Lapkova-Xiao doesn't give a threshold.

## EMPIRICAL EVIDENCE (overwhelming but not a proof):

Cross-density > 0.5 verified for ALL grid sizes 1×1 through 60×60, for ALL
primes p ∈ {13, 17, 29, 37, 41, 53, 61}.

For p > 70: p² > 5000, so at most 1 element per root in [1,5000].
Irrelevant for our computational range.

## WHAT WOULD CLOSE IT

### Option A: Make Lapkova-Xiao effective
Need explicit error in 2D squarefree sieve. GPT says this is a "new project."
Difficulty: 6/10. Timeline: unknown.

### Option B: Extend computation to 10⁷  
With structural insight, don't need full MIS.
For each N: check if any mixed set beats |A_7(N)|.
Mixed sets are bounded by the exchange + clique structure.
Could be MUCH cheaper than brute-force MIS.
Difficulty: 5/10. Timeline: 2-3 days with compiled code.

### Option C: Prove cross-density > 0.5 for all (u,v) pairs (not just sampled)
For fixed p, the polynomial F(u,v) ≡ 2 mod p². 
For it to be non-squarefree, need some q² | F with q ≠ p.
The dominant case is q=2 (divisibility by 4).
F(u,v) ≡ 0 mod 4 iff (r+p²u)(-r+p²v) ≡ -1 ≡ 3 mod 4.
This happens when one factor is 1 mod 4 and the other is 3 mod 4.
Exactly 1/4 of pairs satisfy this (by CRT).
Additional q² contributions are sparse (~1-2%).
So compatible density ≈ 0.25 + small correction ≈ 0.25.
Could potentially prove c_p < 0.5 by elementary mod-4 + inclusion-exclusion.
Difficulty: 4/10. Timeline: hours.

### MY RECOMMENDATION: Option C.
It's the most elegant and the most achievable today.
