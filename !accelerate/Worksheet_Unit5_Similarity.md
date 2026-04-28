# Unit 5: Similarity (Honors Geometry)
## Layered Decomposition Protocol (LDP) Worksheet

---

## MODULE 1: MODEL EXAMPLES (Foundation Building)

### Problem 1.1: Determine Similarity & State Theorem
Triangle ABC has angles 45°, 65°, 70°. Triangle DEF has angles 45°, 65°, 70°.
Are the triangles similar? If so, which similarity theorem applies?

**Answer:** Similar; AA (Angle-Angle) Similarity
**Pattern observed:** When two angles match, the third must match too (angles in a triangle sum to 180°). AA guarantees similarity without checking sides.

---

### Problem 1.2: Find Scale Factor
Triangle ABC ~ Triangle DEF. Side AB = 6 cm, side DE = 9 cm.
What is the scale factor from ABC to DEF?

**Answer:** k = 9/6 = 1.5 (or 3/2)
**Pattern observed:** Scale factor = (side of second figure) / (corresponding side of first figure). If k > 1, the second figure is enlarged.

---

### Problem 1.3: Solve Proportion for Missing Side
Triangle PQR ~ Triangle XYZ. PQ = 8, QR = 12, XY = 10, YZ = ?

Set up the proportion: $\frac{PQ}{XY} = \frac{QR}{YZ}$

$\frac{8}{10} = \frac{12}{YZ}$

Cross-multiply: $8 \cdot YZ = 10 \cdot 12$

$YZ = \frac{120}{8} = 15$

**Pattern observed:** Corresponding sides are in the same ratio. Line up sides carefully: if PQ corresponds to XY, then QR corresponds to YZ.

---

### Problem 1.4: Apply Triangle Proportionality Theorem (Side-Splitter)
Triangle ABC has a line DE parallel to BC, where D is on AB and E is on AC.
If AD = 4, DB = 6, and AE = 5, find EC.

**Triangle Proportionality Theorem (Side-Splitter):**
If DE ∥ BC, then $\frac{AD}{DB} = \frac{AE}{EC}$

$\frac{4}{6} = \frac{5}{EC}$

Cross-multiply: $4 \cdot EC = 6 \cdot 5 = 30$

$EC = 7.5$

**Pattern observed:** A line parallel to one side of a triangle divides the other two sides proportionally. The ratio on one side equals the ratio on the other side.

---

### Problem 1.5: Find Geometric Mean
Find the geometric mean of 4 and 9.

**Geometric Mean Definition:** If $x$ is the geometric mean of $a$ and $b$, then $\frac{a}{x} = \frac{x}{b}$

$\frac{4}{x} = \frac{x}{9}$

$x^2 = 4 \cdot 9 = 36$

$x = 6$

**Pattern observed:** Geometric mean is the square root of the product. Alternatively: GM = $\sqrt{ab} = \sqrt{4 \cdot 9} = \sqrt{36} = 6$.

---

### Problem 1.6: Ratio of Perimeters
Triangle ABC ~ Triangle DEF with scale factor k = 2.
If the perimeter of ABC is 20 cm, what is the perimeter of DEF?

**Key Insight:** If linear scale factor = k, then perimeter ratio = k.

Perimeter of DEF = 2 × Perimeter of ABC = 2 × 20 = **40 cm**

**Pattern observed:** Perimeters scale by the same factor as side lengths. If k = 2 (sides are twice as long), then perimeter is also twice as long.

---

### Problem 1.7: Ratio of Areas
Triangle ABC ~ Triangle DEF with scale factor k = 3.
If the area of ABC is 25 cm², what is the area of DEF?

**Key Insight:** If linear scale factor = k, then area ratio = k².

Area of DEF = 3² × Area of ABC = 9 × 25 = **225 cm²**

**Pattern observed:** Areas scale by the square of the linear scale factor. Doubling side lengths quadruples area (k² = 2²). This is the most common error: students confuse k with k².

---

### Problem 1.8: Combine Scale Factor & Proportions
Rectangle ABCD has length 12 and width 8. Rectangle EFGH is similar with scale factor k = 0.5.
(a) Find the length and width of EFGH.
(b) Find the ratio of areas.

**(a)** Length of EFGH = 0.5 × 12 = 6
Width of EFGH = 0.5 × 8 = 4

**(b)** Area ratio = k² = 0.5² = 0.25. Area of EFGH is 1/4 the area of ABCD.

**Pattern observed:** Scale factors less than 1 indicate reduction. The area shrinks by k² = 0.25 (to 1/4 of original).

---

### Problem 1.9: Set Up Multiple Proportions
Quadrilateral ABCD ~ Quadrilateral PQRS.
AB = 5, BC = 7, CD = 6, PQ = 10, QR = 14, RS = ?

First, find the scale factor: k = 10/5 = 2

Using the scale factor:
CD corresponds to RS, so RS = 2 × 6 = **12**

Alternatively, set up a proportion:
$\frac{AB}{PQ} = \frac{CD}{RS}$

$\frac{5}{10} = \frac{6}{RS}$

