# Session Log — Day 2 (March 13, 2026)
## Conversation compacted mid-response around 11:30 AM

---

## Pre-compaction work (recovered from workspace + screenshot + transcript):

### 848 Residue-Class Attack (MY idea, not GPT's)
- Computed local squarefree density for ALL 24 non-base residue classes mod 25
- RESULT: Every class > 63%. Minimum = 0.6341 at r=1 (progression 25m+8)
- Empirical verification: worst outsider x in [0,100] at N=5000 → 61.5% conflict rate
- Even at M=1 (just ONE base element), the worst-case progression (25m+8) hits 50% by M=5
- This is MY Q3 shortcut: handle each residue class separately instead of one uniform theorem

### Sent to GPT (running now):
- The 848 residue-class attack prompt with full density data
- Asking for explicit error bounds on worst-case progression 25m+8
- Key question: can we get N₀ ≤ 200 (= N=5000)?

### Sent to Codex (running now):  
- 686 four_three option 2: package Chan reduction, isolate Bennett gap
- Axiomatize Bennett's bound, leave finite search as sorry/native_decide

### What I was about to do when compaction hit:
- Scout Problem 701 (searched erdosproblems.com, found it's open, combinatorics + intersecting family, 0 comments)
- Run more empirical tests on the 848 exchange inequality

---

## KEY INSIGHT I don't want to lose:

The residue-class-by-class approach is FUNDAMENTALLY different from what GPT proposed.
GPT wants a UNIFORM exchange inequality (one constant C for all outsiders).
I want 24 SEPARATE exchange inequalities (one per residue class mod 25).

Why mine might be easier:
- Each progression has a COMPUTABLE local density (product over primes)
- The error term for a SPECIFIC progression is easier to bound than a uniform one
- We only need to verify 24 cases, each with a known asymptotic density
- The worst case (r=1, density 0.6341) has a 13.4% margin above 0.5

Why it might fail:
- The outsider x is NOT just its residue class mod 25. x=1 and x=26 are both r=1
  but the progression modulus changes: x=1 gives 25m+8, x=26 gives 650m+183
- So the ACTUAL progression depends on x, not just x mod 25
- The local density I computed is for fixed r, but the error term depends on q=25x
- For large x (say x=4999), q=25×4999=124975, and the error term √(N/q) is tiny
- For small x (say x=1), q=25, error is √(N/25) which is larger
- So the SMALL outsiders are the hard case

ACTUALLY this is good — small x means small q means MORE terms in the AP means 
BETTER error bounds. The dangerous case would be q ≈ N^{1/2} but even there,
Hooley's range covers q ≤ N^{2/3}.

I think this works. The computation I ran ALREADY shows it working empirically.
The question is whether GPT can make the error explicit.
