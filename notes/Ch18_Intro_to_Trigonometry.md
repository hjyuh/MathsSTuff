# Chapter 18: Introduction to Trigonometry — Problem-Solving Notes

---

## Section 18.1: Trigonometry and Right Triangles

### Core Definitions

**sin A = opposite / hypotenuse = a/c**
**cos A = adjacent / hypotenuse = b/c**
**tan A = opposite / adjacent = a/b = sin A / cos A**

(In right triangle △ABC with ∠C = 90°, BC = a, AC = b, AB = c)

**Why these work:** All right triangles sharing the same acute angle are similar (by AA Similarity). So the *ratio* of any two sides is the same across all of them. Sine, cosine, and tangent are just names for these three fixed ratios. You're not computing a property of a specific triangle — you're computing a property of the *angle*.

**Mnemonic:** SOH-CAH-TOA (Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, Tangent = Opposite/Adjacent)

### Special Angle Values

| Angle | sin | cos | tan |
|-------|-----|-----|-----|
| 0° | 0 | 1 | 0 |
| 30° | 1/2 | √3/2 | 1/√3 = √3/3 |
| 45° | √2/2 | √2/2 | 1 |
| 60° | √3/2 | 1/2 | √3 |
| 90° | 1 | 0 | undefined |

**Don't memorize this table.** These come directly from the 30-60-90 triangle (sides 1 : √3 : 2) and the 45-45-90 triangle (sides 1 : 1 : √2). If you know those triangles, you can rebuild this table in seconds.

### Key Identities

**sin²A + cos²A = 1**

**Why it works:** In right triangle △ABC with hypotenuse c, sin A = a/c and cos A = b/c. So sin²A + cos²A = a²/c² + b²/c² = (a² + b²)/c² = c²/c² = 1, by the Pythagorean Theorem. This identity *is* the Pythagorean Theorem in disguise.

**sin A = cos(90° − A)**

**Why it works:** The side opposite angle A is the side adjacent to angle B = 90° − A, and vice versa. So sine and cosine are "co-functions" — the "co" in cosine literally means "complement."

### Bounds on Trig Functions

- **0 < sin A < 1** and **0 < cos A < 1** for acute angles (because the hypotenuse is always the longest side)
- **tan A > 0** with **no upper bound** for acute angles (as the angle approaches 90°, the opposite leg grows without limit relative to the adjacent leg)

### Trigger → Technique Map

| You see... | You do... | Watch out for... |
|---|---|---|
| Right triangle + angle + one side, need another side | Use sin/cos/tan to set up a ratio and solve | Make sure you identify opposite/adjacent relative to the *given angle*, not just any angle |
| Need to find a trig value of 30°, 45°, or 60° | Draw the special right triangle and read off the ratio | Don't confuse sin 30° = 1/2 with sin 60° = √3/2 — draw the triangle every time until it's automatic |
| Expression with sin²A + cos²A | Replace with 1 | Works for ANY angle, not just acute |
| Know sin, need cos (or vice versa) | Use sin²A + cos²A = 1 to find the other | Remember to take the positive root for acute angles (both sin and cos are positive) |
| Problem says "angle of elevation" or "angle of depression" | Draw horizontal line, mark angle from horizontal, build right triangle | Angle of elevation/depression is from the HORIZONTAL, not from the vertical |

### Worked Examples

**Level 1 — Straightforward application**

> *Problem 18.5:* In △PQR, ∠P = 90°, PQ = 3, QR = 7. Find sin Q, cos R, and sin²R + cos²R.

*Trigger:* Right triangle with known sides → apply definitions directly.
*Solution:* First, PR = √(QR² − PQ²) = √(49 − 9) = √40 = 2√10.
- sin Q = opposite/hypotenuse = PR/QR = 2√10/7
- cos R = adjacent/hypotenuse = PR/QR = 2√10/7 (notice sin Q = cos R, because Q and R are complementary!)
- sin²R + cos²R = (3/7)² + (2√10/7)² = 9/49 + 40/49 = 1 ✓

**Level 2 — Multi-step with right triangle construction**

> *Problem 18.9:* Right triangle ABC has ∠ABC = 90°. Let M be the midpoint of AB. The perpendicular bisector of AB intersects AC at D, and sin ∠MDB = 1/5. If MD = 1, find AC.

