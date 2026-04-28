# EP699 Research Starts

Researched: 2026-04-26

## Statement and Status

EP699 asks whether for every `1 <= i < j <= n/2` there is a prime `p >= i`
such that

```tex
p \mid \gcd\left(\binom{n}{i}, \binom{n}{j}\right).
```

The problem is still listed as open/falsifiable on ErdosProblems. I found no
claimed proof or counterexample in current web sources beyond the official page
and its January 2026 discussion thread. The original Erdos-Szekeres paper states
the conjecture in terms of the greatest prime factor of the gcd and calls the
problem probably very deep.

## Known Results and Partials

- Erdos-Szekeres proved the baseline fact
  `gcd(binomial(n,i), binomial(n,j)) > 1` for `0 < i < j <= n/2`. This already
  proves EP699 for `i = 1` and `i = 2`.
- Sylvester-Schur gives, for each `1 <= i <= n/2`, a prime `p > i` dividing
  `binomial(n,i)`. A useful reduction: if such a prime also satisfies `p > j`,
  then it automatically divides `binomial(n,j)`, because for `p > j`,
  `p | binomial(n,k)` iff `n mod p < k`.
- Erdos-Szekeres proposed the stronger variant with `p > i`, except for a few
  special cases. Known strong-variant failures include `i = 2` at special powers
  of 2, scattered `i = 3` examples, and the famous `i >= 4` example
  `gcd(binomial(28,5), binomial(28,14)) = 2^3 * 3^3 * 5`. This does not refute
  EP699 because the shared prime `5` is exactly `i`.
- Bergman resolved the neighboring growth problem EP698: for
  `2 <= i < j <= n/2`,
  `gcd(binomial(n,i), binomial(n,j)) >> n^(1/2) 2^i / i^(3/2)`. This proves the
  gcd is large, but not that it has a prime factor at least `i`.

## Latest Literature and Comments

- The ErdosProblems page was last edited 2025-09-30 and currently has a Lean
  formalized statement link.
- The January 2026 forum thread reports an unverified Rust computation checking
  the official statement for all `n <= 10^7`, plus targeted rows `n = 2^k` for
  `k <= 27` and `n = 3^m + 1` for `m <= 17`, with no EP699 counterexamples.
  The same run logs only strong-variant near misses, where the common large
  prime is exactly `p = i`.
- The Rust scanner is public and documents Lucas/Legendre divisibility, bitset
  support sets, resumable JSONL logs, and the exact 10M and targeted-family
  runs.
- Adjacent least-prime-factor work around "good binomial coefficients" and the
  Erdos-Selfridge function is relevant for technique but does not appear to
  settle EP699. Konyagin gives lower bounds for the Erdos-Selfridge function,
  and Sorenson-Sorenson-Webster give a modern algorithmic treatment.
- Bergman's multinomial-coefficient paper is the closest peer-reviewed adjacent
  source I found for gcds of binomial coefficients of equal weight.

## Natural First Attack Routes

1. Exploit the `p > j` reduction. Try to show that `binomial(n,i)` has a prime
   divisor `p > j` in large ranges. The hard cases are exactly those where all
   Sylvester-Schur primes for `binomial(n,i)` lie in `(i,j]`.
2. Classify failures of the stronger `p > i` statement. The computation suggests
   that known near misses still satisfy EP699 via `p = i`. Proving that every
   no-`p>i` case has `i` prime and `i | gcd(...)` would prove the official
   problem in that regime.
3. Use a smoothness contradiction. A counterexample forces the gcd to be
   `(i-1)`-smooth. Bergman's lower bound then requires high powers of small
   primes. Kummer/Legendre digit constraints may make that impossible for fixed
   small `i`, or reduce it to finite automata over residues.
4. Recast as a residue covering problem. For each prime `p >= i`, Lucas gives a
   forbidden residue/digit set for `n` where both binomial coefficients vanish
   mod `p`. A counterexample must avoid all these sets. This is well suited to
   CRT sieving and may yield rigorous finite exclusions for bounded `i` or
   bounded `j/i`.

## Computational and Formalization Hooks

- Computation: reuse or audit `conglu1997/erdos_699_rust`. The immediate
  reproducibility task is to verify the 10M run from source, not just trust the
  forum comment. Its bitset design is the right shape: for each row `n`, store
  prime support sets for `binomial(n,k)` and test intersections with primes
  `>= i`.
- Fast divisibility tests: Lucas gives `p | binomial(n,k)` iff some base-`p`
  digit of `k` exceeds the corresponding digit of `n`; Legendre/Kummer gives
  valuations by floor sums or carries.
- Formalization: the formal-conjectures repository has `Erdos699.lean` with the
  statement and a stub for Sylvester-Schur. Mathlib already has Lucas theorem for
  `Nat.choose`; useful first lemmas include the `p > j` reduction and the
  Lucas digit criterion for divisibility by a prime.

## Risks and Unknowns

- A full proof likely needs more than size bounds: a large gcd can still be very
  smooth.
- Prime distribution in the intervals from `n mod p < i` can become a short
  interval problem, especially when `i` is small relative to `j`.
- Current computation is useful but unverified in this workspace; there is no
  independent certificate for the 10M sweep.
- Literature search found adjacent work, not a decisive modern attack on the
  largest-prime-factor-of-gcd formulation.

## Tractability Score

3/10 for a serious proof/counterexample attempt over the next few days. A useful
partial or verified computational extension is much more plausible than a full
resolution.

## Three Concrete Next Steps

1. Clone/audit the Rust scanner, reproduce the small sanity runs, then verify the
   published near-miss rows and gcd factorizations.
2. Prove and write down the `p > j` lemma formally; use it to reduce searches to
   rows/pairs where all primes `> i` dividing `binomial(n,i)` are at most `j`.
3. Pick fixed `i = 3,4,5` and build a residue/Kummer analysis for hypothetical
   counterexamples where the gcd is `(i-1)`-smooth.

## Sources

- ErdosProblems EP699: https://www.erdosproblems.com/699
- EP699 discussion thread: https://www.erdosproblems.com/forum/thread/699
- Erdos-Szekeres, "Some number theoretic problems on binomial coefficients":
  https://www.renyi.hu/~p_erdos/1978-46.pdf
- Bergman, "On common divisors of multinomial coefficients":
  https://arxiv.org/abs/0806.0607 and
  https://doi.org/10.1017/S0004972710001723
- ErdosProblems EP698, Bergman's related gcd-growth result:
  https://www.erdosproblems.com/698
- Rust scanner: https://github.com/conglu1997/erdos_699_rust
- Formalized EP699 statement:
  https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/699.lean
- Mathlib Lucas theorem docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Lucas.html
- Granville, binomial coefficients modulo prime powers:
  https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/binomial.html
- MathWorld, good binomial coefficient / Erdos-Selfridge context:
  https://mathworld.wolfram.com/GoodBinomialCoefficient.html
- Konyagin, least prime factor of a binomial coefficient:
  https://doi.org/10.1112/S0025579300007555
- Sorenson-Sorenson-Webster, algorithm and estimates for the Erdos-Selfridge
  function: https://www.math.auckland.ac.nz/~sgal018/ANTS/papers/Sorenson-Sorenson-Webster.pdf
