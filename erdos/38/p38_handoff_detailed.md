# P38 Handoff Note (Detailed)

This note is a self-contained handoff for a new model with no prior context.

## 0. Problem context

We are working on Erdős Problem 38 via dyadic shifts.

Let `N = 2^K`. Let `A ⊆ {0,1,...,N}` with `0 ∈ A`. Define

- `x_n = 1_A(n)` for `1 ≤ n ≤ N`
- `F(m) = |A ∩ [1,m]|`
- `α = σ(A) = min_{m≥1} F(m)/m` (Schnirelmann density)
- `β = F(N)/N`

The regime of interest is

- `F(m) ≥ α m` for all `1 ≤ m ≤ N`
- `β ≤ α + η`, with `η` small.

The original goal was a linear lower bound on the dyadic gain `G_{2^k}(A,N)` for some `k`.

---

## 1. Definitions that matter now

For a shift `b` with `1 ≤ b ≤ N-1`, define the disagreement

`D_b(x) = Σ_{n=1}^{N-b} |x_{n+b} - x_n|`.

This is the Hamming disagreement between `x[1..N-b]` and `x[1+b..N]`.

For a dyadic shift `L = 2^k`, if we partition the word into consecutive blocks

`x = U_1 U_2 ... U_t`, where each `U_i` has length `L` and `t = N/L`,

then

`D_L(x) = Σ_{i=1}^{t-1} Ham(U_i, U_{i+1})`.

So dyadic shifts measure **adjacent-block Hamming variation**, not Haar imbalance.

The gain is

`G_b(A,N) = Σ_{n=1}^{N-b} x_n (1 - x_{n+b})`.

Exact identity:

`G_b = (1/2) D_b + (1/2)(F(b) + F(N-b) - F(N))`.

Hence if `β ≤ α + η`, then for dyadic `b`

`G_b ≥ (1/2) D_b - O(ηN)`.

So a linear lower bound on some dyadic `D_{2^k}` would imply a linear lower bound on the gain.

---

## 2. The original Bridge Lemma is false

### 2.1 Statement that failed

For dyadic blocks at scale `k`, with left/right halves `L,R`, define

`Δ_B = |A ∩ L| - |A ∩ R|`.

The hoped-for lemma was:

`∃ k such that Σ_B |Δ_B| ≥ c(α) N`.

This is false.

### 2.2 Counterexample family

Take `r` a power of `2`. Let

- `M = 2^r`
- `N = r M = r 2^r`.

For `j = 0,1,...,r-1`, define

`W_j = (1^{2^j} 0^{2^j})^{2^{r-j-1}}`.

Concatenate

`w = W_0 W_1 ... W_{r-1}`.

Let `A = {0} ∪ {1 ≤ n ≤ N : w_n = 1}`.

Facts:

- `α = β = 1/2`
- `F(m) ≥ m/2` for all `m`
- at dyadic Haar scale `k`,
  - `Σ_B |Δ_B| = M/2` for `0 ≤ k < r`
  - `Σ_B |Δ_B| = 0` for `k ≥ r`
- therefore

`max_k Σ_B |Δ_B| = M/2 = N/(2r) = Θ(N / log N)`.

This kills the Bridge Lemma.

### 2.3 Additional important feature

This counterexample has **flat dyadic Parseval energy** across the active scales `0,...,r-1`. So the ballot condition does **not** prevent flat dyadic spectrum.

### 2.4 Error in the old Haar argument

A previous route used Cauchy–Schwarz in the wrong direction. The valid inequality is

`(Σ_B |Δ_B|)^2 ≤ M Σ_B Δ_B^2`,

not `≥`. So there is no rigorous `N / sqrt(log N)` lower bound from Parseval + Cauchy–Schwarz.

---

## 3. Why the gain survives on the counterexample

Although the Haar bridge dies, the gain stays linear because of **cross-block structural mismatch**.

For the above `W_j` family, the best shift is `b = M = 2^r`.

That shift maps `W_j` onto `W_{j+1}`. Adjacent macro-blocks have the same density `1/2` but different internal structure, and

`Ham(W_j, W_{j+1}) = M/2`.

Hence

`D_M = (r-1) M / 2`

and therefore

`G_M = (r-1) M / 4 = (1 - 1/r) N / 4`.

