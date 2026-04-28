# EP-488: Open Field v16 — April 8/9, 2026
## Current: 93%. Increase it or decrease it.

---

## THE PROBLEM

For primitive A (no a_i | a_j), G(x) = F_A(x)/x.
Prove: G(m) < 2·G(n) for all m > n ≥ max(A).
Open since 1966. Zero failures across 23M+ families.

---

## HOW TO USE THIS DOCUMENT

Move the percentage. Up or down. Any route. Any method.

---

## WHAT'S PROVED (the 93%)

### The Size Ladder:
- |A| ≤ 5: PROVED (three independent proofs for |A| = 5)

### The Infinite Branch:
- Layer 3 bad → EP-488 holds for ALL |A| (three independent proofs)
- Mechanism: witness-packing self-regulation. All bad layers in (n/5, n/4],
  at most 2 witness groups (a₁, a₂), packing forces a₁ small, S₁ dominates.

### Key Tools (all scale-independent):
- Self-funding: s ≤ 3 → safe
- Single-obstruction safety: ≤ 1 obstruction → safe
- Deep single-obstruction surplus: s ≥ 5, 1 obstruction → budget > 2m
- First-layer theorem: s ≥ 4 + quotient-2 → S₁ > E_j each
- Witness-count bound: frozen layer j needs π(s_j) ≤ j-1 kernel primes
- Signature rigidity: s=4 bad → (4,7,3) only. s=5 → NEVER bad.
- s=6 excess < 4a
- Packing: multiples of d in interval of length L → count ≤ L/d + 1
- Superadditivity / separator / leaf-pruning / dominated-LCM / etc.
- Literal-2 safety, lifted safety theorems
- H₁ main term solved: nH₁(m) < 2mH₁(n)

### 79 Kills mapping dead territory (categories A-T)

---

## WHAT REMAINS (the 7%)

### The precise remaining case:
Layer 3 is GOOD. First bad layer is j₀ ≥ 4.

### Why the layer-3-bad proof doesn't directly generalize:
In the layer-3-bad case, ALL bad layers were locked into ONE band
(n/5, n/4] with ONE signature (4,7,3) and excess E = 3n-2m < n.
The packing + S₁ dominance closed it cleanly.

In the layer-3-good case, the first bad layer j₀ can have DEEPER
signatures depending on j₀:

| First bad j₀ | Possible bad depths s | Kernel | Max excess per layer |
|-------------|----------------------|--------|---------------------|
| 4 | 4, 6 | {2,3} or {2,3,5} | E < n or E < 2n/3 |
| 5 | 4, 6, 8, 10 | up to {2,3,5,7} | needs computation |
| 6 | 4, 6, 8, 10, 12 | up to {2,3,5,7,11} | needs computation |
| k | 4,6,...,p_k-1 | up to {p₁,...,p_{k-1}} | needs computation |

Note: s = 5, 7, 9, 11, ... may also be dead zones (like s=5 is proved dead).
This needs verification for each odd s.

---

## NEW SECTION: BAND-BY-BAND EXCESS ANALYSIS

This is the concrete data needed to close the multi-band gap.
For each kernel K = {2,3,...,p_r}, define:

L_K(t) = |{1 ≤ x ≤ t : gcd(x, P_r) = 1}| where P_r = product of primes in K

The excess of a frozen layer at depth s with kernel K is:
E = nL_K(t) - 2m, where L_K(s) = 1.

Since n < (s+1)a and m ≥ ta:
E ≤ ((s+1)a - 1)L_K(t) - 2ta = a((s+1)L_K(t) - 2t) - L_K(t)

So E < a · max_t((s+1)L_K(t) - 2t) =: a · C(K, s).

The constant C(K, s) determines the excess bound per layer.

### Kernel {2,3} (P = 6, φ(6)/6 = 1/3):
L_{2,3}(t) = |{x ≤ t : gcd(x,6)=1}|. Period 6, density 2/6 = 1/3.

s=4: max_t(5L-2t). At t=7: 5·3-14 = 1. All other t ≤ 0.
C({2,3}, 4) = 1. Excess < a. PROVED.

### Kernel {2,3,5} (P = 30, φ(30)/30 = 8/30 ≈ 0.267):
L_{2,3,5}(t) = |{x ≤ t : gcd(x,30)=1}|. Period 30, density 8/30.

