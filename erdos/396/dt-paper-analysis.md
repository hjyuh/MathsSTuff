# DT PAPER ANALYSIS — What It Gives and Doesn't Give for Problem 396
## March 16, 2026

---

## Paper: Dartyge & Tenenbaum (2005), "Sommes des chiffres de multiples d'entiers"
## Annales de l'Institut Fourier, 55(7), 2423-2474.

---

## Summary

DT studies the joint distribution of digit-sum vectors s_q(h₁n+k₁), ..., s_q(h_rn+k_r)
with uniform control in h and k. The main results are power-saving bounds for
exponential sums involving digit sums, and applications to equidistribution in APs.

## What DT Gives Us

### Theorem 2.1 (Main Exponential Sum Bound)
For our setup: q=p (odd prime), r=2, h=(1,2), k=(0,c).
Bounds |G_2(x,y; ϑ; α, (1,2), (0,c))| with power saving in y.
The bound is (equation 2.3):

|G_2| ≤ y(8 + 3D/h)e^{-δD/(80m²h)} + 4ρ^{E+D}

where h=2, m is a Dirichlet approximation denominator, δ and K depend on p and r.

### Corollary 2.10 (Equidistribution in APs)
For digit-sum congruence conditions s_q(h_jn) ≡ a_j (mod m_j) intersected with APs:

A(x; h, a, m; b, d) = (x/Δ) ∏(m*_j/m_j) + O(x^{1-c₀/(m²h_r log Kh_r)})

This is useful for computing the density of the carry-good set R_A in step 4.

### Theorem 2.5 (Density of Digit-Sum Conditions)
For almost all d, the digit-sum condition s_q(hd) ≢ a (mod m) holds for some small h.
This is related to showing carry-good residues exist.

## What DT Does NOT Give Us (Per Codex Review)

### 1. Threshold Events
DT controls CONGRUENCE CLASSES: s_q(hn) ≡ a (mod m).
The carry deficit κ < T is a THRESHOLD: s_p(n) + s_p(n+c) - s_p(2n+c) < T(p-1).
Cannot express κ < T as residue classes mod fixed m.
To approximate, need m ~ T(p-1), but then error exponent deteriorates as m².

### 2. Uniformity Across Primes
The error exponent in Corollary 2.10 is c₀/(m²h log(Kh)).
For different primes p, the modulus m and parameters change.
Not uniform in p — each prime gives a different (weaker) bound.

### 3. Three-Digit-Sum Problem
κ_p^{(c)}(n) involves s_p(n), s_p(n+c), and s_p(2n+c) — THREE digit sums.
DT requires h_j pairwise distinct. Taking h=(1,1,2) violates this.
Must work with r=2, h=(1,2), which doesn't capture the full carry structure.

## Where DT IS Used in Our Proof

1. **Step 4 (Depth-A truncation):** Corollary 2.10 gives equidistribution of digit-sum
   conditions in APs, which is needed to compute the density of R_A via CRT.

2. **Possibly medium primes:** Theorem 2.5 might help show that for primes Y < p ≤ √K,
   the digit-sum condition is satisfied for almost all K.

## The Replacement for Step 6

Instead of using DT for the high-depth completion, we use direct Markov chain
concentration on the carry process. This avoids all three issues above:
- No need to approximate thresholds by congruences
- Explicit constants at each fixed prime
- Natural 2-state chain, no three-digit-sum problem

See: markov-chain-gap-closure.md for the full argument.
