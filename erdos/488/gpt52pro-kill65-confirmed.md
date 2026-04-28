# EP-488: 5.2 Pro — Kill #65 CONFIRMED (Swarm Repaired)
## April 7, 2026

## 5.4's challenges to Kill #65 (from earlier):
1. Simultaneity: must count elements bad at ONE fixed (n,m)
2. Support: each bad element needs actual ancestors in A

## 5.2's repair addresses BOTH:

### Construction:
n = 4M, m ≈ (113/20)M, so m/n ≈ 1.4125.

Simultaneity band for (s,t)=(4,7):
  I = (4M/5, 113M/140], length = M/140.

Every a ∈ I automatically has ⌊n/a⌋ = 4, ⌊m/a⌋ = 7.

### Swarm:
S = {a ∈ I : gcd(a,6)=1, P⁻(a) ≥ y ≈ log M, a composite}

### Ancestors:
A_anc = {2p, 3p : p prime, y ≤ p ≤ M/3}

### Support verified:
Each a ∈ S is composite with least prime factor ≥ y.
So ∃ prime p | a with p ∈ [y, M/3].
Then 2p, 3p ∈ A_anc ⊂ A, giving quotients exactly 2 and 3.

### No extra relevant obstructions:
Since y > 20, all other quotients from ancestors are > 20,
inert at compact scale t = 7. Relevant kernel = {2,3} exactly.

### Count:
|S| ≈ (M/140) · Π_{p<y}(1-1/p) ≈ cM/log log M (by Mertens)

### Excess:
Each E_a = 3n - 2m ≈ 0.7M > 0.
Σ E_j ≈ 0.7M · cM/log log M = c'M²/log log M.

### First layer:
a_1 = 2y ≈ 2 log M.
S_1 ≈ M²/log M.

### Kill confirmed:
S_1/Σ E_j ≈ (log log M)/(log M) → 0.

## STATUS

Kill #65 is now CONFIRMED, not just challenged.
5.4's objections were valid but 5.2 repaired the construction
to satisfy simultaneity + support explicitly.

S_1 ≥ Σ E_j is FALSE in general. Step 7 is dead.

The global charging route (ALL good layers, not just S_1)
remains the only viable architecture.

## KILL COUNT: 69
## PERCENTAGE: 80%
