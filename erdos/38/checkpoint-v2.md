# Erdős Problem #38 — Checkpoint at 8.8/10

## Goal
We are trying to resolve Erdős problem #38.

Problem shape:
- Need an infinite set `B ⊂ ℕ` that is **not** an additive basis,
- but for every `A ⊂ ℕ` with Schnirelmann density `d_s(A)=α∈(0,1)` and every `N`,
- there exists `b ∈ B` such that
  \[
  |(A \cup (A+b)) \cap [1,N]| \ge (\alpha + f(\alpha))N
  \]
  for some `f(α) > 0`.

Our strongest work so far is on the **half-density slice** `α = 1/2`.

---

## Current score
**8.8/10**

Meaning:
- We have a sharp finite obstruction/classification program on `α=1/2`.
- We have ruled out several tempting local routes INCLUDING the full spectral same-lag route.
- We do **not** yet have the final bridge to one infinite non-basis `B`.
- The current bottleneck is now very clearly identified: the global bridge + general α.

---

# 1. Frozen facts / theorems

## 1.1 Half-density finite classification above 1/6
In the finite MPB/Farey model at `α=1/2`, for gain threshold `δ > 1/6`:

- all positive-width survivors are exactly the **1/4-spike** and **3/4-spike** families;
- all `J_max ≥ 2` survivors are impossible;
- all surviving `J_max = 1` branches are classified.

## 1.2 Spike set on dyadic units
For `q = 2^m`, the half-density survivor ratio set is exactly
\[
\mathcal S_q = \{u \in (\mathbb Z/q\mathbb Z)^\times : u \equiv 3 \pmod 4\}.
\]

Equivalently, `{x : χ_4(x) = -1}`.

## 1.3 Pair graph outcome
The spike quotient graph collapses to mod-4 parity:
- complete bipartite, triangle-free, clique number 2.
- Pair-graph structure alone is too weak to force growth of `|R_q(B)|`.

## 1.4 Mixed-shift exact formula
For block construction with block size `q`, total length `Mq`, shift `b=tq+r`:
\[
G(tq+r)=\sum_{j=t}^{M-1} K_r^P(\sigma_{j-t},\sigma_j)
+
\sum_{j=t+1}^{M-1} K_r^Q(\sigma_{j-t-1},\sigma_j).
\]

## 1.5 3-word period-8 mixed-shift theorem
Words: `W_0 = 11110000`, `W_1 = 10101010`, `W_2 = 10110100`.

### Argmin structure
- `r ≡ 1,7 (mod 8)` → monochromatic optimal core `(0,0,0)`
- `r ≡ 3,5 (mod 8)` → monochromatic optimal core `(2,2,2)`

### Gap theorem
- On correct core: local cost `q/8 + O(1)`
- Off core: local cost `q/4 - O(1)`

### Consequence
For `1/6 < δ < 3/16`, same lag `t` cannot support both odd residue families.

## 1.6 Cross-lag incompatibility theorem
For `1/6 < δ < 3/16`, if lag `t` is F₀-type and lag `u` is F₂-type:
\[
t+u \ge (3-16\delta)M - O(1).
\]
Two small lags cannot simultaneously support opposite odd residue families.

## 1.7 Dyck correction bridge (A5.1)
For any half-density word `W` with prefix defect `H(W) = max_k (-S(k))_+`:
- ∃ Dyck half-density word `W^#` with `|W^# △ W| ≤ 2H(W)`
- If `H(W) = o(q)`, all mixed kernels perturbed by `o(q)`.

## 1.8 Random balanced biased blocks (A7.1-A7.2)
- Random balanced sign sequences: `H(x) ≪ √(q log q)` w.h.p.
- For any fixed finite Fourier palette: balanced sign words exist with prescribed bias `c√q` and `H(x) ≪ √(q log q)`.

## 1.9 **[NEW] Spectral same-lag route: DEAD (verified March 19, 2026)**

### 1.9.1 Scalar spectral feasibility
The scalar LP with:
- `ρ ≥ η` on `F₀ = {1,7 mod 8}`
- `ρ ≤ -η` on `F₂ = {3,5 mod 8}`  
- `|ρ| ≥ η` on even classes `{2,4,6 mod 8}`

is **FEASIBLE** with `η* ≈ 0.4010 > 1/3`. Unique optimizer uses period-7 frequencies (breaks 8-periodicity). Survives even under L∞ diffuseness cap of 0.01.

