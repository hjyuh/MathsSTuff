# Erdos 509 - Degree 2 Proof and a Cubic Cassini Reduction

## Setup

For a monic polynomial `f`, write

`E(f) = { z in C : |f(z)| <= 1 }`

and

`tau(f) = inf { sum r_j : E(f) is covered by closed disks of radii r_j }`.

The global problem asks whether `tau(f) <= 2` for every monic polynomial.

## Degree 2: a complete elementary proof

Let

`f(z) = (z-a)(z-b)`

be monic of degree `2`. Then

`E(f) = { z : |z-a||z-b| <= 1 }`.

This is the usual Cassini oval with foci `a,b`.

### Covering argument

If `z` is outside both unit disks `D(a,1)` and `D(b,1)`, then

`|z-a| > 1` and `|z-b| > 1`,

so

`|f(z)| = |z-a||z-b| > 1`.

Therefore

`E(f) subset D(a,1) union D(b,1)`.

Hence

`tau(f) <= 1 + 1 = 2`.

That proves the conjectured bound for every monic quadratic.

### Remarks

1. If `a=b`, then `E(f) = D(a,1)` and in fact `tau(f) = 1`.
2. After translation and rotation one may write `f(z) = z^2 - s^2`, so
   `E(f) = { |z-s||z+s| <= 1 }`; the proof above says the Cassini oval is always covered by the two focal unit disks.
3. This argument is completely different from Pommerenke's connected-case proof:
   it does not use schlicht maps, the area theorem, or connectedness.

## Comparison with Cartan and Pommerenke

For arbitrary degree:

- Cartan gives `tau(f) <= 2e`.
- Pommerenke gives `tau(f) <= pi*sqrt(e)/2 ~= 2.59`.
- Pommerenke also proves `tau(f) <= 2` when `E(f)` is connected.

For degree `2`, the factorization above gives `tau(f) <= 2` directly, whether the Cassini oval is connected or disconnected. So in degree `2`, the conjectured sharp constant follows from the product structure alone.

## Degree 3: what the same idea gives

Let

`f(z) = (z-a)(z-b)(z-c)`.

The trivial root-by-root cover is

`E(f) subset D(a,1) union D(b,1) union D(c,1)`,

so `tau(f) <= 3`. That is too weak.

### Why the naive factorization split stalls at 3

Fix one root `a`. If `|z-a| >= r` and `z in E(f)`, then

`|(z-b)(z-c)| <= 1/r`.

Applying the degree-2 argument to the quadratic factor gives a cover of the remaining set by two disks of total radius `2/sqrt(r)`. Thus

`tau(f) <= r + 2/sqrt(r)`.

The right-hand side is minimized at `r=1`, and the minimum is exactly `3`. So pure one-root-plus-quadratic factorization does not prove the cubic case.

## A better cubic Cassini reduction

Group two roots together. Let `m = (b+c)/2`, and let `s = |b-c|/2`. After rotating about `m`, the pair is `m-s, m+s`.

For any `z`, put `w = z-m`. Then

`|(z-b)(z-c)| = |(w-s)(w+s)| = |w^2 - s^2|`.

So if `|z-m| = |w| >= S >= s`, then

`|(z-b)(z-c)| >= ||w|^2 - s^2| >= S^2 - s^2`.

Therefore, if also `|z-a| >= R`, then

`|f(z)| = |z-a| |(z-b)(z-c)| >= R (S^2 - s^2)`.

Hence we get the explicit two-disk cover

`E(f) subset D(a,R) union D(m,S)`

whenever

`S >= s` and `R (S^2 - s^2) >= 1`.

Taking `R = 1/(S^2 - s^2)` gives

`tau(f) <= S + 1/(S^2 - s^2)`.

This improves the naive cubic bound `3`, and it depends on the actual root geometry through the half-separation `s` of the chosen pair.

### Concrete consequence

Let

`T_s(S) = S + 1/(S^2 - s^2)` for `S > s`.

Numerically, `min_S T_s(S) <= 2` for

`s <= 0.5416337578...`

that is, whenever some pair of roots has distance

`|b-c| <= 1.0832675156...`.

So any monic cubic with a root pair this close already satisfies `tau(f) <= 2` by an explicit two-disk covering argument.

## What remains open for degree 3

The midpoint-disk reduction is the cleanest elementary improvement I found, but it does not settle all cubics. For more spread-out root configurations, the function

`S + 1/(S^2 - s^2)`

can stay above `2`, and then one needs extra information beyond bare factorization:

- the position of the third root relative to the pair,
- the actual location of the cubic critical points,
- or a genuinely analytic input of Pommerenke type.

So:

- degree `2` is completely done by the Cassini/factorization cover;
- degree `3` admits a useful explicit reduction, but I do not have a full proof of `tau(f) <= 2` for every cubic from this method alone.
