# EP-488: IE Bound KILLED — GPT-5.4 Counterexample
## March 30, 2026

### The counterexample (GPT-5.4)

Take A = {2, 3} ∪ {primes 5 ≤ p ≤ P}. All quotient-tail moduli are the primes themselves.

IE(Q_a) = (1/2)(∏(1+1/p) - ∏(1-1/p)) ~ log(P)/2 → ∞

But a·α(s) → constant (4/3 or 2 depending on s definition).

**Concrete failure at P = 5003:** IE = 2.211, a·α = 1.465 (or 2.131). Both < IE.

### Why our computation missed it

We only tested |T| ≤ 4. The counterexample uses |T| = 669 (all primes from 5 to 5003).

### What the IE bound $W^+/y ≤ Σ_{|S| odd} 1/lcm(S)$ actually does wrong

It uses {u} ≤ u for ALL subsets simultaneously. For prime antichains, the odd-subset sum 
grows like an Euler product (log P), but the actual W+ has massive cancellation between 
the fractional parts that the bound throws away.

### What survives
- 20-theorem reduction chain: INTACT
- Bridge Lemma B': INTACT
- W+ ≤ 2^{k-1}: INTACT (but useless for large k)
- Refined sufficient condition Σ 1/q_{>y} + W+/y < a·α(s): INTACT
- Actual F(m)/m < 2F(s)/s: TRUE computationally for all systems including large P

### What's dead
- IE bound as proxy for W+/y: KILLED (approach #16)

### What's needed
A DIRECT bound on W+/y that captures cancellation. Options:
1. **Hough-Nielsen Shearer-type bound** → dependency graph → relative equidistribution → W+
2. **Direct Fourier/Erdős-Turán** on the Q-free set
3. **Peak-regime analysis**: at the actual ratio peak, W+/y is controlled by 
   different structure than IE

### Key insight from GPT-5.4
"The failure is not Bridge B'; it is the replacement W+/y ≤ IE(Q). For long prime 
antichains, IE is the wrong scale. The next viable route is to bound the true 
ratio-peak correction, not the full odd-subset IE mass."

### Updated killed approaches (16 total)
1-13: [earlier approaches, see previous logs]
14. Active coprimality → Tao reduction (non-coprime active pairs at a=2)
15. "Coprime is worst case" hypothesis (failed by 0.000043)
16. **IE bound W+/y ≤ Σ 1/lcm(S) as structural lemma** (GPT-5.4 prime antichain counterexample at P=5003)
