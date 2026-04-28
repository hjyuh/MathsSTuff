"""
Compute the LCM lattice for primitive sets.
1. |L_A| = number of distinct lcms of all non-empty subsets
2. Compare to 2^|A|
3. Mobius function sum for small examples
"""
from math import gcd
from itertools import combinations
from collections import defaultdict

def lcm2(a, b):
    return a * b // gcd(a, b)

def lcm_set(S):
    l = S[0]
    for x in S[1:]:
        l = lcm2(l, x)
    return l

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def all_subset_lcms(A):
    """Return set of all lcms of non-empty subsets."""
    lcms = set()
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            lcms.add(lcm_set(combo))
    return lcms

def lcm_lattice_with_mobius(A):
    """Compute the LCM lattice and Mobius function.
    The lattice L has bottom = 1 (lcm of empty set) and elements = all subset lcms.
    Partial order: d1 <= d2 iff d1 | d2.
    Mobius function mu(1, d) computed by inclusion on the lattice.
    """
    # Get all lcms including 1 (empty set convention)
    lcms = {1}  # bottom element
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            lcms.add(lcm_set(combo))
    lcms = sorted(lcms)

    # Build divisibility poset: d1 covers d2 iff d1 | d2 and no d3 with d1|d3|d2
    # For Mobius: mu(1, 1) = 1, mu(1, d) = -sum_{d' | d, d' != d, d' in L} mu(1, d')
    mu = {}
    mu[1] = 1
    for d in lcms:
        if d == 1:
            continue
        mu[d] = 0
        for d2 in lcms:
            if d2 < d and d % d2 == 0 and d2 in mu:
                mu[d] -= mu[d2]

    return lcms, mu

# ============================================
# PART 1: Small examples
# ============================================
print("LCM LATTICE ANALYSIS")
print("=" * 60)

small_examples = [
    [3, 5, 7],           # coprime triple
    [6, 10, 15],         # non-coprime triple (all share factors)
    [4, 6, 10, 14],      # = 2*{2,3,5,7}
    [4, 6, 9, 10],       # mixed
    [4, 6, 9, 10, 14, 15],  # larger non-coprime
    [2, 3, 5, 7],        # coprime quad (primes)
    [3, 4, 5, 7],        # coprime quad
    [4, 6, 10, 14, 22, 26],  # = 2*{2,3,5,7,11,13}
]

for A in small_examples:
    A = sorted(A)
    if not is_primitive(A):
        print(f"\n{A}: NOT PRIMITIVE")
        continue
    k = len(A)
    lcms = all_subset_lcms(A)
    lcm_list, mu = lcm_lattice_with_mobius(A)

    # Check coprimality
    cop = all(gcd(A[i],A[j])==1 for i in range(k) for j in range(i+1,k))

    # Mobius sum
    mu_sum = sum(abs(mu[d]) for d in lcm_list)
    mu_sum_nonbottom = sum(abs(mu[d]) for d in lcm_list if d > 1)

    print(f"\nA = {A} ({'coprime' if cop else 'non-coprime'})")
    print(f"  |A| = {k}, 2^|A| = {2**k}")
    print(f"  |L_A| = {len(lcms)} (distinct lcms of non-empty subsets)")
    print(f"  |L_A|/2^|A| = {len(lcms)/(2**k):.4f}")
    print(f"  Lattice size (incl bottom 1) = {len(lcm_list)}")
    print(f"  sum |mu(1,d)| = {mu_sum}")
    print(f"  sum |mu(1,d)| for d>1 = {mu_sum_nonbottom}")

    if k <= 5:
        print(f"  Lattice elements: {lcm_list[:30]}{'...' if len(lcm_list)>30 else ''}")
        # Show Mobius values
        print(f"  Mobius values:")
        for d in lcm_list[:20]:
            print(f"    mu(1,{d}) = {mu[d]}")

# ============================================
# PART 2: Scaling set A = {2p : p <= P}
# ============================================
print("\n" + "=" * 60)
print("SCALING SETS A = {2p : p prime, p <= P}")
print("=" * 60)

for P in [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]:
    primes = [p for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73] if p <= P]
    A = [2*p for p in primes]
    k = len(A)
    if k > 18:  # 2^18 = 262144 subsets -- feasible
        print(f"  P={P}: |A|={k}, 2^|A|={2**k} -- skipping (too large)")
        continue

    lcms = all_subset_lcms(A)

    # For the coprime base {primes}: each subset has distinct lcm (product)
    # For the scaled version: lcms may collide

    cop = all(gcd(A[i],A[j])==1 for i in range(k) for j in range(i+1,k))

    print(f"  P={P:2d}: |A|={k:2d}, 2^|A|={2**k:>8d}, "
          f"|L_A|={len(lcms):>8d}, ratio={len(lcms)/(2**k):.4f}, "
          f"{'coprime' if cop else 'non-coprime'}")

# ============================================
# PART 3: Compare coprime vs non-coprime lattice sizes
# ============================================
print("\n" + "=" * 60)
print("COPRIME VS NON-COPRIME LATTICE COMPARISON")
print("=" * 60)

# For coprime sets: every subset has a DISTINCT lcm (= product of elements)
# So |L_A| = 2^k - 1 (all non-empty subsets give distinct lcms)

# For non-coprime: lcms can collide, so |L_A| < 2^k - 1

# Compare pairs
print("\nPrimitive pairs:")
for A in [[3,5], [3,7], [4,6], [6,10], [6,15], [10,15]]:
    if not is_primitive(A): continue
    lcms = all_subset_lcms(A)
    cop = gcd(A[0],A[1]) == 1
    print(f"  {A}: |L|={len(lcms)}, 2^k-1={2**len(A)-1}, "
          f"{'coprime' if cop else f'non-coprime (gcd={gcd(A[0],A[1])})'}")

# Triples
print("\nPrimitive triples:")
for A in [[3,5,7], [6,10,15], [4,6,9], [4,6,10], [3,4,5]]:
    if not is_primitive(A): continue
    lcms = all_subset_lcms(A)
    cop = all(gcd(A[i],A[j])==1 for i in range(3) for j in range(i+1,3))
    print(f"  {A}: |L|={len(lcms)}, 2^k-1={2**len(A)-1}, "
          f"{'coprime' if cop else 'non-coprime'}")

# Quads
print("\nPrimitive quadruples:")
for A in [[2,3,5,7], [4,6,10,14], [4,6,9,10], [6,10,14,15]]:
    if not is_primitive(A): continue
    lcms = all_subset_lcms(A)
    cop = all(gcd(A[i],A[j])==1 for i in range(4) for j in range(i+1,4))
    print(f"  {A}: |L|={len(lcms)}, 2^k-1={2**len(A)-1}, "
          f"{'coprime' if cop else 'non-coprime'}")

print("\nDONE.")
