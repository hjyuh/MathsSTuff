# Unit 2: Transformations — Comprehensive Study Notes
## Honors Geometry Curriculum

---

## Table of Contents
1. [Foundational Concepts](#foundational-concepts)
2. [Translations](#translations)
3. [Reflections](#reflections)
4. [Rotations](#rotations)
5. [Dilations](#dilations)
6. [Rigid Motions vs. Non-Rigid Motions](#rigid-motions-vs-non-rigid-motions)
7. [Composition of Transformations](#composition-of-transformations)
8. [Symmetry](#symmetry)
9. [Congruence and Transformations](#congruence-and-transformations)
10. [Glide Reflections](#glide-reflections)
11. [Parallel Lines and Transformations](#parallel-lines-and-transformations)
12. [Study Strategies & Exam Tips](#study-strategies--exam-tips)

---

# Foundational Concepts

## What is a Transformation?

### Plain English Definition
A **transformation** is a rule that moves or changes a figure in some way. It takes every point on the original figure and maps it to a new location or new size. The original figure is called the **pre-image**, and the result after applying the transformation is called the **image**.

**Think of it like this:** Imagine you have a sticker of a star (the pre-image). If you move that sticker to a different spot on your paper, the new location of the star is the image. The rule "move 3 inches to the right and 2 inches up" is the transformation.

### Key Vocabulary
- **Pre-image**: The original figure before transformation
- **Image**: The figure after the transformation has been applied
- **Prime notation (′)**: When we label points, we use primes to show the image. Point A maps to point A′ (read "A prime")
- **Mapping**: The relationship between a pre-image point and its image point, written as: A → A′
- **Function**: A transformation is a function because each point in the pre-image maps to exactly one point in the image

### Core Concept: Transformations as Functions

In Honors Geometry, we treat transformations as **functions**. Just like in algebra where f(x) takes an input x and produces an output, a transformation takes coordinates (x, y) and produces new coordinates (x′, y′).

**Example:**
- Pre-image point: A = (2, 3)
- Transformation rule: "Move 4 units right and 1 unit down"
- Image point: A′ = (6, 2)
- We write this as: (2, 3) → (6, 2)

### The Four Main Types of Transformations

There are four main transformations you'll study in Honors Geometry:

1. **Translation** — slides a figure without rotating or flipping
2. **Reflection** — flips a figure across a line (like a mirror)
3. **Rotation** — turns a figure around a fixed point
4. **Dilation** — enlarges or shrinks a figure (but doesn't rotate or flip)

Each of these works differently and has its own coordinate rules.

---

# Translations

## Definition

A **translation** (or **slide**) is a transformation that moves every point on a figure the same distance in the same direction. The figure slides without rotating, flipping, or changing size.

**Key insight:** In a translation, the figure maintains its size and orientation. If you have a triangle, it stays the same size and shape—it just moves.

## Key Vocabulary

- **Translation vector**: Describes the direction and distance of the slide, usually written as ⟨a, b⟩ or sometimes as an arrow notation
- **Horizontal displacement**: How far left or right the figure moves (the "a" value)
- **Vertical displacement**: How far up or down the figure moves (the "b" value)

## Core Concepts Step by Step

### Understanding Translation

A translation is defined by two numbers:
1. How far to move horizontally (left/right)
2. How far to move vertically (up/down)

**Direction convention:**
- Positive horizontal value = move RIGHT
- Negative horizontal value = move LEFT
- Positive vertical value = move UP
- Negative vertical value = move DOWN

### Coordinate Rule for Translation

If you translate a point (x, y) by vector ⟨a, b⟩, the image point is:

$$\boxed{(x, y) \rightarrow (x + a, y + b)}$$

**What this means:**
- Add "a" to the x-coordinate
- Add "b" to the y-coordinate
- That's it! It's the simplest transformation.

## Worked Examples

### Example 1: Basic Translation

**Problem:** Point A = (3, 2). Translate by vector ⟨5, -3⟩. Find A′.

**Solution:**
Using the rule (x, y) → (x + a, y + b):
- x-coordinate of A′: 3 + 5 = 8
- y-coordinate of A′: 2 + (-3) = -1
- **Answer: A′ = (8, -1)**

**Check yourself:** Did I add 5 to the x-coordinate? Yes. Did I add -3 to the y-coordinate? Yes. ✓

---

### Example 2: Translating Multiple Points (a Figure)

**Problem:** Triangle ABC has vertices A = (1, 1), B = (4, 1), and C = (3, 4). Translate the triangle by vector ⟨-2, 3⟩. Find the vertices of triangle A′B′C′.

**Solution:**
Apply the rule (x, y) → (x - 2, y + 3) to each vertex:

- Point A = (1, 1):
  - A′ = (1 - 2, 1 + 3) = (-1, 4)

- Point B = (4, 1):
  - B′ = (4 - 2, 1 + 3) = (2, 4)

- Point C = (3, 4):
  - C′ = (3 - 2, 4 + 3) = (1, 7)

**Answer: A′ = (-1, 4), B′ = (2, 4), C′ = (1, 7)**

**Visual note:** The triangle ABC and triangle A′B′C′ have the same shape and size. The only difference is position.

---

### Example 3: Writing the Translation Rule from Two Points

**Problem:** Point M = (5, 3) is translated to M′ = (1, 8). Describe the translation using vector notation.

**Solution:**
Use the rule: (x, y) → (x + a, y + b)

From M = (5, 3) to M′ = (1, 8):
- Horizontal change: 1 - 5 = -4 (so a = -4, move 4 units LEFT)
- Vertical change: 8 - 3 = 5 (so b = 5, move 5 units UP)

**Answer: The translation vector is ⟨-4, 5⟩** (or "move 4 units left and 5 units up")

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Adding both a and b to x-coordinate | You must add a to x and b to y separately | Remember: x-value gets a, y-value gets b |
| Forgetting negative signs | ⟨-3, 4⟩ means move LEFT, not right | Treat -3 as -3, not 3. Double-check your signs |
| Mixing up direction | Confusing which number is horizontal | Write it out: "a = 5 means right, b = -2 means down" |
| Using subtraction instead of addition | The rule is always addition, even with negative numbers | (x, y) → (x + a, y + b), never subtract |

---

## Exam Tips for Translations

1. **Always write the full coordinate rule** — Don't just give numbers. Show (x, y) → (x + a, y + b) with your a and b values.

2. **Check by using two points** — If you're given one point's translation, verify using another point or the reverse direction.

3. **Use a table for multiple points** — When translating a whole figure, organize your work:
   ```
   Point | Original | Image
   A     | (2, 3)   | (5, 7)
   B     | (1, 0)   | (4, 4)
   ```

4. **Visualize before calculating** — Sketch where the figure should go. This catches many errors.

5. **The translation vector is always the same for every point** — This is how you know it's a translation, not some other transformation.

---

# Reflections

## Definition

A **reflection** is a transformation that flips a figure across a line (called the **line of reflection**). The line of reflection acts like a mirror. Every point on the pre-image is the same distance from the line of reflection as its image, but on the opposite side.

**Think of it this way:** If you hold a piece of paper up to a mirror, the mirror image is a reflection. The mirror itself is the line of reflection.

## Key Vocabulary

- **Line of reflection**: The line across which the figure is flipped (acts like a mirror)
- **Perpendicular distance**: The shortest distance from a point to the line of reflection
- **Mirror image**: The reflected figure

## Core Concepts Step by Step

### How Reflection Works

In a reflection:
1. Every point and its image are equidistant from the line of reflection
2. The line connecting a point to its image is perpendicular to the line of reflection
3. If a point is ON the line of reflection, it doesn't move

**Visual example:** If reflecting across the x-axis, point (3, 5) reflects to (3, -5). Both are 5 units away from the x-axis, but on opposite sides.

### Five Main Lines of Reflection

There are five lines of reflection you absolutely must know:

#### 1. Reflection over the X-Axis

**Line of reflection:** The x-axis (the horizontal line y = 0)

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (x, -y)}$$

**What happens:** The x-coordinate stays the same. The y-coordinate changes sign (becomes its opposite).

**Why:** Points above the x-axis (positive y) go to the same distance below (negative y), and vice versa.

**Example:**
- (2, 3) → (2, -3)
- (5, -1) → (5, 1)
- (0, 4) → (0, -4)

---

#### 2. Reflection over the Y-Axis

**Line of reflection:** The y-axis (the vertical line x = 0)

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (-x, y)}$$

**What happens:** The y-coordinate stays the same. The x-coordinate changes sign.

**Why:** Points to the right of the y-axis (positive x) go to the same distance to the left (negative x), and vice versa.

**Example:**
- (3, 2) → (-3, 2)
- (-1, 5) → (1, 5)
- (4, -3) → (-4, -3)

---

#### 3. Reflection over the Line y = x

**Line of reflection:** The diagonal line y = x (45° angle through origin)

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (y, x)}$$

**What happens:** The x and y coordinates swap places.

**Why:** The line y = x is the "diagonal mirror." Points reflect across this diagonal by exchanging their coordinates.

**Example:**
- (2, 5) → (5, 2)
- (3, 1) → (1, 3)
- (-2, 4) → (4, -2)

**Interesting note:** If you plot both the original point and its reflection over y = x, the line y = x passes exactly through the middle of them.

---

#### 4. Reflection over the Line y = -x

**Line of reflection:** The diagonal line y = -x (goes down 45°)

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (-y, -x)}$$

**What happens:** The coordinates swap AND both change sign.

**Why:** This line goes the opposite direction from y = x, so both coordinates change sign after swapping.

**Example:**
- (2, 3) → (-3, -2)
- (1, -4) → (4, -1)
- (-2, -1) → (1, 2)

**Memory trick:** "Swap and negate" — swap the coordinates AND make them both negative.

---

#### 5. Reflection over Horizontal or Vertical Lines (Not Axes)

Sometimes the line of reflection is NOT the x-axis or y-axis.

**Reflection over a vertical line x = a:**

To reflect (x, y) over the vertical line x = a:
1. Find the distance from x to the line: distance = |x - a|
2. Go that same distance on the other side: x′ = a + (a - x) = 2a - x
3. y-coordinate doesn't change: y′ = y

$$\boxed{(x, y) \rightarrow (2a - x, y)}$$

**Example:** Reflect (3, 4) over the vertical line x = 5
- Distance from x = 3 to line x = 5: |3 - 5| = 2 units
- Go 2 units on the other side: 5 + 2 = 7
- **Answer: (3, 4) → (7, 4)**

**Check:** The line x = 5 passes through (5, 4), which is the midpoint of (3, 4) and (7, 4). ✓

---

**Reflection over a horizontal line y = b:**

To reflect (x, y) over the horizontal line y = b:
1. Find the distance from y to the line: distance = |y - b|
2. Go that same distance on the other side: y′ = b + (b - y) = 2b - y
3. x-coordinate doesn't change: x′ = x

$$\boxed{(x, y) \rightarrow (x, 2b - y)}$$

**Example:** Reflect (2, 1) over the horizontal line y = 3
- Distance from y = 1 to line y = 3: |1 - 3| = 2 units
- Go 2 units on the other side: 3 + 2 = 5
- **Answer: (2, 1) → (2, 5)**

**Check:** The line y = 3 passes through (2, 3), which is the midpoint of (2, 1) and (2, 5). ✓

---

## Worked Examples

### Example 1: Reflection over the X-Axis

**Problem:** Triangle PQR has vertices P = (1, 2), Q = (4, 2), and R = (3, 5). Reflect the triangle over the x-axis. Find P′, Q′, and R′.

**Solution:**
Use rule: (x, y) → (x, -y)

- P = (1, 2) → P′ = (1, -2)
- Q = (4, 2) → Q′ = (4, -2)
- R = (3, 5) → R′ = (3, -5)

**Answer: P′ = (1, -2), Q′ = (4, -2), R′ = (3, -5)**

**Visualization note:** The original triangle sits above the x-axis. The reflected triangle sits below it at the same distance. They would be mirror images if you folded the paper along the x-axis.

---

### Example 2: Reflection over the Line y = x

**Problem:** A quadrilateral has vertices A = (1, 1), B = (3, 1), C = (4, 3), D = (2, 3). Reflect over y = x.

**Solution:**
Use rule: (x, y) → (y, x)

- A = (1, 1) → A′ = (1, 1) [Note: Points on y = x don't move!]
- B = (3, 1) → B′ = (1, 3)
- C = (4, 3) → C′ = (3, 4)
- D = (2, 3) → D′ = (3, 2)

**Answer: A′ = (1, 1), B′ = (1, 3), C′ = (3, 4), D′ = (3, 2)**

**Key insight:** Point A didn't move because it's ON the line of reflection. Any point on the line of reflection stays fixed.

---

### Example 3: Reflection over a Non-Axis Line

**Problem:** Reflect point (6, 2) over the vertical line x = 2.

**Solution:**
Use rule: (x, y) → (2a - x, y) where a = 2

- x′ = 2(2) - 6 = 4 - 6 = -2
- y′ = 2

**Answer: (6, 2) → (-2, 2)**

**Verification:**
- Distance from (6, 2) to line x = 2: |6 - 2| = 4 units to the right
- Should be 4 units to the left of x = 2: 2 - 4 = -2 ✓
- Midpoint of (6, 2) and (-2, 2) is (2, 2), which lies on x = 2 ✓

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Changing the wrong coordinate | Reflection over x-axis changes y, not x | Remember: horizontal line (x-axis) flips the y-value |
| Forgetting to change the sign | (3, 5) over x-axis is NOT (3, 5) | Always apply the sign change: (x, y) → (x, -y) |
| Mixing up y = x and y = -x | These are two different diagonal lines | y = x swaps only; y = -x swaps and negates both |
| Not recognizing fixed points | Some points don't move in a reflection | Any point ON the line of reflection stays in place |
| Miscalculating the formula for non-axis lines | Using (x, y) → (2a - x, y) incorrectly | Verify with a test point: Is the line the perpendicular bisector? |

---

## Exam Tips for Reflections

1. **Memorize the five basic rules** — You should know them without hesitation:
   - x-axis: (x, y) → (x, -y)
   - y-axis: (x, y) → (-x, y)
   - y = x: (x, y) → (y, x)
   - y = -x: (x, y) → (-y, -x)
   - Other lines: Use the perpendicular bisector approach

2. **Use the perpendicular bisector method** — For any line of reflection, the reflected point should be such that the line of reflection is the perpendicular bisector of the segment connecting the original and image points.

3. **Check: Are distances preserved?** — In a reflection, all distances should stay the same. If you reflected a triangle, all side lengths should be identical before and after.

4. **Don't forget the line of reflection** — Always state clearly which line you're reflecting over. Different lines give different answers!

5. **Sketch it** — Even a rough sketch can prevent sign errors and coordinate mix-ups.

---

# Rotations

## Definition

A **rotation** is a transformation that turns a figure around a fixed point (called the **center of rotation**). The figure spins like a wheel. Rotations are defined by:
1. The center point around which you rotate
2. The angle of rotation (in degrees)
3. The direction (clockwise or counterclockwise)

**Think of it this way:** Imagine a figure is drawn on a sheet of plastic and you put a pin through one point (the center). Now spin the sheet. That's a rotation.

## Key Vocabulary

- **Center of rotation**: The fixed point around which the figure rotates
- **Angle of rotation**: How many degrees the figure turns (measured in degrees)
- **Clockwise (CW)**: Rotation direction like clock hands
- **Counterclockwise (CCW)**: Rotation direction opposite to clock hands (the positive direction in mathematics)
- **Image distance**: The distance from the center of rotation to any point stays the same after rotation

## Core Concepts Step by Step

### Understanding Rotation

In a rotation with center C and angle θ:
1. Every point moves along a circle centered at C
2. The radius of that circle (distance from C to the point) never changes
3. The point rotates through angle θ

**Key insight:** Unlike translations, the position of the center matters enormously. Rotating around (0,0) is completely different from rotating around (5,3).

### Rotations Around the Origin (0, 0)

These are the most common rotations you'll see in Honors Geometry.

#### 90° Counterclockwise Rotation

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (-y, x)}$$

**How to remember:**
- The original x becomes the new y (with a sign change)
- The original y becomes the new x (with a sign change)
- Or: "Negate x and swap them"

**Examples:**
- (1, 0) → (0, 1) [point on positive x-axis goes to positive y-axis]
- (0, 1) → (-1, 0) [point on positive y-axis goes to negative x-axis]
- (2, 3) → (-3, 2)
- (-1, 4) → (-4, -1)

**Visual check:** If you start at (1, 0) and rotate 90° counterclockwise, you should end up at (0, 1). Does our rule give that? (1, 0) → (-0, 1) = (0, 1) ✓

---

#### 90° Clockwise Rotation

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (y, -x)}$$

**How to remember:**
- The opposite of counterclockwise
- Swap coordinates and negate the new x

**Examples:**
- (1, 0) → (0, -1) [point on positive x-axis goes to negative y-axis]
- (0, 1) → (1, 0) [point on positive y-axis goes to positive x-axis]
- (3, 2) → (2, -3)
- (-2, 5) → (5, 2)

**Relationship:** 90° CW is the same as 270° CCW. If you're ever confused, you can use the counterclockwise formula three times: 90° + 90° + 90° = 270° = one 90° clockwise.

---

#### 180° Rotation

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (-x, -y)}$$

**How to remember:**
- Both coordinates become their opposites
- The point is now on the exact opposite side of the origin

**Examples:**
- (2, 3) → (-2, -3)
- (-1, 5) → (1, -5)
- (3, 0) → (-3, 0)

**Visual note:** 180° rotation is equivalent to two 90° rotations. You can verify: (2, 3) → (-3, 2) → (-2, -3) ✓

---

#### 270° Counterclockwise Rotation (= 90° Clockwise)

**Coordinate rule:**
$$\boxed{(x, y) \rightarrow (y, -x)}$$

This is the same as 90° clockwise, as mentioned above.

---

### Rotations Around Other Centers

What if the center of rotation is NOT the origin?

**General process for rotating (x, y) around center (a, b) by angle θ:**

1. **Translate** so the center of rotation becomes the origin
   - New point: (x - a, y - b)

2. **Apply the rotation rule** for the angle around the origin
   - For 90° CCW: (x - a, y - b) → (-(y - b), x - a)

3. **Translate back** to restore the original coordinate system
   - Add the center back: (-(y - b) + a, (x - a) + b)
   - Simplify: (a - y + b, x - a + b)

**General formula for 90° CCW around center (a, b):**
$$\boxed{(x, y) \rightarrow (a - (y - b), b + (x - a))}$$

Simplified:
$$\boxed{(x, y) \rightarrow (a - y + b, x - a + b)}$$

**This is complicated!** In most cases, you'll be rotating around the origin. If you must rotate around another point, the three-step process above is clearer than memorizing a formula.

---

## Worked Examples

### Example 1: 90° Counterclockwise Rotation Around Origin

**Problem:** Rotate triangle ABC around the origin by 90° counterclockwise. Given: A = (1, 0), B = (3, 1), C = (2, 3).

**Solution:**
Use rule: (x, y) → (-y, x)

- A = (1, 0) → A′ = (-0, 1) = (0, 1)
- B = (3, 1) → B′ = (-1, 3)
- C = (2, 3) → C′ = (-3, 2)

**Answer: A′ = (0, 1), B′ = (-1, 3), C′ = (-3, 2)**

**Visualization:** Original triangle is in the first quadrant (upper right). After 90° CCW rotation, it moves to the second quadrant (upper left).

---

### Example 2: 180° Rotation Around Origin

**Problem:** Rotate point P = (5, -2) by 180° around the origin.

**Solution:**
Use rule: (x, y) → (-x, -y)

- P = (5, -2) → P′ = (-5, 2)

**Answer: P′ = (-5, 2)**

**Check:** The origin (0, 0) is the midpoint of (5, -2) and (-5, 2). This makes sense because a 180° rotation puts you on the opposite side of the center. ✓

---

### Example 3: 90° Clockwise Rotation Around a Non-Origin Center

**Problem:** Rotate point Q = (4, 3) by 90° clockwise around center C = (1, 1).

**Solution:**
Use the three-step process:

**Step 1: Translate Q so C becomes the origin**
- Subtract the center: (4 - 1, 3 - 1) = (3, 2)

**Step 2: Rotate (3, 2) by 90° clockwise around the origin**
- Use rule: (x, y) → (y, -x)
- (3, 2) → (2, -3)

**Step 3: Translate back by adding the center**
- (2, -3) + (1, 1) = (2 + 1, -3 + 1) = (3, -2)

**Answer: Q′ = (3, -2)**

**Verification:**
- Original Q is 3 units right and 2 units up from C
- Image Q′ should be 2 units right and 3 units down from C
- From C = (1, 1): (1 + 2, 1 - 3) = (3, -2) ✓

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Confusing rotation direction | 90° CCW is NOT the same as 90° CW | Learn both rules: CCW is (x,y)→(-y,x), CW is (x,y)→(y,-x) |
| Forgetting the center matters | Rotating around origin vs. another point gives different answers | Always identify the center first. If it's not (0,0), use the three-step process |
| Applying the rule multiple times incorrectly | Trying to compose rotations mentally | If stuck, apply the rule step-by-step. 270° CCW = three 90° rotations |
| Sign errors | Getting the negatives wrong | Test with (1,0): it should go to (0,1) for 90° CCW. Check your rule. |
| Forgetting to translate back | Only doing steps 1 and 2 of the three-step process | After applying the rotation, ALWAYS add the center back |

---

## Exam Tips for Rotations

1. **For rotations around the origin, memorize these four rules:**
   - 90° CCW: (x, y) → (-y, x)
   - 90° CW: (x, y) → (y, -x)
   - 180°: (x, y) → (-x, -y)
   - 270° CCW: (x, y) → (y, -x) [same as 90° CW]

2. **Use the origin test** — For a rotation around the origin, check your work: (1, 0) should go to (0, 1) for 90° CCW, (-1, 0) for 90° CW, and (-1, 0) for 180°.

3. **For non-origin centers, use the three-step process** — Translate, rotate, translate back. Don't try to memorize complex formulas.

4. **Preserve distances** — The distance from any point to the center of rotation never changes. Use this to verify your answer.

5. **Check orientation** — In a rotation, the figure doesn't flip. If the vertices were labeled clockwise, they should still be clockwise after rotation.

---

# Dilations

## Definition

A **dilation** is a transformation that enlarges or shrinks a figure by a certain factor. Unlike the previous three transformations, a dilation can change the size of a figure. All points in the figure scale by the same ratio relative to a center point.

**Think of it this way:** Imagine you're resizing a photo. If you double the dimensions, you're applying a dilation with scale factor 2. If you shrink it to half the size, that's a dilation with scale factor 0.5.

## Key Vocabulary

- **Center of dilation**: The fixed point from which the scaling happens
- **Scale factor (k)**: The ratio of the image size to the pre-image size
  - If k > 1: **Enlargement** (figure gets bigger)
  - If 0 < k < 1: **Reduction** (figure gets smaller)
  - If k = 1: **No change** (not really a transformation)
  - If k < 0: **Opposite side** (reflection + dilation combined, less common)
- **Congruent**: Same shape and size
- **Similar**: Same shape but possibly different size

## Core Concepts Step by Step

### How Dilation Works

In a dilation with center C and scale factor k:
1. Every point is scaled by factor k relative to the center
2. Distances from the center are multiplied by k
3. The shape stays the same (similar figures)
4. The size changes (unless k = 1)

**Key insight:** Unlike rigid motions (translation, reflection, rotation), dilations do NOT preserve size. Dilations ARE preserving shape and angles.

### Coordinate Rule for Dilation

If the center of dilation is the **origin** (0, 0) and the scale factor is k:

$$\boxed{(x, y) \rightarrow (kx, ky)}$$

**What this means:**
- Multiply the x-coordinate by k
- Multiply the y-coordinate by k

**Examples:**
- With scale factor 2: (3, 4) → (6, 8)
- With scale factor 0.5: (4, 6) → (2, 3)
- With scale factor 3: (1, -2) → (3, -6)

### Dilation Around a Non-Origin Center

For a dilation with center (a, b) and scale factor k:

1. **Translate** so the center becomes the origin
   - New point: (x - a, y - b)

2. **Apply the dilation rule**
   - Multiply by k: (k(x - a), k(y - b))

3. **Translate back**
   - Add the center: (k(x - a) + a, k(y - b) + b)

**General formula:**
$$\boxed{(x, y) \rightarrow (a + k(x - a), b + k(y - b))}$$

Simplified: $\boxed{(x, y) \rightarrow (kx - ka + a, ky - kb + b) = (kx + a(1-k), ky + b(1-k))}$

---

## Worked Examples

### Example 1: Dilation with Center at Origin

**Problem:** Dilate triangle ABC with scale factor 2 around the origin. Given: A = (1, 2), B = (2, 1), C = (3, 3).

**Solution:**
Use rule: (x, y) → (2x, 2y)

- A = (1, 2) → A′ = (2, 4)
- B = (2, 1) → B′ = (4, 2)
- C = (3, 3) → C′ = (6, 6)

**Answer: A′ = (2, 4), B′ = (4, 2), C′ = (6, 6)**

**Verification:**
- Original side AB: from (1, 2) to (2, 1), distance = √[(2-1)² + (1-2)²] = √2
- Image side A′B′: from (2, 4) to (4, 2), distance = √[(4-2)² + (2-4)²] = √8 = 2√2
- The ratio is 2√2 / √2 = 2, matching our scale factor ✓

---

### Example 2: Reduction (Scale Factor < 1)

**Problem:** Dilate point P = (8, 6) with scale factor 0.5 around the origin.

**Solution:**
Use rule: (x, y) → (0.5x, 0.5y)

- P = (8, 6) → P′ = (4, 3)

**Answer: P′ = (4, 3)**

**Note:** The new point is half as far from the origin as the original point.

---

### Example 3: Dilation with Non-Origin Center

**Problem:** Dilate point Q = (5, 3) with scale factor 2 around center C = (1, 1).

**Solution:**
Use the three-step process:

**Step 1: Translate Q so C becomes the origin**
- Subtract the center: (5 - 1, 3 - 1) = (4, 2)

**Step 2: Dilate (4, 2) by scale factor 2**
- (4, 2) → (8, 4)

**Step 3: Translate back by adding the center**
- (8, 4) + (1, 1) = (9, 5)

**Answer: Q′ = (9, 5)**

**Alternative formula method:**
- (x, y) → (a + k(x - a), b + k(y - b))
- (5, 3) → (1 + 2(5 - 1), 1 + 2(3 - 1))
- = (1 + 2(4), 1 + 2(2))
- = (1 + 8, 1 + 4)
- = (9, 5) ✓

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Multiplying by (scale factor + 1) | You multiply by k, not k+1 | Use (x, y) → (kx, ky), not ((k+1)x, (k+1)y) |
| Forgetting the center exists | Assuming all dilations are around origin | Always check: is the center given? If not, it's the origin. |
| Adding the scale factor instead of multiplying | The rule is multiplication, not addition | (x, y) → (kx, ky), not (x+k, y+k) |
| Using the wrong formula for non-origin centers | Applying (kx, ky) without translating first | Use (a + k(x-a), b + k(y-b)) or the three-step process |
| Confusing scale factor with position | Thinking k = 2 means the image is at (2x, 2y) without considering the center | The image is 2 times as far from the center, not 2 times the coordinate values |

---

## Exam Tips for Dilations

1. **Always multiply coordinates** — Don't add or subtract. Dilation is always multiplication.

2. **Check if the center is the origin** — Most introductory problems use the origin. Only use the complex formula if a non-origin center is explicitly given.

3. **Scale factors greater than 1 mean enlargement** — The image is bigger than the pre-image.

4. **Scale factors between 0 and 1 mean reduction** — The image is smaller than the pre-image.

5. **Similar but not congruent** — Dilations create similar figures (same shape, different size). If you're asked if figures are congruent, a dilation means they're NOT congruent.

6. **Use the center-to-point distance** — The distance from the center to any point is multiplied by k. Use this to verify:
   - Original distance from C to P = √[(5-1)² + (3-1)²] = √20 = 2√5
   - New distance from C to P′ = √[(9-1)² + (5-1)²] = √80 = 4√5
   - Ratio: 4√5 / 2√5 = 2 ✓

---

# Rigid Motions vs. Non-Rigid Motions

## What Are Rigid Motions?

A **rigid motion** (also called an **isometry**) is a transformation that preserves distances and angles. When you apply a rigid motion, the figure doesn't change size or shape—only position or orientation.

**Important principle:** If you can map one figure onto another using only rigid motions, the figures are **congruent**.

### The Three Rigid Motions

✓ **Translations** — rigid motion (preserve distance and angle)
✓ **Reflections** — rigid motion (preserve distance and angle)
✓ **Rotations** — rigid motion (preserve distance and angle)

---

## Dilations Are NOT Rigid Motions

**Dilations are non-rigid** because they change the size of the figure.

- In a dilation with scale factor k ≠ 1, all distances are multiplied by k
- If the pre-image has a side of length 3 and you dilate by scale factor 2, the image has a side of length 6
- Distances are NOT preserved

### What IS Preserved in a Dilation?
- **Angles** — All angles stay the same
- **Proportions** — If side A is twice as long as side B, that relationship stays true
- **Shape** — The figures are similar (not congruent)

---

## What's Preserved in Each Transformation?

| Transformation | Distances Preserved | Angles Preserved | Size Preserved | Rigid? |
|----------------|--------------------|-----------------|-----------------|----|
| Translation    | ✓ YES               | ✓ YES            | ✓ YES           | ✓ YES |
| Reflection     | ✓ YES               | ✓ YES            | ✓ YES           | ✓ YES |
| Rotation       | ✓ YES               | ✓ YES            | ✓ YES           | ✓ YES |
| Dilation       | ✗ NO                | ✓ YES            | ✗ NO (unless k=1) | ✗ NO |

---

## Why This Matters

**For congruence:** Two figures are congruent if you can map one onto the other using rigid motions (translation, reflection, and/or rotation in any combination).

**For similarity:** Two figures are similar if you can map one onto the other using rigid motions and dilation.

**Example:**
- Triangle ABC and Triangle DEF with the same angle measures but different side lengths → They are SIMILAR, not congruent
- Triangle ABC and Triangle DEF with the same angle measures and side lengths → They are CONGRUENT

---

# Composition of Transformations

## Definition

A **composition of transformations** (or **composite transformation**) means doing more than one transformation in sequence. You apply one transformation, then apply another to the result.

**Think of it like this:** You translate a figure, then rotate what you just translated. That's a composition of a translation followed by a rotation.

## Key Vocabulary

- **Order matters** — Doing transformation A then B usually gives a different result than doing B then A
- **Notation:** T₁ ∘ T₂ means "do T₂ first, then do T₁" (same as function composition in algebra)
- **Composition of rigid motions is rigid** — If all transformations are rigid, the result is rigid

---

## How to Work with Compositions

### Basic Process

1. **Apply the first transformation** using its rule
2. **Use the result** as the input for the second transformation
3. **Apply the second transformation** to get the final answer

### Example: Translation Then Rotation

**Problem:** Point A = (1, 0) is first translated by vector ⟨2, 3⟩, then the result is rotated 90° counterclockwise around the origin.

**Solution:**

**Step 1: Translate (1, 0) by ⟨2, 3⟩**
- A₁ = (1 + 2, 0 + 3) = (3, 3)

**Step 2: Rotate (3, 3) by 90° CCW around origin**
- Use rule: (x, y) → (-y, x)
- A₂ = (-3, 3)

**Answer: A′ = (-3, 3)**

---

## Important Composite Transformations

### Reflection + Reflection = Translation (or Identity)

Two reflections over parallel lines equals a translation.
Two reflections over the same line equals the identity (no change).

### Reflection + Reflection = Rotation (Angle = Double the Angle Between Lines)

Two reflections over intersecting lines equals a rotation around the intersection point, with angle equal to twice the angle between the lines.

**Example:** Two reflections over perpendicular lines (like the x and y axes) = 180° rotation

### Translation + Translation = Translation

Two translations compose to form a single translation with vector equal to the sum of the two vectors.

**Example:** ⟨2, 3⟩ then ⟨-1, 5⟩ = single translation ⟨2 + (-1), 3 + 5⟩ = ⟨1, 8⟩

---

## Worked Examples

### Example 1: Reflection Then Translation

**Problem:** Reflect point B = (2, 3) over the y-axis, then translate the result by vector ⟨-4, 2⟩.

**Solution:**

**Step 1: Reflect (2, 3) over y-axis**
- Use rule: (x, y) → (-x, y)
- B₁ = (-2, 3)

**Step 2: Translate (-2, 3) by ⟨-4, 2⟩**
- Use rule: (x, y) → (x - 4, y + 2)
- B₂ = (-2 - 4, 3 + 2) = (-6, 5)

**Answer: B′ = (-6, 5)**

---

### Example 2: Two Reflections Over Perpendicular Lines

**Problem:** Reflect point C = (3, 2) first over the x-axis, then over the y-axis.

**Solution:**

**Step 1: Reflect (3, 2) over x-axis**
- Use rule: (x, y) → (x, -y)
- C₁ = (3, -2)

**Step 2: Reflect (3, -2) over y-axis**
- Use rule: (x, y) → (-x, y)
- C₂ = (-3, -2)

**Answer: C′ = (-3, -2)**

**Observation:** We got (-3, -2), which is the same as a 180° rotation! Two perpendicular reflections = 180° rotation. This confirms our principle.

---

### Example 3: Rotation Then Dilation

**Problem:** Rotate point D = (2, 0) by 90° counterclockwise around the origin, then dilate the result by scale factor 3 around the origin.

**Solution:**

**Step 1: Rotate (2, 0) by 90° CCW**
- Use rule: (x, y) → (-y, x)
- D₁ = (0, 2)

**Step 2: Dilate (0, 2) by scale factor 3**
- Use rule: (x, y) → (3x, 3y)
- D₂ = (0, 6)

**Answer: D′ = (0, 6)**

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Doing transformations in reverse order | T₁ ∘ T₂ means do T₂ first | Read carefully. "Then" indicates order. Do left-most last. |
| Forgetting to use the result of the first as input to the second | Only applying the first transformation | Write out both results: A → A₁ → A″ |
| Mixing up the rules for each transformation | Getting confused about which rule applies where | Apply one complete rule, THEN apply the next complete rule |
| Assuming order doesn't matter | Some compositions are order-dependent | Always work left to right unless specifically told otherwise |

---

## Exam Tips for Compositions

1. **Write intermediate steps** — Show A → A′ → A″ so it's clear you're applying transformations in sequence.

2. **Use the result of the first as input to the second** — Don't forget to substitute.

3. **Know the special cases:**
   - Two reflections over parallel lines = translation
   - Two reflections over intersecting lines = rotation
   - Translation + translation = translation (add the vectors)

4. **Try both orders if unsure** — If you're not sure which order, work both ways. Usually, the problem will specify clearly.

5. **Check reasonableness** — If you composed a rigid motion with a dilation, the size should change. If you composed two rigid motions, the size should stay the same.

---

# Symmetry

## Definition

**Symmetry** describes when a figure looks the same after a transformation. There are two main types:
1. **Line symmetry (reflective symmetry)** — the figure looks the same after reflecting across a line
2. **Rotational symmetry** — the figure looks the same after rotating

## Line Symmetry (Reflective Symmetry)

### What It Is

A figure has **line symmetry** if there exists a line such that reflecting the figure across that line produces the exact same figure.

**Think of it this way:** If you fold the figure along the line of symmetry, both halves match perfectly.

The line is called the **line of symmetry** or **axis of symmetry**.

### How to Find Line Symmetry

1. Look for a line that would divide the figure into two identical halves
2. The line of symmetry is often through the middle or center of the figure
3. Test: If you fold along this line, do both halves match exactly?

### Examples of Line Symmetry

- **Isosceles triangle:** 1 line of symmetry (down the middle)
- **Equilateral triangle:** 3 lines of symmetry (through each vertex and the opposite side's midpoint)
- **Square:** 4 lines of symmetry (2 through opposite corners, 2 through midpoints of opposite sides)
- **Circle:** Infinite lines of symmetry (any line through the center)
- **Rectangle (not square):** 2 lines of symmetry (through opposite side midpoints)
- **Scalene triangle:** No line symmetry

### Worked Example: Finding Line Symmetry

**Problem:** Does the letter "A" have line symmetry? If so, describe the line of symmetry.

**Solution:**
- The letter "A" is symmetric down the middle
- The line of symmetry is a vertical line through the center
- If you fold along this line, the left and right halves match
- **Answer:** Yes, one line of symmetry (vertical, through the center)

---

## Rotational Symmetry

### What It Is

A figure has **rotational symmetry** if rotating it by some angle less than 360° produces the same figure.

The point you rotate around is called the **center of symmetry**.

### Order of Rotational Symmetry

The **order of rotational symmetry** is the number of times a figure maps onto itself during a complete 360° rotation.

**Formula:** If the order is n, then the rotation angle is 360°/n

### Examples of Rotational Symmetry

- **Square:** Order 4 (rotations of 90°, 180°, 270° map it to itself)
- **Equilateral triangle:** Order 3 (rotations of 120°, 240° map it to itself)
- **Regular hexagon:** Order 6 (rotations of 60°, 120°, 180°, 240°, 300° map it to itself)
- **Circle:** Infinite order (any rotation maps it to itself)
- **Rectangle (not square):** Order 2 (only 180° maps it to itself)
- **Scalene triangle:** Order 1 (only 360° maps it to itself, so technically no rotational symmetry)

### How to Determine Rotational Symmetry

1. Imagine rotating the figure around its center
2. Count how many times it matches itself as you rotate through 360°
3. That count is the order
4. Divide 360° by the order to get the rotation angle

### Worked Example: Finding Rotational Symmetry

**Problem:** A regular pentagon has rotational symmetry. What is the order and rotation angle?

**Solution:**
- A regular pentagon has 5 identical sides
- It maps to itself when rotated by 360°/5 = 72°, 144°, 216°, and 288°
- That's 4 rotations plus the original (360°), so order = 5
- **Answer:** Order 5, with rotation angles of 72°, 144°, 216°, 288° (and 360°, which is the identity)

---

## Point Symmetry (180° Rotational Symmetry)

A special case of rotational symmetry is **point symmetry** (or **central symmetry**).

A figure has **point symmetry** if rotating it 180° around a point produces the same figure. That point is called the **center of symmetry**.

### Examples of Point Symmetry

- **Square:** Has point symmetry (around the center)
- **Rectangle:** Has point symmetry (around the center)
- **Equilateral triangle:** NO point symmetry (180° rotation doesn't map it to itself)
- **Regular hexagon:** Has point symmetry (around the center)
- **Letter "S":** Has point symmetry (around the center)

---

## Relationship Between Line Symmetry and Rotational Symmetry

An important fact: **If a figure has two different lines of symmetry that intersect, those lines intersect at the center of rotational symmetry.**

**Example:** A square has 4 lines of symmetry. They all intersect at the center. If you rotate the square around that center, it has rotational symmetry of order 4.

---

## Worked Examples

### Example 1: Analyzing Symmetry of a Rectangle

**Problem:** Analyze the line and rotational symmetry of a rectangle (that is not a square).

**Solution:**

**Line symmetry:**
- Vertical line through the center: ✓ (left and right halves match)
- Horizontal line through the center: ✓ (top and bottom halves match)
- Diagonal lines: ✗ (no match)
- **Total: 2 lines of symmetry**

**Rotational symmetry:**
- 90° rotation: ✗ (rectangle is wider than tall, so no match)
- 180° rotation: ✓ (looks the same)
- 270° rotation: ✗ (same issue as 90°)
- **Order: 2 (only 180° and 360° map it to itself)**

**Answer:**
- Line symmetry: 2 lines (vertical and horizontal through the center)
- Rotational symmetry: Order 2, with 180° rotation angle

---

### Example 2: Analyzing Symmetry of an Equilateral Triangle

**Problem:** Analyze the line and rotational symmetry of an equilateral triangle.

**Solution:**

**Line symmetry:**
- Each vertex to the midpoint of opposite side: ✓ (3 such lines)
- **Total: 3 lines of symmetry**

**Rotational symmetry:**
- 120° rotation: ✓ (3 vertices, so 360°/3 = 120°)
- 240° rotation: ✓ (second application)
- **Order: 3 (rotations of 120°, 240°, 360°)**

**Answer:**
- Line symmetry: 3 lines (through each vertex and the midpoint of the opposite side)
- Rotational symmetry: Order 3, with 120° rotation angle

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Confusing line and rotational symmetry | They're different things | Check: is it a reflection (line) or a rotation (rotational)? |
| Counting 360° as a separate rotation | 360° is always one | Order counts rotations less than 360°, not including 360° |
| Missing lines of symmetry | Only checking obvious lines | Check diagonals, horizontals, and verticals separately |
| Saying a figure has no rotational symmetry if order ≠ 2, 3, 4 | Order can be any number | Any regular n-gon has order n |
| Confusing center of rotational symmetry with center of line symmetry | They're often the same point but not always | For figures with both, the intersection of lines of symmetry is the center |

---

## Exam Tips for Symmetry

1. **Sketch the figure** — Even a rough sketch helps you identify lines and rotations.

2. **Test your lines** — For line symmetry, mentally fold along the line and check if halves match.

3. **Rotate methodically** — For rotational symmetry, try 90°, 180°, 270° first.

4. **Use regular polygons as references** — Regular hexagon = order 6, square = order 4, equilateral triangle = order 3.

5. **Remember the formula:** Order of rotational symmetry = 360° / (rotation angle)

6. **Every figure has order 1 symmetry** — Because rotating 360° always works. Real rotational symmetry has order ≥ 2.

---

# Congruence and Transformations

## Definition of Congruence

Two figures are **congruent** if they have the same shape and size.

**In terms of transformations:** Two figures are congruent if one can be mapped onto the other using a sequence of rigid motions (translations, reflections, and/or rotations).

**Notation:** We write ABC ≅ DEF to mean "triangle ABC is congruent to triangle DEF"

---

## The Role of Rigid Motions in Congruence

### Why Rigid Motions?

Rigid motions preserve:
- ✓ Distances (side lengths stay the same)
- ✓ Angles (angle measures stay the same)

These are the properties that define congruence. If you can map one figure onto another using rigid motions, then all corresponding distances and angles are equal.

### The Reverse: If Congruent, Then Rigid Motions Exist

**Theorem:** If two figures are congruent, then there exists a sequence of rigid motions that maps one onto the other.

This is a fundamental connection in geometry.

---

## Correspondence in Congruent Figures

When two figures are congruent, we must establish which vertices correspond to each other.

**Order matters in notation:** ABC ≅ DEF means:
- A corresponds to D
- B corresponds to E
- C corresponds to F

### Writing Correspondence from a Transformation

If figure ABC is transformed to produce figure A′B′C′, then:
- A ↔ A′
- B ↔ B′
- C ↔ C′

---

## Worked Examples

### Example 1: Proving Congruence Using Translation

**Problem:** Triangle ABC has vertices A = (1, 1), B = (4, 1), C = (3, 4). Triangle DEF has vertices D = (2, 3), E = (5, 3), F = (4, 6). Prove that ABC ≅ DEF.

**Solution:**

**Step 1: Find the translation that maps A to D**
- From A = (1, 1) to D = (2, 3)
- Translation vector: ⟨2 - 1, 3 - 1⟩ = ⟨1, 2⟩

**Step 2: Check if this translation maps B to E and C to F**
- B = (4, 1) → (4 + 1, 1 + 2) = (5, 3) = E ✓
- C = (3, 4) → (3 + 1, 4 + 2) = (4, 6) = F ✓

**Conclusion:** The translation by vector ⟨1, 2⟩ maps triangle ABC to triangle DEF. Since translation is a rigid motion, ABC ≅ DEF.

---

### Example 2: Proving Congruence Using Rotation and Translation

**Problem:** Quadrilateral PQRS has vertices P = (0, 0), Q = (1, 0), R = (1, 1), S = (0, 1). Quadrilateral P′Q′R′S′ has vertices P′ = (3, 4), Q′ = (3, 5), R′ = (2, 5), S′ = (2, 4). Prove that PQRS ≅ P′Q′R′S′.

**Solution:**

**Option 1: Check if a translation alone works**
- From P to P′: ⟨3 - 0, 4 - 0⟩ = ⟨3, 4⟩
- Q = (1, 0) → (1 + 3, 0 + 4) = (4, 4) ≠ (3, 5) ✗

So it's not just a translation.

**Option 2: Try a composition of rigid motions**
Let's try: rotate 90° CCW around origin, then translate.

- After 90° CCW: (x, y) → (-y, x)
  - P = (0, 0) → (0, 0)
  - Q = (1, 0) → (0, 1)
  - R = (1, 1) → (-1, 1)
  - S = (0, 1) → (-1, 0)

- Check if translation ⟨3, 4⟩ completes it:
  - (0, 0) + ⟨3, 4⟩ = (3, 4) = P′ ✓
  - (0, 1) + ⟨3, 4⟩ = (3, 5) = Q′ ✓
  - (-1, 1) + ⟨3, 4⟩ = (2, 5) = R′ ✓
  - (-1, 0) + ⟨3, 4⟩ = (2, 4) = S′ ✓

**Conclusion:** A 90° CCW rotation followed by translation by ⟨3, 4⟩ maps PQRS to P′Q′R′S′. Since both are rigid motions, PQRS ≅ P′Q′R′S′.

---

## Congruence Criteria for Triangles

You already know these from earlier geometry:

- **SSS (Side-Side-Side):** All three pairs of corresponding sides are equal
- **SAS (Side-Angle-Side):** Two sides and the included angle are equal
- **ASA (Angle-Side-Angle):** Two angles and the included side are equal
- **AAS (Angle-Angle-Side):** Two angles and a non-included side are equal

**Connection to transformations:** If any of these criteria are met, you could theoretically find a sequence of rigid motions to prove congruence. However, the traditional congruence criteria are usually faster.

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Using dilations to prove congruence | Dilations change size, so they don't prove congruence | Only use rigid motions (translation, reflection, rotation) |
| Saying figures are congruent without rigid motions | You need to show HOW they're congruent | Always specify which transformation(s) map one to the other |
| Mismatching corresponding vertices | Order matters in notation | Write ABC ≅ DEF carefully; check which vertex corresponds to which |
| Not checking all vertices after a transformation | A transformation might work for one point but not others | Always verify that ALL vertices map correctly |

---

## Exam Tips for Congruence

1. **Know the definition:** Congruent = same shape and size = can be mapped by rigid motions

2. **Use rigid motions only:** Translation, reflection, rotation. NOT dilation.

3. **Show your work:** Specify which transformation maps one figure to the other.

4. **Check correspondence:** Make sure you're matching vertices correctly in notation.

5. **If stuck, use congruence criteria:** SSS, SAS, ASA, AAS are faster than finding transformations.

6. **Similar ≠ Congruent:** Similar figures have the same shape but not necessarily the same size. Dilations create similar but not congruent figures.

---

# Glide Reflections

## Definition

A **glide reflection** is a composition of a reflection followed by a translation (or vice versa) in a direction parallel to the line of reflection.

**Think of it this way:** Imagine you have a footprint. Reflect it across a line (like a mirror). Then slide it along that same line. That's a glide reflection.

The term "glide" comes from this sliding motion.

## Key Vocabulary

- **Reflection component:** The reflection across the line
- **Translation component:** The translation parallel to the line of reflection
- **Glide reflection** is a rigid motion — it preserves distances and angles

---

## How Glide Reflections Work

In a glide reflection:
1. The line of reflection is fixed
2. The translation is parallel to this line (moves along the line)
3. Order doesn't matter: reflection then translation = translation then reflection

### Coordinate Rule for Glide Reflection

For a glide reflection across the x-axis with translation vector ⟨a, 0⟩:

1. Reflect across x-axis: (x, y) → (x, -y)
2. Translate by ⟨a, 0⟩: (x, -y) → (x + a, -y)

**Combined:** $(x, y) \rightarrow (x + a, -y)$

**General form:** For glide reflection across a line with parallel translation ⟨a, b⟩:
- The translation vector must be parallel to the line of reflection
- This means the translation "slides" along the line

---

## Worked Examples

### Example 1: Glide Reflection Across X-Axis

**Problem:** Apply a glide reflection to point A = (2, 3) where:
- Reflection is across the x-axis
- Translation is by vector ⟨5, 0⟩ (parallel to x-axis)

**Solution:**

**Method 1: Reflect first, then translate**
- Reflect (2, 3) across x-axis: (2, -3)
- Translate (2, -3) by ⟨5, 0⟩: (2 + 5, -3 + 0) = (7, -3)

**Method 2: Translate first, then reflect (should give same answer)**
- Translate (2, 3) by ⟨5, 0⟩: (7, 3)
- Reflect (7, 3) across x-axis: (7, -3) ✓

**Answer: A′ = (7, -3)**

---

### Example 2: Glide Reflection Across Y-Axis

**Problem:** Apply a glide reflection to point B = (1, 4) where:
- Reflection is across the y-axis
- Translation is by vector ⟨0, -2⟩ (parallel to y-axis)

**Solution:**

**Reflect first:**
- Reflect (1, 4) across y-axis: (-1, 4)

**Translate:**
- Translate (-1, 4) by ⟨0, -2⟩: (-1, 4 - 2) = (-1, 2)

**Answer: B′ = (-1, 2)**

---

### Example 3: Glide Reflection with a Diagonal Line

**Problem:** Apply a glide reflection to point C = (3, 1) with:
- Reflection across the line y = x
- Translation by vector ⟨2, 2⟩ (parallel to y = x, since (2,2) goes along the diagonal)

**Solution:**

**Reflect across y = x:**
- (3, 1) → (1, 3)

**Translate by ⟨2, 2⟩:**
- (1, 3) → (1 + 2, 3 + 2) = (3, 5)

**Answer: C′ = (3, 5)**

---

## Glide Reflections in Real Life

Glide reflections appear naturally in patterns:

- **Footprints in sand:** Each footprint is a glide reflection of the previous one
- **Repeating border patterns:** Many decorative patterns use glide reflections
- **Frieze patterns:** Patterns that repeat along a line often involve glide reflections

---

## Common Mistakes and How to Avoid Them

| Mistake | Why It's Wrong | How to Avoid It |
|---------|----------------|-----------------|
| Translation is not parallel to the line | Glide reflections REQUIRE parallel translation | Check: does the translation vector point along the line? |
| Getting the order wrong | You might get lost | It doesn't matter—reflection then translation = translation then reflection |
| Forgetting to apply both transformations | Only reflecting or only translating | Write: Original → After reflection → Final. Two steps! |
| Applying a random translation | The translation must be parallel to the line | If reflecting across x-axis, translate only in x-direction |

---

## Exam Tips for Glide Reflections

1. **Identify the line and translation carefully** — You'll be told which line to reflect across and what translation to apply.

2. **Check that the translation is parallel to the line** — This is what makes it a glide reflection.

3. **You can do either order** — Reflection then translation, or translation then reflection. Pick whichever you find easier.

4. **It's a rigid motion** — Distances and angles are preserved.

5. **Recognize glide reflections in patterns** — If you see a repeated pattern along a line with a "slide," it's likely a glide reflection.

---

# Parallel Lines and Transformations

## Connection to Unit 2 Standards (G.CO.7)

While parallel lines aren't a transformation themselves, transformations help us understand parallel line properties. Specifically:

- **Translations preserve parallelism** — If you translate two parallel lines, they remain parallel
- **Reflections preserve parallelism** — If you reflect two parallel lines across any line, they remain parallel
- **Rotations can change parallelism** — Rotating parallel lines might make them no longer parallel (except for 180° rotation)

---

## Why Parallel Lines Stay Parallel Under Translations

**Theorem:** If two lines are parallel and you translate both by the same vector, the image lines are parallel.

**Reason:**
- Translations move every point the same distance in the same direction
- If one line is parallel to another, this property is preserved because all points move identically
- The slope (direction) of both lines remains unchanged

**Example:**
- Original: Line 1 is y = 2x + 3, Line 2 is y = 2x - 5 (parallel, same slope)
- After translation by ⟨1, 2⟩:
  - Line 1 becomes y = 2x + (3 + 2 - 2·1) = 2x + 3 (same line!)
  - Line 2 becomes y = 2x + (-5 + 2 - 2·1) = 2x - 5 (same line!)

Wait, that's not right for translations of general lines. Let me reconsider.

Actually, a translation moves lines to parallel positions:
- Line y = 2x + 3 translates to a new line with same slope 2, so it's parallel to itself
- All parallel lines remain parallel to each other

---

## Parallel Lines and Alternate Interior Angles

**Theorem (Standard G.CO.7):** When a transversal crosses two parallel lines:
- **Alternate interior angles are equal**
- **Corresponding angles are equal**
- **Co-interior (same-side interior) angles are supplementary**

**Connection to transformations:**
- These angle relationships can be proven using reflection
- If you reflect one of the parallel lines across the transversal, alternate interior angles map to each other
- This provides a transformation-based proof of the angle relationships

---

## Worked Example: Using Transformations to Prove Angle Relationships

**Problem:** Prove that alternate interior angles are equal when a transversal crosses parallel lines using a reflection.

**Solution:**

**Given:** Lines l and m are parallel, transversal t crosses both.

**Prove:** Alternate interior angles are equal.

**Proof using reflection:**
1. Reflect the configuration across the transversal t
2. Since lines are parallel and the transversal crosses both, the reflection maps:
   - One intersection point to a point on the other line
   - The angle at one intersection to a corresponding angle
3. Under reflection, angles are preserved
4. Alternate interior angles are equal because the reflection maps one to the other

This is a more intuitive (though less rigorous) proof of the parallel line angle theorem.

---

## Exam Tips for Parallel Lines and Transformations

1. **Translations preserve parallelism** — Remember this for proofs and problems about parallel lines.

2. **Use reflections for angle proofs** — Reflecting across a transversal can help you establish angle relationships.

3. **Rotations usually don't preserve parallelism** — Exception: 180° rotations do preserve some parallel relationships.

4. **Connect to angle theorems** — When parallel lines are involved, think about corresponding angles, alternate interior angles, etc.

---

# Study Strategies & Exam Tips

## General Strategy

### 1. Master the Coordinate Rules

This is non-negotiable. You should be able to write these from memory:

| Transformation | Rule |
|---|---|
| Translation by ⟨a, b⟩ | (x, y) → (x + a, y + b) |
| Reflection over x-axis | (x, y) → (x, -y) |
| Reflection over y-axis | (x, y) → (-x, y) |
| Reflection over y = x | (x, y) → (y, x) |
| Reflection over y = -x | (x, y) → (-y, -x) |
| 90° CCW rotation | (x, y) → (-y, x) |
| 90° CW rotation | (x, y) → (y, -x) |
| 180° rotation | (x, y) → (-x, -y) |
| Dilation, scale factor k | (x, y) → (kx, ky) |

---

### 2. Sketch Everything

When you see a transformation problem:
1. Sketch the pre-image
2. Sketch the image
3. Verify that the transformation makes sense visually

Many errors are caught this way.

---

### 3. Know What's Preserved

- **Rigid motions:** Preserve distances, angles, and size
- **Dilations:** Preserve angles and shape, but not size
- **Glide reflections:** Preserve distances and angles (rigid)

---

### 4. Practice Multi-Step Problems

- Composition of transformations
- Proving congruence
- Identifying transformations from coordinates

---

## Common Problem Types

### Type 1: "Apply this transformation to these coordinates"

**Strategy:**
1. Identify the transformation type
2. Write the coordinate rule
3. Substitute each coordinate
4. Verify by sketching

---

### Type 2: "What transformation maps figure A to figure B?"

**Strategy:**
1. Compare the two figures
2. Check if they're the same size (rigid or dilation?)
3. Compare orientations (reflected? rotated?)
4. Find the specific transformation rule
5. Verify with at least two points

---

### Type 3: "Prove these figures are congruent"

**Strategy:**
1. Verify they have the same shape and size
2. Find a sequence of rigid motions that maps one to the other
3. Show that ALL vertices/points map correctly
4. State the conclusion

---

### Type 4: "Identify lines/rotational symmetry"

**Strategy:**
1. Sketch the figure
2. For line symmetry: try folding along potential lines
3. For rotational symmetry: try rotating by 90°, 120°, 60°, etc.
4. Count how many times it matches itself

---

## Exam Day Tips

1. **Bring a straightedge and ruler** — You'll need to sketch figures accurately

2. **Take time to draw** — A quick sketch prevents many errors

3. **Show all work** — Partial credit requires showing your process

4. **Double-check coordinates** — Transcription errors happen; verify you copied coordinates correctly

5. **Use test points** — When in doubt, test your transformation rule with a simple point like (1, 0) or (0, 1)

6. **Watch for negative signs** — They're easy to miss but change everything

7. **State your answer clearly** — Don't just do calculations; write "The image of A is A′ = (3, 5)"

8. **Time management:**
   - Coordinate rule problems: ~2 minutes
   - Proofs: ~5 minutes
   - Multi-step problems: ~8-10 minutes

---

## Key Formulas to Memorize

**The transformation rules above are essential.** Additionally:

- Scale factor k and distance: New distance = k × Original distance
- Order of rotational symmetry: n = 360° / rotation angle
- Composition: Do transformations in order, using the output of one as input to the next
- For non-origin centers: Use translate-transform-translate-back process

---

## Final Checklist

Before the exam, ensure you can:

- [ ] Write all coordinate rules from memory
- [ ] Apply a transformation to a single point in < 30 seconds
- [ ] Apply a transformation to a figure (multiple points) in < 2 minutes
- [ ] Identify whether a transformation is rigid or non-rigid
- [ ] Determine what's preserved and what's not for each transformation
- [ ] Compose transformations in the correct order
- [ ] Prove congruence using transformations
- [ ] Identify lines of symmetry in common figures
- [ ] Determine the order of rotational symmetry
- [ ] Solve problems involving parallel lines and transformations
- [ ] Explain why certain properties are preserved

---

## Additional Resources for Practice

- Draw figures on coordinate planes and apply transformations
- Use geometry software (GeoGebra) to visualize transformations
- Work through old exams and practice problems
- Teach someone else—explaining helps cement understanding
- Create flashcards with rules on one side and examples on the other

---

## Conclusion

Unit 2: Transformations is foundational for all geometry that follows. The key is to:

1. **Understand the rules deeply**, not just memorize them
2. **Practice applying them** to many different problems
3. **Connect to congruence** and similarity
4. **Visualize** everything you do
5. **Verify your work** with sketches and test points

With solid mastery of these concepts, you'll be prepared for more advanced geometry topics and be able to solve complex multi-step problems with confidence.

---

**Good luck with your studies! Remember: geometry is visual. Sketch everything, and the rules will make sense.**
