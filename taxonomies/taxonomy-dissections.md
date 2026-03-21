# Solution Architecture Taxonomy — Dissection Guide
## What Each Architecture Type Actually Looks Like Inside
### Mahmoud — March 18, 2026

---

## Type 1: Reduction / Translation ⟿
### Dissection: Erdős #1148 (Chojecki, 2026)

**Problem:** Every sufficiently large n can be written as x² + y² - z² with max(x²,y²,z²) ≤ n.

**The actual moves:**

**Move 1 — Identify what the problem is "secretly about."**
The problem says "represent n as x² + y² - z²." But Chojecki notices that if you set a = x+z, b = 2y, c = z-x, then x² + y² - z² = (b² - 4ac)/4. So the problem is secretly about finding (a,b,c) with b² - 4ac = 4n. That's a binary quadratic form of discriminant 4n.

> **This is the reduction.** One line of algebra transformed a ternary representation problem into a binary quadratic form problem. The ternary problem is unknown. The binary problem has 200 years of theory behind it.

**Move 2 — Translate the boundedness condition.**
The constraint max(x²,y²,z²) ≤ n translates to: the point (a/2√n, b/2√n, c/2√n) lies in a specific bounded region K of the hyperboloid B² - 4AC = 1.

> **This is the dictionary being extended.** Not just the algebraic identity, but the geometric constraint also translates.

**Move 3 — Apply the known theorem in the new language.**
Duke-ELMV says: primitive binary quadratic forms of discriminant d become equidistributed on the hyperboloid as d → ∞. So for large enough d = 4n, some primitive form must land in K.

> **This is the payoff.** In the original language (find x,y,z), there's no tool. In the translated language (find a form in K), there's a 2012 theorem that hands you the answer.

**Move 4 — Translate back + clean up.**
The form might not satisfy the parity condition (b even, a ≡ c mod 2). Apply T or U operators to fix parity. These preserve the discriminant and keep the point in K. Then translate back to (x,y,z).

**What made this Type 1 and not something else:**
The problem was NOT hard because of deep technique. It was hard because nobody had seen the right dictionary. Once Chojecki wrote down a = x+z, b = 2y, c = z-x, the rest was assembling known pieces. The creative act was the translation.

**How to recognize this shape in new problems:**
Ask: "Does this problem involve a mathematical object that has a known representation in another domain?" If yes, write down the dictionary explicitly and see if the translated problem is already solved.

---

## Type 2: Parametric Family ∞
### Dissection: Erdős #397 (Somani + GPT-5.2, 2026)

**Problem:** Are there only finitely many solutions to ∏ C(2mᵢ,mᵢ) = ∏ C(2nⱼ,nⱼ) with distinct mᵢ, nⱼ?

**The actual moves:**

**Move 1 — Guess a parametric form.**
Instead of searching for random solutions, assume the simplest possible structure: three terms on each side. Try C(2a,a) · C(4a+4,2a+2) · C(2c,c) = C(2a+2,a+1) · C(4a,2a) · C(2c+2,c+1).

> **This is the key insight of Type 2:** don't search the solution space — parameterize it. Assume a specific algebraic form with one free variable and see if you can make it work.

**Move 2 — Express central binomial coefficients via factorials.**
C(2k,k) = (2k)!/(k!)². Write both sides in terms of factorials of a and c. Simplify.

**Move 3 — Find the constraint on c.**
After cancellation, the identity holds if and only if c satisfies a specific polynomial relation with a. Solving: c = 8a² + 8a + 1.

> **This is the construction.** One formula: for ANY a ≥ 2, set c = 8a² + 8a + 1, and the identity holds. That's infinitely many solutions, parameterized by a.

**Move 4 — Verify.**
Plug in a=2: c=49. Check that C(4,2)·C(12,6)·C(98,49) = C(6,3)·C(8,4)·C(100,50). It works.
Plug in a=3: c=97. Check. It works.
The identity is algebraic, so it works for all a.

**What made this Type 2 and not something else:**
The problem asked "finitely many?" — which is an invitation to construct an infinite family. The answer was NO, and the proof was exhibiting the family. No deep theory needed. Just the right algebraic identity.