*Trigger:* Given a trig value and one side length of a right triangle → we can find all sides. But first we need to figure out what D is.
*First move:* Recognize that the perpendicular bisector of AB in a right triangle passes through the circumcenter, which is the midpoint of the hypotenuse AC. So D is the midpoint of AC.
*Solution:*
1. D = midpoint of AC (perpendicular bisector of a side of a right triangle passes through the circumcenter = midpoint of hypotenuse)
2. In right triangle △MDB: sin ∠MDB = MB/BD = 1/5, and we need BD.
3. We know MD = 1, and cos ∠MDB = MD/BD, so BD = MD/cos ∠MDB.
4. From sin²∠MDB + cos²∠MDB = 1: cos²∠MDB = 1 − 1/25 = 24/25, so cos ∠MDB = 2√6/5.
5. BD = 1/(2√6/5) = 5/(2√6) = 5√6/12.
6. AC = 2·BD = 2 · 5√6/12 = **5√6/6**.

*Alternative approach:* You could also find MB first from sin ∠MDB = MB/BD, then use Pythagorean Theorem on △MDB. Same answer, slightly longer.

**Level 3 — Real-world application combining trig with geometry**

> *Problem 18.10:* I am 500 feet from a building. I look up at 7° to see the top, and down at 2° to see the base. How tall is the building?

*Trigger:* Angles of elevation/depression → draw horizontal, build two right triangles.
*First move:* The 7° up and 2° down are from horizontal, so we have TWO right triangles sharing the same horizontal leg of 500 ft.
*Solution:*
1. Upper triangle: tan 7° = BC/500, so BC = 500·tan 7° ≈ 500(0.1228) ≈ 61.4 ft
2. Lower triangle: tan 2° = BD/500, so BD = 500·tan 2° ≈ 500(0.0349) ≈ 17.5 ft
3. Total height = BC + BD ≈ **79 feet**

### Common Mistakes & Traps

**Conceptual:**
- **Confusing which side is "opposite" vs. "adjacent":** These are relative to the angle you're working with, NOT fixed labels. The same side can be "opposite" for one angle and "adjacent" for another.
- **Thinking sin/cos can be > 1 for acute angles:** Never. The hypotenuse is always the longest side of a right triangle. If you compute sin A = 1.3, you made an error.

**Execution:**
- **Calculator in wrong mode:** If sin 30° doesn't give you 0.5, your calculator is in radians, not degrees. Fix this before proceeding.
- **Forgetting to take the positive root:** When using sin²A + cos²A = 1, for acute angles both sin and cos are positive. But later (Section 18.2), the sign depends on the quadrant.

### Generalizations & Edge Cases

- sin²A + cos²A = 1 holds for ALL angles, not just acute ones (proven via unit circle in Section 18.2)
- As angle A → 0°, sin A → 0 and cos A → 1. As A → 90°, sin A → 1 and cos A → 0. Tangent blows up (→ ∞) as A → 90° because you're dividing by cos A → 0.
- There are three more trig functions: csc A = 1/sin A, sec A = 1/cos A, cot A = 1/tan A. You don't need them now, but they show up later.

### Connections

- **Builds on:** Similar triangles (Chapter 8), Pythagorean Theorem (Chapter 9), 30-60-90 and 45-45-90 triangles (Chapter 12)
- **Leads to:** Unit circle definition (Section 18.2), Law of Sines/Cosines (Section 18.3), competition geometry where trig provides cleaner solutions than synthetic approaches
- **Related to:** The identity sin²A + cos²A = 1 is the Pythagorean Theorem restated

---

## Section 18.2: Not Just For Right Triangles

### Core Definition

**Unit circle definition of sine and cosine:**

Let A = (1, 0). Let B be the point on the unit circle that is θ degrees counterclockwise from A. Then:
- **cos θ = x-coordinate of B**
- **sin θ = y-coordinate of B**
- **tan θ = sin θ / cos θ** (undefined when cos θ = 0)

**Why this matters:** The right-triangle definitions only work for angles between 0° and 90°. The unit circle definition extends sine and cosine to ALL angles — negative, greater than 360°, anything.

**Why it's consistent:** For acute angles, dropping a perpendicular from B to the x-axis creates a right triangle with hypotenuse 1 (the radius). The x-leg = cos θ and y-leg = sin θ — exactly matching the right triangle definitions.

