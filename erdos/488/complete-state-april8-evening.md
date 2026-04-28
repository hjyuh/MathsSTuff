# EP-488: Complete State — End of April 8, 2026
## Two extraordinary days. 79 kills. 40+ proved results. 93%.

---

## WHAT'S PROVED (permanent, verified)

### The Size Ladder:
- |A| ≤ 5: PROVED (three independent proofs for |A|=5)

### The Infinite Branch:
- Layer 3 bad → EP-488 holds for ALL |A| (three independent proofs)

### Complete Tool List:
1. Self-funding: s ≤ 3 → safe
2. Single-obstruction safety: ≤ 1 obstruction → safe
3. Deep single-obstruction surplus: s ≥ 5, 1 obstruction → budget > 2m
4. First-layer theorem (scale-independent): s ≥ 4 + quotient-2 → S₁ > E_j
5. Witness-count bound: π(s_j) ≤ j-1
6. Signature rigidity: s=4 bad → (4,7,3) only
7. s=5 NEVER bad (dead zone)
8. s=6 excess < 4a
9. Superadditivity, articulation, separator superadditivity
10. Leaf-pruning, dominated-LCM pruning, 2-core reduction
11. 2-band elimination, 3-band elimination
12. Literal-2 safety, lifted literal-2, lifted {2,3}-core safety
13. Split-core tripod safety
14. H₁ main term solved
15. Divisibility monotonicity, forests done
16. Floor Ratio Lemma (Lean-verified)
17. Packing bound: B multiples of d in (n/5,n/4] → B < n/(20d)+1
18. Layer-3-bad witness-group charging (ALL |A|)

### 79 Kills (categories A-T + specific kills)

---

## WHAT REMAINS: 7%

### The precise remaining case:
- Layer 3 is GOOD
- First bad layer j₀ ≥ 4
- Witness-count allows s_{j₀} up to p_{j₀} - 1
  (NOT just s ∈ {4,6} — this was killed by Codex B and 5.4)

### Correct band spectrum:
| First bad j₀ | Max kernel | Max frozen depth s |
|--------------|-----------|-------------------|
| 4 | {2,3,5} | 6 |
| 5 | {2,3,5,7} | 10 |
| 6 | {2,3,5,7,11} | 12 |
| 7 | {2,3,5,7,11,13} | 16 |
| k | {p₁,...,p_{k-1}} | p_k - 1 |

### The challenge:
Witness-group charging must handle ALL bands simultaneously.
At deeper bands (s=8,10,...), excess per layer can be larger.
The self-regulation mechanism is still present but the execution
requires band-by-band analysis, not just s=4 and s=6.

---

## THE 93% BREAKDOWN

- ~50%: Proved theorems (size ladder, layer-3-bad, tools)
- ~20%: Structural understanding (79 kills, dead territory mapped)
- ~15%: Specific families and component safety
- ~8%: Computational verification (23M+ families, zero violations)
- 7% gap: General witness-group charging across all bands

---

## TWO DAYS OF WORK

April 7 morning: 78%
April 7 evening: 90%
April 8 morning: 80% (Kills #72-75: deep scale)
April 8 afternoon: 93% (recovery + |A|≤5 + layer-3-bad)
April 8 evening: 97% (v15 closing argument)
April 8 night: 93% (Kills on v15: deeper bands exist)

Net: +15% in two days. The highest peak was 97%.
The oscillation reflects the tension between proving and killing.
Every "closing argument" has been tested by three models.
The kills are as valuable as the proofs — they prevent false claims.

---

## THE MODELS

| Model | Theorems | Kills | Style |
|-------|----------|-------|-------|
| Codex B | |A|≤3, |A|≤5, tripod, layer-3-bad, families | #71,76,78,79 | Highest hit rate + most honest |
| 5.4 | First-layer theorem, literal-2, lifted-2, layer-3-bad | #72-75,77b,79 | Best kill-finder |
| 5.2 | Superadditivity, leaf-pruning, separator, layer-3-bad | — | Deepest structural analysis |
| Gemini | Self-funding, Buchstab | — | Creative but gap-prone |
| Muse Spark | K₄ packing (partial) | — | Novel angles, needs polish |
