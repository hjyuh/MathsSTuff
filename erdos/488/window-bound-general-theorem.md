# General Window-Bound Theorem for Pair-Tail Systems

Let `(a,b|T)` be a primitive pair-tail system and let `l = lcm(a,b)`.

Write the quotient-tail decomposition in the exact form

`F(n) = A_{Q_a}(floor(n/a)) + A_{Q_b}(floor(n/b)) - A_{Q_l}(floor(n/l))`,

where for any finite set `Q` of positive integers,

`A_Q(y) := #{m <= y : q !| m for every q in Q}`.

Let `rho_Q` denote the `Q`-free density, so

`A_Q(y) = rho_Q y + c_Q(y)`

with `c_Q` periodic and bounded. Then

`delta = rho_{Q_a}/a + rho_{Q_b}/b - rho_{Q_l}/l`.

The purpose of this note is to state exactly what the direct window method gives in general, and exactly where it stops.

## 1. Window-count operators on quotient tails

For a quotient-tail set `Q` and an integer `k >= 0`, define

`N_Q^+(k) := max_t (A_Q(t) - A_Q(t-k))`

and

`N_Q^-(k) := min_t (A_Q(t) - A_Q(t-k))`.

These are the maximal and minimal numbers of `Q`-free integers in an interval of `k` consecutive quotient slots.

Because `A_Q(y) = rho_Q y + c_Q(y)` with bounded periodic `c_Q`, we have

`N_Q^+(k) = rho_Q k + O_Q(1)`,

`N_Q^-(k) = rho_Q k + O_Q(1)`.

More explicitly, if

`osc(Q) := max c_Q - min c_Q`,

then

`rho_Q k - osc(Q) <= N_Q^-(k) <= rho_Q k <= N_Q^+(k) <= rho_Q k + osc(Q)`.

## 2. General window upper bound

Fix any integer window length `L >= 1`.

For each divisor stream `d in {a,b,l}`, set

`k_d^-(L) := floor(L/d)`,

`k_d^+(L) := ceil(L/d)`.

Then for every `n`,

`floor(n/d) - floor((n-L)/d)`

lies between `k_d^-(L)` and `k_d^+(L)`.

Therefore the quotient-tail decomposition gives the pointwise bound

`F(n) - F(n-L) <= c(L)`,

where

`c(L) := N_{Q_a}^+(k_a^+(L)) + N_{Q_b}^+(k_b^+(L)) - N_{Q_l}^-(k_l^-(L))`.

This is the direct general analogue of the `(48,54,{64,72,81})` bound `F(n)-F(n-540) <= 12`.

### Proof

The `a`-stream contribution to `F(n)-F(n-L)` is

`A_{Q_a}(floor(n/a)) - A_{Q_a}(floor((n-L)/a))`,

which counts `Q_a`-free quotient integers in an interval of length either `floor(L/a)` or `ceil(L/a)`. Hence it is at most `N_{Q_a}^+(k_a^+(L))`.

The same argument bounds the `b`-stream by `N_{Q_b}^+(k_b^+(L))`.

The overlap contribution is subtracted, and its quotient interval has length at least `floor(L/l)`, so it is at least `N_{Q_l}^-(k_l^-(L))`. Subtracting it gives the claimed upper bound.

## 3. Asymptotic form of the window constant

Define

`alpha(L) := c(L)/L`.

Then

`alpha(L) = delta + O(1/L)`.

Indeed,

`N_{Q_a}^+(k_a^+(L)) = rho_{Q_a} * (L/a) + O(1)`,

`N_{Q_b}^+(k_b^+(L)) = rho_{Q_b} * (L/b) + O(1)`,

`N_{Q_l}^-(k_l^-(L)) = rho_{Q_l} * (L/l) + O(1)`.

After dividing by `L`, this gives `alpha(L) -> delta` as `L -> infinity`.

So the window method controls the growth rate of `F` at slope `delta + o(1)` without using any envelope comparison.

## 4. Inductive propagation theorem

Let `S` be any cutoff. Assume that for some `L >= 1` and some `alpha`, we have

1. `F(n) - F(n-L) <= alpha * L` for every `n >= S+L+1`.
2. `F(m)/m <= alpha` for every `S < m <= S+L`.

Then

`F(n)/n <= alpha` for every `n > S`.

### Proof

Induct on `n > S+L`. For the induction step,

`F(n) <= F(n-L) + alpha * L <= alpha*(n-L) + alpha*L = alpha*n`.

Thus the ratio bound propagates from one base strip of width `L` to all larger `n`.

Applied with `alpha = alpha(L) = c(L)/L`, this yields a complete non-envelope closure mechanism:

- prove `2F(s)/s > alpha(L)` on the visible slab,
- verify `F(m)/m <= alpha(L)` on the first post-slab strip of width `L`,
- deduce `F(m)/m <= alpha(L)` for every larger `m`.

## 5. What the window method does prove

The method gives the following exact reduction.

> Theorem (Window-bound reduction).
> For every primitive pair-tail system `(a,b|T)` and every `L >= 1`, define `c(L)` as above. If
>
> - `2F(s)/s > c(L)/L` for every visible-slab residue `s`, and
> - `F(m)/m <= c(L)/L` for every `m` in the first post-slab strip `S_vis < m <= S_vis + L`,
>
> then the split inequality holds for every visible-slab residue `s` against every `m > s`.

This is the genuine generalization of the `540`-window proof in the sub-exceptional family.

## 6. Where the method breaks if one tries to avoid the base strip

The tempting stronger claim is:

- choose a canonical period window `L_0` so that `F(n)-F(n-L_0) = delta * L_0` exactly,
- conclude `F(m)/m <= delta` for all large `m`.

This is false.

Exact periodic-window increments control the average slope, not the pointwise ratio. Positive periodic corrections survive.

To see the obstruction concretely, return to the model family `(48,54,{64,72,81})`.

There, the canonical exact-period window is

`L_0 = lcm(48*lcm(Q_48), 54*lcm(Q_54), 432*lcm(Q_432)) = lcm(576,648,432) = 5184`.

For this window,

`F(n) - F(n-5184) = delta * 5184 = 102`

exactly, so

`delta = 102/5184 = 17/864`.

But

`F(270)/270 = 6/270 = 1/45 > 17/864 = delta`.

So even in the family that motivated the window method, the exact equality `c/L = delta` does **not** upper-bound `F(m)/m` beyond the slab.

This is the exact point where the naive generalization fails.

The window method therefore does **not** eliminate the need for a first-strip check. What it eliminates is the need for envelope optimization over all later residues.

## 7. Final verdict

The direct window idea generalizes, but only in the following precise form:

- it produces a computable one-sided growth constant `alpha(L) = c(L)/L`,
- it propagates a ratio bound from one post-slab strip of width `L` to all larger `m`,
- and `alpha(L)` tends to `delta` as `L` grows.

What it does **not** do by itself is prove `F(m)/m <= delta`, or even `F(m)/m <= alpha(L)`, without an initial strip verification.

So the correct general theorem is the window-bound reduction above.
The exact obstruction to a fully automatic proof is the uncontrolled positive periodic correction on the first strip after the slab.
