# FIXES FOR BLOCKERS 2-3 + MINOR ISSUES
# Ready to merge into final proof once Blocker 1 (sieve) is resolved

## Fix for Blocker 2 (Step 3: Small Primes)

### Fixed Step 3: Small Primes (p ≤ Y)

**Lemma 3.1 (Valuation upper bound).** For any prime p and K ≥ n,
  Σ_{j=0}^n ν_p(K-j) = ν_p(∏_{j=0}^n(K-j)) = ν_p((n+1)! · C(K, n+1)) = ν_p((n+1)!) + ν_p(C(K,n+1)).
In particular, Σ ν_p(K-j) ≥ ν_p((n+1)!), and for the bottom A base-p digits fixed (via CRT), the value Σ ν_p(K-j) is determined by those digits. Call it R_p(r).

Define R_p := ν_p((n+1)!) (the minimum possible value of Σ ν_p(K-j) over K).

**Lemma 3.2 (Carries grow).** Fix a residue class K ≡ r (mod p^A). For K uniform in this class with K ≤ X, the number of carries κ_p(K) when doubling K in base p satisfies:

E[κ_p(K)] = (L_p - A)/2 + O_A(1)

where L_p = ⌊log_p X⌋ + 1. Moreover, by the spectral gap (1-1/p) of the carry Markov chain:

P(κ_p(K) < R_p) ≤ C · (1/p)^{(L_p-A)/2 - R_p} → 0 as X → ∞.

*Proof sketch.* The carries at digits ≥ A form a Markov chain with known transition matrix. The chain has stationary probability 1/2 for each state, so E[carries per digit] = 1/2. The spectral gap gives exponential concentration around the mean. Since L_p → ∞ and R_p is fixed, the probability of having fewer than R_p carries in O(L_p) digits vanishes geometrically. ∎

**Lemma 3.3 (CRT for small primes).** Choose Y ≥ n+1. For each p ≤ Y, choose the bottom A digits of K in base p to minimize R_p(r) (this is always achievable with R_p(r) ≤ ν_p((n+1)!) + A, a constant). By CRT (the p^A are coprime for distinct p), there exists r modulo Q_A = ∏_{p≤Y} p^A satisfying all choices simultaneously.

For K ≡ r (mod Q_A) with K ≤ X:
P(∃ p ≤ Y : κ_p(K) < R_p(r)) ≤ Σ_{p≤Y} C·(1/p)^{Ω(L_p)} → 0

since there are only π(Y) = O_n(1) primes and each probability vanishes. ∎

---

## Fix for Step 5 (Overlap check for ω(p))

**Lemma 5.1 (Distinct residue classes).** For p > n, the (n+1)⌈p/2⌉ residue classes {j + pt mod p² : 0 ≤ j ≤ n, 0 ≤ t < ⌈p/2⌉} are all distinct.

*Proof.* Suppose j₁ + pt₁ ≡ j₂ + pt₂ (mod p²). Then j₁ - j₂ ≡ p(t₂ - t₁) (mod p²). Since |j₁ - j₂| ≤ n < p, the LHS is not divisible by p unless j₁ = j₂. Then p(t₁ - t₂) ≡ 0 (mod p²), so t₁ ≡ t₂ (mod p). Since 0 ≤ t₁, t₂ < ⌈p/2⌉ < p, we get t₁ = t₂. ∎

---

## Fix for Step 2 (Squarefree sieve compatibility)

**Note.** The squarefree sieve condition (p² ∤ (K-j) for p > Y) is IMPLIED by the M_p sieve. Since M_p forbids residue classes j + pt mod p² for t = 0,...,⌈p/2⌉-1, in particular it forbids t = 0, i.e., K ≡ j (mod p²). So K ∉ M_p implies p² ∤ (K-j) for the relevant j. Hence the squarefree condition is redundant once the M_p sieve is applied.

---

## Fix for quantifier order (Minor issue 17)

Parameters are chosen in this order:
1. n is given (fixed throughout)
2. Y = Y(n) ≥ n+1 is chosen (depends only on n)
3. A = A(n,Y) is chosen (depends only on n, Y)
4. Q_A = ∏_{p≤Y} p^A is computed (fixed constant depending on n)
5. r (mod Q_A) is chosen for small primes (fixed)
6. X is taken sufficiently large (depending on all of the above)

No circularity: all parameters except X are fixed before X is chosen.

---

## Fix for Step 1 (Minor: explicit Kummer)

ν_p(C(2K,K)) = ν_p((2K)!) - 2ν_p(K!) = Σ_{t≥1}(⌊2K/p^t⌋ - 2⌊K/p^t⌋) = #{carries when adding K+K in base p} = κ_p(K).

The divisibility ∏(K-j) | C(2K,K) holds iff for every p, ν_p(∏(K-j)) ≤ ν_p(C(2K,K)), i.e., Σ_j ν_p(K-j) ≤ κ_p(K). ∎
