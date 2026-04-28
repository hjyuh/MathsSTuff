# Candidate scout: EP689-adjacent covering/sieve problems

Date: 2026-04-26.

Scope: identify nearby Erdos Problems where the EP689 machinery might transfer.
This is a scout note only; it deliberately does not try to solve any problem.

## Current EP689 machinery to port

The working EP689 stack in `erdos/689` is:

- finite congruence-cover formulation: choose one class `a_p mod p` per prime;
- tokenized residual demand after structured initial choices;
- fixed finite residue data `S` and robust large-prime switches;
- residue-density checks modulo a fixed `W`;
- finite-core truncation of coefficient families;
- prime-difference hypergraphs with edges `|x-y|=2P`;
- Green-Tao-Ziegler style first/second moment inputs for fixed linear-form systems;
- fractional/kernel feasibility plus Kahn/Frankl-Rodl-Pippenger rounding;
- exact cleanup by unused robust primes.

The main question for transfer is whether a target problem can be reduced to a
finite residual-token cover with enough large-prime labels and bounded
codegrees. If it also requires modulus economy, uniformity across growing
coefficient ranges, or an upper-bound/supremum statement, the transfer becomes
much weaker.

## Top 5 candidates

### 1. EP467 - partitioned two-cover by prime residue classes

Source: [EP467](https://www.erdosproblems.com/467).

Problem shape: choose one residue class `a_p mod p` for every prime `p <= x`
and partition the primes into two nonempty sets `A sqcup B` so that every
`n < x` is hit by at least one prime from `A` and at least one prime from `B`.
The page notes that the source formulation is ambiguous, so the exact intended
quantifiers should be treated carefully.

Relation to EP689: this is a colored strengthening of EP689. EP689 asks for
two hits among all primes. EP467 asks for one hit in each of two prime colors.
Thus EP467 would imply the `r=2` EP689 statement at the same scale, but an
EP689 cover need not split into two covers.

Likely transfer:

- The token language transfers cleanly if residual demand is vector-valued:
  `(d_A(m), d_B(m))` instead of a scalar demand.
- The robust-switch lemma should have a colored version: switching a robust
  prime in color `c` must not create new color-`c` debt at `P,2P,3P,4P`.
- The large-prime matching/Kahn framework can be run on two disjoint reservoirs,
  one per color, if the residual sets after the initial colored zero stage have
  sparse structured main terms.

Likely non-transfer:

- EP689 robustness preserves total two-coverage, not one-hit-per-color.
  It is not enough for EP467.
- The current EP689 pair edge covers two total residual tokens with one prime.
  EP467 needs color-specific tokens, so the matching must remember color and
  cannot freely merge the two demands.
- The initial parity-first EP689 setup is asymmetric; EP467 probably needs a
  deliberately balanced initial split of small primes.

Known comments/literature: the EP467 page gives only the Erdos-Graham source
and warns that the original problem statement may be missing quantifiers. I did
not find incorporated partial results on the page.

Difficulty: 8/10. It is close enough to port definitions, but the colored
side-debt condition is a real new constraint.

First reduction lemma to write: **Colored robust-switch reduction.** Fix
disjoint finite small-prime sets `S_A,S_B` with residues in each color. Define
color-robust primes `P > x/5` by requiring enough same-color backup coverage at
`P,2P,4P` and a same-color backup for `3P`. Prove that switching any
color-robust `P` to a nonzero residue creates no new deficit in that color.
Then reduce EP467 to covering two finite color-specific residual token sets
using disjoint robust prime reservoirs.

### 2. EP1139 - long gaps between integers with at most two prime factors

Sources: [EP1139](https://www.erdosproblems.com/1139) and the
[EP1139 discussion thread](https://www.erdosproblems.com/forum/thread/1139).

Problem shape: for the sequence `u_k` of integers with at most two prime
factors, decide whether
`\limsup (u_{k+1}-u_k)/\log k = infinity`.

Relation to EP689: the EP1139 discussion explicitly points to a two-fold
congruence cover of `[1,n]`. If we choose residues `a_p mod p` so every
`1 <= j <= n` is hit by at least two primes, CRT gives an `N` with
`N == -a_p mod p`; then each `N+j` has at least two prescribed prime divisors.
With a small enough CRT modulus, this creates long intervals containing no
primes or semiprimes.

Likely transfer:

- The EP689 token-cover language is almost exactly the finite combinatorial
  object needed.
- The staged zero-residue/sieve decomposition from the early EP689 notes is
  the same Erdos-Rankin shape described in the EP1139 thread.
- The GTZ/Kahn machinery is plausible for the prime-linear-form moment systems
  that occur when covering primes and structured semiprimes by reservoir primes.

Likely non-transfer:

- Plain EP689 has no modulus-economy requirement. It may use too many primes,
  giving `log M ~ n` rather than the `log M = o(n)` needed for a divergent
  gap-to-log ratio.
- The current robust fixed-`S` proof leaves a residual set of `S`-smooth
  coefficient times one prime. EP1139 needs a multi-stage cover of primes and
  semiprime families with careful `sum log p` bookkeeping.
- The singleton cleanup step in EP689 is cheap only because all primes up to
  `n` are available. EP1139 needs every cleanup prime paid for in the modulus.

Known comments/literature: EP1139 is open and formalized on the site. The
discussion thread says the core missing input is a two-fold multi-covering or
hypergraph-cover lemma plus linear-equations-in-primes technology.

Difficulty: 9/10. The combinatorial core is closest to EP689, but the modulus
economy changes the problem.

First reduction lemma to write: **Economical two-cover implies EP1139.** Assume
there are arbitrarily large `n` and two-fold covers of `[1,n]` using prime set
`P_n` with `sum_{p in P_n} log p = o(n)`. Let `M_n = prod_{p in P_n} p` and
choose `N` by CRT with `M_n <= N < 2M_n` and `N == -a_p mod p`. Prove that
`[N+1,N+n]` contains no integer with at most two prime factors and hence gives
the desired limsup. This isolates exactly the extra economy needed beyond
EP689.

### 3. EP688 - one-cover by only large prime moduli

Source: [EP688](https://www.erdosproblems.com/688).

Problem shape: define `epsilon_n` as the largest exponent such that one can
choose residue classes for primes `n^{epsilon_n} < p <= n` and cover every
integer in `[1,n]` at least once. Estimate `epsilon_n`, especially whether
`epsilon_n = o(1)`.

Relation to EP689: EP688 is the one-fold, large-prime-only sibling. EP689
allows all primes up to `n` and asks for multiplicity two. EP689's cleanup
stage already uses very large primes, but only after small-prime structure has
made the remaining demand sparse.

Likely transfer:

- The exact bitset/capacity search from `erdos/689/computation` can be reused
  with required coverage `1` and prime domains restricted to `p > n^epsilon`.
- The Kahn/fractional-cover viewpoint is relevant: residue classes modulo large
  primes are hyperedges on `[1,n]`.
- If an iterative nibble leaves only `O(n/log n)` holes, EP689's singleton
  cleanup idea with primes `> n/2` becomes available.

Likely non-transfer:

- There is no small-prime zero stage in EP688, so the initial residual set is
  all of `[1,n]`, not a sparse set of prime-parametrized tokens.
- Random residues over a fixed large-prime range give only constant expected
  coverage and leave a positive-density residual set. The EP689 last-mile
  machinery starts much later.
- GTZ prime-linear-form estimates are mostly irrelevant for arbitrary targets
  `m`; the hard part is semirandom set cover/discrepancy rather than counting
  prime configurations.

Known comments/literature: the page records Erdos's lower bound
`\epsilon_n >> log log log n / log log n` and links EP687, EP689, and EP1200.
Green's open-problems list places the related Jacobsthal covering problem
near EP689 as Problem 46.

Difficulty: 8/10 for improving lower bounds; 10/10 for the `o(1)` question.

First reduction lemma to write: **Large-prime iterative residual lemma.** For
fixed `0 < alpha < beta <= 1`, formulate a theorem saying that primes
`p in [n^alpha,n^beta]` can reduce any residual set `R subset [1,n]` satisfying
explicit residue-discrepancy hypotheses by the expected factor, while
preserving the same hypotheses for the next block. Add a final clause that
`|R| <= pi(n)-pi(n/2)` permits singleton cleanup by primes `> n/2`.

### 4. EP1200 - bounded reciprocal-mass prime cover

Sources: [EP1200](https://www.erdosproblems.com/1200) and Green's open-problem
list discussion near Problems 46-47
([PDF](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)).

Problem shape: decide whether there is a constant `C` such that, for all large
`x`, some primes `p_i < x` with `sum 1/p_i < C` and residues `a_i mod p_i`
cover every `n < x`.

Relation to EP689: this is an economical one-cover version. EP688 with a fixed
positive lower bound for `epsilon_n` would imply EP1200 by taking all primes in
`[x^c,x]`, whose reciprocal sum is bounded. The economy issue is also exactly
what EP1139 needs.

Likely transfer:

- The fractional-cover/Kahn language is appropriate: minimize harmonic cost of
  a prime-residue cover.
- EP689's bookkeeping of exact residual tokens and singleton cleanup can be
  reused once a bounded-cost fractional/nibble stage has reduced the uncovered
  set enough.
- The dyadic-prime reservoir framework from EP1139 would be the right common
  abstraction.

Likely non-transfer:

- Current EP689 spends the whole prime set up to `n`, whose reciprocal mass is
  `log log n + O(1)`, not bounded.
- Fixed small-prime zero stages are too expensive for EP1200 unless replaced by
  sparse/economical stages.
- The EP1200 page notes the Erdos-Ruzsa opposite formulation: bounded
  reciprocal mass might always leave `gg_C x` uncovered integers. If that is
  true, the desired cover is false.

Known comments/literature: EP1200 is open. The page links EP783 and EP784 and
states the Erdos-Ruzsa question about whether bounded reciprocal prime systems
must leave a positive-density uncovered set. Green's list gives the same
bounded-`sum 1/p` formulation as an "elegant problem of a similar type."

Difficulty: 10/10. This is a true economy problem, not just a cleanup variant.

First reduction lemma to write: **Harmonic-budget cover LP.** Define a dyadic
block model with variables selecting one residue per prime and objective
`sum 1/p`. Prove that any rounded cover with block costs `h_j` and residual
decay factors `rho_j` must satisfy a deterministic inequality of the form
`prod rho_j <= O(1/x)` plus a singleton-cleanup budget. This lemma would either
show what an EP689-style proof must beat or expose the Erdos-Ruzsa obstruction.

### 5. EP687 - Jacobsthal interval one-cover estimates

Sources: [EP687](https://www.erdosproblems.com/687), Green's Problem 46 in
the [open-problems PDF](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf),
and the FGKMT paper [Long gaps in sieved sets](https://arxiv.org/abs/1802.07604).

Problem shape: let `Y(x)` be the largest `y` such that one can choose residue
classes `a_p mod p` for all primes `p <= x` and cover every integer in `[1,y]`.
Estimate `Y(x)`.

Relation to EP689: EP689 is a multiplicity-two assertion at the diagonal scale
`y=x`. EP687 is the one-cover optimization problem and is the classical
Jacobsthal/large-prime-gap sibling.

Likely transfer:

- The residual-token decomposition after a zero-residue stage is directly in
  the Jacobsthal/large-gap tradition.
- The EP689 exact-search code can be specialized to one-cover certificates for
  finite `Y(x)` probes.
- For the weaker variant mentioned on the EP687 page, "cover all except
  `o(y/log y)`", EP689's residual-tail accounting and singleton cleanup
  language may give a clean formulation.

Likely non-transfer:

- The main EP687 lower-bound frontier is already Ford-Green-Konyagin-Maynard-
  Tao technology; the current EP689 route is unlikely to improve it without a
  new economical multi-stage cover.
- EP687 upper bounds are anti-covering statements. EP689's constructive
  machinery points in the opposite direction.
- For `y >> x`, residue classes modulo `p <= x` hit long progressions, so the
  large-prime pair geometry `|x-y|=2P` is not the natural hypergraph.

Known comments/literature: EP687 lists Iwaniec's upper bound `Y(x) << x^2`,
the FGKMT lower bound
`Y(x) >> x log x log log log x / log log x`, and the Maier-Pomerance conjecture
`Y(x) << x (log x)^{2+o(1)}`. Green's list describes this as the Jacobsthal
problem and notes that improvements would affect prime-gap methods.

Difficulty: 10/10 for the main problem; 6/10 for writing a useful weak-variant
reduction.

First reduction lemma to write: **EP689-style almost-cover reduction for
EP687.** Fix `y = x L(x)` and a preliminary zero-residue threshold. Express
the uncovered set as rough/semismooth residual tokens, then formulate a
one-batch reservoir lemma that covers all but `o(y/log y)` of them. The point is
not to beat FGKMT immediately, but to make the exact overlap with EP689's
token-and-nibble framework explicit.

## Lower-priority nearby problems

- [EP1205](https://www.erdosproblems.com/1205) is the all-integer-moduli
  analogue of EP689 and is already solved with `F(x) ~ log x`. It is useful as
  a sanity-check model for random residues plus greedy cleanup, but it is not a
  research target.
- [EP1202](https://www.erdosproblems.com/1202), Green's Problem 44, is a
  half-residue-class large-sieve question now resolved negatively. It is useful
  as a warning: large-sieve intuition can fail above the square-root scale.
- [EP1204](https://www.erdosproblems.com/1204) is about admissible sets missing
  a residue class modulo every prime. It is residue-adjacent but dual to EP689;
  the present covering machinery does not transfer directly.
- [EP429](https://www.erdosproblems.com/429) is another admissibility/missing
  residue-class problem and is already disproved, with a Lean-verified negative
  result noted on the site.

## Source links

- [EP689](https://www.erdosproblems.com/689)
- [EP467](https://www.erdosproblems.com/467)
- [EP1139](https://www.erdosproblems.com/1139) and
  [thread](https://www.erdosproblems.com/forum/thread/1139)
- [EP688](https://www.erdosproblems.com/688)
- [EP1200](https://www.erdosproblems.com/1200)
- [EP687](https://www.erdosproblems.com/687)
- [EP1205](https://www.erdosproblems.com/1205)
- [EP1202](https://www.erdosproblems.com/1202)
- [EP1204](https://www.erdosproblems.com/1204)
- [EP429](https://www.erdosproblems.com/429)
- Ben Green, [100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)
- Green and Tao, [Linear equations in primes](https://annals.math.princeton.edu/2010/171-3/p08)
- Ford, Konyagin, Maynard, Pomerance, Tao,
  [Long gaps in sieved sets](https://arxiv.org/abs/1802.07604)
- Filaseta, Ford, Konyagin, Pomerance, Yu,
  [Sieving by large integers and covering systems of congruences](https://arxiv.org/abs/math/0507374)
