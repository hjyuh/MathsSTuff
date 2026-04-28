# EP-488: 5.4 Pro — Challenge to Kill #65 (Swarm Overcounting)
## April 7, 2026

## 5.4's ARGUMENT: Kill #65 is not rigorous as stated

The swarm construction overcounts bad layers by conflating:
- "rough compact elements that COULD have kernel {2,3}" (many)
- "elements that are SIMULTANEOUSLY BAD at one fixed (n,m)" (fewer)

### Two issues identified:

**1. Support issue:**
For swarm element a to have {2,3} in its kernel, needs:
  - 2p ∈ A with p | a (2-ancestor exists in A)
  - 3q ∈ A with q | a (3-ancestor exists in A)
Primes a > M/2 are DISQUALIFIED: their ancestors 2a, 3a > M.
Only supported COMPOSITES count.

**2. Simultaneity / band issue:**
At fixed (n,m), bad layers with s=4 need a ∈ (n/5, n/4].
With t=7, also need a ∈ (m/8, m/7].
The intersection is a NARROW band, much smaller than (M/2, M].

### What this might change:
If the actual count of simultaneously bad layers at one (n,m) is
O(M/log M) instead of O(M/log log M), then:
  S_1 ≈ M²/log M and Σ E_j ≈ M²/log M
  These are the SAME ORDER — the S_1 route might revive.

### What this does NOT change:
Kill #66 (B unbounded) is still valid — Codex B's explicit construction
with primes in narrow intervals works. But the GROWTH RATE of B at
a fixed (n,m) might be slower than Gemini claimed.

## MY ASSESSMENT

5.4 raises a LEGITIMATE concern. Kill #65 as stated is a heuristic
argument, not a rigorous proof. The overcounting of supported composites
in narrow bands is real.

BUT: the challenge doesn't REVERSE the kill. It says "the kill needs
more work" not "the kill is wrong." The swarm construction might still
work with a more careful count, or it might fail to achieve the
O(M/log log M) rate that was claimed.

STATUS: Kill #65 is CHALLENGED but not reversed. The S_1 route is
in limbo — neither proved dead nor proved alive.

## WHAT NEEDS TO HAPPEN

Someone (model or human) needs to rigorously count:
"At one fixed (n,m), how many elements in A ∩ (n/5, n/4] can
simultaneously have kernel ⊇ {2,3} and positive excess?"

If this count is O(M/log M): S_1 route may revive.
If this count is O(M/log log M): Kill #65 stands, S_1 is dead.
If this count is O(1): the uniqueness-like approach revives.

## KILL COUNT: 65 (Kill #65 challenged, not reversed)
## PERCENTAGE: 79%

Slight bump for challenging a claimed kill — this is Route 2 done right.
5.4 found a hole, explained how it was missed, gave structural lesson,
and suggested the fix. Exactly what v5 asked for.
