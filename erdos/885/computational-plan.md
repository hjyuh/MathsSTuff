# EP885 computational search audit and next plan

Audit date: 2026-04-26.

This audit inspected `stageA_search.py`, `delta_first_search.py`, the C++ sources under
`include/` and `src/`, and the existing `out_*` directories. No large search was run.

## Exact incidence formulation

For positive `n`, the code uses positive factor pairs. This is sufficient even if the
problem statement allows integer factors, because the negative factor pair `(-a,-b)`
gives the same absolute difference as `(a,b)`.

Define

```text
D(n) = { delta >= 0 : exists a >= 1 with n = a(a + delta) }.
```

Equivalently, `delta in D(n)` iff

```text
s^2 = delta^2 + 4n
s == delta (mod 2)
a = (s - delta) / 2 >= 1
n = a(a + delta).
```

For a bounded computation with `n <= X` and `0 <= delta <= Delta`, define a bipartite
graph

```text
L = {0, 1, ..., Delta}
R = candidate n values, or all n <= X in the exact delta-first search
edge (delta, n) iff delta in D(n).
```

A `K_{5,5}` certificate is exactly:

```text
distinct deltas d_1 < ... < d_5
distinct integers n_1 < ... < n_5
for every i,j, n_j = a_ij(a_ij + d_i) for some positive integer a_ij.
```

This implies `|D(n_1) intersection ... intersection D(n_5)| >= 5`. Conversely, any
solution to the `k = 5` problem supplies such a biclique by taking five common deltas.

The current logs should therefore be interpreted as biclique logs:

```text
deltas = left vertices
n_values = right vertices
support = number of right vertices common to all listed deltas
```

## What the current code searches

### `stageA_search.py`

This is the most feature-complete implementation currently in the directory.

It has two candidate generators.

`square` mode:

- Enumerates smooth `m <= m_max` over the selected prime set.
- Builds `n = m^2 * t` for `t` in `--multipliers`.
- Computes the factorization and divisor count `tau(n)`.
- Keeps the top `--max-candidates` by high `tau`, then sorts by `n`.

Default square parameters:

```text
X = 10^10
m_max = 200000
primes = 2,3,5,7,11,13,17,19
multipliers = 1,2,3,6,10,15
max_candidates = 80000
```

`closepair` mode:

- Enumerates smooth `u` and `v`.
- Keeps `u <= v`, `uv <= X`, `v <= u * --pair-ratio`, and, if positive,
  `v <= u + --pair-gap-max`.
- Scores candidate `n = uv` by many divisors, smaller factor gap, then smaller `n`.
- Keeps the top `--max-candidates`.

Default closepair parameters:

```text
smooth_limit = 200000
pair_ratio = 1.20
pair_gap_max = 50000
candidate_mode = closepair
```

`both` mode merges the two candidate sets by `n`, preferring the higher `tau` entry.

After candidate generation, Stage A:

- Enumerates divisors for every candidate, capped by `--max-divisors`.
- Computes `D(n) intersection [0, --delta-max]`.
- Builds `delta -> sorted candidate ids`.
- Keeps deltas with support at least `--min-support`.
- Runs an Eclat-style DFS looking for `--target-k` deltas with at least
  `--min-support` common candidates.
- Logs pair/triple/k4/biclique records subject to logging thresholds.
- Writes `maxima.json` only after the DFS exits normally.

Important behavior:

- `stats.txt` is written before the expensive DFS, so it is not proof of completion.
- `maxima.json` is the best completion marker in current Python output.
- Existing output files are opened with mode `w`; reusing an existing output directory
  will overwrite files.

### `delta_first_search.py`

This is the exact bounded search over all `n <= X`, without choosing a candidate family.

For each delta, it builds the exact posting list

```text
S_delta = { a(a + delta) : a >= 1 and a(a + delta) <= X }.
```

Then it runs the same Eclat-style DFS over the posting lists.

Default parameters:

```text
X = 100000000
delta_max = 5000
min_support = 5
target_k = 5
```

This is exact inside the rectangle `n <= X`, `0 <= delta <= delta_max`, but it is much
heavier than Stage A. For `X = 10^8`, each small-delta posting list has about `10^4`
integers, so `5001` deltas means roughly tens of millions of Python integers before
the DFS even starts.

### C++ sources

The C++ code is a Stage A prototype, not a feature-parity replacement for the Python
search.

Current C++ behavior:

- `config.hpp` hardcodes `X = 10^10`, `delta_max = 20000`, `min_support = 5`,
  `target_k = 5`, `m_max = 200000`, primes up to 19, `max_candidates = 80000`.
