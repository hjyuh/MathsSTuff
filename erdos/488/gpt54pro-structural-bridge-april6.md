# EP-488: Fill In This Proof Skeleton
## For GPT-5.4 Pro Extended — April 7, 2026

You produced the 29-kernel classification and the Quotient Transport Lemma.
A proof skeleton for the final missing piece now exists with exactly TWO gaps.
Fill them in. Nothing else.

---

## THE SKELETON

### Step 1: 3-ancestor exists ✅
If compact layer j has positive excess, its active kernel K contains {2,3}.
Since 3 ∈ B_j, ∃ a_i with a_i/gcd(a_i,a_j) = 3. Set g = gcd(a_i,a_j),
a_i = 3g, a_j = hg. Primitivity forces gcd(h,3) = 1 and h ≥ 5.

### Step 2: Child excess bounded ✅
L_K(s) = 1 in every bad case. So child excess = n·L_K(t) - 2m.
Since n ≤ (s+1)a_j - 1 and m ≥ t·a_j:
  E_j ≤ a_j · [(s+1)L_K(t) - 2t] - L_K(t)
This is a bounded constant times a_j for each of the 29 bad signatures.
Worst case: ≤ 17·a_j (at K={2,3,5,7}, (s,t)=(10,19)).

### Step 3: Parent slack bounded from below [GAP A — FILL THIS IN]

**Claim:** L_i(x) ≥ L_{B_j\{3}}(x) for all x.

**Why it should be true:** By your Quotient Transport Lemma, q_{k,j} | 3·q_{k,i}.
For primes p ≠ 3: ν_p(q_{k,j}) = max{0, ν_p(q_{k,i}) - ν_p(h)}.
So every non-3 prime in a child obstruction divides the corresponding parent
obstruction. The parent obstruction is a MULTIPLE of the child's non-3 part.
Multiples of an obstruction sieve FEWER integers (every multiple of b' is
a multiple of b, so avoiding b' is easier). Therefore L_i(x) ≥ L_{B_j\{3}}(x).

Then by Buchstab: L_{B_j\{3}}(x) = L_{B_j}(x) + L_{B_j\{3}}(x/3)

So: L_i(s') ≥ L_j(s') + L_{B_j\{3}}(s'/3)

This gives the "double advantage": deeper evaluation AND additive boost.

**YOUR TASK:** Make this rigorous. Prove L_i(x) ≥ L_{B_j\{3}}(x) from the
quotient transport, or find a counterexample.

### Step 4: Comparison [GAP B — FILL THIS IN]

From Steps 2 and 3, the comparison reduces to:

  2t · [L_i(s') - 1] ≥ (s+1) · [L_i(t') + L_j(t)]

where s' ≥ ⌊(h/3)s⌋, t' ≥ ⌊(h/3)t⌋, h ≥ 5.

**For large h:** Both sides grow as ~th, but LHS has coefficient 2s vs
RHS coefficient (s+1). Since 2s ≥ s+1 for s ≥ 1, LHS dominates.

**For small h (h = 5, 7, 11, 13, 17):** Finite check needed.

**YOUR TASK:** Either prove the discrete inequality uniformly, or prove
it for large h analytically and verify small h by finite computation.
The computation has already been done (6,657 instances, zero failures,
minimum margin 134). You need to make it a PROOF, not just a verification.

### Step 5: All 29 kernels ✅
Follows from Steps 3-4 applied to each kernel. The parameter space is
finite and already enumerated.

---

## RULES

- Do NOT re-derive the 29-kernel classification. It's done.
- Do NOT re-derive the Quotient Transport Lemma. It's done.
- Do NOT propose a new framework. The skeleton is the framework.
- Do NOT verify EP-488 on examples. It's verified to 23M+ families.
- ONLY fill in Gap A (sieve monotonicity from quotient transport) and
  Gap B (the discrete inequality for all h).
- If Gap A is false, give an explicit counterexample.
- If Gap B requires case analysis, do the cases.
