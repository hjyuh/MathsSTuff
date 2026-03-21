# Crossing Atlas — Erdős Problem 38 (Updated March 20, 2026)

## Surface Domain
Additive combinatorics / Schnirelmann density

## Solution Domain (UPDATED — was: Fourier/characters)
Symbolic dynamics, combinatorics on words, deterministic autocorrelation.
Fourier/Haar analysis is secondary — it hits a log N wall.

## The Crossing
A dyadic shift L = 2^k overlays adjacent length-L words, so gain becomes
one-sided Hamming mismatch between neighboring blocks.

## Bridge Invariant (UPDATED — was: Haar imbalance Σ|Δ_B|)
Adjacent-block Hamming variation:
  V_L := Σ_i Ham(U_i, U_{i+1})
where U_i are consecutive length-L blocks.

**Dead bridge:** Σ|Δ_B| (aligned Haar imbalance). Killed by 5.4 Pro's 
flat-spectrum ballot counterexample (W_j construction).

## Key Identities
1. G_b = (1/2)D_b + (1/2)(F(b) + F(N-b) - F(N))
2. D_{2^k} = Σ_i Ham(U_i, U_{i+1})
3. G_{2^k} = (1/2)Σ Ham(U_i, U_{i+1}) + (1/2)(|U_1| - |U_t|)
4. Σ_{b=1}^{N-1} D_b = β(1-β)N² (pair-count identity)
5. D_b ≤ Σ_{k: bit k of b = 1} D_{2^k} (subadditivity)

## Structural Reason
Same-density blocks can be structurally far apart (Hamming distance ≈ L/2).
Schnirelmann gives prefix-majorization bias converting symmetric mismatch into net gain.

## Prediction Rule
When translation/gain survives after density-based invariants vanish, 
inspect window-by-window Hamming/autocorrelation structure rather than 
aligned density imbalance.

## Current Conjecture (Dyadic Domination)
For ballot sequences: max_b D_b ≤ C(α) · max_k D_{2^k}.
If true: P38 solved with f(α) = α(1-α)/C(α).
Computationally verified: C ≤ 1.5 for all tested families (N up to 10240).

## Three Proof Branches (from 5.4 Pro)
1. Compressed-weight induction: block weights w_i satisfy ballot prefix constraint
2. Symbolic dynamics: same-density words that are Hamming-far when adjacent
3. Dyck-path combinatorics: for α = 1/2, Dyck word variation at dyadic scales
