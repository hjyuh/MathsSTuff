# Forum Post — Problem 396
# DRAFT — needs final review before posting

Some computational data and an observation on Problem 396.

## Extending A375077

Using a prime-by-prime Kummer carry check (no direct computation of `C(2k,k)`), I verified `a(1)` through `a(7)` and found:

**a(8) = 339,949,252.**

For each prime `p`, the check is: the number of carries when adding `k + k` in base `p` must be at least `Σ_{i=0}^{n} ν_p(k - i)`. The value `k = 339,949,252` passes for `n = 8`, and `k - 1 = 339,949,251` fails.

Updated table:

| `n` | `a(n)` | `a(n)/a(n-1)` |
|---|---|---|
| 1 | 2 | — |
| 2 | 2,480 | 1240 |
| 3 | 8,178 | 3.30 |
| 4 | 45,153 | 5.52 |
| 5 | 3,648,841 | 80.8 |
| 6 | 7,979,090 | 2.19 |
| 7 | 101,130,029 | 12.7 |
| 8 | 339,949,252 | 3.36 |

The ratios remain wildly irregular.

## A necessary smoothness condition

**Claim.** If `∏_{i=0}^{n}(K - i)` divides `C(2K, K)` and `K > n`, then every prime `p > 2n` dividing some `K - j` satisfies `p ≤ √(2K)`.

*Proof.* Suppose `p > 2n`, `p > √(2K)`, and `p | (K - j)` for some `0 ≤ j ≤ n`. Write `K = ap + j`. Since `p² > 2K`, we have `a < K/p < p/2`, so `K` has at most two base-`p` digits with leading digit `a < p/2` and units digit `j ≤ n < p/2`. Adding `K + K` in base `p`: the units digit gives `2j < p` (no carry), the leading digit gives `2a < p` (no carry). By Kummer's theorem, `ν_p(C(2K, K)) = 0`. But `ν_p(∏(K - i)) ≥ ν_p(K - j) ≥ 1`, so the divisibility fails. ∎

In other words: `P⁺(∏_{i=0}^{n}(K - i)) ≤ max(2n, ⌊√(2K)⌋)`.

## Empirical confirmation

For `a(8) = 339,949,252`, the bound gives `⌊√(2 · 339,949,252)⌋ = 26,075`. The actual largest prime factor across the block `k, k-1, ..., k-8` is `25,643` (from `k - 1 = 3³ · 491 · 25,643`). The margin is only `432`.

More strikingly, the factorization of the full block is:

| term | factorization | largest PF |
|---|---|---|
| `k` | `2² · 29 · 541 · 5417` | 5417 |
| `k-1` | `3³ · 491 · 25643` | 25643 |
| `k-2` | `2 · 5³ · 859 · 1583` | 1583 |
| `k-3` | `191 · 701 · 2539` | 2539 |
| `k-4` | `2⁶ · 3 · 743 · 2383` | 2383 |
| `k-5` | `11 · 73 · 331 · 1279` | 1279 |
| `k-6` | `2 · 7 · 13² · 23 · 6247` | 6247 |
| `k-7` | `3 · 5 · 41 · 79 · 6997` | 6997 |
| `k-8` | `2² · 4127 · 20593` | 20593 |

Every large prime factor `p > 31` has Kummer slack exactly `0`: `κ_p(k) = 1 = ν_p(k - j)`. The solution is completely saturated.

## Connection to #728

Problem #728 (arXiv:2601.07421) proved the existence of "carry-rich but spike-free" integers for ascending windows `m+1, ..., m+k` using the fact that when `p > 2k` and `p^r | (m+i)`, the low base-`p` digits of `m` are forced to be large, automatically producing carries (Lemma 5). For descending blocks `K, K-1, ..., K-n`, this mechanism reverses: `p | (K - j)` forces low digits of `K` to be *small*, so no carries are automatic. This is why the #728 argument does not directly prove `a(n) < ∞`.

The smoothness condition above makes this precise: the obstruction is not in the Kummer digit-pattern analysis (which #728 handles for small primes), but in controlling the large prime factors of the descending block. This aligns with Tao's observation (Sep 2025) that the initial difficulty is "securing a string of consecutive smooth numbers."

The problem thus decomposes into two parts:
1. **Digit-pattern control** for primes `p ≤ B(K)`: handled by #728-style carry-rich constructions.
2. **Smoothness control** ensuring `P⁺(∏(K-i)) ≤ √(2K)`: an arithmetic input that #728 does not provide.

For primes in the intermediate range `√K < p ≤ √(2K)`, the Kummer constraint allows at most one carry, and the data shows this is always achieved with zero margin. The "one-carry regime" appears to be the binding constraint in practice.

AI disclosure: computations in Python (Numba JIT) and verified against PARI/GP. The smoothness bound was identified with AI assistance (Claude, GPT, Codex). All computational claims and the proof above were checked by the author.
