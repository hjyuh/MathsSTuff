# Problem 848 — GPT's Full Solution Roadmap
## March 12, 2026 (late evening)

## THE KEY INSIGHT

The central obstacle is NOT "check 400,000 cases."
It is: "How do you turn asymptotic stability into an explicit exchange inequality?"

## THE CANDIDATE KEY LEMMA (Route 1)

"There exists explicit c > 0 and N₁ such that for every N ≥ N₁, every x < N with 
x ≢ 7 (mod 25), the number of y < N with y ≡ 7 (mod 25) and xy+1 squarefree 
is at least cN."

If proved: one outsider kills ~cN base-class elements. Since adding one outsider 
only gains +1 but loses ~cN, no outsider can help. Pure class wins.

## SIX ROUTES RANKED

1. **Outsider-cost exchange lemma** (MOST PROMISING)
   - Prove outsiders conflict with positive fraction of base class
   - Squarefree density in arithmetic progressions
   
2. **Bounded-defect theorem + finite certification**
   - Prove near-extremal sets differ from principal class by ≤ D elements
   - Search only defect patterns, not full graph
   
3. **Residue-density optimization** (SUPPORT)
   - 25-variable LP over residue classes
   - Shows global structure but only asymptotic

4. **Witness-prime rigidity** (SIDE LEMMAS)
   - Most pairs in large valid sets use p=5
   - Larger primes too sparse to sustain large cliques

5. **Lower the analytic threshold** 
   - Push N₀ from 10⁷ to 10⁶ or lower
   - Makes finite check easier but doesn't eliminate it

6. **Structured finite certification**
   - Not raw max-clique — bounded-defect search
   - Depends on Route 2 succeeding first

## THE SOLUTION SHAPE

Theorem A: Near-extremal sets are close to a principal class (stability)
Theorem B: Exchange inequality kills outsiders for N ≥ N₂  
Corollary: Extremal = principal class for N ≥ max(N₁, N₂)
Finite check: Verify N < max(N₁, N₂)

## WHAT TO DO TOMORROW

Priority 1: Attack the candidate key lemma (Route 1)
- Prove: for x ≢ 7 mod 25, positive proportion of y ≡ 7 mod 25 have xy+1 squarefree
- This is a squarefree-in-AP result
- Literature: Prachar, Hooley, Heath-Brown on squarefree values of polynomials

Priority 2: Run the exact small verifier to find crossover point
- python erdos848_exact_small.py 500 --show-witness
- Determines where A₇ permanently leads

Priority 3: If Route 1 works, determine N₁ and do the small finite check
