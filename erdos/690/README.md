# EP690: kth Prime Factor Density Unimodality

## Status

Problem page: https://www.erdosproblems.com/690

Let `d_k(p)` be the density of integers whose `k`th smallest distinct prime
factor is `p`. Erdős asked whether the sequence `d_k(p)`, over primes `p`, is
unimodal for fixed `k`.

Cambie (2025) proves:

- `d_k(p)` is unimodal for `k = 1,2,3`;
- `d_k(p)` is not unimodal for `4 <= k <= 20`.

The remaining interesting target is therefore the classification

```text
d_k(p) is unimodal iff k <= 3.
```

Equivalently, prove non-unimodality for every `k >= 4`, or at least for all
sufficiently large `k`.

## Exact Formula

Let the primes be

```text
p_1 = 2 < p_2 = 3 < ...
```

For a fixed `k`, put `r = k - 1`. For index `i`, define

```text
A_i = prod_{j<i} (1 - 1/p_j),
x_j = 1/(p_j - 1),
E_r(i) = e_r(x_1,...,x_{i-1}).
```

Then

```text
d_k(p_i) = A_i E_r(i) / p_i.
```

The adjacent ratio is

```text
d_k(p_{i+1}) / d_k(p_i)
  = (p_i - 1 + R_r(i)) / p_{i+1},
```

where

```text
R_r(i) = E_{r-1}(i) / E_r(i).
```

Thus the sequence increases at `p_i -> p_{i+1}` exactly when

```text
R_r(i) > g_i + 1,
g_i = p_{i+1} - p_i.
```

So EP690 reduces to comparing a smooth threshold `R_r(i)-1` with the irregular
prime-gap sequence `g_i`.

## Low-Compute Plan

### Phase 1: Reproduce Cambie and build diagnostics

Goal: independent, exact reproduction of `k <= 20`, plus extension as far as is
cheap.

Tasks:

1. Implement exact rational or high-precision recurrence for `E_r(i)`.
2. Use the ratio criterion above rather than density values directly.
3. Record sign patterns of

   ```text
   S_r(i) = R_r(i) - (g_i + 1).
   ```

4. Verify unimodality for `k=1,2,3`.
5. Verify non-unimodality for `4 <= k <= 20`.
6. Extend numerically to larger `k` as scouting data, but do not treat finite
   verification as a proof.

### Phase 2: Study the threshold `R_r(i)`

Goal: get clean analytic bounds for the threshold in the region where the
maximum occurs.

Tasks:

1. Prove monotonicity or controlled variation of `R_r(i)`.
2. Obtain asymptotics for `R_r(i)` via the saddle point of

   ```text
   prod_{j<i} (1 + z/(p_j - 1)).
   ```

3. Identify the main window where `R_r(i)` is comparable to prime gaps. Erdős'
   heuristic says the maximum occurs around

   ```text
   p = exp((1+o(1))k).
   ```

4. Derive usable inequalities of the form

   ```text
   R_r(i) = (1+o(1)) log p_i
   ```

   or the correct refined version in the transition window.

### Phase 3: Convert prime-gap oscillation into non-unimodality

Goal: prove a sign pattern `+ - +` or `- + -` for `S_r(i)`.

Potential routes:

1. Conditional theorem:

   Prove that if, near `x = exp(k)`, there is one prime gap exceeding
   `R_r(i)-1` and a later/earlier gap below `R_r(i)-1` before `R_r(i)` changes
   too much, then `d_k(p)` is not unimodal.

2. Known-gap theorem:

   Combine threshold control with known results on large prime gaps and small
   prime gaps. This may only prove infinitely many `k`, because current prime
   gap theorems may not place both gap types in every required window.

3. Meta-result:

   State a clean prime-gap hypothesis that implies non-unimodality for all
   sufficiently large `k`. This would answer Thomas Bloom's forum question by
   identifying the exact mainstream prime-gap input needed.

### Phase 4: Try for unconditional all-large-`k`

This is the hard step. It likely needs a theorem guaranteeing enough local
prime-gap oscillation around the scale where `R_r(i)` is close to the typical
gap size.

Known tools to audit:

- Baker-Harman-Pintz prime gaps;
- Maynard/Tao bounded gaps;
- Ford-Green-Konyagin-Maynard-Tao large gaps;
- short interval prime existence;
- average prime-gap distribution results strong enough to force both above- and
  below-threshold gaps in the transition window.

## First Deliverable

Produce a short note:

```text
EP690 reduced to prime-gap threshold crossings
```

containing:

1. the exact formula for `d_k(p_i)`;
2. the adjacent-ratio criterion;
3. a reproduction table for Cambie's `k <= 20`;
4. a plot/table of threshold crossings for larger `k`;
5. a conditional theorem showing precisely what prime-gap oscillation would
   imply non-unimodality for all large `k`.

This is low-compute and gives a concrete mathematical interface, even if the
full unconditional closure remains hard.
