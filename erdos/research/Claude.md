# Best Erdős problem targets for AI-augmented formal verification

**The most promising pipeline targets cluster in three areas: additive combinatorics counterexample proofs (Tier A), number theory AI-replications (Tier B), and finite-set/Sidon-set moonshots (Tier C).** Given your team's demonstrated strength at Finset arithmetic, counterexample constructions, and one-shot formalizations under 200 lines, the sweet spot is "research solved" problems in the Formal Conjectures repo with `sorry`-tagged proofs that involve concrete finite objects. The pipeline (Claude → GPT → Codex → Aristotle → Axle) maps cleanly onto the Boris Alexeev workflow that has already formalized ~10 Erdős problems, and the eight candidates below are ranked by feasibility within that workflow.

## Landscape: what's already been done

Before diving into targets, a critical orientation. Of the **1,183 problems** in the erdosproblems.com database, **491 are solved** and **378 have Lean statements** in the Formal Conjectures repo. However, only **~116 solutions are formalized in Lean** — leaving roughly **260+ problems** with formalized statements but unformalized proofs. This gap is your opportunity.

Boris Alexeev's pipeline (ChatGPT → Aristotle → Lean, documented at the Xena Project blog in December 2025) has been the dominant formalization engine, producing the majority of public Lean proofs on erdosproblems.com. Problems already formalized by Alexeev, Neel Somani, and Terence Tao — including 56, 105, 124, 198, 316, 367, 379, 397, 401, 418, 481, 488, 613, 645, 707, 728, 729, 871, 942, 958, 987, 1026, 1043, and 1077 — are excluded below. Problems 728, 729, and 397 (the reference "AI-solved" examples) were all formalized within days of proof discovery via GPT-5.2 Pro + Aristotle, demonstrating that the full pipeline cycle takes **hours, not weeks**, when the proof is elementary.

