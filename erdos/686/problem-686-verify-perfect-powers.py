"""
Problem 686 — Perfect Power Verification Script
Checks whether perfect powers N can be written as:
    N = prod(m+1, ..., m+k) / prod(n+1, ..., n+k)
for some k >= 2 and m >= n+k (non-overlapping blocks).

Key question: do ALL perfect powers fail, or just some?
If all fail up to 10000, the conjecture sharpens to:
"every non-perfect-power N >= 2 is representable."

Author: Mahmoud (pipeline orchestration) + Claude (implementation)
Date: March 14, 2026
"""

import math
from itertools import count

def is_perfect_power(n):
    """Check if n is a perfect power (n = a^b for some a >= 2, b >= 2)."""
    if n < 4:
        return False
    for b in range(2, int(math.log2(n)) + 1):
        a = round(n ** (1/b))
        for candidate in [a - 1, a, a + 1]:  # check neighbors due to float imprecision
            if candidate >= 2 and candidate ** b == n:
                return True
    return False

def consecutive_product(start, k):
    """Compute (start+1)(start+2)...(start+k) = prod_{i=1}^{k} (start + i)."""
    result = 1
    for i in range(1, k + 1):
        result *= (start + i)
    return result

def check_representable(N, max_k=50, max_n=500):
    """
    Check if N can be written as a ratio of two equal-length
    products of consecutive integers with non-overlapping blocks.
    
    Returns (True, k, n, m) if found, (False, None, None, None) if not.
    """
    for k in range(2, max_k + 1):
        for n in range(0, max_n + 1):
            denom = consecutive_product(n, k)
            numer_needed = N * denom
            
            # We need prod(m+1,...,m+k) = numer_needed with m >= n+k
            # The product of k consecutive integers starting at m+1 is
            # (m+1)(m+2)...(m+k). We need to find m such that this equals numer_needed.
            
            # Lower bound: m >= n+k (non-overlapping)
            m_min = n + k
            
            # The product (m+1)...(m+k) grows roughly as m^k for large m.
            # Upper bound: (m+k)^k >= numer_needed, so m <= numer_needed^(1/k)
            if numer_needed <= 0:
                continue
            m_upper = int(numer_needed ** (1.0/k)) + 2
            
            for m in range(m_min, min(m_upper + 1, m_min + 10000)):
                prod_m = consecutive_product(m, k)
                if prod_m == numer_needed:
                    return (True, k, n, m)
                elif prod_m > numer_needed:
                    break  # products only grow from here
    
    return (False, None, None, None)

def find_perfect_powers(limit):
    """Find all perfect powers up to limit."""
    powers = set()
    for n in range(2, limit + 1):
        if is_perfect_power(n):
            powers.add(n)
    return sorted(powers)

def main():
    LIMIT = 10000
    MAX_K = 80      # search up to k=80
    MAX_N = 1000    # search n up to 1000
    
    print(f"Problem 686 — Perfect Power Verification")
    print(f"Checking all perfect powers N <= {LIMIT}")
    print(f"Search bounds: k <= {MAX_K}, n <= {MAX_N}")
    print(f"=" * 70)
    
    perfect_powers = find_perfect_powers(LIMIT)
    print(f"\nFound {len(perfect_powers)} perfect powers up to {LIMIT}")
    print(f"First 20: {perfect_powers[:20]}")
    print()
    
    representable = []
    not_representable = []
    
    for i, N in enumerate(perfect_powers):
        result = check_representable(N, max_k=MAX_K, max_n=MAX_N)
        
        if result[0]:
            _, k, n, m = result
            representable.append((N, k, n, m))
            status = f"YES  k={k}, n={n}, m={m}"
            # Verify
            numer = consecutive_product(m, k)
            denom = consecutive_product(n, k)
            assert numer == N * denom, f"Verification failed for N={N}!"
        else:
            not_representable.append(N)
            status = "NO   (no representation found)"
        
        # Identify the power structure
        power_str = ""
        for b in range(2, int(math.log2(N)) + 2):
            a = round(N ** (1/b))
            for candidate in [a-1, a, a+1]:
                if candidate >= 2 and candidate ** b == N:
                    power_str += f" = {candidate}^{b}"
                    break
        
        print(f"  N = {N:>6}{power_str:20s} -> {status}")
        
        # Progress indicator
        if (i + 1) % 25 == 0:
            print(f"  ... checked {i+1}/{len(perfect_powers)} perfect powers ...")
    
    print(f"\n{'=' * 70}")
    print(f"RESULTS SUMMARY")
    print(f"{'=' * 70}")
    print(f"Perfect powers checked: {len(perfect_powers)}")
    print(f"Representable:          {len(representable)}")
    print(f"Not representable:      {len(not_representable)}")
    
    if representable:
        print(f"\nREPRESENTABLE PERFECT POWERS:")
        for N, k, n, m in representable:
            numer_prod = " × ".join(str(m+i) for i in range(1, min(k+1, 6)))
            if k > 5:
                numer_prod += " × ..."
            denom_prod = " × ".join(str(n+i) for i in range(1, min(k+1, 6)))
            if k > 5:
                denom_prod += " × ..."
            print(f"  N={N}: ({numer_prod}) / ({denom_prod})  [k={k}]")
    
    if not_representable:
        print(f"\nNOT REPRESENTABLE (within search bounds):")
        # Group by type
        squares_only = [n for n in not_representable if is_perfect_power(n) 
                       and any(round(n**(1/2))**2 == n for _ in [1])]
        print(f"  Count: {len(not_representable)}")
        print(f"  Values: {not_representable[:30]}{'...' if len(not_representable) > 30 else ''}")
    
    print(f"\n{'=' * 70}")
    if len(not_representable) == len(perfect_powers):
        print("CONCLUSION: NO perfect power found representable.")
        print("Conjecture: Problem 686 holds for all non-perfect-powers,")
        print("and NO perfect power N >= 4 is representable.")
    elif len(representable) > 0 and len(not_representable) > 0:
        print("CONCLUSION: MIXED — some perfect powers are representable, some are not.")
        print("The obstruction is more subtle than just 'perfect power'.")
        print("Investigate what distinguishes representable from non-representable.")
    elif len(not_representable) == 0:
        print("CONCLUSION: ALL perfect powers are representable!")
        print("The {4,25,49,64,81} failures were due to insufficient search bounds.")
    
    # Save results
    with open("problem-686-perfect-power-results.tsv", "w") as f:
        f.write("N\tis_representable\tk\tn\tm\tpower_factorization\n")
        for N, k, n, m in representable:
            f.write(f"{N}\tYES\t{k}\t{n}\t{m}\t\n")
        for N in not_representable:
            f.write(f"{N}\tNO\t\t\t\t\n")
    
    print(f"\nResults saved to problem-686-perfect-power-results.tsv")

if __name__ == "__main__":
    main()
