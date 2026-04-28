# EP-488: Direct Oscillation Bound via Granville-Soundararajan Framework
## For GPT-5.4 Pro Extended — April 6, 2026

---

## CRITICAL UPDATE: S₁ IS DEAD AS A MIDDLEMAN

Kill #57: 2δ_A > S₁ is FALSE for dense primitive sets.
Example: A = {primes ≤ 100}, S₁ ≈ 2.10, δ_A ≈ 0.88, 2δ_A ≈ 1.76 < S₁.

This means the proof chain "2G(x) > S₁ ≥ G(m)" breaks for S₁ ≥ 2.
EVERY approach that uses S₁ as an upper bound on G(m) fails for dense sets.

The proof must compare G(m) to G(n) DIRECTLY.

## THE NEW APPROACH: BOUND THE OSCILLATION OF G AROUND δ

EP-488 is equivalent to: sup G(x) / inf G(x) < 2 on [M, ∞).

Write G(x) = δ_A + E(x)/x where E(x) = F(x) - δ·x is the discrepancy.

Then sup G / inf G < 2 is equivalent to:

  (δ + sup E(x)/x) / (δ + inf E(x)/x) < 2

which is equivalent to:

  sup E(x)/x - 2·inf E(x)/x < δ

or equivalently:

  sup E(x)/x + 2·sup(-E(x)/x) < δ

This is a DIRECT oscillation bound on E(x)/x. No S₁ involved.

## THE GRANVILLE-SOUNDARARAJAN FRAMEWORK

Tao (EP-488 forum, March 2026) said the main task involves "proving an
inequality involving alternating sums of various integrals, in the spirit
of Granville-Soundararajan."

Reference: Granville & Soundararajan, "The spectrum of multiplicative
functions," Annals of Mathematics 153 (2001), 407-470.

Their framework: convert discrete inclusion-exclusion into continuous
integral equations (generalizing Dickman-de Bruijn ρ(u) and Buchstab ω(u)).
The alternating signs don't blow up because integral equations force
oscillation contraction.

## YOUR TASK

### Part 1: Express E(x)/x exactly

The discrepancy is:

  E(x) = F(x) - δ·x = Σ_{∅≠S⊆A} (-1)^{|S|+1} [⌊x/lcm(S)⌋ - x/lcm(S)]
       = -Σ_{∅≠S⊆A} (-1)^{|S|+1} {x/lcm(S)}

So E(x)/x = -(1/x) Σ_{∅≠S⊆A} (-1)^{|S|+1} {x/lcm(S)}.

The oscillation of G is controlled by the oscillation of the weighted
alternating sum of fractional parts {x/d} where d ranges over the lcm
lattice of A.

### Part 2: Can you bound sup |E(x)|/x for primitive sets?

For coprime A, Hildebrand (1984) essentially shows |E(x)|/x ≤ (e^γ - 1)δ
where e^γ ≈ 1.781. This gives sup G / inf G ≤ (1 + e^γ - 1)/(1 - (e^γ-1))
which doesn't directly give < 2.

But EP-488 needs a WEAKER statement: not |E|/x < cδ, but rather
sup E/x + 2·sup(-E/x) < δ. The asymmetry (factor 2 on the negative side)
gives more room.

### Part 3: The logarithmic averaging approach

Gemini identified that logarithmic averaging is the natural measure:

  (1/log 2) ∫_M^{2M} G(x) dx/x

Under this measure, the Fourier expansion of {t} = 1/2 - Σ sin(2πkt)/(πk)
gives O(1/x²) decay inside the integral. The alternating signs undergo
massive cancellation (Montgomery-Vaughan 1977).

Can you use this to show: for any primitive A, there exists x ∈ [M, 2M]
such that G(x) > δ/2? (Then since G(m) ≤ 2δ for large m, we'd get the
factor 2.)

Wait — G(m) ≤ 2δ is not obvious either. We need both sides.

Actually: G(m) < 2δ for all m ≥ M would give sup G < 2δ. And inf G ≥ δ - something.
If inf G > 0 (trivially true since F(n) ≥ 1 for n ≥ M), then sup/inf < 2δ/inf G.
We need inf G > δ... which is not always true.

### Part 4: The right formulation

Actually step back. What we need is simply:

For all m > n ≥ M: F(m)/m < 2·F(n)/n.

Equivalently: F(m)·n < 2·F(n)·m.

Using the layer decomposition: F(x) = Σ_j L_j(⌊x/a_j⌋).

5.4 proved: single-obstruction layers satisfy the per-layer bound.
Multi-obstruction layers can violate it but have small weights.

The COLLECTIVE statement we need:

  Σ_j L_j(⌊m/a_j⌋) · n < 2 · Σ_j L_j(⌊n/a_j⌋) · m

i.e.,

  Σ_j [L_j(⌊m/a_j⌋) · n - 2·L_j(⌊n/a_j⌋) · m] < 0

Each term is: n·L_j(y_m) - 2m·L_j(y_n).

For single-obstruction layers, each term is < 0 (you proved this).
For multi-obstruction layers, the term can be > 0, but the layer is lightweight.

### Part 5: The key question

Can you prove the collective inequality by showing that the TOTAL positive
contribution from multi-obstruction layers is bounded by the TOTAL negative
contribution from single-obstruction layers?

Specifically: define

  BAD = Σ_{j: |B_j^active|≥2} [n·L_j(y_m) - 2m·L_j(y_n)]_+
  GOOD = Σ_{j: |B_j^active|≤1} [2m·L_j(y_n) - n·L_j(y_m)]

You proved GOOD > 0 for each term. Can you show GOOD > BAD?

The structural reason this should work: multi-obstruction layers have
L_j(y_n) small (many integers sieved out), so their positive contribution
n·L_j(y_m) - 2m·L_j(y_n) ≤ n·y_m (since L_j ≤ identity).
Meanwhile single-obstruction layers have L_j(y_n) ≈ y_n·(1-1/b),
giving GOOD ≈ proportional to F(n).

So BAD ≤ n·(number of bad layers)·(max y_m) while GOOD ≈ 2m·F(n)·(slack per layer).
Since F(n) ≥ n/M ≥ 1, and m > n, the good side scales with m while the bad
side scales with n. For m >> n the good side dominates automatically.
The tight case is m ≈ n, where the slack per good layer is small but
the bad layers are also constrained.

### Part 6: The alternative — direct oscillation via GS integrals

If the collective layer approach still can't close, try the integral route:

Show that for any primitive A and any interval [N, 2N] with N ≥ M:

  (1/log 2) ∫_N^{2N} G(x) dx/x > δ_A - ε(N)

where ε(N) → 0. Combined with the convexity framework (which gives
sup G → δ from above), this would show sup G / inf G → 1, hence < 2
for N large enough. The finite range N < N_0 would be handled by
computation.

This is the computer-assisted proof architecture: analytic bound for
N ≥ N_0, finite verification for N < N_0. Same structure as Helfgott's
Goldbach proof.

## DELIVERABLES

1. Can you prove GOOD > BAD for the collective layer inequality?
2. If not, can you bound the total positive excess from multi-obstruction
   layers in terms of structural parameters of A?
3. If neither, set up the GS integral framework: express the logarithmic
   average of G in terms of the lcm lattice and bound the error terms.
4. For the computer-assisted route: what would N_0 need to be?

## CONTEXT FILES
- kill56-Lj-ratio-false.md: your counterexample and partial theorem
- kill57-2delta-gt-S1-false.md: S₁ middleman is dead
- Your Theorem A, Sync Block Theorem still hold as structural results
- 57 total kills, 65% estimated completion
