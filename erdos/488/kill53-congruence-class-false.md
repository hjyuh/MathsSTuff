# EP-488: Kill #53 — Congruence Class Enlargement Route FALSE
## April 5, 2026

## THE KILL

"Prove EP-488 for general congruence classes, then deduce multiples" is IMPOSSIBLE.

### The general congruence class EP-488 is FALSE.

Counterexample: A = {3,4,5}, residues (0, 3, 3).
Cover: 0 mod 3, 3 mod 4, 3 mod 5.
- F(5) = 1 (only integer 3 is covered), G(5) = 1/5
- F(13) = 8, G(13) = 8/13
- Ratio: G(13)/G(5) = 40/13 ≈ 3.077 > 2

### The ratio can be made ARBITRARILY LARGE.

A = {M/2+1, ..., M}, all with residue r = M/2.
- At x = M: only integer M/2 covered → G(M) = 1/M
- At x = 2M: each class adds a distinct hit → G(2M) ≥ 1/4
- Ratio ≥ M/4 → ∞

### Why Rogers' theorem doesn't help:

Rogers' theorem: among all residue choices, r_i = 0 MINIMIZES the
density of the covered union (equivalently, MAXIMIZES the sieved complement).

But this is a GLOBAL DENSITY statement (average over full period).
Oscillation (sup G / inf G) depends on PREFIX COUNTS, which are
sensitive to where progressions start relative to evaluation points.

Rogers extremality ≠ oscillation extremality. They're different objects.

### What this means:

The multiples case (r_i = 0) is special. It has LESS oscillation than
arbitrary residue choices, not more. EP-488 is a theorem about the
specific structure of multiples (zero residue classes), not a general
fact about unions of arithmetic progressions.

Any proof of EP-488 must use the r_i = 0 structure essentially.
You can't prove it by going to a broader class and specializing back.

## ALSO: Tao blog post on Rogers' theorem
5.2 cited: terrytao.wordpress.com/2026/01/19/rogers-theorem-on-sieving/
This is a recent (Jan 2026) exposition by Tao. Worth reading.

## KILL COUNT: 53
## PERCENTAGE: 68%
Dropped from 70%. Direction A (congruence class) was a major hoped-for
escape route. Its death means no "enlarge and specialize" strategy works.
The proof must engage directly with the multiples structure.
