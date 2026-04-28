# Unit 4: Properties of Polygons & Quadrilaterals
## Honors Geometry Study Notes

---

## Table of Contents
1. [Polygon Basics](#polygon-basics)
2. [Angles in Polygons](#angles-in-polygons)
3. [The Quadrilateral Hierarchy](#the-quadrilateral-hierarchy)
4. [Parallelograms](#parallelograms)
5. [Rectangles](#rectangles)
6. [Rhombi](#rhombi)
7. [Squares](#squares)
8. [Trapezoids](#trapezoids)
9. [Isosceles Trapezoids](#isosceles-trapezoids)
10. [Kites](#kites)
11. [Coordinate Geometry Proofs](#coordinate-geometry-proofs)
12. [Perimeter and Distance](#perimeter-and-distance)

---

# POLYGON BASICS

## What is a Polygon? (Plain English Definition)

A **polygon** is a closed figure made up of straight line segments (called sides) that connect to form a shape. The sides only touch at their endpoints (called vertices), and the figure doesn't cross itself.

Think of it like a fence: the straight boards are sides, the corners where they meet are vertices, and the whole enclosure is the polygon.

## Key Vocabulary

- **Vertex (Vertices)**: The corners where two sides of a polygon meet. (Plural: vertices)
- **Side**: A line segment that forms one edge of the polygon.
- **Diagonal**: A line segment connecting two non-adjacent vertices (two vertices that don't share a side).
- **n-gon**: A polygon with n sides. For example, a pentagon is a 5-gon, a hexagon is a 6-gon.

## Naming Polygons by Number of Sides

| Sides | Name |
|-------|------|
| 3 | Triangle |
| 4 | Quadrilateral |
| 5 | Pentagon |
| 6 | Hexagon |
| 7 | Heptagon |
| 8 | Octagon |
| 9 | Nonagon |
| 10 | Decagon |
| 12 | Dodecagon |
| n | n-gon |

## Convex vs. Concave Polygons

### Convex Polygon
A polygon where **all interior angles are less than 180°**. Equivalently, if you pick any two points inside the polygon and draw a line between them, that entire line segment stays inside the polygon. The polygon is "bulging outward" everywhere—no dents.

**Example**: A regular pentagon, a square, most shapes you think of as "normal."

### Concave Polygon
A polygon where **at least one interior angle is greater than 180°** (a reflex angle). Equivalently, there exist two points inside the polygon such that the line segment between them goes outside the polygon. The polygon has a "dent" or "indent."

**Example**: A star shape, an arrow, a boomerang.

**Visual Test**: Imagine tracing around the perimeter. For a convex polygon, you always turn in the same direction (all left turns or all right turns). For a concave polygon, you have to turn back on yourself at least once.

## Regular vs. Irregular Polygons

### Regular Polygon
A polygon where **all sides are congruent (equal in length) AND all interior angles are congruent (equal in measure)**.

**Examples**: A square (4 congruent sides, 4 right angles), a regular pentagon (5 equal sides, 5 equal angles), an equilateral triangle.

### Irregular Polygon
A polygon where the sides are not all equal in length, or the angles are not all equal in measure, or both.

**Examples**: A rectangle (not regular—sides differ in length), an isosceles triangle (not regular—angles aren't all equal), a trapezoid.

## Core Concept: How Many Diagonals?

An important question: **How many diagonals does an n-gon have?**

**Derivation**:
- From each vertex, you can draw diagonals to all other vertices except itself and its two adjacent vertices (which would form sides).
- So from each vertex: you can draw (n - 3) diagonals.
- Total: n vertices × (n - 3) diagonals each = n(n - 3).
- But this counts each diagonal twice (once from each endpoint), so: **Diagonals = n(n - 3) / 2**

**Example**: A hexagon (n = 6)
- Number of diagonals = 6(6 - 3) / 2 = 6(3) / 2 = 9 diagonals

---

# ANGLES IN POLYGONS

## Interior Angle Sum Formula

### The Formula
For any convex polygon with n sides:

$$\text{Sum of interior angles} = (n - 2) \times 180°$$

### Derivation (Why Does This Work?)

The key insight: **Any polygon can be divided into triangles by drawing diagonals from one vertex.**

**Step-by-step**:
1. Take any polygon with n sides.
2. Pick one vertex and draw diagonals to all non-adjacent vertices.
3. This divides the polygon into (n - 2) triangles. (A quadrilateral makes 2 triangles, a pentagon makes 3, etc.)
4. The sum of all angles in a triangle is 180°.
5. So the sum of all interior angles = (n - 2) × 180°.

**Visual Example: Quadrilateral**
- Pick one vertex. Draw diagonals from it.
- You create 2 triangles inside.
- Sum of interior angles = 2 × 180° = 360°.
- Using the formula: (4 - 2) × 180° = 2 × 180° = 360°. ✓

### Using the Formula

**Example 1**: What is the sum of interior angles in a pentagon (5-sided polygon)?
$$\text{Sum} = (5 - 2) \times 180° = 3 \times 180° = 540°$$

**Example 2**: A heptagon (7 sides) has an interior angle sum of:
$$\text{Sum} = (7 - 2) \times 180° = 5 \times 180° = 900°$$

**Example 3**: If the sum of interior angles of a polygon is 1260°, how many sides does it have?
$$1260 = (n - 2) \times 180$$
$$7 = n - 2$$
$$n = 9$$
It's a nonagon (9-sided polygon).

## Each Interior Angle of a Regular Polygon

### The Formula
For a **regular n-gon** (all angles equal):

$$\text{Each interior angle} = \frac{(n - 2) \times 180°}{n}$$

### Why?
- Sum of all interior angles = (n - 2) × 180°
- If all n angles are equal, divide by n to get each one.

### Examples

**Example 1**: Each interior angle of a regular hexagon:
$$\text{Each angle} = \frac{(6 - 2) \times 180°}{6} = \frac{4 \times 180°}{6} = \frac{720°}{6} = 120°$$

**Example 2**: Each interior angle of a regular octagon (stop sign):
$$\text{Each angle} = \frac{(8 - 2) \times 180°}{8} = \frac{6 \times 180°}{8} = \frac{1080°}{8} = 135°$$

**Example 3**: A regular polygon has each interior angle equal to 108°. How many sides?
$$108 = \frac{(n - 2) \times 180}{n}$$
$$108n = (n - 2) \times 180$$
$$108n = 180n - 360$$
$$-72n = -360$$
$$n = 5$$
It's a regular pentagon.

## Exterior Angles

### What is an Exterior Angle?

An **exterior angle** of a polygon is formed by one side of the polygon and the extension of an adjacent side.

At each vertex, there's one interior angle (inside the polygon) and two exterior angles (one on each side). The exterior angles at a vertex are congruent and supplementary to the interior angle.

### Exterior Angle Sum Theorem (CRITICAL!)

**For ANY convex polygon, the sum of exterior angles is ALWAYS 360°.**

**This is true no matter how many sides!**

$$\text{Sum of exterior angles} = 360°$$

### Why Is This True?

Think of "walking around" the polygon:
- As you walk around the perimeter, at each vertex you turn through an exterior angle.
- After you complete the full loop and return to your starting point, you've rotated a total of 360° (one full turn).
- Therefore, the sum of exterior angles = 360°.

This is elegant because it doesn't depend on the number of sides!

### Each Exterior Angle of a Regular Polygon

For a **regular n-gon**, all exterior angles are equal:

$$\text{Each exterior angle} = \frac{360°}{n}$$

### Examples

**Example 1**: Each exterior angle of a regular hexagon:
$$\text{Each exterior angle} = \frac{360°}{6} = 60°$$

**Example 2**: Each exterior angle of a regular octagon:
$$\text{Each exterior angle} = \frac{360°}{8} = 45°$$

**Example 3**: A regular polygon has each exterior angle equal to 18°. How many sides?
$$18 = \frac{360}{n}$$
$$18n = 360$$
$$n = 20$$
It's a regular 20-gon.

### Relationship Between Interior and Exterior Angles

At any vertex of a polygon:
$$\text{Interior angle} + \text{Exterior angle} = 180°$$ (they are supplementary)

**Example**: If an interior angle is 140°, the exterior angle at that vertex is 180° - 140° = 40°.

---

# THE QUADRILATERAL HIERARCHY

## Understanding the Hierarchy

One of the most important concepts in this unit is understanding how different quadrilaterals are related. Think of it as a family tree:

```
                    QUADRILATERAL
                          |
                    TRAPEZOID
                          |
                    PARALLELOGRAM
                    /            \
                RECTANGLE      RHOMBUS
                    \            /
                      SQUARE

          Also: KITE (different family line)
```

### What This Means

- **Every square is a rhombus, rectangle, parallelogram, trapezoid, and quadrilateral.**
- **Every rectangle is a parallelogram, trapezoid, and quadrilateral (but not necessarily a rhombus).**
- **Every rhombus is a parallelogram, trapezoid, and quadrilateral (but not necessarily a rectangle).**
- **Every parallelogram is a trapezoid and quadrilateral.**
- **A kite is a quadrilateral, but it's not necessarily on this main tree.**

This is crucial: **If a quadrilateral is a rectangle, then it MUST have all the properties of a rectangle, a parallelogram, a trapezoid, and a quadrilateral.**

---

# PARALLELOGRAMS

## Definition

A **parallelogram** is a quadrilateral (4-sided polygon) where **both pairs of opposite sides are parallel**.

That's the defining characteristic. If you have a quadrilateral and both pairs of opposite sides are parallel, it's a parallelogram.

## Key Vocabulary

- **Opposite sides**: Sides that don't share a vertex. In quadrilateral ABCD, sides AB and CD are opposite; sides BC and DA are opposite.
- **Opposite angles**: Angles at non-adjacent vertices. In quadrilateral ABCD, angles A and C are opposite; angles B and D are opposite.
- **Consecutive angles**: Angles at adjacent vertices. In quadrilateral ABCD, angles A and B are consecutive, B and C are consecutive, etc.

## Properties of Parallelograms (If It's a Parallelogram, Then...)

### Property 1: Opposite Sides Are Congruent

**Theorem**: In a parallelogram, opposite sides are congruent (equal in length).

$$\text{If ABCD is a parallelogram, then } AB = CD \text{ and } BC = DA$$

### Property 2: Opposite Angles Are Congruent

**Theorem**: In a parallelogram, opposite angles are congruent (equal in measure).

$$\text{If ABCD is a parallelogram, then } \angle A \cong \angle C \text{ and } \angle B \cong \angle D$$

### Property 3: Consecutive Angles Are Supplementary

**Theorem**: In a parallelogram, consecutive angles are supplementary (they add to 180°).

$$\text{If ABCD is a parallelogram, then } \angle A + \angle B = 180°, \angle B + \angle C = 180°, \text{ etc.}$$

### Property 4: Diagonals Bisect Each Other

**Theorem**: In a parallelogram, the diagonals bisect each other. (They cut each other in half at their intersection point.)

If the diagonals AC and BD intersect at point E, then:
$$AE = EC \text{ and } BE = ED$$

This is one of the most useful properties!

## Proving a Quadrilateral is a Parallelogram (If ... Then It's a Parallelogram)

Sometimes you're given information about a quadrilateral and need to prove it's a parallelogram. Here are the converse theorems:

### Method 1: Show Both Pairs of Opposite Sides Are Parallel
If both pairs of opposite sides are parallel, it's a parallelogram. (This is literally the definition.)

### Method 2: Show Both Pairs of Opposite Sides Are Congruent
**Theorem**: If both pairs of opposite sides of a quadrilateral are congruent, then it's a parallelogram.

### Method 3: Show Both Pairs of Opposite Angles Are Congruent
**Theorem**: If both pairs of opposite angles of a quadrilateral are congruent, then it's a parallelogram.

### Method 4: Show One Pair of Opposite Sides Are Both Parallel AND Congruent
**Theorem**: If one pair of opposite sides of a quadrilateral are both parallel and congruent, then it's a parallelogram.

This is powerful because you only need to verify one pair!

### Method 5: Show the Diagonals Bisect Each Other
**Theorem**: If the diagonals of a quadrilateral bisect each other, then it's a parallelogram.

## Worked Examples

### Example 1: Find All Angles in a Parallelogram

**Given**: Parallelogram ABCD where ∠A = 65°. Find all four angles.

**Solution**:
- Since opposite angles are congruent: ∠C = ∠A = 65°
- Since consecutive angles are supplementary: ∠B = 180° - 65° = 115°
- Since opposite angles are congruent: ∠D = ∠B = 115°

**Check**: 65° + 115° + 65° + 115° = 360° ✓ (angles of a quadrilateral sum to 360°)

**Answer**: ∠A = 65°, ∠B = 115°, ∠C = 65°, ∠D = 115°

### Example 2: Use Diagonal Bisecting Property

**Given**: Parallelogram PQRS with diagonals intersecting at point M. If PM = 3x + 1 and MR = 5x - 7, find x and the length of diagonal PR.

**Solution**:
- Since diagonals bisect each other: PM = MR
- Set up equation: 3x + 1 = 5x - 7
- Solve: 1 + 7 = 5x - 3x
- 8 = 2x
- x = 4

Length of diagonal PR = PM + MR = (3(4) + 1) + (5(4) - 7) = 13 + 13 = 26

**Answer**: x = 4, and PR = 26

### Example 3: Prove a Quadrilateral is a Parallelogram

**Given**: Quadrilateral EFGH where EF ∥ HG and EF = HG. Prove that EFGH is a parallelogram.

**Proof**:
1. We're given that EF ∥ HG and EF = HG.
2. By the "one pair opposite sides parallel and congruent" theorem, EFGH is a parallelogram.

**Done!** (This is an application of Method 4 above.)

### Example 4: Two-Step Reasoning

**Given**: Quadrilateral ABCD with AB = CD = 5 cm and BC = DA = 8 cm. Prove that ABCD is a parallelogram.

**Proof**:
1. We're given that both pairs of opposite sides are congruent: AB = CD and BC = DA.
2. By the "opposite sides congruent" theorem (Method 2), ABCD is a parallelogram.

**Answer**: ABCD is a parallelogram.

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Thinking a quadrilateral is a parallelogram just because it "looks" like one.
✓ **Tip**: You MUST verify one of the conditions (opposite sides parallel, opposite sides congruent, opposite angles congruent, one pair opposite sides parallel and congruent, or diagonals bisect each other).

❌ **Mistake 2**: Forgetting that consecutive angles are supplementary.
✓ **Tip**: In a parallelogram, adjacent angles add up to 180°. This is different from opposite angles being equal.

❌ **Mistake 3**: Confusing "diagonals bisect each other" with "diagonals are equal in length."
✓ **Tip**: A parallelogram's diagonals bisect each other, but they're NOT necessarily equal in length. (That extra property comes in rectangles.)

❌ **Mistake 4**: Only checking one pair of opposite sides when you need to check both pairs.
✓ **Tip**: If you're showing opposite sides are congruent or parallel, you must verify both pairs, not just one.

---

# RECTANGLES

## Definition

A **rectangle** is a quadrilateral that is **both a parallelogram AND has all four right angles (90°)**.

Equivalently: A rectangle is a parallelogram where every interior angle equals 90°.

## Key Vocabulary

- **Length**: Usually the longer pair of opposite sides.
- **Width**: Usually the shorter pair of opposite sides.
- These terms are informal; mathematically, we just call them sides.

## Properties of Rectangles

A rectangle has **all properties of a parallelogram**, PLUS these special properties:

### Property 1: All Angles Are Right Angles
$$\angle A = \angle B = \angle C = \angle D = 90°$$

### Property 2: Diagonals Are Congruent

**Theorem**: In a rectangle, the diagonals are congruent (equal in length).

This is the KEY property that distinguishes rectangles from general parallelograms!

$$\text{If ABCD is a rectangle, then diagonal } AC = \text{ diagonal } BD$$

### Property 3: Diagonals Bisect Each Other (from Parallelogram)

Just like any parallelogram, the diagonals bisect each other.

## Proving a Quadrilateral is a Rectangle

You can prove a quadrilateral is a rectangle in these ways:

### Method 1: Show It's a Parallelogram with One Right Angle
If you can prove it's a parallelogram and then show that one angle is 90°, then all angles are 90° (by the consecutive angles supplementary property), and it's a rectangle.

### Method 2: Show It's a Parallelogram with Congruent Diagonals
**Theorem**: If a parallelogram has congruent diagonals, then it's a rectangle.

### Method 3: Show All Four Angles Are Right Angles
This directly satisfies the definition.

### Method 4: Show It's a Parallelogram with Perpendicular Diagonals (Not This!)
❌ This does NOT work. Perpendicular diagonals make a rhombus, not a rectangle.

## Worked Examples

### Example 1: Find the Diagonal Length

**Given**: Rectangle ABCD with length AB = 8 and width BC = 6. Find the length of diagonal AC.

**Solution**:
- The diagonal AC forms a right triangle ABC with legs AB = 8 and BC = 6.
- By the Pythagorean theorem: AC² = 8² + 6² = 64 + 36 = 100
- AC = 10

**Answer**: The diagonal is 10 units.

### Example 2: Diagonals and Bisection

**Given**: Rectangle PQRS with diagonals intersecting at point M. If diagonal PR = 20, find PM.

**Solution**:
- Since the diagonals bisect each other in a parallelogram (and a rectangle is a parallelogram):
- PM = PR / 2 = 20 / 2 = 10

**Answer**: PM = 10

### Example 3: Prove a Parallelogram is a Rectangle

**Given**: Parallelogram EFGH with diagonals EG = 26 and FH = 26. Prove EFGH is a rectangle.

**Proof**:
1. We know EFGH is a parallelogram (given).
2. The diagonals EG and FH are congruent (both equal 26).
3. By the "parallelogram with congruent diagonals is a rectangle" theorem, EFGH is a rectangle.

**Answer**: EFGH is a rectangle.

### Example 4: Complex Angle Problem

**Given**: Rectangle JKLM. One angle is listed as (2x + 10)°. Find x.

**Solution**:
- Every angle in a rectangle is 90°.
- So: 2x + 10 = 90
- 2x = 80
- x = 40

**Answer**: x = 40

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Thinking a quadrilateral with one right angle is a rectangle.
✓ **Tip**: All four angles must be right angles (or equivalently, it must be a parallelogram with congruent diagonals).

❌ **Mistake 2**: Assuming the diagonals of a rectangle are perpendicular.
✓ **Tip**: Rectangle diagonals are congruent and bisect each other, but they're NOT perpendicular (that's a rhombus property).

❌ **Mistake 3**: Using the wrong method to prove it's a rectangle.
✓ **Tip**: The most powerful method is usually "it's a parallelogram with congruent diagonals."

---

# RHOMBI

## Definition

A **rhombus** is a quadrilateral that is **both a parallelogram AND has all four sides congruent (equal in length)**.

Equivalently: A rhombus is a parallelogram where every side has the same length.

Plural: **Rhombi** (or sometimes "rhombuses").

## Key Vocabulary

- **Diagonal**: In a rhombus, the diagonals have special properties (see below).

## Properties of Rhombi

A rhombus has **all properties of a parallelogram**, PLUS these special properties:

### Property 1: All Sides Are Congruent
$$AB = BC = CD = DA$$

### Property 2: Diagonals Are Perpendicular

**Theorem**: In a rhombus, the diagonals are perpendicular to each other (they meet at 90°).

This is the KEY property that distinguishes rhombi from general parallelograms!

### Property 3: Diagonals Bisect the Angles

**Theorem**: In a rhombus, each diagonal bisects the angles at its endpoints.

If diagonal AC is drawn, then:
- It bisects ∠A: ∠DAC = ∠BAC
- It bisects ∠C: ∠DCA = ∠BCA

**Intuition**: The rhombus is symmetric along each diagonal, so the diagonal cuts each angle in half.

### Property 4: Diagonals Bisect Each Other (from Parallelogram)

Just like any parallelogram, the diagonals bisect each other.

## Proving a Quadrilateral is a Rhombus

### Method 1: Show It's a Parallelogram with All Sides Congruent
If you prove it's a parallelogram and then show all four sides are equal, it's a rhombus.

### Method 2: Show All Four Sides Are Congruent
**Theorem**: If all four sides of a quadrilateral are congruent, then it's a rhombus.

### Method 3: Show It's a Parallelogram with Perpendicular Diagonals
**Theorem**: If a parallelogram has perpendicular diagonals, then it's a rhombus.

### Method 4: Show It's a Parallelogram Where the Diagonals Bisect the Angles
**Theorem**: If a parallelogram has diagonals that bisect the angles, then it's a rhombus.

## Worked Examples

### Example 1: All Sides Congruent

**Given**: Quadrilateral ABCD with all sides equal to 7 cm. Is this necessarily a rhombus?

**Solution**:
- No! Having all sides equal is necessary but not sufficient. A rhombus must be a quadrilateral with all equal sides, but we haven't verified the definition fully.
- Wait, let me reconsider: The definition of a rhombus is "a parallelogram with all sides congruent." So we'd need to first verify it's a parallelogram.
- However, actually, there's a theorem: if all four sides are congruent, then the quadrilateral IS a rhombus (it forces it to be a parallelogram).

**Answer**: Yes, it's a rhombus.

### Example 2: Perpendicular Diagonals in a Parallelogram

**Given**: Parallelogram PQRS where the diagonals PR and QS are perpendicular. Prove PQRS is a rhombus.

**Proof**:
1. PQRS is a parallelogram (given).
2. The diagonals PR and QS are perpendicular (given).
3. By the "parallelogram with perpendicular diagonals is a rhombus" theorem, PQRS is a rhombus.

**Answer**: PQRS is a rhombus.

### Example 3: Using the Angle Bisecting Property

**Given**: Rhombus EFGH with diagonal EG. If ∠FEG = 35°, find ∠FEH.

**Solution**:
- In a rhombus, diagonal EG bisects ∠E (which is ∠FEH).
- So ∠FEG = ∠HEG.
- We're told ∠FEG = 35°.
- Therefore: ∠FEH = ∠FEG + ∠HEG = 35° + 35° = 70°

**Answer**: ∠FEH = 70°

### Example 4: Diagonals and Perpendicularity

**Given**: Rhombus ABCD with diagonals AC and BD intersecting at point M. If diagonal AC = 12 and diagonal BD = 16, find the length of side AB.

**Solution**:
- The diagonals bisect each other: AM = 6 and BM = 8.
- The diagonals are perpendicular, so triangle AMB is a right triangle with legs AM = 6 and BM = 8.
- By the Pythagorean theorem: AB² = 6² + 8² = 36 + 64 = 100
- AB = 10

**Answer**: AB = 10

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Confusing rectangle and rhombus.
✓ **Tip**: Rectangle has congruent diagonals; rhombus has perpendicular diagonals. They're different!

❌ **Mistake 2**: Thinking a quadrilateral with all equal sides is automatically a rhombus.
✓ **Tip**: Technically, if all four sides are equal, it IS a rhombus. But a non-planar quadrilateral (a skewed one) could be different. In plane geometry, equal sides implies a rhombus (or a square, which is a special rhombus).

❌ **Mistake 3**: Assuming a rhombus's diagonals are equal in length.
✓ **Tip**: A rhombus's diagonals are perpendicular but NOT equal in length (unless it's a square!).

❌ **Mistake 4**: Forgetting that a rhombus is a parallelogram.
✓ **Tip**: A rhombus has ALL properties of a parallelogram (opposite sides parallel, opposite angles congruent, consecutive angles supplementary, diagonals bisect each other) PLUS the special rhombus properties.

---

# SQUARES

## Definition

A **square** is a quadrilateral that is **both a rectangle AND a rhombus**.

Equivalently: A square is a parallelogram with all sides congruent AND all angles right angles.

Or: A square is a rectangle with all sides congruent.

Or: A square is a rhombus with all angles right angles.

## Key Vocabulary

- **Diagonal**: In a square, the diagonals have ALL the special properties.
- **Side**: All four sides are equal in a square.

## Properties of Squares

A square has **all properties of rectangles and rhombi**, combined:

### From Rectangles:
- All angles are 90°
- Diagonals are congruent
- Diagonals bisect each other

### From Rhombi:
- All sides are congruent
- Diagonals are perpendicular
- Diagonals bisect the angles

### Combined in a Square:
1. **All sides congruent**: AB = BC = CD = DA
2. **All angles are right angles**: ∠A = ∠B = ∠C = ∠D = 90°
3. **Diagonals are congruent**: AC = BD
4. **Diagonals are perpendicular**: AC ⊥ BD
5. **Diagonals bisect each other**: They meet at the center
6. **Diagonals bisect the angles**: Each diagonal cuts the corner angles in half (45° each)

## Proving a Quadrilateral is a Square

### Method 1: Show It's a Rectangle with Congruent Sides
If you prove it's a rectangle and then show all four sides are equal, it's a square.

### Method 2: Show It's a Rhombus with Congruent Diagonals
If you prove it's a rhombus and then show the diagonals are equal, it's a square.

### Method 3: Show It's a Rhombus with One Right Angle
If you prove it's a rhombus and then show one angle is 90°, all angles are 90°, so it's a square.

### Method 4: Show It's a Rectangle with Perpendicular Diagonals
If you prove it's a rectangle and then show the diagonals are perpendicular, it's a square.

## Worked Examples

### Example 1: All Properties Present

**Given**: Square ABCD with side length 5. Find:
(a) The length of diagonal AC
(b) The distance from the center to vertex A
(c) The angle between diagonal AC and side AB

**Solution**:

(a) The diagonal and two sides form a right isosceles triangle.
   - AC² = 5² + 5² = 25 + 25 = 50
   - AC = √50 = 5√2

(b) The diagonals bisect each other. The center is at the midpoint of AC.
   - Distance from center to A = AC / 2 = (5√2) / 2 = (5√2) / 2

(c) The diagonal bisects the right angle at A.
   - ∠BAC = 90° / 2 = 45°

**Answer**: (a) 5√2, (b) (5√2)/2, (c) 45°

### Example 2: Prove It's a Square

**Given**: Quadrilateral PQRS where PQ = QR = RS = SP = 8 and all angles are 90°. Prove it's a square.

**Proof**:
1. All sides are congruent: PQ = QR = RS = SP = 8 (given).
2. All angles are right angles (given).
3. By definition, a square is a parallelogram with all sides congruent and all angles right angles.
4. Therefore, PQRS is a square.

**Answer**: PQRS is a square.

### Example 3: Diagonal Angles

**Given**: Square EFGH with diagonals EG and FH intersecting at point M. Find the measure of ∠EMF.

**Solution**:
- The diagonals of a square are perpendicular.
- So ∠EMF = 90°.

**Answer**: ∠EMF = 90°

### Example 4: Side from Diagonal

**Given**: Square JKLM with diagonal JL = 10√2. Find the side length.

**Solution**:
- In a square with side s, the diagonal d satisfies: d = s√2
- So: 10√2 = s√2
- s = 10

**Answer**: The side length is 10.

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Confusing "square" with "rectangle" or "rhombus."
✓ **Tip**: A square is BOTH. It has all the properties of both. A rectangle doesn't need to be a rhombus, and a rhombus doesn't need to be a rectangle. Only a square is both.

❌ **Mistake 2**: Thinking a shape with four equal sides and some right angles is a square.
✓ **Tip**: All four angles MUST be right angles (90°) for it to be a square.

❌ **Mistake 3**: Using the wrong diagonal length formula.
✓ **Tip**: In a square with side s, the diagonal is s√2. Memorize this!

---

# TRAPEZOIDS

## Definition

A **trapezoid** is a quadrilateral with **exactly one pair of parallel sides**.

This is the "exclusive" definition: NOT two pairs of parallel sides (which would be a parallelogram).

The parallel sides are called **bases**, and the non-parallel sides are called **legs**.

## Key Vocabulary

- **Bases**: The two parallel sides of a trapezoid.
- **Legs**: The two non-parallel sides of a trapezoid.
- **Midsegment (or Median)**: The line segment connecting the midpoints of the two legs.
- **Height (or Altitude)**: The perpendicular distance between the two bases.

## Properties of Trapezoids

### Property 1: Midsegment Theorem for Trapezoids

**Theorem**: The midsegment of a trapezoid is:
1. **Parallel to both bases**
2. **Equal in length to the average of the two bases**

If the bases have lengths b₁ and b₂, and M is the midsegment:

$$M = \frac{b_1 + b_2}{2}$$

**Why?** This comes from similar triangles and properties of parallel lines.

### Property 2: Angles on the Same Leg

In a trapezoid, if you look at the two angles on the same leg (same side), they are **supplementary** (add to 180°).

This is because the bases are parallel, and angles on the same transversal (the leg) are supplementary.

## Worked Examples

### Example 1: Find the Midsegment

**Given**: Trapezoid ABCD where AB ∥ CD, AB = 14, and CD = 8. Find the length of the midsegment.

**Solution**:
- Midsegment = (AB + CD) / 2 = (14 + 8) / 2 = 22 / 2 = 11

**Answer**: The midsegment is 11 units.

### Example 2: Find Missing Base

**Given**: Trapezoid PQRS where PQ ∥ RS. The midsegment is 18, and one base (PQ) is 12. Find the other base (RS).

**Solution**:
- Midsegment = (PQ + RS) / 2
- 18 = (12 + RS) / 2
- 36 = 12 + RS
- RS = 24

**Answer**: RS = 24

### Example 3: Angles on the Same Leg

**Given**: Trapezoid EFGH where EF ∥ GH. ∠E = 70°. Find ∠H (the angle on the same leg as E).

**Solution**:
- Angles E and H are on the same leg (EH) of the trapezoid.
- Since EF ∥ GH and EH is a transversal, ∠E and ∠H are supplementary (co-interior angles).
- ∠E + ∠H = 180°
- 70° + ∠H = 180°
- ∠H = 110°

**Answer**: ∠H = 110°

### Example 4: Complex Midsegment Problem

**Given**: Trapezoid JKLM where JK ∥ LM. The midsegment divides the trapezoid into two smaller trapezoids. If JK = 6 and LM = 14, find the midsegment length and verify it bisects the trapezoid properly.

**Solution**:
- Midsegment = (6 + 14) / 2 = 10
- The upper smaller trapezoid has bases JK = 6 and midsegment = 10.
- The lower smaller trapezoid has bases midsegment = 10 and LM = 14.
- Both smaller trapezoids have the same height (half of the original).

**Answer**: The midsegment is 10 units.

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Thinking a trapezoid has two pairs of parallel sides.
✓ **Tip**: A trapezoid has EXACTLY ONE pair of parallel sides. Two pairs would be a parallelogram.

❌ **Mistake 2**: Getting the midsegment formula backwards.
✓ **Tip**: Midsegment = (base₁ + base₂) / 2. It's the AVERAGE of the bases, not their product or sum.

❌ **Mistake 3**: Forgetting that angles on the same leg are supplementary.
✓ **Tip**: If the bases are parallel, then the angles on each leg add up to 180°.

---

# ISOSCELES TRAPEZOIDS

## Definition

An **isosceles trapezoid** is a trapezoid where **the two legs are congruent (equal in length)**.

It's like a trapezoid with a line of symmetry down the middle, so the two legs mirror each other.

## Key Vocabulary

- **Legs**: The non-parallel sides (which are congruent in an isosceles trapezoid).
- **Bases**: The parallel sides.
- **Base angles**: The angles at the ends of the same base.

## Properties of Isosceles Trapezoids

An isosceles trapezoid has **all properties of regular trapezoids**, PLUS these special properties:

### Property 1: Base Angles Are Congruent

**Theorem**: In an isosceles trapezoid, the angles at each base are congruent.

If bases are AB and CD, then:
- ∠A = ∠B (angles at base AB)
- ∠D = ∠C (angles at base CD)

**Intuition**: The symmetry of an isosceles trapezoid means the angles "match" at each base.

### Property 2: Diagonals Are Congruent

**Theorem**: In an isosceles trapezoid, the two diagonals are congruent (equal in length).

$$AC = BD$$

**Intuition**: The symmetry again—the diagonals mirror each other.

### Property 3: The Legs Are Congruent

By definition:
$$AD = BC$$

## Proving a Trapezoid is Isosceles

### Method 1: Show the Legs Are Congruent
If both legs are the same length, it's an isosceles trapezoid.

### Method 2: Show the Base Angles Are Congruent
**Theorem**: If a trapezoid has congruent base angles, then it's isosceles.

### Method 3: Show the Diagonals Are Congruent
**Theorem**: If a trapezoid has congruent diagonals, then it's isosceles.

## Worked Examples

### Example 1: Base Angles

**Given**: Isosceles trapezoid ABCD with AB ∥ CD. If ∠A = 65°, find all four angles.

**Solution**:
- Base angles at AB are congruent: ∠A = ∠B = 65°
- Angles on the same leg are supplementary: ∠A + ∠D = 180°
- So: 65° + ∠D = 180°, which gives ∠D = 115°
- Base angles at CD are congruent: ∠D = ∠C = 115°

**Check**: 65° + 65° + 115° + 115° = 360° ✓

**Answer**: ∠A = 65°, ∠B = 65°, ∠C = 115°, ∠D = 115°

### Example 2: Diagonals

**Given**: Isosceles trapezoid PQRS where the two diagonals have lengths (3x + 2) and (5x - 4). Find x and the diagonal length.

**Solution**:
- In an isosceles trapezoid, diagonals are congruent.
- Set them equal: 3x + 2 = 5x - 4
- Solve: 2 + 4 = 5x - 3x
- 6 = 2x
- x = 3

Diagonal length = 3(3) + 2 = 11

**Answer**: x = 3, and each diagonal is 11 units.

### Example 3: Prove It's Isosceles

**Given**: Trapezoid EFGH with EF ∥ GH. ∠E = 75° and ∠F = 75°. Prove EFGH is isosceles.

**Proof**:
1. EF ∥ GH (given).
2. ∠E = ∠F = 75° (given). These are base angles at the same base EF.
3. By the "trapezoid with congruent base angles is isosceles" theorem, EFGH is isosceles.

**Answer**: EFGH is an isosceles trapezoid.

### Example 4: Mixed Properties

**Given**: Isosceles trapezoid JKLM with JK ∥ LM, legs JM = KL = 5, base JK = 8, and base LM = 12. Find the length of diagonal JL.

**Solution**:
- This requires coordinate geometry or the trapezoid's height.
- The height h can be found by dropping perpendiculars from J and K to the base LM.
- The difference in base lengths is 12 - 8 = 4, divided equally on both sides: 2 units on each side.
- So we have a right triangle with leg = 2 and hypotenuse = 5 (the leg of the trapezoid).
- h² + 2² = 5²
- h² = 25 - 4 = 21
- h = √21

Now, using the right triangle JLM (where L is at the corner of the base):
- JL² = h² + (distance from J to L along the base)²
- From the setup, the horizontal distance is (12 - 8)/2 + 8 = 12. Wait, let me reconsider.

Actually, let me use coordinates:
- Place L at origin (0, 0)
- Place M at (12, 0)
- Place K at (2, √21) [since the extra length 4 is split as 2 on each side]
- Place J at (10, √21)

Wait, I should reconsider the setup. Let me place:
- L at (0, 0)
- M at (12, 0)
- J at (2, √21) [2 units from L horizontally]
- K at (10, √21) [2 units from M horizontally]

Then JK = 10 - 2 = 8 ✓

Diagonal JL from (2, √21) to (0, 0):
JL = √((2-0)² + (√21-0)²) = √(4 + 21) = √25 = 5

**Answer**: JL = 5 (interesting!)

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Confusing "isosceles trapezoid" with "isosceles triangle."
✓ **Tip**: An isosceles trapezoid is a quadrilateral with one pair of parallel sides and congruent legs. An isosceles triangle has two congruent sides.

❌ **Mistake 2**: Thinking ALL angles are congruent in an isosceles trapezoid.
✓ **Tip**: Only the base angles at each base are congruent. The angles at different bases are different (they're supplementary to the other base's angles).

❌ **Mistake 3**: Forgetting that the diagonals are congruent.
✓ **Tip**: This is a powerful property. If a trapezoid has congruent diagonals, it must be isosceles!

---

# KITES

## Definition

A **kite** is a quadrilateral with **two pairs of consecutive congruent sides**.

Think of it like a kite shape: AB = AD and CB = CD (the two "wings" are equal on each side).

## Key Vocabulary

- **Sides**: In kite ABCD with AB = AD and CB = CD:
  - AB and AD are one pair of consecutive congruent sides
  - CB and CD are another pair of consecutive congruent sides
- **Diagonals**: AC and BD. One of them has special properties.
- **Axis of symmetry**: The diagonal that connects the vertices where the congruent sides meet.

## Properties of Kites

### Property 1: One Pair of Opposite Angles Are Congruent

**Theorem**: In a kite, the angles between the congruent sides are congruent.

In kite ABCD (where AB = AD and CB = CD):
$$\angle A \cong \angle C$$

These are the angles at the "pointy" ends of the kite.

**Note**: The other pair of opposite angles (∠B and ∠D) are NOT necessarily congruent.

### Property 2: Diagonals Are Perpendicular

**Theorem**: The diagonals of a kite are perpendicular to each other.

$$AC \perp BD$$

### Property 3: One Diagonal Is Bisected by the Other

**Theorem**: In a kite, one diagonal (the "axis of symmetry") is bisected by the other diagonal.

In kite ABCD with AB = AD and CB = CD, diagonal AC bisects diagonal BD:
$$BE = ED$$ (where E is the intersection point)

**Note**: The other diagonal (BD) is NOT necessarily bisected; only AC bisects BD.

### Property 4: One Diagonal Bisects the Angles

The axis of symmetry bisects the angles at both ends of that diagonal.

## Proving a Quadrilateral is a Kite

### Method 1: Show Two Pairs of Consecutive Congruent Sides
If you show that AB = AD and CB = CD, it's a kite.

### Method 2: Show One Pair of Opposite Angles Are Congruent AND Diagonals Are Perpendicular
**Theorem**: If a quadrilateral has one pair of congruent opposite angles and perpendicular diagonals, it's a kite.

## Worked Examples

### Example 1: Angles in a Kite

**Given**: Kite ABCD with AB = AD and CB = CD. ∠A = 60°, ∠B = 95°. Find ∠C and ∠D.

**Solution**:
- In a kite, opposite angles at the "pointy" ends are congruent.
- ∠A = ∠C = 60°
- The sum of angles in a quadrilateral is 360°.
- ∠A + ∠B + ∠C + ∠D = 360°
- 60° + 95° + 60° + ∠D = 360°
- ∠D = 360° - 215° = 145°

**Answer**: ∠C = 60°, ∠D = 145°

### Example 2: Perpendicular Diagonals

**Given**: Kite PQRS with diagonals PR and QS intersecting at point E. If PR = 12 and QS = 8, and the diagonals are perpendicular, find the area.

**Solution**:
- For any quadrilateral with perpendicular diagonals d₁ and d₂:
- Area = (1/2) × d₁ × d₂
- Area = (1/2) × 12 × 8 = 48

**Answer**: Area = 48 square units

### Example 3: Diagonal Bisection

**Given**: Kite EFGH with EG = 14 and FH = 10. The diagonals intersect at point M. If FH is bisected by EG, find FM and MH.

**Solution**:
- Since EG (the axis of symmetry) bisects FH:
- FM = MH = FH / 2 = 10 / 2 = 5

**Answer**: FM = 5, MH = 5

### Example 4: Complex Kite Problem

**Given**: Kite JKLM with JK = JM = 6 and KL = ML = 8. The diagonals intersect at N. Find:
(a) The position of N on diagonal JL (if JL = 10)
(b) The length of diagonal KM

**Solution**:

(a) In kite JKLM, diagonal JL is the axis of symmetry. Diagonal KM is perpendicular to JL and intersects at N, where JL bisects KM. But we need to find where N is on JL.

Using coordinates:
- Place J at (0, 0)
- Place L at (10, 0) [since JL = 10]
- Place K at (5, h) for some height h

Since JK = 6: (5-0)² + (h-0)² = 36
25 + h² = 36
h² = 11
h = √11

Since KL = 8: (5-10)² + (h-0)² = 64
25 + h² = 64
h² = 39

Wait, this is inconsistent. Let me reconsider. Maybe JL is not on the x-axis for N.

Actually, the axis of symmetry in a kite connects the two vertices where sides of equal length meet. In kite JKLM with JK = JM and KL = ML, the axis of symmetry is... wait, I need to reread.

With JK = JM = 6 and KL = ML = 8, the vertices where equal sides meet are J (where JK and JM meet) and L (where KL and ML meet). So JL is the axis of symmetry.

Let's use coordinates:
- J at (0, 0)
- L at (10, 0)
- Place K symmetrically above the x-axis at some point (x, y)
- M is the reflection of K below the x-axis at (x, -y)

From JK = 6: x² + y² = 36
From KL = 8: (x - 10)² + y² = 64

Expanding: x² - 20x + 100 + y² = 64
Substituting x² + y² = 36: 36 - 20x + 100 = 64
136 - 20x = 64
20x = 72
x = 3.6

Then y² = 36 - (3.6)² = 36 - 12.96 = 23.04
y = 4.8

So K is at (3.6, 4.8) and M is at (3.6, -4.8).

(a) The diagonal KM connects (3.6, 4.8) and (3.6, -4.8), so it's vertical and intersects JL (the x-axis) at (3.6, 0). The distance from J (0, 0) to N (3.6, 0) is 3.6.

(b) The diagonal KM has length 4.8 - (-4.8) = 9.6.

**Answer**: (a) N is 3.6 units from J along JL. (b) KM = 9.6

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Thinking a kite has two pairs of opposite congruent sides.
✓ **Tip**: A kite has two pairs of CONSECUTIVE congruent sides, not opposite. A rhombus has opposite sides congruent.

❌ **Mistake 2**: Thinking both diagonals are bisected in a kite.
✓ **Tip**: Only the axis of symmetry bisects the other diagonal. The axis of symmetry itself is NOT bisected.

❌ **Mistake 3**: Assuming both pairs of opposite angles are congruent.
✓ **Tip**: Only ONE pair of opposite angles (the ones at the ends of the axis of symmetry) are congruent.

❌ **Mistake 4**: Confusing kites with parallelograms.
✓ **Tip**: A kite is NOT a parallelogram. Kites have perpendicular diagonals (like rhombi) but don't have parallel sides.

---

# COORDINATE GEOMETRY PROOFS

## Overview

One of the most powerful tools in geometry is to use **coordinates** to prove properties of quadrilaterals.

The basic idea:
1. Place the quadrilateral on a coordinate plane
2. Use formulas (distance, slope, midpoint) to compute properties
3. Compare properties to characteristics of different quadrilaterals
4. Conclude what type of quadrilateral it is

## Key Formulas

### Distance Formula
The distance between points (x₁, y₁) and (x₂, y₂) is:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Use this to**: Find side lengths, compare if sides are congruent, find diagonal lengths.

### Slope Formula
The slope of the line through (x₁, y₁) and (x₂, y₂) is:

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

**Use this to**: Check if lines are parallel (equal slopes), check if lines are perpendicular (slopes multiply to -1).

### Midpoint Formula
The midpoint of the segment from (x₁, y₁) to (x₂, y₂) is:

$$M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$$

**Use this to**: Check if diagonals bisect each other (do both diagonals have the same midpoint?).

### Slope Relationship for Perpendicularity
Two lines are **perpendicular** if their slopes m₁ and m₂ satisfy:

$$m_1 \cdot m_2 = -1$$

(Or one slope is undefined and the other is 0, meaning vertical and horizontal lines.)

### Slope Relationship for Parallelism
Two lines are **parallel** if their slopes are equal:

$$m_1 = m_2$$

## Strategy: Proving What Type of Quadrilateral

### To Prove a Parallelogram:

**Method 1**: Show opposite sides are congruent using distance formula.
- Find the length of AB, BC, CD, DA.
- Check if AB = CD and BC = DA.

**Method 2**: Show diagonals bisect each other using midpoint formula.
- Find the midpoint of diagonal AC.
- Find the midpoint of diagonal BD.
- Check if they're the same point.

**Method 3**: Show one pair of opposite sides are parallel and congruent.
- Find slopes of AB and CD; check if they're equal (parallel).
- Find lengths of AB and CD; check if they're equal (congruent).

### To Prove a Rectangle:

**Method 1**: Show it's a parallelogram with congruent diagonals.
- Prove it's a parallelogram (using one method above).
- Find diagonal lengths AC and BD.
- Check if AC = BD.

**Method 2**: Show it's a parallelogram with perpendicular sides.
- Prove it's a parallelogram.
- Find slopes of adjacent sides (e.g., AB and BC).
- Check if slopes multiply to -1 (perpendicular) or slopes are undefined and 0.

### To Prove a Rhombus:

**Method 1**: Show it's a parallelogram with all sides congruent.
- Prove it's a parallelogram.
- Find all side lengths.
- Check if all four are equal.

**Method 2**: Show it's a parallelogram with perpendicular diagonals.
- Prove it's a parallelogram.
- Find slopes of diagonals AC and BD.
- Check if they multiply to -1 (perpendicular).

### To Prove a Square:

**Method 1**: Show it's a rectangle with all sides congruent.
- Prove it's a rectangle.
- Find all side lengths.
- Check if all four are equal.

**Method 2**: Show it's a rhombus with congruent diagonals.
- Prove it's a rhombus.
- Find diagonal lengths.
- Check if they're equal.

## Worked Examples

### Example 1: Prove It's a Parallelogram

**Given**: Quadrilateral with vertices A(0, 0), B(4, 1), C(6, 5), D(2, 4). Prove ABCD is a parallelogram.

**Solution**:

We'll show diagonals bisect each other.

Midpoint of AC:
$$M_{AC} = \left( \frac{0 + 6}{2}, \frac{0 + 5}{2} \right) = (3, 2.5)$$

Midpoint of BD:
$$M_{BD} = \left( \frac{4 + 2}{2}, \frac{1 + 4}{2} \right) = (3, 2.5)$$

Since the midpoints are the same, the diagonals bisect each other. By the converse theorem, ABCD is a parallelogram. ✓

### Example 2: Prove It's a Rectangle

**Given**: Quadrilateral with vertices P(0, 0), Q(5, 0), R(5, 3), S(0, 3). Prove PQRS is a rectangle.

**Solution**:

First, we'll show it's a parallelogram by checking opposite sides are equal.

$$PQ = \sqrt{(5-0)^2 + (0-0)^2} = 5$$
$$RS = \sqrt{(0-5)^2 + (3-3)^2} = 5$$

$$QR = \sqrt{(5-5)^2 + (3-0)^2} = 3$$
$$PS = \sqrt{(0-0)^2 + (3-0)^2} = 3$$

Opposite sides are congruent, so PQRS is a parallelogram.

Now, check if diagonals are congruent:
$$PR = \sqrt{(5-0)^2 + (3-0)^2} = \sqrt{25 + 9} = \sqrt{34}$$
$$QS = \sqrt{(0-5)^2 + (3-0)^2} = \sqrt{25 + 9} = \sqrt{34}$$

The diagonals are congruent. A parallelogram with congruent diagonals is a rectangle. ✓

**Alternative check**: We could verify that adjacent sides are perpendicular.
Slope of PQ = 0 (horizontal)
Slope of QR = undefined (vertical)
A horizontal and vertical line are perpendicular. ✓

### Example 3: Prove It's a Rhombus

**Given**: Quadrilateral with vertices J(1, 3), K(4, 0), L(7, 3), M(4, 6). Prove JKLM is a rhombus.

**Solution**:

Find all side lengths:
$$JK = \sqrt{(4-1)^2 + (0-3)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}$$
$$KL = \sqrt{(7-4)^2 + (3-0)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}$$
$$LM = \sqrt{(4-7)^2 + (6-3)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}$$
$$MJ = \sqrt{(1-4)^2 + (3-6)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}$$

All four sides are congruent. We should verify it's a parallelogram (not just a kite).

Midpoint of diagonal JL:
$$M_{JL} = \left( \frac{1+7}{2}, \frac{3+3}{2} \right) = (4, 3)$$

Midpoint of diagonal KM:
$$M_{KM} = \left( \frac{4+4}{2}, \frac{0+6}{2} \right) = (4, 3)$$

The diagonals bisect each other, so it's a parallelogram. A parallelogram with all sides congruent is a rhombus. ✓

### Example 4: Prove It's a Square

**Given**: Quadrilateral with vertices E(0, 0), F(3, 0), G(3, 3), H(0, 3). Prove EFGH is a square.

**Solution**:

Find side lengths:
$$EF = \sqrt{(3-0)^2 + (0-0)^2} = 3$$
$$FG = \sqrt{(3-3)^2 + (3-0)^2} = 3$$
$$GH = \sqrt{(0-3)^2 + (3-3)^2} = 3$$
$$HE = \sqrt{(0-0)^2 + (0-3)^2} = 3$$

All sides are equal, so it's at least a rhombus. Now check diagonals:
$$EG = \sqrt{(3-0)^2 + (3-0)^2} = \sqrt{18} = 3\sqrt{2}$$
$$FH = \sqrt{(0-3)^2 + (3-0)^2} = \sqrt{18} = 3\sqrt{2}$$

Diagonals are congruent. A rhombus with congruent diagonals is a square. ✓

**Alternative**: Check that adjacent sides are perpendicular.
Slope of EF = 0
Slope of FG = undefined
Perpendicular. ✓

### Example 5: Tricky One — Is It a Trapezoid?

**Given**: Quadrilateral with vertices A(0, 0), B(6, 0), C(8, 2), D(2, 2). Determine what type of quadrilateral this is.

**Solution**:

First, check if opposite sides are parallel by comparing slopes.

Slope of AB:
$$m_{AB} = \frac{0-0}{6-0} = 0$$

Slope of CD:
$$m_{CD} = \frac{2-2}{2-8} = \frac{0}{-6} = 0$$

AB and CD are parallel (both horizontal).

Slope of BC:
$$m_{BC} = \frac{2-0}{8-6} = \frac{2}{2} = 1$$

Slope of DA:
$$m_{DA} = \frac{0-2}{0-2} = \frac{-2}{-2} = 1$$

BC and DA are also parallel! So opposite sides are parallel, making it at least a parallelogram.

Now check side lengths:
$$AB = 6$$
$$CD = |8 - 2| = 6$$
$$BC = \sqrt{(8-6)^2 + (2-0)^2} = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}$$
$$DA = \sqrt{(2-0)^2 + (2-0)^2} = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}$$

Opposite sides are equal, confirming it's a parallelogram. But not all four sides are equal, so it's not a rhombus.

Check diagonal lengths:
$$AC = \sqrt{(8-0)^2 + (2-0)^2} = \sqrt{64 + 4} = \sqrt{68} = 2\sqrt{17}$$
$$BD = \sqrt{(2-6)^2 + (2-0)^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$$

Diagonals are not equal, so it's not a rectangle.

**Answer**: ABCD is a **parallelogram** (but not a rectangle, rhombus, or square).

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Computing distance with the wrong formula.
✓ **Tip**: Use $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. Don't forget the square root!

❌ **Mistake 2**: Confusing slope for parallel lines vs. perpendicular lines.
✓ **Tip**: Parallel: equal slopes. Perpendicular: product of slopes = -1.

❌ **Mistake 3**: Not checking that it's a parallelogram before concluding it's a rectangle, rhombus, or square.
✓ **Tip**: These special quadrilaterals are special types of parallelograms. Start by proving it's a parallelogram, then add the special property.

❌ **Mistake 4**: Forgetting to simplify or double-check arithmetic.
✓ **Tip**: Coordinate proofs involve lots of calculation. Double-check midpoints, distances, and slope calculations.

---

# PERIMETER AND DISTANCE

## Computing Perimeter Using the Distance Formula

The **perimeter** of a polygon is the sum of the lengths of all its sides.

**Method**:
1. Find the coordinates of all vertices.
2. Use the distance formula to find the length of each side.
3. Add up all the side lengths.

## Distance Formula (Review)

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

## Worked Examples

### Example 1: Perimeter of a Triangle

**Given**: Triangle with vertices A(0, 0), B(3, 4), C(6, 0). Find the perimeter.

**Solution**:

$$AB = \sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

$$BC = \sqrt{(6-3)^2 + (0-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

$$CA = \sqrt{(0-6)^2 + (0-0)^2} = \sqrt{36 + 0} = 6$$

Perimeter = AB + BC + CA = 5 + 5 + 6 = 16

**Answer**: The perimeter is 16 units.

### Example 2: Perimeter of a Quadrilateral

**Given**: Quadrilateral PQRS with P(0, 0), Q(4, 0), R(5, 3), S(1, 3). Find the perimeter.

**Solution**:

$$PQ = \sqrt{(4-0)^2 + (0-0)^2} = 4$$

$$QR = \sqrt{(5-4)^2 + (3-0)^2} = \sqrt{1 + 9} = \sqrt{10}$$

$$RS = \sqrt{(1-5)^2 + (3-3)^2} = \sqrt{16 + 0} = 4$$

$$SP = \sqrt{(0-1)^2 + (0-3)^2} = \sqrt{1 + 9} = \sqrt{10}$$

Perimeter = 4 + √10 + 4 + √10 = 8 + 2√10 ≈ 8 + 6.32 ≈ 14.32

**Answer**: The perimeter is 8 + 2√10 units (or approximately 14.32 units).

### Example 3: Perimeter of a Pentagon

**Given**: Pentagon with vertices A(0, 0), B(4, 0), C(5, 3), D(2, 4), E(-1, 2). Find the perimeter.

**Solution**:

$$AB = \sqrt{(4-0)^2 + (0-0)^2} = 4$$

$$BC = \sqrt{(5-4)^2 + (3-0)^2} = \sqrt{1 + 9} = \sqrt{10}$$

$$CD = \sqrt{(2-5)^2 + (4-3)^2} = \sqrt{9 + 1} = \sqrt{10}$$

$$DE = \sqrt{(-1-2)^2 + (2-4)^2} = \sqrt{9 + 4} = \sqrt{13}$$

$$EA = \sqrt{(0-(-1))^2 + (0-2)^2} = \sqrt{1 + 4} = \sqrt{5}$$

Perimeter = 4 + √10 + √10 + √13 + √5 = 4 + 2√10 + √13 + √5

Approximate: 4 + 6.32 + 3.61 + 2.24 ≈ 16.17

**Answer**: The perimeter is 4 + 2√10 + √13 + √5 units (or approximately 16.17 units).

## Perimeter Formulas for Special Quadrilaterals

### Rectangle with Length l and Width w
$$P = 2l + 2w = 2(l + w)$$

### Square with Side s
$$P = 4s$$

### Rhombus with Side s
$$P = 4s$$

### Parallelogram with Sides a and b
$$P = 2a + 2b = 2(a + b)$$

### Trapezoid with Bases b₁, b₂ and Legs c, d
$$P = b_1 + b_2 + c + d$$

### Isosceles Trapezoid with Bases b₁, b₂ and Legs c (both equal)
$$P = b_1 + b_2 + 2c$$

## Worked Examples Using Special Formulas

### Example 4: Rectangle Perimeter

**Given**: Rectangle with length 8 and width 5. Find the perimeter.

**Solution**:
$$P = 2(l + w) = 2(8 + 5) = 2(13) = 26$$

**Answer**: The perimeter is 26 units.

### Example 5: Square Perimeter

**Given**: Square with side 6. Find the perimeter.

**Solution**:
$$P = 4s = 4(6) = 24$$

**Answer**: The perimeter is 24 units.

### Example 6: Isosceles Trapezoid Perimeter

**Given**: Isosceles trapezoid with bases 12 and 8, and legs 5 each. Find the perimeter.

**Solution**:
$$P = b_1 + b_2 + 2c = 12 + 8 + 2(5) = 12 + 8 + 10 = 30$$

**Answer**: The perimeter is 30 units.

## Common Mistakes and Exam Tips

❌ **Mistake 1**: Forgetting to take the square root when using the distance formula.
✓ **Tip**: The distance formula has a square root: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. Don't stop at the part under the radical!

❌ **Mistake 2**: Adding only some sides (e.g., forgetting a side).
✓ **Tip**: The perimeter includes ALL sides of the polygon. Count them: a quadrilateral has 4 sides, a pentagon has 5, etc.

❌ **Mistake 3**: Using the wrong formula for a special quadrilateral.
✓ **Tip**: Know the formulas above. They make calculations faster. For example, a rhombus always has P = 4s, regardless of angles.

❌ **Mistake 4**: Not simplifying radicals.
✓ **Tip**: When you get $\sqrt{10}$, leave it as is. When you get $\sqrt{18}$, simplify to $3\sqrt{2}$.

---

## SUMMARY: THE QUADRILATERAL FAMILY TREE

```
                           QUADRILATERAL
                          (4 sides, 360°)
                                 |
                          TRAPEZOID
                     (exactly 1 pair || sides)
                                 |
                        PARALLELOGRAM
                  (2 pairs opposite || sides)
                      /                  \
                 RECTANGLE            RHOMBUS
              (all right angles)   (all sides equal)
                (diag. congruent)   (diag. perpendicular)
                      \                  /
                        SQUARE
                (rect. + rhombus)
        (all sides equal + all right angles)

ALSO: KITE (2 pairs consecutive congruent sides)
```

---

## KEY THEOREMS AT A GLANCE

| Quadrilateral | Opposite Sides | Opposite Angles | Consecutive Angles | All Sides Equal | All Angles Right | Diagonals Congruent | Diagonals Perpendicular | Diagonals Bisect Each Other | Exactly 1 || Side Pair |
|---|---|---|---|---|---|---|---|---|---|
| **Trapezoid** | — | — | Some supplementary | — | — | — | — | — | ✓ |
| **Parallelogram** | ✓ | ✓ | Supplementary | — | — | — | — | ✓ | — |
| **Rectangle** | ✓ | ✓ | Supplementary | — | ✓ | ✓ | — | ✓ | — |
| **Rhombus** | ✓ | ✓ | Supplementary | ✓ | — | — | ✓ | ✓ | — |
| **Square** | ✓ | ✓ | Supplementary | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| **Isosceles Trapezoid** | One pair | Base pairs | Some supplementary | — | — | ✓ | — | — | ✓ |
| **Kite** | — | One pair | — | Two pairs consec. | — | — | ✓ | — | Partial |

---

## PRACTICE: DECISION FLOWCHART

**Given a quadrilateral, how do you figure out what type it is?**

1. **Are both pairs of opposite sides parallel?**
   - YES → It's a PARALLELOGRAM or a special type. Go to step 2.
   - NO → Go to step 3.

2. **For a parallelogram, check special properties:**
   - All sides equal AND all angles right? → SQUARE
   - All sides equal (but not all angles right)? → RHOMBUS
   - All angles right (but not all sides equal)? → RECTANGLE
   - None of the above? → PARALLELOGRAM

3. **Is there exactly one pair of parallel sides?**
   - YES → It's a TRAPEZOID. Is it isosceles (legs equal)? → ISOSCELES TRAPEZOID
   - NO → Go to step 4.

4. **Are there two pairs of consecutive congruent sides?**
   - YES → It's a KITE.
   - NO → It's just a QUADRILATERAL.

---

## FINAL STUDY TIPS

1. **Understand the hierarchy**: Every square is a rectangle, rhombus, and parallelogram. Use this to your advantage when proving properties.

2. **Master the angle formulas**: Interior angle sum = (n-2)×180°, and exterior angles always sum to 360°. These are fundamental.

3. **Know the special properties**:
   - Rectangles: congruent diagonals
   - Rhombi: perpendicular diagonals
   - Parallelograms: diagonals bisect each other
   - Isosceles trapezoids: congruent diagonals

4. **Use coordinate proofs**: When in doubt on a proof, place the shape on a coordinate system and use distance, slope, and midpoint formulas.

5. **Don't memorize blindly**: Understand WHY each property is true. Draw diagrams, test examples, and reason through the proofs.

6. **Practice the converse**: For every "If parallelogram, then..." statement, know the converse: "If ..., then parallelogram."

Good luck with your studies!
