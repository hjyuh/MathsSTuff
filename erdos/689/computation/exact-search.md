# Exact search for original Erdos 689

This file records the separate exact/branching search for the original finite
Problem 689 instance.  Unlike `explore_689.py`, this search does not impose the
square-root zero-residue stage.  It chooses one residue class modulo every
prime `p <= n` and checks whether every integer `1 <= m <= n` receives at
least two hits.

## Script

`exact_search_689.py` is standard-library-only.

Search model:

- variables are primes `p <= n`;
- domain for prime `p` is residue `a = 0, ..., p - 1`;
- a choice `(p, a)` covers all `m <= n` with `m == a mod p`;
- each `m` starts with demand `2`;
- when all demands reach zero, unassigned prime residues are filled with `0`,
  because extra coverage cannot hurt.

Branching:

- select a currently deficient target `m`;
- branch over remaining primes `p`, forcing `a_p = m mod p`;
- recurse after reducing every demand hit by that congruence class.

This is complete: in any full solution, the chosen target is covered by at
least one remaining prime, and independent prime choices can be reordered so
that this covering prime is selected next.

Pruning:

- point capacity: if any demand exceeds the number of remaining primes, fail;
- aggregate capacity: total remaining demand must be at most the sum, over
  remaining primes, of the best one-residue gain against currently deficient
  points;
- small-prefix subset capacity: for several prefixes of high-demand points,
  total demand inside the prefix must be no more than the sum of best
  one-residue gains restricted to that prefix;
- memoization by `(demand tuple, remaining primes tuple)`.

## Commands and results

All commands below were run from repository root on 2026-04-24 with Python 3.

Smoke check:

```powershell
python -m py_compile erdos\689\computation\exact_search_689.py
python erdos\689\computation\exact_search_689.py --help
```

Both completed successfully.

Small-instance sweep:

```powershell
python erdos\689\computation\exact_search_689.py sweep --ns 1,2,3,4,5,10,20,40,80,120,136,137,138,139 --time-limit 2 --node-limit 200000 --target-policy tight
```

Key rows:

| n | primes <= n | required tokens | root capacity | status | nodes | best deficit | note |
|---:|---:|---:|---:|---|---:|---:|---|
| 1 | 0 | 2 | 0 | infeasible | 1 | 2 | root capacity |
| 2 | 1 | 4 | 1 | infeasible | 1 | 4 | root capacity |
| 5 | 3 | 10 | 6 | infeasible | 1 | 10 | root capacity |
| 10 | 4 | 20 | 13 | infeasible | 1 | 20 | root capacity |
| 20 | 8 | 40 | 32 | infeasible | 1 | 40 | root capacity |
| 40 | 12 | 80 | 70 | infeasible | 1 | 80 | root capacity |
| 80 | 22 | 160 | 153 | infeasible | 1 | 160 | root capacity |
| 120 | 30 | 240 | 238 | infeasible | 1 | 240 | root capacity |
| 136 | 32 | 272 | 271 | infeasible | 1 | 272 | root capacity |
| 137 | 33 | 274 | 274 | unknown | 1521 | 146 | 2s limit |
| 138 | 33 | 276 | 275 | infeasible | 1 | 276 | root capacity |
| 139 | 34 | 278 | 279 | unknown | 1808 | 138 | 2s limit |

The root-capacity certificate proves that no full assignment exists for every
`n <= 136`: even if each prime chose the currently best residue class, the sum
of those best possible one-residue gains is less than `2n`.  The first `n`
where this coarse capacity obstruction disappears is `n = 137`, where capacity
equals demand exactly.

Contiguous certification command:

```powershell
python erdos\689\computation\exact_search_689.py search-first --max-n 136 --time-limit 1 --node-limit 100000 --target-policy tight
```

Result: `first_covered` was `null`; every row `1 <= n <= 136` was
`infeasible` at one search node by root capacity.

Boundary search at `n = 137`:

```powershell
python erdos\689\computation\exact_search_689.py exact --n 137 --time-limit 10 --node-limit 1000000 --target-policy tight
```

Result:

```json
{
  "best_deficit": 146,
  "final_deficit": 274,
  "initial_tokens": 274,
  "memo_size": 6041,
  "message": "time limit 10.000s reached",
  "n": 137,
  "nodes": 6054,
  "primes": 33,
  "required": 2,
  "root_capacity": 274,
  "seconds": 10.005033,
  "status": "unknown"
}
```

Larger sampled searches:

```powershell
python erdos\689\computation\exact_search_689.py sweep --ns 150,175,200,250,300 --time-limit 5 --node-limit 200000 --target-policy tight
python erdos\689\computation\exact_search_689.py sweep --ns 150,175,200,250,300 --time-limit 5 --node-limit 200000 --target-policy gain
```

All sampled rows returned `unknown` within 5 seconds.  No actual full
assignment was found in this run.  The first existing `n` is therefore not yet
identified; current exact certificates only establish nonexistence through
`n = 136`.
