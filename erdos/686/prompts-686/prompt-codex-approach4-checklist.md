# Codex Execution Checklist Prompt — Approach 4: Chabauty-Coleman on C_{4,5}
## For Codex at xhigh

You are producing an execution checklist for a concrete mathematical 
computation. This is not a research direction — it is a step-by-step 
procedure that will be executed by a 13-year-old with access to SageMath 
(via CoCalc), PARI/GP, and the LMFDB database. Every step must be:

- Precise enough to execute without mathematical training beyond the instructions
- Accompanied by the EXACT code to run (SageMath or PARI/GP)
- Accompanied by the EXACT output to expect (or the range of possible outputs)
- Accompanied by a decision tree: "if output is X, proceed to step N; if output is Y, the approach fails because Z"

## The Target

The curve C_{4,5} defined by:

  (x+1)(x+2)(x+3)(x+4)(x+5) = 4·(y+1)(y+2)(y+3)(y+4)(y+5)

Equivalently, expanding both sides:

  F(x) = 4·F(y)

where F(t) = (t+1)(t+2)(t+3)(t+4)(t+5) = t⁵ + 15t⁴ + 85t³ + 225t² + 274t + 120.

We want to determine ALL rational points on C_{4,5}, or at minimum all 
INTEGER points with x ≥ y + 5 (admissible 686 solutions).

## Background for Codex

- This is a plane curve of degree 5 in each variable (bidegree (5,5) in P¹×P¹).
- BST (1999) and GPT's analysis indicate genus > 1 for this curve.
- By Faltings' theorem, a genus > 1 curve has finitely many rational points.
- The Chabauty-Coleman method can explicitly determine all rational points 
  when the Mordell-Weil rank of the Jacobian is strictly less than the genus.
- If rank ≥ genus, Chabauty fails and we need alternative methods (Mordell-Weil 
  sieve, étale descent, or explicit Baker bounds).

## THE CHECKLIST

### Phase 0: Verify the curve and compute basic invariants

**Step 0.1: Define the curve in SageMath**

Provide the exact SageMath code to:
- Define the polynomial ring in x, y over QQ
- Define F(t) = (t+1)(t+2)(t+3)(t+4)(t+5)
- Define the curve equation f = F(x) - 4*F(y)
- Verify f is irreducible over QQ (this confirms BST)
- Print the total degree and bidegrees

**Step 0.2: Compute the geometric genus**

Provide the exact SageMath code to:
- Construct the projective closure of C_{4,5}
- Compute the arithmetic genus and geometric genus
- Handle any singularities (list them, compute delta invariants)
- State the genus explicitly

The expected genus for a smooth separated-variables curve f(x) = cg(y) 
with deg f = deg g = 5 is related to the Riemann-Hurwitz formula. 
Provide the exact expected value and how to verify it.

**Step 0.3: Find obvious rational points**

Provide code to:
- Search for integer points with |x|, |y| ≤ 10000 by brute force
- Identify all "trivial" points (where F(x) = F(y) = 0, i.e., x or y ∈ {-1,-2,-3,-4,-5})
- List all found points
- For each, check admissibility (x ≥ y + 5, both ≥ 0)

**Decision point:** If an admissible integer point is found, STOP — N=4 is 
k=5 representable and the whole analysis changes. If not, continue.

### Phase 1: Compute the Jacobian

**Step 1.1: Determine the Jacobian variety**

