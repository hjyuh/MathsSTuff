# EP-488: Updated Synthesis — After Kill #47
## April 5, 2026 — Session state after GPT-5.4 Pro + GPT-5.2 Pro + Claude

---

## WHAT JUST HAPPENED

1. Claude (literature search) proposed: bound excursions using periodicity |D_Q(y)| ≤ φ(q_j),
   plug into 5.2's collective budget V + 2U < C. This gives the structural
   inequality Σ ρ_j(r_j - 3q_j - 2) > 0.

2. GPT-5.4 Pro (structural analysis) proved:
   - Q_j is explicitly characterized (quotients a_i/gcd(a_i,a_j) for i < j)
   - q_j can be VASTLY larger than M (Kill #47 on the structural inequality)
   - A = {2,3,5} already gives sum = -12
   - BUT: gave the FIX — the **active-prime windowed bound**

## THE ACTIVE-PRIME WINDOWED BOUND (proved by 5.4 Pro)

For layer j with scale r_j = M/a_j, primes p > 10r_j CANNOT divide any
integer ≤ 10r_j. So they're invisible to K_Q on the window [r_j, 10r_j].

Refined discrepancy:

  sup_{y ∈ [r,10r]} |D_P(y)| ≤ φ(q_{active}) + 10r · Σ_{p inactive} 1/p

where:
  q_{active} = ∏_{p ∈ P_j, p ≤ 10r_j} p   (only small primes matter)
  inactive primes: p ∈ P_j with p > 10r_j   (contribute only harmonic drift)

### Impact:
- Naive bound for A = {primes ≤ 29}, last layer: φ(q) ≈ 3.6 × 10^7
- Windowed bound for same layer: φ(210) + drift ≈ 51
- Improvement: factor of ~700,000

---

## REVISED COLLECTIVE CRITERION

Using the windowed bound, excursions become:

  e_j ≤ φ(q_{active,j}) + 10r_j · Σ_{p ∈ P_j, p > 10r_j} 1/p + ρ_j

The collective criterion 3·Σ e_j < C = Σ r_j·ρ_j becomes:

  3·Σ_j [φ(q_{active,j}) + 10r_j·(harmonic tail)_j + ρ_j] < Σ_j r_j·ρ_j

### Layer-by-layer analysis:

**Principal layer (j=1):** Q_1 = ∅, so q_{active} = 1, φ(1) = 1, no drift.
  e_1 ≤ 1 + 0 + 1 = 2.  Meanwhile c_1 = r_1 = M/min(A).
  Contribution to surplus: r_1 - 6 = M/min(A) - 6.
  → Positive whenever max/min > 6.

**Heavy interior layers:** r_j moderate (say 10-100), active primes few.
  q_{active} = product of primes ≤ 10r_j that appear in P_j.
  Bounded by the primorial of 10r_j, but P_j may only contain a few of them.
  
**Tail layers (r_j ≈ 1):** Active primes are those ≤ 10.
  q_{active} ≤ 2·3·5·7 = 210, φ(210) = 48.
  e_j ≤ 48 + drift + ρ_j ≈ 50.
  c_j = r_j·ρ_j ≈ ρ_j (small).
  → These layers are NET NEGATIVE in the budget.

### The question reduces to:
**Does the principal layer's surplus M/min(A) - 6 dominate the
tail layers' cumulative deficit of ~50k (where k = number of tail layers)?**

Equivalently: is M/min(A) > 6 + 150k always, for primitive sets?

NO — primitive sets can have k = M/2 elements (e.g., all odd numbers in
[M/2, M]), so this fails in general.

BUT: when all elements are near M (compact), the ACTIVE primes are few
and the windowed bound is much tighter than 48. And compact sets are
already proved.

---

## STATUS OF THE THREE STRATEGIES

### Strategy A (Dominant Stable Mass): PARTIALLY VIABLE
Works for non-compact sets with M/min(A) large relative to k.
Fails for sets with many elements near M (compact).
Could work if combined with Theorem 6 (compact sets already proved).
NEEDS: a clean partition into "compact-like" and "spread" regimes.

### Strategy B (Anti-Alignment / Phase Mixing): MOST PROMISING
5.4 Pro gave a concrete Fourier/large-sieve blueprint.
Key insight: different layers oscillate at different frequencies
(determined by a_j and q_{active,j}), so their errors tend to cancel.
NEEDS: someone to actually execute the large-sieve calculation.
BEST CANDIDATE: GPT-5.2 Pro (analytic strengths).

### Strategy C (Endpoint Control): UNTOUCHED
The observation that inf H(x) may not occur at x = M (where dips are
worst) hasn't been explored. Could give targeted savings.
BEST CANDIDATE: GPT-5.4 Pro or computational verification.

---

## CONCRETE NEXT STEPS

### 1. GPT compute session (READY)
Run gpt-compute-qj-prompt.md but UPDATED:
- Use the WINDOWED bound φ(q_{active,j}) instead of φ(q_j)
- Compute actual e_j vs windowed bound (how tight is it?)
- Compute 3Σe_j / C with windowed bounds
- Find worst cases

### 2. GPT-5.2 Pro (NEXT STRUCTURAL TASK)
Send it Strategy B: formalize the large-sieve argument.
Input: 5.4 Pro's Fourier blueprint (Task 3b)
Goal: prove sup|Σ ε_j(x)| < C/3 using phase mixing.

### 3. GPT-5.4 Pro (STRUCTURAL CLEANUP)
Ask it: for primitive sets, what is the tightest bound on
Σ_j φ(q_{active,j}) in terms of M, k, and the structure of A?
Can the partition into compact/spread be made rigorous?

### 4. Gemini (DEEP RESEARCH, running in parallel)
Literature search already dispatched.

---

## KILL LIST UPDATE
Kill #47: Naive structural inequality Σ ρ_j(r_j - 3q_j - 2) > 0
  Counterexample: A = {2,3,5}, sum = -12.
  Root cause: φ(q_j) bound treats inactive primes as active.
  Fix: active-prime windowed bound (proved by 5.4 Pro).

## PERCENTAGE: 60-65% (unchanged from Claude's estimate)
The windowed bound is a real advance, but converting it to a full
proof requires either closing Strategy A with a compact/spread
partition, or executing Strategy B's large-sieve program.
Neither is done yet.
