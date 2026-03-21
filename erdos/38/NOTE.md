# Erdős Problem #38 — `Z/8` Spectral Feasibility Checkpoint

This note packages the next finite harmonic test suggested by the current state summary.

## Scalar `Z/8` model

Work with an even positive-definite class function on `Z/8`,

```text
rho(r) = w0
       + w1 cos(pi r/4)
       + w2 cos(pi r/2)
       + w3 cos(3 pi r/4)
       + w4 cos(pi r),
```

with `wj >= 0` and `w0 + w1 + w2 + w3 + w4 = 1`.

For a half-density sign model, normalized correlation `rho` corresponds to local cost

```text
m(r) = (1 - rho(r)) q / 4.
```

So the threshold `m(r) <= delta q` is equivalent to `rho(r) >= eta`, where

```text
eta = 1 - 4 delta.
```

## Test 1: odd-only sanity check

Impose

```text
rho(1) >= eta,
rho(3) <= -eta.
```

The optimum is

```text
eta* = 1 / sqrt(2),
```

attained by the concentrated odd spike `w1 = 1`, all others `0`. This reproduces the already-frozen odd-family LP outcome.

## Test 2: odd + even scalar feasibility

The cleanest full scalar mod-8 test is

```text
rho(1) >= eta,
rho(2) >= eta,
rho(4) >= eta,
rho(3) <= -eta.
```

Interpretation:

- `rho(1) >= eta` asks for `F_0`-type low cost,
- `rho(3) <= -eta` asks for the opposite odd family to be expensive,
- `rho(2), rho(4) >= eta` enforce genuine even-class support in the same scalar profile.

The LP optimum is

```text
eta_scalar = 1 / (1 + 2 sqrt(2)) ~= 0.261203874964,
delta_scalar = (1 - eta_scalar) / 4 ~= 0.184699031259.
```

One optimizer is

```text
w1 = sqrt(2) / (1 + 2 sqrt(2)),
w0 = w4 = (1 + sqrt(2)) / (2 + 4 sqrt(2)),
w2 = w3 = 0.
```

So the scalar route cannot reach the full `delta > 1/6` window. It already dies for

```text
1/6 < delta < 0.184699031259...
```

and only survives in the narrow strip

```text
0.184699031259... <= delta < 3/16.
```

### Short proof of the scalar bound

Let

```text
b = w1 + w3,
Delta = w1 - w3.
```

Then

```text
rho(1) - rho(3) = sqrt(2) Delta,
rho(4) = 1 - 2b.
```

The odd constraints force `Delta >= sqrt(2) eta`, hence `b >= Delta >= sqrt(2) eta`. The even constraint at `r = 4` gives

```text
eta <= rho(4) = 1 - 2b <= 1 - 2 sqrt(2) eta,
```

so

```text
(1 + 2 sqrt(2)) eta <= 1.
```

This proves `eta <= 1 / (1 + 2 sqrt(2))`. Equality is attained by the optimizer above.

## Why `r = 4` matters

If one weakens the scalar test by dropping the `rho(4) >= eta` requirement and keeps only

```text
rho(1) >= eta,
rho(2) >= eta,
rho(3) <= -eta,
```

then the optimum jumps to

```text
eta = sqrt(2) - 1 ~= 0.414213562373,
delta = 1/2 - sqrt(2)/4 ~= 0.146446609407.
```

That falls **below** `1/6`. So the scalar obstruction above `1/6` is not coming from the even classes in a vague averaged sense. It is specifically the `r = 4` class that forces the bottleneck. Any successful mixed-window theorem that tries to kill the surviving strip should therefore be expected to use the `4 mod 8` geometry in an essential way.

## Test 3: plain `2 x 2` PSD label model

If one only asks for a label-aware positive-definite kernel without any mixed `P/Q` coupling, the model is too loose.

A concentrated block-diagonal witness is:

```text
M_1 = M_7 = (1/2) E_oo,
M_4 = E_ee,
all other M_k = 0.
```

This gives

```text
rho_oo(r) = cos(pi r / 4),
rho_ee(r) = (-1)^r,
rho_oe(r) = 0.
```

Consequences:

- the odd label attains margin `1 / sqrt(2)` on `F_0` versus `F_2`,
- the even label attains margin `1` on the even classes,
- therefore the uncoupled `2 x 2` PSD model is feasible for every `eta <= 1 / sqrt(2)`.

So plain label-awareness does **not** kill the route. It merely repackages the obvious concentrated atoms.

## Interpretation

The finite harmonic picture now looks like this:

1. Scalar `Z/8` feasibility already kills the one-profile odd+even route on most of the target interval above `1/6`.
2. Plain `2 x 2` PSD survives trivially by separating the odd spike and parity atoms across labels.
3. Therefore the next real bottleneck is not “scalar vs matrix PSD” by itself. It is `2 x 2` PSD **plus actual mixed-window `P/Q` constraints** on the off-diagonal interactions.

That is the sharp next fork:

- either the mixed `P/Q` inequalities destroy the block-diagonal witness, which would be a real theorem-level negative result,
- or they do not, in which case the current spectral route is probably too weak to reach a genuine solution.
