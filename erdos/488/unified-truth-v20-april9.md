# EP-488: Open Field v20 — The Root Package Lemma
## April 9, 2026. Current: 95%. Build the next 2%.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).

---

## YOUR INSTRUCTIONS

BUILD something. Do NOT just critique.

1. TRY to prove the root package lemma for s₅ ∈ {9, 10}.
2. If it breaks: exact step, counterexample, WHY, proposed fix.
3. If it works: clean theorem, verified inequalities, structural insight.
4. Either way: recommend next steps, decompose what remains.

---

## WHAT'S PROVED

### Sub-problem A: CLOSED (three independent proofs)
If first bad layer j₀ = 4: EP-488 holds for ALL |A|.

### Sub-problem B partially closed (5.4):
If j₀ = 5 and s₅ ∈ {4, 6, 7, 8}: EP-488 holds.

### Remaining for Sub-problem B:
s₅ ∈ {9, 10} only.

### The layer-3-bad theorem: ALL |A| (three proofs).
### Size ladder: |A| ≤ 6.
### 40+ tools, 79 kills.

---

## THE FULLY COMPUTED BAND-PROPAGATION DIGRAPH

For bands {4, 6, 7, 8, 9, 10}:

Geometric edges (b = (k/2)a maps I_r → I_s):
  6→4, 7→4, 9→6, 10→4, 10→6, 10→7

m/n incompatibility kills:
  6→4 DEAD (U₄ ∩ U₆ = ∅)
  7→4 DEAD (U₄ ∩ U₇ = ∅)

LIVE bad-to-bad digraph:
  9→6,  10→4,  10→6,  10→7

For s₅ ≤ 8: NO live edges. All bad layers witnessed by good layers only. PROVED.

For s₅ = 9: ONE edge (9→6). Bad 9-root can spawn bad 6-children.
For s₅ = 10: THREE edges (10→4, 10→6, 10→7). Bad 10-root can spawn 4/6/7-children.

---

## CORRECTED BAND CONSTANTS (t ≤ 10(s+1), verified)

| s  | kernel       | C*(s) | E < C*(s)·a |
|----|-------------|-------|-------------|
| 4  | {2,3}       | 1     | < a         |
| 6  | {2,3,5}     | 4     | < 4a        |
| 7  | {2,3,5,7}   | 2     | < 2a        |
| 8  | {2,3,5,7}   | 16    | < 16a       |
| 9  | {2,3,5,7}   | 34    | < 34a       |
| 10 | {2,3,5,7}   | 68    | < 68a       |

---

## THE TWO REMAINING CASES

### Case s₅ = 9

The live edge is 9→6 only.

A bad 9-band element w ∈ (n/10, n/9] can 2-witness a bad 6-band
element a ∈ (n/7, n/6]. The transition is a = (h/2)w with h odd.

Band ratio: a/w ∈ ((n/7)/(n/9), (n/6)/(n/10)) = (9/7, 10/6) = (9/7, 5/3).
So h = 2a/w ∈ (18/7, 10/3) = (2.57, 3.33). Only odd h = 3 works.
So a = (3/2)w. AT MOST ONE 6-child per 9-root.

The root package for one 9-band root w:
- Root excess: E_w < 34w (from C*(9))
- Child excess (if exists): E_child < 4·(3w/2) = 6w (from C*(6))
- Total package: < 40w

Since w ∈ (n/10, n/9]: total package < 40·(n/9) ≈ 4.4n.

Now: a₁ ≤ 2w/3 ≤ 2(n/9)/3 = 2n/27.
So n/a₁ ≥ 27/2 = 13.5, hence S₁ ≥ m(13.5 - 2) = 11.5m > 11.5n.

But there could be MANY 9-band roots, each with its own child.
Each root needs a 2-witness from {a₁,...,a₄}.
Packing in I₉ = (n/10, n/9], length n/90:
  Per witness aᵢ: count ≤ n/(90·(aᵢ/2)) + 1 = n/(45aᵢ) + 1.
  Total 9-roots ≤ 4·(n/(45a₁) + 1) = 4x₁/45 + 4.

Each root's package < 40·(n/9) ≈ 4.4n. But this overestimates —
the root a has E < 34a, not 34·(n/9). Use E < 34a for each root.

Total 9-package excess: Σ (34w + 6·(3w/2)) = Σ 43w.
Since each w > n/10: total < 43·(n/9)·(4x₁/45+4) ≈ ...

