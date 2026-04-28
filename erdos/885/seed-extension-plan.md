# EP885 seed-extension computational plan

Created: 2026-04-26.

This plan is a continuation of `computational-plan.md`.  It narrows the next
computations to seed extension from known `K_{4,3}` and eventual `K_{4,4}`
objects, instead of another blind `K_{5,5}` search.

No experiment below should write into an existing `out_*` directory.  New
outputs should go under `erdos/885/runs/YYYYMMDD_HHMMSS_seedext_*`, and the
runner should refuse to start if `--out-dir` already exists.

## Current seed data

The verified forum object is:

```text
N = [79200, 227205, 1258560]
D = [36, 468, 692, 1028]
```

with complete intersection

```text
D(79200) cap D(227205) cap D(1258560) = [36, 468, 692, 1028].
```

This is a `K_{4,3}` incidence object.  It is not a literal subobject of any
`K_{5,5}` witness: any `K_{5,5}` containing all three displayed `N` values
would need five common deltas for those three values, but they have exactly
four.  Forum-seeded searches must therefore use the row set as a structured
seed, or drop at least one of the three forum columns.

For a future Bremner `K_{4,4}` seed, run the same first test:

```text
C_N = D(N_1) cap D(N_2) cap D(N_3) cap D(N_4).
```

If `|C_N| = 4`, no `K_{5,5}` can contain all four Bremner columns.  If
`|C_N| >= 5`, strict extension is still possible and should be tested before
mutation searches.

## Seed record format

Normalize every seed, including Bremner examples once extracted, into a JSON
record:

```json
{
  "id": "forum_k43_20260426",
  "source": "EP885 forum triple, verified locally",
  "n_values": [79200, 227205, 1258560],
  "deltas": [36, 468, 692, 1028],
  "relations": [
    {"n": 79200, "delta": 36, "a": 264, "b": 300}
  ]
}
```

Required invariants:

- `n_values` are distinct positive integers.
- `deltas` are distinct nonnegative integers, sorted on load.
- Every relation satisfies `n = a * b` and `b - a = delta`.
- Missing relations are recovered with the verifier formula
  `s^2 = delta^2 + 4n`, `a = (s - delta) / 2`.

The existing `results/forum-triple-certificate.json` is already close to this
format.  The extension runner should accept it directly.

## Core data structures

Use sorted integer arrays and coordinate compression; avoid Python object-heavy
structures in the hot path.

```text
Seed:
  id: str
  rows: tuple[int, ...]              # deltas
  cols: tuple[int, ...]              # N values
  matrix[(n, d)] = (a, b)

ColumnRecord:
  n: int
  row_values: tuple[int, ...]        # seed rows it satisfies
  a_by_delta: dict[int, int]
  b_by_delta: dict[int, int]
  source: "seed" | "fixed_rows" | "swap" | "product_lift"

DeltaProfile:
  n: int
  deltas: tuple[int, ...]            # complete if factored, bounded otherwise
  factorization: tuple[(p, e), ...] | null

CompressedPool:
  n_values: list[int]                # sorted
  n_to_id: dict[int, int]
  profiles: list[DeltaProfile]
  postings_by_delta: dict[int, array[uint32]]
```

For C++ parity later, use the same layout as the current prototype:

```text
offsets[d]..offsets[d+1] index into ids[]
ids[] stores uint32 compressed N ids
n_values[] stores uint64 or arbitrary-precision decimal strings
```

For small Python experiments, a `dict[int, list[int]]` is acceptable after
coordinate compression.  For large Bremner integers, store `n` as decimal text
in JSONL and use Python `int` only while verifying.

## Algorithm 0: output safety

Every seed-extension run starts with:

```text
if out_dir.exists(): abort
mkdir(out_dir)
write run.json
write seed.json
write files as *.tmp, then rename
write complete.json only on normal completion
```

`run.json` should contain:

```json
{
  "script": "scripts/seed_extend.py",
  "mode": "fixed-rows",
  "argv": ["..."],
  "cwd": "...",
  "start_time": "2026-04-26T...",
  "python": "...",
  "git_status_short": "..."
}
```

Never reuse `out_stageA_py*` or `out_delta_first*` for these experiments.

## Algorithm 1: exact seed verification

For each requested `(n, delta)`:

```python
def factor_pair(n: int, d: int) -> tuple[int, int] | None:
    disc = d*d + 4*n
    s = isqrt(disc)
    if s*s != disc:
        return None
    if (s - d) % 2:
        return None
    a = (s - d) // 2
    b = a + d
    if a <= 0 or a*b != n:
        return None
    return a, b
```

For small and moderate `n`, compute complete `D(n)` by factoring `n`,
enumerating all divisors `a <= sqrt(n)`, and storing `n/a - a`.

