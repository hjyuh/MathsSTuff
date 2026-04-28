# Mainline Squarefree Audit

Date: 2026-04-27

## Verdict

The linked squarefree proof is mathematically clean at the local-congruence
level. The only serious external gate is the analytic input for least
squarefree integers in arithmetic progressions modulo `p^2`.

If the quoted Nunes published corollary is available exactly as used, the
squarefree growth subquestion is essentially closed:

```text
T_S(N) > exp(N^c) for every fixed c < 25/72.
```

Here `T_S(N)` is the least positive shift preserving the squarefree indicator on
`[1,N]`.

## Abstract Lemma

Assume there is an exponent `theta` such that for every epsilon positive there is
`C_epsilon` with the following property:

```text
For every q >= 1 and every reduced residue r mod q,
there is a squarefree a <= C_epsilon q^(theta+epsilon)
with a == r mod q.
```

Then every squarefree-preserving shift `t` on `[1,N]` is divisible by `p^2` for
every prime

```text
p <= N^c
```

provided

```text
c < min(1/(2 theta), 1/(1 + theta)).
```

Consequently

```text
t >= prod_{p <= N^c} p^2 = exp((2c+o(1))N^c),
```

so in particular `t > exp(N^c)` for all sufficiently large `N`.

## Proof Check

Fix a prime `p <= N^c` and suppose `p^2` does not divide `t`.

### Case 1: `p` does not divide `t`

The residue `-t mod p^2` is reduced. By the least-squarefree input with
`q=p^2`, choose squarefree `a` with

```text
a == -t mod p^2,
a <= C p^(2 theta + epsilon).
```

If `c(2 theta + epsilon) < 1`, then `a <= N` for large `N`. Thus `a` is
squarefree, while `a+t` is divisible by `p^2`, contradiction.

### Case 2: `p | t` but `p^2` does not divide `t`

Write `t = p u` with `p` not dividing `u`. The residue `-u mod p` is reduced.
Choose squarefree `b` with

```text
b == -u mod p,
b <= C p^(theta + epsilon).
```

Then `p` does not divide `b`, so `a = p b` is squarefree. Also

```text
a+t = p(b+u)
```

is divisible by `p^2`. If `c(1+theta+epsilon) < 1`, then `a <= N` for large
`N`, contradiction.

So `p^2 | t`.

## Nunes Exponent

The squarefree note uses `theta = 36/25`, giving

```text
1/(2 theta) = 25/72,
1/(1+theta) = 25/61.
```

The limiting exponent is therefore `25/72`.

Important citation issue: the arXiv version of Nunes states the `36/25` least
squarefree result for squarefree moduli. The EP675 note claims the published
Mathematika version states the needed bound uniformly for all coprime pairs
`(r,q)`, and explicitly supports `q=p^2`. This exact published statement must
be checked before treating the squarefree note as final.

## Possible Improvement Route

A 2026 Journal of Number Theory paper by Zhong and Zhang studies squarefree
integers in arithmetic progressions to prime power moduli and claims a new
record upper bound for the least squarefree integer with prime power modulus.
If their result gives a better exponent for `q=p^2`, then the EP675 squarefree
exponent improves from `25/72` to

```text
min(1/(2 theta_new), 1/(1+theta_new)).
```

This is the highest-leverage literature check.
