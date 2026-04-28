# Candidate Scout: tractable Erdos problems in divisor and multiplicative-number-theory territory

Date: 2026-04-26

Scope: open or still-interesting Erdos Problems in number theory, especially divisor functions, ordered divisors, prime-factor statistics, and multiplicative structures. I filtered out flagship-level problems whose main obstacle appears comparable to EP3-style breakthroughs. This is scouting only: no attempt is made to solve any problem.

## Ranking summary

| Rank | Problem | Short label | Difficulty | Secretly famous/hard risk | Why it made the top 5 |
|---:|---|---|---:|---|---|
| 1 | [EP885](https://www.erdosproblems.com/885) | Common factor-difference sets | 4/10 | Medium-low | First open case is concrete (`k=5`), with local search infrastructure already present in `erdos/885`. |
| 2 | [EP690](https://www.erdosproblems.com/690) | Distribution of the kth smallest prime factor | 4/10 | Medium | Recent partial resolution through `k=20` suggests a finite-pattern or asymptotic continuation may be reachable. |
| 3 | [EP1054](https://www.erdosproblems.com/1054) | Sums of the smallest divisors | 5/10 | Medium | Marked tractable by Tao on erdosproblems; strong form already disproved, leaving sharper residual questions. |
| 4 | [EP1100](https://www.erdosproblems.com/1100) | Consecutive coprime divisor pairs | 6/10 | Medium | Extremal squarefree subproblem is combinatorial and computationally explorable. |
| 5 | [EP887](https://www.erdosproblems.com/887) | Divisors very near `sqrt(n)` | 6/10 | Medium-high | Special cases and quantitative upper bounds exist; narrow enough to attack locally before touching the broader EP886. |

## 1. EP885: common factor-difference sets

**Problem statement.** For integer `n >= 1`, define
`D(n) = {|a-b| : n = ab}`. Is it true that, for every `k >= 1`, there exist integers `N_1 < ... < N_k` such that
`|D(N_1) cap ... cap D(N_k)| >= k`?

**Why tractable.** This is the cleanest finite-structure target in the batch. The first open case is `k=5`; the problem becomes a biclique search in the incidence graph between differences `delta` and numbers `n`, where `delta in D(n)`. The workspace already contains an EP885 search scaffold and outputs, so there is immediate leverage.

**Known partial results.** Erdos and Rosenfeld proved `k=2`; Jimenez-Urroz proved `k=3`; Bremner proved `k=4`. The erdosproblems entry gives these references, and the local [README](./885/README.md) records the same status and a `K_{5,5}` search model.

**Likely first attack.** Treat `k=5` as the target, not the full asymptotic problem. Run an unbiased delta-first search alongside the existing smooth-near-square candidate search, extract any strong `K_{4,t}` or near-`K_{5,5}` patterns, and try to parametrize the algebraic identities behind those patterns. If no example appears, prove a local obstruction for a natural family rather than pushing brute force.

**Difficulty.** 4/10.

**Risk of being secretly famous/hard.** Medium-low. The general `for every k` statement could be hard, but the next case has the right shape for computation plus human pattern extraction.

**Could AI-assisted proof architecture help?** Yes, strongly. This is a good fit for generated search variants, invariant mining, automated identity simplification, and then formal verification of a found construction.

**Sources.** [EP885](https://www.erdosproblems.com/885), [EP885 LaTeX/references](https://www.erdosproblems.com/latex/885), [Jimenez-Urroz paper page](https://www.sciencedirect.com/science/article/pii/S0022314X99924071).

## 2. EP690: density of integers with kth smallest prime factor equal to `p`

**Problem statement.** Let `d_k(p)` be the density of integers whose `k`th smallest prime factor is `p`. For fixed `k >= 1`, is `d_k(p)` unimodal as a function of `p`?

**Why tractable.** The entry already reports a recent finite-range classification: unimodal for `1 <= k <= 3`, non-unimodal for `4 <= k <= 20`. That makes the live problem look less like a mystery and more like extending a method: either prove non-unimodality for all `k >= 4`, or isolate the exact mechanism that begins at `k=4`.

**Known partial results.** Erdos expected unimodality to fail. The maximum is expected near `p = exp((1+o(1))k)`, while the typical `k`th prime factor of `n` is much larger, around `exp(exp(k))`. Cambie is cited by erdosproblems as proving the `k <= 20` classification.

**Likely first attack.** Reconstruct `d_k(p)` from inclusion-exclusion or Euler-product expressions, reproduce Cambie's finite checks, then search for a symbolic certificate that the same sign pattern persists for all sufficiently large `k`. A practical first milestone is a clean independent proof for `k=4`, followed by an automated certificate family for `k=21,22,...`.

**Difficulty.** 4/10.

**Risk of being secretly famous/hard.** Medium. It touches classical distribution of prime factors, but the finite pattern and recent progress reduce the risk.

**Could AI-assisted proof architecture help?** Yes. The main use is not "creative proof from scratch"; it is expression generation, exact rational interval bounds, certificate search, and formalizable monotonicity checks over primes/ranges.

**Sources.** [EP690](https://www.erdosproblems.com/690), [EP690 LaTeX/references](https://www.erdosproblems.com/latex/690), [Cambie arXiv:2501.10333](https://arxiv.org/abs/2501.10333).

## 3. EP1054: minimal `m` such that `n` is a sum of the smallest divisors of `m`

**Problem statement.** Let `f(n)` be the minimal integer `m` such that `n` is the sum of the `k` smallest divisors of `m` for some `k >= 1`. Is `f(n)=o(n)`? Or is this true only for almost all `n`, with `limsup f(n)/n = infinity`?

**Why tractable.** The strongest form has already been disproved in Tao's comment, as summarized on erdosproblems: the upper density of `{n : f(n) <= delta n}` is `O(delta^2)`. That reframes the project toward the remaining almost-all and limsup behavior. The workspace already has EP1054 formalization notes for small unreachable values, which are not the main theorem but help pin down definitions.

**Known partial results.** The function is undefined for `n=2` and `n=5`; it is expected to be defined for all `n >= 6`, which would follow from a strong Goldbach-type input. The erdosproblems page reports Tao's density obstruction to the original `f(n)=o(n)` claim.

**Likely first attack.** Separate the problem into density lower bounds and exceptional constructions. Use computational enumeration to understand which `n` have small `f(n)`, classify the divisor-prefix sums that occur below a moving multiple of `n`, and test whether the almost-all variant is even numerically plausible. A realistic first result would be a new explicit infinite family forcing `f(n)/n` large, or a density theorem for a restricted family of `m`.

**Difficulty.** 5/10.

**Risk of being secretly famous/hard.** Medium. The remaining almost-all statement may hide additive prime input, but the known negative result gives several weaker publishable targets.

**Could AI-assisted proof architecture help?** Yes. It can help with exhaustive small-case classification, conjecture generation for divisor-prefix sums, and Lean-friendly formalization of small obstructions. It is less likely to supply the analytic density argument by itself.

**Sources.** [EP1054](https://www.erdosproblems.com/1054), [OEIS A167485](https://oeis.org/A167485), local notes at [erdos/1054/approaches.md](./1054/approaches.md).

## 4. EP1100: coprime consecutive divisors and `tau_perp(n)`

**Problem statement.** If `1=d_1<...<d_{tau(n)}=n` are the divisors of `n`, let `tau_perp(n)` count the number of adjacent divisor pairs `(d_i,d_{i+1})` with `(d_i,d_{i+1})=1`. Is `tau_perp(n)/omega(n) -> infinity` for almost all `n`? Is `tau_perp(n) < exp((log n)^{o(1)})` for all `n`? For squarefree `n`, determine the growth of `g(k)=max_{omega(n)=k} tau_perp(n)`.

**Why tractable.** The squarefree extremal version is a self-contained combinatorial problem about ordering subset-products of `k` primes. That is much more approachable than the almost-all analytic statement, and it gives a clear proving ground for search, extremal examples, and upper-bound heuristics.

**Known partial results.** It is trivial that `tau_perp(n) >= omega(n)`, with equality infinitely often. Erdos and Hall proved large values below `x`, and Erdos and Simonovits proved `(sqrt(2)+o(1))^k < g(k) < (2-c)^k` for some `c>0`.

**Likely first attack.** Start with squarefree `g(k)`. Generate exact values or strong bounds for small `k`, inspect the prime-ratio regimes that maximize adjacent coprime pairs, and look for a compression argument reducing the problem to separated prime scales. A useful first theorem could improve either exponential base in the existing `sqrt(2)` to `2-c` gap.

**Difficulty.** 6/10.

**Risk of being secretly famous/hard.** Medium. The all-`n` upper bound may be hard, but the squarefree extremal subproblem has enough combinatorial structure to be worth attacking.

**Could AI-assisted proof architecture help?** Yes. The likely workflow is search for extremizers, convert observations into poset/product-order lemmas, and use a proof assistant for finite `k` or structural reductions.

**Sources.** [EP1100](https://www.erdosproblems.com/1100), [OEIS A325864](https://oeis.org/A325864).

## 5. EP887: boundedly many divisors in a `C n^{1/4}` window around `sqrt(n)`

**Problem statement.** Is there an absolute constant `K` such that, for every `C>0`, if `n` is sufficiently large then `n` has at most `K` divisors in `(n^{1/2}, n^{1/2}+C n^{1/4})`?

**Why tractable.** This is narrower than the broader Ruzsa/Erdos-Rosenfeld window problem EP886. Existing results already control the count by `1+C^2`; Chan proved strong special cases for squares and near-products. The question asks whether the dependence on `C` can be removed, so the first attack can focus on ruling out large clusters of near-square factor pairs.

**Known partial results.** Erdos and Rosenfeld found infinitely many `n` with four divisors in `(n^{1/2}, n^{1/2}+n^{1/4})`, and proved that for fixed `C`, all large `n` have at most `1+C^2` divisors in the `C n^{1/4}` interval. Chan proved a bound of five for perfect squares in a slightly wider symmetric window, and later an 18-divisor bound for numbers of the form `(N-a)(N-b)` in a near-square regime.

**Likely first attack.** Translate each close divisor `d = sqrt(n)+O(n^{1/4})` into a near-square factorization constraint. Then attempt a determinant/spacing argument showing that many such divisors force incompatible small integer relations. Start with squares and near-squares to reproduce Chan's setup, then try to remove the structural assumption.

**Difficulty.** 6/10.

**Risk of being secretly famous/hard.** Medium-high. The problem is close to delicate divisor-spacing geometry, and the broader EP886 may be harder. Still, the `n^{1/4}` scale is rigid enough to be a plausible attack surface.

**Could AI-assisted proof architecture help?** Somewhat. AI can help organize case splits, search for forbidden configurations, and verify algebraic identities. The core spacing lemma likely needs traditional human analytic number theory judgment.

**Sources.** [EP887](https://www.erdosproblems.com/887), related [EP886](https://www.erdosproblems.com/886), [Chan arXiv:1303.2069](https://arxiv.org/abs/1303.2069).

## Near misses

- [EP886](https://www.erdosproblems.com/886): closely related to EP887 and even marked tractable by a user, but the `n^{1/2-\epsilon}` window is much broader and looks more dangerous.
- [EP693](https://www.erdosproblems.com/693): gaps between integers with a divisor in `(n,2n)` are appealing, but the current path seems to need stronger short-interval distribution input.
- [EP859](https://www.erdosproblems.com/859): density of integers for which `t` is a sum of distinct divisors has good old bounds, but the requested asymptotic constants look less local.
- [EP252](https://www.erdosproblems.com/252): irrationality of `sum sigma_k(n)/n!` is attractive and known for `k <= 4`, but the general problem seems to lean on prime-pattern conjectures.
- [EP975](https://www.erdosproblems.com/975): average divisor function over irreducible polynomials is too close to serious analytic number theory for this "more solvable than EP3" filter, despite known quadratic cases.
