# EP-488: Corrected Compute Scan — Using L_j (Divisibility Avoidance)
## For GPT with code execution — April 5, 2026

---

## CRITICAL CONTEXT

A previous scan (148,885 sets) revealed that the coprimality-based layer
decomposition K_Q(y) = #{n ≤ y : gcd(n,q)=1} is WRONG for general primitive
sets. The correct decomposition uses DIVISIBILITY AVOIDANCE:

  B_j = {a_i / gcd(a_i, a_j) : i < j, quotient > 1}
  L_j(y) = #{n ≤ y : b ∤ n for every b ∈ B_j}
  F_A(x) = Σ_j L_j(⌊x/a_j⌋)     ← EXACT

This was verified in the previous scan. The previous scan also confirmed
EP-488 holds (true ratio max 1.9899), but the collective oscillation budget
V + 2U < C was tested on the WRONG coprimality surrogate (92% failure).

## YOUR TASK: RETEST V + 2U < C WITH THE CORRECT L_j

### Step 1: Implement the correct layer decomposition

For primitive set A = {a_1 < ... < a_k}, M = a_k:

```python
from math import gcd
from itertools import combinations

def compute_correct_layers(A):
    A = sorted(A)
    k = len(A)
    M = A[-1]
    layers = []
    
    for j in range(k):
        a_j = A[j]
        r_j = M / a_j
        
        # B_j: quotients from EARLIER elements only (i < j)
        B_j = set()
        for i in range(j):
            g = gcd(A[i], a_j)
            b = A[i] // g
            if b > 1:
                B_j.add(b)
        
        # Remove dominated elements: if b1 | b2, keep only b1
        # (b1 dividing b2 means "b1 ∤ n" is stricter than "b2 ∤ n")
        # Actually: we want ALL of them since L_j avoids ALL elements of B_j
        # The antichain reduction is optional for correctness, keep all.
        
        layers.append({
            'a_j': a_j,
            'r_j': r_j,
            'B_j': sorted(B_j),
        })
    
    return layers

def L_j(y, B_j):
    """Count integers in {1,...,y} not divisible by any b in B_j."""
    count = 0
    for n in range(1, y + 1):
        if all(n % b != 0 for b in B_j):
            count += 1
    return count

def L_j_density(B_j):
    """Compute asymptotic density d_j = lim L_j(y)/y via inclusion-exclusion."""
    from functools import reduce
    B = sorted(B_j)
    total = 0.0
    for r in range(len(B) + 1):
        for S in combinations(B, r):
            lcm_S = reduce(lambda a, b: a * b // gcd(a, b), S, 1)
            total += ((-1) ** r) / lcm_S
    return total
```

### Step 2: Compute T_j(x) and excursions with the correct L_j

For each primitive set A, for each x in [M, 10M]:

```python
def compute_correct_budget(A):
    A = sorted(A)
    M = A[-1]
    k = len(A)
    layers = compute_correct_layers(A)
    
    # Compute densities
    for layer in layers:
        layer['d_j'] = L_j_density(layer['B_j'])
        layer['c_j'] = layer['r_j'] * layer['d_j']
    
    C = sum(l['c_j'] for l in layers)
    
    # Compute actual T_j(x) and excursions
    actual_v = [0.0] * k  # upward excursion
    actual_u = [0.0] * k  # downward excursion
    H_values = []
    
    for x in range(M, 10 * M + 1):
        H_x = 0.0
        for j in range(k):
            a_j = A[j]
            y_j = x // a_j
            T_j = (M / x) * L_j(y_j, layers[j]['B_j'])
            eps_j = T_j - layers[j]['c_j']
            actual_v[j] = max(actual_v[j], eps_j)
            actual_u[j] = max(actual_u[j], -eps_j)
            H_x += T_j
        H_values.append(H_x)
    
    V = sum(actual_v)
    U = sum(actual_u)
    sup_H = max(H_values)
    inf_H = min(H_values)
    ratio = sup_H / inf_H if inf_H > 0 else float('inf')
    
    return {
        'A': A, 'M': M, 'k': k,
        'C': C, 'V': V, 'U': U,
        'budget': V + 2 * U,
        'budget_ratio': (V + 2 * U) / C if C > 0 else float('inf'),
        'budget_holds': V + 2 * U < C,
        'sup_H': sup_H, 'inf_H': inf_H,
        'true_ratio': ratio,
        'layers': layers,
        'actual_v': actual_v,
        'actual_u': actual_u,
    }
```

