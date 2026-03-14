# Difficulty Chart: Erdős Problems Solved With AI Models
## March 10, 2026

Ranked from easiest to hardest based on: proof complexity, novelty of techniques,
whether the result existed in literature, and mathematical depth required.

---

## TIER 1: Literature Rediscovery (AI as librarian)
**Difficulty: ★☆☆☆☆**

These weren't "solved" — AI found existing papers that humans hadn't linked to the Erdős database.

| Problem | What happened | Model used |
|---------|--------------|------------|
| #1089 | Gemini found an offhand remark in a 1981 paper | Gemini |
| #339 | Sawhney found it "too approachable," Googled and found the reference | Human + search |
| ~90 problems Oct 2025 | OpenAI claimed GPT-5 "solved" 10 problems — turned out to be literature search | GPT-5 |

**What it takes:** No math. Just good search across obscure papers.

---

## TIER 2: Formalization of Known Proofs (AI as translator)
**Difficulty: ★★☆☆☆**

The proof exists in a paper. AI converts it to Lean. Math is done, engineering remains.

| Problem | What was formalized | Model/Tool |
|---------|-------------------|------------|
| #645 | Boris's first automated pipeline run | Aristotle |
| #316 (main) | Counterexample {2,3,4,5,6,7,10,11,13,14,15} verified by decide | Mehta (human) |
| #379 | Tao's proof formalized | Aristotle |
| #987 | Tao solved it (not knowing Erdős had too), formalized | Aristotle |
| **#494 product (YOU)** | **Counterexample {0,1,2} vs {0,1,3}** | **Aristotle + Axle** |
| #367 | Van Doorn's construction + Tao simplified + Boris formalized | Gemini + Aristotle |

**What it takes:** Working pipeline (Aristotle/Axle), ability to match Lean statements,
patience for debugging. No original mathematical insight needed.

---

## TIER 3: AI Finds Loopholes / Weaker Versions (AI as clever reader)
**Difficulty: ★★★☆☆**

AI doesn't solve the intended problem but finds a version that's easier than anyone realized.

| Problem | What happened | Model/Tool |
|---------|--------------|------------|
| #124 (weak) | Erdős omitted a key hypothesis in two papers. Aristotle exploited this, solving a version that's a corollary of Brown's criterion. "No one noticed until Boris threw it at Aristotle" | Aristotle (autonomous, 6 hours) |
| #481 | Barreto solved it not knowing Klarner solved it in 1982. Aristotle formalized AND solved independently | GPT-5.2 Pro + Aristotle |

**What it takes:** A formalized statement that's slightly different from what humans assume.
AI doesn't have the "but surely Erdős meant..." bias that humans have.

---

## TIER 4: AI Generates Original Counterexamples (AI as constructor)
**Difficulty: ★★★☆☆ to ★★★★☆**

The proof didn't exist in literature. AI constructs an explicit mathematical object that
disproves a conjecture.

| Problem | What was constructed | Model/Tool |
|---------|---------------------|------------|
| #397 | Infinite family: for a≥2, c=8a²+8a+1, specific centralBinom triple equality | GPT-5.2 Pro → Aristotle |
| #316 (Stobart) | Minimal counterexample {2,3,4,5,6,7,10,11,13,14,15} found by search | Human (Tom Stobart) |
| #198 | AlphaProof found a counterexample | AlphaProof |
| #730 | AlphaProof found an interesting example | AlphaProof |

**What it takes:** Computational search + algebraic verification. Disproving is generally
easier than proving because you only need ONE counterexample.

---

## TIER 5: AI Proves Genuinely Open Conjectures (AI as mathematician)
**Difficulty: ★★★★☆**

The conjecture was open. AI generated an original proof. Result wasn't in literature.

| Problem | What was proved | Model/Tool |
|---------|----------------|------------|
| #728 | Factorial divisibility logarithmic gap phenomenon. First Erdős problem "fully resolved autonomously by AI" with no prior literature found | GPT-5.2 Pro → Aristotle |
| #729 | Variant of 728, adapted techniques | GPT-5.2 Pro → Aristotle |
| #1026 | Weighted Erdős-Szekeres: monotone subsequence sum ≥ 1/k. Rectangle packing proof | Aristotle (autonomous) |
| #868 | Minimal asymptotic bases — disproof via canary construction | Larsen + AI assistance |

**What it takes:** Model generates a full mathematical argument humans haven't found.
Usually uses known techniques in a new combination (Disguise Type 3).
Human orchestration critical for problem selection and iteration.

---

## TIER 6: AI Solves Research-Level Open Problems (AI as research partner)
**Difficulty: ★★★★★**

Problems that professional mathematicians actively worked on. Solutions involve
non-trivial creativity.

| Problem | What was proved | Model/Tool |
|---------|----------------|------------|
| FrontierMath Open (hypergraph) | Ramsey-style hypergraph construction beating known bounds by c>1. FIRST FrontierMath Open Problem potentially solved. Constant pushed from 57/56 → 49/48 → ln(4) → 26/25 through iteration | GPT-5.4 Pro (Leeham + AcerFur) |
| Convex optimization bound | Improved known bound from 1/L to 1.5/L. Sébastien Bubeck's open problem | GPT-5 Pro (17 min reasoning) |
| Statistical learning theory | Learning curve monotonicity for MLE. Published as paper | GPT-5.2 Pro |
| Naskręcki's 20-year problem | FrontierMath Tier 4 problem worked on for ~20 years | GPT-5.4 |

**What it takes:** Frontier model capability + precise problem formulation + human
iteration on the output. These are still rare and each one makes news.

---

## TIER 7: Genuinely Hard Open Problems (AI fails here)
**Difficulty: ★★★★★★**

| Problem | Status | Why AI fails |
|---------|--------|-------------|
| $500+ Erdős prizes | Still open | Require genuinely novel techniques |
| FrontierMath Open Problems (most) | GPT-5.4 Pro scored 0/remaining | Need ideas that don't exist in training data |
| Millennium Problems | Untouched | Fundamentally beyond current architecture |
| Erdős problems requiring new math | ~400+ still open | "Connection" approach doesn't work when no connections exist |

---

## WHERE YOU SIT

```
TIER 1  ──  Literature search (not what you did)
TIER 2  ──  ████████████████  ← YOU ARE HERE (494 product variant)
TIER 3  ──  Reachable with current pipeline + smarter problem selection
TIER 4  ──  Reachable now (more 494 variants, stronger counterexamples)  
TIER 5  ──  Reachable in months (with understanding tree + better models)
TIER 6  ──  Where AcerFur/Leeham are today. Reachable by ~2027-2028
TIER 7  ──  Nobody's here yet. This is where the IMO/MOP math training pays off
```

## THE KEY PATTERN ACROSS ALL TIERS

Every tier shares the same structure:
1. Human selects the problem (taste + judgment)
2. AI generates candidate (speed + breadth)  
3. Verification confirms correctness (Lean/Axle or computational check)
4. Community validates and contextualizes (literature search, forum discussion)

What changes between tiers is how much ORIGINAL MATHEMATICAL INSIGHT
the AI contributes vs. how much it's executing known patterns.

At Tier 2 (where you are): AI executes a known proof in a new language.
At Tier 5: AI combines known techniques in a way nobody had tried.
At Tier 6: AI generates ideas that surprise professional mathematicians.
At Tier 7: Nobody yet. The gap is "genuinely new mathematical concepts."

---

*Compiled from: erdosproblems.com, teorth/erdosproblems wiki, Tao's blog,
AcerFur/Leeham Twitter threads, Epoch AI FrontierMath results, Xena blog*
