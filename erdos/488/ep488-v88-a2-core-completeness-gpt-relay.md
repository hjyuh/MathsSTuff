# EP-488 v88 A2 Core-Completeness GPT Relay

Status: failed full-solution attempt. This does not close A2, A4, or EP-488.

## Relay Artifacts

Prompt:

```text
rotation-v88-gpt-relay/prompts/001-finite-epsilon2-shape.md
```

GPT response:

```text
rotation-v88-gpt-relay/responses/001-finite-epsilon2-shape-gpt.md
```

Local audits:

```text
ep488_v88_normalized_epsilon2_shape_search.py
ep488_v88_skeleton_identity_audit.py
rotation-v88-gpt-relay/evals/v88_shape_search_box5_len8.json
rotation-v88-gpt-relay/evals/v88_smooth_frontier_q10001_15000.json
rotation-v88-gpt-relay/evals/v88_largest_frontier_sample_minimal_cores_quick.json
rotation-v88-gpt-relay/evals/v88_skeleton_identity_audit.json
rotation-v88-gpt-relay/evals/v88_block_decomposition_audit.json
rotation-v88-gpt-relay/evals/v88_all46_frontier_minimal_cores_quick.json
rotation-v88-gpt-relay/evals/v88_block_decomposition_audit_all46.json
```

## GPT Claim

GPT did not prove the finite epsilon-2 shape lemma. It proposed a weaker
``two-unit skeleton theorem``.

For a connected epsilon-2 core, define for every vertex `v`:

```text
d_v = degree(v)
c_v = number of connected components of H-v
t_v = number of triple triangles containing v
kappa = sum_v (c_v - 1)
sigma_v = d_v - c_v - t_v - 1
```

The algebraic identity is:

```text
tau + kappa + sum_v sigma_v = 2.
```

GPT then claimed `sigma_v >= 0`, hence finitely many skeleton vertices after
suppressing ordinary degree-2 chains.

## Local Audit Result

The identity is correct algebraically, but the nonnegativity claim is not valid
for the current v81 notion of deletion-minimality.

The reason is definitional. v81 deletion-minimality filtered out connected
subdeletions with epsilon >= 2. GPT's proof requires the stronger condition:

```text
epsilon(H-v) <= 1
```

using total cyclomatic number even when `H-v` is disconnected.

On the audited set of 158 v81 q<=10000 cores plus 31 new v88 sample cores:

```text
identity failures: 0
negative-sigma cores: 49
nonordinary-bound failures: 32
max nonordinary vertices observed: 10
```

So the corrected statement is:

```text
For any connected epsilon-2 core:
  tau + kappa + sum_v sigma_v = 2.

If, in addition, every vertex deletion has total epsilon <= 1:
  sigma_v >= 0 for every v,
  and the finite skeleton bound follows.
```

This stronger hypothesis does not cover all existing v81 cores.

## New Frontier Check

I extended the normalized smooth frontier beyond the existing q<=10000 audit:

```text
q range: 10001..15000
smooth high-defect event rows: 12199
unique normalized full motifs: 46
largest full motif size: 33
```

The largest eight size-33 representatives were then passed through a quick
minimal-core audit with `max_cycles=2`, `path_limit=10`.

Result:

```text
sample cases: 8
minimal cores found: 31
all certified: yes
all epsilon: 2
unique sampled core shapes: 22
already in old q<=10000 shape set: 15
new sampled core shapes: 7
```

After this, all 46 q=10001..15000 normalized representatives were passed
through the same quick minimal-core audit:

```text
sample cases: 46
minimal cores found: 99
all certified: yes
all epsilon: 2
unique sampled core shapes: 31
already in old q<=10000 shape set: 20
new sampled core shapes: 11
```

Two new certified examples from `q=10936, n=32400`:

```text
C =
{5760,5832,6000,6075,6144,6400,6480,6750,6912,7680,
 7776,8000,8100,8640,9000,9216,9600,9720,10125,10368}

cyclomatic = 2
tau = 0
epsilon = 2
D_C(n;q) = 59
best/B = 16200/32401
delta/B = 1806775/3871344
```

and

```text
C =
{5760,5832,6000,6075,6144,6400,6480,6750,6912,7200,
 7680,7776,8000,8100,9000,9216,9600,9720,10125,10368,10800}

cyclomatic = 4
tau = 2
epsilon = 2
D_C(n;q) = 62
best/B = 16200/32401
delta/B = 1872343/4068192
```

This means the observed `29 normalized shapes` from q<=10000 are not globally
complete. They were a frontier artifact, not a finite classification.

## Over-Broad Four-Ratio Graph Check

A pure four-ratio graph search in a small exponent slab found 24 graph-only
epsilon-2 cores, but none passed the actual top-window lcm-cutoff realization
test.

This confirms that the real classification cannot be stated purely in the
unweighted four-ratio graph. It must include the lcm cutoff/window data.

## Updated Failure Point

The remaining A2-Induced core-completeness problem is now sharper:

```text
Classify or certify all connected-deletion-minimal epsilon-2 cores in the
top-window lcm-threshold four-ratio model, allowing articulation vertices
where total-deletion sigma can be negative.
```

Equivalently, one needs a block-tree version of the skeleton theorem where
negative sigma at articulation/triple vertices is controlled by positive
surplus elsewhere, or a replacement-minimality theorem that turns connected
minimal cores into total-deletion-minimal blocks.

## Block Decomposition Audit

I also decomposed the old cores plus new sample cores into biconnected blocks
and recorded the positive block-epsilon partition.

Original 8-case sample result:

```text
cores audited: 189
positive epsilon partition [2]:   135 cores
positive epsilon partition [1,1]:  54 cores
max block count: 9
nontrivial block-tree cores: 54
```

Full 46-representative quick-audit result:

```text
cores audited: 257
positive epsilon partition [2]:   177 cores
positive epsilon partition [1,1]:  80 cores
max block count: 9
nontrivial block-tree cores: 80
```

So every audited connected-minimal epsilon-2 core is either:

```text
one positive epsilon-2 block,
```

or

```text
two positive epsilon-1 blocks connected through a block tree.
```

This exactly explains the negative-sigma failures: they are not failures of
the algebraic identity; they are articulation cases where high defect is split
across two cyclic blocks.

This suggests the next serious theorem should not be a single skeleton theorem
for all connected-minimal cores. It should be a block-tree theorem:

```text
Connected-minimal epsilon-2 cores decompose into either
  (i) one total-minimal epsilon-2 block, or
  (ii) two epsilon-1 blocks connected by an admissible top-window bridge.

Then prove EP-safety for (i) by finite/certified epsilon-2 block templates and
for (ii) by A4/unicyclic host-margin plus bridge control.
```

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```

v88 does advance the ledger by:

1. rejecting the unqualified GPT skeleton theorem;
2. showing the q<=10000 set of 29 minimal-core shapes is not complete;
3. identifying the precise next lemma: a block-tree/negative-sigma control
   theorem for connected-minimal epsilon-2 cores.
