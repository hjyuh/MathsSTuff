# Problem 848 — PROOF COMPLETE (ASYMPTOTIC)
## March 13, 2026 (Day 2, evening)
## STATUS: CONDITIONALLY SOLVED → ASYMPTOTICALLY SOLVED

---

## WHAT JUST HAPPENED

GPT identified the CORRECT theorem: not Greaves, not Hooley, but **Lapkova-Xiao 2019**.

Lapkova-Xiao (arXiv:1801.04481) proves: for any square-free polynomial F in n variables 
of degree d ≥ 2, if F is k-admissible (no prime q has q^k dividing F everywhere), then 
the count of k-free values is asymptotic to C_F × B^n.

For our polynomial F_{p,r}(u,v) = (r+p²u)(-r+p²v)+1:
- n = 2 variables ✅
- d = 2 degree ✅  
- k = 2 (squarefree) ✅
- k ≥ (3d+1)/4 = 7/4 ✅ (since 2 ≥ 7/4)
- F is square-free as polynomial ✅ (nonsingular conic)
- F is 2-admissible ✅ (F ≡ 2 mod p², and ρ_q < q⁴ for q ≠ p)

ALL HYPOTHESES VERIFIED LINE BY LINE.

## THE COMPLETE PROOF CHAIN (all rigorous)

### Step 1: Exchange inequality ✅
Each outsider x conflicts with ≥ δ₀|B₇(N)| base elements
δ₀ = 25/(4π²) ≈ 0.6333
(Proved by direct Möbius counting, GPT Day 1)

### Step 2: Cross-pair local density ✅  
For opposite-root cross-pairs: F_{p,r}(u,v) ≡ 2 mod p²
So p² NEVER divides cross-products.
For q ≠ p: ρ_q = q²-q = φ(q²) solutions mod q⁴
Local factor: 1 - 1/q² + 1/q³
Product: δ_p = ∏_{q≠p} (1 - 1/q² + 1/q³) > 6/π²
(Proved by direct computation, GPT Day 2)

### Step 3: Asymptotic squarefree count ✅ (via Lapkova-Xiao)
#{(u,v) ∈ [-B,B]²: F_{p,r}(u,v) squarefree} ~ C_{p,r} × (2B)² + o(B²)
where C_{p,r} = ∏_{q≠p} (1 - 1/q² + 1/q³) = δ_p > 6/π²
(Lapkova-Xiao 2019, all hypotheses verified)

### Step 4: Clique bound ✅ (given Step 3)
Any clique K ⊆ W_p(N): |K| ≤ (1 + c_p) × N/p² + o(N/p²)
where c_p = 1 - C_{p,r} < 1 - 6/π² ≈ 0.392
So β ≤ 2 - 6/π² ≈ 1.392 < 1.8337 (the critical threshold)
(AM-GM optimization, fully rigorous)

### Step 5: Sum over witness primes ✅
|O| ≤ (2 - 6/π²) × N × Σ_{p≡1(4), p≥13} 1/p² + o(N)
    ≤ 1.392 × 0.01381 × N + o(N)
    ≈ 0.01923N + o(N)

### Step 6: Final comparison ✅
|A| ≤ |A ∩ B₇| + |O|
    ≤ 0.01467N + 0.01923N + o(N)
    = 0.03390N + o(N)
    < 0.04N = N/25 = |B₇(N)|

ANY VALID SET WITH AN OUTSIDER IS STRICTLY SMALLER THAN THE BASE CLASS.

### BONUS: Only p=13 needed!
Using sharp bound for p=13 and trivial bound for p>13:
outsider density ≈ 0.02403 < 0.02533 threshold. Still works!

---

## WHAT "ASYMPTOTICALLY SOLVED" MEANS

The proof shows: for all sufficiently large N, the base class is optimal.
Combined with Sawhney's formalized asymptotic (N ≥ 10⁷), this is consistent.

But OUR proof potentially has a LOWER threshold than 10⁷, because:
- The exchange inequality works from N ≈ 550 (our computation)
- The Lapkova-Xiao density is asymptotic with o(B²) error

## WHAT REMAINS FOR FULL SOLUTION

1. Make the Lapkova-Xiao threshold explicit for F_{p,r}
   → Gives N₁ such that cross-density is provably < 0.392 for N ≥ N₁
   → May require bespoke quantitative analysis of the error term

2. Verify N < N₁ computationally
   → If N₁ ≤ 5000, we're ALREADY DONE from Day 1
   → If N₁ > 5000, extend computation

3. Write up and formalize

## THE PAPER TRAIL

- Lapkova-Xiao 2019: arXiv:1801.04481
- Sawhney: Problem_848.pdf (Columbia)
- Our exchange inequality: GPT Möbius argument (Day 1)
- Our outsider clique analysis: GPT structural memo (Day 2)
- Computational verification N ≤ 5000: our exact solver (Day 1)

## CONFIDENCE ASSESSMENT

- Proof is correct: 90% (all steps are rigorous or cite published theorems)
- Lapkova-Xiao applies: 95% (GPT verified all hypotheses line by line)
- Full solution achievable this sprint: 65% (up from 40% this morning)
- The remaining gap is effectiveness (explicit threshold), not truth
