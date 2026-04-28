# Weighted Covering Theorem Target

Date: 2026-04-28

## Purpose

The random-residue scale check shows that uniform random residues cannot prove
the economical-cover theorem. This note states the weighted replacement needed
for EP1139.

## Residual Families

Work with

```text
y=n/z,      z -> infinity,      z <= sqrt(n),
R={r prime : y < r <= A y},     A=o(z).
```

The residual tokens are:

```text
Type 0: two copies of q, where y<q<=n is prime.
Type 1: one copy of s q, where s=p^a<=z and q>y is prime.
Type P: one copy of p^a, pure prime powers.
```

Type P is small enough to reserve for cleanup. The weighted cover should focus
on Type 0 and Type 1.

## Weighted Residue Distributions

For each reservoir prime `r in R`, we need a probability distribution

```text
mu_r(a),      a mod r,
```

supported on residue classes with unusually many residual targets. The chosen
residue `a_r` will be sampled from `mu_r`.

For a token `t=(m,i)`, define its one-point mass

```text
M(t) = sum_{r in R} mu_r(m mod r).
```

For distinct tokens `t_1=(m_1,i_1)` and `t_2=(m_2,i_2)`, define the codegree
mass

```text
M(t_1,t_2)
  = sum_{r in R, m_1 == m_2 mod r} mu_r(m_1 mod r).
```

## Target Theorem

**Weighted Economical Covering Theorem.** There exist parameters

```text
z -> infinity,     A -> infinity,     A=o(z),
```

and distributions `mu_r` for `r in R` such that:

```text
1. One-point mass:
   M(t) >= C
   for all but o(n/log n) Type 0 and Type 1 tokens,
   where C can be made large enough for the covering nibble.

2. Small atom / edge size:
   for all r,a, the number of typical tokens m == a mod r is at most B,
   with B in the range allowed by the semi-random covering theorem.

3. Codegree:
   for all but negligible pairs of distinct typical tokens,
   M(t_1,t_2)=o(1), or enough averaged codegree control holds for the
   FGKMT/Maynard covering lemma.

4. Atypical tokens:
   the number of tokens failing the above estimates is o(n/log n).
```

Then a semi-random covering theorem gives residue choices `a_r mod r` covering
all but `o(n/log n)` residual tokens. The cleanup stage then proves EP1139.

## Candidate Construction of `mu_r`

Uniform residues fail because

```text
sum_{r in R} 1/r <= log 2 + o(1)
```

in the economical range.

The replacement should imitate Maynard's large-gap weights:

```text
mu_r(a) proportional to a weight measuring how many target primes q
or target semiprimes s q lie in the progression a mod r.
```

For Type 0, this is the usual prime-targeting problem:

```text
q == a mod r,      q prime.
```

For Type 1, after fixing `s=p^a<=z`, the condition is

```text
s q == a mod r,
q prime,
```

or equivalently

```text
q == s^{-1} a mod r
```

when `(s,r)=1`, which is automatic because `s<=z<y<r`.

Thus Type 1 targets are also prime targets after rescaling residues by `s`.

This is promising: the mixed semiprime residual family reduces to many
coefficient-weighted prime target families.

## Main Technical Difficulty

The same residue distribution `mu_r` must serve all coefficients `s<=z`
simultaneously. It is not enough to optimize separately for each `s`.

For a residue `a mod r`, the weighted target count has the form

```text
W_r(a) =
  c_0 * #{q prime: q == a mod r}
  + sum_{s<=z} c_s * #{q prime: s q == a mod r, s q <= n}.
```

Equivalently,

```text
W_r(a) =
  c_0 * pi(n; r, a)
  + sum_{s<=z} c_s * pi(n/s; r, s^{-1}a).
```

The weights `c_s` should reflect residual token multiplicities and coefficient
mass.

The analytic challenge is to prove that choosing residues biased by `W_r(a)`
gives:

```text
large one-point mass for most q and s q tokens,
small codegrees,
controlled edge sizes.
```

## Why This Looks More Plausible Than a Direct Semiprime Problem

The residual semiprimes are not arbitrary products of two large primes. They
are `s q` with `s<=z` and `q>y`. Since every reservoir prime `r>y>z`, the
coefficient `s` is invertible modulo `r`, so semiprime coverage is equivalent
to prime coverage in rescaled residue classes.

This suggests that a Maynard/FGKMT prime-covering argument may extend with
only coefficient bookkeeping, rather than needing a genuinely new theorem
about semiprimes in arithmetic progressions.

## Status After Pass 4

The missing theorem has been reduced to a weighted prime-targeting cover with
many small coefficients `s<=z`.

Estimated full EP1139 closure after this pass:

```text
40-45%
```

The direction is now clearer and somewhat more promising: the semiprime layer
can be rewritten as coefficient-twisted prime coverage. But the weighted
covering theorem itself remains unproved.
