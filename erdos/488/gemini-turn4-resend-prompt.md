# Gemini Deep Think — Corrected Turn 4 Resend Prompt
## Copy-paste this entire block when Gemini times out

---

**EXECUTION PROTOCOL (READ THIS FIRST)**

You have a 192k thinking token limit before you time out. Before doing ANY work:

1. **PLAN your response structure in ≤500 thinking tokens.** Outline what sections you'll write, what computations you'll run, and estimate the token cost of each section.

2. **Budget ruthlessly.** If your plan requires more than ~150k thinking tokens, SPLIT IT. Output your partial results and explicitly state what remains for the next turn.

3. **Never combine heavy computation with proof synthesis in the same turn.** Computation turns produce DATA. Synthesis turns produce ARGUMENTS. Mixing them causes timeout.

4. **If you need to cut your response short:** STOP immediately, output everything you have so far, and end with a clearly labeled section:

   **CONTINUATION INSTRUCTIONS:**
   - What was completed in this turn
   - What remains to be done
   - The exact prompt the user should send to resume
   - Any intermediate results or state that must be carried forward

5. **Output structure:** Lead with results and conclusions. Put derivations after. If you time out mid-derivation, the results are already in the chat history.

6. **Incomplete honest results are infinitely more valuable than a timed-out response that produces nothing.**

---

**CONTEXT: You are resuming EP-488 Turn 4 (proof synthesis). Your Turns 1-3 were outstanding. Here is a summary of all confirmed results:**

## CONFIRMED KILLS (do not re-derive these)

- **Form 1 (L² block-dispersion): KILLED.** A={19}, n=19, m=190 gives R≈90.72. Structural: for singleton prime p, R scales as (log p)². Three independent model confirmations.
- **Form 2 (universal Gram matrix): KILLED.** Your own Turn 3 data: λ_max/|I_s| explodes exponentially with s (s=10→10, s=30→28614, s=40→1.7M, s=50→269M). Cause: highly composite numbers act as "combinatorial black holes" because the universal tuple space forgets primitivity (a_i ∤ a_j).
- **Form 3 (pairwise ⟨ψ_a,ψ_b⟩ ≤ 0): KILLED.** Exact theorem: ∫₀ᴸ ψ_a·ψ_b dx = gcd(a,b)/12 > 0 always. 5.4 Pro rigorous proof.

## CONFIRMED POSITIVE RESULTS (use these)

- **Test 3 (sieve overshoot): PASSES.** Your Turn 3 data:
  - Random dense primitive sets: max R(Q) = 1.0553
  - Prime sieves ≤10: R = 1.1513
  - Prime sieves ≤20: R = 1.1901
  - Prime sieves ≤50: R = 1.1974
  - Prime sieves ≤100: R = 1.2197
  - Prime sieves ≤200: R = 1.2601
  - All safely below e^γ ≈ 1.781, which is safely below 2.

- **The algebraic translation is confirmed:**
  G(m) < 2G(n) ⟺ 2·A_Q(n)/n - A_Q(m)/m < 1

- **Closed cases (j₀ ≤ 6):** Sub-problems A, B, C all proved with multiple independent proofs. Band 5 globally dead. These are permanent and do not need re-verification.

## THE GAP IN YOUR PREVIOUS TURN 4 ATTEMPT

Your Turn 4 had two specific gaps that need fixing:

**Gap 1: Granville-Soundararajan scope.** You cited the e^γ bound as covering "any sifting antichain." It doesn't. The e^γ bound is proved for PRIME SIEVES only. Extending it to primitive-set quotient-tail antichains is not a citation — it IS the theorem EP-488 needs you to prove. Your Test 3 shows it holds computationally. You need to prove it, not cite it.

**Gap 2: Regime 2 √x decay.** You wrote |Δ_A(x)|/x ≤ C₀·√(energy)/√x and cited "the Large Sieve" without applying a specific inequality with specific parameters. Which theorem of Montgomery-Vaughan, applied with which inputs, gives that bound? The step from "Lichtman disjointness implies negative cross-covariance" to "therefore discrepancy decays as 1/√x" skips the entire analytic argument.

## YOUR TASK FOR THIS TURN

**Route the proof through Form 4 (sieve discrepancy).** This is the only surviving form with computational support.

**Option A (ideal):** Prove that for ANY primitive set A, sup A_Q(x)/(δ_A·x) < 2. If you can prove it's < e^γ, even better, but < 2 suffices for EP-488.

**Option B (if A is too hard):** Identify EXACTLY what additional theorem or lemma would close the gap. State it precisely enough that it could be tested computationally or sent to another model.

**Option C (if stuck):** Write an honest diagnostic explaining why Form 4 cannot be proved with current tools, and what mathematical machinery is missing. This is still valuable.

**Do NOT declare the problem solved unless every step is rigorous. Do NOT cite theorems beyond their proved scope. Do NOT hand-wave the hard steps. An honest "I can prove it under assumption X but not unconditionally" is infinitely more valuable than a false claim of completion.**
