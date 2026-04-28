# Slab-Flow Survival Pass

Date: 2026-04-28

## Purpose

This pass tests the warning from the closure attempts:

```text
Mean core-to-core outdegree > 1 does not imply compatible infinite survival.
```

The new script computes finite backward-pruned reachability in the right-core
graph. For each right-core state, it records the farthest complete dyadic slab
reachable by directed core-to-core paths.

## Artifacts

Script:

```text
scripts/slab_flow_survival.py
```

The script supports the strict core from the later 5.5 pass:

```text
--core-multiplier 2.1
```

This requires

```text
P^-(u), P^-(v) > floor(2.1 H(v)) + 1.
```

Verifier:

```text
scripts/verify_buffered_certificate.py
```

Result files:

```text
results/slab-flow-smoke.json
results/slab-flow-theta-N200000.json
results/slab-flow-theta-N1000000.json
results/slab-flow-logpower-N1000000.json
results/slab-flow-theta036-N2200000.json
results/slab-flow-theta036-N4300000.json
```

All emitted certificate paths in these files were verified.

## Method

The flow graph contains only `H`-buffered right-core states `(u,v)`:

```text
u,v composite,
u < v,
v-u <= H(v),
clr(u;v) >= H(v),
P^-(v) > H(v)+1.
```

There is a directed edge `(u,v) -> (v,w)` if the target state is also
right-core and `w` satisfies the raw live condition:

```text
gcd(w, product_{t=u}^v t) = 1.
```

Incomplete dyadic slabs are excluded by default. The important reported
statistics are:

```text
reach_next_slab_fraction:
  fraction of states in a slab that can reach any state in the next slab.

survive_to_top_slab_fraction:
  fraction of states in a slab that can reach the highest complete slab
  in the finite run after backward pruning.
```

## Polynomial Results

For `H(x)=floor(x^theta)`, `N=200000`, the highest complete slab is
`[65536,131072)`. Every theta tested has zero flow across the preceding
`[32768,65536) -> [65536,131072)` boundary.

```text
theta   states in [32768,65536)   reach next
0.34    2774                      0
0.36    2488                      0
0.38    2090                      0
0.40    1603                      0
0.42    1079                      0
0.45     338                      0
```

For `N=1000000`, some higher boundary crossings appear, but the old
`32768 -> 65536` barrier remains.

```text
theta   [65536,131072) reach next   [131072,262144) reach top
0.34    0.00000                     0.00611
0.36    0.00452                     0.00589
0.38    0.00372                     0.00652
0.40    0.00663                     0.00340
```

For theta `0.36`, larger caps show the key compatibility problem.

```text
cap       slab                  states    mean out   reach next   survive to top
2200000   [262144,524288)        35056    2.982      0.01090      0
2200000   [524288,1048576)       85914    3.788      0.00227      0.00227

4300000   [262144,524288)        35056    2.982      0.01090      0
4300000   [524288,1048576)       85914    3.788      0.00227      0
4300000   [1048576,2097152)     206815    4.784      0.00716      0.00716
```

Interpretation:

```text
The graph has local branching and it has one-boundary crossings.
But the crossing image from one slab is not landing inside the next slab's
own forward-surviving subset.
```

This is the finite version of the min-cut/compatibility obstruction.

## Polylog Result

For `H(x)=floor(log(x)^2)` at `N=1000000`:

```text
slab                states   mean out   reach next   survive to top
[65536,131072)       2560    1.402      0.00742      0
[131072,262144)      9290    2.296      0.00398      0.00398
[262144,524288)     27795    3.145      0            1
```

This mirrors the polynomial run: local branching is real, but compatible
multi-slab survival is not yet visible.

## Strong C-Core Result

The later 5.5 closure note suggested using a stronger core
`P^-(u),P^-(v)>(2+epsilon)H(v)` so that future clearance is automatic and the
remaining transition problem is a rough-semiprime expansion problem with one
anchored exclusion window.

This was tested with `core_multiplier=2.1`.

For `N=1000000`:

```text
theta   core states   top slab          [131072,262144) reach top
0.34    30530         [262144,524288)   0.006625
0.36    25068         [262144,524288)   0.004249
0.38    17862         [262144,524288)   0.005346
0.40    10264         [262144,524288)   0.003078
```

For theta `0.36`, `N=4300000`:

```text
slab                  states    mean out   zero out   reach next   survive to top
[262144,524288)        15583    2.370      0.077      0.009754     0
[524288,1048576)       38963    3.046      0.034      0.000744     0
[1048576,2097152)     101011    3.977      0.014      0.000782     0.000782
[2097152,4194304)     249469    5.002      0.004      0            1
```

The stricter core improves the local zero-outdegree rate but does not remove
the compatibility obstruction. The crossing image from one slab is still not
landing inside the next slab's forward-surviving subset.

The reciprocal-candidate diagnostic confirms why this is the right simplified
object: for `C=2.1`, once a reciprocal semiprime candidate exists, the
backward and forward filters are effectively automatic in the tested slabs.
The remaining obstruction is compatible survival, not local clearance.

## Status Change

The previous right-core pass made the fixed-buffer route look like a 55%
candidate. The slab-flow pass lowers that estimate.

Current honest status:

```text
exact graph reduction:          strong
right-core local branching:     strong
compatible slab survival:       not demonstrated
fixed H=x^theta route:          45-50%
full EP1212 solution:           45-50%
```

The project is not one ordinary successor-count lemma away. It needs a
genuine directed expansion/min-cut theorem, or a different state space.

## Next Questions

1. Compare the crossing image from slab `k` with the survivor subset in slab
   `k+1`. The present data says they are nearly disjoint at tested scales.
2. Search for an adaptive-buffer state space using actual clearance rather
   than fixed `H=x^theta`.
3. Test non-dyadic frontiers chosen by the graph itself, not by powers of two.
4. If staying with fixed `H`, formulate the theorem as a lower bound on the
   directed min-cut between survivor cores, not as mean outdegree.
