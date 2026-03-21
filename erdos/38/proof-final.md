# Erdős Problem 38 — Proof (Post-Ready)

## Convention

Throughout, we use the standard Schnirelmann density convention: **0 ∈ A** for any set A of positive Schnirelmann density. This is universal in the literature (Erdős [Er36c], Mann [Ma42], Nathanson *Additive Number Theory*, Halberstam–Roth). The density itself is computed on {1,...,N}: σ(A) = inf_{N≥1} |A ∩ {1,...,N}|/N. Without 0 ∈ A, the problem is trivially false at small N for any B with min(B) ≥ 2.

---

## Theorem

Let B = 3ℕ+2 = {2, 5, 8, 11, 14, ...}. Then B is not an additive basis of any finite order, and for every A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1), and every N ≥ 1, there exists b ∈ B such that

|(A ∪ (A+b)) ∩ {1,...,N}| ≥ (α + α(1−α)/15) N.

---

## Setup

Fix A ⊆ ℕ₀ with 0 ∈ A, σ(A) = α ∈ (0,1). For each N ≥ 1 define:

- x_i = 𝟙[i ∈ A ∩ [0,N]] for i ∈ ℤ, with x_i = 0 for i ∉ [0,N]. Note x_0 = 1.
- δ = (1/N) Σ_{i=1}^N x_i  (density in [1,N]; δ ≥ α always).
- G_b = Σ_{i=1}^N x_{i−b}(1−x_i)  (new elements from shift b).
- g = max_{b ∈ B ∩ [1,N]} G_b/N  (for N ≥ 2; N = 1 handled in Step 6).
- d_b = Σ_{i=1}^N |x_i − x_{i−b}|  (symmetric variation on [1,N]).

Since |(A ∪ (A+b)) ∩ [1,N]| = |A ∩ [1,N]| + G_b = (δ + G_b/N)N, it suffices to show δ + g ≥ α + α(1−α)/15.

---

## Step 0: B is a non-basis

For any h ≥ 1, every element of hB = B+···+B (h terms) satisfies b₁+···+bₕ ≡ 2h (mod 3). This is a single residue class mod 3, so hB misses at least 2 of the 3 classes. B is not an additive basis of any finite order. B has asymptotic density 1/3.

---

## Step 1: GCD Propagation

**Lemma 1a.** d_b ≤ 2G_b + b − 1.

*Proof.* Expanding: d_b = 2G_b + Σ_{i=1}^N x_i − Σ_{i=1}^N x_{i−b}. The difference of sums is Σ_{i=N−b+1}^N x_i − Σ_{i=1−b}^0 x_i. The first sum is at most b; the second equals x_0 = 1. □

**Lemma 1b.** d₁ ≤ d₅ + 2d₂ + 4.

*Proof.* From 5 − 2·2 = 1, we have the algebraic identity

x_i − x_{i−1} = (x_i − x_{i−5}) + (x_{i−5} − x_{i−3}) + (x_{i−3} − x_{i−1}).

Applying the triangle inequality and summing over i = 1,...,N:

d₁ ≤ d₅ + S₂ + S₃

where S₂ = Σ_{i=1}^N |x_{i−5} − x_{i−3}| and S₃ = Σ_{i=1}^N |x_{i−3} − x_{i−1}|.

*Bounding S₂.* The terms i = 1, 2 vanish (both indices < 0). At i = 3: |x_{−2} − x_0| = 1. At i = 4: |x_{−1} − x_1| = x_1 ≤ 1. For i ≥ 5, substituting j = i−3 gives |x_{j−2} − x_j| with j ∈ [2, N−3] ⊆ [1, N], contributing at most d₂. Total: S₂ ≤ d₂ + 2.

*Bounding S₃.* At i = 1: |x_{−2} − x_0| = 1. At i = 2: |x_{−1} − x_1| = x_1 ≤ 1. For i ≥ 3, substituting j = i−1 gives |x_{j−2} − x_j| with j ∈ [2, N−1] ⊆ [1, N], contributing at most d₂. Total: S₃ ≤ d₂ + 2.

Combining: d₁ ≤ d₅ + 2d₂ + 4. □

**Corollary.** d₁ ≤ 6gN + 10.