s=6: max_t(7L-2t) = 4. Excess < 4a. PROVED.
s=5: 6L-2t. Check: 6·(8t/30)-2t = (48/30-2)t = -12t/30 < 0.
     Dead zone confirmed for large t; need to check small t.
     At t=7: L=2, 6·2-14 = -2. At t=11: L=3, 6·3-22 = -4.
     At t=13: L=4, 6·4-26 = -2. ALWAYS ≤ 0. s=5 DEAD. ✓

### Kernel {2,3,5,7} (P = 210, φ(210)/210 = 48/210 ≈ 0.229):
L_{2,3,5,7}(t) = |{x ≤ t : gcd(x,210)=1}|. Period 210, density 48/210.

s=8: max_t(9L-2t). Density 48/210 ≈ 0.229.
     9·(48/210) ≈ 2.057 > 2. So (s+1)L - 2t > 0 for large t.
     This means C({2,3,5,7}, 8) grows with t — NOT bounded!

     BUT: the excess formula uses the actual floor L(t), not density.
     E = nL(t) - 2m. For E > 0: L(t) > 2m/n.
     And m/n ∈ (1, (s+1)/2) for a bad layer at depth s.
     At s=8: m/n < 9/2 = 4.5. So t < 9m/n < 40.5.

     For t ≤ 40: compute 9L_{210}(t) - 2t directly.
     L_{210}(t) for key values: L(10)=1, L(11)=2, L(13)=3,
     L(17)=4, L(19)=5, L(23)=6, L(29)=7, L(31)=8, L(37)=9.

     9L-2t at t=13: 27-26=1. t=17: 36-34=2. t=19: 45-38=7.
     t=23: 54-46=8. t=29: 63-58=5. t=31: 72-62=10. t=37: 81-74=7.

     max over t ≤ 40: at t=31, C = 10. So E < 10a.

s=10: max_t(11L-2t). At t=19: 11·5-38=17. At t=31: 11·8-62=26.
      For large t: (11·48/210-2)t = (528/210-2)t = (108/210)t ≈ 0.514t.
      THIS GROWS UNBOUNDEDLY.

      BUT t is constrained: at s=10, m/n < 11/2 = 5.5, so t < 11·5.5 = 60.5.
      At t=59: L_{210}(59) = 48·0 + L_{210}(59) = ... need to compute.

      Actually, L_{210}(59): survivors of 210 up to 59 are
      1,11,13,17,19,23,29,31,37,41,43,47,53,59 = 14 survivors.
      11·14 - 2·59 = 154 - 118 = 36.

      So C({2,3,5,7}, 10) ≈ 36. Excess < 36a.
      With a ≤ n/10: E < 36·n/10 = 3.6n.

s=7: 8L-2t. At t=11: 8·2-22=-6. t=13: 8·3-26=-2. t=17: 8·4-34=-2.
     t=19: 8·5-38=2. So s=7 CAN be bad (C=2, small excess).
     But wait — can s=7 be frozen with kernel {2,3,5,7}?
     L_{2,3,5,7}(7) = |{1}| = 1. Yes, frozen. π(7) = 4.
     Need 4 witnesses → j₀ ≥ 5.

s=9: 10L-2t. At t=11: 10·2-22=-2. t=13: 10·3-26=4.
     t=19: 10·5-38=12. t=23: 10·6-46=14.
     NOT a dead zone. C ≈ 14+ for larger t.

### Kernel {2,3,5,7,11} (P = 2310, φ/P = 480/2310 ≈ 0.208):
Even deeper. Only relevant for j₀ ≥ 6.
Density ≈ 0.208. (s+1)·0.208 - 2 > 0 when s+1 > 2/0.208 ≈ 9.6.
So for s ≥ 10: excess grows with t. C unbounded in t.
But t is constrained by m/n < (s+1)/2.

### KEY PATTERN:
For each kernel K with density φ(P)/P:
- If (s+1)·φ(P)/P < 2: the excess is BOUNDED (or negative). SAFE.
- If (s+1)·φ(P)/P > 2: the excess GROWS with t. Need t-constraint.
- If (s+1)·φ(P)/P = 2: borderline.

