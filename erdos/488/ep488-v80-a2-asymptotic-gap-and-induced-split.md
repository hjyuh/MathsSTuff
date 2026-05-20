# EP-488 v80 A2 Asymptotic Gap And Induced Split

Status: A2 structural progress and negative information. This does not solve
A2, A4, or EP-488.

## Purpose

v79 proved the four-ratio / 5-smooth normalization reduction and generated a
large smooth full-component frontier. v80 tests the next natural candidate:

```text
delta(C,q) < D_C(n;q)/n.
```

Since `B = 2D_C(n;q)/n`, this is equivalent to:

```text
delta/B < 1/2.
```

This would prove that the asymptotic density of a high-defect component is
already below half of the EP bound. It does not by itself prove A2, but it
would make the remaining task a bounded finite-window problem.

## New Audit Scripts

Asymptotic gap audit:

```text
ep488_v80_a2_asymptotic_gap_audit.py
```

Induced subset audit:

```text
ep488_v80_a2_induced_subset_audit.py
```

## Full-Component / Representative Audit

Command:

```powershell
python .\ep488_v80_a2_asymptotic_gap_audit.py `
  --exact-json ep488_v78_a2_full_component_exact_q1500.json `
  --exact-json ep488_v79_a2_exact_check_1501_1535.json `
  --exact-json ep488_v79_a2_exact_check_q2251.json `
  --exact-json ep488_v79_a2_exact_check_q3751.json `
  --representatives-json ep488_v79_a2_smooth_motif_representative_certs_q10000.json `
  --json-out ep488_v80_a2_asymptotic_gap_audit.json
```

Result:

```text
rows audited = 30762
bad delta/B >= 1/2 rows = 0
```

Worst full-component / representative row:

```text
source = ep488_v78_a2_full_component_exact_q1500.json
q = 479
n = 1436
size = 14
epsilon = 2
delta/B = 50365187/100877400
2delta/B = 50365187/50438700 < 1
best/B = 14719/28431
```

Largest observed finite-window cutoff:

```text
source = ep488_v79_a2_smooth_motif_representative_certs_q10000.json
q = 5001
n = 15000
size = 26
epsilon = 2
cutoff/n = 12163/5000 = 2.4326
```

So the tested full-component branch supports:

```text
full-component high-defect asymptotic half-gap:
    delta(C,q) < D_C(n;q)/n.
```

## Unconditional Gap Is False

The same audit records a simple top-window singleton counterexample:

```text
q = 101
C = {100}
n = 253
D_C(n) = 2
delta = 1/101
D_C(n)/n = 2/253
delta / (D_C(n)/n) = 253/202 > 1
```

Thus the asymptotic half-gap is not a generic top-window fact. It needs
high-defect connected/full-component hypotheses or a more specific structural
replacement.

## Known Induced Rows Break The Half-Gap

When the known induced ledger rows from v76 are added:

```powershell
python .\ep488_v80_a2_asymptotic_gap_audit.py `
  --exact-json ep488_v76_a2_known_high_defect_motifs.json `
  --exact-json ep488_v78_a2_full_component_exact_q1500.json `
  --exact-json ep488_v79_a2_exact_check_1501_1535.json `
  --exact-json ep488_v79_a2_exact_check_q2251.json `
  --exact-json ep488_v79_a2_exact_check_q3751.json `
  --representatives-json ep488_v79_a2_smooth_motif_representative_certs_q10000.json `
  --json-out ep488_v80_a2_asymptotic_gap_audit_with_known_induced.json
```

the result is:

```text
rows audited = 30930
bad delta/B >= 1/2 rows = 4
```

All bad rows are the repeated v56 induced theta core:

```text
q = 71440
n = 213189
size = 13
epsilon = 2
delta/B = 7105518307/14178553920
2delta/B = 7105518307/7089276960 > 1
```

So the clean half-gap is false for the currently known induced high-defect
branch. The v56 core is still finite-certified harmless, but it cannot be
handled by the full-component half-gap theorem.

## Induced Subset Audit

The induced subset audit enumerates connected induced high-defect subsets inside
selected full components and finite-certifies every one found.

Command:

```powershell
python .\ep488_v80_a2_induced_subset_audit.py --max-cutoff 10000000 --json-out ep488_v80_a2_induced_subset_audit.json
```

### q479 size-14 full component

Full component:

```text
q = 479
n = 1436
|C| = 14
```

Result:

```text
high-defect induced subsets = 2
status_counts = {'certified': 2}
delta/B >= 1/2 subsets = 1
```

Worst induced subset:

```text
C = {240,243,256,270,288,300,320,324,360,384,405,432,450}
size = 13
epsilon = 2
D_C(n) = 37
delta/B = 1201214/2392605 > 1/2
best/B = 4667/8991
cutoff = 3039
```

This is the theta13 core, now seen directly as an induced sparse core inside the
q479 full component.

### q1921 size-17 representative

Result:

```text
high-defect induced subsets = 16
status_counts = {'certified': 16}
delta/B >= 1/2 subsets = 0
```

Worst finite-window ratio:

```text
size = 11
epsilon = 2
D_C(n) = 32
delta/B = 940/1921
best/B = 55/108
cutoff = 10926
```

### q1535 size-20 exact new motif

Result:

```text
high-defect induced subsets = 64
status_counts = {'certified': 64}
delta/B >= 1/2 subsets = 0
```

Worst finite-window ratio:

```text
size = 13
epsilon = 2
D_C(n) = 38
delta/B = 364867/736800
best/B = 14963/29184
cutoff = 9360
```

## Interpretation

v80 gives a better A2 split.

The full-component branch appears to satisfy a strong asymptotic half-gap:

```text
delta(C,q) < D_C(n;q)/n.
```

This is supported by:

```text
30762 full-component / representative rows,
0 violations,
q10000 smooth representatives,
and exact unrestricted checks beyond q1500.
```

But arbitrary induced high-defect components cannot be handled by that theorem
alone. The v56/theta13 sparse core violates the half-gap while remaining
finite-certified. Therefore A2 needs two sub-branches:

```text
A2-Full:
  prove the asymptotic half-gap and bounded finite-window theorem for full
  connected 5-smooth four-ratio components.

A2-Induced:
  prove that induced high-defect sparse cores are generated by certified
  theta-like deletions, safe isolated extensions, or another finite-core
  mechanism.
```

This is narrower and more accurate than the v79 missing lemma.

## Updated Missing Lemmas

### Missing Lemma A2-Full

For every reduced top-window full connected component with
`epsilon_n(C,q) >= 2`, after gcd-normalization to the 5-smooth four-ratio
graph:

```text
delta(C,q) < D_C(n;q)/n
```

and the finite-certificate cutoff satisfies a uniform event-window bound, such
as:

```text
cutoff <= K n
```

for an absolute constant `K` small enough to allow a finite event-point proof.

### Missing Lemma A2-Induced

Every connected induced high-defect component either:

```text
1. inherits the full-component A2-Full certificate,
2. is a theta-like sparse core with a direct finite-core certificate,
3. is obtained from such a core by safe isolated extensions, or
4. belongs to another explicitly classified certified sparse-core family.
```

The failure point is now exact: the asymptotic half-gap is false for induced
theta cores, so induced A2 cannot simply reuse the full-component proof.

## Closure State

```text
A2: not closed.
    Full-component branch has a strong new theorem candidate.
    Induced branch is separated and has certified sparse-core evidence, but no
    classification theorem.

A4: not closed.
    Pure-cycle motifs through length 18 remain certified, but no all-length
    theorem yet.

EP-488: not solved.
```
