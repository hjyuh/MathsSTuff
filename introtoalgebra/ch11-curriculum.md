# Chapter 11: Special Factorizations — Complete Teaching Curriculum

**For:** Claude (teaching Mahmoud)
**Source:** AoPS Introduction to Algebra, Chapter 11 (aops11.pdf)
**Philosophy:** Strip the costume. One step at a time. Never solve before he attempts.
**Reference:** math-teaching-prompt.md for all teaching rules.

---

## Chapter Overview

Five factorization identities, each building on the last:

| Section | Identity | Core Idea |
|---------|----------|-----------|
| 11.1 | (a+b)^2 = a^2 + 2ab + b^2 | Recognizing perfect square trinomials |
| 11.2 | a^2 - b^2 = (a-b)(a+b) | Difference of squares |
| 11.3 | a^3 +/- b^3 = ... | Sum and difference of cubes |
| 11.4 | Rationalizing denominators | Applying 11.1-11.3 to eliminate radicals |
| 11.5 | ab + ay + bx + xy = (a+x)(b+y) | Simon's Favorite Factoring Trick |

**Estimated sessions:** 6-8 (one section per session, plus review)

**Mahmoud's current comfort:** Linear equations, systems, basic quadratics, Vieta's formulas, standard factoring. He has NOT yet seen special factorizations systematically.

---

## SESSION PLAN: Section 11.1 — Squares of Binomials

### Big Idea
(a + b)^2 = a^2 + 2ab + b^2. The "2ab" is the key — it's what separates a perfect square trinomial from a random quadratic.

### Pre-check (30 seconds)
Ask Mahmoud to expand (x + 3)^2 cold. If he gets x^2 + 6x + 9 immediately, he already has the expansion down and we focus on RECOGNITION (going backward). If he hesitates or writes x^2 + 9, he needs the expansion first.

### Problem Sequence

#### Phase 1: Build the Identity (Problems 11.1-11.2)

**Problem 11.1:** Expand (y+5)^2 and (3z+8)^2.
- Let him expand by FOIL or distribution
- After he gets results, ask: "What do the first term, last term, and middle term each relate to from the original binomial?"
- He should notice: first and last are squares, middle is 2 * product
- **Trigger sentence target:** "The middle term is always twice the product of the two parts."

**Problem 11.2:** Expand (x-6)^2 and (-2y+9)^2.
- Point: negatives don't break the pattern, they just flip the sign of the middle term
- If he gets confused by (-2y+9)^2, nudge: "What's a? What's b? Just plug into the formula you just found."
- **Watch for:** Writing (x-6)^2 = x^2 - 36 (forgetting the middle term). This is the #1 error.

**After Phase 1 checkpoint:** He should be able to state (a+b)^2 = a^2 + 2ab + b^2 from memory.

#### Phase 2: Recognition — Going Backward (Problem 11.3)

