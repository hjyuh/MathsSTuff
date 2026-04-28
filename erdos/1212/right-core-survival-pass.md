# Right-Core Survival Pass

Date: 2026-04-27

Superseded status note, 2026-04-28: this pass measured local right-core
branching. The later `slab-flow-survival-pass.md` measured compatible
multi-slab survival and found a finite compatibility obstruction. The local
branching signal remains valid, but the overall percentage should be read as
45-50%, not 55%.

## Inputs

Script:

```text
scripts/buffered_live_pair_stats.py
scripts/verify_buffered_certificate.py
```

Primary result files:

```text
results/right-core-theta-scan-N50000.json
results/right-core-theta-scan-N200000.json
results/right-core-theta034-N1000000.json
results/right-core-theta036-N1000000.json
results/right-core-logpower-scan-N1000000.json
```

The script now reports:

```text
right_core_pairs
right_core_fraction
reg_mean_right_core
reg_zero_right_core
core_to_core_mean
core_to_core_zero
longest_core_ray_certificate
```

It also uses a guard band: source pairs satisfy `v + H(v) <= cap`, and
incomplete dyadic slabs are omitted by default.

## Polynomial Buffers

For `H(x)=floor(x^theta)`, the all-pair regenerative mean was misleading.
The right-core conditional statistics are strongly different.

Top complete dyadic slab for each run:

```text
cap       theta  slab              pairs    core    core-frac  reg|core  core->core  zero    longest-core
50000     0.34   [16384,32768)     19972    1128    0.0565     1.587     1.041       0.368   17
50000     0.36   [16384,32768)     20308    1014    0.0499     1.640     1.045       0.383   16
50000     0.38   [16384,32768)     19918     819    0.0411     1.774     1.013       0.380   15
50000     0.40   [16384,32768)     18310     640    0.0350     1.778     0.909       0.430   16
50000     0.42   [16384,32768)     15044     410    0.0273     1.793     0.759       0.478    9
50000     0.45   [16384,32768)      7399     114    0.0154     1.395     0.307       0.763    4

200000    0.34   [65536,131072)   122312    6403    0.0523     2.575     1.687       0.207   70
200000    0.36   [65536,131072)   128371    5971    0.0465     2.764     1.765       0.226   78
200000    0.38   [65536,131072)   131175    5104    0.0389     3.012     1.777       0.229   65
200000    0.40   [65536,131072)   126729    4075    0.0322     3.133     1.671       0.258   54
200000    0.42   [65536,131072)   112086    2859    0.0255     3.214     1.494       0.310   36

1000000   0.34   [262144,524288)  744301   36813    0.0495     3.995     2.734       0.122  385
1000000   0.36   [262144,524288)  812915   35056    0.0431     4.509     2.982       0.118  654
```

Interpretation:

```text
The strict buffered theorem should not be abandoned.
The right-core subgraph is supercritical in these finite ranges.
The strongest observed range is theta roughly 0.34-0.40, with theta=0.36
looking best at N=1e6 among the two million-scale runs completed here.
```

The right-core fraction decreases slowly with `theta`, but the conditional
regenerative count rises with scale. The core-to-core mean crosses 1 around
`theta=0.34-0.38` already by `N=50000`, and is safely above 1 at `N=200000`.

## Polylog Buffers

For `H(x)=floor(log(x)^A)` at `N=1e6`:

```text
A  slab              pairs    core   core-frac  reg|core  core->core  zero    longest-core
2  [131072,262144)  318230   9290   0.0292     4.289     2.296       0.198   263
3  no buffered/right-core states at this cap
4  no buffered/right-core states at this cap
5  no buffered/right-core states at this cap
```

The `A >= 3` null result is not negative evidence at this scale. Strict
buffering forces rough composite coordinates. A composite number `n` with
`P^-(n) > H(n)+1` must satisfy roughly `n > H(n)^2`. For `N=1e6`,
`log(N)^3` is already too large for such composites to appear in the tested
range.

## Status Update

This pass moves the computational side to the requested 55% marker:

```text
graph reduction:             stable
exact DAG formulation:        added
right-core branching signal:  positive to N=1e6 for theta=0.34,0.36
polylog A=2 signal:           positive to N=1e6
analytic theorem:             still absent
```

The next theorem should be stated on the right-core subgraph:

> For some increasing buffer `H`, the `H`-buffered right-core live-pair graph
> has an infinite directed ray.

The next analytic target is not merely a raw rough-number count. It is a
two-stage estimate:

```text
right-core density among buffered states
times
core-to-core regenerative successors conditional on right-core.
```

## Next Work

1. Run `theta=0.38,0.40` at `N=1e6` if runtime permits.
2. Extract local residue statistics along the long core rays, especially
   whether the best rays are just clusters of rough semiprimes or show a
   reusable singular-series pattern.
3. Turn the right-core branching evidence into a formal finite-slab crossing
   conjecture.
