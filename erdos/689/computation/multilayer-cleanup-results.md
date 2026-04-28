# Arbitrary-residue multi-layer cleanup experiment

Created: 2026-04-24

This note records a focused computation for the parity-first arbitrary-residue
cleanup route.

## Model

Start from the parity-first baseline

```text
a_2 = 1 mod 2,
a_p = 0 mod p for odd primes p <= n.
```

Fix a small repair sieve `S` and switch each `s in S` to one nonzero residue
`c_s mod s`. A medium/high odd prime `p > n / K` is called repairable if

```text
p == c_s mod s
```

for some `s in S`. Only repairable primes are allowed to switch away from zero.
Each such prime chooses one arbitrary nonzero residue class modulo `p`.

Exact switching cost is kept throughout: when a prime is switched, every
multiple of that prime gains one unit of demand, and the chosen nonzero residue
class supplies one hit on its congruence class. The cleanup phase uses dynamic
net-greedy selection with `--min-net-gain 0`, so zero-net steps are allowed but
negative-net steps are not.

Two sieve sets were tested:

- `S = {3,5}`. All `8` residue assignments were checked exhaustively by final
  exact deficit after greedy cleanup.
- `S = {3,5,7,11,13}`. All `5760` residue assignments were scanned by a cheap
  capacity score `sum_{repairable p > n/K} floor(n/p)` with direct sieve
  improvement as a tie-break, then the exact greedy cleanup was run on the
  selected assignment.

The key capacity proxy reported below is `independent upper`: after fixing the
repair sieve, sum over repairable primes of their best one-class gross hit count
on the current residual set, ignoring overlap and ignoring later switching
penalties. This is optimistic, not a proof bound, but it is a useful first test
of plausibility.

## Commands

Run from repository root with Python 3.13.1:

```powershell
python -m py_compile erdos\689\computation\multilayer_cleanup_experiment.py
python erdos\689\computation\multilayer_cleanup_experiment.py suite --ns 500,1000,2000 --ks 6,8
```

Observed suite runtime: about `41.6s`.

## Baseline tokens

| n | baseline tokens |
|---:|---:|
| 500 | 158 |
| 1000 | 266 |
| 2000 | 452 |

## Results

| n | K | sieve | chosen residues `c_s` | after sieve deficit | independent upper | final deficit |
|---:|---:|---|---|---:|---:|---:|
| 500 | 6 | `{3,5}` | `(2,3)` | 187 | 101 | 136 |
| 500 | 6 | `{3,5,7,11,13}` | `(2,2,6,10,8)` | 220 | 136 | 133 |
| 500 | 8 | `{3,5}` | `(2,3)` | 187 | 112 | 136 |
| 500 | 8 | `{3,5,7,11,13}` | `(2,2,2,10,8)` | 221 | 155 | 132 |
| 1000 | 6 | `{3,5}` | `(2,2)` | 320 | 186 | 234 |
| 1000 | 6 | `{3,5,7,11,13}` | `(2,3,3,2,12)` | 376 | 239 | 239 |
| 1000 | 8 | `{3,5}` | `(2,2)` | 320 | 205 | 234 |
| 1000 | 8 | `{3,5,7,11,13}` | `(2,2,6,1,7)` | 371 | 269 | 228 |
| 2000 | 6 | `{3,5}` | `(2,4)` | 558 | 329 | 409 |
| 2000 | 6 | `{3,5,7,11,13}` | `(2,4,1,1,9)` | 641 | 419 | 396 |
| 2000 | 8 | `{3,5}` | `(2,2)` | 555 | 365 | 407 |
| 2000 | 8 | `{3,5,7,11,13}` | `(2,2,5,8,6)` | 645 | 465 | 405 |

Selected cleanup coverage from the post-sieve state:

- `{3,5}` recovered about `26.7%` to `27.3%` of the after-sieve deficit.
- `{3,5,7,11,13}` recovered about `36.4%` to `40.3%` of the after-sieve
  deficit.

Best final rows by `n`:

- `n = 500`: final deficit `132` at `K = 8`, `S = {3,5,7,11,13}`.
- `n = 1000`: final deficit `228` at `K = 8`, `S = {3,5,7,11,13}`.
- `n = 2000`: final deficit `396` at `K = 6`, `S = {3,5,7,11,13}`.

These are improvements over baseline, but only by `26`, `38`, and `56` tokens
respectively; the remaining deficit is still large.

## Interpretation

Within this one-class-per-repairable-prime model, the route does not currently
look capacity-plausible.

- Switching the repair sieve itself is expensive. The post-sieve deficit is
  always much larger than the parity-first baseline: from `158` up to
  `187-221`, from `266` up to `320-376`, and from `452` up to `555-645`.
- The larger sieve does help: it creates more repairable high primes and
  recovers roughly `36-40%` of the post-sieve deficit, versus about `27%` for
  `{3,5}`.
- Even so, the optimistic `independent upper` capacity is below the post-sieve
  deficit in every row. So even before overlap and exact switching penalties,
  the available one-class high-prime cover already looks short of what the
  switched sieve creates.
- The best exact greedy runs still leave deficits `132`, `228`, and `396` at
  `n = 500, 1000, 2000`.

This is not an impossibility proof. It only says that, for these finite tests
with a fixed small repair sieve and one arbitrary class per repairable prime
`p > n/K`, the route does not appear close to closing the exact parity-first
deficit.