**How to recognize this shape in new problems:**
Any problem asking "finitely many" or "for all" is a candidate for Type 2. The first move is always: assume a parameterized form and see if you can make it satisfy the conditions identically in the parameter.

---

## Type 3: Flow / Evolution ↻
### Dissection: Poincaré Conjecture (Perelman, 2003)

**Problem:** Every simply connected closed 3-manifold is homeomorphic to S³.

**The actual moves:**

**Move 1 — Define the flow.**
Take any Riemannian metric g on the manifold. Define the Ricci flow: ∂g/∂t = -2·Ric(g). This is a PDE that deforms the metric, making positively curved regions shrink and negatively curved regions expand. It's the geometric analogue of the heat equation — it smooths out the geometry.

> **This is the core of Type 3:** you don't attack the problem directly. You define a process that evolves the object toward the answer.

**Move 2 — Identify the obstacle.**
The Ricci flow can develop singularities — points where the curvature blows up in finite time. Hamilton (who invented the flow in 1982) couldn't get past this.

**Move 3 — Perelman's surgery.**
When a singularity forms, Perelman showed it always looks like a "neck" (roughly S² × ℝ). Cut the manifold along the neck, cap off the two ends with standard 3-balls, and restart the flow. This is "Ricci flow with surgery."

> **This is the technical breakthrough.** The flow was known. The surgery idea was known. Perelman's contribution was proving that: (a) singularities ALWAYS have the neck structure, (b) surgery can ALWAYS be performed, (c) the process terminates in finite time.

**Move 4 — Show convergence.**
After finitely many surgeries, the flow converges to a metric of constant curvature. By Thurston's geometrization, the only constant-curvature simply connected 3-manifold is S³.

**What made this Type 3:**
The proof doesn't construct S³ or find a homeomorphism directly. It defines a process (Ricci flow + surgery) and shows the process inevitably converges to the answer. The manifold "flows" into being a sphere.

**How to recognize in new problems:**
If the problem asks about properties of geometric objects, look for a natural evolution (flow, diffusion, deformation). The key question: is there a quantity that monotonically changes along the flow? For Ricci flow, it was Perelman's W-entropy.

---

## Type 4: Probabilistic Existence 🎲
### Dissection: Bounded Gaps Between Primes (Maynard, 2013)

**Problem:** There are infinitely many pairs of primes with bounded gap (originally: gap ≤ 70,000,000 by Zhang, improved to ≤ 246 by Polymath 8b).

**The actual moves:**

**Move 1 — Choose an admissible tuple.**
Pick k positions h₁, ..., hₖ that don't cover all residue classes mod any prime. For example, {0, 2, 6, 8, 12, ...} — these are positions where primes COULD simultaneously occur without violating divisibility constraints.

> **This is the setup.** You're not finding primes directly — you're setting up a framework where a random argument can force them to exist.

**Move 2 — Define sieve weights.**
For each n, define a weight w(n) = (Σ λ_d)² where the sum is over divisors d of ∏(n + hᵢ). The λ_d are optimized to be large when many of the n + hᵢ are prime.

**Move 3 — Compute the expected number of primes in the tuple.**
Using the sieve weights, compute:
S = Σₙ w(n) · (number of i with n + hᵢ prime)
versus
S₀ = Σₙ w(n)

If S/S₀ > m, then some n must have more than m of the n + hᵢ prime. In particular, if S/S₀ > 1, at least two primes appear in the tuple.

> **This is the probabilistic argument.** You're not finding the specific n. You're showing that the weighted average forces at least one n to work.

**Move 4 — Optimize the weights.**
Maynard's key insight: optimize the sieve weights as a multidimensional variational problem. The optimal weights are given by a specific eigenfunction of an integral operator. With k large enough, the ratio S/S₀ exceeds 1.

**Move 5 — Conclude.**
Since infinitely many n are prime candidates (by the prime number theorem), and the sieve argument shows some n in each large range must have two primes in the tuple, there are infinitely many bounded prime gaps.

**What made this Type 4:**
Nobody found a specific pair of close primes and proved they're prime. Instead, the proof shows that a weighted count over all candidates must be positive — so at least one candidate works. The specific primes are never identified.

**How to recognize:**
Problem asks for existence of an object satisfying many constraints. The key move: instead of finding the object, count (with weights) and show the count is positive.

