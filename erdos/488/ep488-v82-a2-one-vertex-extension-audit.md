# EP-488 v82 A2 One-Vertex Extension Audit

Status: A2 induced-branch evidence. This does not solve A2, A4, or EP-488.

## Purpose

v81 left the following A2-Induced blocker:

```text
minimal high-defect core safety
  + optional-extension monotonicity
```

The v60 theorem proves optional-extension monotonicity only for isolated
singleton additions. The q10000 frontier also has non-isolated optional
vertices, so v82 tests the first local non-isolated version: add one vertex
from the containing full component to each v81 deletion-minimal high-defect
core, then finite-certify the enlarged induced set.

This is an audit, not a proof.

## New Script

```text
ep488_v82_a2_one_vertex_extension_audit.py
```

Command:

```powershell
python .\ep488_v82_a2_one_vertex_extension_audit.py `
  --max-cutoff 10000000 `
  --json-out ep488_v82_a2_one_vertex_extension_audit.json
```

The script uses:

```text
source = ep488_v81_a2_minimal_core_audit_q10000_representatives.json
```

For each v81 minimal core `C0` inside its q10000 representative full component
`Cfull`, and each `a in Cfull \ C0`, it certifies `C0 union {a}` using the v55
finite-certificate theorem.

## Result

```text
unique one-vertex extensions = 1852
status counts = certified: 1852
elapsed seconds = 50.21
```

The extensions split as:

```text
added vertex isolated from core at n:      1137
added vertex has an edge to core at n:     715
```

Defect distribution:

```text
epsilon 2: 1844
epsilon 3:    8
```

Thus every tested one-vertex extension of every v81 q10000 minimal core is
EP-safe by the finite-certificate method, including all 715 non-isolated
one-vertex attachments.

## Worst Non-Isolated Extension

The worst non-isolated row is the same for `best/B` and `delta/B`:

```text
case = v79_motif_106_size29_q7501
q = 7501
n = 22500
full component size = 29
core size = 11
added vertex = 6400
added has edge to core = true
extended size = 12
epsilon = 2
D_C(n;q) = 33
best/B = 625/1188
delta/B = 4234375/8225712
cutoff = 43559
C =
  {3840,3888,4320,4374,4800,4860,5760,5832,6400,6480,7200,7290}
```

This is still far below the EP violation threshold `best/B > 1`.

## Worst Overall One-Vertex Extensions

Largest finite-window ratio:

```text
case = v79_motif_110_size29_q8101
q = 8101
n = 24300
full component size = 29
core size = 11
added vertex = 6561
added has edge to core = false
extended size = 12
epsilon = 2
D_C(n;q) = 35
best/B = 100/189
delta/B = 935475/1814624
cutoff = 47290
C =
  {4096,4320,4608,4860,5120,5400,5760,6144,6480,6561,7680,8100}
```

Largest asymptotic ratio:

```text
case = v79_motif_110_size29_q8101
q = 8101
n = 24300
full component size = 29
core size = 11
added vertex = 5000
added has edge to core = false
extended size = 12
epsilon = 2
D_C(n;q) = 36
best/B = 135/256
delta/B = 1071171/2073856
cutoff = 51655
C =
  {4096,4320,4608,4860,5000,5120,5400,5760,6144,6480,7680,8100}
```

## Epsilon-3 Extensions

Eight one-vertex extensions raise `epsilon` from 2 to 3. All are certified.

```text
q = 4501, n = 13500, core size = 15, added = 3600,
  D_C(n;q) = 46, best/B = 6750/13501, delta/B = 399375/828184

q = 9001, n = 27000, core size = 15, added = 7200,
  D_C(n;q) = 46, best/B = 13500/27001, delta/B = 399375/828092

q = 4321, n = 12960, core size = 17, added = 3240,
  D_C(n;q) = 51, best/B = 2080/4131, delta/B = 1200/2533

q = 7501, n = 22500, core size = 16, added = 5760,
  D_C(n;q) = 47, best/B = 24375/48128,
  delta/B = 18671875/38075076

q = 7501, n = 22500, core size = 20, added = 5760,
  D_C(n;q) = 60, best/B = 11250/22501,
  delta/B = 8243125/17282304

q = 8101, n = 24300, core size = 16, added = 6480,
  D_C(n;q) = 47, best/B = 6075/12032,
  delta/B = 5902875/12183904

q = 7201, n = 21600, core size = 17, added = 6480,
  D_C(n;q) = 52, best/B = 530/1053, delta/B = 44700/93613

q = 8641, n = 25920, core size = 17, added = 6480,
  D_C(n;q) = 51, best/B = 2080/4131, delta/B = 69600/146897
```

These rows are useful regressions for any claimed extension theorem: the
theorem must allow a one-vertex attachment to increase the high-defect value.

## Interpretation

v82 strengthens the v81 induced-core picture:

```text
certified minimal cores
  + all one-vertex extensions inside the q10000 smooth frontier certified
  + non-isolated one-vertex attachments certified
```

The audit gives evidence for a local extension theorem, but it does not prove
the theorem. It also does not cover multi-vertex extension interactions except
one step at a time as tested rows.

## Updated Missing Lemma

The next A2-Induced theorem target can now be sharpened:

```text
Let C0 be a connected deletion-minimal high-defect reduced top-window core
from the normalized four-ratio/5-smooth family. Let a be a top-window vertex
such that C0 union {a} is primitive and connected in B_n, and preserves the
reduced hypotheses. Then

  D_{C0 union {a}}(m;q)/m <= 2D_{C0 union {a}}(n;q)/n

for every m > n.
```

A stronger useful form would make this iterative:

```text
If C0 is safe and every one-vertex top-window extension satisfying the local
four-ratio attachment constraints is safe with slack monotone under further
attachments, then every finite extension of C0 is safe.
```

Failure point: v82 verifies this over the q10000 representative frontier, but
does not provide the analytic inequality or a finite reduction proving all
possible one-vertex attachments.

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```

This moves the A2-Induced branch forward, but it is still evidence toward the
extension theorem, not the theorem itself.

