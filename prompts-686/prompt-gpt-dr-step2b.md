# PROMPT FOR GPT DR — Step 2B: Cross-Branch Lemma Transplant Search
# Paste this entire thing into GPT Deep Research (or ChatGPT with research mode).

---

You are operating as part of a multi-model research pipeline targeting Erdős Problem 686. You are communicating with another model, not a student. Be direct. Commit to claims. Flag errors without softening. I don't care if fields seem unrelated — that's the point.

## Your Role: Step 2B — Cross-Branch Search

## The Target Problem (686)

Can every integer N ≥ 2 be written as N = ∏_{1≤i≤k}(m+i) / ∏_{1≤i≤k}(n+i) for some k ≥ 2 and m ≥ n+k?

Open. Number theory. The known failures are {4, 25, 49, 64, 81} — all perfect powers — up to N = 100.

## The Abstract Obstructions (from Step 0)

Here are five obstruction properties, stripped of number theory vocabulary. For EACH one, I need you to search across all of mathematics for where structurally similar obstructions appeared and were overcome.

### Obstruction 1: Rigid factorization patterns resist flexible representation.
Certain integers (perfect powers) have prime factorizations with a very specific rigid structure (all exponents are multiples of some d). The representation system (ratios of consecutive products) generates numbers whose prime factorizations follow a different pattern (exponents determined by carry-counting in base-p arithmetic). The rigid structure and the generated pattern may be incompatible for specific inputs.

**Search for:** Problems in ANY field where a rigid algebraic structure on the input prevents it from being expressed in a system whose outputs follow a different structural pattern. Where has this incompatibility been characterized or overcome?

### Obstruction 2: Small instances are harder than large instances.
The representation system has more degrees of freedom for large inputs (many possible k, m, n triples). For small inputs, the search space is thin. The hard cases are concentrated at small values.

**Search for:** Results in ANY field where a representability or expressibility theorem was proved by handling large cases analytically and small cases by separate methods. Specifically: what techniques exist for proving "every object above size X has property P" and then separately verifying below X?

### Obstruction 3: A discrete valuation encodes the representation constraint.
The p-adic valuation of the ratio ∏(m+i)/∏(n+i) equals the difference in carry counts (Kummer's theorem) between two base-p additions. For N to be representable, its p-adic valuation at every prime must be achievable as such a carry difference.

**Search for:** Problems in ANY field where a discrete valuation or grading constrains representability. Where has carry arithmetic (base-p digit analysis) appeared outside classical number theory? Has anyone characterized which valuation profiles are achievable by differences of carry counts?

### Obstruction 4: A gap constraint between two structured blocks limits the search.
The numerator product must start AFTER the denominator product ends (m ≥ n+k). This creates a mandatory gap between the two blocks. The gap size interacts with N and k to constrain representations.

**Search for:** Problems in ANY field where two structured objects (intervals, blocks, sequences) must be non-overlapping, and the gap between them constrains what relationships they can encode. Scheduling theory, coding theory, and combinatorial design all have gap constraints — find the most structurally similar instances.

### Obstruction 5: A free parameter provides infinite attempts but success isn't guaranteed.
The parameter k is free — you can try any k ≥ 2. For each k, you get a different Diophantine equation. The question is whether for SOME k a solution exists. Failure means failure for ALL k simultaneously.

**Search for:** Results in ANY field where a universally quantified existence statement ("there exists some k such that...") was proved or disproved. Covering system arguments, Helly-type theorems, compactness arguments — what techniques exist for showing that among infinitely many attempts, at least one succeeds?

## Output Format

For each obstruction, give me:

(a) 3-5 instances from GENUINELY DIFFERENT branches of mathematics where a structurally similar obstruction appeared.
(b) For each instance: the problem, the field, the technique that resolved it.
(c) Rate the structural match: STRONG / MODERATE / WEAK.
(d) For any STRONG match: sketch specifically how the technique would adapt to 686. What maps to what? Where does the analogy break?

Reject any match where you can't state the structural correspondence in ≤ 2 sentences. Vague analogies are useless.

## Special Focus

The perfect powers question is the sharpest sub-problem. Why do 4, 25, 49, 64, 81 fail? Is there a characterization of which integers CANNOT be ratios of equal-length products of consecutive integers? If you find ANY result — in any field — that characterizes when rigid objects can or cannot be expressed through flexible systems, flag it prominently.
