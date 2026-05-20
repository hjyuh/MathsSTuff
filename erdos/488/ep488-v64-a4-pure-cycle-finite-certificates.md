# EP-488 v64 A4 Pure-Cycle Finite Certificates

Date: 2026-05-18

Status: partial A4 progress. This does not prove A4 for all pure cycles, but it
upgrades the v63 checks from bounded event-window evidence to all-`m`
finite certificates for the normalized motifs tested.

## Purpose

For a pure cycle host `Z`, A4 is:

```text
H_Z#(m)/m + c_m(L_cyc)/m <= 2 H_Z#(n)/n.
```

The left side is itself a finite signed sum of q-excluded floor-count terms.
Therefore the grouped finite-certificate theorem applies directly.

## Certificate Form

For a pure cycle `Z = (a_1,...,a_r)`, define coefficients by

```text
N_Z(x) =
  sum_i c_x(a_i;q)
  - sum_i c_x(lcm(a_i,a_{i+1});q)
  + c_x(L_cyc;q).
```

Then A4 is exactly

```text
N_Z(m)/m <= 2 H_Z#(n)/n.
```

Group this signed sum by denominator `d`:

```text
N_Z(x) = sum_d alpha_d c_x(d;q).
```

Set

```text
delta = sum_d alpha_d (1/d - 1/lcm(d,q)),
E = 2 sum_d |alpha_d|,
B = 2 H_Z#(n)/n.
```

Then

```text
N_Z(m)/m <= delta + E/m.
```

If `eta = B - delta > 0`, only

```text
n < m <= floor(E/eta)
```

needs exact checking.

## Script

```powershell
python .\ep488_v64_a4_pure_cycle_finite_cert.py --input-json ep488_v63_a4_normalized_cycle_motifs_len12.json --json-out ep488_v64_a4_pure_cycle_finite_cert_len12.json

python .\ep488_v64_a4_pure_cycle_finite_cert.py --input-json ep488_v63_a4_normalized_cycle_motifs_len14.json --json-out ep488_v64_a4_pure_cycle_finite_cert_len14.json
```

## Results

For the `max_len=12` normalized motif file:

```text
motifs = 28
status_counts = {'certified': 28}
max_cutoff = 13460
```

For the `max_len=14` normalized motif file:

```text
motifs = 84
status_counts = {'certified': 84}
max_cutoff = 123474
```

No eta failures and no finite-window A4 violations occurred.

## Strongest Ratios

The worst ratio among the length-14 certified motifs is still the triangle:

```text
normalized cycle = {12,15,20}
q = 21
n = 60
best m = 61
N_Z(m) = 10
B = 2H_Z#(n)/n
best/B = 100/183 ~= 0.546448
```

Other high ratios:

```text
{8,9,10,12,15}: best/B = 69/128 ~= 0.539062
{24,27,30,36,40,45}: best/B = 585/1088 ~= 0.537684
{96,108,120,135,144,160,180}: best/B = 8/15 ~= 0.533333
```

All are far below an A4 violation.

## What This Fixes

v62/v63 checked event points only in a bounded window. v64 removes that
weakness for the tested normalized motifs: each checked motif is now certified
for every `m > n`.

## What Remains

This still does not prove pure-cycle A4 globally. What remains is:

```text
Prove that every feasible pure cycle in the four-ratio graph either belongs to
a certified finite family, or prove the finite-certificate eta/window bound
uniformly for all such cycles.
```

The likely next theorem is a uniform pure-cycle finite-certificate margin:

```text
B - delta >= positive function of the cycle, sufficient to bound the finite
window by a manageable multiplier table.
```

## Closure State

```text
A2: partially advanced, not closed
A4: leaf-pruned to pure cycles; pure-cycle motifs through length 14 certified
    for all m, but no global pure-cycle theorem yet
EP-488: not solved
```
