# VERTICAL PAIRS
## Research-First Downshift Training

**Author:** Mahmoud  
**Version:** 1.0  
**Created:** March 18, 2026  
**Core Idea:** Pair a solved Erdős problem with a competition problem sharing the same core technique. Do the Erdős problem first. The competition problem becomes the easy version of what you already understand.

---

## The Format

### Step 1: The Research Problem (90-120 min)

Take a **solved** Erdős problem. Your job is NOT to solve it from scratch — it's already solved. Your job is to:

1. **Read the solution** carefully — every line, every trick
2. **Identify the core technique** and classify by taxonomy (Type 1-8)
3. **Identify the composition type** (Solo/Chain/Interleave/Fuse)
4. **Reconstruct the proof from memory** after reading — close the paper, write the key ideas
5. **Write the abstract shape** in one sentence: "This proof works by ___"

This is miles harder than it sounds. Understanding a research proof well enough to reconstruct it requires genuine depth — you have to understand WHY each step exists, not just WHAT each step does. This is fuse-level cognitive load even for "simple" Erdős solutions.

### Step 2: The Bridge (5 min)

Before touching the competition problem, write one sentence:

> "The technique in Erdős #___ was [abstract shape]. A competition version would be: [prediction of what simpler version looks like]."

This forces the transfer to be conscious, not accidental.

### Step 3: The Competition Problem (15-30 min, timed)

Solve a competition problem (AIME/USAJMO/USAMO) that uses the **same core technique** in a simpler costume. Time yourself.

**What should happen:** The competition problem feels like a restricted special case of what you just understood. The technique is immediately visible because you just spent 90 minutes seeing it naked at research depth. The costume can't fool you.

### Step 4: The Log (5 min)

Write:
- Did the research understanding help? (yes/no/partially)
- What specifically transferred? (technique recognition? proof structure? a specific trick?)
- What was the composition level drop? (e.g., Fuse → Chain, Interleave → Solo)
- Time to first productive move on competition problem: ___
- Subjective difficulty rating of competition problem: ___/10

---

## Example Pairs

### Pair 1: CRT (Chinese Remainder Theorem) Constructions

**Erdős Problem #205** (Barreto-Leeham + ChatGPT/Aristotle, 2026)
- **Statement:** Are there infinitely many n that CANNOT be written as 2^k + m where Ω(m) < log log m?
- **Solution:** YES — use CRT to construct n ≡ 0 (mod 2^E) for large E. This handles all k > E. For remaining k ≤ E (only ~log n values), use CRT to force each n - 2^k to have many prime factors by making n ≡ 2^k (mod p₁p₂...pⱼ) for appropriate primes.
- **Core technique:** CRT as a construction tool — simultaneously controlling residues mod many primes to force arithmetic properties
- **Taxonomy:** Type 2 (Parametric Family) — the construction is parameterized
- **Composition:** Chain (CRT setup → counting argument → assembly)
- **Abstract shape:** "Use CRT to place n in a specific position relative to multiple moduli simultaneously, forcing a global property from local constraints."

**Competition Partner: AIME 2019 P9** (or similar)
- Problems where you need to find n satisfying multiple congruence conditions simultaneously
- The CRT is the same tool, but used in a solo/chain context rather than the fuse-level construction of #205
- Example type: "Find the least positive integer n such that n ≡ 3 (mod 7), n ≡ 5 (mod 11), n ≡ 2 (mod 13)"

**Why this pair works:** In #205, CRT is a weapon — you're wielding it creatively to build a counterexample. In the AIME problem, CRT is a calculation — you're applying it mechanically. After understanding CRT as a weapon, applying it as a calculation feels trivial. You're not just "using CRT" — you understand its power, its degrees of freedom, what it CAN and CAN'T do.

---

### Pair 2: Pigeonhole + Divisor Arguments

