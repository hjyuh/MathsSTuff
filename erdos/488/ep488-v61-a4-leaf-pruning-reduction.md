# EP-488 v61 A4 Leaf-Pruning Reduction

Date: 2026-05-18

Status: rigorous partial theorem for A4. This does not solve A4 or EP-488.

## Purpose

A4 asks for the unicyclic host-margin inequality

```text
2m H_U#(n) - n H_U#(m) >= n c_m(L_cyc)
```

for every connected unicyclic top-window host `U` and every relevant event
point `m`.

v61 proves that leaf attachments have nonnegative two-point margin. Therefore
A4 reduces from arbitrary connected unicyclic hosts to their cycle cores.

## Leaf Contribution

Let `a` be a leaf attached to `b`, and put

```text
L = lcm(a,b).
```

The contribution of this leaf-edge pair to the host numerator is

```text
P_x(a,b) = c_x(a;q) - c_x(L;q).
```

The leaf-pruning claim is:

```text
2m P_n(a,b) - n P_m(a,b) >= 0
```

for every reduced top-window configuration

```text
q/2 < a,b < q,
5q/2 <= n < 3q,
L <= n,
q does not divide L,
m > n.
```

## Proof Sketch

Write

```text
g = gcd(a,q),
h = q/g,
L = r a,
f = floor(n/a).
```

Top-window constraints imply:

```text
r in {2,3,4,5},
f in {r,r+1,...,5},
h >= 3.
```

For any `x`, the leaf contribution counts multipliers `k <= floor(x/a)` such
that neither `r | k` nor `h | k`:

```text
P_x = #{k <= floor(x/a) : r does not divide k and h does not divide k}.
```

Define

```text
A(k;r,h) = k - floor(k/r) - floor(k/h) + floor(k/lcm(r,h)).
```

Then `P_n = A(f;r,h)`.

Since `n < a(f+1)`, it is enough to show

```text
max_{k >= f} A(k;r,h)/k <= 2 A(f;r,h)/(f+1).
```

This is a finite multiplier table:

- `r in {2,3,4,5}`;
- `f in {r,...,5}`;
- `h in {3,4,5}` exact;
- `h >= 6` bounded by ignoring `h`-exclusions, since no `h`-multiple appears
  among `1,...,f`.

The only formal-looking bad multiplier row is

```text
r=2, f=4, h=3.
```

It is impossible geometrically. If `h=3`, then `q=3g` and the top-window
condition forces `a=2g`. If `r=2`, then `L=4g`. From `lcm(a,b)=L`, we get
`b | 4g`; but `3g/2 < b < 3g` leaves only `b=2g=a` or `b>3g`, so no distinct
top-window neighbor `b` exists.

Thus every realizable leaf contribution has nonnegative A4 margin.

## A4 Reduction

Let `U` be a connected unicyclic host. Remove a leaf `a` attached to `b`. The
cycle vertices and `L_cyc` are unchanged, and

```text
H_U#(x) = H_{U-a}#(x) + P_x(a,b).
```

Therefore

```text
2m H_U#(n) - n H_U#(m)
= 2m H_{U-a}#(n) - n H_{U-a}#(m)
  + (2m P_n(a,b) - n P_m(a,b)).
```

The parenthesized term is nonnegative. Repeating this pruning removes every
tree attached to the unique cycle.

Consequently:

```text
To prove A4 for all connected unicyclic hosts, it is enough to prove A4 for
leafless unicyclic hosts, i.e. pure cycle hosts.
```

This is the v61 A4 reduction.

## Checks

Script:

```powershell
python .\ep488_v61_a4_leaf_pruning_check.py --q-max 180
```

Output:

```text
finite_table_failures=0
edge_q_max=180
edge_checked=9854734
edge_failures=0
worst={q=10, n=26, a=9, b=6, m=27, P_n=1, P_m=2, L=18, margin=2}
```

The script writes:

```text
ep488_v61_a4_leaf_pruning_check.json
```

## What Remains For A4

The remaining A4 theorem is now:

For every pure cycle top-window host `Z`,

```text
2m H_Z#(n) - n H_Z#(m) >= n c_m(L_cyc(Z))
```

at every relevant event point `m`.

This still needs proof. The next A4 target is therefore a finite/structural
classification or direct analytic proof for pure cycles.

Closure state:

```text
A2: partially advanced, not closed
A4: reduced to pure cycle hosts, not closed
EP-488: not solved
```
