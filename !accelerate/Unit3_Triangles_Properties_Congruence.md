# Unit 3: Triangles — Properties & Congruence
## Honors Geometry Comprehensive Study Notes

---

## Table of Contents
1. [Foundations: What is a Triangle?](#foundations)
2. [Triangle Classification](#classification)
3. [Triangle Angle Sum Theorem](#angle-sum)
4. [Exterior Angle Theorem](#exterior-angle)
5. [Triangle Inequality Theorem](#triangle-inequality)
6. [Isosceles Triangle Theorem](#isosceles-triangle)
7. [Triangle Congruence: The Five Theorems](#congruence-theorems)
8. [Why SSA Doesn't Work](#ssa-fails)
9. [CPCTC: Using Congruence in Proofs](#cpctc)
10. [Two-Column Proofs Explained](#two-column-proofs)
11. [Special Segments in Triangles](#special-segments)
12. [Four Centers of a Triangle](#triangle-centers)
13. [Midsegment Theorem](#midsegment)
14. [Coordinate Proofs](#coordinate-proofs)

---

## <a name="foundations"></a>Foundations: What is a Triangle?

### Plain English Definition
A **triangle** is a polygon (closed shape) made of exactly three straight line segments called **sides** that connect three non-collinear points called **vertices**. The three sides form three interior angles at the vertices.

### Key Vocabulary
- **Vertex (plural: vertices)**: A corner point where two sides meet
- **Side**: A line segment connecting two vertices
- **Interior angle**: An angle formed inside the triangle at a vertex
- **Exterior angle**: An angle formed outside the triangle when one side is extended
- **Legs**: In an isosceles or right triangle, specific sides with special names
- **Base**: In an isosceles triangle, the side that is different from the other two equal sides

### Core Concept: Why Three Sides?
The number three is special in geometry. With three line segments, you create the simplest polygon that has an **interior**—a defined enclosed space. Two line segments can't enclose space; four or more create more complex shapes. Triangles are the building blocks of all geometry.

**Important**: The three vertices cannot be collinear (on the same line). If they are, you don't have a triangle—just a line segment.

---

## <a name="classification"></a>Triangle Classification

Triangles are classified two ways: **by their sides** and **by their angles**.

### Classification by Sides (Comparing the Three Side Lengths)

#### Scalene Triangle
- **Definition**: All three sides have different lengths
- **Visual cue**: Looks "lopsided" or asymmetrical
- **Angles**: All three angles are different sizes
- **Example**: Sides of 3 units, 4 units, and 5 units

#### Isosceles Triangle
- **Definition**: Exactly two sides have equal length
- **Equal sides**: Called the **legs**
- **Third side**: Called the **base**
- **Angles**: Two of the angles are equal (the angles opposite the equal sides—these are called **base angles**)
- **Example**: Sides of 5 units, 5 units, and 7 units
- **Key insight**: In an isosceles triangle, the two base angles are always congruent (this is the **Isosceles Triangle Theorem**)

#### Equilateral Triangle
- **Definition**: All three sides have equal length
- **Angles**: All three angles are equal (each is always 60°)
- **Special property**: An equilateral triangle is also isosceles (with each pair of sides being "legs")
- **Example**: Sides of 5 units, 5 units, and 5 units
- **Symmetry**: Perfectly symmetrical

### Classification by Angles (Comparing the Three Interior Angles)

#### Acute Triangle
- **Definition**: All three interior angles are less than 90°
- **Angle measure examples**: 50°, 60°, 70°
- **Visual**: Looks "pointy" with no right angle
- **Does NOT mean**: Equilateral (acute triangles can be scalene or isosceles)

#### Right Triangle
- **Definition**: Exactly one interior angle equals exactly 90°
- **Special sides**: The two sides forming the right angle are called **legs**; the longest side opposite the right angle is the **hypotenuse**
- **Key symbol**: A small square in the corner shows the right angle
- **Other angles**: The other two angles must be acute (sum to 90°)
- **Example**: Angles of 90°, 60°, 30°
- **Pythagorean relationship**: If legs are *a* and *b*, hypotenuse is *c*, then a² + b² = c²

#### Obtuse Triangle
- **Definition**: Exactly one interior angle is greater than 90° (obtuse)
- **Angle measure examples**: 100°, 40°, 40°
- **Key constraint**: Only ONE angle can be obtuse (the other two must be acute)
- **Why?**: If two angles were obtuse, their sum would exceed 180°, impossible in a triangle

#### Equiangular Triangle
- **Definition**: All three interior angles are equal
- **Angle measure**: Each angle equals 60°
- **Relationship**: An equiangular triangle is always equilateral
- **Converse**: An equilateral triangle is always equiangular

### Venn Diagram Relationships
```
Scalene:     Isosceles:        Equilateral:
  Acute        Acute             60°-60°-60°
  Right        Right             (also isosceles
  Obtuse       Obtuse            & acute)

(Each category on the left is independent
from those on the bottom—a triangle can
be both "acute" AND "isosceles")
```

---

## <a name="angle-sum"></a>Triangle Angle Sum Theorem

### The Theorem
**The sum of the three interior angles of any triangle is 180°.**

In symbols: If a triangle has angles A, B, and C, then:
$$A + B + C = 180°$$

### Why This Is True: An Intuitive Proof

Imagine a triangle ABC. If you walk around the triangle, you turn through the exterior angles at each vertex. When you complete the circuit, you've made one full rotation = 360°.

The exterior angles at each vertex are supplementary to the interior angles (they form a straight line). If the interior angles sum to something other than 180°, then the exterior angles wouldn't sum to 360°.

**More rigorous proof** (using parallel lines):
1. Draw triangle ABC
2. Extend side BC to a point D
3. Through vertex A, draw a line parallel to BC
4. The angle formed at A (between line AC and the parallel line) equals angle C (alternate interior angles)
5. The angle formed at A (between line AB and the parallel line) equals angle B (alternate interior angles)
6. These two angles plus angle A form a straight line = 180°
7. Therefore: A + B + C = 180°

### Worked Examples

**Example 1: Find the missing angle**
A triangle has angles of 45° and 65°. Find the third angle.

*Solution:*
$$A + B + C = 180°$$
$$45° + 65° + C = 180°$$
$$110° + C = 180°$$
$$C = 70°$$

**Example 2: Angles in terms of a variable**
A triangle has angles measuring x°, 2x°, and 3x°. Find each angle.

*Solution:*
$$x + 2x + 3x = 180°$$
$$6x = 180°$$
$$x = 30°$$

The three angles are:
- First angle: x = 30°
- Second angle: 2x = 60°
- Third angle: 3x = 90°

(This is a right triangle!)

**Example 3: Equilateral triangle check**
Prove that each angle in an equilateral triangle measures 60°.

*Solution:*
In an equilateral triangle, all three sides are equal. Since equal sides correspond to equal angles, all three angles are equal.

Let each angle = x.
$$x + x + x = 180°$$
$$3x = 180°$$
$$x = 60°$$

### Common Mistakes
- **Mistake 1**: Forgetting the angles must sum to exactly 180°, not 360° (which is the exterior angle sum)
- **Mistake 2**: Using this theorem on quadrilaterals (which sum to 360°) or other polygons
- **Mistake 3**: Assuming that if you know two angles, they must add to less than 180° (they must!)

### Exam Tips
- Always check: do your three angles sum to 180°? If not, you made an error.
- If you find an angle greater than 180° or negative, you've made a mistake—recheck.
- This theorem is the foundation for almost all angle work in triangles.

---

## <a name="exterior-angle"></a>Exterior Angle Theorem

### The Theorem
**An exterior angle of a triangle equals the sum of the two non-adjacent (remote) interior angles.**

In symbols: If exterior angle E is formed at vertex B, then:
$$E = A + C$$
(where A and C are the two angles not at B)

### Vocabulary
- **Exterior angle**: Formed when a side of a triangle is extended beyond a vertex
- **Remote interior angles** (or **non-adjacent interior angles**): The two interior angles not at the vertex where the exterior angle is formed
- **Adjacent interior angle**: The interior angle at the same vertex as the exterior angle

### Visual Understanding
```
Triangle ABC with side BC extended to point D:

        A
       /|
      / |
     /  |
    B---C---D

Exterior angle ACD is formed at C (by extending BC).
Remote interior angles are A and B.
Adjacent interior angle is ACB.

Exterior angle ACD = angle A + angle B
```

### Why This Works
1. The exterior angle ACD and the interior angle ACB form a linear pair (supplementary)
2. So: exterior angle + interior angle ACB = 180°
3. But we know: angle A + angle B + angle ACB = 180° (angle sum theorem)
4. Therefore: exterior angle = angle A + angle B

### Worked Examples

**Example 1: Finding angles using exterior angle theorem**
An exterior angle of a triangle measures 110°. One of the remote interior angles measures 35°. Find the other remote interior angle.

*Solution:*
$$\text{Exterior angle} = \text{Angle 1} + \text{Angle 2}$$
$$110° = 35° + \text{Angle 2}$$
$$\text{Angle 2} = 75°$$

**Example 2: Using algebra with exterior angles**
A triangle has an exterior angle measuring (3x + 20)°. The two remote interior angles measure x° and (2x)°. Find x and the exterior angle.

*Solution:*
$$3x + 20 = x + 2x$$
$$3x + 20 = 3x$$
$$20 = 0$$

Wait—this is impossible! Let me reconsider the problem setup...

Actually, if the problem is stated correctly:
$$3x + 20 = x + 2x$$

This has no solution, meaning the angle measures given are inconsistent. However, let's solve a valid version:

Exterior angle = (3x + 20)°, remote interior angles = x° and (2x - 10)°

$$3x + 20 = x + (2x - 10)$$
$$3x + 20 = 3x - 10$$
$$20 = -10$$

Still no solution. Let me use a realistic example:

Exterior angle = (5x)°, remote interior angles = (2x - 5)° and (3x + 10)°

$$5x = (2x - 5) + (3x + 10)$$
$$5x = 5x + 5$$
$$0 = 5$$

Let me just use straightforward numbers:

Exterior angle = (5x)°, remote interior angles = (x + 10)° and (2x + 20)°

$$5x = (x + 10) + (2x + 20)$$
$$5x = 3x + 30$$
$$2x = 30$$
$$x = 15°$$

The exterior angle is 5(15) = 75°
The remote interior angles are 15 + 10 = 25° and 2(15) + 20 = 50°
Check: 25 + 50 = 75° ✓

**Example 3: Real-world scenario**
In triangle ABC, angle B = 40°, angle C = 60°. A line extends BC to point D. Find the exterior angle ACD.

*Solution:*
$$\text{Exterior angle ACD} = \text{Angle A} + \text{Angle B}$$

First, find angle A:
$$A + B + C = 180°$$
$$A + 40° + 60° = 180°$$
$$A = 80°$$

Then:
$$\text{Exterior angle} = 80° + 40° = 120°$$

Or, using the exterior angle theorem directly:
$$\text{Exterior angle ACD} = 180° - 60° = 120°$$
(since it's supplementary to the adjacent interior angle)

### Common Mistakes
- **Mistake 1**: Using the adjacent interior angle instead of the remote interior angles
- **Mistake 2**: Confusing which angles to add
- **Mistake 3**: Forgetting that an exterior angle must be greater than either remote interior angle

### Exam Tips
- Always identify which two interior angles are remote from the exterior angle
- The exterior angle is always larger than any of the remote interior angles
- This theorem is great for finding missing angles quickly

---

## <a name="triangle-inequality"></a>Triangle Inequality Theorem

### The Theorem
**The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.**

In symbols: For a triangle with sides a, b, and c:
- a + b > c
- a + c > b
- b + c > a

**Equivalently**: For any triangle, each side must be shorter than the sum of the other two sides.

### Why This Is True (Intuitive Understanding)
Imagine you're trying to form a triangle with three sticks. If two sticks together aren't long enough to reach from one endpoint to the other when you try to close the triangle, you can't form a triangle—the "triangle" would collapse into a line segment (degenerate).

### Worked Examples

**Example 1: Can these sides form a triangle?**
Can sides of length 3, 4, and 5 form a triangle?

*Solution:*
Check all three conditions:
- 3 + 4 = 7 > 5 ✓
- 3 + 5 = 8 > 4 ✓
- 4 + 5 = 9 > 3 ✓

Yes, these form a triangle. (This is the famous 3-4-5 right triangle!)

**Example 2: Can these sides form a triangle?**
Can sides of length 2, 3, and 6 form a triangle?

*Solution:*
Check all three conditions:
- 2 + 3 = 5, and 5 > 6? NO ✗

Since 2 + 3 is not greater than 6, these cannot form a triangle. The two shorter sides together aren't long enough to span the longest side.

**Example 3: Finding a range of possible side lengths**
Two sides of a triangle are 5 cm and 8 cm. What is the range of possible lengths for the third side?

*Solution:*
Let the third side = x

Using the triangle inequality:
1. 5 + 8 > x  →  13 > x  →  x < 13
2. 5 + x > 8  →  x > 3
3. 8 + x > 5  →  x > -3 (automatically true if x > 3)

Combining: 3 < x < 13

The third side must be longer than 3 cm and shorter than 13 cm.

*Alternative approach*:
The third side must be greater than |8 - 5| = 3 and less than 8 + 5 = 13.
So: 3 < x < 13

**Example 4: Determining which measurement is longest**
A triangle has sides 7, 10, and 12. Which side is opposite the largest angle?

*Solution:*
In any triangle, the longest side is opposite the largest angle.
The longest side is 12, so the largest angle is opposite this side.

### Common Mistakes
- **Mistake 1**: Using ≥ instead of > (equality means degenerate, not a real triangle)
- **Mistake 2**: Forgetting to check all three inequalities
- **Mistake 3**: Forgetting that the sum of two sides must be greater than the third (not equal)

### Exam Tips
- Quick check: Is the longest side shorter than the sum of the other two? If yes, it's a triangle.
- For range problems, remember: third side must be greater than (difference of other two) and less than (sum of other two)

---

## <a name="isosceles-triangle"></a>Isosceles Triangle Theorem

### The Theorem
**If two sides of a triangle are congruent, then the angles opposite those sides are congruent.**

In symbols: In triangle ABC, if AB ≅ AC, then ∠B ≅ ∠C

These congruent angles are called the **base angles** (they're at the base of the isosceles triangle).

### The Converse (Also True!)
**If two angles of a triangle are congruent, then the sides opposite those angles are congruent.**

In symbols: In triangle ABC, if ∠B ≅ ∠C, then AB ≅ AC

### Why This Is True
The proof uses the reflection property of isosceles triangles. If you fold an isosceles triangle along its axis of symmetry (the line from the apex to the midpoint of the base), the two halves match perfectly. This symmetry means the base angles must be congruent.

**More rigorous proof**:
1. Draw triangle ABC with AB ≅ AC
2. Draw the angle bisector from A to side BC, meeting BC at point D
3. Triangle ABD ≅ triangle ACD (by SAS: AD ≅ AD, ∠BAD ≅ ∠CAD, AB ≅ AC)
4. Therefore ∠B ≅ ∠C (CPCTC)

### Key Properties of Isosceles Triangles
1. **Altitude = Median = Angle Bisector**: From the apex (vertex between the two equal sides) to the base, these three are the same line segment
2. **Symmetry**: The triangle is symmetric about this special line
3. **Perpendicular bisector**: This line is the perpendicular bisector of the base

### Worked Examples

**Example 1: Finding base angles**
An isosceles triangle has a vertex angle (the angle between the two equal sides) of 40°. Find the two base angles.

*Solution:*
Let each base angle = x

$$\text{Vertex angle} + \text{Base angle} + \text{Base angle} = 180°$$
$$40° + x + x = 180°$$
$$40° + 2x = 180°$$
$$2x = 140°$$
$$x = 70°$$

Each base angle measures 70°.

**Example 2: Finding the vertex angle**
An isosceles triangle has base angles of 55° each. Find the vertex angle.

*Solution:*
$$\text{Vertex angle} + 55° + 55° = 180°$$
$$\text{Vertex angle} = 180° - 110° = 70°$$

**Example 3: Using algebra with congruent sides**
An isosceles triangle has two sides of length (2x + 5) cm and a base of length (4x - 3) cm. Another isosceles triangle has sides of length (x + 8) cm and base of length (2x - 1) cm.

If the two triangles are congruent (exactly the same shape and size), find x and the side lengths.

*Solution:*
For the triangles to be congruent, corresponding sides must be equal.

Assume the legs match legs and base matches base:
$$2x + 5 = x + 8$$
$$x = 3$$

Check with the bases:
$$4x - 3 = 2x - 1$$
$$2x = 2$$
$$x = 1$$

These don't match, so this assumption is wrong.

Try: legs of first = base of second, base of first = legs of second
$$2x + 5 = 2x - 1$$

This gives -5 = -1, impossible.

Actually, if the problem means the two isosceles triangles are similar (same shape, different size), we'd need more information. For congruence with the given information, let's assume it means:

Both triangles are isosceles with the same apex angle. If the legs of triangle 1 are 2x + 5 and the legs of triangle 2 are x + 8:

$$2x + 5 = x + 8$$
$$x = 3$$

So triangle 1 has legs of 2(3) + 5 = 11 cm and base of 4(3) - 3 = 9 cm.

**Example 4: Using the converse theorem**
In triangle ABC, ∠A = 50°, ∠B = 65°, ∠C = 65°. Which sides are congruent?

*Solution:*
Since ∠B ≅ ∠C (both 65°), by the converse of the isosceles triangle theorem:
$$AC ≅ AB$$

(The sides opposite equal angles are congruent.)

The triangle is isosceles with legs AB and AC, and base BC.

### Common Mistakes
- **Mistake 1**: Confusing which sides are congruent with which angles are congruent
- **Mistake 2**: Assuming the vertex angle and a base angle are equal
- **Mistake 3**: Forgetting the converse—that equal angles also mean equal sides

### Exam Tips
- Mark equal sides with the same tick marks; mark equal angles with the same arc marks
- Base angles are always the two angles at the "bottom" of the isosceles triangle
- In an equilateral triangle, all three angles equal 60° and all three sides are congruent

---

## <a name="congruence-theorems"></a>Triangle Congruence: The Five Theorems

### Overview
Two triangles are **congruent** if they have the same size and shape. This means all corresponding sides and angles are equal.

**Question**: Do we need to show all 6 things (three sides + three angles) are equal? No! We can use shortcuts.

### The Five Congruence Theorems

#### 1. SSS (Side-Side-Side) Theorem
**If three sides of one triangle are congruent to three sides of another triangle, then the triangles are congruent.**

*When to use*: You know three side lengths of each triangle

*Visual*:
```
Triangle 1:     Triangle 2:
Sides: 3, 4, 5  Sides: 3, 4, 5
≅ SSS           ✓ They're congruent!
```

*Why this works*: There's only one way to arrange three sticks of fixed lengths (up to reflection). The shape is determined by the side lengths alone.

*Worked Example*:
Triangle ABC: AB = 5, BC = 6, AC = 7
Triangle DEF: DE = 5, EF = 6, DF = 7

Are they congruent?
Yes, by SSS, with correspondence A↔D, B↔E, C↔F.

#### 2. SAS (Side-Angle-Side) Theorem
**If two sides and the included angle of one triangle are congruent to two sides and the included angle of another triangle, then the triangles are congruent.**

**Key term**: **Included angle** = the angle between the two sides

*When to use*: You know two side lengths and the angle between them

*Visual*:
```
Triangle 1:         Triangle 2:
        A                   D
       /|                  /|
    c / | b            f  / | e
     /  |                /  |
    /   |               /   |
   B----C              E----F
   Side a, angle at C   Side d, angle at F

If: a = d, b = e, ∠C = ∠F, then Triangle ABC ≅ Triangle DEF (SAS)
```

*Why this works*: Once you place two sides at a known angle, you've determined the position of the third vertex—no other point could work.

*Worked Example*:
Triangle ABC: AB = 5, ∠B = 60°, BC = 7
Triangle DEF: DE = 5, ∠E = 60°, EF = 7

Are they congruent?
Yes, by SAS, with the correspondence A↔D, B↔E, C↔F. (The angle at B and E is the included angle between the sides.)

#### 3. ASA (Angle-Side-Angle) Theorem
**If two angles and the included side of one triangle are congruent to two angles and the included side of another triangle, then the triangles are congruent.**

**Key term**: **Included side** = the side between the two angles

*When to use*: You know two angles and the side between them

*Visual*:
```
      A                 D
     /|                /|
    / |               / |
   /  |              /  |
  B---C             E---F

If: ∠B = ∠E, BC = EF, ∠C = ∠F, then triangles are congruent (ASA)
(BC and EF are the included sides)
```

*Why this works*: Two angles determine the third angle (by angle sum = 180°). Once you know all three angles, you just need one side to scale the triangle to the right size. The included side acts as that scale.

*Worked Example*:
Triangle ABC: ∠A = 50°, AB = 8, ∠B = 60°
Triangle DEF: ∠D = 50°, DE = 8, ∠E = 60°

Are they congruent?
Yes, by ASA, with the correspondence A↔D, B↔E, C↔F. (AB and DE are the included sides between the angles.)

#### 4. AAS (Angle-Angle-Side) Theorem
**If two angles and a non-included side of one triangle are congruent to two angles and a non-included side of another triangle, then the triangles are congruent.**

**Key term**: **Non-included side** = a side that is NOT between the two angles

*When to use*: You know two angles and a side that's NOT between them

*Visual*:
```
      A                 D
     /|                /|
    / |               / |
   /  |              /  |
  B---C             E---F

If: ∠A = ∠D, ∠B = ∠E, BC = EF, then triangles are congruent (AAS)
(BC and EF are non-included—they're not between the two angles)
```

*Why this works*: If two angles are known, the third angle is determined. Now you have all three angles, making the triangles similar. The non-included side then determines the scale—one side is enough to fix the size.

*Key difference from ASA*: In AAS, the side is NOT between the angles. In ASA, it IS between them.

*Worked Example*:
Triangle ABC: ∠A = 50°, ∠B = 60°, BC = 8
Triangle DEF: ∠D = 50°, ∠E = 60°, EF = 8

Are they congruent?
Yes, by AAS, with the correspondence A↔D, B↔E, C↔F. (BC and EF are not between the two angles we know.)

#### 5. HL (Hypotenuse-Leg) Theorem
**If the hypotenuse and a leg of a right triangle are congruent to the hypotenuse and a leg of another right triangle, then the triangles are congruent.**

**Note**: This only works for RIGHT triangles!

*When to use*: Both triangles have a right angle, and you know the hypotenuse and one leg

*Visual*:
```
Triangle ABC (right angle at B):
    A
    |\
    | \
  a |  \ c (hypotenuse)
    |   \
    |____|
    B    C
      b

Triangle DEF (right angle at E):
    D
    |\
    | \
  d |  \ f (hypotenuse)
    |   \
    |____|
    E    F
      e

If: Right angles present, c = f (hypotenuse), and a = d (one leg), then triangles are congruent
```

*Why this works*: In a right triangle, if you know the hypotenuse and one leg, you can find the other leg using the Pythagorean theorem. This determines the third side, making the triangles congruent by SSS.

*Worked Example*:
Right triangle ABC (right angle at B): AB = 3, AC = 5 (hypotenuse)
Right triangle DEF (right angle at E): DE = 3, DF = 5 (hypotenuse)

Are they congruent?
Yes, by HL, with correspondence A↔D, B↔E, C↔F.

### Summary Table: Which Theorem When?

| Theorem | What You Know | When to Use | Note |
|---------|---------------|------------|------|
| SSS | 3 sides | All three side lengths | Most general |
| SAS | 2 sides + included angle | Two sides with angle between | Angle must be included |
| ASA | 2 angles + included side | Two angles with side between | Side must be included |
| AAS | 2 angles + non-included side | Two angles with side not between | Side can be anywhere |
| HL | Hypotenuse + leg (right triangles only) | Right triangles with hyp & one leg | Only for right triangles |

### Distinguishing Between Theorems

**ASA vs. AAS**:
- Both need two angles and one side
- ASA: the side is BETWEEN the angles
- AAS: the side is NOT between the angles

**SAS vs. SSS**:
- SAS: 2 sides and the angle between them
- SSS: 3 sides (no angles needed)

**HL vs. everything else**:
- HL is ONLY for right triangles
- All others work for any triangle

### Worked Example: Choosing the Right Theorem

**Example 1**: Two sides of one triangle equal two sides of another, and the included angles are equal. Which theorem?
*Answer*: SAS

**Example 2**: All three sides of one triangle equal all three sides of another. Which theorem?
*Answer*: SSS

**Example 3**: Two angles and the side opposite one of them are equal in two triangles. Which theorem?
*Answer*: AAS

**Example 4**: A right triangle has a right angle, hypotenuse 10, and one leg 6. Another right triangle has a right angle, hypotenuse 10, and one leg 6. Which theorem?
*Answer*: HL

**Example 5**: ∠A = ∠D, AB = DE, ∠B = ∠E. Which theorem?
*Answer*: ASA (the side AB/DE is included between the two angles)

---

## <a name="ssa-fails"></a>Why SSA Doesn't Work: The Ambiguous Case

### The Problem
SSA does NOT guarantee triangle congruence. Given two sides and an angle that's NOT between them (an angle opposite one of the sides), there can be zero, one, or two different triangles.

### Why This Happens

**Visual explanation**:
```
Suppose you know:
- Side AB = 5
- Side BC = 4
- Angle A = 40°

You place point B at the origin, side AB of length 5 at an angle.
Now you need to place C such that BC = 4.

C lies on a circle of radius 4 centered at B.
But depending on where A is, this circle might:
1. Not reach side AB at all (0 triangles)
2. Touch it in exactly one spot (1 triangle)
3. Cross it in two spots (2 triangles) ← AMBIGUOUS!
```

### The Ambiguous Case (SSA): Two Possible Triangles

**Setup**: You know sides a, b and angle A (opposite side a), where a < b and angle A is acute.

**Three outcomes**:
1. **No triangle**: If a < b·sin(A), no triangle exists
2. **One right triangle**: If a = b·sin(A), exactly one right triangle exists
3. **One acute triangle**: If b·sin(A) < a < b, typically one triangle (unless in special cases)
4. **Two triangles**: If b·sin(A) < a < b and angle A is acute, two triangles might exist

### Worked Example: The Ambiguous Case

**Example: Two Possible Triangles**
Triangle ABC: AB = 8, BC = 5, ∠A = 30°

Can we determine triangle ABC uniquely?

*Solution*:
We have two sides and an angle, but the angle is not between the sides (it's opposite side BC).

Check: Is 5 < 8·sin(30°)?
sin(30°) = 0.5, so 8·sin(30°) = 4
Is 5 < 4? No.

Check: Is 5 < 8?
Yes.

This is the ambiguous case. There are potentially two triangles satisfying these conditions:
- One with angle B acute
- One with angle B obtuse

Both satisfy: AB = 8, BC = 5, ∠A = 30°

**This is why SSA is not a congruence theorem.**

### How to Avoid the Ambiguity
- Use ASA or AAS instead (which specify which angles are congruent)
- Use HL for right triangles (which specifies the hypotenuse)
- Use SSS or SAS (which don't have this problem)

### Exam Tips
- When you have two sides and an angle, CHECK whether the angle is included
- If yes: use SAS
- If no: use AAS (if you also know another angle) or recognize SSA (which doesn't work)
- SSA problems on exams are often about recognizing that congruence is NOT guaranteed

---

## <a name="cpctc"></a>CPCTC: Corresponding Parts of Congruent Triangles are Congruent

### The Principle
**If two triangles are congruent, then all of their corresponding parts (sides and angles) are congruent.**

CPCTC is the logical conclusion after you've proved two triangles congruent. You've already established the triangles are congruent using one of the five theorems. Now you can conclude that any other parts also match.

### Why This Matters
CPCTC is how you extract information from congruence. It's not for proving triangles congruent—it's for using congruence to prove other things.

### Key Principle: Establishing Correspondence
When triangles are congruent, the order of vertices matters.

If triangle ABC ≅ triangle DEF, then:
- A corresponds to D
- B corresponds to E
- C corresponds to F

And therefore:
- AB ≅ DE
- BC ≅ EF
- AC ≅ DF
- ∠A ≅ ∠D
- ∠B ≅ ∠E
- ∠C ≅ ∠F

### Worked Examples

**Example 1: Proving segments are congruent**

Given: Triangle ABC ≅ Triangle DEF
Prove: AB ≅ DE

*Proof*:
Triangle ABC ≅ Triangle DEF (given)
Therefore, AB ≅ DE (CPCTC)

*Note*: This is simple because congruence is given. The power of CPCTC is using it after you've worked to establish congruence.

**Example 2: Two triangles sharing a side**

Given: Triangle ABC and triangle ABD
- AC ≅ AD
- BC ≅ BD
- Side AB is shared

Prove: ∠CAB ≅ ∠DAB

*Proof*:
1. AC ≅ AD (given)
2. BC ≅ BD (given)
3. AB ≅ AB (reflexive property)
4. Triangle ABC ≅ Triangle ABD (SSS)
5. ∠CAB ≅ ∠DAB (CPCTC)

**Example 3: Using CPCTC to prove angle relationships**

Given: Isosceles triangle ABC with AB ≅ AC
- D is the midpoint of BC
- Draw AD

Prove: ∠ADB ≅ ∠ADC (These should be right angles!)

*Proof*:
1. AB ≅ AC (given, isosceles triangle)
2. BD ≅ DC (D is midpoint of BC)
3. AD ≅ AD (reflexive property)
4. Triangle ABD ≅ Triangle ACD (SSS)
5. ∠ADB ≅ ∠ADC (CPCTC)
6. ∠ADB + ∠ADC = 180° (linear pair)
7. 2∠ADB = 180° (substitution, since angles are congruent)
8. ∠ADB = 90°, ∠ADC = 90° (division)

So AD ⊥ BC!

### Common Patterns Using CPCTC

1. **Proving segments congruent**: Show triangle congruence, then CPCTC gives segment congruence
2. **Proving angles congruent**: Show triangle congruence, then CPCTC gives angle congruence
3. **Proving perpendicularity**: Use CPCTC to show angles are right angles
4. **Proving parallel lines**: Use CPCTC to show corresponding angles are equal (then parallel lines follow)

### Exam Tips
- CPCTC always comes AFTER establishing triangle congruence
- List the congruence statement first: "Triangle ___ ≅ Triangle ___"
- Then write: "(Property name), therefore ___" (listing the congruent parts)
- Pay attention to the order of vertices—correspondence matters
- CPCTC is about extracting information, not establishing it

---

## <a name="two-column-proofs"></a>Two-Column Proofs Explained

### The Format
A two-column proof has two columns:
- **Left column (Statements)**: Facts you claim are true
- **Right column (Reasons)**: Why those facts are true

Each row makes a claim and justifies it.

### Structure
```
Given: [Information provided]
Prove: [What you need to show]

Statement                          | Reason
---|---
(Start with what's given)          | Given
(Build logical chain)              | (Cite theorem or property)
(More statements)                  | (More reasons)
(Conclude with what to prove)      | (Final justification)
```

### Key Reasons You'll Use

| Reason | What It Means |
|--------|---------------|
| Given | Information stated in the problem |
| Definition of [term] | Apply a definition (e.g., "definition of midpoint") |
| Reflexive Property | A segment or angle equals itself: AB ≅ AB |
| Symmetric Property | If A = B, then B = A |
| Transitive Property | If A = B and B = C, then A = C |
| Substitution Property | Replace one thing with an equal thing |
| Addition Property | If A = B, then A + C = B + C |
| Subtraction Property | If A = B, then A - C = B - C |
| Vertical Angles Theorem | Vertical angles are congruent |
| Linear Pair | Angles in a linear pair sum to 180° |
| Triangle Angle Sum | Angles in a triangle sum to 180° |
| Isosceles Triangle Theorem | Base angles of isosceles triangles are congruent |
| SSS, SAS, ASA, AAS, HL | Triangle congruence theorems |
| CPCTC | Corresponding parts of congruent triangles are congruent |

### Worked Examples

**Example 1: Basic two-column proof**

*Given*: Point M is the midpoint of segment AB
*Prove*: AM ≅ MB

```
Statement                          | Reason
---|---
M is the midpoint of AB           | Given
AM ≅ MB                           | Definition of midpoint
```

(Note: This is simple because the statement follows directly from the definition.)

**Example 2: Proving triangles congruent**

*Given*:
- Triangle ABC with AB ≅ AC
- D is the midpoint of BC

*Prove*: AD bisects ∠BAC (meaning ∠BAD ≅ ∠CAD)

```
Statement                          | Reason
---|---
AB ≅ AC                           | Given
D is the midpoint of BC           | Given
BD ≅ DC                           | Definition of midpoint
AD ≅ AD                           | Reflexive Property
Triangle ABD ≅ Triangle ACD      | SSS (AB ≅ AC, BD ≅ DC, AD ≅ AD)
∠BAD ≅ ∠CAD                       | CPCTC
AD bisects ∠BAC                   | Definition of angle bisector
```

**Example 3: More complex proof**

*Given*:
- Points A, B, C, D are positioned such that:
  - AB ≅ DC
  - AC ≅ DB
  - ∠ABC ≅ ∠DCB

*Prove*: Triangle ABC ≅ Triangle DCB

```
Statement                          | Reason
---|---
AB ≅ DC                           | Given
AC ≅ DB                           | Given
∠ABC ≅ ∠DCB                       | Given
BC ≅ BC                           | Reflexive Property
Triangle ABC ≅ Triangle DCB      | SAS (AB ≅ DC, ∠ABC ≅ ∠DCB, BC ≅ BC)
```

*Note*: BC is the included angle between AB and ∠ABC, and between DC and ∠DCB, so SAS applies.

**Example 4: Using Exterior Angle Theorem**

*Given*:
- Triangle ABC
- D is a point on the extension of BC (outside the triangle)
- ∠ACD is an exterior angle at C

*Prove*: ∠ACD = ∠A + ∠B

```
Statement                          | Reason
---|---
∠A + ∠B + ∠ACB = 180°           | Triangle Angle Sum Theorem
∠ACB + ∠ACD = 180°              | Linear Pair
∠ACD = 180° - ∠ACB              | Subtraction Property
∠A + ∠B = 180° - ∠ACB           | Subtraction Property (from first statement)
∠ACD = ∠A + ∠B                   | Transitive Property (or Substitution)
```

### Writing Tips

1. **Number every statement** so you can reference earlier ones
2. **Use standard notation**: ≅ for congruence, ∠ for angles, || for parallel
3. **Be specific**: Don't write "they're equal"—write what's equal and why
4. **Build logically**: Each statement should follow from previous ones
5. **Don't assume**: Everything must be justified
6. **State the theorem name clearly**: "By SSS" or "Triangle Angle Sum Theorem"
7. **Establish congruence first, then CPCTC**: In that order
8. **When using CPCTC**, write exactly which parts are congruent and cite CPCTC

### Common Mistakes

- **Mistake 1**: Using a theorem that requires something you haven't established (e.g., using SAS without establishing all three required parts)
- **Mistake 2**: Assuming facts that weren't given or derived
- **Mistake 3**: Poor statement of congruence (triangle ABC ≅ triangle DEF, not the other way around if correspondence matters)
- **Mistake 4**: Forgetting the "given" statement at the beginning
- **Mistake 5**: Using CPCTC before proving the triangles are congruent
- **Mistake 6**: Writing "obvious" steps without justification

### Exam Tips

- **Flow**: Your proof should tell a story—each step building naturally to the next
- **Clarity**: A person unfamiliar with the problem should follow your logic
- **Completeness**: Every statement needs a reason; don't skip steps
- **Practice**: Write many proofs to get comfortable with the format
- **Check your work**: Verify that your conclusion actually answers the "Prove" statement

---

## <a name="special-segments"></a>Special Segments in Triangles

Triangles have four important special segments. These create special points in the triangle.

### 1. Median

**Definition**: A segment from a vertex to the midpoint of the opposite side

**Notation**: If M is the midpoint of BC, then AM is a median

**How many**: Every triangle has three medians (one from each vertex)

**Key property**: The three medians meet at a single point called the **centroid**

**What it does**:
- Divides the opposite side into two equal segments
- Creates two smaller triangles of equal area (on either side of the median)

**Example**:
In triangle ABC, the median from A goes to the midpoint M of BC.
- BM = MC (M is a midpoint)
- Area of triangle ABM = Area of triangle AMC

### 2. Altitude

**Definition**: A segment from a vertex perpendicular to the opposite side (or the line containing the opposite side)

**Notation**: If H is the foot of the perpendicular from A to BC, then AH is an altitude

**Key property**: AH ⊥ BC

**Symbol**: A small square marks the right angle

**How many**: Every triangle has three altitudes (one from each vertex)

**Key property**: The three altitudes meet at a single point called the **orthocenter**

**Special note**: In an acute triangle, the orthocenter is inside the triangle. In a right triangle, it's at the right angle vertex. In an obtuse triangle, it's outside the triangle.

**What it measures**: The perpendicular distance from a vertex to the opposite side (this is the "height" used in area calculations)

**Example**:
In triangle ABC, the altitude from A goes perpendicular to side BC.
- If altitude meets BC at H, then ∠AHB = 90° and ∠AHC = 90°
- The area of triangle ABC = (1/2) × base × altitude = (1/2) × BC × AH

### 3. Perpendicular Bisector

**Definition**: A line that passes through the midpoint of a segment and is perpendicular to that segment

**Notation**: If M is the midpoint of BC and line ℓ passes through M perpendicular to BC, then ℓ is the perpendicular bisector of BC

**Applies to**: Sides of the triangle (it's not from a vertex, but from the midpoint of a side)

**How many**: Every triangle has three perpendicular bisectors (one for each side)

**Key property**: The three perpendicular bisectors meet at a single point called the **circumcenter**

**Important theorem**: Any point on the perpendicular bisector of a segment is equidistant from the endpoints of that segment.

**What it determines**: The circumcenter is the center of the circle that passes through all three vertices (the circumscribed circle)

**Example**:
In triangle ABC, the perpendicular bisector of side BC:
- Passes through the midpoint M of BC
- Is perpendicular to BC
- Every point P on this perpendicular bisector satisfies: PB = PC

### 4. Angle Bisector

**Definition**: A segment from a vertex that divides the angle into two congruent angles

**Notation**: If AD bisects ∠BAC, then ∠BAD ≅ ∠CAD

**How many**: Every triangle has three angle bisectors (one from each vertex)

**Key property**: The three angle bisectors meet at a single point called the **incenter**

**Important theorem**: Any point on the angle bisector of an angle is equidistant from the sides of the angle.

**What it determines**: The incenter is the center of the circle inscribed in the triangle (the circle touching all three sides)

**Example**:
In triangle ABC, if AD bisects ∠BAC, then:
- ∠BAD = ∠CAD = (∠BAC)/2
- Any point on AD is equidistant from sides AB and AC

### Summary: Four Special Segments

| Segment | From | To | Meets at | Point name |
|---------|------|----|---------|----|
| Median | Vertex | Midpoint of opposite side | Centroid | Center of mass |
| Altitude | Vertex | Opposite side (⊥) | Orthocenter | Varies by type |
| Perp. Bisector | Midpoint of side | (not from vertex) | Circumcenter | Circle center (around) |
| Angle Bisector | Vertex | Opposite side | Incenter | Circle center (inside) |

### Key Distinctions

**Medians vs. Altitudes**:
- Median: to the MIDPOINT (not necessarily perpendicular)
- Altitude: PERPENDICULAR (not necessarily to midpoint)
- In an isosceles triangle with AB ≅ AC, from A these are the same line!

**Perpendicular Bisectors vs. Altitudes**:
- Perpendicular bisector: a LINE (infinite)
- Altitude: a SEGMENT (finite, from vertex)
- For a side, they're perpendicular at the same point, but extend in different directions

**Angle Bisector vs. others**:
- Only the angle bisector divides an angle
- Others divide sides or relate to distances

---

## <a name="triangle-centers"></a>Four Centers of a Triangle

### 1. Centroid

**Definition**: The point where the three medians meet

**Location**: Always inside the triangle (for any triangle)

**Key property - The Centroid Theorem**: The centroid divides each median in a 2:1 ratio, with the longer segment toward the vertex.

If G is the centroid and AM is a median to point M:
$$AG = \frac{2}{3} AM \quad \text{and} \quad GM = \frac{1}{3} AM$$

**Physical meaning**: The centroid is the center of mass (or balance point) of the triangle. If you cut the triangle from cardboard and balance it on a pin, the pin should go through the centroid.

**Coordinate formula**: If a triangle has vertices at (x₁, y₁), (x₂, y₂), (x₃, y₃), then the centroid is at:
$$G = \left(\frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3}\right)$$

(Average of the coordinates)

**Example**:
Triangle with vertices A(0, 0), B(6, 0), C(3, 6)

Centroid:
$$G = \left(\frac{0 + 6 + 3}{3}, \frac{0 + 0 + 6}{3}\right) = (3, 2)$$

The median from A goes to midpoint of BC at (4.5, 3).
Length AG = √[(3-0)² + (2-0)²] = √13
Length of full median AM = √[(4.5-0)² + (3-0)²] = √(20.25 + 9) = √29.25 ≈ 5.41

Check 2:1 ratio: (2/3)√29.25 ≈ 3.61, while √13 ≈ 3.61 ✓

### 2. Orthocenter

**Definition**: The point where the three altitudes meet

**Location**:
- Inside the triangle if the triangle is acute
- At the right angle if the triangle is right
- Outside the triangle if the triangle is obtuse

**Why the location varies**: The altitudes from acute angles of an obtuse triangle must be extended beyond the sides to meet.

**Properties**:
- Reflected across a side, the orthocenter lies on the circumcircle
- For an acute triangle, the orthocenter is the "opposite" of the circumcenter

**Example**:
In a right triangle with the right angle at C:
- The altitude from C to the hypotenuse meets the hypotenuse at some point
- The altitudes from A and B are actually parts of the legs (since legs are perpendicular to each other)
- All three altitudes meet at C, the right angle vertex
- So the orthocenter is at C

### 3. Circumcenter

**Definition**: The point where the three perpendicular bisectors of the sides meet

**Key property**: The circumcenter is equidistant from all three vertices. It's the center of the circumscribed circle (the circle passing through all three vertices).

**Location**:
- Inside the triangle if the triangle is acute (and the circumcircle contains the whole triangle)
- On the hypotenuse if the triangle is right (the circle has the hypotenuse as a diameter)
- Outside the triangle if the triangle is obtuse

**Circumradius**: The distance from the circumcenter to any vertex, denoted R

**Formula for right triangle**: For a right triangle with hypotenuse c, the circumradius R = c/2

**Why?**: In a right triangle, the hypotenuse is a diameter of the circumcircle (by Thales' theorem), so the center is at the midpoint of the hypotenuse.

**Example**:
Right triangle with legs 3 and 4, hypotenuse 5.
The circumcenter is at the midpoint of the hypotenuse.
The circumradius is 5/2 = 2.5.
All three vertices are at distance 2.5 from the circumcenter.

### 4. Incenter

**Definition**: The point where the three angle bisectors meet

**Key property**: The incenter is equidistant from all three sides. It's the center of the inscribed circle (the circle touching all three sides).

**Location**: Always inside the triangle (for any triangle)

**Inradius**: The distance from the incenter to any side, denoted r

**Formula relating inradius to area**:
$$\text{Area} = r \times s$$

where r is the inradius and s is the semiperimeter (half the perimeter).

$$s = \frac{a + b + c}{2}$$

Therefore:
$$r = \frac{\text{Area}}{s}$$

**Example**:
Triangle with sides 3, 4, 5 (the 3-4-5 right triangle).

Area = (1/2) × 3 × 4 = 6

Perimeter = 3 + 4 + 5 = 12
Semiperimeter s = 6

Inradius r = Area / s = 6 / 6 = 1

The incircle has radius 1 and touches all three sides.

### Summary: The Four Centers

| Center | Made from | Equidistant from | Always inside? | Coordinate method |
|--------|-----------|------------------|---|---|
| Centroid | Medians | — | Yes | Average of vertices |
| Orthocenter | Altitudes | — | No (varies) | Intersection of altitudes |
| Circumcenter | Perp. bisectors | Vertices | No (varies) | Intersection of perp. bisectors |
| Incenter | Angle bisectors | Sides | Yes | Intersection of angle bisectors |

### Memorization Tip
- **Centroid**: "Center of MASS" → inside always
- **Circumcenter**: "CIRCUM" → around (circle through vertices)
- **Incenter**: "IN" → inside (circle inside triangle)
- **Orthocenter**: "ORTHO" → right angles (from altitudes)

---

## <a name="midsegment"></a>Midsegment Theorem

### Definition
A **midsegment** of a triangle is a segment connecting the midpoints of two sides.

### The Midsegment Theorem
**A midsegment of a triangle is parallel to the third side and has half its length.**

In symbols: If M and N are midpoints of sides AB and AC respectively, then:
- MN || BC (parallel)
- MN = (1/2)BC (half the length)

### Visual

```
        A
       /|\
      / | \
     /  |  \
    /M--+--N\
   /    |    \
  /     |     \
 B------+------C

M is midpoint of AB
N is midpoint of AC
MN is the midsegment

MN || BC and MN = BC/2
```

### Why This Works

**Proof sketch**:
1. Let M be the midpoint of AB and N be the midpoint of AC
2. Use coordinate geometry or similar triangles
3. Triangle AMN is similar to triangle ABC with a scale factor of 1/2
4. Corresponding sides of similar triangles are proportional: MN/BC = 1/2
5. Corresponding angles are equal: ∠AMN = ∠ABC (corresponding angles with parallel lines)
6. This means MN || BC

### Key Insight
A midsegment divides the triangle into:
- A smaller triangle (the top one with the midsegment) with area 1/4 of the original
- A trapezoid (the bottom part) with area 3/4 of the original

### Converse (Also True!)
**If a segment connects a midpoint of one side to a point on another side, and is parallel to the third side, then it bisects the other side.**

In other words: If M is the midpoint of AB, and MN || BC (where N is on AC), then N is the midpoint of AC.

### Worked Examples

**Example 1: Finding lengths**
Triangle ABC has sides AB = 10, AC = 8, BC = 12.
M and N are midpoints of AB and AC respectively.
Find the length of midsegment MN.

*Solution*:
By the midsegment theorem, MN = (1/2)BC = (1/2)(12) = 6

**Example 2: Finding the perimeter of a triangle formed by midsegments**
Triangle ABC has sides AB = 6, BC = 8, AC = 10.
M, N, P are midpoints of AB, BC, AC respectively.
Find the perimeter of triangle MNP (formed by the three midsegments).

*Solution*:
The three midsegments are:
- MN (connecting midpoints of AB and BC): parallel to AC, length = (1/2)(10) = 5
- NP (connecting midpoints of BC and AC): parallel to AB, length = (1/2)(6) = 3
- MP (connecting midpoints of AB and AC): parallel to BC, length = (1/2)(8) = 4

Perimeter of triangle MNP = 5 + 3 + 4 = 12

*Note*: This is exactly half the perimeter of ABC (which is 6 + 8 + 10 = 24)

**Example 3: Parallel lines**
In triangle ABC, M is the midpoint of AB and N is the midpoint of AC.
Prove that MN || BC.

*Proof*:
1. M is the midpoint of AB (given)
2. N is the midpoint of AC (given)
3. MN is a midsegment of triangle ABC (definition)
4. MN || BC (midsegment theorem)

**Example 4: Proving congruence using midsegments**
In triangle ABC, D and E are midpoints of AB and AC.
F and G are midpoints of AD and AE.
Prove that FG || DE.

*Proof*:
1. D and E are midpoints of AB and AC (given)
2. DE is a midsegment of triangle ABC (definition)
3. DE || BC and DE = (1/2)BC (midsegment theorem)
4. F and G are midpoints of AD and AE (given)
5. FG is a midsegment of triangle ADE (definition)
6. FG || DE and FG = (1/2)DE (midsegment theorem applied to triangle ADE)

Wait—this proves FG || DE, which checks out!

### Common Mistakes
- **Mistake 1**: Forgetting that BOTH points must be midpoints (if only one is, the segment isn't a midsegment)
- **Mistake 2**: Getting the length ratio wrong—it's 1/2, not 2/1
- **Mistake 3**: Forgetting the parallel part (both length AND parallel relationships matter)

### Exam Tips
- Midsegments are great for creating similar triangles with a known ratio
- They divide triangles into smaller regions with predictable area ratios
- Look for midpoint markings or statements like "M is the midpoint of AB"
- Midsegments are often used to prove lines are parallel without needing angle measures

---

## <a name="coordinate-proofs"></a>Coordinate Proofs

### What is a Coordinate Proof?
A **coordinate proof** places a triangle (or other figure) on a coordinate plane and uses algebra to prove geometric properties. Instead of geometric reasoning alone, you use:
- Distance formula
- Slope formula
- Midpoint formula
- Equations of lines

### Key Formulas

**Distance Formula**: The distance between points (x₁, y₁) and (x₂, y₂) is:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Slope Formula**: The slope of a line through (x₁, y₁) and (x₂, y₂) is:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

**Midpoint Formula**: The midpoint of a segment from (x₁, y₁) to (x₂, y₂) is:
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

**Parallel Lines**: Two lines with slopes m₁ and m₂ are parallel if m₁ = m₂

**Perpendicular Lines**: Two lines with slopes m₁ and m₂ are perpendicular if m₁ · m₂ = -1

### Strategy for Setting Up Coordinates

1. **Place one vertex at the origin**: (0, 0) simplifies calculations
2. **Align one side with an axis**: Makes coordinates simpler
3. **Use variables for unknown coordinates**: Allows general proofs that work for any triangle

**Common placement**:
- Right triangle: right angle at origin, legs on axes
- Isosceles triangle: base on x-axis, apex on y-axis above midpoint
- General triangle: one vertex at origin, one on positive x-axis, third in first quadrant

### Worked Examples

**Example 1: Proving a triangle is isosceles**

Set up triangle with vertices A(0, 0), B(4, 0), C(2, 3).

Prove triangle ABC is isosceles.

*Solution*:
Check the side lengths using the distance formula:

$$AB = \sqrt{(4-0)^2 + (0-0)^2} = \sqrt{16} = 4$$

$$AC = \sqrt{(2-0)^2 + (3-0)^2} = \sqrt{4 + 9} = \sqrt{13}$$

$$BC = \sqrt{(2-4)^2 + (3-0)^2} = \sqrt{4 + 9} = \sqrt{13}$$

Since AC = BC = √13, triangle ABC is isosceles (with AC and BC as the equal sides).

**Example 2: Proving a triangle is a right triangle**

Triangle with vertices A(0, 0), B(3, 0), C(0, 4).

Prove triangle ABC is a right triangle.

*Solution - Method 1: Using the Pythagorean theorem*
$$AB = \sqrt{(3-0)^2 + (0-0)^2} = 3$$
$$AC = \sqrt{(0-0)^2 + (4-0)^2} = 4$$
$$BC = \sqrt{(0-3)^2 + (4-0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

Check: 3² + 4² = 9 + 16 = 25 = 5² ✓

By the Pythagorean theorem (converse), triangle ABC is a right triangle.

*Method 2: Using slopes*
Slope of AB: m₁ = (0-0)/(3-0) = 0
Slope of AC: m₂ = (4-0)/(0-0) = undefined (vertical line)

Since one slope is 0 (horizontal) and one is undefined (vertical), the lines are perpendicular. Therefore, ∠BAC = 90°, and triangle ABC is a right triangle.

**Example 3: Proving the midsegment theorem**

General triangle with vertices A(0, 0), B(2a, 0), C(2b, 2c).

M and N are midpoints of AB and AC.

Prove MN || BC and MN = (1/2)BC.

*Solution*:
Midpoint M of AB:
$$M = \left(\frac{0 + 2a}{2}, \frac{0 + 0}{2}\right) = (a, 0)$$

Midpoint N of AC:
$$N = \left(\frac{0 + 2b}{2}, \frac{0 + 2c}{2}\right) = (b, c)$$

**Check parallel** (equal slopes):
Slope of MN: $m_1 = \frac{c - 0}{b - a} = \frac{c}{b - a}$

Slope of BC: $m_2 = \frac{2c - 0}{2b - 2a} = \frac{2c}{2(b - a)} = \frac{c}{b - a}$

Since m₁ = m₂, MN || BC ✓

**Check length**:
$$MN = \sqrt{(b - a)^2 + (c - 0)^2} = \sqrt{(b-a)^2 + c^2}$$

$$BC = \sqrt{(2b - 2a)^2 + (2c - 0)^2} = \sqrt{4(b-a)^2 + 4c^2}$$
$$= \sqrt{4[(b-a)^2 + c^2]} = 2\sqrt{(b-a)^2 + c^2}$$

So MN = BC/2 ✓

**Example 4: Proving a specific property with coordinates**

Triangle with vertices A(0, 0), B(6, 0), C(3, 4).

Let D be the midpoint of AB and E be the midpoint of AC.

Prove that the median from C to side AB has length equal to the distance from C to the midpoint D.

Wait, this doesn't make sense. Let me restate:

Prove that if M is the midpoint of AB, then the median CM divides the triangle into two triangles of equal area.

*Solution*:
Midpoint M of AB:
$$M = \left(\frac{0 + 6}{2}, \frac{0 + 0}{2}\right) = (3, 0)$$

Area of triangle ABC:
Using vertices A(0,0), B(6,0), C(3,4):
$$\text{Area} = \frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$$
$$= \frac{1}{2}|0(0-4) + 6(4-0) + 3(0-0)|$$
$$= \frac{1}{2}|0 + 24 + 0| = 12$$

Area of triangle ACM (with vertices A(0,0), C(3,4), M(3,0)):
$$\text{Area} = \frac{1}{2}|0(4-0) + 3(0-0) + 3(0-4)|$$
$$= \frac{1}{2}|0 + 0 - 12| = 6$$

Area of triangle BCM (with vertices B(6,0), C(3,4), M(3,0)):
$$\text{Area} = \frac{1}{2}|6(4-0) + 3(0-0) + 3(0-4)|$$
$$= \frac{1}{2}|24 + 0 - 12| = 6$$

Both areas are 6, which is half of 12. ✓

The median from C divides triangle ABC into two equal areas.

### Choosing Coordinates Wisely

**For an isosceles triangle**: Place the base on the x-axis centered at origin, apex above center
```
Example: A(-a, 0), B(a, 0), C(0, h)
```

**For a right triangle**: Right angle at origin, legs on axes
```
Example: A(0, 0), B(a, 0), C(0, b)
```

**For a general triangle**: One vertex at origin, one on positive x-axis
```
Example: A(0, 0), B(a, 0), C(b, c)
```

### Common Mistakes

- **Mistake 1**: Using specific numbers when a general proof is needed (use variables)
- **Mistake 2**: Not simplifying the distance formula correctly
- **Mistake 3**: Forgetting to use absolute value when finding area with coordinates
- **Mistake 4**: Calculating slope incorrectly (run over rise, not rise over run)
- **Mistake 5**: Not checking both conditions when needing parallel AND equal length

### Exam Tips

- Always show your algebra—don't skip steps in distance or slope calculations
- When placing coordinates, choose positions that minimize arithmetic
- For general proofs, use variables (a, b, c) not specific numbers
- Double-check the distance formula application—it's easy to make arithmetic errors
- When proving perpendicularity, verify that m₁ · m₂ = -1 exactly
- Area formula with coordinates: Area = (1/2)|x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|

---

## Quick Reference: Key Theorems Summary

### Angle Theorems
- **Triangle Angle Sum**: A + B + C = 180°
- **Exterior Angle Theorem**: Exterior angle = sum of two remote interior angles
- **Isosceles Triangle Theorem**: Equal sides ↔ Equal base angles

### Congruence Theorems (Five)
- **SSS**: Three sides equal
- **SAS**: Two sides + included angle equal
- **ASA**: Two angles + included side equal
- **AAS**: Two angles + non-included side equal
- **HL**: Hypotenuse + leg (right triangles only)

### Why NOT congruence
- **SSA/ASS**: Ambiguous case—doesn't guarantee congruence

### Using Congruence
- **CPCTC**: Corresponding Parts of Congruent Triangles are Congruent

### Special Segments
- **Median**: Vertex to midpoint of opposite side → meets at **centroid** (2:1 ratio)
- **Altitude**: Vertex perpendicular to opposite side → meets at **orthocenter**
- **Perpendicular Bisector**: Of a side → meets at **circumcenter** (circle through vertices)
- **Angle Bisector**: Bisects an angle → meets at **incenter** (circle inside triangle)

### Midsegment
- **Midsegment Theorem**: Connects midpoints, parallel to third side, half its length

### Coordinate Proofs Use
- **Distance Formula**: d = √[(x₂-x₁)² + (y₂-y₁)²]
- **Slope Formula**: m = (y₂-y₁)/(x₂-x₁)
- **Parallel lines**: Equal slopes (m₁ = m₂)
- **Perpendicular lines**: Negative reciprocal slopes (m₁ · m₂ = -1)
- **Midpoint Formula**: M = ((x₁+x₂)/2, (y₁+y₂)/2)

---

## Practice Problems (Answers Below)

### Section 1: Classification
1. A triangle has angles of 30°, 60°, and 90°. Classify by angle type.
2. A triangle has sides of 5, 5, and 7. Classify by side type.

### Section 2: Angle Sum
3. Find the third angle in a triangle with angles 45° and 67°.
4. In a triangle, one angle is 3x°, another is 5x°, and the third is 2x°. Find each angle.

### Section 3: Exterior Angles
5. A triangle has remote interior angles of 35° and 62°. Find the exterior angle.
6. An exterior angle is 120°. One remote interior angle is 45°. Find the other.

### Section 4: Triangle Inequality
7. Can sides 3, 4, and 8 form a triangle?
8. Two sides of a triangle are 6 and 9. Find the range for the third side.

### Section 5: Isosceles Triangles
9. An isosceles triangle has a vertex angle of 50°. Find the base angles.
10. An isosceles triangle has base angles of 72° each. Find the vertex angle.

### Section 6: Congruence
11. Given: Triangle ABC with AB = 5, BC = 6, AC = 7. Triangle DEF with DE = 5, EF = 6, DF = 7. Which theorem proves they're congruent?
12. Given: Triangle ABC with AB = 4, ∠B = 60°, BC = 5. Triangle DEF with DE = 4, ∠E = 60°, EF = 5. Which theorem?

### Section 7: Coordinate Proofs
13. Triangle with vertices A(0,0), B(6,0), C(3,4). Is it isosceles? Prove using distance formula.
14. Triangle with vertices A(0,0), B(5,0), C(0,12). Is it a right triangle? Prove using slopes or Pythagorean theorem.

---

## Answer Key

### Section 1: Classification
1. **Right triangle** (has a 90° angle)
2. **Isosceles triangle** (two sides equal)

### Section 2: Angle Sum
3. 180° - 45° - 67° = **68°**
4. x + 5x + 2x = 180° → 8x = 180° → x = 22.5°
   - First angle: 3(22.5) = **67.5°**
   - Second angle: 5(22.5) = **112.5°**
   - Third angle: 2(22.5) = **45°**

### Section 3: Exterior Angles
5. 35° + 62° = **97°**
6. 120° = 45° + other → other = **75°**

### Section 4: Triangle Inequality
7. Check: 3 + 4 = 7, and 7 > 8? **No**, these cannot form a triangle (two sides together aren't longer than third)
8. Third side must be > |9-6| = 3 and < 9+6 = 15. So: **3 < x < 15**

### Section 5: Isosceles Triangles
9. 50° + 2x = 180° → x = **65°** each
10. x + 72° + 72° = 180° → x = **36°**

### Section 6: Congruence
11. **SSS** (all three sides match)
12. **SAS** (two sides with the included angle match)

### Section 7: Coordinate Proofs
13. AB = 6, AC = √(9+16) = 5, BC = √(9+16) = 5. Since AC = BC, **yes, it's isosceles**.
14. AB = 5, AC = 12, BC = √(25+144) = √169 = 13. Check: 5² + 12² = 25 + 144 = 169 = 13². **Yes, it's right** (3-4-5 triangle scaled by 5/3... actually this is the 5-12-13 right triangle). Or check slopes: AB horizontal (m=0), AC vertical (m=undefined) → perpendicular → right angle at A.

---

## Final Tips for Success

1. **Draw pictures** for every geometry problem—even when it's not required
2. **Label everything**: sides with lengths, angles with measures, special points
3. **Mark congruent parts**: Use tick marks for equal sides, arc marks for equal angles
4. **Write complete proofs**: Every statement needs a reason
5. **Check your work**: Do angles sum to 180°? Do sides satisfy triangle inequality?
6. **Memorize the five congruence theorems**—they're the foundation of triangle geometry
7. **Understand CPCTC**: You use congruence to prove other things
8. **Practice two-column proofs**: They get easier with repetition
9. **Connect theorems**: See how they build on each other (e.g., angle sum → exterior angle)
10. **Use coordinate proofs when appropriate**: They're powerful tools for specific problems

---

**Good luck with Unit 3! Master triangles, and most of the rest of geometry becomes much easier.**
