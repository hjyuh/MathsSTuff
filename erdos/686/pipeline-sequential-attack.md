# Problem 686 — Sequential Attack Pipeline
## March 15, 2026

## The Gap (precisely stated)

For N=4 (simplest stuck square), we need to prove either:
- (A) There exists some k ≥ 2 where 4 is representable, OR
- (B) No such k exists

What's known for N=4:
- k=2: fails (Tao — 4=2², prime square)
- k=3: fails (our computation, Y ≤ 500, not proved)
- k=4: fails (reduces to k=2, natso26)
- k=5: UNKNOWN
- k=6: fails (Vjeko, series expansion)
- k=7 to K₀: UNKNOWN (this is the gap)
- k ≥ K₀: fails (natso26's theorem — but K₀ may be huge)

## Pipeline Structure

### Round 1: Codex plans, GPT attempts

**Codex prompt (planning):**
"Given Problem 686 for N=4, the gap is k ∈ {3,5,7,...,K₀} where K₀ is 
natso26's bound. Propose 3-5 concrete mathematical approaches to either:
(a) prove N=4 is not representable at k=3 (via Thue equations on the 
    cubic X³-X = 4(Y³-Y), not Weierstrass integral points which don't 
    preserve integrality),
(b) prove N=4 is not representable at k=5 (the first unchecked case),
(c) sharpen natso26's large-k bound for N=4 specifically to make K₀ small,
(d) find a uniform argument covering all odd k for N=4.

For each approach: state the exact mathematical setup, what tools are 
needed, what the expected difficulty is, and what failure mode to watch for.
Do NOT attempt the proofs. Just plan."

### Round 2: GPT attempts approach #1

**GPT prompt (extended thinking, attempt):**
"[Paste Codex's approach #1 here]

Attempt this approach now. Show all work. If you get stuck, explain 
EXACTLY where and why. Do not fake progress. If the approach fails, 
state:
1. The exact step where it broke
2. Why it broke (missing lemma, bound too weak, wrong structure)
3. What would need to be true for it to work
4. Whether a modified version might succeed

Do not plan. Attempt the mathematics NOW."

### Round 3: Diagnosis and redirect

**Me (Claude) or Codex:**
Take GPT's failure report. Extract:
- The failure mode
- Whether it's fixable
- What the failure reveals about the problem structure
- Which of Codex's remaining approaches is most promising given this info

Then send GPT the next approach, informed by the failure.

### Repeat until either:
- An approach succeeds (result!)
- All approaches fail with informative failure modes (write up what we learned)
- We discover a new structural insight from the pattern of failures

## Specific Attack Vectors to Try

### Vector 1: Thue equation decomposition for N=4, k=3
The curve X³-X = 4(Y³-Y) can be written as X³-4Y³ = X-4Y.
Factor: X-4Y divides both sides, but X³-4Y³ ≠ (X-4Y)(something nice) 
since 4 isn't a perfect cube.

Alternative: for each divisor d of (X-4Y), get a Thue equation. 
Thue-Mahler methods give effective bounds. SageMath can solve Thue 
equations directly.

**Expected difficulty:** Medium. The Thue decomposition is standard.
**Failure mode:** The Thue equations might have solutions that map to 
non-admissible (X,Y) pairs, requiring case analysis.

### Vector 2: Sharpen natso26's bound for N=4
natso26 (comment 10): if N has ≤ r prime factors and k > 2r, then for 
sufficiently large N of the form a^lcm(S), N is not k-representable.

For N=4=2², we have r=1 prime factor. So k > 2 should suffice... 
but "sufficiently large" is the problem. Can we make this effective 
for N=4 specifically?

**Expected difficulty:** Hard. Requires reading natso26's actual proof 
method and specializing it.
**Failure mode:** The "sufficiently large" bound might genuinely require 
N >> 4, making the theorem useless for small N.

### Vector 3: Vilc's upper bound method (comment 14) for k=5
Vilc derived upper bounds on n for N = prime power at general k.
Apply this to N=4, k=5 specifically. If the bound is small enough, 
exhaustive search completes the proof.

**Expected difficulty:** Medium. The method exists, just need to 
specialize it.
**Failure mode:** The bound might be astronomical for k=5.

### Vector 4: p-adic obstruction for N=4
Check whether X³-X = 4(Y³-Y) has solutions in Z_p for all primes p.
If there's a prime p where no p-adic solution exists (beyond trivials), 
that's a local obstruction proving no global solution.

**Expected difficulty:** Easy to check, unlikely to work (we know 
rational points exist, so local obstructions at finite primes are 
unlikely by Hasse principle intuition — though Hasse principle can fail 
for cubics).
**Failure mode:** Local solutions probably exist everywhere.

### Vector 5: Explicit k=5 curve computation
Write out the k=5 equation for N=4:
(m+1)(m+2)(m+3)(m+4)(m+5) = 4·(n+1)(n+2)(n+3)(n+4)(n+5)
This is a genus ≥ 2 curve. By Faltings, finitely many rational points.
Baker's method or Chabauty-Coleman can find them all explicitly.

**Expected difficulty:** Hard but known to be feasible for specific curves.
**Failure mode:** The curve might be too complex for current Chabauty 
implementations.

## Pipeline Execution Order

1. Start with Vector 1 (Thue for k=3) — most concrete, builds on our data
2. In parallel, try Vector 3 (Vilc's bound for k=5) — independent
3. If both fail, try Vector 2 (sharpen natso26) — harder but higher payoff
4. Vector 4 as a quick check
5. Vector 5 as fallback

## Success Criteria

ANY of the following would be postable:
- Provable non-representability at k=3 for any stuck square (via Thue)
- Provable non-representability at k=5 for any stuck square
- A sharpened large-k bound making K₀ explicit for N=4
- A uniform odd-k argument for prime squares

The COMBINATION of k=3 + k=5 + sharpened K₀ could potentially close 
the gap entirely for N=4, which would be the first complete proof that 
a specific integer is not representable — disproving the conjecture.
