# EP-488 v83 A2 Two-Vertex Extension Audit

Status: A2 induced-branch evidence. This does not solve A2, A4, or EP-488.

## Purpose

v82 certified all one-vertex extensions of the v81 q10000 minimal high-defect
cores. v83 tests the next possible failure mode: two optional vertices added
simultaneously. This checks for pair interactions that a one-step audit might
miss.

This is an audit, not a proof.

## New Script

```text
ep488_v83_a2_k_vertex_extension_audit.py
```

Command:

```powershell
python .\ep488_v83_a2_k_vertex_extension_audit.py `
  --add-count 2 `
  --max-cutoff 10000000 `
  --json-out ep488_v83_a2_two_vertex_extension_audit.json
```

The script uses:

```text
source = ep488_v81_a2_minimal_core_audit_q10000_representatives.json
```

For each v81 minimal core `C0` inside its q10000 representative full component
`Cfull`, and each two-element set `A subset Cfull \ C0`, it certifies
`C0 union A` using the v55 finite-certificate theorem.

## Result

```text
raw two-vertex extensions before dedupe = 10949
unique two-vertex extensions = 10933
status counts = certified: 10933
elapsed seconds = 505.80
```

Defect distribution:

```text
epsilon 2: 10842
epsilon 3:    91
epsilon >= 4:  0
```

Connectivity distribution of `C0 union A`:

```text
1 component: 1817
2 components: 5491
3 components: 3625
```

Attachment counts:

```text
extensions with at least one added-core edge: 6439
extensions with any added-core or added-added edge: 7308
```

Every tested two-vertex extension of every v81 q10000 minimal core is EP-safe
by the finite-certificate method.

## Worst Overall Two-Vertex Extension

The worst overall row is disconnected from the core at height `n`, so it is
less relevant to connected A2-Induced, but it is still certified:

```text
case = v79_motif_110_size29_q8101
q = 8101
n = 24300
full component size = 29
core size = 11
added vertices = {5000,6561}
added-core edge count = 0
added-internal edge count = 0
extension component count = 3
extended size = 13
epsilon = 2
D_C(n;q) = 39
best/B = 560/1053
delta/B = 3517013/6740032
cutoff = 53422
C =
  {4096,4320,4608,4860,5000,5120,5400,5760,6144,6480,
   6561,7680,8100}
```

## Worst Connected Two-Vertex Extension

The worst connected row is:

```text
case = v79_motif_106_size29_q7501
q = 7501
n = 22500
full component size = 29
core size = 11
added vertices = {5400,6400}
added-core edge count = 4
added-internal edge count = 0
extension component count = 1
extended size = 13
epsilon = 2
D_C(n;q) = 36
best/B = 14375/27216
delta/B = 59171875/116655552
cutoff = 46929
C =
  {3840,3888,4320,4374,4800,4860,5400,5760,5832,6400,
   6480,7200,7290}
```

The worst connected asymptotic row is:

```text
case = v79_motif_106_size29_q7501
q = 7501
n = 22500
full component size = 29
core size = 11
added vertices = {4096,5120}
added-core edge count = 1
added-internal edge count = 1
extension component count = 1
extended size = 13
epsilon = 2
D_C(n;q) = 38
best/B = 34375/65664
delta/B = 6640625/12961728
cutoff = 42494
C =
  {3840,3888,4096,4320,4374,4800,4860,5120,5760,5832,
   6480,7200,7290}
```

## Epsilon-3 Rows

There are 91 two-vertex extensions with `epsilon = 3`, all certified. The
largest finite-window ratio among them is:

```text
case = v79_motif_110_size29_q8101
q = 8101
n = 24300
core size = 16
added vertices = {5000,6480}
extension component count = 2
D_C(n;q) = 51
best/B = 700/1377
delta/B = 4334013/8813888
```

These rows strengthen the warning from v82: an extension theorem must allow
the defect to increase from 2 to 3 while preserving EP-safety.

## Next Scale

The next raw extension counts from the same v81 source are:

```text
three-vertex extensions before dedupe = 42482
four-vertex extensions before dedupe = 120259
```

So a k=3 audit is plausible, but it is substantially heavier than v83.

## Interpretation

v83 adds a second extension layer to the A2-Induced evidence:

```text
v81: minimal cores certified
v82: all one-vertex extensions certified
v83: all two-vertex extensions certified
```

This makes an extension-safety theorem more plausible, but it still does not
prove one. The remaining proof need is an analytic or finite-reduction theorem
showing that arbitrary multi-vertex optional attachments cannot push the
finite-window ratio past the EP bound.

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```

