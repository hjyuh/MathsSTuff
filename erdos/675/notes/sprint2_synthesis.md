# EP675 sprint synthesis

Date: 2026-04-27

## Executive verdict

This pass did not double the full EP675 percentage. It did something useful but
less dramatic: it separated the problem into one essentially finished
squarefree partial, one strong sums-of-two-squares lower-bound partial, one
conditional reduction for the sums-of-two-squares construction, and one
promising random/existential theorem for dense prime partitions.

The main negative finding is important:

```text
standard finite-complexity linear-correlation theorems do not prove the
parallel-shift tuple theorem needed for sums of two squares.
```

The forms arising from EP675 are

```text
A s + b_i,
```

so any two are affinely dependent. This is exactly the tuple-type case that
Matthiesen's finite-complexity theorem excludes and that
Freiberg-Kurlberg-Rosenzweig treat conjecturally.

## What improved

### 1. Squarefree exponent

The squarefree note can now safely present

```text
T_S(N) > exp(N^c)       for every c < 25/72,
```

provided it cites the published Nunes theorem and Mangerel's all-moduli
summary. The conservative Heath-Brown fallback remains

```text
c < 9/26.
```

The Zhong-Zhang prime-power paper is promising but cannot yet be used for an
explicit `p^2` exponent from public metadata alone.

### 2. Sums-of-two-squares lower bound

The forced-divisibility theorem is now in good shape. Under an AP input

```text
L_2(q^2,r) <= C q^theta
```

for reduced classes modulo `q^2`, any shift preserving `B_2` on `[1,N]`
satisfies

```text
q^{v_q(t)} > N/(C q^theta)
```

for every prime `q == 3 mod 4`, and hence

```text
log t >= ((1 - theta c)/(2c) + o(1)) N^c
```

for every `c < 1/theta`.

Linnik supplies an unconditional positive exponent.

### 3. Sums-of-two-squares construction

The construction is now reduced to a clean conditional theorem.

For fixed `N`, choose `A_N` divisible by enough powers of all primes up to `N`
and all inert primes `q == 3 mod 4`. For each

```text
a in B_2 cap [1,N],
```

consider

```text
L_a(s)=1+(A_N/a)s.
```

The tuple is locally admissible for sums of two squares. If a fixed
parallel-tuple theorem for `B_2` gives an `s` with all `L_a(s) in B_2`, then

```text
t_N=A_N s
```

is a translation witness. This is written in
`b2_conditional_translation_property.md`.

The missing theorem is not local; it is global:

```text
For every fixed locally admissible finite family A s+b_i,
infinitely many s make all values sums of two squares.
```

Current literature checked in this sprint does not prove this.

### 4. Dense prime partitions

The biggest positive move is the random/existential dense-prime-partition lane.

For a Bernoulli random partition of the primes, the set

```text
S(P) = {n : all prime factors of n lie in P}
```

should have the translation property almost surely, assuming only the standard
Brun/linear-sieve lemma that admissible finite tuples of affine-linear forms
simultaneously take values whose product has boundedly many prime factors.

This avoids prime-tuple conjectures. The bounded almost-prime factors are then
captured by the random prime set `P` with positive independent probability.

This gives:

```text
random/existential dense prime partition: 70-85%
adversarial/universal dense prime partition: 20-30%
```

The remaining task is to cite the almost-prime tuple lemma precisely.

## Current percentages

```text
Squarefree growth lower-bound partial:       85-90%
Sums-of-two-squares lower-bound partial:     80-90%
Sums-of-two-squares translation existence:   20-25%
Dense prime partition, random/existential:   70-85%
Dense prime partition, adversarial/universal:20-30%
Full EP675, all branches:                    30-40%
Headline B_2 route alone:                    25-30%
Publishable partial note:                    75-85%
```

The full-problem percentage did not double because the hoped-for standard
linear-pattern theorem is not available for parallel shifts.

## Best next move

Write a polished partial-results note with four pieces:

1. squarefree lower bound with `c < 25/72`;
2. sums-of-two-squares forced-divisibility lower bound;
3. random/existential dense-prime-partition theorem;
4. conditional theorem: fixed parallel-tuple conjecture for `B_2` implies the
   sums-of-two-squares translation property.

The highest-impact unresolved citation is the almost-prime tuple lemma for the
random dense-prime-partition result.

