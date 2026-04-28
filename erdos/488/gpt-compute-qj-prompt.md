# EP-488: Compute the Quotient-Core Moduli q_j
## Prompt for GPT with code execution — April 5, 2026

---

## WHAT TO COMPUTE

For primitive sets A = {a_1 < ... < a_k} with max(A) = M, we need to understand the "quotient-core moduli" q_j arising from the layer decomposition.

## BACKGROUND

The layer decomposition of F_A(x) (count of multiples of A up to x) is:

F_A(x) = Σ_{j=1}^k K_{Q_j}(⌊x/a_j⌋)

where K_Q(y) = #{n ≤ y : gcd(n, q) = 1 for all q in Q}.

The PEELING PROCESS constructs Q_j as follows (this is inclusion-exclusion rewritten layer-by-layer):

Step 1: Count multiples of a_1 up to x: that's ⌊x/a_1⌋.
But some of those are also multiples of a_2, a_3, etc. — overcounting.

The quotient-core Q_j is the set of "obstructions" at layer j: the quotients a_i/gcd(a_i, a_j) for i ≠ j that tell you which multiples of a_j are also multiples of other elements.

More precisely, for the j-th layer:
- Let b_{ij} = a_i / gcd(a_i, a_j) for each i ≠ j
- Q_j = {b_{ij} : b_{ij} > 1, i ≠ j}
- K_{Q_j}(y) counts integers ≤ y coprime to all elements of Q_j

The "sifting primes" P_j are all prime factors of elements of Q_j.
The "modulus" q_j = ∏_{p ∈ P_j} p.

## TASKS

### Task 1: Implement the peeling process

Write a function `compute_quotient_cores(A)` that, given a primitive set A:
1. For each j, computes Q_j = {a_i/gcd(a_i, a_j) : i ≠ j, a_i/gcd(a_i,a_j) > 1}
2. Computes P_j = set of all prime factors of elements of Q_j
3. Computes q_j = product of primes in P_j
4. Computes r_j = M / a_j
5. Computes ρ_j = ∏_{p ∈ P_j} (1 - 1/p)

### Task 2: Verify the layer decomposition

For each test set, verify that F_A(x) = Σ K_{Q_j}(⌊x/a_j⌋) for several values of x ∈ [M, 10M]. (This confirms we have the right Q_j.)

