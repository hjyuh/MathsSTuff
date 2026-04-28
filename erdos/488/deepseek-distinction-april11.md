# DeepSeek Verification — Definitional Distinction Found
## April 11, 2026

## What DeepSeek caught

DeepSeek did NOT reproduce Gemini's Test 3 numbers, but it surfaced a precision issue Gemini glossed over: **the difference between global maximum and asymptotic limsup in the Granville-Soundararajan bound.**

## The two interpretations of A_Q(x)

DeepSeek flagged that the prompt was ambiguous:
- **Reading 1 (literal):** A_Q(x) = unsifted survivors. R(Q) = 1/δ_Q at x=1. Useless.
- **Reading 2 (Granville-Soundararajan):** A_Q(x) = integers DIVISIBLE by some q ∈ Q. This is the actual sieve quantity.

Gemini was using Reading 2 (correct), and DeepSeek's numbers under Reading 2 (1.11-1.25) match Gemini's order of magnitude. Partial independent confirmation.

## The CRITICAL distinction DeepSeek surfaced

> "The problem's wording 'maximum ... asymptotes to e^γ' conflates the global maximum with the limiting upper bound."

**Granville-Soundararajan e^γ is a LIMSUP as x→∞, not a global maximum over all x.**

For prime sieves:
- The **global maximum** of the overshoot ratio diverges like e^γ · log y
- The **limsup as x→∞** approaches e^γ ≈ 1.781
- These are DIFFERENT quantities

## Why this matters for the Bridge Lemma

The Bridge Lemma needs a **uniform bound** that holds for all x ≥ max(A), not just an asymptotic upper bound. If e^γ is only the asymptotic value, then for finite x the actual ratio could exceed e^γ — and could potentially exceed 2, which would kill EP-488.

Test 3 computational data still shows max R ≤ 1.26 in the tested range, which is well below 2. So empirically the safety margin holds. But the theoretical justification needs to address:

1. Is the overshoot bounded UNIFORMLY (for all x) or just ASYMPTOTICALLY (as x→∞)?
2. If only asymptotically, what is the worst-case finite-x bound?
3. Does that worst-case bound stay below 2 for all primitive sets?

## Impact on confidence

**Percentage stays at 93%.** This is not a kill — Test 3's empirical data is still valid and the Bridge Lemma architecture is still alive. But it adds a precision requirement to whatever proof eventually closes the problem. Gemini's corrected Turn 4 (when it arrives) needs to specifically address the global-max-vs-limsup distinction. If it cites e^γ as a uniform bound when it's only asymptotic, that's another gap to flag.

## Action items

- [ ] When Gemini's Turn 4 arrives, check whether it distinguishes uniform vs asymptotic bounds
- [ ] If Gemini cites e^γ as uniform, send back asking for explicit finite-x bound
- [ ] Possibly extend Test 3 computation to larger y values to see if any prime sieve actually exceeds 1.5 at finite x
- [ ] Add this distinction to the master Bridge Lemma document
