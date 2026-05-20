# EP-488 v81 A2 Induced Minimal-Core Frontier

Status: A2 induced-branch structural and computational progress. This is a
failed full-solution attempt: it does not solve A2, A4, or EP-488.

## Purpose

v80 split the A2 high-defect branch into two different problems:

```text
A2-Full:    full top-window components appear to satisfy delta < D_C(n;q)/n.
A2-Induced: sparse induced high-defect cores can violate that half-gap while
            still remaining far below the EP bound.
```

The v81 audit targets `A2-Induced`. Exhaustive induced-subset enumeration is
not feasible for the larger q10000 smooth motifs, so the audit searches for
deletion-minimal connected high-defect cores by generating unions of cycles
and shortest connecting paths.

This is a generator/audit, not a completeness proof.

## New Scripts And Data

Main audit:

```text
ep488_v81_a2_minimal_core_audit.py
```

Summary data:

```text
ep488_v81_a2_minimal_core_summary_q10000.json
```

Full q10000 representative audit:

```text
ep488_v81_a2_minimal_core_audit_q10000_representatives.json
```

The script:

```text
1. enumerates simple cycles in B_n(C,q),
2. unions up to max_cycles cycles,
3. connects disconnected cycle unions by shortest paths,
4. keeps connected induced subsets with epsilon >= 2,
5. filters to deletion-minimal high-defect cores,
6. applies the v55 finite certificate to each discovered core.
```

## Calibration

Command:

```powershell
python .\ep488_v81_a2_minimal_core_audit.py `
  --max-cycles 4 `
  --path-limit 20 `
  --max-cutoff 10000000 `
  --json-out ep488_v81_a2_minimal_core_audit_calibration.json
```

The audit recovered exactly one deletion-minimal core in each of the three
v80 brute-force induced-subset cases:

```text
q479_size14_full_component:
  core size = 13
  epsilon = 2
  best/B = 4667/8991
  delta/B = 1201214/2392605

q1921_size17_smooth_representative:
  core size = 11
  epsilon = 2
  best/B = 55/108
  delta/B = 940/1921

q1535_size20_exact_new_motif:
  core size = 13
  epsilon = 2
  best/B = 14963/29184
  delta/B = 364867/736800
```

All three recovered minimal cores were finite-certified.

## q10000 Representative Audit

Command:

```powershell
python .\ep488_v81_a2_minimal_core_audit.py `
  --cases-json ep488_v81_a2_minimal_core_cases_q10000_representatives.json `
  --max-cycles 4 `
  --path-limit 20 `
  --max-cutoff 10000000 `
  --json-out ep488_v81_a2_minimal_core_audit_q10000_representatives.json
```

Result:

```text
representative cases = 120
minimal cores found = 158
status counts = certified: 158
epsilon counts = epsilon 2: 158
unique normalized minimal-core shapes = 29
elapsed seconds = 141.63137435913086
```

Core counts per representative:

```text
1 core: 110 cases
3 cores: 3 cases
4 cores: 1 case
5 cores: 3 cases
6 cores: 2 cases
8 cores: 1 case
```

Core size counts:

```text
size 11: 33
size 13: 47
size 14: 29
size 15: 25
size 16: 7
size 17: 10
size 18: 5
size 19: 1
size 20: 1
```

Unique normalized core sizes:

```text
size 11: 4
size 13: 3
size 14: 3
size 15: 5
size 16: 5
size 17: 6
size 18: 1
size 19: 1
size 20: 1
```

## Worst Certified Minimal Cores

Largest finite-window ratio:

```text
case = v79_motif_017_size21_q1251
q = 1251
n = 3750
full component size = 21
core size = 11
epsilon = 2
D_C(n;q) = 31
best/B = 3125/5952
delta/B = 472625/930744
cutoff/n = 7127/3750
C =
  {640,648,720,729,800,810,960,972,1080,1200,1215}
```

Largest asymptotic ratio:

```text
case = v79_motif_106_size29_q7501
q = 7501
n = 22500
full component size = 29
core size = 11
epsilon = 2
D_C(n;q) = 31
best/B = 3125/5952
delta/B = 3203125/6278337
cutoff/n = 3581/1875
C =
  {3840,3888,4320,4374,4800,4860,5760,5832,6480,7200,7290}
```

Largest finite-certificate window:

```text
case = v79_motif_106_size29_q7501
q = 7501
n = 22500
full component size = 29
core size = 19
epsilon = 2
D_C(n;q) = 56
best/B = 225/448
delta/B = 38965625/80650752
cutoff/n = 7903/3750
C =
  {3840,3888,4000,4050,4096,4320,4500,4608,5000,5120,
   5184,5400,5760,6000,6144,6480,6750,6912,7500}
