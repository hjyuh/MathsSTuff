# EP-488 v62 A4 Pure-Cycle Census

Date: 2026-05-18

Status: partial A4 progress. This is not a proof of A4 or EP-488.

## Purpose

v61 reduced A4 from arbitrary connected unicyclic hosts to pure cycle hosts.
v62 attacks the remaining pure-cycle target computationally and structurally.

The target inequality for a pure cycle host `Z` is:

```text
2m H_Z#(n) - n H_Z#(m) >= n c_m(L_cyc(Z)).
```

## Script

```powershell
python .\ep488_v62_a4_pure_cycle_check.py --q-max 500 --max-len 12 --json-out ep488_v62_a4_pure_cycle_check_q500.json
```

The checker enumerates simple cycle subgraphs in the top-window q-excluded LCM
graph, computes `H_Z#`, generates event points, and checks the A4 margin.

## q <= 500 Result

```text
q_max = 500
max_len = 12
pure cycle hosts checked = 116354
failures = 0
length_counts = {
  3: 85920,
  5: 15555,
  6: 8817,
  7: 1173,
  8: 120,
  11: 3464,
  12: 1305
}
L_cyc <= n count = 85920
q divides L_cyc count = 45
normalized motifs = 13
```

The worst margin remains the basic triangle:

```text
q = 21
n = 60
cycle = {12,15,20}
m = 61
H_Z#(n) = 9
H_Z#(m) = 9
L_cyc = 60
margin = 498
```

## Normalized Motifs Seen

The 116354 checked pure cycles collapse to 13 normalized motifs:

```text
length 3:
  {12,15,20}

length 5:
  {8,9,10,12,15}

length 6:
  {24,27,30,36,40,45}
  {32,36,40,45,48,60}

length 7:
  {27,30,32,36,40,45,48}
  {96,108,120,135,144,160,180}

length 8:
  {81,90,96,108,120,135,144,160}
  {108,120,128,135,144,160,180,192}
  {135,144,150,160,180,200,225,240}

length 11:
  {216,240,243,256,270,288,320,324,360,384,405}
  {240,243,256,270,288,320,324,360,384,405,432}
  {243,256,270,288,320,324,360,384,405,432,480}

length 12:
  {240,243,256,270,288,300,320,324,384,405,432,450}
```

The length 11 and 12 motifs are the same arithmetic region as the Kimi/theta
high-defect obstructions, now seen as pure-cycle A4 hosts.

## Structural Observations

1. In the census, `L_cyc <= n` occurs only for the triangle motif
   `{12,15,20}`.

2. For longer cycles, `L_cyc > n` unless `q | L_cyc`, matching U9. When
   `q | L_cyc`, the correction term `c_m(L_cyc)` is identically zero.

3. No length 4, 9, or 10 pure cycle motifs appeared through `q <= 500`.

4. The smallest margins are all triangle margins; longer cycles have much
   larger margins in the checked range.

## Remaining A4 Lemma

The exact remaining theorem is now:

```text
Pure-Cycle A4 Lemma:
For every reduced top-window pure cycle host Z, and every relevant event point
m, 2m H_Z#(n) - n H_Z#(m) >= n c_m(L_cyc(Z)).
```

The best next route is a normalized motif theorem:

```text
Every reduced top-window pure cycle host is one of finitely many normalized
ratio motifs, and each motif satisfies the A4 margin by a finite multiplier
table.
```

v62 supplies the candidate motif list through `q <= 500`, but does not prove
that the list is complete.

## Closure State

```text
A2: partially advanced, not closed
A4: reduced to pure cycles; pure cycles checked to q<=500, not proved
EP-488: not solved
```
