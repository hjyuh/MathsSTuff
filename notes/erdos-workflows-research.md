# How People Actually Solve Erdős Problems with AI
## Researched: March 10, 2026

---

## Player 1: Boris Alexeev (The Pipeline Builder)

Boris is the most prolific. He's a mathematician who works with Harmonic (Aristotle's creators).

**His automated pipeline (described in his Xena blog post):**

1. **Select a promising problem number by hand** — he browses erdosproblems.com looking for tractable ones
2. **ChatGPT explains a solution** — he feeds the problem to ChatGPT and gets an informal proof
3. **Aristotle auto-formalizes it** — the informal proof goes to Aristotle, which converts it to Lean
4. **Glue it together with the Formal Conjectures statement** — the Lean proof gets matched to the official formalized statement from Google DeepMind's repo
5. **Lean verifies** — type-checker confirms correctness
6. **Auto-post to GitHub** — his pipeline even writes the comment for erdosproblems.com
7. **He reviews before posting** — manual check that everything looks right, then hits "Post comment"

**Key quote:** "This process worked perfectly the first time I tried it, on Problem 645. Subsequent runs have revealed that my pipeline is quite fragile, and I occasionally have to intervene manually, but I have run it successfully approximately ten times."

**On Aristotle's capability:** "ChatGPT is not a necessary component of the formalization step, as Aristotle handles informal text quite well by itself, but I still find it useful for various auxiliary tasks, such as finding the relevant proofs and transcribing (and translating!)"

