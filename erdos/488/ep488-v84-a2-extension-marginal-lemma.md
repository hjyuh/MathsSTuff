# EP-488 v84 A2 Extension-Marginal Lemma Audit

Status: A2 induced-branch progress from the GPT relay. This does not solve
A2, A4, or EP-488.

## Source

The in-app ChatGPT relay was asked to attack the current barriers. Its useful
output selected:

```text
Barrier: A2-Induced extension safety
Output D: precise missing lemma + proof attempt + failure point
```

The proposed invariant was the certificate margin

```text
eta(C) = 2D_C(n;q)/n - delta(C,q).
```

For an extension `C = S union {a}`, define the extension marginal

```text
mu(a | S) =
  2(D_{S union {a}}(n;q) - D_S(n;q))/n
  - (delta(S union {a},q) - delta(S,q)).
```

Then exactly:

```text
eta(S union {a}) - eta(S) = mu(a | S).
```

The relay suggested the local missing lemma:

```text
mu(a | S) >= 0
```

for every admissible top-window extension step, or at least a cumulative lower
bound strong enough to keep `eta > 0`.

## New Audit Script

```text
ep488_v84_a2_extension_marginal_audit.py
```

Command:

```powershell
python .\ep488_v84_a2_extension_marginal_audit.py `
  --json-out ep488_v84_a2_extension_marginal_audit.json
```

The script verifies the relay's exact regression numbers and checks `mu >= 0`
on:

```text
1. deletion marginals for theta13, Kimi, and v56;
2. every v82 one-vertex extension;
3. every v83 two-vertex extension;
4. both sequential orderings of every v83 two-vertex extension.
```

## Regression Margins

theta13:

```text
q = 451
n = 1350
eta = 8812/304425
weakest deletion marginal:
  a = 405
  mu = 67/101475
negative deletion marginals = 0
```

Kimi:

```text
q = 427
n = 1280
eta = 7279831/184464000
weakest deletion marginal:
  a = 375
  mu = 13849/20496000
negative deletion marginals = 0
```

v56:

```text
q = 71440
n = 213189
eta =
  15700975779116456429501422939962293/
  58174382838562688550787417989092892240
weakest deletion marginal:
  a = 60345
  mu = 33617877822/8711725270816555
negative deletion marginals = 0
```

These exactly match the relay's claimed regression values.

## v82 One-Vertex Extension Margins

```text
rows checked = 1852
negative mu count = 0
```

Worst margin:

```text
case = v79_motif_077_size26_q9001
q = 9001
n = 27000
core size = 15
added = 7200
extended epsilon = 3
mu = 4501/121513500
best/B = 13500/27001
delta/B = 399375/828092
```

This is important because the weakest one-step margin occurs on a row where
the extension raises `epsilon` to 3.

## v83 Two-Vertex Extension Margins

Total two-vertex margin:

```text
rows checked = 10933
negative total mu count = 0
```

Worst total margin:

```text
case = v79_motif_077_size26_q9001
q = 9001
n = 27000
core size = 15
added = {7200,7290}
extended epsilon = 3
extension component count = 1
total mu = 42509/364540500
best/B = 13500/27001
```

Sequential one-step margins inside the two-vertex rows:

```text
step checks = 43732
negative step mu count = 0
```

Worst sequential margin:

```text
case = v79_motif_089_size27_q7500
q = 7500
n = 21600
core size = 13
added = {4860,7290}
order = 4860 then 7290
stage = second
vertex = 7290
extended epsilon = 2
mu = 7/291600
best/B = 560/1107
```

## Interpretation

The relay did not solve A2-Induced, but it identified a clean candidate
invariant:

```text
extension-safety should be proved by controlling eta under additions.
```

The strongest currently tested local form,

```text
mu(a | S) >= 0,
```

survives all named regressions and every v82/v83 extension check. This gives a
sharper next theorem target than the previous informal "optional-extension
monotonicity" phrase.

## Missing Lemma

The new A2-Induced target is:

```text
Let S be an admissible reduced top-window set in the four-ratio/5-smooth
setting, and let a be an admissible top-window vertex such that S union {a}
preserves the reduced hypotheses. Then

  mu(a | S) >= 0.
```

Equivalently,

```text
2(D_{S union {a}}(n;q) - D_S(n;q))/n
  >= delta(S union {a},q) - delta(S,q).
```

If this local form is too strong globally, the weaker sufficient target is:

```text
For every certified minimal high-defect core C0 and every admissible extension
ordering a1,...,ak,

  eta(C0) + sum_i mu(ai | C0 union {a1,...,a_{i-1}}) > 0,

and the resulting finite certificate window is uniformly controllable.
```

## Failure Point

The audit proves no theorem. It only verifies that the marginal obstruction is
absent from:

```text
theta13, Kimi, v56,
all v82 one-vertex extensions,
all v83 two-vertex extensions and both orderings.
```

The proof still needs a structural inequality comparing the exact finite
new-coverage count at `n` against the asymptotic inclusion-exclusion marginal.

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```

