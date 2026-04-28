# EP-488: GPT-5.4 Periodic Regime Analysis
## March 31, 2026

### Bug found and fixed
Mean-zero claim Σc(r)=0 is FALSE. Correction: F(x) = δx + (δ-1)/2 + c̃(x mod P) with Σc̃(r)=0.

### Key insight: MONOTONICITY BY RESIDUE CLASS
For fixed residue r (mod P), F(r+tP)/(r+tP) is monotone in t.
Therefore sup and inf of F(x)/x for x ≥ max(A) are determined by FIRST WINDOW only.

### Singleton-extremal conjecture (could close EP-488)
For fixed M = max(A), the worst density span sup/inf is achieved by A = {M},
with sharp value 2 - 1/M.

Checked exhaustively for all primitive A with max(A) ≤ 12.
If true → EP-488 is proved completely.

### The exact formula
F(x) = Σ_d λ(d)⌊x/d⌋ = δx - Σ_d λ(d){x/d}
where λ(d) = Σ_{lcm(S)=d} (-1)^{|S|+1}, and Σ_d λ(d) = 1.

### Four recommended routes
1. Singleton-extremal: prove adding elements can't increase the span (compression)
2. Dense/sparse split: if 2F(M)/M > 1, done trivially. Only sparse systems matter.
3. Harmonic-interval matching: multiples in (M/(j+1), M/j]
4. lcm-lattice Fourier: one-sided dominance of sawtooth combination

### Killed approaches: now 19
19. Mean-zero periodic correction (GPT-5.4: singleton counterexample to Σc(r)=0)

### Status
The singleton-extremal conjecture is the cleanest remaining target.
If proved, EP-488 is completely resolved.
