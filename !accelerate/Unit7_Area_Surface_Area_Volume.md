# Unit 7: Area, Surface Area, and Volume
## Honors Geometry - Comprehensive Study Notes

---

## Table of Contents
1. [Introduction & Building Blocks](#introduction--building-blocks)
2. [Area of 2D Shapes](#area-of-2d-shapes)
3. [Area Using Coordinates](#area-using-coordinates)
4. [Circles: Circumference, Arc Length & Sector Area](#circles-circumference-arc-length--sector-area)
5. [Surface Area of 3D Solids](#surface-area-of-3d-solids)
6. [Volume of 3D Solids](#volume-of-3d-solids)
7. [Cavalieri's Principle](#cavalieris-principle)
8. [Real-World Applications: Density & Displacement](#real-world-applications-density--displacement)
9. [Modeling Real Objects](#modeling-real-objects)
10. [Common Mistakes & Exam Tips](#common-mistakes--exam-tips)

---

## Introduction & Building Blocks

### What is Area?

**Plain English Definition:** Area is the amount of space contained inside a 2D (flat) shape, measured in square units.

Think of it this way: if you have a room and you want to know how much carpet you need to cover the floor, you're calculating area. The carpet covers the *inside* of the room.

**Key Vocabulary:**
- **Area (A)**: The measure of interior space in a 2D figure
- **Square units**: The measurement (cm², m², inches², etc.)
- **Base (b)**: Often the bottom side of a shape, but can be any side
- **Height (h)**: The perpendicular distance from the base to the opposite side
- **Perpendicular**: Meeting at a 90° angle

### What is Surface Area?

**Plain English Definition:** Surface area is the total area of all the outer faces/surfaces of a 3D (solid) object.

Imagine wrapping a box with wrapping paper. The amount of paper you need is the surface area. You're covering the *outside* of the object.

**Key Vocabulary:**
- **Surface Area (SA)**: The sum of areas of all faces of a 3D solid
- **Base (B)**: Often the bottom face, but can refer to any principal face
- **Lateral surface area**: The area of the sides only (not including bases)
- **Slant height (l)**: The distance along a slanted surface from apex to base edge

### What is Volume?

**Plain English Definition:** Volume is the amount of 3D space contained *inside* a solid object, measured in cubic units.

Imagine filling a box with water. The amount of water it holds is its volume. You're measuring how much *stuff* can fit inside.

**Key Vocabulary:**
- **Volume (V)**: The measure of 3D space inside a solid
- **Cubic units**: The measurement (cm³, m³, inches³, etc.)
- **Cross-section**: A slice through a solid perpendicular to a specific direction

### The Relationship Between 2D and 3D

- **2D shapes** (rectangle, triangle, circle) have *area*
- **3D solids** (box, pyramid, sphere) have *surface area* (the outside) and *volume* (the inside)
- To find surface area, you often calculate the area of 2D shapes that make up the solid's faces

---

## Area of 2D Shapes

### Rectangle

**Definition:** A quadrilateral with four right angles and opposite sides equal.

**Formula:**
$$A = lw$$

Where:
- $A$ = area (in square units)
- $l$ = length (longer side)
- $w$ = width (shorter side)

**Why it works:** Imagine a rectangle 5 units long and 3 units wide. You can arrange 5 × 3 = 15 unit squares inside it.

**Worked Examples:**

**Example 1:** Find the area of a rectangle with length 8 cm and width 5 cm.
- Given: $l = 8$ cm, $w = 5$ cm
- Substitute: $A = 8 \times 5$
- Calculate: $A = 40$ cm²

**Example 2:** A rectangular garden is 12 meters long and 7 meters wide. How much grass seed is needed to cover it?
- Given: $l = 12$ m, $w = 7$ m
- Substitute: $A = 12 \times 7$
- Calculate: $A = 84$ m²
- Answer: 84 m² of grass seed is needed

**Example 3:** A rectangle has area 72 square inches and length 9 inches. Find the width.
- Given: $A = 72$ in², $l = 9$ in
- Formula: $A = lw$ → $72 = 9w$
- Solve: $w = 72 ÷ 9 = 8$ inches

---

### Parallelogram

**Definition:** A quadrilateral with opposite sides parallel and equal in length. Opposite angles are also equal.

**Key Concept:** A parallelogram is like a "slanted rectangle." The height is NOT the side length—it's the perpendicular distance between parallel sides.

**Formula:**
$$A = bh$$

Where:
- $A$ = area (in square units)
- $b$ = base (any side you choose as the base)
- $h$ = perpendicular height (the perpendicular distance from base to the opposite side)

**Why it works:** If you cut off the triangular slanted part on one end and move it to the other end, you create a rectangle with the same area. This rectangle has dimensions $b × h$.

**Worked Examples:**

**Example 1:** Find the area of a parallelogram with base 10 cm and height 6 cm.
- Given: $b = 10$ cm, $h = 6$ cm
- Substitute: $A = 10 \times 6$
- Calculate: $A = 60$ cm²

**Example 2:** A parallelogram has side length 8 meters, but the height is only 5 meters. What is its area?
- Given: $b = 8$ m, $h = 5$ m (note: we use height, not the slanted side)
- Substitute: $A = 8 \times 5$
- Calculate: $A = 40$ m²

**Example 3:** A parallelogram has area 120 square units and base 15 units. Find the height.
- Given: $A = 120$, $b = 15$
- Formula: $A = bh$ → $120 = 15h$
- Solve: $h = 120 ÷ 15 = 8$ units

**Common Mistake:** Students sometimes use the slanted side as the height. Remember: height must be perpendicular to the base!

---

### Triangle

**Definition:** A three-sided polygon. The area formula works for any triangle.

**Formula:**
$$A = \frac{1}{2}bh$$

Where:
- $A$ = area (in square units)
- $b$ = base (any side)
- $h$ = perpendicular height (from the base to the opposite vertex)

**Why it works:** Any triangle is exactly half of a parallelogram. If you duplicate a triangle and flip it, you create a parallelogram. So triangle area = ½ × base × height.

**Worked Examples:**

**Example 1:** Find the area of a triangle with base 12 cm and height 8 cm.
- Given: $b = 12$ cm, $h = 8$ cm
- Substitute: $A = \frac{1}{2} \times 12 \times 8$
- Calculate: $A = \frac{1}{2} \times 96 = 48$ cm²

**Example 2:** A triangular sail has base 6 feet and height 9 feet. What is its area?
- Given: $b = 6$ ft, $h = 9$ ft
- Substitute: $A = \frac{1}{2} \times 6 \times 9$
- Calculate: $A = \frac{1}{2} \times 54 = 27$ ft²

**Example 3:** A triangle has area 50 square meters and base 10 meters. Find the height.
- Given: $A = 50$ m², $b = 10$ m
- Formula: $A = \frac{1}{2}bh$ → $50 = \frac{1}{2}(10)h$
- Simplify: $50 = 5h$
- Solve: $h = 50 ÷ 5 = 10$ meters

**Common Mistake:** Don't forget the ½! A triangle is half a parallelogram, so you must multiply by ½.

---

### Trapezoid

**Definition:** A quadrilateral with exactly one pair of parallel sides. The parallel sides are called bases.

**Formula:**
$$A = \frac{1}{2}(b_1 + b_2)h$$

Where:
- $A$ = area
- $b_1$ = length of first parallel base
- $b_2$ = length of second parallel base
- $h$ = perpendicular height (distance between the parallel sides)

**Why it works:** A trapezoid is the average of two parallelograms. The two parallel sides have different lengths, so we average them: $\frac{b_1 + b_2}{2}$, then multiply by height.

**Worked Examples:**

**Example 1:** Find the area of a trapezoid with parallel sides of 5 cm and 9 cm, and height 4 cm.
- Given: $b_1 = 5$ cm, $b_2 = 9$ cm, $h = 4$ cm
- Substitute: $A = \frac{1}{2}(5 + 9) \times 4$
- Simplify: $A = \frac{1}{2}(14) \times 4 = 7 \times 4$
- Calculate: $A = 28$ cm²

**Example 2:** A trapezoid has bases of 12 meters and 18 meters, with height 8 meters. Find its area.
- Given: $b_1 = 12$ m, $b_2 = 18$ m, $h = 8$ m
- Substitute: $A = \frac{1}{2}(12 + 18) \times 8$
- Simplify: $A = \frac{1}{2}(30) \times 8 = 15 \times 8$
- Calculate: $A = 120$ m²

**Example 3:** A trapezoid has area 50 square units, one base of 6 units, and height 5 units. Find the other base.
- Given: $A = 50$, $b_1 = 6$, $h = 5$
- Formula: $50 = \frac{1}{2}(6 + b_2) \times 5$
- Simplify: $50 = \frac{5}{2}(6 + b_2)$
- Multiply both sides by $\frac{2}{5}$: $20 = 6 + b_2$
- Solve: $b_2 = 14$ units

---

### Rhombus and Kite

**Definition:**
- **Rhombus:** A parallelogram with all four sides equal length
- **Kite:** A quadrilateral with two pairs of consecutive equal sides

Both use the same area formula based on diagonals.

**Formula:**
$$A = \frac{1}{2}d_1 d_2$$

Where:
- $A$ = area
- $d_1$ = length of diagonal 1
- $d_2$ = length of diagonal 2

**Why it works:** The two diagonals of a rhombus or kite are perpendicular and split the shape into 4 triangles. Together, they create a rectangle of area $d_1 × d_2$, and the shape occupies half that area.

**Worked Examples:**

**Example 1:** Find the area of a rhombus with diagonals 10 cm and 8 cm.
- Given: $d_1 = 10$ cm, $d_2 = 8$ cm
- Substitute: $A = \frac{1}{2} \times 10 \times 8$
- Calculate: $A = \frac{1}{2} \times 80 = 40$ cm²

**Example 2:** A kite has diagonals of 12 inches and 9 inches. What is its area?
- Given: $d_1 = 12$ in, $d_2 = 9$ in
- Substitute: $A = \frac{1}{2} \times 12 \times 9$
- Calculate: $A = \frac{1}{2} \times 108 = 54$ in²

**Example 3:** A rhombus has area 120 square meters and one diagonal of 15 meters. Find the other diagonal.
- Given: $A = 120$ m², $d_1 = 15$ m
- Formula: $120 = \frac{1}{2} \times 15 \times d_2$
- Simplify: $120 = 7.5 d_2$
- Solve: $d_2 = 120 ÷ 7.5 = 16$ meters

---

### Regular Polygon

**Definition:** A polygon with all sides equal and all angles equal.

**Key Concept:** An apothem is the perpendicular distance from the center of the polygon to the midpoint of any side.

**Formula:**
$$A = \frac{1}{2}ap$$

Where:
- $A$ = area
- $a$ = apothem (perpendicular distance from center to side)
- $p$ = perimeter (sum of all side lengths)

**Why it works:** If you draw lines from the center to each vertex, you divide the polygon into congruent triangles. Each triangle has base = side length and height = apothem. The total area is the sum of all triangles.

**Worked Examples:**

**Example 1:** Find the area of a regular hexagon with apothem 5 cm and side length 6 cm.
- Given: $a = 5$ cm, side = 6 cm
- Find perimeter: $p = 6 \times 6 = 36$ cm (hexagon has 6 sides)
- Substitute: $A = \frac{1}{2} \times 5 \times 36$
- Calculate: $A = \frac{1}{2} \times 180 = 90$ cm²

**Example 2:** A regular pentagon has apothem 4 inches and side length 5.8 inches. Find its area.
- Given: $a = 4$ in, side = 5.8 in
- Find perimeter: $p = 5 \times 5.8 = 29$ in (pentagon has 5 sides)
- Substitute: $A = \frac{1}{2} \times 4 \times 29$
- Calculate: $A = \frac{1}{2} \times 116 = 58$ in²

**Example 3:** A regular octagon has area 200 square units and apothem 8 units. Find the perimeter.
- Given: $A = 200$, $a = 8$
- Formula: $200 = \frac{1}{2} \times 8 \times p$
- Simplify: $200 = 4p$
- Solve: $p = 50$ units
- Each side: $50 ÷ 8 = 6.25$ units

---

### Circle

**Definition:** The set of all points equidistant from a center point.

**Key Vocabulary:**
- **Radius (r):** Distance from center to edge
- **Diameter (d):** Distance across through the center; $d = 2r$

**Formula:**
$$A = \pi r^2$$

Where:
- $A$ = area
- $r$ = radius
- $\pi ≈ 3.14159...$

**Why it works:** Imagine cutting a circle into many thin triangular slices. As you make more slices, they approximate a rectangle. The "width" becomes the circumference ($2\pi r$) and the "height" becomes the radius. Rectangle area = $2\pi r × r ÷ 2 = \pi r^2$.

**Worked Examples:**

**Example 1:** Find the area of a circle with radius 5 cm.
- Given: $r = 5$ cm
- Substitute: $A = \pi \times 5^2$
- Calculate: $A = \pi \times 25 = 25\pi$ cm² (or $≈78.54$ cm²)

**Example 2:** A circular pizza has diameter 14 inches. What is its area?
- Given: $d = 14$ inches, so $r = 7$ inches
- Substitute: $A = \pi \times 7^2$
- Calculate: $A = 49\pi$ in² (or $≈153.94$ in²)

**Example 3:** A circular garden has area $100\pi$ m². Find its radius.
- Given: $A = 100\pi$ m²
- Formula: $100\pi = \pi r^2$
- Divide by $\pi$: $100 = r^2$
- Take square root: $r = 10$ meters

---

## Area of Composite Figures

**Definition:** A composite (or compound) figure is made up of two or more simple shapes combined together.

**Strategy:** Break the composite figure into simpler shapes (rectangles, triangles, circles, etc.), find the area of each, then add or subtract as needed.

**When to subtract:** If you have a shape with a hole or cutout, find the area of the whole shape, then subtract the hole.

**Worked Examples:**

**Example 1:** An L-shaped figure can be split into two rectangles. Find the total area.

```
      5 cm
   |---------|
   |         |    3 cm
   |    A    |-------|
   |         |       |
   |---------|       |
   |         |       |
   |    B    |   C   | 5 cm
   |         |       |
   |---------|-------|
      8 cm      3 cm
```

Rectangle A: 5 cm × 3 cm = 15 cm²
Rectangle B: 5 cm × (5-3) cm = 5 × 2 = 10 cm² (or use full 8×5 = 40, then subtract upper right part)

**Better approach:** Split into two rectangles differently:
- Left rectangle: 5 cm × 5 cm = 25 cm²
- Right rectangle: 3 cm × 2 cm = 6 cm²
- Total area = 25 + 6 = 31 cm²

**Example 2:** A rectangle with a circular hole cut out. Rectangle is 10 cm × 8 cm, and the hole is a circle with radius 2 cm.
- Area of rectangle: $10 \times 8 = 80$ cm²
- Area of circle (hole): $\pi \times 2^2 = 4\pi ≈ 12.57$ cm²
- Area of composite: $80 - 4\pi ≈ 67.43$ cm²

**Example 3:** A house shape (rectangle with triangular roof).
- Rectangle base: 12 m × 8 m = 96 m²
- Triangle roof: base 12 m, height 4 m → $\frac{1}{2} \times 12 \times 4 = 24$ m²
- Total area: 96 + 24 = 120 m²

**Common Mistake:** Don't forget to break the shape into non-overlapping pieces. Use a marker or pencil to actually draw the divisions before calculating.

---

## Area Using Coordinates

### The Coordinate Plane Review

On a coordinate plane, each point is labeled $(x, y)$:
- $x$ = horizontal position (left/right)
- $y$ = vertical position (up/down)

To find the area of a polygon given its vertices (corner points), we use the **Shoelace Formula**.

### The Shoelace Formula

**Definition:** A method to find the area of a polygon when you know the coordinates of all vertices.

**Formula for a polygon with vertices $(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)$ listed in order:**

$$A = \frac{1}{2} |x_1(y_2 - y_n) + x_2(y_3 - y_1) + x_3(y_4 - y_2) + ... + x_n(y_1 - y_{n-1})|$$

**Or equivalently (the determinant method):**

$$A = \frac{1}{2} |(x_1 y_2 - x_2 y_1) + (x_2 y_3 - x_3 y_2) + ... + (x_n y_1 - x_1 y_n)|$$

**Why it works:** The formula calculates the area by using the x and y coordinates. The absolute value ensures the answer is positive.

### Step-by-Step Process

1. List all vertices in order (going around the polygon, either clockwise or counterclockwise)
2. Write each vertex as an ordered pair
3. Apply the shoelace formula
4. Take the absolute value
5. Divide by 2

### Worked Examples

**Example 1:** Find the area of a triangle with vertices at $A(0, 0)$, $B(4, 0)$, and $C(2, 3)$.

Method: Use the shoelace formula.
- Vertices in order: $(0, 0)$, $(4, 0)$, $(2, 3)$
- Formula: $A = \frac{1}{2} |(x_1 y_2 - x_2 y_1) + (x_2 y_3 - x_3 y_2) + (x_3 y_1 - x_1 y_3)|$
- Substitute: $A = \frac{1}{2} |(0 \cdot 0 - 4 \cdot 0) + (4 \cdot 3 - 2 \cdot 0) + (2 \cdot 0 - 0 \cdot 3)|$
- Simplify: $A = \frac{1}{2} |0 + 12 + 0|$
- Calculate: $A = \frac{1}{2} \times 12 = 6$ square units

**Verification:** Using the triangle formula with base 4 and height 3: $A = \frac{1}{2} \times 4 \times 3 = 6$ ✓

**Example 2:** Find the area of a quadrilateral with vertices at $P(0, 0)$, $Q(5, 0)$, $R(5, 3)$, and $S(0, 3)$.

This is a rectangle! But let's use the formula.
- Vertices in order: $(0, 0)$, $(5, 0)$, $(5, 3)$, $(0, 3)$
- Formula: $A = \frac{1}{2} |(x_1 y_2 - x_2 y_1) + (x_2 y_3 - x_3 y_2) + (x_3 y_4 - x_4 y_3) + (x_4 y_1 - x_1 y_4)|$
- Substitute: $A = \frac{1}{2} |(0 \cdot 0 - 5 \cdot 0) + (5 \cdot 3 - 5 \cdot 0) + (5 \cdot 3 - 0 \cdot 3) + (0 \cdot 0 - 0 \cdot 3)|$
- Simplify: $A = \frac{1}{2} |0 + 15 + 15 + 0|$
- Calculate: $A = \frac{1}{2} \times 30 = 15$ square units

**Verification:** This is a 5 × 3 rectangle, so area = 5 × 3 = 15 ✓

**Example 3:** Find the area of a trapezoid with vertices at $A(1, 1)$, $B(5, 1)$, $C(6, 4)$, and $D(0, 4)$.

- Vertices in order: $(1, 1)$, $(5, 1)$, $(6, 4)$, $(0, 4)$
- Apply formula: $A = \frac{1}{2} |(1 \cdot 1 - 5 \cdot 1) + (5 \cdot 4 - 6 \cdot 1) + (6 \cdot 4 - 0 \cdot 4) + (0 \cdot 1 - 1 \cdot 4)|$
- Simplify: $A = \frac{1}{2} |(1 - 5) + (20 - 6) + (24 - 0) + (0 - 4)|$
- Simplify: $A = \frac{1}{2} |(-4) + 14 + 24 + (-4)|$
- Calculate: $A = \frac{1}{2} \times 30 = 15$ square units

---

## Circles: Circumference, Arc Length & Sector Area

### Circumference

**Definition:** The perimeter of a circle; the distance around the circle.

**Formula:**
$$C = 2\pi r = \pi d$$

Where:
- $C$ = circumference
- $r$ = radius
- $d$ = diameter
- $\pi ≈ 3.14159...$

**Why it works:** The circumference is always approximately 3.14159 times the diameter. This ratio is $\pi$.

**Worked Examples:**

**Example 1:** Find the circumference of a circle with radius 7 cm.
- Given: $r = 7$ cm
- Substitute: $C = 2\pi \times 7$
- Calculate: $C = 14\pi$ cm (or $≈43.98$ cm)

**Example 2:** A wheel has diameter 2 meters. What is its circumference?
- Given: $d = 2$ m
- Substitute: $C = \pi \times 2$
- Calculate: $C = 2\pi$ m (or $≈6.28$ m)

**Example 3:** A circular track has circumference 400 meters. Find its radius.
- Given: $C = 400$ m
- Formula: $400 = 2\pi r$
- Divide by $2\pi$: $r = \frac{400}{2\pi} = \frac{200}{\pi} ≈ 63.66$ meters

---

### Arc Length

**Definition:** The length of a portion of the circumference (part of the circle's edge).

**Key Concept:** An arc is measured by its central angle (the angle at the center of the circle).

**Formula:**
$$\text{Arc Length} = \frac{\theta}{360°} \times 2\pi r = \frac{\theta}{360°} \times C$$

Where:
- $\theta$ = central angle (in degrees)
- $r$ = radius
- $C$ = circumference

**Alternative formula (in radians):**
$$\text{Arc Length} = \theta \times r$$
(where $\theta$ is in radians)

**Why it works:** An arc is a fraction of the full circumference. If the central angle is $\theta°$ out of 360°, then the arc is $\frac{\theta}{360}$ of the full circle.

**Worked Examples:**

**Example 1:** Find the arc length of a sector with central angle 60° and radius 10 cm.
- Given: $\theta = 60°$, $r = 10$ cm
- Substitute: Arc Length $= \frac{60°}{360°} \times 2\pi \times 10$
- Simplify: Arc Length $= \frac{1}{6} \times 20\pi = \frac{20\pi}{6} = \frac{10\pi}{3}$ cm
- Calculate: Arc Length $≈ 10.47$ cm

**Example 2:** A circle has radius 5 inches and an arc with central angle 90°. Find the arc length.
- Given: $\theta = 90°$, $r = 5$ in
- Substitute: Arc Length $= \frac{90°}{360°} \times 2\pi \times 5$
- Simplify: Arc Length $= \frac{1}{4} \times 10\pi = 2.5\pi$ in
- Calculate: Arc Length $≈ 7.85$ in

**Example 3:** An arc has length $4\pi$ meters and is part of a circle with radius 12 meters. Find the central angle.
- Given: Arc Length $= 4\pi$ m, $r = 12$ m
- Formula: $4\pi = \frac{\theta}{360°} \times 2\pi \times 12$
- Simplify: $4\pi = \frac{\theta}{360°} \times 24\pi$
- Divide by $\pi$: $4 = \frac{\theta}{360°} \times 24$
- Multiply by 360 and divide by 24: $\theta = \frac{4 \times 360°}{24} = \frac{1440°}{24} = 60°$

---

### Sector Area

**Definition:** A sector is a "pie slice" of a circle—the region between two radii and the arc connecting them.

**Formula:**
$$\text{Sector Area} = \frac{\theta}{360°} \times \pi r^2$$

Where:
- $\theta$ = central angle (in degrees)
- $r$ = radius

**Why it works:** A sector is a fraction of the full circle. If the angle is $\theta°$ out of 360°, the sector area is $\frac{\theta}{360}$ of the full circle's area ($\pi r^2$).

**Worked Examples:**

**Example 1:** Find the area of a sector with central angle 90° and radius 6 cm.
- Given: $\theta = 90°$, $r = 6$ cm
- Substitute: Sector Area $= \frac{90°}{360°} \times \pi \times 6^2$
- Simplify: Sector Area $= \frac{1}{4} \times 36\pi = 9\pi$ cm²
- Calculate: Sector Area $≈ 28.27$ cm²

**Example 2:** A pizza slice has radius 8 inches and central angle 45°. What is the area of the slice?
- Given: $\theta = 45°$, $r = 8$ in
- Substitute: Sector Area $= \frac{45°}{360°} \times \pi \times 8^2$
- Simplify: Sector Area $= \frac{1}{8} \times 64\pi = 8\pi$ in²
- Calculate: Sector Area $≈ 25.13$ in²

**Example 3:** A sector has area $10\pi$ square meters and is part of a circle with radius 10 meters. Find the central angle.
- Given: Sector Area $= 10\pi$ m², $r = 10$ m
- Formula: $10\pi = \frac{\theta}{360°} \times \pi \times 10^2$
- Simplify: $10\pi = \frac{\theta}{360°} \times 100\pi$
- Divide by $\pi$: $10 = \frac{\theta}{360°} \times 100$
- Divide by 100 and multiply by 360: $\theta = \frac{10 \times 360°}{100} = 36°$

---

## Surface Area of 3D Solids

### Prism

**Definition:** A 3D solid with two parallel, congruent bases connected by rectangular faces.

**Types:** Rectangular prism (box), triangular prism, pentagonal prism, etc.

**Key Concept:** The surface area includes the two bases plus all the lateral (side) faces.

**Formula:**
$$SA = 2B + Ph$$

Where:
- $SA$ = surface area
- $B$ = area of one base
- $P$ = perimeter of the base
- $h$ = height of the prism (distance between the bases)

**Breaking it down:**
- $2B$ = area of the two bases
- $Ph$ = lateral surface area (the rectangular sides)

**Worked Examples:**

**Example 1:** Find the surface area of a rectangular prism with length 5 cm, width 3 cm, and height 4 cm.
- Base area: $B = 5 \times 3 = 15$ cm²
- Base perimeter: $P = 2(5 + 3) = 16$ cm
- Height: $h = 4$ cm
- Substitute: $SA = 2(15) + 16(4) = 30 + 64 = 94$ cm²

**Example 2:** A triangular prism has a triangular base with area 12 m² and perimeter 12 m. The height of the prism is 8 m. Find its surface area.
- Base area: $B = 12$ m²
- Base perimeter: $P = 12$ m
- Height: $h = 8$ m
- Substitute: $SA = 2(12) + 12(8) = 24 + 96 = 120$ m²

**Example 3:** A prism has surface area 500 square units, base area 50 square units, and height 10 units. Find the base perimeter.
- Given: $SA = 500$, $B = 50$, $h = 10$
- Formula: $500 = 2(50) + P(10)$
- Simplify: $500 = 100 + 10P$
- Solve: $10P = 400$, so $P = 40$ units

---

### Cylinder

**Definition:** A 3D solid with two parallel, congruent circular bases connected by a curved lateral surface.

**Key Concept:** Imagine unrolling the curved side—it becomes a rectangle with width = circumference and height = cylinder height.

**Formula:**
$$SA = 2\pi r^2 + 2\pi rh$$

Where:
- $SA$ = surface area
- $r$ = radius of the circular base
- $h$ = height of the cylinder

**Breaking it down:**
- $2\pi r^2$ = area of the two circular bases
- $2\pi rh$ = lateral (curved) surface area

**Why it works:**
- Each circular base has area $\pi r^2$, and there are two of them
- The lateral surface is a rectangle: width = circumference = $2\pi r$, height = $h$
- Rectangle area = $2\pi r \times h = 2\pi rh$

**Worked Examples:**

**Example 1:** Find the surface area of a cylinder with radius 4 cm and height 10 cm.
- Substitute: $SA = 2\pi(4)^2 + 2\pi(4)(10)$
- Simplify: $SA = 2\pi(16) + 2\pi(40) = 32\pi + 80\pi = 112\pi$ cm²
- Calculate: $SA ≈ 351.86$ cm²

**Example 2:** A soup can has radius 3 inches and height 5 inches. What is its surface area?
- Substitute: $SA = 2\pi(3)^2 + 2\pi(3)(5)$
- Simplify: $SA = 2\pi(9) + 2\pi(15) = 18\pi + 30\pi = 48\pi$ in²
- Calculate: $SA ≈ 150.80$ in²

**Example 3:** A cylinder has surface area $100\pi$ m² and radius 5 m. Find its height.
- Given: $SA = 100\pi$, $r = 5$
- Formula: $100\pi = 2\pi(5)^2 + 2\pi(5)h$
- Simplify: $100\pi = 50\pi + 10\pi h$
- Subtract: $50\pi = 10\pi h$
- Divide: $h = 5$ meters

---

### Pyramid

**Definition:** A 3D solid with a polygonal base and triangular faces that meet at a point (apex).

**Key Concept:** All the triangular faces are congruent isosceles triangles (same size and shape) if the pyramid is regular.

**Key Vocabulary:**
- **Slant height (l):** The distance from the apex to the midpoint of a base edge, measured along a triangular face

**Formula:**
$$SA = B + \frac{1}{2}Pl$$

Where:
- $SA$ = surface area
- $B$ = area of the base
- $P$ = perimeter of the base
- $l$ = slant height

**Breaking it down:**
- $B$ = area of the base
- $\frac{1}{2}Pl$ = lateral surface area (sum of all triangular faces)

**Why it works:** Each triangular face has base = side length and height = slant height. If there are $n$ sides, the sum of all triangular areas is $\frac{1}{2} \times (\text{perimeter}) \times (\text{slant height})$.

**Worked Examples:**

**Example 1:** Find the surface area of a square pyramid with base side length 6 cm and slant height 8 cm.
- Base area: $B = 6 \times 6 = 36$ cm²
- Base perimeter: $P = 4 \times 6 = 24$ cm
- Slant height: $l = 8$ cm
- Substitute: $SA = 36 + \frac{1}{2}(24)(8) = 36 + 96 = 132$ cm²

**Example 2:** A triangular pyramid (tetrahedron) has a triangular base with area 20 m² and perimeter 15 m. The slant height is 12 m. Find the surface area.
- Base area: $B = 20$ m²
- Base perimeter: $P = 15$ m
- Slant height: $l = 12$ m
- Substitute: $SA = 20 + \frac{1}{2}(15)(12) = 20 + 90 = 110$ m²

**Example 3:** A square pyramid has surface area 200 square units, base area 64 square units. If the base side is 8 units, find the slant height.
- Given: $SA = 200$, $B = 64$, base side = 8 units
- Base perimeter: $P = 4 \times 8 = 32$ units
- Formula: $200 = 64 + \frac{1}{2}(32)l$
- Simplify: $200 = 64 + 16l$
- Solve: $16l = 136$, so $l = 8.5$ units

**Important Note:** Don't confuse slant height with perpendicular height! The perpendicular height goes straight up from the center of the base to the apex. The slant height goes along the triangular face.

---

### Cone

**Definition:** A 3D solid with a circular base and a curved lateral surface that comes to a point (apex).

**Key Vocabulary:**
- **Slant height (l):** The distance from the apex to a point on the edge of the base, measured along the lateral surface

**Formula:**
$$SA = \pi r^2 + \pi rl$$

Where:
- $SA$ = surface area
- $r$ = radius of the base
- $l$ = slant height

**Breaking it down:**
- $\pi r^2$ = area of the circular base
- $\pi rl$ = lateral (curved) surface area

**Why it works:** The lateral surface, when unrolled, becomes a sector of a circle with radius = slant height and arc length = circumference = $2\pi r$. The area is $\frac{1}{2} \times \text{arc length} \times \text{radius} = \frac{1}{2} \times 2\pi r \times l = \pi rl$.

**Worked Examples:**

**Example 1:** Find the surface area of a cone with radius 3 cm and slant height 10 cm.
- Substitute: $SA = \pi(3)^2 + \pi(3)(10)$
- Simplify: $SA = 9\pi + 30\pi = 39\pi$ cm²
- Calculate: $SA ≈ 122.52$ cm²

**Example 2:** An ice cream cone has radius 2 inches and slant height 8 inches. What is its lateral surface area (not including the base)?
- Lateral area: $\pi rl = \pi(2)(8) = 16\pi$ in²
- Calculate: $≈ 50.27$ in²

**Example 3:** A cone has surface area $50\pi$ m² and base radius 5 m. Find the slant height.
- Given: $SA = 50\pi$, $r = 5$
- Formula: $50\pi = \pi(5)^2 + \pi(5)l$
- Simplify: $50\pi = 25\pi + 5\pi l$
- Subtract: $25\pi = 5\pi l$
- Divide: $l = 5$ meters

**Important Note:** To find the perpendicular height (not slant height) from a cone, use the Pythagorean theorem: $l^2 = h^2 + r^2$.

---

### Sphere

**Definition:** A 3D solid that is perfectly round; all points on the surface are equidistant from the center.

**Key Vocabulary:**
- **Radius (r):** Distance from center to any point on the surface

**Formula:**
$$SA = 4\pi r^2$$

Where:
- $SA$ = surface area
- $r$ = radius

**Why it works:** The surface area of a sphere is exactly 4 times the area of a great circle (a circle on the sphere with the same radius).

**Worked Examples:**

**Example 1:** Find the surface area of a sphere with radius 6 cm.
- Substitute: $SA = 4\pi(6)^2$
- Simplify: $SA = 4\pi(36) = 144\pi$ cm²
- Calculate: $SA ≈ 452.39$ cm²

**Example 2:** A basketball has radius 4.7 inches. What is its surface area?
- Substitute: $SA = 4\pi(4.7)^2$
- Simplify: $SA = 4\pi(22.09) = 88.36\pi$ in²
- Calculate: $SA ≈ 277.59$ in²

**Example 3:** A sphere has surface area $100\pi$ m². Find its radius.
- Given: $SA = 100\pi$
- Formula: $100\pi = 4\pi r^2$
- Divide by $\pi$: $100 = 4r^2$
- Divide by 4: $r^2 = 25$
- Take square root: $r = 5$ meters

---

## Volume of 3D Solids

### Prism

**Definition:** Volume is the space inside a prism.

**Formula:**
$$V = Bh$$

Where:
- $V$ = volume
- $B$ = area of the base
- $h$ = height of the prism

**Why it works:** Think of stacking copies of the base shape. If you have $h$ layers of area $B$, the total is $B \times h$.

**Worked Examples:**

**Example 1:** Find the volume of a rectangular prism with length 5 cm, width 4 cm, and height 10 cm.
- Base area: $B = 5 \times 4 = 20$ cm²
- Height: $h = 10$ cm
- Substitute: $V = 20 \times 10 = 200$ cm³

**Example 2:** A triangular prism has a triangular base with area 15 m² and height 8 m. Find its volume.
- Base area: $B = 15$ m²
- Height: $h = 8$ m
- Substitute: $V = 15 \times 8 = 120$ m³

**Example 3:** A prism has volume 360 cubic units and base area 24 square units. Find its height.
- Given: $V = 360$, $B = 24$
- Formula: $360 = 24h$
- Solve: $h = 15$ units

---

### Cylinder

**Definition:** A cylinder is like a prism with a circular base.

**Formula:**
$$V = \pi r^2 h$$

Where:
- $V$ = volume
- $r$ = radius of the circular base
- $h$ = height

**Why it works:** The base is a circle with area $\pi r^2$. Stacking layers of height $h$ gives volume $\pi r^2 \times h$.

**Worked Examples:**

**Example 1:** Find the volume of a cylinder with radius 3 cm and height 12 cm.
- Substitute: $V = \pi(3)^2(12) = \pi(9)(12) = 108\pi$ cm³
- Calculate: $V ≈ 339.29$ cm³

**Example 2:** A cylindrical water tank has radius 2 meters and height 5 meters. What volume of water can it hold?
- Substitute: $V = \pi(2)^2(5) = \pi(4)(5) = 20\pi$ m³
- Calculate: $V ≈ 62.83$ m³

**Example 3:** A cylinder has volume $150\pi$ cm³ and height 6 cm. Find its radius.
- Given: $V = 150\pi$, $h = 6$
- Formula: $150\pi = \pi r^2(6)$
- Divide by $\pi$: $150 = 6r^2$
- Divide by 6: $r^2 = 25$
- Take square root: $r = 5$ cm

---

### Pyramid

**Definition:** A pyramid comes to a point, so it's "thinner" than a prism with the same base.

**Formula:**
$$V = \frac{1}{3}Bh$$

Where:
- $V$ = volume
- $B$ = area of the base
- $h$ = perpendicular height (from base to apex)

**Why it works:** A pyramid takes up exactly one-third the volume of a prism with the same base and height. This is because as you go up from the base to the apex, the cross-section gets smaller.

**Worked Examples:**

**Example 1:** Find the volume of a square pyramid with base side 6 cm and height 10 cm.
- Base area: $B = 6 \times 6 = 36$ cm²
- Height: $h = 10$ cm
- Substitute: $V = \frac{1}{3}(36)(10) = \frac{360}{3} = 120$ cm³

**Example 2:** A triangular pyramid has a base with area 20 m² and height 9 m. Find its volume.
- Base area: $B = 20$ m²
- Height: $h = 9$ m
- Substitute: $V = \frac{1}{3}(20)(9) = \frac{180}{3} = 60$ m³

**Example 3:** A pyramid has volume 200 cubic units and base area 50 square units. Find its height.
- Given: $V = 200$, $B = 50$
- Formula: $200 = \frac{1}{3}(50)h$
- Simplify: $200 = \frac{50h}{3}$
- Multiply by $\frac{3}{50}$: $h = \frac{200 \times 3}{50} = 12$ units

---

### Cone

**Definition:** A cone is like a pyramid, but with a circular base.

**Formula:**
$$V = \frac{1}{3}\pi r^2 h$$

Where:
- $V$ = volume
- $r$ = radius of the base
- $h$ = perpendicular height

**Why it works:** Like a pyramid, a cone is one-third the volume of a cylinder with the same base and height.

**Worked Examples:**

**Example 1:** Find the volume of a cone with radius 4 cm and height 12 cm.
- Substitute: $V = \frac{1}{3}\pi(4)^2(12) = \frac{1}{3}\pi(16)(12) = \frac{192\pi}{3} = 64\pi$ cm³
- Calculate: $V ≈ 201.06$ cm³

**Example 2:** An ice cream cone has radius 2 inches and height 8 inches. What volume of ice cream can it hold?
- Substitute: $V = \frac{1}{3}\pi(2)^2(8) = \frac{1}{3}\pi(4)(8) = \frac{32\pi}{3}$ in³
- Calculate: $V ≈ 33.51$ in³

**Example 3:** A cone has volume $100\pi$ m³ and height 12 m. Find its radius.
- Given: $V = 100\pi$, $h = 12$
- Formula: $100\pi = \frac{1}{3}\pi r^2(12)$
- Simplify: $100\pi = 4\pi r^2$
- Divide by $4\pi$: $r^2 = 25$
- Take square root: $r = 5$ meters

---

### Sphere

**Definition:** The volume of a sphere is the space inside it.

**Formula:**
$$V = \frac{4}{3}\pi r^3$$

Where:
- $V$ = volume
- $r$ = radius

**Why it works:** This formula comes from integration in calculus. A sphere can be thought of as many thin circular disks stacked together.

**Worked Examples:**

**Example 1:** Find the volume of a sphere with radius 5 cm.
- Substitute: $V = \frac{4}{3}\pi(5)^3 = \frac{4}{3}\pi(125) = \frac{500\pi}{3}$ cm³
- Calculate: $V ≈ 523.60$ cm³

**Example 2:** A basketball has radius 4.7 inches. What is its volume?
- Substitute: $V = \frac{4}{3}\pi(4.7)^3 = \frac{4}{3}\pi(103.823) ≈ 435.64\pi$ in³
- Calculate: $V ≈ 1368.61$ in³

**Example 3:** A sphere has volume $288\pi$ m³. Find its radius.
- Given: $V = 288\pi$
- Formula: $288\pi = \frac{4}{3}\pi r^3$
- Divide by $\pi$: $288 = \frac{4}{3}r^3$
- Multiply by $\frac{3}{4}$: $r^3 = 216$
- Take cube root: $r = 6$ meters

---

## Cavalieri's Principle

### Understanding Cross-Sections

**Definition:** A cross-section is a 2D slice of a 3D object made by cutting it with a plane.

**Visual Example:** If you slice a loaf of bread, each slice is a cross-section.

### Cavalieri's Principle Explained

**Plain English Statement:** If two 3D solids have equal heights and their cross-sectional areas are equal at every height, then the solids have equal volumes.

**More Intuitive Explanation:** Imagine two stacks of coins. If both stacks are the same height and at each height level the coins have the same total area, then both stacks have the same total volume—even if one stack is tilted!

### Why It Works

The principle is based on the idea that volume can be calculated by summing up infinitely many thin cross-sections. If two objects have identical cross-sectional areas at every height, then the sum of all these infinitesimal slices will be equal.

### Applications

**Example 1: Prism vs. Oblique Prism**

A rectangular prism and an oblique prism (slanted prism) with:
- Same base area
- Same height

will have the same volume, even though the oblique prism is "tilted."

**Proof by Cavalieri:**
- At every height $h$ from the bottom, both solids have the same cross-sectional area (equal to the base area)
- Therefore, by Cavalieri's Principle, their volumes are equal

**Example 2: Cylinder vs. Tilted Cylinder**

A cylinder and a tilted (oblique) cylinder with:
- Same base radius (and thus same base area)
- Same height

will have the same volume.

**Example 3: Pyramid vs. Other Solids**

A pyramid with base area $B$ and height $h$ has volume $\frac{1}{3}Bh$. You can verify this using Cavalieri's Principle by comparing it to a prism with the same base and height. At each height $y$ from the base:
- The prism's cross-section has area $B$
- The pyramid's cross-section has area $B \times \frac{(h-y)^2}{h^2}$ (smaller as you go up)

The pyramid's cross-sections are smaller at each level, which is why its volume is only one-third.

### Worked Example

**Problem:** Two solids have the same height of 10 cm. At every height, both have the same cross-sectional area of 25 cm². Find the volume of each solid.

**Solution:**
- Since both solids have the same height and the same cross-sectional area at every height, by Cavalieri's Principle they have the same volume.
- We can think of them as stacking many thin "slices" of area 25 cm²
- With 10 cm height, the volume is approximately $25 × 10 = 250$ cm³ (this is exact for prisms, exact as the slices get infinitesimally thin)
- Both volumes = 250 cm³

---

## Real-World Applications: Density & Displacement

### Density

**Plain English Definition:** Density tells you how "heavy" or "tightly packed" something is. It's the amount of mass in a certain amount of space.

**Formula:**
$$\text{Density} = \frac{\text{Mass}}{\text{Volume}}$$

Or in symbols: $D = \frac{M}{V}$

**Units:** Common units are g/cm³, kg/m³, g/mL, etc.

**Why it matters:** Objects with the same mass but different volumes have different densities. For example, a small piece of lead is much denser than a large piece of foam.

**Worked Examples:**

**Example 1:** A block of iron has mass 78 grams and volume 10 cm³. What is its density?
- Given: $M = 78$ g, $V = 10$ cm³
- Formula: $D = \frac{78}{10} = 7.8$ g/cm³
- Interpretation: Each cm³ of iron has mass 7.8 grams

**Example 2:** Water has density 1 g/cm³. A container holds 500 cm³ of water. What is the mass?
- Given: $D = 1$ g/cm³, $V = 500$ cm³
- Formula: $M = D × V = 1 × 500 = 500$ grams

**Example 3:** A material has density 2.5 g/cm³ and mass 100 grams. Find its volume.
- Given: $D = 2.5$ g/cm³, $M = 100$ g
- Formula: $V = \frac{M}{D} = \frac{100}{2.5} = 40$ cm³

### Population Density

**Definition:** Population density measures how many people live in a certain area.

**Formula:**
$$\text{Population Density} = \frac{\text{Number of People}}{\text{Area}}$$

**Units:** People per square mile, people per km², etc.

**Worked Example:**

**Example:** A city has population 500,000 and covers area 250 km². What is its population density?
- Given: Population = 500,000, Area = 250 km²
- Formula: Population Density $= \frac{500,000}{250} = 2,000$ people per km²

### Displacement

**Plain English Definition:** When an object is placed in water (or another liquid), it pushes the liquid out of the way. The volume of liquid pushed out equals the volume of the submerged object.

**Key Principle:**
$$\text{Volume of object} = \text{Volume of liquid displaced}$$

**Worked Examples:**

**Example 1:** A rock is placed in a graduated cylinder. The water level rises from 50 mL to 65 mL. What is the volume of the rock?
- Initial volume: 50 mL
- Final volume: 65 mL
- Volume displaced: $65 - 50 = 15$ mL
- Rock volume: 15 cm³ (since 1 mL = 1 cm³)

**Example 2:** A spherical ball has radius 5 cm. How much water does it displace when fully submerged?
- Volume of sphere: $V = \frac{4}{3}\pi(5)^3 = \frac{500\pi}{3} ≈ 523.6$ cm³
- Water displaced: 523.6 cm³ (or 523.6 mL)

**Example 3:** An irregular stone displaces 200 mL of water. What is its volume?
- Volume displaced: 200 mL
- Stone volume: 200 cm³ (or 200 mL, depending on units)

---

## Modeling Real Objects

### What is Geometric Modeling?

**Definition:** Using simple geometric shapes to represent or approximate real-world objects, making them easier to analyze and solve problems.

**Why it's useful:** Real objects are often complex. By modeling them with simple shapes, we can calculate volume, surface area, and other properties.

### Common Real Objects and Their Models

**Objects and Shapes to Model:**

| Real Object | Geometric Model |
|---|---|
| Can | Cylinder |
| Box/Crate | Rectangular prism |
| Cone-shaped roof | Cone |
| Ball/sphere | Sphere |
| Tent | Triangular prism or pyramid |
| Building | Combination of rectangular prisms |
| Water tank | Cylinder or prism |
| Tree (trunk only) | Cylinder |
| Pencil | Cylinder |
| Ice cream cone with scoop | Cone + sphere |

### Worked Examples

**Example 1: Soup Can**

A cylindrical soup can has radius 4 cm and height 12 cm.

a) Find the lateral (curved) surface area (the label area).
- Lateral SA $= 2\pi rh = 2\pi(4)(12) = 96\pi ≈ 301.59$ cm²

b) Find the total surface area (including top and bottom).
- Total SA $= 2\pi r^2 + 2\pi rh = 2\pi(16) + 96\pi = 32\pi + 96\pi = 128\pi ≈ 402.12$ cm²

c) Find the volume of soup it can hold.
- Volume $= \pi r^2 h = \pi(4)^2(12) = 192\pi ≈ 603.19$ cm³ (or mL)

**Example 2: Conical Roof**

A conical roof has base radius 8 meters and slant height 10 meters.

a) Find the lateral surface area (area that needs roofing material).
- Lateral SA $= \pi rl = \pi(8)(10) = 80\pi ≈ 251.33$ m²

b) Find the volume of space under the roof. (First find height using Pythagorean theorem)
- $l^2 = h^2 + r^2$ → $100 = h^2 + 64$ → $h^2 = 36$ → $h = 6$ m
- Volume $= \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(64)(6) = 128\pi ≈ 402.12$ m³

**Example 3: Building**

A building consists of a rectangular prism base (length 20 m, width 15 m, height 8 m) with a rectangular prism on top (length 20 m, width 15 m, height 4 m).

a) Find the total volume.
- Base volume: $V_1 = 20 × 15 × 8 = 2400$ m³
- Top volume: $V_2 = 20 × 15 × 4 = 1200$ m³
- Total: $2400 + 1200 = 3600$ m³

b) Find the exterior surface area (5 faces of base + 4 faces of top, accounting for connections).
- This is complex, so we'd count carefully...
- (Full calculation omitted for length, but demonstrates the concept)

---

## Common Mistakes & Exam Tips

### Mistake 1: Confusing Height with Slant Height

**The Problem:** Students use slant height where perpendicular height is needed, or vice versa.

**Example:** For a cone with volume, you must use perpendicular height, not slant height.
- WRONG: $V = \frac{1}{3}\pi r^2 l$ (using $l$ instead of $h$)
- RIGHT: $V = \frac{1}{3}\pi r^2 h$ (using perpendicular $h$)

**How to Remember:**
- **Height (h):** Always perpendicular (straight up)
- **Slant height (l):** Along the slanted face

**Relationship:** Use Pythagorean theorem to convert between them: $l^2 = h^2 + r^2$

---

### Mistake 2: Forgetting the ½ in Triangle Formulas

**The Problem:** Students calculate $A = bh$ instead of $A = \frac{1}{2}bh$ for triangles.

**Example:** A triangle with base 8 and height 5.
- WRONG: $A = 8 × 5 = 40$
- RIGHT: $A = \frac{1}{2} × 8 × 5 = 20$

**Why it happens:** Rectangles use $A = lw$, and students confuse this with triangles.

**Memory trick:** A triangle is half a rectangle (if you draw a diagonal), so divide by 2.

---

### Mistake 3: Mixing Up Area and Volume Units

**The Problem:** Writing the wrong units for area (should be squared) or volume (should be cubed).

**Examples of mistakes:**
- WRONG: "The area is 50 meters" (should be 50 square meters or 50 m²)
- WRONG: "The volume is 100 cm" (should be 100 cubic centimeters or 100 cm³)

**How to remember:**
- **Area:** 2D shape → 2D units: cm², m², in², ft², etc.
- **Volume:** 3D solid → 3D units: cm³, m³, in³, ft³, etc.

---

### Mistake 4: Not Using Perpendicular Height for Parallelograms

**The Problem:** Students use the slanted side length instead of the perpendicular height.

**Example:** A parallelogram with side 10 cm and perpendicular height 6 cm.
- WRONG: $A = 10 × 10 = 100$ cm² (using the side twice)
- RIGHT: $A = 10 × 6 = 60$ cm² (base × perpendicular height)

**How to remember:** The height must be perpendicular (forming a 90° angle) to the base.

---

### Mistake 5: Forgetting About Both Bases in Surface Area

**The Problem:** For cylinders and prisms, students calculate only the lateral surface area and forget the two bases.

**Example:** A cylinder with radius 5 and height 10.
- WRONG: SA $= 2\pi rh = 100\pi$ (missing the base areas!)
- RIGHT: SA $= 2\pi r^2 + 2\pi rh = 50\pi + 100\pi = 150\pi$

**How to remember:** Surface area is the TOTAL area of all surfaces. Count: two bases + lateral sides.

---

### Mistake 6: Confusing Prism Volume with Pyramid Volume

**The Problem:** Using $V = Bh$ for a pyramid (should be $V = \frac{1}{3}Bh$).

**Example:** A pyramid with base area 40 and height 15.
- WRONG: $V = 40 × 15 = 600$ (this is prism volume)
- RIGHT: $V = \frac{1}{3} × 40 × 15 = 200$ (pyramid is one-third)

**Why it matters:** A pyramid comes to a point, so it holds much less than a prism.

**Memory trick:** Pyramids and cones are "pointy," so they're one-third the volume of their prism/cylinder counterparts.

---

### Mistake 7: Using Diameter Instead of Radius (or Vice Versa)

**The Problem:** The formulas use radius, but students might be given diameter, or vice versa.

**Example:** A circle with diameter 10 cm.
- WRONG: $A = \pi(10)^2 = 100\pi$ (using diameter as radius)
- RIGHT: $r = 5$ cm, so $A = \pi(5)^2 = 25\pi$ (converting diameter to radius first)

**Relationship:** $d = 2r$ or $r = \frac{d}{2}$

**How to remember:** Always check: are you given radius or diameter? Convert if needed!

---

### Mistake 8: Not Simplifying Composite Figures Correctly

**The Problem:** Students either count overlapping areas twice or forget to subtract holes.

**Example:** A rectangle 10 × 8 with a circular hole (radius 2) cut out.
- WRONG: Just adding: $80 + 4\pi$ (makes no sense)
- RIGHT: Rectangle minus hole: $80 - 4\pi ≈ 67.43$

**Strategy:**
1. Sketch and label the figure
2. Identify each simple shape
3. Calculate area of each
4. ADD if shapes are separate; SUBTRACT if one is removed

---

### Exam Tips

**Tip 1: Read Carefully**
- Is it asking for area, surface area, or volume?
- Are units given in meters, cm, inches, or feet?
- Is it asking for the exact answer ($\pi$ form) or approximate (decimal)?

**Tip 2: Draw and Label**
- Sketch the shape
- Label all given measurements
- Mark which measurements are height, base, radius, slant height, etc.

**Tip 3: Show All Work**
- Write the formula
- Substitute values
- Show intermediate steps
- Give units in final answer

**Tip 4: Double-Check Units**
- Area = square units (m², cm², etc.)
- Volume = cubic units (m³, cm³, etc.)
- If your units are wrong, your answer is wrong

**Tip 5: Use Pythagorean Theorem When Needed**
- To convert between height and slant height: $l^2 = h^2 + r^2$
- To find missing sides: $a^2 + b^2 = c^2$

**Tip 6: Know Your Formulas**
- Don't memorize all at once
- Group by type: all area formulas, all surface area, all volume
- Practice deriving them from more basic ideas

**Tip 7: Check Reasonableness**
- Does your answer make sense?
- Is a cone's volume less than a cylinder's with the same dimensions?
- Is surface area of a sphere realistic given the radius?

**Tip 8: Practice Mixed Problems**
- Don't just do "surface area" problems—practice identifying what's being asked
- Work with composite figures and real-world scenarios
- Try problems where you must solve for an unknown dimension

---

## Summary of Key Formulas

### Area Formulas (2D)

| Shape | Formula | Variables |
|---|---|---|
| Rectangle | $A = lw$ | $l$ = length, $w$ = width |
| Parallelogram | $A = bh$ | $b$ = base, $h$ = perpendicular height |
| Triangle | $A = \frac{1}{2}bh$ | $b$ = base, $h$ = height |
| Trapezoid | $A = \frac{1}{2}(b_1 + b_2)h$ | $b_1, b_2$ = parallel bases, $h$ = height |
| Rhombus/Kite | $A = \frac{1}{2}d_1 d_2$ | $d_1, d_2$ = diagonals |
| Regular Polygon | $A = \frac{1}{2}ap$ | $a$ = apothem, $p$ = perimeter |
| Circle | $A = \pi r^2$ | $r$ = radius |

### Circumference and Arc Length

| Measurement | Formula | Variables |
|---|---|---|
| Circumference | $C = 2\pi r = \pi d$ | $r$ = radius, $d$ = diameter |
| Arc Length | $\text{Arc} = \frac{\theta}{360°} × 2\pi r$ | $\theta$ = central angle (degrees) |
| Sector Area | $\text{Sector} = \frac{\theta}{360°} × \pi r^2$ | $\theta$ = central angle (degrees) |

### Surface Area Formulas (3D)

| Shape | Formula | Variables |
|---|---|---|
| Prism | $SA = 2B + Ph$ | $B$ = base area, $P$ = base perimeter, $h$ = height |
| Cylinder | $SA = 2\pi r^2 + 2\pi rh$ | $r$ = radius, $h$ = height |
| Pyramid | $SA = B + \frac{1}{2}Pl$ | $B$ = base area, $P$ = base perimeter, $l$ = slant height |
| Cone | $SA = \pi r^2 + \pi rl$ | $r$ = radius, $l$ = slant height |
| Sphere | $SA = 4\pi r^2$ | $r$ = radius |

### Volume Formulas (3D)

| Shape | Formula | Variables |
|---|---|---|
| Prism | $V = Bh$ | $B$ = base area, $h$ = height |
| Cylinder | $V = \pi r^2 h$ | $r$ = radius, $h$ = height |
| Pyramid | $V = \frac{1}{3}Bh$ | $B$ = base area, $h$ = perpendicular height |
| Cone | $V = \frac{1}{3}\pi r^2 h$ | $r$ = radius, $h$ = perpendicular height |
| Sphere | $V = \frac{4}{3}\pi r^3$ | $r$ = radius |

### Other Important Formulas

| Concept | Formula | Variables |
|---|---|---|
| Density | $D = \frac{M}{V}$ | $M$ = mass, $V$ = volume |
| Population Density | $D = \frac{\text{Population}}{\text{Area}}$ | People per unit area |
| Pythagorean Theorem | $a^2 + b^2 = c^2$ | Relating height and slant height |

---

## Final Thoughts

Mastering Unit 7 requires understanding not just formulas, but *why* they work. Each formula builds on simpler geometric ideas:

- **Area** = counting squares
- **Volume** = counting cubes (or stacking area)
- **Surface area** = summing up the areas of all outer surfaces

Practice with both abstract problems and real-world applications. Draw pictures, show your work, and always pay attention to units. With these skills, you're prepared to handle geometry's 3D world!

Good luck on your exam!
