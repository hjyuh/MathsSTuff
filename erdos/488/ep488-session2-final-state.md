# EP-488: Session 2 Final State — March 31, 2026

## What's proved
- a=2 case: PROVED (elementary, 4 lines, GPT-verified twice, forum post published)

## What's killed (22 approaches)
1-13: [Session 1 — various direct bounds, IE manipulations]
14. Active coprimality → Tao reduction
15. "Coprime is worst case" hypothesis
16. IE bound as structural lemma (prime antichain)
17. Composite sparsity lemma A/B/C
18. Chojecki reduction for a ≥ 3 (tail-packing counterexample)
19. Mean-zero periodic correction
20. Monotone compression (adding elements decreases ratio)
21. "Small M check + large M automatic" (consecutive block family)
22. Top-tail reduction: min(A) ≤ M/2 ⟹ R(A) ≤ c < 2 (one-anchor block family)

## What survives
- EP-488 itself: no counterexample found, verified through max(A) ≤ 16
- Singleton-extremal conjecture: survives through max(A) ≤ 16
- The a=2 proof (published on forum)

## Current understanding
- Near-sharp examples exist at EVERY scale of min(A)/max(A)
- The dangerous structure is one-anchor block families: A = {a} ∪ T, T ⊂ (ka, (k+1)a)
- R(A) → 2 but never reaches 2 (EP-488 is about strict inequality)
- The problem is fundamentally about WHY the ratio can approach 2 but never reach it

## GPT-5.4's recommendation
Prove EP-488 first for one-anchor block families A = {a} ∪ {ka+1, ..., ka+t}.
If that class falls, compression/reduction becomes believable.

## Honest assessment
We are NOT close. Every "reduction to a simpler problem" has been killed.
The problem resists being reduced — it wants a direct proof that R(A) < 2 for ALL primitive A.
The a=2 case is real progress. The general case may require genuinely new ideas
that current models (including GPT-5.4 with extended thinking) cannot produce.
