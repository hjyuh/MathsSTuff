# AoPS Intro Algebra - Chapter 11 Notes (Prompt-Aligned)

Source: `introtoalgebra/aops11.pdf` (Chapter 11, Special Factorizations)
Style target: `math-teaching-prompt.md` ("strip the costume", one-step nudges, trigger sentences)

## Chapter Goal
Build fast recognition for 5 patterns and choose the right one from problem wording:

1. Square of a binomial
2. Difference of squares
3. Sum/difference of cubes
4. Rationalizing denominators
5. Simon's Favorite Factoring Trick (SFFT)

## Identity Pack (Must Know Cold)

```text
(a + b)^2 = a^2 + 2ab + b^2
(a - b)^2 = a^2 - 2ab + b^2
a^2 - b^2 = (a - b)(a + b)
a^3 - b^3 = (a - b)(a^2 + ab + b^2)
a^3 + b^3 = (a + b)(a^2 - ab + b^2)
ab + ay + bx + xy = (a + x)(b + y)
```

## 11.1 Squares of Binomials

What to notice:
- Outer terms are squares.
- Middle term is twice the product.
- Negative constant means not a perfect-square trinomial.

Nudges to use:
- "What are the two things being squared at the ends?"
- "Does the middle term match `2 * (root first) * (root last)`?"
- "Can you expand first, then substitute?"

Common mistakes:
- Dropping the middle term in `(x - k)^2`.
- Forcing a non-perfect-square trinomial into a square.

Trigger sentence:
- "I checked the middle term against `2ab`, so I knew whether it was a square trinomial."

## 11.2 Difference of Squares

What to notice:
- Two perfect squares with subtraction.
- Factor repeatedly if a new difference of squares appears.

Nudges to use:
- "Are both terms perfect squares right now, or after GCF?"
- "Can this factor be broken again?"
- "If this is `m^2 - n^2 = k`, what happens after factoring?"

Common mistakes:
- Stopping too early (example pattern: `z^4 - 1`).
- Missing GCF before applying identity.

Trigger sentence:
- "I saw two squares being subtracted, so I factored first and solved from factor pairs."

## 11.3 Sum and Difference of Cubes

What to notice:
- Linear factor matches the sign (`a-b` or `a+b`).
- Sign in quadratic middle term is opposite.

Nudges to use:
- "What cube is this near?"
- "Do you see `x^2 +/- xy + y^2` hidden in the problem?"
- "Can you factor out a common coefficient first?"

Common mistakes:
- Sign mix-up in the quadratic factor.
- Treating non-cubes as cubes without preprocessing.

Trigger sentence:
- "The linear sign matched the original, so the quadratic middle sign had to flip."

## 11.4 Rationalizing Denominators

What to notice:
- One square root: multiply by same root.
- `a +/- b` radical binomial: multiply by conjugate.
- Cube-root binomial: use cube identities, not conjugates.

Nudges to use:
- "What multiplier makes the denominator a rational number?"
- "Is this a difference of squares or cubes setup?"
- "Can you group terms first, then conjugate?"

Common mistakes:
- Multiplying by random radicals that do not cancel structure.
- Using square-root conjugate logic on cube-root forms.

Trigger sentence:
- "I matched denominator structure to the identity that cancels it (conjugate for squares, cube factor for cube roots)."

## 11.5 Simon's Favorite Factoring Trick (SFFT)

What to notice:
- Form looks like `mn + am + bn = const` after rearranging.
- Add the missing constant to complete a product.

Nudges to use:
- "If this were `(m + ?)(n + ?)`, what constant is missing?"
- "After clearing fractions, does it now look like SFFT?"
- "What factor pairs satisfy the completed product?"

Common mistakes:
- Choosing wrong add-on constant.
- Forgetting negative factor pairs when domain is all integers.

Trigger sentence:
- "After rearranging to `mn + am + bn`, I added `ab` to complete `(m+b)(n+a)` and used factor pairs."

## Fast "Which Tool?" Checklist

1. Two squares subtracted -> difference of squares.
2. Three-term quadratic with square ends -> check `2ab`.
3. Close to a clean cube -> sum/difference of cubes.
4. Radicals in denominator -> conjugate or cube identity.
5. Mixed product/linear terms in two variables -> SFFT.

## Practice Sequence (Chapter 11)

1. Identity speed drill: state all 6 formulas from memory.
2. Recognition drill: name tool only, no solving.
3. Solve 1-2 representative problems per section.
4. Write one trigger sentence per problem.

## Minimal Trigger Log Template

```text
Problem:
First move I should make:
Feature that triggered it:
Mistake I made (if any):
Correct trigger sentence:
```

