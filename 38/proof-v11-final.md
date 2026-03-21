# Erdős Problem 38 — Proof (Post-Ready v11-final)

**Convention.** Throughout, we use the standard Schnirelmann density convention: 0 ∈ A for every set A under consideration. This is universal in the Schnirelmann density literature (Schnirelmann [1930], Erdős [Er36c], Mann [Ma42], Nathanson). The Schnirelmann density σ(A) = inf_{N≥1} |A ∩ {1,...,N}|/N is computed on {1,...,N}; the element 0 does not affect the density but participates in shifts. Without 0 ∈ A, the problem is trivially false at small N for any B with min(B) ≥ 2: take A = {1,3,5,...}, N = 2.

---

## Theorem

Let B = 3ℕ+2 = {2, 5, 8, 11, 14, ...}. Then B is not an additive basis of any finite order, and for every A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1), and every N ≥ 1, there exists b ∈ B such that

|(A ∪ (A+b)) ∩ {1,...,N}| ≥ (α + α(1-α)/15) · N.

---

## Setup

Fix infinite A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1). For each N ≥ 1, define:

- x_i = 𝟙[i ∈ A ∩ [0,N]] for i ∈ ℤ, with x_i = 0 for i < 0 or i > N. Note x_0 = 1.
- δ = (1/N) Σ_{i=1}^N x_i  (actual density in [1,N]; δ ≥ α)
- G_b = Σ_{i=1}^N x_{i-b}(1 - x_i)  (new elements from shift b)
- g = max_{b ∈ B ∩ [1,N]} G_b / N  (for N ≥ 2; N = 1 handled separately in Step 6)
- d_b = Σ_{i=1}^N |x_i - x_{i-b}|  (truncated symmetric variation)
- B_N = B ∩ [1,N],  t = (1-δ)N = |A^c ∩ [1,N]|

---

## Step 0: B is a non-basis

For any h ≥ 1, every element of hB satisfies b₁ + ··· + bₕ ≡ 2h (mod 3). Since 2h mod 3 is a single residue class, hB misses at least 2 of the 3 residue classes mod 3. So B is not an additive basis of any finite order. B has asymptotic density 1/3.

---

## Step 1: GCD Propagation — d₁ ≤ 6gN + 10

**Lemma 1a.** d_b ≤ 2G_b + b - 1.

*Proof.* Expanding: d_b = Σ_{i=1}^N (x_i + x_{i-b} - 2x_i x_{i-b}) = 2G_b + Σ_{i=1}^N x_i - Σ_{i=1}^N x_{i-b}. The difference of sums equals Σ_{i=N-b+1}^N x_i - Σ_{i=1-b}^0 x_i. The first sum is at most b. The second sum: only the i=0 term is nonzero (since x_j = 0 for j < 0), contributing x_0 = 1. So the difference ≤ b - 1. □

**Lemma 1b.** d₁ ≤ d₅ + 2d₂ + 4.

*Proof.* From the identity 5 - 2·2 = 1, decompose: x_i - x_{i-1} = (x_i - x_{i-5}) + (x_{i-5} - x_{i-3}) + (x_{i-3} - x_{i-1}).

By the triangle inequality, summing |·| over i = 1,...,N: d₁ ≤ d₅ + S₂ + S₃, where S₂ = Σ_{i=1}^N |x_{i-5} - x_{i-3}| and S₃ = Σ_{i=1}^N |x_{i-3} - x_{i-1}|.

**Bounding S₂:** i=1: |x_{-4}-x_{-2}|=0. i=2: |x_{-3}-x_{-1}|=0. i=3: |x_{-2}-x_0|=1. i=4: |x_{-1}-x_1|=x_1≤1. For i≥5: substituting j=i-3 gives |x_{j-2}-x_j| with j∈[2,N-3]⊆[1,N], contributing ≤ d₂. Total: S₂ ≤ d₂ + 2.

**Bounding S₃:** i=1: |x_{-2}-x_0|=1. i=2: |x_{-1}-x_1|=x_1≤1. For i≥3: substituting j=i-1 gives |x_{j-2}-x_j| with j∈[2,N-1]⊆[1,N], contributing ≤ d₂. Total: S₃ ≤ d₂ + 2.

**Combining:** d₁ ≤ d₅ + (d₂+2) + (d₂+2) = d₅ + 2d₂ + 4. □

**Corollary.** d₁ ≤ (2gN+4) + 2(2gN+1) + 4 = 6gN + 10. □

---

## Step 2: Halved Lipschitz — G_k ≤ 4gN + 6

**Lemma 2a.** |G_{k+1} - G_k| ≤ (d₁+2)/2.

