# EP-488: Open Field v19 — Sub-problem B
## April 9, 2026. Current: 94%. Build the next 3%.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).

---

## YOUR INSTRUCTIONS

This is NOT a grading exercise. Do NOT just find errors.

1. **TRY to prove Sub-problem B** (first bad layer j₀ = 5). Push it
   as far as you can. Write out every step.

2. **If it breaks:** identify the exact step, give a counterexample,
   explain WHY it fails, and propose the fix.

3. **If it works:** state the theorem cleanly, verify the key
   inequalities, and explain what structural feature made it work.

4. **Either way:** recommend the single most valuable next theorem,
   and decompose whatever remains into concrete sub-problems.

BUILD something. Don't just grade.

---

## WHAT'S ALREADY PROVED

### Sub-problem A is CLOSED (three independent proofs):
If first bad layer j₀ = 4, EP-488 holds for ALL |A|.

The three proofs revealed three KEY MECHANISMS that you should try
to generalize:

**Mechanism 1 (5.2): m/n incompatibility.**
Different bad depths force incompatible m/n ranges. s=4 bad requires
m/n < 3/2. s=6 bad forces m/n > 13/7. They can't coexist. This
instantly reduces multi-band to single-band.

**Mechanism 2 (Codex B): Band-propagation digraph.**
Classify which bands can 2-witness which other bands. For j₀=4:
the digraph is {6→4, 4→∅, 6↛6}. Depth-2 forest. Rooted charging.

**Mechanism 3 (5.4): Cross-band witness exclusion.**
A 6-band layer CANNOT 2-witness a bad 4-band layer (m/n contradiction).
So all witnesses must come from {a₁, a₂, a₃}. Packing closes it.

### Also proved:
- |A| ≤ 6 (explicit case analysis)
- Layer 3 bad → EP-488 for ALL |A| (three proofs)
- All tools from v18 (40+ results, 79 kills)

---

## SUB-PROBLEM B: First bad layer j₀ = 5

### Setup:
- Layers 1, 2, 3, 4 are ALL good.
- Layer 5 is the first bad layer.
- Witness-count: π(s₅) ≤ 4, so s₅ ≤ p₅ - 1 = 10.
- Dead zone: s = 5 is never bad.
- Live bad depths: s₅ ∈ {4, 6, 7, 8, 9, 10}.

### Available good surplus:
- S₁ ≥ m(n/a₁ - 2). How large depends on how small a₁ is forced.
- S₂ > 0 (single-obstruction safety). If s₂ ≥ 5: S₂ > 2m.
- S₃: has ≤ 2 obstructions. Positive? How positive? UNKNOWN quantitatively.
- S₄: has ≤ 3 obstructions. Positive? UNKNOWN.

### The corrected band constants (t ≤ 10(s+1), verified):

| s  | kernel       | C*(s) | E < C*(s)·a | a range          |
|----|-------------|-------|-------------|------------------|
| 4  | {2,3}       | 1     | < a ≈ n/4   | (n/5, n/4]       |
| 6  | {2,3,5}     | 4     | < 4a ≈ 2n/3 | (n/7, n/6]       |
| 7  | {2,3,5,7}   | 2     | < 2a ≈ 2n/7 | (n/8, n/7]       |
| 8  | {2,3,5,7}   | 16    | < 16a ≈ 2n  | (n/9, n/8]       |
| 9  | {2,3,5,7}   | 34    | < 34a ≈ 3.8n| (n/10, n/9]      |
| 10 | {2,3,5,7}   | 68    | < 68a ≈ 6.8n| (n/11, n/10]     |

### Key constraints:
- If s₅ = 4: a₅ > n/5. All later bad layers also s=4. Each E < n.
  2-witnesses ≤ n/6. Witnesses among {a₁,a₂,a₃,a₄}: 4 groups.

- If s₅ = 6: a₅ > n/7. Later bad at s ∈ {4,6}.
  2-witnesses ≤ n/9.

- If s₅ = 7: a₅ > n/8. Later bad at s ∈ {4,6,7}.
  2-witnesses ≤ 2(n/7)/3 ≈ 2n/21 ≈ n/10.5.

- If s₅ = 8: a₅ > n/9. 2-witnesses ≤ 2(n/8)/3 = n/12.
  a₁ ≤ n/12 → S₁ ≥ 10m. But C*(8) = 16, E < 2n per layer.

