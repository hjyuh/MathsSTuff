# EP1190 Difficulty Assessment

Date: 2026-04-28

## Problem

Let

```text
epsilon_m = max sum_i 1/n_i,
```

where the maximum is over finite sequences

```text
m < n_1 < ... < n_k
```

for which one can choose residue classes `a_i mod n_i` such that no integer
lies in two of the chosen classes.

Estimate `epsilon_m`.

## Current Public Status

The Erdős Problems page for #1190 still marks the problem open. The listed
published consequence of de la Bretèche--Ford--Vandehey is

```text
L(m)^(-1+o(1)) < epsilon_m < L(m)^(-sqrt(3)/2+o(1)),
L(m)=exp(sqrt(log m log log m)).
```

The related counting problem #202 asks for the maximum `f(N)` of disjoint
congruence classes with distinct moduli at most `N`. The same BFV paper gives

```text
N / L(N)^(1+o(1)) < f(N) < N / L(N)^(sqrt(3)/2+o(1)).
```

BFV conjectured the lower bound is sharp.

## Recent Claimed Solution

The #202 discussion thread has a 2026-04-23 claimed solution, currently not
incorporated into the official page. The note claims

```text
f(N) = N / L(N)^(1+o(1)).
```

By partial summation, this gives

```text
epsilon_m = L(m)^(-1+o(1)).
```

The claimed new ingredient is a spread-core lemma using the Park--Pham
expectation-threshold theorem, replacing the older Erdős--Lovász/minimal-family
loss in the BFV descending-chain argument.

## Difficulty Estimate

If the claimed #202 proof is correct, EP1190 is essentially solved at the
natural `L`-scale. The remaining work is verification and polishing, not a new
attack.

Difficulty after the claimed note:

```text
verify / polish #1190 corollary: 3/10
verify full #202 proof carefully: 5-6/10
produce an independent clean writeup: 5/10
```

Difficulty before the claimed note:

```text
close the BFV exponent gap: 7/10
```

This is significantly less forbidding than EP1212. It is a serious
combinatorial-number-theory problem, but the claimed solution route uses a
known major theorem as a plug-in and modifies an existing proof framework.

## Main Risk Points

1. The Park--Pham spread-disjointness consequence must be applied with the
   correct expectation-threshold definitions and constants.
2. The dense-core lemma must replace the BFV Erdős--Lovász step without
   breaking the exact prime-power/residue descending chain.
3. The `o(1)` terms must be uniform across `O(sqrt(log x/log log x))` chain
   steps.
4. The partial summation from `f(N)` to `epsilon_m` is straightforward once
   the #202 asymptotic is proved.

## Current Best Guess

Conditional on the posted #202 argument surviving review:

```text
epsilon_m = exp(-(1+o(1)) sqrt(log m log log m)).
```

I would treat #1190 as likely near-closed, but not officially closed.

## Conditional Proof Artifact

The reduction from sharp EP202 to EP1190 is written separately:

```text
conditional-proof-from-202.md
solution-assuming-202.md
```

It proves both bounds by partial summation and by taking
`N=floor(m L(m)^2)` in an extremal EP202 construction, then discarding moduli
at most `m`.

If the sharp EP202 theorem is accepted, `solution-assuming-202.md` is a full
proof of EP1190 with no further input from the EP202 proof.
