# EP-488 v27 — Bridge Lemma Computation Report (April 11, 2026)

This file records the computation-first tests from the “EP-488: The Bridge Lemma” document.

## How to reproduce

- Test 1:
  - Run: `python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\ep488_bridge_lemma_tests_v27.py`
- Tests 3–4:
  - Run: `python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\ep488_bridge_lemma_tests_34_v27.py`

## Test 1 (L² block-dispersion ratio R(A,n,m))

Search space:
- all primitive `A ⊆ {2,…,20}`, `A≠∅` (10,239 sets)
- `n = max(A)`
- all `m` with `n < m ≤ 10n`
- partition = minimum-coloring partition into L-primitive blocks using the overlap criterion for `L_a`

### Max of the ratio as written in the test definition

`R(A,n,m) = [Σ_ℓ E_ℓ(n,m)^2 / (m^2 n^2 D_ℓ)] / [Σ_ℓ D_ℓ]`

Maximizer found:
- `A = {19}`
- blocks: `[{19}]`
- `n = 19`, `m = 190`
- `left = Σ E_ℓ^2/(m^2 n^2 D_ℓ) = 85616515609/99324825600 ≈ 0.861985058537`
- `R = left / (Σ D_ℓ) = 85616515609/943718400 ≈ 90.722524440553`  (**≫ 1**)

### Max of the un-normalized left side

`left(A,n,m) = Σ_ℓ E_ℓ(n,m)^2 / (m^2 n^2 D_ℓ)`

Maximizer found:
- `A = {11,13,17,19}`
- blocks: `[{11,13,17,19}]` (already L-primitive as a set)
- `n = 19`, `m = 120`
- `left = 2051284515845/1082857872096 ≈ 1.894324794328`  (**> 1**)

**Conclusion from Test 1:** Form 1 as stated (and the Test‑1 ratio `R`) fails on very small primitive sets.

## Test 3 (Sieve overshoot ratio)

Definition:
- `A` sampled primitive sets with `max(A) ∈ [50,200]`
- anchor `a = min(A)`
- `Q = prim({b/gcd(a,b) : b∈A, b≠a} \\ {1})`
- `A_Q(x) = #{1≤n≤x : ∀q∈Q, q∤n}`
- `δ_Q` computed exactly (product if coprime; else IE)
- `R(Q) = max_{x∈[max(Q),10·max(Q)]} A_Q(x)/(δ_Q x)`

Worst found in a 3,000‑sample run:
- `A = {14,21,24,27,66}`
- `Q = {3}`
- `δ_Q = 2/3`
- argmax `x = 5`
- `R(Q) = 6/5 = 1.2` (well below `e^γ ≈ 1.78107…`)

## Test 4 (Sawtooth inner-product sign)

Definition:
- `ψ_d(x) = {x/d} - 1/2` evaluated on integer `x`
- inner product on `[n,10n)`:
  `⟨ψ_d,ψ_e⟩ = (1/(9n)) Σ_{x=n}^{10n-1} ψ_d(x)ψ_e(x)`

Worst (most positive) cross-inner-product found in an 800‑sample run with `n=2000`:
- `A = {2,3,7,37,41,53}`
- pairs = 15
- positive pairs = 14/15
- `max ⟨ψ_d,ψ_e⟩ = 1/24 ≈ 0.0416666666667`  (**positive**)
- `min ⟨ψ_d,ψ_e⟩ ≈ -1.669779535633e-4`

**Conclusion from Test 4:** pairwise nonpositivity of these sawtooth inner products is false in general.

