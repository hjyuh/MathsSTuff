# EP-488: Unified Truth v3 — The Uniqueness Conjecture
## April 7, 2026 — For all models

---

## THE PROBLEM

Erdős Problem 488 (1966): For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).

---

## THE PROOF IS ONE CONJECTURE AWAY

### What's proved (complete chain except step 5):

1. ✅ **Convexity:** extrema in [M, 10M].
2. ✅ **Decomposition:** F(x) = Σ L_j(⌊x/a_j⌋), divisibility avoidance.
3. ✅ **Weighted average:** F(m)/F(n) = Σ w_j R_j, Σw_j = 1.
4. ✅ **Self-funding:** layers with s_j ≤ 3 always have E_j ≤ 0.
5. ❓ **UNIQUENESS: at most one bad compact layer per (A, n, m).**
6. ✅ **First-layer theorem:** S_1 > E_j for every individual bad child.
7. ✅ **Conclusion:** steps 4+5+6 → S_1 covers the single bad child → EP-488.

### Why step 5 completes the proof:

The first layer (a_1 = min A) has no obstructions, so L_1(y) = y.
Its slack S_1 ≥ 28a_j > 17a_j ≥ E_j for every individual bad child.
If at most one bad child exists per (n,m), then S_1 > Σ E_j = E_j, done.

---

## THE UNIQUENESS CONJECTURE

**Statement:** For every finite primitive set A and every m > n ∈ [M, 10M],
at most one compact layer j has positive excess E_j = n·L_j(t_j) - 2m·L_j(s_j) > 0.

**Computational evidence:** Verified on ALL 10,240 primitive subsets of [2,20].
Zero cases with two positive-excess bad compact layers at the same (A,n,m).
Worst ratio S_1/Σ E_j = 2734/81 ≈ 33.75.

---

## WHAT WE KNOW ABOUT BAD LAYERS

A layer j is "bad" (positive excess possible) only if ALL of these hold:

1. **K_j ⊇ {2,3}** — kernel contains both 2 and 3 (29-kernel classification)
2. **K_j is all-prime** — subset of {2,3,5,7,11,13,17,19}
3. **L_K(s_j) = 1** — only integer 1 survives up to s_j (prime-cover rigidity)
4. **s_j ∈ [4, 19]** — self-funding kills s ≤ 3, prime-cover kills s ≥ 20
5. **a_j ∈ (M/2, M]** — compact layer
6. **a_j ≤ n/4** — because s_j ≥ 4 means n ≥ 4a_j

---

## WHY TWO BAD LAYERS SHOULD CONFLICT

For j₁ and j₂ to both be bad at the same (n,m):

**Both need 2-obstructions.** ∃ a_r₁ with a_r₁/gcd(a_r₁,a_{j₁}) = 2, and
∃ a_r₂ with a_r₂/gcd(a_r₂,a_{j₂}) = 2. These could be the same element or different.

**Both need 3-obstructions.** Similarly, 3-ancestors for both layers.

**Both are compact:** a_{j₁}, a_{j₂} ∈ (M/2, M]. So a_{j₂}/a_{j₁} < 2.
Since A is primitive, a_{j₁} ∤ a_{j₂} and a_{j₂} ∤ a_{j₁}.

**Both need s ≥ 4:** a_{j₁} ≤ n/4 and a_{j₂} ≤ n/4.

**Both need positive excess at the SAME (n,m):** This means both layers
"unfreeze" (gain survivors past their frozen L_K(s)=1 state) in the
interval from n to m. Survivors are coprime-to-6 integers (since K ⊇ {2,3}).
The survivor spikes happen at 5, 7, 11, 13, 17, 19, 23, 25, 29, 31...
These are evaluated at different scales (⌊x/a_{j₁}⌋ vs ⌊x/a_{j₂}⌋).
For BOTH to spike simultaneously requires a very specific relationship
between a_{j₁} and a_{j₂}.

**Key: the excess E_j = n·L_K(t) - 2m is positive only when m < n·L_K(t)/2.**
For two layers, both need m < n·L_{K₁}(t₁)/2 AND m < n·L_{K₂}(t₂)/2.
So m < n·min(L_{K₁}(t₁), L_{K₂}(t₂))/2. This is a TIGHT constraint on m.

---

## APPROACHES TO PROVE UNIQUENESS

### Approach 1: Direct contradiction from primitivity
Assume j₁, j₂ both bad. Both compact (> M/2). Both have K ⊇ {2,3}.
Both need 2-ancestors and 3-ancestors from earlier elements.
Show the element interactions under primitivity force one layer to
lose its positive excess.

### Approach 2: Timing/phase argument
Both layers have survivors at coprime-to-6 integers.
Layer j₁ sees survivors at ⌊x/a_{j₁}⌋ = 5, 7, 11...
Layer j₂ sees survivors at ⌊x/a_{j₂}⌋ = 5, 7, 11...
For both to have E_j > 0: both need L_K(t) ≥ 3 (since E_j = n·L_K(t)-2m > 0
requires L_K(t) > 2m/n > 2). So both need t ≥ 7 (since L_{2,3}(6)=2).
Show that a_{j₁} and a_{j₂} can't both have t ≥ 7 while also both having
s ≥ 4 and s ≤ 19 at the same (n,m).

### Approach 3: Weight argument for |A| ≥ 3
If |A| ≥ 3, F(n) ≥ 3. Even two bad layers have total weight ≤ 2/3.
The first layer contributes w_1 · R_1 < w_1 · 2m/n to the average.
Show that two bad layers with total weight 2/F(n) can't overcome
the good layers' contribution, using R_j bounds from the 29-kernel
classification.

### Approach 4: Exhaustive finite check
The parameters are finite: s ∈ [4,19], t ∈ [7,20], K one of 29 kernels.
For two layers: s₁, s₂ ∈ [4,19], t₁, t₂ ∈ [7,20], K₁, K₂ from the 29.
Show that for each pair (K₁, s₁, t₁, K₂, s₂, t₂), the existence of
a_{j₁} and a_{j₂} both in (M/2, M] with these parameters AND with
both having positive excess is impossible under primitivity.

---

## TOOLS AVAILABLE

- 29-kernel classification (complete list of bad kernels)
- Prime-cover rigidity: L_K(s)=1 iff all primes ≤ s in K
- Quotient transport: q_{k,j} | 3·q_{k,i}
- First-layer theorem: S_1 ≥ 28a_j > 17a_j ≥ E_j
- Self-funding: s ≤ 3 → E_j ≤ 0
- Stock-flow identity: exact algebra, D = 2m-n > n
- Computational verification: 10,240 sets checked, zero two-bad-layer cases
- Six Lean-verified foundational lemmas

---

## YOUR TASK

Prove the uniqueness conjecture. Or find a counterexample.

If you prove it: EP-488 is solved. State the proof clearly.
If you find a counterexample: state the primitive set A and the pair (n,m)
where two layers both have positive excess.
If you can reduce it to a finite check: state the check precisely.
If you can prove a weaker version (e.g., Σ E_j ≤ S_1): state it.

This is the last step. Push as hard as you can.
