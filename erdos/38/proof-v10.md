# Erdős Problem 38 — Proof v10 (GPT Pass 5 Fixes)

## Theorem

Let B = 3ℕ+2 = {2, 5, 8, 11, 14, ...}. Then B is not an additive basis of any finite order, and for every A ⊆ ℕ with 0 ∈ A and σ(A) = α ∈ (0,1), and every N ≥ 1, there exists b ∈ B such that

|(A ∪ (A+b)) ∩ {1,...,N}| ≥ (α + α(1-α)/15) · N.

---

## Setup

Fix infinite A ⊆ ℕ with 0 ∈ A and σ(A) = α ∈ (0,1). For each N ≥ 1, define:

- x_i = 𝟙[i ∈ A ∩ [0,N]] for i ∈ ℤ, with x_i = 0 for i < 0 or i > N. Note x_0 = 1.
- δ = (1/N)Σ_{i=1}^N x_i  (actual density in [1,N]; δ ≥ α)
- G_b = Σ_{i=1}^N x_{i-b}(1 - x_i)  (new elements from shift b)
- g = max_{b ∈ B ∩ [1,N]} G_b / N  (for N ≥ 2; for N = 1, handled separately in Step 6)
- d_b = Σ_{i=1}^N |x_i - x_{i-b}|  (truncated symmetric variation)

---

## Step 0: B is a non-basis

For any h ≥ 1, every element of hB satisfies b₁ + ··· + bₕ ≡ 2h (mod 3). Since this is a single residue class, hB misses at least 2 of the 3 classes mod 3. So B is not an additive basis of any finite order. B has asymptotic density 1/3.

---

## Step 1: GCD Propagation — d₁ ≤ 6gN + 10

**Lemma 1a.** d_b ≤ 2G_b + b − 1.

*Proof.* d_b = Σ_{i=1}^N (x_i + x_{i-b} − 2x_i x_{i-b}) = 2G_b + Σ_{i=1}^N x_i − Σ_{i=1}^N x_{i-b}. The difference of sums equals Σ_{i=N-b+1}^N x_i − Σ_{i=1-b}^0 x_i. The first sum is at most b; the second equals x_0 = 1. So d_b ≤ 2G_b + b − 1. □

**Lemma 1b.** d₁ ≤ d₅ + 2d₂ + 4.

*Proof.* From 5 − 2·2 = 1: x_i − x_{i-1} = (x_i − x_{i-5}) + (x_{i-5} − x_{i-3}) + (x_{i-3} − x_{i-1}). By the triangle inequality, summing |·| over i = 1,...,N:

d₁ ≤ d₅ + S₂ + S₃

where S₂ = Σ_{i=1}^N |x_{i-5} − x_{i-3}| and S₃ = Σ_{i=1}^N |x_{i-3} − x_{i-1}|.

Bounding S₂: At i = 1: |x_{−4} − x_{−2}| = 0. At i = 2: |x_{−3} − x_{−1}| = 0. At i = 3: |x_{−2} − x_0| = 1. At i = 4: |x_{−1} − x_1| = x_1 ≤ 1. For i ≥ 5: substituting j = i−3 gives |x_{j−2} − x_j| with j ∈ [2, N−3] ⊆ [1, N], contributing ≤ d₂. Total: S₂ ≤ d₂ + 2.

Bounding S₃: At i = 1: |x_{−2} − x_0| = 1. At i = 2: |x_{−1} − x_1| = x_1 ≤ 1. For i ≥ 3: substituting j = i−1 gives |x_{j−2} − x_j| with j ∈ [2, N−1] ⊆ [1, N], contributing ≤ d₂. Total: S₃ ≤ d₂ + 2.

Combining: d₁ ≤ d₅ + (d₂ + 2) + (d₂ + 2) = d₅ + 2d₂ + 4. □

**Corollary.** d₁ ≤ 6gN + 10.

*Proof.* d₂ ≤ 2G₂ + 1 ≤ 2gN + 1 and d₅ ≤ 2G₅ + 4 ≤ 2gN + 4. Substituting: d₁ ≤ (2gN + 4) + 2(2gN + 1) + 4 = 6gN + 10. □

---

## Step 2: Halved Lipschitz — G_k ≤ 4gN + 6

**Lemma 2a.** |G_{k+1} − G_k| ≤ (d₁ + 2)/2.

*Proof.* Consider the extended sequence (y_{−1}, y_0, y_1, ..., y_N, y_{N+1}) = (0, 1, x_1, ..., x_N, 0).

