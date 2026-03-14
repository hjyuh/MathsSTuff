# Open Questions — Things I Want To Investigate
## Updated: March 13, 2026

---

## HIGH PRIORITY (today/tomorrow)

### Q1: What is the maximum number of outsiders in any extremal set for 848?
Our computation verified N ≤ 5000 with alpha = A7, but we only checked 
alpha, not the STRUCTURE of the extremal sets. After N = 82, every witness 
was a pure class. But is that because pure classes are the ONLY extremal 
sets, or because the solver happens to find them first?

HOW TO CHECK: re-run erdos848_exact_small.py with --show-witness and look 
for ANY witness that isn't purely {7 mod 25} or {18 mod 25} after N = 82.
From Day 1 data: last mixed witness was at N=82. Need to confirm this holds.

### Q2: For 686 k≥5, what happens with Sylvester's theorem specifically?
For the upper block ∏(m+i) with k terms starting at m+1 > k, Sylvester says 
there's a prime p > k dividing the product. For N=4, we need this prime to 
appear in the lower block too. Since the lower block starts at n+1 < m+1-k,
the prime p > k must divide some n+j where n+j < m+1. This is possible only 
if p ≤ n+k. So we need: the largest prime factor of the upper block is ≤ n+k.
But Sylvester gives p > k. Is p > n+k possible? Only if p divides ONLY the 
upper block. The equation says ∏(m+i) = 4·∏(n+i), so every prime in the upper 
block must be in the lower block (with appropriate multiplicity). Wait — no.
The prime could come from the factor of 4 = 2². Only p=2 is special.
For p ≥ 3: v_p(∏(m+i)) = v_p(∏(n+i)). So any p dividing the upper block 
MUST divide the lower block too. But if p > n+k, it can't divide any n+j.
So p ≤ n+k. Combined with p > k and n ≈ k²/3, we get k < p ≤ k²/3 + k.
This IS satisfiable. So Sylvester alone doesn't kill k≥5.
NEED STRONGER ARGUMENT.

### Q3: For 848, can the 24 non-base residue classes mod 25 be handled individually?
Instead of a uniform constant C for ALL outsiders, handle each residue class 
r ∈ {0,1,...,6,8,...,17,19,...,24} separately. For each r, compute the local 
squarefree density of the progression r(25m+7)+1. If EVERY class has density 
> 1/2, the exchange inequality works class-by-class. No uniform theorem needed.
This is 24 separate computations, each straightforward.

### Q4: What is Problem 701 actually asking?
Haven't read it yet. Need to check erdosproblems.com/701.

## MEDIUM PRIORITY (this sprint)

### Q5: Can the 848 exchange inequality be proved WITHOUT Hooley?
GPT used Hooley/Nunes for the squarefree-in-AP estimate. But for a SPECIFIC 
linear form ax+b, the squarefree count is just Σ_{d²|ax+b} μ(d), summed over 
x in range. This can be bounded by elementary inclusion-exclusion over primes 
up to √(aN+b). For small moduli (q=25x with x < N), this might give an 
explicit and TIGHT error term without any deep analytic input.

### Q6: Is there a k=4 → k=2 reduction that works in Lean?
Natso showed this on the forum. Can it be formalized? The key step is a 
quadratic substitution. If yes, k=4 is immediately done for 686.

### Q7: For the intersecting family problems (701), what is the $500 technique?
Problem 21 carried a $500 prize and shares tags with 701. Understanding 
WHY Problem 21 was hard (and what solved it) is the key to 701.

## LOW PRIORITY (future)

### Q8: Is there a META-technique for the "effective vs asymptotic" gap?
Connection 7 in cross-connections.md notes this gap appears in 848, 388, 931, 
and 686. All have the same structure: fixed-parameter finiteness exists, 
uniform finiteness doesn't. Is there a general method for bridging this?

### Q9: Can the 931 CRT argument be saved?
My Day 1 hypothesis about CRT constraints from prime assignments felt right 
but couldn't be closed. Is there a way to make the CRT modulus grow faster 
than the gap d? Maybe by using the MULTIPLICATIVE structure of the primes 
(not just their count) to boost the modulus.

### Q10: What other Formal Conjectures sorry's are low-hanging?
The scouting report identified 786 and 699 as having "research solved" sorry's 
for classical theorems. These are the same type of work we did on Day 1 
(formalize known results). Could bank more theorems quickly.