- `smooth.cpp` only builds `n = m^2` from smooth `m`; it does not implement Python's
  multipliers, closepair mode, or `both` mode.
- `main.cpp` has no CLI, so changing parameters requires editing/recompiling.
- `logging.cpp` writes `candidates.tsv`, `k4.jsonl`, `bicliques.jsonl`, and `stats.txt`.
- It does not log pairs/triples, does not write `maxima.json`, and does not recover
  sample factor pairs.
- `build/` contains CMake configuration files only; no compiled executable was present
  in the inspected tree.

## Existing output audit

Current output directories are all dated March 20, 2026. Sizes and counts below are
from the inspected files.

| Directory | Apparent status | Key facts | Interpretation |
|---|---:|---|---|
| `out_stageA_py_smoke` | old or incomplete | 217 candidates, `delta_max=200`, 25 kept deltas, no k4/bicliques | Small square-style smoke run; no evidence of higher intersections. |
| `out_stageA_py_smoke2` | old or incomplete | 408 candidates, `delta_max=200`, 116 kept deltas, no k4/bicliques | Small closepair/square variant; no evidence of higher intersections. |
| `out_stageA_py_smoke3` | incomplete by current script criteria | 500 candidates, `delta_max=200`, 200 kept deltas, empty pair/triple/k4/biclique files, no `maxima.json` | Current script would write `maxima.json` on completion, so treat as interrupted or from an intermediate code version. |
| `out_stageA_py` | old or incomplete | 3419 candidates, `delta_max=20000`, 1966 kept deltas, no k4/bicliques | Likely square-style `n=m^2*t`; no current completion marker. |
| `out_stageA_py_run2` | old or incomplete | 22302 candidates, `delta_max=20000`, 12789 kept deltas, no k4/bicliques | Closepair-style broader run; no current completion marker. |
| `out_stageA_py_run3` | incomplete by current script criteria | 30000 candidates, `delta_max=20000`, 19988 kept deltas, empty pair/triple/k4/biclique files, no `maxima.json` | Started a dense search but did not finish under current script semantics. |
| `out_stageA_py_run4` | completed | 30000 candidates, `delta_max=20000`, 19988 kept deltas, `maxima.json` present | Best pair support is only 5, deltas `[9537, 18084]`; no triple/k4/k5 found. |
| `out_delta_first_smoke` | completed | `X=1000000`, `delta_max=200`, 201 kept deltas, 1000 logged pairs, no triples/k4/k5 | Exact small run found pair intersections up to support 20, best deltas `[195, 15]`; no triple survived support 5. |
| `out_delta_first_run1` | incomplete | 920 logged pairs, no `stats.txt`, no `maxima.json`, no triples/k4/k5 | Exact larger run was interrupted before final stats/maxima. Best logged pair support is 31, deltas `[1000, 440]`. |

Candidate summary:

```text
out_stageA_py:       3419 rows, max tau 1323
out_stageA_py_run2: 22302 rows, max tau 1512
out_stageA_py_run3: 30000 rows, max tau 2304
out_stageA_py_run4: 30000 rows, max tau 2304
```

For `out_stageA_py_run4`, the absence of `pairs.jsonl` records does not mean there
were no pairs. The default pair logging threshold is `--log-pair-min-support 30`, while
the completed `maxima.json` says the best pair support was only 5. Thus no pair met
the logging threshold.

## Why the outputs found or failed

The current runs successfully build incidence graphs, but they have not produced
evidence close to a `K_{5,5}`.

Stage A failed for two different reasons:

- Older/smoke directories do not have reliable current-script completion markers.
  They can show "no logged k4/k5", but they should not be treated as final negative
  evidence.
- The completed `out_stageA_py_run4` is stronger evidence: within its biased
  30000-candidate, `delta <= 20000` closepair-style window, even the best pair of
  deltas has exactly 5 common candidates, and no triple has 5 common candidates.

That suggests the selected candidate family is not producing dense higher-order
overlap. It may still contain divisor-rich numbers, but the small-delta factor-pair
incidences are not aligned across multiple deltas.

The exact delta-first smoke run found many pairs but no triples at support 5. This is
not surprising: pair intersections are common because two quadratic sequences can
meet repeatedly in a bounded range, while requiring a third delta imposes another
quadratic condition. The larger exact run found better pairs but did not finish, so it
is only useful as a source of promising pair seeds.

