# Unit 6: Right Triangles & Trigonometry (Honors Geometry)
## Comprehensive Worksheet — Layered Decomposition Protocol

---

## MODULE 1: MODEL EXAMPLES (8-10 Problems)

**Instructions:** Study these worked examples carefully. After each solution, a pattern is noted to help you recognize when and how to apply each technique.

---

### Problem 1.1: Find Hypotenuse Using Pythagorean Theorem

**Problem:** In right triangle ABC with legs a = 5 cm and b = 12 cm, find the hypotenuse c.

**Solution:**
$$c^2 = a^2 + b^2$$
$$c^2 = 5^2 + 12^2$$
$$c^2 = 25 + 144 = 169$$
$$c = 13 \text{ cm}$$

**Pattern observed:** When you know both legs of a right triangle, use $a^2 + b^2 = c^2$ directly. This is a Pythagorean triple: (5, 12, 13).

---

### Problem 1.2: Find a Leg Using Pythagorean Theorem

**Problem:** In right triangle DEF, the hypotenuse is 15 m and one leg is 9 m. Find the other leg.

**Solution:**
$$a^2 + b^2 = c^2$$
$$9^2 + b^2 = 15^2$$
$$81 + b^2 = 225$$
$$b^2 = 144$$
$$b = 12 \text{ m}$$

**Pattern observed:** When you know the hypotenuse and one leg, subtract the known leg squared from the hypotenuse squared. This is also a Pythagorean triple: (9, 12, 15) or 3(3, 4, 5).

---

### Problem 1.3: Identify Pythagorean Triples

**Problem:** Determine which of these are Pythagorean triples:
- (7, 24, 25)
- (5, 6, 7)
- (8, 15, 17)

**Solution:**
- (7, 24, 25): $7^2 + 24^2 = 49 + 576 = 625 = 25^2$ ✓ **YES**
- (5, 6, 7): $5^2 + 6^2 = 25 + 36 = 61 \neq 49 = 7^2$ ✗ **NO**
- (8, 15, 17): $8^2 + 15^2 = 64 + 225 = 289 = 17^2$ ✓ **YES**

**Pattern observed:** Pythagorean triples are sets of three positive integers that satisfy $a^2 + b^2 = c^2$. Common triples include (3, 4, 5), (5, 12, 13), (8, 15, 17), and multiples of these.

---

### Problem 1.4: Use Converse to Classify Triangle

**Problem:** A triangle has sides 6, 8, and 10. Is it a right triangle? If not, is it acute or obtuse?

**Solution:**
Check if $a^2 + b^2 = c^2$ (where c is the longest side):
$$6^2 + 8^2 = 36 + 64 = 100 = 10^2$$ ✓

**This is a right triangle.** (The converse of the Pythagorean theorem tells us that if the equation holds, the triangle must be right.)

**Pattern observed:** Use the converse: if $a^2 + b^2 = c^2$, it's right; if $a^2 + b^2 > c^2$, it's acute; if $a^2 + b^2 < c^2$, it's obtuse.

---

### Problem 1.5: Find Missing Sides in 45-45-90 Triangle

**Problem:** In a 45-45-90 triangle, one leg is 7 inches. Find the hypotenuse.

**Solution:**
In a 45-45-90 triangle, the sides are in the ratio $1 : 1 : \sqrt{2}$ (leg : leg : hypotenuse).

If one leg is 7, then:
- Other leg = 7
- Hypotenuse = $7\sqrt{2}$ inches

**Pattern observed:** In a 45-45-90 triangle, **multiply the leg by $\sqrt{2}$ to get the hypotenuse**. If given the hypotenuse, divide by $\sqrt{2}$ to get the legs.

---

### Problem 1.6: Find Missing Sides in 30-60-90 Triangle

**Problem:** In a 30-60-90 triangle, the short leg (opposite the 30° angle) is 5 cm. Find the long leg and hypotenuse.

**Solution:**
In a 30-60-90 triangle, the sides are in the ratio $1 : \sqrt{3} : 2$ (short leg : long leg : hypotenuse).

If the short leg is 5:
- Short leg = 5
- Long leg = $5\sqrt{3}$ cm
- Hypotenuse = $2(5) = 10$ cm

**Pattern observed:** In a 30-60-90 triangle, **the hypotenuse is twice the short leg**, and **the long leg is $\sqrt{3}$ times the short leg**. Always identify which leg you're given first.

---

### Problem 1.7: Find Trig Ratios (SOH-CAH-TOA)

**Problem:** In right triangle PQR with right angle at Q, PQ = 3, QR = 4, and PR = 5. Find sin P, cos P, and tan P.

**Solution:**
From angle P's perspective:
- Opposite = QR = 4
- Adjacent = PQ = 3
- Hypotenuse = PR = 5

$$\sin P = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{4}{5}$$
$$\cos P = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{3}{5}$$
$$\tan P = \frac{\text{opposite}}{\text{adjacent}} = \frac{4}{3}$$

**Pattern observed:** SOH-CAH-TOA tells you which sides to use relative to the angle you're analyzing. The denominator is always the hypotenuse for sine and cosine; for tangent, it's the adjacent leg.

---

### Problem 1.8: Use Inverse Trig to Find an Angle

**Problem:** In a right triangle, the opposite side to angle A is 7 and the hypotenuse is 10. Find angle A to the nearest degree.

**Solution:**
$$\sin A = \frac{7}{10} = 0.7$$
$$A = \sin^{-1}(0.7) = 44.4° \approx 44°$$

**Pattern observed:** Inverse trig functions ($\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$) undo the trig functions. Use them when you know sides but need to find an angle.

---

## MODULE 2: WEAK THEOREM LADDER (8 Problems)

**Instructions:** Solve each problem. After each one, **trigger extraction** occurs (indicated by a shaded box). This means: pause and extract what you learned, what tool you used, and why it worked.

---

### Problem 2.1: Pythagorean Theorem (Straightforward)

**Problem:** A ladder leans against a wall. The base is 4 feet from the wall, and the ladder is 10 feet long. How high up the wall does the ladder reach?

**Solution:**
Let h = height. The ladder, wall, and ground form a right triangle.
$$4^2 + h^2 = 10^2$$
$$16 + h^2 = 100$$
$$h^2 = 84$$
$$h = \sqrt{84} = 2\sqrt{21} \approx 9.17 \text{ feet}$$

