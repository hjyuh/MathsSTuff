# Analysis of Cumberbatch IRIF Slides (April 15, 2025)
## "Smooth Integers with Restricted Digits"

### His Results

**Theorem 1 (slide 14):** For b=10 or b large, |D|=b-1, for exp((log log X)^7) < y < X^δ:
|A_{k,D} ∩ S(X,y)| = Ψ(X,y)|A_{k,D}|/X · (1+o(1))
i.e., smoothness and digit restriction are INDEPENDENT in this range.

**Theorem 2 (slide 24):** More precise asymptotic with corrective factors S_b and S_∞ for (log X)^{c1} < y < exp((log X)^{1-ε}).

**Method:** Hardy-Littlewood circle method. Fourier transforms of digit indicator and smooth indicator. Major/minor arc decomposition. Key: digit-restricted integer is "secretly the sum of many variables" n = n_0 + 10·n_1 + ... + 10^{k-1}·n_{k-1}.

**Advisor:** Trevor Wooley (world expert on circle method).

### Gaps Between His Work and Our Problem 396

**Gap 1 — Smoothness range:** His y < X^δ. We need y = X^{1/2}. But our regime is EASIER — ρ(2) > 0 means smooth numbers have positive density. His hard work is for tiny y.

**Gap 2 — One base vs. many bases:** His restriction is in ONE fixed base (b=10). We need carry conditions across ALL primes p ≤ √X simultaneously. This is the fundamental gap.

**Gap 3 — Digit type:** His "restricted" = ban one digit. Ours = carry condition on digit PAIRS when doubling in base p. Different structure.

### What IS Directly Useful

- The circle method framework for combining digit conditions with smoothness
- His exponential sum analysis of digit indicators (slide 25)
- The major/minor arc technique for handling the interaction
- Structural insight: digit conditions have additive structure → no multiplicative structure expected → smoothness should be "independent"

### Questions Sent to Author (March 16, 2026)

1. Does the exponential sum machinery adapt to pair-digit constraints (carries) vs single-digit bans?
2. Can CRT handle cross-base independence for simultaneous multi-base digit conditions?
3. Is the y = X^{1/2} regime easier or harder for digit-smoothness interaction?
4. Is a preprint available?

### Implications for Our Attack

If his method DOES extend to carry conditions:
- The carry-good set would have a well-defined Fourier structure
- The circle method would give the joint count directly
- This would close the entire proof (carry-good ∩ smooth is nonempty, in fact has positive density)

If his method does NOT extend:
- We still need a different approach for the joint distribution
- Possible alternatives: Holte Markov chain for carries + sieve theory, or direct CRT/Euler product

### Status
Email sent March 16, 2026. Awaiting response.
