# EP-488: Critical Correction — Coprimality vs. Divisibility Avoidance
## April 5, 2026 — After GPT compute scan of 148,885 primitive sets

---

## THE ERROR

The entire analysis chain (Claude + 5.4 Pro + 5.2 Pro) was built on the
WRONG interpretation of K_Q(y).

**What 5.4 Pro originally wrote (layer-decomposition-framework.md):**
  K_Q(y) = y - F_Q(y)  (complement count)

This means: L_j(y) = #{n ≤ y : b ∤ n ∀ b ∈ B_j} — DIVISIBILITY AVOIDANCE.

**What we all started computing with:**
  K_Q(y) = #{n ≤ y : gcd(n, q) = 1 ∀ q ∈ Q} — COPRIMALITY.

**These are NOT the same.** Example: n = 6, b = 4.
  - 4 ∤ 6 ✓ (L_j counts this)
  - gcd(6, 4) = 2 ≠ 1 ✗ (coprimality does NOT count this)

**Consequence:** The coprimality version is a STRICT UNDERCOUNT.
Counterexample: A = {10, 21}, x = 30.
  - Coprimality layer sum: 3
  - True F_A(30): 4

The compute scan confirms: coprimality decomposition fails for 99.9% of
primitive sets.

---

## WHAT THE CORRECT DECOMPOSITION IS

Sort A = (a_1 < ... < a_k). Assign each multiple n to the SMALLEST a_j | n.

B_j = {a_i / gcd(a_i, a_j) : i < j, quotient > 1}

L_j(y) = #{n ≤ y : b ∤ n for every b ∈ B_j}

F_A(x) = Σ_j L_j(⌊x/a_j⌋)    ← EXACT for all primitive sets

This was verified across all 148,885 scanned sets.

---

## WHAT SURVIVES

1. **The layer decomposition structure** — still exact and valid with L_j.
2. **The constant-mean observation** — L_j(y) ≈ d_j · y where d_j is the
   density of integers avoiding divisibility by B_j. So T_j(x) ≈ r_j · d_j.
3. **5.2's collective oscillation budget V + 2U < C** — this is a general
   algebraic fact, independent of which function we use.
4. **EP-488 itself** — max true ratio in scan was 1.9899 (singleton {99}).
   Zero failures across 148,885 sets.

---

## WHAT'S INVALIDATED

1. **All φ(q)-based discrepancy bounds** — these apply to coprime counts,
   not to non-divisibility counts.
2. **The structural inequality Σ ρ_j(r_j - 3q_j - 2) > 0** — already
   killed (Kill #47), but doubly dead now.
3. **5.4 Pro's windowed active-prime bound** — correct for coprime counts,
   but needs reformulation for L_j.
4. **The phase mixing / Fourier blueprint** — conceptually still valid
   but the frequencies and periods need to use lcm(B_j), not q_j.

---

## THE CORRECT ANALYSIS FOR L_j

L_j has an inclusion-exclusion expansion:

  L_j(y) = Σ_{S ⊆ B_j} (-1)^|S| · ⌊y / lcm(S)⌋

This gives:
- **Period:** lcm(B_j) (not q_j = ∏ primes)
- **Density:** d_j = Σ_{S ⊆ B_j} (-1)^|S| / lcm(S) (NOT ∏(1-1/b))
- **Discrepancy:** |L_j(y) - d_j·y| ≤ 2^|B_j| - 1

### Key difference from coprimality:
The period lcm(B_j) can be MUCH SMALLER than q_j = ∏ primes of Q_j,
because the B_j elements may share prime factors (and we take lcm, not product).

### Windowed bound analogue:
For y ≤ 10r_j, any b ∈ B_j with b > 10r_j is automatically inactive
(b ∤ n for all n ≤ 10r_j, since n < b). So:

  L_j(y) = L_{B_j^{active}}(y)

where B_j^{active} = {b ∈ B_j : b ≤ 10r_j}.

This is STRONGER than the active-prime analogue because we eliminate
entire COMPOSITE moduli, not just individual primes.

### The correct excursion bound:

  |D_j(y)| ≤ 2^|B_j^{active}| - 1

where B_j^{active} = {b ∈ B_j : b ≤ 10r_j}.

For tail layers (r_j ≈ 1): B_j^{active} = {b ∈ B_j : b ≤ 10}.
Since B_j elements are quotients a_i/gcd(a_i, a_j) for i < j, and
primitive sets have no divisibility, these quotients are ≥ 2.
The elements ≤ 10 are {2, 3, 4, 5, 6, 7, 8, 9, 10} — at most 9.
So 2^|B_j^{active}| ≤ 2^9 = 512.

But: how many quotients actually land in [2, 10]? For a tail layer
(a_j ≈ M), the quotients a_i/gcd(a_i, a_j) can be large (≈ a_i)
unless a_i and a_j share many factors.

---

## IMMEDIATE NEXT STEPS

### 1. RERUN the compute session with the CORRECT L_j
Compute:
- d_j (density of divisibility-avoidance) for each layer
- c_j = r_j · d_j (correct main term)
- Actual excursions v_j, u_j of L_j-based T_j
- |B_j^{active}| for each layer
- The collective criterion V + 2U < C with correct L_j

### 2. Send 5.4 Pro the CORRECTED framework
The structural question becomes: for the correct B_j and L_j,
does the collective oscillation budget hold?

### 3. Revisit 5.2's reformulation
V + 2U < C is still the right condition, but c_j, u_j, v_j all
change with the correct L_j. The reformulation survives — only
the bounds plug-in changes.

---

## HONEST ASSESSMENT

### What this means for the percentage:
The correction doesn't change the PROVED THEOREMS (pairs, triples,
consecutive k-tuples, etc. — those proofs don't use the layer decomposition).

But the layer-decomposition path to the general case just had its
foundation rebuilt. We're not starting from zero — the correct
decomposition F_A = Σ L_j(⌊x/a_j⌋) is known and verified — but
all the bounds infrastructure needs to be redone with L_j instead
of K_Q.

**Revised percentage: 55-60%.** The proved special cases are solid.
The general strategy (layers → collective budget → bound excursions)
is still viable. But we need to redo the analysis with the right function.

## KILL COUNT: 48
Kill #48: Coprimality model K_Q(y) = #{gcd(n,q)=1} as exact decomposition.
Counterexample: A = {10, 21} at x = 30.
True count F_A(30) = 4, coprimality layer sum = 3.