**TRIGGER EXTRACTION:**
- **Tool used:** Pythagorean theorem
- **Why it worked:** We have two sides of a right triangle and need the third.
- **Key insight:** Always identify the hypotenuse (longest side, opposite the right angle).

---

### Problem 2.2: Special Right Triangle with Algebra

**Problem:** In a 45-45-90 triangle, the hypotenuse is 14 cm. Find the length of each leg.

**Solution:**
In a 45-45-90 triangle, if legs = x, then hypotenuse = $x\sqrt{2}$.
$$x\sqrt{2} = 14$$
$$x = \frac{14}{\sqrt{2}} = \frac{14\sqrt{2}}{2} = 7\sqrt{2} \text{ cm}$$

**TRIGGER EXTRACTION:**
- **Tool used:** 45-45-90 triangle ratio
- **Why it worked:** This triangle has a fixed ratio, so knowing one side lets you find all others.
- **Key insight:** Rationalize denominators: multiply by $\frac{\sqrt{2}}{\sqrt{2}}$.

---

### Problem 2.3: SOH-CAH-TOA to Find a Missing Side

**Problem:** In right triangle ABC with right angle at C, angle A = 35°, and the adjacent side AC = 8 cm. Find the opposite side BC.

**Solution:**
$$\tan A = \frac{\text{opposite}}{\text{adjacent}}$$
$$\tan 35° = \frac{BC}{8}$$
$$BC = 8 \tan 35° = 8(0.7002) \approx 5.60 \text{ cm}$$

**TRIGGER EXTRACTION:**
- **Tool used:** Tangent ratio
- **Why it worked:** We knew the adjacent side and angle, needed the opposite side. Tangent uses only these two.
- **Key insight:** Identify which sides you know and which you need, then choose the trig ratio that connects them.

---

### Problem 2.4: Inverse Trig to Find a Missing Angle

**Problem:** A ramp rises 3 feet over a horizontal distance of 8 feet. What angle does the ramp make with the ground?

**Solution:**
$$\tan \theta = \frac{\text{rise}}{\text{run}} = \frac{3}{8}$$
$$\theta = \tan^{-1}\left(\frac{3}{8}\right) = \tan^{-1}(0.375) \approx 20.6°$$

**TRIGGER EXTRACTION:**
- **Tool used:** Inverse tangent
- **Why it worked:** We had a ratio of sides and needed the angle.
- **Key insight:** The angle of inclination is found using inverse trig when you know side ratios.

---

### Problem 2.5: Angle of Elevation/Depression Word Problem

**Problem:** A person stands 50 meters from the base of a building. Looking at the top of the building, their angle of elevation is 32°. How tall is the building?

**Solution:**
The horizontal distance is the adjacent side. The height is the opposite side.
$$\tan 32° = \frac{\text{height}}{50}$$
$$\text{height} = 50 \tan 32° = 50(0.6249) \approx 31.2 \text{ meters}$$

**TRIGGER EXTRACTION:**
- **Tool used:** Angle of elevation with tangent
- **Why it worked:** The angle of elevation is measured from the horizontal up to the line of sight.
- **Key insight:** Angle of elevation/depression problems are just right triangles in real-world contexts.

---

### Problem 2.6: Area Using ½ab sin C

**Problem:** In triangle XYZ, sides XY = 8 cm, XZ = 6 cm, and the angle between them (angle X) is 50°. Find the area.

**Solution:**
$$\text{Area} = \frac{1}{2} ab \sin C$$
$$\text{Area} = \frac{1}{2}(8)(6) \sin 50°$$
$$\text{Area} = 24 \sin 50° = 24(0.766) \approx 18.4 \text{ cm}^2$$

**TRIGGER EXTRACTION:**
- **Tool used:** Area formula with sine
- **Why it worked:** We had two sides and the included angle, but NOT a right angle. This formula generalizes area beyond right triangles.
- **Key insight:** This works for ANY triangle (not just right triangles) when you know two sides and their included angle.

---

### Problem 2.7: Law of Sines (AAS Case)

**Problem:** In triangle DEF, angle D = 40°, angle E = 65°, and side DE = 10 units (opposite angle F). Find side DF (opposite angle E).

**Solution:**
First, find angle F:
$$\angle F = 180° - 40° - 65° = 75°$$

Use Law of Sines:
$$\frac{DE}{\sin F} = \frac{DF}{\sin E}$$
$$\frac{10}{\sin 75°} = \frac{DF}{\sin 65°}$$
$$DF = \frac{10 \sin 65°}{\sin 75°} = \frac{10(0.906)}{0.966} \approx 9.38 \text{ units}$$

**TRIGGER EXTRACTION:**
- **Tool used:** Law of Sines
- **Why it worked:** We had AAS (two angles and a side opposite one of them).
- **Key insight:** Law of Sines is a proportion: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$.

---

### Problem 2.8: Law of Cosines (SAS Case) — Peak of Ladder

**Problem:** In triangle ABC, side AB = 7 cm, side AC = 5 cm, and angle A = 55°. Find side BC.

**Solution:**
$$BC^2 = AB^2 + AC^2 - 2(AB)(AC)\cos A$$
$$BC^2 = 7^2 + 5^2 - 2(7)(5)\cos 55°$$
$$BC^2 = 49 + 25 - 70(0.574)$$
$$BC^2 = 74 - 40.18 = 33.82$$
$$BC \approx 5.82 \text{ cm}$$

