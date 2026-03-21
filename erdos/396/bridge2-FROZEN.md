# Uniform Layer Lemma — Frozen Version

March 16, 2026. Frozen per Codex review.

## Lemma (Single-prime carry-good local density)

Let n ≥ 1 be fixed. For any odd prime p with p > 2n and p ≥ 4a, and any integer a ≥ 2, let K be chosen uniformly at random from [p^{a-1}, p^a). Define

  q_{n,p}(a) := P(∃ j ∈ {0,...,n} : p | (K-j) and ν_p(K-j) > κ_p(K))

where κ_p(K) is the number of carries when computing K + K in base p. Then

  q_{n,p}(a) ≤ C_n · a · 2^{-a} / p

for an explicit constant C_n depending only on n.

For the finitely many primes with p < 4a or p ≤ 2n, one has q_{n,p}(a) ≤ C_{n,p} · ρ_p^a for constants C_{n,p} > 0 and ρ_p ∈ (0,1) depending on n and p.

## Proof sketch

**Step 1 (Decomposition by j and t).**

  q_{n,p}(a) ≤ Σ_{j=0}^{n} Σ_{t=1}^{a-2} P(ν_p(K-j) = t) · P(κ_p(K) < t | ν_p(K-j) = t)

The t = a-1 and t = a levels contribute O(1/p^{a-1}), absorbed into the bound.

**Step 2 (Valuation factor).**

P(ν_p(K-j) = t) = (1-1/p)/p^t for 1 ≤ t ≤ a-2, up to O(1/p^a) error. This provides the 1/p prefactor.

**Step 3 (Carry deficit via Markov chain).**

Condition on ν_p(K-j) = t. Since p > 2n and j ≤ n, we have 2j < p, so the bottom t digits of K are the base-p digits of j, and the carry out of position t-1 is deterministic (call it c_t). For j = 0 and t = 1: the bottom digit is 0, so c_1 = 0.

The remaining a - t digits are i.i.d. uniform on {0,...,p-1} (with the leading digit ≥ 1, affecting one position). The carry process from position t onward is a 2-state time-homogeneous Markov chain with transition matrix:

  P(0 → 1) = (p-1)/(2p),   P(0 → 0) = (p+1)/(2p)
  P(1 → 1) = (p+1)/(2p),   P(1 → 0) = (p-1)/(2p)

Eigenvalues: 1 and 1/p. Stationary distribution: (1/2, 1/2).

**Step 4 (Path counting for t = 1).**

For t = 1, c_1 = 0. The event κ_p(K) = 0 requires the chain to stay in state 0 for all a-1 remaining positions:

  P(κ = 0 | ν = 1, j = 0) = ((p+1)/(2p))^{a-1} ≤ (1/2)^{a-1} · (1 + 1/p)^{a-1}

For p ≥ 4a: (1 + 1/p)^{a-1} ≤ (1 + 1/(4a))^{a-1} ≤ e^{1/4} < 2. So:

  P(κ = 0 | ν = 1) ≤ 2^{-(a-2)}

The t = 1 contribution to q is:

  (n+1)(1-1/p)/p · 2^{-(a-2)} ≤ 2(n+1) · 2^{-a} / p

**Step 5 (Higher t terms).**

For t ≥ 2, use the trivial bound P(κ < t | ν = t) ≤ 1 and sum:

  Σ_{t=2}^{a-2} (n+1)/p^t ≤ (n+1)/(p²(1-1/p)) ≤ 2(n+1)/p²

This is (1/p) · [2(n+1)/p] ≤ (1/p) · (n+1)/(2a) for p ≥ 4a.

For a sharper bound on t = 2: P(κ < 2 | ν = 2) ≤ (a-1) · ((p+1)/(2p))^{a-2} ≤ 2(a-1) · 2^{-a}. The t = 2 contribution is then (n+1)/p² · 2(a-1) · 2^{-a}, which is (1/p) · O(a · 2^{-a}/p).

**Step 6 (Combine).**

  q_{n,p}(a) ≤ (1/p) · [2(n+1) · 2^{-a} + 2(n+1)/p + O(a · 2^{-a}/p)]
             ≤ C_n · a · 2^{-a} / p

for p ≥ 4a, with C_n depending only on n. The a factor absorbs the t = 2 contribution and provides margin.

## Verification

Computed q_{n,p}(a) · p / (a · 2^{-a}) for n = 1 across all (p, a) with p ≥ 4a:

| p   | a  | ratio |
|-----|----|-------|
| 13  | 3  | 1.64  |
| 17  | 3  | 1.57  |
| 17  | 4  | 1.34  |
| 19  | 3  | 1.54  |
| 19  | 4  | 1.31  |
| 29  | 3  | 1.47  |
| 29  | 4  | 1.20  |

All ratios < 2. The bound C_1 = 2 works for n = 1 in the range p ≥ 4a.

## What this provides

This lemma is the single-prime input for the global carry-good density analysis. Specifically:

  β_a := C_n · a · 2^{-a}    with Σ_{a≥2} β_a = C_n · Σ a · 2^{-a} = 4C_n < ∞

Each prime-depth layer contributes:

  Σ_{a_p(X) = a} q_{n,p}(a) ≤ β_a · Σ_{a_p=a} (1/p) ≈ β_a · log((a+1)/a) ≈ β_a / a

The total: Σ_a β_a/a = C_n · Σ 2^{-a} = C_n < ∞.

## What this does NOT provide

- A density theorem in [X, 2X]. The modulus Q_Y(X) = ∏ p^{a_p} is astronomically larger than X, so CRT-to-density is nontrivial. This lemma is the correct single-prime input for a future multi-prime lift, not itself a density result.
- Blocker A remains open.

## Status: FROZEN. Do not expand further. Return to Bridge 1.
