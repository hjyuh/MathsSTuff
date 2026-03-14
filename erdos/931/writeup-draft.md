# A Reduction of Erdős Problem 931 to Gap Finiteness with Computational Evidence for (4,3)

**Authors:** Mahmoud (with AI assistance from Claude, GPT-5.4, and GPT Deep Research)

**Date:** March 12, 2026

**Abstract:** We study Erdős Problem 931 in the special case (k₁, k₂) = (4, 3). The problem asks whether there are only finitely many pairs (n₁, n₂) with n₂ ≥ n₁ + k₁ such that the products ∏(n₁ + i) for 1 ≤ i ≤ k₁ and ∏(n₂ + j) for 1 ≤ j ≤ k₂ share the same set of prime divisors. We prove that the global problem reduces to showing finiteness of admissible gaps d = n₂ - n₁. Specifically, we establish (1) local finiteness: for each fixed n₁, only finitely many n₂ are valid, via S-unit equations; (2) gap-fixed finiteness: for each fixed gap d, only finitely many pairs exist, via a structural lemma confining large primes to a short interval around d. We present an exhaustive computational search for (4,3) through n₁ ≤ 10⁶ and n₂ ≤ 1.1 × 10⁷, finding exactly 26 solutions, all with n₁ ≤ 636 and n₂ ≤ 10,932. We survey the literature on effective S-unit bounds and consecutive smooth numbers, and identify the precise structural theorem needed to close the global finiteness question.

---

## 1. Introduction

### 1.1 The Problem

Let k₁ ≥ k₂ ≥ 3. Define

  A = ∏_{i=1}^{k₁} (n₁ + i),    B = ∏_{j=1}^{k₂} (n₂ + j).

Erdős Problem 931 asks: are there only finitely many n₂ ≥ n₁ + k₁ such that Supp(A) = Supp(B), where Supp denotes the set of prime divisors?

We study the case (k₁, k₂) = (4, 3), so A = (n₁+1)(n₁+2)(n₁+3)(n₁+4) and B = (n₂+1)(n₂+2)(n₂+3).

### 1.2 Summary of Results

We establish a three-level decomposition of the problem:

- **Level 1 (Theorem 1):** For fixed n₁, only finitely many n₂ are valid. (S-unit equations / Størmer's theorem.)
- **Level 2 (Theorem 2):** For fixed gap d = n₂ - n₁, only finitely many pairs (n₁, n₂) exist. (Structural d-window lemma + S-unit equations.)
- **Level 3 (Open):** Only finitely many gaps d are admissible.

We present exhaustive computational evidence for (4,3) and a literature survey identifying why current effective tools do not close Level 3.

---

## 2. Level 1: Local Finiteness

### Theorem 1

*For fixed n₁, k₁, k₂ with k₁ ≥ k₂ ≥ 2, there are only finitely many n₂ ≥ n₁ + k₁ such that Supp(A) = Supp(B).*

Note: k₂ ≥ 2 suffices; the condition k₂ ≥ 3 in the original problem is stronger than needed.

### Proof

Fix n₁ and k₁. Set

  S := Supp(∏_{i=1}^{k₁} (n₁ + i)).

Since n₁ and k₁ are fixed, S is a fixed finite set of primes.

If Supp(B) = S, then every prime dividing any term n₂ + j must lie in S. So each of n₂ + 1, n₂ + 2, ..., n₂ + k₂ is an S-smooth integer (all prime factors in S).

Since k₂ ≥ 2, the pair (n₂ + 1, n₂ + 2) consists of consecutive S-smooth integers. By Størmer's theorem, for any fixed finite prime set S, there are only finitely many consecutive positive integers that are both S-smooth. Therefore there are only finitely many valid n₂. □

---

## 3. Level 2: Gap-Fixed Finiteness

### 3.1 The d-Window Structural Lemma

**Lemma 1.** *Let d = n₂ - n₁ ≥ k₁. For any prime p > k₁ in the common support Supp(A) = Supp(B), we have*

  p | ∏_{t=1-k₁}^{k₂-1} (d + t).

*Proof.* Since p > k₁, the prime p divides at most one term in each block (both blocks have length ≤ k₁ < p). So there exist unique i ∈ {1, ..., k₁} and j ∈ {1, ..., k₂} with p | (n₁ + i) and p | (n₂ + j). Subtracting:

  p | (n₂ + j) - (n₁ + i) = d + (j - i).

Since j - i ∈ {1 - k₁, ..., k₂ - 1}, we have p | (d + t) for some t in this range. □

### 3.2 Support Containment

**Corollary.** *All primes > k₁ in the common support satisfy:*

  Supp_{> k₁}(A) ⊆ Supp(∏_{t=1-k₁}^{k₂-1} (d + t)).

### 3.3 Gap-Fixed Finiteness

**Theorem 2.** *For fixed d = n₂ - n₁, only finitely many pairs (n₁, n₂) satisfy Supp(A) = Supp(B).*

*Proof.* For fixed d, define

  S_d := {p : p ≤ k₁} ∪ Supp(∏_{t=1-k₁}^{k₂-1} (d + t)).

By the structural lemma, every prime in the common support lies in S_d. Since d is fixed, S_d is a fixed finite set. Every term in both blocks is S_d-smooth, so by the same Størmer/S-unit argument as Theorem 1, only finitely many n₁ (hence pairs) are valid. □

### 3.4 The Remaining Problem

**The global finiteness question reduces to:** *Are there only finitely many admissible gaps d?*

---

## 4. Approaches to Level 3

We attempted four approaches to Level 3 for (k₁, k₂) = (4, 3). Each provides partial insight but none closes the argument.

### 4.1 Prime Counting / Pigeonhole (Round 1)

For large n₁, at least k₁ - 1 = 3 of the four first-block terms have a prime factor > k₁ = 4. These give 3 distinct primes that must each divide one of the 6 d-window terms. By pigeonhole, some d-window term absorbs multiple large primes.

**Why it stalls:** Having multiple large prime factors is not a contradiction — integers with many prime factors exist infinitely often. The bound ω(R) ≥ k₁ - 1 is constant, not growing with n₁.

### 4.2 Smoothness via Reverse Inclusion (Round 2)

The reverse inclusion Supp(B) ⊆ Supp(A) forces every prime dividing the second block to satisfy p ≤ n₁ + k₁ =: y. So all k₂ = 3 terms of the second block are y-smooth.

**Why it stalls:** By the Dickman function, y-smooth numbers near x have density ρ(log x / log y), which is positive for any fixed ratio u = log x / log y. So y-smoothness alone cannot rule out solutions at polynomial scales. Concrete counterexample: the triple (7496643, 7496644, 7496645) is 97-smooth and lies between 97³ and 97⁴.

### 4.3 Combined Weighted Divisibility (Round 3)

For (4,3) explicitly, define L_i = large-prime kernel of (n₁ + i) and V_r = y-smooth radical of (d + r). The matching constraints give:

  L₁L₂L₃L₄ | V₋₃ · V₋₂² · V₋₁³ · V₀³ · V₁² · V₂.

**Why it stalls:** Computation shows L₁L₂L₃L₄ < U(d;y) on EVERY observed solution, with the ratio shrinking to 10⁻²¹. The weighted divisibility goes the wrong direction.

### 4.4 |S(n₁)| Growth Rate Comparison (Round 4)

|S(n₁)| ~ 4 log log n₁ by Erdős-Kac. Known Størmer/Lehmer bounds give the largest S-smooth triple as a function of S. If the reach grows slower than the required n₂, Level 3 closes.

**Why it stalls:** Any reach bound of the form T(n₁) ≤ f(n₁) (however small) still allows infinitely many pairs unless f(n₁) forces a bounded gap. Current explicit bounds (Baker/Lehmer) are astronomically large and insensitive to the arithmetic structure of S(n₁).

---

## 5. Computational Results

### 5.1 Search Parameters

We performed an exhaustive search for (k₁, k₂) = (4, 3) with:
- n₁ ≤ 10⁶
- n₂ ≤ 1.1 × 10⁷
- Checking Supp((n₁+1)(n₁+2)(n₁+3)(n₁+4)) = Supp((n₂+1)(n₂+2)(n₂+3))

### 5.2 Results

Exactly **26 valid pairs** were found. Key statistics:
- All solutions satisfy n₁ ≤ 636 and n₂ ≤ 10,932
- No solutions exist for 10,932 < n₂ ≤ 11,000,000
- The largest gap is d = 10,296 (for the pair (636, 10932))
- Support sets range from |S| = 3 to |S| = 8

### 5.3 Complete Solution Table

| n₁ | n₂ | d | Support | |S| |
|----|------|-------|---------|-----|
| 1 | 7 | 6 | {2,3,5} | 3 |
| 2 | 7 | 5 | {2,3,5} | 3 |
| 3 | 13 | 10 | {2,3,5,7} | 4 |
| 3 | 47 | 44 | {2,3,5,7} | 4 |
| 4 | 13 | 9 | {2,3,5,7} | 4 |
| 4 | 47 | 43 | {2,3,5,7} | 4 |
| 6 | 13 | 7 | {2,3,5,7} | 4 |
| 6 | 47 | 41 | {2,3,5,7} | 4 |
| 9 | 63 | 54 | {2,3,5,11,13} | 5 |
| 11 | 62 | 51 | {2,3,5,7,13} | 5 |
| 12 | 62 | 50 | {2,3,5,7,13} | 5 |
| 13 | 33 | 20 | {2,3,5,7,17} | 5 |
| 13 | 48 | 35 | {2,3,5,7,17} | 5 |
| 18 | 54 | 36 | {2,3,5,7,11,19} | 6 |
| 18 | 74 | 56 | {2,3,5,7,11,19} | 6 |
| 21 | 43 | 22 | {2,3,5,11,23} | 5 |
| 24 | 62 | 38 | {2,3,5,7,13} | 5 |
| 31 | 118 | 87 | {2,3,5,7,11,17} | 6 |
| 32 | 118 | 86 | {2,3,5,7,11,17} | 6 |
| 48 | 167 | 119 | {2,3,5,7,13,17} | 6 |
| 53 | 74 | 21 | {2,3,5,7,11,19} | 6 |
| 62 | 349 | 287 | {2,3,5,7,11,13} | 6 |
| 73 | 1329 | 1256 | {2,3,5,7,11,19,37} | 7 |
| 74 | 207 | 133 | {2,3,5,7,11,13,19} | 7 |
| 88 | 4093 | 4005 | {2,3,5,7,13,23,89} | 7 |
| 636 | 10932 | 10296 | {2,3,5,7,11,13,29,71} | 8 |

### 5.4 Observations

1. Solutions are extremely sparse and concentrated at small values.
2. The gap d grows much faster than n₁ (the largest has d/n₁ ≈ 16).
3. Support sets grow slowly with solution size.
4. The weighted divisibility ratio L₁L₂L₃L₄/U(d;y) shrinks dramatically on each solution (from 0.04 to 3.7 × 10⁻²¹), confirming the Round 3 approach fails.

---

## 6. Literature Survey and the Quantitative Gap

### 6.1 What Existing Tools Can Do

- **For each fixed n₁:** Størmer/Lehmer Pell-equation methods can compute ALL valid n₂ by enumerating S(n₁)-smooth consecutive triples. This is fully effective for |S| ≈ 5-8.
- **For each fixed d:** The Level 2 reduction packages primes into a finite set S_d, giving complete computability.

### 6.2 What Existing Tools Cannot Do

- **Baker-type explicit bounds** (Győry 1979, Bugeaud-Győry 1996, Győry 2019) give computable upper bounds for S-unit equations but are "too large for practical use" (Evertse-Győry, Cambridge Monographs 2015). Even after LLL reduction (de Weger 1987), the bounds for S = {2,3,5,7,11,13,29,71} vastly exceed 10⁷.
- **Lehmer's 1964 tables** show that for S = first t primes up to 41, the largest S-smooth neighbor is already ~6.4 × 10¹⁰. A uniform Størmer function f(y) exists but is far too large to be useful.
- **Dickman-type estimates** give average density of y-smooth numbers but do not control S-smooth consecutive triples for sparse specific S.
- **Our computation cannot be "promoted to proof"** via existing Baker bounds without a new structural ingredient.

### 6.3 The Missing Theorem

The needed result must exploit the special structure of S(n₁) = Supp((n₁+1)(n₁+2)(n₁+3)(n₁+4)), not merely its size or maximum element. The precise open question is:

**Conjecture.** *For (k₁, k₂) = (4, 3), there exists D such that for all sufficiently large n₁, if x, x+1, x+2 are S(n₁)-smooth, then x ≤ n₁ + D.*

Or equivalently:

**Conjecture.** *For S(n₁) = Supp((n₁+1)(n₁+2)(n₁+3)(n₁+4)), only finitely many gaps d = n₂ - n₁ can occur with Supp(B) = S(n₁).*

---

## 7. Remarks on the Proof Landscape

Based on the four rounds of Level 3 attempts and the literature survey, we believe the eventual proof of global finiteness (if one exists) will not come from analytic estimates (Baker bounds, Dickman function, smooth number density). Instead, it will likely be a **finite-configuration rigidity argument** that:

1. Classifies the possible prime support shapes of four consecutive integers,
2. Determines which of those support shapes can be realized by three consecutive integers,
3. Exploits the "private" large primes (p ≥ 5 that are tagged to individual first-block terms) and their forced placement in the d-window,
4. Handles the small primes 2 and 3 separately, as they are the only source of overlap between block terms and likely conceal much of the real obstruction.

The computational evidence strongly supports the conjecture: 26 solutions, all small, with a sharp cutoff. The problem appears to be structurally rigid but poorly matched to standard tools — a genuine open question requiring a new lemma, not a routine application of existing machinery.

---

## 8. Acknowledgments

This work was conducted with AI assistance. Level 1 proof by Mahmoud. Level 2 reduction and Rounds 1-3 by GPT-5.4. Computational search by GPT-5.4. Literature survey by GPT Deep Research. Orchestration, analysis, and mathematical direction by Mahmoud with Claude (Anthropic).

---

## References

1. Størmer, C. (1897). "Quelques théorèmes sur l'équation de Pell x² - Dy² = ±1 et leurs applications." *Skr. Vidensk.-Selsk. Christiania*, I, No. 2.
2. Lehmer, D. H. (1964). "On a problem of Størmer." *Illinois Journal of Mathematics*, 8(1), 57-79.
3. Evertse, J.-H., Győry, K. (2015). *Unit Equations in Diophantine Number Theory.* Cambridge University Press.
4. Győry, K. (2019). "Bounds for the solutions of S-unit equations and decomposable form equations II." arXiv:1901.11289.
5. Bugeaud, Y., Győry, K. (1996). "Bounds for the solutions of unit equations." *Acta Arithmetica*, 74(1), 67-80.
6. de Weger, B. M. M. (1987). "Algorithms for Diophantine equations." *CWI Tract*, 65.
7. Smart, N. P. (1999). "Determining the small solutions to S-unit equations." *Mathematics of Computation*, 68(228), 1687-1699.
8. Evertse, J.-H., Győry, K., Stewart, C. L., Tijdeman, R. (1988). "S-unit equations and their applications." In *New Advances in Transcendence Theory*, Cambridge University Press.
9. Bloom, T. F. Erdős Problem 931. https://www.erdosproblems.com/931

---

*Last updated: March 12, 2026*
*Computational data: k4k3_pairs_to_1_1e7_combined.csv (26 solutions)*