So the right invariant is not aligned Haar imbalance but adjacent-block Hamming variation.

---

## 4. Exact identities that are now central

### 4.1 Pair-count identity

For every binary word of length `N` with `β = F(N)/N`,

`Σ_{b=1}^{N-1} D_b = β(1-β) N^2`.

Reason: each unequal pair `(i,j)` with `i < j` is counted exactly once, at shift `b = j-i`.

### 4.2 Subadditivity

`D_{a+b} ≤ D_a + D_b`.

This follows from

`|x_{n+a+b} - x_n| ≤ |x_{n+a+b} - x_{n+a}| + |x_{n+a} - x_n|`.

Hence if `b = Σ ε_k 2^k`, then

`D_b ≤ Σ ε_k D_{2^k}`.

Combining with the pair-count identity yields the unconditional dyadic lower bound

`max_k D_{2^k} ≥ 2 β(1-β) N / K`.

This is the clean `N / log N` bound.

---

## 5. Cyclic reduction: the real core is not ballot-specific

Every exact-density periodic binary word has a ballot rotation.

### 5.1 Rotation-at-the-minimum / cycle-lemma reduction

If `y ∈ {0,1}^p` has exactly `m` ones and `α = m/p`, define partial sums

`S_j = Σ_{i=1}^j (y_i - α)`.

Rotate at an index where `S_j` is minimal. The resulting periodic word `x` satisfies

`Σ_{i=1}^n (x_i - α) ≥ 0` for all `n`.

So every exact-density periodic word has a ballot realization after rotation.

### 5.2 Cyclic disagreement model

For a cyclic word `y` of length `p`, define

`d_r(y) = #{ i mod p : y_i ≠ y_{i+r} }`.

For the associated periodic ballot word, finite disagreements satisfy

`D_b(x;N) = floor((N-b)/p) d_{b mod p}(y) + O(p)`.

Therefore any dyadic-domination statement for ballot words would already imply a cyclic doubling-orbit sampling statement.

This means the core obstruction survives even after ballot geometry is removed.

---

## 6. Any dyadic-domination constant must satisfy `C(1/2) ≥ 2`

A rigorous construction shows this.

Take

- `q = 2^m - 1`
- `p = 2q`
- choose a random `u ∈ {0,1}^q`
- form the cyclic word `y = (u, complement(u))`.

Then

`y_{i+q} = 1 - y_i`,

so

`d_q(y) = p`.

But the distinct dyadic residues mod `p` are only `1,2,4,...,2^m`, and for a random choice of `u` they all satisfy

`d_{2^k mod p}(y) ≤ p/2 + O(sqrt(p log log p))`

simultaneously with positive probability.

Therefore

`max_r d_r(y) / max_k d_{2^k mod p}(y) ≥ 2 - o(1)`.

After ballot rotation and truncation, this gives ballot words with ratio approaching `2`.

Conclusion:

Any true dyadic-domination theorem must have constant at least `2` when `α = 1/2`.

---

## 7. Spectral barrier: why average/Fourier methods lose a log

On periods

`p = 2(2^m - 1)`,

the parity character is an almost-eigenfunction for averaging over the dyadic residues `1,2,4,...,2^m mod p`.

The corresponding spectral gap is only `Θ(1 / log p)`.

Implication:

Any method based only on averages over dyadic shifts, Parseval, or a plain spectral gap will lose a logarithm. This explains why the `N / log N` barrier appears naturally.

---

## 8. Even/odd recursion and exact synchronization

This is the clean recursive structure that survived.

### 8.1 Basic even/odd split

Let

- `o_i = x_{2i-1}`
- `e_i = x_{2i}`.

Then

`D_{2t}(x) = D_t(o) + D_t(e)`.

Also

`D_1(x) = Σ_i |o_i - e_i| + Σ_i |e_i - o_{i+1}|`.

### 8.2 General residue-class recursion

For level `j` and residue `r`, define

`x^{(j,r)}_m = x_{1 + r + m 2^j}`.

Then for `0 ≤ j ≤ k ≤ K-1`,

`D_{2^k}(x) = Σ_{r=0}^{2^j-1} D_{2^{k-j}}(x^{(j,r)})`.

In particular,

`D_{2^j}(x) = Σ_{r=0}^{2^j-1} D_1(x^{(j,r)})`.

