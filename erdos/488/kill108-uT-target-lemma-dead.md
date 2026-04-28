# KILL #108 — u_T Target Lemma is FALSE
## April 12, 2026

This kills the v29 “u_T target lemma” as stated.

---

## Statement (v29)

For finite `T ⊂ Z_{>=2}`, define

`u_T(x) = #{ 1 <= k <= x : ∀t∈T, t ∤ k }`.

Claim (v29): for all integers `b >= a >= 1`,

`u_T(b)/b <= 2 * u_T(a)/(a+1)`.

---

## Counterexample (small, primitive)

Take `T = {2,3}` (primitive antichain), `a=4`, `b=7`.

- `u_T(4) = 1` (only `{1}` survives)
- `u_T(7) = 3` (survivors `{1,5,7}`)

So

- `u_T(7)/7 = 3/7 ≈ 0.428571`
- `2*u_T(4)/(4+1) = 2/5 = 0.4`

Violation: `3/7 > 2/5`.

Repro:

`python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\uT_target_lemma_check.py one --T 2,3 --Bmax 50`

---

## Lift: monotonicity-under-adjoining fails (even with fixed max(q))

The lemma was being used to prove that adding a modulus `r` to a set `S ⊃ {q}`
forces the two-point operator to decrease pointwise, via the incremental
coverage count

`D(x) = A_S(x) - A_{S∪{r}}(x)`.

But the same lattice effect produces explicit failures of the required
two-point inequality for `D`.

Example:

- Start with primitive `S = {10,21,77}` and adjoin `r=35` (still primitive).
- For `s ∈ S`, the induced sieve moduli are `t_s = lcm(r,s)/r = s/gcd(r,s)`,
  giving `T = {2,3,11}`.
- `u_T(4)=1`, `u_T(7)=3` still holds for `T={2,3,11}` (since `11>7`).

Pick `n=174` and `m=245` so that:

- `floor(n/35)=4`, `floor(m/35)=7`,
- and `n` is maximal / `m` minimal in those blocks (worst-case for the
  inequality).

Then `D(n)=1`, `D(m)=3`, so:

- `2*D(n)/n = 2/174 ≈ 0.011494`
- `D(m)/m = 3/245 ≈ 0.012245`

Hence `2*D(n)/n < D(m)/m`, so adding `r` can *increase* `O_Q(n,m)` at that
pair.

Concrete check (exact rationals):

- `O_{S}(174,245) = 5944/7105 ≈ 0.836594`
- `O_{S∪{35}}(174,245) = 17848/21315 ≈ 0.837345` (increased)

---

## Script

`C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\uT_target_lemma_check.py`

Use `scan` mode to mine more violations for primitive `T ⊂ [2,N]` on a finite
window.

