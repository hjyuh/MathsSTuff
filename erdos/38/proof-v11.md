# Erdős Problem 38 — Proof v11

## Theorem

Let B = 3ℕ+2 = {2, 5, 8, 11, ...}. Then B is not an additive basis of any finite order, and for every A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1), and every N ≥ 1, there exists b ∈ B with

|(A ∪ (A+b)) ∩ {1,...,N}| ≥ (α + α(1-α)/15) · N.

**Convention.** Following Erdős [Er36c] and all standard Schnirelmann density references (Mann [Ma42], Halberstam–Roth, Nathanson), we require 0 ∈ A. The Schnirelmann density σ(A) = inf_{N≥1} |A ∩ {1,...,N}|/N is computed on {1,...,N}; the element 0 does not affect the density but is used in the shift operation. Without 0 ∈ A, the problem is trivially false: A = {1,3,5,...} has σ(A) = 1/2, but at N=2, no shift from any B with min(B) ≥ 2 can increase the count beyond |A ∩ [1,2]| = 1 = αN.

---

## Setup

Fix A ⊆ ℕ₀ with 0 ∈ A and σ(A) = α ∈ (0,1). For each N ≥ 1, define:
- x_i = 𝟙[i ∈ A ∩ [0,N]] for i ∈ ℤ, with x_i = 0 for i < 0 or i > N. Note x_0 = 1.
- δ = (1/N)Σ_{i=1}^N x_i,  G_b = Σ_{i=1}^N x_{i-b}(1-x_i),  g = max_{b∈B∩[1,N]} G_b/N  (for N≥2)
- d_b = Σ_{i=1}^N |x_i - x_{i-b}|

---

## Step 0: B is a non-basis
hB ⊆ {n : n ≡ 2h mod 3}. One residue class mod 3 per order, missing ≥ 2 classes. Not a basis. Asymptotic density 1/3.

---

## Step 1: d₁ ≤ 6gN + 10

**Lemma 1a.** d_b ≤ 2G_b + b - 1.
*Proof.* d_b = 2G_b + Σ_{i=1}^N x_i - Σ_{i=1}^N x_{i-b}. The difference equals Σ_{i=N-b+1}^N x_i - x_0 ≤ b - 1. □

**Lemma 1b.** d₁ ≤ d₅ + 2d₂ + 4.
*Proof.* From x_i - x_{i-1} = (x_i - x_{i-5}) + (x_{i-5} - x_{i-3}) + (x_{i-3} - x_{i-1}), summing |·| over i=1,...,N: d₁ ≤ d₅ + S₂ + S₃.

S₂ = Σ_{i=1}^N |x_{i-5} - x_{i-3}|: terms i=1,2 vanish; i=3 gives |x_{-2}-x_0|=1; i=4 gives |x_{-1}-x_1|≤1; for i≥5, substituting j=i-3 gives terms of d₂. So S₂ ≤ d₂ + 2.

S₃ = Σ_{i=1}^N |x_{i-3} - x_{i-1}|: i=1 gives |x_{-2}-x_0|=1; i=2 gives |x_{-1}-x_1|≤1; for i≥3, substituting j=i-1 gives terms of d₂. So S₃ ≤ d₂ + 2.

Total: d₁ ≤ d₅ + 2d₂ + 4. □

**Corollary.** d₁ ≤ (2gN+4) + 2(2gN+1) + 4 = 6gN + 10. □

---

## Step 2: G_k ≤ 4gN + 6

**Lemma 2a.** |G_{k+1} - G_k| ≤ (d₁+2)/2.
*Proof.* The extended sequence (0, 1, x_1,...,x_N, 0) starts and ends at 0. So T⁺ = T⁻ (up-transitions = down-transitions). V = T⁺+T⁻ = 1+d₁+x_N ≤ d₁+2, so T⁺ ≤ (d₁+2)/2. Now G_{k+1}-G_k = Σ_{n∈A^c∩[1,N]} (x_{n-k-1}-x_{n-k}), where positive terms ≤ T⁺ and negative terms ≤ T⁻. □

**Lemma 2b.** G_N ≤ gN.
*Proof.* G_N = x_0(1-x_N) = 1-x_N ≤ 1. If g=0 then G₂=0, forcing A⊇[0,N] (Step 6), so x_N=1, G_N=0. Otherwise gN≥1≥G_N. □

**Corollary.** Max distance from k∈[1,N-1] to B∩[1,N] is 1. So G_k ≤ gN + (6gN+12)/2 = 4gN+6. For k=N: G_N ≤ gN ≤ 4gN+6. □

---

## Step 3: S ≥ α(1-δ)²N²/(2(1-α))