Key tools in the ecosystem: **Aristotle** (Harmonic) handles autoformalization from LaTeX/natural language to Lean 4 and can solve problems autonomously. **AlphaProof** (DeepMind) produces Lean output but often needs cleanup. **GPT-5.2 Pro** has been the breakthrough model for generating candidate proofs. **Axle** (Axiom Math's Lean Engine) provides proof verification primitives and achieved 12/12 on Putnam 2025 but has not yet been applied to Erdős problems — making your pipeline a novel combination.

---

## Candidate #1: Problem 868 — Additive basis without minimal sub-basis

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/868 |
| **Statement** | Let A be an additive basis of order 2 (every sufficiently large integer is a sum of two elements of A), and let f(n) count the number of representations of n as a+a' with a,a' ∈ A. If f(n) → ∞, must A contain a minimal additive basis of order 2 (one where removing any single element destroys the basis property)? **Answer: No.** |
| **Tier** | **A** (solved, not formalized) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/868.lean`, tagged `research solved`, AMS 11. Uses `Set.IsAsymptoticAddBasisOfOrder`. Contains `sorry`. |
| **Status** | Disproved (23 Jan 2026). Solution NOT formalized in Lean. |
| **Why good target** | This is a **counterexample construction** — exactly your team's demonstrated strength from Problem 494. The disproof builds an additive basis with f(n)→∞ but no minimal sub-basis. The formal statement already exists using Mathlib's additive basis infrastructure. Counterexample disproofs are the most pipeline-amenable pattern: GPT generates the construction, Codex encodes it in Lean, Aristotle fills sorry holes, Axle verifies. |
| **Difficulty** | **4/10** |
| **Mathlib deps** | `Finset`, `Nat`, `Set.IsAsymptoticAddBasisOfOrder`, basic arithmetic, `Filter.Tendsto`, `Filter.atTop` |
| **Forum activity** | 8 posts; Terence Tao has commented. Active discussion but nobody is formalizing. |

---

## Candidate #2: Problem 899 — Difference sets must grow unboundedly

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/899 |
| **Statement** | Let A ⊂ ℕ be an infinite set. Is it true that |(A − A) ∩ {1,…,N}| / |A ∩ {1,…,N}| → ∞ as N → ∞? Equivalently: the ratio of the number of differences to the number of elements must diverge. **Answer: Yes.** |
| **Tier** | **A** (solved, not formalized) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/899.lean`, tagged `@[category research solved, AMS 11]`, 51 lines. Contains `sorry`. |
| **Status** | Proved by Ruzsa. Statement formalized; proof NOT formalized in Lean. |
| **Why good target** | The statement is **51 lines of Lean** — compact and clean. Uses basic set difference and density concepts with excellent Mathlib coverage. Ruzsa's proof uses the **Plünnecke-Ruzsa inequality** or direct counting arguments, both within reach of additive combinatorics infrastructure that's already in Mathlib. The proof is self-contained and elementary. Your team's Finset arithmetic strength maps directly onto the required set-difference computations. |
| **Difficulty** | **5/10** |
| **Mathlib deps** | `Finset`, `Finset.card`, set arithmetic (`Set.sub`), `Filter.atTop`, `Filter.Tendsto`, density/counting lemmas |
| **Forum activity** | Minimal. No evidence anyone is working on formalization. |

---

## Candidate #3: Problem 245 — Sumsets grow at least threefold

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/245 |
| **Statement** | Let A ⊂ ℕ be an infinite set with |A ∩ {1,…,N}| = f(N). Must |(A + A) ∩ {1,…,N}| / f(N) ≥ 3 − ε for all ε > 0 and N sufficiently large? **Answer: Yes.** |
| **Tier** | **A** (solved, not formalized) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/245.lean`, tagged `@[category research solved, AMS 11]`, 83 lines. Contains `sorry`. |
| **Status** | Proved (Freiman's work, classical result). Statement formalized; proof NOT formalized in Lean. |
| **Why good target** | Structurally identical to Problem 899 — same Finset counting infrastructure, same proof style. The factor-of-3 growth for sumsets is a foundational result in additive combinatorics provable via **elementary pigeonhole-style arguments** on the sumset structure. Having both 899 and 245 in the pipeline creates a "batch formalization" opportunity — the Lean scaffolding for one carries over to the other. |
| **Difficulty** | **5/10** |
| **Mathlib deps** | `Finset`, `Finset.card`, `Set.add` (pointwise sum), `Filter.atTop`, `Filter.Tendsto`, `Nat.lt_wfRel` |
| **Forum activity** | Minimal. Not under active formalization. |

---

## Candidate #4: Problem 123 (3,5,7 variant) — Complete sequences from three coprime bases

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/123 |
| **Statement** | Let a, b, c be pairwise coprime integers > 1. Is every sufficiently large integer the sum of distinct elements of {aⁱ · bʲ · cᵏ : i,j,k ≥ 0}? The variant for (a,b,c) = (3,5,7) was proved by Erdős and Lewin; the variant for (2,3) is easier. The general case remains open. |
| **Tier** | **A** (the (3,5,7) variant is solved; the general case is Tier C) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/123.lean`, 128+ lines. Contains both `research open` (general) and `research solved` (specific variants) tags. Contains `sorry` in all proof terms. |
| **Status** | Variant (3,5,7): Proved (Erdős-Lewin). General: Open. The .lean file includes both. |
| **Why good target** | The (3,5,7) variant is a **concrete finite-verification-style proof** involving specific products of powers of 3, 5, and 7. The proof that these form a complete sequence for large integers uses **induction and explicit Finset constructions** — directly in your wheelhouse. The formal statement already distinguishes the solved variant, so you can target just the `sorry` for that theorem. Proving the specific case avoids the abstract generalization entirely. |
| **Difficulty** | **6/10** (for the 3,5,7 variant; 9/10 for general) |
| **Mathlib deps** | `Finset`, `Nat.Coprime`, `Nat.pow`, `Finset.sum`, membership proofs, `omega`, `norm_num` for base cases |
| **Forum activity** | Moderate discussion. Multiple variants under study. The specific (3,5,7) case is settled and quiet. |

---

## Candidate #5: Problem 944 (large k variant) — Critical chromatic graphs exist

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/944 |
| **Statement** | A graph G is k-critical if χ(G) = k but every proper subgraph has chromatic number < k. Dirac conjectured that for k ≥ 4, every k-critical graph has a "critical edge" (one whose removal reduces the chromatic number). Erdős asked: is this true for all k? **Answer for large k: No** — Martinsson and Steiner (2025) constructed k-critical graphs without critical edges for all sufficiently large k. |
| **Tier** | **A** (large k variant solved in 2025; k=4 case remains open) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/944.lean`. The large k variant is tagged `@[category research solved]`. Contains `sorry`. |
| **Status** | Large k: Disproved (Martinsson-Steiner, 2025). k=4: Open. |
| **Why good target** | Graph coloring is one of your target areas. Mathlib has `SimpleGraph.chromaticNumber` and related infrastructure. The large k disproof is a **construction** — building a specific family of graphs. If the construction is explicit enough (rather than probabilistic), it's amenable to your counterexample pipeline. The k=4 case is a natural follow-up moonshot. |
| **Difficulty** | **6/10** |
| **Mathlib deps** | `SimpleGraph`, `SimpleGraph.chromaticNumber`, `SimpleGraph.Subgraph`, `Finset`, graph coloring definitions |
| **Forum activity** | Limited. The Martinsson-Steiner result is recent (2025) and not yet targeted for formalization. |

---

## Candidate #6: Problem 533 — Graph theory counterexample

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/533 |
| **Statement** | Exact statement not retrievable (site returns 403). Based on database: a graph theory problem disproved on 27 Jan 2026. GPT-5.2 Pro attempted a proof but made a **subtle error** — the corrected disproof was completed by humans. |
| **Tier** | **B** (recently solved, GPT attempted, pipeline could replicate/fix) |
| **.lean file** | Status uncertain — .lean statement may exist given the formalization drive in early 2026. |
| **Status** | Disproved (27 Jan 2026). Not formalized in Lean. |
| **Why good target** | This is a **Tier B paradigm case**: GPT-5.2 Pro generated a candidate proof with a subtle error. Your pipeline is designed to catch exactly these errors — Aristotle formalizes the candidate, and the Lean type checker catches the subtle mistake, allowing iteration. Counterexample disproofs in graph theory generally use `SimpleGraph` and `Finset`, which are your strengths. The fact that GPT already came close means the pipeline has a plausible attack vector. |
| **Difficulty** | **5/10** (estimated; GPT nearly solved it) |
| **Mathlib deps** | `SimpleGraph`, `Finset`, likely `Fintype`, `decide` for finite graph verification |
| **Forum activity** | 6 posts, last by Adenwalla (Feb 2026). No formalization effort visible. |

---

## Candidate #7: Problem 340 — Computational properties of greedy Sidon sequences

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/340 |
| **Statement** | Define the greedy Sidon sequence: start with {1}, and iteratively add the smallest integer that preserves the Sidon property (all pairwise sums distinct). This gives A = {1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, …}. (a) Is |A ∩ {1,…,N}| ≫ N^{1/2−ε} for all ε > 0? (b) Does A − A have positive lower density? (c) Does A − A contain 22? |
| **Tier** | **C** (open, moonshot — but sub-question (c) is computationally accessible) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/340.lean`, tagged `@[category research open, AMS 5]`, **176 lines**. Includes a computable `greedySidon` function with verified computation. Uses `IsSidon`, `Finset`. |
| **Status** | Open. Trivial lower bound |A ∩ {1,…,N}| ≫ N^{1/3} known. |
| **Why good target** | The .lean file already defines a **computable `greedySidon` function** — this is tailor-made for `norm_num`, `omega`, and `decide` tactics. Sub-question (c) ("Does A−A contain 22?") is a **finite computation** verifiable by exhaustive search. Even partial results on (b) could be attacked computationally. The Sidon set infrastructure (`IsSidon` predicate) is fully implemented in `ForMathlib/Combinatorics/Basic.lean`. This problem plays to every one of your team's strengths: Finset arithmetic, membership proofs, computational verification, concrete constructions. |
| **Difficulty** | **3/10** for sub-question (c); **8/10** for main conjecture (a) |
| **Mathlib deps** | `IsSidon`, `Finset`, `Finset.card`, `Nat`, `decide`, `norm_num`, `omega` |
| **Forum activity** | Minimal. Not under active attack. Related to Problems 155 and 329 (Sidon set family). |

---

## Candidate #8: Problem 913 — Integers with distinct prime exponents

| Field | Detail |
|-------|--------|
| **Link** | https://www.erdosproblems.com/913 |
| **Statement** | Write n(n+1) = p₁^{k₁} · p₂^{k₂} · … · pₘ^{kₘ}. Are there infinitely many n such that all exponents k₁, k₂, …, kₘ are **distinct**? A variant asks: are there infinitely many primes p such that 8p² − 1 is also prime? (If yes, this implies the main conjecture.) |
| **Tier** | **C** (open, moonshot) |
| **.lean file** | **Yes** — `FormalConjectures/ErdosProblems/913.lean`, tagged `@[category research open, AMS 11]`. Uses `Set.InjOn`, `.factorization`, `.primeFactors`, `Nat.Prime`, `Set.Infinite`. Reviewed by b-mehta (2025-05-27). |
| **Status** | Open. |
| **Why good target** | The Lean formalization uses **exactly your team's core infrastructure**: `Nat.Prime`, `Nat.factorization`, `primeFactors`, `Set.InjOn` — all well-established in Mathlib. The problem has a beautiful structure where the variant (8p²−1 prime) is **computationally checkable** for specific instances. A partial result showing the implication (variant → main conjecture) is already in the .lean file and could be formalized. The n(n+1) factorization structure involves `norm_num`-amenable computations. Even producing verified computational evidence (e.g., "all n < 10⁸ satisfying the condition") would be a meaningful contribution. |
| **Difficulty** | **4/10** for the implication theorem; **9/10** for the infinitude statement |
| **Mathlib deps** | `Nat.Prime`, `Nat.factorization`, `Nat.primeFactors`, `Set.InjOn`, `Set.Infinite`, `norm_num`, `omega` |
| **Forum activity** | Minimal. No formalization effort visible. |

---

## The priority matrix

The following table ranks all eight candidates by the combined signal of feasibility, pipeline fit, and strategic value:

| Rank | Problem | Tier | Difficulty | Pipeline fit | Key advantage |
|------|---------|------|------------|-------------|---------------|
| 1 | **868** | A | 4/10 | ★★★★★ | Counterexample construction — your exact specialty |
| 2 | **899** | A | 5/10 | ★★★★☆ | Clean 51-line statement, pure Finset arithmetic |
| 3 | **340 (sub-q c)** | C | 3/10 | ★★★★★ | Computable greedySidon + decide/norm_num |
| 4 | **245** | A | 5/10 | ★★★★☆ | Batch-formalizable with 899 (same scaffolding) |
| 5 | **533** | B | 5/10 | ★★★★☆ | GPT already attempted — pipeline fixes the gap |
| 6 | **123 (3,5,7)** | A | 6/10 | ★★★☆☆ | Concrete base case, induction + Finset sums |
| 7 | **913 (implication)** | C | 4/10 | ★★★★☆ | Factorization infrastructure perfectly matched |
| 8 | **944 (large k)** | A | 6/10 | ★★★☆☆ | Graph coloring target area, recent construction |

## How the pipeline maps to each phase

The Claude → GPT → Codex → Aristotle → Axle pipeline maps naturally onto the Alexeev workflow that has proven successful on 10+ problems. For each candidate above, the flow would be:

**Claude (orchestration)** selects the problem, retrieves the Formal Conjectures `.lean` file, and identifies the `sorry` targets. **GPT (proof strategy)** reads the published proof (or generates a candidate for Tier C problems) and produces a structured informal proof in LaTeX, broken into lemma-level steps. **Codex (Lean code)** translates each lemma into Lean 4 skeleton code with `sorry` placeholders, importing the Formal Conjectures statement directly. **Aristotle (formalization)** fills the `sorry` holes using its Monte Carlo Graph Search and 200B+ parameter transformer, connecting to Mathlib tactics. **Axle (verification)** runs the final Lean type check and confirms the proof is complete.

For your team's strongest problems (868, 340 sub-question c, 899), this pipeline should complete in **under 24 hours** based on Alexeev's reported timings: ChatGPT ~13 minutes, Aristotle ~1–19 hours, Lean verification ~1–11 minutes.

## What to avoid and what to watch

Three misformalization traps documented in the community deserve attention. Problem 480 (sequences in [0,1]) had `m ≠ 0` instead of `n ≠ 0` — Aristotle exploited this for a trivial "proof." Problem 124 was solved for Erdős's stated (weaker) version, not the intended conjecture. Problem 707 had an `n = 0` edge case issue. **Always manually verify the Formal Conjectures statement against erdosproblems.com before running the pipeline.**

Forum threads to monitor: Problem 868 has Terence Tao commenting (8 posts), though no formalization is underway. Problem 340 relates to an active Sidon set research cluster (Problems 44, 155, 329). Problem 1038 (not in our list) is explicitly flagged as "in progress" by Tao and natso38 — avoid it entirely. The AI Contributions wiki at `github.com/teorth/erdosproblems/wiki/AI` is updated regularly and should be checked before committing to any target to avoid duplication with Alexeev's ongoing systematic sweeps.