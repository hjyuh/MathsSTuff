# Literature map for Erdos Problem 689

Created: 2026-04-24

## Problem and nearby Erdos problems

**#689.** For all sufficiently large `n`, choose one residue class
`a_p (mod p)` for each prime `p <= n` so that every `m in [1,n]`
satisfies at least two congruences `m == a_p (mod p)`.

Primary problem page: T. F. Bloom, Erdos Problem #689,
<https://www.erdosproblems.com/689>. The page cites Erdos
`[Er79d]` and `[Er80, p.108]`, records the fixed-`r` variant, and notes
that replacing primes by all integers is #1205.

**Original Erdos source to check.** P. Erdos, "Problems and results on
combinatorial number theory III", Annals of Discrete Mathematics 6
(1980), 43--72? / 89--115 in the online scan metadata; p.108 contains:
let `f(x)` be the largest integer for which there is a system of
congruences `a_p (mod p)` over primes `p <= x` such that every integer
`n < x` satisfies at least `f(x)` of them. Online scan:
<https://combinatorica.hu/~p_erdos/1980-03.pdf>. This is the closest
primary source for #689/#1205 language.

**#1205, all moduli.** T. F. Bloom, Erdos Problem #1205,
<https://www.erdosproblems.com/1205>. Here
`F(x) = max min_{m <= x} sum_{n <= x} 1_{m == a_n (mod n)}` and the
page records the simple estimate
`F(x) = log x + O(sqrt(log x log log x))` up to the upper `O(1)` scale.
The proof uses random residues for `n <= x/2`, Chernoff concentration,
and greedy cleanup with `x/2 < n <= x`.

Use for #689: the random+cleanup architecture is relevant. It is much
too strong in available mass: all moduli give `sum_{n <= x} 1/n ~ log x`,
whereas primes give only `sum_{p <= x} 1/p ~ log log x`. Random residues
alone leave about `x log log x / log x` points with coverage `<2`, so the
#1205 proof does not transfer.

**#1139.** T. F. Bloom, Erdos Problem #1139,
<https://www.erdosproblems.com/1139>. The problem asks whether, for
`u_k` the integers with at most two prime factors,
`limsup (u_{k+1}-u_k)/log k = infinity`.

Connection to #689: a 2-fold congruence cover of `[1,n]` by distinct
primes `S` gives, by CRT, an `N` with `N == -a_p (mod p)` for all
`p in S`. Then each `N+j`, `1 <= j <= n`, has at least two prescribed
prime divisors. To force an interval with no `Omega <= 2`, one also needs
size/modulus bookkeeping, roughly
`log N <= sum_{p in S} log p`, and enough room so `N+j` is not just the
product of the two forced primes. Thus #689 is the cleaner covering
problem: it needs no economical modulus, while #1139 needs the same
covering technology with primes concentrated near a scale `y = n/z`.

The #1139 forum thread explicitly identifies the bottleneck as a
two-fold hypergraph/random-sieve cover for primes and structured
semiprimes:
<https://www.erdosproblems.com/forum/thread/1139>.

## Erdos--Rankin large-gap framework

Classical references, as cited in modern papers:

- P. Erdos, "On the difference of consecutive primes", Quart. J. Math.
  Oxford Ser. 6 (1935), 124--128.
- R. A. Rankin, "The difference between consecutive prime numbers",
  J. London Math. Soc. 13 (1938), 242--247.

Reusable statement pattern: choose residue classes `a_p (mod p)` for
small/moderate primes so that an interval is covered by congruences.
Then CRT translates the covering into a prime-free interval. Rankin's
quantitative bound has the shape
`G(X) >= (c+o(1)) log X log_2 X log_4 X / (log_3 X)^2`.

For #689: the CRT translation is optional; the direct finite covering
problem is the target. The useful part is the staged sieve:
small primes remove most integers, and a reservoir of larger primes
randomly covers the structured survivors. The classical construction is
only one-fold and aims to avoid primes, not to give every integer two
touches.

## Maynard, "Large gaps between primes"

James Maynard, "Large gaps between primes", Ann. of Math. 183 (2016),
915--933. DOI page: <https://annals.math.princeton.edu/2016/183-3/p03>.
Preprint/PDF: <https://arxiv.org/abs/1408.5110>,
<https://arxiv.org/pdf/1408.5110>.

Main theorem: with `G(X)=max_{p_n <= X}(p_{n+1}-p_n)`,
`limsup_n (p_{n+1}-p_n) / (log p_n log_2 p_n log_4 p_n (log_3 p_n)^(-2))
= infinity`.

