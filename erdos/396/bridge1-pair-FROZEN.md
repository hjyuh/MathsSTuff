# Short-Block Pair Theorem — Careful Writeup

March 16, 2026. Cleanup per Codex stress points.

## Theorem

For fixed n ≥ 1, q ≥ 1, residue a mod q, ε > 0, and distinct shifts j₁ ≠ j₂ with d = j₂ - j₁:

  T^{short}_{j₁,j₂}(X;a,q) ≪_{n,q,ε} X/q

where T^{short} sums over the short-block regime defined precisely below.

## Setup (from codex-pair-linearization.md)

Let y = √(2X). For K ∈ (X, 2X] with K ≡ a mod q, the pair event E_{j₁}(K) ∧ E_{j₂}(K) means both K-j₁ and K-j₂ have a prime factor > y. This determines unique primes p₁, p₂ > y and cofactors m₁ = (K-j₁)/p₁, m₂ = (K-j₂)/p₂ with m_i < y.

Writing m₁ = gu, m₂ = gv with g = gcd(m₁,m₂), (u,v) = 1, we get g | d.

For fixed (g,u,v), the pair event parametrizes as:
  p₁ = B₁ + A₁s,  p₂ = B₂ + A₂s
with A₁ = v·(q/Δ), A₂ = u·(q/Δ), Δ = gcd(q, guv), and s ranging over an interval J_{g,u,v} of length:

  H_{g,u,v} = XΔ/(q·g·u·v) + O(1)

## Precise short-block condition

**Codex stress point #2:** The short-block condition is H_{g,u,v} < X^ε, which means:

  XΔ/(q·g·u·v) < X^ε  ⟺  guv > XΔ/(qX^ε) = X^{1-ε}·Δ/q

Since Δ = gcd(q, guv) ≤ q, we have X^{1-ε}·Δ/q ≤ X^{1-ε}. So:

  guv > X^{1-ε}·Δ/q ≥ X^{1-ε}/q·1 (when Δ=1)

For fixed q, this is still guv ≫_q X^{1-ε}. The Δ/q factor helps (makes the threshold smaller), so our argument is only strengthened.

**Working threshold:** guv > c_q · X^{1-ε} where c_q = 1/q (worst case Δ=1).

## Step 1: Both cofactors are large

Since g | d with |d| ≤ n, g is bounded: g ≤ n. Since v < y/g ≤ y:

  u > c_q · X^{1-ε}/(g·v) > c_q · X^{1-ε}/(n · y) = c_q · X^{1-ε}/(n·√(2X)) = c'_{n,q} · X^{1/2-ε}

Define U := c'_{n,q} · X^{1/2-ε}. Then u > U. By symmetry (swapping j₁ ↔ j₂ and u ↔ v), v > U also.

## Step 2: Upper bound by forgetting p₂

**Codex stress point #1 (injectivity):** Each K counted in T^{short} has a UNIQUE factorization K - j₁ = p₁ · (gu) with p₁ > y prime and gu < y (since K-j₁ ≤ 2X and p₁ > √(2X) forces (K-j₁)/p₁ < √(2X) = y). So the map K ↦ (g, u, p₁) is injective.

**Why forgetting p₂ gives an upper bound, not an overcount:**

For fixed (g, u), define:

  S_{g,u} := {K ∈ (X,2X] : K ≡ a mod q, K-j₁ = gu·p₁ with p₁ > y prime}

Then T^{short} counts a SUBSET of K's that additionally satisfy the p₂ condition. So:

  T^{short} ≤ Σ_{g|d} Σ_{u: u>U} |S_{g,u}|

This is valid because:
- Each K in T^{short} determines a unique (g,u,p₁) with u > U
- The set S_{g,u} counts ALL K with this (g,u) structure, regardless of the p₂ condition
- So T^{short} ⊆ ∪_{g,u} S_{g,u}

**Potential overcount issue:** Could one K appear in S_{g,u} for multiple values of (g,u)? NO, because g = gcd(m₁, m₂) and u = m₁/g are determined by K (once j₁, j₂ are fixed).

