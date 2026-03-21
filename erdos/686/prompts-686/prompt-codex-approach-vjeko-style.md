# Codex Execution Checklist — Vjeko-Style Asymptotic Expansion for k=5, N=4

## For Codex at xhigh

You already identified this as the correct approach in your previous 
response. Now produce the full execution checklist.

## Recap of what you said

You proposed:
1. Let M(n) be the unique real root m > n of F(m) = 4F(n).
2. Derive a Puiseux/asymptotic expansion M(n) = 4^{1/5}·n + c₀ + c₁/n + c₂/n² + ...
3. Prove that for all large n, the interval between F(⌊M(n)⌋) and F(⌈M(n)⌉) 
   is too wide for 4F(n) to land exactly on it.
4. Then check the remaining finite range by brute force.

You said this is the RIGHT SHAPE for the problem and uses the same style 
as Vjeko's k=6, N=64 argument (forum comment 13).

## Now produce the checklist

For each step below, provide:
- MATHEMATICAL CONTENT: what we're computing and why
- EXACT SAGEMATH CODE: runnable in CoCalc SageMath 10.x
- EXPECTED OUTPUT: what numbers/expressions to expect
- DECISION: if X → proceed; if Y → the approach fails because Z
- FAILURE MODE: what could go wrong
- ESTIMATED TIME: how long the computation takes

### Phase 0: Setup and notation

**Step 0.1: Define F and verify basic properties**

Define F(t) = (t+1)(t+2)(t+3)(t+4)(t+5) in SageMath. Verify:
- F(t) = t⁵ + 15t⁴ + 85t³ + 225t² + 274t + 120
- F is strictly increasing for t ≥ 0
- For each n ≥ 0, there is a unique real m > n with F(m) = 4F(n)

**Step 0.2: Define M(n) numerically**

Write SageMath code that, given n, computes M(n) to 50 decimal places 
using mpmath or RealField. Verify:
- M(0) = ? (compute explicitly)
- M(10) = ? 
- M(100) = ?
- M(1000) = ?
- Check: does M(n)/n → 4^{1/5} as n → ∞?

**Step 0.3: Verify that M(n) is never an integer for small n**

Write code that checks: for n = 0, 1, 2, ..., 100000, is M(n) ever 
an integer (or within 10^{-40} of an integer)? This is the brute force 
part that we'll extend later once we have the cutoff.

### Phase 1: Derive the asymptotic expansion

**Step 1.1: First-order term**

MATHEMATICAL CONTENT: For large n, F(n) ≈ n⁵, so F(m) = 4F(n) gives 
m ≈ 4^{1/5}·n. More precisely:

F(t) = t⁵(1 + 15/t + 85/t² + 225/t³ + 274/t⁴ + 120/t⁵)

So F(m) = 4F(n) becomes:
m⁵(1 + 15/m + ...) = 4n⁵(1 + 15/n + ...)

Writing m = 4^{1/5}·n + c₀ + c₁/n + c₂/n² + ..., substitute into 
the equation and match coefficients.

Provide:
- The exact algebraic computation of c₀ (should be a rational function 
  of 4^{1/5})
- SageMath code to compute this symbolically or to high numerical precision
- Verification against the numerical M(n) values from Step 0.2

**Step 1.2: Higher-order terms (c₁, c₂, c₃)**

Derive at least c₀, c₁, c₂, c₃ in the expansion:

  M(n) = 4^{1/5}·n + c₀ + c₁/n + c₂/n² + c₃/n³ + O(1/n⁴)

Provide:
- The exact expressions for each cᵢ (in terms of 4^{1/5})
- SageMath code to derive them (either by series inversion or by 
  successive approximation)
- Numerical verification: compare the truncated expansion to the exact 
  M(n) for n = 100, 1000, 10000

**Step 1.3: Bound the remainder**

This is the critical step for turning the asymptotic expansion into a proof.

MATHEMATICAL CONTENT: After computing M(n) = 4^{1/5}·n + c₀ + ... + cₖ/nᵏ + R(n),
we need a RIGOROUS bound on |R(n)| for all n ≥ N₀.

Provide:
- The explicit bound |R(n)| ≤ C/n^{k+1} with C computed
- The SageMath code to verify this bound numerically
- The value of N₀ above which the bound holds

### Phase 2: The integrality gap argument

**Step 2.1: Fractional part analysis**

MATHEMATICAL CONTENT: For M(n) to be an integer, the fractional part 
{M(n)} must be 0. From the expansion:

  {M(n)} = {4^{1/5}·n + c₀ + c₁/n + ...}

For large n, the c₁/n + c₂/n² + ... terms are small, so:

  {M(n)} ≈ {4^{1/5}·n + c₀}