```

## Most Repeated Normalized Cores

The most frequent normalized core is the theta13 core:

```text
C =
  {240,243,256,270,288,300,320,324,360,384,405,432,450}
occurrences = 35
max best/B = 8125/15984
max delta/B = 546875/1110148
```

The next repeated shapes are:

```text
size 14, occurrences 25:
  {1152,1200,1215,1280,1296,1350,1440,1600,1620,1728,
   1800,1920,2025,2160}
  max best/B = 560/1107
  max delta/B = 406250/830373

size 15, occurrences 13:
  {2048,2160,2187,2304,2430,2560,2592,2880,2916,3072,
   3240,3456,3645,3840,3888}
  max best/B = 23500/45927
  max delta/B = 334375/680484

size 11, occurrences 12:
  {243,256,270,288,320,324,360,384,405,432,480}
  max best/B = 55/108
  max delta/B = 4700/9601

size 11, occurrences 11:
  {640,648,720,729,800,810,960,972,1080,1200,1215}
  max best/B = 3125/5952
  max delta/B = 3203125/6278337
```

## Regression Checks

theta13:

```text
q = 451
n = 1350
C = {240,243,256,270,288,300,320,324,360,384,405,432,450}
cyclomatic = 2
tau = 0
epsilon = 2
D_C(n;q) = 37
B = 37/675
delta = 35/1353
delta/B = 7875/16687
cutoff = 2694
best = 37/1351 at m = 1351
best/B = 675/1351
status = certified
```

Kimi obstruction:

```text
q = 427
n = 1280
C = {216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405}
cyclomatic = 4
tau = 2
epsilon = 2
D_C(n;q) = 47
B = 47/640
delta = 783343/23058000
delta/B = 6266744/13546575
cutoff = 2685
best = 1/27 at m = 1296
best/B = 640/1269
status = certified
```

v56 strongest known high-defect near-miss:

```text
q = 71440
n = 213189
C =
  {35760,36207,36269,38144,38296,40230,42912,43640,44700,
   46678,47680,48276,53640,57216,60345,63116,64368,67050,68055}
cyclomatic = 2
tau = 0
epsilon = 2
D_C(n;q) = 61
B = 122/213189
delta =
  247527163896052833247853914829/
  818631113780204727506401615314480
delta/B =
  17590022847945202489092242749493227/
  33290998627061658918593665689455520
cutoff = 7165749
best = 1033/3411504 at m = 3411504
best/B = 73408079/138734496
status = certified
```

These checks preserve the v55/v56 claim that the named regressions are
harmless for the EP bound, while still invalidating the forbidden structural
shortcuts.

## Interpretation

Within the q10000 smooth frontier, high-defect induced behavior appears to be
controlled by small deletion-minimal cores. Every discovered minimal core has
`epsilon = 2`, even when the containing full component has larger defect.

This suggests the current A2 program should not try to prove that induced
high-defect cores are impossible, and should not rely on `delta/B < 1/2` for
arbitrary induced subsets. The correct target looks like:

```text
minimal high-defect core safety
  + optional-extension monotonicity
  + full-component asymptotic half-gap
```

## Missing Lemma

The precise missing A2-Induced lemma is:

```text
Let C be a connected reduced top-window component or induced connected
subcomponent with epsilon_n(C,q) >= 2. Then C contains a connected
deletion-minimal induced subset C0 with epsilon_n(C0,q) >= 2 such that:

1. C0 is generated by at most four simple cycles together with shortest
   connecting paths in the four-ratio graph;
2. after 5-smooth normalization, C0 belongs to a finite automatically
   certifiable family of minimal cores;
3. every extension C0 subset C obtained by adding top-window vertices that
   preserves primitivity and connectedness remains EP-safe:

      D_C(m;q)/m <= 2D_C(n;q)/n

   for every m > n.
```

Failure point: v81 verifies many instances of (1) and (2), but it does not
prove the cycle/path generator is complete. It also does not prove (3). The
existing v60 extension lemma covers isolated singleton extensions, but the
q10000 frontier needs non-isolated optional-extension monotonicity.

## Closure Status

```text
A2 closed: no
A4 closed: no
EP-488 solved: no
```

This v81 result strictly advances the A2 induced branch by reducing the
observed sparse-core frontier to 29 normalized, certified minimal-core shapes,
but it leaves the two proof obligations above open.

