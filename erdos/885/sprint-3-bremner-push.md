# EP885 sprint 3: Bremner/K44 push

Date: 2026-04-26.

Superseded note: the Bremner paper was later obtained locally on 2026-04-26.
See `sprint-4-bremner-found.md` and `known-constructions.md` for verified
K4,4 certificates and extension checks.  The acquisition section below records
the earlier state before the PDF was available.

Goal: push the main remaining EP885 branch:

```text
obtain or reconstruct a K_{4,4} seed -> test K_{4,4} to K_{5,5}
```

## Acquisition result

The legal acquisition pass is in `bremner-acquisition-pass.md`.

Bottom line:

- no legal full text found;
- no explicit Bremner `K_{4,4}` seed found;
- OpenAlex, Unpaywall, and Semantic Scholar all report no open-access copy;
- World Scientific PDF/ePDF/full endpoints returned `403`;
- ResearchGate exposes only a publisher preview/first page;
- the author email visible in the preview and ASU page is:

```text
bremner@asu.edu
```

The report includes a ready-to-send email request for either an author
manuscript or one explicit `K_{4,4}` certificate.

## New code

`scripts/seed_extend.py` now has two more modes:

```text
product-lift
restricted-delta-mine
```

`product-lift` tests common-multiplier/divisor-split transforms of a seed.
`restricted-delta-mine` builds a small seed-derived delta universe and searches
for high-support rowsets inside that restricted universe.

I also added:

```text
scripts/quartic_k44_scan.py
```

This implements the integer-parameter scan from `k44-reconstruction-plan.md`.
For ordered rows `(d1,d2,d3,d4)`, it checks whether both

```text
Q_3(p) = p^4 + (2A - 4B)p^2 + A^2
Q_4(p) = p^4 + (2A + 4K)p^2 + A^2
```

are integer squares, where

```text
A = d1^2 - d2^2
B = d1^2 - d3^2
K = d4^2 - d1^2.
```

This is not full elliptic arithmetic, but it is a cheap falsifiable scan.

## Runs completed

### Forum seed

Product-lift:

```text
runs/20260426_152000_seedext_forum_product_M2000
```

Result:

```text
lift_count = 176
nontrivial_lift_count = 0
trivial_square_scale_count = 176
```

Restricted delta mining:

```text
runs/20260426_153000_seedext_forum_restricted_X1e7_D5e3
```

Result:

```text
delta_universe_count = 6
rowset_count = 0
witness_count = 0
```

Quartic scan:

```text
runs/20260426_162000_forum_quartic_p200k.json
```

Result:

```text
p_max = 200000
total_hit_count = 144
k44_candidate_count = 0
```

### Guiduli seed 1

Product-lift:

```text
runs/20260426_154000_seedext_guiduli1_product_M2000
```

Result:

```text
lift_count = 176
nontrivial_lift_count = 0
```

Restricted delta mining:

```text
runs/20260426_160000_seedext_guiduli1_restricted_X1e9_D2e5
```

Result:

```text
delta_universe_count = 9
triple_count = 25
rowset_count = 0
witness_count = 0
```

Quartic scan:

```text
runs/20260426_163000_guiduli1_quartic_p200k.json
```

Result:

```text
p_max = 200000
total_hit_count = 144
k44_candidate_count = 0
```

### Guiduli seed 2

Product-lift:

```text
runs/20260426_155000_seedext_guiduli2_product_M2000
```

Result:

```text
lift_count = 176
nontrivial_lift_count = 0
```

Restricted delta mining:

```text
runs/20260426_161000_seedext_guiduli2_restricted_X1e9_D2e5
```

Result:

```text
delta_universe_count = 6
triple_count = 1
rowset_count = 0
witness_count = 0
```

Quartic scan:

```text
runs/20260426_164000_guiduli2_quartic_p200k.json
```

Result:

```text
p_max = 200000
total_hit_count = 104
k44_candidate_count = 0
```

## Interpretation

The public `K_{4,3}` seeds are very rigid under every cheap transformation
tested so far:

- strict fixed-row extension fails through `X=10^12`;
- one-row swaps around the forum seed do not produce serious near misses;
- product-lift only gives square scalings;
- restricted seed-derived delta mining finds no promoted four-row object;
- the integer `p` quartic scan finds individual hits but no `K_{4,4}` group.

This does not make EP885 implausible.  It means the known public `K_{4,3}`
examples are probably not the right local objects.  Bremner's actual `K_{4,4}`
construction remains the highest-value missing input.

## Next move

The best next action is external:

```text
email Bremner for the paper or one explicit K_{4,4} witness
```

If we continue locally without the paper, the next meaningful coding task is
full elliptic arithmetic for the three-row curve:

```text
E(A,B): W^2 = X(X-A)(X-B)
```

Then generate combinations of known column-points and apply the fourth-row
square filter.  The integer `p` scan is only a thin slice of that search.