**Erdős Problem #848** (Sawhney, asymptotic; Mahmoud, computational verification N ≤ 10^7)
- **Statement:** For any k, show that for large enough n, n can be written as a product of k distinct integers all lying in (n^{1/k} - n^{1/k - ε}, n^{1/k} + n^{1/k - ε}) for some ε > 0.
- **Core technique:** Divisor distribution — understanding how divisors of n cluster near n^{1/k}
- **Taxonomy:** Type 7 (Bootstrap) + Type 1 (Reduction to divisor distribution)
- **Composition:** Interleave (divisor theory ↔ interval counting)
- **Abstract shape:** "Divisors of typical numbers cluster around powers; exploit this clustering for representation."

**Competition Partner: AIME problems on counting divisors / divisor properties**
- Example type: "How many positive integers n ≤ 1000 have exactly 12 divisors?"
- Or: "Find the number of ordered pairs (a,b) with a·b = 2^8 · 3^6 and a < b"
- The divisor-counting machinery is the same — you're reasoning about how divisors distribute — but at solo level

**Why this pair works:** After understanding how divisors distribute in the research context (clustering around n^{1/k}, the delicate balance between "typical" and "atypical" divisor structures), a competition problem asking you to count divisors is just the baby version. You understand the LANDSCAPE of divisors, not just the formula τ(n) = Π(aᵢ+1).

---

### Pair 3: Modular Arithmetic + Parity

**Erdős Problem #1148** (Chojecki, 2026 — the one you formalized)
- **Statement:** Every sufficiently large n can be written as x² + y² - z² with max(x²,y²,z²) ≤ n
- **Core technique:** Reduction to binary quadratic forms, parity correction (the key Lemma 3.1 you formalized), equidistribution via Duke-ELMV
- **Taxonomy:** Type 1 (Reduction) + Type 6 (Rigidity via equidistribution)
- **Composition:** Fuse (quadratic forms + ergodic theory + parity correction create a unified argument)
- **Abstract shape:** "Translate a representation problem to a lattice point problem, then use equidistribution to guarantee points exist in the right region."

**Competition Partner: USAJMO/AIME problems on quadratic representations**
- Example type: "In how many ways can 2025 be written as a² + b² where a,b are non-negative integers?"
- Or: "Prove that every prime of the form 4k+1 can be written as a sum of two squares"
- The quadratic representation machinery is the SAME FAMILY, but at solo/chain level

**Why this pair works:** After understanding that n = x² + y² - z² requires parity corrections across a hyperboloid and equidistribution of lattice points — after formalizing every step in Lean — a competition problem asking "how many ways can n = a² + b²" is almost laughably transparent. You UNDERSTAND representations at a level where the competition version is just one special case.

---

### Pair 4: Additive Combinatorics / Sidon Sets

**Erdős Problem #42** (classical; you formalized in Lean)
- **Statement:** A Sidon set in {1,...,N} has at most (1+o(1))√N elements
- **Core technique:** Double counting — count the number of pairwise sums, use distinctness, compare to the range
- **Taxonomy:** Type 7 (Bootstrap — the counting argument bootstraps a bound)
- **Composition:** Chain (set up counting → apply distinctness → extract bound)
- **Abstract shape:** "When all pairwise sums are distinct, the number of pairs bounds the set size via the available range."

**Competition Partner: AMC 12 / AIME problems on sets with distinct sums**
- Example type: "What is the maximum number of elements in a subset of {1,2,...,100} such that no two elements have the same sum?"
- Or: "Find the maximum size of a set S ⊆ {1,...,30} such that all pairwise sums are distinct"
- The double-counting argument is identical, just on a smaller scale

**Why this pair works:** The Lean formalization forced you to justify EVERY step of the double-counting argument. After that, recognizing "distinct pairwise sums → pigeonhole on the range" is automatic. The competition problem is literally the theorem you proved, applied to specific numbers.

---

### Pair 5: Density / Probabilistic Arguments

**Erdős Problem #205** (positive direction: Romanoff's theorem)
- **Statement:** A positive proportion of integers can be written as 2^k + p for prime p
- **Core technique:** Sieve/density argument — show the set of representable numbers has positive density by counting representations on average
- **Taxonomy:** Type 4 (Probabilistic) 
- **Composition:** Chain (set up average → bound from below → extract density)
- **Abstract shape:** "Count the average number of representations; if the average is positive, many numbers are represented."

