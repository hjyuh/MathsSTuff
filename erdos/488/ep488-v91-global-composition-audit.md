# EP-488 v91 Global Composition Audit

Status: reduced top-window closed; global EP-488 not yet closed.

Date: 2026-05-19

## Summary

The v90 theorem proves the full reduced top-window inequality:

```text
If q/2 < a < q for every a in C and 5q/2 <= n < 3q, then

  D_C(m;q)/m <= 2D_C(n;q)/n

for every m > n.
```

This is stronger than the previous A2/A4 split because it does not require
connectedness, primitivity, high defect, unicyclic structure, or any graph
classification.

However, v90 does not by itself prove the original EP-488 statement. The
remaining composition gap is the global reduction from an arbitrary potential
counterexample to the range

```text
C subset (q/2,q),        5q/2 <= n < 3q.
```

The lower-strip reductions already cover the range below `5q/2` inside the
top-window framework. The unresolved global issue is the upper cutoff:

```text
n < 3q.
```

Older BBDS formalization notes show that the theorem `extremizer_bound`
depends on the remaining unproved lemma

```text
extremizer_implies_bad_block.
```

Therefore the composition to full EP-488 is still conditional unless this
global reduction is supplied by another rigorous argument.

## What v90 Closes

Within the reduced top-window framework:

```text
A2 high-defect branch: closed.
A4 unicyclic branch: closed.
Reduced top-window D_C theorem: closed.
```

Reason: v90 proves the actual `D_C` inequality for every finite `C` in the
upper strip, so the high-defect and unicyclic subdivisions are no longer
needed in that range.

## D_C To F_Q Composition

For `Q = C union {q}`, `q = max(Q)`, and

```text
D_C(x;q) = #{t <= x : q does not divide t and some a in C divides t},
```

we have the exact identity

```text
F_Q(x) = floor(x/q) + D_C(x;q).
```

If a `D_C` inequality is known for the relevant `n,m`, then it composes with
the `q`-row because for every `n >= q` and `m > n`,

```text
floor(m/q)/m <= 1/q < 2 floor(n/q)/n.
```

Indeed, if `k = floor(n/q) >= 1`, then `n < (k+1)q <= 2kq`.

Thus the `D_C` inequality is sufficient to imply the strict original `F_Q`
inequality in any regime where that `D_C` inequality has been proved.

## Exact Missing Lemma

The missing global composition lemma can be stated as:

```text
Global n<3q reduction.

Let Q be a finite primitive set, q=max(Q), C=Q\{q}, and suppose
m>n>=q. If

  F_Q(m)/m >= 2F_Q(n)/n

or equivalently the corresponding q-excluded counterexample survives after
the standard reductions, then there is a counterexample with

  q/2 < a < q for every a in C,
  5q/2 <= n < 3q.
```

The lower bound `5q/2 <= n` is supported by the lower-strip reductions once
top-window and component reductions are assumed. The upper bound `n < 3q` is
the remaining unclosed part.

In the BBDS Lean summary, the relevant dependency is:

```text
RunEndExtremal C q n m -> TopWindow C q -> BadBlock C q (Height q n)
```

named:

```text
extremizer_implies_bad_block
```

Without this or a replacement argument, the global proof cannot be certified.

## Why v90 Does Not Automatically Extend Past 3q

The v86 pointwise extension theorem uses

```text
R = floor(n/a) in {2,3,4,5},
```

which follows from `q/2 < a < q` and `5q/2 <= n < 3q`.

Outside that window the pointwise extension mechanism can fail.

Concrete marginal failure:

```text
q = 9
a = 6
S = {5,7,8}
n = 65
m = 258
```

Here `q/2 < 5,6,7,8 < q`, but `n >= 3q`. For

```text
N_x(a|S) =
  #{t <= x : q does not divide t, a divides t, and no s in S divides t},
```

exact computation gives

```text
N_65(6|S) = 2
N_258(6|S) = 16
```

and therefore

```text
N_258(6|S)/258 = 8/129
2N_65(6|S)/65 = 4/65
8/129 > 4/65.
```

So the v86/v90 induction cannot be naively promoted to all `n`.

This is not an EP-488 counterexample. For `C={5,6,7,8}`:

```text
D_C(65;9) = 27
D_C(258;9) = 106
(D_C(258)/258) / (2D_C(65)/65) ~= 0.494545.
```

It only shows that the current proof mechanism is genuinely upper-window
dependent.

## Current Percent Estimate

Defensible estimate: about 92-94% within the current framework.

Why higher than v55/v57:

- v90 removes the A2/A4 split inside the reduced top-window range.
- High-defect and unicyclic event-point branches are no longer separate
  mathematical obstacles once `5q/2 <= n < 3q` is reached.

Why not 100%:

- The global `n < 3q` reduction is not proved in the current audited ledger.
- The known formal BBDS path to that bound still depends on
  `extremizer_implies_bad_block`.
- v90's extension proof cannot simply be stretched beyond `3q`.

## Next Target

The next proof-search goal should be:

```text
Prove the global n<3q reduction, or replace it with a direct all-n
top-window D_C theorem.
```

The cleanest prompt is not another A2/A4 prompt. It should target the precise
composition blocker:

```text
Given v90, prove that every minimal EP-488 counterexample reduces to the
upper strip 5q/2 <= n < 3q, or produce a counterexample to that reduction.
```

