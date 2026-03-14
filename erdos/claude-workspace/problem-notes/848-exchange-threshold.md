# Problem 848 — Exchange Inequality Threshold Data
## Computed: March 13, 2026 (Day 2)

## KEY RESULT

From N = 550 onward (at least through N = 1500), ALL outsiders have 
conflict rate ≥ 50% against the base class {7 mod 25}.

Last problematic N: 525 (x=205 has rate 47.6%, i.e., 10/21)

Combined with computational verification through N = 5000:
- For N ≤ 5000: alpha = A7 verified by exact computation
- For N ≥ 550: exchange inequality empirically holds (all outsiders > 50%)

The overlap [550, 5000] means: IF we can prove the exchange inequality 
implies optimality of the base class for N ≥ 550, we're done by combining 
with the computation.

## IMPORTANT CAVEAT (realized during computation)

The exchange inequality (outsider x conflicts with ≥ 50% of base class)
does NOT by itself prove the base class is optimal. Here's why:

Suppose outsider x conflicts with 50% of base class (half the base elements 
can't coexist with x). If we add x and remove those 50% of base elements,
we could potentially fill the gaps with OTHER outsiders.

The admissible density is ~10.5%, so there are ~0.105N potential outsiders.
Even with 50% of base removed, we have:
  0.5 × N/25 + 0.105N = 0.02N + 0.105N = 0.125N > N/25 = 0.04N

So the exchange inequality for ONE outsider doesn't kill the possibility of 
a large mixed set. You need OUTSIDER-OUTSIDER constraints too.

THIS IS EXACTLY GPT'S BLOCKER 2.

## WHAT THE DATA IS STILL GOOD FOR

1. It confirms the exchange inequality is REAL at finite N (not just asymptotic)
2. It identifies the exact threshold (N ≈ 550) where it kicks in
3. It identifies the worst-case outsiders (x=205, x=173, x=95, x=311)
4. It provides empirical grounding for any theoretical argument

## PROBLEMATIC OUTSIDERS

| x | x mod 25 | Worst rate seen | At N |
|---|----------|----------------|------|
| 205 | 5 | 0.4762 | 525 |
| 173 | 23 | 0.3333 | 225 |
| 95 | 20 | 0.2500 | 100 |
| 311 | 11 | 0.5500 | 1000 |

x=173 is especially bad at small N because 173 ≡ 23 mod 25, and the 
progression 173(25m+7)+1 = 4325m+1212 starts with few terms.
At N=225: only 9 base elements, and 173×7+1=1212=2²×303 (not squarefree),
173×32+1=5537 (squarefree), 173×57+1=9862=2×4931 (squarefree), etc.
3/9 = 0.333 — but the non-squarefree fraction is just bad luck at small scale.

## NEXT STEPS

1. Wait for GPT's explicit error bound on the worst-case progression
2. The real question for GPT: given the exchange inequality PLUS the 
   Sawhney asymptotic stability, can we combine them to get a finite threshold?
3. The computation shows the exchange works from N=550. The Sawhney 
   asymptotic works from N=10⁷. Is there a way to bridge [550, 10⁷]?
