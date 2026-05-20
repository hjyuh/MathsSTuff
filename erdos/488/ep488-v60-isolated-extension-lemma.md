# EP-488 v60 Isolated-Extension Lemma

Date: 2026-05-18

Status: rigorous partial theorem. This does not solve EP-488, A2, or A4.

## Purpose

v59 showed that the v56 theta high-defect near-miss can be strengthened by
adding many isolated top-window vertices. The grouped inclusion-exclusion
certificate becomes computationally weak as the number of isolates grows.

v60 proves that this isolate mechanism is harmless analytically. Isolated
top-window vertices can be added to any already-safe core without creating an
EP violation.

## Definitions

For `C subset (q/2,q)` define

```text
D_C(x;q) = #{t <= x : q does not divide t and exists a in C with a | t}.
```

For a singleton `a`, write

```text
c_x(a;q) = floor(x/a) - floor(x/lcm(a,q)).
```

The reduced top-window hypotheses are:

```text
q/2 < a < q,
5q/2 <= n < 3q,
m > n.
```

## Lemma 1: Singleton Top-Window Safety

For every `q/2 < a < q` and `5q/2 <= n < 3q`,

```text
c_m(a;q)/m < 2 c_n(a;q)/n
```

for every `m > n`.

### Proof

Let

```text
g = gcd(a,q), h = q/g, f = floor(n/a).
```

Since `a < q`, `h > 1`. Since `a > q/2`, the case `h = 2` is impossible:
`g = q/2` would force the only positive multiple of `g` below `q` and above
`q/2` to be absent. Hence `h >= 3`.

Also, since `5q/2 <= n < 3q` and `q/2 < a < q`,

```text
2 <= f <= 5.
```

Among the multiples `a,2a,...,fa`, a term is excluded by `q` exactly when
`h` divides its multiplier. Since `h >= 3` and `f <= 5`, at most one multiplier
is excluded. Therefore

```text
c_n(a;q) = f - floor(f/h).
```

If `f = 2`, then `floor(f/h)=0`, so `c_n(a;q)=2` and

```text
f + 1 = 3 <= 4 = 2 c_n(a;q).
```

If `f >= 3`, then either no multiplier is excluded and
`c_n(a;q)=f`, or one is excluded and `c_n(a;q)=f-1`. In both cases,

```text
f + 1 <= 2 c_n(a;q).
```

Since `f <= n/a < f+1`, we get

```text
1/a < (f+1)/n <= 2 c_n(a;q)/n.
```

Finally,

```text
c_m(a;q) <= floor(m/a) <= m/a,
```

so

```text
c_m(a;q)/m <= 1/a < 2 c_n(a;q)/n.
```

This proves the lemma.

## Lemma 2: Isolated Extension

Let `C0` be a reduced top-window set satisfying

```text
D_C0(m;q)/m <= 2 D_C0(n;q)/n
```

for every `m > n`.

Let `I` be a finite set of top-window vertices disjoint from `C0`. Assume every
vertex in `I` is isolated from `C0 union I` in the q-excluded graph `B_n`, i.e.
for every distinct `a in I` and `b in C0 union I`,

```text
lcm(a,b) > n or q divides lcm(a,b).
```

Then `C = C0 union I` also satisfies

```text
D_C(m;q)/m <= 2 D_C(n;q)/n
```

for every `m > n`.

### Proof

The isolation hypothesis means there is no q-excluded collision at height
`<= n` involving a vertex of `I`. Hence the `n`-side count is additive:

```text
D_C(n;q) = D_C0(n;q) + sum_{a in I} c_n(a;q).
```

For `m > n`, union subadditivity gives

```text
D_C(m;q) <= D_C0(m;q) + sum_{a in I} c_m(a;q).
```

Divide by `m` and apply the safety hypothesis for `C0` and Lemma 1 for each
singleton `a`:

```text
D_C(m;q)/m
 <= D_C0(m;q)/m + sum_{a in I} c_m(a;q)/m
 <  2D_C0(n;q)/n + sum_{a in I} 2c_n(a;q)/n
 =  2D_C(n;q)/n.
```

Thus isolated extensions of safe cores are safe.

## Computational Checks

Script:

```powershell
python .\ep488_v60_isolated_extension_check.py
```

Output:

```text
singleton q<=500 checked=10385375 failures=0
worst={q=498, n=1327, a=332, floor_n_over_a=3, c_n=2,
       q_over_gcd=3, margin=1/440564}

v56_core_plus_original_isolates:
isolated_at_n=True
D_additive=True
core_cert=certified
full_epsilon=2
ceiling ~= 0.8312098458
probe_ratio = 73408079/138734496 ~= 0.5291263609

v59_core_plus_20_near_q_isolates:
isolated_at_n=True
D_additive=True
core_cert=certified
full_epsilon=2
ceiling ~= 0.8700692997
probe_ratio = 13715159/21890484 ~= 0.6265352105
```

The v60 check also writes:

```text
ep488_v60_isolated_extension_check.json
```

## Consequences

This theorem certifies the v56 original isolate layer and the v59 greedy-20
near-`q` isolate layer without using the exploding grouped inclusion-exclusion
certificate for the full enlarged set.

It also proves a useful reduction:

```text
In A2 high-defect analysis, singleton B_n components may be discarded after
the non-singleton core components are proved safe.
```

More generally, if the full reduced top-window set decomposes into `B_n`
components and one component is a singleton, that singleton cannot be the cause
of an EP violation once the other components are safe.

## What Remains Open

This does not close A2 because non-singleton tree/unicyclic attachments and
connected high-defect components still require proof or classification.

This does not touch A4.

Closure state:

```text
A2: partially advanced, not closed
A4: not closed
EP-488: not solved
```