*Proof.* By Lemma 1a: d₅ ≤ 2G₅ + 4 ≤ 2gN + 4 and d₂ ≤ 2G₂ + 1 ≤ 2gN + 1. Substituting into Lemma 1b: d₁ ≤ (2gN+4) + 2(2gN+1) + 4 = 6gN + 10. □

---

## Step 2: Halved Lipschitz

**Lemma 2a.** |G_{k+1} − G_k| ≤ (d₁ + 2)/2.

*Proof.* Consider the extended binary sequence

y = (y_{−1}, y_0, y_1, ..., y_N, y_{N+1}) = (0, 1, x_1, ..., x_N, 0).

Since y starts and ends at 0, define T⁺ = #{m : y_m = 1, y_{m+1} = 0} and T⁻ = #{m : y_m = 0, y_{m+1} = 1}. Every maximal run of 1s begins with an upward transition and ends with a downward transition, so T⁺ = T⁻.

The total variation V = T⁺ + T⁻ satisfies V = 1 + d₁ + x_N ≤ d₁ + 2, giving T⁺ = T⁻ = V/2 ≤ (d₁+2)/2.

Now write G_{k+1} − G_k = Σ_{n ∈ A^c ∩ [1,N]} (x_{n−k−1} − x_{n−k}). Each positive summand (x_{n−k−1}=1, x_{n−k}=0) corresponds to a downward transition in the x-sequence; each negative summand to an upward transition. Since we sum over a subset of all positions (only n ∈ A^c), the number of positive summands is at most T⁺ and negative summands at most T⁻. Therefore |G_{k+1} − G_k| ≤ max(T⁺, T⁻) = (d₁+2)/2. □

**Lemma 2b.** G_N ≤ gN for all N ≥ 2.

*Proof.* G_N = x_0(1−x_N) = 1−x_N ≤ 1. If gN ≥ 1 then G_N ≤ gN. If g = 0 then G₂ = 0; by the argument of Step 6, this forces x_i = 1 for all i ∈ [0,N], so G_N = 0 = gN. □

**Corollary.** G_k ≤ 4gN + 6 for all k ∈ [1, N].

*Proof.* B = 3ℕ+2 has consecutive gap 3, so every k ∈ [1, N−1] is within distance 1 of some b ∈ B ∩ [1, N], giving G_k ≤ G_b + (d₁+2)/2 ≤ gN + (6gN+12)/2 = 4gN + 6. For k = N: Lemma 2b gives G_N ≤ gN ≤ 4gN + 6. □

---

## Step 3: Average Gain Lower Bound

**Lemma 3.** Let S = Σ_{k=1}^N G_k, t = (1−δ)N, and {c₁ < ··· < c_t} = A^c ∩ [1,N]. Then S ≥ α(1−δ)²N²/(2(1−α)).

*Proof.*

(a) S = Σ_{j=1}^t |A ∩ [0, c_j−1]|. (Each pair (m,n) with m ∈ A, n ∉ A, 0 ≤ m < n ≤ N contributes 1 to G_{n−m}.)

(b) Since 0 ∈ A: |A ∩ [0, c_j−1]| ≥ 1 + α(c_j−1).

(c) The Schnirelmann condition gives j ≤ |A^c ∩ [1,c_j]| ≤ (1−α)c_j, so c_j ≥ j/(1−α).

(d) Substituting: |A ∩ [0, c_j−1]| ≥ 1 + α(j/(1−α) − 1) = 1 − α + αj/(1−α).

(e) Summing: S ≥ t(1−α) + αt(t+1)/(2(1−α)).

Since both terms are non-negative and t(t+1) ≥ t²:

S ≥ αt²/(2(1−α)) = α(1−δ)²N²/(2(1−α)). □

---

## Step 4: Upper Bound on S

**Lemma 4.** For N ≥ 2: S ≤ 3gN² + 2gN + 4N + 4.

*Proof.* For k ∈ B_N := B ∩ [1,N]: G_k ≤ gN. For k ∉ B_N: G_k ≤ 4gN + 6. Therefore:

S ≤ |B_N| · gN + (N − |B_N|)(4gN + 6).

Now |B_N| = ⌊(N−2)/3⌋ + 1 for N ≥ 2, which satisfies |B_N| ≥ (N−1)/3. (Verification: N=2: 1 ≥ 1/3; N=3: 1 ≥ 2/3; N=4: 1 ≥ 1; N=5: 2 ≥ 4/3.) Therefore:

