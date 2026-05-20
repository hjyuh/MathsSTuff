# EP-488 v86 A2 Pointwise Extension Theorem

Status: rigorous local theorem. This closes the A2-Induced extension
finite-window barrier, but does not by itself close A2-Induced, A2-Full, A4,
or EP-488.

## Theorem

Let `q/2 < a < q`, `5q/2 <= n < 3q`, and let `S` be a finite top-window set
disjoint from `{a}`. Define the new-coverage function

```text
N_x(a|S) =
  #{t <= x : q does not divide t, a divides t, and no s in S divides t}.
```

Then for every `m > n`,

```text
N_m(a|S)/m <= 2N_n(a|S)/n.
```

Consequently, if `S` is pointwise EP-safe, i.e.

```text
D_S(m;q)/m <= 2D_S(n;q)/n
```

for every `m > n`, then `S union {a}` is also pointwise EP-safe.

## Proof

Put

```text
R = floor(n/a).
```

The reduced top-window inequalities imply

```text
2 <= R <= 5.
```

For each `s in S`, define

```text
d_s = s / gcd(a,s),
```

and define

```text
h = q / gcd(a,q).
```

Since `a < q` and `a > q/2`, `h >= 3`.

Writing `t = ak`, we have

```text
q divides ak    iff h divides k,
s divides ak    iff d_s divides k.
```

Let

```text
Lambda = {h} union {d_s : s in S}.
```

Then

```text
N_x(a|S) = A(floor(x/a)),
```

where

```text
A(M) = #{1 <= k <= M : no lambda in Lambda divides k}.
```

If `m > n` and `floor(m/a) = R`, then `N_m(a|S) = N_n(a|S)` and therefore

```text
N_m(a|S)/m < N_n(a|S)/n <= 2N_n(a|S)/n.
```

It remains to consider `M = floor(m/a) > R`.

Since `m >= aM`,

```text
N_m(a|S)/m <= A(M)/(aM).
```

Since `n < a(R+1)`, it is enough to prove

```text
A(M)/M <= 2A(R)/(R+1)
```

for every `M > R`.

## Structural Restriction On Divisors

Only elements of `Lambda` at most `R` can affect `A(R)`. Elements larger than
`R` can only decrease `A(M)`, so they may be discarded for an upper bound on
`A(M)/M`.

The only subtlety is that the raw finite inequality fails for `R=4` with a
forbidden divisor `2`; however that pattern cannot occur in the top-window
when `R >= 4`.

Indeed, suppose `d_s = 2`. Write

```text
a = ug,  s = 2g,  gcd(u,2)=1.
```

If `R >= 4`, then `n >= 4a`, while `n < 3q`, so

```text
q > 4a/3 = 4ug/3.
```

Since `s > q/2`, we also have

```text
q < 2s = 4g.
```

Thus `u < 3`. Because `u` is odd, `u=1`; but then `s=2a`, contradicting
`s < q` and `a > q/2`. Hence `d_s=2` is impossible whenever `R >= 4`.

Thus the finite divisor cases are:

```text
R = 2: D subset {2}
R = 3: D subset {2,3}
R = 4: D subset {3,4}
R = 5: D subset {3,4,5}
```

where `D = {lambda in Lambda : lambda <= R}`.

## Finite Check

For these cases, the exact finite inequality

```text
A(M)/M <= 2A(R)/(R+1)
```

holds for all `M > R`.

This was also checked by the rerunnable exact certificate:

```text
ep488_v86_pointwise_finite_check.py
ep488_v86_pointwise_finite_check.json
```

The certificate uses the period `L = lcm(D)`. For `M = kL+r`,

```text
A(M) = kA(L) + A(r).
```

Since `A(L)/L <= 2A(R)/(R+1)` in each allowed case, it is enough to check
the least admissible `k` for every residue `r mod L`. The script checks all
18 allowed `(R,D)` cases and reports `all_ok = true`.

Worst cases:

```text
R = 2:
  worst D = {2}
  A(R) = 1
  sup_{M>R} A(M)/M = 2/3 at M=3
  2A(R)/(R+1) = 2/3
  slack = 0

R = 3:
  worst D = {2,3}
  A(R) = 1
  sup_{M>R} A(M)/M = 3/7 at M=7
  2A(R)/(R+1) = 1/2
  slack = 1/14

R = 4:
  worst D = {3,4}
  A(R) = 2
  sup_{M>R} A(M)/M = 3/5 at M=5
  2A(R)/(R+1) = 4/5
  slack = 1/5

R = 5:
  worst D = {3,4,5}
  A(R) = 2
  sup_{M>R} A(M)/M = 10/23 at M=23
  2A(R)/(R+1) = 2/3
  slack = 16/69
```

This proves

```text
N_m(a|S)/m <= 2N_n(a|S)/n.
```

The extension consequence follows from additivity of new coverage:

```text
D_{S union {a}}(x;q) = D_S(x;q) + N_x(a|S).
```

If `S` is safe, then

```text
D_{S union {a}}(m;q)/m
  = D_S(m;q)/m + N_m(a|S)/m
  <= 2D_S(n;q)/n + 2N_n(a|S)/n
  = 2D_{S union {a}}(n;q)/n.
```

So every top-window one-vertex extension of a safe set is safe. Iterating,
every finite top-window extension of a safe core is safe.

## Relation To v85

v85 proved the weaker asymptotic margin monotonicity:

```text
eta(S union {a}) >= eta(S).
```

v86 proves pointwise safety of the new contribution for every `m > n`, which
bypasses the finite-certificate window `E/eta` entirely.

The in-app GPT relay suggested this pointwise route, but its raw finite lemma
missed the structural exclusion of `d=2` for `R >= 4`. With that correction,
the proof goes through.

## Consequence For A2-Induced

The extension part of A2-Induced is now reduced to a clean statement:

```text
If every deletion-minimal induced high-defect core is EP-safe, then every
top-window extension of such a core is EP-safe.
```

Thus the remaining A2-Induced barrier is no longer finite-window control under
extensions. It is the core-completeness/classification problem:

```text
Every induced high-defect component must contain a certified deletion-minimal
high-defect core from the finite normalized family.
```

## v90 Strengthening

The consequence above is too conservative. Since the empty set is pointwise
safe, the extension theorem iterates from `S=empty` and proves the reduced
top-window inequality for every finite `C subset (q/2,q)`.

See:

```text
ep488-v90-reduced-topwindow-closure.md
```

This closes the reduced top-window `D_C` theorem directly; the remaining
question is whether the existing global reductions compose exactly to that
statement.

## Closure Status

```text
A2 extension finite-window barrier: closed
A2-Induced: not closed
A2-Full: not closed
A4: not closed
EP-488: not solved
```
