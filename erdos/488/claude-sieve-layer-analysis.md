# EP-488: Sieve-Layer Analysis — Bounding u_j, v_j via Literature
## Source: Claude — April 5, 2026
## Integrates: Montgomery-Vaughan (1986), Gorodetsky (2021), Friedlander-Iwaniec

---

## 1. WHAT THE LITERATURE GIVES

### Montgomery-Vaughan (1986), Ann. Math.
Studies k-th moments M_k(q,h) of the distribution of reduced residues
(coprime counts) in short intervals mod q.

For k=2 (variance): asymptotic formula when q = product of primes ≤ z.
The variance of coprime counts in intervals of length h is ~ h (× log factors).

**Verdict for EP-488:** L² (average) bound only. Controls how much K_Q(y)
deviates from ρ_Q·y ON AVERAGE over y, but NOT pointwise. Cannot give
sup/inf control directly.

### Gorodetsky (2021, arXiv:2111.00853)
Studies variance of rough numbers α_y(n) in short intervals.
Key: when H ≥ y^ε, variance is SMALLER than naive prediction HPy.

**Verdict for EP-488:** Same limitation — L² not L∞. Motivates why the
sum should behave better than individual layers, but doesn't prove it.

### Bloom-Kuperberg (2023, Proc. LMS 2025)
Confirmed Montgomery-Vaughan's conjecture for odd moments of coprime
residue distribution.

**Verdict for EP-488:** Extends M-V to all moments. Still average bounds.

### Hall-Tenenbaum (1988), Divisors Ch. 5
Density of sets of multiples. Key result used by Lichtman: Theorem 21
bounds density of M_{(x^{1-ε}, x]}.

**Verdict for EP-488:** Density framework, not oscillation control.
Tangential to the direct EP-488 proof but relevant context.

### Friedlander-Iwaniec, Opera de Cribro Ch. 6
The Fundamental Lemma gives POINTWISE sieve bounds:
  f(s)·y·ρ ≤ S(y,z) ≤ F(s)·y·ρ + R
where s = log y / log z, and F(s) = 1 + O(e^{-s}), f(s) = 1 - O(e^{-s}).

**BUT:** For K_Q(y) with FINITE Q, inclusion-exclusion is EXACT.
No sieve approximation needed. The sieve bounds are LOOSER than exact I-E.

---

## 2. THE RIGHT TOOL: EXACT DISCREPANCY VIA PERIODICITY

Since K_Q(y) is computed by exact inclusion-exclusion (not sieve approx),
the tightest bounds come from the PERIODICITY of K_Q.

Let P = set of prime factors of elements of Q.
Let q = ∏_{p ∈ P} p (the primorial/product of sifting primes).

K_Q(y) is q-periodic: K_Q(y + q) = K_Q(y) + φ(q).

So: K_Q(y) = ⌊y/q⌋·φ(q) + K_Q(y mod q)

Discrepancy: |D_Q(y)| = |K_Q(y) - y·ρ_Q| ≤ φ(q) + 1

Relative discrepancy: |D_Q(y)|/(y·ρ_Q) ≤ q/y + 1/(y·ρ_Q)

### Plugging into 5.2's framework:

For layer j with y_j(x) ∈ [r_j/10, r_j]:
  |D_j(y_j)| ≤ φ(q_j) + 1

So:
  v_j ≤ φ(q_j) + 1                    (upward)
  u_j ≤ φ(q_j) + 1 + ρ_j             (downward, +ρ from floor term)

The collective condition V + 2U < C becomes:

  Σ_j (φ(q_j) + 1) + 2·Σ_j (φ(q_j) + 1 + ρ_j) < Σ_j r_j·ρ_j

  3·Σ_j (φ(q_j) + 1) + 2·Σ_j ρ_j < Σ_j r_j·ρ_j

  3·Σ_j φ(q_j) + 3k + 2·Σ_j ρ_j < Σ_j r_j·ρ_j

This holds when Σ r_j·ρ_j ≫ Σ φ(q_j), i.e., when the heavy layers
(large r_j) dominate.

---

## 3. THE HEAVY/LIGHT SPLIT (Strategy A from 5.2)

### Heavy layers (H): r_j ≥ R
- y_j ≥ R/10, so relative discrepancy |D_j|/(y_j·ρ_j) ≤ 10(φ(q_j)+1)/(R·ρ_j)
- Main term contribution: c_j = r_j·ρ_j ≥ R·ρ_j
- Excursion: e_j ≤ φ(q_j) + 1 + ρ_j

For the criterion: e_j / c_j ≤ (φ(q_j) + 1 + ρ_j)/(r_j·ρ_j)
≤ (φ(q_j) + 2)/(R·ρ_j)

This is small when R ≫ φ(q_j)/ρ_j.

### Light layers (L): r_j < R
- T_j(x) ∈ [0, r_j], can be wildly oscillatory
- Total weight: Σ_{L} r_j ≤ k·R (trivial)
- But also: Σ_{L} r_j = Σ_{L} M/a_j

### The ratio condition (from 5.2, Strategy A):

Need: Σ_{L} r_j + 3·Σ_{H} e_j < Σ_{H} r_j·ρ_j

Or: the heavy layers' stable mass dominates both:
(a) the light layers' total amplitude, AND
(b) the heavy layers' own excursions.

---

## 4. CRITICAL STRUCTURAL QUESTION

**What is φ(q_j) for a quotient-core Q_j arising from a primitive set?**

q_j = product of primes appearing in Q_j's factorization.

