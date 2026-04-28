# Erdos Problem 689 computation

This directory contains a reproducible, standard-library Python exploration for
Erdos Problem 689.

The script implements:

- residual-demand computation after the zero-residue stage `a_p = 0` for
  primes `p <= y`;
- greedy and staged greedy heuristics using reservoir primes `y < p <= n`;
- a small exact backtracking solver for fixed staged instances.

Heuristic failures are only heuristic failures. They are not disproofs of the
problem or of any asymptotic strategy.

## Commands

Run from the repository root:

```powershell
python erdos\689\computation\explore_689.py residual --n 1000 --y sqrt
python erdos\689\computation\explore_689.py greedy --n 1000 --y sqrt --stages 1.5,2,4,all
python erdos\689\computation\explore_689.py exact --n 30 --y sqrt --time-limit 10 --show-assignment
python erdos\689\computation\explore_689.py sweep --ns 50,100,200,500,1000 --y sqrt
```

Useful options:

- `--y sqrt`, `--y n/z --z 10`, `--y none`, or an integer cutoff choose the
  zero-residue stage.
- `--cap A` restricts the reservoir to primes `y < p <= A*y`.
- `--stages 1.5,2,4,all` reports cumulative staged reservoir use.
- `--refine-passes K` runs a conservative coordinate-refinement pass after
  greedy.
- `--exact-up-to N` in `sweep` runs exact search for the small rows only.

## Observed baseline results

These results were produced on 2026-04-24 with Python 3 using:

```powershell
python erdos\689\computation\explore_689.py sweep --ns 50,100,200,500,1000,2000 --y sqrt
```

The zero stage uses `y = floor(sqrt(n))`; greedy then uses all primes
`sqrt(n) < p <= n`.

| n | y | initial residual tokens | greedy remaining tokens | greedy remaining points |
|---:|---:|---:|---:|---:|
| 50 | 7 | 44 | 20 | 16 |
| 100 | 10 | 89 | 32 | 27 |
| 200 | 14 | 157 | 56 | 52 |
| 500 | 22 | 363 | 109 | 92 |
| 1000 | 31 | 673 | 186 | 179 |
| 2000 | 44 | 1284 | 350 | 271 |

For `n = 1000`, the residual classification after the zero stage was:

| class | points | tokens |
|---|---:|---:|
| one | 1 | 2 |
| prime | 168 | 325 |
| prime_power | 25 | 25 |
| one_small_one_large | 321 | 321 |

A staged greedy run for `n = 1000` with `--stages 1.5,2,4,all` gave:

| cumulative reservoir | new primes | deficit before | deficit after |
|---:|---:|---:|---:|
| `1.5*y` | 3 | 673 | 629 |
| `2*y` | 4 | 629 | 582 |
| `4*y` | 12 | 582 | 478 |
| all primes to `n` | 138 | 478 | 186 |

Adding `--refine-passes 2` on that same instance improved the remaining token
deficit from `186` to `169`.

The exact backtracker is intended only for small fixed staged instances. A
typical check is:

```powershell
python erdos\689\computation\explore_689.py exact --n 30 --y sqrt --time-limit 10 --show-assignment
```

Observed exact result:

```text
n=30, y=5: infeasible for this fixed zero stage and reservoir.
The capacity prune certifies this at the root: the sum of best possible
one-residue gains over primes 5 < p <= 30 is already below the 30 residual
tokens.
```

The same root capacity obstruction appears for the fixed `y = floor(sqrt(n))`
staged instances checked at `n = 5, 10, 15, 20, 25, 30, 35, 40, 50, 100, 150,
200, 300`. This only rules out those finite fixed-stage instances; it says
nothing against the asymptotic problem.

## Interpretation

For `y = sqrt(n)`, residual tokens are concentrated on `1`, large primes,
prime powers, and integers with exactly one small distinct prime factor. The
greedy heuristic is useful for measuring how much the most naive staged cover
misses, but it should not be read as a certificate. The exact solver can certify
small fixed staged instances, but its search tree grows quickly.
