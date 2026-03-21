# Erdős Problems — Formalization Targets for Mahmoud
## Solved problems with NO Lean formalization, in pure math areas
### Last updated: March 17, 2026

---

## TIER 1: Recently solved, self-contained proofs, strong pipeline fit

### Problem 397 — Central binomial coefficient products (DISPROVED, Lean proof exists but related problems don't)
- **Statement:** Are there only finitely many solutions to ∏ C(2mᵢ,mᵢ) = ∏ C(2nⱼ,nⱼ) with distinct mᵢ,nⱼ?
- **Answer:** No — infinite family: for any a≥2, c=8a²+8a+1 gives an identity.
- **Tags:** Number theory, combinatorics
- **Why it fits:** Pure algebra. The parametric identity is clean and verifiable. Somani found it with ChatGPT, Aristotle formalized. But related problems (additional families by SharkyKesa, Tao's entropy argument) are NOT formalized.
- **Your angle:** Formalize the extended families and Tao's entropy-based proof of infinitely many solutions.

### Problem 205 — Goldbach-type with 2^k + p (DISPROVED, NO formalization)
- **Statement:** Is it true that for almost all n, n-2^k has a bounded number of prime factors for some k?
- **Answer:** No — infinitely many n where all n-2^k have ≫ (log n/log log n)^{1/2} prime factors.
- **Tags:** Number theory, primes
- **Why it fits:** Uses CRT (Chinese Remainder Theorem) + weak PNT. Tao described the proof as "natural in retrospect." The construction is explicit and algebraic.
- **Difficulty:** Medium — CRT is within your bridge, but PNT formalization in Mathlib may need axiomatization.

### Problem 315 — Sylvester-Fibonacci sequence (PROVED, NO formalization)
- **Statement:** About the Sylvester sequence and its properties.
- **Answer:** Proved independently by Kamio and Li-Tang (2025).
- **Tags:** Number theory, sequences
- **Why it fits:** Clean number theory, likely self-contained proof.
- **Status:** "No (Create a formalisation here)" — wide open for you.

### Problem 1026 — Weighted Erdős-Szekeres (PROVED, proof formalized by Aristotle but statement NOT in Formal Conjectures)
- **Statement:** Weighted form of Erdős-Szekeres theorem — monotonic subsequences with large sum.
- **Answer:** c = 1, proved by Tidor-Wang-Yang and independently by Chan + Aristotle.
- **Tags:** Combinatorics, sequences
- **Why it fits:** Pure combinatorics. The Erdős-Szekeres theorem is beautiful and at your level conceptually. The weighted version adds algebraic flavor.
- **Your angle:** The statement isn't in Formal Conjectures yet — you could add both statement and proof.

### Problem 333 — Additive bases and density (DISPROVED, NO formalization)
- **Statement:** If A has density 0, must there exist B with |B∩[0,N]| = o(√N) and A ⊆ B+B?
- **Answer:** No — constructive proof using dyadic blocks.
- **Tags:** Additive combinatorics
- **Why it fits:** The proof sketch is clean: construct A as union of blocks on dyadic intervals, then counting argument. GPT-5.2 gave the argument, Claude Opus 4.5 helped formalize, but it's NOT in Lean on erdosproblems.com yet.
- **Your angle:** This is literally your pipeline — take the informal proof, feed to Aristotle Agent, formalize.

---

## TIER 2: Classic results with clean proofs, higher formalization value

### Problem 28 — Explicit Sidon-type additive basis (PROVED, NO formalization, $100 prize was attached)
- **Statement:** Explicit construction of A ⊆ ℕ with A+A = ℕ but representation function growing slowly.
- **Answer:** Constructive proof by Jain-Pham-Sawhney-Zakharov (2024).
- **Tags:** Number theory, additive combinatorics, Sidon sets
- **Why it fits:** This is a constructive existence proof — exactly the kind of thing that formalizes well. The paper is recent (2024) and likely self-contained.
- **Difficulty:** The paper may be long; worth checking if the core construction is extractable.

### Problem 73 — Square-free products (DISPROVED, NO formalization)
- **Statement:** Is F₅(N) = (1-o(1))N, where F_k(N) = largest A ⊆ {1,...,N} with no k-element subset having square product?
- **Answer:** No.
- **Tags:** Number theory, multiplicative number theory
- **Why it fits:** Multiplicative structure + counting arguments. Pure number theory.

### Problem 762 — Chromatic number vs fold cover number (DISPROVED, NO formalization)
- **Statement:** Is χ(G) ≤ ζ(G) + 1 for triangle-free graphs?
- **Answer:** No — Steiner constructed G with ω=4, ζ=4, χ=7.
- **Tags:** Graph theory
- **Why it fits:** Explicit counterexample construction. If the graph is small enough, this is directly verifiable in Lean.
- **Your angle:** Counterexample verifications are Aristotle's sweet spot.

### Problem 281 — Logarithmic density of covered integers (PROVED, NO formalization)
- **Statement:** About logarithmic density of integers covered by congruence systems.
- **Answer:** Proved — turns out to follow from a 1936 paper by Davenport and Erdős himself!
- **Tags:** Number theory, covering systems
- **Why it fits:** The proof uses Rogers' theorem + classical results. Tao did extensive discussion on the forum. The mathematical content is number theory + measure theory.
- **Irony factor:** Erdős posed a problem in 1980 that he had essentially co-solved in 1936. Formalizing this would be historically interesting.

---

## TIER 3: Deeper results, worth monitoring for when proofs appear

### Problem 1148 — Bounded representations by x²+y²-z² (PROVED March 16, 2026 — you're already on this!)
- **Status:** Aristotle Agent running on your skeleton right now.

### Problem 885 — Close divisors (OPEN — your bridge target)
- **Status:** No proof exists yet. If someone solves it, be ready to formalize.

### Problem 347 — Subset sums with ratio limit 2 (PROVED Jan 2026, formalized in Lean)
- **Status:** Already done by Barschkis. But the proof technique may have applications to nearby problems.

---

## HOW TO PICK YOUR NEXT TARGET

1. **Check the problem page** — look for "No (Create a formalisation here)"
2. **Read the proof** — is it self-contained? Does it use techniques you understand or are learning?
3. **Check the forum** — has anyone posted an informal proof sketch? Those are gold for your pipeline.
4. **Estimate Mathlib coverage** — does the proof need facts that are in Mathlib? Or will you need to axiomatize?
5. **Run Aristotle Agent** — submit the skeleton, see what it fills.

## THE META-STRATEGY

You're not competing with Boris Alexeev (who has a PhD and an automated pipeline) on volume. You're competing on:
- **Speed on fresh proofs** (like 1148 — paper dropped yesterday, you're formalizing today)
- **Quality of mathematical understanding** (your forum posts show you understand the math, not just the code)
- **The narrative** (13-year-old using AI-augmented pipeline to formalize research mathematics)

The ideal cadence: one formalization every 1-2 weeks, each one deepening your understanding of a different area of mathematics.
