# EP-488 Final Push — Quotient-Core Margin Recursion
# For GPT-5.4 Pro Extended — April 4, 2026
# Attach ep488-final-lemma.tex (the self-contained 3-page doc)

You killed Bonferroni-4 and 2δ > S₁ as universal claims. Both kills are correct. But EP-488 is still true — 23 million sets tested, zero failures.

The surviving framework is YOUR quotient-core margin recursion:

Φ(A) = 2δ_A - S₁(A)
Φ(A) = Φ(A') + (1 - 2δ_{Q_a})/a

where a = min(A), A' = A\{a}, Q_a = prim{b/gcd(a,b) : b ∈ A'}.

You showed Φ can be negative (first 21 primes). But EP-488 doesn't need Φ > 0. It needs G(m) < 2G(n), which is:

δ + D(m mod L)/m < 2(δ + D(n mod L)/n)

i.e. D(m mod L)/m - 2D(n mod L)/n < δ.

The LEFT side is bounded by 3C/n (discrepancy). So EP-488 holds whenever:
3C/n < δ, i.e., n > 3C/δ.

For coprime sets with δ > 1/2: the tail works (n > 6C). For Φ < 0 (your counterexample): δ ≈ 0.874, C ≤ 2^20 ≈ 10^6, horizon ≈ 3×10^6. Finite verification.

But for non-coprime sets where δ < 1/2 AND Φ < 0: both tail arguments fail. The ONLY example is {2p : p ≤ 73} with δ ≈ 0.437. For this set: C ≤ 2^20, horizon ≈ 10^7. Still finitely verifiable.

KEY QUESTION: Is there a primitive set where δ is so small that the horizon 3C/δ exceeds what's computable? This requires small δ and large C simultaneously. But:

- Small δ means SPARSE set (few elements relative to their size)
- Sparse sets satisfy S₁ ≤ 2/min(A), handled by sparse-mass lemma
- Dense sets have δ bounded away from 0

So maybe there's a UNIFORM bound: for all primitive sets, δ > f(k, max(A)) where f is large enough that 3·2^{k-1}/f is manageable?

YOUR TASK: Analyze the recursion Φ(A) = Φ(A') + (1-2δ_{Q_a})/a.

1. When (1-2δ_{Q_a})/a is negative (δ_{Q_a} > 1/2): Φ decreases. How fast? Is |Φ| bounded?

2. Your transfer inequality: Δ_A(n,m) > ρ_Q/a - 3(C_Q+1)/n gives EP-488 for n > 3a(C_Q+1)/ρ_Q. The parameter Λ(Q) = (C_Q+1)/(1-δ_Q). What is Λ for the worst quotient-cores?

3. Your complement halving: ρ_A ≥ ρ_{A'}/2, so 1-δ_A ≥ 2^{-k}. This gives δ_A ≤ 1-2^{-k}. But we need δ BOUNDED AWAY FROM 0, not bounded away from 1.

4. For the scaling counterexample {2p : p ≤ 73}: compute the exact quotient-core Q_4 when peeling off min = 4. What does Q look like? Is it small? Does the transfer inequality give a manageable horizon?

The question isn't "is Φ positive?" anymore. It's "does the transfer lemma chain terminate in a finite computation for every primitive set?" If yes, EP-488 is proved (as a theorem schema indexed by k). If the chain gives computable bounds for EVERY k simultaneously, EP-488 is proved uniformly.

Extended thinking ON.