Key covering proposition (Proposition 5 in the preprint): fix `delta>0`.
For an even parameter `m` in the Erdos--Rankin residual set and an
interval `I_m subset [x/2,x]` of primes with length at least
`delta |R_m| log x`, there are residue classes `a_q (mod q)` for primes
`q in I_m` such that every prime `p in R_m` is covered,
`p == a_q (mod q)` for some `q in I_m`. The proof actually obtains
all but `epsilon |R_m|` first, then appends cleanup primes.

Reusable for #689:

- It gives the exact model "one residue class per reservoir prime covers
  a sparse target set".
- The probability measure `mu_{m,q}` biases toward residue classes
  containing many admissible primes, using Maynard/GPY-type weights.
- The proof target is `sum_{q in I_m} mu_{m,q}(p) >> delta log k` for
  almost all target primes `p`; choosing `k` large gives arbitrary
  expected multiplicity.

Mismatch:

- It is one-fold, prime-only, and decomposes the residual set by a fixed
  smooth multiplier `m`.
- #689 after a zero-residue stage has demand tokens for primes and for
  structured semiprimes/prime powers, and some points need two remaining
  hits.
- Maynard's cleanup may use separate primes per leftover target; for
  #1139 that is expensive unless leftovers are reduced to `o(y/log y)`
  and cleaned at the reservoir scale.

## Ford--Green--Konyagin--Tao and FGKMT

Kevin Ford, Ben Green, Sergei Konyagin, Terence Tao, "Large gaps between
consecutive prime numbers", Ann. of Math. 183 (2016), 935--974.
DOI page: <https://annals.math.princeton.edu/2016/183-3/p04>.
Preprint: <https://arxiv.org/abs/1408.4505>.

Main theorem: for `G(X)` the largest prime gap below `X`,
`G(X) >= f(X) log X log_2 X log_4 X / (log_3 X)^2`, where
`f(X) -> infinity`. Their proof combines Erdos--Rankin with a random
construction covering primes by arithmetic progressions and relies on
linear-equations-in-primes technology.

Kevin Ford, Ben Green, Sergei Konyagin, James Maynard, Terence Tao,
"Long gaps between primes", JAMS 31 (2018), 65--105.
Preprint/PDF: <https://arxiv.org/abs/1412.5029>,
<https://arxiv.org/pdf/1412.5029>. This is the most reusable source for
the hypergraph-cover lemma.

Theorem 2 in FGKMT 2018, "sieving primes": with
`y = c x log x log_3 x / log_2 x`, and primes split into
`S = {log^20 x < s <= z}`, `P = {x/2 < p <= x}`,
`Q = {x < q <= y}`, there are residue vectors `a_s (mod s)` and
`b_p (mod p)` such that
`#(Q cap S(a) cap S(b)) << x/log x`.

Corollary 4 / Theorem 3, probabilistic covering: for random subsets
`e_p subset Q'`, if

- edge sizes are bounded by
  `r = O(log x log_3 x / log_2^2 x)`,
- sparsity holds: `P(q in e_p) <= x^{-1/2-1/10}`,
- uniform covering holds:
  `sum_p P(q in e_p) = C + O(1/log_2^2 x)` for almost all `q`, with
  `C` bounded below by a positive constant,
- codegrees are small:
  `sum_p P(q_1,q_2 in e_p) <= x^{-1/20}`,

then one may choose admissible realized edges `e'_p` so that after
`m <= log_3 x/log 5` nibbles the uncovered set has size
`~ 5^{-m} #Q'`, uniformly also for large subsets `Q'' subset Q'`.

Reusable for #689:

- This is the right abstract form: vertices are residual demand tokens;
  edges are possible residue classes for one reservoir prime.
- The small-codegree check is especially favorable when reservoir primes
  are about `y`: two distinct targets `u,v` can lie in the same residue
  class modulo `p` only if `p | u-v`, so few `p` contribute.
- The theorem handles non-identical edge distributions and variable edge
  sizes, unlike vanilla Pippenger--Spencer.

Mismatch:

- It reduces the target set by a fixed factor per nibble but does not by
  itself prove complete coverage; a cleanup stage is still needed.
- It is stated for one-fold coverage of vertices. A two-fold #689 proof
  should either duplicate vertices into demand tokens or run two
  coupled passes while controlling collisions on the same integer.
- The random construction is built for primes `Q`; #689 needs comparable
  first/second moment estimates for mixed targets such as `q`,
  `r q`, `r^e q`, and prime powers left by the small-prime stage.

## Hypergraph nibble and semi-random set cover

Primary combinatorial sources:

- V. Rodl, "On a packing and covering problem", European J. Combin. 6
  (1985), 69--78.
- N. Pippenger and J. Spencer, "Asymptotic behavior of the chromatic
  index for hypergraphs", J. Combin. Theory Ser. A 51 (1989), 24--42.
  DOI page: <https://doi.org/10.1016/0097-3165(89)90074-5>.