### Signs by Quadrant

| Quadrant | Angle range | sin | cos | tan |
|----------|-------------|-----|-----|-----|
| I | 0° – 90° | + | + | + |
| II | 90° – 180° | + | − | − |
| III | 180° – 270° | − | − | + |
| IV | 270° – 360° | − | + | − |

**How to remember:** "All Students Take Calculus" — **A**ll positive in QI, **S**ine positive in QII, **T**angent positive in QIII, **C**osine positive in QIV. Or just think about which coordinates are positive/negative in each quadrant.

### Key Identity for Non-Acute Angles

**sin(180° − θ) = sin θ**

**Why it works:** On the unit circle, the point at angle θ and the point at angle 180° − θ are mirror images across the y-axis. Same y-coordinate (same sine), opposite x-coordinates (opposite cosines). This is why two different angles can have the same sine — critical for understanding why SSA doesn't prove congruence.

### The Area Formula

**[ABC] = ½ · AC · BC · sin C**

**Why it works:** Drop an altitude from A to BC. The altitude length = AC · sin C (from the right triangle it creates). Area = ½ · base · height = ½ · BC · (AC · sin C). This works for acute, right, AND obtuse angles because sin(180° − θ) = sin θ handles the obtuse case.

### Angles Beyond 360° and Negative Angles

- **θ + 360°** lands on the same point as θ → same trig values: sin(θ + 360°) = sin θ, cos(θ + 360°) = cos θ
- **Negative angles** mean go clockwise: cos(−300°) = cos 60° = 1/2

### Trigger → Technique Map

| You see... | You do... | Watch out for... |
|---|---|---|
| Trig function of angle > 90° (like sin 150°) | Find the reference angle, place the point on the unit circle, determine sign from quadrant | The reference angle is the acute angle between the terminal point and the x-axis, NOT the y-axis |
| sin(180° − θ) | Replace with sin θ | cos(180° − θ) = −cos θ (NOT +cos θ) — cosine flips sign |
| Triangle area with two sides and included angle | Use [ABC] = ½ab sin C | C must be the angle BETWEEN sides a and b |
| Angle > 360° or negative angle | Reduce: add/subtract 360° until in [0°, 360°), then find quadrant | −300° is the same as +60° (add 360°) |

### Worked Examples

**Level 1 — Evaluate trig of non-acute angle**

> *Problem:* Find cos 225° and sin 225°.

*Trigger:* Angle in quadrant III (between 180° and 270°) → find reference angle, apply signs.
*Solution:*
1. 225° − 180° = 45°, so the reference angle is 45°.
2. Drop perpendicular from the unit circle point to x-axis → 45-45-90 triangle with hypotenuse 1 → legs = √2/2.
3. Quadrant III: both x and y are negative.
4. cos 225° = −√2/2, sin 225° = −√2/2.

**Level 2 — Why SSA fails, using Law of Sines foreshadowing**

> *Problem:* Explain why knowing ∠A = 30°, BC = 3, AC = 4 in △ABC does NOT uniquely determine the triangle.

*Trigger:* This is the SSA (side-side-angle) configuration.
*Solution:* From the Law of Sines: sin B = (AC/BC) · sin A = (4/3)(1/2) = 2/3. But there are TWO angles between 0° and 180° with sin θ = 2/3 — one acute, one obtuse. Both produce valid triangles. So the triangle isn't uniquely determined.

*Alternative approach:* Geometrically, draw a circle of radius 3 centered at C. The circle intersects the ray from A at two points, giving two different triangles.

**Level 3 — Area formula with obtuse angle**

> *Problem 18.18:* Show that [ABC] = ½(AC)(BC) sin C for ANY triangle.

*Trigger:* Area formula with trig → need to handle all cases.
*First move:* Split into cases by ∠C (acute, right, obtuse) and use altitude construction in each case.
*Solution:*
- **∠C acute:** Altitude from A to BC has length h = AC · sin C. Area = ½ · BC · h = ½(AC)(BC) sin C. ✓
- **∠C = 90°:** sin 90° = 1. Area = ½(AC)(BC) · 1 = ½(AC)(BC). ✓
- **∠C obtuse:** Altitude from A falls OUTSIDE the triangle. h = AC · sin(180° − C). But sin(180° − C) = sin C, so Area = ½(AC)(BC) sin C. ✓

