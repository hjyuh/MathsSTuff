# EP-488 v89 A2 Block Partition Theorem

Status: rigorous structural progress for A2-Induced. This does not close A2,
A4, or EP-488.

## Theorem

Let `C` be a connected reduced top-window induced core with

```text
epsilon(C) = beta(B_n(C,q)) - tau(C) = 2.
```

Decompose `B_n(C,q)` into its biconnected edge blocks. For each block `B`,
define

```text
beta(B) = |E(B)| - |V(B)| + 1,
tau(B)  = number of triple fibers whose three vertices lie in B,
epsilon(B) = beta(B) - tau(B).
```

Then every block has

```text
epsilon(B) >= 0.
```

Consequently, the positive block-epsilon partition of `C` is either

```text
[2]
```

or

```text
[1,1].
```

In particular:

```text
no block has epsilon >= 3;
no connected epsilon-2 core contains an epsilon-2 block plus another positive block;
no connected epsilon-2 core contains three positive epsilon-1 blocks.
```

This theorem does not require deletion-minimality. It applies to every
connected reduced top-window induced core with total `epsilon=2`.

## Proof

We use the v87 top-window triple-fiber structure:

```text
Every triple fiber is exactly {L/3, L/4, L/5}.
```

For such a triple fiber, the three pairwise lcms are all exactly `L`:

```text
lcm(L/3, L/4) = L,
lcm(L/3, L/5) = L,
lcm(L/4, L/5) = L.
```

Thus the triple fiber forms a triangle in `B_n(C,q)`.

Now an edge cannot belong to two distinct triple-fiber triangles. Indeed, if an
edge `{a,b}` lies in a triple fiber at height `L`, then

```text
lcm(a,b) = L.
```

If the same edge lay in a second triple fiber at height `L'`, then also

```text
lcm(a,b) = L',
```

so `L=L'`. But the triple fiber at height `L` is exactly
`{L/3,L/4,L/5}`, so the third vertex is unique. Hence the two triple fibers
are the same.

Therefore the triple-fiber triangles are edge-disjoint.

In any graph, edge-disjoint cycles are linearly independent in the cycle space:
for each such cycle, choose an edge belonging to no other selected cycle; a
nontrivial mod-2 sum cannot cancel that private edge. Hence in every block `B`,

```text
tau(B) <= beta(B).
```

So `epsilon(B)=beta(B)-tau(B)>=0`.

Cyclomatic number is additive over biconnected edge blocks:

```text
beta(B_n(C,q)) = sum_B beta(B).
```

Triple-fiber triangles also lie inside single biconnected blocks, because each
triangle is 2-connected. Since distinct triple-fiber triangles are counted in
their unique blocks,

```text
tau(C) = sum_B tau(B).
```

Therefore

```text
epsilon(C) = sum_B epsilon(B).
```

Since `epsilon(C)=2` and every block epsilon is a nonnegative integer, the
positive block-epsilon partition must be a partition of `2`, namely `[2]` or
`[1,1]`.

This proves the theorem.

## Audit

The theorem matches the full v88 audit:

```text
old q<=10000 cores: 158
new q=10001..15000 quick-audit cores: 99
total audited cores: 257

positive epsilon partition [2]:   177
positive epsilon partition [1,1]:  80
other positive partitions:          0
```

The audit artifact is:

```text
rotation-v88-gpt-relay/evals/v88_block_decomposition_audit_all46.json
```

The positive block-type partitions in the same audit are:

```text
[(2,0,2)]               68
[(3,1,2)]               62
[(4,2,2)]               47
[(1,0,1),(1,0,1)]       10
[(2,1,1),(1,0,1)]       62
[(2,1,1),(2,1,1)]        8
```

Here each tuple is `(beta,tau,epsilon)`. Thus the audited `[1,1]` branch is
made from unicyclic blocks `(1,0,1)` and triple-inflated unicyclic blocks
`(2,1,1)`.

## Consequence

This replaces the failed finite-skeleton theorem from v88 with a clean
block-additive theorem.

A2-Induced now splits into two precise subproblems:

```text
A2-Induced-[2]:
  certify every connected top-window epsilon-2 biconnected block.

A2-Induced-[1,1]:
  certify every bridge/tree connection of two epsilon-1 biconnected blocks.
```

The second branch is structurally close to unicyclic host-margin/A4 behavior,
but this note does not close that branch.

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```
