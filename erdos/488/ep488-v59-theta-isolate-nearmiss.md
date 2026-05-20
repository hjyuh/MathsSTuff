# EP-488 v59 Theta-Isolate Near-Miss Search

Date: 2026-05-18

Status: partial progress, not a proof and not a counterexample.

## Purpose

The v56 strongest recorded high-defect near-miss was:

```text
q = 71440
n = 213189
core = theta13 scaled by 149
plus six isolated top-window vertices
best/B = 73408079/138734496 ~= 0.529126
```

The v59 question was whether the isolated layer is locally optimized. It is
not. A greedy search adding near-`q` isolated vertices to the same theta core
finds stronger finite-certified near-misses.

Script:

```powershell
python .\ep488_v59_theta_isolate_search.py --max-greedy 10 --max-cert-k 10 --json-out ep488_v59_theta_isolate_search.json
```

## Fixed Framework

```text
q = 71440
n = 213189
m_probe = 3411504
scale = 149
theta core =
{35760,36207,38144,40230,42912,44700,47680,
 48276,53640,57216,60345,64368,67050}
```

The core has:

```text
epsilon = 2
D_C(n) = 37
D_C(3411504) = 595
fixed probe ratio = 42282485/84150432 ~= 0.502463
```

## Greedy Isolates

The greedy exact fixed-`m_probe` search selected:

```text
71064,71065,71066,71067,71068,
71069,71070,71071,71072,71074
```

Each selected vertex is isolated from the theta core in `B_n(C,q)`. The
10-isolate prefix remains high-defect only through the theta core:

```text
|C| = 23
epsilon = 2
cyclomatic = 2
tau = 0
D_C(n) = 57
D_C(3411504) = 1074
fixed probe ratio = 12720277/21606192 ~= 0.588733
```

## Strongest Certified Prefix

For the 10-isolate prefix:

```text
C =
{35760,36207,38144,40230,42912,44700,47680,48276,53640,
 57216,60345,64368,67050,71064,71065,71066,71067,71068,
 71069,71070,71071,71072,71074}

B = 2D_C(n)/n = 38/71063
delta/B =
1555521561215874863099555045006187215873 /
2645687795967877418944058566679332295520
E = 14398
IE terms = 7199
cutoff = 65344340
```

Exact finite-window check:

```text
best = 23/72414 at m = 217242, D_C(m) = 69
best/B = 1634449/2751732 ~= 0.593971
failures = 0
```

Thus this is a stronger certified high-defect near-miss than the v56 recorded
near-miss, but it is still far below an EP violation.

For the original `F_Q` statement with `Q = C union {q}` at the best `m=217242`:

```text
F_Q(n) = 59
F_Q(m) = 72
(F_Q(m)/m) / (2F_Q(n)/n) = 142126/237357 ~= 0.598786
```

So this is not a counterexample to EP-488.

## Certified Prefix Table

```text
k  |C|  D(n)  best_over_B          status      cutoff
0  13   37    923819/1786212       certified   450457
1  14   39    497441/941382        certified   528116
2  15   41    355315/659772        certified   733482
3  16   43    284252/518967        certified   1398178
4  17   45    1208071/2172420      certified   2571771
5  18   47    71063/126054         certified   4624291
6  19   49    1350197/2365524      certified   9042973
7  20   51    355315/615519        certified   13490995
8  21   53    497441/852876        certified   26390519
9  22   55    71063/120690         certified   33528091
10 23   57    1634449/2751732      certified   65344340
```

## Uncertified Direction Beyond the Boundary

A separate greedy-only run:

```powershell
python .\ep488_v59_theta_isolate_search.py --max-greedy 20 --max-cert-k 0 --json-out ep488_v59_theta_isolate_greedy20.json
```

found that the fixed probe ratio continues increasing:

```text
20-isolate fixed probe ratio = 13715159/21890484 ~= 0.626535
```

This is not finite-certified by the current grouped-IE theorem; the naive
certificate becomes too loose because the inclusion-exclusion term count and
cutoff grow rapidly.

## Implication For A2

This changes the local picture of the A2 high-defect branch:

1. The strongest known certified high-defect near-miss is now the v59
   theta-plus-10-near-q-isolates example, with certified ratio about `0.593971`
   of the EP bound.
2. The old v56 example was not optimized once disconnected isolated vertices
   are allowed.
3. A2 cannot be closed by classifying only the cyclic high-defect component.
   One also needs an argument showing that attaching many isolated/top-window
   tree components cannot lift the global reduced ratio to 1.
4. The current finite-certificate theorem remains useful but becomes
   computationally weak for many isolates because `E` and the lcm term count
   explode.

## Closure State

- A2: not closed.
- A4: not closed.
- EP-488: not solved.
