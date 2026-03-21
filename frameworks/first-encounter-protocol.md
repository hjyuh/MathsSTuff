# FIRST ENCOUNTER PROTOCOL (FEP)

**Version:** 1.0  
**Created:** March 6, 2026  
**Author:** Mahmoud  
**Purpose:** A systematic approach for competition math problems you've never seen before. Designed to replace floundering with structured decomposition.

**Design principle:** See a worked example → replicate on a similar problem → extrapolate to harder versions. No Socratic guessing games. No withholding. The example IS the teaching.

---

## The Core Idea

When you hit a problem you've never seen before, the failure mode is almost always the same: you jump to a technique name ("use Vieta's," "try substitution") before understanding what the problem is actually asking you to compute. The First Encounter Protocol forces you to decompose the problem from what it literally says, check whether the obvious approach is viable, and find the structural shortcut — all before choosing a technique.

**The principle:** The method should feel forced by the end, not guessed at the start.

---

## The Protocol (7 Steps + Abort Signals)

### Step 1: State the Target

Write down exactly what you need to find. Not "solve the equation" but the specific quantity or object.

Bad: "Solve 3z² - 5z + 8 = 0"  
Good: "Find r₁² + r₂² where r₁, r₂ are roots of 3z² - 5z + 8 = 0"

Bad: "Find a quadratic"  
Good: "Find a quadratic whose roots are 1/p and 1/q, where p, q are roots of x² + 2x + 2 = 0"

**Why this matters:** Many problems hide the real target inside their phrasing. Restating it in bare mathematical terms often reveals the structure immediately.

### Step 2: Name the Brute Force

What's the most direct, obvious method? Name it honestly, even if you suspect it's bad.

- "Use the quadratic formula to find the roots, then compute the expression"
- "Expand everything and simplify"  
- "Try every case"
- "Plug in and compute"

Don't judge it yet. Just name it.

### Step 3: Friction Check

Before committing to brute force, do a 30-second viability check:

- Is the discriminant ugly (negative, non-square)?
- Will the algebra produce nested fractions or radicals?
- Are there more than 4-5 cases to check?
- Does the computation feel disproportionate to the problem's length?

**If the friction is low:** Just do it. Brute force on a clean problem is fine.

**If the friction is high:** STOP. Don't start the ugly computation. Proceed to Step 4.

### Step 4: Property Check

Ask: "Does this problem ask me to find the objects themselves, or a PROPERTY of the objects?"

- Find the roots → objects (brute force may be necessary)
- Find the SUM OF SQUARES of the roots → property (shortcut likely exists)
- Find the roots → objects
- Find a NEW EQUATION whose roots are transformations of old roots → property

**If it's a property, there's almost always a path that avoids finding the objects.**

### Step 5: Classify the Target

What kind of expression or object is the target?

| Target type | What to look for |
|------------|-----------------|
| Symmetric in roots (r₁² + r₂², r₁³ + r₂³) | Vieta's + algebraic identities |
| Ratio of root expressions (1/r₁ + 1/r₂) | Combine fractions, express via sum and product |
| New equation from transformed roots | Build new sum and product from old sum and product |
| Maximum or minimum | AM-GM, completing the square, or derivatives |
| Integer solutions | Divisibility, modular arithmetic, factoring |
| Count with constraints | Complementary counting, casework, generating functions |
| Existence or impossibility | Discriminant sign, parity argument, modular obstruction |
| One root given, find the other | Vieta's gives the other root directly |
| Relationship between roots | Substitute the relationship into Vieta's equations |

You won't know all of these yet. The table grows as you learn. The important thing is asking "what TYPE of target is this?" before "what technique do I use?"

### Step 6: What's Free?

What information is available WITHOUT full computation?

For polynomials:
- Sum of roots = -b/a
- Product of roots = c/a
- Discriminant sign tells you real vs complex
- Parity of coefficients constrains root properties

For equations in general:
- Symmetry reduces the problem
- Modular arithmetic gives constraints
- Bounds limit the search space
- Factorization reveals structure

### Step 7: Rebuild and Solve

Can you rewrite the target using the free information?

Find the algebraic identity that connects the target to what you know. At this point, the technique should feel forced — you're not guessing, you're assembling.

**Only now name the technique.** "This is Vieta's" or "this is discriminant analysis" comes AFTER you've identified why it's the right tool, not before.

---

## Abort Signals

**Stop your current approach and restart from Step 4 if:**

- Algebra gets ugly within 3-4 lines
- Problem asks for a property but you're computing objects
- Answer "should" be clean but you're producing nested fractions
- The problem is 2 lines but your solution is filling a page
- You're using techniques from multiple chapters when the problem is from one chapter
- You've been computing for 5+ minutes on what should be a 2-minute problem

---

## Step 8: After Solving — Generalize

Once you have the answer, ask:

