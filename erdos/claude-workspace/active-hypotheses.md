# Active Hypotheses — What I Actually Think
## Updated: March 13, 2026

---

## Problem 848

### My core belief:
The exchange inequality IS the right approach, and the explicit constant C 
is probably small enough that N₀ < 5000. Here's why I believe this despite 
GPT saying "no plug-and-play K exists":

The empirical data is TOO clean. Alpha = A7 at EVERY checkpoint through 5000.
Not "usually equal" — EXACTLY equal. Every single time. And the worst outsider 
conflict rate GPT found was 55% (x=349 at N=5000). That's already well above 
the 50% threshold needed. The asymptotic density is 6/π² ≈ 60.8%.

If the conflict rate is already 55% at the WORST case at N=5000, and converging 
toward 60.8%, the crossover from "not enough" to "enough" happened long before 
N=5000. I suspect the exchange inequality is effective from N ≈ 100-200.

### What I think the solution looks like:
NOT the full GPT 6-phase plan (too complex). Instead:

1. Prove the explicit outsider-conflict by DIRECT Möbius counting, not by 
   citing Hooley/Nunes. The progression 25xm + (7x+1) is a SPECIFIC linear 
   form. For a specific linear form, the squarefree count is:
   
   Σ_{d²|n, n≡a mod q} μ(d) = (6/π²) × correction × N/q + error
   
   The correction is ∏_{p|q} (1-1/p²)^{-1} which is COMPUTABLE.
   The error for a specific linear form with q < N^{1/2} should be O(√N).
   
   I think a direct Möbius argument gives C ≤ 10 or even C ≤ 5.
   Then N₀ = (25C/0.108)² which for C=10 gives N₀ ≈ 535,000.
   Still too big for our Python script but reachable with Rust.

2. BUT there might be a shortcut I haven't seen GPT explore:
   What if instead of making the error term explicit for ALL outsiders,
   we prove that outsiders from SPECIFIC residue classes mod 25 have 
   guaranteed conflict rates? There are only 24 non-base residue classes.
   If we can handle each one with a separate (easy) argument, we bypass 
   the need for a uniform constant entirely.

### What I was WRONG about yesterday:
- The pure mod-25 classification (Task B) fails because admissible density 
  is 10.5%, not 4%. I underestimated contributions from p=13, 17, 29, etc.
- Mixed sets DO exist ({7, 41} is valid). But they never BEAT the pure class.
- The problem is harder than 3/10. More like 5-6/10 honestly.

### My confidence that 848 is solvable this sprint: 60%

---

## Problem 686

### My core belief:
N=4 is unrepresentable for ALL k ≥ 2, and the proof for k≥5 is achievable 
via a Stirling + Sylvester argument. Here's my reasoning:

For large k, the equation ∏(m+i) = 4·∏(n+i) with m ≥ n+k forces:
- m/n ≈ 4^{1/k} → 1 as k → ∞
- m - n ≥ k (disjointness)
- Therefore n ≈ k/(4^{1/k} - 1) ≈ k²/(2ln4) ≈ k²/2.77

At this scale (n ≈ k²/3), the products have ~k log k distinct prime factors.
The ratio is exactly 4 = 2². So the p-adic valuations must match for ALL 
primes except p=2, where v₂(LHS) = v₂(RHS) + 2.

For p ≥ 3: v_p(∏(m+i)) = v_p(∏(n+i)). Both products contain ~k/p multiples 
of p. For the valuations to match exactly, the distribution of p-powers must 
be identical across both blocks. But the blocks are shifted by d = m-n ≥ k,
so the multiples of p in each block are in different positions.

I think for k ≥ some small K₀ (maybe 5 or 6), the number of prime constraints 
exceeds the degrees of freedom (only 2: m and n), making solutions impossible.

### What I'm less sure about:
Whether the k≥5 argument can be made UNIFORM or needs case-by-case checking.
If K₀ = 5, we need k=5 specifically. If K₀ = 10, we need k=5,6,7,8,9 individually.
Each fixed k is a Faltings/Siegel curve — finitely many solutions, checkable.

### The formalization gap:
Bennett's irrationality measure for ∛2 is NOT in Mathlib. This blocks k=3 
formalization. Codex couldn't get around it. Options:
a) Axiomatize Bennett's bound and isolate the sorry to one statement
b) Use Aristotle (queued but no result yet)
c) Skip k=3 formalization for now, prove k≥5 bound instead

### My confidence that 686 is disprovable this sprint: 50%

---

## Problem 701 (NEW — intersecting family)

### My hypothesis (before reading the problem):
The fact that 0 comments exist and it shares tags with a $500-prize solved 
problem suggests either:
a) Nobody has looked at it (opportunity)
b) People looked and it's obviously hard (risk)

The pattern from 388 (solved neighbor technique transfers to open problem) 
worked once. If the intersecting family techniques are generic enough to 
transfer, this could be a quick win. If they're problem-specific, it's a dead end.

### My confidence: unknown (need to read the problem first)

---

## Problem 931

### My belief about Level 3:
I genuinely think the CRT-based assignment rigidity argument I described 
on Day 1 is the right FRAMEWORK, even though neither GPT nor I could close it.

The key insight I had: each large prime p tagged to position i in the first 
block gives a congruence d ≡ i-j (mod p) on the gap. Multiple primes give 
multiple congruences. CRT pins d modulo a growing product.

Where it fails: pinning d doesn't kill d unless the product of primes exceeds 
d itself. And d can be as large as n₂ ≈ n₁^{k₁/k₂}, which grows faster than 
the CRT modulus for small numbers of primes.

But I still think this is the right direction. Someone with more analytic NT 
background might see how to close the gap.

### My confidence that 931 is solvable this sprint: 10%

---

## Problem 388 Theorem 2

### My belief:
GPT's deep research was right — current unconditional tools are insufficient.
The gap between P(n,k) > ck₂ (Laishram-Shorey) and P(n,k) > m₁+k₁ (what we need) 
is not closable with existing technology.

But I think the problem is "almost solved" in the sense that ONE new theorem 
about prime factors of consecutive integers at polynomial scales would close it.
That theorem doesn't exist yet. It might exist in 5 years.

### My confidence that 388 is fully solvable this sprint: 5%