So the total number of transitions across all subsequences at level `j` is exactly `D_{2^j}`.

### 8.3 Recovering the `N/K` bound recursively

Using the recursion plus the odd/even split of all shifts, one gets

`β(1-β) N^2 ≤ (N/2) Σ_{j=0}^{K-1} D_{2^j}(x)`.

Hence if `D_{2^j}(x) ≤ εN` for every `j`, then

`ε ≥ 2 β(1-β) / K`.

This is another proof of the `N / log N` barrier.

### 8.4 Exact synchronization lemma

Let a parent subsequence have children `u,v`, and define

- `m_i = u_i ⊕ v_i`
- `τ_u(i) = u_i ⊕ u_{i+1}`
- `τ_v(i) = v_i ⊕ v_{i+1}`.

Then the exact identity is

`τ_u(i) ⊕ τ_v(i) = m_i ⊕ m_{i+1}`.

Interpretation:

- if `m_i = m_{i+1}`, then `u` and `v` have transitions at position `i` simultaneously or not at all
- transitions of sibling subsequences can differ only at boundaries of the mismatch set.

Summed over all parents at level `j`, this gives

`Σ_r D_1(m^{(j,r)}) ≤ D_{2^{j+1}}(x)`.

So next-scale disagreement controls the number of places where current-scale defect patterns can switch on/off.

### 8.5 Interval consequence

For each parent fiber, the support of `m^{(j,r)}` is a union of intervals. If `c_{j,r}` is the number of interval components, then

`c_{j,r} ≤ 1 + (1/2) D_1(m^{(j,r)})`.

Therefore

`Σ_r c_{j,r} ≤ 2^j + (1/2) D_{2^{j+1}}(x)`.

So if `D_{2^{j+1}}` is small, then the level-`j` defect set consists of relatively few long components.

This is the precise “fiber regularity” supplied by the recursion.

---

## 9. Cube encoding

Encode the word as a Boolean function on the cube:

`f(a_0,...,a_{K-1}) = x_{1 + Σ_{t=0}^{K-1} a_t 2^t}`.

Then the aligned level-`j` defect mass is exactly the edge boundary in coordinate `j`.

More precisely, let `E_j` be the set of edges in direction `j` crossing the cut `{f=1}`. Let

`μ_j = |E_j|`.

Then

`I_j(f) = μ_j / 2^{K-1}`

is the usual influence.

Also

`μ_j ≤ D_{2^j}(x)`.

So lower bounds on some influence imply lower bounds on some dyadic disagreement.

---

## 10. KKL gives a rigorous improvement

Applying KKL / influence lower bounds on the Boolean cube gives

`max_j I_j(f) ≥ c β(1-β) (log K)/K`.

Hence

`max_j μ_j ≥ c β(1-β) N (log K)/K`.

Since `μ_j ≤ D_{2^j}(x)`, we get

`max_k D_{2^k}(x) ≥ c β(1-β) N (log K)/K`.

Because `K = log_2 N`, this is

`max_k D_{2^k}(x) ≥ c β(1-β) N (log log N)/(log N)`.

This is a rigorous improvement over the crude `N / log N` bound.

---

## 11. BGK gives a linear theorem in the prime cyclic model

There is a clean analogue in the prime-period model.

Let `p` be prime, `S ⊆ F_p`, and let

`d_r = |S triangle (S+r)|`.

Let `H = <2> ⊆ F_p^×` be the multiplicative subgroup generated by `2`.

If `|H| > p^γ`, the Bourgain–Glibichuk–Konyagin theorem implies that all nontrivial additive character sums over `H` are small. Fourier expansion then shows

`(1/|H|) Σ_{h∈H} d_h = 2 β(1-β) p + O_γ(p^{1-ν})`

for some `ν = ν(γ) > 0`.

Therefore some dyadic residue `h = 2^k mod p` satisfies

`d_h ≥ 2 β(1-β) p - O_γ(p^{1-ν})`.

So in the prime cyclic model with a large doubling orbit, the dyadic disagreements are automatically linear.

This is the closest solved analogue found so far.

---

## 12. The first cube conjecture and why it failed

### 12.1 False conjecture

A natural conjecture was:

If every coordinate boundary `E_j` has small fiber-boundary `b_j` (few interval components on each fiber), then some influence `I_j` must be bounded below by a positive constant depending only on density.