This is the hardest computational step. Provide:
- The mathematical procedure to go from the plane curve to its Jacobian
- Whether SageMath can compute this directly for a genus-g curve with g > 1
- If SageMath can't do it directly, provide the MAGMA online calculator 
  commands (http://magma.maths.usyd.edu.au/calc/) as fallback
- If neither works, provide the manual procedure using divisor classes

**Step 1.2: Check if the Jacobian splits**

For separated-variables curves f(x) = cg(y), the Jacobian sometimes 
decomposes into a product of lower-dimensional abelian varieties. 
If it splits, each factor is easier to analyze.

Provide:
- How to check for splitting in SageMath or MAGMA
- What the expected decomposition might look like for this specific curve
- How splitting affects the Chabauty computation

### Phase 2: Compute the Mordell-Weil rank

**Step 2.1: Rank bound via 2-Selmer group**

Provide the exact code to:
- Compute an upper bound on the rank of J(Q) via the 2-Selmer group
- State what software can do this (SageMath? MAGMA? PARI?)
- Give the expected runtime

**Step 2.2: Rank lower bound via point search**

Provide code to:
- Search for independent rational points on C_{4,5}
- Compute the images of these points in J(Q)
- Check linear independence via height pairing or regulator

**Step 2.3: Decision point**

- If rank < genus: Chabauty-Coleman applies. Proceed to Phase 3.
- If rank = genus: Chabauty may still work with extra effort (quadratic 
  Chabauty, Mordell-Weil sieve). Describe what to do.
- If rank > genus: Chabauty fails entirely. Describe the fallback 
  (Baker/LLL bounds, or Approach 5 from our list).

For each case, state:
- What it means mathematically
- What to do next
- How likely each case is (your estimate)

### Phase 3: Chabauty-Coleman (if rank < genus)

**Step 3.1: Choose a good prime p**

Provide:
- How to choose p for Chabauty-Coleman
- Criteria: good reduction, p > 2, rank condition on the mod-p reduction
- The exact SageMath/MAGMA code to verify good reduction at candidate primes
- A list of the first few candidate primes to try

**Step 3.2: Compute Coleman integrals**

Provide:
- The mathematical setup (which p-adic integrals to compute)
- The exact code to run (SageMath's hyperelliptic Chabauty if applicable, 
  or MAGMA's Chabauty)
- What the output looks like (a set of p-adic points)
- How to interpret the output

**Step 3.3: Determine all rational points**

Provide:
- How to go from Chabauty's p-adic output to a provably complete list 
  of rational points
- The Mordell-Weil sieve step (if needed to rule out extra points)
- The exact code
- How to verify the result is complete

**Step 3.4: Check admissibility**

For each rational point found:
- Map back to (x, y) coordinates on the original curve
- Check if x, y are integers
- Check if x ≥ y + 5
- If any admissible point exists: N=4 IS k=5 representable
- If no admissible point exists: N=4 is NOT k=5 representable (PROOF)

### Phase 4: Fallback procedures

**Step 4.1: If SageMath can't compute the Jacobian**

Provide:
- MAGMA online calculator commands for the full pipeline
- How to use the LMFDB if the curve or Jacobian is in the database
- Manual genus computation via Riemann-Hurwitz if computational tools fail

**Step 4.2: If rank ≥ genus**

Provide:
- The Baker/LLL approach (Approach 5): exact mathematical setup for C_{4,5}
- What effective height bounds look like for this specific curve
- How to run the final exhaustive search once bounds are known
- Estimated feasibility (is the bound likely to be computationally reachable?)

**Step 4.3: If the curve turns out to have genus ≤ 1**

This would be surprising but must be handled:
- If genus 1: use the k=3 approach (elliptic curve, integral points on 
  Weierstrass model — but with the caveat about integrality preservation)
- If genus 0: parametrize and directly enumerate

## Output Format

For each step, provide:

```
STEP N.M: [Title]
MATHEMATICAL CONTENT: [What we're computing and why]
SAGMATH CODE:
```python
[exact code to paste into CoCalc]
```
EXPECTED OUTPUT: [What you expect to see]
DECISION: 
  - If [condition A]: proceed to Step N.M+1
  - If [condition B]: the approach fails; go to Step 4.X
  - If [condition C]: STOP — we have a result
FAILURE MODE: [What could go wrong at this step]
ESTIMATED TIME: [How long the computation takes]
```

## Constraints

- Every piece of code must be runnable in CoCalc's free SageMath environment 
  (SageMath 10.x) or the free MAGMA online calculator.
- Do not assume access to paid software, supercomputers, or custom C code.
- Do not skip steps. The person executing this has never done Chabauty before.
- Do not say "this is standard" without providing the code.
- If a step is genuinely beyond free software capabilities, say so explicitly 
  and provide the MAGMA online calculator alternative.
- If the entire approach is infeasible with free tools, say so at the START 
  before wasting anyone's time, and describe exactly what tools would be needed.

## Context

This computation, if successful, would prove that N=4 is not representable 
at k=5 in Erdős Problem 686. Combined with existing results for k=2,3,4,6, 
this would rule out six consecutive k values for N=4 and bring a disproof 
of the Erdős conjecture significantly closer. The computation is being 
executed as part of a human-AI collaborative research pipeline involving 
Claude, GPT, Codex, and Aristotle. Results will be posted to the 
erdosproblems.com forum with full AI disclosure.