To compute K_Q(y): count integers n ∈ {1,...,y} such that gcd(n, q) = 1 for all q ∈ Q. (Equivalently, n is coprime to lcm of all elements of Q... no, coprime to EACH element of Q separately, which is the same as coprime to their lcm if they're squarefree, but use the exact definition to be safe.)

### Task 3: Compute the structural ratio

For each primitive set and each layer j, compute:
- r_j / q_j (the ratio that must be > 3 for "good" layers)
- c_j = r_j · ρ_j (main term contribution)
- e_j = (q_j + 1) · ρ_j (excursion bound)

Then compute:
- C = Σ c_j (total mean)
- E = Σ e_j (total excursion bound)
- The ratio E/C (want this < 1/3 for the proof to work)
- The "structural surplus" Σ ρ_j · (r_j - 3q_j - 2)

### Task 4: Scan over primitive sets

Generate primitive sets systematically:
- All primitive sets with max ≤ 30, |A| ≤ 6
- Random primitive sets with max ≤ 100, |A| ≤ 10
- Adversarial cases: sets with many "smooth" elements (elements with small prime factors), which should maximize q_j

For each, report:
- worst layer r_j/q_j ratio
- structural surplus Σ ρ_j(r_j - 3q_j - 2)
- whether the collective criterion E < C/3 holds

### Task 5: Also compute the ACTUAL excursions

For each layer j and each x ∈ {M, M+1, ..., 10M}:
- Compute T_j(x) = (M/x) · K_{Q_j}(⌊x/a_j⌋)
- Compute ε_j(x) = T_j(x) - c_j
- Record actual v_j = max ε_j(x) and u_j = max(-ε_j(x))

Compare actual (v_j, u_j) with theoretical bounds (q_j·ρ_j, q_j·ρ_j + ρ_j).
Report: how tight are the theoretical bounds?

Also compute:
- Actual V + 2U vs C (the collective criterion with ACTUAL excursions)
- Actual sup H / inf H (the EP-488 ratio)

### Task 6: Find the worst cases

Which primitive sets have the SMALLEST structural surplus?
Which have the LARGEST E/C ratio?
Do any come close to violating V + 2U < C with actual excursions?

## OUTPUT FORMAT

For each set, print one line:
A = {a1, ..., ak}, M = ..., E/C = ..., surplus = ..., actual ratio = ..., V+2U/C = ...

At the end, print summary statistics:
- worst E/C across all sets
- worst surplus across all sets  
- worst V+2U/C (actual) across all sets
- whether ANY set violates the theoretical criterion
- whether ANY set violates the actual criterion

## PYTHON STARTER CODE

```python
from math import gcd, prod
from functools import reduce
from sympy import factorint

def prime_factors(n):
    """Return set of prime factors of n."""
    if n <= 1:
        return set()
    return set(factorint(n).keys())

def is_primitive(A):
    """Check if A is a primitive set (no element divides another)."""
    A = sorted(A)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def compute_layers(A):
    """Compute quotient cores, moduli, and layer quantities for primitive set A."""
    A = sorted(A)
    k = len(A)
    M = A[-1]
    
    layers = []
    for j in range(k):
        a_j = A[j]
        r_j = M / a_j
        
        # Quotient core Q_j
        Q_j = set()
        for i in range(k):
            if i == j:
                continue
            g = gcd(A[i], a_j)
            b = A[i] // g
            if b > 1:
                Q_j.add(b)
        
        # Sifting primes
        P_j = set()
        for q in Q_j:
            P_j |= prime_factors(q)
        
        # Modulus
        q_j = prod(P_j) if P_j else 1
        
        # Coprime density
        rho_j = 1.0
        for p in P_j:
            rho_j *= (1 - 1/p)
        
        # Main term and excursion bound
        c_j = r_j * rho_j
        e_j = (q_j + 1) * rho_j
        
        layers.append({
            'a_j': a_j, 'r_j': r_j, 'Q_j': Q_j, 'P_j': P_j,
            'q_j': q_j, 'rho_j': rho_j, 'c_j': c_j, 'e_j': e_j
        })
    
    return layers

def K_Q(y, Q):
    """Count integers in {1,...,y} coprime to all elements of Q."""
    count = 0
    for n in range(1, y + 1):
        if all(gcd(n, q) == 1 for q in Q):
            count += 1
    return count

def compute_actual_excursions(A, layers):
    """Compute actual T_j(x), excursions, and EP-488 ratio."""
    A = sorted(A)
    M = A[-1]
    k = len(A)
    
    H_values = []
    actual_v = [0.0] * k
    actual_u = [0.0] * k
    
    for x in range(M, 10 * M + 1):
        H_x = 0.0
        for j in range(k):
            a_j = A[j]
            y_j = x // a_j
            Q_j = layers[j]['Q_j']
            T_j = (M / x) * K_Q(y_j, Q_j)
            eps_j = T_j - layers[j]['c_j']
            actual_v[j] = max(actual_v[j], eps_j)
            actual_u[j] = max(actual_u[j], -eps_j)
            H_x += T_j
        H_values.append(H_x)
    
    sup_H = max(H_values)
    inf_H = min(H_values)
    ratio = sup_H / inf_H if inf_H > 0 else float('inf')
    
    V_actual = sum(actual_v)
    U_actual = sum(actual_u)
    C = sum(l['c_j'] for l in layers)
    
    return {
        'ratio': ratio, 'sup': sup_H, 'inf': inf_H,
        'V': V_actual, 'U': U_actual, 'C': C,
        'budget': V_actual + 2 * U_actual,
        'budget_ratio': (V_actual + 2 * U_actual) / C if C > 0 else float('inf')
    }

# Generate primitive sets and test
# ... (add generation code here)
```

## IMPORTANT NOTES

1. The K_Q function above is O(y·|Q|) — fine for small M, slow for large M. For M > 100, use inclusion-exclusion instead of brute force.

2. The quotient-core Q_j definition above (using a_i/gcd(a_i,a_j)) is the SIMPLEST version. The actual peeling process in the layer decomposition may be slightly different — verify by checking F_A(x) = Σ K_{Q_j}(⌊x/a_j⌋) for test values.

3. If the decomposition doesn't match, try the alternative: Q_j = {a_i/a_j : a_j | a_i, i ≠ j}... but this can't happen for primitive sets (no divisibility). So Q_j should use the gcd-based quotients.

4. Priority: get Task 3 and Task 6 results first. The structural surplus is the key number.
