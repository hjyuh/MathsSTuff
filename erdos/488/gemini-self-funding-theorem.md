# EP-488: Gemini A — Initial-Gap Self-Funding Theorem + Global Budget
## April 7, 2026

## NEW THEOREM: Layers with s_j ≤ 3 are SELF-FUNDING (E_j ≤ 0 always)

### Case s_j = 1 (a_j > n/2):
L_j(t_j) ≤ m/a_j < 2m/n. So n·L_j(t_j) < 2m. E_j < 0. ✅
(This is EP-488 for singletons, Lean-verified.)

### Case s_j = 2 (a_j ∈ (n/3, n/2]):
L_j(2) = 1 implies 2 ∈ K. Survivors are odd: L_j(t_j) ≤ ⌈t_j/2⌉.
Since a_j > n/3: t_j < 3m/n. So L_j(t_j) ≤ 3m/(2n) + 1/2.
E_j ≤ n(3m/(2n) + 1/2) - 2m = 3m/2 + n/2 - 2m = (n-m)/2 < 0. ✅

### Case s_j = 3 (a_j ∈ (n/4, n/3]):
L_j(3) = 1 implies {2,3} ⊆ K. Survivors coprime to 6 (density 1/3).
If m ≥ 1.5n: L_j(t_j) ≤ m/(3a_j) + 1 < 4m/(3n) + 1.
  E_j < n(4m/(3n) + 1) - 2m = 4m/3 + n - 2m = n - 2m/3.
  Since m ≥ 1.5n: 2m/3 ≥ n. So E_j ≤ 0. ✅
If m < 1.5n: t_j = ⌊m/a_j⌋ < 1.5n/(n/4) = 6. So t_j ≤ 5.
  L_{2,3}(5) = 2 (survivors: 1, 5). E_j = 2n - 2m < 0 since m > n. ✅

### CONCLUSION:
Only layers with s_j ≥ 4 can have positive excess.
s_j ≥ 4 means a_j ≤ n/4.

## VERIFICATION

Checking against known bad cases:
- A={2,3,5}, layer a=5, n=24, m=35: s=4, t=7. ✅ (s ≥ 4, confirms theorem)
- A={2,9,15,25}, layer a=25, n=124, m=175: s=4, t=7. ✅ (s ≥ 4)
- All 29 bad kernel signatures have s ≥ 4. ✅ (consistent)

This is a PROVED THEOREM narrowing the dangerous zone.

## THE GLOBAL BUDGET IDEA

Since only s_j ≥ 4 layers are dangerous (a_j ≤ n/4):
- Each bad layer's excess ≤ 17a_j ≤ 17n/4
- Total deficit ≤ 17·Σ_{bad} a_j (bounded by primitivity)
- Elements ≤ n/4 generate massive F(n) through their many multiples
- The global good slack from layers with s_j ≤ 3 should dominate

## KEY STRUCTURAL SPLIT

Layers with a_j > n/4 (s_j ≤ 3): ALWAYS safe, zero compensation needed.
Layers with a_j ≤ n/4 (s_j ≥ 4): can be bad, but each generates huge
  coverage of [1,n] through its multiples (≥ 4 multiples each).

The more dangerous layers you have, the larger F(n) is, the smaller
each bad weight w_j = 1/F(n) becomes. Self-regulating!

## KILL COUNT: 62 (unchanged)
## PERCENTAGE: 80%

Jump from 78% — the self-funding theorem is a genuine new proved result
that eliminates s_j ≤ 3 from consideration entirely. Combined with the
global budget framework, this is the strongest new direction.