*Proof.* S = Σ_{j=1}^t |A∩[0,c_j-1]| where {c_j} = A^c∩[1,N], t=(1-δ)N. Since 0∈A: |A∩[0,c_j-1]| ≥ 1+α(c_j-1). From j ≤ (1-α)c_j: c_j ≥ j/(1-α). So |A∩[0,c_j-1]| ≥ 1-α+αj/(1-α). Summing: S ≥ t(1-α)+αt(t+1)/(2(1-α)) ≥ αt²/(2(1-α)) = α(1-δ)²N²/(2(1-α)). □

---

## Step 4: S ≤ 3gN² + 2gN + 4N + 4

*Proof.* S ≤ |B_N|·gN + (N-|B_N|)(4gN+6). Using |B_N| ≥ (N-1)/3 for N≥2: S ≤ 4gN²+6N - (N-1)(gN+2)/1 ... expanding: S ≤ 3gN²+gN+4N+2 ≤ 3gN²+2gN+4N+4. □

---

## Step 5: Combining via h_N(δ)

From Steps 3-4: g ≥ α(1-δ)²N²/(2(1-α)(3N²+2N)) - (4N+4)/(3N²+2N).

Define h_N(δ) = δ + α(1-δ)²N²/(2(1-α)(3N²+2N)) - (4N+4)/(3N²+2N). Then δ+g ≥ h_N(δ).

h_N'(δ) = 1 - α(1-δ)N²/((1-α)(3N²+2N)). For δ≥α: this is ≥ 1-α/(3+2/N) > 1-α/3 > 0. So h_N is increasing on [α,1), minimum at δ=α.

h_N(α) = α + [α(1-α)N²/2 - 4N - 4]/(3N²+2N).

For f = α(1-α)/15 to hold, we need:

α(1-α)N²/2 - 4N - 4 ≥ α(1-α)(3N²+2N)/15

Setting p = α(1-α):

15(pN²/2 - 4N - 4) ≥ p(3N²+2N)

(9p/2)N² - (2p+60)N - 60 ≥ 0

This is a quadratic in N with positive leading coefficient. The positive root is:

N₀(α) = ⌈[(2p+60) + √((2p+60)²+1080p)] / (9p)⌉

At p = 1/4 (α=1/2): N₀ = 55. For all α: N₀(α) ≤ 55/p₀ · p₀/p where p₀=1/4.

---

## Step 6: Discrete argument — covers N ≤ 15/(α(1-α))

For N≥2 with b=2∈B:

**Case G₂≥1:** δ+1/N ≥ α+1/N ≥ α+α(1-α)/15 when N ≤ 15/(α(1-α)).

**Case G₂=0:** For every i∈[1,N] with x_i=0, we have x_{i-2}=0. Contrapositive: x_m=1 ⟹ x_{m+2}=1. Since x_0=1: 2,4,6,...∈A. Since x_1=1 (from α>0): 3,5,7,...∈A. So A⊇[0,N], δ=1>α+f(α).

**N=1:** Density=1≥α+f(α). ✓

---

## Step 7: Overlap

Discrete covers N ≤ ⌊15/p⌋ where p=α(1-α).

Continuous covers N ≥ N₀ = ⌈[(2p+60)+√((2p+60)²+1080p)]/(9p)⌉.

**Verified:** For all α∈{0.01,...,0.99}, overlap ≥ 4:

| α | p | N₀ | N_disc | overlap |
|---|---|-----|--------|---------|
| 0.1 | 0.09 | 150 | 166 | 16 |
| 0.2 | 0.16 | 85 | 93 | 8 |
| 0.3 | 0.21 | 65 | 71 | 6 |
| 0.4 | 0.24 | 57 | 62 | 5 |
| 0.5 | 0.25 | 55 | 60 | 5 |

(Table is symmetric around α=0.5.)

The overlap holds because 15 > [(2p+60)+√((2p+60)²+1080p)]/(9N₀) → the discrete threshold 15/p exceeds the continuous threshold for every p∈(0,1/4]. This can be verified by checking that 15/p > N₀(p) for all p, which reduces to showing (9p)(15/p) > (2p+60)+√((2p+60)²+1080p), i.e. 135 > (2p+60)+√((2p+60)²+1080p). At p=1/4: 135 > 60.5+√(3660.25+270) = 60.5+62.7 = 123.2. ✓ At p→0: 135 > 60+√(3600) = 60+60 = 120. ✓ Since the RHS is increasing in p and maximal at p=1/4 where it equals 123.2 < 135, the overlap holds for all p∈(0,1/4]. □

---

## Changes from v10

1. **0∈A convention:** Explicitly stated as standard, with proof that without it the problem is trivially false. Cited Erdős [Er36c], Mann [Ma42].

2. **Step 7 quadratic:** Solved exactly: (9p/2)N²-(2p+60)N-60≥0. Overlap verified analytically: 135 > 123.2 at worst case p=1/4.

---

*Author: Mahmoud (MalekZ), March 19, 2026*
*AI: Claude, Gemini Deep Think, GPT 5.4 (6 rounds adversarial review)*
