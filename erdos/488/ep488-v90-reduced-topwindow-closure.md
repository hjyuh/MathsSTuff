# EP-488 v90 Reduced Top-Window Closure

Status: rigorous reduced-framework theorem. This closes the reduced
top-window `D_C` inequality. It should close the remaining A2/A4 top-window
branches if the existing global reductions compose exactly to this reduced
statement. This note does not independently reprove those global reductions.

## Theorem

Let `q` be fixed and let

```text
5q/2 <= n < 3q.
```

Let `C` be any finite set satisfying

```text
q/2 < a < q    for every a in C.
```

Define

```text
D_C(x;q) =
  #{t : 1 <= t <= x, q does not divide t, and some a in C divides t}.
```

Then for every `m > n`,

```text
D_C(m;q)/m <= 2D_C(n;q)/n.
```

No connectedness, primitivity, high-defect, unicyclic, or block-structure
hypothesis is needed for this reduced top-window inequality.

## Proof

Order the elements of `C` arbitrarily:

```text
C = {a_1,...,a_k}.
```

Let

```text
S_0 = empty,
S_i = {a_1,...,a_i}.
```

The empty set is pointwise safe:

```text
D_empty(m;q)/m = 0 <= 0 = 2D_empty(n;q)/n.
```

Now apply the v86 pointwise extension theorem. For any finite top-window set
`S` and any `a` with `q/2<a<q`, define the new contribution

```text
N_x(a|S) =
  #{t <= x : q does not divide t, a divides t, and no s in S divides t}.
```

v86 proves, for every `m>n`,

```text
N_m(a|S)/m <= 2N_n(a|S)/n.
```

Since

```text
D_{S union {a}}(x;q) = D_S(x;q) + N_x(a|S),
```

pointwise safety of `S` implies pointwise safety of `S union {a}`.

By induction on `i`, every `S_i` is pointwise safe. Taking `S_k=C` gives

```text
D_C(m;q)/m <= 2D_C(n;q)/n
```

for every `m>n`.

This proves the theorem.

## Consequence For The Original Top-Window F_Q Statement

If `Q = C union {q}` with `q=max(Q)` and `C subset (q/2,q)`, then

```text
F_Q(x) = floor(x/q) + D_C(x;q).
```

Since `5q/2 <= n < 3q`, we have

```text
floor(n/q) = 2.
```

For every `m>n`,

```text
floor(m/q)/m <= 1/q < 4/n = 2 floor(n/q)/n,
```

because `n<3q`.

Combining this strict `q`-term inequality with the non-strict `D_C` inequality
gives

```text
F_Q(m)/m < 2F_Q(n)/n.
```

Thus the original strict EP inequality holds for every reduced top-window
instance.

## Audit

The audit script

```text
ep488_v90_topwindow_pointwise_audit.py
```

checks the composed theorem directly.

Exhaustive small audit:

```text
q <= 22
all C subset (q/2,q)
m <= 20q
checked rows: 13,403,885
D violations: 0
F violations: 0
worst D ratio: 11/14
worst F ratio: 65/88
```

Artifact:

```text
rotation-v88-gpt-relay/evals/v90_topwindow_pointwise_audit_q22_full.json
```

## Ledger Impact

This theorem supersedes the narrower v86 interpretation:

```text
"If every deletion-minimal high-defect core is safe, extensions are safe."
```

The stronger conclusion is:

```text
Every reduced top-window C subset (q/2,q) is safe, starting from the empty set.
```

Therefore:

```text
A2 high-defect top-window branch: closed inside the reduced framework.
A4 unicyclic top-window branch: closed inside the reduced framework.
Reduced top-window framework: closed.
```

What remains before claiming EP-488 solved is an explicit composition audit:
the existing global reductions must be checked line by line to confirm that
all remaining original EP-488 cases reduce to this exact top-window statement
with no extra unresolved hypotheses.

## Closure Status

```text
Reduced top-window D_C theorem: closed.
A2 within reduced top-window: closed.
A4 within reduced top-window: closed.
Global EP-488: not claimed here.
```