**Problem 11.3:** Is each expression a perfect square trinomial? Factor if yes.
- (a) x^2 - 6x + 9 → YES, (x-3)^2
- (b) y^2 + 14y + 25 → NO (14 != 2*y*5 = 10y? No, 2*1*5 = 10 ≠ 14)
- (c) z^2 - 8z - 16 → NO (constant is negative, can't be a perfect square)
- (d) x^2 + x + 1/4 → YES, (x + 1/2)^2
- (e) 16z^2 - 24z - 9 → NO (constant is negative)
- (f) 4y^2 - 28yz + 49z^2 → YES, (2y - 7z)^2

**Teaching notes:**
- The recognition checklist: (1) Are the first and last terms perfect squares? (2) Is the constant positive? (3) Does the middle term = 2 * sqrt(first) * sqrt(last)?
- Part (b) is the critical one — students often force-fit. Make sure he checks the middle term.
- Part (f) is the jump: two variables. Nudge: "What squares to give 4y^2? What squares to give 49z^2? Now check the middle."
- **Common mistake:** Forgetting that (2y - 7z)^2 = (-2y + 7z)^2. Both are valid.

**Trigger sentence target:** "To check if a quadratic is a perfect square, I check if the middle term equals twice the product of the square roots of the outer terms."

#### Phase 3: Application (Problems 11.4-11.6)

**Problem 11.4:** If x = sqrt(6/7), evaluate (x + 1/x)^2. (Source: Mandelbrot)
- This is the first "costume" problem. The costume is the radical.
- **If stuck:** "What if you expand (x + 1/x)^2 using the formula BEFORE plugging in x?"
- Key insight: (x + 1/x)^2 = x^2 + 2 + 1/x^2. The "2" is free — it comes from 2(x)(1/x) = 2.
- Then x^2 = 6/7 and 1/x^2 = 7/6, so the answer is 6/7 + 2 + 7/6 = (36 + 84 + 49)/42 = 169/42.
- **Watch for:** Him trying to compute sqrt(6/7) + sqrt(7/6) directly. If he does, let him struggle for a moment, then ask: "Is there a way to avoid the radicals entirely?"

**Problem 11.5:** Compute 20062005^2 - 2(20062005)(20062003) + 20062003^2.
- Three approaches in the book. Let him try whichever he wants.
- **If stuck:** "Those numbers are huge. What if you replaced them with small numbers like 5 and 3? What would you get?"
- Best approach: recognize it's (20062005 - 20062003)^2 = 2^2 = 4.
- **Trigger sentence target:** "When I see a^2 - 2ab + b^2 with giant numbers, I factor it as (a-b)^2 first."

**Problem 11.6:** Square 71, 65, 204, 99 in your head.
- Fun mental math. The technique: split into nearby round number + small number.
- 71 = 70+1, so 71^2 = 4900 + 140 + 1 = 5041
- 99 = 100-1, so 99^2 = 10000 - 200 + 1 = 9801
- Let him try each one. Don't rush. This builds confidence with the identity.

#### Phase 4: Extension — Pascal's Triangle (Problem 11.7)

**Problem 11.7:** Expand (x+y)^n for n = 3, 4, 5, 6.
- This is a preview, not a mastery requirement. He does NOT need to memorize Pascal's Triangle yet.
- Have him expand (x+y)^3 by multiplying (x+y)(x^2 + 2xy + y^2).
- After he gets (x+y)^3 and (x+y)^4, show him the coefficient triangle pattern.
- **Don't dwell here.** Point out the pattern exists, tell him it comes back in Intro to Counting & Probability.
- If he's excited, let him explore. If not, move on.

#### Phase 5: Exercises

**Assign these as practice (from the book):**
- 11.1.1: Expand (t-5)^2, (x+5)^3, (3y-7)^2, (3y+7)^2
- 11.1.2: Identify and factor perfect square trinomials (6 parts)
- 11.1.4: Compute 31^2 and 299^2 in your head
- 11.1.5: The "numbers ending in 5" squaring trick

**Skip unless he's hungry for more:**
- 11.1.3: Geometric proof of (a+b)^2 — nice but not essential now
- 11.1.6: The ARML problem — save for review

### Custom Layering Exercise: Recognizing (a+b)^2

After he finishes the section, if the recognition feels too easy, do this:

**Layer 0:** Factor x^2 + 10x + 25. (Naked — obvious perfect square)

**Layer 1:** Factor 4t^2 + 12t + 9. (Variable rename — coefficients hide the structure)

**Layer 2:** If a + b = 7 and ab = 10, find a^2 + b^2. (Must realize a^2 + b^2 = (a+b)^2 - 2ab)

**Layer 3:** Simplify sqrt(x^2 + 6x + 9) for all real x. (Must factor inside the radical, then handle absolute value)

**Layer 4:** Given that x^2 + 1/x^2 = 7, find x + 1/x. (Full costume — must work backward from the expansion)

### Section 11.1 Mastery Checklist
- [ ] Can expand (a+b)^2 and (a-b)^2 instantly
- [ ] Can identify whether a trinomial is a perfect square in under 10 seconds
- [ ] Can factor perfect square trinomials with coefficients (like 4y^2 - 28yz + 49z^2)
- [ ] Can use the identity to simplify expressions (like Problem 11.4)
- [ ] Can use the identity for mental arithmetic (squaring numbers near round numbers)
- [ ] Knows to look for the pattern when they see a^2 + 2ab + b^2 or a^2 - 2ab + b^2

---

## SESSION PLAN: Section 11.2 — Difference of Squares

### Big Idea
a^2 - b^2 = (a - b)(a + b). This is arguably the most important factorization in all of competition math.

### Connection to 11.1
"You just learned to recognize when something IS a perfect square. Now you'll learn what happens when you SUBTRACT two perfect squares."

### Problem Sequence

#### Phase 1: Discover the Identity (Problem 11.8)

**Problem 11.8:** Factor x^2 - 1, x^2 - 4, x^2 - 9, then x^2 - y^2.
- He should already know how to factor x^2 - 1 from Chapter 10 (basic quadratic factoring).
- The point is seeing the PATTERN: x^2 - y^2 = (x-y)(x+y).
- Have him verify by expanding (x-y)(x+y).
- **Trigger sentence target:** "Whenever I see a difference of two things that are both perfect squares, I factor."

#### Phase 2: Practice Factoring (Problem 11.9)

**Problem 11.9:** Factor r^2 - 400, 4t^2 - 121, 3r^2 - 147, z^4 - 1.
- (a) and (b) are straightforward
- (c) is the key teaching moment: factor out the 3 FIRST, then use difference of squares
- (d) is the other key moment: z^4 - 1 = (z^2)^2 - 1^2, then factor AGAIN because z^2 - 1 is also a difference of squares
- **Watch for:** Him stopping at (z^2-1)(z^2+1) and not factoring further.
- **Nudge for (d):** "Is z^2 - 1 itself a difference of squares?"
- **Common mistake on (c):** Trying to use difference of squares directly on 3r^2 - 147 without factoring out 3. The numbers aren't perfect squares until you factor.

#### Phase 3: Arithmetic Application (Problem 11.10)

**Problem 11.10:** Evaluate 5^2 - 4^2, 6^2 - 5^2, 7^2 - 6^2, 8^2 - 7^2.
- Results: 9, 11, 13, 15. Each is the sum of the two bases!
- He should prove it: (n+1)^2 - n^2 = (n+1-n)(n+1+n) = 2n+1 = (n+1) + n.
- **Trigger sentence target:** "The difference of consecutive squares is always their sum."
- This is useful for mental math: 121^2 = 120^2 + 120 + 121 = 14400 + 241 = 14641.

#### Phase 4: Diophantine Equations (Problem 11.11) — KEY PROBLEM

**Problem 11.11:** Find all positive integer pairs (m, n) with m^2 - n^2 = 105.
- This is the first time he'll see factoring used to solve a Diophantine equation. It's a BIG idea.
- **Step-by-step pacing:**
  1. "Write the equation." → m^2 = n^2 + 105, so m^2 - n^2 = 105
  2. "Can you factor the left side?" → (m-n)(m+n) = 105
  3. "m and n are positive integers, so m-n and m+n are both integers. What are the factor pairs of 105?"
  4. 105 = 1*105 = 3*35 = 5*21 = 7*15
  5. For each pair, solve the system: m-n = small, m+n = big
  6. Solutions: (53,52), (19,16), (13,8), (11,4)
- **Watch for:** Him not knowing how to go from factor pairs to (m,n). The system m-n=a, m+n=b gives m=(a+b)/2, n=(b-a)/2.
- **Also watch for:** Not checking that m-n < m+n (since m,n > 0).
- **Trigger sentence target:** "When I have a Diophantine equation with x^2 - y^2 = k, I factor the left side and use factor pairs of k."

#### Phase 5: Clever Application (Problem 11.12)

**Problem 11.12:** Given x = z - sqrt(z^2 - 5) and 5y = z + sqrt(z^2 - 5), find x when y = 2/3.
- The costume: it LOOKS like you need to solve for z. You don't.
- **If stuck:** "Look at the right sides of both equations. What do they remind you of? Think a - b and a + b."
- Key insight: multiply the equations. (x)(5y) = (z - sqrt(z^2-5))(z + sqrt(z^2-5)) = z^2 - (z^2-5) = 5.
- So 5xy = 5, xy = 1, x = 1/y = 3/2.
- **This is a beautiful problem.** Give him real time to struggle before nudging.
- **Trigger sentence target:** "When I see a-b and a+b with square roots, I multiply to use difference of squares and eliminate the radicals."

#### Phase 6: Computation Problem (Problem 11.13)

**Problem 11.13:** Compute sqrt(1998 * 1996 * 1994 * 1992 + 16). (Source: Mandelbrot)
- This is a hard problem. Multiple techniques needed.
- **Approach:** Let z = 1995 (the middle value). Then the four numbers are z+3, z+1, z-1, z-3.
- Product: (z+3)(z-3)(z+1)(z-1) = (z^2-9)(z^2-1) = z^4 - 10z^2 + 9.
- Add 16: z^4 - 10z^2 + 25 = (z^2 - 5)^2.
- sqrt of that = z^2 - 5 = 1995^2 - 5.
- Then compute 1995^2 = (2000-5)^2 = 4000000 - 20000 + 25 = 3980025. Minus 5 = 3980020.
- **If he's struggling with the substitution choice:** "What number is right in the middle of 1992, 1994, 1996, 1998? What happens if you measure distances from there?"
- **If he gets the z substitution but can't simplify:** "Group the factors into pairs: (z+3)(z-3) and (z+1)(z-1). What's each pair?"
- **This problem uses 11.1 AND 11.2 together.** Make that explicit.
- Consider saving this for review if the session is running long.

#### Phase 7: Exercises

**Assign:**
- 11.2.1: Factor expressions (4 parts)
- 11.2.2: Given 55555^2 = 3086358025, find 55556^2 (use consecutive squares pattern)
- 11.2.3: Prime factorization of 3^4 - 2^4
- 11.2.4: Factor w^4 - 16 completely

**Skip unless hungry:**
- 11.2.5: Geometric proof — nice visual, not essential
- 11.2.6: HMMT problem — very hard, save for challenge

### Custom Layering Exercise: Difference of Squares

**Layer 0:** Factor x^2 - 49. (Naked)

**Layer 1:** Factor 9a^2 - 16b^2. (Coefficient disguise)

**Layer 2:** Find all positive integers n such that n^2 - 81 is a prime. (Must factor: (n-9)(n+9) is prime only if n-9 = 1, so n = 10, check: 10^2 - 81 = 19. Yes, prime.)

**Layer 3:** Evaluate 2023^2 - 2022*2024 without a calculator. (Rewrite 2022*2024 = (2023-1)(2023+1) = 2023^2 - 1. Answer: 1.)

**Layer 4:** If x + y = 10 and x - y = 3, find x^2 - y^2. (Full costume — looks like a system, but x^2 - y^2 = (x+y)(x-y) = 30 immediately.)

### Section 11.2 Mastery Checklist
- [ ] Can factor any difference of squares instantly, including with coefficients
- [ ] Knows to factor out common factors first when terms aren't perfect squares
- [ ] Can chain: recognize when a factor is itself a difference of squares (z^4 - 1)
- [ ] Can use difference of squares to solve Diophantine equations
- [ ] Can spot a-b and a+b patterns to eliminate radicals by multiplying
- [ ] Can use consecutive squares identity for mental arithmetic

---

## SESSION PLAN: Section 11.3 — Sum and Difference of Cubes

### Big Idea
x^3 - y^3 = (x - y)(x^2 + xy + y^2)
x^3 + y^3 = (x + y)(x^2 - xy + y^2)

The linear factor is the "obvious" one. The quadratic factor is the tricky one to remember. Don't memorize — derive.

### Connection to 11.2
"Difference of squares let you factor a^2 - b^2. Can you factor a^3 - b^3? What about a^3 + b^3? (Note: a^2 + b^2 CANNOT be factored over reals. But a^3 + b^3 CAN. Why?)"

### Problem Sequence

#### Phase 1: Discover the Difference of Cubes (Problem 11.14)

**Problem 11.14:** Expand (x-1)(x^2+x+1), (x-2)(x^2+2x+4), (x-3)(x^2+3x+9), then factor x^3 - y^3.
- Have him expand all three products. The pattern should pop:
  - (x-1)(x^2+x+1) = x^3 - 1
  - (x-2)(x^2+2x+4) = x^3 - 8
  - (x-3)(x^2+3x+9) = x^3 - 27
- "So what should x^3 - y^3 factor as?"
- Have him verify by expanding (x-y)(x^2+xy+y^2).
- **Teaching note:** Emphasize that the quadratic factor has ALL POSITIVE terms in the difference of cubes. This is counterintuitive — the minus is only in the linear factor.

#### Phase 2: Discover the Sum of Cubes (Problem 11.15)

**Problem 11.15:** Factor x^3 + y^3.
- Two approaches in the book. The substitution approach is elegant: replace y with -y in the difference formula.
- x^3 + y^3 = x^3 - (-y)^3 = (x-(-y))(x^2 + x(-y) + (-y)^2) = (x+y)(x^2 - xy + y^2).
- **The sign pattern:**
  - DIFFERENCE of cubes: (x **-** y)(x^2 **+** xy + y^2)
  - SUM of cubes: (x **+** y)(x^2 **-** xy + y^2)
  - The linear factor matches the original sign. The quadratic factor has the OPPOSITE sign on xy.
- **Watch for:** Mixing up which factorization has the minus in the quadratic. If he confuses them, ask: "If x = y, should x^3 - y^3 equal zero? Which factorization gives zero when x = y?" (x-y) does, not (x+y).

**Trigger sentence target:** "In the cubic factorizations, the linear factor matches the sign, and the middle term of the quadratic factor is opposite."

#### Phase 3: Practice Factoring (Problem 11.16)

**Problem 11.16:** Factor r^3 - 125, x^3 + 1000, 27y^3 + 1, 32t^3 - 108.
- (a) Straightforward: (r-5)(r^2 + 5r + 25)
- (b) Sum of cubes: (x+10)(x^2 - 10x + 100)
- (c) 27y^3 = (3y)^3, so (3y+1)(9y^2 - 3y + 1)
- (d) Factor out 4 first: 4(8t^3 - 27) = 4(2t-3)(4t^2 + 6t + 9)
- **Watch for (d):** Same issue as 11.2 — must factor out the GCF before applying the identity.

#### Phase 4: Number Theory Application (Problem 11.17)

**Problem 11.17:** Find two prime factors of 7,999,999,999. (Source: HMMT)
- The number is near 8,000,000,000 = (2000)^3.
- So 7,999,999,999 = 2000^3 - 1 = (2000-1)(2000^2 + 2000 + 1) = 1999 * 4,002,001.
- **If stuck:** "The number is very close to a nice round number. What round number? Is that a perfect cube?"
- **Trigger sentence target:** "When a number is close to a perfect cube, I check if it's a sum or difference of cubes."

#### Phase 5: System of Equations (Problem 11.18) — HARD

**Problem 11.18:** Given equations with x^2 - xy + y^2 and x^2 + xy + y^2 in denominators, find x. (Source: HMMT)
- This is hard. The key insight: recognize that x^2 + xy + y^2 and x^2 - xy + y^2 are the QUADRATIC FACTORS from sum/difference of cubes.
- Cross-multiplying gives: x^3 + y^3 = 1 + z^3 and x^3 - y^3 = 27 - z^3.
- Adding: 2x^3 = 28, so x^3 = 14, x = 14^(1/3).
- **Consider saving this for review** if the session is long. It requires comfort with the identities.
- **If he attempts it:** "Look at those denominators. Where have you seen x^2 + xy + y^2 before?"

#### Phase 6: Exercises

**Assign:**
- 11.3.1: Factor expressions (4 parts)
- 11.3.2: Prime factorization of 3^6 + 2^6
- 11.3.3: Express x^6 - 64 as product of four factors
- 11.3.4: Factor x^4 - y^4 and x^5 - y^5

**Skip unless hungry:**
- 11.3.5: Dropped AIME problem — save for challenge

### Custom Layering Exercise: Sum/Difference of Cubes

**Layer 0:** Factor x^3 - 8. (Naked)

**Layer 1:** Factor 64a^3 + 27b^3. (Coefficient disguise)

**Layer 2:** If x - y = 3 and x^2 + xy + y^2 = 19, find x^3 - y^3. (Just multiply! Answer: 57.)

**Layer 3:** Is 9,261,000 divisible by 211? (9261000 = 9261 * 1000 = 21^3 * 10^3 = (210)^3 + extra? Actually, 210^3 = 9261000. So 211^3 - 210^3 = ... actually test: use the factorization. 211^3 - 210^3 = (211-210)(211^2 + 211*210 + 210^2) = 1 * (big number). Hmm, different angle: 9261000 = 210^3. Is 210 divisible by 211? No. So 9,261,000 is NOT divisible by 211.)

**Layer 4:** Find the value of 1/(1+a) + 1/(1+b) + 1/(1+c) if a^3 + b^3 + c^3 = a + b + c and a*b*c = 1. (Competition-style costume over cubes identity.)

### Section 11.3 Mastery Checklist
- [ ] Can state both sum and difference of cubes factorizations
- [ ] Knows which sign goes where (linear factor matches, quadratic middle term is opposite)
- [ ] Can apply to expressions with coefficients (like 27y^3 + 1)
- [ ] Can recognize cube factorization patterns in number theory
- [ ] Can spot the quadratic factors (x^2 + xy + y^2) in equations and connect back to cubes

---

## SESSION PLAN: Section 11.4 — Rationalizing Denominators

### Big Idea
Use the factorizations from 11.1-11.3 to eliminate radicals from denominators. This section is about APPLICATION of everything learned so far.

### Connection to Previous Sections
"You've learned three factorizations. Now you'll see they have a very practical use: cleaning up fractions with square roots in the denominator."

### Problem Sequence

#### Phase 1: Simple Radicals (Problem 11.19)

**Problem 11.19:** Rationalize 1/sqrt(2) and 6/cbrt(3).
- (a) Multiply top and bottom by sqrt(2): 1/sqrt(2) = sqrt(2)/2.
- (b) For cube roots, multiply by cbrt(3^2) = cbrt(9): 6/cbrt(3) * cbrt(9)/cbrt(9) = 6*cbrt(9)/3 = 2*cbrt(9).
- **Teaching note:** Make sure he understands WHY we multiply by sqrt(2): because sqrt(2) * sqrt(2) = 2 (an integer).
- **For cube roots:** We need cbrt(3) * cbrt(3^2) = cbrt(3^3) = 3. So multiply by cbrt(3^2).
- **Trigger sentence target:** "To rationalize sqrt(b) in a denominator, multiply by sqrt(b). For cbrt(b), multiply by cbrt(b^2)."

#### Phase 2: Difference of Squares Application (Problem 11.20)

**Problem 11.20:** Rationalize 1/(sqrt(7) - sqrt(6)).
- This is where difference of squares becomes a tool, not just a factoring exercise.
- Multiply top and bottom by the CONJUGATE: sqrt(7) + sqrt(6).
- (sqrt(7) - sqrt(6))(sqrt(7) + sqrt(6)) = 7 - 6 = 1. Beautiful.
- **If stuck:** "You have a - b in the denominator, where a = sqrt(7) and b = sqrt(6). What do you multiply a - b by to get something without square roots?"
- **Trigger sentence target:** "When the denominator is a +/- b with square roots, I multiply by the conjugate."

#### Phase 3: Multi-step Rationalization (Problem 11.21)

**Problem 11.21:** Rationalize 1/(sqrt(2) + sqrt(3) + sqrt(5)).
- This is a multi-step problem. Three square root terms.
- Strategy: group two terms as "a" and treat the third as "b". Multiply by the conjugate.
  - Let a = sqrt(2) + sqrt(3), view denominator as a + sqrt(5).
  - Multiply by (a - sqrt(5)) = (sqrt(2) + sqrt(3) - sqrt(5)).
  - Denominator becomes a^2 - 5 = (2 + 2*sqrt(6) + 3) - 5 = 2*sqrt(6).
  - Then rationalize 2*sqrt(6) by multiplying by sqrt(6)/sqrt(6).
- **Don't give him the grouping strategy right away.** Let him try. If he's stuck after a minute: "Can you group two of the three terms together?"
- **Watch for:** Trying to multiply by sqrt(2)*sqrt(3)*sqrt(5) or some product — that doesn't work.

#### Phase 4: Cube Root Rationalization (Problem 11.22)

**Problem 11.22:** Rationalize 1/(2 - cbrt(2)).
- Now difference of CUBES is the tool.
- a^3 - b^3 = (a-b)(a^2 + ab + b^2), so (2 - cbrt(2)) is the (a-b) factor with a = 2, b = cbrt(2).
- Multiply by (a^2 + ab + b^2) = 4 + 2*cbrt(2) + cbrt(4).
- Denominator becomes 2^3 - (cbrt(2))^3 = 8 - 2 = 6.
- **If stuck:** "The cbrt(2) makes you think of cubes. If 2 - cbrt(2) is the first factor in a^3 - b^3, what's the second factor?"
- **Teaching note:** This is a gorgeous connection between sections. Make it explicit: "You just used 11.3 to solve a problem that looks nothing like 11.3."

#### Phase 5: Exercises

**Assign:**
- 11.4.2: Rationalize fractions with conjugate denominators (3 parts)
- 11.4.3: Rationalize 4/(cbrt(9) - cbrt(3) * sqrt(3) + cbrt(9)) — cube root practice

**Challenge (assign if he's feeling strong):**
- 11.4.4: Rationalize 2/(sqrt(6) - sqrt(2))
- 11.4.5: Telescoping sum 1/(sqrt(100)+sqrt(99)) + 1/(sqrt(99)+sqrt(98)) + ... + 1/(sqrt(2)+sqrt(1))

### Custom Layering Exercise: Rationalizing Denominators

**Layer 0:** Rationalize 5/sqrt(3). (Naked)

**Layer 1:** Rationalize 3/(sqrt(5) - 2). (One conjugate step)

**Layer 2:** Simplify 1/(sqrt(n+1) + sqrt(n)). Then compute the sum for n = 1 to 99. (Telescoping — each term becomes sqrt(n+1) - sqrt(n) after rationalizing.)

**Layer 3:** Rationalize 1/(1 + cbrt(3)). (Must use sum of cubes idea with a = 1, b = cbrt(3), so multiply by 1 - cbrt(3) + cbrt(9).)

**Layer 4:** Given that 1/(3 + 2*sqrt(2)) = a + b*sqrt(2) for integers a, b, find a + b. (Rationalize, then read off a and b.)

### Section 11.4 Mastery Checklist
- [ ] Can rationalize simple radical denominators (1/sqrt(n))
- [ ] Can use conjugates to rationalize (a + sqrt(b)) denominators
- [ ] Can handle two-step rationalization (three radical terms)
- [ ] Can use difference/sum of cubes for cube root denominators
- [ ] Recognizes which factorization to use based on the radical type

---

## SESSION PLAN: Section 11.5 — Simon's Favorite Factoring Trick (SFFT)

### Big Idea
ab + ay + bx + xy = (a + x)(b + y). When you see the product of two variables plus linear terms in those variables, add a constant to both sides so you can factor.

### Connection to Previous Sections
"Every factorization so far has been about recognizing a pattern. SFFT is about CREATING a pattern that isn't there yet — by adding the right constant to both sides."

### Why This Section Matters
SFFT appears constantly in competition math, especially AMC/AIME. It's one of the highest-value techniques in this chapter.

### Problem Sequence

#### Phase 1: Introduction (Problem 11.23)

**Problem 11.23:** Find all positive integer pairs (m, n) with mn + m + n = 76.
- Guide him step by step:
  1. "Can you factor the left side?" He can't — it's mn + m + n.
  2. "What if you factor m from the first two terms?" → m(n+1) + n = 76.
  3. "The left side has an (n+1) and a plain n. What if that n were also n+1?" → Add 1 to both sides.
  4. m(n+1) + (n+1) = 77, so (m+1)(n+1) = 77.
  5. Factor pairs of 77: 1*77, 7*11.
  6. Since m, n positive: (m+1, n+1) = (7, 11) or (11, 7). So (m, n) = (6, 10) or (10, 6).
- **Teaching note:** The "trick" is realizing you need to add a constant. The method for finding the constant: try to write the left side as (m + ?)(n + ?), expand, and see what's missing.
- **Trigger sentence target:** "When I see mn + am + bn, I try to factor it as (m + b)(n + a) by adding ab to both sides."

#### Phase 2: General Case (Problem 11.24)

**Problem 11.24:** Find all integer pairs (b, c) with bc - 7b + 3c = 70.
- Now the coefficients of b and c are NOT 1. This is the general case.
- Target factorization: (b + 3)(c - 7).
- Expand: bc - 7b + 3c - 21. So add -21 to both sides... wait, that means SUBTRACT 21.
- (b + 3)(c - 7) = 70 - 21 = 49.
- Factor pairs of 49: 1*49, 7*7, 49*1, (-1)(-49), (-7)(-7), (-49)(-1).
- **Watch for:** Him forgetting negative factor pairs. The problem says "integers", not "positive integers"!
- **Key teaching moment:** HOW to find the constant. Method: "Look at the coefficients of b and c. The -7 on b means c has -7 in its factor. The +3 on c means b has +3 in its factor. So (b+3)(c-7). Expand to find what constant to add."
- **Trigger sentence target:** "In SFFT, the coefficient of one variable tells me what to add to the OTHER variable's factor."

#### Phase 3: Hidden SFFT (Problem 11.25)

**Problem 11.25:** How many ordered pairs (m, n) of positive integers solve 4/n + 2/m = 1? (Source: AHSME)
- The costume: it doesn't LOOK like SFFT. It looks like a fraction equation.
- Step 1: Multiply both sides by mn: 4m + 2n = mn.
- Step 2: Rearrange: mn - 2n - 4m = 0.
- Step 3: Now it looks like SFFT! Factor: (m - 2)(n - 4) = 8.
  - (To get there: we want (m-?)(n-?) = mn - 2n - 4m + ?. The constant is (-2)(-4) = 8. Add 8 to both sides.)
- Step 4: Factor pairs of 8 with m-2 > -2 and n-4 > -4 (positive integers): 1*8, 2*4, 4*2, 8*1.
- All four give valid positive integer solutions. Answer: 4.
- **If stuck after clearing fractions:** "You have mn, 2n, and 4m. What technique deals with the product of two variables plus linear terms in those variables?"
- **Trigger sentence target:** "When I clear fractions in 1/m + 1/n = something and get mn mixed with m and n, that's SFFT."

#### Phase 4: Exercises

**Assign:**
- 11.5.1: Factor ab + 5b + 2a + 10.
- 11.5.2: Factor xy + 8x - 3y - 24.
- 11.5.3: Prime factorization of 19*13 - 7*13 + 3*19 - 21.
- 11.5.4: Write 1/7 as sum of two distinct positive unit fractions. (Very good SFFT problem!)
- 11.5.5: Find all integer pairs (p, q) with pq - 3p + 5q = 0.

**Skip unless hungry:**
- 11.5.6: Factor x^2*y^2 - 4y^2 - x^2 + 4 and 2cd - 3d - 14c + 21.

### Custom Layering Exercise: SFFT

**Layer 0:** Factor xy + 3x + 2y + 6. (Naked — just group and factor.)

**Layer 1:** Find all positive integer pairs (a, b) with ab + a + b = 35. (Direct SFFT, add 1: (a+1)(b+1) = 36.)

**Layer 2:** Find all positive integer solutions to 1/x + 1/y = 1/6. (Clear fractions → xy - 6x - 6y = 0 → add 36 → (x-6)(y-6) = 36.)

**Layer 3:** A rectangle has integer side lengths and perimeter equal to its area. Find all possible dimensions. (If sides are a, b: ab = 2a + 2b → ab - 2a - 2b = 0 → add 4 → (a-2)(b-2) = 4. Solutions: (3,6), (4,4), (6,3).)

**Layer 4:** Find all ordered pairs of positive integers (m, n) such that 1/m + 1/n + 1/(mn) = 1/2. (Clear fractions, rearrange, apply SFFT. The costume is thick — three fraction terms.)

### Section 11.5 Mastery Checklist
- [ ] Can factor expressions of the form ab + ay + bx + xy by grouping
- [ ] Knows how to determine the constant to add (product of the coefficients of the linear terms)
- [ ] Can apply SFFT to Diophantine equations
- [ ] Can recognize SFFT opportunities even when hidden behind fraction clearing or rearrangement
- [ ] Remembers to check ALL factor pairs (including negatives when the problem allows integers, not just positive integers)

---

## SESSION PLAN: Review & Summary (Section 11.6)

### Session Structure

**Part 1: Identity Speed Round (5 minutes)**
Quiz him rapid-fire. He states each factorization from memory:
1. (a+b)^2 = ?
2. a^2 - b^2 = ?
3. a^3 - b^3 = ?
4. a^3 + b^3 = ?
5. ab + ay + bx + xy = ?

If he hesitates on any, that section needs more practice before moving on.

**Part 2: "Which Tool?" Drill (10 minutes)**
Give him problem STATEMENTS only (no solving). He identifies which factorization to use:
- "Factor 25x^2 - 49y^2" → Difference of squares
- "Factor 8a^3 + 27" → Sum of cubes
- "mn + 5m + 3n = 100, find positive integer solutions" → SFFT
- "Rationalize 1/(sqrt(5) - sqrt(3))" → Difference of squares (conjugate)
- "Is 9x^2 + 30x + 25 a perfect square?" → Square of binomial
- "Factor x^6 - 1" → Difference of squares, then difference/sum of cubes

This trains RECOGNITION, which is Mahmoud's stated gap.

**Part 3: Review Problems (from Section 11.6)**

**Assign in order:**
- 11.26: Expand (7-x)^2 and (2t-9)^2 — warmup
- 11.27: Mental squares — 45, 91, 401, 199
- 11.28: Find a such that 9x^2 + 24x + a is a perfect square
- 11.29: Factor 1-121t^2 and -32t^2 + 50
- 11.30: Compute 111^2 - 89^2 in your head (difference of squares: 200 * 22 = 4400)
- 11.31: Compute (207+100)^2 - (207-100)^2 (difference of squares: 2*207*2*100? No: (307)^2 - (107)^2 = (307-107)(307+107) = 200*414 = 82800)
- 11.32: Which is bigger, 4050607^2 or 4050608*4050606? (The product = 4050607^2 - 1, so the square is bigger by 1.)
- 11.33: Let x = 2001^10 - 2001^(-10) and y = 2001^10 + 2001^(-10). Find x^2 - y^2. (x^2 - y^2 = (x-y)(x+y). x-y = -2*2001^(-10), x+y = 2*2001^10. Product = -4. Beautiful.)
- 11.34: Consecutive perfect squares with difference 63. (n^2 - (n-1)^2 = 2n-1 = 63, so n = 32. Squares: 31^2 and 32^2.)
- 11.35: Factor expressions with cubes (4 parts)
- 11.36: Expand (sqrt(v) - sqrt(u))(sqrt(v) + sqrt(vu) + sqrt(u)) — this is a cube root rationalization in disguise
- 11.37: Rationalize denominators (3 parts)

### Section 11.6 Mastery Checklist (Chapter-Level)
- [ ] Can state all five factorizations from memory
- [ ] Can identify which factorization to use from a problem statement in under 10 seconds
- [ ] Can apply each factorization in both directions (expand and factor)
- [ ] Can solve Diophantine equations using difference of squares and SFFT
- [ ] Can rationalize denominators using difference of squares and sum/difference of cubes
- [ ] Can compose multiple factorizations in one problem (e.g., Problem 11.13)

---

## SESSION PLAN: Challenge Problems

### Triage

**Accessible (try first):**
- 11.38: Rationalize denominators (more practice)
- 11.39: Factor pq - 7p + 9q - 63 and -rs + 5r + 2s - 10 (SFFT)
- 11.41: Diophantine: xy - 2x + 7y = 49 (SFFT)
- 11.42: Telescoping sum with rationalization (AHSME) — gorgeous problem
- 11.43: Consecutive odd integers with b^2 - a^2 = 344 — difference of squares
- 11.44: Evaluate 29^2, 299^2, 2999^2 and find digit sum of 29999999^2

**Medium (attempt after accessible set):**
- 11.40: Rationalize 2/(cbrt(something)) — cube root technique
- 11.45: Big product with difference of squares (Mandelbrot)
- 11.46: Harder rationalization
- 11.48: ab = a - b, find a/b + b/a - ab (AMC 12)
- 11.50: Geometric proof of (a+b+c)^2

**Hard (stretch problems):**
- 11.47: Largest prime divisor of 5^14 - 2*10^7 + 2^14
- 11.49: Factor x^5 + y^5 and generalize to x^(2n+1) + y^(2n+1)
- 11.51: How many triples (a,b,c) from {1,...,5} satisfy a^2 + bc = b^2 + ac (Mandelbrot)
- 11.52: Right triangle with expressions involving 10^n
- 11.53: sqrt(1 + 50*51*52*53) (MATHCOUNTS)
- 11.54: Factor x^4 + 4y^4 (Sophie Germain identity!)
- 11.55: Express 2^72 + 1 as product of two four-digit numbers
- 11.56-11.57: Hard computation problems

### Challenge Problem Teaching Notes

**11.42 (Telescoping):** 1/(sqrt(3) - sqrt(2)) + 1/(sqrt(4) - sqrt(3)) + ... + 1/(sqrt(9) - sqrt(8)). Each term rationalizes to sqrt(n+1) + sqrt(n). Sum telescopes to sqrt(9) - sqrt(2) = 3 - sqrt(2). This is a HIGH-VALUE technique. Make sure he sees the telescoping.

**11.48 (AMC 12):** ab = a - b. Want a/b + b/a - ab. Key: ab = a - b means a = b/(1-b) if b != 1, or a(b-1) = -b. Then a/b + b/a = (a^2+b^2)/(ab) and ab = a - b. Substitute. Answer: a/b + b/a - ab. From ab = a - b, we get a/b - 1 = -1 + 1/b, etc. The answer is -1. (Or use SFFT: ab - a + b = 0, add 1: (a+1)(b-1) = -1.)

**11.53 (MATHCOUNTS):** sqrt(1 + 50*51*52*53). Let the middle be 51.5 (or use z = 51 or z = 52). With z = 51: 50*51*52*53 = (51^2 - 1)(51^2 + 51*2) ... actually, let z = 51.5: the four numbers are z-1.5, z-0.5, z+0.5, z+1.5. Product = (z^2 - 0.25)(z^2 - 2.25) = z^4 - 2.5z^2 + 0.5625. Add 1: z^4 - 2.5z^2 + 1.5625 = (z^2 - 1.25)^2. sqrt = z^2 - 1.25 = 51.5^2 - 1.25 = 2652.25 - 1.25 = 2651. (This is very similar to Problem 11.13!)

**11.54 (Sophie Germain):** x^4 + 4y^4 = (x^4 + 4x^2y^2 + 4y^4) - 4x^2y^2 = (x^2 + 2y^2)^2 - (2xy)^2 = (x^2 + 2y^2 - 2xy)(x^2 + 2y^2 + 2xy). This is a FAMOUS identity. Add and subtract to complete the square, then use difference of squares.

---

## PACING GUIDE

| Session | Content | Est. Time | Prerequisites |
|---------|---------|-----------|---------------|
| 1 | 11.1 Squares of Binomials | 45-60 min | Chapter 10 factoring |
| 2 | 11.2 Difference of Squares | 45-60 min | 11.1 mastery |
| 3 | 11.3 Sum/Difference of Cubes | 45-60 min | 11.2 mastery |
| 4 | 11.4 Rationalizing Denominators | 30-45 min | 11.1-11.3 mastery |
| 5 | 11.5 Simon's Favorite Factoring Trick | 45-60 min | Diophantine equations from 11.2 |
| 6 | Review (11.6) + Which-Tool Drill | 30-45 min | All sections |
| 7 | Challenge Problems (accessible set) | 45-60 min | All sections mastered |
| 8 | Challenge Problems (medium + hard) | 45-60 min | Session 7 |

**Adjust pacing based on Mahmoud's speed:**
- If he's flying through a section (getting problems right quickly, trigger sentences come easy), compress two sections into one session.
- If he's struggling with recognition (can do the math but can't identify WHEN to use a technique), slow down and add more layering exercises.
- The review session (Session 6) is mandatory. Don't skip it even if he seems comfortable.

## TRIGGER SENTENCE LOG (Build This Throughout)

Start a running list. After every problem, write one. By the end of the chapter, he should have ~15-20 triggers. Example targets:

1. "The middle term is always twice the product of the two parts." (11.1)
2. "To check if a trinomial is a perfect square, I check if the middle term = 2 * sqrt(first) * sqrt(last)." (11.1)
3. "When I see a^2 - 2ab + b^2 with big numbers, factor as (a-b)^2 first." (11.1)
4. "Whenever I see the difference of two perfect squares, I factor." (11.2)
5. "The difference of consecutive squares is always their sum." (11.2)
6. "For Diophantine equations with x^2 - y^2 = k, factor and use factor pairs." (11.2)
7. "When I see a-b and a+b with square roots, multiply to eliminate radicals." (11.2)
8. "In cubic factorizations, the linear factor matches the sign, the quadratic middle term is opposite." (11.3)
9. "When a number is close to a perfect cube, check if it's a sum/difference of cubes." (11.3)
10. "To rationalize sqrt(b), multiply by sqrt(b). For cbrt(b), multiply by cbrt(b^2)." (11.4)
11. "Conjugate multiplication eliminates square roots: (a+sqrt(b))(a-sqrt(b)) = a^2 - b." (11.4)
12. "When I see mn + am + bn, try (m+b)(n+a) by adding ab to both sides." (11.5)
13. "After clearing fractions, if I get mn mixed with m and n, that's SFFT." (11.5)
14. "Always check ALL factor pairs — including negatives for integer (not positive integer) problems." (11.5)

## META-NOTES FOR TEACHING

### Mahmoud's Known Patterns (from math-teaching-prompt.md)
- **Jumps to answers:** Push for intermediate steps on multi-step factoring problems (e.g., Problem 11.9d where you need to factor TWICE).
- **Discounts easy things:** Fine. If he says "that's obvious" after nailing perfect square recognition, don't comment, move on.
- **Rushing errors:** If he's making sign errors in the cube factorizations (very common), slow him down: "Show me each term." Don't lecture about being careful.
- **Thinks out loud:** Give him a beat before correcting. He might catch his own mistakes.

### Hardest Transitions (Where He'll Likely Get Stuck)
1. **11.2 → Diophantine:** The leap from "I can factor x^2 - y^2" to "I should factor this equation to solve it" is not obvious. Problem 11.11 is the bridge.
2. **11.4 → Using identities as tools:** Rationalizing denominators requires seeing factorizations as TOOLS, not just patterns. Problem 11.22 (cube root rationalization) is the hardest jump.
3. **11.5 → Finding the constant:** The hardest part of SFFT is knowing WHAT constant to add. Teach the method: "Guess (m+?)(n+?), expand, compare."
4. **Recognition across sections:** The review session's "Which Tool?" drill is critical. He needs to see ALL five tools side by side.

### Red Flags (When to Slow Down)
- If he can't state (a+b)^2 from memory by the end of Session 1 → re-drill
- If he confuses the signs in sum vs. difference of cubes → go back to derivation
- If he can factor when told which identity to use but can't identify the identity from a problem statement → needs more layering exercises
- If SFFT problems feel like magic rather than method → more practice finding the constant

### When to Speed Up
- If he's getting exercises right on first attempt with no errors → skip the custom layering and move to next section
- If trigger sentences come naturally ("oh, I should factor because...") → he's internalized the recognition
- If he starts solving challenge problems unprompted → he's ready for next chapter
