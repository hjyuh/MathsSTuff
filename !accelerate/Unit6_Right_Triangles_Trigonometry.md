# Unit 6: Right Triangles & Trigonometry
## Honors Geometry Study Notes

---

## Table of Contents
1. [The Pythagorean Theorem](#the-pythagorean-theorem)
2. [Pythagorean Triples](#pythagorean-triples)
3. [The Converse of the Pythagorean Theorem](#the-converse-of-the-pythagorean-theorem)
4. [Special Right Triangles](#special-right-triangles)
5. [Introduction to Trigonometric Ratios](#introduction-to-trigonometric-ratios)
6. [SOH-CAH-TOA: The Three Main Ratios](#soh-cah-toa-the-three-main-ratios)
7. [Cofunctions and Complementary Angles](#cofunctions-and-complementary-angles)
8. [Finding Missing Sides Using Trig Ratios](#finding-missing-sides-using-trig-ratios)
9. [Finding Missing Angles Using Inverse Trig](#finding-missing-angles-using-inverse-trig)
10. [Angles of Elevation and Depression](#angles-of-elevation-and-depression)
11. [Area of a Triangle Using Sine](#area-of-a-triangle-using-sine)
12. [Law of Sines](#law-of-sines)
13. [Law of Cosines](#law-of-cosines)
14. [Choosing Between Laws and Methods](#choosing-between-laws-and-methods)

---

## The Pythagorean Theorem

### What It Is (Plain English)
The Pythagorean Theorem is one of the most famous relationships in mathematics. It describes the connection between the three sides of any **right triangle** (a triangle with one 90° angle). The theorem states that if you take the two sides that form the right angle and square them, their sum equals the square of the longest side.

### Key Vocabulary
- **Right triangle**: A triangle containing exactly one 90° angle (shown with a small square in the corner)
- **Legs**: The two sides that form the right angle (usually labeled *a* and *b*)
- **Hypotenuse**: The side opposite the right angle; always the longest side (labeled *c*)
- **Theorem**: A mathematical statement that has been proven true

### Core Concept
In a right triangle:
- The two legs meet at the right angle
- The hypotenuse is always across from the right angle
- The hypotenuse is ALWAYS longer than either leg

### The Formula

$$a^2 + b^2 = c^2$$

Where:
- *a* = length of first leg
- *b* = length of second leg
- *c* = length of hypotenuse (longest side)

### How to Use the Theorem

**Step 1:** Identify which sides are the legs (they form the right angle) and which is the hypotenuse.

**Step 2:** Substitute the known values into $a^2 + b^2 = c^2$.

**Step 3:** Solve for the unknown side.

### Worked Example 1: Finding the Hypotenuse
A right triangle has legs of length 3 cm and 4 cm. Find the hypotenuse.

**Solution:**
- Legs: *a* = 3, *b* = 4
- Unknown: *c* (hypotenuse)
- Substitute into $a^2 + b^2 = c^2$:
  $$3^2 + 4^2 = c^2$$
  $$9 + 16 = c^2$$
  $$25 = c^2$$
  $$c = 5$$
- **Answer: The hypotenuse is 5 cm**

### Worked Example 2: Finding a Leg
A right triangle has a hypotenuse of 13 inches and one leg of 5 inches. Find the other leg.

**Solution:**
- Hypotenuse: *c* = 13
- One leg: *a* = 5
- Unknown: *b*
- Substitute into $a^2 + b^2 = c^2$:
  $$5^2 + b^2 = 13^2$$
  $$25 + b^2 = 169$$
  $$b^2 = 169 - 25$$
  $$b^2 = 144$$
  $$b = 12$$
- **Answer: The other leg is 12 inches**

### Worked Example 3: Determining if it's Actually a Right Triangle
A triangle has sides 5, 8, and 10. Is it a right triangle?

**Solution:**
- Test if $a^2 + b^2 = c^2$ using the two smaller sides as legs and the largest as hypotenuse
- $$5^2 + 8^2 = 10^2$$
- $$25 + 64 = 100$$
- $$89 ≠ 100$$
- **Answer: No, this is NOT a right triangle** (it's close, but not exact!)

### Common Mistakes
- **Mistake 1**: Forgetting to square the sides. The formula is $a^2 + b^2 = c^2$, NOT $a + b = c$.
- **Mistake 2**: Using the wrong sides. Always use the legs (sides forming the right angle) for *a* and *b*, and the longest side for *c*.
- **Mistake 3**: Forgetting to take the square root. If $c^2 = 25$, then $c = 5$ (not 25).

### Exam Tips
- Always identify the right angle first—the hypotenuse is ALWAYS opposite it.
- Draw a diagram if one isn't provided; it helps you see which side is which.
- Check your answer: the hypotenuse should always be longer than either leg.

---

## Pythagorean Triples

### What They Are
A **Pythagorean triple** is a set of three positive integers that satisfy the Pythagorean Theorem. These are "nice" right triangles with whole number side lengths.

### Key Vocabulary
- **Primitive triple**: A Pythagorean triple where the three numbers share no common factor other than 1
- **Multiple of a triple**: Multiplying all three numbers in a triple by the same whole number creates a new triple

### Why They Matter
When you encounter a Pythagorean triple, you can immediately recognize a right triangle without calculating. They appear frequently on exams and in real-world problems.

### The Five Most Common Triples

#### Triple 1: 3-4-5
- Check: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$ ✓
- **Multiples**: 6-8-10, 9-12-15, 12-16-20, 15-20-25, etc.

#### Triple 2: 5-12-13
- Check: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$ ✓
- **Multiples**: 10-24-26, 15-36-39, 20-48-52, etc.

#### Triple 3: 8-15-17
- Check: $8^2 + 15^2 = 64 + 225 = 289 = 17^2$ ✓
- **Multiples**: 16-30-34, 24-45-51, etc.

#### Triple 4: 7-24-25
- Check: $7^2 + 24^2 = 49 + 576 = 625 = 25^2$ ✓
- **Multiples**: 14-48-50, 21-72-75, etc.

#### Triple 5: 20-21-29
- Check: $20^2 + 21^2 = 400 + 441 = 841 = 29^2$ ✓
- **Multiples**: 40-42-58, 60-63-87, etc.

### Recognizing Multiples

If you see sides 6, 8, and 10:
- Notice: 6 = 2(3), 8 = 2(4), 10 = 2(5)
- This is 2 times the 3-4-5 triple
- It's a **right triangle** with hypotenuse 10

### Worked Example 1: Identifying a Triple
Is 9-12-15 a Pythagorean triple?

**Solution:**
- Test: $9^2 + 12^2 = 15^2$?
- $81 + 144 = 225$?
- $225 = 225$ ✓
- Also notice: 9 = 3(3), 12 = 3(4), 15 = 3(5)
- This is **3 times the 3-4-5 triple**
- **Answer: Yes, 9-12-15 is a Pythagorean triple**

### Worked Example 2: Using Triples to Avoid Calculation
A right triangle has legs of 20 and 21. Find the hypotenuse without a calculator.

**Solution:**
- Recognize that 20-21 matches the 20-21-29 triple
- The hypotenuse must be **29**
- (If you didn't recognize the triple: $20^2 + 21^2 = 400 + 441 = 841 = 29^2$)
- **Answer: 29**

### Worked Example 3: Finding a Side Using a Multiple
A right triangle has legs of 15 and 20. Find the hypotenuse.

**Solution:**
- Notice: 15 = 5(3) and 20 = 5(4)
- These are 5 times the 3-4-5 triple
- The hypotenuse is 5 times the hypotenuse of 3-4-5
- Hypotenuse = 5(5) = **25**
- **Answer: 25**

### Common Mistakes
- **Mistake**: Assuming any triple with these numbers in different order works. The legs must be 3 and 4 (or their multiples) for the 3-4-5 triple—not 5 and 3.

### Exam Tips
- Memorize the five common triples. You'll be amazed how often they appear.
- Always check multiples: if you see large numbers, factor them to find the base triple.

---

## The Converse of the Pythagorean Theorem

### What It Is
The **converse** of a theorem reverses the "if-then" statement. The original Pythagorean Theorem says: "If it's a right triangle, then $a^2 + b^2 = c^2$."

The **Converse** says: "If $a^2 + b^2 = c^2$, then it's a right triangle."

### Why This Matters
The converse lets us **identify** right triangles without measuring angles. We can also classify triangles as acute or obtuse!

### The Three Cases

When given three sides of a triangle with *a* ≤ *b* < *c*:

| Case | Relationship | Triangle Type |
|------|--------------|----------------|
| **Case 1** | $a^2 + b^2 = c^2$ | **Right triangle** (right angle opposite side *c*) |
| **Case 2** | $a^2 + b^2 > c^2$ | **Acute triangle** (all angles less than 90°) |
| **Case 3** | $a^2 + b^2 < c^2$ | **Obtuse triangle** (one angle greater than 90°) |

### Core Concept
Think of it this way: if the two smaller sides have enough combined "power" (when squared) to match the largest side, we have a right angle. If they have MORE power, the angle is sharp (acute). If they have LESS power, the angle is dull (obtuse).

### Worked Example 1: Identifying a Right Triangle
A triangle has sides 5, 12, and 13. What type of triangle is it?

**Solution:**
- Order sides: 5 ≤ 12 < 13
- Test: $5^2 + 12^2 = 13^2$?
- $25 + 144 = 169$?
- $169 = 169$ ✓
- **Answer: This is a RIGHT TRIANGLE** (the 5-12-13 Pythagorean triple!)

### Worked Example 2: Identifying an Acute Triangle
A triangle has sides 6, 7, and 8. What type of triangle is it?

**Solution:**
- Order sides: 6 ≤ 7 < 8
- Test: $6^2 + 7^2$ compared to $8^2$
- $36 + 49 = 85$ compared to $64$
- $85 > 64$
- So $6^2 + 7^2 > 8^2$
- **Answer: This is an ACUTE TRIANGLE** (all angles less than 90°)

### Worked Example 3: Identifying an Obtuse Triangle
A triangle has sides 2, 3, and 4. What type of triangle is it?

**Solution:**
- Order sides: 2 ≤ 3 < 4
- Test: $2^2 + 3^2$ compared to $4^2$
- $4 + 9 = 13$ compared to $16$
- $13 < 16$
- So $2^2 + 3^2 < 4^2$
- **Answer: This is an OBTUSE TRIANGLE** (one angle greater than 90°)

### Common Mistakes
- **Mistake**: Comparing the wrong sides. Always compare $a^2 + b^2$ with $c^2$ where *c* is the LONGEST side.
- **Mistake**: Forgetting which case corresponds to which triangle type. Use the mnemonic: **More power = acute, Equal power = right, Less power = obtuse**.

### Exam Tips
- The converse is often tested in problems disguised as "determine the triangle type."
- Always arrange sides in order before testing.
- Remember: the longest side is always relevant for the comparison.

---

## Special Right Triangles

### Why They're Special
Some right triangles appear so frequently in mathematics that their side ratios are worth memorizing. These are the **45-45-90 triangle** and the **30-60-90 triangle**. Knowing these ratios saves time on exams.

---

## The 45-45-90 Triangle

### What It Is
A right triangle where the two acute angles both measure 45°. This means the two legs are **equal in length**.

### Key Vocabulary
- **Isosceles right triangle**: Another name for a 45-45-90 triangle (isosceles means two equal sides)
- **Unit leg**: If we call each leg length 1, the hypotenuse is √2

### The Ratio
$$\text{leg} : \text{leg} : \text{hypotenuse} = 1 : 1 : \sqrt{2}$$

### How to Remember It
- Both legs are the **same**
- The hypotenuse is the leg length times **√2**

### The Formula
If each leg has length *x*, then:
- Each leg = *x*
- Hypotenuse = $x\sqrt{2}$

### Worked Example 1: Finding the Hypotenuse
In a 45-45-90 triangle, each leg measures 5 cm. Find the hypotenuse.

**Solution:**
- Each leg = 5
- Using the pattern: hypotenuse = leg × √2
- Hypotenuse = $5\sqrt{2}$ cm
- **Answer: $5\sqrt{2}$ cm** (approximately 7.07 cm if decimal form is needed)

### Worked Example 2: Finding the Legs
A 45-45-90 triangle has a hypotenuse of 8 inches. Find each leg.

**Solution:**
- Hypotenuse = 8
- Using the pattern: hypotenuse = leg × √2
- $8 = \text{leg} \times \sqrt{2}$
- $\text{leg} = \frac{8}{\sqrt{2}}$
- Rationalize: $\frac{8}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{8\sqrt{2}}{2} = 4\sqrt{2}$ inches
- **Answer: Each leg is $4\sqrt{2}$ inches** (approximately 5.66 inches)

### Worked Example 3: Applied Problem
A square has a diagonal of 10 feet. What is the length of each side?

**Solution:**
- A square with a diagonal forms a 45-45-90 triangle (the diagonal is the hypotenuse)
- The two legs are the sides of the square
- Hypotenuse = 10
- Using leg = hypotenuse ÷ √2:
- $\text{side} = \frac{10}{\sqrt{2}} = \frac{10\sqrt{2}}{2} = 5\sqrt{2}$ feet
- **Answer: Each side is $5\sqrt{2}$ feet**

### Common Mistakes
- **Mistake 1**: Forgetting to rationalize denominators. Don't leave $\frac{8}{\sqrt{2}}$—rationalize it to $4\sqrt{2}$.
- **Mistake 2**: Confusing which dimension is which. The legs are EQUAL; the hypotenuse is different.
- **Mistake 3**: Multiplying by √2 when you should divide, or vice versa. Remember: going from leg to hypotenuse multiplies by √2; going from hypotenuse to leg divides by √2.

### Exam Tips
- Memorize the ratio 1 : 1 : √2 so you recognize it instantly.
- These triangles often appear in coordinate geometry and area problems.

---

## The 30-60-90 Triangle

### What It Is
A right triangle where the two acute angles measure 30° and 60°. The sides have a special relationship that depends on which angle is which.

### Key Vocabulary
- **Short leg**: The side opposite the 30° angle (shortest side overall)
- **Long leg**: The side opposite the 60° angle
- **Hypotenuse**: The side opposite the 90° angle

### The Ratio
$$\text{short leg} : \text{long leg} : \text{hypotenuse} = 1 : \sqrt{3} : 2$$

### How to Remember It
- The short leg (opposite 30°) is the base unit: 1
- The long leg (opposite 60°) is √3 times the short leg
- The hypotenuse is 2 times the short leg

### The Formulas
If the short leg (opposite 30°) has length *x*:
- Short leg = *x*
- Long leg = $x\sqrt{3}$
- Hypotenuse = $2x$

### Worked Example 1: Finding All Sides from the Short Leg
In a 30-60-90 triangle, the short leg (opposite 30°) is 4 cm. Find the long leg and hypotenuse.

**Solution:**
- Short leg = 4
- Using the pattern 1 : √3 : 2
- Long leg = short leg × √3 = $4\sqrt{3}$ cm
- Hypotenuse = short leg × 2 = 4 × 2 = 8 cm
- **Answer: Long leg = $4\sqrt{3}$ cm; Hypotenuse = 8 cm**

### Worked Example 2: Finding All Sides from the Hypotenuse
In a 30-60-90 triangle, the hypotenuse is 10 inches. Find both legs.

**Solution:**
- Hypotenuse = 10
- Using the pattern where hypotenuse = 2 × short leg:
- $10 = 2 \times \text{short leg}$
- Short leg = 5 inches
- Long leg = short leg × √3 = $5\sqrt{3}$ inches
- **Answer: Short leg = 5 inches; Long leg = $5\sqrt{3}$ inches**

### Worked Example 3: Finding All Sides from the Long Leg
In a 30-60-90 triangle, the long leg (opposite 60°) is $6\sqrt{3}$ feet. Find the short leg and hypotenuse.

**Solution:**
- Long leg = $6\sqrt{3}$
- Using the pattern where long leg = √3 × short leg:
- $6\sqrt{3} = \sqrt{3} \times \text{short leg}$
- Short leg = 6 feet
- Hypotenuse = short leg × 2 = 6 × 2 = 12 feet
- **Answer: Short leg = 6 feet; Hypotenuse = 12 feet**

### How to Identify Which Leg Is Which
When a 30-60-90 triangle is drawn, you must determine which leg is opposite which angle:
- **The short leg is ALWAYS opposite the 30° angle**
- **The long leg is ALWAYS opposite the 60° angle**
- The hypotenuse is opposite the 90° angle

### Common Mistakes
- **Mistake 1**: Reversing the short and long legs. The short leg (smaller number) is opposite 30°. The long leg (with √3) is opposite 60°.
- **Mistake 2**: Using the wrong multiplier. Remember: long leg = short leg × √3 (not short leg × 2).
- **Mistake 3**: Not rationalizing when needed. If you have $\frac{10}{\sqrt{3}}$, rationalize: $\frac{10}{\sqrt{3}} \times \frac{\sqrt{3}}{\sqrt{3}} = \frac{10\sqrt{3}}{3}$.

### Exam Tips
- Always label the angles in the triangle if they're not already labeled.
- Draw the triangle and mark the 30° and 60° angles clearly.
- These triangles appear frequently in geometry, trigonometry, and even calculus.

---

## Introduction to Trigonometric Ratios

### What Trigonometry Is (Plain English)
**Trigonometry** is the study of the relationships between angles and side lengths in triangles. The word comes from "tri" (three), "gon" (angle), and "metry" (measure).

The key insight: **In similar triangles with the same angle, the ratios of the sides are always the same.** This fact lets us use one known angle and one known side to find everything else about a right triangle.

### Key Vocabulary
- **Trigonometric ratio**: A fraction comparing two sides of a right triangle in relation to a specific angle
- **Angle of reference**: The angle we're using to determine which sides are "opposite," "adjacent," and "hypotenuse"
- **Opposite side**: The side across from the angle of reference (not touching it)
- **Adjacent side**: The side next to the angle of reference that is NOT the hypotenuse
- **Hypotenuse**: The side opposite the right angle (always the longest)

### Why This Matters
Trigonometry solves the problem: "I know one angle and one side length. How do I find the other sides?" This is incredibly useful in real-world applications like surveying land, building structures, and navigation.

### The Core Principle: Similar Triangles
Consider all right triangles with a 35° angle. Even though they're different sizes, they all have the SAME shape. This means:
- In all of them, the ratio of (opposite side) ÷ (hypotenuse) is identical
- In all of them, the ratio of (adjacent side) ÷ (hypotenuse) is identical
- And so on...

This is why we can make a table of trig ratios once and use it for ALL triangles.

### Identifying the Three Sides Relative to an Angle

**Step 1:** Locate the angle of reference in the triangle.

**Step 2:** Identify the three sides:
- **Hypotenuse**: Always opposite the right angle (always the longest)
- **Opposite side**: The side across from your angle of reference
- **Adjacent side**: The side next to your angle of reference (NOT the hypotenuse)

**Step 3:** Use these identifications in your trigonometric ratios.

### Worked Example: Identifying Sides
In a right triangle, one acute angle is 40°. Label the sides relative to this 40° angle.

**Solution:**
- The hypotenuse is opposite the right angle (it doesn't change based on which angle we're looking at)
- The **opposite** side is the side across from the 40° angle (it doesn't touch the 40° angle)
- The **adjacent** side is the side next to the 40° angle that is NOT the hypotenuse
- [Visual: If we mark the right angle, then mark 40° at another vertex, the side opposite 40° is clearly across from it, and the remaining leg is adjacent to 40°]

### Common Mistakes
- **Mistake 1**: Confusing opposite and adjacent. Remember: opposite is across from the angle; adjacent is next to it.
- **Mistake 2**: Including the hypotenuse as a choice for opposite or adjacent. The hypotenuse is always its own thing.
- **Mistake 3**: Mixing up which angle is the angle of reference. The problem will tell you which angle to use; be careful.

### Exam Tips
- Always draw a diagram and label the angle of reference clearly.
- Use different colors or symbols to mark opposite, adjacent, and hypotenuse.
- The side names change if you switch angles, but the hypotenuse never changes.

---

## SOH-CAH-TOA: The Three Main Ratios

### The Mnemonic
**SOH-CAH-TOA** is the most important memory device in trigonometry. It tells you the three basic trigonometric ratios:

| Mnemonic | Stands For | Means |
|----------|-----------|-------|
| **SOH** | **S**ine = **O**pposite/**H**ypotenuse | $\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}$ |
| **CAH** | **C**osine = **A**djacent/**H**ypotenuse | $\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}$ |
| **TOA** | **T**angent = **O**pposite/**A**djacent | $\tan \theta = \frac{\text{opposite}}{\text{adjacent}}$ |

### Understanding Each Ratio

#### Sine (sin)
**Plain English:** Sine compares the opposite side to the hypotenuse. It tells you what fraction of the hypotenuse the opposite side is.

$$\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}$$

#### Cosine (cos)
**Plain English:** Cosine compares the adjacent side to the hypotenuse. It tells you what fraction of the hypotenuse the adjacent side is.

$$\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}$$

#### Tangent (tan)
**Plain English:** Tangent compares the opposite side to the adjacent side. It's the only ratio that doesn't involve the hypotenuse.

$$\tan \theta = \frac{\text{opposite}}{\text{adjacent}}$$

### The Angle Symbol
In all three ratios, *θ* (theta, a Greek letter) represents the angle we're using as our reference. You can read "$\sin \theta$" as "sine of theta" or "sine of angle theta."

### Worked Example 1: Writing Ratios from a Diagram
In a right triangle, angle A is acute. The side opposite A is 3, the side adjacent to A is 4, and the hypotenuse is 5.

Write sin A, cos A, and tan A.

**Solution:**
- For angle A: opposite = 3, adjacent = 4, hypotenuse = 5
- $\sin A = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{3}{5}$
- $\cos A = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{4}{5}$
- $\tan A = \frac{\text{opposite}}{\text{adjacent}} = \frac{3}{4}$

### Worked Example 2: Evaluating Trigonometric Ratios
In the same right triangle (opposite = 3, adjacent = 4, hypotenuse = 5), also write sin B, cos B, and tan B for angle B (the other acute angle).

**Solution:**
- Now angle B is at a different vertex, so the opposite and adjacent sides SWITCH
- For angle B:
  - The opposite side is now 4 (it was adjacent to A)
  - The adjacent side is now 3 (it was opposite to A)
  - The hypotenuse is still 5
- $\sin B = \frac{4}{5}$
- $\cos B = \frac{3}{5}$
- $\tan B = \frac{4}{3}$

**Important observation**: Notice that $\sin A = \frac{3}{5} = \cos B$ and $\cos A = \frac{4}{5} = \sin B$. This is not a coincidence! (More on this in the cofunctions section.)

### Worked Example 3: Using a Calculator
A right triangle has an angle of 35° and the hypotenuse is 10 cm. The side opposite the 35° angle is unknown. Find it.

**Solution:**
- Angle of reference: 35°
- Known: hypotenuse = 10
- Unknown: opposite side
- Choose the ratio that relates opposite and hypotenuse: **sine**
- $\sin 35° = \frac{\text{opposite}}{10}$
- From a calculator: $\sin 35° \approx 0.5736$
- $0.5736 = \frac{\text{opposite}}{10}$
- opposite = $0.5736 \times 10 = 5.736$ cm
- **Answer: The opposite side is approximately 5.74 cm**

### Common Mistakes
- **Mistake 1**: Forgetting that opposite and adjacent change based on which angle you're looking at. The hypotenuse NEVER changes.
- **Mistake 2**: Mixing up the fractions. Use the mnemonic SOH-CAH-TOA to avoid this.
- **Mistake 3**: Using the wrong ratio. If you need the opposite and hypotenuse, use sine—not tangent (which doesn't involve the hypotenuse).

### Exam Tips
- Write SOH-CAH-TOA at the top of your test page before you start.
- Always identify the angle of reference first.
- Circle or highlight which side is opposite, which is adjacent, and where the hypotenuse is.
- When choosing a ratio, ask: "Which two of the three sides do I know or need?" Then pick the ratio that uses exactly those two.

---

## Cofunctions and Complementary Angles

### What Cofunctions Are
Two trigonometric ratios are **cofunctions** if one equals the other applied to the complementary angle. "Co" means "together" or "paired."

### Key Vocabulary
- **Complementary angles**: Two angles that add up to 90°
- **Cofunction pair**: Two trig ratios that have this special relationship
- **Cofunction identity**: A formula showing this relationship

### The Cofunction Identities
For any acute angle *A*:

$$\sin A = \cos(90° - A)$$
$$\cos A = \sin(90° - A)$$
$$\tan A = \cot(90° - A)$$

In words:
- The sine of an angle equals the cosine of its complement
- The cosine of an angle equals the sine of its complement
- The tangent of an angle equals the cotangent of its complement

### Why This Happens

Remember our earlier observation in Example 2 under "SOH-CAH-TOA"? When we switched from angle A to angle B in the same right triangle, sine and cosine swapped. Here's why:

In any right triangle:
- Angles A and B are complementary (they add to 90°)
- The side opposite A is adjacent to B
- The side adjacent to A is opposite to B
- The hypotenuse is the same for both

Therefore:
- $\sin A = \frac{\text{opp to A}}{\text{hyp}} = \frac{\text{adj to B}}{\text{hyp}} = \cos B = \cos(90° - A)$

### Worked Example 1: Using Cofunction Identity
If $\sin 25° = 0.4226$, find $\cos 65°$ without a calculator.

**Solution:**
- Notice: 25° + 65° = 90° (they're complementary)
- Using the cofunction identity: $\sin 25° = \cos(90° - 25°) = \cos 65°$
- Therefore: $\cos 65° = 0.4226$
- **Answer: 0.4226**

### Worked Example 2: Rewriting Using Cofunctions
Rewrite $\tan 42°$ using a sine and cosine of a complementary angle.

**Solution:**
- The complement of 42° is 90° - 42° = 48°
- Using the cofunction identity: $\tan 42° = \cot 48°$
- We can also write: $\cot 48° = \frac{\cos 48°}{\sin 48°}$
- Therefore: $\tan 42° = \frac{\cos 48°}{\sin 48°}$
- **Answer: $\tan 42° = \cot 48° = \frac{\cos 48°}{\sin 48°}$**

### Worked Example 3: Solving Using Cofunctions
Solve for *x*: $\sin(3x) = \cos(x + 20°)$

**Solution:**
- Recognize that if $\sin A = \cos B$, then A and B must be complementary
- So: $3x + (x + 20°) = 90°$
- $4x + 20° = 90°$
- $4x = 70°$
- $x = 17.5°$
- **Answer: x = 17.5°**

### Common Mistakes
- **Mistake 1**: Forgetting that angles must be complementary (sum to 90°). Don't confuse this with other angle relationships.
- **Mistake 2**: Using supplementary angles (sum to 180°) instead. Complementary = 90°; Supplementary = 180°.
- **Mistake 3**: Misapplying the identity. $\sin 30°$ is NOT equal to $\sin 60°$ just because they're related—but $\sin 30° = \cos 60°$ because they're complementary.

### Exam Tips
- When you see two trig ratios of different types (sin with cos, tan with cot), check if the angles are complementary.
- This concept often appears in equation-solving problems.
- Memorize the cofunction identities; they're tested frequently.

---

## Finding Missing Sides Using Trig Ratios

### When to Use This Method
When you know:
- One angle (other than the right angle)
- One side length (any of the three: opposite, adjacent, or hypotenuse)

And you need to find another side length.

### The Process

**Step 1:** Identify the angle of reference and label all three sides relative to it.

**Step 2:** Determine which sides you know and which you need using the labels: opposite, adjacent, hypotenuse.

**Step 3:** Choose the trigonometric ratio (sin, cos, or tan) that relates your known side to your unknown side.

**Step 4:** Write the ratio equation and solve for the unknown.

### Worked Example 1: Finding the Opposite Side
A right triangle has an acute angle of 32° and the adjacent side is 15 cm. Find the opposite side.

**Solution:**
- Angle of reference: 32°
- Known side: adjacent = 15 cm
- Unknown side: opposite = ?
- Choose ratio: We know adjacent and need opposite. Use **tangent** (TOA).
- Write the equation: $\tan 32° = \frac{\text{opposite}}{15}$
- Solve: opposite = $15 \times \tan 32°$
- From a calculator: $\tan 32° \approx 0.6249$
- opposite = $15 \times 0.6249 \approx 9.37$ cm
- **Answer: The opposite side is approximately 9.37 cm**

### Worked Example 2: Finding the Adjacent Side
A right triangle has an acute angle of 50° and the hypotenuse is 20 feet. Find the adjacent side.

**Solution:**
- Angle of reference: 50°
- Known side: hypotenuse = 20 feet
- Unknown side: adjacent = ?
- Choose ratio: We know hypotenuse and need adjacent. Use **cosine** (CAH).
- Write the equation: $\cos 50° = \frac{\text{adjacent}}{20}$
- Solve: adjacent = $20 \times \cos 50°$
- From a calculator: $\cos 50° \approx 0.6428$
- adjacent = $20 \times 0.6428 \approx 12.86$ feet
- **Answer: The adjacent side is approximately 12.86 feet**

### Worked Example 3: Finding the Hypotenuse
A right triangle has an acute angle of 28° and the opposite side is 8 inches. Find the hypotenuse.

**Solution:**
- Angle of reference: 28°
- Known side: opposite = 8 inches
- Unknown side: hypotenuse = ?
- Choose ratio: We know opposite and need hypotenuse. Use **sine** (SOH).
- Write the equation: $\sin 28° = \frac{8}{\text{hypotenuse}}$
- Solve: $\text{hypotenuse} = \frac{8}{\sin 28°}$
- From a calculator: $\sin 28° \approx 0.4695$
- $\text{hypotenuse} = \frac{8}{0.4695} \approx 17.05$ inches
- **Answer: The hypotenuse is approximately 17.05 inches**

### Worked Example 4: Two Unknowns
A right triangle has an acute angle of 55° and the hypotenuse is 12 cm. Find both legs.

**Solution:**
- **For the opposite side:**
  - $\sin 55° = \frac{\text{opposite}}{12}$
  - opposite = $12 \times \sin 55° = 12 \times 0.8192 \approx 9.83$ cm

- **For the adjacent side:**
  - $\cos 55° = \frac{\text{adjacent}}{12}$
  - adjacent = $12 \times \cos 55° = 12 \times 0.5736 \approx 6.88$ cm

- **Answer: One leg is approximately 9.83 cm, the other is approximately 6.88 cm**

### Common Mistakes
- **Mistake 1**: Choosing the wrong trig ratio. Remember SOH-CAH-TOA: if you have opposite and hypotenuse, it MUST be sine (not cosine or tangent).
- **Mistake 2**: Multiplying when you should divide (or vice versa). If the unknown is in the numerator, multiply. If it's in the denominator, divide.
- **Mistake 3**: Forgetting to identify which side is which relative to the angle. Draw a diagram every time.
- **Mistake 4**: Using the wrong angle. Make sure you're using the acute angle that's given, not 90° or another angle.

### Exam Tips
- Always draw and label the triangle, even if a diagram is provided.
- Write out the trig equation before solving; this prevents algebraic mistakes.
- Check reasonableness: the hypotenuse should always be longer than either leg.
- Use a calculator with trigonometric functions; make sure it's in degree mode (not radian mode).

---

## Finding Missing Angles Using Inverse Trig

### What Inverse Trig Functions Do
The **inverse trigonometric functions** (also called "arc functions") reverse what regular trig functions do.

- Regular trig: You input an angle and get a ratio.
- Inverse trig: You input a ratio and get an angle.

### Key Vocabulary
- **Inverse sine** (written as $\sin^{-1}$ or $\arcsin$): Finds the angle when you know sine
- **Inverse cosine** (written as $\cos^{-1}$ or $\arccos$): Finds the angle when you know cosine
- **Inverse tangent** (written as $\tan^{-1}$ or $\arctan$): Finds the angle when you know tangent

### Important Note on Notation
The $^{-1}$ does NOT mean a reciprocal or "one over." It means "inverse function." So $\sin^{-1}(0.5)$ does NOT mean $\frac{1}{\sin(0.5)}$—it means "the angle whose sine is 0.5."

### The Three Inverse Functions

$$\sin^{-1}\left(\frac{\text{opposite}}{\text{hypotenuse}}\right) = \theta$$

$$\cos^{-1}\left(\frac{\text{adjacent}}{\text{hypotenuse}}\right) = \theta$$

$$\tan^{-1}\left(\frac{\text{opposite}}{\text{adjacent}}\right) = \theta$$

### When to Use Each

| You Know | Find | Use |
|----------|------|-----|
| Opposite and Hypotenuse | Angle | $\sin^{-1}$ |
| Adjacent and Hypotenuse | Angle | $\cos^{-1}$ |
| Opposite and Adjacent | Angle | $\tan^{-1}$ |

### Worked Example 1: Using Inverse Sine
In a right triangle, the opposite side is 7 and the hypotenuse is 12. Find the angle.

**Solution:**
- Known: opposite = 7, hypotenuse = 12
- Unknown: angle = ?
- Use inverse sine: $\sin^{-1}\left(\frac{7}{12}\right) = \text{angle}$
- $\sin^{-1}(0.5833) \approx 35.69°$
- **Answer: The angle is approximately 35.69°** (or 35.7°)

### Worked Example 2: Using Inverse Cosine
In a right triangle, the adjacent side is 10 and the hypotenuse is 15. Find the angle.

**Solution:**
- Known: adjacent = 10, hypotenuse = 15
- Unknown: angle = ?
- Use inverse cosine: $\cos^{-1}\left(\frac{10}{15}\right) = \text{angle}$
- Simplify: $\cos^{-1}\left(\frac{2}{3}\right)$
- $\cos^{-1}(0.6667) \approx 48.19°$
- **Answer: The angle is approximately 48.19°** (or 48.2°)

### Worked Example 3: Using Inverse Tangent
In a right triangle, the opposite side is 6 and the adjacent side is 8. Find the angle.

**Solution:**
- Known: opposite = 6, adjacent = 8
- Unknown: angle = ?
- Use inverse tangent: $\tan^{-1}\left(\frac{6}{8}\right) = \text{angle}$
- Simplify: $\tan^{-1}\left(\frac{3}{4}\right) = \tan^{-1}(0.75)$
- $\tan^{-1}(0.75) \approx 36.87°$
- **Answer: The angle is approximately 36.87°** (or 36.9°)

### Finding Both Acute Angles
Since the two acute angles in a right triangle are complementary:

If you find one angle is 35°, the other must be 90° - 35° = 55°.

You don't need to use inverse trig twice; find one angle, subtract from 90°.

### Worked Example 4: Complete Triangle Solution
A right triangle has legs of 9 cm and 12 cm. Find both acute angles.

**Solution:**
- Known: opposite = 9 (relative to one angle), adjacent = 12
- **For the first angle:**
  - $\tan^{-1}\left(\frac{9}{12}\right) = \tan^{-1}(0.75) \approx 36.87°$

- **For the second angle:**
  - $90° - 36.87° = 53.13°$

- **Answer: The two acute angles are approximately 36.87° and 53.13°**

### Common Mistakes
- **Mistake 1**: Forgetting that $\sin^{-1}$ is an inverse function, not a reciprocal. $\sin^{-1}(0.5) = 30°$, not $\frac{1}{\sin(0.5°)}$.
- **Mistake 2**: Using the wrong inverse function. If you have opposite and adjacent, you MUST use tangent, not sine or cosine.
- **Mistake 3**: Forgetting to simplify ratios before entering into a calculator. While it doesn't change the answer, it's good practice.
- **Mistake 4**: Not checking that your calculator is in degree mode. If it's in radian mode, you'll get a completely wrong answer.

### Exam Tips
- Write out the inverse trig expression before evaluating: $\sin^{-1}(7/12)$ not just "7÷12."
- Always check: Is your answer reasonable for an acute angle? (It should be between 0° and 90°.)
- These questions often appear after finding sides, so be prepared to use both skills in sequence.

---

## Angles of Elevation and Depression

### What They Are (Plain English)
**Angles of elevation and depression** describe the angle between the horizontal and your line of sight when you're looking up or down at an object. These angles make trigonometry useful in real-world situations like surveying land, calculating building heights, or finding distances.

### Key Vocabulary
- **Angle of elevation**: The angle between the horizontal and your line of sight when looking UP at something
- **Angle of depression**: The angle between the horizontal and your line of sight when looking DOWN at something
- **Horizontal line**: An imaginary line parallel to the ground at your eye level
- **Line of sight**: An imaginary line from your eye to the object you're looking at

### The Key Insight
When one person looks up at an angle of elevation *α*, and another person at the object looks down at the same angle *α*, those angles are **equal** (alternate interior angles with the horizontal as a transversal). This is crucial for solving these problems.

### Setting Up the Problem

**Step 1:** Draw a diagram with:
- The observer's position
- The object being observed
- A horizontal line through the observer's eye level
- The line of sight from observer to object
- The angle of elevation or depression

**Step 2:** Identify the right triangle:
- The horizontal line and vertical distance form a right angle
- One leg is the horizontal distance
- One leg is the vertical distance
- The hypotenuse is part of the line of sight

**Step 3:** Label the triangle:
- Identify which side is opposite, adjacent, and hypotenuse relative to the angle
- Identify which sides are known and which are unknown

**Step 4:** Use trigonometric ratios or inverse trig to solve.

### Worked Example 1: Angle of Elevation to Find Height
You stand 50 feet away from the base of a building and look up at the top at an angle of elevation of 35°. How tall is the building?

**Solution:**
- Your position: ground level, 50 feet from the building
- Object: top of the building
- Angle of elevation: 35° (angle up from horizontal)

**Diagram setup:**
- Horizontal distance (along ground): 50 feet = adjacent side (relative to your 35° angle)
- Vertical distance (up the building): height = opposite side = unknown
- Angle: 35°

**Using trigonometry:**
- $\tan 35° = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{height}}{50}$
- height = $50 \times \tan 35°$
- height = $50 \times 0.7002 \approx 35.01$ feet
- **Answer: The building is approximately 35 feet tall**

### Worked Example 2: Angle of Depression to Find Distance
From the top of a 200-meter tall building, you look down at an object on the ground at an angle of depression of 28°. How far away is the object from the base of the building?

**Solution:**
- Your position: top of the 200-meter building
- Object: ground level
- Angle of depression: 28° (angle down from horizontal)

**Diagram setup:**
- Vertical distance (building height): 200 meters = opposite side (relative to your 28° angle, measured from the horizontal looking down)
- Horizontal distance (ground): unknown = adjacent side
- Angle: 28°

**Using trigonometry:**
- The angle of depression equals the angle of elevation from the object looking back (alternate interior angles)
- $\tan 28° = \frac{\text{opposite}}{\text{adjacent}} = \frac{200}{\text{distance}}$
- distance = $\frac{200}{\tan 28°}$
- distance = $\frac{200}{0.5317} \approx 376.28$ meters
- **Answer: The object is approximately 376 meters away from the building**

### Worked Example 3: Two-Stage Problem with Angles
From point A on the ground, you look up at the top of a tower at an angle of elevation of 25°. If you move 30 meters closer (to point B), the angle of elevation becomes 40°. Find the height of the tower.

**Solution:**
This requires setting up two equations. Let h = height of tower, and d = distance from point B to the tower.

**From point B (closer):**
- $\tan 40° = \frac{h}{d}$
- $h = d \tan 40°$ ... (equation 1)

**From point A (farther):**
- Distance from A = d + 30
- $\tan 25° = \frac{h}{d+30}$
- $h = (d+30) \tan 25°$ ... (equation 2)

**Solve by setting equations equal:**
- $d \tan 40° = (d+30) \tan 25°$
- $d(0.8391) = (d+30)(0.4663)$
- $0.8391d = 0.4663d + 13.989$
- $0.3728d = 13.989$
- $d \approx 37.53$ meters

**Find height:**
- $h = d \tan 40° = 37.53 \times 0.8391 \approx 31.49$ meters
- **Answer: The tower is approximately 31.5 meters tall**

### Common Mistakes
- **Mistake 1**: Confusing angle of elevation with angle of depression. Elevation = looking UP; Depression = looking DOWN.
- **Mistake 2**: Using the wrong sides in the trig ratio. The angle of elevation/depression is measured from the horizontal, so think carefully about which side is opposite and which is adjacent.
- **Mistake 3**: Forgetting that angle of depression from the observer equals angle of elevation from the object (alternate interior angles). This creates a right triangle.
- **Mistake 4**: Misidentifying the triangle. Make sure you have a right angle before using trigonometry.

### Exam Tips
- **Always draw a diagram**, even if the problem seems straightforward. Diagrams prevent mistakes.
- Mark the angle of elevation or depression clearly on your diagram.
- When the problem says "angle of elevation of 25°," that angle is measured UP from the horizontal—not from the vertical.
- Two-stage problems often require you to write multiple equations and solve a system.
- These are among the most commonly tested applications of trigonometry, so practice them thoroughly.

---

## Area of a Triangle Using Sine

### Why We Need This Formula
The usual triangle area formula is $A = \frac{1}{2} \times \text{base} \times \text{height}$. But sometimes we don't know the height. When we know two sides and the **included angle** (the angle between them), we can find the area using sine.

### Key Vocabulary
- **Included angle**: The angle between two known sides of a triangle
- **Non-right triangle**: A triangle that doesn't have a 90° angle (also called oblique)

### The Formula

$$A = \frac{1}{2}ab\sin C$$

Where:
- *a* and *b* are two sides of the triangle
- *C* is the included angle (the angle between sides *a* and *b*)
- The angle must be in degrees (or radians, but we'll use degrees)

### Why This Works
This formula comes from the fact that when you drop a perpendicular from one vertex to the opposite side, the height equals $b \sin C$ (or $a \sin C$, depending on which perpendicular you draw). Substituting this into the regular area formula gives us this sine formula.

### When to Use This Formula
Use this when you know:
- Two sides of a triangle
- The **included angle** (the angle between those two sides)

You want to find the area (you cannot find area with three sides unless you also know an angle, or you have enough information to find an angle).

### Worked Example 1: Simple Area Calculation
A triangle has sides 8 cm and 12 cm with an included angle of 60°. Find the area.

**Solution:**
- Known: *a* = 8, *b* = 12, *C* = 60°
- Use formula: $A = \frac{1}{2}ab\sin C$
- $A = \frac{1}{2} \times 8 \times 12 \times \sin 60°$
- $A = \frac{1}{2} \times 8 \times 12 \times 0.8660$
- $A = 48 \times 0.8660 = 41.57$ cm²
- **Answer: The area is approximately 41.57 cm²**

### Worked Example 2: Finding Area of a Right Triangle
A right triangle has legs of 5 feet and 9 feet. Find the area using the sine formula.

**Solution:**
- The included angle between the two legs is 90°
- Known: *a* = 5, *b* = 9, *C* = 90°
- Use formula: $A = \frac{1}{2}ab\sin C$
- $A = \frac{1}{2} \times 5 \times 9 \times \sin 90°$
- $A = \frac{1}{2} \times 5 \times 9 \times 1$
- $A = 22.5$ feet²
- **Answer: The area is 22.5 feet²**

Note: This matches the usual $\frac{1}{2} \times 5 \times 9 = 22.5$, confirming our formula!

### Worked Example 3: Finding Area When You Must Find the Angle First
A triangle has sides 10 inches and 14 inches. The angle opposite the side of 10 inches is 35°. Find the area.

**Solution:**
- This is trickier because the 35° angle is NOT the included angle
- We must find the included angle using the fact that this angle is opposite the 10-inch side
- Actually, for this problem, we'd need more information to find the included angle
- **Better approach for this problem**: Use the Law of Sines (see later section) or determine if we have enough information

Let me revise this example:

### Worked Example 3 (Revised): Using the Sine Formula
A triangle has sides 7 cm and 11 cm, and the angle between them is 42°. Find the area.

**Solution:**
- Known: *a* = 7, *b* = 11, *C* = 42° (included angle)
- Use formula: $A = \frac{1}{2}ab\sin C$
- $A = \frac{1}{2} \times 7 \times 11 \times \sin 42°$
- $A = \frac{1}{2} \times 7 \times 11 \times 0.6691$
- $A = 38.5 \times 0.6691 \approx 25.76$ cm²
- **Answer: The area is approximately 25.76 cm²**

### Common Mistakes
- **Mistake 1**: Using a non-included angle. The angle MUST be between the two sides you're using. If the angle is opposite one of the sides, it's not the included angle.
- **Mistake 2**: Using the wrong angle measure. Make sure you're using degrees, not radians, unless the problem specifically asks for radians.
- **Mistake 3**: Forgetting to use $\frac{1}{2}$. Always include the one-half in the formula.
- **Mistake 4**: Confusing this with finding area of a right triangle using the basic formula. Both methods work for right triangles, but the sine formula is more general.

### Exam Tips
- Identify the included angle carefully; it's the angle **between** the two sides, not opposite to one of them.
- This formula is particularly useful in physics and engineering applications.
- Always double-check that the angle you're using is included.

---

## Law of Sines

### What It Is
The **Law of Sines** is a relationship between the sides and angles of **any triangle** (not just right triangles). It states that the ratio of a side to the sine of its opposite angle is constant for all three sides and angles.

### Key Vocabulary
- **Opposite**: In a triangle, the side opposite an angle is the side that doesn't touch that angle
- **Proportional**: Having a constant ratio relationship

### The Formula

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

Where:
- *a*, *b*, *c* are the side lengths
- *A*, *B*, *C* are the opposite angles (angle A is opposite side a, etc.)
- All angles are in degrees or all in radians (be consistent)

### Understanding the Formula
The formula says: "For any triangle, if you divide a side by the sine of its opposite angle, you get the same number every time." This works because of the proportional relationship between sides and their opposite angles.

### When to Use the Law of Sines

Use this law when you know:
- **Case 1 (AAS)**: Two angles and a side opposite one of them
- **Case 2 (ASA)**: Two angles and the side between them (the included side)

In both cases, once you know two angles, you automatically know the third angle (since angles sum to 180°).

Do NOT use the Law of Sines when you know SSS or SAS—use the Law of Cosines instead.

### Solving with the Law of Sines

**Step 1:** If you're given two angles, find the third angle: third angle = 180° - angle 1 - angle 2.

**Step 2:** Identify which sides and angles you know.

**Step 3:** Write the Law of Sines using the known and unknown quantities.

**Step 4:** Cross-multiply and solve.

### Worked Example 1: AAS Case (Angle-Angle-Side)
A triangle has angles 40° and 65°. The side opposite the 40° angle is 10 cm. Find the side opposite the 65° angle.

**Solution:**
- Known angles: 40° and 65°
- Third angle: 180° - 40° - 65° = 75°
- Known side: a = 10 cm (opposite the 40° angle)
- Unknown side: b = ? (opposite the 65° angle)

**Using Law of Sines:**
$$\frac{a}{\sin A} = \frac{b}{\sin B}$$
$$\frac{10}{\sin 40°} = \frac{b}{\sin 65°}$$

**Cross-multiply:**
$$b \times \sin 40° = 10 \times \sin 65°$$
$$b = \frac{10 \times \sin 65°}{\sin 40°}$$
$$b = \frac{10 \times 0.9063}{0.6428} = \frac{9.063}{0.6428} \approx 14.09 \text{ cm}$$

- **Answer: The side opposite 65° is approximately 14.09 cm**

### Worked Example 2: ASA Case (Angle-Side-Angle)
A triangle has angles 30° and 80° with the side between them equal to 12 inches. Find the other two sides.

**Solution:**
- Known angles: 30° and 80° (with the 12-inch side between them)
- Third angle: 180° - 30° - 80° = 70°
- The side between the two angles is opposite the third angle
- So: side opposite 70° = 12 inches (given)
- Unknown: sides opposite 30° and 80°

**Find the side opposite 30°:**
$$\frac{a}{\sin 30°} = \frac{12}{\sin 70°}$$
$$a = \frac{12 \times \sin 30°}{\sin 70°} = \frac{12 \times 0.5}{0.9397} = \frac{6}{0.9397} \approx 6.38 \text{ inches}$$

**Find the side opposite 80°:**
$$\frac{b}{\sin 80°} = \frac{12}{\sin 70°}$$
$$b = \frac{12 \times \sin 80°}{\sin 70°} = \frac{12 \times 0.9848}{0.9397} = \frac{11.818}{0.9397} \approx 12.58 \text{ inches}$$

- **Answer: The sides are approximately 6.38 inches and 12.58 inches**

### Worked Example 3: Finding an Angle (Inverse Case)
A triangle has sides 8 and 10 with an angle of 50° opposite the side of length 8. Find the angle opposite the side of length 10.

**Solution:**
- Known: side a = 8 (opposite angle A = 50°), side b = 10 (opposite angle B = ?)
- Use Law of Sines:
$$\frac{8}{\sin 50°} = \frac{10}{\sin B}$$
$$\sin B = \frac{10 \times \sin 50°}{8} = \frac{10 \times 0.7660}{8} = \frac{7.660}{8} = 0.9575$$
$$B = \sin^{-1}(0.9575) \approx 73.28°$$

- **Answer: The angle opposite the side of length 10 is approximately 73.28°**

**Important note:** Since sin(73.28°) ≈ sin(106.72°), there could be a second solution. We'd need to check if 180° - 50° - 73.28° = 56.72° works geometrically. (It does in this case, but the first solution is typically the expected answer unless the ambiguous case is specifically mentioned.)

### The Ambiguous Case (SSA)
When you know two sides and an angle opposite one of them (SSA), there might be **zero, one, or two valid triangles**. This is called the ambiguous case. Most textbooks avoid this, but be aware it exists.

### Common Mistakes
- **Mistake 1**: Confusing which side is opposite which angle. Double-check: angle A is opposite side a, angle B is opposite side b, etc.
- **Mistake 2**: Using the Law of Sines when you should use the Law of Cosines. If you know SSS or SAS, you MUST use the Law of Cosines, not the Law of Sines.
- **Mistake 3**: Forgetting to find the third angle when given two angles and wanting to find a third side.
- **Mistake 4**: Mixing degrees and radians. Stay consistent throughout the problem.

### Exam Tips
- Always label sides with lowercase letters (a, b, c) and angles with uppercase letters (A, B, C), with angle A opposite side a, etc.
- The Law of Sines is specifically for AAS and ASA cases. If you have two angles, you can always find all sides and the third angle using this law.
- Check your answer: the longest side should be opposite the largest angle.

---

## Law of Cosines

### What It Is
The **Law of Cosines** is a relationship that generalizes the Pythagorean Theorem to all triangles (not just right triangles). It relates three sides and one angle.

### Key Vocabulary
- **Included angle**: The angle between two known sides
- **Generalization**: A rule that applies to more cases than the original rule (e.g., the Law of Cosines applies to any triangle, while the Pythagorean Theorem only applies to right triangles)

### The Formula

$$c^2 = a^2 + b^2 - 2ab\cos C$$

Where:
- *a* and *b* are two sides
- *C* is the **included angle** (between sides a and b)
- *c* is the side opposite angle C

**Alternative forms** (rotate letters):
$$a^2 = b^2 + c^2 - 2bc\cos A$$
$$b^2 = a^2 + c^2 - 2ac\cos B$$

### How It Relates to the Pythagorean Theorem
If angle *C* = 90°, then $\cos 90° = 0$, and the formula becomes:
$$c^2 = a^2 + b^2 - 2ab(0) = a^2 + b^2$$

This is exactly the Pythagorean Theorem! So the Law of Cosines is the Pythagorean Theorem generalized.

### When to Use the Law of Cosines

Use this law when you know:
- **Case 1 (SAS)**: Two sides and the included angle
- **Case 2 (SSS)**: All three sides (usually to find an angle)

Do NOT use the Law of Cosines when you have AAS or ASA—use the Law of Sines instead.

### Solving with the Law of Cosines

**For Case 1 (SAS - finding a side):**

**Step 1:** Identify the two known sides and the included angle.

**Step 2:** Write the Law of Cosines with the unknown side on the left: $c^2 = a^2 + b^2 - 2ab\cos C$

**Step 3:** Substitute and solve.

**For Case 2 (SSS - finding an angle):**

**Step 1:** Rearrange to solve for the cosine of the angle: $\cos C = \frac{a^2 + b^2 - c^2}{2ab}$

**Step 2:** Substitute and solve.

**Step 3:** Use inverse cosine to find the angle: $C = \cos^{-1}(\cos C)$

### Worked Example 1: SAS Case (Finding a Side)
A triangle has sides 7 cm and 9 cm with an included angle of 55°. Find the third side.

**Solution:**
- Known: *a* = 7, *b* = 9, *C* = 55°
- Unknown: *c* (opposite the 55° angle)

**Using Law of Cosines:**
$$c^2 = a^2 + b^2 - 2ab\cos C$$
$$c^2 = 7^2 + 9^2 - 2(7)(9)\cos 55°$$
$$c^2 = 49 + 81 - 126\cos 55°$$
$$c^2 = 130 - 126(0.5736)$$
$$c^2 = 130 - 72.27 = 57.73$$
$$c = \sqrt{57.73} \approx 7.60 \text{ cm}$$

- **Answer: The third side is approximately 7.60 cm**

### Worked Example 2: SSS Case (Finding an Angle)
A triangle has sides 5, 7, and 8. Find the angle opposite the side of length 7.

**Solution:**
- Known: *a* = 5, *b* = 8, *c* = 7 (opposite angle C)
- Unknown: angle *C*

**Rearrange the Law of Cosines:**
$$\cos C = \frac{a^2 + b^2 - c^2}{2ab}$$
$$\cos C = \frac{5^2 + 8^2 - 7^2}{2(5)(8)}$$
$$\cos C = \frac{25 + 64 - 49}{80} = \frac{40}{80} = 0.5$$
$$C = \cos^{-1}(0.5) = 60°$$

- **Answer: The angle opposite the side of length 7 is 60°**

### Worked Example 3: Complete Triangle with SAS
A triangle has two sides of 10 feet and 14 feet with an included angle of 68°. Find all missing parts (the third side and the other two angles).

**Solution:**

**Part 1: Find the third side (using Law of Cosines):**
$$c^2 = 10^2 + 14^2 - 2(10)(14)\cos 68°$$
$$c^2 = 100 + 196 - 280\cos 68°$$
$$c^2 = 296 - 280(0.3746) = 296 - 104.89 = 191.11$$
$$c \approx 13.83 \text{ feet}$$

**Part 2: Find one of the other angles (using Law of Sines):**
$$\frac{10}{\sin A} = \frac{13.83}{\sin 68°}$$
$$\sin A = \frac{10 \times \sin 68°}{13.83} = \frac{10 \times 0.9272}{13.83} = \frac{9.272}{13.83} \approx 0.6704$$
$$A \approx \sin^{-1}(0.6704) \approx 42.14°$$

**Part 3: Find the third angle:**
$$B = 180° - 68° - 42.14° = 69.86°$$

- **Answer: Third side ≈ 13.83 feet; Other angles ≈ 42.14° and 69.86°**

### Working with Obtuse Angles
If an angle is obtuse (greater than 90°), its cosine is **negative**. This doesn't cause any problems with the formula; just be careful with your arithmetic.

### Worked Example 4: SAS with an Obtuse Angle
A triangle has sides 6 and 10 with an included angle of 120°. Find the third side.

**Solution:**
- Known: *a* = 6, *b* = 10, *C* = 120°
- Unknown: *c*

$$c^2 = 6^2 + 10^2 - 2(6)(10)\cos 120°$$

Note: $\cos 120° = -0.5$ (negative because 120° is obtuse)

$$c^2 = 36 + 100 - 120(-0.5)$$
$$c^2 = 136 + 60 = 196$$
$$c = \sqrt{196} = 14$$

- **Answer: The third side is 14 units**

### Common Mistakes
- **Mistake 1**: Using the wrong angle. The angle in the formula MUST be the included angle (between the two known sides).
- **Mistake 2**: Forgetting the negative sign in the formula. It's $-2ab\cos C$, not $+2ab\cos C$.
- **Mistake 3**: Mixing up when to use Law of Sines vs. Law of Cosines. Remember: AAS/ASA → Law of Sines; SAS/SSS → Law of Cosines.
- **Mistake 4**: Incorrectly handling negative cosines when the angle is obtuse. Negative cosines are fine; just use them.

### Exam Tips
- Write out the full formula before substituting values; this prevents algebraic errors.
- Check reasonableness: in a SAS case, the unknown side should be "reasonable" relative to the two known sides (roughly between their difference and their sum).
- The Law of Cosines is often used first in a problem, then the Law of Sines can be used to find other angles or sides.
- Practice both the SAS case (finding a side) and SSS case (finding an angle); they require different algebraic manipulations.

---

## Choosing Between Laws and Methods

### Decision Tree

This chart helps you decide which method to use:

**START: What do you know?**

| What You Know | Method to Use | Why |
|---------------|---------------|-----|
| One angle and one side in a right triangle | Trigonometric ratios (sin, cos, tan) | Specific to right triangles |
| Two angles (and therefore third angle) and any side | Law of Sines | The sine rule applies to all triangles with two angles known |
| Two sides and the **included angle** (angle between them) | Law of Cosines | Generalization of Pythagorean Theorem |
| All three sides | Law of Cosines (solve for angle) | Only way to find an angle when you have all sides |
| Two sides and an angle **NOT included** (opposite one side) | Law of Sines (be aware of ambiguous case) | Use this, but check for two possible triangles |
| Three angles only | Not solvable | You need at least one side length |
| One side only | Not solvable | You need at least one angle or another side |

### The Complete Decision Process

**Step 1:** Count what you know (angles and sides).

**Step 2:** Check if it's a right triangle. If yes and you have one acute angle and any side, use trigonometric ratios.

**Step 3:** If you have two angles, use the Law of Sines (even if you only have one side).

**Step 4:** If you have SAS (two sides and included angle), use the Law of Cosines.

**Step 5:** If you have SSS (all three sides), use the Law of Cosines to find angles.

**Step 6:** If you have two sides and an angle NOT between them, use Law of Sines (but watch for the ambiguous case).

### Worked Example: Classification
For each scenario, identify the method to use.

**Scenario A:** Triangle with sides 6, 8, and 10.
- **Classification:** SSS (all three sides known)
- **Method:** Law of Cosines (to find an angle if needed)
- **Note:** Actually, recognize this as a 3-4-5 triple (6-8-10 = 2 × 3-4-5), so it's a right triangle!

**Scenario B:** Triangle with angles 40° and 60°, and side 12 opposite the 40° angle.
- **Classification:** AAS (two angles and a side opposite one)
- **Method:** Law of Sines
- **First:** Find the third angle: 180° - 40° - 60° = 80°

**Scenario C:** Triangle with sides 7 and 9, and an included angle of 45°.
- **Classification:** SAS (two sides and included angle)
- **Method:** Law of Cosines

**Scenario D:** Right triangle with one leg 8 and hypotenuse 15.
- **Classification:** Right triangle with one angle (90°) and partial information
- **Method:** Trigonometric ratios (or Pythagorean Theorem)

**Scenario E:** Triangle with two sides 5 and 8, and an angle 30° opposite the side of 5.
- **Classification:** SSA (two sides and an angle, but the angle is NOT included)
- **Method:** Law of Sines (with caution about ambiguous case)

### Common Mistakes in Choice
- **Mistake 1**: Using Law of Sines when you should use Law of Cosines. If you have SAS, you MUST use Law of Cosines.
- **Mistake 2**: Using trigonometric ratios on a non-right triangle.
- **Mistake 3**: Not realizing you can find the third angle when you know two angles (sum = 180°).
- **Mistake 4**: Forgetting which formula corresponds to which cases.

### Exam Tips for Method Selection
- On exam problems, read carefully to identify exactly what's given.
- Sketch the triangle if not provided; mark the known sides and angles.
- If unsure, write out what you know: "I have sides ____ and ____, and angle ____. Is the angle included?"
- Remember the key phrases:
  - "Two angles and a side" → Law of Sines
  - "Two sides and included angle" → Law of Cosines
  - "Three sides" → Law of Cosines
  - "Right triangle with one angle and one side" → Trig ratios
- When in doubt, Law of Cosines works for more cases, but it's often harder to use, so try Law of Sines first if applicable.

---

## Summary of Key Formulas

### Right Triangles
- **Pythagorean Theorem:** $a^2 + b^2 = c^2$
- **45-45-90 ratio:** $1 : 1 : \sqrt{2}$
- **30-60-90 ratio:** $1 : \sqrt{3} : 2$

### Trigonometric Ratios
- **Sine:** $\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}$
- **Cosine:** $\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}$
- **Tangent:** $\tan \theta = \frac{\text{opposite}}{\text{adjacent}}$

### Inverse Trigonometric Functions
- $\theta = \sin^{-1}(x)$ gives angle when you know sine
- $\theta = \cos^{-1}(x)$ gives angle when you know cosine
- $\theta = \tan^{-1}(x)$ gives angle when you know tangent

### Cofunctions
- $\sin A = \cos(90° - A)$
- $\cos A = \sin(90° - A)$

### Area Formulas
- **Triangle (right):** $A = \frac{1}{2} \times \text{base} \times \text{height}$
- **Triangle (any):** $A = \frac{1}{2}ab\sin C$

### Laws for Non-Right Triangles
- **Law of Sines:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ (use with AAS, ASA)
- **Law of Cosines:** $c^2 = a^2 + b^2 - 2ab\cos C$ (use with SAS, SSS)

---

## Study Tips for Success

1. **Memorize key relationships:**
   - SOH-CAH-TOA (the foundation of trigonometry)
   - The 45-45-90 and 30-60-90 special triangle ratios
   - The Law of Sines and Law of Cosines formulas
   - When to use each method

2. **Always draw diagrams:**
   - Mark right angles
   - Label sides relative to angles (opposite, adjacent, hypotenuse)
   - Mark known and unknown quantities
   - Diagrams prevent more mistakes than any other technique

3. **Show your work:**
   - Write out the formula before substituting
   - Write the substitution step
   - Show the calculation step
   - Write the answer with units

4. **Check your answers:**
   - In right triangles: hypotenuse > either leg
   - In any triangle: largest side is opposite the largest angle
   - In any triangle: sum of angles = 180°
   - Area should be positive and reasonable in size

5. **Practice method selection:**
   - Before solving, identify what you have (AAS? SAS? SSS? Right triangle?)
   - Say aloud which method to use
   - This prevents using the wrong approach

6. **Understand, don't memorize:**
   - Understand WHY sine is opposite/hypotenuse (based on similar triangles)
   - Understand WHY the Law of Cosines reduces to Pythagorean Theorem when C = 90°
   - Understanding transfers to new problems; memorization doesn't

---

## Final Exam Checklist

Before your test, verify you can:

- [ ] State and apply the Pythagorean Theorem
- [ ] Identify Pythagorean triples and their multiples
- [ ] Use the converse to classify triangles (right, acute, obtuse)
- [ ] Use the 45-45-90 triangle ratios correctly
- [ ] Use the 30-60-90 triangle ratios correctly
- [ ] Identify opposite, adjacent, and hypotenuse relative to an angle
- [ ] Apply SOH-CAH-TOA to find missing sides
- [ ] Apply inverse trig to find missing angles
- [ ] Solve angles of elevation and depression problems
- [ ] Calculate triangle area using $A = \frac{1}{2}ab\sin C$
- [ ] Apply the Law of Sines correctly for AAS and ASA cases
- [ ] Apply the Law of Cosines correctly for SAS and SSS cases
- [ ] Choose the correct method based on given information
- [ ] Solve complete triangles (find all sides and angles)
- [ ] Use cofunctions to simplify expressions
- [ ] Verify answers are reasonable

---

## Glossary of Terms

- **Acute angle**: An angle less than 90°
- **Acute triangle**: A triangle with all angles less than 90°
- **Adjacent side**: In a right triangle, the side next to a given angle (not the hypotenuse)
- **Ambiguous case**: When SSA data gives two possible triangles (rare in typical problems)
- **Angle of depression**: The angle downward from horizontal when looking at something below eye level
- **Angle of elevation**: The angle upward from horizontal when looking at something above eye level
- **Complementary angles**: Two angles that sum to 90°
- **Congruent**: Identical in size and shape
- **Hypotenuse**: In a right triangle, the side opposite the right angle (the longest side)
- **Included angle**: The angle between two known sides
- **Leg**: In a right triangle, either of the two sides that form the right angle
- **Obtuse angle**: An angle greater than 90° and less than 180°
- **Obtuse triangle**: A triangle with one angle greater than 90°
- **Opposite side**: In a right triangle, the side across from a given angle
- **Pythagorean triple**: A set of three positive integers satisfying $a^2 + b^2 = c^2$
- **Right angle**: An angle exactly equal to 90°
- **Right triangle**: A triangle with exactly one 90° angle
- **Similar triangles**: Triangles with the same shape but different sizes
- **Trigonometric ratio**: A fraction comparing two sides of a triangle related to an angle
- **Trigonometry**: The study of relationships between angles and sides in triangles

---

**End of Unit 6 Study Notes**

*Remember: Geometry and trigonometry are about understanding relationships. Don't just memorize formulas—understand WHY they work. The more you understand the concepts, the easier the problems become.*
