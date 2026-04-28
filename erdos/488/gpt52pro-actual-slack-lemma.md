# EP-488: The Actual-Slack Ancestor Lemma — Final Missing Piece
## For GPT-5.2 Pro Extended — April 6, 2026

---

## SITUATION

EP-488 is one lemma away from a complete proof. Here is the exact state.

### The proof chain (steps 1-5 proved, step 6 open, step 7 follows):

1. ✅ Reduce to m, n ∈ [M, 10M] by convexity/stabilization.
2. ✅ Write F(m)/F(n) = Σ w_j · R_j (weighted average of layer ratios, weights sum to 1).
3. ✅ Single-obstruction layers (≤1 active obstruction) satisfy R_j < 2m/n (per-layer EP-488).
4. ✅ Only 29 bad compact kernels exist (all containing {2,3}, all prime, all with L_K(s)=1). Exhaustive check of 10,239 kernels.
5. ✅ Ancestor compensation arithmetic verified for all 29 kernels, zero failures, margins enormous (tightest = 134 in the K\{3} model, and actual-slack margins even larger).
6. ❓ **THE ACTUAL-SLACK ANCESTOR LEMMA** (stated precisely below).
7. ✅ If step 6 holds: F(m)/F(n) < 2m/n for all primitive A, all m > n ≥ M. EP-488 proved. ∎

---

## WHAT JUST HAPPENED (Kill #59 + replacement)

The exact bridge "parent kernel = K \ {3}" was KILLED by A = {8, 9, 12}:
- Child a_j = 12 has kernel {2,3}
- 3-ancestor a_i = 9 has B_i = {8}, NOT {2} = K\{3}
- BUT parent actual slack = 552 >> child excess = 3

So the kernel doesn't need to match — the ACTUAL CONTRIBUTION just needs to be large enough.

### New proved result: Quotient Transport Lemma (5.4 Pro, rigorous)

If q_{i,j} = 3 (i.e., a_i/gcd(a_i,a_j) = 3), then for any k < i:
  q_{k,j} | 3 · q_{k,i}

Meaning: child obstructions are bounded by 3× parent obstructions.
The parent-child relationship is structurally controlled even when
the kernels don't match exactly.

---

## THE LEMMA TO PROVE

For every finite primitive set A, every m > n with M ≤ n < m ≤ 10M,
and every compact layer j with a_j ∈ (M/2, M] whose layer ratio
R_j = L_j(⌊m/a_j⌋)/L_j(⌊n/a_j⌋) exceeds 2m/n (i.e., the layer
contributes positive excess):

**There exists a 3-ancestor layer i < j** (meaning a_i/gcd(a_i,a_j) = 3)
**such that layer i's actual negative slack exceeds layer j's actual
positive excess:**

  2m · L_i(⌊n/a_i⌋) - n · L_i(⌊m/a_i⌋) ≥ n · L_j(⌊m/a_j⌋) - 2m · L_j(⌊n/a_j⌋)

That's it. Parent actual slack ≥ child actual excess.

---

## WHAT'S KNOWN ABOUT THIS LEMMA

### Computational verification:
- 4,673 primitive sets (M ≤ 20): 6,073 positive-excess instances, ALL compensated. Zero failures.
- 5,000 random sets (M ≤ 100): 584 positive-excess instances, ALL compensated. Zero failures.
- Total: 6,657 instances checked, zero failures.
- Margins are enormous (worst case: parent slack 552 vs child excess 3).

### Structural facts available:
- The child has L_K(s) = 1 in every bad case (maximally weak denominator).
- The child's active kernel always contains {2,3} and only primes.
- The quotient transport lemma constrains how parent and child obstructions relate: q_{k,j} | 3·q_{k,i}.
- The parent's floor positions are tightly controlled: ⌊n/a_i⌋ ≈ (h/3)·s, ⌊m/a_i⌋ ≈ (h/3)·t where h = a_j/gcd(a_i,a_j).
- Since a_i = 3g and a_j = hg with gcd(h,3) = 1 and h ≥ 5 (because h must avoid the child's kernel primes), the parent samples at ≈5/3× the child's scale.

### Why the parent has large slack (intuition):
- The parent a_i = 3g is SMALLER than the child a_j = hg (since h ≥ 5 > 3).
- So the parent's floor values ⌊n/a_i⌋ and ⌊m/a_i⌋ are LARGER.
- Larger floor values mean L_i is evaluated deeper into its range, where L_i(y) ≈ d_i · y is well-approximated by its density.
- In the density regime, the layer ratio approaches y_m/y_n ≈ m/n, which is well below 2m/n.
- The parent also has FEWER active obstructions (or different ones that are less harmful at this scale).

### Key example showing the mechanism:
A = {8, 9, 12}:
- Child (a=12): ⌊57/12⌋=4, ⌊84/12⌋=7, L_{2,3}(4)=1, L_{2,3}(7)=3, excess = 3
- Parent (a=9): ⌊57/9⌋=6, ⌊84/9⌋=9, L_{8}(6)=6, L_{8}(9)=8, slack = 552
- Parent is deeper (y=6,9 vs y=4,7) and less obstructed ({8} vs {2,3})

---

## YOUR TASK

Prove the actual-slack ancestor lemma. Or find a counterexample.

### Approach 1: Scale separation
The parent samples at scale h/3 ≥ 5/3 relative to the child.
At the child's worst case (s,t) = (4,7) with L_K(s) = 1:
  Parent has s' ≈ (5/3)·5 - 1 = 7, t' ≈ (5/3)·7 = 11
So the parent sees y ∈ {7, 11} while the child sees y ∈ {4, 7}.

The parent is deeper. Deeper layers are closer to their density.
Can you show that for ANY obstruction set B_i, if s' ≥ 7 and t' ≥ 11,
the layer is safe (contributes negative slack)?

### Approach 2: Direct bound on L_i
Since q_{k,j} | 3·q_{k,i}, the parent's obstructions are controlled.
The parent can have obstructions that are up to 3× smaller than the
child's, but also can have LARGER obstructions (like {8} in the example).
Larger obstructions are less harmful (they sieve fewer integers).
Can you show that the net effect always produces enough slack?

### Approach 3: Use the margin
The finite verification shows minimum margin = 134 in the normalized
model, and actual margins (like 552 vs 3) are even larger. The parent
doesn't need to be barely adequate — it needs to beat a tiny excess
from a maximally weak child (L_K(s) = 1). Can you show that ANY
layer with floor values ≥ 5 has enough slack to beat a child with
L_K(s) = 1 and L_K(t) ≤ 8 (the maximum over all 29 bad signatures)?

### Approach 4: Induction on kernel size
The child has kernel K ⊇ {2,3}. The parent has kernel related by
quotient transport. Can you induct on |K|, showing compensation at
each level of the obstruction ancestry tree?

### What counts as a proof:
A rigorous argument that for EVERY primitive set A and EVERY bad
compact child layer, the 3-ancestor exists AND its actual slack
exceeds the child's actual excess. The argument can use the quotient
transport lemma, the single-obstruction theorem, the 29-kernel
classification, and any structural property of primitive sets.

### What counts as a counterexample:
A specific primitive set A, specific m > n ∈ [M, 10M], and a specific
bad compact child layer j, such that NO 3-ancestor i has sufficient
actual slack to compensate. This would kill the ancestor compensation
approach entirely.

---

## DO NOT HOLD BACK.

6,657 computational instances say this lemma is true. Zero say it's false.
The margins are enormous. The structural ingredients are in place.
Either prove it or find the counterexample that 6,657 instances missed.