Equivalently: “fiber-regular KKL.”

### 12.2 Counterexample: tribes

This conjecture is false.

The counterexample is the balanced tribes function.

Take tribe width `w`, number of tribes `m ≈ 2^w log 2`, so `K = mw`. Let `T_{m,w}` be the OR of `m` many ANDs of width `w`.

Facts:

- density tends to `1/2`
- `max_j I_j(T_{m,w}) ≍ 1/2^w ≍ (log K)/K`
- the lex-fiber boundary variation parameter also satisfies
  `max_j b_j / 2^K ≍ (log K)/K`.

Thus the extra “few interval components on lexicographic fibers” hypothesis is too weak to upgrade KKL from `(log K)/K` to a constant.

### 12.3 Exact lesson

Lex-path regularity does **not** control higher-order influence structure strongly enough.

The proof attempt broke at the missing implication

`small b_j  =>  small pair influences`

which is false in this level of generality.

---

## 13. Current best open direction

The unrestricted fiber-regular KKL conjecture is dead. The remaining route is to identify a **stronger structural invariant** enjoyed by cube functions coming from Schnirelmann / ballot words, but not by tribes.

Two plausible candidates:

### 13.1 Pair influences / second-order influences

Try to show the P38 image on the cube has small pair influences `I_{j,k}` in a sense strong enough to trigger an Oleszkiewicz-type theorem.

### 13.2 Sensitivity moments

Try to show the P38 image has bounded `p`-moment of sensitivity for some `p > 1/2`, which by Eldan–Kindler–Lifshitz–Minzer gives junta-type structure and hence a large coordinate influence.

In both cases, the missing task is to extract a structural invariant from the original one-dimensional ballot setting that tribes does not satisfy.

---

## 14. Current state of the project in one page

### Proven / rigorous

1. The original Haar Bridge Lemma is false.
2. The `W_j` family gives a ballot counterexample with flat dyadic Haar spectrum.
3. The dyadic gain is governed by disagreement `D_b`, not Haar imbalance.
4. Exact identities:
   - `G_b = (1/2) D_b + (1/2)(F(b)+F(N-b)-F(N))`
   - `Σ_b D_b = β(1-β) N^2`
   - `D_{2^k} = Σ Ham(adjacent blocks)`.
5. Unconditional dyadic lower bound:
   - `max_k D_{2^k} ≥ 2 β(1-β) N / K`.
6. Cyclic reduction: ballotness is not the whole story.
7. Any dyadic-domination constant at `α=1/2` must satisfy `C ≥ 2`.
8. Spectral / average methods cannot beat the log barrier on certain even periods.
9. Exact synchronization lemma and interval-regularity consequence.
10. Cube encoding gives a KKL improvement:
    - `max_k D_{2^k} ≥ c β(1-β) N (log log N)/(log N)`.
11. BGK proves a linear dyadic-disagreement theorem in the prime cyclic model.
12. The unrestricted fiber-regular KKL conjecture is false (tribes counterexample).

### Open

1. Find a stronger cube-level invariant inherited from ballot words.
2. Show that invariant excludes tribes-like obstructions.
3. Use that invariant to upgrade the KKL-type lower bound from `(log log N)/(log N)` to a constant.
4. Convert that back to a linear dyadic gain lower bound for Problem 38.

---

## 15. Suggested prompt for a new model

Use this exact handoff as the starting context. Then ask:

> We already know the original Haar Bridge Lemma is false and the unrestricted fiber-regular KKL conjecture is false by tribes. The live target is to identify a stronger structural invariant satisfied by Boolean cube functions arising from Schnirelmann / ballot words but not by tribes.
>
> Please do all of the following:
> 1. Propose candidate invariants at the cube level that are actually inherited from the one-dimensional ballot condition.
> 2. Test those invariants against tribes and the `W_j` family.
> 3. Try to prove that one such invariant implies a constant lower bound on some coordinate influence, or on some dyadic disagreement `D_{2^k}`.
> 4. Be explicit about exactly where each candidate argument fails.
>
> The key proved facts available are the exact identities, cyclic reduction, synchronization lemma, KKL improvement, BGK prime-model theorem, and the tribes disproof of naive fiber-regular KKL.

