# Erdős Problem 38 — Model Attribution Correction + Status
# March 20, 2026

## Correct Attribution

| Response | Model | What it did |
|----------|-------|-------------|
| Response 1: Cofinite counterexample | GPT 5.2 Pro | Killed unconditional gain lemma, gave correct conditional form |
| Response 2: Haar analysis + Lemma 1 | GPT 5.2 Pro | Proved N/log N bound, identified Bridge Lemma as target |
| Response 3: "Improved" to N/√(log N) | GPT 5.2 Pro | Claimed Cauchy-Schwarz upgrade — WRONG (inequality backwards) |
| Response 4: Bridge Lemma counterexample | GPT 5.4 Pro | Killed Bridge Lemma with explicit construction, caught 5.2's error |

## Key correction from 5.4 Pro
GPT 5.2 Pro claimed: Σ|Δ| ≥ √(M·ΣΔ²) (lower bound via Cauchy-Schwarz)
GPT 5.4 Pro caught: Cauchy-Schwarz gives Σ|Δ| ≤ √(M·ΣΔ²) (UPPER bound, not lower)
So the N/√(log N) bound is INVALID. Only the N/log N bound from pigeonhole stands.

## What's proved (rigorous):
- Step 0: B = {2^k} is not a basis ✅
- Step 1: P38 ⟺ conditional gain lemma ✅ (5.2 Pro)
- Step 2: Lemma 1 (small G → small D under β ≈ α) ✅ (5.2 Pro)
- Step 3: max D ≥ cN/log N ✅ (5.2 Pro, pigeonhole on Parseval)

## What's disproved:
- Bridge Lemma (max Σ|Δ| ≥ cN) ❌ (5.4 Pro, explicit counterexample)
- N/√(log N) bound ❌ (5.2 Pro had inequality backwards, caught by 5.4)

## What's still alive:
- B = {2^k} as P38 candidate: max G_b/N stays ~0.21 even on 5.4's counterexample
- The gain comes from CROSS-BLOCK shifts, not within-block imbalance
- The Haar approach cannot see this — need a fundamentally different proof

## Still running:
- Gemini Deep Think (hours, still going)
