# EP-488 v30 Path 1: the D(x) two-point inequality (open)
## April 12, 2026

This note isolates Path 1 from Unified Truth v30.

---

## Definitions

Let `Q ⊂ Z_{>=2}` be a finite primitive modulus antichain, and let `q = max(Q)`.

Define the survivor count

`A_Q(x) := #{ 1 <= n <= x : for all d in Q, d does NOT divide n }`.

For the singleton `{q}`, write

`A_q(x) := A_{ {q} }(x) = x - floor(x/q)`.

Define the extra coverage beyond the singleton:

`D(x) := A_q(x) - A_Q(x)`.

Equivalently,

`D(x) = #{ t <= x : q does NOT divide t, and t is divisible by some r in Q \\ {q} }`.

---

## Target inequality (equivalent to singleton dominance)

For all integers `m > n >= q`, prove:

`D(m)/m <= 2 * D(n)/n`.

Reason: the singleton dominance inequality

`O_Q(n,m) <= O_{ {q} }(n,m)`

for

`O_Q(n,m) = 2*A_Q(n)/n - A_Q(m)/m`

is equivalent (after rearranging) to

`2*(A_q(n)-A_Q(n))/n >= (A_q(m)-A_Q(m))/m`,

which is exactly `2*D(n)/n >= D(m)/m`.

This avoids the killed v29 `u_T` lemma because `D(x)` *explicitly excludes multiples of q*.

---

## Evidence / tooling

Script:

`C:\\Users\\z20ma\\OneDrive\\Documents\\!math\\erdos\\488\\dx_two_point_check.py`

Examples:

- Scan all primitive `Q ⊂ [2,15]` (on the finite window `q <= n < m <= 30q`):
  `python C:\\Users\\z20ma\\OneDrive\\Documents\\!math\\erdos\\488\\dx_two_point_check.py scan --N 15 --Bmult 30 --min-size 2 --limit 10`

No violations have been observed so far in the project's ad hoc tests; this script makes the check reproducible.

---

## What is still missing

A proof of the two-point bound `D(m)/m <= 2*D(n)/n` for all primitive antichains `Q`
is currently not known.

If proved, this implies singleton dominance for all `Q`, hence EP-488 immediately.

