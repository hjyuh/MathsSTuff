# Unit 1: Foundations of Geometry — Complete Study Guide

## Table of Contents
1. [Basic Building Blocks](#basic-building-blocks)
2. [Angles and Angle Relationships](#angles-and-angle-relationships)
3. [Parallel Lines Cut by a Transversal](#parallel-lines-cut-by-a-transversal)
4. [Distance and Midpoint Formulas](#distance-and-midpoint-formulas)
5. [Slope and Lines in Coordinate Geometry](#slope-and-lines-in-coordinate-geometry)
6. [Compass and Straightedge Constructions](#compass-and-straightedge-constructions)
7. [Proving Theorems Using Coordinate Geometry](#proving-theorems-using-coordinate-geometry)

---

## Basic Building Blocks

### What Are Points, Lines, Planes, Segments, and Rays?

Geometry is the study of shapes, sizes, and positions. Everything in geometry is built from a few fundamental objects that we need to understand before we can do anything else.

#### **Points**

**Definition:** A point is a location in space. It has no size, no length, no width — it's just a position.

**Key Idea:** Think of a point like a dot on paper, but mathematically, it's infinitely small (it has zero dimensions).

**Notation:** We name points using capital letters. Example: Point A, Point P, Point M.

**Visual:**
```
    • A
```

**In Plain English:** If you poke your pencil on a piece of paper, that tiny hole is approximately a point.

---

#### **Lines**

**Definition:** A line is a straight path that extends infinitely in both directions. It has no endpoints and no thickness.

**Key Idea:** A line is one-dimensional — it only has length. You can travel along it forever in either direction.

**Notation:**
- We name lines using two points on the line with a line symbol above them: $\overleftrightarrow{AB}$ (read as "line AB")
- Or we can use a lowercase letter: line $l$, line $m$, etc.

**Visual:**
```
    A ————————————————— B
    (this extends forever in both directions)
```

**In Plain English:** Imagine taking a piece of string and extending it infinitely in both directions. That's a line.

**Important Principle:** Through any two distinct points, there is exactly one line. This is one of the fundamental axioms (basic rules) of geometry.

---

#### **Rays**

**Definition:** A ray is a part of a line that starts at a point (called the endpoint) and extends infinitely in one direction.

**Key Idea:** A ray has exactly one endpoint, and it goes on forever in one direction.

**Notation:** We write $\overrightarrow{AB}$, which means "ray starting at A and passing through B." The first letter is always the endpoint.

**Visual:**
```
    A ————————————————————→ B
    (starts at A, goes through B, continues forever)
```

**In Plain English:** Imagine a beam of light from a flashlight — it starts at the bulb (endpoint) and travels outward forever.

---

#### **Line Segments**

**Definition:** A line segment is part of a line that has two endpoints. It does not extend beyond these endpoints.

**Key Idea:** Unlike a line (infinite), a segment is finite. It has a definite beginning and a definite end.

**Notation:** We write $\overline{AB}$ to mean "segment AB," with endpoints A and B.

**Visual:**
```
    A ————————————————— B
    (finite — has both endpoints)
```

**In Plain English:** If you take a piece of string and cut it at both ends, you have a segment.

**The Length:** The length of segment $\overline{AB}$ is written as $AB$ (without the overline). For example, if the segment is 5 cm long, we write $AB = 5$ cm.

---

#### **Planes**

**Definition:** A plane is a flat surface that extends infinitely in all directions. It has no thickness.

**Key Idea:** A plane is two-dimensional — it has length and width, but no height. It's like an infinite, flat table.

**Notation:**
- We name planes using three non-collinear points: Plane ABC
- Or we can use a capital letter: Plane P

**Visual (3D representation):**
```
    A ___________
    /|          /|
   / B________ /  |
  |  |       | C |
  |  |_______|___|
  | /        |  /
  |/         | /
  |__________|/

  (This shows a plane — imagine it extends forever)
```

**In Plain English:** The surface of your desk, or the ground you stand on, is approximately a plane (though it's not infinite).

**Important Principle:** Through any three non-collinear points (three points not all on the same line), there is exactly one plane.

---

#### **Collinear and Coplanar Points**

**Collinear Points:** Points that lie on the same line.
- Example: If points A, B, and C are all on line $\overleftrightarrow{AB}$, they are collinear.

**Coplanar Points:** Points that lie on the same plane.
- Example: If all your points are on your desk (Plane P), they are coplanar.

**Key Difference:** Any two points are always collinear (you can draw a line through them). But three points might or might not be collinear.

---

### Summary of Basic Notation

| Object | Notation | Meaning |
|--------|----------|---------|
| Point A | A | A single location |
| Line through A and B | $\overleftrightarrow{AB}$ | Infinite line in both directions |
| Ray starting at A through B | $\overrightarrow{AB}$ | Starts at A, goes through B forever |
| Segment from A to B | $\overline{AB}$ | Only the part between A and B |
| Length of segment AB | $AB$ | The distance between A and B |
| Plane containing A, B, C | Plane ABC | Flat surface through three points |

---

---

## Angles and Angle Relationships

### What Is an Angle?

**Definition:** An angle is formed by two rays that share the same endpoint (called the vertex).

**Key Idea:** When two rays start at the same point and go in different directions, the "opening" between them is the angle.

**Notation:**
- We write $\angle ABC$ to mean "the angle at B, formed by ray $\overrightarrow{BA}$ and ray $\overrightarrow{BC}$"
- The vertex (the middle letter) is always the point where the rays meet
- Or we can write just $\angle B$ if it's clear which angle we're talking about

**Visual:**
```
         A
        /
       /
      / ← angle
     /
    B ————— C
    ↑
  vertex
```

**In Plain English:** If you hold two pencils at one end and spread them apart, the space between them is an angle.

---

### Measuring Angles: Degrees

Angles are measured in **degrees**, written with the symbol °.

**Why degrees?** It's historical — people chose to divide a complete rotation into 360 parts, called degrees. So:
- A full rotation = 360°
- Half a rotation = 180°
- A quarter rotation = 90°

**Key Fact:** Every angle has a measure between 0° and 360°. When we talk about angles in geometry class, we usually work with angles between 0° and 180°.

---

### Types of Angles (by Measure)

#### **Acute Angle**
- **Definition:** An angle that measures more than 0° but less than 90°
- **Notation:** $0° < \text{angle} < 90°$
- **Example:** 45°, 60°, 89°
- **Visual:**
```
     /
    / ← acute
   /___
   small opening
```

#### **Right Angle**
- **Definition:** An angle that measures exactly 90°
- **Notation:** We write a small square at the vertex to show 90°
- **Example:** The corner of a piece of paper, the corner of a room
- **Visual:**
```
    |
    |
    |___
    90°
```

#### **Obtuse Angle**
- **Definition:** An angle that measures more than 90° but less than 180°
- **Notation:** $90° < \text{angle} < 180°$
- **Example:** 120°, 135°, 179°
- **Visual:**
```
    \     /
     \   /
      \ /
       | ← obtuse
       large opening
```

#### **Straight Angle**
- **Definition:** An angle that measures exactly 180°
- **Key Idea:** The two rays form a straight line
- **Example:** A line is a straight angle
- **Visual:**
```
    ——————————
    180° (straight line)
```

#### **Reflex Angle**
- **Definition:** An angle that measures more than 180° but less than 360°
- **Key Idea:** It's the "larger" angle between two rays
- **Example:** 270°, 350°
- **Visual:**
```
    Ray 1
       ↓
      /
     /
    /___→ Ray 2

    The reflex angle is the outer part (more than 180°)
```

**In Honors Geometry, we rarely work with reflex angles, but it's good to know they exist.**

---

### Angle Pairs and Their Relationships

#### **Complementary Angles**

**Definition:** Two angles are complementary if their measures add up to 90°.

**Notation:** If $\angle A$ and $\angle B$ are complementary, then $m\angle A + m\angle B = 90°$ (where $m\angle$ means "measure of angle")

**Key Idea:** Complementary angles don't have to be adjacent (next to each other) or even in the same figure.

**Example 1:**
- $\angle A = 30°$ and $\angle B = 60°$
- $30° + 60° = 90°$
- So $\angle A$ and $\angle B$ are complementary

**Example 2:**
- Two angles inside a right triangle (that aren't the right angle itself) are always complementary
- If one acute angle is 35°, the other must be 55° (because they add to 90°)

**Practice Tip:** If you see "complementary," think "**C**omplement → 90 → **C**orner of a square"

---

#### **Supplementary Angles**

**Definition:** Two angles are supplementary if their measures add up to 180°.

**Notation:** If $\angle A$ and $\angle B$ are supplementary, then $m\angle A + m\angle B = 180°$

**Key Idea:** Like complementary angles, supplementary angles don't have to be adjacent.

**Example 1:**
- $\angle A = 120°$ and $\angle B = 60°$
- $120° + 60° = 180°$
- So $\angle A$ and $\angle B$ are supplementary

**Example 2:**
- Angles on a straight line are supplementary
- If you have a straight line and draw a ray from it, the two angles formed are supplementary (they add to 180°)

**Practice Tip:** If you see "supplementary," think "**S**upplementary → 180 → **S**traight line"

---

#### **Vertical Angles (Vertically Opposite Angles)**

**Definition:** When two lines intersect (cross), they form four angles. The angles that are opposite each other (not adjacent) are called vertical angles.

**Key Theorem:** **Vertical angles are always congruent** (equal in measure).

**Visual:**
```
         2 | 1
          \|/
       ———┼———
          /|\
         3 | 4

Vertical angle pairs:
- Angles 1 and 3 are vertical angles
- Angles 2 and 4 are vertical angles

Therefore: m∠1 = m∠3 and m∠2 = m∠4
```

**Why is this true?**
- Angles 1 and 2 form a straight line, so they're supplementary: $m\angle 1 + m\angle 2 = 180°$
- Angles 2 and 3 form a straight line, so they're supplementary: $m\angle 2 + m\angle 3 = 180°$
- If we subtract the second equation from the first: $(m\angle 1 + m\angle 2) - (m\angle 2 + m\angle 3) = 0$
- This simplifies to: $m\angle 1 = m\angle 3$

**Worked Example:**
Two lines intersect. One of the angles formed is 65°. What are all four angles?

**Solution:**
- If one angle is 65°, its vertical angle is also 65°
- The angles adjacent to 65° are supplementary to it: $180° - 65° = 115°$
- The other two angles are: 65°, 115°, 65°, 115° (going around)

---

#### **Linear Pair**

**Definition:** A linear pair is two adjacent angles that form a straight line.

**Key Property:** The angles in a linear pair are supplementary (they add up to 180°).

**Visual:**
```
          |
         /  ← Angle 1
        /
   ————|———————  ← Straight line
        \
         \  ← Angle 2
          |

Angles 1 and 2 are a linear pair.
m∠1 + m∠2 = 180°
```

**In Plain English:** If you draw any line, then draw a ray from any point on that line, you create a linear pair.

**Worked Example:**
Two angles form a linear pair. One angle measures 48°. What is the measure of the other angle?

**Solution:**
- Linear pair means the angles add to 180°
- Let the unknown angle be $x$
- $48° + x = 180°$
- $x = 180° - 48° = 132°$

---

#### **Adjacent Angles**

**Definition:** Two angles are adjacent if they:
1. Share the same vertex
2. Share a common side (ray)
3. Do not overlap

**Visual:**
```
       Ray 1
        /
       /
      / ← Angle A
     /___Ray 2 (common side)
        \
         \ ← Angle B
          \
           Ray 3

Angles A and B are adjacent (they share Ray 2)
```

**Key Idea:** Adjacent angles can be complementary, supplementary, or neither. The word "adjacent" just describes their position, not their sum.

---

### Summary Table: Angle Relationships

| Relationship | Condition | Angles are... |
|--------------|-----------|---------------|
| Complementary | Sum to 90° | Two different angles |
| Supplementary | Sum to 180° | Two different angles |
| Vertical | Opposite when lines intersect | Congruent ✓ |
| Linear Pair | Adjacent, form a line | Supplementary |
| Adjacent | Share vertex and side | Position only (no sum rule) |

---

---

## Parallel Lines Cut by a Transversal

### What Are Parallel Lines?

**Definition:** Two lines are parallel if they are in the same plane and never intersect (no matter how far they extend).

**Notation:** We write $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$ to mean "line AB is parallel to line CD"

**Key Idea:** Parallel lines are "the same distance apart" at every point. If you measure the perpendicular distance between them at any location, it's the same everywhere.

**Visual:**
```
Line 1: ——————————————————→
Line 2: ——————————————————→
(both going the same direction, never meeting)
```

**In Plain English:** Train tracks are parallel. The two rails run in the same direction and are always the same distance apart.

---

### What Is a Transversal?

**Definition:** A transversal is a line that intersects two or more other lines at different points.

**Key Idea:** When a transversal crosses two parallel lines, it creates a special pattern of angles that we can use to solve problems.

**Visual:**
```
Line 1:    ——————1|2——————
           ———————|———————
Transversal       4|3
           ———————|———————
Line 2:    ——————5|6——————
           ———————|———————
                8|7

The transversal crosses both parallel lines.
This creates 8 angles total (4 at each intersection).
```

---

### The 8 Angles Created

When a transversal crosses two parallel lines, it creates 8 angles. Here's what they're called:

**At the first intersection (Line 1 and Transversal):**
- Angles 1, 2, 3, 4

**At the second intersection (Line 2 and Transversal):**
- Angles 5, 6, 7, 8

**The angles have special names based on their position:**

#### **Interior Angles**
Angles between the two parallel lines: **3, 4, 5, 6**

#### **Exterior Angles**
Angles outside the two parallel lines: **1, 2, 7, 8**

#### **Angles on the Same Side of the Transversal**
- Left side: **3, 4, 5, 6** (actually these are interior, but location matters)
- Right side: **1, 2, 7, 8** (actually these are exterior, but location matters)

**Visual with labels:**
```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————
       5   |  6
      _____|_____  ← Line 2
        7  |  8

Interior angles: 3, 4, 5, 6 (between the lines)
Exterior angles: 1, 2, 7, 8 (outside the lines)
```

---

### The 8 Angle Relationships When Lines Are Parallel

When the two lines **are parallel**, these special relationships always hold:

#### **1. Corresponding Angles Are Congruent**

**Definition:** Corresponding angles are angles in the same relative position at each intersection.

**Which angles?**
- Angles 1 and 5
- Angles 2 and 6
- Angles 3 and 7
- Angles 4 and 8

**The Rule:** If the two lines are parallel, then corresponding angles are equal.
$$m\angle 1 = m\angle 5$$
$$m\angle 2 = m\angle 6$$
$$m\angle 3 = m\angle 7$$
$$m\angle 4 = m\angle 8$$

**Visual:**
```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————
       5   |  6
      _____|_____  ← Line 2
        7  |  8

Corresponding angles (same position):
1 ↔ 5, 2 ↔ 6, 3 ↔ 7, 4 ↔ 8
All are EQUAL when lines are parallel
```

**In Plain English:** Imagine the transversal is a camera that takes the same picture at both intersections. Corresponding angles would be in the exact same spot in each picture.

---

#### **2. Alternate Interior Angles Are Congruent**

**Definition:** Alternate interior angles are interior angles (between the two lines) on opposite sides of the transversal.

**Which angles?**
- Angles 4 and 5 (one on each side of the transversal, both interior)
- Angles 3 and 6 (one on each side of the transversal, both interior)

**The Rule:** If the two lines are parallel, then alternate interior angles are equal.
$$m\angle 4 = m\angle 5$$
$$m\angle 3 = m\angle 6$$

**Visual:**
```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————  ← Between the lines
       5   |  6
      _____|_____  ← Line 2
        7  |  8

Alternate interior angles:
3 ↔ 6 (alternate means opposite sides, interior means between lines)
4 ↔ 5 (alternate means opposite sides, interior means between lines)
All are EQUAL when lines are parallel
```

**In Plain English:** These angles are on opposite sides of the transversal and both live "inside" (between) the two parallel lines. The word "alternate" means they switch sides.

---

#### **3. Alternate Exterior Angles Are Congruent**

**Definition:** Alternate exterior angles are exterior angles (outside both lines) on opposite sides of the transversal.

**Which angles?**
- Angles 1 and 8 (opposite sides, both exterior)
- Angles 2 and 7 (opposite sides, both exterior)

**The Rule:** If the two lines are parallel, then alternate exterior angles are equal.
$$m\angle 1 = m\angle 8$$
$$m\angle 2 = m\angle 7$$

**Visual:**
```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————
       5   |  6
      _____|_____  ← Line 2
        7  |  8

Alternate exterior angles:
1 ↔ 8 (alternate means opposite sides, exterior means outside the lines)
2 ↔ 7 (alternate means opposite sides, exterior means outside the lines)
All are EQUAL when lines are parallel
```

**In Plain English:** These angles are on opposite sides of the transversal and both live "outside" both parallel lines.

---

#### **4. Co-Interior Angles Are Supplementary**
*(Also called: Consecutive Interior Angles or Same-Side Interior Angles)*

**Definition:** Co-interior angles are interior angles (between the two lines) on the **same side** of the transversal.

**Which angles?**
- Angles 3 and 5 (same side of transversal, both interior)
- Angles 4 and 6 (same side of transversal, both interior)

**The Rule:** If the two lines are parallel, then co-interior angles are supplementary (add to 180°).
$$m\angle 3 + m\angle 5 = 180°$$
$$m\angle 4 + m\angle 6 = 180°$$

**Visual:**
```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————  ← Between the lines
       5   |  6
      _____|_____  ← Line 2
        7  |  8

Co-interior angles (same side interior):
3 & 5 on the left → add to 180°
4 & 6 on the right → add to 180°
```

**In Plain English:** These angles are between the two lines and on the same side of the transversal. They're "partners" in the sense that they always add to 180°.

---

### The Converse: Using Angle Relationships to Prove Lines Are Parallel

Here's something important: We've been saying "IF the lines are parallel, THEN these angle relationships hold." But the opposite is also true:

**If the angle relationships hold, THEN the lines are parallel.**

**The converses:**

| Angle Relationship | If This is True... | Then the Lines Are Parallel |
|-------------------|------------------|---------------------------|
| Corresponding angles are congruent | $m\angle 1 = m\angle 5$ | Yes ✓ |
| Alternate interior angles are congruent | $m\angle 4 = m\angle 5$ | Yes ✓ |
| Alternate exterior angles are congruent | $m\angle 1 = m\angle 8$ | Yes ✓ |
| Co-interior angles are supplementary | $m\angle 3 + m\angle 5 = 180°$ | Yes ✓ |

**In Plain English:** If you can show that any ONE of these angle relationships is true, you've proven the lines are parallel.

---

### Worked Examples: Parallel Lines and Transversals

**Example 1: Finding Missing Angles**

Two parallel lines are cut by a transversal. If angle 1 measures 75°, find the measures of angles 2, 3, 4, 5, 6, 7, and 8.

```
        1  |  2
      _____|_____  ← Line 1
       3   |  4
    ——————|——————
       5   |  6
      _____|_____  ← Line 2
        7  |  8
```

**Solution:**

Given: $m\angle 1 = 75°$

Step 1: Find angle 2 (linear pair with angle 1)
$$m\angle 1 + m\angle 2 = 180°$$
$$75° + m\angle 2 = 180°$$
$$m\angle 2 = 105°$$

Step 2: Find angle 3 (vertical angle with angle 1)
$$m\angle 3 = m\angle 1 = 75°$$ (vertical angles)

Step 3: Find angle 4 (linear pair with angle 3)
$$m\angle 3 + m\angle 4 = 180°$$
$$75° + m\angle 4 = 180°$$
$$m\angle 4 = 105°$$

Step 4: Find angles at line 2 using parallel line relationships
$$m\angle 5 = m\angle 1 = 75°$$ (corresponding angles with parallel lines)
$$m\angle 6 = m\angle 2 = 105°$$ (corresponding angles with parallel lines)
$$m\angle 7 = m\angle 3 = 75°$$ (corresponding angles with parallel lines)
$$m\angle 8 = m\angle 4 = 105°$$ (corresponding angles with parallel lines)

**Check:** Angles alternate between 75° and 105° ✓

**Answer:** $\angle 2 = 105°$, $\angle 3 = 75°$, $\angle 4 = 105°$, $\angle 5 = 75°$, $\angle 6 = 105°$, $\angle 7 = 75°$, $\angle 8 = 105°$

---

**Example 2: Using Angle Relationships to Prove Lines Are Parallel**

A transversal crosses two lines. The transversal makes a 58° angle with the first line and a 58° angle with the second line (in corresponding positions). Are the two lines parallel?

**Solution:**

The two angles are in corresponding positions and have equal measures (both 58°).

Since corresponding angles are congruent, the lines are parallel.

**Answer:** Yes, the lines are parallel. ✓

---

**Example 3: Finding Unknown Angles**

Two parallel lines are cut by a transversal. One of the co-interior angles measures 112°. What is the measure of the other co-interior angle?

**Solution:**

Co-interior angles are supplementary when lines are parallel:
$$m\angle_1 + m\angle_2 = 180°$$
$$112° + m\angle_2 = 180°$$
$$m\angle_2 = 180° - 112° = 68°$$

**Answer:** The other co-interior angle measures 68°.

---

### Common Mistakes to Avoid

**Mistake 1:** Confusing which angles are alternate interior vs. corresponding
- **Fix:** Remember: Alternate means opposite sides of transversal. Interior means between the two lines.

**Mistake 2:** Forgetting that alternate exterior angles exist
- **Fix:** Exterior angles are just as important as interior angles when determining if lines are parallel.

**Mistake 3:** Not recognizing when angles are vertical angles
- **Fix:** Always look for opposite angles when two lines intersect — they're automatically equal.

**Mistake 4:** Adding angles that should be equal instead of setting them equal
- **Fix:** When you have corresponding angles or alternate angles, they're **equal** (not supplementary) when lines are parallel.

---

---

## Distance and Midpoint Formulas

### The Distance Formula: Finding the Distance Between Two Points

#### **Where Does the Distance Formula Come From?**

Imagine you have two points on a coordinate plane: Point A at $(x_1, y_1)$ and Point B at $(x_2, y_2)$.

To find the straight-line distance between them, we can create a right triangle:

**Visual:**
```
        B (x₂, y₂)
        *
        |\
        | \  ← distance (hypotenuse)
        |  \
        |   \
    y₂-y₁ |    \
        |      \
        |_______\
        A -------C

        x₂-x₁

The horizontal leg has length |x₂ - x₁|
The vertical leg has length |y₂ - y₁|
The hypotenuse is the distance we want to find
```

**Using the Pythagorean Theorem:**

The Pythagorean theorem states: $a^2 + b^2 = c^2$, where $a$ and $b$ are the legs of a right triangle and $c$ is the hypotenuse.

Applying this to our triangle:
$$(x_2 - x_1)^2 + (y_2 - y_1)^2 = d^2$$

Taking the square root of both sides:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**This is the Distance Formula.**

---

#### **The Distance Formula (Official)**

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**What each variable means:**
- $d$ = the distance (length of the segment)
- $(x_1, y_1)$ = the coordinates of the first point
- $(x_2, y_2)$ = the coordinates of the second point
- $(x_2 - x_1)$ = the horizontal distance (change in $x$)
- $(y_2 - y_1)$ = the vertical distance (change in $y$)

**Key Idea:** It doesn't matter which point you call "1" and which you call "2." The answer will be the same because we're squaring the differences.

---

#### **Worked Examples: Distance Formula**

**Example 1: Simple Integer Coordinates**

Find the distance between Point A(1, 2) and Point B(4, 6).

**Solution:**

Identify your points:
- Point A: $(x_1, y_1) = (1, 2)$
- Point B: $(x_2, y_2) = (4, 6)$

Plug into the formula:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
$$d = \sqrt{(4 - 1)^2 + (6 - 2)^2}$$
$$d = \sqrt{(3)^2 + (4)^2}$$
$$d = \sqrt{9 + 16}$$
$$d = \sqrt{25}$$
$$d = 5$$

**Answer:** The distance is 5 units.

---

**Example 2: Negative Coordinates**

Find the distance between Point A(-3, 1) and Point B(2, -2).

**Solution:**

Identify your points:
- Point A: $(x_1, y_1) = (-3, 1)$
- Point B: $(x_2, y_2) = (2, -2)$

Plug into the formula:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
$$d = \sqrt{(2 - (-3))^2 + (-2 - 1)^2}$$
$$d = \sqrt{(2 + 3)^2 + (-3)^2}$$
$$d = \sqrt{(5)^2 + (-3)^2}$$
$$d = \sqrt{25 + 9}$$
$$d = \sqrt{34}$$

**Answer:** The distance is $\sqrt{34}$ units (or approximately 5.83 units).

---

**Example 3: Finding an Approximate Decimal Answer**

Find the distance between Point C(0, 0) and Point D(5, 12). Round to the nearest hundredth.

**Solution:**

Identify your points:
- Point C: $(x_1, y_1) = (0, 0)$
- Point D: $(x_2, y_2) = (5, 12)$

Plug into the formula:
$$d = \sqrt{(5 - 0)^2 + (12 - 0)^2}$$
$$d = \sqrt{25 + 144}$$
$$d = \sqrt{169}$$
$$d = 13$$

**Answer:** The distance is exactly 13 units.

---

**Example 4: Verifying a Right Triangle**

Three points are P(0, 0), Q(3, 4), and R(3, 0). Verify that these points form a right triangle.

**Solution:**

For a right triangle, we need the Pythagorean theorem to hold: $a^2 + b^2 = c^2$

Find all three distances:

Distance PQ:
$$PQ = \sqrt{(3 - 0)^2 + (4 - 0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

Distance PR:
$$PR = \sqrt{(3 - 0)^2 + (0 - 0)^2} = \sqrt{9 + 0} = 3$$

Distance QR:
$$QR = \sqrt{(3 - 3)^2 + (0 - 4)^2} = \sqrt{0 + 16} = 4$$

Check if Pythagorean theorem holds:
$$PR^2 + QR^2 = 3^2 + 4^2 = 9 + 16 = 25 = 5^2 = PQ^2$$ ✓

**Answer:** Yes, these points form a right triangle. (In fact, this is a 3-4-5 right triangle!)

---

### The Midpoint Formula: Finding the Point Exactly in the Middle

#### **What Is a Midpoint?**

The midpoint is the point that is exactly halfway between two given points.

**Key Idea:** If you have a segment from A to B, the midpoint M is the same distance from A as it is from B.

**Visual:**
```
    A ————————— M ————————— B
    |←—distance d—→|←—distance d—→|

    M is the midpoint
```

---

#### **The Midpoint Formula (Official)**

If you have two points $(x_1, y_1)$ and $(x_2, y_2)$, the midpoint M is:

$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

**What it means:**
- The $x$-coordinate of the midpoint is the average of the two $x$-coordinates
- The $y$-coordinate of the midpoint is the average of the two $y$-coordinates

**In Plain English:** To find the midpoint, add the $x$-coordinates and divide by 2, then add the $y$-coordinates and divide by 2.

---

#### **Why Does This Work?**

The midpoint should be at the same distance from each endpoint. If we average the coordinates:
- The average of the $x$-coordinates gives us the $x$-value halfway between
- The average of the $y$-coordinates gives us the $y$-value halfway between

This places us equidistant from both points.

---

#### **Worked Examples: Midpoint Formula**

**Example 1: Simple Positive Coordinates**

Find the midpoint of segment $\overline{AB}$ where A(2, 4) and B(8, 10).

**Solution:**

Plug into the midpoint formula:
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$
$$M = \left(\frac{2 + 8}{2}, \frac{4 + 10}{2}\right)$$
$$M = \left(\frac{10}{2}, \frac{14}{2}\right)$$
$$M = (5, 7)$$

**Check:**
- Distance from A(2,4) to M(5,7): $\sqrt{(5-2)^2 + (7-4)^2} = \sqrt{9+9} = \sqrt{18} = 3\sqrt{2}$
- Distance from M(5,7) to B(8,10): $\sqrt{(8-5)^2 + (10-7)^2} = \sqrt{9+9} = \sqrt{18} = 3\sqrt{2}$ ✓

**Answer:** The midpoint is M(5, 7).

---

**Example 2: Negative and Decimal Coordinates**

Find the midpoint of segment $\overline{CD}$ where C(-6, -3) and D(4, 9).

**Solution:**

$$M = \left(\frac{-6 + 4}{2}, \frac{-3 + 9}{2}\right)$$
$$M = \left(\frac{-2}{2}, \frac{6}{2}\right)$$
$$M = (-1, 3)$$

**Answer:** The midpoint is M(-1, 3).

---

**Example 3: Finding an Endpoint Using the Midpoint**

The midpoint of segment $\overline{PQ}$ is M(5, 2). If P is at (-1, 4), find the coordinates of Q.

**Solution:**

We know: $M = \left(\frac{x_P + x_Q}{2}, \frac{y_P + y_Q}{2}\right)$

Substitute what we know:
$$(5, 2) = \left(\frac{-1 + x_Q}{2}, \frac{4 + y_Q}{2}\right)$$

For the $x$-coordinate:
$$5 = \frac{-1 + x_Q}{2}$$
$$10 = -1 + x_Q$$
$$x_Q = 11$$

For the $y$-coordinate:
$$2 = \frac{4 + y_Q}{2}$$
$$4 = 4 + y_Q$$
$$y_Q = 0$$

**Answer:** Q is at (11, 0).

---

**Example 4: Three Points on a Line**

Point A is at (2, 3) and Point B is at (8, 9). Point C is on segment $\overline{AB}$ and is 1/3 of the way from A to B. Find the coordinates of C.

**Solution:**

Since C is 1/3 of the way from A to B:
- The horizontal distance from A to B is: $8 - 2 = 6$
- 1/3 of this distance is: $6 \times \frac{1}{3} = 2$
- So the $x$-coordinate of C is: $2 + 2 = 4$

- The vertical distance from A to B is: $9 - 3 = 6$
- 1/3 of this distance is: $6 \times \frac{1}{3} = 2$
- So the $y$-coordinate of C is: $3 + 2 = 5$

**Answer:** C is at (4, 5).

---

### Common Mistakes to Avoid

**Mistake 1:** Forgetting to square both the $x$ and $y$ differences in the distance formula
- **Fix:** Write out the full formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ — both differences are squared.

**Mistake 2:** Not taking the square root in the distance formula
- **Fix:** After adding the squared differences, you MUST take the square root. The distance formula has a square root.

**Mistake 3:** Mixing up the order of points in distance formula
- **Fix:** It doesn't matter — squaring removes any negative signs, so you'll get the same answer either way.

**Mistake 4:** Forgetting to divide by 2 in the midpoint formula
- **Fix:** The midpoint formula requires you to **average** the coordinates, which means dividing by 2.

**Mistake 5:** Using the midpoint formula when you need distance, or vice versa
- **Fix:** Distance formula has a square root; midpoint formula has averages. They're different!

---

---

## Slope and Lines in Coordinate Geometry

### Understanding Slope: The Steepness of a Line

#### **What Is Slope?**

Slope is a number that describes how steep a line is. It tells you how much a line goes up (or down) as you move from left to right.

**In Plain English:** Imagine walking along a hill. The slope tells you how steep the hill is.

---

#### **The Slope Formula**

If you have two points on a line: $(x_1, y_1)$ and $(x_2, y_2)$, the slope $m$ is:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\text{rise}}{\text{run}}$$

**What this means:**
- **Rise** = the change in $y$ (how far up or down)
- **Run** = the change in $x$ (how far left or right)
- **Slope** = rise ÷ run

**Visual:**
```
        (x₂, y₂)
           •
           |\
           | \
    rise   |  \
  (y₂-y₁) |   \
           |    •
           |    (x₁, y₁)
           |______|
             run
          (x₂-x₁)

    slope = rise/run
```

---

#### **Interpreting Slope Values**

**Positive Slope (m > 0):**
- The line goes upward from left to right
- Example: $m = 2$ means for every 1 unit right, you go up 2 units

```
    |  /
    | /
    |/___
   rises from left to right
```

**Negative Slope (m < 0):**
- The line goes downward from left to right
- Example: $m = -3$ means for every 1 unit right, you go down 3 units

```
    \
     \
      \___
    falls from left to right
```

**Zero Slope (m = 0):**
- The line is horizontal (flat)
- Example: A line passing through (1, 5) and (10, 5) has slope 0

```
    ————————
    horizontal line
```

**Undefined Slope:**
- The line is vertical
- Example: A line passing through (3, 1) and (3, 10) has undefined slope (because we'd be dividing by zero)

```
    |
    |
    | vertical line
    |
```

---

#### **Worked Examples: Calculating Slope**

**Example 1: Positive Slope**

Find the slope of the line passing through A(1, 2) and B(4, 8).

**Solution:**

Use the slope formula:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$
$$m = \frac{8 - 2}{4 - 1}$$
$$m = \frac{6}{3}$$
$$m = 2$$

**Interpretation:** For every 1 unit you move right, the line goes up 2 units.

**Answer:** The slope is 2.

---

**Example 2: Negative Slope**

Find the slope of the line passing through C(-2, 5) and D(3, -5).

**Solution:**

$$m = \frac{-5 - 5}{3 - (-2)}$$
$$m = \frac{-10}{5}$$
$$m = -2$$

**Interpretation:** For every 1 unit you move right, the line goes down 2 units.

**Answer:** The slope is -2.

---

**Example 3: Zero Slope**

Find the slope of the line passing through E(1, 4) and F(7, 4).

**Solution:**

$$m = \frac{4 - 4}{7 - 1}$$
$$m = \frac{0}{6}$$
$$m = 0$$

**Interpretation:** No matter how far you move right, the $y$-value never changes (horizontal line).

**Answer:** The slope is 0.

---

**Example 4: Undefined Slope**

Find the slope of the line passing through G(3, -1) and H(3, 5).

**Solution:**

$$m = \frac{5 - (-1)}{3 - 3}$$
$$m = \frac{6}{0}$$
$$m = \text{undefined}$$

**Interpretation:** The denominator is zero, which means the line is vertical.

**Answer:** The slope is undefined.

---

### Slope Criteria for Parallel and Perpendicular Lines

#### **Parallel Lines Have Equal Slopes**

**Theorem:** If two lines are parallel, they have the same slope. Conversely, if two lines have the same slope, they are parallel.

$$\text{If } \overleftrightarrow{AB} \parallel \overleftrightarrow{CD}, \text{ then } m_{AB} = m_{CD}$$

**Example:**
- Line 1 passes through (1, 2) and (3, 6). Slope = $\frac{6-2}{3-1} = \frac{4}{2} = 2$
- Line 2 passes through (0, 0) and (2, 4). Slope = $\frac{4-0}{2-0} = \frac{4}{2} = 2$
- Since both slopes equal 2, these lines are parallel.

**Visual:**
```
  /______ ← both lines have the same slope (same steepness)
 /
/______ ← parallel lines never meet
```

---

#### **Perpendicular Lines Have Negative Reciprocal Slopes**

**Theorem:** If two lines are perpendicular (meet at a 90° angle), their slopes are negative reciprocals of each other. Conversely, if two slopes are negative reciprocals, the lines are perpendicular.

**What are negative reciprocals?**
- The reciprocal of $m$ is $\frac{1}{m}$ (flip the fraction)
- The negative reciprocal is $-\frac{1}{m}$ (flip it and change the sign)

**Formula:**
$$\text{If } \overleftrightarrow{AB} \perp \overleftrightarrow{CD}, \text{ then } m_{AB} \times m_{CD} = -1$$

Or equivalently:
$$m_{CD} = -\frac{1}{m_{AB}}$$

**Examples of Perpendicular Slopes:**

| Slope 1 | Negative Reciprocal | Are they perpendicular? |
|---------|------------------|----------------------|
| 2 | $-\frac{1}{2}$ | Yes |
| 3 | $-\frac{1}{3}$ | Yes |
| $-4$ | $\frac{1}{4}$ | Yes |
| $\frac{1}{2}$ | $-2$ | Yes |
| 0 | undefined | Yes (horizontal ⊥ vertical) |

**Why does this work?**

Think of a line with slope 2. Every time you move 1 unit right, you move 2 units up. A perpendicular line needs to be rotated 90°. This rotation causes the rise and run to swap and one to become negative, giving us slope $-\frac{1}{2}$.

**Visual:**
```
        |
        | ← perpendicular line (undefined slope, vertical)
    /   |
   / ← line with slope 2
  /_____|_____

These lines meet at 90°
Their slopes are -1/2 and 2, which are negative reciprocals
Check: 2 × (-1/2) = -1 ✓
```

---

#### **Worked Examples: Parallel and Perpendicular Lines**

**Example 1: Determining if Lines Are Parallel**

Are the lines through (1, 3) & (3, 7) and through (0, -1) & (2, 3) parallel?

**Solution:**

Find slope of Line 1:
$$m_1 = \frac{7 - 3}{3 - 1} = \frac{4}{2} = 2$$

Find slope of Line 2:
$$m_2 = \frac{3 - (-1)}{2 - 0} = \frac{4}{2} = 2$$

Since $m_1 = m_2 = 2$, the lines are parallel. ✓

**Answer:** Yes, the lines are parallel.

---

**Example 2: Determining if Lines Are Perpendicular**

Are the lines through (1, 1) & (3, 5) and through (0, 0) & (2, -1) perpendicular?

**Solution:**

Find slope of Line 1:
$$m_1 = \frac{5 - 1}{3 - 1} = \frac{4}{2} = 2$$

Find slope of Line 2:
$$m_2 = \frac{-1 - 0}{2 - 0} = \frac{-1}{2}$$

Check if they're negative reciprocals:
$$m_1 \times m_2 = 2 \times \left(-\frac{1}{2}\right) = -1$$ ✓

Since the product is -1, the lines are perpendicular. ✓

**Answer:** Yes, the lines are perpendicular.

---

**Example 3: Finding the Slope of a Perpendicular Line**

A line has slope 3. What is the slope of a line perpendicular to it?

**Solution:**

The perpendicular slope is the negative reciprocal:
$$m_{\perp} = -\frac{1}{3}$$

**Answer:** The perpendicular slope is $-\frac{1}{3}$.

---

### Writing Equations of Lines

#### **Slope-Intercept Form**

**Definition:** The equation of a line in slope-intercept form is:

$$y = mx + b$$

**What each variable means:**
- $y$ = the $y$-coordinate of any point on the line
- $x$ = the $x$-coordinate of that same point
- $m$ = the slope
- $b$ = the $y$-intercept (where the line crosses the $y$-axis)

**Why is this useful?**
- It immediately tells you the slope ($m$) and $y$-intercept ($b$)
- It's easy to graph — start at $b$ on the $y$-axis, then use slope to find other points

**Example:**
- $y = 2x + 3$ has slope 2 and $y$-intercept 3
- The line crosses the $y$-axis at (0, 3)
- For every 1 unit right, it goes up 2 units

---

#### **Point-Slope Form**

**Definition:** The equation of a line in point-slope form is:

$$y - y_1 = m(x - x_1)$$

**What each variable means:**
- $(x_1, y_1)$ = a known point on the line
- $m$ = the slope of the line
- $(x, y)$ = any other point on the line

**When to use it:**
- When you know the slope and a point (but not the $y$-intercept)
- When you need to write an equation quickly

**How to use it:**
1. Plug in the slope $m$ and the point $(x_1, y_1)$
2. Simplify the equation
3. (Optional) Convert to slope-intercept form if requested

---

#### **Worked Examples: Writing Equations of Lines**

**Example 1: Using Slope-Intercept Form (Given Slope and $y$-Intercept)**

Write the equation of a line with slope 3 and $y$-intercept -2.

**Solution:**

Use $y = mx + b$:
$$y = 3x + (-2)$$
$$y = 3x - 2$$

**Check:**
- Slope is 3 ✓
- When $x = 0$: $y = 3(0) - 2 = -2$ (so $y$-intercept is -2) ✓

**Answer:** $y = 3x - 2$

---

**Example 2: Using Slope-Intercept Form (Given Two Points)**

Write the equation of a line passing through (1, 3) and (4, 9).

**Solution:**

Step 1: Find the slope
$$m = \frac{9 - 3}{4 - 1} = \frac{6}{3} = 2$$

Step 2: Find the $y$-intercept using one of the points
Use $(1, 3)$ and $y = mx + b$:
$$3 = 2(1) + b$$
$$3 = 2 + b$$
$$b = 1$$

Step 3: Write the equation
$$y = 2x + 1$$

**Check with the other point (4, 9):**
$$y = 2(4) + 1 = 8 + 1 = 9$$ ✓

**Answer:** $y = 2x + 1$

---

**Example 3: Using Point-Slope Form**

Write the equation of a line with slope -2 passing through (3, 5). Then convert to slope-intercept form.

**Solution:**

Step 1: Use point-slope form with $m = -2$ and $(x_1, y_1) = (3, 5)$
$$y - 5 = -2(x - 3)$$

Step 2: Simplify
$$y - 5 = -2x + 6$$
$$y = -2x + 6 + 5$$
$$y = -2x + 11$$

**Check:** When $x = 3$: $y = -2(3) + 11 = -6 + 11 = 5$ ✓

**Answer:** Point-slope form: $y - 5 = -2(x - 3)$; Slope-intercept form: $y = -2x + 11$

---

**Example 4: Writing an Equation for a Parallel Line**

Write the equation of a line parallel to $y = 4x - 1$ that passes through (2, 3).

**Solution:**

Step 1: Identify the slope of the original line
From $y = 4x - 1$, the slope is 4.

Step 2: Parallel lines have the same slope
The new line also has slope 4.

Step 3: Use point-slope form with the new point (2, 3)
$$y - 3 = 4(x - 2)$$
$$y - 3 = 4x - 8$$
$$y = 4x - 5$$

**Check:**
- Slope is 4 (same as original) ✓
- When $x = 2$: $y = 4(2) - 5 = 8 - 5 = 3$ ✓

**Answer:** $y = 4x - 5$

---

**Example 5: Writing an Equation for a Perpendicular Line**

Write the equation of a line perpendicular to $y = \frac{1}{2}x + 4$ that passes through (-1, 2).

**Solution:**

Step 1: Identify the slope of the original line
From $y = \frac{1}{2}x + 4$, the slope is $\frac{1}{2}$.

Step 2: Find the perpendicular slope
Perpendicular slope $= -\frac{1}{\frac{1}{2}} = -2$

Step 3: Use point-slope form with the new point (-1, 2)
$$y - 2 = -2(x - (-1))$$
$$y - 2 = -2(x + 1)$$
$$y - 2 = -2x - 2$$
$$y = -2x$$

**Check:**
- Slope is -2, and $\frac{1}{2} \times (-2) = -1$ (perpendicular) ✓
- When $x = -1$: $y = -2(-1) = 2$ ✓

**Answer:** $y = -2x$

---

### Common Mistakes to Avoid

**Mistake 1:** Writing slope upside-down (run/rise instead of rise/run)
- **Fix:** Remember the formula: $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\text{rise}}{\text{run}}$ — the $y$ values go on top!

**Mistake 2:** Confusing which slope is steeper
- **Fix:** A larger absolute value means steeper. Slope 5 is steeper than slope 2, even though both are positive.

**Mistake 3:** Forgetting that parallel lines have the **same** slope
- **Fix:** Parallel = same slope. Perpendicular = negative reciprocal slopes.

**Mistake 4:** Incorrectly calculating negative reciprocals
- **Fix:** For slope $\frac{3}{5}$, the negative reciprocal is $-\frac{5}{3}$ (flip AND negate).

**Mistake 5:** Forgetting the negative sign when using point-slope form
- **Fix:** Write out the form carefully: $y - y_1 = m(x - x_1)$ — note the minus signs!

**Mistake 6:** Not simplifying to slope-intercept form when asked
- **Fix:** If the problem asks for the equation in a specific form, make sure you convert to it.

---

---

## Compass and Straightedge Constructions

### What Are Compass and Straightedge Constructions?

**Definition:** A compass and straightedge construction is a geometric figure drawn using only two tools:
- **Compass:** A tool for drawing circles and marking equal distances
- **Straightedge:** A ruler without markings (so you can't measure lengths)

**Key Rule:** You can ONLY draw circles and straight lines. You CANNOT measure distances with a ruler or mark specific lengths.

**Why does this matter?** These constructions prove that certain geometric objects can be created using just circles and lines — they show the power of basic geometry principles.

---

### Construction 1: Copying a Segment

**What you're doing:** Creating a new segment with the same length as a given segment.

**Given:** Segment $\overline{AB}$ and a ray $\overrightarrow{CD}$

**Goal:** Find point E on ray $\overrightarrow{CD}$ such that $\overline{AB} \cong \overline{CE}$

**Steps:**

1. **Place compass point at A and open it to point B**
   - This "locks in" the length of segment AB

2. **Place the compass point at C (the endpoint of your ray)**
   - Keep the same opening size from step 1

3. **Draw an arc that intersects the ray $\overrightarrow{CD}$**
   - The intersection point is E
   - Now $CE = AB$

**Why it works:** The compass maintains the same radius throughout. Both arcs are drawn with the same radius, so they're the same length.

**Visual:**
```
Original segment:
A ————— B
  (length to copy)

Ray:
C ————————→

Step 1-3: Draw arc from C with radius = AB
C ————————→
  |————— E
  (E is the same distance from C as B is from A)
```

---

### Construction 2: Copying an Angle

**What you're doing:** Creating a new angle with the same measure as a given angle.

**Given:** Angle $\angle ABC$ and a ray $\overrightarrow{DE}$

**Goal:** Create angle $\angle FDE$ equal to $\angle ABC$

**Steps:**

1. **Place compass point at B (the vertex of the original angle)**
   - Draw an arc that intersects both sides of the angle
   - Label the intersections P (on ray BA) and Q (on ray BC)

2. **Place the compass point at D (the vertex of your ray)**
   - Using the same radius as step 1, draw an arc
   - This arc should intersect ray $\overrightarrow{DE}$
   - Label this intersection R

3. **Measure the distance PQ with your compass**
   - Place compass point at P, open to Q

4. **Place compass point at R (from step 2)**
   - Draw an arc with radius PQ
   - This arc intersects the arc from step 2
   - Label this intersection S

5. **Draw ray $\overrightarrow{DS}$**
   - Angle $\angle RDS$ equals angle $\angle ABC$

**Why it works:** We're creating two triangles with the same side lengths (arcs), so they're congruent, making the angles equal.

**Visual:**
```
Original angle:        New angle:
    C                      F
    |                      |
    | angle to copy         | copied angle
    |                       |
A———B                   D———E
```

---

### Construction 3: Bisecting a Segment (Finding the Midpoint)

**What you're doing:** Finding the exact midpoint of a segment.

**Given:** Segment $\overline{AB}$

**Goal:** Find point M such that $AM = MB$ (M is the midpoint)

**Steps:**

1. **Place compass point at A**
   - Open the compass more than halfway to B (open it to any length greater than half of AB)

2. **Draw an arc above and below the segment**
   - Keep the compass radius the same

3. **Without changing the compass opening, place the compass point at B**
   - Draw arcs above and below the segment
   - These arcs should intersect the arcs from step 2
   - Label the intersections C (above) and D (below)

4. **Using the straightedge, draw line $\overleftrightarrow{CD}$**
   - This line intersects $\overline{AB}$ at point M
   - M is the midpoint of $\overline{AB}$

**Why it works:** Points C and D are equidistant from both A and B. The line through them (the perpendicular bisector) passes through the midpoint.

**Visual:**
```
        C
       /|\
      / | \
     /  |  \
    A———M———B
     \  |  /
      \ | /
       \|/
        D
```

---

### Construction 4: Bisecting an Angle

**What you're doing:** Dividing an angle exactly in half.

**Given:** Angle $\angle ABC$

**Goal:** Find ray $\overrightarrow{BD}$ such that $\angle ABD = \angle DBC$

**Steps:**

1. **Place compass point at B (the vertex)**
   - Draw an arc that intersects both sides of the angle
   - Label the intersections P (on ray BA) and Q (on ray BC)

2. **Place compass point at P**
   - Open to any radius greater than half of PQ
   - Draw an arc in the interior of the angle

3. **Without changing the compass, place compass point at Q**
   - Draw an arc in the interior of the angle
   - This arc intersects the arc from step 2
   - Label the intersection R

4. **Using the straightedge, draw ray $\overrightarrow{BR}$**
   - This ray bisects angle $\angle ABC$

**Why it works:** Points P and Q are equidistant from R (because we used the same compass radius). This makes triangle BPR congruent to triangle BQR, so the angles are equal.

**Visual:**
```
        A
        |
        |P
       /\
      /  \R
     /    |  \
    B—————+———Q———C
     (R is equidistant from P and Q)
     ← equal angles →
```

---

### Construction 5: Constructing a Perpendicular Line (from a Point on the Line)

**What you're doing:** Drawing a line perpendicular to a given line through a point on that line.

**Given:** Line $\overleftrightarrow{AB}$ and point P on the line

**Goal:** Construct line perpendicular to $\overleftrightarrow{AB}$ through point P

**Steps:**

1. **Place compass point at P**
   - Draw arcs on both sides of P on line $\overleftrightarrow{AB}$
   - Make both arcs the same distance from P
   - Label the intersections Q (left) and R (right)

2. **Place compass point at Q**
   - Open the compass to more than half the distance from Q to R
   - Draw an arc above (or below) the line

3. **Without changing the compass, place compass point at R**
   - Draw an arc above (or below) the line
   - This arc intersects the arc from step 2
   - Label the intersection S

4. **Using the straightedge, draw line $\overleftrightarrow{PS}$**
   - This line is perpendicular to $\overleftrightarrow{AB}$

**Why it works:** S is equidistant from Q and R, which means S lies on the perpendicular bisector of QR. This perpendicular bisector is perpendicular to the original line.

**Visual:**
```
          S
          |
          |
    Q—P—R |
          |
    ——————|—— line AB

   angle QPS = 90°
```

---

### Construction 6: Constructing a Perpendicular Bisector

**What you're doing:** Creating a line that is perpendicular to a segment AND passes through its midpoint.

**Note:** This is actually a combination of two previous constructions!

**Given:** Segment $\overline{AB}$

**Goal:** Construct the perpendicular bisector of $\overline{AB}$

**Steps:**
(This is the same as Construction 3: Bisecting a Segment)

1. **Place compass point at A**
   - Open the compass more than halfway to B

2. **Draw arcs above and below the segment**

3. **Place compass point at B, keeping the same radius**
   - Draw arcs above and below that intersect the first arcs
   - Label intersections C and D

4. **Draw line $\overleftrightarrow{CD}$**
   - This line is the perpendicular bisector

**Why it works:** This construction creates a line that:
- Passes through the midpoint (by bisecting)
- Is perpendicular to the segment (by the properties of the perpendicular bisector)

---

### Construction 7: Constructing a Perpendicular Line (from a Point NOT on the Line)

**What you're doing:** Drawing a line perpendicular to a given line through a point that's not on the line.

**Given:** Line $\overleftrightarrow{AB}$ and point P not on the line

**Goal:** Construct line through P perpendicular to $\overleftrightarrow{AB}$

**Steps:**

1. **Place compass point at P**
   - Open the compass to a radius larger than the distance from P to line $\overleftrightarrow{AB}$
   - Draw an arc that intersects line $\overleftrightarrow{AB}$ at two points
   - Label the intersections Q and R

2. **Now construct the perpendicular bisector of $\overline{QR}$**
   - Place compass point at Q with radius greater than half of QR
   - Draw arcs above and below line $\overleftrightarrow{AB}$
   - Place compass point at R, same radius
   - Draw arcs that intersect the first arcs
   - Label intersections C and D

3. **Draw line $\overleftrightarrow{CD}$**
   - This line passes through P and is perpendicular to $\overleftrightarrow{AB}$

**Why it works:** The perpendicular bisector of QR passes through P (because P is equidistant from Q and R). Since we constructed the perpendicular bisector of a segment of line AB, this perpendicular bisector is perpendicular to AB.

---

### Construction 8: Constructing a Parallel Line

**What you're doing:** Drawing a line parallel to a given line through a point not on that line.

**Given:** Line $\overleftrightarrow{AB}$ and point P not on the line

**Goal:** Construct a line through P parallel to $\overleftrightarrow{AB}$

**Method 1: Using Corresponding Angles**

**Steps:**

1. **Draw a line through P and any point Q on line $\overleftrightarrow{AB}$**
   - This creates a transversal
   - Label the angle formed at Q as $\angle AQP$ (angle between QA and QP)

2. **Copy angle $\angle AQP$ at point P (using Construction 2: Copying an Angle)**
   - The copied angle should be on the opposite side of the transversal
   - This creates corresponding angles

3. **Since corresponding angles are congruent, the two lines are parallel**

**Visual:**
```
           P
          /|
         / | ← copied angle
        /  |
       /———|
  ————Q———/———— line AB
    angle at Q ≅ angle at P (corresponding angles)
    Therefore, line through P is parallel to AB
```

**Method 2: Using the Perpendicular Method**

**Steps:**

1. **Construct a perpendicular from P to line $\overleftrightarrow{AB}$** (using Construction 7)
   - Label the foot of the perpendicular as Q

2. **Construct a perpendicular to $\overleftrightarrow{PQ}$ at point P** (using Construction 5)
   - This new perpendicular is parallel to $\overleftrightarrow{AB}$
   - (Perpendicular to a perpendicular = parallel)

**Visual:**
```
Line through P ————— (perpendicular to PQ)
                 |
                 | PQ (perpendicular to AB)
                 |
    Q ————————————————— line AB
```

---

### Summary: Quick Reference for Constructions

| Construction | What You Create | Tools You Use |
|--------------|-----------------|---------------|
| Copy segment | Segment same length as given | Compass |
| Copy angle | Angle same measure as given | Compass + straightedge |
| Bisect segment | Midpoint of segment | Compass + straightedge |
| Bisect angle | Ray that divides angle in half | Compass + straightedge |
| Perpendicular (on line) | 90° line through point on given line | Compass + straightedge |
| Perpendicular bisector | Line perpendicular to and bisecting segment | Compass + straightedge |
| Perpendicular (off line) | 90° line through point NOT on given line | Compass + straightedge |
| Parallel line | Line parallel to given line | Compass + straightedge |

---

---

## Proving Theorems Using Coordinate Geometry

### What Does "Proving Algebraically" Mean?

When we prove something using coordinate geometry, we:
1. Place figures on a coordinate plane
2. Use the distance formula, midpoint formula, and slope formulas
3. Calculate algebraically to verify geometric properties

**Why do this?** It bridges algebra and geometry, showing that shapes with specific properties can be described mathematically.

---

### Strategy: Proving Properties of Parallelograms

#### **What is a Parallelogram?**

A parallelogram is a quadrilateral (4-sided figure) where both pairs of opposite sides are parallel.

**Properties we can prove:**
- Opposite sides are equal in length
- Opposite sides are parallel (equal slopes)
- Diagonals bisect each other (same midpoint)
- Consecutive angles are supplementary
- Opposite angles are equal

---

#### **Worked Example 1: Proving a Figure Is a Parallelogram**

**Problem:** The vertices of a quadrilateral are A(0, 0), B(3, 0), C(5, 2), and D(2, 2). Prove that ABCD is a parallelogram by showing opposite sides have equal lengths.

**Solution:**

**Step 1:** Find the length of side AB
$$AB = \sqrt{(3-0)^2 + (0-0)^2} = \sqrt{9} = 3$$

**Step 2:** Find the length of side DC
$$DC = \sqrt{(5-2)^2 + (2-2)^2} = \sqrt{9} = 3$$

**Step 3:** Find the length of side AD
$$AD = \sqrt{(2-0)^2 + (2-0)^2} = \sqrt{4+4} = \sqrt{8} = 2\sqrt{2}$$

**Step 4:** Find the length of side BC
$$BC = \sqrt{(5-3)^2 + (2-0)^2} = \sqrt{4+4} = \sqrt{8} = 2\sqrt{2}$$

**Step 5:** Compare

We have:
- $AB = DC = 3$ (opposite sides equal) ✓
- $AD = BC = 2\sqrt{2}$ (opposite sides equal) ✓

**Conclusion:** Since both pairs of opposite sides are equal in length, ABCD is a parallelogram.

---

#### **Worked Example 2: Proving Diagonals Bisect Each Other**

**Problem:** Prove that the diagonals of parallelogram ABCD (from the previous problem) bisect each other.

**Note:** Diagonals bisect each other if they have the same midpoint.

**Given:** A(0, 0), B(3, 0), C(5, 2), D(2, 2)

**Solution:**

**Step 1:** Find the midpoint of diagonal AC
$$M_{AC} = \left(\frac{0+5}{2}, \frac{0+2}{2}\right) = \left(2.5, 1\right)$$

**Step 2:** Find the midpoint of diagonal BD
$$M_{BD} = \left(\frac{3+2}{2}, \frac{0+2}{2}\right) = \left(2.5, 1\right)$$

**Step 3:** Compare

Both diagonals have the same midpoint: (2.5, 1)

**Conclusion:** The diagonals bisect each other. ✓

---

#### **Worked Example 3: Proving Opposite Sides Are Parallel**

**Problem:** Prove that ABCD (from before) has parallel opposite sides by showing they have equal slopes.

**Given:** A(0, 0), B(3, 0), C(5, 2), D(2, 2)

**Solution:**

**Step 1:** Find the slope of side AB
$$m_{AB} = \frac{0-0}{3-0} = \frac{0}{3} = 0$$

**Step 2:** Find the slope of side DC
$$m_{DC} = \frac{2-2}{5-2} = \frac{0}{3} = 0$$

**Step 3:** Find the slope of side AD
$$m_{AD} = \frac{2-0}{2-0} = \frac{2}{2} = 1$$

**Step 4:** Find the slope of side BC
$$m_{BC} = \frac{2-0}{5-3} = \frac{2}{2} = 1$$

**Step 5:** Compare

We have:
- $m_{AB} = m_{DC} = 0$ (opposite sides parallel) ✓
- $m_{AD} = m_{BC} = 1$ (opposite sides parallel) ✓

**Conclusion:** Since opposite sides have equal slopes, they are parallel. Therefore ABCD is a parallelogram. ✓

---

### Strategy: Proving Properties of Rectangles

#### **What is a Rectangle?**

A rectangle is a parallelogram with four right angles (90°).

**Special properties to prove:**
- All angles are right angles
- Diagonals are equal in length
- Diagonals bisect each other

---

#### **Worked Example 4: Proving a Figure Is a Rectangle**

**Problem:** The vertices of a quadrilateral are A(0, 0), B(4, 0), C(4, 3), and D(0, 3). Prove that ABCD is a rectangle.

**Solution:**

**Step 1:** Verify it's a parallelogram (from previous examples, we know to check opposite sides)

Find slopes:
- $m_{AB} = \frac{0-0}{4-0} = 0$
- $m_{DC} = \frac{3-3}{4-0} = 0$ ✓
- $m_{AD} = \frac{3-0}{0-0}$ = undefined (vertical)
- $m_{BC} = \frac{3-0}{4-4}$ = undefined (vertical) ✓

It's a parallelogram (opposite sides parallel).

**Step 2:** Verify that consecutive sides are perpendicular

For sides to be perpendicular, their slopes must be negative reciprocals.
- $m_{AB} = 0$ (horizontal)
- $m_{BC}$ = undefined (vertical)
- A horizontal line is perpendicular to a vertical line ✓

Therefore, side AB ⊥ side BC, creating a right angle.

**Step 3:** Since it's a parallelogram and has one right angle, it has four right angles

(In a parallelogram, if one angle is a right angle, all are right angles.)

**Conclusion:** ABCD is a rectangle. ✓

---

#### **Worked Example 5: Proving Diagonals Are Equal**

**Problem:** Prove that the diagonals of rectangle ABCD are equal in length.

**Given:** A(0, 0), B(4, 0), C(4, 3), D(0, 3)

**Solution:**

**Step 1:** Find the length of diagonal AC
$$AC = \sqrt{(4-0)^2 + (3-0)^2} = \sqrt{16+9} = \sqrt{25} = 5$$

**Step 2:** Find the length of diagonal BD
$$BD = \sqrt{(0-4)^2 + (3-0)^2} = \sqrt{16+9} = \sqrt{25} = 5$$

**Step 3:** Compare

$AC = BD = 5$

**Conclusion:** The diagonals are equal in length. ✓ (This is a special property of rectangles, not all parallelograms!)

---

### Strategy: Proving Properties of Triangles

#### **Worked Example 6: Proving a Triangle Is Isosceles**

**Definition:** An isosceles triangle has two sides of equal length.

**Problem:** The vertices of a triangle are A(0, 0), B(6, 0), and C(3, 5). Prove that triangle ABC is isosceles.

**Solution:**

**Step 1:** Find the length of side AB
$$AB = \sqrt{(6-0)^2 + (0-0)^2} = \sqrt{36} = 6$$

**Step 2:** Find the length of side AC
$$AC = \sqrt{(3-0)^2 + (5-0)^2} = \sqrt{9+25} = \sqrt{34}$$

**Step 3:** Find the length of side BC
$$BC = \sqrt{(3-6)^2 + (5-0)^2} = \sqrt{9+25} = \sqrt{34}$$

**Step 4:** Compare

$AC = BC = \sqrt{34}$, but $AB = 6 \neq \sqrt{34}$

**Conclusion:** Since two sides have equal length (AC and BC), triangle ABC is isosceles. ✓

---

#### **Worked Example 7: Proving a Triangle Is Right-Angled**

**Definition:** A right triangle has one 90° angle.

**Method:** Use the Pythagorean theorem: $a^2 + b^2 = c^2$

**Problem:** The vertices of a triangle are A(0, 0), B(3, 0), and C(0, 4). Prove that triangle ABC is a right triangle.

**Solution:**

**Step 1:** Find all three side lengths
$$AB = \sqrt{(3-0)^2 + (0-0)^2} = 3$$
$$AC = \sqrt{(0-0)^2 + (4-0)^2} = 4$$
$$BC = \sqrt{(0-3)^2 + (4-0)^2} = \sqrt{9+16} = \sqrt{25} = 5$$

**Step 2:** Check if Pythagorean theorem holds
$$AB^2 + AC^2 = 3^2 + 4^2 = 9 + 16 = 25 = 5^2 = BC^2$$ ✓

**Step 3:** Identify the right angle

Since $AB^2 + AC^2 = BC^2$, the right angle is at vertex A (opposite the longest side BC).

**Conclusion:** Triangle ABC is a right triangle with the right angle at A. ✓

---

### Strategy: Proving Midpoint Properties

#### **Worked Example 8: The Midsegment Theorem**

**Definition:** A midsegment of a triangle is a segment connecting the midpoints of two sides.

**Theorem:** The midsegment is parallel to the third side and half its length.

**Problem:** Triangle ABC has vertices A(0, 0), B(8, 0), and C(4, 6). Let M be the midpoint of AB and N be the midpoint of AC. Prove that MN is parallel to BC and that $MN = \frac{1}{2} BC$.

**Solution:**

**Step 1:** Find the midpoint M of AB
$$M = \left(\frac{0+8}{2}, \frac{0+0}{2}\right) = (4, 0)$$

**Step 2:** Find the midpoint N of AC
$$N = \left(\frac{0+4}{2}, \frac{0+6}{2}\right) = (2, 3)$$

**Step 3:** Find the slope of MN
$$m_{MN} = \frac{3-0}{2-4} = \frac{3}{-2} = -\frac{3}{2}$$

**Step 4:** Find the slope of BC
$$m_{BC} = \frac{6-0}{4-8} = \frac{6}{-4} = -\frac{3}{2}$$

**Step 5:** Compare slopes
$m_{MN} = m_{BC}$, so **MN is parallel to BC**. ✓

**Step 6:** Find the length of MN
$$MN = \sqrt{(2-4)^2 + (3-0)^2} = \sqrt{4+9} = \sqrt{13}$$

**Step 7:** Find the length of BC
$$BC = \sqrt{(4-8)^2 + (6-0)^2} = \sqrt{16+36} = \sqrt{52} = 2\sqrt{13}$$

**Step 8:** Compare lengths
$$MN = \sqrt{13} = \frac{1}{2} \cdot 2\sqrt{13} = \frac{1}{2} BC$$ ✓

**Conclusion:** The midsegment MN is parallel to BC and has half its length. ✓

---

### Common Mistakes to Avoid

**Mistake 1:** Using the distance formula incorrectly
- **Fix:** Make sure both differences are squared: $(x_2-x_1)^2$ and $(y_2-y_1)^2$

**Mistake 2:** Confusing the midpoint formula with the distance formula
- **Fix:** Midpoint uses averages (division by 2); distance uses square root.

**Mistake 3:** Not checking all properties when asked to "prove it's a [shape]"
- **Fix:** Read the definition. For parallelogram, you might check slopes (parallel sides) or side lengths (equal opposite sides). For rectangle, you need to also check that angles are right angles.

**Mistake 4:** Incorrectly determining perpendicularity using slopes
- **Fix:** Perpendicular slopes multiply to -1. Check: slope 2 × slope $-\frac{1}{2}$ = -1 ✓

**Mistake 5:** Not simplifying radical answers
- **Fix:** $\sqrt{8} = 2\sqrt{2}$, not $\sqrt{8}$. Simplify your final answers.

---

---

## Final Study Tips and Exam Strategies

### Before the Exam

1. **Know all the formulas:**
   - Distance: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
   - Midpoint: $M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$
   - Slope: $m = \frac{y_2 - y_1}{x_2 - x_1}$
   - Line equations: $y = mx + b$ and $y - y_1 = m(x - x_1)$

2. **Memorize angle relationships:**
   - Complementary: 90°
   - Supplementary: 180°
   - Vertical angles: equal
   - Corresponding angles (parallel lines): equal
   - Alternate interior angles: equal
   - Co-interior angles: supplementary

3. **Practice compass constructions:** Draw them multiple times until they feel automatic.

4. **Review the 8 angles created by a transversal:** Draw the diagram and label all angles.

---

### During the Exam

1. **Read the question carefully**
   - What are you given?
   - What are you asked to find or prove?

2. **Draw a picture** (even if one isn't provided)
   - Label all given information
   - Use correct notation

3. **Show your work**
   - Write out all steps
   - Use formulas correctly

4. **Check your answer**
   - Does it make sense?
   - Can you verify it using a different method?

---

### Practice Problem Tips

**Look for problems asking you to:**

1. **Find angles:** Use angle relationships and linear pairs
2. **Find distances:** Use distance formula; simplify radicals
3. **Write equations:** Identify slope and point; choose form (slope-intercept or point-slope)
4. **Prove parallel lines:** Show corresponding angles equal, or alternate interior angles equal, or slopes equal
5. **Prove perpendicular lines:** Show slopes are negative reciprocals, or show right angles exist
6. **Prove geometric figures:** Check side lengths (distance formula) and angles (slopes or Pythagorean theorem)

---

## Conclusion

This unit covers the essential foundations of geometry. Master these topics, and you'll have a solid base for all future geometry study. Key to success:

- **Understand WHY**, not just HOW
- **Practice problems** of every type
- **Don't memorize** — derive formulas from first principles
- **Draw pictures** — geometry is visual

Good luck! 🎯