**TRIGGER EXTRACTION:**
- **Tool used:** Law of Cosines
- **Why it worked:** We had SAS (two sides and the included angle). Law of Cosines is the generalization of Pythagorean theorem to non-right triangles.
- **Key insight:** When you have sides and the angle between them (but it's not a right angle), Law of Cosines is your tool.

---

## MODULE 3: BARRIER INVENTORY (5 Traps)

**Instructions:** Below are five common mistakes students make. Read each, understand why it's wrong, and practice avoiding it.

---

### Trap 1: Using Pythagorean Theorem When It's NOT a Right Triangle

**The Trap:**
Student sees a triangle problem and automatically reaches for $a^2 + b^2 = c^2$ without checking if the triangle is actually a right triangle.

**Why It's Wrong:**
The Pythagorean theorem **only applies to right triangles**. If the triangle doesn't have a 90° angle, the formula is invalid.

**How to Avoid It:**
- **Always check:** Is there a right angle marked, or is one side explicitly called the hypotenuse?
- **If unsure:** Use Law of Cosines instead. It works for ANY triangle.
- **Red flag:** If you're given two sides and an angle that's NOT 90° and NOT between those sides, you probably need Law of Sines or Cosines, not Pythagorean theorem.

**Example of the Error:**
"Triangle has sides 5, 6, and 7. Using Pythagorean theorem: $5^2 + 6^2 = 25 + 36 = 61 \neq 49 = 7^2$, so... error?"
→ **No!** This triangle is NOT right. You can't use Pythagorean theorem. Use the converse to classify it: since $5^2 + 6^2 > 7^2$, it's acute.

---

### Trap 2: Special Right Triangles — Multiplying the Wrong Side

**The Trap:**
In a 45-45-90 or 30-60-90 triangle, multiplying the hypotenuse by the ratio instead of the correct leg, or vice versa.

**Why It's Wrong:**
Each ratio is tied to a specific side. 45-45-90 has ratio $1 : 1 : \sqrt{2}$ (leg : leg : hyp). If you're given a leg and multiply by $\sqrt{2}$, you get the hypotenuse. But if you're given the hypotenuse and multiply by $\sqrt{2}$, you get the WRONG answer.

**How to Avoid It:**
- **45-45-90:** If leg = x, then hypotenuse = $x\sqrt{2}$. If hypotenuse = y, then leg = $\frac{y}{\sqrt{2}}$.
- **30-60-90:** If short leg = x, then long leg = $x\sqrt{3}$ and hypotenuse = $2x$. Always start from the SHORT leg.
- **Key:** Identify which side you're given, then follow the chain.

**Example of the Error:**
"In a 45-45-90 triangle, the hypotenuse is 10. So each leg is $10\sqrt{2}$?"
→ **No!** $10\sqrt{2} \approx 14.14$, which is larger than 10. Legs must be smaller than the hypotenuse. Correct: leg = $\frac{10}{\sqrt{2}} = 5\sqrt{2} \approx 7.07$.

---

### Trap 3: SOH-CAH-TOA — Misidentifying Opposite vs Adjacent

**The Trap:**
Mixing up which side is opposite and which is adjacent relative to the angle you're using.

**Why It's Wrong:**
"Opposite" and "adjacent" depend entirely on which angle you're analyzing. From angle A, one side is opposite; from angle B, that same side is adjacent.

**How to Avoid It:**
- **Always ask:** Relative to which angle am I working?
- **Opposite:** The side that does NOT touch the angle you're using.
- **Adjacent:** The side that DOES touch the angle (but is NOT the hypotenuse).
- **Draw a picture.** Label the angle, mark opposite and adjacent with different colors.

**Example of the Error:**
In right triangle ABC with right angle at C, if you're finding sin A, don't use side AC as "opposite." AC is adjacent to angle A. The opposite side is BC.

---

### Trap 4: Confusing Angle of Elevation vs Angle of Depression

**The Trap:**
Treating the angle as if it's always measured from the top, or forgetting that elevation and depression are measured differently.

**Why It's Wrong:**
- **Angle of elevation:** Measured UP from the horizontal line of sight.
- **Angle of depression:** Measured DOWN from the horizontal line of sight.
These create different triangles and different solutions if you mess up which angle you're using.

**How to Avoid It:**
- **Draw the situation:** Person looking up → angle of elevation. Person looking down → angle of depression.
- **Horizontal is key:** The horizontal always forms one side of your right triangle.
- **Memo:** "E-levation = up, D-epression = down."

**Example of the Error:**
"A person on a 40-foot cliff looks down at a boat with angle of depression 25°. Distance to boat?"
→ Right setup: horizontal leg = distance, vertical leg = 40. $\tan 25° = \frac{40}{\text{distance}}$, so distance $= \frac{40}{\tan 25°} \approx 85.8$ feet.
→ Wrong setup: Using $\tan 25° = \frac{\text{distance}}{40}$ gives the opposite answer.

---

### Trap 5: Law of Sines vs Law of Cosines — Using the Wrong Law

**The Trap:**
Blindly applying one law when the other is needed, based on habit or misremembering when each applies.

**Why It's Wrong:**
- **Law of Sines** requires an angle-opposite-side pair and at least one other side. It works for AAS, ASA, SSA.
- **Law of Cosines** requires two sides and the included angle (SAS) or all three sides (SSS).
Using the wrong law gives wrong answers or fails entirely.

**How to Avoid It:**
Use this **decision tree:**
1. Do you have **two angles and any side**? → Law of Sines.
2. Do you have **two sides and the angle BETWEEN them**? → Law of Cosines.
3. Do you have **all three sides**? → Law of Cosines (to find an angle).
4. Do you have **two sides and an angle NOT between them**? → Law of Sines (check for ambiguous case).

**Example of the Error:**
"Sides a = 5, b = 7, angle C = 50°. Find c."
→ Angle C is BETWEEN sides a and b, so use **Law of Cosines**: $c^2 = a^2 + b^2 - 2ab\cos C$.
→ Wrong: Using Law of Sines leads to a dead end because you don't have an angle-opposite pair.

---

## MODULE 4: REPRESENTATION SWITCHES (4-5 Problems)

**Instructions:** Each problem shows two different methods to solve the same problem. Understand both, then decide which is more efficient for each context.

---

### Problem 4.1: Special Right Triangle Ratios vs Trig Ratios

**Scenario:** In a 30-60-90 triangle, the short leg is 6 cm. Find the hypotenuse without a calculator.

**Method A: Special Right Triangle Ratios**
$$\text{Ratio: } 1 : \sqrt{3} : 2$$
$$\text{Short leg} = 6 \Rightarrow \text{Hypotenuse} = 2 \times 6 = 12 \text{ cm}$$

**Method B: Trig Ratios**
The angle opposite the short leg is 30°.
$$\sin 30° = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{6}{h}$$
$$0.5 = \frac{6}{h}$$
$$h = 12 \text{ cm}$$

**Why Method A is Better Here:**
Faster and requires no calculator. The fixed ratios are memorized.

**Why Method B is Useful:**
If you forget the ratio, you can derive it using sine of 30°.

**Key Insight:**
Both arrive at the same answer. Special triangles are *special* because their trig values are nice (30° sin = 0.5, 45° sin = $\frac{\sqrt{2}}{2}$, etc.).

---

### Problem 4.2: Law of Cosines (Algebraic) vs Breaking into Right Triangles

**Scenario:** Find the area of a triangle with sides a = 8, b = 6, c = 7 (all sides known, SSS).

**Method A: Law of Cosines + Area Formula**

First, find an angle using Law of Cosines:
$$c^2 = a^2 + b^2 - 2ab\cos C$$
$$49 = 64 + 36 - 2(8)(6)\cos C$$
$$49 = 100 - 96\cos C$$
$$\cos C = \frac{51}{96} = 0.531$$

Now use area formula:
$$\text{Area} = \frac{1}{2}ab\sin C$$

Since $\cos C = 0.531$, find $\sin C = \sqrt{1 - 0.531^2} = \sqrt{0.718} \approx 0.848$.
$$\text{Area} = \frac{1}{2}(8)(6)(0.848) \approx 20.4 \text{ cm}^2$$

**Method B: Drop an Altitude to Create Right Triangles**

Drop a perpendicular from angle C to side c, creating height h. Let the perpendicular hit c at point P, dividing c into segments x and (7-x).

From the two right triangles:
$$h^2 + x^2 = 8^2 = 64$$
$$h^2 + (7-x)^2 = 6^2 = 36$$

Subtract the second from the first:
$$x^2 - (7-x)^2 = 28$$
$$x^2 - (49 - 14x + x^2) = 28$$
$$14x - 49 = 28$$
$$x = 5.5$$

Then $h^2 = 64 - 30.25 = 33.75$, so $h = 5.81$.
$$\text{Area} = \frac{1}{2} \times 7 \times 5.81 \approx 20.3 \text{ cm}^2$$

**Why Each Method Works:**
- **Method A:** Direct and systematic. Works for any triangle.
- **Method B:** Leverages right triangles. More geometric and visual.

**Key Insight:**
Both methods work. Method A is faster once you're comfortable with inverse trig. Method B is more concrete and avoids inverse trig.

---

### Problem 4.3: Angles of Elevation — Pure Trig vs Similar Triangles

**Scenario:** A 30-foot tree casts a 40-foot shadow. What is the angle of elevation of the sun?

**Method A: Pure Trig (Direct)**
$$\tan \theta = \frac{\text{height}}{\text{shadow}} = \frac{30}{40} = 0.75$$
$$\theta = \tan^{-1}(0.75) \approx 36.9°$$

**Method B: Similar Triangles (Indirect)**
The sun's rays form angle θ with the ground. If we imagine the sun's ray as the hypotenuse of a right triangle (tree height = 30, shadow = 40), the angle at the far end of the shadow equals the sun's angle.

By properties of similar triangles, the angle of elevation equals the angle in the triangle with legs 30 and 40:
$$\tan \theta = \frac{30}{40}$$
$$\theta \approx 36.9°$$

**Why Method A is More Direct:**
Fewer steps; recognizes "angle of elevation" as a standard setup.

**Why Method B Builds Understanding:**
Shows *why* the ratio works: similar triangles guarantee proportional sides and equal angles.

**Key Insight:**
Angle of elevation problems are applications of similar triangles and trig working together.

---

### Problem 4.4: Ambiguous Case (SSA)

**Scenario:** In triangle ABC, side a = 10, side b = 12, angle A = 40°. Find angle B.

**Method A: Law of Sines**
$$\frac{a}{\sin A} = \frac{b}{\sin B}$$
$$\frac{10}{\sin 40°} = \frac{12}{\sin B}$$
$$\sin B = \frac{12 \sin 40°}{10} = \frac{12(0.643)}{10} = 0.771$$

Now, $B = \sin^{-1}(0.771) = 50.5°$ OR $B = 180° - 50.5° = 129.5°$.

**Two valid triangles exist!** (Ambiguous case.)

**Method B: Check Feasibility with Altitude**

The altitude from C to side c has height $h = b \sin A = 12 \sin 40° = 7.71$.

- If $a < h$, no triangle.
- If $a = h$, one right triangle.
- If $h < a < b$, two triangles (ambiguous).
- If $a \geq b$, one triangle.

Here, $h = 7.71 < a = 10 < b = 12$, so two triangles exist.

**Why Method A is Computational:**
Gives exact angle values.

**Why Method B is Conceptual:**
Shows *why* ambiguity occurs: multiple angles have the same sine.

**Key Insight:**
SSA (side-side-angle where the angle is NOT between the sides) can yield zero, one, or two solutions. Always check!

---

## MODULE 5: TRIGGER EXTRACTION (6-8 Exam Problems)

**Instructions:** Solve each problem, then **extract the decision process** (shown in a box after each). These are mixed problems covering all of Unit 6. Use the decision tree provided.

---

### Decision Tree for Unit 6

```
START: What information do you have?

├─ RIGHT TRIANGLE?
│  ├─ YES, two sides given
│  │  └─ Use Pythagorean Theorem or trig ratios (SOH-CAH-TOA)
│  └─ YES, one side and one angle given
│     └─ Use trig ratios (SOH-CAH-TOA) or inverse trig
│
├─ NOT RIGHT, but two angles and a side given (AAS, ASA, or SAA)
│  └─ Use Law of Sines
│
├─ NOT RIGHT, but two sides and included angle given (SAS)
│  └─ Use Law of Cosines
│
└─ NOT RIGHT, but all three sides given (SSS)
   └─ Use Law of Cosines to find an angle
```

---

### Problem 5.1: Right Triangle, Two Sides

**Problem:** A right triangle has legs 9 and 12. Find the hypotenuse and one of the acute angles.

**Solution:**

*Hypotenuse:*
$$c = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15$$

*Angle opposite the leg of length 9:*
$$\sin \theta = \frac{9}{15} = 0.6$$
$$\theta = \sin^{-1}(0.6) \approx 36.9°$$

**EXTRACTION:**
- **Decision:** Right triangle, two legs given → Pythagorean theorem + SOH-CAH-TOA.
- **Tools:** Pythagorean theorem, then inverse sine.
- **Why this works:** Legs are known, so we can compute the hypotenuse and then trig ratios.

---

### Problem 5.2: Right Triangle, Angle and One Side

**Problem:** In a right triangle, one acute angle is 25° and the opposite side is 8 cm. Find the hypotenuse and the adjacent side.

**Solution:**

*Hypotenuse:*
$$\sin 25° = \frac{8}{h}$$
$$h = \frac{8}{\sin 25°} = \frac{8}{0.423} \approx 18.9 \text{ cm}$$

*Adjacent side:*
$$\tan 25° = \frac{8}{a}$$
$$a = \frac{8}{\tan 25°} = \frac{8}{0.466} \approx 17.2 \text{ cm}$$

**EXTRACTION:**
- **Decision:** Right triangle, angle and one side given → Inverse trig or direct trig.
- **Tools:** Sine and tangent.
- **Why this works:** Angle and opposite side determine everything; we use trig ratios to find unknowns.

---

### Problem 5.3: Special Right Triangle (45-45-90)

**Problem:** In a 45-45-90 triangle, the hypotenuse is $8\sqrt{2}$ meters. Find the legs.

**Solution:**

Using the ratio $1 : 1 : \sqrt{2}$:
$$\text{leg} = \frac{8\sqrt{2}}{\sqrt{2}} = 8 \text{ meters}$$

Both legs are 8 meters.

**EXTRACTION:**
- **Decision:** 45-45-90 triangle, hypotenuse given.
- **Tools:** Memorized ratio.
- **Why this works:** Hypotenuse is $\sqrt{2}$ times a leg, so divide by $\sqrt{2}$.

---

### Problem 5.4: Not Right, Two Angles and a Side (AAS)

**Problem:** In triangle XYZ, angle X = 30°, angle Y = 100°, and side XY = 20 units. Find side YZ.

**Solution:**

First, angle Z:
$$Z = 180° - 30° - 100° = 50°$$

Side XY is opposite angle Z. Side YZ is opposite angle X.
$$\frac{XY}{\sin Z} = \frac{YZ}{\sin X}$$
$$\frac{20}{\sin 50°} = \frac{YZ}{\sin 30°}$$
$$YZ = \frac{20 \sin 30°}{\sin 50°} = \frac{20(0.5)}{0.766} \approx 13.0 \text{ units}$$

**EXTRACTION:**
- **Decision:** Not right, two angles and a side given (AAS).
- **Tools:** Law of Sines.
- **Why this works:** We have angle-opposite pairs, which Law of Sines directly uses.

---

### Problem 5.5: Not Right, Two Sides and Included Angle (SAS)

**Problem:** In triangle ABC, side AB = 11, side AC = 7, angle A = 65°. Find side BC.

**Solution:**
$$BC^2 = AB^2 + AC^2 - 2(AB)(AC)\cos A$$
$$BC^2 = 121 + 49 - 2(11)(7)\cos 65°$$
$$BC^2 = 170 - 154(0.423) = 170 - 65.1 = 104.9$$
$$BC \approx 10.2$$

**EXTRACTION:**
- **Decision:** Not right, two sides and included angle (SAS).
- **Tools:** Law of Cosines.
- **Why this works:** We have the two sides and the angle between them. Law of Cosines generalizes Pythagorean theorem.

---

### Problem 5.6: Not Right, All Three Sides (SSS)

**Problem:** In triangle DEF, side d = 5, side e = 6, side f = 8. Find angle F (opposite side f).

**Solution:**
$$f^2 = d^2 + e^2 - 2de\cos F$$
$$64 = 25 + 36 - 2(5)(6)\cos F$$
$$64 = 61 - 60\cos F$$
$$\cos F = -\frac{3}{60} = -0.05$$
$$F = \cos^{-1}(-0.05) \approx 92.9°$$

The triangle is obtuse (angle F is greater than 90°).

**EXTRACTION:**
- **Decision:** Not right, all three sides given (SSS).
- **Tools:** Law of Cosines.
- **Why this works:** With all sides known, we can find angles using Law of Cosines rearranged.

---

### Problem 5.7: Angle of Elevation Word Problem

**Problem:** From a point on the ground 100 meters from a building, the angle of elevation to the roof is 35°. What is the height of the building?

**Solution:**
$$\tan 35° = \frac{h}{100}$$
$$h = 100 \tan 35° = 100(0.700) = 70 \text{ meters}$$

**EXTRACTION:**
- **Decision:** Right triangle (formed by observer, building, ground), angle of elevation, and horizontal distance given.
- **Tools:** Tangent.
- **Why this works:** Angle of elevation and horizontal distance set up a right triangle where tangent applies directly.

---

### Problem 5.8: Determine Missing Info and Solve

**Problem:** In triangle PQR, angle P = 50°, angle Q = 60°, and side PQ = 15 units. Find the area of the triangle.

**Solution:**

First, angle R:
$$R = 180° - 50° - 60° = 70°$$

Using Law of Sines to find side QR (opposite angle P):
$$\frac{PQ}{\sin R} = \frac{QR}{\sin P}$$
$$\frac{15}{\sin 70°} = \frac{QR}{\sin 50°}$$
$$QR = \frac{15 \sin 50°}{\sin 70°} = \frac{15(0.766)}{0.940} \approx 12.2 \text{ units}$$

Now use area formula with two sides and included angle:
$$\text{Area} = \frac{1}{2}(PQ)(QR) \sin Q$$
$$\text{Area} = \frac{1}{2}(15)(12.2) \sin 60°$$
$$\text{Area} = \frac{1}{2}(15)(12.2)(0.866) \approx 79.2 \text{ square units}$$

**EXTRACTION:**
- **Decision:** Two angles and a side given. Use Law of Sines to find another side. Then use area formula.
- **Tools:** Law of Sines, then area formula.
- **Why this works:** We need to convert the given information into "two sides + included angle" to apply the area formula.

---

## MODULE 6: CANDIDATE ATTACK CHALLENGE (2-3 Hard Problems)

**Instructions:** These problems combine multiple concepts and require strategic tool selection. Work through each step-by-step.

---

### Challenge Problem 1: Find Area, Then Use It in a Volume Context

**Problem:**
A tent is shaped like a triangular prism. The triangular cross-section has sides 10 feet, 8 feet, and 12 feet. The prism extends 20 feet in length.
(a) Find the area of the triangular face.
(b) Find the volume of the tent.

**Solution:**

*Part (a): Area of the triangular cross-section*

Using Heron's formula (since we have all three sides):
$$s = \frac{10 + 8 + 12}{2} = 15$$
$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$$
$$\text{Area} = \sqrt{15(15-10)(15-8)(15-12)}$$
$$\text{Area} = \sqrt{15 \times 5 \times 7 \times 3}$$
$$\text{Area} = \sqrt{1575} \approx 39.7 \text{ square feet}$$

**Alternative using Law of Cosines:**

Find an angle first. Using sides a=10, b=8, c=12:
$$c^2 = a^2 + b^2 - 2ab\cos C$$
$$144 = 100 + 64 - 160\cos C$$
$$\cos C = -\frac{20}{160} = -0.125$$
$$\sin C = \sqrt{1 - 0.0156} \approx 0.992$$
$$\text{Area} = \frac{1}{2}(10)(8)(0.992) \approx 39.7 \text{ square feet}$$

*Part (b): Volume of the tent*
$$\text{Volume} = \text{(Base Area)} \times \text{(Length)}$$
$$\text{Volume} = 39.7 \times 20 = 794 \text{ cubic feet}$$

**DECISION PROCESS:**
1. Recognize: Three sides given (SSS) → need area.
2. Choose method: Heron's formula OR Law of Cosines + area formula.
3. Once area found, multiply by length for volume.
4. This combines geometry (triangle area) with spatial reasoning (prism volume).

---

### Challenge Problem 2: Navigation / Bearing Problem

**Problem:**
A boat leaves port A and travels 40 kilometers on a bearing of 050° (50° east of north). It then turns and travels 30 kilometers on a bearing of 130° (50° east of south). How far is the boat from port A? What is its bearing from port A?

**Solution:**

*Set up a coordinate system:* North is the positive y-axis; East is the positive x-axis.

*Leg 1: 40 km at bearing 050°*
- Change in x: $40 \sin 50° = 40(0.766) = 30.64$ km (east)
- Change in y: $40 \cos 50° = 40(0.643) = 25.72$ km (north)
- Position after leg 1: $(30.64, 25.72)$

*Leg 2: 30 km at bearing 130°*
From the current position, bearing 130° is 40° south of east.
- Change in x: $30 \sin 130° = 30(0.766) = 22.98$ km (east)
- Change in y: $30 \cos 130° = 30(-0.643) = -19.29$ km (south)
- Position after leg 2: $(30.64 + 22.98, 25.72 - 19.29) = (53.62, 6.43)$

*Distance from port A:*
$$d = \sqrt{53.62^2 + 6.43^2} = \sqrt{2874.91 + 41.34} = \sqrt{2916.25} \approx 54.0 \text{ km}$$

*Bearing from port A:*
$$\tan \theta = \frac{53.62}{6.43} = 8.33$$
$$\theta = \tan^{-1}(8.33) \approx 83.1°$$

So the bearing is approximately 083° (83° east of north), or equivalently, $6.43$ km north and $53.62$ km east.

**DECISION PROCESS:**
1. Translate bearings into coordinates using sine and cosine.
2. Add component-wise to find final position.
3. Use distance formula to find displacement.
4. Use inverse tangent to find bearing angle.
5. This combines trigonometry (bearing conversion) with vectors (addition) and spatial reasoning.

---

### Challenge Problem 3: Bridge Construction Problem

**Problem:**
Engineers need to find the width of a river to design a bridge. From point A on one bank, they measure 300 meters along the bank to point B. From A, the angle to a marker C on the opposite bank is 50°. From B, the angle to C is 35°. Find the width of the river (the perpendicular distance from C to line AB).

**Solution:**

*Set up: A and B are on one bank, 300 meters apart. C is across the river.*
- Angle CAB = 50°
- Angle CBA = 35°
- Side AB = 300 meters

First, find angle ACB:
$$\angle ACB = 180° - 50° - 35° = 95°$$

Using Law of Sines to find AC:
$$\frac{AB}{\sin(\angle ACB)} = \frac{AC}{\sin(\angle ABC)}$$
$$\frac{300}{\sin 95°} = \frac{AC}{\sin 35°}$$
$$AC = \frac{300 \sin 35°}{\sin 95°} = \frac{300(0.574)}{0.996} \approx 172.9 \text{ meters}$$

Now, the width of the river is the height of triangle ABC dropped from C perpendicular to AB. Using the area formula:
$$\text{Area of triangle ABC} = \frac{1}{2}(AB)(h)$$

where h is the width.

Also:
$$\text{Area} = \frac{1}{2}(AC)(AB) \sin(\angle CAB)$$
$$\text{Area} = \frac{1}{2}(172.9)(300) \sin 50°$$
$$\text{Area} = \frac{1}{2}(172.9)(300)(0.766) \approx 19,864 \text{ square meters}$$

So:
$$19,864 = \frac{1}{2}(300)(h)$$
$$h = \frac{2 \times 19,864}{300} = \frac{39,728}{300} \approx 132.4 \text{ meters}$$

**DECISION PROCESS:**
1. Recognize: Two angles and a side given (AAS) → Law of Sines to find another side.
2. Use area formula (½ab sin C) to find the area of the triangle.
3. Relate area to the perpendicular distance (width).
4. This combines Law of Sines, area formulas, and geometric reasoning about height.

---

## INTUITIVE EXPLANATIONS & FULL SOLUTIONS

This section provides detailed walkthroughs of every problem, explaining not just the "what" but the "why."

---

### Why the Pythagorean Theorem Works (Module 1, Problem 1.1)

The Pythagorean theorem ($a^2 + b^2 = c^2$) arises from the geometry of right triangles. Imagine a right triangle with legs a and b and hypotenuse c.

**Visual Proof Idea:** If you construct squares on each side:
- Square on side a has area $a^2$.
- Square on side b has area $b^2$.
- Square on side c has area $c^2$.

The magic: **the area of the two smaller squares exactly equals the area of the largest square**. This is because of how the angles align in a right triangle.

**For Problem 1.1:**
- Legs: 5 and 12
- Hypotenuse: $\sqrt{5^2 + 12^2} = \sqrt{169} = 13$

Why 13? Because 13 is the side length of a square with area 169, which is exactly the sum of areas 25 and 144.

---

### Understanding 45-45-90 Triangles (Module 1, Problem 1.5)

A 45-45-90 triangle is **isosceles** (two equal angles means two equal sides). Both legs are the same length.

If each leg is x, then by Pythagorean theorem:
$$c = \sqrt{x^2 + x^2} = \sqrt{2x^2} = x\sqrt{2}$$

So the ratio is $x : x : x\sqrt{2}$, or simplified: $1 : 1 : \sqrt{2}$.

**Mnemonic:** "In a 45-45-90 triangle, if the leg is 1, the hypotenuse is $\sqrt{2}$."

**For Problem 1.5:**
- Leg = 7
- Hypotenuse = $7\sqrt{2}$ (multiply by $\sqrt{2}$)

---

### Understanding 30-60-90 Triangles (Module 1, Problem 1.6)

A 30-60-90 triangle is **half of an equilateral triangle**. Here's how:

Start with an equilateral triangle with all sides = 2.
- Drop a perpendicular from one vertex to the opposite side.
- This perpendicular bisects the base, creating two 30-60-90 triangles.
- Each has hypotenuse 2, short leg (half the base) = 1, and height = $\sqrt{3}$.

So the ratio is $1 : \sqrt{3} : 2$ (short leg : long leg : hypotenuse).

**Mnemonic:** "30-60-90 has sides 1, $\sqrt{3}$, 2. The side opposite 30° is shortest. The side opposite 60° is $\sqrt{3}$ times that."

**For Problem 1.6:**
- Short leg (opposite 30°) = 5
- Long leg (opposite 60°) = $5\sqrt{3}$
- Hypotenuse (opposite 90°) = 10

---

### SOH-CAH-TOA in Depth (Module 1, Problem 1.7)

**SOH-CAH-TOA** is a mnemonic for three basic trig ratios:

- **S**ine = **O**pposite / **H**ypotenuse
- **C**osine = **A**djacent / **H**ypotenuse
- **T**angent = **O**pposite / **A**djacent

The key insight: These ratios depend on the *angle* you're analyzing.

**For Problem 1.7:**
In right triangle PQR, angle at Q is 90°. We're analyzing angle P.
- Opposite (does NOT touch P, but touches the right angle) = QR = 4
- Adjacent (touches P, but is NOT the hypotenuse) = PQ = 3
- Hypotenuse (opposite the right angle) = PR = 5

So:
- $\sin P = 4/5$ (opposite over hypotenuse)
- $\cos P = 3/5$ (adjacent over hypotenuse)
- $\tan P = 4/3$ (opposite over adjacent)

**Why this matters:** If you were analyzing angle R instead:
- Opposite to R = PQ = 3
- Adjacent to R = QR = 4
- So $\sin R = 3/5$, which is different from $\sin P$!

Always specify which angle you're using.

---

### Inverse Trig Functions (Module 1, Problem 1.8)

Inverse trig functions **undo** the regular trig functions.

If $\sin A = 0.7$, then $A = \sin^{-1}(0.7)$ means "the angle whose sine is 0.7."

**For Problem 1.8:**
- $\sin A = 7/10 = 0.7$
- $A = \sin^{-1}(0.7) \approx 44.4°$

On a calculator, this is usually the [INV] or [2nd] button followed by [SIN].

**Caution:** Inverse sine, cosine, and tangent have **restricted ranges**:
- $\sin^{-1}$ gives angles from -90° to 90°
- $\cos^{-1}$ gives angles from 0° to 180°
- $\tan^{-1}$ gives angles from -90° to 90°

So if the angle you're looking for is obtuse (> 90°), you may need to adjust using $180° - \sin^{-1}(x)$.

---

### Law of Sines (Module 2, Problem 2.7)

The **Law of Sines** says that in ANY triangle:
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

where a, b, c are sides and A, B, C are the opposite angles.

**Why it works:** This ratio is actually related to the circumradius (radius of the circle passing through all three vertices). But the practical takeaway is:

"If you know an angle and the side opposite it, you can find any other side if you also know its opposite angle."

**For Problem 2.7:**
- Angle D = 40°, side DE = 10 (opposite angle F)
- Angle E = 65°, side DF = ? (opposite angle E)
- Find angle F = 180° - 40° - 65° = 75°

Then:
$$\frac{DE}{\sin F} = \frac{DF}{\sin E}$$
$$\frac{10}{\sin 75°} = \frac{DF}{\sin 65°}$$
$$DF = 10 \cdot \frac{\sin 65°}{\sin 75°} \approx 9.38$$

The key is identifying the angle-opposite-side pairs.

---

### Law of Cosines (Module 2, Problem 2.8)

The **Law of Cosines** generalizes the Pythagorean theorem:
$$c^2 = a^2 + b^2 - 2ab \cos C$$

When C = 90°, $\cos 90° = 0$, so this reduces to $c^2 = a^2 + b^2$ (the Pythagorean theorem).

**Why it works:** It accounts for the "angle effect." If the angle between sides a and b is acute (< 90°), the cosine is positive, and the side c is shorter than Pythagorean would suggest. If the angle is obtuse (> 90°), the cosine is negative, and c is longer.

**For Problem 2.8:**
- Sides AB = 7, AC = 5, angle A = 55°
- Find BC:

$$BC^2 = 7^2 + 5^2 - 2(7)(5) \cos 55°$$
$$BC^2 = 49 + 25 - 70(0.574)$$
$$BC^2 = 74 - 40.18 = 33.82$$
$$BC \approx 5.82$$

Note: If angle A were 90°, we'd get $BC = \sqrt{49 + 25} = \sqrt{74} \approx 8.60$, which is larger. The 55° angle "pulls" B and C closer together, so BC is shorter.

---

### Angle of Elevation and Depression (Module 2, Problem 2.5)

**Angle of elevation:** The angle above the horizontal when looking up at something.
**Angle of depression:** The angle below the horizontal when looking down at something.

These are always measured from the horizontal.

**For Problem 2.5:**
- Person on ground, building height h meters away.
- Horizontal distance = 50 meters.
- Angle of elevation = 32° (looking up from horizontal).

The right triangle has:
- Horizontal leg = 50
- Vertical leg = h
- Angle between them (at the person) = 32°

From the person's perspective, the building height is the *opposite* side.
$$\tan 32° = \frac{h}{50}$$
$$h = 50 \tan 32° \approx 31.2 \text{ meters}$$

**Common mistake:** Confusing which angle is which. If the problem said "angle of depression from the top of the building to the person is 32°," it's the same angle (by alternate interior angles with parallel lines), but measured from the opposite direction.

---

### Area Formula with Sine (Module 2, Problem 2.6)

For a right triangle, area = ½ × base × height. But what if the triangle isn't right?

**General formula:** Area = ½ab sin C, where a and b are two sides and C is the angle between them.

**Why it works:** The "height" perpendicular to side a is $b \sin C$ (from the geometry of the right triangle formed by the perpendicular). So:
$$\text{Area} = \frac{1}{2} a (b \sin C) = \frac{1}{2} ab \sin C$$

**For Problem 2.6:**
- Sides XY = 8, XZ = 6, angle X = 50°
- Area = ½(8)(6) sin 50° = 24(0.766) ≈ 18.4 cm²

This works for ANY triangle, not just right triangles.

---

### Heron's Formula (Module 6, Challenge 1)

When you have all three sides (SSS) but the triangle isn't right, you can find the area using **Heron's formula**:
$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$$
where $s = \frac{a+b+c}{2}$ (the semi-perimeter).

**Why it works:** It's derived using the Law of Cosines behind the scenes, but it avoids needing to find an angle explicitly.

**For Challenge 1:**
- Sides: 10, 8, 12
- $s = (10+8+12)/2 = 15$
- Area = $\sqrt{15 \cdot 5 \cdot 7 \cdot 3} = \sqrt{1575} \approx 39.7$ square feet

---

### Bearings and Navigation (Module 6, Challenge 2)

A **bearing** is an angle measured clockwise from north.
- Bearing 050° = 50° east of north
- Bearing 130° = 50° east of south (or equivalently, 40° south of east)
- Bearing 270° = due west

**Converting to Cartesian coordinates:**
- North direction = positive y-axis
- East direction = positive x-axis

For a bearing θ and distance d:
- Change in x = d sin θ (east component)
- Change in y = d cos θ (north component)

**For Challenge 2:**
- Leg 1: 40 km at bearing 050°
  - Δx = 40 sin 50° ≈ 30.64, Δy = 40 cos 50° ≈ 25.72
  - Position: (30.64, 25.72)
- Leg 2: 30 km at bearing 130°
  - Δx = 30 sin 130° ≈ 22.98, Δy = 30 cos 130° ≈ -19.29
  - Position: (30.64 + 22.98, 25.72 - 19.29) = (53.62, 6.43)

Distance from origin: $\sqrt{53.62^2 + 6.43^2} \approx 54.0$ km.

---

### Ambiguous Case: SSA (Module 4, Problem 4.4)

When you have **two sides and an angle NOT between them** (SSA), there can be 0, 1, or 2 solutions.

**The issue:** Given sides a, b and angle A (opposite side a), the Law of Sines gives:
$$\sin B = \frac{b \sin A}{a}$$

But sine is not one-to-one: both θ and (180° - θ) have the same sine value. So there might be two valid angles B.

**Checking for ambiguity:**
The altitude from C to side c has height $h = b \sin A$.
- If $a < h$: no triangle (side a is too short to reach the opposite side).
- If $a = h$: one right triangle.
- If $h < a < b$: two triangles (ambiguous).
- If $a \geq b$: one triangle.

**For Problem 4.4:**
- $a = 10$, $b = 12$, $A = 40°$
- $h = 12 \sin 40° \approx 7.71$
- Since $7.71 < 10 < 12$, two triangles exist.

---

### Choosing Between Law of Sines and Law of Cosines

**Law of Sines** works when:
- You have an angle-opposite-side pair AND another angle or side.
- Cases: AAS, ASA, SAA (all two angles + one side), or SSA (ambiguous).

**Law of Cosines** works when:
- You have SAS (two sides + included angle).
- You have SSS (all three sides) and need an angle.

**Decision tree (repeated for emphasis):**
1. **Right triangle?** Use Pythagorean theorem or SOH-CAH-TOA.
2. **Two angles + any side?** Law of Sines.
3. **Two sides + included angle?** Law of Cosines.
4. **All three sides?** Law of Cosines.

---

### Practical Problem-Solving Strategy

When you encounter a triangle problem:

1. **Draw a picture.** Label all known sides and angles.
2. **Identify what you know:** How many sides? How many angles? Which sides are opposite which angles?
3. **Identify what you need:** A side? An angle? An area?
4. **Consult the decision tree:** Choose Pythagorean theorem, SOH-CAH-TOA, Law of Sines, or Law of Cosines.
5. **Solve step-by-step.** Write out the formula and substitute values.
6. **Check reasonableness:** Is the answer in the right ballpark? (Areas shouldn't be huge; sides shouldn't be negative.)

---

### Why Special Right Triangles Matter

Special right triangles (45-45-90 and 30-60-90) appear constantly in geometry and physics.

**45-45-90:** Shows up in squares, diagonals of squares, and anywhere symmetry is involved.

**30-60-90:** Shows up in hexagons, equilateral triangles, and many physical systems.

Because their side ratios involve only simple numbers and $\sqrt{2}$ or $\sqrt{3}$, they're easier to work with than arbitrary triangles. Memorizing the ratios lets you solve many problems without a calculator.

---

## FINAL NOTES

This worksheet covers the full span of Unit 6: Right Triangles & Trigonometry. The six modules build from understanding to application:

- **Module 1** teaches the basic tools and patterns.
- **Module 2** applies them in a carefully scaffolded sequence.
- **Module 3** guards against common pitfalls.
- **Module 4** shows flexibility by solving the same problem multiple ways.
- **Module 5** is exam-style: mixed problems requiring tool selection.
- **Module 6** challenges you with multi-step, real-world scenarios.

Throughout, the **Layered Decomposition Protocol** ensures that you're not just getting answers, but understanding *why* each method works and *when* to use it.

**Next steps:**
- Attempt each problem on your own first.
- Check your answers against the solutions.
- If stuck, read the "intuitive explanation" to understand the reasoning.
- Revisit the traps in Module 3 if you find yourself making those mistakes.

Good luck!
