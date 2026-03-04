# Chapter 11: Special Factorizations — Problem-Solving Notes

## 11.1 Squares of Binomials

### Core Identity

**(a + b)² = a² + 2ab + b²**

This works for any values of a and b (including negatives). The key is recognizing that:
- Two terms are perfect squares (a² and b²)
- The middle term is **twice the product** of the terms in the binomial (2ab)

### How to Recognize a Perfect Square Trinomial

Given a quadratic like `Ax² + Bx + C`, check:
1. Is A a perfect square? (A = a²)
2. Is C a perfect square? (C = b²) — **C must be non-negative!**
3. Does B = 2ab (or B = -2ab)?

If all three hold → it factors as (a + b)² or (a - b)².

**Watch out:** If the constant term is negative (like x² - 8z - 16), it **cannot** be a perfect square.

### Problem-Solving Techniques

**Technique 1: Expand strategically to avoid radicals**

> *Problem 11.4 (Mandelbrot):* If x = √(6/7), evaluate (x + 1/x)².

Instead of substituting and grinding, use the expansion:
```
(x + 1/x)² = x² + 2(x)(1/x) + (1/x)² = x² + 2 + 1/x²
```
Now x² = 6/7 and 1/x² = 7/6, so:
```
(x + 1/x)² = 6/7 + 2 + 7/6 = (36 + 84 + 49)/42 = 169/42
```
The expansion **eliminates the radicals** entirely.

**Technique 2: Substitute variables for giant numbers**

> *Problem 11.5:* Compute 20062005² − 2(20062005)(20062003) + 20062003².

Let x = 20062003. Then 20062005 = x + 2, and the expression becomes:
```
(x + 2)² − 2(x + 2)(x) + x² = x² + 4x + 4 − 2x² − 4x + x² = 4
```
Or recognize directly: this is **(20062005 − 20062003)² = 2² = 4**.

**Technique 3: Mental math squaring**

To square a number near a "nice" number, write it as (nice ± small):
- 71² = (70 + 1)² = 4900 + 140 + 1 = **5041**
- 99² = (100 − 1)² = 10000 − 200 + 1 = **9801**
- 204² = (200 + 4)² = 40000 + 1600 + 16 = **41616**

**Shortcut for numbers ending in 5:** To compute (10n + 5)², calculate n(n+1) and append 25.
- 65² → 6 × 7 = 42 → **4225**
- 45² → 4 × 5 = 20 → **2025**

### Pascal's Triangle (Higher Powers)

The coefficients of (x + y)ⁿ follow Pascal's Triangle:
```
n=0:                1
n=1:              1   1
n=2:            1   2   1
n=3:          1   3   3   1
n=4:        1   4   6   4   1
n=5:      1   5  10  10   5   1
n=6:    1   6  15  20  15   6   1
```
Each entry = sum of the two entries directly above it.

### Key Exercises
- 11.1.1: Practice expanding (x−5)², (x+5)³, (3y−7)², (3y+7)³
- 11.1.4: Compute 31² and 299² mentally
- 11.1.6★: Compute 1999199819972² − 2·199919981994² + 199919981991² (use substitution!)

---

## 11.2 Difference of Squares

### Core Identity

**a² − b² = (a − b)(a + b)**

### How to Spot It

Any expression where two perfect squares are **subtracted**. This includes:
- Obvious: x² − 49 = (x − 7)(x + 7)
- Hidden squares: 4t² − 121 = (2t)² − 11² = (2t − 11)(2t + 11)
- Factor first: 3r² − 147 = 3(r² − 49) = 3(r − 7)(r + 7)
- Higher powers: z⁴ − 1 = (z²)² − 1² = (z² − 1)(z² + 1) = **(z − 1)(z + 1)(z² + 1)**

Always check if you can factor **further** after the first application!

### Problem-Solving Techniques

**Technique 1: Consecutive squares pattern**

> *Problem 11.10:* Evaluate 5² − 4², 6² − 5², 7² − 6², 8² − 7².

Results: 9, 11, 13, 15. Pattern: **(n+1)² − n² = 2n + 1 = (n+1) + n**

Proof: (n+1)² − n² = [(n+1) − n][(n+1) + n] = 1 · (2n + 1)

**Application:** Compute 121² = 120² + 120 + 121 = 14400 + 241 = 14641.

**Technique 2: Diophantine equations via factoring**

> *Problem 11.11:* Find all pairs of positive integers m, n such that m² − n² = 105.

Factor: (m − n)(m + n) = 105.

Since m, n are positive integers, m − n < m + n and both are factors of 105.
```
105 = 1 × 105 = 3 × 35 = 5 × 21 = 7 × 15
```
Solve each system:
| m − n | m + n | m  | n  |
|-------|-------|----|----|
| 1     | 105   | 53 | 52 |
| 3     | 35    | 19 | 16 |
| 5     | 21    | 13 | 8  |
| 7     | 15    | 11 | 4  |

**Key insight:** Factoring the Diophantine equation lets us systematically find **all** solutions.

**Technique 3: Eliminating square roots by multiplying (a−b)(a+b)**

