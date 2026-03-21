# Erdos Problem 885

## Problem

For an integer `n >= 1`, define

`D(n) = {|a-b| : ab = n}`.

Question: for every `k >= 1`, do there exist integers

`N_1 < ... < N_k`

such that

`|D(N_1) ∩ ... ∩ D(N_k)| >= k`?

Known:

- `k = 2`: Erdős-Rosenfeld
- `k = 3`: Jiménez-Urroz
- `k = 4`: Bremner
- `k = 5`: first open case

## Current local plan

This workspace implements the first computational attack for `k = 5`.

The search is based on the bipartite graph:

- left vertices: differences `delta`
- right vertices: integers `n`
- edge `delta ~ n` iff `delta in D(n)`

Then `k = 5` becomes a `K_{5,5}` biclique search.

## Stage A

Stage A is deliberately conservative:

- generate candidate numbers `n = m^2` where `m` is smooth over small primes
- compute `D(n) ∩ [0, Delta]`
- build the inverted index `delta -> {candidate ids}`
- run an Eclat-style search for 5 deltas with at least 5 common candidates
- log strong `k = 4` intersections even if `k = 5` is not found

## Build

```powershell
cmake -S . -B build
cmake --build build --config Release
```

## Run

```powershell
.\build\Release\ep885.exe
```

or on single-config generators:

```powershell
.\build\ep885.exe
```

Outputs land in `out_stageA/`.

## Python fallback

If you do not have a C++ compiler installed, use the pure Python Stage A search:

```powershell
cd C:\Users\z20ma\Documents\MathsSTuff\erdos\885
python .\stageA_search.py
```

This writes outputs to `out_stageA_py/`.

For a faster smoke test:

```powershell
python .\stageA_search.py --x 1000000000 --m-max 50000 --delta-max 5000 --max-candidates 15000
```

For the stronger first real run, use a richer candidate family:

```powershell
python .\stageA_search.py `
  --x 10000000000 `
  --candidate-mode closepair `
  --smooth-limit 200000 `
  --delta-max 20000 `
  --max-candidates 30000 `
  --primes "2,3,5,7,11,13,17,19,23,29" `
  --pair-ratio 1.20 `
  --pair-gap-max 50000 `
  --progress-interval 500 `
  --out-dir out_stageA_py_run2
```

The Python version keeps the same basic pipeline:

- generate structured candidates, either:
  - smooth near-squares `n = m^2 * t`, or
  - close smooth factor pairs `n = u*v` with `u ≈ v`
- compute `D(n) ∩ [0, Delta]`
- build `delta -> {candidate ids}`
- search for `K_{5,5}` bicliques
- log strong pair/triple/`k=4` intersections even if `k=5` is not found
- recover sample factor pairs `(a,b)` for logged `(n, delta)` relations

## Direct delta-first fallback

If candidate-family search looks too biased, use the direct delta-first search:

```powershell
python .\delta_first_search.py --x 100000000 --delta-max 5000 --out-dir out_delta_first_run1
```

This does **not** guess a family of `n` first. It builds the exact sets

`S_delta = { a(a+delta) : a >= 1, a(a+delta) <= X }`

and then searches for large common intersections of these `S_delta`.