$RS = 12$

**Pattern observed:** Once you identify the correspondence and find the scale factor, you can apply it consistently to all sides. Consistency is crucial.

---

### Problem 1.10: Multi-Step Model
Triangle XYZ has sides 6, 8, 10 (right triangle). Triangle PQR is similar with perimeter 36.
(a) Find the scale factor.
(b) Find all sides of triangle PQR.

**(a)** Perimeter of XYZ = 6 + 8 + 10 = 24
Scale factor k = 36 / 24 = 1.5

**(b)** Sides of PQR = 1.5 × (6, 8, 10) = **(9, 12, 15)**

Check: 9 + 12 + 15 = 36 ✓

**Pattern observed:** Perimeter ratio directly gives you the linear scale factor. Then multiply each side to find the new triangle's dimensions.

---

---

## MODULE 2: WEAK THEOREM LADDER (Building Reasoning)

### Level 1: Identify Similar Triangles by AA

**Problem 2.1:**
Triangle ABC and Triangle DEF both have a 50° angle. In ABC, angle B = 70°. In DEF, angle E = 70°.
Prove that ABC ~ DEF by AA. Which angles correspond?

**Solution:**
In ABC: angles are 50°, 70°, and (180° - 50° - 70° = 60°)
In DEF: angles are 50°, 70°, and (180° - 50° - 70° = 60°)

By AA: ABC ~ DEF (two pairs of angles are equal).

Corresponding angles:
- Angle A (50°) ↔ Angle D (50°)
- Angle B (70°) ↔ Angle E (70°)
- Angle C (60°) ↔ Angle F (60°)

**Trigger extraction:** Recognize angle equality → AA applies → state correspondence.

---

### Level 2: Solve for Missing Side Using Proportion

**Problem 2.2:**
Triangle JKL ~ Triangle MNO.
JK = 9, KL = 12, MN = 6, NO = ?

Find NO.

**Solution:**
Since JKL ~ MNO:
$\frac{JK}{MN} = \frac{KL}{NO}$

$\frac{9}{6} = \frac{12}{NO}$

Cross-multiply: $9 \cdot NO = 6 \cdot 12 = 72$

$NO = 8$

**Trigger extraction:** Set up proportion with corresponding sides → cross-multiply → solve.

---

### Level 3: Use Triangle Proportionality Theorem with Algebra

**Problem 2.3:**
In triangle ABC, line segment DE is parallel to BC. D is on AB and E is on AC.
AD = 2x, DB = x, AE = 3x + 5, EC = x + 1.

Find the value of x.

**Solution:**
By Triangle Proportionality Theorem:
$\frac{AD}{DB} = \frac{AE}{EC}$

$\frac{2x}{x} = \frac{3x + 5}{x + 1}$

$2 = \frac{3x + 5}{x + 1}$

$2(x + 1) = 3x + 5$

$2x + 2 = 3x + 5$

$-x = 3$

$x = -3$

**Wait:** Check for validity. If x = -3, then DB = -3 (negative length). This is impossible.

Actually, re-examine the setup. Let me assume AD = 2x, DB = 3x (revised).

$\frac{2x}{3x} = \frac{3x + 5}{x + 1}$

$\frac{2}{3} = \frac{3x + 5}{x + 1}$

$2(x + 1) = 3(3x + 5)$

$2x + 2 = 9x + 15$

$-7x = 13$

$x = -\frac{13}{7}$ (still negative)

**Corrected Problem:**
AD = x, DB = 2x, AE = 3, EC = 6.

$\frac{x}{2x} = \frac{3}{6}$

$\frac{1}{2} = \frac{1}{2}$ ✓ (This is always true; any positive x works.)

**Better version:** AD = x, DB = 2, AE = x + 3, EC = 4.

$\frac{x}{2} = \frac{x + 3}{4}$

$4x = 2(x + 3) = 2x + 6$

$2x = 6$

$x = 3$

**Trigger extraction:** Set up proportion from parallel line condition → cross-multiply → solve linear equation → check for valid (positive) lengths.

---

### Level 4: Multi-Step — Find Scale Factor, Then Use It

**Problem 2.4:**
Triangle PQR ~ Triangle STU.
PQ = 5, QR = 8, PR = 7, ST = 15.

(a) Find the scale factor from PQR to STU.
(b) Find TU and SU.

**Solution:**

**(a)** Scale factor k = ST / PQ = 15 / 5 = 3

**(b)** Using k = 3:
- TU = 3 × QR = 3 × 8 = 24
- SU = 3 × PR = 3 × 7 = 21

**Verification:** Ratio check: 15/5 = 24/8 = 21/7 = 3 ✓

**Trigger extraction:** Identify a corresponding pair → calculate scale factor → apply uniformly to all sides.

---

### Level 5: Indirect Measurement (Real-World Context)

**Problem 2.5: Shadow Problem**
A tree casts a shadow 20 feet long when a 6-foot-tall person casts a 4-foot shadow.
Find the height of the tree.

**Solution:**
The angle of sunlight is the same for both objects, so the triangles (formed by the object, shadow, and light ray) are similar.

