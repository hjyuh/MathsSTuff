# EP-488 v72 A4 Length-13 Period Probe

Date: 2026-05-18

Status: partial A4 progress. This does not solve A4 or EP-488.

## Purpose

After v71 closed all normalized pure-cycle motifs through length 12, the same
correction-aware fixed-motif certificate was tested through length 13 with a
period cap of `4,000,000`.

## Script

```powershell
python .\ep488_v71_a4_vertex_correction_bounds.py --max-length 13 --period-cap 4000000 --json-out ep488_v71_a4_vertex_correction_bounds_len13_cap4m.json
```

## Result

```text
status_counts = {'proved': 32, 'period_too_large': 19}
```

By length:

```text
3:  proved 1
5:  proved 1
6:  proved 2
7:  proved 2
8:  proved 3
9:  proved 3
10: proved 1
11: proved 3
12: proved 12
13: proved 4, period_too_large 19
```

So the v71 method proves:

```text
all motifs through length 12,
4 of 23 motifs of length 13,
32 of 51 motifs through length 13.
```

No slope failure, period failure, or correction-state failure occurred. The
only obstruction at length 13 under this run is computational period size.

## Remaining Length-13 Obstruction

The remaining 19 motifs all have periods larger than `4,000,000`; examples:

```text
{480,486,512,540,576,600,640,648,675,768,810,864,900}
period = 6220800
B0 = 13/480
slope = 10969/622080

{720,729,768,810,864,900,960,972,1152,1215,1280,1296,1350}
period = 9331200
B0 = 19/1080
slope = 107701/9331200

{960,972,1024,1080,1152,1200,1215,1280,1296,1536,1620,1728,1800}
period = 12441600
B0 = 19/1440
slope = 18431/2073600
correction states = 1
```

The largest periods seen in the remaining list are:

```text
15552000
12441600
9331200
7464960
6220800
```

## Interpretation

The v71 certificate shape appears to continue past length 12. The next
engineering target is not a new inequality yet; it is an optimized period
checker for floor envelopes with periods in the `6M` to `16M` range and then
larger length-14/16 periods.

Mathematically, the current candidate A4 theorem is:

```text
For every feasible pure-cycle motif in the ratio graph, the correction-aware
B0 bound exceeds the q-independent period envelope A(k)/k.
```

The data through length 13 has found no contradiction to this theorem.

## Closure State

```text
A2: not closed
A4: pure-cycle motifs through length 12 closed; 32/51 through length 13 closed
    by the current period cap; global pure-cycle theorem still open
EP-488: not solved
```
