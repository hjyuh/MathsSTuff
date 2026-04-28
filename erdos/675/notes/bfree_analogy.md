# EP675 constructive lane D: B-free analogies and sums of two squares

Date: 2026-04-27

This note compares three translation-property settings:

1. squarefree numbers;
2. general `B`-free sets;
3. the set `B_2` of sums of two squares.

The goal is to decide whether `B_2` can be modeled by `B`-free technology well
enough to prove the translation property.

## 1. Translation-property template

For a set `A subset N`, a shift `t` is an `N`-witness if

```text
1_A(a+t) = 1_A(a)       for every 1 <= a <= N.
```

The standard construction for `B`-free sets has two phases.

First, freeze all small forbidden moduli so that nonmembers in `[1,N]` remain
nonmembers after shifting. Second, find a multiplier so that the finitely many
good prefix values remain good.

This phase split is still the right way to think about `B_2`.

## 2. Genuine B-free sets

Let `B` be a pairwise coprime set of integers `b >= 2`, and define

```text
A_B = {n >= 1 : b does not divide n for every b in B}.
```

For fixed `N`, put

```text
G_N = A_B cap [1,N],
L_N = prod_{b in B, b <= N} b.
```

If `t=L_N m`, then every bad prefix point remains bad:

```text
a notin A_B, a <= N  =>  a+t notin A_B.
```

For `a in G_N`, the condition `L_N m+a in A_B` excludes finitely many residue
classes modulo each `b>N`. Since the moduli in `B` are pairwise coprime, CRT
and Brun-type sieves can be applied directly.

This proves the translation property in the summable case

```text
sum_{b in B} 1/b < infinity,
```

and in the thinner nonsummable case recorded on the EP675 page,

```text
sum_{b<x, b in B} 1/b = o(log log x).
```

Squarefree numbers are the model example:

```text
B = {p^2 : p prime}.
```

## 3. Why `B_2` is not literally B-free

Let

```text
B_2 = {n >= 1 : n = x^2+y^2 for some x,y in Z}.
```

By the two-squares theorem,

```text
n in B_2
iff
v_q(n) is even for every prime q == 3 mod 4.
```

So the forbidden local event at `q == 3 mod 4` is

```text
v_q(n) = 1,3,5,...
```

not simply `q | n` or `q^2 | n`.

For one fixed bad prime `q`, the good local set is

```text
{v_q(n)=0} union {v_q(n)=2} union {v_q(n)=4} union ...
```

This is an infinite alternating `q`-adic condition. It is not a single
divisibility avoidance condition.

Equivalently, the bad set is

```text
union_{j >= 0} { q^(2j+1) || n }.
```

The exact-valuation symbol `||` is the obstruction: exact valuation is a
Boolean combination of two divisibility conditions,

```text
q^(2j+1) | n  and  q^(2j+2) does not divide n,
```

and all `j` are needed globally.

Thus:

```text
B_2 is not an A_B set for any pairwise-coprime forbidden-moduli family B.
```

It is also not a finite Boolean combination of fixed `B`-free sets, because
any finite Boolean combination can only inspect finitely many valuation
thresholds at a fixed prime, while `B_2` needs parity at arbitrarily high
`q`-adic depth.

## 4. Finite-prefix inverse-limit model

Although `B_2` is not globally finite Boolean, it is locally finite on a fixed
prefix.

Fix `N`. For a bad prime

```text
q == 3 mod 4,
```

define

```text
E_q(N) = 1 + floor(log_q N).
```

For every `a <= N`, the value `v_q(a)` is determined by `a mod q^E_q(N)`.
Hence membership in `B_2` on `[1,N]` is determined by the finite modulus

```text
M_N^loc = prod_{q <= N, q == 3 mod 4} q^E_q(N).
```

If a shift `t` is divisible by `M_N^loc`, then, for every `a <= N` and every
bad prime `q <= N`,

```text
v_q(a+t) = v_q(a).
```

Indeed, if `v_q(a)=e<E_q(N)`, then `a+t == a mod q^(e+1)`, so the valuation
is unchanged.

Therefore the small bad primes can be frozen exactly, just as in the B-free
case. The difference is only in the tail:

```text
For a in B_2 cap [1,N], we still need a+t to have even valuation at every
bad prime q > N.
```

This gives an inverse-limit picture:

```text
B_2 = inverse limit of finite q-adic parity cylinders.
```

The inverse-limit formulation handles the local prefix constraints, but it
does not by itself construct the multiplier.

## 5. A clean sufficient reduction

Let

```text
F_N = B_2 cap [1,N],
M_N = prod_{q <= N, q == 3 mod 4} q^E_q(N).
```

It is enough to find `s >= 1` such that

```text
M_N s + a in B_2       for every a in F_N.
```

Then `t=M_N s` is an `N`-witness for `B_2`.

Proof:

- If `a in F_N`, the condition is exactly the positive side.
- If `a notin B_2`, then there is a bad prime `q == 3 mod 4` with
  `v_q(a)` odd. Since `a <= N`, this prime satisfies `q <= N`, and
  `v_q(a)<E_q(N)`. Because `M_N | t`, the valuation is preserved:

```text
v_q(a+t)=v_q(a),
```

so `a+t notin B_2`.

Thus the full translation-property problem for `B_2` reduces to this finite
linear-pattern problem:

> For every `N`, can the finite set of linear forms
>
> ```text
> L_a(s)=M_N s+a,      a in B_2 cap [1,N],
> ```
>
> simultaneously take values in `B_2`?

