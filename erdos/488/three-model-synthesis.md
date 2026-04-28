# EP-488: Three-Model Synthesis — April 2, 2026

## Models Used
- GPT-5.4 xhigh (Codex): First Plateau Lemma, full context
- GPT-5.4 Pro extended: First Plateau Lemma, fresh context  
- GPT-5.2 Pro extended: Post-Peak Bound (Lemma 2), fresh context

## Key Results

### Corrections to Two-Lemma Strategy
1. First Plateau Lemma has THIN-REGIME counterexamples: (a=3,k=3,t=2) etc.
   Must restrict to wide regime t > 2√a (thin already proved separately).
2. Post-peak constant c₀ = 3/5 is NOT universal: (3,3,2) gives 0.6071 > 0.6.
   Need c₀ ∈ (0.6072, 2/3). Target c₀ = 5/8 = 0.625.

### Convergent Discovery: Window Lemma (W)
BOTH GPT-5.4 models independently reduced the first plateau to the SAME statement:

**Window Lemma (W):** For B = {ka+1,...,ka+t}, every interval of length 2ka 
below a(ka+1) contains at least t integers divisible by some element of B.

Equivalently: U(x+2ka) - U(x) ≥ t for all x < a(ka+1) - 2ka.

Stronger version (also survives computationally through a ≤ 41):
For any consecutive C ⊆ B, every interval of length 2ka contains at least |C| multiples from C.

### Proved: Base Strip
Both models independently proved: G(n) ≥ β for all 2ka-1 ≤ n ≤ 4ka-1.
Two different proofs, same result. This is now a theorem.

### Why Window Lemma (W) Closes the First Plateau
If (W) holds, then F(x+2ka) - F(x) ≥ 2k + t (anchor contributes 2k, block contributes t).
So H(x+2ka) - H(x) ≥ 2k + t - 2ka·β = (2k(a-1)-t)/(2ka-1) > 0.
Combined with base strip H(n) ≥ 0, induction gives H(n) ≥ 0 for all n < a(ka+1).
Combined with m* < a(ka+1) (computationally verified), first plateau is done.

### Collision Structure (from Codex)
Layers u and v can only collide if u > k(v-u). So only nearby layers collide.
Exact pair-overlap formula:
|uB ∩ vB| = max(0, floor((ka+t)/(v/g)) - floor(ka/(u/g))), g = gcd(u,v).

Dip monotonicity is FALSE: in (167,2,166), dip at 6a-1 is higher than at 7a-1.
So the proof cannot use "later dips are always shallower."

### Post-Peak Analysis (from GPT-5.2)
- Any 6/5 rebound forces local density d(n,m) ≥ G(n)(6/5 + n/(5L))
- Raw capacity bound gives ceiling ≈ 0.5, threshold ≈ 0.405 — too weak alone
- Needs sharper window bounds accounting for overlaps in B
- "Record peaks are immediately before gaps" — structural handle

## Three-Lemma Endgame (Revised)

### Lemma 1 (Window Lemma W)
For wide regime (t > 2√a): every interval of length 2ka below a(ka+1) 
contains at least t B-multiples.
Status: Computationally verified (a ≤ 41), unproved.

### Lemma 2 (Post-Peak Bound)  
sup_{n ≥ m*} E(n)/(2G(n)) ≤ 5/8 for wide one-anchor families.
Status: Computationally strong (worst observed 0.5984), unproved.
Note: need finite check for small a where c₀ = 3/5 fails.

### Lemma 3 (Finite Verification)
For small a (a ≤ some bound), verify EP-488 by direct computation.
Handles thin-regime first-plateau counterexamples and small post-peak exceptions.

## Computational Verification Summary
- 3402 families for first plateau (a ≤ 101, k ∈ {2,3,4})
- Window Lemma (W) verified through a ≤ 41
- Post-peak bound verified through a ≤ 199
- Zero EP-488 failures in any scan

## What Failed
- Dip monotonicity: FALSE
- G(n) ≥ α_A/2 as universal theorem: cannot work asymptotically (Ford)
- Raw minus pair overlaps: triple overlaps already appear
- Hall/SDR matching: too strong, fails even when union is large
- Per-anchor-interval lower bounds: increments can be 0

## Next Target
Prove Window Lemma (W). This is a pure combinatorial statement about 
consecutive integers in short intervals. No Ford, no sieves, no asymptotics.
The consecutive-subblock strengthening might be the right induction handle.
