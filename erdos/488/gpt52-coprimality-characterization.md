# EP-488: GPT-5.2 Coprimality Characterization
## March 30, 2026

### The Key Formula (GPT-5.2, verified)

For q_a(t) = t/gcd(t,a):

  gcd(q_a(t₁), q_a(t₂)) = gcd(t₁,t₂) / gcd(a, gcd(t₁,t₂))

Therefore:

  **gcd(q_a(t₁), q_a(t₂)) > 1  ⟺  gcd(t₁,t₂) ∤ a**

### What this means

Non-coprime quotient-tail elements arise when two tail elements share a prime 
factor p that doesn't divide a (or share higher p-power than a contains).

### Computational finding (coprimality probe, 5000 systems)

- 22.8% of systems have non-coprime Q_a^{ex}
- But 0% have non-coprime ACTIVE moduli (q ≤ y at ratio peak)
- Every non-coprime pair has at least one element in the tail (q > y)

### The remaining question

For ACTIVE moduli (q_a(t) ≤ y, i.e., t ≤ (a/2)y), does gcd(t₁,t₂) | a always hold?

**Why it might be true:** Active moduli come from SMALL tail elements (t close to a). 
For t₁, t₂ near a, their common factors are constrained by the fact that t₁, t₂ > a 
(tail elements exceed max(a,b) for the pair), and primitivity prevents divisibility 
relationships. But this doesn't directly force gcd(t₁,t₂) | a.

**Why it might fail in theory:** Take a = 4. If t₁ = 15 (q = 15, active if y ≥ 15) 
and t₂ = 21 (q = 21, active if y ≥ 21), then gcd(15,21) = 3, 3 ∤ 4. Both are 
active if y ≥ 21. BUT: does this system satisfy F(s) ≥ 5 with these as the only 
active moduli? Need to check with actual primitive set constraints.

### Proof strategy if active coprimality holds

1. For active Q_{≤y}: coprime → CRT → density = δ_{active} + O(k/y)
   → oscillation W+ ≤ k (not 2^k)
2. For inactive Q_{>y}: handled by tail sum Σ 1/q = O(1/y)  
3. Combined: refined sufficient condition holds with margin

### Next step

Run enlarged computation specifically targeting systems where:
- |Q_active| ≥ 2
- Both active moduli come from composite tail elements
- Check gcd(t₁,t₂) vs a in every such case
