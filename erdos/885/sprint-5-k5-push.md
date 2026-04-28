# EP885 sprint 5: K5 push after Bremner reconstruction

Date: 2026-04-26.

## What changed

This sprint moved from "we have Bremner's K4,4 examples" to "we can generate
and test the Bremner rank-one family."

New or updated files:

```text
scripts/bremner_map.py
scripts/common_deltas_factor.py
scripts/bremner_family_scan.py
notes/k5-fifth-row-condition.md
notes/common-delta-scaling-strategy.md
bremner-reconstruction-and-k5-analogue.md
```

## Exact Bremner-family scan

The scanner now supports:

- per-`N` factorization timeout;
- anchor-divisor bound;
- anchor-based exact common-delta testing;
- status counts and runtime reporting.

The exact common-delta method factors all four `N_i`, chooses the one with the
fewest divisors, enumerates only that `D(N_i)`, and tests each candidate delta
against the other `N_j` via

```text
delta^2 + 4N_j = square.
```

This avoids materializing all four huge divisor sets.

## Runs completed

```text
runs/20260426_bremner_family_scan_n3_14_d90_t12_a5m.json
runs/20260426_bremner_family_scan_n7_10_d130_t12_a25m.json
runs/20260426_bremner_family_scan_n3_8_d90.json
```

Exact checked points:

```text
3Q+T
4Q
5Q+T
6Q
7Q+T
8Q+T
```

Every checked point had:

```text
common_delta_count = 4
candidate_count = 0
```

The `8Q+T` check reached 89-digit `N_i` values.  Larger generated examples were
skipped by digit or divisor bounds; for example, the targeted scan reports
`9Q+T` with anchor divisor count `130,024,440,000`, which is not a sensible
direct divisor-enumeration target.

## Structural fifth-row status

For a Bremner-family point \(P\), the known K4,4 rows give four sections:

```text
x, y, z, t.
```

A fifth row \(u\) must satisfy

```text
u_i^2 - u_0^2 = N_i(P),    i = 1,2,3,4.
```

For a fixed generic Bremner point, this is a fiber product of four double
covers of the \(u_0\)-line.  Generically it has genus `17`.  That is the main
reason a naive K4-to-K5 extension is much harder than the K3-to-K4 Bremner
step.

Even a nontrivial fifth row would only produce a K5,4 object.  A full K5,5
certificate also needs a fifth column satisfying all five rows.

## Interpretation

The current evidence weakens the direct promotion route:

- the first printed Bremner seed has exactly four common deltas;
- fixed-row extension failed to find a fifth column up to `10^12`;
- product lifting gave only square scalings;
- Bremner-family points checked through `8Q+T` have exactly four common deltas;
- the generic fifth-row fiber is high-genus.

This does not rule out EP885.  It means the next useful approaches are more
specific:

1. Implement the difference-first common-delta enumeration from
   `notes/common-delta-scaling-strategy.md` so huge divisor-anchor cases can be
   tested exactly.
2. Symbolically study whether the genus-17 fifth-row fiber over Bremner's final
   elliptic curve has special rational sections or low-degree multisections.
3. Search for a multiplicative/product-lift mechanism that produces `K_{k,k}`
   objects without passing through generic high-genus fibers.

## Percentage

After this sprint:

```text
isolated K5,5 search: 20-25%
whole EP885 closure: 10-15%
```

This is lower than a pure optimism estimate because the first real structural
look shows a high-genus barrier rather than a nearby missing parameter.  It is
higher than zero because we now have exact family generation, exact
factorization-based checking, and a concrete fifth-row equation to attack.
