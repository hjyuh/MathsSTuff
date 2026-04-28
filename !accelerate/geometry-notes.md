# Honors Geometry — Accelerated Notes
## Mahmoud | Sprint for Test-Out

---

## UNIT 1: Foundations — Proof Language

**What's new:** Not the math (you know slope, distance, midpoint). The PROOF FORMAT.

### Two-Column Proof Structure
| Statement | Reason |
|-----------|--------|
| AB ≅ CD | Given |
| BC ≅ BC | Reflexive Property |
| AB + BC = AC | Segment Addition Postulate |

Every claim needs a reason from: Given, Definition, Postulate, or Theorem.

### Key Vocabulary
- **Bisector** — cuts into two equal parts (segment bisector → midpoint, angle bisector → two equal angles)
- **Perpendicular bisector** — bisects AND is perpendicular. KEY THEOREM: every point on the perp bisector is equidistant from the segment's endpoints.
- **Constructions** — compass + straightedge only. Can construct: copy segment, copy angle, bisect both, perpendicular/parallel lines.

### Common Proof Reasons to Memorize
- Reflexive Property: AB ≅ AB (a thing equals itself)
- Symmetric Property: if AB ≅ CD then CD ≅ AB
- Transitive Property: if AB ≅ CD and CD ≅ EF then AB ≅ EF
- Segment Addition Postulate: if B is between A and C, then AB + BC = AC
- Angle Addition Postulate: if D is in the interior of ∠ABC, then ∠ABD + ∠DBC = ∠ABC
- Substitution Property: swap equal things

---

## UNIT 2: Transformations

### Rigid Motions (Isometries) — preserve distance and angles

**Translation:** (x, y) → (x + a, y + b)

**Reflection:**
- Across x-axis: (x, y) → (x, −y)
- Across y-axis: (x, y) → (−x, y)  
- Across y = x: (x, y) → (y, x)

**Rotation about origin:**
- 90° CCW: (x, y) → (−y, x)
- 180°: (x, y) → (−x, −y)
- 270° CCW / 90° CW: (x, y) → (y, −x)

**KEY IDEA:** If you can map figure A onto figure B using only rigid motions → they are CONGRUENT.

### Symmetry
- **Line symmetry:** figure maps onto itself across a reflection line
- **Rotational symmetry:** figure maps onto itself by rotation < 360°. Regular n-gon → every 360°/n

### Parallel Lines + Transversal — THE ANGLE RELATIONSHIPS

When a transversal crosses two parallel lines, 8 angles form. Memorize these:

| Relationship | Position | Result |
|-------------|----------|--------|
| Corresponding | Same position at each intersection | CONGRUENT |
| Alternate Interior | Opposite sides, between parallels | CONGRUENT |
| Alternate Exterior | Opposite sides, outside parallels | CONGRUENT |
| Co-Interior (Same-Side Interior) | Same side, between parallels | SUPPLEMENTARY (sum = 180°) |

**Goes both ways:** angles equal → lines parallel. Lines parallel → angles equal.

Also remember from intersecting lines (no parallel requirement):
- **Vertical angles** — across from each other at an intersection → always CONGRUENT
- **Linear pair** — adjacent angles on a straight line → always SUPPLEMENTARY (sum = 180°)

---

## UNIT 3: Triangles & Congruence

### Properties Within One Triangle

**Interior angles sum to 180°.**

**Exterior angle theorem:** An exterior angle of a triangle = sum of the two remote (non-adjacent) interior angles.

**Isosceles triangle theorem:** If two sides are congruent (equal tick marks), the base angles opposite them are congruent. Works in reverse too — equal base angles → equal sides.

**Midsegment theorem:** Connect the midpoints of two sides → that segment is:
1. PARALLEL to the third side
2. Exactly HALF the length of the third side

### Triangle Congruence Theorems (The Big Five)

| Theorem | What Matches | Notes |
|---------|-------------|-------|
| SSS | All 3 sides | |
| SAS | 2 sides + INCLUDED angle | Angle must be BETWEEN the two sides |
| ASA | 2 angles + INCLUDED side | Side must be BETWEEN the two angles |
| AAS | 2 angles + non-included side | |
| HL | Hypotenuse + Leg | RIGHT TRIANGLES ONLY |

**What does NOT work:** SSA (two sides + non-included angle). Ambiguous — can make two different triangles.

### How Congruence Proofs Work
1. You're given info about a figure
2. Identify two triangles within it
3. List pairs of congruent parts until you have one of the Big Five
4. Conclude: △ABC ≅ △DEF by [theorem]
5. **CPCTC** — Corresponding Parts of Congruent Triangles are Congruent
   - This is the PAYOFF. Prove triangles congruent → unlock any remaining part congruence.