### Common Mistakes & Traps

**Conceptual:**
- **Getting sin and cos backwards on the unit circle:** cos = x-coordinate, sin = y-coordinate. Alphabetical order: **C**os → x, **S**in → y.
- **Thinking sin(180° − θ) = −sin θ:** WRONG. sin(180° − θ) = +sin θ. It's cosine that flips sign: cos(180° − θ) = −cos θ.

**Execution:**
- **Reference angle errors:** The reference angle is always measured to the x-axis, not the y-axis. For 150°, the reference angle is 30° (not 60°).
- **Forgetting the included angle in the area formula:** [ABC] = ½ab sin C works only when C is the angle BETWEEN sides a and b. If C is not the included angle, you'll get the wrong answer.

### Generalizations & Edge Cases

- sin²θ + cos²θ = 1 works for ALL angles (both coordinates on the unit circle satisfy x² + y² = 1)
- tan 90° and tan 270° are undefined (cos = 0 at those points)
- The area formula [ABC] = ½ab sin C unifies three cases into one elegant statement

### Connections

- **Builds on:** Unit circle, special right triangles (Section 18.1)
- **Leads to:** Law of Sines and Law of Cosines (Section 18.3), which are the main computational tools
- **Related to:** Circle properties (inscribed angles, circumradius) — the Extended Law of Sines connects trig to circles

---

## Section 18.3: Law of Sines and Law of Cosines

### Core Theorems

In △ABC with a = BC, b = AC, c = AB:

**Law of Cosines: c² = a² + b² − 2ab cos C**

**Why it works:** Drop altitude from B to AC, creating two right triangles. Use trig to express the altitude and base segments in terms of a, b, and C. Apply the Pythagorean Theorem to the resulting right triangle, then simplify using sin²C + cos²C = 1. The −2ab cos C term is the "correction" from the Pythagorean Theorem when the angle isn't 90°.

**When ∠C = 90°:** cos 90° = 0, so c² = a² + b². The Law of Cosines *becomes* the Pythagorean Theorem. It's the generalization.

**Law of Sines: a/sin A = b/sin B = c/sin C**

**Why it works:** Drop an altitude from any vertex. Express its length using trig from two different base triangles. Set the two expressions equal and simplify. The ratio a/sin A is the same from any vertex you choose.

**Extended Law of Sines: a/sin A = b/sin B = c/sin C = 2R** (where R = circumradius)

### Trigger → Technique Map

| You see... | You do... | Watch out for... |
|---|---|---|
| Know 2 sides + included angle, need 3rd side | **Law of Cosines** | Make sure the angle is BETWEEN the two known sides |
| Know 2 angles + 1 side, need other sides | **Law of Sines** (find 3rd angle first: A + B + C = 180°) | Two possible angles with the same sine — check if the obtuse option is geometrically valid |
| Know 3 sides, need an angle | **Law of Cosines** rearranged: cos C = (a² + b² − c²)/(2ab) | cos C can be negative (obtuse angle) — that's fine, don't panic |
| Need area with 2 sides + included angle | **Area = ½ab sin C** | This is not Law of Sines or Cosines, but it shows up alongside them |
| Know a side and its opposite angle + another side, need its opposite angle | **Law of Sines** | SSA ambiguity! sin B = (b/a) sin A may give 0, 1, or 2 valid triangles |

### Worked Examples

**Level 1 — Direct Law of Cosines**

> *Problem 18.19:* In △ABC, AC = 15, BC = 12, ∠C = 34°. Find AB.

*Trigger:* Two sides and the included angle → Law of Cosines.
*Solution:*
AB² = BC² + AC² − 2(BC)(AC) cos C = 144 + 225 − 2(12)(15) cos 34° ≈ 369 − 298.5 ≈ 70.5
AB ≈ **8.40**

**Level 2 — Law of Cosines then Law of Sines in sequence**

> *Problem 18.23:* In the diagram, △ABC has AB = 8, AC = 12, ∠A = 66°. Point D is such that ∠BCD = 65° and ∠BDC = 85°. Find BC, CD, and BD.