> *Problem 11.12:* Given x = z − √(z²−5) and 5y = z + √(z²−5), find x when y = 2/3.

Multiply the equations:
```
(x)(5y) = [z − √(z²−5)][z + √(z²−5)] = z² − (z²−5) = 5
```
So xy = 1. Since y = 2/3, we get **x = 3/2**.

**Technique 4: Clever substitution for computation**

> *Problem 11.13 (Mandelbrot):* Compute √(1998·1996·1994·1992 + 16).

Let z = 1995 (the middle value). Then the four numbers are z+3, z+1, z−1, z−3:
```
(z+3)(z−3)(z+1)(z−1) + 16 = (z²−9)(z²−1) + 16 = z⁴ − 10z² + 9 + 16 = z⁴ − 10z² + 25
```
Recognize: z⁴ − 10z² + 25 = **(z² − 5)²**

So the answer = z² − 5 = 1995² − 5 = (2000−5)² − 5 = 4000000 − 20000 + 25 − 5 = **3,980,020**.

**Key insight:** Choose your substitution to maximize symmetry and simplify the algebra.

### Key Exercises
- 11.2.2: Given 55555² = 3086358025, calculate 55556² without a calculator
- 11.2.4: Factor w⁴ − 16 completely
- 11.2.6★ (HMMT): Find x − y given x⁴ = y⁴ + 18√3, x² + y² = 6, x + y = 3

---

## 11.3 Sum and Difference of Cubes

### Core Identities

**x³ − y³ = (x − y)(x² + xy + y²)**

**x³ + y³ = (x + y)(x² − xy + y²)**

### How to Remember (Don't Just Memorize!)