**Set up proportion:**
$\frac{\text{height of tree}}{\text{height of person}} = \frac{\text{shadow of tree}}{\text{shadow of person}}$

$\frac{h}{6} = \frac{20}{4}$

$\frac{h}{6} = 5$

$h = 30$ feet

**Pattern observed:** Similar right triangles allow us to measure something indirectly by comparing it to something we can measure directly.

**Trigger extraction:** Identify the similar triangles → set up proportion with corresponding measurements → solve for unknown.

---

### Level 6: Prove a Relationship Using Similarity

**Problem 2.6: Midsegment Theorem via Similarity**
In triangle ABC, point M is the midpoint of AB and point N is the midpoint of AC.
Prove that MN is parallel to BC and MN = (1/2)BC.

**Solution:**

Consider triangle AMN and triangle ABC.

- Angle A is common to both.
- AM = (1/2)AB (M is the midpoint)
- AN = (1/2)AC (N is the midpoint)

By SAS Similarity (we have two sides in proportion and the included angle equal):
$\frac{AM}{AB} = \frac{AN}{AC} = \frac{1}{2}$, and angle A = angle A.

Therefore, triangle AMN ~ triangle ABC with scale factor k = 1/2.

Since the triangles are similar:
- Corresponding angles are equal → angle AMN = angle ABC
- These are alternate interior angles, so MN ∥ BC
- Corresponding sides are proportional: $\frac{MN}{BC} = \frac{1}{2}$

Therefore, $MN = \frac{1}{2}BC$ ✓

**Trigger extraction:** Use similarity criteria (here, SAS~) to establish relationship → use properties of similar triangles (equal angles, proportional sides) to prove the desired result.

---

---

## MODULE 3: BARRIER INVENTORY (Common Traps & Misconceptions)

### Barrier 1: Wrong Correspondence in Proportions

**The Trap:**
Triangle ABC ~ Triangle PQR.
AB = 6, BC = 8, PQ = 9, QR = ?

**Incorrect approach:** $\frac{AB}{BC} = \frac{PQ}{QR}$ → $\frac{6}{8} = \frac{9}{QR}$ → QR = 12

**Why it's wrong:** AB and BC are on the same triangle. We need to match sides across triangles.
- AB corresponds to PQ (first side of each triangle)
- BC corresponds to QR (second side of each triangle)

**Correct approach:** $\frac{AB}{PQ} = \frac{BC}{QR}$ → $\frac{6}{9} = \frac{8}{QR}$ → $\frac{2}{3} = \frac{8}{QR}$ → QR = 12

Wait, same answer. Let me revise.

**Better example:**
Triangle ABC ~ Triangle RST.
AB = 4, AC = 6, RS = 10, ST = ?