*Trigger:* First triangle has SAS → Law of Cosines. Second triangle has ASA (once we know BC) → Law of Sines.
*First move:* Use Law of Cosines on △ABC to find BC, then pivot to △BCD with Law of Sines.
*Solution:*
1. **Find BC** (Law of Cosines on △ABC):
   BC² = 8² + 12² − 2(8)(12) cos 66° ≈ 64 + 144 − 78.1 ≈ 129.9 → BC ≈ 11.4
2. **Find angles in △BCD:** ∠BCD = 65°, ∠BDC = 85°, so ∠DBC = 180° − 65° − 85° = 30°.
3. **Find BD and CD** (Law of Sines on △BCD):
   BC/sin D = BD/sin C = CD/sin B
   11.4/sin 85° = BD/sin 65° = CD/sin 30°
   BD = 11.4 · sin 65°/sin 85° ≈ **10.4**
   CD = 11.4 · sin 30°/sin 85° ≈ **5.7**

*Alternative approach for step 1:* You could drop an altitude from B to AC and use right triangle trig directly (the method the book uses to *derive* the Law of Cosines). Same answer, more steps.

**Level 3 — Proving the Law of Cosines (competition-style understanding)**

> *Problem 18.20:* Prove that c² = a² + b² − 2ab cos C for acute △ABC.

*Trigger:* "Prove a general formula" → start with a specific example, then generalize.
*First move:* Draw altitude BX from B to AC. This creates right triangles we can work with.
*Solution:*
1. From right △BXC: BX = a sin C, CX = a cos C
2. AX = AC − CX = b − a cos C
3. From right △ABX (Pythagorean Theorem):
   c² = BX² + AX² = (a sin C)² + (b − a cos C)²
   = a²sin²C + b² − 2ab cos C + a²cos²C
   = a²(sin²C + cos²C) + b² − 2ab cos C
   = **a² + b² − 2ab cos C** ∎

The key step is sin²C + cos²C = 1 cleaning everything up.

### Common Mistakes & Traps

**Conceptual:**
- **Using Law of Cosines when you should use Law of Sines (or vice versa):** Law of Cosines needs SAS or SSS. Law of Sines needs AAS, ASA, or SSA.
- **SSA ambiguity with Law of Sines:** If you solve sin B = k and get k < 1, there are generally TWO possible angles (one acute, one obtuse). You must check if both produce valid triangles.
- **Circular reasoning with the Pythagorean Theorem:** The Law of Cosines is PROVED using the Pythagorean Theorem. You cannot use the Law of Cosines to prove the Pythagorean Theorem — that's circular. (See Problem 18.39.)

**Execution:**
- **Sign error in Law of Cosines:** It's −2ab cos C. If ∠C is obtuse, cos C is negative, so −2ab cos C becomes positive, making c² > a² + b². This makes geometric sense — the side opposite an obtuse angle is the longest.
- **Forgetting to square root:** Law of Cosines gives c², not c. Don't forget the final step.

### Generalizations & Edge Cases

- When ∠C = 90°: Law of Cosines → Pythagorean Theorem (cos 90° = 0)
- When ∠C = 0° or 180°: degenerate triangle (points collinear)
- Extended Law of Sines: a/sin A = 2R (circumradius). This connects trig to circle geometry — extremely useful in competition math
- The area formula [ABC] = abc/(4R) follows from combining [ABC] = ½ab sin C with the Extended Law of Sines

### Connections

- **Builds on:** Right triangle trig (Section 18.1), unit circle (Section 18.2), Pythagorean Theorem
- **Leads to:** Competition geometry problems combining circles with trig, Extended Law of Sines, Heron's formula connections
- **Related to:** Circumscribed circles (the Extended Law of Sines ties side lengths to circumradius)

---

## Chapter Summary

### All Identities / Theorems in One Place

| Name | Formula | When to Use |
|---|---|---|
| SOHCAHTOA | sin = opp/hyp, cos = adj/hyp, tan = opp/adj | Right triangle with a known angle and side |
| Pythagorean Identity | sin²A + cos²A = 1 | Converting between sin and cos; simplifying expressions |
| Complementary Identity | sin A = cos(90° − A) | Relating sine of one angle to cosine of the other |
| Reflection Identity | sin(180° − θ) = sin θ | Simplifying trig of obtuse angles |
| Area Formula | [ABC] = ½ab sin C | Two sides + included angle → area |
| Law of Cosines | c² = a² + b² − 2ab cos C | SAS → find third side; or SSS → find an angle |
| Law of Sines | a/sin A = b/sin B = c/sin C | AAS/ASA → find other sides; SSA → find angle (with caution) |
| Extended Law of Sines | a/sin A = 2R | Connecting side lengths to circumradius |

