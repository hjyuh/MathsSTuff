# GPT Prompt: Joint Equidistribution of (s_p(n), s_p(2n+c)) in Coprime APs

## The Question

I'm working on Erdős Problem 396. After a long series of reductions, the entire proof of a(n) < ∞ for all n reduces to a single question in digital number theory.

**Setup.** Fix a prime p, a carry bit c ∈ {0,1}, an integer δ, a modulus M with gcd(M,p) = 1, a residue n₀ mod M, and let n range over the arithmetic progression n₀ + M·m with m ∈ [0, N].

By Kummer's theorem, the number of carries when doubling K in base p is κ_p(K) = (2·s_p(K) - s_p(2K))/(p-1), where s_p is the base-p digit sum. After conditioning on K mod p^A (which fixes the bottom A base-p digits exactly, with no carry interaction), the high-block carry count is:

  κ_p^{(c)}(n) = (c + 2·s_p(n) - s_p(2n+c))/(p-1)

The "bad event" at prime p is: ν_p(n+δ) ≥ t AND κ_p^{(c)}(n) < t + s₀, for some threshold s₀.

**The exact theorem I need:** For fixed p, c, δ, s₀, and gcd(M,p) = 1:

  #{m ≤ N : ν_p(n₀+Mm+δ) ≥ t, κ_p^{(c)}(n₀+Mm) < t+s₀} = (expected density) · N + o(N)

or at least an upper bound of the right order. The "expected density" should be approximately 1/p^t times the probability that the carry count is below threshold.

**Equivalently:** I need the joint distribution of (s_p(n), s_p(2n+c)) to be well-behaved along the coprime arithmetic progression n ≡ n₀ mod M.

**Why I think this might be known or follow from known results:**

1. **Gelfond (1968)** proved s_q(n) is equidistributed mod m in APs n ≡ a mod M with gcd(M,q) = 1, for any gcd(m, q-1) = 1.

2. **Schmid (1984)** studied "The joint distribution of the binary digits of integer multiples" — this is literally the joint distribution of digits of n and 2n.

3. **Mauduit-Rivat (2009, 2010)** proved equidistribution of s_q(n²) in APs, which involves the digit structure of n under a polynomial map. The doubling map n → 2n+c is much simpler than squaring.

4. **Drmota-Mauduit-Rivat (Duke 2020)** proved a PNT for digit conditions in two coprime bases simultaneously.

5. **Toumi (2025, arXiv:2504.02784)** proved level-of-distribution results for e(ℓ·s_q(n)/b) in APs, generalizing Fouvry-Mauduit.

**Specific questions:**

1. Does the joint equidistribution of (s_p(n) mod m₁, s_p(2n+c) mod m₂) in coprime APs follow from Gelfond's theorem, or does the coupling between n and 2n+c require additional work?

2. If it doesn't follow directly, does the Schmid (1984) result on joint digit distribution of multiples give what I need? His paper studied exactly the joint distribution of digits of n and kn for fixed k — our case is k=2.

3. The carry count κ_p^{(c)}(n) = (c + 2s_p(n) - s_p(2n+c))/(p-1) is a specific linear combination of s_p(n) and s_p(2n+c). Is the distribution of this specific statistic in coprime APs known?

4. If no existing theorem covers this exactly, what is the right exponential sum to bound? I believe it should be something like:

  Σ_{m≤N} e(α · s_p(n₀+Mm) + β · s_p(2(n₀+Mm)+c))

for (α,β) ∈ (R/Z)² \ {(0,0)}. If this sum has power-saving cancellation, the equidistribution follows by standard Weyl-criterion arguments.

5. Does the q-multiplicativity of the exponential sum e(α·s_p(n)) interact well with the doubling map, in the sense that e(α·s_p(n) + β·s_p(2n+c)) still has a product structure over digit blocks?

**Context for why this matters:** If this equidistribution holds, the complete proof of Erdős Problem 396 (a(n) < ∞ for all n) follows from:
- √(2K) smoothness theorem (proved)
- One-carry automaticity (proved)
- Exact digit split: κ_p(K) = κ_p(r) + κ_p^{(c_r)}(n) for K = r + p^A·n (proved)
- Depth-A truncation gives periodic carry-good set (proved)
- THIS equidistribution theorem → completion step
- Collapse: carry-good ⟹ smooth (proved)

So this is the single missing piece in a complete proof.