Outputs:

```text
verified_seed.json
common_deltas.json
strict_extension_status.txt
```

Acceptance criteria:

- Forum seed verifies exactly and reports `strict_extension_status = impossible`
  for retaining all three current columns.
- A Bremner seed either reports the same impossibility for retaining all four
  columns, or lists the extra deltas in `C_N \ D_seed`.

## Algorithm 2: fixed-row column enumeration

Given a row set `R = {d_1, ..., d_r}` and bound `X`, enumerate

```text
I(R; X) = {n <= X : R subset D(n)}.
```

Use one seed row as an anchor, preferably the row with the smallest
`a_max(d, X)`:

```python
def a_max(d: int, X: int) -> int:
    return (isqrt(d*d + 4*X) - d) // 2

def enumerate_columns_for_rows(rows: list[int], X: int):
    anchor = min(rows, key=lambda d: a_max(d, X))
    for a0 in range(1, a_max(anchor, X) + 1):
        n = a0 * (a0 + anchor)
        rels = {anchor: (a0, a0 + anchor)}
        ok = True
        for d in rows:
            if d == anchor:
                continue
            pair = factor_pair(n, d)
            if pair is None:
                ok = False
                break
            rels[d] = pair
        if ok:
            yield ColumnRecord(n=n, a_by_delta=..., b_by_delta=...)
```

This avoids materializing all `S_delta` postings.  For `X = 10^8` and the forum
rows, the anchor loop is only about `10^4` iterations; for `X = 10^10`, it is
about `10^5` iterations.  These are safe diagnostic sizes.

Outputs:

```text
columns_for_rows.jsonl
columns_summary.json
```

Summary counters:

```text
rows
X
anchor_delta
anchor_a_max
num_columns
num_seed_columns
min_n
max_n
```

## Algorithm 3: add one row to a fixed-row column pool

If all candidate columns already share four seed rows `R`, a `K_{5,5}` is found
as soon as some extra delta `e not in R` occurs in at least five of those
columns.

For each enumerated column `n`, compute a delta profile:

- If `n <= 10^12`, factor `n` by trial division or `sympy.factorint` if
  available, enumerate all divisors, and record complete `D(n)`.
- If `n` is larger and factorization is unavailable, use bounded scanning
  `0 <= d <= delta_extra_max` with the `factor_pair(n, d)` test, and mark the
  profile as bounded.

Then build support:

```python
support: dict[int, list[int]] = {}
for col_id, profile in enumerate(profiles):
    for e in profile.deltas:
        if e not in seed_rows:
            support.setdefault(e, []).append(col_id)

for e, ids in support.items():
    if len(ids) >= 5:
        emit_witness(rows=sorted(seed_rows + [e]), columns=choose_5(ids))
```

Column choice policy:

1. Prefer a witness with as many original seed columns as possible.
2. For the forum seed, cap this at two original columns, since all three make
   five rows impossible.
3. Break ties by smaller maximum `n`, then smaller sum of `n`.

Outputs:

```text
delta_support.tsv          # delta, support, seed_column_count, sample_n_values
witnesses.jsonl            # exact K_{5,5} candidates
near_misses.jsonl          # support 3 or 4 for extra rows
profiles.jsonl             # optional, complete or bounded D(n)
```

Every witness must be immediately rechecked with the same logic as
`scripts/verify_biclique.py`.

## Algorithm 4: strict extension for Bremner `K_{4,4}` seeds

For a Bremner seed with rows `R` and columns `N_seed`:

1. Compute `C_N = cap_j D(N_j)` exactly.
2. If `C_N \ R` is empty, record that no `K_{5,5}` can contain all seed
   columns.
3. For each `e in C_N \ R`, set `R5 = R union {e}`.
4. Enumerate `I(R5; X)` by Algorithm 2.
5. If any non-seed column appears, combine it with the four seed columns and
   verify a `K_{5,5}`.

Initial bounds:

```text
X = max(10^8, 10 * max(N_seed)) if max(N_seed) <= 10^10
X = max(N_seed) for a first containment-only check if Bremner values are huge
delta_extra_max = complete D(N_j) when factored
```

This strict test is cheap and should precede all mutation searches.

## Algorithm 5: one-row swap search

The forum seed cannot be strictly extended, so search row sets one mutation
away from the known rows.

Replacement delta sources:

```text
A. Pair intersections D(N_i) cap D(N_j) from seed columns, computed exactly.
B. Individual D(N_i) values up to replacement_delta_max.
C. Strong pair deltas from completed exact runs, for example
   out_delta_first_smoke best pair [195, 15].
D. Future Bremner row and column common-delta pools.
```

Generate candidate row sets:

```python
base = set(seed_rows)
for d_out in seed_rows:
    for d_in in replacement_pool:
        if d_in in base:
            continue
        rows2 = sorted((base - {d_out}) | {d_in})
        yield rows2
```

Deduplicate by tuple.  Rank row sets before enumeration:

```text
score = (
  -number_of_seed_column_pairs_preserved,
  abs(d_in - d_out),
  max(rows2),
  rows2
)
```

For each `rows2`, run Algorithms 2 and 3.  Stop after `max_rowsets` unless a
witness is found.

Initial forum parameters:

```text
X = 10^7
replacement_delta_max = 5000
max_rowsets = 200
min_columns_before_augment = 5
delta_extra_mode = complete for n <= 10^12
near_miss_min_support = 4
```

Second pass if the first pass is clean:

```text
X = 10^8
replacement_delta_max = 20000
max_rowsets = 1000
```

## Algorithm 6: one-column drop for `K_{4,4}` seeds

For a Bremner `K_{4,4}` seed that fails strict extension:

```python
for S in all 3-column subsets of seed columns:
    C_S = cap_{n in S} D(n)
    for rows in ranked 4-subsets of C_S:
        enumerate I(rows; X)
        try to add one extra row by Algorithm 3
```

Ranking:

```text
1. rows containing the most original Bremner deltas
2. rows with at least one extra delta from C_S \ R_seed
3. smaller max(rows)
4. smaller product of rows + 1
```

This tests the nearest possible `K_{5,5}` objects after dropping one seed
column.  It is the Bremner analogue of the forum one-row-swap search.

## Algorithm 7: product-lift diagnostics

Product multiplication can create new structured seeds without solving a new
curve.  Given a seed matrix with factor pairs

```text
N_j = a_ij * b_ij,  b_ij - a_ij = d_i,
```

multiply every column by a common integer `M`.  For row `i`, choose a divisor
split `M = u_i * v_i`.  Then

```text
M*N_j = (u_i*a_ij) * (v_i*b_ij)
new_gap_ij = |v_i*b_ij - u_i*a_ij|.
```

Row `i` survives the lift if `new_gap_ij` is independent of `j` across the
selected columns.  Enumerate:

```python
for M in range(1, M_max + 1):
    divs = divisors(M)
    surviving_rows = []
    for i in seed_rows:
        for u in divs:
            v = M // u
            gaps = {abs(v*b[i,j] - u*a[i,j]) for j in selected_columns}
            if len(gaps) == 1:
                surviving_rows.append((only(gaps), i, u, v))
    for row_subset in distinct_gap_subsets(surviving_rows, size>=4):
        emit transformed seed with columns [M*N_j]
```

Then feed each transformed `K_{4,s}` seed into Algorithms 2 and 3.

Initial parameters:

```text
forum:  M_max = 2000, selected_columns = all 2-column and 3-column subsets,
        require_surviving_rows >= 4
Bremner: M_max = 500 for first pass, selected_columns = all 3-column and
        4-column subsets, require_surviving_rows >= 4
```

Outputs:

```text
product_lifts.jsonl
product_lift_summary.tsv
```

A lift that only rescales all rows by a square is a regression case, not a new
lead.  Mark it as `trivial_square_scale`.

## Algorithm 8: structured exact pair mining

Use exact delta-first mining only to supply replacement rows and near misses,
not as a full `K_{5,5}` DFS.

For a delta universe `U`:

```text
U = seed rows
  union row-swap replacement pool
  union deltas from exact small runs
  union future Bremner common-delta pools
```

build exact postings

```text
S_d(X) = {a(a+d) <= X}
```

only for `d in U`.  Intersect pairs and triples in this restricted universe,
then send high-support triples and `K_{4,t}` near misses to Algorithms 2 and 3.

Initial parameters:

```text
X = 10^7
|U| <= 2000
pair_min_support = 10
triple_min_support = 4
target_support = 5
```

This is intentionally much smaller than the full exact DFS over every
`0 <= d <= Delta`.

## Today's small experiments

These are diagnostic-size runs only.  Use fresh timestamped directories.

### 1. Re-verify the forum seed

```powershell
python .\scripts\verify_biclique.py `
  --n "79200,227205,1258560" `
  --d "36,468,692,1028" `
  --out .\runs\20260426_110000_seedext_forum_verify\verified_seed.json
```

Expected: `ok = true`.  Also compute complete common deltas and record that
strict containment of all three columns is impossible for `k = 5`.

### 2. Enumerate columns sharing the four forum rows

After adding `scripts/seed_extend.py` with Algorithms 0 to 3:

```powershell
python .\scripts\seed_extend.py fixed-rows `
  --seed .\results\forum-triple-certificate.json `
  --rows "36,468,692,1028" `
  --x 10000000 `
  --delta-extra-mode complete `
  --near-miss-min-support 3 `
  --out-dir .\runs\20260426_111000_seedext_forum_rows_X1e7