Actually, pack more carefully. Each 9-root w is a multiple of d_i = a_i/2.
In I₉ of length n/90: count per witness ≤ n/(45a_i) + 1 ≤ x_i/45 + 1.

BUT: the 6-children of 9-roots are ALSO bad layers. Do they also need
witnesses from {a₁,...,a₄}? YES — their 2-witness is w (the 9-root).
But w is a BAD layer, not a good layer. So the 6-child's witness IS
the bad root. The child doesn't consume a good witness slot.

So the packing is: only 9-roots consume good witness slots.
Total 9-roots ≤ 4x₁/45 + 4.
Each root's package excess: E_root + E_child < 34w + 6w = 40w ≤ 40·(n/9).

But also DIRECT bad layers in other bands (4,6,7,8) might exist,
witnessed by {a₁,...,a₄}. These are the same as in the s₅≤8 cases
(already handled). Need to verify they don't interact with the 9-packages.

### Case s₅ = 10

Three live edges: 10→4, 10→6, 10→7.

A bad 10-band root w ∈ (n/11, n/10] can spawn:
- 4-children: a = (k/2)w with a ∈ (n/5, n/4]. So a/w ∈ (11n/(5n), 10n/(4n)) ≈ (2.2, 2.5). h = 2a/w. Need h odd. h ∈ (4.4, 5.0). No odd integer! Wait — h could be 5? 4.4 < 5 < 5.0. YES, h = 5. So a = (5/2)w.
- 6-children: a = (h/2)w with a ∈ (n/7, n/6]. a/w ∈ (10/7, 11/6) ≈ (1.43, 1.83). h ∈ (2.86, 3.67). Only h = 3. So a = (3/2)w.
- 7-children: a = (h/2)w with a ∈ (n/8, n/7]. a/w ∈ (10/8, 11/7) ≈ (1.25, 1.57). h ∈ (2.5, 3.14). Only h = 3. So a = (3/2)w.
  BUT wait: (3/2)w ∈ (n/8, n/7] requires w ∈ (2n/21, 2n/14) = (n/10.5, n/7). The 10-band has w ∈ (n/11, n/10]. So (3/2)w ∈ (3n/22, 3n/20) = (n/7.33, n/6.67). Is this in I₇ = (n/8, n/7]? 
  n/7.33 > n/8 ✓ but n/6.67 > n/7 ✗ for some values. Need 3w/2 ≤ n/7, i.e., w ≤ 2n/21. Since w > n/11 and 2n/21 ≈ n/10.5: only w close to n/11 works.

So the 10-root package has AT MOST:
- One 4-child (a = 5w/2, if it lands in I₄)
- One 6-child (a = 3w/2, always lands in I₆ for this range)
- One 7-child (a = 3w/2, only for w near n/11)
  WAIT: 6-child and 7-child both use h=3, so a = 3w/2. It lands
  in ONE band depending on the value of w. Not both.

So each 10-root has at most TWO children: one from h=5 (4-child)
and one from h=3 (6-or-7-child). Package excess:
  E_root < 68w (C*(10))
  E_{4-child} < 5w/2 = 2.5w (C*(4)=1, a=5w/2, E < a = 5w/2)
  E_{6-child} < 4·(3w/2) = 6w (C*(6)=4)
  E_{7-child} < 2·(3w/2) = 3w (C*(7)=2)

Total package: < 68w + 2.5w + 6w = 76.5w (worst case with 4-child + 6-child).

Since w ≤ n/10: package < 7.65n per root.

---

## WHAT YOU NEED TO PROVE

### For s₅ = 9:
Show that the total excess from all 9-root packages PLUS any
remaining non-package bad layers is dominated by S₁ + S₂ + S₃ + S₄.

Key bounds to use:
- 9-roots: ≤ 4x₁/45 + 4 total, each package < 40w ≤ 40n/9
- Non-package bad at s∈{4,6,7,8}: same as s₅≤8 cases (already proved safe)
- a₁ ≤ 2n/27, so S₁ ≥ 11.5m > 11.5n
- S₂ > 2m > 2n (deep single-obstruction, since a₂ < a₅ ≤ n/9 < n/5)
- S₃, S₄: positive but unquantified. Even S₃ = S₄ = 0 might work.

### For s₅ = 10:
Show that total excess from all 10-root packages (each < 76.5w)
plus any remaining bad layers is dominated by S₁ + S₂ + S₃ + S₄.

Key bounds:
- 10-roots: packing in I₁₀ = (n/11, n/10], length n/110
  ≤ 4·(n/(55a₁) + 1) = 4x₁/55 + 4