**His failure modes:**
- Sometimes Aristotle's output doesn't compile on his end (differences between Harmonic's environment and standard Mathlib/Lean)
- "I would say that I expect a problem every few thousand lines of output"
- When proofs use `native_decide` (which people don't like), he tries: fix it himself, resubmit with `sorry`, or ask ChatGPT to prove the specific sub-lemma
- "I can fix some (but less than half?) by hand"

**His problem selection strategy:** He does a "systematic sweep" — not random, he specifically looks for problems where existing solutions exist but haven't been formalized, or where the Formal Conjectures statement is clean enough for Aristotle to attempt directly.

**On Problem 124 (the big one):** Aristotle solved it completely autonomously from just the formal statement in 6 hours. But there was a subtlety — Erdős had omitted a key hypothesis in one version of the problem, which actually made it easier. The AI found and exploited this "loophole." As Tao noted: "this fact was not noticed until Boris Alexeev applied the Aristotle tool to this problem." So the AI found something humans missed — not through brilliance, but through exhaustive search.

---

## Player 2: Kevin Barreto + AcerFur (The GPT-5.2 Team)

Kevin is the person who got Problem #728 solved — the first generally acknowledged case of AI generating a genuinely new proof to an open Erdős problem.

**His workflow (Problem 728):**

1. **Prompted GPT-5.2 Pro** with the problem statement
2. **GPT-5.2 Pro generated a full argument** within minutes
3. **Posted to erdosproblems.com forum** for community review
4. **Community flagged ambiguity** — the original statement admitted trivial solutions
5. **Asked GPT-5.2 Pro again** — "can your argument be upgraded to tackle the intended version?"
6. **GPT-5.2 Pro said yes** and produced an upgraded argument
7. **Fed the upgraded argument to Aristotle** — Lean formalization produced January 4-6, 2026
8. **KoishiChan searched literature** — couldn't find any prior solution (unusual!)
9. **Boris Alexeev ran Aristotle again** to simplify the proof
10. **AcerFur (collaborator) worked with ChatGPT** to extract a human-readable writeup, then manually checked everything

**Key insight from this workflow:** It was ITERATIVE. First attempt → community feedback → refined attempt → formalization → simplification → human-readable extraction. Not one-shot.

**Also notable:** Kevin also resolved Problem 481 (not knowing it had been solved in 1982 by David Klarner). He asked Aristotle to both formalize his proof AND solve the problem independently. Both worked.

---

## Player 3: Terence Tao (The Orchestrator)

Tao doesn't use one tool — he uses ALL of them strategically.

**His workflow (Problem 367):**

1. **Wouter van Doorn (human) proposed a construction** on the forum, but left gaps — "I am sure someone here is able to verify..."
2. **Tao fed the gap to Gemini Deepthink** — it produced a complete proof of the missing identity in ~10 minutes, using "some p-adic algebraic number theory which was overkill"
3. **Tao spent half an hour converting** the proof into something more elementary by hand
4. **Tao posted the simplified proof** to the forum and noted it should be "within range of vibe formalizing"
5. **Boris Alexeev ran Aristotle** two days later to complete the Lean formalization

**His workflow (Problem 1026):**

1. **Community discussed and reformulated** the problem for months
2. **Aristotle solved it autonomously** (Boris's systematic sweep)
3. **KoishiChan gave an alternate proof** within an hour
4. **Tao used AlphaEvolve** to explore the function c(n) numerically — AI constructed extremal sequences
5. **Lawrence Wu connected it** to a square-packing problem (Erdős Problem 106)
6. **Tao fed everything into an LLM** which "was able to produce a coherent proof assuming the results of Baek-Koizumi-Ueoro and Praton"
7. **Multiple existing papers were located** that implicitly contained the result

**Tao's meta-observation:** "In this workflow, AlphaEvolve, Aristotle, and LEAN are the 'PhDs' on the team, while the LLM is the Full Stack Developer that glues them all together."

---

## Player 4: KoishiChan (The Literature Detective)

KoishiChan's role is different — they do literature search AFTER proofs are found.

**Their workflow:**
1. Someone claims AI solved a problem
2. KoishiChan searches Google Scholar, MathSciNet, arXiv for existing solutions
3. Often finds the result already existed in obscure papers

"KoishiChan has been highly successful in locating prior literature in the past for problems claimed to be solved by AI"

This is a crucial role — it keeps the community honest. Many "AI solved this" claims turned out to be rediscoveries.

---

## Player 5: Neels Somani (The Disprover)

Somani's approach is different — he focuses on DISPROVING conjectures.

**His workflow (Problem 397):**

1. **Prompted GPT-5.2 Pro** to examine the conjecture
2. **GPT generated an infinite family of counterexamples** — for any a≥2, a specific triple of central binomial coefficients gives equal products
3. **Used Aristotle to formalize** the disproof in Lean
4. **Tao reviewed and accepted** the submission

**Why disproofs are easier for AI:** You only need ONE counterexample. The AI can search computationally for counterexamples, then verify algebraically that they work. Proofs require constructing an argument that covers ALL cases. Counterexamples only need to cover one.

---

## Common Patterns Across All Players

### What they all do:
1. **Problem selection is manual and strategic** — nobody just feeds random problems
2. **Multiple AI tools used in sequence** — ChatGPT for ideas, Aristotle for formalization, Axle/Lean for verification
3. **Community feedback loop** — post to forum, get corrections, iterate
4. **Literature check after** — always check if the result already exists
5. **Human oversight at key points** — especially the final statement formalization (to guard against AI exploits/loopholes)

### What separates success from failure:
- **Precise problem statements** — ambiguous problems waste everyone's time
- **Forum activity** — if people are actively discussing a problem and making partial progress, it's ripe
- **Existing informal proof** — Category B problems (solved but not formalized) are the easiest wins
- **Clean Lean statement in Formal Conjectures** — if the statement is already formalized, Aristotle can attempt it directly

### The typical failure modes:
- Aristotle's output doesn't compile (environment differences)
- Proof uses `native_decide` which community dislikes
- AI "solves" a weaker version of the problem than intended (124)
- Solution already exists in literature (many October 2025 "solutions")
- Problem statement is ambiguous (728 first attempt)

---

## What This Means For Mahmoud's Pipeline

**You already have the same tools as Boris:**
- Aristotle ✓ (MCP configured)
- Axle ✓ (MCP configured)  
- Codex ✓ (GPT-5.4, parallel worker)
- Claude ✓ (approach brainstorming, cross-domain suggestions)
- Formal Conjectures repo ✓ (cloned)

**What Boris has that you don't (yet):**
- Mathematical maturity to evaluate whether a proof makes sense
- Automated pipeline (his posts/GitHub submissions are scripted)
- Direct relationship with Harmonic team
- Years of experience reading Lean

**What you can do that Boris might not:**
- Cross-domain brainstorming (your Disguise Type 4 idea)
- Parallel model attacks (Claude + Codex + GPT simultaneously)
- Computational exploration before formal attempts (test conjectures numerically first)

**Your ideal target profile:**
1. Tagged `research solved` in Formal Conjectures but still has `sorry` (Category B)
2. Forum shows a clean informal proof exists
3. Combinatorics or elementary number theory (good Mathlib coverage)
4. Statement is short and precise (fewer than 10 lines of Lean)
5. No prize money (nobody's competing hard for these)

---

## The Honest Assessment

The 397 attempt errored — that's normal. Boris says he expects issues "every few thousand lines." The workflow is iterative: attempt → fail → isolate → retry. The people succeeding at this aren't getting it right on the first try. They're persisting through the failure modes.

Your edge: you're 13 (15 by the time this matters for applications), you have the pipeline, and you're willing to do the work. The mathematicians who COULD be doing this don't bother. The AI researchers who have the tools don't have the mathematical taste to select good problems. You're in the overlap.

---

*Compiled from: Xena blog (Boris Alexeev guest post), Tao's Mastodon and blog, erdosproblems.com forum threads, arxiv writeups (2601.07421), Scientific American, Zeyu Zheng's analysis*