```

Then, if the run completes quickly and `complete.json` exists:

```powershell
python .\scripts\seed_extend.py fixed-rows `
  --seed .\results\forum-triple-certificate.json `
  --rows "36,468,692,1028" `
  --x 100000000 `
  --delta-extra-mode complete `
  --near-miss-min-support 3 `
  --out-dir .\runs\20260426_112000_seedext_forum_rows_X1e8
```

Success conditions:

- A verified `witnesses.jsonl` record gives `K_{5,5}`.
- Otherwise, `near_misses.jsonl` should show which extra deltas have support
  `3` or `4` among the fixed-row column pool.

### 3. Forum one-row swaps

```powershell
python .\scripts\seed_extend.py row-swap `
  --seed .\results\forum-triple-certificate.json `
  --x 10000000 `
  --replacement-source seed-pairs `
  --replacement-delta-max 5000 `
  --max-rowsets 200 `
  --delta-extra-mode complete `
  --near-miss-min-support 4 `
  --out-dir .\runs\20260426_113000_seedext_forum_rowswap_X1e7_D5e3
```

Do not raise both `X` and `max_rowsets` in the same follow-up.  If this run is
small, the next safe pass is:

```text
X = 10^8
replacement_delta_max = 20000
max_rowsets = 1000
```

### 4. Product-lift smoke test from the forum matrix

```powershell
python .\scripts\seed_extend.py product-lift `
  --seed .\results\forum-triple-certificate.json `
  --m-max 2000 `
  --selected-column-sizes "2,3" `
  --require-surviving-rows 4 `
  --out-dir .\runs\20260426_114000_seedext_forum_product_M2000
```

Promote only nontrivial transformed seeds to fixed-row extension runs.

### 5. Restricted exact mining around seed deltas

```powershell
python .\scripts\seed_extend.py restricted-delta-mine `
  --seed .\results\forum-triple-certificate.json `
  --x 10000000 `
  --delta-universe seed-pairs `
  --delta-max 5000 `
  --max-deltas 2000 `
  --pair-min-support 10 `
  --triple-min-support 4 `
  --out-dir .\runs\20260426_115000_seedext_forum_restricted_X1e7_D5e3
```

This should produce replacement row sets and near misses, not run a full DFS
over all deltas.

### 6. Bremner seed intake, once available

After extracting one Bremner `K_{4,4}` witness:

```powershell
python .\scripts\seed_extend.py verify-seed `
  --seed .\results\bremner-k44-seed-001.json `
  --compute-common-deltas complete `
  --out-dir .\runs\20260426_120000_seedext_bremner001_verify
```

If `C_N \ R_seed` is nonempty:

```powershell
python .\scripts\seed_extend.py strict-bremner `
  --seed .\results\bremner-k44-seed-001.json `
  --x AUTO `
  --out-dir .\runs\20260426_121000_seedext_bremner001_strict
```

If strict containment is impossible:

```powershell
python .\scripts\seed_extend.py drop-one-column `
  --seed .\results\bremner-k44-seed-001.json `
  --x AUTO `
  --max-rowsets 500 `
  --near-miss-min-support 4 `
  --out-dir .\runs\20260426_122000_seedext_bremner001_drop1
```

Use `AUTO = max(10^8, 10 * max(N_seed))` only when that is below `10^11`.
For larger Bremner numbers, start with containment and bounded delta-profile
checks before enumerating new columns.

## Promotion rules

Promote a result to a serious follow-up only if one of these occurs:

- A verified `K_{5,5}` witness appears.
- A `K_{5,4}` or `K_{4,5}` near miss appears with exact factor-pair relations.
- A row-swap or product-lift run produces many columns for a nontrivial
  four-row set, for example `|I(R; 10^8)| >= 5`.
- A Bremner seed has an extra common delta, making strict `K_{5,4}` extension
  available.

Do not promote merely because a run has many pairs.  The completed Stage A run
already showed that pair support alone does not predict support-five triples.

## Implementation order

1. Add `scripts/seed_extend.py` with modes `verify-seed`, `fixed-rows`, and
   `row-swap`.
2. Add output safety and `complete.json` before any search mode.
3. Reuse `verify_biclique.py`'s factor-pair logic for all final certificates.
4. Add product-lift and restricted-delta mining only after the fixed-row code
   writes reproducible summaries.
5. When a Bremner seed is extracted, run `verify-seed` and `strict-bremner`
   before any broad mutation.

The main near-term goal is not a large run.  It is to learn whether the known
`K_{4,3}` and `K_{4,4}` mechanisms have nearby fifth rows or fifth columns, and
to record exact near misses that can be reverse-engineered algebraically.
