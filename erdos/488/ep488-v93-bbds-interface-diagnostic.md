# EP-488 v93 BBDS Interface Diagnostic

Status: local exact diagnostics for the remaining global `n < 3q` reduction.

Date: 2026-05-19

## Summary

The v90 reduced top-window theorem still closes A2/A4 inside

```text
5q/2 <= n < 3q.
```

The remaining global blocker is unchanged:

```text
reduce arbitrary top-window run-end counterexamples with n >= 3q
to a contradiction.
```

The old BBDS interface asked for the strong current-height statement:

```text
RunEndExtremal(C,q,n,m), TopWindow(C,q), h=floor(n/q)>=3
  => BadBlock(C,q,h).
```

v92 observed that this is stronger than necessary. Since `AtomicClosed`
forbids every bad block at height at least `3`, it is enough to prove:

```text
RunEndExtremal(C,q,n,m), TopWindow(C,q), 3q <= n
  => exists j >= 3, BadBlock(C,q,j).
```

## GPT Relay

Prompt 005 asked GPT for the strong current-height interface. It stalled and
was stopped; no proof, counterexample, or usable lemma was produced.

The next relay prompt is now:

```text
Prove or disprove the weaker interface:

  no BadBlock(j) for every j>=3
  => D_C(m;q)/m <= 2D_C(n;q)/n

under RunEndExtremal.
```

This is recorded in:

```text
rotation-v88-gpt-relay/prompts/006-weak-some-bad-block-interface.md
```

## Diagnostic Script

The exact search script is:

```text
ep488_v93_bbds_interface_search.py
```

It scans top-window primitive subsets and records the exact ratio

```text
(D_C(m;q)/m) / (2D_C(n;q)/n)
  = D_C(m;q) * n / (2 * D_C(n;q) * m).
```

It now supports:

```text
--connected-only
--run-end-only
```

where `--run-end-only` enforces:

```text
n uncovered,
n+1 covered,
m covered,
m+1 uncovered.
```

It also records bad blocks up to both:

```text
h = floor(n/q)
hm = floor(m/q).
```

## Exact Search Results

All listed searches found zero violations of the EP ratio.

| file | checked | worst ratio | case |
|---|---:|---:|---|
| `v93_bbds_interface_q18.json` | 41,876,718 | `59/84 = 0.702381` | `q=16, C={12}, n=59, m=84` |
| `v93_bbds_interface_q24_s4.json` | 98,706,894 | `89/126 = 0.706349` | `q=24, C={18}, n=89, m=126` |
| `v93_bbds_interface_connected_q28_s5.json` | 19,991,979 | `1349/2160 = 0.624537` | `q=23, C={12,15,20}, n=71, m=108` |
| `v93_bbds_interface_connected_q50_s3.json` | 135,513,775 | `2717/4320 = 0.628935` | `q=47, C={24,30,40}, n=143, m=216` |
| `v93_bbds_interface_runend_q18_all_mbad.json` | 1,726,966 | `59/84 = 0.702381` | `q=16, C={12}, n=59, m=84` |
| `v93_bbds_interface_runend_connected_q28_s5_mbad.json` | 504,716 | `1349/2160 = 0.624537` | `q=23, C={12,15,20}, n=71, m=108` |
| `v93_bbds_interface_runend_connected_q50_s3_mbad.json` | 1,023,785 | `2717/4320 = 0.628935` | `q=47, C={24,30,40}, n=143, m=216` |

For the strongest connected run-end case,

```text
q=47,
C={24,30,40},
n=143,
m=216,
D_C(n;q)=10,
D_C(m;q)=19,
h=3,
BlockCov(h)=2,
SlotMass(h)=4.
```

Thus:

```text
(D_C(m;q)/m) / (2D_C(n;q)/n)
  = 19*143/(2*10*216)
  = 2717/4320
  < 1.
```

There is no bad block up to `floor(m/q)` in this case.

## Interpretation

The diagnostics do not prove the BBDS interface. They also do not refute it.
They show:

1. No finite counterexample was found in the tested ranges.
2. Near-misses with no bad block exist, including exact run-end near-misses.
3. Those near-misses are far below the EP threshold; the best connected
   run-end frontier is only about `62.9%` of the forbidden ratio.
4. Therefore a valid BBDS proof cannot be a naive statement that near-misses
   force bad blocks. It must use the full strict violation

```text
D_C(m;q)/m > 2D_C(n;q)/n.
```

## Remaining Missing Lemma

The current best target is the weak BBDS interface:

```text
theorem extremizer_implies_some_bad_block:
  TopWindow(C,q)
  RunEndExtremal(C,q,n,m)
  3q <= n
  =>
  exists j >= 3, BadBlock(C,q,j).
```

Equivalently, prove the contrapositive:

```text
TopWindow(C,q)
no BadBlock(C,q,j) for every j>=3
RunEnd endpoint conditions
  =>
D_C(m;q)/m <= 2D_C(n;q)/n.
```

The exact failure point remains the summatory inequality converting
non-badness of blocks into an upper bound on later coverage. Existing
proved infrastructure gives:

```text
D_C(kq;q) = sum_{j<=k} BlockCov(j)
BlockCov(j) <= SlotMass(j)
no BadBlock(j) => 2*BlockCov(j) >= SlotMass(j)
```

but this has not yet been turned into the needed global ratio comparison for
arbitrary run-end `n,m`.

## Status

```text
A2 inside reduced top-window: closed by v90.
A4 inside reduced top-window: closed by v90.
Global EP-488: not closed.
Remaining blocker: weak BBDS interface / global n<3q reduction.
Current percent estimate: still about 92-94%.
```

