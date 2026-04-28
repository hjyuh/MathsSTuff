# EP-488 Route 2 — Consecutive Triple `{q-2,q-1,q}`: Closed Form Extremizer (empirical)
## April 12, 2026

This note records the closed-form extremizing pair for the consecutive triple

`Q = {q-2, q-1, q}` with `q >= 5`,

as found by exhaustive window search and verified by exact counting at the stated `(n,m)`.

It is **not** (yet) a standalone proof that this is the *global* maximum over all `m>n>=q`; it is the sharpest available “|Q|=3 benchmark” supporting Route 2.

---

## Definitions

For `Q ⊂ Z_{>=2}` finite, define

- `A_Q(x) := #{1 <= n <= x : ∀d∈Q, d ∤ n}` (survivors),
- `O_Q(n,m) := 2*A_Q(n)/n - A_Q(m)/m` for `m>n>=max(Q)`.

Fix `q >= 5` and set `Q = {q-2,q-1,q}`.

Let `a := q-2` and `g := gcd(a,q) = gcd(q,2)` (so `g=1` if `q` odd, `g=2` if `q` even).

---

## Observed maximizer (window-exhaustive)

All searches I ran (e.g. `n` up to `10q`, `m` up to `O(q^2)` and larger) return:

- `n0 = 2q-5 = 2a-1`,
- `m0 = a^2/g = (q-2)^2/gcd(q,2)`,

as the maximizing pair.

This matches the “first run end” (`n0`) and an “lcm-edge” (`m0`) phenomenon analogous to the adjacent-pair case.

---

## Exact value at `(n0,m0)` (proved)

At `n0=2a-1`, we have `n0 < 2a`, so each modulus `a,a+1,a+2` contributes exactly one covered point ≤ `n0` (namely itself). Hence

- covered count `F(n0)=3`,
- survivors `A(n0)=n0-3=2a-4`,
- so `A(n0)/n0 = (2a-4)/(2a-1)`.

At `m0=a^2/g`, there are still no overlaps among the three progressions up to `m0` (since `m0` lies strictly below the smallest pairwise lcm among `{a,a+1,a+2}`), so the covered count is the sum of floors:

`F(m0) = floor(m0/a) + floor(m0/(a+1)) + floor(m0/(a+2))`.

Compute the floors:

- `floor(m0/a) = a/g`,
- `floor(m0/(a+1)) = a/g - 1`,
- `floor(m0/(a+2)) = a/g - 1` if `g=2` (i.e. `q` even),
- `floor(m0/(a+2)) = a-2` if `g=1` (i.e. `q` odd).

So:

- if `q` odd (`g=1`, `m0=a^2`): `F(m0)=a+(a-1)+(a-2)=3a-3`, hence `A(m0)=a^2-3a+3`;
- if `q` even (`g=2`, `m0=a^2/2`): `F(m0)=a/2+(a/2-1)+(a/2-1)=(3a-4)/2`, hence `A(m0)=(a^2-3a+4)/2`.

Therefore the exact operator value is:

- if `q` odd:
  `O(n0,m0) = 2*(2a-4)/(2a-1) - (a^2-3a+3)/a^2 = 1 - 6/(2q-5) + 3(q-3)/(q-2)^2`;
- if `q` even:
  `O(n0,m0) = 2*(2a-4)/(2a-1) - (a^2-3a+4)/a^2 = 1 - 6/(2q-5) + (3q-10)/(q-2)^2`.

This matches the value printed by `two_point_operator_tools.py`.

---

## Comparison to adjacent pair (proved)

From `route2-adjacent-pair-global-max.md`, for the adjacent pair `{q-1,q}` we have

`O_max({q-1,q}) = 1 - (4q-5)/((2q-3)(q-1)^2)`.

A direct (denominator-clearing) check shows that for every `q >= 5`,

`O(n0,m0) < O_max({q-1,q}) < 1`.

So if Route 2 can prove the remaining extremality step

> for every primitive `Q` with `|Q|>=3` and `max(Q)=q`, `max O_Q <= O(n0,m0)`,

then EP-488 follows immediately for all `|Q|>=3` (together with the proved singleton and pair cases).

