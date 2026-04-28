# Kernel Feasibility Toy Probe

Created: 2026-04-25

This note records a lightweight computational probe for the deterministic
limiting kernel feasibility lemma in the averaged-nibble route for Erdos
Problem 689.

The actual lemma lives in a much richer setting: a fixed but enormous switched
set `S`, residue classes modulo `W`, Green--Tao singular-integral densities, and
bounded kernels on finitely many block polytopes. The point of this script is
much narrower. It asks whether a residue-free discretized continuum model can
even *numerically* saturate label bins while keeping target-side loads below
`1 - gamma` on toy coefficient cores.

Because `scipy` was not available in this workspace, the runs below used the
standard-library greedy fallback, not an exact LP solve. So every positive
`gamma` below is a *greedy lower bound* for this toy discretization, and every
negative result is only a heuristic obstruction.

## Toy model

I used coefficient cores with odd `a` on the `A1` side and even `b` on the
`A2` side, always requiring `gcd(a, b) = 1`.

For fixed `beta` and a coarse robust-density parameter `rho`, I discretized:

- labels: `t = P / n` into `18` bins in `(1/5, beta]`;
- target positions: `z = x / n` or `y / n` into `48` bins in `(0, 1]`.

The edge geometry is the deterministic one from the kernel heuristic:

```text
z_y = z_x + 2 t
```

or the reverse orientation.

For each compatible oriented cell `(a, b, sigma, z-bin, t-bin)` I used a
nonnegative bounded variable `g`. In the simplified residue-free model the
discretized coefficients are

```text
label gain = dz / (2ab),
A1 load    = rho * dt / b,
A2 load    = rho * dt / a.
```

So the discrete feasibility problem is:

```text
for each t-bin:  total label load = 1,
for each A1/A2 target bin: total side load <= 1 - gamma,
0 <= g <= kernel_cap.
```

The default bound was `kernel_cap = 128`, chosen only to keep the toy kernels
bounded on the grid. A small sensitivity check at the end shows that the
threshold-like results below were unchanged when `kernel_cap` was changed to
`64` or `192`.

## Solver used here

The script is written to use `scipy.optimize.linprog` if available. In this
workspace `scipy` was missing, so all reported results come from the greedy
fallback:

1. fix a candidate `gamma`;
2. give every target bin capacity `1 - gamma`;
3. repeatedly pick the hardest unsatisfied label bin;
4. fill it fractionally through the cheapest currently available cells, where
   "cheap" means low endpoint pressure relative to remaining capacity.

I ran `12` randomized restarts for each `gamma`, on the grid
`0.40, 0.38, ..., 0.00`, and kept the best run.

## Commands

Run from repository root:

```powershell
python -m py_compile erdos\689\computation\kernel_feasibility_lp.py
python erdos\689\computation\kernel_feasibility_lp.py suite
python erdos\689\computation\kernel_feasibility_lp.py run --core wide --scenario threshold_like
```

The default suite finished in about `38` seconds here.

## Core families

I tested four toy coefficient cores:

| name | `A1` odd cores | `A2` even cores |
|---|---|---|
| `pair12` | `{1}` | `{2}` |
| `small` | `{1,3}` | `{2,4}` |
| `medium` | `{1,3,5}` | `{2,4,6}` |
| `wide` | `{1,3,5,7}` | `{2,4,6,8}` |

## Results

### Sanity checks

These first two scenarios are *not* in the real density window, since
`beta_threshold = 1/rho - 3/5` already exceeds `1/2`. They are only numerical
sanity checks for the machinery.

| scenario | `(beta, rho)` | `beta_threshold` | core | greedy-feasible `gamma` |
|---|---:|---:|---|---:|
| `sanity_low` | `(0.35, 0.75)` | `0.733333` | all four cores | `>= 0.40` |
| `sanity_mid` | `(0.45, 0.85)` | `0.576471` | `pair12` | `0.04` |
| `sanity_mid` | `(0.45, 0.85)` | `0.576471` | `small` | `0.34` |
| `sanity_mid` | `(0.45, 0.85)` | `0.576471` | `medium` | `>= 0.40` |
| `sanity_mid` | `(0.45, 0.85)` | `0.576471` | `wide` | `>= 0.40` |

So the coarse discretization does behave the way it should in easy regimes:
once there is enough geometric room, the greedy solver can saturate every label
bin with comfortable target slack.

### Threshold-like scenario

The interesting row is

```text
beta = 0.49,   rho = 0.92,   1/rho - 3/5 = 0.486956...
```

so this is the only tested case that actually mimics the `delta > 10/11`
window.

| core | cells | minimum compatible cells in a label bin | greedy-feasible `gamma` | comment |
|---|---:|---:|---:|---|
| `pair12` | 518 | 2 | none | only `3.9%` of label mass filled even at `gamma = 0` |
| `small` | 2072 | 8 | `0.04` | barely feasible; the best run sits right on the side cap |
| `medium` | 4144 | 16 | `0.22` | clear improvement once three odd/even cores are present |
| `wide` | 7770 | 30 | `0.30` | strongest toy result in this suite |

More explicitly:

- `pair12` failed badly. At `gamma = 0`, the best restart filled only
  `0.039043` of the total label demand, with the `A2` side already hitting load
  `1`. In this toy model, a single coefficient pair does not have enough local
  flexibility near the top of the interval.
- `small` succeeded, but only just: the best full-saturation lower bound was
  `gamma = 0.04`, with both sides peaking at load `0.96`.
- `medium` gave a much healthier toy margin: full saturation persisted up to
  `gamma = 0.22`, with best-run peak load `0.78`.
- `wide` pushed that lower bound to `gamma = 0.30`, with best-run peak load
  `0.70`.

At `gamma = 0`, every successful threshold-like run ended up with maximum target
load exactly `1.0`, so the informative statistic is not the `gamma = 0` row
itself but the largest `gamma` on the search grid for which full label
saturation still survived.

## Kernel-cap sensitivity

For the threshold-like scenario I reran the three successful cores with
`kernel_cap = 64, 128, 192`. The best full-saturation lower bounds were
unchanged:

| core | `cap = 64` | `cap = 128` | `cap = 192` |
|---|---:|---:|---:|
| `small` | `0.04` | `0.04` | `0.04` |
| `medium` | `0.22` | `0.22` | `0.22` |
| `wide` | `0.30` | `0.30` | `0.30` |

So in this finite probe the threshold-like transition appears to be driven more
by endpoint-capacity geometry than by the particular cap value.

## Interpretation

Finite takeaway only:

1. The residue-free toy model does **not** show an obvious deterministic
   side-capacity obstruction once more than one coefficient pair is allowed.

2. A single `(a, b) = (1, 2)` core is too rigid in the threshold-like window.
   That failure is real signal: the hardest label bins near `t = beta` have
   almost no geometric support there.

3. The picture changes sharply once several coprime odd/even cores are present.
   In the threshold-like test, the greedy lower bound rises from "none" to
   `0.04`, then `0.22`, then `0.30` as the core widens.

4. This is still far from a proof of the real deterministic kernel lemma.
   The toy model ignores residue classes modulo `W`, ignores singular-series
   variation, replaces the continuous optimization by a coarse grid, and here is
   solved only heuristically because `scipy` was unavailable.

So the right reading is modest but useful: this finite probe does *not* suggest
that the deterministic kernel-feasibility step is obviously impossible on pure
side-capacity grounds. What it does suggest is that the coefficient core must be
genuinely multi-type; the single-pair model is much too narrow, while a richer
core can already balance the toy loads with positive slack even in a
threshold-like discretization.