S ≤ |B_N| · gN + (N − |B_N|)(4gN + 6)
  = 4gN² + 6N − |B_N|(3gN + 6)
  ≤ 4gN² + 6N − ((N−1)/3)(3gN + 6)
  = 4gN² + 6N − (N−1)gN − 2(N−1)
  = 3gN² + gN + 4N + 2
  ≤ 3gN² + 2gN + 4N + 4. □

---

## Step 5: Combining via h_N(δ)

For N ≥ 2, combining Lemmas 3 and 4 for a fixed δ ∈ [α, 1):

3gN² + 2gN + 4N + 4 ≥ α(1−δ)²N²/(2(1−α)).

Solving for g:

g ≥ α(1−δ)²N²/(2(1−α)(3N²+2N)) − (4N+4)/(3N²+2N).

The achieved density is δ + g, which satisfies δ + g ≥ h_N(δ) where

h_N(δ) := δ + α(1−δ)²N²/(2(1−α)(3N²+2N)) − (4N+4)/(3N²+2N).

**h_N is increasing on [α, 1).** We compute:

h_N'(δ) = 1 − α(1−δ)N²/((1−α)(3N²+2N)).

For δ ≥ α: 1−δ ≤ 1−α, so α(1−δ)N²/((1−α)(3N²+2N)) ≤ αN²/(3N²+2N) = α/(3+2/N) ≤ α/3 < 1. Hence h_N'(δ) > 0 on [α, 1).

**Minimum at δ = α.** Therefore, for all δ ∈ [α, 1):

δ + g ≥ h_N(δ) ≥ h_N(α) = α + [α(1−α)N²/2 − 4N − 4]/(3N²+2N).

Setting p = α(1−α), the condition h_N(α) ≥ α + p/15 is equivalent to:

[pN²/2 − 4N − 4]/(3N²+2N) ≥ p/15,

which rearranges to the quadratic:

(9p/2)N² − (2p+60)N − 60 ≥ 0.

The positive root is N* = [(2p+60) + √((2p+60)² + 1080p)]/(9p), giving threshold

N₀(α) = ⌈N*⌉.

---

## Step 6: Discrete Argument

For N ≥ 2, the shift b = 2 ∈ B is available.

**Case G₂ ≥ 1.** The density is δ + G₂/N ≥ α + 1/N ≥ α + p/15 whenever N ≤ 15/p.

**Case G₂ = 0.** For every i ∈ [1,N] with x_i = 0, we have x_{i−2} = 0 (contrapositive of G₂ = 0). Equivalently: x_m = 1 implies x_{m+2} = 1 for all m with m+2 ≤ N. Since x_0 = 1, inductively 2, 4, 6, ... ∈ A ∩ [1,N]. Since σ(A) = α > 0, |A ∩ {1}|/1 ≥ α > 0 forces x_1 = 1, and inductively 3, 5, 7, ... ∈ A ∩ [1,N]. So δ = 1 > α + p/15.

**N = 1.** |A ∩ {1}| ≥ α · 1 > 0, so |A ∩ {1}| = 1, density = 1 ≥ α + p/15. ✓

---

## Step 7: Regime Overlap

The discrete argument covers N ≤ ⌊15/p⌋. The continuous argument covers N ≥ N₀ = ⌈N*⌉.

We verify 15/p > N* for all p ∈ (0, 1/4], i.e.:

9p · (15/p) > (2p+60) + √((2p+60)² + 1080p)

135 > (2p+60) + √((2p+60)² + 1080p).

The right side is increasing in p. At p = 1/4 (the maximum, attained at α = 1/2):

RHS = 60.5 + √(60.5² + 270) = 60.5 + √(3930.25) ≈ 60.5 + 62.69 = 123.19 < 135. ✓

So 15/p > N* for all p ∈ (0, 1/4], confirming the overlap for every α ∈ (0, 1).

There is no gap. The theorem holds for all N ≥ 1. □

---

*Author: Mahmoud (MalekZ), March 19, 2026*
*AI assistance disclosed per forum rules: Claude (orchestration, computation, adversarial review), Gemini Deep Think (boundary analysis), GPT 5.4 (6 rounds adversarial review). All mathematics verified by the author.*