**Incorrect:** Assume AC corresponds to ST (wrong—they're not corresponding sides).
$\frac{AC}{ST} = \frac{AB}{RS}$ → $\frac{6}{ST} = \frac{4}{10}$ → ST = 15

**Correct:** AC corresponds to RT (second and third sides in the correspondence A↔R, B↔S, C↔T).
$\frac{AB}{RS} = \frac{AC}{RT}$ → $\frac{4}{10} = \frac{6}{RT}$ → RT = 15

And ST corresponds to... we need more info. The point is: **verify correspondence first.**

### Barrier 2: Confusing k and k² (Perimeter vs Area)

**The Trap:**
Circle A has radius 5. Circle B has radius 10 (scale factor k = 2).

Incorrect: "Circle B has 2 times the area."
Correct: Circle B has 2² = 4 times the area.

**Why:** Area scales by k². If all linear dimensions double (k = 2), the area quadruples (4 = 2²).

**Quick check:**
- Area of A = π(5)² = 25π
- Area of B = π(10)² = 100π
- Ratio: 100π / 25π = 4 ✓

---

### Barrier 3: AA Requires Angles, Not Sides

**The Trap:**
"Triangle ABC has sides 3, 4, 5. Triangle PQR has sides 6, 8, 10. By AA, they're similar."

**Why it's wrong:** AA means **Angle-Angle**. You need angle measures, not side lengths.

**Correct statement:** By SSS Similarity (sides are proportional), they're similar. 3/6 = 4/8 = 5/10 = 1/2.

**Common student error:** Confusing the three similarity theorems:
- **AA:** Two angles equal
- **SSS~:** All three sides proportional
- **SAS~:** Two sides proportional + included angle equal

---

### Barrier 4: Geometric Mean — Which Numbers Go Where?

**The Trap:**
"Find the geometric mean of 2 and 8."

Incorrect: GM = 2 + 8 / 2 = 5 (arithmetic mean, not geometric)
Correct: GM = √(2 × 8) = √16 = 4

**Setup check:**
If x is the geometric mean, then 2/x = x/8 (proportional).
x² = 2 × 8 = 16, so x = 4.

**In the altitude-on-hypotenuse theorem:**
In a right triangle, if an altitude is drawn to the hypotenuse, the altitude is the geometric mean of the two segments of the hypotenuse.

If altitude = h, and hypotenuse segments are p and q, then:
h² = p × q, or h = √(pq)

---

### Barrier 5: Forgetting to Check All Conditions for SSS~ and SAS~

**The Trap:**
"Triangle ABC has sides 4, 5, 6. Triangle PQR has sides 8, 10, 12. They're similar by SSS."

This is correct: 4/8 = 5/10 = 6/12 = 1/2. All three ratios match.

**The real trap:**
What if the sides are 4, 5, 6 and 8, 10, 13?
4/8 = 1/2, 5/10 = 1/2, but 6/13 ≠ 1/2.

Not all three ratios match → **not similar by SSS~** → these triangles are not similar.

**For SAS~:**
Triangle ABC: sides 6, 9, angle C = 50°.
Triangle PQR: sides 4, 6, angle R = 50°.

Are they similar by SAS~?

Check: 6/4 = 1.5, 9/6 = 1.5, and angles match.

**Yes, SAS~ applies** (the two sides forming the given angle are proportional, and the angle is the same).

---

---

## MODULE 4: REPRESENTATION SWITCHES (Flexible Problem-Solving)

### Switch 1: Similarity Proof — Transformation vs. Criteria

**Problem 4.1a: Transformation Approach**

Prove that a dilation with scale factor 2 centered at origin followed by a reflection over the x-axis transforms triangle ABC to triangle A'B'C', which is similar to ABC.

**Solution:**
- **Dilation** with scale factor k = 2 preserves angles and scales all sides by 2.
- **Reflection** is a rigid motion (preserves angles and side lengths).

Combined: ABC is transformed to A'B'C'' by dilation (now similar with ratio 2:1), then to A'B'C' by reflection (still similar, since rigid motions preserve similarity).

Therefore, ABC ~ A'B'C' by the definition of similarity via transformations.

**Problem 4.1b: Criteria Approach**

Given: In triangle ABC, angle A = 45°, AB = 8, AC = 12.
In triangle A'B'C', angle A' = 45°, A'B' = 4, A'C' = 6.

Prove ABC ~ A'B'C' using SAS~.

**Solution:**
- Angle A = Angle A' = 45° ✓
- $\frac{AB}{A'B'} = \frac{8}{4} = 2$
- $\frac{AC}{A'C'} = \frac{12}{6} = 2$

Two sides are proportional with scale factor 2, and the included angle is equal.

By SAS~: ABC ~ A'B'C' ✓

---

### Switch 2: Proportion Algebraically vs. Scale Factor Method

**Problem 4.2a: Algebraic (Proportion) Method**

Triangle DEF ~ Triangle GHI.
DE = 5, EF = 7, GH = 15, HI = x.

Find x using a proportion.

**Solution:**
$\frac{DE}{GH} = \frac{EF}{HI}$

$\frac{5}{15} = \frac{7}{x}$

Cross-multiply: $5x = 105$, so $x = 21$

**Problem 4.2b: Scale Factor Method**

Find the scale factor: k = GH / DE = 15 / 5 = 3

Apply to the other side: HI = 3 × EF = 3 × 7 = 21

Both methods give **x = 21**.

**Difference:** Scale factor is faster once you've found it; proportions work even if you don't explicitly compute k.

---

### Switch 3: Geometric Mean — Algebraic vs. Geometric Construction

**Problem 4.3a: Algebraic Definition**

Find the geometric mean of 9 and 16.

**Solution:**
Let x = geometric mean.

$\frac{9}{x} = \frac{x}{16}$

$x^2 = 144$, so $x = 12$

Or: GM = √(9 × 16) = √144 = 12

**Problem 4.3b: Geometric Construction (Conceptual)**

On a number line, position 9 and 16. The geometric mean is the side length of a square whose area equals the product 9 × 16 = 144.

Area = 144 → side length = √144 = 12

**Or using the right triangle altitude:**
Draw a right triangle with legs of length 9 and 16. The hypotenuse has length √(9² + 16²) = √(81 + 256) = √337 ≈ 18.36.

If you draw an altitude from the right angle to the hypotenuse, that altitude has length 12 (the geometric mean). This follows from the altitude-on-hypotenuse theorem.

---

---

## MODULE 5: TRIGGER EXTRACTION (Exam-Style Problems)

### Problem 5.1: Identify & Apply AA Similarity

In triangle ABC, angle A = 58°, angle B = 67°.
In triangle XYZ, angle X = 58°, angle Y = 55°.

Are the triangles similar? Justify.

**Solution:**
In ABC: angles are 58°, 67°, and 180° - 58° - 67° = 55°.
In XYZ: angles are 58°, 55°, and 180° - 58° - 55° = 67°.

ABC and XYZ both have angles {58°, 67°, 55°}.

**By AA, ABC ~ XYZ.**

Correspondence: A ↔ X (58°), C ↔ Y (55°), B ↔ Z (67°).

**Technique trigger:** Recognize angle equality → AA applies.
**Switch trigger:** Once similar, you could prove correspondence algebraically (proportions) or geometrically (transformations).

---

### Problem 5.2: Set Up & Solve Proportion with Multiple Unknowns

In triangle PQR, the sides are PQ = 10, QR = 15, PR = 12.
Triangle STU ~ PQR with scale factor k = 2.5.

Find all sides of STU.

**Solution:**
Scale factor k = 2.5 (STU is 2.5 times as large).

- ST (corresponds to PQ) = 2.5 × 10 = 25
- TU (corresponds to QR) = 2.5 × 15 = 37.5
- SU (corresponds to PR) = 2.5 × 12 = 30

**STU has sides: 25, 37.5, 30**

**Technique trigger:** Identify correspondence → apply scale factor uniformly.
**Switch trigger:** Could also set up three separate proportions and solve each.

---

### Problem 5.3: Triangle Proportionality Theorem with Parameters

In triangle ABC, line DE is parallel to BC, with D on AB and E on AC.
AD = a, DB = b, AE = a + 3, EC = b + 4.

Find the relationship between a and b.

**Solution:**
By the Triangle Proportionality Theorem:
$\frac{AD}{DB} = \frac{AE}{EC}$

$\frac{a}{b} = \frac{a + 3}{b + 4}$

Cross-multiply: $a(b + 4) = b(a + 3)$

$ab + 4a = ab + 3b$

$4a = 3b$

$\frac{a}{b} = \frac{3}{4}$

**Relationship:** a = (3/4)b, or equivalently, 4a = 3b.

**Technique trigger:** Set up proportion → cross-multiply → simplify to find parametric relationship.
**Switch trigger:** Given specific values for a or b, you could compute the other.

---

### Problem 5.4: Multi-Step with Perimeter and Area

Triangle ABC has perimeter 30 and area 40 square units.
Triangle PQR ~ ABC with scale factor k = 1/2.

Find the perimeter and area of PQR.

**Solution:**

Perimeter of PQR = k × Perimeter of ABC = (1/2) × 30 = **15 units**

Area of PQR = k² × Area of ABC = (1/2)² × 40 = (1/4) × 40 = **10 square units**

**Technique trigger:** Recognize k applies to perimeter; k² applies to area.
**Switch trigger:** Could verify using specific side and height calculations.

---

### Problem 5.5: Real-World — Mirror Problem

A 5-foot-tall person stands 8 feet away from a plane mirror and can see the top of a 20-foot-tall building in the mirror. How far is the person from the building?

**Solution:**
The light path creates similar triangles:
1. Triangle formed by person: height 5 ft, horizontal distance d to mirror.
2. Triangle formed by building: height 20 ft, horizontal distance (total distance - d) to mirror.

For the reflection to work, angle of incidence = angle of reflection. This means:
$\frac{5}{d} = \frac{20}{8 + x}$

where x is the distance from the mirror to the building.

Hmm, we need the person's distance from the building, which is 8 + x.

Actually, let me reconsider. If the person is 8 feet from the mirror:

$\frac{5}{8} = \frac{20}{D}$, where D is the building's distance from the mirror.

$5D = 160$, so $D = 32$ feet.

The person's distance from the building = 8 + 32 = **40 feet** (if they're on opposite sides of the mirror).