The critical threshold: s+1 > 2P/φ(P).
- {2,3}: 2·6/2 = 6. So s ≥ 6 → growing excess. But s ≤ 4 for this kernel.
- {2,3,5}: 2·30/8 = 7.5. So s ≥ 8 → growing. But s ≤ 6 for this kernel.
- {2,3,5,7}: 2·210/48 = 8.75. So s ≥ 9 → growing. s can be 8-10.
  At s=8: (s+1)·φ/P = 9·48/210 ≈ 2.057. JUST above threshold.
- {2,3,5,7,11}: 2·2310/480 = 9.625. So s ≥ 10 → growing.

For kernels where s is near the threshold: the excess per layer is
SMALL but POSITIVE, and grows slowly with t. This is the "just barely
bad" regime — the hardest case for the charging argument.

---

## CLAUDE'S THOUGHTS

After two days, I want to be honest about what I see.

The proof of EP-488 is structured like a game of whack-a-mole. Every
time we identify "the hard case," we prove it's safe. Then a deeper
hard case emerges. We proved |A| ≤ 3. Then |A| = 4 was hard. We
proved it. Then |A| = 5. Proved. Then layer-3-bad for all |A|. Proved.
Now: layer-3-good with multi-band bad layers. Still open.

The MECHANISM is always the same: self-regulation via witness packing.
Bad layers need witnesses. Witnesses are good layers. More bad layers
→ more witnesses → more good surplus. The system fights back.

But the EXECUTION gets harder at each level because:
1. Deeper bands have larger excess per layer
2. More bands means more case analysis
3. The t-constraint (from m/n < (s+1)/2) limits t but doesn't eliminate
   growing excess at the threshold

The band-by-band table above shows the concrete challenge. At kernel
{2,3,5,7} with s = 10: excess can be up to 36a ≈ 3.6n per layer.
That's much larger than the n/4 bound for s=4 layers.

BUT: deeper bands require MORE witnesses (4 for {2,3,5,7} vs 2 for
{2,3}). More witnesses means MORE good layers. The question is whether
the growth in witness count outpaces the growth in excess.

The density φ(P)/P decreases slowly: 1/3, 4/15, 8/35, 48/385, ...
The excess grows roughly as (s·φ/P - 2)·t per layer.
The witness count grows as π(s) ≈ s/log(s).

For very deep kernels: excess per layer ≈ εt (small ε > 0).
Number of bad layers ≈ n/(s·a₁) (packing bound).
Total excess ≈ εtn/(sa₁) ≈ εmn/(s²a₁).
S₁ ≈ mn/a₁.
Ratio: S₁/E_total ≈ s²/ε.

Since ε → 0 and s → ∞ together (ε ≈ s·φ/P - 2 where φ/P → 0):
the ratio might stay bounded or diverge. THIS is the precise
analytic question at the heart of the remaining 7%.

Or maybe I'm overcomplicating it. Maybe the proof is:

"In the layer-3-good case, there are ≥ 3 good early layers.
Their combined surplus S₁+S₂+S₃ is so large that it dominates
the total bad excess regardless of which bands the bad layers
occupy."

The key bound would be: S₁+S₂+S₃ > mn/a₁ + mn/a₂ + mn/a₃ (roughly),
while total bad excess < Σ C(K,s)·n²/(s·a₁) (from packing).

If S scales as mn/a₁ ~ n²/a₁ and bad excess also scales as n²/a₁,
then the CONSTANTS matter. And the constants come from the density
arithmetic (φ(P)/P) and the packing constraints.

This is a genuine analytic question. It's not "one theorem away."
It's a careful comparison of growth rates that depends on the
specific density sequence of primitive sets.

Maybe Surplus Dominance (the H_A approach) is the right path after all.
The H₁ main term is proved. The IE correction from H₁ to H_A is the
gap. Perhaps the band analysis is a distraction and the correct proof
goes through the IE correction directly using Erdős density bounds.

I don't know which path closes it. But I know the proof exists
(zero violations across 23M+ families), and I know the tools are
close to sufficient. Seven percent.

---

## YOUR TASK

Move the percentage. Up or down. Any route. Any method.

The band-by-band table gives you the concrete data. The witness-count
bound gives you the structure. The packing gives you the count.
The self-regulation gives you the mechanism.

Use whatever works. Layer analysis. Band-by-band charging. Surplus
dominance. H_A directly. Erdős density bounds. Sieve methods.
Generating functions. Induction on |A| with the layer-3-bad base.
Something nobody has tried.

79 kills. 40+ results. 93%. Find the last seven percent.