*Proof.* Consider the extended binary sequence Y = (y_{-1}, y_0, y_1, ..., y_N, y_{N+1}) = (0, 1, x_1, ..., x_N, 0). This starts and ends at 0.

Define T⁺ = |{m : y_m=1, y_{m+1}=0}| and T⁻ = |{m : y_m=0, y_{m+1}=1}|. Since Y starts at 0 and ends at 0, every maximal run of 1s begins with an upward transition and ends with a downward transition, giving T⁺ = T⁻.

The total variation V = T⁺ + T⁻. Counting transitions: the m=-1 transition (0→1) contributes 1; transitions at m=0,...,N-1 contribute d₁; the m=N transition (x_N→0) contributes x_N. So V = 1 + d₁ + x_N ≤ d₁ + 2, giving T⁺ = V/2 ≤ (d₁+2)/2.

Now: G_{k+1} - G_k = Σ_{n ∈ A^c ∩ [1,N]} (x_{n-k-1} - x_{n-k}). Each positive summand (x_{n-k-1}=1, x_{n-k}=0) corresponds to a downward transition in the x-sequence. Each negative summand (x_{n-k-1}=0, x_{n-k}=1) corresponds to an upward transition. Since we sum over n ∈ A^c ∩ [1,N], a *subset* of all positions: the number of positive summands ≤ T⁺ and the number of negative summands ≤ T⁻. Therefore |G_{k+1}-G_k| ≤ max(T⁺, T⁻) = T⁺ ≤ (d₁+2)/2. □

**Lemma 2b.** G_N ≤ gN for all N ≥ 2.

*Proof.* G_N = Σ_{i=1}^N x_{i-N}(1-x_i) = x_0(1-x_N) = 1-x_N ≤ 1. If gN ≥ 1, then G_N ≤ 1 ≤ gN. If g = 0, then G₂ = 0, which by Step 6's argument forces A ⊇ [0,N], giving x_N = 1 and G_N = 0 = gN. □

**Corollary.** For all k ∈ [1,N]: G_k ≤ 4gN + 6.

*Proof.* B = 3ℕ+2 has consecutive gap 3. Every k ∈ [1,N-1] is within distance 1 of some b ∈ B_N. For such k: G_k ≤ G_b + (d₁+2)/2 ≤ gN + (6gN+12)/2 = 4gN + 6. For k = N: Lemma 2b gives G_N ≤ gN ≤ 4gN + 6. □

---

## Step 3: Average Gain Lower Bound — S ≥ α(1-δ)²N²/(2(1-α))

**Lemma 3.** Let S = Σ_{k=1}^N G_k. Then S ≥ α(1-δ)²N²/(2(1-α)).

*Proof.* Let A^c ∩ [1,N] = {c₁ < ··· < c_t}.

(a) S = Σ_{j=1}^t |A ∩ [0, c_j-1]|. (Each gap c_j collects all A-elements ≤ c_j-1, including 0.)

(b) Since 0 ∈ A: |A ∩ [0,c_j-1]| = 1 + |A ∩ [1,c_j-1]| ≥ 1 + α(c_j-1).

(c) From the Schnirelmann condition: j ≤ |A^c ∩ [1,c_j]| ≤ (1-α)c_j, so c_j ≥ j/(1-α).

(d) S ≥ Σ_{j=1}^t [1 + α(j/(1-α) - 1)] = Σ_{j=1}^t [(1-α) + αj/(1-α)] = t(1-α) + αt(t+1)/(2(1-α)).

(e) Since t(1-α) ≥ 0 and t+1 ≥ t: S ≥ αt²/(2(1-α)) = α(1-δ)²N²/(2(1-α)). □

---

## Step 4: Upper Bound — S ≤ 3gN² + 2gN + 4N + 4

**Lemma 4.** For N ≥ 2: S ≤ 3gN² + 2gN + 4N + 4.

*Proof.* For k ∈ B_N: G_k ≤ gN. For k ∉ B_N: G_k ≤ 4gN + 6. So S ≤ |B_N|·gN + (N-|B_N|)(4gN+6) = N(4gN+6) - |B_N|(3gN+6).

For N ≥ 2: |B_N| = ⌊(N-2)/3⌋ + 1 ≥ (N-1)/3. Substituting:

S ≤ 4gN² + 6N - ((N-1)/3)(3gN + 6) = 4gN² + 6N - (N-1)gN - 2(N-1) = 3gN² + gN + 4N + 2 ≤ 3gN² + 2gN + 4N + 4. □

---

## Step 5: Combining via h_N(δ)

From Steps 3 and 4, for any δ ∈ [α, 1):

α(1-δ)²N²/(2(1-α)) ≤ S ≤ 3gN² + 2gN + 4N + 4

Solving for g:

g ≥ α(1-δ)²N² / (2(1-α)(3N²+2N)) - (4N+4)/(3N²+2N)

