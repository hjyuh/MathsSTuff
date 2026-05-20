# EP-488 v74 A4 Length-17 Frontier

Date: 2026-05-18

Status: rigorous finite normalized-motif A4 progress. This does not solve A4
or EP-488 globally.

## Purpose

v73 closed every normalized pure-cycle motif through length 16 in the current
ratio-graph census. v74 extends the normalized motif census to length 17 and
certifies every new length-17 motif with the v73 jump-period method.

## Enumeration

Command:

```powershell
python .\ep488_v63_a4_normalized_cycle_motifs.py --max-len 17 --json-out ep488_v74_a4_normalized_cycle_motifs_len17.json
```

Result:

```text
motifs = 456
failures = 0
elapsed_seconds = 28.62
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
```

Thus v74 adds:

```text
217 new normalized pure-cycle motifs of length 17.
```

## Certification

The length-17 certificate was run incrementally because the frontier is large:

```powershell
python .\ep488_v74_a4_incremental_jump_certificate.py --motifs-json ep488_v74_a4_normalized_cycle_motifs_len17.json --min-length 17 --max-length 17 --jsonl-out ep488_v74_a4_jump_certificate_len17.clean.jsonl --summary-out ep488_v74_a4_jump_certificate_len17_summary.json --resume
```

Authoritative outputs:

```text
ep488_v74_a4_jump_certificate_len17.clean.jsonl
ep488_v74_a4_jump_certificate_len17_summary.json
```

Result:

```text
selected_motifs = 217
completed = 217
status_counts = {'proved': 217}
elapsed_seconds for final resumed pass = 544.56
```

Coverage check:

```text
source17 = 217
cert17 = 217
missing = 0
extra = 0
all_proved = True
```

## Combined Frontier

Combining the v73 certificates through length 16 with the v74 length-17
certificate gives:

```text
456 normalized pure-cycle motifs through length 17 certified.
```

Combined status:

```text
status_counts = {'proved': 456}
```

Combined length distribution:

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
```

## Extremal Certificate Stats

Largest period handled at length 17:

```text
period = 3732480000
jump_points_checked = 1956816
```

for

```text
{17280,18000,18225,18432,19200,19440,20250,20480,22500,
 23040,24000,24300,25600,25920,30375,30720,33750}.
```

Smallest observed gap between the lower bound `B0` and the period slope:

```text
B0 - slope = 198503/2239488000
```

for

```text
{72900,73728,76800,77760,81000,81920,91125,92160,96000,
 97200,102400,103680,108000,121500,122880,138240,144000}.
```

At length 17, correction-state distribution:

```text
0 states: 171 motifs
1 state:   46 motifs
```

Combined through length 17:

```text
0 states: 321 motifs
1 state:  119 motifs
2 states:  16 motifs
```

No length-17 motif required more than one positive vertex-correction state.

## Caveat

An interrupted earlier checkpoint file

```text
ep488_v74_a4_jump_certificate_len17.jsonl
```

is not authoritative. Use the cleaned checkpoint:

```text
ep488_v74_a4_jump_certificate_len17.clean.jsonl
```

and the summary JSON listed above.

## What This Closes

This closes the finite normalized pure-cycle census through length 17 as
fixed-motif A4 theorems. It is stronger than canonical-realization testing:
each certified motif is proved for every scale and every admissible `q,n,m`
under the reduced top-window pure-cycle hypotheses.

It still does not close A4 globally, because the normalized ratio graph has
not been proved finite and previous census data shows new motifs continue to
appear as length increases.

## Closure State

```text
A2: not closed
A4: all normalized pure-cycle motifs through length 17 closed by fixed-motif
    certificates; global pure-cycle theorem still open
EP-488: not solved
```
