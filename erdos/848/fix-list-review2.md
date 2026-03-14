# Proof-Writeup Fix List (from GPT Review #2)
## March 13, 2026

## STATUS: No fatal issues. Six presentation fixes needed.

### Fix 1: Symmetry (Section 2.2 + Case 1) — EASY
- Remove "a ↦ 25−a mod 25" claim
- Instead: B₇ and B₁₈ are both valid; can't mix (7×18+1=127 squarefree); |B₇|≥|B₁₈| always
- Case 1 becomes: valid set with no outsider ⊆ one base class

### Fix 2: Three β values (Section 5) — MEDIUM
- Add explicit paragraph:
  - β ≤ 1.2775: asymptotic (Lemma B, union bound density)
  - β₁₃ < 1.6117: rigorous and uniform for ALL V (Lemma R + direct computation V<58)
  - β₁₃ ≤ 1.47: stronger finite constant from rowwise computation V≥30
- Explain: 1.6117 is what closes the proof; 1.47 gives a better threshold

### Fix 3: Section 5 detail — MEDIUM
- Expand Lemma R proof: define S_u(D) explicitly, show the {4,9,13} exclusion
- Show the D optimization step by step
- Expand Section 5.3: show the threshold calculation explicitly

### Fix 4: Section 6 as formal proposition — MEDIUM
- State: "Proposition 6.1. For all N with 1882 ≤ N ≤ 500,000 and every prime p ≡ 1 mod 4
  with p² ≤ N, the inequality s_max^(p)(N) + max(V⁺,V⁻) + d_max^(p)(N) + R_{>p}(N) < M(N) holds."
- Explain N < 1882 covered by exact computation (separate tool, not the structured inequality)
- Add: script name, expected output, runtime, platform

### Fix 5: References — EASY
- Full bibliographic entries for Erdős-Sárközy, Sawhney, Van Doorn, Weisenberg

### Fix 6: Tone and authorship — EASY
- Move AI credits to acknowledgments
- Remove "age 13"
- Soften "resolve" → "give a proof"
- Soften "novel" → "introduce"
- Add "conditional on correctness of verification scripts"

## NONE OF THESE CHANGE THE MATH.
## The computation (0 failures through 500K) stands.
## The analytical bound (β₁₃ < 1.6117) stands.
## The cross-pair analysis (F ≡ 2 mod p²) stands.
