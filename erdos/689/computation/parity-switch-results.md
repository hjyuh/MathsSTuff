# Parity-first switching experiment

Created: 2026-04-24

This note records a standard-library computational experiment for the
parity-first switching model from `../parity-first.md`.

## Model

The baseline assignment is

```text
a_2 = 1 mod 2
a_p = 0 mod p for odd primes p <= n.
```

For a selected set `R` of odd primes moved away from zero, the script scores
the exact switching demand

```text
q_R(m) = max(0, 2 - C0(m) + L_R(m)),
```

where `C0(m) = 1_{m odd} + omega_odd(m)` and
`L_R(m) = #{p in R : p | m}`.  Chosen switched residues are constrained to be
nonzero, and the final deficit is recomputed from scratch as a verification of

```text
G_R(m) >= max(0, 2 - C0(m) + L_R(m)).
```

Pool conventions:

- `block:K` means odd primes in `n/(K+1) < p <= n/K`.
- `le-half` means odd primes `p <= n/2`.
- random medium pools sample from `0.05 n < p <= 0.5 n`.

## Commands

All commands were run from repository root on 2026-04-24 with Python 3.13.1.

Smoke checks:

```powershell
python -m py_compile erdos\689\computation\parity_switch_experiment.py
python erdos\689\computation\parity_switch_experiment.py --help
python erdos\689\computation\parity_switch_experiment.py baseline --n 100
```

Main suites:

```powershell
python erdos\689\computation\parity_switch_experiment.py suite --n 500 --blocks 2,3,4,5,8,12,16 --selection both --order initial-gain --local-passes 2 --seed 689 --random-trials 3 --random-count 80
python erdos\689\computation\parity_switch_experiment.py suite --n 1000 --blocks 2,3,4,5,8,12,16 --selection both --order initial-gain --local-passes 2 --seed 689 --random-trials 3 --random-count 80
python erdos\689\computation\parity_switch_experiment.py suite --n 2000 --blocks 2,3,4,5,8,12,16 --selection both --order initial-gain --local-passes 2 --seed 689 --random-trials 3 --random-count 120
```

Zero-net greedy probes:

```powershell
python erdos\689\computation\parity_switch_experiment.py run --n 1000 --pool le-half --selection net-greedy --min-net-gain 0 --max-switches 80 --local-passes 2 --seed 689
python erdos\689\computation\parity_switch_experiment.py run --n 2000 --pool le-half --selection net-greedy --min-net-gain 0 --max-switches 120 --local-passes 2 --seed 689
```

Dynamic-order random medium probes:

```powershell
python erdos\689\computation\parity_switch_experiment.py random --n 1000 --count 80 --seed 689 --selection fixed --order dynamic --local-passes 2
python erdos\689\computation\parity_switch_experiment.py random --n 1000 --count 80 --seed 690 --selection fixed --order dynamic --local-passes 2
python erdos\689\computation\parity_switch_experiment.py random --n 1000 --count 80 --seed 691 --selection fixed --order dynamic --local-passes 2
python erdos\689\computation\parity_switch_experiment.py random --n 2000 --count 120 --seed 689 --selection fixed --order dynamic --local-passes 2
python erdos\689\computation\parity_switch_experiment.py random --n 2000 --count 120 --seed 690 --selection fixed --order dynamic --local-passes 2
python erdos\689\computation\parity_switch_experiment.py random --n 2000 --count 120 --seed 691 --selection fixed --order dynamic --local-passes 2
```

## Baseline demand

| n | baseline points | baseline tokens |
|---:|---:|---:|
| 500 | 150 | 158 |
| 1000 | 257 | 266 |
| 2000 | 442 | 452 |

The `n=100` smoke baseline classified the positive demand exactly as expected:
`1`, powers of two, and even numbers with one odd prime factor.

## Contiguous block and half-pool results

The entries below are final token deficits after greedy plus two local residue
passes.  No run found a zero deficit.

| n | pool / method | switched | final deficit | uncovered points | note |
|---:|---|---:|---:|---:|---|
| 500 | best fixed block: `block:2` | 15 | 153 | 136 | baseline was 158 |
| 500 | `le-half`, fixed | 52 | 152 | 101 | best contiguous/half result |
| 500 | `le-half`, positive-net greedy | 5 | 153 | 138 | selected few switches |
| 1000 | best fixed block: `block:2` | 28 | 257 | 227 | baseline was 266 |
| 1000 | `le-half`, fixed | 94 | 260 | 187 | many hits, high switching cost |
| 1000 | `le-half`, positive-net greedy | 2 | 264 | 253 | very conservative |
| 2000 | best fixed block: `block:2` | 47 | 434 | 398 | baseline was 452 |
| 2000 | `le-half`, fixed | 167 | 464 | 329 | worse than baseline in tokens |
| 2000 | `le-half`, positive-net greedy | 2 | 450 | 438 | small improvement only |

Allowing zero-net greedy switches into the half-pool improved the net-greedy
behavior:

| n | pool / method | switched | final deficit | uncovered points | local improvement |
|---:|---|---:|---:|---:|---:|
| 1000 | `le-half`, net greedy, `--min-net-gain 0 --max-switches 80` | 72 | 248 | 198 | 3 |
| 2000 | `le-half`, net greedy, `--min-net-gain 0 --max-switches 120` | 120 | 427 | 323 | 6 |

## Random medium pools

Random fixed medium sets were stronger than contiguous blocks in these runs.
The first table uses `--order initial-gain`.

| n | sampled switches | seeds | final deficits |
|---:|---:|---|---|
| 500 | 44 available | 689, 690, 691 | 140, 140, 141 |
| 1000 | 80 | 689, 690, 691 | 241, 244, 243 |
| 2000 | 120 | 689, 690, 691 | 426, 432, 427 |

Dynamic residue ordering improved the random medium fixed sets:

| n | sampled switches | seed | final deficit | uncovered points |
|---:|---:|---:|---:|---:|
| 1000 | 80 | 689 | 240 | 165 |
| 1000 | 80 | 690 | 239 | 166 |
| 1000 | 80 | 691 | 243 | 170 |
| 2000 | 120 | 689 | 422 | 312 |
| 2000 | 120 | 690 | 420 | 311 |
| 2000 | 120 | 691 | 430 | 310 |

## Interpretation

These are heuristic failures, not impossibility certificates.

The exact switching cost is large enough that simply moving many primes can
make token demand worse, as seen for the full `p <= n/2` fixed pool at
`n=2000`.  Contiguous `n/K` blocks give modest improvements at best.  Random
medium sets are more effective, especially with dynamic ordering, but still
leave a large residual deficit.

The positive-net greedy rule is too conservative: it often stops after zero to
five switches.  Permitting zero-net switches helps, which suggests that useful
switching may need temporarily neutral moves whose created obligations are
repaired by later primes.  Coordinate local improvement was small in these
runs, usually `0` and at most `6` tokens.

Current computational takeaway: the parity-first model is faithfully thinner
at baseline, but the exact switching inequality remains the bottleneck.  The
observed successful moves look more like medium-prime global coordination than
like a one-block or purely positive-net greedy cleanup.
