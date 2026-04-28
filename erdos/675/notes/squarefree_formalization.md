# EP675 squarefree shift lower bound

This note formalizes the squarefree lower-bound mechanism discussed in the
EP675 thread.

## Setup

Let

```text
S = {m >= 1 : m is squarefree}.
```

For `q >= 1` and `(r,q)=1`, define

```text
L_sf(q,r) = min {m >= 1 : m is squarefree and m == r mod q}.
```

Assume the following uniform least-squarefree-in-progressions hypothesis.

**Hypothesis H(theta).** There are constants `C >= 1` and `theta >= 1` such
that, for every `q >= 1` and every reduced residue class `r mod q`,

```text
L_sf(q,r) <= C q^theta.
```

The cleanest version of this note assumes such a bound for all moduli, because
the proof below will use `q = p^2`.

The known Nunes-type input has the shape

```text
L_sf(q,r) <= C_epsilon q^(36/25 + epsilon),
```

uniformly over reduced residue classes for squarefree moduli. Under an
all-moduli or prime-square-moduli version of that input, one may take
`theta = 36/25 + epsilon`. If one only uses Heath-Brown's older all-moduli
bound `L_sf(q,r) <<_epsilon q^(13/9+epsilon)`, the same proposition gives
`c < 9/26`.

## One-sided preservation is enough

The translation property for squarefree numbers asks for shifts `t` such that

```text
a is squarefree  iff  a+t is squarefree
```

for all `1 <= a <= n`. The lower bound below uses only the forward implication:

```text
a <= n and a squarefree  =>  a+t squarefree.
```

Thus it applies to any two-sided squarefree-preserving shift.

## Proposition

Assume `H(theta)`. Let `n >= 1` and `t >= 1` be such that

```text
a squarefree and 1 <= a <= n  =>  a+t squarefree.
```

Then for every prime `p` satisfying

```text
C p^(2 theta) <= n
```

we have

```text
p^2 | t.
```

Consequently, for every fixed

```text
c < 1/(2 theta),
```

and all sufficiently large `n`,

```text
prod_{p <= n^c} p^2 | t.
```

In particular,

```text
log t >= 2 sum_{p <= n^c} log p = (2+o(1)) n^c,
```

so

```text
t >= exp((2+o(1)) n^c).
```

For the minimal squarefree translation shift `t_n`, this gives

```text
t_n > exp(n^c)
```

for every `c < 1/(2 theta)` and all sufficiently large `n`.

With an all-moduli or prime-square-moduli exponent
`theta = 36/25 + epsilon`, this yields

```text
c < 25/72.
```

## Proof

Fix a prime `p` with `C p^(2 theta) <= n`. We prove `p^2 | t`.

### Case 1: `p` does not divide `t`

Then the class

```text
r == -t mod p^2
```

is reduced modulo `p^2`. By `H(theta)`, there is a squarefree integer `a`
such that

```text
a == -t mod p^2,
a <= C (p^2)^theta = C p^(2 theta) <= n.
```

Since `a` is squarefree and `a <= n`, the preservation hypothesis says that
`a+t` is squarefree. But `p^2 | a+t`, contradiction.

Therefore `p | t`.

### Case 2: `p` divides `t`, but `p^2` does not divide `t`

Write

```text
t = p u,    p does not divide u.
```

The class

```text
s == -u mod p
```

is reduced modulo `p`. By `H(theta)`, there is a squarefree integer `b` such
that

```text
b == -u mod p,
b <= C p^theta.
```

Because `b == -u mod p` and `p` does not divide `u`, we also have `p` not
dividing `b`. Hence

```text
a := p b
```

is squarefree. Moreover, since `theta >= 1`,

```text
a = p b <= C p^(theta+1) <= C p^(2 theta) <= n.
```

By preservation, `a+t` should be squarefree. But

```text
a+t = p b + p u = p(b+u),
```

and `b+u == 0 mod p`, so `p^2 | a+t`. This is impossible for a positive
squarefree integer.

Therefore the case `p || t` is impossible.

Combining the two cases gives `p^2 | t`.

Finally, if `c < 1/(2 theta)`, then for all sufficiently large `n` and all
primes `p <= n^c`,

```text
C p^(2 theta) <= C n^(2 theta c) <= n.
```

Thus `p^2 | t` for every prime `p <= n^c`. The product lower bound follows
from the prime number theorem in the form

```text
sum_{p <= x} log p = (1+o(1))x.
```

## Edge-case ledger

The only delicate point is when `-t mod p^2` is not a reduced residue class.
There are two possibilities:

1. `p^2 | t`. This is exactly the desired conclusion.
2. `p || t`. This is handled by reducing to the reduced residue class
   `-t/p mod p`, finding `b`, and using `a = p b`.

So the argument does not need a least squarefree representative in arbitrary
non-reduced residue classes modulo `p^2`.

The proof also works for `p=2`. In the second case, `b` is chosen odd modulo
`2`, so `2b` is squarefree.

## What this proves for EP675

The squarefree part of EP675 asks how quickly the minimal squarefree
translation shift grows. Conditional on `H(theta)`, the answer is at least

```text
exp(n^c)
```

for every `c < 1/(2 theta)`.

Using an all-moduli or prime-square-moduli exponent
`theta = 36/25 + epsilon`, this gives the claimed range

```text
c < 25/72.
```

The citation point is important. Nunes' 2017 paper proves the `36/25+epsilon`
least-representative exponent from distribution in squarefree moduli. The
present proof needs a least squarefree representative in the reduced residue
class `-t mod p^2`, so a bound for prime-square moduli, or for all moduli, is
needed for the first case. Heath-Brown's all-moduli exponent is enough to run
the argument with the slightly weaker range `c < 9/26`.

Thus this note should be read as a clean reduction: improving the
least-squarefree-in-AP exponent for prime-square moduli immediately improves
the EP675 squarefree shift exponent.

## References and next check

- D. R. Heath-Brown, "The least square-free number in an arithmetic
  progression", J. Reine Angew. Math. 332 (1982), 204-220. This gives an
  all-moduli least-squarefree-in-AP bound, commonly quoted with exponent
  `13/9 + epsilon`.
- R. M. Nunes, "A note on the least squarefree number in an arithmetic
  progression", Mathematika 63 (2017), 483-498; arXiv:1605.03347. This gives
  the `36/25 + epsilon` least-representative exponent from distribution in
  squarefree moduli.

The next citation task is to check whether the newer prime-power-moduli
literature gives `L_sf(p^2,r) << p^(72/25+epsilon)` or better uniformly in
`(r,p)=1`. If yes, the thread's `25/72` exponent follows exactly from the
proposition above. If not, the rigorous off-the-shelf exponent from this
argument is currently `9/26`.