**Or:** If the building and person are on the same side:
Distance = 32 - 8 = 24 feet.

(Clarify the setup with a diagram in a real problem.)

**Technique trigger:** Identify similar triangles formed by light reflection → set up proportion.
**Switch trigger:** Could use angle relationships or slopes instead.

---

### Problem 5.6: Similarity & Indirect Measurement (Proportional Segments)

A telephone pole 25 feet tall casts a shadow 40 feet long.
At the same time, a nearby building casts a shadow 120 feet long.
How tall is the building?

**Solution:**
The sun's angle is the same, so the triangles are similar.

$\frac{\text{height of pole}}{\text{shadow of pole}} = \frac{\text{height of building}}{\text{shadow of building}}$

$\frac{25}{40} = \frac{h}{120}$

$\frac{5}{8} = \frac{h}{120}$

$h = \frac{5 \times 120}{8} = \frac{600}{8} = 75$ feet

**The building is 75 feet tall.**

**Technique trigger:** Recognize similar triangles from parallel sun rays → set up proportion.
**Switch trigger:** Could use scale factor: k = 120/40 = 3, so h = 3 × 25 = 75.

---

### Problem 5.7: Prove Proportionality Using Similarity

Given: In triangle ABC, point D is on AB and point E is on AC such that DE ∥ BC.

Prove: $\frac{AD}{AB} = \frac{AE}{AC}$ (Alternative form of Triangle Proportionality Theorem)

**Solution:**
Since DE ∥ BC:
- Triangle ADE ~ Triangle ABC (by AA: angle A is common, and corresponding angles are equal because DE ∥ BC).

By the definition of similar triangles, corresponding sides are proportional:
$\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}$

Therefore, $\frac{AD}{AB} = \frac{AE}{AC}$ ✓

**Technique trigger:** Use parallel lines → establish similarity (AA) → apply proportional sides definition.
**Switch trigger:** Could instead use the original form: AD/DB = AE/EC.