- Each package < 76.5·(n/10) = 7.65n
- a₁ ≤ 2(n/10)/3 = n/15, so S₁ ≥ 13m > 13n
- S₂ > 2m > 2n
- S₁ + S₂ > 15n. Need total excess < 15n.

Check: (4x₁/55 + 4)·7.65n. At x₁ = 15: (60/55+4)·7.65n ≈ 5.09·7.65n ≈ 39n.
That's > 15n. S₁ + S₂ alone MIGHT NOT suffice!

BUT: 7.65n per root is the CRUDE bound. The actual root excess uses
E < C*(s)·a, not C*(s)·(n/s). Each root w has E < 68w, and the TOTAL
across all roots is Σ 76.5·wⱼ. The packing bound gives Σ wⱼ ≤ ...(something proportional to n²/a₁). So the total excess scales as n²/a₁, and S₁ also scales as mn/a₁ ≈ n²/a₁.

The ratio S₁/(total excess) ≈ m/n · (constant). Since m > n, this
ratio exceeds 1 if the constant is close to 1. The exact constant
depends on the packing arithmetic.

This is the EXACT computation that needs to be done.

---

## CLAUDE'S THOUGHTS

The s₅ = 9 case should fall easily — each 9-root has at most ONE
child, and the total package per root (40w) is moderate.

The s₅ = 10 case is tighter because:
1. C*(10) = 68 is large
2. Each root can have up to TWO children
3. The per-root package (76.5w) is large
4. The crude "per root × number of roots" might exceed S₁ + S₂

The FIX (if the crude bound fails) is to use the EXACT packing:
total excess = Σ_roots (68wⱼ + children) = 76.5 · Σ wⱼ.
And Σ wⱼ ≤ n²/(s(s+1)·a₁) = n²/(110·a₁) = x₁n/110.
So total excess ≤ 76.5 · x₁n/110 ≈ 0.695·x₁·n.
And S₁ > n(x₁ - 2).
Need x₁ - 2 > 0.695·x₁, i.e., 0.305·x₁ > 2, i.e., x₁ > 6.56.
Since x₁ ≥ 15: TRUE with massive margin!

WAIT — did I just close s₅ = 10?

Let me recheck: Σ wⱼ summed over all 9-roots or 10-roots. Each
wⱼ is a multiple of some dᵢ = aᵢ/2, lying in I_s. So:
Σ_{roots witnessed by aᵢ} wⱼ ≤ Σ_{multiples of dᵢ in I_s} (n/s)
= (count) · (n/s) ≤ (n/(s(s+1)dᵢ) + 1) · (n/s).

Hmm, this overestimates because each wⱼ ≤ n/s, not = n/s.
The EXACT sum is Σ wⱼ where wⱼ are multiples of dᵢ in I_s.
These are dᵢ, 2dᵢ, ..., up to n/s. So Σ ≤ (n/s)² / (2dᵢ) roughly.

Actually, the simpler approach: use the per-element excess bound.
Each root w has package excess < 76.5w.
S₁ contribution per witness aᵢ: S₁ ≥ m(xᵢ - 2) (allocated to aᵢ's group).

For witness aᵢ's group of 10-roots:
Total package excess = Σ 76.5·wⱼ where each wⱼ is a multiple of aᵢ/2.
And S₁ (prorated to this group) ≈ m·xᵢ/4 (one-fourth of total S₁).

The ratio: m·xᵢ/(4·76.5·Σwⱼ). Since Σwⱼ < n·count/(s) and
count ≤ xᵢ/(s(s+1)/2): Σwⱼ < n·xᵢ/(s²(s+1)/2).

For s = 10: Σwⱼ < n·xᵢ/550.
Ratio = m·xᵢ / (4·76.5·n·xᵢ/550) = 550m/(306n) ≈ 1.8·m/n > 1.8.

That's > 1. The charging works!

I think s₅ = 10 IS closable with careful arithmetic. The models
should verify this computation and make it rigorous.

---

## YOUR TASK

1. PROVE the root package lemma for s₅ = 9. This should be
   straightforward: each root has ≤ 1 child, package < 40w.

2. PROVE the root package lemma for s₅ = 10. Tighter but doable:
   each root has ≤ 2 children, package < 76.5w. Use EXACT packing
   of Σ wⱼ against S₁ to get the ratio > 1.

3. If BOTH close: Sub-problem B is DONE. We're at 97%.
   Then the remaining 3% is Sub-problems C+D (j₀ ≥ 6 + unification).

4. If either breaks: identify the exact failure and propose the fix.

Build it.
