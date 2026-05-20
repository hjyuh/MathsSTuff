# EP-488 v75 A4 Length-18 Frontier

Date: 2026-05-18

Status: rigorous finite normalized-motif A4 progress. This does not solve A4
or EP-488 globally.

## Purpose

v74 closed every normalized pure-cycle motif through length 17. v75 extends
the normalized motif census through length 18 and certifies every new length-18
motif with the correction-aware jump-period method.

## Enumeration

Command:

```powershell
python .\ep488_v63_a4_normalized_cycle_motifs.py --max-len 18 --json-out ep488_v75_a4_normalized_cycle_motifs_len18.json
```

Result:

```text
motifs = 817
failures = 0
elapsed_seconds = 73.47
```

Length distribution:

```text
3: 1
5: 1
6: 2
7: 2
8: 3
9: 3
10: 1
11: 3
12: 12
13: 23
14: 33
15: 51
16: 104
17: 217
18: 361
```

Thus v75 adds:

```text
361 new normalized pure-cycle motifs of length 18.
```

## Compact Certificate

The original v73/v74 certificate stored the full finite `y` table for the
lower-bound side. For length 18, v75 uses the same proof but stores only:

```text
worst y row,
correction-state summary,
period,
slope,
worst jump row.
```

The underlying proof check is unchanged and rerunnable from:

```text
ep488_v75_a4_compact_jump_certificate.py
```

Because the length-18 frontier is large, it was certified in independent
chunks:

```text
001-045
046-090
091-135
136-180
181-225
226-270
271-315
316-361
```

Authoritative chunk files are the cleaned JSONL files:

```text
ep488_v75_a4_compact_jump_certificate_len18_001_045.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_046_090.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_091_135.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_136_180.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_181_225.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_226_270.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_271_315.clean.jsonl
ep488_v75_a4_compact_jump_certificate_len18_316_361.clean.jsonl
```

Combined compact summary:

```text
ep488_v75_a4_compact_jump_certificate_len18_combined_summary.json
```

Some interrupted non-clean JSONL files exist and should not be treated as
authoritative.

## Certification Result

Coverage check:

```text
source18 = 361
cert18 = 361
missing = 0
extra = 0
all_proved = True
```

Length-18 status:

```text
status_counts = {'proved': 361}
```

Combined through length 18:

```text
status_counts = {'proved': 817}
```

So all normalized pure-cycle motifs in

```text
ep488_v75_a4_normalized_cycle_motifs_len18.json
```

are certified by fixed-motif A4 theorems.

## Extremal Stats

Largest length-18 period handled:

```text
period = 14929920000
jump_points_checked = 2079696
```

for

```text
{69120,72000,72900,73728,76800,77760,81000,81920,90000,
 91125,92160,96000,97200,102400,103680,121500,122880,135000}.
```

Smallest observed length-18 gap between the lower bound `B0` and the period
slope:

```text
B0 - slope = 821257/26873856000
```

for

```text
{218700,221184,230400,233280,243000,245760,273375,276480,
 288000,291600,307200,311040,324000,364500,368640,409600,
 414720,432000}.
```

Length-18 correction-state distribution:

```text
0 states: 306 motifs
1 state:   55 motifs
```

Combined through length 18:

```text
0 states: 627 motifs
1 state:  174 motifs
2 states:  16 motifs
```

No length-18 motif required more than one positive vertex-correction state.

## Interpretation

The correction-aware jump-period certificate continues to scale. The frontier
has moved from length 17 to length 18 without any slope failure, jump failure,
or correction-state obstruction.

The remaining A4 problem is still global: prove that this certificate works
for every feasible pure cycle in the infinite four-ratio graph, or prove a
finite reduction of that graph.

## Verification

The compact checker compiles:

```powershell
python -m py_compile .\ep488_v75_a4_compact_jump_certificate.py
```

## Closure State

```text
A2: not closed
A4: all normalized pure-cycle motifs through length 18 closed by fixed-motif
    certificates; global pure-cycle theorem still open
EP-488: not solved
```
