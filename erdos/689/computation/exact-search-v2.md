# Exact search v2 for original Erdos 689

Created: 2026-04-24

Scope: this note records the second exact finite search for the original
no-zero-stage Problem 689.  It does not modify `exact_search_689.py`; the v2
implementation is `exact_search_689_v2.py` and uses only the Python standard
library.

## Model

For each prime `p <= n`, choose one residue `a_p mod p`.  Every `1 <= m <= n`
must receive at least two hits.

The v2 search stores the remaining demand as two Python integer bitsets:

- `need1`: points still needing at least one hit;
- `need2`: points still needing two hits.

Selecting `(p, a)` updates these masks by moving hit points from `need2` to
`need1`, and from `need1` to finished.  This avoids tuple-sized demand states
and makes gain computations simple `bit_count()` operations.

## Pruning and certificates

The old root capacity cut remains:

\[
  \sum_{p\le n}\max_a |\{m\le n:m\equiv a\pmod p\}| \ge 2n.
\]

This still proves all `n <= 136` infeasible.

The new search adds:

- capacity-tight residue domains: if current deficit is `D`, current aggregate
  capacity is `C`, and a residue for prime `p` loses more than `C-D` compared
  with the best current residue for `p`, then that residue cannot occur in any
  completion;
- subset capacity cuts: for any tested point subset `S`, the remaining demand
  inside `S` must be at most the sum over remaining primes of the best allowed
  residue intersection with `S`;
- tested subsets consisting of the two demand layers, small residue partitions
  modulo `2,3,5,7`, and constrained prefixes;
- forced propagation when a prime has only one allowed residue, or a point has
  exactly as many eligible prime-residue choices as remaining demand;
- exact branching on a point or prime with minimum branching count.

There is also a fast parity precheck.  After choosing the residue modulo `2`,
the opposite parity class needs two hits from odd primes.  For an odd prime
`p`, v2 computes exactly

\[
  M_b(n,p)=\max_a |\{m\le n:m\equiv a\pmod p,\ m\equiv b\pmod2\}|.
\]

If both

\[
  \sum_{p\le n,\ p\ odd} M_0(n,p)<2\lfloor n/2\rfloor
\]

and

\[
  \sum_{p\le n,\ p\ odd} M_1(n,p)<2\lceil n/2\rceil
\]

hold, then either choice modulo `2` leaves the opposite parity with too little
odd-prime capacity.  This is an exact subset-capacity certificate, not a
heuristic.

## Commands run

Smoke checks:

```powershell
python -m py_compile erdos\689\computation\exact_search_689_v2.py
python erdos\689\computation\exact_search_689_v2.py --help
```

Both completed successfully.

Boundary `n = 137` with fast precheck:

```powershell
python erdos\689\computation\exact_search_689_v2.py exact --n 137
```

Result: `infeasible`, `root_capacity = 274 = 2n`, certified by the parity
subset-capacity obstruction in `0.000039s`.

Same row with the fast precheck disabled, exercising the bitset search:

```powershell
python erdos\689\computation\exact_search_689_v2.py exact --n 137 --no-fast-precheck --time-limit 10 --node-limit 100000
```

Result: `infeasible`, `nodes = 1`, `prunes.subset = 1`, `seconds = 0.001963`.

Contiguous certificate through the parity threshold:

```powershell
python erdos\689\computation\exact_search_689_v2.py certify-range --max-n 3916 --time-limit 1 --node-limit 100000 --no-prefix-cuts --cut-moduli 2
```

Result:

```json
{
  "counts": {"infeasible": 3916},
  "first_covered": null,
  "first_unknown": null,
  "last_infeasible": {
    "n": 3916,
    "root_capacity": 9612,
    "primes": 541,
    "status": "infeasible",
    "prunes": {"parity": 1}
  }
}
```

First row after the parity obstruction clears:

```powershell
python erdos\689\computation\exact_search_689_v2.py certify-range --min-n 3917 --max-n 3917 --time-limit 2 --node-limit 100000 --no-prefix-cuts --cut-moduli 2 --stop-on-unknown
```

Result: `n = 3917` returned `unknown`.  The fast parity precheck no longer
applies: both parity capacities meet demand exactly at this row.  The bitset
search reached one root node and hit the time limit while computing root-level
cuts.

A stripped search at the same row, with the expensive subset families disabled,
does branch but still does not solve the instance:

```powershell
python erdos\689\computation\exact_search_689_v2.py exact --n 3917 --time-limit 5 --node-limit 100000 --no-prefix-cuts --no-residue-partition-cuts
```

Result: `unknown`, `nodes = 2`, `best_deficit = 5875`, `seconds = 7.229881`.

## Current status

The previous exact note established root-capacity infeasibility through
`n = 136` and left `n = 137` unknown.  V2 proves:

- `n = 137` is infeasible;
- every `1 <= n <= 3916` is infeasible;
- no covered instance has been found;
- the first currently unresolved finite row for v2 is `n = 3917`.

Thus the first solvable `n` is still not identified.  The search target has
moved from `137` to `3917`, where the simple parity capacity obstruction first
stops ruling out the instance.
