# EP617

Researched: 2026-04-26

Canonical page: https://www.erdosproblems.com/617

Status: falsifiable - open, but a finite counterexample could disprove it.

Tags: graph theory.

## Statement

For every integer `r >= 3`, every `r`-coloring of the edges of
`K_{r^2+1}` should contain `r+1` vertices whose induced `K_{r+1}` is
missing at least one color.

Equivalently, the conjecture rules out a balanced coloring of
`K_{r^2+1}`.

## Current Notes

This is an Erdos-Gyarfas conjecture. The official page says it is known
for `r = 3` and `r = 4`, false for `r = 2`, and that replacing `r^2+1`
by `r^2` fails for infinitely many `r`.

The statement is formalized in Lean according to the Erdos Problems
database. The existing local folder already contains computational work in
`notes/`, `results/`, and `scripts/`; this file is only the top-level
orientation note.

## Source Trail

- Erdos Problems official page: https://www.erdosproblems.com/617
- Discussion thread: https://www.erdosproblems.com/forum/thread/617
- Source keys on the page: `[ErGy99]`, `[Er99]`

