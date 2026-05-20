# EP-488 v94 Prefix-Reserve Audit

Status: audit of GPT's proposed BBDS replacement inequality.

Date: 2026-05-19

## GPT Proposal

GPT proposed reducing the weak BBDS interface to the prefix-reserve
inequality:

```text
M(n) + 2|C| <= 2D_C(n;q),
```

where

```text
M(x) = sum_{t<=x} #{r in C : r|t and q does not divide t}.
```

Together with the per-row growth bound

```text
F_r(m) <= (m/n)(F_r(n)+2),
```

this would imply

```text
D_C(m;q)/m <= 2D_C(n;q)/n.
```

So proving prefix reserve under `AtomicClosed` would close the weak BBDS
interface and hence the global `n < 3q` reduction.

## Important Correction

Prefix reserve is false if one only assumes nonbadness of the complete blocks
seen near the prefix.

Exact failure:

```text
q = 31
C = {16,18,20,24,27,30}
n = 95
```

This is top-window and primitive. Also:

```text
n >= 3q,
n is uncovered,
n+1 = 96 is covered.
```

Exact prefix values:

```text
D_C(95;31) = 17
M(95) = 23
|C| = 6
```

Therefore

```text
M(95) + 2|C| = 23 + 12 = 35
2D_C(95;31) = 34
```

so prefix reserve fails by `1`.

The early complete blocks are not bad:

```text
block 1: cov=6, mass=6, slack=6
block 2: cov=6, mass=9, slack=3
block 3: cov=5, mass=8, slack=2
block 4: cov=5, mass=9, slack=1
block 5: cov=6, mass=8, slack=4
block 6: cov=5, mass=9, slack=1
```

The failure is not a contradiction to the full `AtomicClosed` route, because
this `C` has later bad blocks. The block period is `2160`, and the first bad
block is:

```text
j=16, BlockCov=3, SlotMass=7.
```

## Search Check

A bounded all-period search found no prefix-reserve failures under the stronger
condition that no bad block occurs over the whole block period.

Search:

```text
q < 31,
primitive C subset (q/2,q),
|C| <= 6,
block period <= 10000,
n in [3q,12q),
n uncovered, n+1 covered.
```

Result:

```text
checked 10562 candidate sets
2692 all-period nonbad sets
0 prefix-reserve failures
```

This is only evidence, not a proof.

## Updated Missing Lemma

The proof target should be strengthened to use all-height nonbadness:

```text
PrefixReserveAtomic:

TopWindow(C,q)
n >= 3q
n uncovered
n+1 covered
forall j >= 3, not BadBlock(C,q,j)
  =>
M(n) + 2|C| <= 2D_C(n;q).
```

If this is proved, then GPT's growth argument gives the weak BBDS interface:

```text
RunEndExtremal(C,q,n,m), TopWindow(C,q), n>=3q
  =>
exists j>=3, BadBlock(C,q,j).
```

## Failure Point

The missing mechanism is a future-block discharge:

```text
prefix reserve failure at a run start
  =>
some future block j>=3 is bad.
```

The q=31 example shows why local prefix slack alone is insufficient. It fails
prefix reserve at `n=95`, and the debt is eventually exposed as a bad block at
height `16`.