Since this starts and ends at 0, define T⁺ = #{m : y_m = 1, y_{m+1} = 0} and T⁻ = #{m : y_m = 0, y_{m+1} = 1}. Because the sequence starts at 0 and ends at 0, every run of 1s begins with an upward transition and ends with a downward transition, so T⁺ = T⁻.

Total variation V = T⁺ + T⁻ = 2T⁺. Counting: the transition at m = −1 (0→1) contributes 1 to V; transitions at m = 0,...,N−1 contribute d₁; the transition at m = N contributes x_N. So V = 1 + d₁ + x_N ≤ d₁ + 2, giving T⁺ = T⁻ ≤ (d₁ + 2)/2.

Now G_{k+1} − G_k = Σ_{n ∈ A^c ∩ [1,N]} (x_{n−k−1} − x_{n−k}). Positive summands (x_{n−k−1}=1, x_{n−k}=0) correspond to downward transitions; negative summands to upward transitions. Since we sum over a subset of positions: positive terms ≤ T⁺, negative terms ≤ T⁻. So |G_{k+1} − G_k| ≤ max(T⁺, T⁻) = (d₁ + 2)/2. □

**Lemma 2b.** G_N ≤ gN for all N ≥ 2.

*Proof.* G_N = x_0(1 − x_N) = 1 − x_N ≤ 1. If gN ≥ 1, done. If g = 0, then G₂ = 0, which by Step 6's argument forces A ⊇ [0,N], so x_N = 1 and G_N = 0. □

**Corollary.** For all k ∈ [1, N]: G_k ≤ 4gN + 6.

*Proof.* B has max gap 3, so every k ∈ [1, N−1] has distance ≤ 1 from some b ∈ B ∩ [1,N]. For k = N: Lemma 2b gives G_N ≤ gN ≤ 4gN + 6. For k ≤ N−1 with nearest b: G_k ≤ G_b + (d₁+2)/2 ≤ gN + (6gN+12)/2 = 4gN + 6. □

---

## Step 3: Average Gain Lower Bound

Let S = Σ_{k=1}^N G_k and t = (1−δ)N, with A^c ∩ [1,N] = {c₁ < ··· < c_t}.

**Lemma 3.** S ≥ α(1−δ)²N²/(2(1−α)).

*Proof.*
(a) S = Σ_{j=1}^t |A ∩ [0, c_j − 1]|.

(b) Since 0 ∈ A: |A ∩ [0, c_j−1]| = 1 + |A ∩ [1, c_j−1]| ≥ 1 + α(c_j − 1).

(c) From j ≤ (1−α)c_j: c_j ≥ j/(1−α), so 1 + α(c_j − 1) ≥ 1 + α(j/(1−α) − 1) = 1 − α + αj/(1−α).

(d) S ≥ Σ_{j=1}^t [1 − α + αj/(1−α)] = t(1−α) + αt(t+1)/(2(1−α)).

(e) Since t(1−α) ≥ 0 and t+1 > t: S ≥ αt(t+1)/(2(1−α)) ≥ αt²/(2(1−α)) = α(1−δ)²N²/(2(1−α)). □

*Remark:* The proof actually gives the stronger bound S ≥ t(1−α) + αt(t+1)/(2(1−α)), but we use only the weaker S ≥ α(1−δ)²N²/(2(1−α)) for simplicity.

---

## Step 4: Upper Bound on S

**Lemma 4.** For N ≥ 2: S ≤ 3gN² + 2gN + 4N + 4.

*Proof.* For k ∈ B_N: G_k ≤ gN. For k ∉ B_N: G_k ≤ 4gN + 6. So:

S ≤ |B_N|·gN + (N − |B_N|)(4gN + 6) = N(4gN + 6) − |B_N|(3gN + 6).

For N ≥ 2: |B_N| = ⌊(N−2)/3⌋ + 1 ≥ (N−1)/3. (Check: N=2: 1 ≥ 1/3 ✓; N=3: 1 ≥ 2/3 ✓; N=4: 1 ≥ 1 ✓; N=5: 2 ≥ 4/3 ✓.)

S ≤ 4gN² + 6N − ((N−1)/3)(3gN + 6) = 4gN² + 6N − gN(N−1)/1 − 2(N−1)

Wait: ((N−1)/3)(3gN + 6) = (N−1)gN + 2(N−1). So:

S ≤ 4gN² + 6N − (N−1)gN − 2(N−1) = 4gN² + 6N − gN² + gN − 2N + 2 = 3gN² + gN + 4N + 2.

