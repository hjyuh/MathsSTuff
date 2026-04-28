# EP-488: Test the Up-Fold Conjecture R(A) ≤ R(C)
## For GPT with code execution — April 6, 2026

---

## THE IDEA (from Gemini, unverified)

For a primitive set A with M = max(A), define the "up-fold":
- For each a ∈ A, pick the smallest k_a such that c_a = a·k_a ∈ (M, 2M]
- Let C = {c_a : a ∈ A}

Properties (proved):
- C ⊂ (M, 2M] — by construction
- C is automatically primitive — any subset of (M, 2M] is an antichain
- EP-488 holds for C — it's compact (max ≤ 2·min)

**UNVERIFIED CLAIM:** R(A) ≤ R(C), where R(X) = sup G_X / inf G_X on [max(X), ∞).

If true: R(A) ≤ R(C) < 2, and EP-488 is proved.

## YOUR TASK: VERIFY OR DISPROVE R(A) ≤ R(C)

### Step 1: Implement the up-fold

```python
from math import gcd, ceil

def up_fold(A):
    """Map primitive set A to compact set C ⊂ (M, 2M]."""
    A = sorted(A)
    M = A[-1]
    C = []
    for a in A:
        # Find smallest k such that a*k > M
        k = ceil((M + 1) / a)  # smallest k with a*k > M
        c = a * k
        # Make sure c <= 2M
        if c > 2 * M:
            # This shouldn't happen since interval (M, 2M] has length M >= a
            # But handle edge case
            k = k  # already minimal
            c = a * k
        C.append(c)
    # Remove duplicates (different a's might map to same c)
    C = sorted(set(C))
    return C

def is_primitive(A):
    A = sorted(A)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True
```

### Step 2: Compute R(X) = sup G / inf G

```python
def compute_ratio(A, window_mult=10):
    """Compute sup G(x) / inf G(x) for x in [max(A), window_mult * max(A)]."""
    A = sorted(A)
    M = A[-1]
    
    sup_G = 0
    inf_G = float('inf')
    
    for x in range(M, window_mult * M + 1):
        # Count multiples of A up to x
        # Use inclusion-exclusion for exact count
        F = count_multiples(A, x)
        G = F / x
        sup_G = max(sup_G, G)
        inf_G = min(inf_G, G)
    
    return sup_G / inf_G if inf_G > 0 else float('inf')

def count_multiples(A, x):
    """Count |{n <= x : a|n for some a in A}| by inclusion-exclusion."""
    from itertools import combinations
    from math import gcd
    from functools import reduce
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def lcm_list(lst):
        return reduce(lcm, lst)
    
    total = 0
    for r in range(1, len(A) + 1):
        for S in combinations(A, r):
            L = lcm_list(S)
            if L > x:
                continue
            if r % 2 == 1:
                total += x // L
            else:
                total -= x // L
    return total
```

### Step 3: Scan and compare R(A) vs R(C)

```python
from itertools import combinations

def scan_upfold():
    results = []
    violations = 0
    
    # Generate all primitive sets with max <= 20, |A| <= 5
    for M in range(2, 21):
        for k in range(1, min(6, M)):
            # Generate primitive subsets of [2, M] containing M, of size k
            candidates = [a for a in range(2, M+1)]
            for combo in combinations(candidates, k):
                A = list(combo)
                if M not in A:
                    continue
                if not is_primitive(A):
                    continue
                
                C = up_fold(A)
                
                # Check C is primitive
                if not is_primitive(C):
                    # Duplicates or divisibility in C
                    # Record but skip
                    continue
                
                R_A = compute_ratio(A)
                R_C = compute_ratio(C)
                
                holds = R_A <= R_C + 1e-10  # small tolerance
                if not holds:
                    violations += 1
                
                results.append({
                    'A': A, 'C': C, 'R_A': R_A, 'R_C': R_C,
                    'holds': holds, 'diff': R_C - R_A
                })
    
    return results, violations

results, violations = scan_upfold()
print(f"Total sets tested: {len(results)}")
print(f"R(A) <= R(C) violations: {violations}")
print(f"Pass rate: {(len(results)-violations)/len(results)*100:.2f}%")

# Show worst cases
results.sort(key=lambda r: r['diff'])
print("\nWorst cases (smallest R(C) - R(A)):")
for r in results[:10]:
    print(f"  A={r['A']}, C={r['C']}, R(A)={r['R_A']:.6f}, R(C)={r['R_C']:.6f}, diff={r['diff']:.6f}")

print("\nBest cases (largest R(C) - R(A)):")
for r in results[-5:]:
    print(f"  A={r['A']}, C={r['C']}, R(A)={r['R_A']:.6f}, R(C)={r['R_C']:.6f}, diff={r['diff']:.6f}")
```

### Step 4: Handle edge cases

The up-fold can produce DUPLICATE values (two different a's map to the same c).
When this happens, |C| < |A|. Record these cases separately.

Also check: when A is already compact (all elements in (M/2, M]), 
C should equal A (each element maps to itself). Verify this.

### Step 5: Also test 5.4's counterexample family

Test A_N = {2p : p prime in [N, 1.1N]} ∪ {5p : p prime in [N, 1.1N]}
for N = 10, 20, 50, 100.

These have bounded ρ but growing compact excess. Does R(A) ≤ R(C) still hold?

## KEY QUESTION

Is R(A) ≤ R(C) for ALL primitive sets tested?

If yes: the up-fold direction is confirmed, and the proof reduces to
showing WHY R(A) ≤ R(C) (which might not need Kawamura's partitioning at all).

If no: find the smallest counterexample and report A, C, R(A), R(C).

## OUTPUT

Print summary:
```
UP-FOLD VERIFICATION
====================
Total tested: ...
R(A) <= R(C): ... (pass rate ...%)
Violations: ...

Duplicate collapses (|C| < |A|): ...
Already-compact cases: ...

Worst diff (closest to violation): A=..., R(A)=..., R(C)=...
```
