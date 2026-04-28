# Sub-Exceptional Family `(48,54,{64,72,81})`: Direct Two-Stream Density Argument

We work with `(a,b,T) = (48,54,{64,72,81})` and

`F(n) = #{x <= n : (48 | x or 54 | x), 64 !| x, 72 !| x, 81 !| x}`.

## 1. Quotient reduction kills the overlap

For the `48`-stream,

`Q_48(T) = Min{64/gcd(64,48), 72/gcd(72,48), 81/gcd(81,48)} = Min{4,3,27} = {3,4}`.

For the `54`-stream,

`Q_54(T) = Min{64/gcd(64,54), 72/gcd(72,54), 81/gcd(81,54)} = Min{32,4,3} = {3,4}`.

For the overlap stream `l = lcm(48,54) = 432`,

`Q_432(T) = Min{64/gcd(64,432), 72/gcd(72,432), 81/gcd(81,432)} = Min{1,1,3} = {1}`.

So the overlap contributes nothing at all. Every common multiple of `48` and `54` is killed by the tail.

Define

`A(y) := #{m <= y : 3 !| m, 4 !| m}`.

Then

`F(n) = A(floor(n/48)) + A(floor(n/54))`.

Equivalently, the survivors are exactly the disjoint union of `48u` and `54v` with `u,v` not divisible by `3` or `4`.

## 2. The admissible quotient set

Let `U := {m >= 1 : 3 !| m, 4 !| m}`.

Modulo `12`, this is `U mod 12 = {1,2,5,7,10,11}`. So every block of `12` consecutive integers contains exactly `6` admissible quotients.

The first few survivors are

`48,54,96,108,240,270,336,378,480,528,540,594,624,672,702,756,...`

and in particular `F(n)=4` for `108 <= n <= 239`.

## 3. A 540-window lemma

For every `n >= 540`,

`F(n) - F(n-540) <= 12`.

Proof:

- New `48`-stream survivors in `(n-540,n]` correspond to `u in U` inside `((n-540)/48, n/48]`, an interval of length `11.25`. So there are at most `12` possible integers, hence at most `6` admissible ones because any `12` consecutive integers contain exactly `6` elements of `U`.
- New `54`-stream survivors in `(n-540,n]` correspond to `v in U` inside `((n-540)/54, n/54]`, an interval of length `10`. Any `10` consecutive integers contain at most `6` elements of `U`.
- The streams are disjoint, so the total is at most `6 + 6 = 12`.

## 4. Global ratio bound for `n >= 240`

We claim `F(n)/n <= 1/45` for every `n >= 240`.

Base range `240 <= n < 780`:

From the survivor list,

- `F(n)=5` on `[240,269]`
- `F(n)=6` on `[270,335]`
- `F(n)=7` on `[336,377]`
- `F(n)=8` on `[378,479]`
- `F(n)=9` on `[480,527]`
- `F(n)=10` on `[528,539]`
- `F(n)=11` on `[540,593]`
- `F(n)=12` on `[594,623]`
- `F(n)=13` on `[624,671]`
- `F(n)=14` on `[672,701]`
- `F(n)=15` on `[702,755]`
- `F(n)=16` on `[756,779]`

The ratio is maximized at `n=270`, where `F(270)/270 = 6/270 = 1/45`.

Now let `n >= 780` and assume inductively that `F(m) <= m/45` for all `240 <= m < n`. Then

`F(n) <= F(n-540) + 12 <= (n-540)/45 + 12 = n/45`.

So `F(n)/n <= 1/45` for all `n >= 240`, with equality at `n=270`.

## 5. Consequence for the visible-slab `F(s)=4` range

For every `s` with `108 <= s <= 239`, we have `F(s)=4`, so

`2F(s)/s = 8/s >= 8/239 > 1/45`.

Now take any `m > s`.

- If `m < 240`, then `F(m)=4`, hence `F(m)/m = 4/m < 4/s < 8/s = 2F(s)/s`.
- If `m >= 240`, then `F(m)/m <= 1/45 < 8/239 <= 8/s = 2F(s)/s`.

Therefore every `s` in the bad visible slab `108 <= s <= 239` satisfies

`2F(s)/s > F(m)/m` for all `m > s`.

So the apparent obstruction at `(48,54,{64,72,81})` is not real. The forced-envelope failure is purely a bound failure.

## 6. Interpretation

This family does not want a free bound on the periodic corrections. It wants a coupled local-density statement:

- reduce to quotient streams
- exploit that the overlap stream is gone
- prove a finite-window inequality `F(n)-F(n-L) <= c` with `c/L` below the dangerous visible-slab slope

For this family the winning scale is `L = 540`, `c = 12`.
