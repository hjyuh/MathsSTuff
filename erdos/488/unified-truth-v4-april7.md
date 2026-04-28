# EP-488: Unified Truth v4 — Prove S_1 ≥ Σ E_j
## April 7, 2026 — For all models

---

## THE PROBLEM

Erdős Problem 488: G(m) < 2·G(n) for all m > n ≥ max(A), primitive A.

---

## THE PROOF IS ONE INEQUALITY AWAY

### Proved:
1. ✅ Convexity: extrema in [M, 10M]
2. ✅ F(x) = Σ L_j(⌊x/a_j⌋) (positive decomposition)
3. ✅ F(m)/F(n) = Σ w_j R_j (weighted average, Σw_j = 1)
4. ✅ Self-funding: s_j ≤ 3 → E_j ≤ 0 (no compensation needed)
5. ✅ 29-kernel classification: bad layers have K ⊇ {2,3}, all prime, L_K(s)=1
6. ✅ First layer pays EACH bad child: S_1 ≥ 28a_j > 17a_j ≥ E_j

### The one remaining step:
7. ❓ **S_1 ≥ Σ_{bad} E_j** (first layer pays all bad children collectively)

### If step 7 is proved:
8. Total budget = S_1 + Σ_{good,j≥2} S_j - Σ_{bad} E_j ≥ S_1 - Σ E_j ≥ 0.
   So 2mF(n) - nF(m) > 0, i.e. G(m) < 2G(n). EP-488 proved. ✎

---

## WHAT WE KNOW ABOUT S_1

The first layer (a_1 = min A) has no obstructions: L_1(y) = y.

S_1 = 2m·⌊n/a_1⌋ - n·⌊m/a_1⌋

From the first-layer theorem proof:
  S_1 ≥ m(n/a_1 - 2)

Key facts about a_1:
- For EACH bad child j: ∃ element a_r ∈ A with a_r/gcd(a_r,a_j) = 2
  and a_r ≤ 2a_j/3. Since a_1 ≤ a_r: a_1 ≤ 2a_j/3.
- For EACH bad child j: a_j > M/2 (compact) and a_j ≤ n/4 (since s ≥ 4).
- Therefore: a_1 ≤ 2·(n/4)/3 = n/6. So n/a_1 ≥ 6.
- S_1 ≥ m(6-2) = 4m.

More precisely: a_1 ≤ 2·min(bad a_j)/3. If there are multiple bad
layers, a_1 ≤ 2·min_j(a_j)/3 where min is over ALL bad a_j.

---

## WHAT WE KNOW ABOUT Σ E_j

Each bad child has:
- E_j ≤ 17a_j (child excess bound)
- a_j ∈ (M/2, M] (compact)
- s_j ∈ [4, 19], t_j ∈ [7, 20]
- K_j ⊇ {2,3}, L_K(s_j) = 1

Let B = number of bad layers, and let a_{j_1} < a_{j_2} < ... < a_{j_B}
be the bad elements. All are in (M/2, M].

Σ E_j ≤ 17·Σ a_{j_i} ≤ 17·B·M

Meanwhile S_1 ≥ 4m ≥ 4n (since m > n).

So we need: 4n ≥ 17·B·M, i.e., B ≤ 4n/(17M).
Since n can be up to 10M: B ≤ 40/17 ≈ 2.35, so B ≤ 2.

But B can be 2 (verified counterexample). And potentially more for
larger sets. So this simple bound is NOT sufficient for B ≥ 3.

---

## THE SELF-REGULATING PROPERTY

More bad layers → more ancestor elements → smaller a_1 → larger S_1.

Each bad layer j needs:
- A 2-ancestor: element with quotient 2 to a_j
- A 3-ancestor: element with quotient 3 to a_j
- These ancestors are ≤ 2a_j/3 < 2M/3

So each bad layer requires AT LEAST 2 supporting elements in A.
If B bad layers have DISJOINT ancestor sets: |A| ≥ B + 2B = 3B.
The ancestors are all ≤ 2M/3, so a_1 ≤ 2M/3.

But the ancestors might be SHARED. In the {6,8,9,20,21} example:
- Layer 20: 2-ancestor is 8 (8/gcd(8,20)=2), 3-ancestor is 6 (6/gcd(6,20)=3)
- Layer 21: 2-ancestor is 6 (6/gcd(6,21)=2), 3-ancestor is 9 (9/gcd(9,21)=3)
Element 6 is SHARED (2-ancestor for 21, 3-ancestor for 20).

---

## THE KEY QUESTION

Can we show that S_1 = m(n/a_1 - 2) grows faster than Σ E_j ≤ 17·B·M
as B increases?

S_1 depends on a_1 (smaller = better).
Σ E_j depends on B and the bad a_j values.

As B grows:
- More elements needed in A → a_1 potentially smaller
- But bad a_j all in (M/2, M] → their sum ≤ B·M
- S_1 ≥ m(n/a_1 - 2)

Can we prove a_1 ≤ f(B)·M for some decreasing function f(B)?

---

## COMPUTATIONAL EVIDENCE

| Set | B | Σ E_j | S_1 | Ratio |
|-----|---|-------|-----|-------|
| {6,8,9,20,21} | 2 | 6 | 2328 | 388:1 |
| {82,123,136,153,204,205} | 2 | 200 | 17800 | 89:1 |
| All M≤20 (10,240 sets) | ≤1 | varies | varies | ≥33:1 |

No case with B ≥ 3 has been found yet.

---

## YOUR TASK

Prove S_1 ≥ Σ_{bad} E_j for all primitive A and all m > n ∈ [M, 10M].

Approaches:

1. **Bound B (number of bad layers).** Show B ≤ C for some constant C,
   then use S_1 ≥ 28·min(a_j) and Σ E_j ≤ 17·C·M.

2. **Sharpen the S_1 bound using multiple ancestors.** Each bad layer
   forces small elements into A. Multiple bad layers force a_1 even
   smaller. Show S_1 grows faster than B·17M.

3. **Use the exact formula.** S_1 = 2m·⌊n/a_1⌋ - n·⌊m/a_1⌋ and
   E_j = n·L_j(t_j) - 2m. Don't bound — compute directly.

4. **Show B ≤ 2 always.** If at most 2 bad layers can coexist
   (suggested by computational evidence), then Σ E_j ≤ 2·17M = 34M,
   and S_1 ≥ 4m ≥ 4M suffices if... hmm, 4M < 34M. Doesn't work.
   Need the SHARPER bound E_j ≤ 17a_j where a_j ≈ M, but S_1 uses
   the actual n/a_1 ratio which is much larger.

5. **Global charging.** Don't match S_1 to bad layers. Show that
   2mF(n) - nF(m) > 0 directly by bounding F(m) in terms of F(n).

If you find a counterexample to S_1 ≥ Σ E_j, report immediately.
If you can prove B ≤ C for some explicit constant, report it.
Push as far as you can.
