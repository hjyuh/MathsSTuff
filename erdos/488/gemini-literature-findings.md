# EP-488: Gemini Literature Findings — The LCM-Lattice Approach
## April 4, 2026

## THE KEY INSIGHT

The discrepancy C is bounded by Σ|μ_L(1,d)| over the LCM-lattice L_A,
NOT by 2^k (number of subsets).

For coprime sets: L_A = Boolean lattice, |L_A| = 2^k, C ~ 2^{k/2}.
For non-coprime: |L_A| << 2^k, massive Möbius cancellation, C is small.

This explains why actual C ≈ 47 for k=21 non-coprime sets.

## SPECIFIC REFERENCES TO LOOK UP

1. **Gasharov-Peeva-Welker**: LCM lattices of monomial ideals.
   Shellability → bounded Betti numbers → bounded |Σ μ|.
   Paper: "Coordinate subspace arrangements and free resolutions"

2. **Rota's Crosscut Theorem**: Controls IE cancellation via lattice topology.
   The Möbius function of a shellable lattice has bounded alternating sum.

3. **Hall-Tenenbaum "Divisors"**: Error terms in density of multiples.
   Exactly our Σ c_d {x/d} sum. Chapter on primitive sequences.

4. **Koukoulopoulos**: Modern multiplicative number theory approach
   to density of multiples and IE oscillation.

5. **Behrend's Theorem / Besicovitch sequences**: The quotient-core
   recursion δ_A = δ_{A'} + (1-δ_{Q_a})/a appears in this context.

## HOW THIS CLOSES THE GAP

Step 1: Prove |L_A| = poly(k, number of distinct prime factors) for
        non-coprime primitive sets. (Should follow from antichain structure.)

Step 2: Prove C ≤ |L_A|/2 using Rota/GPW shellability.

Step 3: For non-coprime dense sets: |L_A| is polynomial → C is polynomial
        → discrepancy tail gives finite horizon → EP-488.

Step 4: Coprime sets already handled by the product-exponential proof.

## ACTION ITEMS

1. Send GPT-5.4 Pro or Claude Code: "Compute |L_A| for the counterexample
   A = {2p : p ≤ 73}. How many distinct lcm's are there? Compare to 2^21."

2. Look up Gasharov-Peeva-Welker. The key theorem bounds the total
   Betti number of the LCM lattice, which bounds Σ|μ|.

3. Apply the bound: if Σ|μ_L(1,d)| ≤ poly(|L_A|), then
   C ≤ poly(|L_A|)/2 and the tail closes.
