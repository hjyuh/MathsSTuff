# Cross-Problem Connections
## Updated: March 13, 2026

---

## Connection 1: The "outsider exchange" pattern appears in BOTH 848 and 686

In 848: adding an outsider (x ≢ 7 mod 25) to the base class forces deletions 
because xy+1 becomes squarefree for many base-class y.

In 686: for large k, the ratio ∏(m+i)/∏(n+i) = 4 forces the two blocks to 
have nearly identical prime factorizations except at p=2. Any "outsider prime" 
(one appearing in the upper block but not the lower) would break the equation.

Both are "exchange inequality" problems: you want to show that deviating from 
the optimal structure costs more than it gains.

## Connection 2: 931 and 686 share the same "support matching" core

931 asks: can two blocks have the same PRIME SUPPORT?
686 asks: can two blocks have the same PRODUCT (hence same prime support AND valuations)?
388 asks: can two blocks of DIFFERENT lengths have equal products?

These form a hierarchy: 388 ⊃ 686 ⊃ 931 in terms of constraint strength.
Techniques that work for the weaker version should transfer to the stronger.

## Connection 3: The Bilu-Tichy toolkit spans 388, 686, and potentially 421

388: f_{k₁}(x) = f_{k₂}(y) — we used Bilu-Tichy + Kulkarni-Sury
686: f_k(x) = N·f_k(y) — same framework (Chan/Rakaczki confirm this)
421: split-product curves ∏(x-aᵢ) = ∏(y+bⱼ) — forum suggests Bilu-Tichy applies

Our 388 Theorem 1 experience directly informs how to approach 686 and 421.

## Connection 4: The "decidable via computation" pattern in 848 and 686

848: asymptotic result exists → reduce to finite verification → verify
686: each fixed (N,k) has finitely many solutions → bound k → verify remaining

Both follow the same template: analytic/algebraic theorem handles the tail,
computation handles the head. The technology for the computation step (compiled 
verifiers, certificate generation) is shared.

## Connection 5: Problem 363 (disproved) illuminates 388 and 686

363 has INFINITE families (multiple intervals, product = square).
388 conjectures FINITELY many (two intervals, products equal).
686 is between them (two intervals, ratio = integer).

The boundary between infinite and finite solutions is exactly at 
"two intervals + exact equality." Adding intervals or weakening to 
"product is a square" crosses into infinite territory. This structural 
insight explains WHY 388 and 686 are hard: they sit exactly on the boundary.

## Connection 6: Self-pair condition in 848 is analogous to diagonal terms in 494

848: NonSquarefreeProductProp requires a²+1 non-squarefree (self-pairs)
494: multiset sum uniqueness has diagonal contributions (k=2 means a+a = 2a)

Both problems have "diagonal" constraints that restrict the admissible set 
before you even consider cross-pairs. In 848, this restricts to ~10.5% density.
In 494, diagonal terms constrain the possible multiset structures.

## Connection 7: The "effective vs asymptotic" gap appears everywhere

848: Sawhney proved asymptotically, need effective
388 Theorem 2: Bilu-Tichy gives fixed-pair finiteness, need uniform
931 Level 3: Level 2 gives gap-fixed finiteness, need gap finiteness
686: each (N,k) is finite (Faltings), need uniform k-bound

This is the SAME structural gap in every problem. The tools give "for each fixed 
parameter, finitely many." We need "across all parameters, finitely many."
This suggests there might be a META-technique for bridging this gap.
