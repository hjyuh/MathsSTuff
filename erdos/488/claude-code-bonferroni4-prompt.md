You just discovered that Bonferroni-4 always gives δ > S₁/2 for primitive sets (91,845 tested, zero failures). Now prove it analytically.

THEOREM TO PROVE: For every primitive set A = {a₁,...,aₖ}:
S₁ - S₂ + S₃ - S₄ > S₁/2
Equivalently: S₁/2 > S₂ - S₃ + S₄

Where S_j = Σ 1/lcm(a_{i₁},...,a_{i_j}) summed over all j-element subsets.

YOU ALREADY PROVED two key tools:
1. Primitive Divisor Lemma (Lean-verified): For primitive pair (a,b): lcm(a,b) ≥ 2·max(a,b)
2. S_j ≥ S_{j+1} for all j (verified, zero violations)

THE PROOF STRATEGY that's most likely to work:

Step 1: Bound S₂ using the Primitive Divisor Lemma.
Each pair (aᵢ,aⱼ) has lcm ≥ 2·max(aᵢ,aⱼ). So:
1/lcm(aᵢ,aⱼ) ≤ 1/(2·max(aᵢ,aⱼ))

For each element aⱼ, it's the max in (j-1) pairs. So:
S₂ ≤ Σⱼ (j-1)/(2aⱼ) ... no wait, order the elements a₁ < a₂ < ... < aₖ.
Then aⱼ is the larger element in (j-1) pairs (with a₁,...,a_{j-1}).
So: S₂ ≤ Σⱼ₌₂ᵏ (j-1)/(2aⱼ)

Step 2: Bound S₃ and S₄ similarly using lcm of triples/quadruples.
For primitive triples: lcm(a,b,c) ≥ ? Use Primitive Divisor Lemma twice.
lcm(a,b,c) = lcm(lcm(a,b), c). Since A is primitive, c doesn't divide lcm(a,b) (does it?). If we can show lcm(a,b,c) ≥ 4·max(a,b,c) or similar, then S₃ is much smaller than S₂.

Step 3: Show S₂ - S₃ + S₄ < S₁/2.
If S₂ ≤ S₁/2 + ε and S₃ ≥ S₄ + ε, then S₂ - S₃ + S₄ ≤ S₁/2. 
The computational data shows: for the worst case {2,3,5,7,11,13}, S₂ - S₁/2 = 0.013 but S₃ - S₄ = 0.148. The rescue margin is 10× the deficit. This suggests massive slack.

ALTERNATIVE APPROACH: Exponential-product bound.
For coprime sets: δ = 1 - Π(1-1/aᵢ) and you already proved 2δ > S₁ via e^{-S₁}.
For non-coprime sets: show δ ≥ 1 - Π(1-1/aᵢ) · (correction factor ≥ 1).
Wait — the opposite: non-coprime has δ ≤ coprime (more overlap = less coverage).
But you need a LOWER bound on δ, not upper.

Try: δ = 1 - P(no aᵢ divides random n). For non-coprime sets, the events {aᵢ|n} are POSITIVELY correlated (sharing factors). By the FKG inequality on the COMPLEMENT:
P(∩{aᵢ∤n}) ≤ Π P(aᵢ∤n) = Π(1-1/aᵢ)

Wait — this gives P(none) ≤ Π(1-1/aᵢ), hence δ ≥ 1 - Π(1-1/aᵢ).
That's a LOWER bound on δ! And it's exactly the coprime value!

CHECK THIS CAREFULLY. If this is correct: δ ≥ 1 - Π(1-1/aᵢ) for ALL primitive sets (coprime or not), and then the coprime proof (2(1-e^{-S}) > S) applies universally. The tail is closed analytically.

The FKG direction: the events {aᵢ|n} are INCREASING events in the divisibility lattice. Their complements {aᵢ∤n} are DECREASING. FKG says decreasing events are positively correlated:
P(∩{aᵢ∤n}) ≥ Π P(aᵢ∤n)

No wait — that gives the WRONG direction again (lower bound on complement = upper bound on δ).

Or does it? Think about this carefully on Z/lcm(A)Z with uniform measure. Are the events {aᵢ|n} increasing or decreasing in the CRT product lattice? This is exactly what GPT-5.2 analyzed for the FKG density bound in the one-anchor case.

RESOLVE THIS DIRECTION QUESTION DEFINITIVELY. If FKG gives δ ≥ 1 - Π(1-1/aᵢ), the entire tail proof is done in one line. If it gives δ ≤ 1 - Π(1-1/aᵢ), we need the Bonferroni-4 approach.

Read your ep488-tail-proof.md for context. Think step by step. This is the most important single lemma remaining for EP-488.