Key: In the peeling process, Q_j comes from dividing elements of A by a_j
and keeping the quotient structure. The primes in Q_j are bounded by the
primes in A's elements.

CONJECTURE: q_j ≤ M for all j (since Q_j arises from quotients of elements ≤ M).

If true: φ(q_j) < M, and the criterion becomes approximately:
  3kM < Σ r_j·ρ_j

Since Σ r_j·ρ_j = μ (the total mean of H(x)), this requires μ > 3kM.

But μ = Σ M·ρ_j/a_j, so μ ≤ M·Σ 1/a_j = M·S₁.
And S₁ ≤ 1 + ln(max/min) by standard bounds.

So this needs S₁ > 3k, which is FALSE for large k.

### DIAGNOSIS: The naive periodicity bound is too weak!

The bound |D_Q(y)| ≤ φ(q) + 1 treats all y equally. But for y ≫ q,
the discrepancy is much smaller (it's periodic with period q, so it
averages out over many periods).

---

## 5. REFINED DISCREPANCY FOR LARGE y

For y ≥ q: K_Q(y) = (y/q)·φ(q) + D̃_Q(y) where D̃_Q(y) depends only
on y mod q.

|D̃_Q(y)| = |K_Q(y mod q) - (y mod q)·ρ_Q| ≤ φ(q)

But: |D_Q(y)| = |K_Q(y) - y·ρ_Q| = |⌊y/q⌋·φ(q) + K_Q(y mod q) - y·ρ_Q|
= |K_Q(y mod q) - {y/q}·φ(q)| ≤ φ(q)

This is still O(φ(q)), NOT o(y). The periodicity helps with L² but not L∞.

### The actual pointwise bound:

|D_Q(y)| ≤ φ(q) for ALL y.

This is tight: at y just before a big "gap" in coprime residues, D can
be as large as ~φ(q).

BUT: for the RATIO |D_Q(y)|/(y·ρ_Q) → 0 as y → ∞. Specifically:
|D_Q(y)|/(y·ρ_Q) ≤ φ(q)/(y·ρ_Q) = q/y.

So for heavy layers with r_j ≥ R, the RELATIVE discrepancy is ≤ 10q_j/R.

---

## 6. REVISED CRITERION

Using the relative discrepancy bound:

For heavy layer j: |ε_j(x)| ≤ (M/x)·(|D_j(y_j)| + ρ_j)
≤ |D_j(y_j)|/y_j · r_j + ρ_j   (since (M/x)·y_j ≈ r_j and |D|/y ≤ ρ always)

Actually: |ε_j(x)| = |(M/x)(D_j(y_j) - ρ_j{x/a_j})|
≤ (M/x)(|D_j(y_j)| + ρ_j)
≤ 1·(q_j/y_j · y_j · ρ_j + ρ_j)     [using |D| ≤ q_j·ρ_j when y ≥ q ... no]

Let me be more careful. |D_Q(y)| ≤ φ(q) always. And φ(q) = q·ρ_Q.

So: |D_j(y_j)| ≤ q_j·ρ_j.

Then: |ε_j(x)| ≤ (M/x)(q_j·ρ_j + ρ_j) = (M/x)·ρ_j·(q_j + 1)

For x ∈ [M, 10M]: M/x ∈ [1/10, 1], so |ε_j(x)| ≤ ρ_j·(q_j + 1).

And c_j = r_j·ρ_j.

Relative excursion: e_j/c_j ≤ (q_j + 1)/r_j.

The criterion Σ e_j < C/3 becomes: Σ ρ_j·(q_j+1) < (1/3)·Σ r_j·ρ_j
⟺ Σ ρ_j·q_j < (1/3)·Σ r_j·ρ_j - Σ ρ_j
⟺ Σ ρ_j·(q_j + 3) < (1/3)·Σ r_j·ρ_j   [roughly]

This holds when r_j ≫ 3q_j for enough layers to dominate.

Since r_j = M/a_j and q_j ≤ (some function of the elements):

**THIS IS THE KEY STRUCTURAL INEQUALITY TO VERIFY.**

---

## 7. RECOMMENDATIONS

### For Codex:
Compute, for each primitive set in the test suite:
  - q_j for each peeling step (product of sifting primes in Q_j)
  - r_j / q_j for each layer
  - The ratio Σ ρ_j·q_j / Σ r_j·ρ_j (want this < 1/3)

### For 5.4 Pro:
Prove structural bound: for primitive A with max M, the quotient-core
Q_j at step j has q_j ≤ ??? (bound in terms of M, a_j, k).

### For 5.2 Pro:
Apply Strategy B (anti-alignment): can the ε_j(x) be shown to have
different "phases" so their sum is smaller than Σ|ε_j|?

The layers use different quotient cores Q_j, evaluated at different
scales y_j = ⌊x/a_j⌋. As x varies, the different layers cycle through
their periodic patterns at DIFFERENT rates (period q_j/a_j in x-space).
If the q_j are pairwise coprime, the combined oscillation is like a
multi-frequency signal with generically small sup.

---

## 8. STATUS

The heavy/light split + periodicity bound gives a clean sufficient
condition: r_j ≫ 3q_j for dominant layers. The structural question
is whether primitive sets always have this property.

This is NOT yet proved. But it gives the first concrete, checkable
condition that would close EP-488 via Strategy A (dominant stable mass).

Strategy B (anti-alignment via phase mixing) is the more powerful
approach but requires genuine Fourier analysis of the layer sum.