**"What family of problems does this technique cover?"**

One solved problem should unlock an entire family. Write:

- The trigger: "When I see [feature], the move is [technique]"
- The family: "This also works for [variation 1], [variation 2], [variation 3]"
- The identity: the specific algebraic identity you used, stated generally

---

## Worked Example 1: Sum of Squares of Roots

### The Problem
Find the sum of the squares of the solutions of 3z² - 5z + 8 = 0.

### Running the Protocol

**Step 1 — Target:** Find r₁² + r₂² where r₁, r₂ are roots of 3z² - 5z + 8 = 0.

**Step 2 — Brute force:** Quadratic formula → find r₁ and r₂ → square each → add.

**Step 3 — Friction check:** Discriminant = 25 - 96 = -71. Negative. Roots are complex with √71 in them. Squaring those and adding is a nightmare. STOP.

**Step 4 — Property check:** The problem asks for r₁² + r₂², a property of the roots, not the roots themselves. Shortcut likely exists.

**Step 5 — Classify:** r₁² + r₂² is symmetric in the roots (swapping r₁ and r₂ doesn't change it). → Vieta's + algebraic identity.

**Step 6 — What's free?** From Vieta's: r₁ + r₂ = 5/3, r₁r₂ = 8/3.

**Step 7 — Rebuild:** I need to express r₁² + r₂² using r₁ + r₂ and r₁r₂. The identity:

r₁² + r₂² = (r₁ + r₂)² - 2r₁r₂

Plug in: (5/3)² - 2(8/3) = 25/9 - 48/9 = **-23/9**

**Step 8 — Generalize:**

Trigger: "When a problem asks for a symmetric expression of roots and the roots are ugly, express the target using sum and product via algebraic identities."

Family this also covers:
- r₁² + r₂² = (r₁ + r₂)² - 2r₁r₂
- r₁³ + r₂³ = (r₁ + r₂)³ - 3r₁r₂(r₁ + r₂)
- 1/r₁ + 1/r₂ = (r₁ + r₂)/(r₁r₂)
- (r₁ - r₂)² = (r₁ + r₂)² - 4r₁r₂
- r₁²r₂ + r₁r₂² = r₁r₂(r₁ + r₂)

---

## Worked Example 2: Building a New Equation from Transformed Roots

### The Problem
The solutions of x² + 2x + 2 = 0 are x = p and x = q. Find a quadratic equation with solutions y = 1/p and y = 1/q.

### Running the Protocol

**Step 1 — Target:** Find a quadratic whose roots are 1/p and 1/q.

**Step 2 — Brute force:** Quadratic formula → find p and q → compute 1/p and 1/q → build equation from those values.

**Step 3 — Friction check:** Discriminant = 4 - 8 = -4. Negative. Roots are -1 ± i. Computing 1/(-1+i) requires rationalizing complex denominators. Ugly. STOP.

**Step 4 — Property check:** The problem doesn't ask me to find 1/p and 1/q. It asks for an EQUATION that has them as roots. That's a property — I need the equation, not the roots.

**Step 5 — Classify:** I need to build a quadratic from its roots. A quadratic with roots r and s is:

y² - (r + s)y + rs = 0

So I need: (1/p + 1/q) and (1/p)(1/q).

**Step 6 — What's free?** From Vieta's on the original: p + q = -2, pq = 2.

**Step 7 — Rebuild:**

Sum of new roots: 1/p + 1/q = (p + q)/(pq) = -2/2 = -1

Product of new roots: (1/p)(1/q) = 1/(pq) = 1/2

New equation: y² - (-1)y + 1/2 = 0 → y² + y + 1/2 = 0

Multiply by 2 to clear fractions: **2y² + 2y + 1 = 0**

**Step 8 — Generalize:**

Trigger: "When a problem asks for a new equation whose roots are transformations of old roots, don't find the old roots. Express the new sum and product in terms of the old sum and product."

Family this also covers:
- Roots are reciprocals (1/p, 1/q): new sum = (p+q)/(pq), new product = 1/(pq)
- Roots are squares (p², q²): new sum = (p+q)² - 2pq, new product = (pq)²
- Roots are shifted (p+k, q+k): new sum = (p+q) + 2k, new product = pq + k(p+q) + k²
- Roots are negatives (-p, -q): new sum = -(p+q), new product = pq
- Roots are scaled (kp, kq): new sum = k(p+q), new product = k²(pq)

---

## Worked Example 3: Discriminant as Decision Tool

### The Problem
Find the positive value of h such that the sum of the squares of the roots of x² + 2hx - 3 = 0 is 10.

### Running the Protocol

**Step 1 — Target:** Find h > 0 such that r₁² + r₂² = 10.

**Step 2 — Brute force:** Solve x² + 2hx - 3 = 0 in terms of h, square both roots, set sum equal to 10, solve for h.

**Step 3 — Friction check:** The roots involve h as a parameter inside a square root. Squaring those expressions will be messy. STOP.

**Step 4 — Property check:** The problem asks for a property (sum of squares = 10), not the roots themselves.

**Step 5 — Classify:** r₁² + r₂² is symmetric. Same type as Example 1.

**Step 6 — What's free?** From Vieta's: r₁ + r₂ = -2h, r₁r₂ = -3.

**Step 7 — Rebuild:**

r₁² + r₂² = (r₁ + r₂)² - 2r₁r₂ = (-2h)² - 2(-3) = 4h² + 6

Set equal to 10: 4h² + 6 = 10 → 4h² = 4 → h² = 1 → h = ±1

Positive value: **h = 1**

**Step 8 — Generalize:**

Trigger: "When a problem has a parameter in the equation and asks for a root property equal to a value, use Vieta's to express the property in terms of the parameter, then solve the resulting equation."

This combines two moves: Vieta's identity (Example 1) + parameter equation (new).

---

## How to Use This Document

### When studying a new AoPS section:

1. Read the section
2. Try the challenge problems using the protocol
3. After each problem, write the Step 8 generalization
4. Your trigger log grows with every problem

### When you encounter an unfamiliar problem:

1. Run Steps 1-3 before doing ANY computation
2. If friction is high, Steps 4-7 will find the shortcut
3. If friction is low, just compute — not every problem needs a shortcut
4. After solving, always do Step 8

### When you're stuck:

1. Check which step you're stuck on
2. If stuck on Step 1 → re-read the problem more literally
3. If stuck on Step 5 → check the classification table, or try small cases
4. If stuck on Step 7 → look for algebraic identities that connect known quantities to the target
5. If stuck everywhere → the problem may require a technique you haven't learned yet. Flag it and move on.

### When teaching yourself:

The ideal flow:
1. See ONE worked example (like the three above)
2. Replicate on a similar problem with no help
3. Extrapolate to a harder variation
4. Write the trigger sentence and family

**Do NOT Socratic-method yourself into the technique.** See the example, replicate it, own it. Speed comes from pattern recognition, not from rediscovering the wheel every time.

---

## The Abort Signal Cheat Sheet

| Signal | What it means | What to do |
|--------|-------------|-----------|
| Discriminant is ugly | Roots are messy | Look for a property-based shortcut |
| More than 5 cases | Casework will explode | Look for a symmetry or counting shortcut |
| Algebra filling the page | You're computing, not solving | Step back to Step 4 |
| Using 3+ techniques | Problem probably needs 1 | You're on the wrong path |
| Answer should be clean but isn't | Computation error or wrong method | Restart from Step 4 |
| 5+ minutes on a 2-line problem | Approach mismatch | Protocol from the top |

---

## Growing the Classification Table

As you progress through AoPS and competition math, add rows to the Step 5 table:

**From Intro to Algebra:**
- Symmetric root expressions → Vieta's + identities
- New equations from transformed roots → new Vieta's from old Vieta's
- Discriminant conditions → discriminant = 0 (one root), < 0 (complex), > 0 (two real)

**From Counting & Probability (upcoming):**
- "How many ways" with constraints → complementary counting
- "At least one" → total minus "none"
- Probability of union → inclusion-exclusion

**From Number Theory (upcoming):**
- "Find all integers" → divisibility + bounding
- "Remainder when divided by" → modular arithmetic
- "Prove divisibility" → factor or use mod

**From Geometry (upcoming):**
- "Find the area" with complex shapes → decompose or subtract
- "Prove parallel/perpendicular" → slopes or angle chasing
- "Find the length" in circles → power of a point

Each new chapter adds entries. The table becomes your personal opening book for first encounters.

---

## Connection to Other Systems

**To the teaching prompt:** The FEP replaces the Socratic back-and-forth for new problem types. See the example, replicate, extrapolate. The teaching prompt's layering system (Layers 0-4) kicks in AFTER the FEP has identified the technique — layering shows you the same technique in progressively harder costumes.

**To the Forge:** When Step 8 identifies a technique family, that family becomes a Forge candidate. The FEP discovers techniques; the Forge deepens them.

**To the OOB:** Step 5 classifications become OOB entries. The FEP builds the opening book one first encounter at a time.

**To Chain Training:** When a problem requires Steps 4-7 to be run twice (two technique layers), that's a chain. The FEP handles single techniques; Chain Training handles combinations.

**To the LDP:** The FEP is the competition-level version of what the LDP does at research level. Same principle — decompose before committing to a method. Different scale.

---

*Companion to the Family Forge, Chain Training, Speed Forge, OOB, PCM, LDP, and Parallel Problem Protocol.*  
*See MASTER.md for the complete training architecture.*  
*Last updated: March 6, 2026*