- x − y is a factor of x³ − y³ because x³ − y³ = 0 when x = y ✓
- x + y is a factor of x³ + y³ because x³ + y³ = 0 when x = −y ✓
- x + y is **NOT** a factor of x³ − y³ (doesn't equal 0 when x = −y in general)

The quadratic factor always has the form: (first term)² ∓ (product) + (second term)²
- The sign of the middle term is **opposite** to the sign in the linear factor.

### Problem-Solving Techniques

**Technique 1: Factor out common factors first**

> *Problem 11.16d:* Factor 32t³ − 108.

Factor out 4: 4(8t³ − 27) = 4[(2t)³ − 3³] = **4(2t − 3)(4t² + 6t + 9)**

**Technique 2: Recognize cubes hiding in large numbers**

> *Problem 11.17 (HMMT):* Find the two prime factors of 7,999,999,999.

Note: 8,000,000,000 = 2000³. So:
```
7,999,999,999 = 2000³ − 1³ = (2000 − 1)(2000² + 2000 + 1) = 1999 × 4,002,001
```

**Technique 3: Recognize the quadratic factors in equations**

> *Problem 11.18 (HMMT):* Given (x+y)/(1+z) = (1−z+z²)/(x²−xy+y²) and (x−y)/(3−z) = (9+3z+z²)/(x²+xy+y²), find x.

Cross-multiply to recognize sum/difference of cubes:
- First equation: (x+y)(x²−xy+y²) = (1+z)(1−z+z²) → **x³ + y³ = 1 + z³**
- Second equation: (x−y)(x²+xy+y²) = (3−z)(9+3z+z²) → **x³ − y³ = 27 − z³**

Adding: 2x³ = 28, so x³ = 14, and **x = ∛14**.

**Key insight:** Always look for the quadratic factors (x²±xy+y²) — they're the giveaway that sum/difference of cubes is in play.

### Key Exercises
- 11.3.2: Find the prime factorization of 3⁶ + 2⁶
- 11.3.3: Express x⁶ − 64 as a product of **four** factors
- 11.3.4c★: Write xᵏ − yᵏ as a product of two factors
- 11.3.5★ (Dropped AIME): Given |x| ≠ |y|, x³ = 15x + 4y, y³ = 4x + 15y, find x² + y²

---

## 11.4 Rationalizing Denominators

### Core Techniques

**Type 1: Single radical in denominator**

Multiply top and bottom by the radical:
```
a/√b = a√b/b
```

For cube roots: multiply by the appropriate power to complete the cube.
```
6/∛3 = 6·∛(3²)/3 = 6∛9/3 = 2∛9
```

**Type 2: Binomial with square roots (use difference of squares)**

For denominators like √a + √b, multiply by the **conjugate** √a − √b:
```
1/(√7 − √6) · (√7 + √6)/(√7 + √6) = (√7 + √6)/(7 − 6) = √7 + √6
```

**Type 3: Three-term denominator (apply conjugate twice)**

> *Problem 11.21:* Rationalize 1/(√2 + √3 + √5).

Group as (√2 + √3) + √5 and multiply by (√2 + √3) − √5:
```
Numerator: √2 + √3 − √5
Denominator: (√2 + √3)² − 5 = 2 + 2√6 + 3 − 5 = 2√6
```
Then multiply top and bottom by √6:
```
(√12 + √18 − √30) / 12
```

**Type 4: Cube root in denominator (use sum/difference of cubes)**

> *Problem 11.22:* Rationalize 1/(2 − ∛2).

Use a² + ab + b² with a = 2, b = ∛2:
```
Multiply by (4 + 2∛2 + ∛4)/(4 + 2∛2 + ∛4)
Denominator: 2³ − (∛2)³ = 8 − 2 = 6
Result: (4 + 2∛2 + ∛4)/6
```

### Key Exercises
- 11.4.2: Rationalize 2/(√4 + √5) and √7/(...)
- 11.4.5★: Telescope 1/(√100+√99) + 1/(√99+√98) + ... + 1/(√2+√1)

---

## 11.5 Simon's Favorite Factoring Trick

### Core Identity

**ab + ay + bx + xy = (a + x)(b + y)**

### The Technique

When you have the **product of two variables** plus **linear terms** in both variables, you can add a constant to both sides to factor.

### Step-by-Step Method

1. Start with something like mn + 3m + 5n = k
2. Guess the factored form: (m + ?)(n + ?) — the blanks come from the coefficients of the linear terms
3. Here: (m + 5)(n + 3) = mn + 3m + 5n + **15**
4. So add 15 to both sides: (m + 5)(n + 3) = k + 15
5. Use factor pairs of the right side to find all solutions

### Problem-Solving Techniques

**Technique 1: Basic SFFT**

> *Problem 11.23:* Find all pairs of positive integers (m, n) with mn + m + n = 76.

We want (m + 1)(n + 1). Expanding: mn + m + n + 1. Add 1 to both sides:
```
(m + 1)(n + 1) = 77 = 7 × 11
```
Since m, n > 0: (m+1, n+1) = (7, 11) or (11, 7) → **(m, n) = (6, 10) or (10, 6)**.

**Technique 2: SFFT with different coefficients**

> *Problem 11.24:* Find all integer pairs (b, c) with bc − 7b + 3c = 70.

Target: (b + 3)(c − 7) = bc − 7b + 3c − 21. Subtract 21 from both sides:
```
(b + 3)(c − 7) = 49
```
Factor pairs of 49: ±1 × ±49, ±7 × ±7 → **6 solutions**.

**Technique 3: Clearing fractions first**

> *Problem 11.25 (AHSME):* How many ordered pairs (m, n) of positive integers satisfy 4/m + 2/n = 1?

Multiply by mn: 4n + 2m = mn → mn − 2m − 4n = 0.

Target: (m − 4)(n − 2) = mn − 2m − 4n + 8. Add 8:
```
(m − 4)(n − 2) = 8
```
Factor pairs of 8 (positive only, since m, n > 0):
```
8 = 8×1 = 4×2 = 2×4 = 1×8
```
All four give valid positive solutions → **4 ordered pairs**.

### Key Exercises
- 11.5.1: Factor ab + 5b + 2a + 10
- 11.5.3: Find the prime factorization of 19·13 − 7·13 + 3·19 − 21 (try it in your head!)
- 11.5.4: Write 1/6 as the sum of two distinct positive unit fractions (count the ways)
- 11.5.5: Find all integer pairs (p, q) with pq − 3p + 5q = 0

---

## Chapter Summary: All Five Factorizations

| Factorization | Formula |
|---|---|
| Square of binomial | a² + 2ab + b² = (a + b)² |
| Difference of squares | a² − b² = (a − b)(a + b) |
| Sum of cubes | x³ + y³ = (x + y)(x² − xy + y²) |
| Difference of cubes | x³ − y³ = (x − y)(x² + xy + y²) |
| Simon's Favorite Factoring Trick | ab + ay + bx + xy = (a + x)(b + y) |

## Master Problem-Solving Strategies

1. **Giant numbers?** → Substitute a variable or look for a pattern with smaller numbers
2. **Diophantine equation?** → Get all variables on one side, factor, use factor pairs of the constant
3. **Square roots causing trouble?** → Multiply expressions of the form (a+b)(a−b) to eliminate them
4. **Making a substitution?** → Choose the one that maximizes symmetry (e.g., the middle value)
5. **See x² ± xy + y²?** → Think sum/difference of cubes — the quadratic factor is the giveaway
6. **Product of variables + linear terms?** → Simon's Favorite Factoring Trick
7. **Don't just memorize** — understand *why* each factorization works so you can spot them in disguise

---

## Challenge Problems Worth Attempting

- **11.43:** Three consecutive odd integers with b² − a² = 344 (difference of squares + Diophantine)
- **11.45 (Mandelbrot):** Telescoping product involving differences of squares
- **11.47:** Largest prime divisor of 5¹⁴ − 2·10⁷ + 2¹⁴ (recognize as a perfect square!)
- **11.48 (AMC 12):** ab = a − b, find a/b + b/a − ab (use SFFT to solve for the relationship)
- **11.54★:** Factor x⁴ + 4y⁴ (Sophie Germain identity — a beautiful trick!)
- **11.57★ (Mandelbrot):** Sum of digits of 2003⁴ − 1997⁴ (layer difference of squares)
