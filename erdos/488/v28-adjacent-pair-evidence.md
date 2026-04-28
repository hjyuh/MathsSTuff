# EP-488 v28 — Adjacent-Pair Evidence (Two-Point Operator)
## April 12, 2026

This note records a computational pattern that strengthens the v28 “singleton extremality” picture:

> Among primitive multi-modulus antichains with fixed `q = max(Q)` and `|Q| ≥ 2`,
> the worst cases appear to be the adjacent pair `Q = {q-1, q}`.

If this can be proved, EP-488 reduces further: we only need to show that even the adjacent pair cannot beat the singleton `Q={q}`.

---

## Definitions (v28)

- `A_Q(x) := #{1 ≤ n ≤ x : ∀q∈Q, q ∤ n}` (unsieved survivors)
- `O_Q(n,m) := 2*A_Q(n)/n − A_Q(m)/m` (two-point operator)

The v28 singleton extremality conjecture is:

> For all primitive `Q` and all `m>n ≥ max(Q)=q`,
> `O_Q(n,m) ≤ 1 − 1/(q(2q−1))`,
> with equality for the singleton `Q={q}` at `(n,m)=(2q−1,2q)`.

---

## New tooling

Script: `C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py`

It computes exact maxima over finite windows using an `O(X)` suffix-min trick and (optionally) the run-end restriction.

Examples:

- `python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py maxO --Q 165`
- `python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py maxO --Q 164,165`
- `python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py worstPair --q 200`

---

## Empirical pattern 1: worst primitive pair (r,q) is always (q−1,q)

For each `q` in `[6,60]`, scanning all primitive pairs `Q={r,q}` with:

- `n ∈ [q, 10q]`, `m ∈ [n+1, 10q]`,
- and using the run-end restriction,

the worst pair was always `Q={q−1,q}`.

This matches an earlier faster scan up to `q=200` with a smaller window.

Repro (example):

`python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py worstPair --q 60`

---

## Empirical pattern 2 (corrected): adjacent-pair max is an O(q²) “lcm-edge” configuration

On the *short window* `m ≤ 10q`, the adjacent pair `Q = {q−1,q}` maximizer does occur at the “double-hit”

- `(n,m) = (2q−3, 2q)` with value `1 − 6/(q(2q−3))`,

as recorded above.

But when the search window is extended to `m = O(q²)`, a **larger** maximizer appears at an “lcm-edge” point:

- `(n,m) = (2q−3, (q−1)²)`,
- equivalently `m = lcm(q−1,q) − (q−1) = q(q−1) − (q−1)`,
- and the closed form is

`O_{ {q−1,q} }(2q−3, (q−1)²) = 1 − (4q−5)/((2q−3)(q−1)²)`.

This holds in every check I ran (e.g. q=20,25,50,60,200,500) and matches the argmax returned by `maxO` as soon as the window includes `m=(q−1)²`.

Repro (example):

`python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py maxO --Q 49,50 --n-mult 10 --m-mult 100`

Interpretation: `m=(q−1)²` is the last multiple of `q−1` before the first overlap at `lcm(q−1,q)=q(q−1)`, and empirically it is where `A(m)/m` is minimized.

---

## Why this helps: a corrected “multi-modulus” target bound

For every `q ≥ 2`:

`1 − (4q−5)/((2q−3)(q−1)²) < 1 − 1/(q(2q−1))`

so **any universal bound of the form**

> for `|Q| ≥ 2`, `O_Q(n,m) ≤ 1 − (4q−5)/((2q−3)(q−1)²)`

would immediately imply the v28 singleton extremality conjecture, hence EP-488.

This reframes the last 6% as a *purely combinatorial extremal statement*:

> For fixed `q=max(Q)`, adding any additional modulus beyond `{q}` cannot make `O_Q` exceed the singleton resonance; in fact, among `|Q|≥2` the adjacent pair `{q−1,q}` is extremal.

---

## Suggested proof direction (non-rigorous sketch)

1. Use the run-end extremizer lemma to restrict to run boundaries.
2. Show that any configuration achieving `O` within `O(1/q^2)` of `1` forces:
   - `Q` has exactly two elements (else too many early covers),
   - the second element must be `q−1` (largest possible “delayed” extra modulus),
   - and the maximizing pair is forced to be the “lcm-edge” `(2q−3,(q−1)²)` for `q` sufficiently large.
3. Compute the adjacent-pair maximum explicitly and compare to the singleton maximum.

The computations above are consistent with this narrative.
