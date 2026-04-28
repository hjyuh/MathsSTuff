# EP424

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/424

Status: open.

Tags: number theory.

OEIS: A005244.

## Statement

Begin with `a_1=2` and `a_2=3`. Continue by appending every possible value
of

```tex
a_i a_j - 1
```

with `i != j`. Does the set of integers that eventually appear have
positive lower density?

## Current Notes

This is a Hofstadter question. The sequence begins

```text
2, 3, 5, 9, 14, 17, 26, ...
```

The page clarifies an important correction: the stronger "almost all
integers appear" version is false, because no integer congruent to `1`
modulo `3` ever appears. Therefore the density is at most `2/3`.

The intended open question is whether the appearing set has positive lower
density. The page also points to Guy's `Unsolved Problems in Number
Theory`, section E31, and Green's open problems list, Problem 63.

The statement is formalized in Lean according to the Erdos Problems
database.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/424
- OEIS A005244: https://oeis.org/A005244
- Green open problems list linked from the page: https://people.maths.ox.ac.uk/greenbj/openquestions.html
- Source keys on the page: `[Er77c,p.71]`, `[ErGr80,p.84]`

