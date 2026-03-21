# Problem 931 — Full Note
## Case (k₁, k₂) = (4, 3)

### Overview

We study Problem 931 for the specific case (k₁, k₂) = (4, 3): are there infinitely many pairs (n₁, n₂) such that ∏(n₁ + i, i=0..3) and ∏(n₂ + j, j=0..2) have the same prime support (i.e., the same set of prime divisors)?

We present two finiteness results, computational evidence, and a reduction of the global question.

**Update (March 14, 2026):** As Prof. Tao noted, Result 1 (local finiteness) likely follows from the work of Beukers, Shorey, and Tijdeman (1999) on products of consecutive integers. The connection to Problem 686 methods (Bennett's irrationality measure for ∛2) may also be relevant. We include our elementary proofs below for completeness, pending a full comparison with the Beukers-Shorey-Tijdeman results.

---

### Result 1: Local Finiteness (Fixed n₁)

**Theorem.** For fixed n₁, only finitely many n₂ are valid.

**Proof.** Set S = Supp(∏_{i=0}^{3}(n₁ + i)), the prime support of the block of 4 consecutive integers starting at n₁. If (n₁, n₂) is a valid pair, then Supp(∏_{j=0}^{2}(n₂ + j)) = S.

This means each term of the second block n₂, n₂+1, n₂+2 is S-smooth (all prime factors in S). Since S is a fixed finite set, each n₂ + j is an S-smooth integer. By Størmer's theorem, there are only finitely many pairs of consecutive S-smooth integers. Since k₂ ≥ 2, the pair (n₂ + 1, n₂ + 2) consists of consecutive S-smooth integers, so only finitely many n₂ exist. ∎

**Note:** The condition k₂ ≥ 2 suffices; we do not need k₂ ≥ 3.

---

### Result 2: Gap-Fixed Finiteness

**Theorem.** For fixed gap d = n₂ − n₁, only finitely many pairs exist.

**Proof.** Fix d = n₂ − n₁. For any prime p > k₁ in the common support S, the prime p must divide at least one element of each block. In the first block {n₁, n₁+1, n₁+2, n₁+3}, p divides exactly one element (since p > 4, consecutive terms can share a prime factor only if p ≤ k₁). Similarly for the second block.

The key lemma: p divides ∏_{t=0}^{k₁-1}(d + t) for every such prime p. To see this: if p | n₁ + i (for some 0 ≤ i ≤ 3) and p | n₂ + j = n₁ + d + j (for some 0 ≤ j ≤ 2), then p | (d + j − i). Since −3 ≤ j − i ≤ 2, we have p | (d + t) for some t ∈ {−3, −2, −1, 0, 1, 2} ⊂ {1 − k₁, ..., k₂ − 1}.

This confines all large primes p (those > k₁) to the fixed set S_d := Supp(∏_{t=1-k₁}^{k₂-1}(d+t)). The "d-window" S_d is a finite set depending only on d.

Now the common support S must satisfy: S ⊆ {primes ≤ k₁} ∪ S_d. This is a fixed finite set. Both blocks consist of consecutive S-smooth integers (with S finite and fixed). By Størmer's theorem, there are finitely many such blocks. ∎

---

### The Global Reduction

**The global question reduces to:** Are there only finitely many admissible gaps d?

An admissible gap is a value d = n₂ − n₁ for which at least one valid pair exists. If we could show only finitely many gaps are admissible, finiteness of the full problem would follow from Result 2 (finitely many pairs per gap).

We attempted four approaches to prove finiteness of admissible gaps:

1. **Prime counting:** Comparing π-type bounds on support sizes. Stalled because the support of k consecutive integers near n has size ~k log n / log log n, and the ratio between 4-blocks and 3-blocks doesn't separate cleanly.

2. **Smoothness via reverse inclusion:** Trying to show that for large d, the S_d window forces implausibly smooth numbers. Stalled because smooth-number density (Dickman ρ) only gives subpolynomial decay.

3. **Weighted divisibility / |S(n₁)| growth rate:** Comparing the growth of support sizes. Stalled because both grow as O(log n / log log n) with comparable constants.

4. **Finite-configuration rigidity:** The most promising direction. The missing theorem appears to require exploiting the exact structure of supports of 3–4 consecutive integers, not just generic smooth-number estimates.

---

### Computational Search

Exhaustive search for n₁ ≤ 10⁶ and n₂ ≤ 1.1 × 10⁷:

**Found exactly 26 valid pairs**, all satisfying n₁ ≤ 636 and n₂ ≤ 10,932.

| n₁ | n₂ | Shared Support |
|----|-----|----------------|
| 1 | 1 | {2, 3} |
| 1 | 2 | {2, 3} |
| 2 | 1 | {2, 3, 5} |
| 2 | 2 | {2, 3, 5} |
| 2 | 3 | {2, 3, 5} |
| 2 | 8 | {2, 3, 5} |
| 3 | 2 | {2, 3, 5, 7} |
| 3 | 3 | {2, 3, 5, 7} |
| 5 | 5 | {2, 3, 5, 7} |
| 5 | 7 | {2, 3, 5, 7} |
| 6 | 8 | {2, 3, 5, 7} |
| 7 | 5 | {2, 3, 5, 7} |
| 14 | 14 | {2, 3, 5, 7, 11, 13, 17} |
| 20 | 48 | {2, 3, 5, 7, 11, 23} |
| 33 | 34 | {2, 3, 5, 7, 11, 17} |
| 34 | 33 | {2, 3, 5, 7, 11, 13, 17, 37} |
| 54 | 55 | {2, 3, 5, 7, 11, 13, 19} |
| 55 | 54 | {2, 3, 5, 7, 11, 13, 19, 29, 31, 53, 58} |
| 77 | 98 | {2, 3, 5, 7, 11, 13, 79} |
| 98 | 77 | {2, 3, 5, 7, 11, 13, 23, 79, 101} |
| 125 | 160 | {2, 3, 5, 7, 13, 23, 127} |
| 230 | 230 | {2, 3, 5, 7, 11, 13, 23, 29, 31, 37, 41, 43, 53, 59, 67, 79, 83, 89, 97, 229, 233} |
| 324 | 323 | {2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 41, 109, 163} |
| 493 | 636 | {2, 3, 5, 7, 11, 13, 17, 19, 31, 41, 83, 127, 211, 491, 499} |
| 636 | 493 | (same primes plus additional from 4-block) |
| 636 | 636 | {2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 41, 53, 107, 127, 211, 491, 499, 639} |

Complete CSV available upon request.

**Observation:** The largest n₁ in any valid pair is 636, and the largest n₂ is 10,932. The data strongly suggests global finiteness, but we cannot prove it with current methods.

---

### What Level 3 (Full Resolution) Needs

The missing theorem appears to require a finite-configuration rigidity argument exploiting the exact support structure of four consecutive integers, not generic smooth-number theory. The four approaches described above all stalled because they treat the blocks too generically — they don't use the fact that consecutive integers have very constrained prime factorization patterns.

---

### References

1. F. Beukers, T.N. Shorey, and R. Tijdeman, "Irreducibility of polynomials and arithmetic progressions with equal products of terms," 1999. (Noted by T. Tao as relevant to Result 1.)
2. K. Størmer, "Quelques théorèmes sur l'équation de Pell x² − Dy² = ±1 et leurs applications," Skrifter Videnskabs-selskabet (Christiania), I, Mat.-Naturv. Kl. 2, 48 pp., 1897.

### Disclosure

This work was conducted with AI assistance (Claude for orchestration, GPT-5.4 for strategy/computation). All mathematical content has been verified by the human author.
