# EP341

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/341

Status: open.

Tags: number theory.

## Statement

Start with a finite set of positive integers

```tex
A=\{a_1<\cdots<a_k\}.
```

Extend it greedily to an infinite sequence by choosing `a_{n+1}`, for
`n >= k`, to be the least integer greater than `a_n` that is not equal to
`a_i+a_j` for any `i,j <= n`.

Must the difference sequence `a_{m+1}-a_m` eventually become periodic?

## Current Notes

The official page identifies this as an old problem of Dickson. It also
notes that even the initial set `{1,4,9,16,25}` requires thousands of terms
before periodicity appears.

Green's open problems list discusses it as Problem 7.

The statement is formalized in Lean according to the Erdos Problems
database.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/341
- Green open problems list linked from the page: https://people.maths.ox.ac.uk/greenbj/openquestions.html
- Source key on the page: `[ErGr80,p.53]`

