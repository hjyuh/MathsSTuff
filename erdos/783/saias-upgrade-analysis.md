# EP-783: Saias Upgrade — Finite-N Precision
## Mahmoud's Analysis, March 30, 2026

### The Observation

Tao's proof of the weak form uses Dickman approximation Ψ(N, N^{1/e^C}) ~ Nρ(e^C), 
which is only first-order asymptotic. Saias' theorem upgrades this to finite-N.

### Saias' Theorem

For fixed ε > 0, in the range 1 ≤ u := log N / log y ≤ exp{(log y)^{3/5-ε}}:

  Ψ(N, y) = Λ(N, y)(1 + O(exp{-(log y)^{3/5-ε}}))

where Λ(N, y) := N ∫ ρ(u - v) d(⌊y^v⌋/y^v - v).

### Application to EP-783

**Upper bound side (improved):**

The prime-tail sieve has exact identity σ_N(P(y;N)) = Ψ(N,y)/N.

Choosing y = y(N,C) maximal such that Σ_{y<p≤N} 1/p ≤ C:

  Σ(N,C) ≤ Λ(N, y(N,C))/N + O(exp{-(log N)^{3/5-ε}})

Error far smaller than any power of 1/log N. All boundary-layer sensitivity at 
scale N/(log N)^2 captured by Λ.

Can optimize y within boundary layer y = N^{1/w} exp(θ/log N) by analyzing Λ 
without analytic remainder contamination.

**Lower bound side (what's still needed):**

1. Finite-N Hildebrand: upgrade his O(1/log^c N) error for prime moduli to 
   O(exp{-(log N)^{3/5-ε}}) matching Saias
2. Finite-N Tao reduction: quantify the ε-errors in Lemmas 2.2-2.5 to get 
   comparable precision for coprime → prime reduction

Step 2 is likely straightforward (Tao's lemmas are already quantitative).
Step 1 requires importing Saias machinery into Hildebrand's Main Lemma framework.

### What Remains Fully Open

Full classification of minimizer sets — even with Saias precision, we only know 
the prime-tail competitor achieves Λ/N. We don't know if other admissible sets 
can beat it at finite N. Hunter notes small improving perturbations exist.

### Source

This analysis was developed by Mahmoud after reading:
- Tao, "Sieving by coprime numbers" (Feb 22, 2026)  
- Hildebrand, "Quantitative mean value theorems II" (1987)
- EP-783 forum thread (Saias upgrade discussion)
