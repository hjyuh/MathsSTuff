# EP-488: Prove the Primitive-Compatibility Lemma (Last Gap)
## For Codex xhigh — April 7, 2026

You just proved Box 1 and identified the exact remaining gap for Box 2.
Now close it.

---

## WHAT YOU PROVED

Box 1 ✅: E_j ≤ 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋)  (child excess ≤ 3-tax)

Box 2 abstract counterexample: C={2}, parent B={2,5}, a_j=20, a_i=12
gives parent slack 160 < tax 200. BUT you showed this is killed by
primitivity: the element creating obstruction 5 at a_i=12 must divide
a_j=20, violating primitivity.

## THE EXACT GAP

Prove: **Any parent obstruction profile that would make Box 2 fail is
primitive-incompatible with a bad compact child carrying the 3-edge.**

More precisely: if a_i = 3g, a_j = hg, gcd(h,3) = 1, h ≥ 5, and the
child has bad kernel K ⊇ {2,3}, then any obstruction b ∈ B_i that is
"small enough" to make the parent's sieve too strong (reducing L_i(s')
below what Box 2 needs) must come from an element a_k that divides a_j,
contradicting primitivity.

## THE ARGUMENT TO FORMALIZE

You already sketched the key observation: to get obstruction b at
a_i = 3g, you need element a_k with a_k/gcd(a_k, 3g) = b.

If b is a small prime p, then a_k = p · gcd(a_k, 3g). For this
obstruction to be "dangerous" (making L_i small), p must be small
(2, 3, 5, 7, etc.).

Now check: does a_k divide a_j = hg?

The quotient transport gives q_{k,j} | 3·q_{k,i} = 3b. So q_{k,j}
divides 3b. If q_{k,j} = 1, then a_k | a_j, contradicting primitivity.

So q_{k,j} > 1 (a_k doesn't divide a_j). But q_{k,j} | 3b, so
q_{k,j} ∈ {divisors of 3b greater than 1}.

The question: for which values of b does the constraint q_{k,j} | 3b
with q_{k,j} > 1 allow a parent obstruction profile that defeats Box 2?

## WHAT TO PROVE

Either:

(A) For every bad compact child (K ⊇ {2,3}, (s,t) violating, h ≥ 5)
and every PRIMITIVE-COMPATIBLE parent obstruction set B_i, the parent
slack S_i = 2m·L_i(s') - n·L_i(t') exceeds the 3-tax T = 2m·L_C(⌊s/3⌋) - n·L_C(⌊t/3⌋).

Or:

(B) Find an actual primitive set A where Box 2 fails (you checked 6,202
instances and found zero failures, so this is unlikely).

## APPROACHES

1. **Direct primitive constraint.** Show that for each dangerous small
obstruction b at the parent, the element a_k creating it satisfies
a_k | a_j (contradicting primitivity) or a_k creates a compensating
effect elsewhere.

2. **Finite case analysis.** The bad signatures are finite (29 kernels,
s ≤ 4, t ≤ 20, h takes finitely many primitive-compatible values for
each kernel). Enumerate the possible parent obstruction sets that are
primitive-compatible and verify Box 2 for each.

3. **Cash-flow argument.** From the D = 2m - n identity: parent slack =
D·L_i(s') - n·Δ_i. Show that primitive-compatible B_i always gives
L_i(s') ≥ 3 (because dangerous small obstructions are excluded by
primitivity), which combined with D > n gives enough slack.

4. **Combine with quotient transport.** q_{k,j} | 3·q_{k,i}. If
q_{k,i} = b (parent obstruction), then q_{k,j} | 3b. If q_{k,j} > 1
(primitivity), then a_k contributes obstruction q_{k,j} to the CHILD's
kernel. But the child's kernel is already classified (one of 29). This
constrains which parent obstructions can coexist with which child kernels.

## RULES
- Do not re-derive Box 1. It's proved.
- Do not re-derive the abstract counterexample. It's done.
- Focus ONLY on proving the primitive-compatibility lemma or finding
  a real counterexample.
- If it reduces to a finite check, state the check precisely and verify it.