---

## Type 5: Explicit Construction ✦
### Dissection: Erdős #707 (Hall, 1947 / rediscovered 2025)

**Problem:** Can every finite Sidon set be extended to a perfect difference set mod p²+p+1 for some prime p?

**The actual moves:**

**Move 1 — Understand what's being asked.**
A Sidon set has all pairwise differences distinct. A perfect difference set mod m is a set where every nonzero residue appears exactly once as a difference. The question: can you always complete a Sidon set to a perfect difference set?

**Move 2 — Find a counterexample.**
The set A = {1, 3, 9, 10, 13} is a Sidon set (check: all 20 pairwise differences are distinct).

**Move 3 — Verify it can't be extended.**
For A to extend to a perfect difference set mod p²+p+1, we need p²+p+1 ≥ 13 (to contain all elements). Check small primes:
- p=3: mod 13. Check if {1,3,9,10,13≡0} can extend to a perfect difference set of size 4 in Z/13Z. Exhaustive check: no.
- p=4: not prime.
- p=5: mod 31. Check all possible extensions of {1,3,9,10,13} to a 6-element set in Z/31Z. Exhaustive check: none work.
- Continue for all relevant p. None work.

> **This is the entire proof.** One specific set. Exhaustive verification. Done.

**The irony:** This counterexample was found by Marshall Hall Jr. in 1947. Erdős posed the problem in 1976. For almost 50 years, nobody noticed that the problem had already been solved 30 years before it was asked. It was rediscovered in 2025 by Alexeev and Mixon using AI-assisted search, who then found Hall's original paper.

**What made this Type 5:**
No theory needed. No clever argument. Just the right object plus verification. The difficulty was finding {1,3,9,10,13}, not proving anything about it.

**How to recognize:**
Problem says "for all X, property Y holds?" If you suspect the answer is no, search for small counterexamples systematically. Check known objects from adjacent areas.

---

## Type 6: Structural Rigidity ◆
### Dissection: Duke's Theorem via ELMV (2012)

**Problem:** Prove that closed geodesics of discriminant d become equidistributed on the modular surface as d → ∞.

**The actual moves:**

**Move 1 — Translate to measures.**
Each set of closed geodesics of discriminant d defines a probability measure μ_d on the modular surface. "Equidistribution" means μ_d → μ_Haar (the uniform measure) in the weak-* topology.

