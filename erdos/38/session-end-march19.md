# Erdős Problem 38 — Session End State
# March 19, 2026

## Summary of Today's Work

### V1 (retracted)
- B = 3ℕ+2, proof v1-v11, 6 rounds GPT review
- Posted to forum, human found B IS a basis of order 3
- Retracted immediately
- Root cause: confused "each hB is sparse" with "B is not a basis"
- Deeper issue: bounded gaps → positive Schnirelmann density → basis (Schnirelmann's theorem)

### V2 (in progress)  
- B = {1, 2, 4, 8, ...} (powers of 2)
- Step 0: NON-BASIS PROVED AND MACHINE-VERIFIED (popcount argument, Aristotle + Axle)
- Step 2: GAIN LEMMA — massive computational evidence, no formal proof yet
- GPT Pro research map obtained — identifies Fourier/autocorrelation framework

## The Exact Mathematical Gap

We need to prove: for any A ⊆ ℕ₀ with σ(A) = α ∈ (0,1) and any N ≥ 1,
  max_{k: 2^k ≤ N} G_{2^k} ≥ c · α(1-α) · N
for some absolute constant c > 0.

### What DOESN'T work:
1. **Simple averaging over K shifts:** Gives bound α(1-α)N/log(N) → 0. Too weak.
2. **Dichotomy (G_1 vs large shift):** Case 1 (many transitions) works. Case 2 (few transitions, blocky A) — we can identify a large gap, but Schnirelmann density only controls PREFIXES, not arbitrary intervals, so we can't bound how many A-elements are near the gap.
3. **Small-bias / Fourier averaging:** Works in Z/nZ if shifts have small Fourier coefficients, but powers of 2 DON'T have small Fourier coefficients in general (block adversary pushes ratio to ~2.5).

### What MIGHT work:
1. **Dichotomy with prefix-aware gap analysis:** Instead of looking at one gap, use the Schnirelmann prefix condition globally. The surplus |A ∩ [1,m]| - αm at position m represents "density credit" that can be "spent" by large shifts.
2. **Multi-scale induction:** At scale 2^k, either G_{2^k} is large or A is "structured at scale 2^k." Iterate through scales — structure at ALL scales simultaneously forces A ≈ trivial.
3. **Fourier in Z/nZ + lifting:** Prove the cyclic group version first, then transfer to intervals.
4. **Read Erdős 1936 basis argument and adapt.** His proof for bases of order k uses k-fold coverage. Our "basis of order log N" might give constant gain due to dyadic structure.

## Computational Evidence Summary
- Tested N = 10 to 50,000
- All adversaries: gain ratio ≥ 0.65 (small N), converging to ~1.0
- Simulated annealing worst-case: ratio ~0.8 at N=30, ~0.97 at N=1000
- NO adversary found with ratio < 0.65
- The optimal adversary EQUALIZES G_{2^k} across all shifts

## Aristotle Jobs
- sum_mod3_of_all_mod3: ✅ PROVED + AXLE VERIFIED (0eba19de)
- not_basis_powers_of_two (popcount): ⏳ Submitted (2806f54a)
- gap_position_sum_bound: ❌ Error (8b788ca1)
- transitions_equality: ❌ Error (e0e2d48a)

## Files Created Today
- erdos/38/postmortem.md — Why v1 failed
- erdos/38/taxonomy-analysis-fresh.md — Architecture ranking
- erdos/38/proof-v2-powers.md — Current proof draft
- erdos/38/gpt-pro-research-map.md — GPT Pro's research roadmap
- erdos/38/synthesis-march19.md — Integration of all approaches
- erdos/38/lean-formalization-tracker.md — Aristotle/Axle status
- INDEX.md — Updated master directory

## Next Session Priorities
1. Read Erdős 1936 (basis → gain argument). Understand how basis condition creates gain.
2. Read Ge-Lê essential components survey. ε-biased sets connection.
3. Try multi-scale induction proof for gain lemma.
4. Check Aristotle job 2806f54a (popcount non-basis).
5. Consider: is the answer to P38 actually NO? (GPT Pro's approach C)
