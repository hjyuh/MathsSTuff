# Unit 5: Similarity — Comprehensive Study Notes
## Honors Geometry Curriculum

---

## Table of Contents
1. [Introduction to Similarity](#introduction-to-similarity)
2. [Scale Factor](#scale-factor)
3. [Dilations](#dilations)
4. [Properties of Similar Figures](#properties-of-similar-figures)
5. [Triangle Similarity Theorems](#triangle-similarity-theorems)
6. [Setting Up and Solving Proportions](#setting-up-and-solving-proportions)
7. [Triangle Proportionality Theorem](#triangle-proportionality-theorem)
8. [Geometric Mean](#geometric-mean)
9. [Perimeters and Areas of Similar Figures](#perimeters-and-areas-of-similar-figures)
10. [Proving the Pythagorean Theorem Using Similarity](#proving-the-pythagorean-theorem-using-similarity)
11. [Real-World Applications](#real-world-applications)
12. [Practice Problems and Solutions](#practice-problems-and-solutions)

---

## Introduction to Similarity

### What Does "Similar" Mean?

In everyday language, "similar" means "kind of the same but not exactly." In geometry, we need to be much more precise.

**Definition:** Two figures are **similar** if they have the same shape but not necessarily the same size. This means:
- All corresponding angles are equal
- All corresponding sides are proportional (the ratio between matching sides is constant)

**Symbol:** We write △ABC ~ △DEF to mean "triangle ABC is similar to triangle DEF"

### Understanding Similarity at Its Core

Imagine you take a photograph and enlarge it for a poster. The enlarged poster looks exactly like the original photograph — just bigger. The angles are the same, and if you measure the sides, they grew by the same factor (like if you doubled the width, you also doubled the height).

That's what similar figures are: one is a scaled version of the other.

### Key Vocabulary

- **Correspondence:** Which vertex (or side) in one figure matches which in the other. Written as △ABC ~ △DEF means A↔D, B↔E, C↔F
- **Corresponding Angles:** Angles in the same relative position in similar figures (these are equal)
- **Corresponding Sides:** Sides in the same relative position in similar figures (the ratios of these are equal)
- **Scale Factor (k):** The ratio of corresponding lengths between two similar figures
- **Dilation:** A transformation that enlarges or reduces a figure by a scale factor

### Core Concept: Three Necessary Conditions for Similarity

For two figures to be similar, ALL three must be true:

1. **Corresponding angles must be equal**
   - In similar triangles, if angle A = angle D, angle B = angle E, and angle C = angle F, that's necessary

2. **Corresponding sides must be proportional**
   - If △ABC ~ △DEF, then AB/DE = BC/EF = CA/FD (each ratio equals the scale factor)

3. **The same constant scale factor applies to all sides**
   - You can't have one pair of sides with ratio 2:1 and another pair with ratio 3:1

### Example: Similar vs. Not Similar

**Similar Figures:**
- Rectangle with dimensions 2 × 3 and rectangle with dimensions 4 × 6 ✓
  - Angles: all 90° in both ✓
  - Sides: 2/4 = 1/2, and 3/6 = 1/2 (same ratio) ✓
  - Scale factor: 2 (the larger is 2 times the smaller)

**NOT Similar:**
- Rectangle with dimensions 2 × 3 and rectangle with dimensions 2 × 4 ✗
  - Angles: all 90° in both ✓
  - Sides: 2/2 = 1, but 3/4 ≠ 1 (different ratios) ✗
  - These are not similar because the sides don't scale by the same factor

---

## Scale Factor

### What Is a Scale Factor?

The **scale factor** is the number you multiply the dimensions of one figure by to get the dimensions of a similar figure.

**Definition:** If figure A ~ figure B with scale factor k, then each length in figure B equals k times the corresponding length in figure A.

In equation form: if side in B corresponds to side in A, then:
$$\text{side in B} = k \times \text{side in A}$$

### Understanding Scale Factor Intuitively

- If k = 2, the new figure is twice as large
- If k = 1/2, the new figure is half the size
- If k = 1, the figures are congruent (identical)
- If k > 1, the figure is enlarged
- If 0 < k < 1, the figure is reduced/shrunk

### How to Find the Scale Factor

The scale factor is always a ratio of corresponding lengths:
$$k = \frac{\text{length in new figure}}{\text{length in original figure}}$$

#### Example 1: Finding Scale Factor from Dimensions

Triangle A has a side of length 6 cm. Triangle B (similar to Triangle A) has the corresponding side of length 9 cm. Find the scale factor from A to B.

**Solution:**
$$k = \frac{\text{new length}}{\text{original length}} = \frac{9}{6} = \frac{3}{2} = 1.5$$

Triangle B is 1.5 times as large as Triangle A.

#### Example 2: Using Scale Factor to Find Unknown Sides

Rectangle ABCD has length 8 and width 5. Rectangle EFGH is similar to ABCD with scale factor k = 2. Find the dimensions of EFGH.

**Solution:**
- Length of EFGH = 2 × 8 = 16
- Width of EFGH = 2 × 5 = 10

Rectangle EFGH has dimensions 16 × 10.

#### Example 3: Finding All Corresponding Sides

△PQR ~ △XYZ with scale factor 3/4. If XY = 12, YZ = 16, and XZ = 20, find the sides of △PQR.

**Solution:**
The scale factor from △PQR to △XYZ is 3/4, which means each side of PQR is 3/4 of the corresponding side in XYZ.

$$PQ = \frac{3}{4} \times XY = \frac{3}{4} \times 12 = 9$$

$$QR = \frac{3}{4} \times YZ = \frac{3}{4} \times 16 = 12$$

$$PR = \frac{3}{4} \times XZ = \frac{3}{4} \times 20 = 15$$

So △PQR has sides 9, 12, and 15.

### Common Mistakes with Scale Factor

**Mistake 1:** Confusing which figure is "new" and which is "original"
- Always write your ratio as (dimension you want) / (dimension you know)
- If you have △ABC with side 10 and △DEF with corresponding side 15, and you want the scale factor FROM ABC TO DEF: k = 15/10 = 1.5

**Mistake 2:** Forgetting that scale factor applies to ALL lengths
- Every single length in the figure (sides, heights, medians, etc.) is multiplied by k
- It's not just some sides that scale

**Exam Tip:** When a problem gives you that figures are similar, IMMEDIATELY write down the equation for scale factor as a ratio. This sets up most problems for success.

---

## Dilations

### What Is a Dilation?

A **dilation** is a transformation (a movement/change) that either enlarges or reduces a figure using a center point and a scale factor.

**Definition:** A dilation with center C and scale factor k transforms every point P in the plane to a new point P' such that:
$$\overrightarrow{CP'} = k \cdot \overrightarrow{CP}$$

In other words: the distance from the center to the new point is k times the distance from the center to the original point, and they're in the same direction.

### Why Dilations Matter

Dilations are one of the main ways we CREATE similar figures. If you dilate any figure (with any scale factor > 0), the result is similar to the original.

### Understanding Dilations Step by Step

**Step 1:** Choose a center point C (this could be the origin, or any point on the plane)

**Step 2:** Identify the scale factor k

**Step 3:** For each point P in the original figure:
- Draw a line from C through P
- Measure the distance from C to P (call it d)
- Mark a new point P' on the same line, at distance k·d from C

**Step 4:** Connect all the new points to form the dilated figure

### Dilation with Center at the Origin

This is the most common type, and it has a simple coordinate rule.

**The Dilation Rule for Center at Origin:**

If you dilate a point (x, y) with center at the origin and scale factor k:
$$(x, y) \rightarrow (kx, ky)$$

**Why this works:**
- Distance from origin to (x,y) is √(x² + y²)
- Distance from origin to (kx, ky) is √((kx)² + (ky)²) = √(k²(x² + y²)) = k√(x² + y²)
- So the new point is exactly k times as far from the origin ✓

#### Example 1: Dilating a Point

Dilate point A(3, 4) with center at the origin and scale factor 2.

**Solution:**
$$(3, 4) \xrightarrow{k=2} (2 \cdot 3, 2 \cdot 4) = (6, 8)$$

The new point A' is at (6, 8).

**Check:**
- Original distance from origin: √(3² + 4²) = √25 = 5
- New distance from origin: √(6² + 8²) = √100 = 10
- 10 = 2 × 5 ✓

#### Example 2: Dilating a Triangle with Center at Origin

Triangle ABC has vertices A(1, 2), B(4, 2), and C(2, 5). Dilate with scale factor 1/2.

**Solution:**
Apply the rule (x, y) → (½x, ½y) to each vertex:

- A(1, 2) → A'(½, 1)
- B(4, 2) → B'(2, 1)
- C(2, 5) → C'(1, 5/2)

The new triangle A'B'C' has vertices at (½, 1), (2, 1), and (1, 5/2).

### Dilation with a Center NOT at the Origin

When the center isn't at the origin, the process is more involved.

**General Dilation Rule (any center C):**

For a point P and center C with scale factor k:
$$P' = C + k(P - C)$$

Or in steps:
1. Translate so C is at the origin: move from P to (P - C)
2. Apply the scale factor: multiply by k to get k(P - C)
3. Translate back: add C to get C + k(P - C)

#### Example 3: Dilating with Center NOT at Origin

Triangle PQR has vertices P(0, 0), Q(4, 0), and R(2, 4). Dilate with center C(2, 2) and scale factor 2.

**Solution:**

For P(0, 0):
- Step 1: P - C = (0, 0) - (2, 2) = (-2, -2)
- Step 2: k(P - C) = 2(-2, -2) = (-4, -4)
- Step 3: C + k(P - C) = (2, 2) + (-4, -4) = (-2, -2)

So P' = (-2, -2)

For Q(4, 0):
- Step 1: Q - C = (4, 0) - (2, 2) = (2, -2)
- Step 2: k(Q - C) = 2(2, -2) = (4, -4)
- Step 3: C + k(Q - C) = (2, 2) + (4, -4) = (6, -2)

So Q' = (6, -2)

For R(2, 4):
- Step 1: R - C = (2, 4) - (2, 2) = (0, 2)
- Step 2: k(R - C) = 2(0, 2) = (0, 4)
- Step 3: C + k(R - C) = (2, 2) + (0, 4) = (2, 6)

So R' = (2, 6)

The dilated triangle has vertices P'(-2, -2), Q'(6, -2), R'(2, 6).

### Properties of Dilations (Standards G.SRT.1, G.SRT.1a, G.SRT.1b)

#### Property 1: Lines Through the Center Remain Unchanged
Any line passing through the center of dilation is mapped to itself (though points on that line move along it).

#### Property 2: Lines NOT Through the Center Map to Parallel Lines
If a line ℓ does NOT pass through center C, then the dilated line ℓ' is parallel to ℓ.

**Why?** Think of dilation as a "photocopy machine" centered at C. If a line doesn't go through the machine's center, it gets copied at a different distance from the center, but at the same angle — which means it's parallel to the original.

**Formal Proof Sketch:**
- Line ℓ is dilated to line ℓ'
- All points on ℓ are scaled by factor k from center C
- The direction vector of ℓ stays the same (scaled by k)
- Since direction vectors are proportional (differ only by factor k), the lines are parallel

#### Property 3: Lengths Are Multiplied by |k|
Every length in the figure is multiplied by the absolute value of the scale factor.

If segment AB has length d, then the dilated segment A'B' has length |k| · d.

#### Property 4: Angles Are Preserved
All angles in the original figure equal the corresponding angles in the dilated figure.

**This is crucial:** Dilation preserves angle measures. So if you dilate a right angle, you get another right angle.

#### Property 5: Dilation Creates Similar Figures
The dilated figure is similar to the original figure with scale factor |k|.

### Negative Scale Factors

What if k is negative? The figure is reflected through the center AND scaled.

If k = -2, a point at distance d from the center C ends up on the opposite side of C at distance 2d.

For example, dilating (1, 1) with center at origin and k = -2:
$$(1, 1) \xrightarrow{k=-2} (-2 \cdot 1, -2 \cdot 1) = (-2, -2)$$

The point (1, 1) is in the first quadrant; (-2, -2) is in the third quadrant (opposite direction).

### Common Mistakes with Dilations

**Mistake 1:** Applying the scaling rule without worrying about the center
- (x, y) → (kx, ky) ONLY works when the center is at the origin
- For other centers, you must use P' = C + k(P - C)

**Mistake 2:** Forgetting about absolute value on the scale factor
- |k| determines the size change, not k itself
- A factor of -0.5 enlarges by 0.5 and reflects (the negative is reflection, the 0.5 is reduction)

**Exam Tip:** Always draw a picture when dilating. Mark the center C, the original figure, and trace out the new figure point by point. This prevents errors and helps you understand what's happening.

---

## Properties of Similar Figures

### Characteristics of Similar Figures

When we say two figures are similar, we mean:

1. **Corresponding angles are congruent** (equal in measure)
2. **Corresponding sides are proportional** (their ratios are equal)
3. **The same scale factor applies throughout**

### How to Identify Corresponding Parts

When figures are similar, we must know which parts correspond. This is indicated by:
- The order we write the similarity: △ABC ~ △DEF means A↔D, B↔E, C↔F
- Sometimes there's a diagram showing which vertices match
- We look for equal angles to figure out which vertices correspond

### Angles in Similar Figures

**Key Fact:** Corresponding angles in similar figures are always equal.

If △ABC ~ △XYZ, then:
- ∠A = ∠X
- ∠B = ∠Y
- ∠C = ∠Z

This is true regardless of how the figures are oriented or positioned.

#### Example: Finding Angles in Similar Figures

△PQR ~ △STU. If ∠P = 40°, ∠Q = 65°, find ∠T.

**Solution:**
From △PQR ~ △STU:
- ∠P corresponds to ∠S, so ∠S = 40°
- ∠Q corresponds to ∠T, so ∠T = 65°
- ∠R corresponds to ∠U, so ∠U = ?

We can find ∠R using the fact that angles in a triangle sum to 180°:
$$∠R = 180° - 40° - 65° = 75°$$

Therefore, **∠T = 65°**

### Sides in Similar Figures

**Key Fact:** Corresponding sides in similar figures are proportional.

If △ABC ~ △XYZ with scale factor k, then:
$$\frac{AB}{XY} = \frac{BC}{YZ} = \frac{CA}{ZX} = k$$

#### Example 1: Finding Sides Using Proportions

△ABC ~ △DEF with AB = 6, BC = 8, AC = 10, and DE = 9. Find EF and DF.

**Solution:**

First, find the scale factor:
$$k = \frac{DE}{AB} = \frac{9}{6} = \frac{3}{2}$$

Now use the scale factor to find other sides:
$$EF = k \cdot BC = \frac{3}{2} \cdot 8 = 12$$

$$DF = k \cdot AC = \frac{3}{2} \cdot 10 = 15$$

So EF = 12 and DF = 15.

#### Example 2: Setting Up the Proportion

Two similar rectangles have a scale factor of 2:3. If the smaller rectangle has length 8 cm, what is the length of the larger rectangle?

**Solution:**

The scale factor 2:3 means:
$$\frac{\text{smaller}}{\text{larger}} = \frac{2}{3}$$

So:
$$\frac{8}{x} = \frac{2}{3}$$

Cross-multiply:
$$2x = 24$$
$$x = 12$$

The larger rectangle has length 12 cm.

---

## Triangle Similarity Theorems

### Why Triangle Similarity Is Enough

Here's a remarkable fact: **To prove two triangles are similar, you don't need to show that ALL angles are equal and ALL sides are proportional.** You only need to show one of these combinations, and the rest follows automatically.

This is because triangles are "rigid" shapes — once you fix the angles, the side ratios are determined (by the law of sines).

### AA Similarity (Angle-Angle) — MOST IMPORTANT

**AA Similarity Theorem:** If two angles of one triangle are congruent to two angles of another triangle, then the triangles are similar.

**Why this works:** If two angles are equal, the third angle must also be equal (since angles in a triangle sum to 180°). So all three angles are equal, which means the triangles have the same shape, which means they're similar.

**In symbols:** If ∠A = ∠D and ∠B = ∠E, then △ABC ~ △DEF

#### Example 1: Using AA Similarity

In triangles ABC and DEF, ∠A = 50°, ∠B = 60°, and ∠D = 50°, ∠E = 60°. Prove △ABC ~ △DEF.

**Solution:**

We're given:
- ∠A = ∠D = 50° ✓
- ∠B = ∠E = 60° ✓

By the AA Similarity Theorem, **△ABC ~ △DEF** ✓

We don't even need to check the third angle! (It would be 70° in both triangles, but we don't need to verify it.)

#### Example 2: AA with Right Triangles

Right triangle ABC has a right angle at C. Right triangle DEF has a right angle at F. If ∠A = 35° and ∠D = 35°, are they similar? Explain.

**Solution:**

Both triangles have:
- A right angle (∠C = 90° and ∠F = 90°) ✓
- ∠A = ∠D = 35° ✓

By AA Similarity (in fact, we only needed one more angle since both have right angles!), **△ABC ~ △DEF**

#### Example 3: AA in a Word Problem

A vertical pole casts a shadow, and at the same time, a person standing nearby casts a shadow. The triangles formed by the pole/shadow and person/shadow share the angle at the ground (where the shadow meets the pole). Is this enough to say the triangles are similar?

**Solution:**

No, not enough. We have:
- ∠ at ground = same angle for both triangles ✓
- But we need one more angle to be equal

However, if the sun's rays are parallel (which they essentially are for objects close to each other on Earth), then the angle at the top of each object (where the sun's ray hits) is equal by the property of parallel lines and transversals.

So yes, with the addition of this observation, the triangles ARE similar by AA.

### SSS Similarity (Side-Side-Side)

**SSS Similarity Theorem:** If all three pairs of corresponding sides of two triangles are proportional, then the triangles are similar.

**In symbols:** If $\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD}$, then △ABC ~ △DEF

**Why this works:** If all side ratios are equal, the triangles have the same proportions, which means they have the same shape (even if they're different sizes).

#### Example 1: Proving SSS Similarity

Triangle ABC has sides 6, 8, 10. Triangle DEF has sides 9, 12, 15. Are they similar? If so, find the scale factor.

**Solution:**

Check if all three ratios are equal:
$$\frac{6}{9} = \frac{2}{3}$$
$$\frac{8}{12} = \frac{2}{3}$$
$$\frac{10}{15} = \frac{2}{3}$$

All three ratios equal 2/3, so by SSS Similarity, **△ABC ~ △DEF** with scale factor k = 2/3 (from ABC to DEF).

#### Example 2: SSS Similarity with Larger Numbers

Do the triangles with sides (5, 7, 8) and (15, 20, 24) look similar? Check using SSS.

**Solution:**

$$\frac{5}{15} = \frac{1}{3}$$
$$\frac{7}{20} = 0.35 = \frac{7}{20}$$

Since 1/3 ≠ 7/20, the ratios are NOT all equal. Therefore, these triangles are **NOT similar**.

### SAS Similarity (Side-Angle-Side)

**SAS Similarity Theorem:** If two pairs of corresponding sides are proportional and the included angle (the angle between those sides) is congruent, then the triangles are similar.

**In symbols:** If $\frac{AB}{DE} = \frac{AC}{DF}$ and ∠A = ∠D, then △ABC ~ △DEF

**Key point:** The angle must be between the two sides you're checking the ratios on. This is called the "included angle."

#### Example 1: Using SAS Similarity

In △ABC and △DEF:
- AB = 8, AC = 12, ∠A = 50°
- DE = 4, DF = 6, ∠D = 50°

Are the triangles similar?

**Solution:**

Check the ratios:
$$\frac{AB}{DE} = \frac{8}{4} = 2$$
$$\frac{AC}{DF} = \frac{12}{6} = 2$$

Both ratios equal 2 ✓

Check the included angles:
$$∠A = ∠D = 50°$$ ✓

By SAS Similarity, **△ABC ~ △DEF** with scale factor 2.

#### Example 2: SAS with Angle NOT Between the Sides

In △PQR and △STU:
- PQ = 10, QR = 15, ∠P = 45°
- ST = 6, TU = 9, ∠S = 45°

Are they similar? (Note: ∠P and ∠S are both at the "first" vertex.)

**Solution:**

Check the ratios:
$$\frac{PQ}{ST} = \frac{10}{6} = \frac{5}{3}$$
$$\frac{QR}{TU} = \frac{15}{9} = \frac{5}{3}$$

Both ratios equal 5/3 ✓

Check the angles: ∠P = ∠S = 45° ✓

BUT — is ∠P included between PQ and QR?
- ∠P is at vertex P
- PQ and PR share vertex P
- So ∠P is between PQ and PR, NOT between PQ and QR

This is NOT an included angle setup for sides PQ and QR. We cannot use SAS Similarity here.

(We could use AA if we can verify another angle is equal, or we could check if PQ/ST = PR/SU using the law of cosines, but SAS directly doesn't apply.)

### Summary Table of Triangle Similarity Theorems

| Theorem | What You Need | Why It Works |
|---------|---------------|--------------|
| **AA** | Two pairs of angles equal | If two angles are equal, the third must be equal too, so all angles are equal → same shape |
| **SSS** | All three pairs of sides proportional | Same proportions on all sides → same shape |
| **SAS** | Two pairs of sides proportional + included angle equal | The included angle locks in the proportions; you can't have different shapes with these constraints |

### Common Mistakes with Similarity Theorems

**Mistake 1:** Confusing SSS Similarity with SSS Congruence
- **SSS Congruence:** All three sides are equal in length (=, not proportional)
- **SSS Similarity:** All three sides have the same ratio (proportional)
- Don't mix them up!

**Mistake 2:** Using SAS Similarity with a non-included angle
- The angle MUST be between the two sides
- If the angle is NOT between the sides, it's not SAS Similarity
- For example, if you have sides AB and BC with angle at C, that angle is not included (it's opposite AB)

**Mistake 3:** Forgetting to check that ALL pairs of sides are proportional for SSS
- You must verify that EVERY ratio equals the scale factor
- If even one ratio is different, it's not SSS Similarity

**Exam Tip:** Always identify which similarity theorem you're using by writing it down. This forces you to check all the conditions:
- AA → list two angle pairs
- SSS → show three equal ratios
- SAS → show two equal ratios AND an included angle

---

## Setting Up and Solving Proportions

### What Is a Proportion?

A **proportion** is an equation stating that two ratios are equal.

**General form:** $\frac{a}{b} = \frac{c}{d}$

We read this as "a is to b as c is to d."

### Cross-Multiplication

The most useful property of proportions is **cross-multiplication:**

If $\frac{a}{b} = \frac{c}{d}$, then $a \cdot d = b \cdot c$

This lets us solve for unknown values.

**Why this works:**
$$\frac{a}{b} = \frac{c}{d}$$

Multiply both sides by bd:
$$\frac{a}{b} \cdot bd = \frac{c}{d} \cdot bd$$
$$ad = bc$$

#### Example 1: Basic Proportion Solving

Solve: $\frac{x}{12} = \frac{5}{8}$

**Solution:**

Cross-multiply:
$$8x = 12 \cdot 5$$
$$8x = 60$$
$$x = \frac{60}{8} = \frac{15}{2} = 7.5$$

**Check:** $\frac{7.5}{12} = 0.625$ and $\frac{5}{8} = 0.625$ ✓

### Setting Up Proportions from Similar Figures

The key to using similarity is **setting up the proportion correctly.** Here's the strategy:

**Step 1:** Identify which figures are similar (use AA, SSS, or SAS)

**Step 2:** Identify corresponding sides

**Step 3:** Write a proportion: $\frac{\text{side 1 from figure A}}{\text{corresponding side 1 from figure B}} = \frac{\text{side 2 from figure A}}{\text{corresponding side 2 from figure B}}$

**Step 4:** Cross-multiply and solve

#### Example 1: Setting Up Proportions in Similar Triangles

△ABC ~ △DEF. If AB = 6, BC = 8, DE = 9, and EF = x, find x.

**Solution:**

Since △ABC ~ △DEF, corresponding sides are proportional:
$$\frac{AB}{DE} = \frac{BC}{EF}$$

Substitute known values:
$$\frac{6}{9} = \frac{8}{x}$$

Cross-multiply:
$$6x = 72$$
$$x = 12$$

So **EF = 12**.

#### Example 2: Multiple Unknown Sides

△PQR ~ △STU with a scale factor of 3:2. If ST = 10 and TU = 14, find PQ and QR.

**Solution:**

If the scale factor is 3:2, this means:
$$\frac{PQ}{ST} = \frac{3}{2}$$

So:
$$PQ = \frac{3}{2} \cdot ST = \frac{3}{2} \cdot 10 = 15$$

Similarly:
$$QR = \frac{3}{2} \cdot TU = \frac{3}{2} \cdot 14 = 21$$

**PQ = 15 and QR = 21**

#### Example 3: More Complex Setup

Two similar rectangles have areas in the ratio 4:9. If the length of the smaller rectangle is 8 cm, what is the length of the larger rectangle?

**Solution:**

The key insight: if areas are in ratio 4:9, then the **scale factor is √(4/9) = 2/3** (because area scales as the square of the linear scale factor).

Wait, let me clarify: if the smaller rectangle has area 4 and the larger has area 9, then:
$$\text{linear scale factor} = \sqrt{\frac{9}{4}} = \frac{3}{2}$$

So the larger rectangle is 3/2 times the size of the smaller:
$$\text{length of larger} = \frac{3}{2} \cdot 8 = 12 \text{ cm}$$

**Length of larger rectangle = 12 cm**

### Common Mistakes When Setting Up Proportions

**Mistake 1:** Not identifying corresponding sides correctly
- Make sure you're comparing side AB from one triangle to the correct corresponding side from the other triangle
- The similarity statement △ABC ~ △DEF tells you the correspondence: A↔D, B↔E, C↔F
- So AB corresponds to DE, BC corresponds to EF, and CA corresponds to FD

**Mistake 2:** Writing the proportion upside-down
- You can write it as $\frac{AB}{DE} = \frac{BC}{EF}$ OR $\frac{DE}{AB} = \frac{EF}{BC}$ (both are correct)
- But make sure you're consistent — don't switch styles halfway through

**Mistake 3:** Setting up proportions with non-corresponding sides
- If you do $\frac{AB}{EF} = \frac{BC}{DE}$, this is wrong because AB doesn't correspond to EF
- Always match sides that are in the same relative position

**Exam Tip:** Before you cross-multiply, take a moment to verify that you've matched corresponding sides correctly. Draw lines connecting corresponding parts if it helps.

---

## Triangle Proportionality Theorem

### The Theorem (Side-Splitter Theorem)

**Triangle Proportionality Theorem:** If a line is parallel to one side of a triangle and intersects the other two sides, then it divides those two sides proportionally.

**In symbols:** If line ℓ is parallel to BC and intersects AB at D and AC at E, then:
$$\frac{AD}{DB} = \frac{AE}{EC}$$

Or equivalently:
$$\frac{AD}{AB} = \frac{AE}{AC}$$

Or:
$$\frac{AB}{AD} = \frac{AC}{AE}$$

### Why This Theorem Works

The key insight is that a line parallel to one side of a triangle creates similar triangles.

**Proof sketch:**
- Let line DE be parallel to BC
- By the properties of parallel lines and transversals:
  - ∠ADE = ∠ABC (corresponding angles)
  - ∠AED = ∠ACB (corresponding angles)
- By AA Similarity, △ADE ~ △ABC
- Since the triangles are similar, corresponding sides are proportional:
$$\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}$$
- Rearranging: $\frac{AD}{DB} = \frac{AE}{EC}$

### Using the Triangle Proportionality Theorem

#### Example 1: Finding Unknown Segments

In △ABC, a line segment DE is drawn parallel to BC, with D on AB and E on AC. If AD = 6, DB = 4, and AE = 9, find EC.

**Solution:**

By the Triangle Proportionality Theorem:
$$\frac{AD}{DB} = \frac{AE}{EC}$$

Substitute known values:
$$\frac{6}{4} = \frac{9}{EC}$$

Cross-multiply:
$$6 \cdot EC = 4 \cdot 9$$
$$6 \cdot EC = 36$$
$$EC = 6$$

So **EC = 6**.

#### Example 2: More Complex Setup

In △PQR, a line segment MN is drawn parallel to QR, with M on PQ and N on PR. If PM = 8, MQ = 12, and PN = 10, find NR.

**Solution:**

By the Triangle Proportionality Theorem:
$$\frac{PM}{MQ} = \frac{PN}{NR}$$

Substitute:
$$\frac{8}{12} = \frac{10}{NR}$$

Simplify the left side:
$$\frac{2}{3} = \frac{10}{NR}$$

Cross-multiply:
$$2 \cdot NR = 3 \cdot 10$$
$$2 \cdot NR = 30$$
$$NR = 15$$

So **NR = 15**.

#### Example 3: Checking if Lines Are Parallel

In △ABC, D is a point on AB and E is a point on AC. If AD = 5, DB = 7, AE = 6, and EC = 8.4, is DE parallel to BC?

**Solution:**

Check if the ratios are equal:
$$\frac{AD}{DB} = \frac{5}{7} ≈ 0.714$$
$$\frac{AE}{EC} = \frac{6}{8.4} = \frac{60}{84} = \frac{5}{7} ≈ 0.714$$

Since the ratios are equal, **DE is parallel to BC** (by the converse of the Triangle Proportionality Theorem).

### The Converse of the Triangle Proportionality Theorem

**Converse:** If a line divides two sides of a triangle proportionally, then the line is parallel to the third side.

**In symbols:** If $\frac{AD}{DB} = \frac{AE}{EC}$, then DE || BC

This is extremely useful for proving that lines are parallel without directly measuring angles.

#### Example: Using the Converse

Prove that the line segment connecting the midpoints of two sides of a triangle is parallel to the third side.

**Solution:**

Let M be the midpoint of AB and N be the midpoint of AC in △ABC.

Then:
$$\frac{AM}{MB} = \frac{1/2 \cdot AB}{1/2 \cdot AB} = 1$$
$$\frac{AN}{NC} = \frac{1/2 \cdot AC}{1/2 \cdot AC} = 1$$

Since $\frac{AM}{MB} = \frac{AN}{NC}$, by the Converse of the Triangle Proportionality Theorem:
$$MN \text{ is parallel to } BC$$

### Common Mistakes with Triangle Proportionality

**Mistake 1:** Setting up the proportion with the wrong segments
- Make sure you're comparing the two pieces of one side to the two pieces of the other side
- Don't accidentally compare pieces of different sides

**Mistake 2:** Forgetting which segments form the ratios
- The ratio $\frac{AD}{DB}$ uses the two pieces of side AB
- The ratio $\frac{AE}{EC}$ uses the two pieces of side AC
- Both ratios must equal each other (this is what the theorem says)

**Mistake 3:** Confusing the direction of the line
- The line DE must be parallel to BC
- If DE is parallel to AB, that's a different situation entirely (it wouldn't use this theorem)

**Exam Tip:** Always draw the triangle and label all the segments. Mark the parallel line clearly. This prevents confusion about which ratio to use.

---

## Geometric Mean

### What Is the Geometric Mean?

The **geometric mean** of two numbers a and b is the value x such that:
$$\frac{a}{x} = \frac{x}{b}$$

Or equivalently:
$$x = \sqrt{ab}$$

**Definition:** The geometric mean of a and b is $\sqrt{ab}$.

### Geometric Mean vs. Arithmetic Mean

- **Arithmetic mean** (regular average): $\frac{a + b}{2}$
- **Geometric mean:** $\sqrt{ab}$

**Example:** For 4 and 9:
- Arithmetic mean: (4 + 9)/2 = 6.5
- Geometric mean: √(4 × 9) = √36 = 6

### Why Geometric Mean Matters in Similar Triangles

When you draw an altitude from the right angle to the hypotenuse in a right triangle, it creates similar triangles, and the geometric mean relationships appear.

### Geometric Mean in Right Triangles

**Theorem:** In a right triangle, when an altitude is drawn from the right angle to the hypotenuse:

1. **The altitude is the geometric mean of the segments of the hypotenuse:**
   $$h = \sqrt{p \cdot q}$$
   where p and q are the lengths of the two segments of the hypotenuse, and h is the altitude.

2. **Each leg is the geometric mean of the hypotenuse and the segment of the hypotenuse adjacent to that leg:**
   $$a = \sqrt{c \cdot p}$$
   $$b = \sqrt{c \cdot q}$$
   where a and b are the legs, c is the hypotenuse, and p and q are the segments.

### Understanding These Relationships

Let's say we have right triangle ABC with right angle at C. We draw an altitude CD from C to the hypotenuse AB, meeting at point D.

This creates three similar triangles:
- △ABC (original)
- △CAD (created by altitude)
- △CBD (created by altitude)

All three are similar: △ABC ~ △CAD ~ △CBD

From the similarity relationships, we get the geometric mean formulas.

#### Example 1: Finding an Altitude Using Geometric Mean

In right triangle ABC with right angle at C, an altitude CD is drawn to the hypotenuse AB. If AD = 4 and DB = 9, find the length of the altitude CD.

**Solution:**

Using the geometric mean formula for altitude:
$$CD = \sqrt{AD \cdot DB} = \sqrt{4 \cdot 9} = \sqrt{36} = 6$$

The altitude **CD = 6**.

#### Example 2: Finding a Leg Using Geometric Mean

In right triangle PQR with right angle at Q, an altitude QS is drawn to hypotenuse PR. If PR = 13 and PS = 4, find the length of leg PQ.

**Solution:**

Using the geometric mean formula for a leg:
$$PQ = \sqrt{PR \cdot PS} = \sqrt{13 \cdot 4} = \sqrt{52} = 2\sqrt{13}$$

The leg **PQ = 2√13** (or approximately 7.21).

#### Example 3: Finding All Segments

Right triangle ABC has a right angle at C and hypotenuse AB = 20. An altitude CD is drawn to the hypotenuse, and AD = 8. Find DB, CD, AC, and BC.

**Solution:**

First, find DB:
$$DB = AB - AD = 20 - 8 = 12$$

Find CD (altitude):
$$CD = \sqrt{AD \cdot DB} = \sqrt{8 \cdot 12} = \sqrt{96} = 4\sqrt{6}$$

Find AC (leg):
$$AC = \sqrt{AB \cdot AD} = \sqrt{20 \cdot 8} = \sqrt{160} = 4\sqrt{10}$$

Find BC (leg):
$$BC = \sqrt{AB \cdot DB} = \sqrt{20 \cdot 12} = \sqrt{240} = 4\sqrt{15}$$

**Summary:**
- DB = 12
- CD = 4√6 ≈ 9.80
- AC = 4√10 ≈ 12.65
- BC = 4√15 ≈ 15.49

**Check with Pythagorean Theorem:**
$$AC^2 + BC^2 = (4\sqrt{10})^2 + (4\sqrt{15})^2 = 160 + 240 = 400 = 20^2 = AB^2$$ ✓

### Common Mistakes with Geometric Mean

**Mistake 1:** Confusing which segments to multiply
- For altitude h: multiply the two segments of the hypotenuse (p and q)
- For leg a: multiply the whole hypotenuse (c) by the adjacent segment (p)
- It's easy to mess this up, so write it down carefully!

**Mistake 2:** Using arithmetic mean instead of geometric mean
- If you calculate (p + q)/2 instead of √(pq), you'll get the wrong answer
- The geometric mean involves multiplication and square roots, not addition

**Mistake 3:** Not simplifying the radical
- √96 = √(16 × 6) = 4√6, not just "√96"
- Always simplify radicals on exams

**Exam Tip:** Memorize the three geometric mean formulas, or at least remember that geometric mean involves √(product). When you see an altitude to the hypotenuse in a right triangle, geometric mean is usually the key to solving it.

---

## Perimeters and Areas of Similar Figures

### Ratio of Perimeters

**Theorem:** If two figures are similar with scale factor k, then the ratio of their perimeters equals k.

**In symbols:** If figure A ~ figure B with scale factor k, then:
$$\frac{\text{perimeter of A}}{\text{perimeter of B}} = k$$

Or equivalently:
$$\text{perimeter of B} = k \cdot \text{perimeter of A}$$

### Why This Works

If every length in figure B is k times the corresponding length in figure A, then the perimeter (sum of all lengths) in B is also k times the perimeter in A.

**Example:**
- Figure A: rectangle with sides 3 and 4, perimeter = 2(3) + 2(4) = 14
- Figure B: similar rectangle with scale factor k = 2, sides 6 and 8, perimeter = 2(6) + 2(8) = 28
- Ratio of perimeters: 28/14 = 2 = k ✓

#### Example 1: Finding Perimeter Using Scale Factor

Rectangle ABCD has perimeter 24 cm. Rectangle EFGH is similar to ABCD with scale factor 3. Find the perimeter of EFGH.

**Solution:**

$$\text{perimeter of EFGH} = 3 \cdot \text{perimeter of ABCD} = 3 \cdot 24 = 72 \text{ cm}$$

**Perimeter of EFGH = 72 cm**

#### Example 2: Finding Scale Factor from Perimeters

Two similar triangles have perimeters 15 and 25. What is the scale factor?

**Solution:**

$$k = \frac{\text{perimeter of first}}{\text{perimeter of second}} = \frac{15}{25} = \frac{3}{5}$$

The scale factor is **3/5** (from the first to the second).

Or: the scale factor from the second to the first is **5/3**.

### Ratio of Areas

**Theorem:** If two figures are similar with scale factor k, then the ratio of their areas equals k².

**In symbols:** If figure A ~ figure B with scale factor k, then:
$$\frac{\text{area of A}}{\text{area of B}} = k^2$$

Or equivalently:
$$\text{area of B} = k^2 \cdot \text{area of A}$$

### Why This Works

Area is two-dimensional, while length is one-dimensional. When you scale all lengths by k, the area gets scaled by k².

**Example:**
- Figure A: square with side 3, area = 9
- Figure B: similar square with scale factor k = 2, side 6, area = 36
- Ratio of areas: 36/9 = 4 = 2² = k² ✓

#### Example 1: Finding Area Using Scale Factor

Triangle ABC has area 20 square units. Triangle DEF is similar to ABC with scale factor 2. Find the area of DEF.

**Solution:**

$$\text{area of DEF} = 2^2 \cdot \text{area of ABC} = 4 \cdot 20 = 80 \text{ square units}$$

**Area of DEF = 80 square units**

#### Example 2: Finding Scale Factor from Areas

Two similar circles have areas 16π and 25π. What is the scale factor?

**Solution:**

$$k^2 = \frac{\text{area of first}}{\text{area of second}} = \frac{16π}{25π} = \frac{16}{25}$$

$$k = \sqrt{\frac{16}{25}} = \frac{4}{5}$$

The scale factor is **4/5**.

#### Example 3: Complex Problem with Perimeter and Area

Two similar rectangles have a scale factor of 3:5. If the smaller rectangle has area 12 cm², what is the area of the larger rectangle?

**Solution:**

The scale factor is k = 5/3 (from smaller to larger).

$$\text{area of larger} = k^2 \cdot \text{area of smaller} = \left(\frac{5}{3}\right)^2 \cdot 12 = \frac{25}{9} \cdot 12 = \frac{300}{9} = \frac{100}{3} ≈ 33.33 \text{ cm}^2$$

**Area of larger rectangle = 100/3 cm² or about 33.33 cm²**

### Summary Table: Comparing Scale Factors

| Measurement | Ratio Formula | Example |
|-------------|---------------|---------|
| Linear (length, perimeter) | ratio = k | If k = 2, perimeter is 2× |
| Area | ratio = k² | If k = 2, area is 4× |
| Volume | ratio = k³ | If k = 2, volume is 8× |

### Common Mistakes with Perimeters and Areas

**Mistake 1:** Using k² for perimeter instead of k
- Perimeter is linear, so use k
- Area is 2D, so use k²
- The exponent matters!

**Mistake 2:** Forgetting to square the scale factor for area
- If scale factor is 3, area ratio is 9, not 3
- This is one of the most common exam mistakes

**Mistake 3:** Confusing which figure is which
- If problem says "scale factor is 2:3," make sure you know if that's (small:large) or (large:small)
- Always read carefully

**Exam Tip:** Create a mental checklist:
- Linear measurements (sides, perimeters) → multiply by k
- Area → multiply by k²
- Volume → multiply by k³

---

## Proving the Pythagorean Theorem Using Similarity

### The Classic Proof Using Similarity

The Pythagorean Theorem is one of the most important results in all of mathematics. There are many proofs, but the one using similarity is elegant and instructive.

**Pythagorean Theorem:** In a right triangle with legs a and b and hypotenuse c:
$$a^2 + b^2 = c^2$$

### The Setup

Consider a right triangle ABC with:
- Right angle at C
- Legs AC = b and BC = a
- Hypotenuse AB = c
- Altitude CD drawn from C perpendicular to AB, meeting at D
- Let AD = p and DB = q, so p + q = c

### The Proof

**Step 1:** Identify the similar triangles.

When we draw altitude CD, we create three similar triangles:
- △ABC (the original)
- △CAD (right angle at D)
- △CBD (right angle at D)

These are all similar: △ABC ~ △CAD ~ △CBD

**Why are they similar?**
- All three have a right angle ✓
- △ABC and △CAD share angle A
- △ABC and △CBD share angle B
- By AA Similarity, they're all similar ✓

**Step 2:** Write proportions from the similar triangles.

From △ABC ~ △CAD:
$$\frac{AB}{AC} = \frac{AC}{AD}$$
$$\frac{c}{b} = \frac{b}{p}$$
$$b^2 = cp \quad \text{...(i)}$$

From △ABC ~ △CBD:
$$\frac{AB}{BC} = \frac{BC}{BD}$$
$$\frac{c}{a} = \frac{a}{q}$$
$$a^2 = cq \quad \text{...(ii)}$$

**Step 3:** Add the equations.

From (i) and (ii):
$$a^2 + b^2 = cq + cp$$
$$a^2 + b^2 = c(q + p)$$
$$a^2 + b^2 = c \cdot c$$
$$a^2 + b^2 = c^2$$

**QED** (end of proof)

### Understanding the Proof Intuitively

The key insight is that the altitude to the hypotenuse creates similar triangles, and the proportions from these similar triangles encode the Pythagorean relationship.

Think of it this way:
- The altitude "decomposes" the big triangle into two smaller similar triangles
- Each smaller triangle has the same angles as the big triangle
- The proportions between sides in similar triangles give us a + b² = c²

### Working Through an Example

Let's verify this proof with actual numbers.

Right triangle with legs a = 3 and b = 4. Then c = 5 (since 3² + 4² = 9 + 16 = 25 = 5²).

When we draw the altitude to the hypotenuse:
- The hypotenuse is divided into segments p and q where p + q = 5
- From b² = cp: 16 = 5p, so p = 16/5 = 3.2
- From a² = cq: 9 = 5q, so q = 9/5 = 1.8
- Check: 3.2 + 1.8 = 5 ✓
- And: (16/5) × 5 + (9/5) × 5 = 16 + 9 = 25 ✓

### Why Use Similarity to Prove Pythagorean Theorem?

This proof is powerful because it:
1. Shows that Pythagorean Theorem is a consequence of similar triangles
2. Reveals deep structure: how the altitude relates the legs to the hypotenuse
3. Produces the geometric mean relationships we studied earlier
4. Is elegant and geometrically intuitive

### Common Mistakes in Understanding This Proof

**Mistake 1:** Not seeing why the three triangles are similar
- Remember: altitude to hypotenuse in a right triangle creates two smaller right triangles
- Each smaller triangle is similar to the original
- You need all three to set up the right proportions

**Mistake 2:** Confusing which proportion gives which formula
- △ABC ~ △CAD gives b² = cp (using leg AC and segment AD)
- △ABC ~ △CBD gives a² = cq (using leg BC and segment BD)
- Don't mix them up!

**Mistake 3:** Forgetting why p + q = c
- p and q are the segments that the altitude divides the hypotenuse into
- Together, they make up the entire hypotenuse
- So p + q = c

**Exam Tip:** If you're asked to prove Pythagorean Theorem on an exam, practice this proof several times beforehand. Write out the three similar triangles, the two key proportions, and the addition step. It shows deep understanding.

---

## Real-World Applications

### Why Real-World Applications Matter

Similarity isn't just an abstract concept. It's used in:
- Architecture and engineering (scaling designs)
- Photography and graphics (resizing images)
- Navigation (maps use scale factors)
- Astronomy (calculating distances to stars)
- Construction (indirect measurement)

### Shadow Problems (Indirect Measurement)

**Concept:** When the sun is at a certain angle, shadows cast by objects of different heights will create similar triangles.

#### Example 1: Finding Building Height

A tree that is 8 feet tall casts a shadow of 10 feet. At the same time, a building casts a shadow of 50 feet. How tall is the building?

**Solution:**

The tree and its shadow form a right triangle. The building and its shadow form a similar right triangle (same sun angle).

By similarity:
$$\frac{\text{height of tree}}{\text{shadow of tree}} = \frac{\text{height of building}}{\text{shadow of building}}$$

$$\frac{8}{10} = \frac{h}{50}$$

Cross-multiply:
$$10h = 8 \cdot 50$$
$$10h = 400$$
$$h = 40 \text{ feet}$$

The building is **40 feet tall**.

#### Example 2: Finding Shadow Length

A pole is 15 meters tall and casts a shadow of 20 meters. At the same time, a person 1.8 meters tall casts a shadow. Using similarity, what is the length of the person's shadow?

**Solution:**

$$\frac{\text{pole height}}{\text{pole shadow}} = \frac{\text{person height}}{\text{person shadow}}$$

$$\frac{15}{20} = \frac{1.8}{x}$$

Cross-multiply:
$$15x = 20 \cdot 1.8$$
$$15x = 36$$
$$x = \frac{36}{15} = 2.4 \text{ meters}$$

The person's shadow is **2.4 meters long**.

### Mirror Method (Another Indirect Measurement Technique)

**Concept:** Use a mirror on the ground. The angle of reflection equals the angle of incidence. This creates similar triangles.

#### Example: Finding Height Using a Mirror

A person 6 feet tall stands back from a mirror until they can see the top of a tree. The person is 8 feet from the mirror, and the tree is 20 feet from the mirror. How tall is the tree?

**Solution:**

The angle of incidence equals angle of reflection, so:
- Triangle formed by person's eye height, their distance from mirror, and the mirror equals
- Triangle formed by tree's height, tree's distance from mirror, and the mirror

By similar triangles:
$$\frac{\text{person height}}{\text{person distance}} = \frac{\text{tree height}}{\text{tree distance}}$$

$$\frac{6}{8} = \frac{h}{20}$$

Cross-multiply:
$$8h = 6 \cdot 20$$
$$8h = 120$$
$$h = 15 \text{ feet}$$

The tree is **15 feet tall**.

### Map Scale Problems

**Concept:** Maps use a scale factor to represent real distances.

#### Example: Using Map Scale

A map has a scale of 1 inch : 5 miles. If two cities are 3.5 inches apart on the map, how far apart are they in reality?

**Solution:**

Set up the proportion:
$$\frac{1 \text{ inch}}{5 \text{ miles}} = \frac{3.5 \text{ inches}}{x \text{ miles}}$$

Cross-multiply:
$$x = 3.5 \cdot 5 = 17.5 \text{ miles}$$

The cities are **17.5 miles apart in reality**.

### Enlargement/Reduction Problems

**Concept:** Photographs, diagrams, and models are often scaled versions of real objects.

#### Example: Blueprint Scale

An architect creates a blueprint with scale 1 inch : 20 feet. If a room is 4 inches long on the blueprint, what is its actual length?

**Solution:**

$$\frac{1}{20} = \frac{4}{x}$$

$$x = 4 \cdot 20 = 80 \text{ feet}$$

The actual room is **80 feet long**.

### Design/Model Problems

**Concept:** When building models or scale designs, use similarity to calculate dimensions.

#### Example: Model Car

A model car is made to a scale of 1:32 (1 inch on model : 32 inches on real car). If the model car is 5 inches long, how long is the real car?

**Solution:**

$$\frac{1}{32} = \frac{5}{x}$$

$$x = 5 \cdot 32 = 160 \text{ inches} = 13\frac{1}{3} \text{ feet} ≈ 13.33 \text{ feet}$$

The real car is **160 inches or about 13.33 feet long**.

### Common Mistakes in Real-World Problems

**Mistake 1:** Setting up the scale ratio backwards
- Scale 1:5 means 1 unit on model = 5 units in reality
- Don't flip it: it's not 5:1
- Always write "map : reality" or "model : actual"

**Mistake 2:** Forgetting units
- Always include units in your answer (feet, meters, inches, miles, etc.)
- Check that units match on both sides of the proportion

**Mistake 3:** Not simplifying or calculating correctly
- Double-check your arithmetic
- Make sure the answer makes sense (e.g., a model should be smaller than the real thing)

**Exam Tip:** For shadow problems, always draw a picture showing:
- The object and its shadow (vertical and horizontal)
- The angle of the sun's rays
- Mark the right angles
- Identify the two similar right triangles
This visual approach prevents mistakes.

---

## Practice Problems and Solutions

### Problem Set 1: Basic Similarity

**Problem 1.1:** Triangle ABC has sides 5, 7, and 9. Triangle DEF has sides 10, 14, and 18. Are these triangles similar? If so, what is the scale factor?

**Solution:**

Check if all ratios are equal (SSS Similarity):
$$\frac{10}{5} = 2, \quad \frac{14}{7} = 2, \quad \frac{18}{9} = 2$$

All ratios equal 2, so **Yes, △ABC ~ △DEF** with **scale factor k = 2** (from ABC to DEF).

---

**Problem 1.2:** In △PQR, ∠P = 45°, ∠Q = 75°. In △STU, ∠S = 45°, ∠T = 75°. Are the triangles similar?

**Solution:**

We have:
- ∠P = ∠S = 45° ✓
- ∠Q = ∠T = 75° ✓

By AA Similarity, **yes, △PQR ~ △STU** ✓

---

**Problem 1.3:** Rectangle ABCD has length 12 and width 8. Rectangle EFGH is similar to ABCD with scale factor 3/4. Find the dimensions of EFGH.

**Solution:**

$$\text{length of EFGH} = \frac{3}{4} \cdot 12 = 9$$

$$\text{width of EFGH} = \frac{3}{4} \cdot 8 = 6$$

**EFGH has dimensions 9 × 6**.

---

### Problem Set 2: Dilations

**Problem 2.1:** Dilate point B(4, -2) with center at the origin and scale factor 3.

**Solution:**

$$(4, -2) \xrightarrow{k=3} (3 \cdot 4, 3 \cdot (-2)) = (12, -6)$$

**B' = (12, -6)**

---

**Problem 2.2:** Dilate triangle XYZ with vertices X(2, 0), Y(0, 2), Z(2, 2) with center at the origin and scale factor 1/2.

**Solution:**

Apply (x, y) → (½x, ½y):
- X(2, 0) → X'(1, 0)
- Y(0, 2) → Y'(0, 1)
- Z(2, 2) → Z'(1, 1)

**X'Y'Z' has vertices (1, 0), (0, 1), (1, 1)**

---

**Problem 2.3:** The line through points A(1, 1) and B(3, 1) is dilated with center C(0, 0) and scale factor 2. What is the new line?

**Solution:**

Dilate both points:
- A(1, 1) → A'(2, 2)
- B(3, 1) → B'(6, 2)

The original line AB is horizontal (y = 1). The new line A'B' passes through (2, 2) and (6, 2), so it's also horizontal: **y = 2**.

The lines are parallel ✓ (confirming the dilation property)

---

### Problem Set 3: Triangle Similarity Theorems

**Problem 3.1:** In △ABC and △DEF, AB = 6, AC = 8, ∠A = 50°, and DE = 9, DF = 12, ∠D = 50°. Are the triangles similar? If so, name the similarity and find the scale factor.

**Solution:**

Check if sides are proportional:
$$\frac{DE}{AB} = \frac{9}{6} = \frac{3}{2}$$
$$\frac{DF}{AC} = \frac{12}{8} = \frac{3}{2}$$

Both ratios are 3/2 ✓

Check the included angles:
$$∠A = ∠D = 50°$$ ✓

By SAS Similarity, **△ABC ~ △DEF** with **scale factor 3/2** (from ABC to DEF).

---

**Problem 3.2:** Solve the proportion: $\frac{x}{8} = \frac{15}{12}$

**Solution:**

Cross-multiply:
$$12x = 8 \cdot 15$$
$$12x = 120$$
$$x = 10$$

**x = 10**

---

**Problem 3.3:** △ABC ~ △XYZ with scale factor 2:5. If XY = 10, find AB.

**Solution:**

If the scale factor from AB to XYZ is 2:5, then:
$$\frac{AB}{XY} = \frac{2}{5}$$

$$\frac{AB}{10} = \frac{2}{5}$$

$$5 \cdot AB = 2 \cdot 10$$
$$AB = 4$$

**AB = 4**

---

### Problem Set 4: Triangle Proportionality Theorem

**Problem 4.1:** In △ABC, a line DE is parallel to BC, with D on AB and E on AC. If AD = 3, DB = 5, and AE = 4.5, find EC.

**Solution:**

By Triangle Proportionality Theorem:
$$\frac{AD}{DB} = \frac{AE}{EC}$$

$$\frac{3}{5} = \frac{4.5}{EC}$$

Cross-multiply:
$$3 \cdot EC = 5 \cdot 4.5$$
$$3 \cdot EC = 22.5$$
$$EC = 7.5$$

**EC = 7.5**

---

**Problem 4.2:** In △PQR, point M is on PQ and point N is on PR. If PM = 6, MQ = 9, and PN = 8, is MN parallel to QR?

**Solution:**

Check if the ratios are equal:
$$\frac{PM}{MQ} = \frac{6}{9} = \frac{2}{3}$$
$$\frac{PN}{NR} = ?$$

We need NR. From the given information, we can't determine if MN || QR without knowing NR or QR.

**We cannot determine without more information.**

(If the problem gave us PN and NR, we could check if their ratio equals 2/3.)

---

### Problem Set 5: Geometric Mean

**Problem 5.1:** In right triangle ABC with right angle at C, an altitude CD is drawn to the hypotenuse AB. If AD = 6 and DB = 8, find CD.

**Solution:**

$$CD = \sqrt{AD \cdot DB} = \sqrt{6 \cdot 8} = \sqrt{48} = 4\sqrt{3}$$

**CD = 4√3** (or approximately 6.93)

---

**Problem 5.2:** In right triangle DEF with right angle at E, an altitude EG is drawn to the hypotenuse DF. If DF = 25 and DG = 9, find DE.

**Solution:**

$$DE = \sqrt{DF \cdot DG} = \sqrt{25 \cdot 9} = \sqrt{225} = 15$$

**DE = 15**

---

**Problem 5.3:** Find the geometric mean of 12 and 27.

**Solution:**

$$\text{geometric mean} = \sqrt{12 \cdot 27} = \sqrt{324} = 18$$

**The geometric mean is 18**.

---

### Problem Set 6: Perimeters and Areas

**Problem 6.1:** Two similar triangles have a scale factor of 2:3. The smaller triangle has perimeter 20 cm. Find the perimeter of the larger triangle.

**Solution:**

$$\frac{\text{perimeter of smaller}}{\text{perimeter of larger}} = \frac{2}{3}$$

$$\frac{20}{\text{perimeter of larger}} = \frac{2}{3}$$

Cross-multiply:
$$2 \cdot (\text{perimeter of larger}) = 3 \cdot 20$$
$$\text{perimeter of larger} = 30 \text{ cm}$$

**Perimeter of larger triangle = 30 cm**

---

**Problem 6.2:** Two similar circles have areas 16π and 64π. Find the scale factor.

**Solution:**

$$k^2 = \frac{\text{area 1}}{\text{area 2}} = \frac{16π}{64π} = \frac{1}{4}$$

$$k = \sqrt{\frac{1}{4}} = \frac{1}{2}$$

**Scale factor = 1/2** (from larger to smaller)

or **Scale factor = 2** (from smaller to larger)

---

**Problem 6.3:** Rectangle A has area 40 square units. Rectangle B is similar to Rectangle A with scale factor 5. Find the area of Rectangle B.

**Solution:**

$$\text{area of B} = k^2 \cdot \text{area of A} = 5^2 \cdot 40 = 25 \cdot 40 = 1000$$

**Area of Rectangle B = 1000 square units**

---

### Problem Set 7: Real-World Applications

**Problem 7.1:** A tree that is 6 meters tall casts a shadow of 8 meters. A nearby building casts a shadow of 24 meters at the same time. How tall is the building?

**Solution:**

By similarity of shadows:
$$\frac{\text{tree height}}{\text{tree shadow}} = \frac{\text{building height}}{\text{building shadow}}$$

$$\frac{6}{8} = \frac{h}{24}$$

Cross-multiply:
$$8h = 6 \cdot 24$$
$$8h = 144$$
$$h = 18 \text{ meters}$$

**The building is 18 meters tall**.

---

**Problem 7.2:** A map has a scale of 1 cm : 15 km. If the distance between two cities is 4.5 cm on the map, what is the actual distance?

**Solution:**

$$\frac{1}{15} = \frac{4.5}{x}$$

$$x = 4.5 \cdot 15 = 67.5 \text{ km}$$

**The actual distance is 67.5 km**.

---

**Problem 7.3:** A blueprint uses a scale of 1 inch : 12 feet. If a wall is 6 inches on the blueprint, what is the actual wall length?

**Solution:**

$$\frac{1}{12} = \frac{6}{x}$$

$$x = 6 \cdot 12 = 72 \text{ feet}$$

**The actual wall is 72 feet long**.

---

### Problem Set 8: Challenge Problems

**Problem 8.1:** Right triangle ABC has legs 5 and 12. After finding the hypotenuse, draw an altitude from the right angle to the hypotenuse. Find all segments created and the length of the altitude.

**Solution:**

**Step 1: Find the hypotenuse**
$$c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$$

**Step 2: Set up the geometric mean relationships**

Let a = 5 (one leg), b = 12 (other leg), c = 13 (hypotenuse)
Let p = segment adjacent to leg a, q = segment adjacent to leg b

From a² = cp:
$$25 = 13p$$
$$p = \frac{25}{13}$$

From b² = cq:
$$144 = 13q$$
$$q = \frac{144}{13}$$

**Step 3: Find the altitude h**
$$h = \sqrt{pq} = \sqrt{\frac{25}{13} \cdot \frac{144}{13}} = \sqrt{\frac{3600}{169}} = \frac{60}{13}$$

**Summary:**
- Hypotenuse = 13
- Segment p (adjacent to 5) = 25/13
- Segment q (adjacent to 12) = 144/13
- Altitude h = 60/13

---

**Problem 8.2:** Two similar figures have area ratio 9:16. Find the scale factor and the perimeter ratio.

**Solution:**

From area ratio:
$$k^2 = \frac{9}{16}$$
$$k = \frac{3}{4}$$

The scale factor is 3:4 (from first to second).

For perimeter ratio:
$$\text{perimeter ratio} = k = \frac{3}{4}$$

**Scale factor is 3:4; perimeter ratio is 3:4**

---

**Problem 8.3:** In △ABC, point D is on AB such that AD:DB = 2:3. A line through D parallel to BC intersects AC at point E. Find AE:EC.

**Solution:**

Since DE || BC, by the Triangle Proportionality Theorem:
$$\frac{AD}{DB} = \frac{AE}{EC}$$

We're given:
$$\frac{AD}{DB} = \frac{2}{3}$$

Therefore:
$$\frac{AE}{EC} = \frac{2}{3}$$

**AE:EC = 2:3**

---

## Summary and Key Takeaways

### Core Concepts to Master

1. **Similarity** = same shape, different size (equal angles, proportional sides)
2. **Scale Factor** = the ratio by which lengths are multiplied
3. **Dilations** = transformations using center and scale factor
4. **Similar Triangle Tests** = AA, SSS, SAS (you only need one!)
5. **Proportions** = cross-multiply to solve for unknowns
6. **Triangle Proportionality** = parallel line creates proportional segments
7. **Geometric Mean** = √(ab), appears in right triangles with altitudes
8. **Perimeter & Area Ratios** = k for perimeter, k² for area
9. **Pythagorean Theorem** = proved using similarity and altitudes
10. **Applications** = shadows, maps, models, indirect measurement

### Most Common Exam Questions

1. "Prove these triangles are similar" (use AA, SSS, or SAS)
2. "Find the scale factor" (write ratio of corresponding sides)
3. "Find missing side lengths" (set up proportions)
4. "Are these figures similar?" (check angle equality and side proportions)
5. "Find area/perimeter of similar figure" (use k² for area, k for perimeter)
6. "Solve real-world application" (shadow, map, or model problem)

### Study Tips

- **Draw pictures** for every problem
- **Label corresponding parts** clearly
- **Write the similarity statement** early (e.g., △ABC ~ △DEF)
- **Always check units** in word problems
- **Simplify radicals** in geometric mean problems
- **Verify answers** make sense (similar figures should have reasonable sizes)

### Final Advice

Similarity is about recognizing that figures have the same shape even when they're different sizes. This is fundamental to geometry and has applications everywhere. Master the definitions and theorems, practice setting up proportions, and always draw pictures. You've got this!

