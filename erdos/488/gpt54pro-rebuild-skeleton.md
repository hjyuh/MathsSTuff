# EP-488: Rebuild the Skeleton — Counterexample-Proof Version
## For GPT-5.4 Pro Extended — April 7, 2026
## SEND THIS AFTER 5.4 RETURNS WITH GAP A KILLED

---

You just showed that [Gap A claim] is false. Good — that's Kill #60.

Now rebuild the proof skeleton so that it AVOIDS the killed claim entirely.

## CONSTRAINTS ON THE REBUILT SKELETON

The rebuilt proof must:

1. NOT require the parent's kernel to equal K \ {3} (killed in Kill #59)
2. NOT require L_i(x) ≥ L_{B_j\{3}}(x) (killed just now, if applicable)
3. NOT bound layers individually (Kill #56)
4. NOT use any scalar summary as threshold (Kills #45, 50, 54, 57)
5. NOT fold or reduce to simpler sets (Kills #52, 55)

The rebuilt proof CAN use:

1. The 29-kernel classification (proved, no known issues)
2. The Quotient Transport Lemma: q_{k,j} | 3·q_{k,i} (proved)
3. The single-obstruction theorem (proved)
4. The Buchstab identity: L_B(x) = L_{B\{p}}(x) - L_{B\{p}}(x/p)
5. Computational verification (6,657 instances, zero failures)
6. The bound: child excess ≤ 17·a_j (proved by 5.2)
7. The fact that parent evaluates deeper: s' ≥ (h/3)s with h ≥ 5
8. ANY new structural fact about primitive sets

## THE CORE QUESTION

The actual-slack ancestor lemma says:

  parent actual slack ≥ child actual excess

for the REAL L_i and L_j functions, not model kernels.

6,657 instances verify this with enormous margins. The tightest margin
is 134 (normalized) or 552 (actual). The child excess is always tiny
(≤ 17a_j). The parent slack is always huge.

WHY is the parent slack always huge? What structural property of
primitive sets guarantees this? Don't tell me what the parent kernel
looks like — tell me why its ACTUAL COUNT at the deeper evaluation
point is large enough.

## FORMAT

Give me a new skeleton with numbered steps. For each step:
- If proved: state the proof in ≤ 3 sentences
- If reduces to finite check: say [FINITE CHECK — VERIFIED]
- If genuinely open: state EXACTLY what needs to be proved
- If you find a counterexample to the actual-slack lemma itself: STOP and report it

## THE NUCLEAR OPTION

If you believe the actual-slack ancestor lemma is FALSE, say so and
give the counterexample. This would kill the entire compensation approach
and we'd need a fundamentally different proof strategy.

But 6,657 instances with margins of 134-552 say you won't find one.
