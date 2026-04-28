# EP675 Sprint Status

Date: 2026-04-27

## Current Assessment

EP675 is a good low-compute target. The first sprint produced one safe
squarefree theorem, one stronger conditional squarefree theorem, and a promising
new lower-bound direction for sums of two squares.

## Squarefree Subproblem

Let `T_S(N)` be the least shift preserving squarefreeness on `[1,N]`.

### Safe theorem

Using Heath-Brown's all-moduli least-squarefree-in-AP bound

```text
L(q,r) <<_eps q^(13/9 + eps),
```

the formalized argument gives

```text
T_S(N) > exp(N^c)
```

for every fixed

```text
c < 9/26.
```

This is already enough to answer the squarefree growth question positively.

### Stronger published-theorem upgrade

If one has the prime-square/all-moduli bound

```text
L(q,r) <<_eps q^(36/25 + eps)
```

for `q=p^2`, then the exponent improves to

```text
c < 25/72.
```

The accessible Nunes arXiv text only confirms `36/25` for squarefree moduli,
but Mangerel's open-access paper records the published Nunes theorem as an
all-moduli result. Thus the `25/72` range is usable if the public note cites
published Nunes plus Mangerel rather than the arXiv abstract alone.

### Possible improvement

A 2026 Zhong-Zhang paper on squarefree integers in APs to prime power moduli
may give a better exponent for `q=p^2`. Exact access is still needed.

## Translation Existence

The standard construction for squarefree numbers is solid:

1. Freeze all forbidden small moduli by taking a shift divisible by their
   product.
2. For the prefix entries that are allowed, choose a multiplier avoiding all
   larger forbidden divisors.
3. Use a finite/Brun sieve to prove such a multiplier exists.

This also gives the known summable forbidden-moduli case
`sum 1/b < infinity`. The broader condition

```text
sum_{b<x} 1/b = o(log log x)
```

needs a clean Brun-sieve citation or standalone finite-sieve lemma in any
public write-up.

## Sums of Two Squares

The squarefree forced-divisibility idea extends in p-adic form.

Membership in the sums-of-two-squares set is controlled by primes
`q == 3 mod 4`: each such prime must occur to even valuation.

Polished partial theorem:

```text
If a shift t preserves the sums-of-two-squares indicator on [1,N],
then for every prime q == 3 mod 4,
q^{v_q(t)} > N/(C q^theta)
```

under the AP input `L_2(q^2,r) <= C q^theta` for reduced residues. Summing
this high-valuation bound over `q <= N^c` gives

```text
log t >= ((1 - theta c)/(2c) + o(1)) N^c.
```

This has now been written as a standalone conditional theorem in
`notes/sums_two_squares_forced_divisibility.md`. With Linnik's theorem it gives
an unconditional lower bound

```text
t >= exp(K_c N^c)
```

for every `c < 1/(2L)`, where `L` is any admissible Linnik exponent. More
explicitly, any `K_c < (1 - 2Lc)/(2c)` is admissible.

The dedicated audit note is `notes/b2_forced_divisibility_review.md`.

This does not solve the existence of translation witnesses for sums of two
squares, but it is a real theorem directly about the headline case.

## B-free Analogy / Constructive Lane

The B-free analogy has now been separated cleanly in
`notes/bfree_analogy.md`.

The conclusion is:

```text
squarefree numbers are genuinely pairwise-coprime B-free;
sums of two squares are not B-free, but are an inverse limit of local
q-adic parity conditions at primes q == 3 mod 4.
```

For a fixed prefix `[1,N]`, define

```text
M_N = prod_{q <= N, q == 3 mod 4} q^(1+floor(log_q N)).
```

Taking `t=M_N s` freezes every small bad-prime valuation for all `a <= N`.
Thus the full translation-property problem for sums of two squares reduces to
the following finite-pattern problem:

```text
Find s such that M_N s+a is a sum of two squares
for every a in B_2 cap [1,N].
```

A stronger multiplicative variant takes `A_N=lcm(1,...,N) M_N` and asks for

```text
1+(A_N/a)s in B_2        for every a in B_2 cap [1,N].
```

So the current headline interface is:

> If every locally admissible finite tuple of affine-linear forms can be
> simultaneously specialized to sums of two squares, then `B_2` has the
> translation property.

This is not a direct consequence of the elementary B-free Brun argument,
because the first-level bad primes `q == 3 mod 4` have reciprocal density
`(1/2) log log x`. The missing constructive input is a positive-dimensional
linear-pattern theorem for the multiplicative set `B_2`.

## Dense Prime Partition Question

Let `A = S(P)` be integers with all prime factors in a dense prime set `P`, and
let `Q` be the complementary dense set.

For a prefix `[1,N]`, if

```text
M_N = product_{q in Q, q <= N} q
```

and one can find `s` such that

```text
M_N s + a in A
```

for all `a in A cap [1,N]`, then `t = M_N s` is a translation witness.

There is no finite CRT obstruction. The difficulty is distribution of the
`P`-smooth semigroup in the required residue/progression patterns. This is
probably harder than the squarefree subproblem for adversarial dense
partitions.

### Random-partition theorem

The new note `notes/prime_partition_regular_partial.md` gives a strong
regular-model result. For a Bernoulli random partition of the primes, with

```text
P(p)=alpha,       Q(p)=1-alpha,
```

the set `S(P)` has the translation property almost surely, assuming only the
standard Brun/linear-sieve almost-prime tuple lemma.

For a fixed prefix `[1,N]`, freeze small `Q`-primes by