The achieved density is δ + g. Define:

h_N(δ) = δ + α(1-δ)²N² / (2(1-α)(3N²+2N)) - (4N+4)/(3N²+2N)

Then δ + g ≥ h_N(δ).

**h_N is increasing on [α, 1):** h_N'(δ) = 1 - α(1-δ)N²/((1-α)(3N²+2N)). For δ ≥ α: (1-δ) ≤ (1-α), so α(1-δ)N²/((1-α)(3N²+2N)) ≤ αN²/(3N²+2N) = α/(3+2/N) ≤ α/3 < 1. Hence h_N'(δ) > 0.

**Minimum at δ = α:** h_N(α) = α + [α(1-α)N²/2 - 4N - 4]/(3N²+2N).

For f(α) = α(1-α)/15 to hold, we need h_N(α) ≥ α + α(1-α)/15, i.e.:

[α(1-α)N²/2 - 4N - 4]/(3N²+2N) ≥ α(1-α)/15

Setting p = α(1-α) and cross-multiplying:

(9p/2)N² - (2p+60)N - 60 ≥ 0

This quadratic in N has positive leading coefficient 9p/2 > 0. Its positive root is:

N₀(p) = [(2p+60) + √((2p+60)² + 1080p)] / (9p)

The continuous argument holds for all N ≥ ⌈N₀(p)⌉.

---

## Step 6: Discrete Argument — covers N ≤ 15/p

For N ≥ 2 (so that 2 ∈ B_N), consider the shift b = 2.

**Case 1: G₂ ≥ 1.** The density gain is at least 1/N: δ + G₂/N ≥ α + 1/N. This exceeds α + p/15 whenever N ≤ 15/p, i.e., N ≤ ⌊15/(α(1-α))⌋.

**Case 2: G₂ = 0.** For every i ∈ [1,N] with x_i = 0, we have x_{i-2} = 0. Contrapositive: x_m = 1 implies x_{m+2} = 1. Since x_0 = 1 (convention): 2 ∈ A, 4 ∈ A, ..., all even numbers ≤ N are in A. Since σ(A) = α > 0: |A ∩ {1}|/1 ≥ α > 0, so 1 ∈ A. Then 3 ∈ A, 5 ∈ A, ..., all odd numbers ≤ N are in A. Therefore δ = 1 > α + α(1-α)/15.

**N = 1:** |A ∩ {1}| ≥ α·1 > 0, so |A ∩ {1}| = 1 (it's an integer), giving density 1 ≥ α + f(α). ✓

---

## Step 7: Overlap — No gap for any α

The discrete argument covers all N ≤ ⌊15/p⌋.

The continuous argument covers all N ≥ ⌈N₀(p)⌉ where N₀(p) = [(2p+60)+√((2p+60)²+1080p)]/(9p).

**Claim:** 15/p > N₀(p) for all p ∈ (0, 1/4].

*Proof.* We need (9p)(15/p) > (2p+60) + √((2p+60)²+1080p), i.e.:

135 > (2p+60) + √((2p+60)²+1080p)

The right-hand side is increasing in p. At p = 1/4 (maximum, achieved at α = 1/2):

RHS = 60.5 + √(60.5² + 270) = 60.5 + √(3930.25) = 60.5 + 62.69... = 123.19... < 135. ✓

At p → 0⁺: RHS → 60 + √3600 = 60 + 60 = 120 < 135. ✓

Since RHS is continuous, increasing, and at its maximum (p=1/4) equals 123.2 < 135, the inequality holds for all p ∈ (0, 1/4]. Therefore ⌈N₀(p)⌉ ≤ ⌊15/p⌋ for all α ∈ (0,1), and the two regimes overlap. □

---

## Notes

1. The bound f(α) = α(1-α)/15 is not optimal. The continuous asymptotic gives f ≈ α(1-α)/6 for large N; the constant 15 is chosen to ensure clean overlap with the discrete regime.

2. Brauer [Br38] and Selberg [Se44] improved the constant in Erdős's basis result (where B is a basis of order k). Our result shows that the gain phenomenon extends beyond bases: B = 3ℕ+2 is not a basis of any order, yet still provides a positive density gain for every set A of positive Schnirelmann density.

3. All lemmas verified computationally for 8 adversary types at N = 50 and N = 200. Regime overlap verified for all α ∈ {0.01, 0.02, ..., 0.99}, with minimum overlap of 4.

---

*Author: Mahmoud (MalekZ), March 19, 2026*
*AI assistance disclosed per forum rules: Claude (orchestration, computation, adversarial review), Gemini Deep Think (boundary analysis, block averaging), GPT 5.4 (6 rounds adversarial review). All mathematics verified by the author.*
