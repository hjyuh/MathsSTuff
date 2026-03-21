# Corrections Log — Problem 396

## Post-publication errors found by natso26's GPT-5.4 check

### Error 1 (trivial arithmetic)
- **Claimed:** ⌊√(2·339,949,252)⌋ = 26,075, margin 432
- **Correct:** ⌊√(2·339,949,252)⌋ = 26,074, margin 431
- **Impact:** None on the theorem. Off-by-one rounding.

### Error 2 (overclaimed empirical observation)
- **Claimed:** "Every large prime factor p > 31 has slack exactly 0, κ_p(k) = 1 = ν_p(k-j)"
- **Counterexample:** 859 | (K-2), and K in base 859 is (460, 610, 2) — three digits. κ_859(K) = 2 ≠ 1.
- **Correct statement:** The one-carry saturation holds for primes p > √K (where K has exactly two base-p digits). For primes p ≤ √K, K can have three or more base-p digits and more carries are possible.
- **Impact:** The empirical commentary was wrong. The √(2K) theorem is unaffected. The one-carry lemma (GPT Entry 11) is unaffected — it only claims automaticity for √K < p ≤ √(2K), which is exactly the two-digit regime.
- **Root cause:** Claude Code's digit analysis (Entry 10) did not verify the number of base-p digits for each prime. It assumed all primes > 31 were in the two-digit regime, which is false for p < √K ≈ 18,440.

### What survived review vs what didn't
- √(2K) theorem: sent to Codex → PASSED → correct in GPT-5.4 check ✓
- a(8) value: verified by CC → confirmed by GPT-5.4 ✓  
- Empirical saturation claim: NOT sent to Codex → WRONG → caught by GPT-5.4 ✗

### Pipeline lesson
**Every claim in a forum post must go through adversarial review. Not just theorems — empirical observations too.** The saturation claim felt "obvious" from the data but was wrong. Codex would have caught it (the 859 counterexample is immediate once you check whether 859 < √K).