Since 4^{1/5} is irrational (proved in Step 0.3 of the previous checklist: 
u⁵-4 is irreducible over Q), the sequence {4^{1/5}·n} is equidistributed 
mod 1 (Weyl's theorem). So {M(n)} visits every part of [0,1).

BUT: for M(n) to be EXACTLY an integer, we need {M(n)} = 0 exactly, 
not just approximately. The question is: can 4^{1/5}·n + c₀ + c₁/n + ... 
ever be exactly an integer?

Provide:
- The argument for why equidistribution is NOT enough (it tells us the 
  fractional part is often near 0, but not that it's never exactly 0)
- What additional argument is needed

**Step 2.2: The gap between consecutive F values**

MATHEMATICAL CONTENT: This is the key step. Let m₀ = ⌊M(n)⌋. Then:

  F(m₀) < 4F(n) < F(m₀ + 1)

iff M(n) is not an integer (since F is strictly increasing on integers ≥ 0).

The gap F(m₀+1) - F(m₀) can be computed:
  F(m₀+1) - F(m₀) ≈ F'(m₀) ≈ 5m₀⁴ ≈ 5·(4^{1/5}·n)⁴ = 5·4^{4/5}·n⁴

Meanwhile, 4F(n) - F(m₀) is the "landing error." If this error is bounded 
away from 0 and from F(m₀+1) - F(m₀), then M(n) can't be an integer.

More precisely: define δ(n) = M(n) - ⌊M(n)⌋ = {M(n)}. Then:

  4F(n) - F(⌊M(n)⌋) ≈ F'(M(n)) · δ(n) ≈ 5·4^{4/5}·n⁴ · δ(n)

For this to equal 0 exactly, we need δ(n) = 0, i.e., M(n) ∈ Z.

The point is: from the expansion, δ(n) = {4^{1/5}·n + c₀ + O(1/n)}, 
and we need to show this is NEVER zero for n ≥ some N₀.

Provide:
- The exact SageMath code to compute δ(n) for large n
- The argument (if one exists) for why δ(n) ≠ 0 for all n ≥ N₀
- If no such argument exists purely from asymptotics, explain what's 
  missing and what additional input is needed

**Step 2.3: The irrationality measure argument (if needed)**

If Step 2.2 can't close the argument with asymptotics alone, the 
remaining tool is bounds on how well 4^{1/5} can be approximated by 
rationals. Specifically:

If M(n) = m is an integer, then:
  |4^{1/5} - (m - c₀ - c₁/n - ...)/n| < C/n^{k+2}

This means (m - c₀)/n approximates 4^{1/5} to within O(1/n^{k+2}). 
By the Thue-Siegel-Roth theorem, for any algebraic irrational α and 
any ε > 0, there are only finitely many p/q with |α - p/q| < 1/q^{2+ε}.

Since 4^{1/5} is algebraic of degree 5, and the approximation quality 
is O(1/n^{k+2}) with k ≥ 3 (so quality ≥ 1/n⁵), this exceeds the 
Roth exponent of 2+ε. Therefore only finitely many n can give M(n) ∈ Z.

Provide:
- The exact formulation of this argument
- The resulting finite bound N₁ (above which no integer M(n) exists)
- Whether N₁ is effective (Roth is ineffective! But Thue-Siegel gives 
  effective bounds for specific algebraic numbers)
- The SageMath code to verify the bound, if effective

### Phase 3: Brute force below the cutoff

**Step 3.1: Determine the cutoff**

From Phase 2, we have a cutoff N₀ (from asymptotics) or N₁ (from 
irrationality measure) below which we must search exhaustively.

State the cutoff explicitly.

**Step 3.2: Exhaustive search**

Provide SageMath code to check all n from 0 to the cutoff:
- For each n, compute 4·F(n)
- Check if 4·F(n) = F(m) for any integer m ≥ n + 5
- Use exact integer arithmetic (no floats)

**Step 3.3: Combine into a proof**

If the exhaustive search finds no solution below the cutoff, and the 
asymptotic/irrationality argument rules out all n above the cutoff, 
then N=4 is provably not k=5 representable.

State the complete proof structure.

### Phase 4: Feasibility check (CRITICAL — answer this FIRST)

Before producing the full checklist:

**Is this approach actually feasible?**

Specifically:
1. Can the Puiseux expansion be computed to enough terms in SageMath?
2. Can the remainder be bounded rigorously?
3. Does the irrationality measure argument give an EFFECTIVE bound?
   (Roth is ineffective. Thue-Siegel is effective but bounds can be huge.
   Baker gives effective bounds for specific algebraic numbers.)
4. Is the resulting cutoff small enough for brute force?

If ANY of these fail, say so IMMEDIATELY and explain what would be needed.
Do NOT produce a fake checklist. The Baker/LLL attempt already died 
honestly — this one should too if it's not going to work.

## Context

We have now killed 6 approaches to this problem:
- KB irreducibility framework (Codex: converse false)
- Hasse-Minkowski (Codex: vacuous)
- k=2 dominance (Codex: self-contradictory)
- Modular sieve (GPT: proved impossible for any modulus)
- Chabauty on C_{4,5} (Codex: genus 6, nonhyperelliptic, no free tools)
- Baker/LLL (Codex: Λ=0 on solutions, αᵢ vary, 4^{1/5} irrational)

This is the 7th attempt. If it also fails, say so honestly and we will 
write up the negative results as a research note. Honest failure is 
more valuable than fake progress.