**Competition Partner: AIME problems on counting representations**
- Example type: "How many positive integers n ≤ 1000 can be written as 2^a + 3^b for non-negative integers a,b?"
- The counting/representation machinery is the same — you're asking "how many n have a decomposition of form X?" — but at chain level

**Why this pair works:** After understanding the probabilistic/density heuristic at research depth (linearity of expectation, sieve bounds, density arguments), a competition problem that asks "how many n can be written as..." triggers the same mental framework. You immediately think about representations, counts, and density — even though the competition problem wants an exact answer, not an asymptotic.

---

## How to Find More Pairs

### Method 1: Start from the Erdős problem
1. Pick a solved Erdős problem you want to study
2. Classify its core technique
3. Search AoPS / Art of Problem Solving wiki for competition problems using that technique
4. Match by technique family (CRT, pigeonhole, quadratic forms, etc.)

### Method 2: Start from the competition problem
1. You encounter a competition problem that stumps you
2. Identify the technique you needed
3. Search erdosproblems.com for solved problems using the same technique at research depth
4. Study the research problem FIRST, then return to the competition problem

**Method 2 is especially powerful for problems you got wrong.** The reason you got it wrong is likely not that you don't know the technique — it's that you don't understand the technique deeply enough to recognize it through the costume. Studying the research version builds that depth.

### Method 3: Technique-first
1. Pick a technique from the taxonomy (e.g., "extremal principle")
2. Find the simplest solved Erdős problem using it
3. Find competition problems at each level: AMC → AIME → USAJMO → USAMO
4. Build a full vertical stack: research problem at top, competition problems layered below
5. Work top-down: research first, then descend through competition levels

This is a SPINE in Forge terminology, but organized by composition level rather than just difficulty.

---

## Scheduling

### Current Phase (Now → Summer 2026)
- **One Vertical Pair per week** (weekend session)
- Pick solved Erdős problems that use techniques you're learning in AoPS
- Pair with AMC 10/12 or easy AIME problems
- Total time: ~2.5 hours (90 min research + 30 min competition + 30 min log/reflection)

### Phase B (Fall 2026 → 2027)
- **Two Vertical Pairs per week**
- Pair with AIME P8-15 and USAJMO problems
- Start using Method 2 (competition misses trigger research study)

### Phase C (2027+)
- **Three pairs per week** + spontaneous pairing from research
- Pair with USAMO/IMO problems
- The pairs become bidirectional: research informs competition AND competition techniques feed research ideas

---

## Quality Markers

A vertical pair is working when:
- [ ] You can reconstruct the research proof's key ideas from memory
- [ ] Your bridge sentence accurately predicts what the competition version looks like
- [ ] Time to first productive move on competition problem is < 3 minutes
- [ ] You can articulate SPECIFICALLY what transferred (not just "it felt easier")
- [ ] The competition problem's composition level drop is clearly perceptible

A vertical pair is NOT working when:
- [ ] You read the research proof but can't reconstruct it
- [ ] The competition problem still feels hard despite the research work
- [ ] You can't articulate what transferred
- [ ] The two problems don't actually share a core technique (bad pairing)

If pairs consistently don't work, the technique vocabulary gap is too large — the research proof is so far above your current level that the bridge can't form. Solution: pick simpler Erdős problems or study the prerequisite techniques first.

---

## The Vision

Over time, your collection of vertical pairs builds a **technique atlas from two directions simultaneously**:
- From below (AoPS): what does each technique look like in its simplest form?
- From above (Erdős): what does each technique look like at full power?

When you encounter a competition problem, you're not matching it against "techniques I learned in a textbook." You're matching it against "techniques I've seen deployed at research depth." The costume can't fool you because you've seen the technique both naked AND in its most elaborate disguise. The competition costume is always somewhere in between — always recognizable.

That's the Tao effect, made deliberate and systematic.

---

*Companion to: Overtraining Protocol, Solution Architecture Taxonomy, Chain Training System*
*Last updated: March 18, 2026*