- P. Frankl and V. Rodl, "Near perfect coverings in graphs and
  hypergraphs", European J. Combin. 6 (1985), 317--326.
- J. Kahn, "A linear programming perspective on the Frankl--Rodl--
  Pippenger theorem", Random Structures Algorithms 8 (1996), 149--157.

Pippenger--Spencer theorem, usable summary: in a nearly regular uniform
hypergraph with maximum codegree `o(D)` compared with degree `D`, the
edge set decomposes into almost-perfect matchings/covers; equivalently,
one can select near-optimal disjoint or covering families under strong
regularity, uniformity, and codegree hypotheses.

For #689, plain Pippenger--Spencer is weaker as a black box because
residue-class edges have nonuniform sizes and depend heavily on the
prime modulus. FGKMT's probabilistic covering theorem is the relevant
relaxation: it keeps the nibble mechanism but replaces regular uniform
edges by probability distributions with degree and codegree control.

## Distributional inputs likely needed

1. **Mertens/PNT baseline.** For random residues,
   `sum_{p <= n} 1/p = log log n + M + o(1)`. This proves the available
   mass is enough but also predicts many `<2` holes.

2. **Bombieri--Vinogradov / fundamental lemma.** Maynard's Lemma 3 for
   `R_m` counts primes `p` with `(mp-1,P_y)=1` uniformly enough using a
   fundamental-lemma sieve plus Bombieri--Vinogradov. This is the model
   for counting target hits in one residue class.

3. **Maynard multidimensional sieve.** Maynard's "Small gaps between
   primes", Ann. of Math. 181 (2015), 383--413,
   <https://annals.math.princeton.edu/2015/181-1/p07>, supplies the
   prime-detecting weights that make some residue classes unusually rich
   in target primes. "Dense clusters of primes in subsets",
   Compos. Math. 152 (2016), 1517--1554,
   <https://arxiv.org/abs/1405.2593>, abstracts this to well-distributed
   subsets of primes.

4. **Linear equations in primes.** FGKT's 2016 paper uses Green--Tao
   linear-equations-in-primes technology rather than Maynard weights:
   B. Green and T. Tao, "Linear equations in primes", Ann. of Math. 171
   (2010), 1753--1850. This is probably stronger than #689 needs unless
   the mixed semiprime targets force high-order correlation estimates.

For #689, a promising weaker input may suffice: for reservoir primes
`p ~ y`, prove that a random or weighted residue class contains the
expected `~ z/log z` useful targets and that pair codegrees are small,
uniformly across the residual target families. The target set is not
arbitrary; after setting `a_p=0` for small primes it is made from primes,
prime powers, and numbers with one small prime factor.

## Suggested reusable theorem statement for #689

Let `y = n/z` with `z -> infinity` slowly. After assigning `a_p=0` for
`p <= y`, form demand tokens
`T = {(m,i): 1 <= i <= max(0,2-omega_y(m))}`.
Let `P_res` be a set of reservoir primes `p ~ y`. For each `p`, let the
available edges be
`E_{p,a} = {(m,i) in T: m == a (mod p)}`.

A sufficient covering theorem would say: if there are probability
measures `mu_p` on residues modulo `p` such that

- `|E_{p,a}|` is bounded by `O(z polylog z)` on the relevant support,
- for all but negligible tokens `t`,
  `sum_{p in P_res} P_{a~mu_p}(t in E_{p,a}) >= C` with `C` an
  arbitrarily large constant after batching,
- for distinct tokens `t1,t2`,
  `sum_p P(t1,t2 in E_{p,a}) = o(1)`,
- the exceptional tokens can be reduced below the number of affordable
  cleanup primes,

then FGKMT's nibble gives a constant-factor survivor reduction per
batch. Iterating and cleaning up would prove #689.

This theorem is stronger than Maynard's prime-only Proposition 5 in the
target class and fold requirement, but weaker than the full large-prime-gap
theorems in modulus economy and final CRT output. It is also weaker than
FGKMT's random construction if we can avoid Green--Tao linear-equation
technology and prove the needed moments by elementary sieve/BV estimates
for these semiprime families.

## Current assessment

The main technical gap is not the abstract nibble: FGKMT already provides
the right semi-random covering technology. The missing #689-specific
work is an arithmetic input producing residue-class distributions for
mixed residual demand tokens with:

1. near-uniform one-point degrees,
2. small two-point codegrees,
3. enough expected useful hits per reservoir prime, and
4. a cleanup stage that is cheap for #689 and, if desired, economical
enough for #1139.

For a first proof attempt, ignore #1139 modulus economy and allow all
primes `<= n`. Once a 2-fold cover is obtained, revisit the same proof
with reservoir primes `~ n/z` and track `sum log p` to test whether it
also implies #1139.
