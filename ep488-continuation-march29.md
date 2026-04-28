# EP-488 CONTINUATION PROMPT — March 29, 2026
# Paste this into a new chat to resume work.

## STATUS: Proof chain ~95% complete, one open subproblem

## COMPLETE PROVED THEOREM CHAIN (all survived GPT-5.2 hostile audit)

1. **Corrected Quotient-Tail Reduction** — Q̂_d(T) = Min(Q̃_d(T))
2. **Final Positivity Theorem** — δ_{a,b|T} > 0
3. **Finite-Window Residue Reduction** — F(n) = δn + c_{n mod P}
4. **Exact Finite Obstruction Theorem** — Split inequality ↔ linear (A) + quadratic (B) checks
5. **Scalar Route DEAD** — Counterexample at (3,4,{5})
6. **Off-Slab Closure Theorem** — All s < N_0 automatically harmless
7. **Visible-Slab Base-Residue Reduction** — Only base-level checks V1, V2, V3 on S_vis
8. **Sharp Visible-Slab Reduction Theorem** — If 2F(s)/s > 1/a+1/b, all checks pass; F(s)=2 ALWAYS harmless
9. **F(s)=3 Reduction Theorem** — F(s)=3 ALWAYS harmless
10. **F(s)=4 Exceptional Family Reduction** — Every F(s)=4 visible-slab residue harmless UNLESS 3a/2∈T, 4a/3∈T, 3b/2∈T (forces 6|a, 2|b, a<b<4a/3)
11. **Forced Envelope Reduction** — Upper bound U_for(s) on F(n)/n using forced quotient sets; harmless if 8/s > U_for(s)
12. **Computational finding:** Forced envelope closes MOST of exceptional family but FAILS for sub-exceptional family where 8|u, v=27u/8 (i.e., a=48k, b=54k, T={64k, 72k, 81k})
    - Concrete failure: a=48, b=54, T={64,72,81}, s=239, U_for=0.037 > 8/239=0.033

## CURRENT FRONTIER

**Verdict GPT assessment (March 29):** 95/98 → pivot recommended.

**Strategic pivot:** Stop chasing sub-exceptional families through staircase. Instead, prove V1-V3 directly using periodicity F(n) = δn + c_{n mod P}.

**The core remaining question:** For every primitive pair-tail system with δ > 0, do the visible-slab checks V1, V2, V3 hold? Specifically:
- V1: 2F(s) - δs > 0 (i.e., F(s)/s > δ/2)
- V2, V3: comparison inequalities between F(s)/s and F(r)/r at different residues

**What's been tried and failed:**
- Crude threshold 2F(s)/s > 1/a + 1/b: works for F=2,3 and most F=4, but not exceptional family
- Forced envelope U_for(s): works for most exceptional family, but not sub-family (48k, 54k)
- Staircase (find k+1 counted integers below threshold): exhausts at exceptional family

**What verdict GPT recommends trying next:**
- Direct proof of V1-V3 using F(n) = δn + c_r periodicity
- Bound periodic corrections c_r relative to δ
- Use convexity of quadratic K_{sr}

## KEY COMPUTATIONAL RESULTS

- 693 primitive pair-tail systems tested up to a=60: ALL have δ > 0 ✓
- Split inequality F(m)/m < 2F(n)/n verified to n=10,000,000 for P848: zero failures
- 45 exceptional family systems found (a ≤ 60): all have threshold obstructions but most pass envelope
- 3 sub-exceptional systems found (a=48k, k=1,2,3): envelope fails, need direct V1-V3 check

## MODELS USED
- Claude Opus 4.6: orchestration, computation, hostile audit
- GPT-5.2 Pro: hostile audit, pessimistic estimates ("verdict GPT") — current rating 95/96
- GPT-5.4 Pro extended: theorem generation

## CONTEXT
- Tao marked P488 as "tractable" and "formalisable" on erdosproblems.com
- Tao commented on forum at 3:02 AM March 29, 2026
- Chojecki's 26-page paper identified pair-vs-two-tail as the bottleneck (Conjecture 4.8)
- Our work goes beyond Chojecki: complete reduction to visible-slab residue checks
- Quality gate: no forum posts without triple-check + Lean verification

## NEXT ACTIONS
1. Send verdict GPT's direct-V1-V3 prompt to 5.4
2. Include note about sub-exceptional family (48k, 54k) as evidence envelope route has limits
3. If direct approach works: Lean formalize, then post
4. If direct approach fails: consider Perelman move (different sufficient condition entirely)
