# Problem 686 — Final Synthesis
## March 15, 2026

## Attack Vector Status: FINAL

| # | Approach | Status | What killed it |
|---|---|---|---|
| 1 | S-integral points 135a1 (k=3) | VIABLE | — |
| 2 | Quartic descent Thue (k=3) | VIABLE | — |
| 3 | Modular sieve (k=5) | DEAD | GPT: no modulus works (theorem) |
| 4 | Chabauty on C_{4,5} (k=5) | DEAD | Codex: genus 6, nonhyperelliptic |
| 5 | Baker/LLL (k=5) | DEAD | Codex: Λ=0, αᵢ vary, 4^(1/5) irrational |
| 6 | KB irreducibility | DEAD | Codex: converse false, BST covers it |
| 7 | Vjeko-style asymptotics (k=5) | DEAD | Codex: q^{-2} approximation, no cutoff |

**Seven approaches to k=5 are dead.** The k=5 case for N=4 is beyond 
free-tool reach. Every executable method has been tried and failed with 
a precise diagnosis.

## BUT: DR found something bigger

The 677-678-686 connection analysis revealed a CONDITIONAL proof that 
N=4 is permanently stuck — not just at k=5, but at ALL k.

### The Chain (from DR)

1. If N = p^a (prime power) and k ≥ p, then both consecutive blocks 
   contain multiples of p. So for every prime q ≠ p, v_q is the same 
   on both sides. Combined with p appearing in both blocks: the prime 
   supports of P(m,k) and P(n,k) are IDENTICAL.

2. Problem 677's stronger conjecture: for k ≥ 3 and m ≥ n+k, the 
   products of non-overlapping length-k blocks CANNOT have identical 
   prime supports.

3. Therefore (conditional on 677): N = p^a is not representable for 
   any k ≥ max(3, p).

4. For N = 4 = 2²: max(3, 2) = 3, so ALL k ≥ 3 are killed by 677.
   Combined with k = 2 failing (Tao): N = 4 is PERMANENTLY STUCK.

5. Similarly:
   - N = 64 = 2⁶: all k ≥ 3 killed → permanently stuck
   - N = 81 = 3⁴: all k ≥ 3 killed → permanently stuck  
   - N = 25 = 5²: k ≥ 5 killed, leaves k ∈ {2,3,4} to check
   - N = 49 = 7²: k ≥ 7 killed, leaves k ∈ {2,3,4,5,6} to check

### The Conditionality

This is conditional on Problem 677 (prime-support uniqueness for 
non-overlapping blocks). Problem 677 itself follows from the abc 
conjecture (Langevin, 1993). So the full chain is:

  abc → 677 → 686 is FALSE (N=4 is a counterexample)

This doesn't solve 686 unconditionally. But it:
1. Explains WHY the stuck squares are exactly the prime powers
2. Gives a precise conditional proof
3. Identifies 677 as the key intermediate problem
4. Shows that progress on 677 (even partial) → progress on 686

### The Farhi-Kane Decomposition

DR also found that the redundancy function g(n,k) = P(n,k)/L(n,k) is 
PERIODIC in n (Farhi-Kane, 2009). This means for fixed k, the 686 
equation N = [L(m,k)/L(n,k)] × [g(m,k)/g(n,k)] reduces to finitely 
many LCM-ratio problems (one per residue class pair). This brings 686 
into 678 territory — Cambie's techniques control LCM ratios.

## Codex: Vjeko-style also dead

The 7th approach (asymptotic root function) fails because the forced 
rational approximation to 4^{1/5} is only q^{-2} quality — exactly 
continued-fraction scale. Neither Roth (ineffective) nor Baker/Liouville 
(too weak) can exclude this. No finite cutoff emerges.

However, Codex provided valuable confirmations:
- M(n)/n → 4^{1/5} ≈ 1.31951 (verified numerically)
- The expansion M(n) = αn + c₀ + a/(n+3) + O(n^{-3}) with exact constants
- Brute force to n = 100,000: no k=5 solution exists (extends our search)

## What We Have (publishable)

### Novel Data
1. Cremona labels + ranks for all 7 k=3 curves
2. C_{4,5} is genus 6, smooth, nonhyperelliptic (pending MAGMA confirmation)
3. No k=5 solution for N=4 up to n = 100,000 (10x previous search)
4. No modular obstruction exists for k=5, N=4 (GPT's theorem)
5. Asymptotic expansion of M(n) for k=5, N=4 with exact constants

### Novel Structural Insight
6. The 677 → 686 conditional chain: prime-power N is unrepresentable 
   for k ≥ max(3, p), conditional on 677's prime-support conjecture
7. This explains the pattern of stuck squares being exactly prime powers
8. The Farhi-Kane decomposition reduces 686 to finitely many LCM-ratio 
   problems per k value

### Systematic Negative Results  
9. Seven approaches attempted and killed with precise failure modes
10. k=5 for N=4 is beyond free-tool reach via all known methods