---

### Problem 5.8: SSS Similarity Check

Triangle ABC has sides 10, 15, 18.
Triangle DEF has sides 12, 18, 21.6.

Are they similar by SSS~?

**Solution:**
Check if all ratios of corresponding sides are equal:

$\frac{10}{12} = \frac{5}{6} ≈ 0.833$

$\frac{15}{18} = \frac{5}{6} ≈ 0.833$

$\frac{18}{21.6} = \frac{18}{21.6} = \frac{5}{6} ≈ 0.833$

All three ratios equal 5/6.

**Yes, ABC ~ DEF by SSS~ with scale factor k = 5/6.**

**Technique trigger:** Check all three ratio pairs → confirm all equal → conclude SSS~.
**Switch trigger:** Once similar, could set up proportions or use scale factor.

---

---

## MODULE 6: CANDIDATE ATTACK CHALLENGE (Synthesis & Proof)

### Challenge 6.1: Complex Multi-Step with Algebra

**Problem:**
In triangle ABC, angle C = 90°. Points D, E, F divide the sides such that:
- D is on AB with AD = 2, DB = 8 (so AB = 10)
- E is on BC with BE = 4, EC = 6 (so BC = 10)
- F is on AC (to be determined)

A line is drawn through E parallel to AC. This line intersects AB at point D'. Is D' the same as D? Justify using similarity.

**Solution:**
Since the line through E is parallel to AC, and AC is a side of triangle ABC, by the Intercept Theorem (or Basic Proportionality Theorem applied backward):

If the line through E parallel to AC intersects AB at D', then:
$\frac{AD'}{D'B} = \frac{AE}{EC}$

We have AE = AB - BE = AB - 4. But wait, E is on BC, not AB.

Let me reconsider. If a line through E (on BC) is parallel to AC (a side of triangle ABC), it intersects AB at some point D'.

