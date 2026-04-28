# EP-488 Session Log — March 28-29, 2026 (Updated)

## Summary
Single-session candidate proof development for Erdős Problem 488.
Started from Chojecki's March 2026 framework.
Current status: ONE growth lemma from completion (F(s)=4 case).

## Proved Theorems (all survived hostile audit from GPT-5.2)

### 1. Corrected Quotient-Tail Reduction
- Q̂_d(T) = Min(Q̃_d(T))

### 2. Final Positivity Theorem
- δ_{a,b|T} > 0

### 3. Finite-Window Residue Reduction
- F(n) = δn + c_{n mod P} (exact periodicity)

### 4. Exact Finite Obstruction Theorem
- Split inequality equivalent to linear (A) and quadratic (B) checks

### 5. Scalar Route (DEAD — counterexample at (3,4,{5}))

### 6. Off-Slab Closure Theorem
- All s < N_0 automatically harmless

### 7. Visible-Slab Base-Residue Reduction
- Only base-level checks V1, V2, V3 remain on S_vis

### 8. Sharp Visible-Slab Reduction Theorem
- 2F(s)/s > 1/a + 1/b implies all checks pass
- F(s)=2 proved ALWAYS harmless

### 9. Visible-Slab F=3 Reduction Theorem
- F(s)=3 proved ALWAYS harmless via case split on b vs 2a

### 10. Visible-Slab Envelope Reduction Theorem
- Reduced checks to record-low residues of Φ(s) = 2F(s)/s

## Computational Verification
- 693 systems tested, ZERO failures
- ZERO visible slab points with 2F(s)/s ≤ 1/a+1/b for ANY F(s) value
- Tightest system: (11,12,{19}), s=21, F(s)=2, margin=0.68

## What Remains
Prove F(s)=4 is harmless (and ideally general k≥4).
Pattern: k=2 used 3 counted integers, k=3 used 4.
k=4 should use 5 counted integers below 8ab/(a+b).

## Current Estimates
- Current lemma (F(s)=4): 97% (GPT verdict)
- Full EP-488: 98% (GPT verdict)

## Models Used
- Claude Opus 4.6: orchestration, computation, hostile audit
- GPT-5.2 Pro: hostile audit, pessimistic estimates
- GPT-5.4 Pro extended: theorem generation, proof attempts

## Context
- Tao marked P488 as "tractable" and "formalisable"
- Tao posted on erdosproblems.com forum at 3:02 AM March 29
- Tao's January 2026 blog post was about sieving (same territory)
- Tao credited ChatGPT Pro in a March 23 paper
- Chojecki already knows Mahmoud from 4 forum discussions
