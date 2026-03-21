# Erdős Problem 38 — Proof Chain Status (CURRENT)
# March 20, 2026 — After full session with GPT 5.4 Pro Extended Thinking

## The Proof Chain (B = {2^k : k ≥ 0})

| Step | Statement | Status | Source |
|------|-----------|--------|--------|
| 0 | B is not a basis of any finite order | ✅ PROVED | Popcount. Lean verified. |
| 1 | P38 ⟺ conditional gain lemma | ✅ PROVED | GPT 5.2 Pro |
| 2 | Lemma 1: small G ⟹ small D under β ≈ α | ✅ PROVED | GPT 5.2 Pro |
| 3 | Haar bound: max D ≥ cN/log N | ✅ PROVED | Pair-count identity + pigeonhole |
| 3+ | KKL improvement: max D ≥ cN·log(log N)/log N | ✅ PROVED | Cube encoding + Falik-Samorodnitsky KKL |
| 4 | BGK linear bound in prime cyclic model | ✅ PROVED | Bourgain-Glibichuk-Konyagin via Fourier |
| 5 | C(1/2) ≥ 2 for any dyadic domination constant | ✅ PROVED | GPT 5.4 Pro. (u, ū) construction |
| 6 | Spectral methods provably lose log factor | ✅ PROVED | GPT 5.4 Pro. Spectral gap O(1/log p) |
| 7 | Synchronization lemma (exact) | ✅ PROVED | τ_u ⊕ τ_v = m_i ⊕ m_{i+1} |
| 8 | Fiber-regular KKL conjecture | ❌ FALSE | Tribes counterexample (GPT 5.4 Pro) |

## Dead routes (proved impossible):
- ❌ Haar Bridge Lemma (flat spectrum counterexample: W_j construction)
- ❌ N/√(log N) via Cauchy-Schwarz (inequality was backwards)
- ❌ Fiber-regular KKL (tribes satisfies fiber-regularity with vanishing influences)
- ❌ Spectral/Parseval/expander methods (provable log wall)
- ❌ Ballot-specific arguments (cyclic reduction shows core is not ballot-specific)

## Current open target:
Find a stronger structural invariant satisfied by Boolean cube functions from ballot words but NOT by tribes.

Two candidates:
1. Pair influences / second-order influences → Oleszkiewicz theorem
2. Bounded p-moment of sensitivity → Eldan-Kindler-Lifshitz-Minzer junta theorem

## Paper-ready deliverables:
- 10-page PDF: `p38_cube_note.pdf` (propositions, KKL, BGK, synchronization)
- Handoff document: `p38_handoff_detailed.md` (15-section self-contained summary)

## Score: 3.5/10 for full solve. But the reduction + partial results are publishable.
