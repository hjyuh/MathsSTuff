# Blocker A: The Multi-Prime Lift — Exact Theorem Target

March 16, 2026

## What We Have

1. **Truncated carry-good periodicity (Codex):** For fixed Y, G_Y(X) = {K ∈ (X,2X] : carry-good at all p ≤ Y} is a union of residue classes mod Q_Y(X) = ∏_{p≤Y} p^{a_p(X)}.

2. **Uniform layer lemma (frozen):** For p > 2n, p ≥ 4a: q_{n,p}(a) ≤ C_n·a·2^{-a}/p. Summable over layers.

3. **Collapse theorem:** If K is carry-good (at all primes p > 2n), then P⁺(∏(K-j)) ≤ √(2K). So carry-good ⟹ smooth.

## What We Need

**The multi-prime lift:** Show that G_Y(X) is nonempty — ideally, has positive density in (X,2X] — for all large X and some Y = Y(X) → ∞.

## Why This Is Hard

Q_Y(X) = ∏_{p≤Y} p^{a_p(X)} is MUCH larger than X for any Y > exp(c·√(log X)).

For example, with Y = 100 and X = 10^{20}:
- Q_Y ≈ ∏_{p≤100} p^{log_p(10^{20})} = ∏ 10^{20} × (stuff) ≫ 10^{500}

So [X,2X] contains only X/Q_Y ≈ 0 complete residue classes mod Q_Y. The CRT product ∏(1-q_{n,p}) gives the density WITHIN a complete residue system mod Q_Y, but says nothing about density in the short interval [X,2X].

This is not a technicality — it's the core mathematical difficulty.

## Three Possible Approaches

### Approach 1: Truncate Y at a level where Q_Y < X

If Y is small enough that Q_Y(X) < X, then [X,2X] contains ≥ X/Q_Y complete periods, and the CRT density theorem gives:

  |G_Y(X)| ≥ (X/Q_Y) · |R_Y| ≥ (X/Q_Y) · Q_Y · ∏(1-q_{n,p}) = X · ∏(1-q_{n,p}) > 0

The question: how large can Y be while keeping Q_Y < X?

  log Q_Y = Σ_{p≤Y} a_p(X)·log(p) = Σ_{p≤Y} (log X + O(log p)) ≈ π(Y)·log X

So Q_Y < X requires π(Y)·log X < log X, i.e., π(Y) < 1. That means Y < 3.

This is useless — we can only handle Y = 2, covering a single prime.

### Approach 2: Use the layer structure

The key insight from the uniform layer lemma: primes at depth a contribute bad mass ≈ β_a/a, which is summable. So most of the "work" in the CRT product comes from small primes (large depth), where the conditions are very easy to satisfy.

Idea: instead of Q_Y = ∏ p^{a_p}, use a TRUNCATED modulus where we only impose conditions at bounded depth:

  Q'_Y(X) = ∏_{p≤Y} p^{min(a_p(X), A)}

for some fixed A. Then Q'_Y ≤ (∏_{p≤Y} p)^A = e^{Aθ(Y)} where θ(Y) ≈ Y. So Q'_Y < X requires A·Y < log X, i.e., Y < (log X)/A.

For Y = (log X)/(2A), Q'_Y < √X, and [X,2X] contains > √X complete periods. The density of the depth-A truncated carry-good set is ∏_p (1 - q_{n,p}(A)), which by the uniform layer lemma is ≥ exp(-C_n·Σ_p 1/p) ≥ exp(-C_n·log log Y) > 0.

But this only gives carry-goodness at depth A at primes p ≤ (log X)/(2A). The remaining primes — and the full-depth conditions — are not covered.

### Approach 3: Sieve completion / Selberg trick

Use the depth-A truncated periodicity from Approach 2 as a "base" set, then use sieve methods to remove the remaining bad residue classes.

The depth-A carry-good set G'(X) has positive density ≈ δ > 0 in [X,2X] (from Approach 2). Then:

  G_Y(X) = G'(X) \ ∪_{conditions at depth > A or primes > (log X)/(2A)} {bad K}

If the additional bad conditions remove only a small fraction of G'(X), then G_Y(X) is still nonempty.

The additional conditions are:
- For each prime p ≤ Y, the carry condition at positions A+1, ..., a_p: these are conditions on the base-p digits of K at high positions, which are "local" in the sense that they affect K mod p^{a_p} but not K mod p^A.
- For primes (log X)/(2A) < p ≤ Y: full carry conditions.

The question: can we bound the measure of {K ∈ G'(X) : bad at some additional condition}?

### Approach 4: Direct exponential sum / circle method (Cumberbatch-style)

Use Fourier analysis. The indicator function of G_Y(X) has a Fourier expansion in terms of characters mod Q_Y. The count of K ∈ [X,2X] ∩ G_Y(X) is:

  |G_Y(X)| = Σ_{χ mod Q_Y} â(χ) · Σ_{X < K ≤ 2X} χ(K)

The main term (χ = χ_0) gives X·∏(1-q_{n,p}). The error terms need cancellation over the huge character group mod Q_Y.

This is exactly what Cumberbatch's circle method does for digit-restricted sets. His f(θ) = Σ_{n∈A_k} e(nθ) has the same structure — a sum over a thin set defined by digit conditions in one base.

For our problem, we'd need this for MULTIPLE bases simultaneously. That's the multi-base extension question we asked Cumberbatch.

## My Assessment

**Approach 2 + 3 is the most promising near-term path.** It avoids the full circle-method machinery and uses the layer structure we've already established.

**The key lemma needed:** For fixed A and Y ≤ (log X)/(2A):

  |{K ∈ G'_A(X) : carry-bad at some p at depth > A}| ≤ δ/2 · |G'_A(X)|

where G'_A is the depth-A truncated carry-good set.

If this holds, then |G_Y(X)| ≥ (δ/2) · X > 0, which gives nonemptiness and positive density.

**The obstacle:** The high-depth conditions are NOT residue conditions mod Q'_Y. They depend on the full base-p expansion of K, which is not captured by K mod p^A. So bounding the overlap requires understanding how the high-digit conditions correlate with the low-digit conditions.

This is exactly where the carry Markov chain helps: conditioned on the first A digits being good, the probability of failure at higher digits is exponentially small in a-A. The uniform layer lemma quantifies this.

## Exact Next Theorem Target

**Theorem (Multi-prime lift for fixed Y).** For fixed n ≥ 1 and any Y ≥ 2n+1, there exists c_n > 0 such that for all sufficiently large X:

  |G_Y(X)| ≥ c_{n,Y} · X

where G_Y(X) = {K ∈ (X,2X] : ν_p(K-j) ≤ κ_p(K) for all p ≤ Y, all 0 ≤ j ≤ n with p|(K-j)}.

**If this is proved:** Set Y = Y(X) → ∞ slowly enough that c_{n,Y} stays positive. Then G_Y(X) is nonempty for all large X. By the collapse theorem, each K ∈ G_Y(X) has P⁺(∏(K-j)) ≤ √(2K). Done.

## STATUS
This is the formulation. Not yet a proof or even a proof sketch. Waiting for Codex's input on which approach to push.
