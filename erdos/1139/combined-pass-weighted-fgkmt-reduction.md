# Combined Pass: Weighted FGKMT Reduction for EP1139

Date: 2026-04-28

## Purpose

This pass combines the next two proof steps:

```text
1. reduce EP1139 to one coefficient-weighted random covering theorem;
2. analyze whether that theorem is plausibly an existing Maynard/FGKMT-type
   input or a genuinely new lemma.
```

No computation is used.

## Parameter Choice

Take a slowly growing function `H=H(n)->infinity` and set

```text
z = floor(sqrt(n)/H),
y = n/z ~ sqrt(n) H,
A = floor(z/H) ~ sqrt(n)/H^2.
```

Then

```text
z -> infinity,
z <= sqrt(n),
A -> infinity,
A = o(z),
Ay ~ n/H = o(n).
```

Thus all primes used up to `Ay` have total logarithmic cost

```text
sum_{p <= Ay} log p = O(Ay)=o(n).
```

This is the economical regime needed for EP1139.

## Residual Tokens

After zeroing all primes `p <= y`, the previous decomposition gives residual
tokens:

```text
Type 0: two copies of primes q>y.
Type 1: one copy of s q <= n, where s=p^a<=z and q>y is prime.
Type P: one copy of pure prime powers p^a.
```

Type P has size `O(n/log n)` by the crude bound, but it is much smaller in the
economical scale after the main cover if needed; it can be assigned to cleanup
or folded into the same framework. The main targets are Type 0 and Type 1.

For reservoir primes

```text
R={r prime : y < r <= Ay},
```

we have

```text
s <= z < y < r.
```

Hence every coefficient `s` is invertible modulo every reservoir prime `r`.
The condition

```text
s q == a mod r
```

is equivalent to

```text
q == s^{-1}a mod r.
```

So the Type 1 layer is not a semiprime distribution problem. It is a prime
covering problem in coefficient-rescaled residue classes.

## The Final Covering Input

The following theorem would close EP1139.

**Coefficient-Weighted Random Covering Theorem.** For the parameters above,
there are probability distributions

```text
mu_r(a),       a mod r,       r in R,
```

and a typical token set `T_typ subset T_y(n)` such that:

```text
1. |T_y(n) \ T_typ| = o(n/log n).

2. One-point mass:
   for every t=(m,i) in T_typ,
   M(t):=sum_{r in R} mu_r(m mod r) >= C(n),
   where C(n)->infinity arbitrarily slowly.

3. Edge-size bound:
   with mu_r-probability 1-o(1), the selected residue class modulo r
   contains at most n^{o(1)} typical tokens.

4. Codegree bound:
   for distinct typical tokens t1=(m1,i1), t2=(m2,i2),
   sum_{r in R, m1==m2 mod r} mu_r(m1 mod r) = o(1)
   on average in the sense required by the FGKMT/Maynard covering lemma.
```

Then one may choose one residue `a_r mod r` for each `r in R` so that all but
`o(n/log n)` tokens are covered.

The remaining `o(n/log n)` tokens are covered singly by cleanup primes
`Ay < p <= n`, still at total logarithmic cost `o(n)`.

By `economical-two-cover-implies-1139.md`, this proves EP1139.

## Why a Covering Lemma Follows from the Four Conditions

This is the standard semi-random covering mechanism.

Sample each residue `a_r` independently using `mu_r`. For a typical token `t`,
the probability it survives all reservoir choices is at most

```text
exp(-M(t)) <= exp(-C(n)).
```

Thus the expected number of uncovered typical tokens is

```text
<= |T_typ| exp(-C(n)) = o(n/log n)
```

if `C(n)->infinity` slowly. Edge-size and codegree hypotheses are the standard
conditions needed to convert this expectation into an actual covering statement
using the Maynard/FGKMT random covering lemma or a Rödl-nibble/Janson form.

The atypical tokens and the final random leftovers are both `o(n/log n)`, so
the cleanup is economical.

## Candidate Construction of `mu_r`

For each reservoir prime `r`, define a target-weight score

```text
W_r(a)
  = lambda_0 * #{q prime : y<q<=n, q==a mod r}
    + sum_{s<=z} lambda_s *
        #{q prime : y<q<=n/s, q==s^{-1}a mod r}.
```

Then set

```text
mu_r(a) = W_r(a) / sum_b W_r(b).
```

The weights `lambda_s` should reflect the residual coefficient mass. A natural
first choice is

```text
lambda_0 ~ 1,
lambda_s ~ 1/s
```

or a normalized finite-core truncation of this rule. The sum over coefficients
is

```text
sum_{s=p^a<=z} 1/s = log log z + O(1).
```

The important feature is that all target counts are prime counts in arithmetic
progressions, not semiprime counts.

## What Existing Technology Should Supply

The Maynard/FGKMT large-gap machinery supplies exactly this kind of biased
residue distribution for prime targets:

```text
residue classes are weighted toward classes containing many primes;
one-point mass is amplified beyond the uniform sum 1/r;
pair-codegrees are controlled by divisibility of target differences;
semi-random covering turns the mass estimates into actual residue choices.
```

For Type 0 targets, this is directly the prime-target problem.

For Type 1 targets `s q`, the coefficient `s` only rescales the target residue
for `q`. Since `s<r`, it does not create a new local obstruction. Therefore
the main extension from the classical prime-target setting is not conceptual;
it is a bookkeeping issue over the growing coefficient set `s<=z`.

## The Actual Remaining Analytic Lemma

The single serious gap is:

> Prove Maynard/FGKMT one-point mass and codegree estimates uniformly for the
> weighted target score
>
> ```text
> W_r(a)
>   = prime targets in a
>     + coefficient-weighted prime targets in s^{-1}a, s<=z.
> ```

Equivalently, prove that the growing coefficient family can be handled by
truncating to finite coefficient cores, applying the prime-target covering
theorem uniformly on the core, and then sending the coefficient tail to zero
without losing the `o(n/log n)` cleanup budget.

This is very close in spirit to the finite-core strategy used in the EP689
proof, but harder because the small-prime zero stage and coefficient family now
move with `n`.

## Conditional Closure

Assuming the Coefficient-Weighted Random Covering Theorem, EP1139 is solved:

```text
CWRC theorem
=> economical two-cover
=> CRT bridge
=> intervals of length n with no Omega<=2 integers and log N=o(n)
=> limsup (u_{k+1}-u_k)/log k = infinity.
```

## Status After This Combined Pass

This pass does not produce an unconditional proof. It reduces the entire
remaining problem to one precise analytic covering theorem.

Percent estimates:

```text
Conditional on CWRC: 90-95%.
Unconditional EP1139 closure: 45-50%.
```

The route is now essentially a question of whether the Maynard/FGKMT weighted
prime-covering theorem can absorb a growing coefficient family `s<=z`.
