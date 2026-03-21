# Bridge 1: Short-Block Pair Theorem — Exact Statement and GPT Prompt

March 16, 2026

## Context

The pair large-prime tail T_{j1,j2}(X;a,q) counts K ∈ (X,2X] with K ≡ a (mod q) such that BOTH K-j1 and K-j2 have a prime factor > √(2X).

After the gcd factorization (Codex, codex-pair-linearization.md), this decomposes as:

T_{j1,j2}(X;a,q) = Σ_{g|d} Σ_{(u,v)=1} 1_{Δ|(a-j1-gur)} · N_{g,u,v}(X;a,q)

where d = j2-j1, and N_{g,u,v} counts s in an interval J of length H = XΔ/(qguv) + O(1) such that two linear forms L1(s) = A1·s + B1 and L2(s) = A2·s + B2 are both prime > y = √(2X).

The LONG-BLOCK regime (H ≥ X^ε) is already handled (Codex proved: contribution is O(X/q)).

## THE EXACT THEOREM TARGET (Bridge 1)

**Short-block pair theorem:** For fixed n, q, a, ε > 0, and distinct j1 ≠ j2:

  T^{short}_{j1,j2}(X;a,q) := Σ over (g,u,v) with H_{g,u,v} < X^ε of N_{g,u,v}(X;a,q) ≪_{n,q,ε} X/q

Equivalently: the total contribution from blocks where guv > c·X^{1-ε} is O(X/q).

## Why per-block sieve fails here

For a single short block with H < X^ε, the Selberg sieve gives N ≤ H/(log H)² + 1, and the "+1" term dominates. There are potentially ~X^{1-ε} such blocks (one for each (g,u,v) triple), so the total from the +1 terms alone is ~X^{1-ε}, which is NOT o(X/q) for any ε.

The resolution must use AVERAGING across the (g,u,v) family.

## Key structural features available for averaging

1. **Linear forms have coefficients depending on (u,v):** A1 = vm, A2 = um where m = q/Δ. So the leading coefficients vary across blocks.

2. **The primality condition couples L1 and L2:** We need BOTH to be prime. For a short interval, having even ONE prime in a short interval is rare. Having TWO is much rarer.

3. **The s-intervals for different (u,v) blocks are essentially disjoint in K-space:** Different (g,u,v) triples produce different values of K (because the factorizations K-j1 = gup1 are different).

4. **The constraint guv > cX^{1-ε} means at least one of g,u,v is large.** Since g|d and d ≤ n, g is bounded. So EITHER u or v (or both) must be ≥ X^{(1-ε)/2}/O(1).

5. **When u is large (u > X^{1/2-ε}): p1 = (K-j1)/(gu) < X^{1/2+ε}, so p1 is barely above √(2X).** This is a very constrained range for p1.

## Possible approaches

### Approach A: Double counting / switching
Count pairs (K, p1, p2) where both primes barely exceed √(2X). Since p_i is barely above √(2X) and m_i = (K-j_i)/p_i is barely below √(2X), the pair is constrained to a narrow band. The total number of such pairs can be bounded by counting from the prime side.

### Approach B: Large sieve over the coefficient family
The different blocks (u,v) produce linear forms with varying slopes. A large sieve inequality can exploit the fact that these slopes are "spread out" (since (u,v) ranges over coprime pairs).

### Approach C: Bombieri-Vinogradov averaging
For fixed p1, the condition that L2(s) = (K-j2)/g·v = c + u·(s - s0) is prime is a primality condition in a progression with modulus depending on u. BV gives this for most moduli u, which could handle most of the short blocks.

## GPT PROMPT

Below is the prompt to fire at GPT for the short-block theorem.

---

I'm working on Erdős Problem 396. After a series of reductions, I need to prove the following averaged theorem.

**Setup:** Fix integers n ≥ 1, q ≥ 1, a residue a mod q, and distinct shifts j1, j2 ∈ {0,...,n}. Put d = j2-j1, y = √(2X).

For each divisor g|d and coprime positive integers u,v < y/g, define linear forms in one variable s:
  L1(s) = A1·s + B1,  L2(s) = A2·s + B2
with A1 = v·(q/Δ), A2 = u·(q/Δ), where Δ = gcd(q, guv). The variable s ranges over an interval J_{g,u,v} of length H = XΔ/(q·g·u·v) + O(1).

Let N_{g,u,v} = #{s ∈ J : L1(s) and L2(s) are both prime > y}.

The **long-block** regime (H ≥ X^ε) is already handled: those blocks contribute O_{n,q,ε}(X/q) by a per-block Selberg sieve.

**The theorem I need:** The **short-block** regime (H < X^ε, equivalently guv > c·X^{1-ε}) also contributes O_{n,q,ε}(X/q). That is:

  Σ_{g|d} Σ_{u,v: (u,v)=1, guv > cX^{1-ε}} N_{g,u,v}(X;a,q) ≪_{n,q,ε} X/q

**Why per-block sieve fails:** Each block gives N ≤ 1 + H/(log H)², and there are ~X^{1-ε} blocks, so the trivial bound is X^{1-ε}, not X/q.

**Key constraint:** Since g|d and d ≤ n, g is bounded. So the short-block condition forces either u or v to be ≥ X^{(1-ε)/2}/O(1). This means the corresponding prime p_i = (K-j_i)/(g·u or g·v) is barely above y = √(2X).

**Three possible approaches I see:**

1. **Double counting from the prime side:** For each prime p1 in (y, y+y/X^{1/2-ε}), count how many K ∈ (X,2X] have K-j1 divisible by p1 AND K-j2 having a large prime factor. The number of such K for fixed p1 is O(X/(p1·log X)) by sieve, and summing over the narrow prime range gives O(X^{1/2+ε}/log X) = o(X).

2. **Bombieri-Vinogradov for the second prime:** Fix p1 > y dividing K-j1, so K is determined mod p1. Then K-j2 ≡ d (mod p1), and asking whether (K-j2)/something is prime is a question about primes in a progression. BV handles this for most moduli.

3. **Large sieve over the (u,v) family:** The slopes A1 = vm, A2 = um vary as (u,v) ranges over coprime pairs. A large sieve bound could show that on average, the N_{g,u,v} are small when the interval is short.

**Questions:**
1. Which of these three approaches (or a combination) is most likely to close?
2. Can you execute the double-counting argument (Approach A) and check if it gives the right bound?
3. Is there a standard reference for averaged binary prime counts over a family of linear forms with varying coefficients?

---

## Also needed: r=3 template

Once Bridge 1 is resolved for pairs, need to check whether the same method scales to triples. The r=3 analogue (codex-triple-linearization.md) reduces to three linear forms in one variable. If the pair method dies at triples, then a pair theorem alone doesn't finish 396.

## Status
- Theorem target precisely stated
- GPT prompt written
- Ready to fire