### Master Trigger → Technique List

| Trigger | Technique | Section |
|---|---|---|
| Right triangle + angle + side → find another side | SOHCAHTOA | 18.1 |
| 30°, 45°, 60° angle → exact trig value | Draw special right triangle | 18.1 |
| Know sin, need cos (or vice versa) | sin²A + cos²A = 1 | 18.1 |
| Angle of elevation or depression | Build right triangle from horizontal | 18.1 |
| Trig of angle > 90° | Unit circle: find reference angle + quadrant sign | 18.2 |
| Triangle area with two sides + included angle | ½ab sin C | 18.2 |
| Two sides + included angle → third side | Law of Cosines | 18.3 |
| Three sides → angle | Law of Cosines rearranged | 18.3 |
| Two angles + one side → other sides | Law of Sines | 18.3 |
| Side length + circumradius relationship | Extended Law of Sines: a/sin A = 2R | 18.3 |

### Problem-Solving Strategies

- **When stuck, draw an altitude.** Most trig proofs and computations start by constructing a right triangle inside the given figure. This converts a general triangle problem into a right triangle problem where SOHCAHTOA applies.
- **Prove general statements by solving a specific case first.** The Law of Cosines was discovered by solving one specific triangle (Problem 18.19), then replacing the numbers with variables (Problem 18.20). This is a powerful problem-solving pattern.
- **Check formulas against known cases.** After proving the Law of Cosines, plug in your earlier numerical answer to verify. After any derivation, test it on a case you already solved.
- **When choosing between Law of Sines and Law of Cosines**, count what you know: SAS or SSS → Cosines. AAS/ASA → Sines. SSA → Sines, but beware ambiguity.

---

## Self-Test Problems

*Do these using ONLY the notes above. No book, no solutions. If you can do all of them, the notes work. If you can't, we know what to fix.*

**Problem 1** (Section 18.1, Level 1):
> In right triangle △DEF with ∠E = 90°, DE = 5, and DF = 13. Find sin D, cos D, tan D, and verify that sin²D + cos²D = 1.

**Problem 2** (Section 18.2, Level 2):
> Without a calculator, evaluate sin 240°, cos 240°, and tan 240°.

**Problem 3** (Sections 18.1 + 18.2, Level 2):
> Two sides of a triangle are 7 and 10, and the included angle is 120°. Find the area of the triangle. (Exact answer, no calculator.)

**Problem 4** (Section 18.3, competition-level) — *Target: 4 minutes*
> In △ABC, AB = 7, BC = 8, and ∠ABC = 45°. Find AC to the nearest hundredth.

**Problem 5** (Full chapter, competition-level) — *Target: 5 minutes*
> In △PQR, PQ = 10, ∠P = 50°, and ∠Q = 70°. Find PR and QR to the nearest tenth. Then find the area of △PQR to the nearest tenth. (Calculator allowed.)

---

## Self-Test Answers

1. EF = 12, sin D = 12/13, cos D = 5/13, tan D = 12/5. Verification: (12/13)² + (5/13)² = 144/169 + 25/169 = 169/169 = 1. ✓
2. Reference angle = 60°, Quadrant III (both negative). sin 240° = −√3/2, cos 240° = −1/2, tan 240° = √3.
3. Area = ½(7)(10) sin 120° = 35 · (√3/2) = **35√3/2**.
4. AC² = 49 + 64 − 2(7)(8) cos 45° = 113 − 56√2 ≈ 113 − 79.20 ≈ 33.80. AC ≈ **5.81**.
5. ∠R = 60°. By Law of Sines: 10/sin 60° = PR/sin 70° = QR/sin 50°. PR ≈ 10·sin 70°/sin 60° ≈ **10.9**. QR ≈ 10·sin 50°/sin 60° ≈ **8.8**. Area = ½(10)(PR) sin 50° ≈ ½(10)(10.9)(0.766) ≈ **41.7**.
