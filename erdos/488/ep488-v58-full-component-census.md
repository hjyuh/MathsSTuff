# EP-488 v58 Full-Component High-Defect Census

Date: 2026-05-18

Status: partial progress, not a proof and not a counterexample.

## Purpose

This pass strengthens the prior Kimi full-top-window census by attaching exact
finite-certificate checks to every feasible high-defect component it finds.

Script:

```powershell
python .\ep488_v58_full_component_census.py --q-max 500 --json-out ep488_v58_full_component_census_q500.json
```

Output file:

```text
ep488_v58_full_component_census_q500.json
```

## Scope

The census analyzes connected components of the full top-window graph on

```text
{floor(q/2)+1, ..., q-1}
```

with `n in [5q/2, 3q)`. It is exact in `n` through `q <= 100`, and uses sampled
`n` values for `q > 100`, matching the Kimi search style.

This is not an induced-subset census and is not a proof of Uniform High-Defect
Safety.

## Results

For `q <= 150`, the census checked `11547` full components and found no
high-defect component.

For `q <= 500`, sampled as above:

```text
components checked = 106829
high-defect components = 162
certificate status = {'certified': 162}
unique C-families = 3
epsilon values = {2: 162}
q range among high-defect rows = 427..485
n range among high-defect rows = 1280..1454
```

No high-defect full-component row had nonpositive finite-certificate margin
`eta = B - delta`. No row had a finite-window EP violation.

## Strongest Sampled Full-Component Near-Miss

```text
q = 479
n = 1436
C = {240,243,256,270,288,300,320,324,360,384,400,405,432,450}
|C| = 14
epsilon = 2
D_C(n) = 39
B = 39/718
delta/B = 50365187/100877400
eta/B = 50512213/100877400
cutoff = 3161
best = 41/1458 at m = 1458
best/B = 14719/28431
failures = 0
```

This is below the v56 induced/engineered near-miss
`73408079/138734496 ~= 0.529126`, but it is the strongest sampled
full-component row found through `q <= 500`.

## Three Families Found

### Family 1: Kimi-type obstruction

```text
count = 9
|C| = 16
q range = 427..431
n range = 1280..1292
C = {216,225,240,243,250,256,270,288,300,320,324,360,375,384,400,405}
best row: q=431, n=1292
D_C(n)=47
delta/B = 153237337/328163400
cutoff = 2733
best = 1/27 at m=1296
best/B = 646/1269
```

The original Kimi obstruction `q=427,n=1280` is recovered and certified:

```text
D_C(n)=47
best/B = 640/1269
failures = 0
```

### Family 2: theta-plus-400 full-component family

```text
count = 145
|C| = 14
q range = 451..479
n range = 1350..1436
C = {240,243,256,270,288,300,320,324,360,384,400,405,432,450}
best row: q=479, n=1436
D_C(n)=39
delta/B = 50365187/100877400
cutoff = 3161
best = 41/1458 at m=1458
best/B = 14719/28431
```

At `q=451,n=1350`, the full component with `400` added is also certified:

```text
D_C(n)=39
B = 13/225
delta = 587/21648
delta/B = 44025/93808
cutoff = 2804
best = 39/1351 at m=1351
best/B = 675/1351
failures = 0
```

### Family 3: shifted theta-plus-480 family

```text
count = 8
|C| = 14
q range = 481..485
n range = 1441..1454
C = {243,256,270,288,300,320,324,360,384,400,405,432,450,480}
best row: q=485, n=1454
D_C(n)=39
delta/B = 118420303/245138400
cutoff = 3101
best = 20/729 at m=1458
best/B = 14540/28431
```

## Interpretation

This strengthens the evidence that high-defect full top-window components are
not extremizers. In this sampled full-component regime, every high-defect row
has a positive finite-certificate margin and a best event ratio below the EP
bound.

It does not close A2 because:

- it is a full-component census, not an arbitrary induced-subset census;
- it samples `n` for `q > 100`;
- the v56 near-miss already shows that induced/engineered high-defect cases can
  have substantially weaker density-gap behavior than the full-component rows.

## Refined Missing A2 Lemma

The missing A2 theorem can now be split more sharply:

1. Prove that full top-window high-defect components are density-gapped, or
   classify them into the three observed families and their continuations.
2. Separately handle induced/engineered high-defect components, where the v56
   near-miss shows that the simple `delta < B/2` pattern is false.

Closure state remains unchanged:

- A2: not closed.
- A4: not closed.
- EP-488: not solved.