```text
M_N = product_{q in Q, q <= N} q.
```

Then apply the almost-prime tuple lemma to

```text
M_N s + a,       a in S(P) cap [1,N].
```

It supplies infinitely many candidate `s` for which the product over these
forms has boundedly many outside prime factors. The candidates can be chosen
with disjoint outside prime-factor sets. Since the prime partition is random,
each candidate succeeds with probability bounded below by a positive constant,
independently along the selected subsequence. Hence one succeeds almost
surely.

This likely gives an existential dense prime partition with the translation
property. It does not settle a universal adversarial interpretation.

## Gaussian-Integer Constructive Lane

The Gaussian-integer attempt is now written in
`notes/gaussian_construction_attempts.md`.

Verdict:

```text
Gaussian CRT removes finite local obstructions, but does not construct the
global additive shift.
```

For finite `H subset B_2`, taking `t` highly divisible by finitely many
primes `q == 3 mod 4` preserves all selected local valuation parities. Thus
there is no finite congruence obstruction to `t+H subset B_2`.

However, the norm identity

```text
N(u)N(v)=N(uv)
```

scales configurations rather than translating them. If `a_i+t=N(z_i)`, then
after multiplying by a common norm `L`, the translated shift would have to be

```text
t_i' = Lt + (L-1)a_i,
```

which depends on `i`. Likewise, taking `t=N(beta)` creates overdetermined
orthogonality conditions

```text
Im(beta \bar alpha_i)=0
```

or

```text
Re(beta \bar alpha_i)=constant.
```

The useful reformulation is the difference-of-norms system

```text
x_i^2+y_i^2 - x_0^2-y_0^2 = a_i-a_0.
```

For fixed `|H|` this is a plausible quadratic-forms/circle-method object, but
EP675 requires `H=B_2 cap [1,N]`, whose size grows like
`N/sqrt(log N)`. So this lane clarifies the exact missing input rather than
closing it:

```text
prove a lower-bound theorem for simultaneous affine-linear values in B_2
with prescribed finite local conditions.
```

## Recommended Next Move

Write a polished note with three results/reductions:

1. **Unconditional squarefree growth partial**

   `T_S(N) > exp(N^c)` for every `c < 9/26`, using Heath-Brown.

2. **Conditional exponent upgrade**

   If a least-squarefree AP bound with exponent `theta` holds for moduli
   `p^2`, then

   ```text
   T_S(N) > exp(N^c) for all c < 1/(2 theta).
   ```

3. **Random dense prime partition theorem**

   Cite the standard almost-prime tuple lemma precisely, then include the
   Bernoulli random partition proof from
   `notes/prime_partition_regular_partial.md`. This likely gives a positive
   answer to the prime-partition bullet in the existential/random sense.

4. **Sums-of-two-squares reduction**

   Prove formally that a finite affine-linear-pattern theorem for `B_2`
   implies the translation property. The first literature audit for exactly
   that theorem is now recorded in
   `notes/b2_linear_patterns_literature.md`.

This formal conditional reduction has now been written in
`notes/b2_conditional_translation_property.md`. The clean version uses

```text
t_N = A_N s,
a+t_N = a(1+(A_N/a)s)
```

for `a in B_2 cap [1,N]`. This multiplicative form avoids small-prime
annoyances and gives a direct local-admissibility proof for the forms

```text
1+(A_N/a)s.
```

Thus the exact missing input is not local solubility; it is the global
parallel-shift tuple theorem for the sums-of-two-squares indicator.

## Linear-Pattern Literature Audit

The new audit `notes/b2_linear_patterns_literature.md` checks Hooley,
Matthiesen, Kimmel-Kuperberg, Freiberg-Kurlberg-Rosenzweig, and norm-form /
linear-correlation results.

Verdict:

```text
No known theorem found here proves that every fixed admissible family
L_i(n)=A n+b_i has infinitely many simultaneous values in B_2.
```

The key obstruction is that the EP675 constructive forms are one-variable
parallel shifts. Matthiesen-style correlation theorems require
finite-complexity systems, i.e. no two affine forms are affinely dependent.
Kimmel-Kuperberg and McGrath-type results prove weaker consecutive-residue or
bin-detection statements. Freiberg-Kurlberg-Rosenzweig formulate the right
Hardy-Littlewood-style tuple conjecture, but it is not an unconditional theorem.

This audit is useful because it identifies the exact missing black box:

```text
parallel-shift tuple correlations for the sums-of-two-squares indicator,
with congruence restrictions.
```

If this black box were proved, the current `M_N s+a` reduction would likely
finish the sums-of-two-squares translation property after a local admissibility
check. But the black box is a real analytic barrier, not standard literature.

## Percent Estimate

- Squarefree growth question: `80-90%` for a positive-power lower bound;
  `35-45%` for sharp/optimized exponent work.
- Dense prime partition, random/existential interpretation: `70-85%` after
  citing the almost-prime tuple lemma cleanly.
- Dense prime partition, universal adversarial interpretation: `20-30%`.
- Sums of two squares translation property: `20-25%`. The lower-bound side now
  has a rigorous high-valuation theorem; the constructive side has precise
  linear-pattern and Gaussian norm-form reductions, but the main existence
  theorem is not currently available from the literature.
- Full EP675: `30-40%` if one counts the random/existential dense-prime-
  partition result as one of the problem's main branches; `25-30%` for the
  headline sums-of-two-squares route alone. The previous optimistic route
  through standard linear-pattern results does not close the constructive
  sums-of-two-squares lane.
- Publishable partial note: `70-80%` after cleaning citations.
