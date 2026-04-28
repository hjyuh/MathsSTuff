# EP-488: GPT-5.4 Pro Structural Analysis of (RQ_q)
## April 3, 2026

## Key New Results

### 1. Exact Row Parametrization
Everything depends on (s, Δ) where q = p+s (s ∈ {0,...,4}) and Δ = pU - x.
Active row sets, collision carriers, and capacities all have closed-form expressions.

### 2. Collision Carriers Are Single APs
For each collision distance d, the set S_{q,q-d}(x) is a single arithmetic progression
mod v_d = (q-d)/gcd(q,d) inside a carrier interval of length λ_d.
Carriers are NESTED: λ_1 ≥ λ_2 ≥ ... ≥ λ_s.

### 3. Distance-d Extinction (PROVED)
If q(t-1) < dU, then S_{q,q-d} = ∅.
This kills d=3,4 collisions in most pre-peak cases.

### 4. Partial (RQ_q) for s=1, Δ ≤ N-t (PROVED)
C_q ≤ ⌈Δ/q⌉ ≤ ⌈Δ/(q-1)⌉ = E_{q-1}.

### 5. s=2 Reduces to Two Coprime Moduli (PROVED)
gcd(v_1, v_2) = 1 always. So the collision union is two coprime APs on nested carriers.

### 6. The Real Obstruction (IDENTIFIED)
Pair-sum fails only when one base hits both d=1 and d=2 streams.
But the UNION corrects this: |T_1 ∪ T_2| = |T_1| + |T_2| - |T_1 ∩ T_2| ≤ E_{q-1}.
This is a TWO-MODULUS OVERLAP-CORRECTION LEMMA.

### 7. Computational Finding
No pre-peak d=3 or d=4 collisions found in tested range (a ≤ 61, k ∈ {2,3,4}).
Every pair-sum excess is exactly 1, repaired by exactly 1 overlap.

## The Bridge Lemma (UNPROVED but precisely stated)
Prove: for two coprime moduli v_1, v_2 on nested carriers I_2 ⊆ I_1,
|T_1 ∪ T_2| ≤ E_{q-1}(x)
where T_i = I_i ∩ v_i·ℤ.

This is the exact remaining step for a fully analytic proof of (RQ_q).

## Relationship to Other Models
- Gemini proved (RQ_q) computationally (a ≤ 211) + continuous analysis (a ≥ 212)
- GPT-5.4 Pro provides the STRUCTURAL explanation for why it's true
- The two-modulus lemma would give a clean analytic proof without finite verification
- These are complementary, not competing

## Status
- Multiple rigorous lemmas proved
- Problem reduced to a clean two-modulus statement
- (RQ_q) itself may already be proved via finite+continuous route
