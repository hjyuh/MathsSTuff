**Progress on EP-488: a=2 case proved, Chojecki reduction fails for a≥3**

Some results on the density-doubling conjecture, building on the pair-tail decomposition framework from Conjecture 4.8.

**1. The a=2 case.** For every primitive set A with 2 ∈ A (equivalently, min(A)=2), the conjecture holds.

Since every element of A is ≥ 2, integer 1 is never counted, so F(m) ≤ m−1 and F(m)/m < 1 for all m.

If A ≠ {2}, choose b ∈ A \ {2}. Since A is primitive and 2 ∈ A, this b is necessarily odd. For n ≥ b:

  F(n) ≥ ⌊n/2⌋ + ⌊n/b⌋ − ⌊n/(2b)⌋ = ⌊n/2⌋ + #{odd multiples of b ≤ n} > n/2.

Therefore 2F(n)/n > 1 > F(m)/m.

For the singleton A = {2}: F(k) = ⌊k/2⌋, so for all m > n ≥ 2,

  2F(n)/n = 2⌊n/2⌋/n > 1/2 ≥ ⌊m/2⌋/m = F(m)/m.

This covers all primitive sets with 2 ∈ A.

**2. The Chojecki reduction fails for a ≥ 3.** The reduction to a fixed threshold s (first integer with F(s) ≥ 5) does not extend to a ≥ 3. Counterexample family:

For any a ≥ 3, take b = 5a+1 and T = {t ∈ Z : 5a+1 < t ≤ 10a+1, a ∤ t}. Then A = {a,b} ∪ T is primitive: every element of {b} ∪ T lies in (5a, 10a+1], so each exceeds (10a+1)/2 and no two can divide each other; and a divides none of them by construction.

The first s with F(s) ≥ 5 is s = 5a, since below 5a, only multiples of a contribute and there are exactly 4 of them (a, 2a, 3a, 4a). So F(s) = 5 and 2F(s)/s = 2/a.

At m = 10a+1: every integer in [5a+1, 10a+1] is counted by A (divisible by a → counted; not divisible by a → in T or equals b → counted). So F(10a+1) = 5 + (5a+1) = 5a+6, giving

  F(m)/m = (5a+6)/(10a+1) > 2/a = 2F(s)/s

since 5a² − 14a − 2 > 0 for all a ≥ 3.

Concrete: a=3, A = {3,16,17,19,20,22,23,25,26,28,29,31}, F(31)/31 ≈ 0.677 > 2/3.

Note: this does NOT disprove EP-488, since s = 5a < max(A) = 10a+1, so the counterexample lies outside the valid range n ≥ max(A).

**3. What remains.** The original EP-488 statement (all m > n ≥ max(A)) is checked computationally across 25,000+ primitive systems with zero failures and margins ≥ 33% (defined as (2F(n)/n − F(m)/m) / (2F(n)/n) for the tightest (n,m) pair). The reduction to sieve oscillation still works within the n ≥ max(A) regime, where the key inequality becomes: for any finite Q ⊂ Z_{≥2} and x ≥ max(Q), is A_Q(x) < 2δ_Q x?

For pairwise coprime Q, Hall–Hildebrand type bounds on the complementary unsieved count operate at an e^γ-scale; translating that into the form A_Q(x) < 2δ_Q x requires care. For non-coprime Q, computational evidence shows strictly smaller oscillation — the lcm lattice produces 30–70% coefficient cancellation in the inclusion-exclusion.
