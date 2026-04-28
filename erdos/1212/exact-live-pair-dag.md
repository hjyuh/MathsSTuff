# Exact Live-Pair DAG for EP1212

Date: 2026-04-27

## Purpose

This note records the exact directed graph on composite live pairs. Unlike the
buffered graph, it contains no scale parameter and no slack condition. It is
the literal two-window condition needed to concatenate monotone visible
rectangles into an EP1212 path.

## Definitions

For integers `u < v`, define

```text
clr(u; v) = max { L >= 0 : gcd(u, product_{t=v}^{v+L} t) = 1 }.
```

Equivalently, `clr(u; v) >= L` iff

```text
gcd(u, product_{t=v}^{v+L} t) = 1.
```

The exact live-pair DAG `D_exact` has vertices the ordered pairs `(u, v)` such
that

```text
u, v are composite,
u < v.
```

There is a directed edge

```text
(u, v) -> (v, w)
```

iff

```text
u, v, w are composite,
u < v < w,
w - v <= clr(u; v),
gcd(w, product_{t=u}^{v} t) = 1.
```

The graph is acyclic because every edge strictly increases both entries after
one shift:

```text
(u, v) -> (v, w),    u < v < w.
```

## Infinite Rays Give EP1212 Paths

Let

```text
(a_0, a_1) -> (a_1, a_2) -> (a_2, a_3) -> ...
```

be an infinite directed ray in `D_exact`. Then every `a_i` is composite and

```text
a_0 < a_1 < a_2 < ...
```

For each `i >= 0`, the edge condition gives

```text
a_{i+2} - a_{i+1} <= clr(a_i; a_{i+1})
```

and hence

```text
gcd(a_i, t) = 1
```

for every integer `t` with `a_{i+1} <= t <= a_{i+2}`. It also gives

```text
gcd(a_{i+2}, product_{t=a_i}^{a_{i+1}} t) = 1,
```

so

```text
gcd(s, a_{i+2}) = 1
```

for every integer `s` with `a_i <= s <= a_{i+1}`.

Therefore the following monotone two-window path consists entirely of visible
lattice points:

```text
(a_i, a_{i+1})
  -> (a_i, a_{i+1}+1)
  -> ...
  -> (a_i, a_{i+2})
  -> (a_i+1, a_{i+2})
  -> ...
  -> (a_{i+1}, a_{i+2}).
```

On the vertical part the first coordinate is the composite number `a_i`. On the
horizontal part the second coordinate is the composite number `a_{i+2}`. Hence
every vertex has `min(x, y) > 1` and at least one composite coordinate.

Concatenating these finite paths over all `i` gives an infinite all-composite
two-window live zig-zag chain. In particular, it is an infinite EP1212 path.

## Converse

Conversely, suppose

```text
a_0 < a_1 < a_2 < ...
```

is a monotone all-composite two-window zig-zag chain in the natural sense that,
for every `i >= 0`, the rectangle path

```text
(a_i, a_{i+1})
  -> (a_i, a_{i+1}+1)
  -> ...
  -> (a_i, a_{i+2})
  -> (a_i+1, a_{i+2})
  -> ...
  -> (a_{i+1}, a_{i+2})
```

is visible at every vertex. Visibility on the vertical part implies

```text
gcd(a_i, product_{t=a_{i+1}}^{a_{i+2}} t) = 1,
```

so

```text
a_{i+2} - a_{i+1} <= clr(a_i; a_{i+1}).
```

Visibility on the horizontal part implies

```text
gcd(a_{i+2}, product_{t=a_i}^{a_{i+1}} t) = 1.
```

Since all `a_i` are composite and strictly increasing, these two conditions are
exactly the edge condition

```text
(a_i, a_{i+1}) -> (a_{i+1}, a_{i+2})
```

in `D_exact`. Thus any such monotone all-composite two-window zig-zag chain
yields an infinite directed ray in the exact live-pair DAG.

