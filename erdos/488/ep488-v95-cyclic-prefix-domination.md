# EP-488 v95 Cyclic Prefix Domination

Status: exact finite reformulation of the weak BBDS blocker.

Date: 2026-05-19

## What GPT Added

GPT narrowed `PrefixReserveAtomic` to a finite cyclic-prefix domination
problem.

Let

```text
mu(t) = #{r in C : r divides t and q does not divide t}
M(x) = sum_{t<=x} mu(t)
S(x) = 2D_C(x;q) - M(x).
```

Prefix reserve is:

```text
S(n) >= 2|C|
```

for every run-start prefix:

```text
mu(n)=0,
mu(n+1)>0,
n>=3q.
```

For each block:

```text
sigma_j = 2BlockCov(j) - SlotMass(j).
```

Then:

```text
BadBlock(j) iff sigma_j < 0.
```

So `AtomicClosed` is exactly:

```text
sigma_j >= 0 for every j >= 3.
```

## Finite-CPD

Set

```text
P = lcm_{r in C} r/gcd(r,q),
T = qP.
```

The block slack sequence has period `P`, and `mu(t)` has period `T`.

Thus the remaining finite lemma is:

```text
Finite-CPD:

If sigma_j >= 0 for every 3 <= j <= P+2,
then S(n) >= 2|C| for every run-start n in [3q, 3q+T).
```

This is currently the cleanest exact form of the weak BBDS interface.

## Verified GPT Example

GPT's obstruction to a naive local-prefix proof checks exactly:

```text
q = 18
C = {10,12,15}
P = 10
```

The block slacks are:

```text
sigma_3..sigma_12 = 4,0,3,3,0,4,2,3,3,2.
```

At `n=69`:

```text
mu(69)=0
mu(70)=1
D_C(69;18)=11
M(69)=14
|C|=3
M(69)+2|C|=20 <= 22=2D_C(69;18).
```

Inside block 4, the prefix slack is negative:

```text
rho_4(69) = -1.
```

So a nonbad full block can contain a negative run-start prefix. The missing
proof must use accumulated global reserve, not local block nonnegativity.

## New Search Script

The exact search script is:

```text
ep488_v95_cpd_search.py
```

It checks:

```text
primitive C subset (q/2,q),
P <= p_max,
sigma_j >= 0 for 3 <= j <= P+2,
run-start n in [3q,3q+qP),
S(n) >= 2|C|.
```

Search results:

```text
q <= 30, |C| <= 6, P <= 10000:
checked 10562 candidate sets
skipped_period 22174
no_bad_period 2692
failures 0
```

```text
q <= 40, |C| <= 3, P <= 10000:
checked 11085 candidate sets
skipped_period 1265
no_bad_period 4050
failures 0
```

These searches found no Finite-CPD counterexample.

## What Remains

The remaining proof chain is now:

1. Prove `Finite-CPD`.
2. Deduce `PrefixReserveAtomic`.
3. Combine prefix reserve with the row-growth inequality

```text
F_r(m) <= (m/n)(F_r(n)+2)
```

to prove:

```text
no BadBlock(j) for all j>=3
  =>
D_C(m;q)/m <= 2D_C(n;q)/n
```

under `RunEndExtremal`.

4. Contrapose to get the weak BBDS interface:

```text
RunEndExtremal, TopWindow, n>=3q
  =>
exists j>=3, BadBlock(j).
```

5. Use `AtomicClosed` to rule out that bad block, forcing `n<3q`.
6. Compose with v90 to close the original EP-488 framework.

Until Step 1 is proved, EP-488 is still not solved.