**Move 2 — Extract a convergent subsequence.**
By compactness of the space of probability measures (Prokhorov's theorem), every subsequence of {μ_d} has a further subsequence converging to some limit measure μ_∞. We need to show μ_∞ = μ_Haar.

**Move 3 — Show the limit has maximal entropy.**
Using the dynamics of the geodesic flow, ELMV show that μ_∞ must have entropy equal to 1 (the maximum). This uses Lindenstrauss's measure rigidity machinery — the key technical input.

> **This is the rigidity step.** Among all measures invariant under the geodesic flow on SL₂(Z)\SL₂(R), there is exactly ONE with maximal entropy: the Haar measure. So μ_∞ = μ_Haar. No other possibility.

**Move 4 — Conclude.**
Since every convergent subsequence has the same limit (Haar), the full sequence converges: μ_d → μ_Haar. That's equidistribution.

**What made this Type 6:**
The proof doesn't compute anything about the geodesics directly. It shows there's only one possible answer (Haar measure) by entropy maximization, so the answer MUST be that. The rigidity of the dynamical system does all the work.

**How to recognize:**
If the answer is expected to be unique or canonical, look for a classification result that constrains the possibilities. The strategy: show all possibilities are eliminated except one.

---

## Type 7: Induction / Bootstrap ⇑
### Dissection: Szemerédi's Theorem (1975)

**Problem:** Any set of integers with positive upper density contains arbitrarily long arithmetic progressions.

**The actual moves (Gowers's proof, which makes the bootstrap structure clearest):**

**Move 1 — State the dichotomy.**
For any set A of density α in {1,...,N}, exactly one of two things is true:
(a) A contains the expected number of k-term APs (it's "pseudorandom"), or
(b) A has increased density on some long arithmetic progression P ⊂ {1,...,N}.

> **This is the structure-vs-randomness dichotomy** — the engine of every bootstrap proof.

**Move 2 — If (a), we're done.** Pseudorandom sets contain APs by a counting argument.

**Move 3 — If (b), iterate.** A has density α' > α on some progression P of length N' ≥ N^c. Restrict to P and repeat the dichotomy.

**Move 4 — Show termination.** Each iteration increases the density: α < α' < α'' < ... But density can never exceed 1. So after at most 1/ε iterations, we must land in case (a).

> **This is the bootstrap.** You don't prove the theorem directly. You prove: either the theorem holds, or you've made measurable progress. Since progress is bounded, the theorem must eventually hold.

**What made this Type 7:**
The proof never directly shows "here is an AP in A." It shows that the FAILURE to find an AP implies a density increment, and density increments can only happen finitely many times.

**How to recognize:**
If a weak version of the result is known or easy, and there's a natural "progress measure" (density, energy, count), try showing that failure implies progress. The iteration then proves the full result.

---

## Type 8: Cross-Pollination ⚡
### Dissection: Cap Set Problem (Ellenberg-Gijswijt, 2016)

**Problem:** How large can a subset of F₃ⁿ be without containing a 3-term arithmetic progression?

**The actual moves:**

**Move 1 — The barrier.**
For decades, the best bounds came from Fourier analysis over F₃ⁿ. These methods could prove bounds like N/n^{1+ε} but not the conjectured exponential bound c^n for c < 3.

> **There was a provable barrier:** Fourier methods alone could not get exponential bounds. Everyone knew this. The problem was stuck.

**Move 2 — Croot, Lev, and Pach's breakthrough (in a different group).**
In early 2016, CLP proved an exponential bound for a DIFFERENT problem: cap sets in F₄ⁿ (not F₃ⁿ). Their method: the polynomial method from algebraic geometry/coding theory.

The key lemma: if p(x₁,...,xₙ) is a polynomial of low degree that vanishes on a large set S, then a related polynomial has low rank as a tensor → S must be small.

> **This is the cross-pollination.** The polynomial method was known in algebraic geometry and coding theory. Nobody had applied it to additive combinatorics cap sets. CLP imported it.

**Move 3 — Ellenberg and Gijswijt adapt to F₃ⁿ.**
Within weeks of CLP's paper, Ellenberg and Gijswijt adapted the method to F₃ⁿ. The adaptation required a different polynomial choice and a cleaner version of the rank argument, but the core idea was the same.

Result: any cap set in F₃ⁿ has size at most 2.756ⁿ. This was a massive improvement over all previous bounds.

**Move 4 — Consequences cascade.**
The exponential bound on cap sets immediately resolved the weak sunflower conjecture (for k=3), via a connection observed by Alon, Shpilka, and Umans years earlier. The bridge had been built in 2013. The missing piece was the cap set bound, which CLP/EG provided in 2016.

> **This is why cross-pollination is the hardest to predict:** the connecting piece (polynomial method) existed in a different field for years. The connection (cap sets ↔ tensor rank) was known. But nobody had put them together until CLP tried it.

**What made this Type 8:**
Every technique native to additive combinatorics had hit a barrier. The breakthrough required importing from algebraic geometry/coding theory. The "new climbing tool" was the polynomial method — old in its home field, revolutionary in its new application.

**How to recognize:**
If a problem has resisted all known approaches for decades and experts say "we need a new idea" — the new idea almost always comes from a different field. The question is: what other field has problems with the same abstract shape?

---

## The Meta-Pattern

Looking across all 8 dissections:

**Types 1-2** are about **seeing the problem correctly** (finding the right dictionary or the right parameterization). The math is usually not hard once you see it.

**Types 3-4** are about **designing the right process** (flow or random construction). The creativity is in the setup; the execution follows from known machinery.

**Types 5-6** are about **finding the right object** (counterexample or unique answer). Type 5 finds it by search; Type 6 proves it's the only possibility.

**Types 7-8** are about **building power iteratively** (bootstrapping from weakness or importing from other fields). These are the deepest and least predictable.

The difficulty gradient roughly follows this ordering: Type 5 (just find an object) is often easiest. Types 1-2 (find the right perspective) are medium. Types 3-4-6-7 (design a process or classify) are hard. Type 8 (import from another field) is hardest because you can't know in advance which field to look in.