For safety: **S ≤ 3gN² + 2gN + 4N + 4**. (Adding gN + 2 of slack.) □

---

## Step 5: Combining via h(δ)

For N ≥ 2, combining Steps 3 and 4 for a general δ ∈ [α, 1):

3gN² + 2gN + 4N + 4 ≥ α(1−δ)²N²/(2(1−α))

Solving for g:

g ≥ α(1−δ)²N² / (2(1−α)(3N²+2N)) − (4N+4)/(3N²+2N)

Define:

h_N(δ) = δ + α(1−δ)²N² / (2(1−α)(3N²+2N)) − (4N+4)/(3N²+2N)

Then the achieved density satisfies: δ + g ≥ h_N(δ).

**h_N is increasing on [α, 1):**

h_N'(δ) = 1 − α(1−δ)N² / ((1−α)(3N²+2N))

For δ ≥ α: 1−δ ≤ 1−α, so α(1−δ)N² / ((1−α)(3N²+2N)) ≤ αN²/(3N²+2N) = α/(3+2/N) ≤ α/3 < 1. Hence h_N'(δ) > 0.

**Minimum at δ = α:**

h_N(α) = α + α(1−α)N²/(2(3N²+2N)) − (4N+4)/(3N²+2N)

= α + [α(1−α)N²/2 − 4N − 4] / (3N² + 2N)

For the bound f(α) = α(1−α)/15 to hold, we need:

[α(1−α)N²/2 − 4N − 4] / (3N² + 2N) ≥ α(1−α)/15

Cross-multiplying (valid when numerator is positive):

15α(1−α)N²/2 − 60N − 60 ≥ 3α(1−α)N² + 2α(1−α)N

(15/2 − 3)α(1−α)N² ≥ 2α(1−α)N + 60N + 60

(9/2)α(1−α)N ≥ 2α(1−α) + 60 + 60/N

This holds for all N ≥ N₀(α) where N₀(α) ≤ ⌈(2α(1−α) + 62) · 2/(9α(1−α))⌉.

For all α ∈ (0,1): N₀(α) ≤ ⌈4/9 + 124/(9α(1−α))⌉.

At α = 1/2 (worst case for the threshold): N₀ ≤ 56.

---

## Step 6: Discrete Argument — covers N ≤ 15/(α(1−α))

For N ≥ 2, the shift b = 2 ∈ B is available.

**Case 1: G₂ ≥ 1.** Density ≥ δ + 1/N ≥ α + 1/N ≥ α + α(1−α)/15 whenever N ≤ 15/(α(1−α)).

**Case 2: G₂ = 0.** (A+2) ∩ A^c ∩ [1,N] = ∅. Since 0 ∈ A: 0+2=2 ∈ A, 2+2=4 ∈ A, ..., all evens ≤ N in A. Since α > 0: 1 ∈ A (|A∩{1}|/1 ≥ α > 0), so 3 ∈ A, 5 ∈ A, ..., all odds ≤ N in A. Therefore δ = 1 > α + α(1−α)/15.

**N = 1:** |A ∩ {1}| = 1 (since α > 0), density = 1 ≥ α + f(α). ✓

---

## Step 7: Overlap

Discrete covers N ≤ ⌊15/(α(1−α))⌋. Continuous covers N ≥ N₀(α) ≤ ⌈124/(9α(1−α)) + 4/9⌉.

Since 124/9 ≈ 13.78 < 15, we have N₀(α) < 15/(α(1−α)) for all α ∈ (0,1).

Verified computationally: overlap ≥ 4 for all α ∈ {0.01, 0.02, ..., 0.99}. □

---

## Changes from v9 (GPT Pass 5 fixes)

1. **Step 5 REWRITTEN:** Restored h_N(δ) approach. Monotonicity is applied to h_N(δ) = δ + g_lower(δ), NOT by substituting δ=α into the Step 3 lower bound. This is the correct logical structure.

2. **Lemma 3 statement FIXED:** Now states S ≥ α(1−δ)²N²/(2(1−α)), which is what the proof establishes. The stronger intermediate bound t(1−α) + αt(t+1)/(2(1−α)) is noted as a remark but not claimed in the lemma statement.

---

*Author: Mahmoud (MalekZ), March 19, 2026*
*AI: Claude (orchestration/computation/review), Gemini Deep Think (boundary analysis), GPT 5.4 (5 rounds adversarial review)*