This is the correct analogue of the `B`-free multiplier problem.

## 6. A stronger Q-free sufficient condition

There is an even stronger condition that is closer to ordinary B-free sieving.

Let

```text
Q = {q prime : q == 3 mod 4}.
```

If we can find `s` such that, for every `a in F_N`, the number

```text
M_N s+a
```

has no prime factor from `Q` except those already frozen by `M_N`, then all
these values are in `B_2`.

After freezing the small primes, this becomes a finite tuple of linear forms
that must avoid the positive-density prime set `Q`.

Heuristically, for `m=|F_N|`, the expected number of `s <= X` satisfying this
stronger condition is about

```text
X / (log X)^(m/2),
```

which tends to infinity for fixed `N`.

However, this is no longer the dimension-zero Brun situation. The forbidden
primes have reciprocal density `1/2`:

```text
sum_{q <= x, q == 3 mod 4} 1/q ~ (1/2) log log x.
```

So the ordinary squarefree proof does not transfer automatically. Proving the
strong Q-free condition for many simultaneous forms is closer to a positive-
dimension linear sieve or multiplicative-set linear-forms theorem.

## 7. Multiplicative factoring variant

There is a useful reformulation that may be better than `M_N s+a`.

Let

```text
A_N = lcm(1,2,...,N) * M_N.
```

Take shifts of the form

```text
t=A_N s.
```

For each positive prefix value `a in F_N`, write

```text
a+t = a (1 + (A_N/a)s).
```

Since `a in B_2` and `B_2` is multiplicatively closed, it is enough to find
`s` such that every form

```text
1 + (A_N/a)s,      a in F_N,
```

lies in `B_2`.

The nonmember side is still frozen by the `M_N` factor in `A_N`.

This reduces the constructive problem to simultaneous `B_2` values of linear
forms with constant term `1`. These forms have no obvious local obstruction at
bad primes: for every `q == 3 mod 4`, the value is `1 mod q` whenever
`q | A_N/a`, and otherwise only one residue class of `s mod q` is dangerous
at valuation `1`.

This looks like the most promising abstract interface:

> If every finite admissible tuple of linear forms can be simultaneously
> specialized to sums of two squares, then `B_2` has the translation property.

The word "admissible" must include the local `q`-adic parity conditions for
all `q == 3 mod 4`.

## 8. What a black-box theorem would need to say

A sufficient theorem would be:

**Finite linear-pattern theorem for `B_2`.**  
Let

```text
L_i(s)=u_i s+v_i,       1 <= i <= m,
```

be finitely many nonconstant affine-linear forms with integer coefficients and
positive leading coefficients. Suppose there is no local obstruction to all
`L_i(s)` being sums of two squares. Then there exists an integer `s` such that

```text
L_i(s) in B_2       for all i.
```

This theorem would immediately imply the translation property for `B_2`, by
applying it to the forms in Section 5 or Section 7.

This is weaker than a Hardy-Littlewood theorem for primes. The set `B_2` has
size asymptotic to `C x / sqrt(log x)`, and finite simultaneous patterns are
expected to have order

```text
X / (log X)^(m/2)
```

solutions. But it is still a serious sieve/automorphic input, not a direct
corollary of the elementary B-free argument.

Recent work on finite patterns in sums of two squares may be relevant here,
but the exact theorem needed is broader than "there are long consecutive runs"
unless it handles arbitrary finite tuples of affine-linear forms.

## 9. What fails if we try to use B-free sets directly

The following tempting reductions fail.

### Attempt 1: `B_2` as one B-free set

False. Avoiding a set of divisibility moduli can only say "these moduli do not
divide `n`." It cannot allow `q^2 | n` but forbid `q || n`.

### Attempt 2: `B_2` as finite Boolean combination of B-free sets

False globally. For each bad prime `q`, membership depends on valuation parity
at every depth.

### Attempt 3: use Brun's dimension-zero condition

Not enough. The first-level forbidden primes `q == 3 mod 4` have positive
reciprocal density, so

```text
sum_{q <= x, q == 3 mod 4} 1/q ~ (1/2) log log x,
```

not `o(log log x)`.

### Attempt 4: force every translated good value to avoid bad primes

This is sufficient and plausible, but it is a positive-dimension linear sieve
problem for a growing finite tuple. It is not the same easy argument that
proves the squarefree translation property.

## 10. Current verdict

The B-free analogy is useful, but only up to the local-freezing step.

The correct picture is:

```text
squarefree:
    true pairwise-coprime B-free set
    => freeze small p^2
    => dimension-zero/summable sieve finds the multiplier

sums of two squares:
    inverse limit of q-adic parity cylinders
    => freeze small q == 3 mod 4 valuations
    => need finite linear-pattern recurrence inside B_2
```

So `B_2` can be modeled as an inverse limit of finite local conditions, and
that is enough to reduce EP675 to a clean finite-pattern theorem. It is not
enough to prove the translation property by existing B-free Brun machinery
alone.

## 11. Best next theorem target

The next useful target is a conditional proposition:

**Proposition.** Suppose `B_2` satisfies the finite linear-pattern theorem from
Section 8. Then `B_2` has the translation property.

This proposition should be written formally. It would turn the full EP675
headline question into a precise known-theorem search:

```text
Does the literature prove finite affine-linear patterns in sums of two squares
under local admissibility?
```

If yes, EP675 may be close. If no, this lane identifies the missing analytic
input exactly.