### 1.9.2 2×2 PSD matrix test: VIOLENTLY INFEASIBLE
With the true mixed P/Q geometry using words W₀, W₂:

**Hand-verified kernel matrices at r=4, t=0:**
\[
K^P_4 = \begin{pmatrix} 4 & 3 \\ 3 & 3 \end{pmatrix}, \quad K^Q_4 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}
\]

The minimum mean mismatch over ALL valid transition distributions is exactly **3.5 mismatches** (fraction 0.4375).

The permitted threshold for δ > 1/6 is **1.333 mismatches** (fraction 0.1667).

3.5 >> 1.333. **No PSD spectral measure can bridge this gap.**

### 1.9.3 Frozen conclusion
The spectral same-lag route is rigorously and totally dead. The abstract scalar formulation allowed fake survival via non-dyadic period-7 harmonics, but the rigid P/Q window geometry in true block transitions overrides any macroscopic spectral tuning. The bridge to infinite non-basis B cannot come through same-lag multi-class survival.

---

# 2. Dead routes / negative bottlenecks (COMPLETE LIST)

The following are now rigorously dead for the target regime δ > 1/6:

1. Period-8 same-lag projected-core (best threshold < 1/6)
2. Period-16 structured same-lag projected-core (did not beat 1/6)
3. 2-symbol local compatibility (exhausted)
4. Pure-time obstruction alone (single periodic adversary defeats it)
5. Finite-palette CLT-scale spectral bias (A8.2: correlation O(1), too weak)
6. Odd-family-only LP (feasible but insufficient alone)
7. "Diffuse spectrum" in weak sense of all masses o(1)
8. **[NEW] Full spectral same-lag route including even classes and P/Q geometry**

Do **not** spend more passes on ANY of these.

---

# 3. What is still alive

## 3.1 **[PRIMARY] Global bridge to one infinite non-basis B**
This is the biggest missing conceptual piece (estimated 0.9 points).

We need to go from "finite block obstructions constrain B" to "one infinite B exists (or doesn't) with the required density-boosting property."

### Candidate approaches:
1. **Compactness/ultrafilter:** Finite obstructions → infinite structure via König/Tychonoff
2. **Probabilistic construction:** Random non-basis B has quantitative boosting w.h.p.
3. **Linnik strengthening:** Can Linnik's essential component be shown to have quantitative bounds?
4. **Character-theoretic construction:** Use χ₄ structure to build B algebraically
5. **Ergodic-theoretic:** Shift-invariant measures, spectral gap arguments

### What we know about the bridge:
- Ruzsa-type essential-component bounds give only necessary conditions, not the bridge
- Our finite obstruction program constrains what B must look like in every finite window
- The spectral same-lag route is dead, so the bridge must use fundamentally mixed/multi-lag geometries or pivot entirely

## 3.2 General α, not just 1/2
(Estimated 0.3 points)

Need:
- Admissible-word machinery for general rational α = m/q
- Analogue of spike families for general α
- Route that doesn't collapse when α ≠ 1/2
- The χ₄ classification should generalize to other Dirichlet characters

## 3.3 Multi-lag geometries
The spectral same-lag death theorem implies progress must come from:
- Mixed multi-lag constructions
- Fundamentally different structural approaches
- Or pivoting away from the block model entirely

---

# 4. Exact next task when resuming

## Task 1: Global bridge (the 0.9 gap)
Explore five independent approaches to constructing or proving existence/non-existence of the infinite non-basis B:

1. Compactness from finite obstructions
2. Probabilistic construction
3. Linnik strengthening  
4. Character-theoretic construction
5. Ergodic construction

For each: state the key lemma needed, assess feasibility, identify the exact obstacle.

## Task 2: General α (the 0.3 gap)
Extend the χ₄ classification to general rational densities. What character-theoretic structure governs spike survivors at α = 1/3, 1/4, 2/5?

---

# 5. Honest state summary

We are **not** one lemma away from proving #38.

We **are** at an excellent stopping point because:
- The finite half-density obstruction side is sharp
- EIGHT dead ends are now rigorously dead (including the full spectral same-lag route, verified by hand)
- The remaining live directions are clearly enumerated
- The global bridge is the dominant bottleneck

## Resume with:
> "Explore five independent approaches to the global bridge (Section 3.1), assessing feasibility and identifying the key lemma for each."

That targets the 0.9 gap directly.

---

*Last updated: March 19, 2026*
*Previous version: 8.6/10 (pre-spectral feasibility test)*