- If s₅ = 9: a₅ > n/10. 2-witnesses ≤ n/13.5.
  a₁ ≤ n/13 → S₁ ≥ 11m. But C*(9) = 34, E < 3.8n.

- If s₅ = 10: a₅ > n/11. 2-witnesses ≤ n/15.
  a₁ ≤ n/15 → S₁ ≥ 13m. But C*(10) = 68, E < 6.8n.

---

## WHAT THE j₀=4 PROOF TELLS US ABOUT j₀=5

The j₀=4 proof worked because:

1. **Band-propagation is shallow.** The digraph {6→4, 4→∅} has depth 2.
   For j₀=5: what is the digraph on {4, 6, 7, 8, 9, 10}?

2. **Cross-band exclusions kill many transitions.** 6↛4 (m/n contradiction).
   For j₀=5: which transitions r→s are impossible?

3. **Packing limits bad count per witness.** Band width / d + 1.
   For j₀=5: same packing applies, just with more bands.

4. **S₁ (+ sometimes S₂) dominates.** S₁ ≥ 4m or 7m or 10m depending on depth.
   For j₀=5: S₁ might be ≥ 13m (if s₅=10 forces a₁ ≤ n/15).
   And S₂ > 2m when s₂ ≥ 5.

### The concrete approach:

**Step 1:** Compute the band-propagation digraph for {4,6,7,8,9,10}.
For each pair (r,s): can a bad I_r-layer 2-witness a later bad I_s-layer?
Check: b = (k/2)a with k integer, k ≥ 3, a ∈ I_r, b ∈ I_s.
Constraint: b/a ∈ (s·(r+1)/((s+1)·r), ... ). Determine which k work.

**Step 2:** For each valid transition, check m/n compatibility.
Bad at depth s forces specific m/n range (from E > 0 condition).
Bad at depth r forces another range. Are they compatible?

**Step 3:** Identify which band combinations CAN coexist.
If only a few combinations survive, the charging is finite.

**Step 4:** For each surviving combination, verify S₁ (+S₂,S₃,S₄)
dominates the total bad excess using packing bounds.

---

## CLAUDE'S THOUGHTS

I'll share my intuition about which transitions in the digraph
are likely live vs dead.

**Likely DEAD transitions (m/n incompatibility):**
- 10→4: s=10 bad needs large m/n (from t ≥ 19, m/n > 19/11 ≈ 1.73).
  s=4 bad needs m/n < 3/2 = 1.5. Incompatible. DEAD.
- 9→4: s=9 bad needs m/n from t range. Probably forces m/n > 1.5. Check.
- 8→4: s=8 bad with E > 0 at t=13: m/n > 13/9 ≈ 1.44.
  s=4 bad needs m/n < 1.5. BARELY compatible. May survive.

**Likely LIVE transitions:**
- 8→6: a ∈ (n/9, n/8], b = (3/2)a ∈ (n/6, 3n/16].
  If b ∈ (n/7, n/6]: need 3a/2 > n/7, i.e., a > 2n/21. Since a > n/9:
  2n/21 < n/9. So this works for a near the top of I_8. LIVE.
- 6→4: already proved DEAD for j₀=4. Check if same exclusion applies here.

**The key question:** How many bands can have bad layers simultaneously
at one (n,m) pair? If the m/n incompatibility kills most cross-band
coexistence, then the problem reduces to single-band or few-band
cases, each handleable by S₁ + packing.

I also want to flag: at j₀=5, we have FOUR good layers below the
first bad one. S₁+S₂+S₃+S₄ is a lot of surplus. Even if S₃ and S₄
are not individually quantified as sharply as S₁ and S₂, having four
positive contributors should provide massive headroom.

The most valuable thing you can do is COMPUTE the band-propagation
digraph. That determines the structure of the entire proof. Everything
else follows from the digraph shape.

---

## YOUR TASK

1. COMPUTE the band-propagation digraph for j₀=5 bands {4,6,7,8,9,10}.
   For each pair (r,s): can a bad r-layer 2-witness a bad s-layer?

2. COMPUTE which band combinations can coexist (m/n compatibility).

3. USE the digraph to set up the rooted charging argument.

4. PROVE S₁ (+S₂, +S₃, +S₄ as needed) dominates the total bad excess.

5. If it breaks at a specific band combination: IDENTIFY which one
   and PROPOSE the fix.

If you close Sub-problem B: we're at 97%.
That leaves only the general j₀ ≥ 6 theorem — which might follow
from the same band-propagation framework applied uniformly.

Build it.