Wait — S_{g,u} doesn't know about j₂. It just counts K with K-j₁ = gu·p₁. The same K could have K-j₁ = g'u'·p'₁ for different (g',u')? NO: since K-j₁ < 2X and p₁ > y = √(2X), there is AT MOST ONE prime factor of K-j₁ exceeding y. So p₁ is unique, and m₁ = (K-j₁)/p₁ is unique, giving unique g = gcd(m₁, m₂) and u = m₁/g.

BUT: S_{g,u} doesn't involve m₂ at all. It counts K with K-j₁ = gu·p₁ for p₁ > y prime. The parameter g here is being summed over divisors of d, and u over U < u < y/g. For a given K, there's exactly one factorization K-j₁ = m₁·p₁, hence one m₁ = gu. But different choices of g | m₁ with u = m₁/g could place K in different (g,u) bins.

**Fix:** Actually, in the pair decomposition, g = gcd(m₁, m₂) is determined by K (since m₁ and m₂ are both determined by K). So K appears in exactly one (g,u) bin. No overcount.

**Alternative cleaner formulation:** Simply define M_u = #{primes p₁ ∈ (y, 2X/u] : p₁ ≡ (a-j₁)·(gu)^{-1} mod q/(q,gu), p₁ > y}. Then:

  T^{short} ≤ Σ_{g|d} Σ_{U<u<y/g} M_{g,u}

with no overcounting, since each K uniquely determines (g,u,p₁).

## Step 3: Count primes in one AP

For fixed (g,u): p₁ ranges over primes in an interval of length X/(gu), in one residue class mod q_{g,u} = q/gcd(q,gu).

By Brun-Titchmarsh:

  M_{g,u} ≪ X/(gu · φ(q_{g,u}) · log(X/(gu·q_{g,u})))

For gu < y and q fixed, log(X/(gu·q_{g,u})) ≫ log X. And φ(q_{g,u}) ≥ q_{g,u}/log log(2q). So:

  M_{g,u} ≪ X·gcd(q,gu) / (gu·q·log X) · log log(2q)

## Step 4: Sum over u > U

  Σ_{U<u<y/g} M_{g,u} ≪ (X·log log(2q))/(q·log X) · Σ_{U<u<y/g} gcd(q,gu)/(gu)

Since g is bounded (g | d, d ≤ n):

  Σ_u gcd(q,gu)/(gu) ≤ (1/g) Σ_u gcd(q,gu)/u

For fixed q, using Σ_{u≤Y} gcd(q,u)/u ≤ τ(q)·log Y:

  Σ_{U<u<y/g} gcd(q,gu)/(gu) ≪_q log(y/U) ≍ ε·log X

## Step 5: Combine

  T^{short} ≤ Σ_{g|d} [above] ≪_{n,q,ε} (X·log log(2q))/(q·log X) · ε·log X = X·ε·log log(2q)/q

Since ε and log log(2q) are absorbed into O_{n,q,ε}:

  T^{short} ≪_{n,q,ε} X/q  ∎

## Combined Result

Together with the long-block theorem (codex-pair-long-blocks.md):

  T_{j₁,j₂}(X;a,q) = T^{long} + T^{short} ≪_{n,q,ε} X/q

for all pairs of distinct shifts j₁ ≠ j₂.

## Stress Test Results

**Injectivity (Codex point a):** ✓ Each K uniquely determines (g,u,p₁) via the factorization K-j₁ = m₁·p₁ and g = gcd(m₁, m₂). No overcounting.

**Δ/q dependence (Codex point b):** ✓ The short-block condition H < X^ε translates to guv > X^{1-ε}·Δ/q. Since Δ ≤ q, this only lowers the threshold, strengthening the argument. The working threshold guv > X^{1-ε}/q suffices.

## Why This Is Pair-Specific

The miracle: guv > cX^{1-ε} with u,v < √X and g bounded forces BOTH u,v > c'X^{1/2-ε}.

For r=3: gu₁u₂u₃ > cX^{1-ε} with u_i < √X does NOT force all three large. Two can be X^{1/4} while the third is X^{1/2-ε}. The "forget all but one prime" argument requires ALL cofactors large.

## STATUS: FROZEN. Clean theorem, both stress points addressed.
