# EP-488 v87 A2 Minimal-Core Defect-Two Theorem

Status: rigorous A2-Induced structural theorem. This does not close A2,
A2-Full, A4, or EP-488.

## Theorem

Let `C0` be a connected reduced top-window induced component with

```text
epsilon(C0) >= 2.
```

Assume `C0` is deletion-minimal high-defect: for every vertex `v in C0`,
the induced graph on `C0 \ {v}` has

```text
epsilon(C0 \ {v}) <= 1.
```

For disconnected deletion graphs, use the total cyclomatic number

```text
beta(G) = |E(G)| - |V(G)| + components(G).
```

Then

```text
epsilon(C0) = 2.
```

Thus every induced high-defect component contains a deletion-minimal
high-defect core of exact defect `2`.

## Proof

Let

```text
H = B_n(C0,q),
V = |V(H)|,
E = |E(H)|,
beta = E - V + 1,
tau = tau(C0),
epsilon = beta - tau.
```

Because `H` is connected, this is the usual connected cyclomatic number.

### Triple Fibers

A triple fiber at height `L <= n`, `q` not dividing `L`, consists of vertices
of `C0` dividing `L`.

If `a in C0` divides `L`, then

```text
1 < L/a < 6,
```

because `q/2 < a < q` and `L < 3q`. Hence `L/a in {2,3,4,5}`.

For three vertices dividing the same `L`, their denominator set is a
three-element subset of `{2,3,4,5}`. Pairwise collision ratios must lie in

```text
{2:3, 3:4, 3:5, 4:5}.
```

The only possible three-element subset is `{3,4,5}`. Therefore every triple
fiber has exactly the vertices

```text
{L/3, L/4, L/5}.
```

In particular, if `t_v` is the number of triple fibers containing `v`, then

```text
sum_v t_v = 3tau.
```

Deleting `v` removes exactly `t_v` triple fibers and creates none:

```text
tau(H-v) = tau - t_v.
```

The "creates none" clause also follows from the no-`K4` lemma below: a
quadruple-or-larger fiber would contain a `K4`.

### No K4

After 5-smooth normalization, represent a vertex by its exponent vector

```text
(nu_2, nu_3, nu_5).
```

Every collision edge has difference vector in

```text
D = {
  +/-(-1,1,0),
  +/-(-2,1,0),
  +/-(0,-1,1),
  +/-(-2,0,1)
}.
```

A `K4` would give three distinct difference vectors `u,v,w in D` from one
vertex such that `u-v`, `u-w`, and `v-w` are also in `D` up to sign.

The eight-vector finite check has no such triple:

```text
K4 direction triples = []
```

This was verified directly by:

```powershell
python - <<'PY'
from itertools import combinations
D=[(-1,1,0),(1,-1,0),(-2,1,0),(2,-1,0),
   (0,-1,1),(0,1,-1),(-2,0,1),(2,0,-1)]
Ds=set(D)
tri=[]
for u,v,w in combinations(D,3):
    ok=True
    for a,b in [(u,v),(u,w),(v,w)]:
        diff=tuple(a[i]-b[i] for i in range(3))
        if diff not in Ds and tuple(-x for x in diff) not in Ds:
            ok=False
            break
    if ok:
        tri.append((u,v,w))
print(tri)
PY
```

So `H` contains no `K4`.

### Deletion Formula

For `v in V(H)`, let

```text
d_v = degree_H(v),
c_v = number of connected components of H-v.
```

Since `H` is connected, `c_v >= 1`. The total cyclomatic number after deletion
is

```text
beta(H-v) = (E-d_v) - (V-1) + c_v
          = beta - d_v + c_v.
```

Using the triple-fiber deletion formula:

```text
epsilon(H-v)
  = beta(H-v) - tau(H-v)
  = (beta - d_v + c_v) - (tau - t_v)
  = epsilon - d_v + c_v + t_v.
```

Deletion minimality gives `epsilon(H-v) <= 1`, hence

```text
d_v - c_v - t_v >= epsilon - 1.
```

Summing over all vertices:

```text
V(epsilon-1)
  <= sum_v d_v - sum_v c_v - sum_v t_v.
```

Now

```text
sum_v d_v = 2E,
sum_v c_v >= V,
sum_v t_v = 3tau.
```

Therefore

```text
V(epsilon-1) <= 2E - V - 3tau.
```

Since

```text
E = V + beta - 1 = V + tau + epsilon - 1,
```

we get

```text
V(epsilon-1)
  <= 2(V + tau + epsilon - 1) - V - 3tau
  = V + 2epsilon - 2 - tau.
```

Thus

```text
V(epsilon-2) <= 2epsilon - 2 - tau <= 2epsilon - 2.
```

Assume for contradiction that `epsilon >= 3`.

If `epsilon = 3`, then

```text
V <= 4.
```

If `epsilon >= 4`, then

```text
V <= 3.
```

For `V <= 3`, a simple graph has cyclomatic number at most `1`, so
`epsilon = beta - tau <= 1`, contradiction.

For `V = 4` and `epsilon = 3`, we have

```text
beta = epsilon + tau >= 3.
```

A connected simple graph on four vertices has `beta <= 3`, with equality only
for `K4`. But `K4` is impossible in the normalized four-ratio graph. This is
again a contradiction.

Therefore `epsilon` cannot be at least `3`. Since `C0` is high-defect,

```text
epsilon(C0) = 2.
```

## Regression Checks

theta13:

```text
|V| = 13
|E| = 14
beta = 2
tau = 0
epsilon = 2
```

Kimi:

```text
|V| = 16
|E| = 19
beta = 4
tau = 2
epsilon = 2
```

The two triple fibers are:

```text
{216,270,360}, lcm = 1080
{240,300,400}, lcm = 1200
```

v56 active theta core:

```text
|V| = 13
|E| = 14
beta = 2
tau = 0
epsilon = 2
```

The isolated vertices in the v56 full set do not affect the active
high-defect core.

## Consequence

The A2-Induced core-completeness problem no longer needs to consider
deletion-minimal cores with `epsilon >= 3`. Extensions can raise `epsilon`
from `2` to `3`, as v82/v83 observed, but the raised-defect objects are not
deletion-minimal high-defect cores.

The remaining A2-Induced core theorem is now:

```text
Finite epsilon-2 shape lemma:
Every deletion-minimal induced core with epsilon = 2 in the normalized
four-ratio/5-smooth graph belongs to the finite certified core family.
```

Equivalently, prove the missing bounded-diameter/finite-shape statement for
epsilon-2 deletion-minimal cores.

## Closure Status

```text
A2 minimal-core epsilon=2 theorem: closed
A2 extension finite-window barrier: closed by v86
A2-Induced: not closed
A2-Full: not closed
A4: not closed
EP-488: not solved
```

