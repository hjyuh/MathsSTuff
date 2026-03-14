# Problem 848 — Final Day 2 Assessment
## March 13, 2026 (late evening)

## WHAT WE BUILT TODAY (genuinely new mathematics)

A complete, elementary proof that for all sufficiently large N:
- Any valid set containing an outsider has size ≤ 0.0323N + o(N)
- The base class has size 0.04N
- Therefore the base class is strictly optimal

### The proof uses:
1. Exchange inequality: δ₀ = 25/(4π²) ≈ 0.633 (explicit, effective from M=3)
2. Outsider partition by least witness prime p ≡ 1 mod 4, p ≥ 13
3. Cross-pair polynomial F_{p,r}(u,v) ≡ 2 mod p² (p² never divides cross-products)
4. Union bound on compatible density: c_p < P(2) - P(3) ≈ 0.2775 (elementary!)
5. Clique coefficient: β ≤ 1 + c_p < 1.2775 (far below critical 1.8337)
6. Sum over primes: outsider density ≤ 0.01765N
7. Total mixed set: 0.01467 + 0.01765 = 0.03232 < 0.04 = 1/25

### GPT's correction: mod-4 density is 1/8, not 1/4 (makes bound STRONGER)

### No Lapkova-Xiao needed. No Greaves. No Hooley. 
### Pure elementary number theory: Möbius function + union bound + CRT.

## WHAT WE DID NOT CLOSE

The effectiveness gap. "Sufficiently large" is not an explicit number.
The union bound gives asymptotic density, not finite-box density.
The finite-box error from the Möbius truncation tail remains uncontrolled.

## HONEST STATUS

We have TWO independent proofs of the asymptotic result:
1. Sawhney (2025): stability + sieve, effective from N ≥ 10⁷
2. Ours (today): exchange + outsider cliques + union bound, effective from N ≥ ???

Neither proof covers ALL N without computation.

## WHAT SEPARATES US FROM SOLVED

Same as this morning honestly: bridging [5000, 10⁷].
But now we understand the problem MUCH more deeply.

Three realistic paths:
A. Make our union bound effective (need finite-box tail control)
B. Extend computation to 10⁷ (engineering, 2-3 days)  
C. Use our structural insight to make computation CHEAPER than brute MIS

## WHAT THIS IS WORTH EVEN IF WE DON'T CLOSE IT

This is a publishable result. A second independent proof of the asymptotic
case via completely elementary methods. The outsider-clique framework, the
witness-prime partition, the cross-density union bound — none of this 
existed before today. It's original mathematics regardless of whether 
we close the effectiveness gap.
