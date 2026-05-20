# GPT Response: Global Composition Audit

GPT's verdict matched the local v91 audit:

```text
No: the stated v90 result does not fully solve original F_Q for primitive Q
and all m > n >= max(Q), unless there is an additional rigorous reduction
from arbitrary n >= q to n < 3q.
```

It treats v90 as closing the fixed-q top-window upper-strip theorem:

```text
C subset (q/2,q), 5q/2 <= n < 3q, m > n
  => D_C(m)/m <= 2D_C(n)/n.
```

But it says the retrieved chain still leaves the global reduction

```text
arbitrary primitive Q, n >= max(Q)
  => top-window instance with n < 3q
```

conditional rather than rigorous.

The exact missing lemma it identified is:

```text
extremizer_implies_bad_block.
```

In BBDS form:

```text
If (C,q,n,m) is a run-end/minimal extremal counterexample,
h = floor(n/q) >= 3, and

  D_C(m)/m > 2D_C(n)/n,

then

  BadBlock(C,q,h).
```

GPT's stated failure point:

```text
The solid parts are the block decomposition, slot-mass formula, and
indexing of the last full block. The unproved part is the propagation
inequality: from non-badness of the last block,

  2 BlockCov(h) >= SlotMass(h),

one must derive a global upper bound on later block contribution strong
enough to contradict extremality.
```

GPT also noted that a weaker weighted-defect route would at best prove
existence of some bad block `j <= h`, not necessarily badness at the current
height `h`, and that the old BBDS descent route is known false.

Final GPT status:

```text
v90 solves the upper-strip local component theorem, not original F_Q.

To claim original F_Q solved, one still needs:

Every primitive-Q counterexample with n >= max(Q) reduces to a top-window
component counterexample with n < 3q.
```

