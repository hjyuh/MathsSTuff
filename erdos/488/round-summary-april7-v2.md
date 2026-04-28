# EP-488: Round Summary — All Models on Unified Truth v2
## April 7, 2026

## FOUR RESPONSES, TWO CAMPS

### Team Global (Gemini A + Claude A + Claude B):
- Gemini A: PROVED self-funding theorem for s ≤ 3. Proposed global budget.
- Claude A: Developed weighted average anti-correlation. Noted pairs already proved.
- Claude B: Tried Approach E counting bad layers. Got stuck at kernel comparison wall.

### Team Direct (5.4):
- Killed counting-only approaches for all-compact case
- Sharpened target to L_i(u)+1 ≥ Δ_i + Δ_j
- New observation: s ≤ 19 for all bad children (finite rough-flow)

## NEW PROVED RESULTS THIS ROUND

1. Self-funding theorem (Gemini A): s_j ≤ 3 → E_j ≤ 0 always. ✅
   - s=1: singleton EP-488 (Lean-verified)
   - s=2: odd-number density argument
   - s=3: coprime-to-6 density + case split

2. Bad children have s ∈ [4, 19] (5.4): ✅
   Prime-cover rigidity + bad kernels ⊆ {2,...,19}

## WHAT'S DEAD FROM THIS ROUND

Counting-only weighted approaches (5.4's argument):
If A ⊂ (M/2, M], all weights = 1/k, bad weight → 1.
BUT: Gemini showed s=1 layers are always safe, so this case
is actually fine. The tension is at larger n where s ≥ 4.

## CONSENSUS PICTURE

1. Layers with s ≤ 3: SAFE (proved by Gemini)
2. Layers with s ∈ [4, 19]: DANGEROUS ZONE (only place excess can occur)
3. Layers with s ≥ 20: SAFE (no bad kernel has reach ≥ 20)
4. The dangerous zone is FINITE: s ∈ [4,19], 29 kernels, bounded parameters
5. Direct stock-flow comparison still the frontier for proving compensation

## THE HONEST STATE

The dangerous zone has been compressed to a finite window (s ∈ [4,19])
by combining:
- Self-funding theorem (eliminates s ≤ 3)
- Prime-cover rigidity (eliminates s ≥ 20)
- 29-kernel classification (enumerates all bad signatures)

Within this finite window, the stock-flow comparison
  L_i(u)+1 ≥ (Δ_i + Δ_j)/(2r-1)
remains unproved. 6,659+ instances say it's true.

## KILL COUNT: 62
## PERCENTAGE: 80%
