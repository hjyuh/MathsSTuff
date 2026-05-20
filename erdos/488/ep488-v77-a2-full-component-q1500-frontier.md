# EP-488 v77 A2 Full-Component q1500 Frontier

Date: 2026-05-18

Status: A2 structural/census progress. This does not solve A2 or EP-488.

## Purpose

v76 showed that the current ledger's known connected A2 high-defect examples
collapse to four normalized motifs. v77 tests whether that small motif list is
stable by extending the sampled full top-window component census.

## Census

Command:

```powershell
python .\ep488_v58_full_component_census.py --q-max 1500 --max-cert-size 24 --max-cutoff 10000000 --json-out ep488_v77_full_component_census_q1500.json
```

Result:

```text
q_max = 1500
components checked = 924545
high_defect = 1412
status_counts = {'certified': 1412}
elapsed_seconds = 489.84
```

Every high-defect full-component row found is finite-certified. There are no
finite-window EP violations and no nonpositive `eta` rows in this sampled
full-component census.

## Normalization

Command:

```powershell
python .\ep488_v77_a2_full_component_q1000_motifs.py --input ep488_v77_full_component_census_q1500.json --json-out ep488_v77_a2_full_component_q1500_motifs.json
```

Result:

```text
high_defect rows = 1412
unique normalized full-component motifs = 14
bad edge-type rows = 0
status_counts = {'certified': 1412}
```

Every normalized edge type is still in the top-window alphabet:

```text
2:3, 3:4, 3:5, 4:5.
```

## Comparison To q1000

The q1000 full-component frontier had:

```text
high_defect rows = 527
unique normalized motifs = 7
```

The q1500 frontier has:

```text
high_defect rows = 1412
unique normalized motifs = 14
```

So the normalized full-component high-defect family is still growing between
`q=1000` and `q=1500`.

Size distribution at q1500:

```text
size 14: 2 motifs
size 16: 3 motifs
size 18: 1 motif
size 19: 2 motifs
size 20: 1 motif
size 21: 5 motifs
```

All have:

```text
epsilon = 2
```

in this census.

## Strongest Full-Component Near-Miss

The strongest row remains the q479 motif already seen in v58:

```text
q = 479
n = 1436
C =
{240,243,256,270,288,300,320,324,360,384,400,405,432,450}
size = 14
B = 39/718
best/B = 14719/28431
```

New larger motifs do not beat this full-component ratio.

## New Larger Motif Layer

Representative largest q1500 motifs:

```text
size 20:
{640,648,675,720,729,750,768,800,810,864,900,960,
 972,1000,1024,1080,1125,1152,1200,1215}
best/B = 52486/103125

size 21:
{640,648,675,720,729,750,768,800,810,864,900,960,
 972,1000,1024,1080,1125,1152,1200,1215,1250}
best/B = 4795/9396

size 21:
{720,729,750,768,800,810,864,900,960,972,1000,1024,
 1080,1125,1152,1200,1215,1250,1280,1296,1350}
best/B = 65819/129033
```

These are harmless in the finite certificates, but they show that a finite
list of the four v76 motifs cannot be the A2 proof.

## Interpretation

This is useful negative information. The A2 full-component branch does not
appear to stabilize to a tiny fixed list after q500/q1000. Instead, it behaves
more like the A4 pure-cycle branch: normalized motifs keep appearing at larger
scales while remaining safely below the EP bound.

The plausible A2 target is therefore:

```text
Develop a correction-aware fixed-motif density certificate for connected
epsilon >= 2 components in the four-ratio graph, analogous to the v71-v75 A4
certificate.
```

The full-component data suggests this may be viable:

```text
all q1500 high-defect rows are certified,
all use only the four allowed edge types,
all have epsilon = 2,
and the strongest ratio remains far below 1.
```

## Limitations

This is still not A2:

- it is a full top-window component census, not arbitrary induced subsets;
- for `q > 100`, the existing v58 census samples `n` values;
- it does not handle engineered induced examples like v56/v59 except through
  the separate v76 normalization and v60 isolate theorem.

## Closure State

```text
A2: not closed; q1500 full-component high-defect frontier has 14 normalized
    motifs, all certified
A4: all normalized pure-cycle motifs through length 18 closed; global A4 open
EP-488: not solved
```
