# Problem 848 — GPT Outsider Clique Analysis (MAJOR UPDATE)
## March 13, 2026 (Day 2, afternoon)

## GPT'S VERDICT: Strategy is sound. Specific N/169 bound is wrong. Weaker bound suffices.

### What GPT CORRECTED:
- My claim "outsider cliques live in one 13² progression" is FALSE
- Example: {41, 70, 239} are mutually compatible but from DIFFERENT prime families
  - 41²+1 divisible by 29², 70²+1 and 239²+1 divisible by 13²
  - All cross-products are non-squarefree
- So outsider cliques CAN mix different p²-classes

### What GPT CONFIRMED:
- The mixed-set strategy IS sound
- We DON'T need |O| ≤ N/169. That's stronger than necessary.
- We ONLY need: outsider clique density < 0.02533
- Because: mixed set ≤ (1-δ₀)(N/25) + |O|, and to beat N/25 need |O| ≥ δ₀(N/25) ≈ 0.02533N

### What GPT BELIEVES is true:
Outsider clique density ≤ Σ_{p≡1(4), p≥13} 1/p² + o(1) ≈ 0.01381

This is FAR below the 0.02533 threshold (by almost factor 2).

### THE PROOF STRUCTURE GPT OUTLINED:
1. Partition outsiders by "witness prime" p: each outsider a has p² | a²+1
2. For each prime p, outsider lives in one of 2 root classes mod p²
3. Prove: same-prime, opposite-root exclusion (can't have linear-size sets from both roots)
4. Prove: different-prime exclusion (can't have large bipartite compatibility across primes)  
5. Sum surviving one-class-per-prime densities: Σ 1/p² ≈ 0.01381
6. Combine with exchange inequality: 0.01467N + 0.01381N = 0.02848N < 0.04N = N/25

### THE KEY INEQUALITY:
(1 - δ₀)(N/25) + c_out × N < N/25
⟺ c_out < δ₀/25 ≈ 0.02533

GPT's predicted c_out ≈ 0.01381 << 0.02533. HUGE margin.

### WHAT'S LEFT TO PROVE:
The outsider-clique stability theorem:
"For every pair of outsider residue classes (R,S) that are not the same root class 
modulo the same p², any complete bipartite compatible set has min(|X|,|Y|) = o(N)."

This is the FINAL BOSS of Problem 848.

### WHAT THIS MEANS:
If GPT can prove the outsider-clique density bound, 848 is SOLVED for large N.
Combined with computation for small N (we have N ≤ 5000), and making the 
exchange + clique bounds effective, the problem closes WITHOUT computing to 10⁷.

848 has been reduced from "verify 10 million cases" to "prove one density theorem 
about outsider cliques."
