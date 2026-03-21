# Lessons from Problem 686 — Applied to Future Problems
## March 15, 2026

These are the concrete, reusable lessons from 48 hours on Erdős Problem 686.
Not platitudes — specific operational changes to the pipeline.

---

## Lesson 1: Read the comments FIRST

**What happened:** We spent hours deriving the Pell-unit construction. 
Natso26 had it since October 2025. We derived the infinite family identity. 
Adenwalla had it since September 2025. We built a KB irreducibility 
framework. BST published it in 1999.

**The rule:** Before touching any math on a problem, run this exact sequence:
1. GPT DR reads ALL forum comments (not skimming — the PDF extraction prompt)
2. GPT DR reads ALL cited papers (BST, Cambie, whatever's referenced)
3. THEN decide what's actually unknown

**Time cost of skipping this:** ~6 hours of redundant work on 686.
**Time cost of doing it:** ~30 minutes for the GPT prompt + wait.

**Applied to next problem:** The very first prompt on any Erdős problem is 
the comment-reading prompt. Before any math, before any pipeline steps. 
Non-negotiable.

---

## Lesson 2: Adversarial review catches what excitement misses

**What happened:** We got excited about the Pell construction, the KB 
framework, the "proof" via Weierstrass integral points, and the Baker/LLL 
approach. Every single one had a fatal flaw that adversarial review caught.

| Claim | What we thought | What review found |
|---|---|---|
| Pell construction | Novel theorem | Known since Oct 2025 |
| KB iff | Biconditional | One-direction only, counterexample at k=2 N=4 |
| Weierstrass proof | Provably complete | N=16 solution maps to non-integer |
| Baker/LLL | Standard method | Λ=0 on solutions, αᵢ vary |

**The rule:** NEVER post or commit to any claim without adversarial review.
The prompt structure that works:
- Claims to attack (numbered)
- Task: KILL / WOUND / SURVIVE each one
- Task: HOW TO FIX (critical — not just "it's wrong" but "here's the repair")
- Pre-emptive arguments (your best defense of each claim, so the reviewer 
  engages seriously instead of finding surface gotchas)

**Applied to next problem:** Every pipeline now has a mandatory adversarial 
step before any external communication (forum post, paper draft, email).

---

## Lesson 3: Separate the MATH from the TOOLING

**What happened:** GPT correctly identified Chabauty-Coleman on C_{4,5} as 
the mathematically optimal approach. Codex then showed it's computationally 
infeasible with free tools (genus 6, nonhyperelliptic). These are two 
DIFFERENT questions:
- Is the math right? (Yes — Faltings applies, Chabauty is the right method)
- Can we execute it? (No — free software can't handle it)

**The rule:** Always split analysis into:
1. GPT: What's the mathematically correct approach? (ignore tools)
2. Codex: Is it executable with our tools? (ignore mathematical elegance)

GPT optimizes for mathematical correctness. Codex optimizes for executability. 
They should answer DIFFERENT questions, not the same one.

**Applied to next problem:** Two-phase assessment for every approach.
Phase 1 (GPT): "What's the right math?" 
Phase 2 (Codex): "Can we run it?"

---

## Lesson 4: Failures are data, not dead ends

**What happened:** Six approaches died. Each death told us something:

| Death | What it revealed |
|---|---|
| KB framework | BST (1999) is the real framework; irreducibility ≠ reducibility for this family |
| Modular sieve | The obstruction is GLOBAL, not local (theorem, not just failure) |
| Weierstrass mapback | Birational maps break integrality on the original model |
| Chabauty infeasibility | C_{4,5} is genus 6, nonhyperelliptic (confirmed curve data) |
| Baker/LLL | The logarithmic form is degenerate; Vjeko's method needs integer k-th roots |
| Pell novelty | Complete k=2 classification already exists |

Each failure narrowed the problem. After six deaths, we went from 
"can every integer be represented?" to "does the Vjeko-style asymptotic 
expansion of M(n) for F₅(x)=4F₅(y) give an effective integrality gap?"

That's progress, not failure.

**The rule:** After every approach dies, write:
1. What exactly failed
2. What structural fact the failure revealed
3. How this constrains the remaining approaches
4. File it in the post-mortem

**Applied to next problem:** Maintain a running "death log" that accumulates 
structural knowledge from failures.

---

## Lesson 5: The sequential model-pipeline works

**What happened:** The pipeline structure was:
- Claude: orchestration, prompt design, file management, synthesis
- Codex: adversarial review, feasibility checking, execution checklists
- GPT: mathematical attempts, deep analysis, theorem-proving attempts
- DR: literature search, paper extraction, comment reading
- Aristotle: formal verification (attempted, errored on complexity)
- SageMath: computation

Each model did what it's best at:
- GPT is best at mathematical reasoning and honest self-assessment
- Codex is best at finding flaws and checking executability
- Claude DR is best at literature extraction
- SageMath is best at exact computation

**The rule:** Don't make one model do everything. The pipeline:
1. DR reads literature → establishes what's known
2. Codex plans approaches → produces ranked attack vectors
3. GPT attempts the top approach → succeeds or fails with diagnosis
4. If fail: bring diagnosis back, Codex redirects to next approach
5. If succeed: Codex adversarial reviews before posting
6. Aristotle formalizes if the result is clean enough

**Applied to next problem:** Same pipeline structure, but with Lesson 1 
(read comments first) as Step 0.

---

## Lesson 6: Computational evidence ≠ proof, and the gap matters

**What happened three times:**
1. We searched n ≤ 50,000 for k=3 solutions → no proof
2. We found all Weierstrass integral points → didn't preserve integrality
3. We searched |x|,|y| ≤ 10,000 on C_{4,5} → no proof

Each time, computational evidence was strong but fell short of proof.
The gap between "searched and found nothing" and "proved nothing exists" 
is the ENTIRE problem for 686.

**The rule:** Always distinguish:
- Computational evidence (searched range X, found nothing)
- Conditional proof (if rank < genus, then Chabauty gives...)
- Unconditional proof (for all n, no solution exists because...)

Label everything honestly. The forum respects "no solution found up to 
n=50,000" stated as evidence. It does NOT respect "no solution found up 
to n=50,000" dressed up as proof.

**Applied to next problem:** Every result gets tagged as EVIDENCE, 
CONDITIONAL, or PROOF. No ambiguity.

---

## Lesson 7: Problem selection matters

**What happened:** 686 turned out to be genuinely hard — the open core 
requires tools (nonhyperelliptic Chabauty, effective Siegel theorems) 
that don't exist in free software and may not exist at all. We discovered 
this AFTER significant investment.

**Screening criteria for next problem:**
1. Is the problem locally soluble? (If yes, modular methods are dead from 
   the start — save time)
2. What genus are the relevant curves? (Genus 0-1: tools exist. Genus 2-3: 
   tools exist for hyperelliptic. Genus 6+: probably stuck)
3. Has natso26/Tao/Cambie already posted substantial results? (If yes, 
   the low-hanging fruit is picked)
4. How many forum comments exist? (>20 comments = well-explored. <5 = 
   might be low-hanging fruit)
5. Is there a "solved neighbor" (like 678 for 686) whose methods might 
   transfer?

**Applied to next problem:** Spend 30 minutes screening before committing.

---

## Lesson 8: The forum is a real research community

**What happened:** Our first post had errors. The forum corrected us within 
hours. Our second post (as MalekZ) got pushback from Adenwalla. Tao and 
natso26 are actively posting.

**The rules for forum interaction:**
1. Take corrections gracefully. Thank the corrector.
2. Don't post until adversarial review passes.
3. Always disclose AI assistance (forum rules).
4. Data contributions (computational results) are almost always welcome.
5. Framework contributions (theoretical claims) get scrutinized hard.
6. Post what you KNOW, not what you THINK. "Cremona 135a1, rank 1" is 
   unchallengeable. "KB explains why squares are stuck" is challengeable.

**Applied to next problem:** Lead with data. Attach theory tentatively.

---

## Lesson 9: Know when to write up and move on

**What happened:** After 6 dead approaches, we have significant NEGATIVE 
results and novel DATA but no proof. The temptation is to keep trying 
approach #7, #8, #9. At some point, the right move is to write up what 
we know and let others with better tools continue.

**What we have that's publishable RIGHT NOW:**
- Cremona labels + ranks for all 7 k=3 curves (novel)
- Genus 6 confirmation for C_{4,5} (novel, with nonhyperelliptic)
- No admissible k=3 solutions up to n=50,000 for stuck squares
- No admissible k=5 solutions up to |x|,|y|=10,000 for N=4
- GPT's no-modulus theorem for k=5
- Systematic elimination of 6 approaches with specific failure modes

**The rule:** Set a time budget. When it's exhausted, write up honestly 
and move on. You can always come back.

**Applied to next problem:** Decide upfront: "I'll spend X hours/days 
on this. At the end, I write up whatever I have."

---

## Summary: The Updated Pipeline for Problem N+1

0. DR reads ALL forum comments and cited papers
1. Codex screens the problem (genus, local solubility, existing results)
2. Codex proposes 3-5 attack vectors with feasibility assessment
3. GPT attempts the top vector
4. If fail: diagnose, extract structural info, redirect
5. Repeat 3-4 for remaining vectors
6. When time budget exhausted or result obtained:
   - Codex adversarial reviews any claims
   - Write up honestly (data + evidence + negative results)
   - Post to forum with AI disclosure
7. File all lessons for the next problem