By similar triangles (triangle formed by the parallel line is similar to ABC):
$\frac{BD'}{BA} = \frac{BE}{BC}$

$\frac{BD'}{10} = \frac{4}{10}$

$BD' = 4$

So D' is located such that AD' = 10 - 4 = 6.

But D has AD = 2, so D ≠ D'.

**Answer:** No, D' ≠ D. The parallel line through E intersects AB at D' where AD' = 6, but D has AD = 2.

**Technique trigger:** Identify the line parallel to a side → use similarity to find intercepts.
**Switch trigger:** Could use the Triangle Proportionality Theorem directly or coordinate geometry.

---

### Challenge 6.2: Indirect Measurement & Real-World Application

**Problem:**
A surveyor needs to find the width of a river. She measures:
- Distance from point A to point B (on the same bank): 200 feet
- Angle at A toward point C (across the river): 60°
- Angle at B toward point C: 45°

Using similar triangles, find the width of the river (the perpendicular distance from C to line AB).

**Solution:**
Let h = perpendicular distance from C to AB (the river width).
Let x = distance from A to the foot of the perpendicular (call it P).

From triangle APC (angle at P is 90°):
tan(60°) = h / x
√3 = h / x
h = x√3

From triangle BPC (angle at P is 90°):
tan(45°) = h / (200 - x)
1 = h / (200 - x)
h = 200 - x

Equate:
x√3 = 200 - x
x√3 + x = 200
x(√3 + 1) = 200
x = 200 / (√3 + 1)

Rationalize:
x = 200(√3 - 1) / ((√3 + 1)(√3 - 1)) = 200(√3 - 1) / (3 - 1) = 200(√3 - 1) / 2 = 100(√3 - 1)

Now, h = 200 - x = 200 - 100(√3 - 1) = 200 - 100√3 + 100 = 300 - 100√3 ≈ 300 - 173.2 ≈ **126.8 feet**

**Answer:** The river is approximately 126.8 feet wide.

**Technique trigger:** Set up right triangles with known angles → use trigonometry (tangent) to relate height to base → solve system of equations.
**Switch trigger:** Could use similarity of triangles and proportions instead of trigonometry.

---

### Challenge 6.3: Prove Pythagorean Theorem via Similar Triangles

**Problem:**
In a right triangle ABC with right angle at C, an altitude is drawn from C to the hypotenuse AB, meeting at point H.

Prove that $AC^2 + BC^2 = AB^2$ (Pythagorean Theorem) using similarity.

**Solution:**
By the altitude-on-hypotenuse construction, three similar right triangles are formed:
1. Triangle ABC (original)
2. Triangle ACH (shares angle A with ABC)
3. Triangle BCH (shares angle B with ABC)

All three are similar.

From ABC ~ ACH:
$\frac{AC}{AB} = \frac{AH}{AC}$

Therefore: $AC^2 = AB \cdot AH$ ... (1)

From ABC ~ BCH:
$\frac{BC}{AB} = \frac{BH}{BC}$

Therefore: $BC^2 = AB \cdot BH$ ... (2)

Adding (1) and (2):
$AC^2 + BC^2 = AB \cdot AH + AB \cdot BH = AB(AH + BH) = AB \cdot AB = AB^2$

**Therefore: $AC^2 + BC^2 = AB^2$ ✓**

**Technique trigger:** Use altitude-on-hypotenuse → identify similar triangles → extract proportions → combine to reach the desired result.
**Switch trigger:** The geometric mean altitude-on-hypotenuse theorem (h² = p·q for segments p and q) follows from the same setup.

---

---

## INTUITIVE EXPLANATIONS (Solutions & LDP Connections)

### Explanation: Why AA Similarity Works

**The Core Idea:**
If two angles in one triangle match two angles in another, the third angles must also match (since angles in a triangle sum to 180°). Matching angles means the triangles "look the same shape." They may differ in size, but the proportions are identical.

**Why Sides Are Proportional:**
Imagine enlarging or shrinking one triangle until one pair of corresponding sides match. Because the angles are the same, the other sides will automatically line up in proportion. This is captured by the theorem: AA → similar → all sides proportional.

---

### Explanation: Why Perimeter Scales by k, but Area by k²

**Perimeter:**
If each side is multiplied by k, then the perimeter (sum of sides) is also multiplied by k.

Example: Triangle with sides 3, 4, 5 (perimeter 12). Scale by k = 2 → sides 6, 8, 10 (perimeter 24 = 2 × 12). ✓

**Area:**
Area involves two dimensions (base and height). If each is multiplied by k, the product (area) is multiplied by k × k = k².

Example: Triangle with base 4 and height 3 (area = 6). Scale by k = 2 → base 8, height 6 (area = 24 = 4 × 6 = k² × 6). ✓

**Real-world context:** A 2×2 square has area 4. A 4×4 square (k = 2) has area 16 (not 8). The area quadruples because it spans a larger region in two directions.

---

### Explanation: Triangle Proportionality Theorem (Side-Splitter)

**The Setup:**
You have a triangle ABC and a line DE parallel to side BC. D is on AB, E is on AC. The parallel line "cuts" the two sides proportionally.

**Why It Works:**
When DE is parallel to BC, triangles ADE and ABC are similar (by AA: angle A is shared, and corresponding angles are equal because DE ∥ BC).

From similarity:
$\frac{AD}{AB} = \frac{AE}{AC}$

This can be rearranged to:
$\frac{AD}{DB} = \frac{AE}{EC}$

Both forms say the same thing: the segments are proportional.

---

### Explanation: Geometric Mean

**The Formula:**
Geometric mean of a and b is √(a·b).

**Why:**
The phrase "geometric mean" suggests it's the side length of a square with area equal to the product a·b. Since area = side², we have side = √(a·b).

**Connection to Right Triangles:**
In a right triangle, when you draw an altitude to the hypotenuse, it divides the hypotenuse into two segments. The altitude itself is the geometric mean of those two segments. This follows from similar triangles:

altitude² = (first segment) × (second segment)

---

### Explanation: SSS vs. SAS vs. AA Similarity

**AA (Angle-Angle):**
If two angles match, the third automatically matches. Simplest to check. Just verify two angles.

**SAS (Side-Angle-Side):**
Two sides are proportional + the angle between them is equal. Checking three things (two ratios and one angle), but more restrictive than AA.

**SSS (Side-Side-Side):**
All three sides are proportional. Most restrictive: you must check three ratios.

**Why These Work:**
All rely on the fact that if the **shape** is preserved (through angle or side relationships), then the **size** can differ. The theorems capture the minimal conditions to guarantee shape preservation.

---

### Explanation: Cross-Multiplication in Proportions

**The Rule:**
If $\frac{a}{b} = \frac{c}{d}$, then $a \cdot d = b \cdot c$.

**Why:**
Multiply both sides of the equation by b·d:
$\frac{a}{b} \cdot bd = \frac{c}{d} \cdot bd$

$a \cdot d = b \cdot c$ ✓

**In Context:**
When you have a proportion from similar triangles and want to solve for an unknown, cross-multiply to eliminate fractions.

---

### Explanation: Scale Factor and Correspondence

**The Critical Step:**
Before using a scale factor, you must identify which sides correspond. A correspondence is an ordered pairing of sides based on angle matching or the similarity statement.

Example: If triangle ABC ~ triangle PQR, then:
- A ↔ P, B ↔ Q, C ↔ R
- Side AB ↔ side PQ
- Side BC ↔ side QR
- Side CA ↔ side RP

Once you know the correspondence, the scale factor (ratio of one pair of corresponding sides) applies to all other pairs.

---

### Explanation: Why Parallel Lines Create Proportional Segments

**The Intuition:**
Imagine two parallel lines cutting across two transversals. The parallel lines "divide" each transversal in the same ratio. This is because the triangles formed are similar (angles are equal by parallel line properties).

**Connection to Triangle Proportionality:**
The triangle proportionality theorem is a special case where one transversal is the hypotenuse and the other two are the legs, and a line parallel to the "base" cuts the legs proportionally.

---

### Explanation: Altitude-on-Hypotenuse and Similar Triangles

**The Setup:**
In a right triangle ABC (right angle at C), drop an altitude from C to the hypotenuse AB, meeting at H.

**What Happens:**
- Triangle ACH is similar to triangle ABC (angle A is shared; angles AHC and ACB are both right angles).
- Triangle BCH is similar to triangle ABC (angle B is shared; angles BHC and ACB are both right angles).
- Therefore, triangle ACH ~ triangle BCH as well.

**Consequences:**
1. $AC^2 = AH \cdot AB$ (geometric mean relation)
2. $BC^2 = BH \cdot AB$ (geometric mean relation)
3. $CH^2 = AH \cdot BH$ (altitude is geometric mean of hypotenuse segments)
4. Adding the first two: $AC^2 + BC^2 = AB(AH + BH) = AB^2$ (Pythagorean Theorem)

---

### Explanation: Midsegment via Similarity

**The Statement:**
In a triangle, the segment connecting the midpoints of two sides is parallel to the third side and has length equal to half the third side.

**Why (via Similarity):**
Let M and N be midpoints of AB and AC respectively.

Triangle AMN has:
- AM = (1/2) AB
- AN = (1/2) AC
- Angle A = angle A (trivial)

By SAS similarity: Triangle AMN ~ Triangle ABC with scale factor k = 1/2.

Since the triangles are similar:
- Corresponding angles are equal → angle AMN = angle ABC → MN ∥ BC (alternate interior angles)
- Corresponding sides are proportional → MN / BC = 1/2 → **MN = (1/2) BC**

---

### Explanation: Real-World Similarity — Shadow & Mirror Problems

**Shadow Problem:**
The sun's rays are parallel (since the sun is very far away). A vertical object and its shadow form a right triangle. Two objects cast shadows under the same angle of sunlight, so their triangles are similar. Thus:

$\frac{\text{height}_1}{\text{shadow}_1} = \frac{\text{height}_2}{\text{shadow}_2}$

**Mirror Problem:**
Light reflects at equal angles (angle of incidence = angle of reflection). An observer and the object being viewed form two triangles with the mirror as a base. These triangles are similar due to the equal reflection angles. Thus:

$\frac{\text{height}_{\text{observer}}}{\text{distance}_{\text{observer}}} = \frac{\text{height}_{\text{object}}}{\text{distance}_{\text{object}}}$

---

### Explanation: Pythagorean Theorem via Similarity (Deep Insight)

**The Proof Idea:**
The Pythagorean theorem isn't just an algebraic identity. It arises naturally from the geometric property that an altitude to the hypotenuse creates similar triangles.

**The Chain:**
1. Draw altitude CH in right triangle ABC (right angle at C).
2. Similarity creates: $AC^2 = AB \cdot AH$ and $BC^2 = AB \cdot BH$
3. Add: $AC^2 + BC^2 = AB \cdot (AH + BH) = AB \cdot AB = AB^2$

**Why This Matters:**
This proof reveals that the Pythagorean theorem is fundamentally about proportions and similarity, not just numerical squares. It shows that the "right angle" property is intimately connected to proportional segments created by the altitude.

---

---

## MASTER CHECKLIST FOR SIMILARITY PROBLEMS

1. **Identify the similarity theorem:**
   - Do I have two angles? → AA
   - Do I have two proportional sides and the included angle? → SAS~
   - Do I have all three sides proportional? → SSS~

2. **Find correspondence:**
   - Which vertices/sides correspond?
   - Verify angles or use the given similarity statement.

3. **Set up the proportion:**
   - Match corresponding sides in order.
   - Use consistent notation.

4. **Solve the proportion:**
   - Cross-multiply if needed.
   - Check for extraneous solutions (lengths must be positive).

5. **Apply scale factor (if beneficial):**
   - Calculate k once.
   - Multiply all unknown sides by k.

6. **Check perimeter and area:**
   - Perimeter scales by k.
   - Area scales by k².

7. **Verify the answer:**
   - Do all ratios match the scale factor?
   - Are all lengths positive?
   - Does the answer make geometric sense?

---

## KEY DEFINITIONS & THEOREMS

- **Similar figures:** Same shape, proportional sides, equal angles.
- **Scale factor k:** Ratio of corresponding sides.
- **AA Similarity:** If two angles are equal, triangles are similar.
- **SSS~ Similarity:** If all three sides are proportional, triangles are similar.
- **SAS~ Similarity:** If two sides are proportional and the included angle is equal, triangles are similar.
- **Triangle Proportionality Theorem:** If a line is parallel to one side of a triangle, it divides the other two sides proportionally.
- **Geometric Mean of a and b:** $\sqrt{ab}$ or the number x such that $\frac{a}{x} = \frac{x}{b}$.
- **Altitude-on-Hypotenuse Theorem:** In a right triangle, the altitude to the hypotenuse is the geometric mean of the hypotenuse segments.
- **Midsegment Theorem:** The segment connecting midpoints of two sides is parallel to the third side and half its length.
- **Perimeter Ratio:** If linear scale factor = k, then perimeter ratio = k.
- **Area Ratio:** If linear scale factor = k, then area ratio = k².

---

**End of Worksheet**