### Step 3: Scan primitive sets

Generate and test:

1. **All primitive sets with max ≤ 20, |A| ≤ 5** (exhaustive, should be manageable)
2. **Random primitive sets with max ≤ 50, |A| ≤ 8** (1000 sets)
3. **Adversarial: sets of consecutive integers {n, n+1, ..., n+k-1}** (these are always primitive)
4. **Adversarial: sets with elements near M** (compact-ish sets)
5. **Adversarial: A = {primes ≤ p}** for various p

For each set, report one line:
```
A = {...}, M = ..., C = ..., V+2U = ..., budget_holds = ..., 
budget_ratio = ..., true_ratio = ...
```

### Step 4: Key questions to answer

1. **What fraction of sets have V + 2U < C with the CORRECT L_j?**
   (Compare to the 7.67% from the coprimality model)

2. **Is there ANY set where the true EP-488 ratio exceeds 1.99?**

3. **For sets where V + 2U < C fails: how close is V + 2U to C?**
   Is the budget ratio (V+2U)/C close to 1, or wildly > 1?

4. **What do the B_j look like for worst-case sets?**
   How many active elements? What's lcm(B_j)?

5. **Correlation between budget failure and true ratio:**
   Do sets with high (V+2U)/C also have high true ratio?
   Or is the budget just too conservative even with the correct L_j?

### Step 5: If V + 2U < C fails broadly

If the budget still fails for most sets with the correct L_j, compute:

- The ACTUAL sup|Σ ε_j(x)| / C (the "phase mixing" ratio)
  This measures whether errors actually cancel in the sum, even though
  individual |ε_j| sums are large.

- Compare: Σ sup|ε_j| vs sup|Σ ε_j|
  If the latter is much smaller, Strategy B (anti-alignment) is viable.

### Step 6: Special analysis for compact sets

For sets with max/min ≤ 2 (compact), verify:
- B_j is typically empty or has few elements
- V + 2U < C should hold trivially
- True ratio is small

This confirms the existing Theorem 6 computationally.

## OUTPUT FORMAT

Print summary at end:
```
CORRECT L_j SCAN RESULTS
========================
Total sets tested: ...
V + 2U < C passed: ... (... %)
V + 2U < C failed: ... (... %)

Worst budget_ratio (V+2U)/C: ... at A = {...}
Worst true_ratio sup/inf: ... at A = {...}
Max true_ratio: ... (EP-488 holds if < 2)

Phase mixing ratio (avg): sup|Σε| / Σsup|ε| = ...
  (if close to 0, errors cancel; if close to 1, they don't)
```

## IMPORTANT NOTES

1. L_j(y, B_j) is O(y·|B_j|) brute force. For large M, use inclusion-exclusion:
   L_j(y) = Σ_{S ⊆ B_j} (-1)^|S| · ⌊y / lcm(S)⌋
   This is exact and much faster for small |B_j|.

2. The density d_j = L_j_density(B_j) uses exact inclusion-exclusion.
   For B_j = ∅ (principal layer j=0): d_j = 1 always.

3. VERIFY the decomposition: check F_A(x) = Σ L_j(⌊x/a_j⌋) for a few x values.
   If this fails, there's a bug.

4. Priority: get the budget pass rate (Step 4 question 1) and phase mixing
   ratio (Step 5) first. Everything else is secondary.
