# Robust-density 18-state DP results

Created: 2026-04-25

This note records bounded computations from
`robust_density_dp.py`, which implements the 18-state dynamic program from
`robust-density-threshold.md` for the initial prime segments
\[
S(y):=\{p\text{ prime}:7\le p\le y\}.
\]

The event is
\[
\delta_{S(y)}=\mathbf P(X_1\ge 1,\ X_2\ge 2,\ X_4\ge 2),
\]
with local step distribution
\[
Z_s=(1,0,0),(0,1,0),(0,0,1)\ \text{each with probability }1/(s-1),
\]
and
\[
Z_s=(0,0,0)\ \text{with probability }(s-4)/(s-1).
\]

The script has three arithmetic modes:

1. `exact`: exact integer weights with common denominator
   \(\prod_{s\in S}(s-1)\);
2. `decimal`: direct `Decimal` state probabilities;
3. `auto`: exact first, then convert to `Decimal` after a chosen prime-count
   threshold.

It also reports the bounds
\[
1-A_S(3+2\mu'_S)\le \delta_S \le 1-A_S(1+\mu'_S),
\]
where
\[
A_S=\prod_{s\in S}\frac{s-2}{s-1},
\qquad
\mu'_S=\sum_{s\in S}\frac1{s-2}.
\]

The target from `robust-density-threshold.md` is
\[
\delta_* \approx 0.943931047925499105.
\]

## Commands run

From the repository root:

```powershell
python -m py_compile erdos\689\computation\robust_density_dp.py
python erdos\689\computation\robust_density_dp.py --mode exact --digits 18 segment --y 1000
python erdos\689\computation\robust_density_dp.py --mode exact --digits 18 segment --y 10000
python erdos\689\computation\robust_density_dp.py --mode exact --digits 18 segment --y 100000
python erdos\689\computation\robust_density_dp.py --mode decimal --digits 18 segment --y 100000
python erdos\689\computation\robust_density_dp.py --digits 18 sweep --ys 50,100,200,1000,10000,100000,1000000,10000000 --format markdown
python erdos\689\computation\robust_density_dp.py --digits 18 search --y-max 10000000
python erdos\689\computation\robust_density_dp.py heuristic --calibrate-y 10000000
```

## Sanity checks

For the exact runs at `y = 1000`, `10000`, and `100000`, the DP matched the
closed-form one-layer identities
\[
\mathbf P(X_1=0)=A_S,
\qquad
\mathbf P(X_2\le 1)=A_S(1+\mu'_S)
\]
to the displayed `Decimal` working precision; the reported discrepancies were
between about `1e-79` and `1e-78`.

At `y = 100000`, exact and decimal mode agreed to all 18 displayed digits:

| y | mode | delta_S |
|---|---|---|
| 100000 | `exact` | 0.214351051159967077 |
| 100000 | `decimal` | 0.214351051159967077 |

So the auto/decimal path appears reliable for larger moderate cutoffs.

## Sample values for initial prime segments

The computed values for `S(y)` are:

| y | p_max | odd_primes | mode | lambda | lower | delta | upper | gap_to_delta_star |
|---|---|---|---|---|---|---|---|---|
| 50 | 47 | 12 | exact | 0.680884152079804254 | 0.000000000000000000 | 0.004858465238212487 | 0.143219337879814896 | 0.939072582687286617 |
| 100 | 97 | 22 | exact | 0.824145023415738668 | 0.000000000000000000 | 0.014317269421159360 | 0.196656421371189661 | 0.929613778504339744 |
| 200 | 199 | 43 | exact | 0.971441010945542305 | 0.000000000000000000 | 0.030821037020426070 | 0.252739991145462205 | 0.913110010905073035 |
| 1000 | 997 | 165 | exact | 1.221109739076738654 | 0.000000000000000000 | 0.074992573370327950 | 0.346662518379956602 | 0.868938474555171155 |
| 10000 | 9973 | 1226 | exact | 1.506206800070458379 | 0.000000000000000000 | 0.146991441743852218 | 0.447616344893177594 | 0.796939606181646886 |
| 100000 | 99991 | 9589 | decimal(auto) | 1.728428045843889414 | 0.000000000000000000 | 0.214351051159967077 | 0.519540932288691405 | 0.729579996765532028 |
| 1000000 | 999983 | 78495 | decimal(auto) | 1.910484700841741483 | 0.003843329841826272 | 0.273745365430549748 | 0.573462455422130162 | 0.670185682494949357 |
| 10000000 | 9999991 | 664576 | decimal(auto) | 2.064606044469448870 | 0.108321979056295522 | 0.325328064609900889 | 0.615483464144227452 | 0.618602983315598215 |

Observed behavior:

1. `delta_S(y)` is strictly increasing across the tested cutoffs.
2. This matches the monotonicity built into the model: adding a new prime adds
   an independent nonnegative increment in one coordinate or no increment, so
   the event \(\{X_1\ge 1,\ X_2\ge 2,\ X_4\ge 2\}\) is increasing.
3. The union-bound lower bound is far too weak at practical scales, but the
   exact DP is still nowhere near \(\delta_*\).

## Search to 10^7

The bounded search

```powershell
python erdos\689\computation\robust_density_dp.py --digits 18 search --y-max 10000000
```

did not reach the target. The last computed value was

\[
\delta_{S(10^7)} \approx 0.325328064609900889,
\]

still about `0.618603` below \(\delta_*\).

## Heuristic scale estimate

The exact DP is practical for moderate `y`, but it cannot enumerate the
astronomical range apparently needed for the threshold. The heuristic command

```powershell
python erdos\689\computation\robust_density_dp.py heuristic --calibrate-y 10000000
```

used
\[
\lambda(y):=\sum_{7\le p\le y}\frac1{p-1}
\]
at `y = 10^7`, where the script found

\[
\lambda(10^7)\approx 2.064606044469449,
\qquad
c_{\mathrm{est}}:=\lambda(y)-\log\log y\approx -0.715336549833820.
\]

With that calibration:

1. a one-coordinate two-hit scale
   \[
   \mathbf P(\mathrm{Poisson}(\lambda)\ge 2)=\delta_*
   \]
   occurs at
   \[
   \lambda\approx 4.604795657248062,
   \qquad
   \log_{10} y\approx 88.774528;
   \]
2. the full independent-Poisson crossover
   \[
   (1-e^{-\lambda})\bigl(1-e^{-\lambda}(1+\lambda)\bigr)^2=\delta_*
   \]
   occurs at
   \[
   \lambda\approx 5.504770866799179,
   \qquad
   \log_{10} y\approx 218.344692.
   \]

These are only heuristics, not rigorous thresholds, but they are consistent
with the bounded DP data: the desired density is far outside any computationally
practical initial segment.

## Bottom line

The 18-state DP is implemented and appears numerically stable:

1. exact rational mode works comfortably through at least `y = 100000`;
2. decimal mode matches exact mode on the overlap tested here;
3. `delta_{S(y)}` is monotone increasing for initial prime segments;
4. within the bounded range `y <= 10^7`, the density only reaches about
   `0.32533`, nowhere near `0.9439310479`.

So this computation gives reliable sample values and monotonic behavior, but it
does not produce a practical finite witness for \(\delta_S > \delta_*\).
