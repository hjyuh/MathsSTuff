# EP-488 v29: the u_T Target Lemma is false (explicit counterexample)
## April 12, 2026

Recall the v29 "u_T target lemma" claim:

> For any finite `T ⊂ Z_{>=2}`, define
> `u_T(x) = #{ 1 <= k <= x : for all t in T, t ∤ k }`.
> Claim: for all integers `b >= a >= 1`,
> `u_T(b)/b <= 2 * u_T(a)/(a+1)`.

This statement is **false**.

---

## Smallest clean counterexample

Take `T = {2, 3}`, `a = 4`, `b = 7`.

- `u_T(4) = 1` since among `{1,2,3,4}` only `1` is not divisible by `2` or `3`.
- `u_T(7) = 3` since among `{1,2,3,4,5,6,7}` the survivors are `{1,5,7}`.

Then

- LHS = `u_T(7)/7 = 3/7 ≈ 0.428571`,
- RHS = `2*u_T(4)/(4+1) = 2/5 = 0.4`,

so `3/7 > 2/5` and the inequality fails.

Equivalently, the best constant `C` in
`u_T(b)/b <= C * u_T(a)/(a+1)`
for this example satisfies `C >= (3/7)/(1/5) = 15/7 ≈ 2.142857`.

---

## Reproduction

The script `C:\\Users\\z20ma\\OneDrive\\Documents\\!math\\erdos\\488\\uT_target_lemma_check.py` finds this immediately, e.g.

`python C:\\Users\\z20ma\\OneDrive\\Documents\\!math\\erdos\\488\\uT_target_lemma_check.py one --T 2,3 --Bmax 50`

prints the violating pair `(a,b) = (4,7)`.

