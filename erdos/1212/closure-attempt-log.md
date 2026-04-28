# EP1212 Closure Attempt Log

Date: 2026-04-28

Purpose: record the requested chained closure attempt:

```text
planning agents
-> gpt-5.2 xhigh proof attempt
-> gpt-5.4 xhigh critique/repair
-> gpt-5.5 xhigh final closure attempt
```

This log distinguishes proved statements from conjectural reductions.

## Current Target

Prove a right-core live-pair branching theorem:

> There exists an increasing integer-valued function `H(x) -> infinity` and an
> infinite directed ray in the `H`-buffered right-core live-pair graph.

By `buffered-live-pair-bridge.md`, this implies EP1212.

## Attempt Status

Completed. Final verdict: **NOT CLOSED**.

## Planning Agents

The planning phase converged on three points.

1. The exact DAG and buffered right-core reductions are sound, but they are
   sufficient monotone/two-window frameworks, not equivalences with every
   possible EP1212 path.
2. The computational signal must be converted into compatible slab survival or
   a min-cut/expansion theorem. Longest finite rays and mean outdegree do not
   imply an infinite ray.
3. For `H(x)=floor(x^theta)`, `1/3<theta<1/2`, the right-core graph is already
   a rough-semiprime graph. CRT/block forcing does not bypass the analytic
   issue because divisibility by two large primes becomes exact-value forcing.

## Sequential Attempts

### gpt-5.2 xhigh

File:

```text
closure-attempt-gpt52.md
```

Verdict: **NOT CLOSED**.

Contribution: restated the exact DAG and buffered right-core reductions, then
identified the missing theorem as slab survival for rough semiprimes in
power-short intervals with moving two-window avoidance constraints.

### gpt-5.4 xhigh

File:

```text
closure-attempt-gpt54.md
```

Verdict: **NOT CLOSED**.

Contribution: sharpened the right-core power-buffer regime into a
rough-semiprime skeleton and explained why CRT/block constructions are unlikely
to bypass the missing analytic theorem.

### gpt-5.5 xhigh

File:

```text
closure-attempt-gpt55-final.md
```

Verdict: **NOT CLOSED**.

Contribution: added final lemmas:

```text
exact rays force local roughness,
automatic-visibility roughness criterion,
constant-gap obstruction for that automatic route,
power-buffer right-core semiprime rigidity,
CRT exact-value obstruction.
```

It also stated the clean compatible slab-survival theorem that would close
EP1212.

## Final Missing Theorem

The problem would be solved by proving:

> For some increasing `H`, the `H`-buffered right-core live-pair graph has
> compatible slab-to-slab survival, equivalently nonempty finite families
> `C_k` in consecutive dyadic slabs such that every state in `C_k` can reach
> some state in `C_{k+1}`.

For the current strongest route, take `H(x)=floor(x^theta)`,
`1/3<theta<1/2`. The missing analytic package is a uniform slab-survival/min-cut
theorem for right-core rough semiprimes satisfying the moving two-window
avoidance constraints.

## Follow-Up Slab-Flow Test

File:

```text
slab-flow-survival-pass.md
```

The follow-up computation tested the exact compatibility issue rather than
local mean outdegree. It found:

```text
theta=0.36, cap=4300000:

[524288,1048576)    reach next = 0.00227, survive to top = 0
[1048576,2097152)   reach next = 0.00716, survive to top = 0.00716
```

Thus adjacent one-boundary crossings exist, but the earlier crossing image
does not land inside the next slab's own survivor set. This is direct finite
evidence for the min-cut/compatibility obstruction.

The stricter `C`-core suggested by the later 5.5 pass was also added to the
script via `--core-multiplier`. At `C=2.1`, theta `0.36`, and cap `4300000`,
the graph has lower local zero-outdegree but the same compatibility failure:

```text
[524288,1048576)     reach next = 0.000744, survive to top = 0
[1048576,2097152)    reach next = 0.000782, survive to top = 0.000782
```

The later 5.2 pass sharpened the analytic wall into a reciprocal thin-set
problem. This was recorded in:

```text
reciprocal-thin-set-obstruction.md
scripts/reciprocal_candidate_stats.py
```

At `N=1000000`, theta `0.36`, `C=2.1`, the top complete slab has:

```text
tested primes per state:          66.66
first multiples in window:        17.51
reciprocal semiprimes:             2.370
valid core successors:             2.370
valid zero fraction:               0.077
```

So in the strong core, the local problem really is the reciprocal semiprime
problem; backward exclusion and forward clearance no longer cost visibly.

The later 5.4 pass added a threshold formulation and a finite-path theorem,
recorded in:

```text
threshold-transition-and-finite-paths.md
```

For fixed middle coordinate `v`, each child `w` is available to the suffix

```text
{u in U(v) : u > beta_v(w)}.
```

Also, for `H=x^theta`, `1/3<theta<1/2`, a parent interval `[u,v]` kills at
most

```text
sum_{t=u}^v omega_{>H(v)}(t) <= 2(v-u+1)
```

candidate children. Hence a concrete sufficient theorem is to produce more
than `2(v-u+1)` future-good children in the next window.

The same note proves that the exact DAG has arbitrarily long finite paths,
using admissible tuples of `E_2` numbers. This confirms that the obstruction is
infinite survival, not finite local pattern creation.

## Final State

```text
EP1212: not closed.
Best route: right-core rough-semiprime compatible slab survival, now in
threshold form.
Main blocker: adaptive pointwise de-sieved rough-semiprime theorem producing
enough future-good children to beat the threshold killing count.
Current project status: strong reduction + strong local branching evidence,
but compatible slab-flow survival is not demonstrated.
Best current estimate: 45-50%, not 55%.
```
