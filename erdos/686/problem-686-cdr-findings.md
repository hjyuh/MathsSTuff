# Problem 686 — Claude DR Step 1D Results: Key Findings

## Date: March 14, 2026
## Source: Claude Deep Research on Beukers-Shorey-Tijdeman + Kulkarni-Sury

---

## THE CRITICAL INSIGHT (from Lemma 4 — Khanduja-Bhatia)

f_k(x) − N·f_k(y) is irreducible if and only if N is NOT a d-th power for d | k, d ≥ 2.

When N IS a perfect power, the polynomial MAY be reducible → creating solution families on lower-genus components.

**THIS IS THE PRECISE MECHANISM BY WHICH {4, 25, 49, 64, 81} ESCAPE REPRESENTATION.**

- 4 = 2² (perfect square)
- 25 = 5² (perfect square)  
- 49 = 7² (perfect square)
- 64 = 2⁶ (perfect square, cube, AND sixth power)
- 81 = 3⁴ (perfect square AND fourth power)

All failures are perfect powers. The Khanduja-Bhatia criterion explains WHY.

## THE GAP (identified by Claude DR)

All per-k finiteness results show: for each fixed k, only finitely many (x,y) satisfy f_k(x) = N·f_k(y).

But 686 asks for EXISTENCE of at least one solution for SOME k.

The finiteness results are necessary but not sufficient. We need an existence/density result.

**What's already handled:**
- Non-square N → k = 2 works (Pell equation gives infinitely many solutions)
- Non-perfect-power N → likely representable for some k (irreducibility + density heuristics)

**The true open core:**
For N ∈ {4, 25, 49, 64, 81, ...} (perfect powers), does there exist ANY k ≥ 3 giving a representation?

No existing lemma in the literature answers this.

## TOP 3 TRANSFERABLE LEMMAS (ranked)

### Rank 1: Hajdu-Tijdeman PTE (Prouhet-Thue-Morse) Connection
- Infinitely many solutions require root sets to satisfy power-sum matching conditions
- Both root sets being the same AP (scaled by N) makes PTE impossible for generic N
- Gives structural insight into WHY perfect powers are hard

### Rank 2: Khanduja-Bhatia Irreducibility
- f_k(x) − N·f_k(y) is irreducible iff N ≠ d-th power for d | k, d ≥ 2
- When irreducible → genus bounds (Faltings) give finiteness per k
- When reducible (N = perfect power) → lower-genus components may exist

### Rank 3: BST Indecomposability (odd k)
- f_k is indecomposable for odd k ≥ 3
- Foundation for all standard pair eliminations
- For even k: unique decomposition via quadratic folding f_k = R_d((x + (k-1)/2)²)

## THE ATTACK PLAN FOR 686

Two-pronged:

**Prong 1 (non-perfect-powers):** Already essentially handled.
- Non-squares: k = 2 Pell equation works
- Non-perfect-powers that are squares: need to show some k ≥ 3 works

**Prong 2 (perfect powers):** This is the hard part.
- Need to show 4, 25, 49, 64, 81 either CAN or CANNOT be represented
- The Khanduja-Bhatia criterion says the polynomial is reducible for these N
- Analyze the lower-genus components — do they have integer points?
- Computational evidence says NO for these specific values up to N ≤ 100
- May need to prove impossibility for all perfect powers, or find large-k representations

## CONNECTION TO MAHMOUD'S 388 WORK

The Kulkarni-Sury framework Mahmoud used on 388 applies directly to 686:
- Theorem C handles f(x) = c·g(y) without modification
- The constant N becomes part of the polynomial G = N·f_k
- Standard pair elimination works the same way
- The AP root structure eliminates all five standard pairs for k ≥ 5

What Mahmoud's 388 work ADDS: the specific elimination of all three exceptional families was done for f_{k1}(x) = f_{k2}(y). The same elimination technique works for f_k(x) = N·f_k(y) with minimal modification.

## NEXT STEPS

1. Investigate the reducible case: when N = m^d with d | k, what are the factors of f_k(x) − N·f_k(y)? What genus are the component curves?
2. For the specific failures {4, 25, 49, 64, 81}: compute the component curves explicitly for small k and check for integer points.
3. Check: is there a perfect power N > 81 that CAN be represented? If yes, the conjecture is "all N work for large enough k." If no perfect power works, the conjecture should be refined.
4. Wait for GPT DR cross-branch results — the PTE connection and carry-counting may provide the existence argument needed for Prong 1.
