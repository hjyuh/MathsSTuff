# EP-488: Codex xhigh — The 3-Tax / Upstream Credit Law
## April 7, 2026

## THE INSIGHT (most important output of the entire project)

"What's actually going on is not 'parent sieve dominates child sieve.'
It is 'every bad compact child is paying a local 3-Buchstab tax, and
the primitive 3-ancestor sits far enough upstream that its credit
overfunds that tax.'"

## THE MECHANISM

### Step 1: Buchstab decomposition of the child

Let K = B_j (child's full kernel), C = K \ {3}. Buchstab gives:
  L_K(x) = L_C(x) - L_C(⌊x/3⌋)

So the child excess decomposes as:
  E_j = n·L_K(t) - 2m·L_K(s)
      = [n·L_C(t) - 2m·L_C(s)] - [n·L_C(⌊t/3⌋) - 2m·L_C(⌊s/3⌋)]

The first bracket is the "good side" — C = K\{3} is NOT in the 29 bad
kernels (removing 3 exits the bad family). So the first bracket is ≤ 0.

The second bracket is the "3-tax" — the cost of having 3 in the kernel.

Therefore:
  E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)

THE CHILD'S ENTIRE EXCESS IS BOUNDED BY ITS OWN 3-DELETED LAYER
EVALUATED AT 1/3 SCALE.

### Step 2: The ancestor overfunds the tax

The 3-ancestor has a_i = 3g, a_j = hg with h ≥ 5.
Parent evaluates at:
  u ≈ (h/3)s,  v ≈ (h/3)t

But the child's 3-tax lives at the compressed pair:
  (⌊s/3⌋, ⌊t/3⌋)

The ancestor is competing with a tax at scale ~s/3, while the ancestor
operates at scale ~(h/3)s ≥ (5/3)s. The ancestor is at LEAST 5× deeper
than the tax's scale. That's why margins are 25:1 or 184:1.

### Step 3: The two-step factorization (the real missing theorem)

Box 1: E_j ≤ S_{C_j}(⌊s_j/3⌋, ⌊t_j/3⌋)
  Child excess bounded by 3-deleted good layer at 1/3 scale.
  This follows from Buchstab + the fact that C is NOT a bad kernel.

Box 2: S_i(u_i, v_i) ≥ S_{C_j}(⌊s_j/3⌋, ⌊t_j/3⌋)
  Parent at full scale overpays the 1/3 scale tax.
  This is the scale/transport theorem.

NO KERNEL COMPARISON NEEDED. Matches every kill.

## WHY THIS MATCHES EVERY COUNTEREXAMPLE

Kill #59 (A={8,9,12}): Parent kernel {8} ≠ K\{3}={2}. Doesn't matter —
  the 3-tax is tiny (lives at ⌊4/3⌋=1, ⌊7/3⌋=2 scale), parent at scale 6-9.

Kill #60 (A={2,9,15,25}): Parent kernel {2,3} more obstructed than K\{3}.
  Doesn't matter — the 3-tax at (⌊4/3⌋, ⌊7/3⌋) = (1,2) scale is tiny.
  Parent at (8,11) scale has huge slack regardless of its kernel.

Kill #61 (discrete inequality false): Wrong reduction entirely.
  The right comparison is tax-at-1/3-scale vs parent-at-h/3-scale,
  not a discrete inequality on kernel counts.

## WHY 2 AND 3 ARE SPECIAL (Codex's structural explanation)

- **2 is the compactness pin**: forces L_K(s) = 1 (half of all integers
  are even, so the sieve wipes out almost everything in short windows)
- **3 is the transport pin**: the ONLY obstruction with a canonical upstream
  ancestor and an exact Buchstab subtraction identity
- **Other primes are dampers**: they make the child lighter but don't create
  new types of badness. They wreck kernel comparisons but don't affect
  the 3-tax structure.

Badness is NOT a whole-kernel phenomenon. It's a 3-TAX on a light
compact layer. The ancestor is the upstream 3-CREDIT RESERVOIR.

## ASSESSMENT

This is the first proposed mechanism that:
1. Avoids all kernel comparisons (matches kills #59, 60)
2. Avoids the discrete inequality reduction (matches kill #61)
3. Explains the enormous margins (5× scale separation)
4. Explains why {2,3} is special structurally
5. Uses Buchstab directly on the child, not as a kernel tool
6. Reduces to two clean boxed inequalities

## KILL COUNT: 61 (unchanged — nothing killed)
## PERCENTAGE: 80%

Major jump. This is the first mechanism that survives all 61 kills.
The two-step factorization is clean, finite, and structurally motivated.
If Box 1 and Box 2 can be proved, EP-488 is done.