The C++ prototype was not used to produce a final result in the inspected tree. It is
also too narrow to replace the Python Stage A search because it only searches smooth
squares.

## Main bottlenecks

1. Too many kept deltas.

In `out_stageA_py_run4`, `19988` of `20001` possible deltas survived support `>= 5`.
The DFS then faces an enormous pair/triple search space even though most intersections
die quickly.

2. Python intersection cost.

Both Python scripts materialize a new list for every intersection. With many deltas,
this creates high allocation pressure. The two-pointer intersection is also inefficient
when intersecting a tiny current support set against a long posting list; binary-search
or bitset membership would be better.

3. Exact delta-first memory.

`delta_first_search.py` stores every `S_delta` as a Python list of Python integers.
At `X=10^8`, `delta_max=5000`, this can require very large memory before search.

4. Candidate-family bias.

Stage A is intentionally biased toward smooth near-squares and close smooth factor
pairs. The completed run indicates this family did not even produce support-5 triples
inside the chosen window.

5. C++ feature gap.

The faster language implementation lacks the Python candidate modes, CLI parameters,
pair/triple/maxima logs, and exact delta-first mode.

6. Output reproducibility.

Current scripts can overwrite prior output directories, do not write a full command or
parameter JSON, and use `maxima.json` as an implicit completion marker. This makes it
hard to distinguish a true negative run from an interrupted run.

## Recommended next experiments

The next phase should pivot from blind `K_{5,5}` DFS to pair/triple-seeded expansion.
The existing exact delta-first output already shows strong pairs; use those to build
triples deliberately.

### Experiment 0: output safety and metadata

Before more computation, make a small code change:

- Refuse to run if `--out-dir` already exists unless an explicit `--overwrite` flag is
  supplied.
- Write `run.json` at start with script name, command-line args, working directory,
  start time, Python version, and git status/hash if available.
- Write `complete.json` or `COMPLETE` only after all files close normally.
- Write `maxima.json` incrementally or at least periodically for long runs.
- Add final counters to `stats.txt`: logged pairs/triples/k4/k5 and best supports.

This is low risk and should happen before any more long run.

### Experiment 1: exact small validation grid

Purpose: verify the search and logging on small exact rectangles, and learn how pair
and triple supports change with `X` and `Delta`.

Suggested commands, each with a fresh output directory:

```powershell
python .\delta_first_search.py --x 1000000 --delta-max 300 --min-support 5 --target-k 5 --out-dir runs\20260426_delta_exact_X1e6_D300_ms5
python .\delta_first_search.py --x 3000000 --delta-max 300 --min-support 5 --target-k 5 --out-dir runs\20260426_delta_exact_X3e6_D300_ms5
python .\delta_first_search.py --x 10000000 --delta-max 500 --min-support 5 --target-k 5 --out-dir runs\20260426_delta_exact_X1e7_D500_ms5
```

Do not expand beyond `X=10^7, delta_max=500` in pure Python unless memory and runtime
are measured first.

Useful acceptance criteria:

- `complete.json` exists.
- `maxima.json` has nonzero best pair support.
- If best triple remains 0, record the largest pair supports and use them as seeds.

### Experiment 2: pair-seeded triple expansion

Purpose: avoid scanning all delta triples.

Algorithm:

1. From an exact run, keep pairs `(d1,d2)` with support at least a threshold such as
   `10`, `15`, or `20`.
2. For each pair, take its common `n` set.
3. For those `n`, enumerate all deltas in `D(n) intersection [0, Delta]`.
4. Count third deltas that appear for at least 5 of the common `n` values.
5. Emit triples and then repeat the same expansion to k4/k5.

Initial parameters:

```text
X = 10^7
Delta = 1000
pair_seed_min_support = 10
target_support = 5
max_pair_seeds = 10000
```

Then try:

```text
X = 10^8
Delta = 2000
pair_seed_min_support = 15
target_support = 5
max_pair_seeds = 50000
```

This should be implemented before attempting another full exact DFS.

### Experiment 3: optimized exact delta-first engine

Purpose: finish exact rectangles that pure Python cannot comfortably finish.

Recommended implementation changes:

- Port `delta_first_search.py` to C++ or add a new C++ mode.
- Store postings as `uint32_t` or `uint64_t` flat arrays with offsets, not Python lists.
- For small current intersections, test membership by binary search in postings.
- Optionally store bitsets for `n` ids only after coordinate-compressing all seen `n`.
- Add pair-seeded expansion as the primary mode, with full DFS as a validation mode.

First optimized targets:

```text
X = 10^7,  Delta = 2000, min_support = 5
X = 10^8,  Delta = 2000, min_support = 5
X = 10^8,  Delta = 5000, min_support = 5
```

Only move to `X = 10^9` after the `10^8` rectangle has completion markers and useful
timing/memory data.

### Experiment 4: Stage A candidate repair

Purpose: determine whether a biased candidate family can be made useful.

The completed Stage A run had no support-5 triples, so do not simply increase
`max_candidates` blindly. Instead:

- Add a `source` column to candidates: `square`, `closepair`, `seeded_exact_pair`,
  or `manual`.
- Inject `n` values from strong exact pair intersections into Stage A candidates.
- Compare candidate-only search with and without those injected values.
- Lower pair logging threshold for diagnostic runs.

Suggested diagnostic Stage A parameters:

```text
X = 10^10
delta_max = 50000
candidate_mode = both
smooth_limit = 200000
m_max = 200000
pair_ratio = 1.50
pair_gap_max = 200000
max_candidates = 50000
log_pair_min_support = 5
log_triple_min_support = 5
log_pair_max_records = 5000
log_triple_max_records = 5000
```

Run this only after output safety is added, because it will overwrite files if pointed
at an existing directory.

### Experiment 5: C++ parity before large Stage A

Before using C++ for serious runs, bring it to parity with the Python search:

- Add CLI flags matching Python names.
- Add `square`, `closepair`, and `both` candidate modes.
- Implement multipliers.
- Log pairs, triples, k4, bicliques, maxima, and completion markers.
- Recover sample factor pairs in logs.
- Add exact delta-first and pair-seeded modes.
- Add a dry-run mode that only generates candidates and delta support histograms.

Then compare C++ output against a small Python run with identical parameters.

## Parameter guidance

Use these starting ranges rather than jumping directly to huge runs.

| Engine | Safe diagnostic range | Next serious range | Avoid until optimized |
|---|---:|---:|---:|
| Python exact delta-first | `X <= 10^7`, `Delta <= 500` | `X = 10^7`, `Delta = 1000` with pair seeding | `X >= 10^8`, `Delta >= 5000` full DFS |
| Python Stage A | `max_candidates <= 50000`, `Delta <= 50000` | seeded candidates plus `both` mode | blind `max_candidates > 100000` |
| C++ Stage A prototype | small square-only validation | after Python parity work | treating current C++ as full search |
| Optimized C++ exact | `X = 10^8`, `Delta = 2000` | `X = 10^8`, `Delta = 5000` | `X >= 10^9` before profiling |

When diagnosing why nothing is logged, set:

```text
log_pair_min_support = 5
log_triple_min_support = 5
log_k4_min_support = 5
```

For production-size logs, raise pair/triple thresholds only after `maxima.json` shows
that lower-support data is uninteresting.

## File and output conventions

Use a new run root:

```text
erdos/885/runs/YYYYMMDD_HHMMSS_engine_shortparams/
```

Examples:

```text
runs/20260426_143000_delta_exact_X1e7_D500_ms5/
runs/20260426_151500_stageA_both_X1e10_D5e4_C5e4_seeded/
```

Every run directory should contain:

```text
run.json           full args, command, code version, start time
stats.txt          human-readable counters
maxima.json        best pair/triple/k4/k5 seen so far
complete.json      written only on normal completion
pairs.jsonl        optional; thresholded records
triples.jsonl      optional; thresholded records
k4.jsonl           optional; thresholded records
bicliques.jsonl    candidate K_{5,5} certificates
candidates.tsv     only for candidate-family runs
support.tsv        recommended: delta, support histogram rows
```

JSONL record convention:

```json
{
  "type": "triple",
  "support": 7,
  "deltas": [15, 195, 440],
  "n_values": [594, 1000],
  "relations": [
    {"n": 594, "delta": 15, "a": 18, "b": 33}
  ]
}
```

Conventions:

- `deltas` sorted ascending.
- `n_values` sorted ascending.
- `support` is the full common support, not just the number of sample values written.
- `relations` may be sampled, but every sampled relation must satisfy
  `n = a(a + delta)`.
- Never reuse an existing output directory.
- Prefer writing to temporary files and renaming at completion for large outputs.

## Immediate next step

Make the output-safety/metadata patch first. Then implement pair-seeded expansion using
the exact delta-first incidence formulation. The current data says that blind Stage A
scaling is less promising than exploiting strong exact pairs and trying to grow them
to triples, k4, and finally `K_{5,5}`.
