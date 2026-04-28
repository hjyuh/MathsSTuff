"""
Check R = S1 - 2*S2 for primitive sets.
Task 1: All primitive quadruples (dense + sparse) with max <= 200
Task 2: Dense sets with k=4,5,6 -- does R ever go negative?
Task 3: Find largest k0 where R > 0 for all dense sets
"""
from math import gcd
from itertools import combinations
from fractions import Fraction
import time

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def compute_R_exact(A):
    """Compute R = S1 - 2*S2 exactly using Fractions."""
    S1 = sum(Fraction(1, a) for a in A)
    S2 = Fraction(0)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            l = lcm2(A[i], A[j])
            S2 += Fraction(1, l)
    return S1 - 2 * S2, S1, S2

def compute_R_float(A):
    """Fast float version."""
    S1 = sum(1.0/a for a in A)
    S2 = 0.0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            S2 += gcd(A[i], A[j]) / (A[i] * A[j])
    return S1 - 2*S2, S1, S2

# ============================================
# TASK 1: R FOR ALL PRIMITIVE QUADRUPLES
# ============================================
print("=" * 70)
print("TASK 1: R = S1 - 2*S2 FOR PRIMITIVE QUADRUPLES")
print("=" * 70)

t0 = time.time()
count = 0
neg_count = 0
min_R = float('inf')
min_R_set = None
neg_examples = []

# Search all primitive quadruples with min >= 3, max <= 100
for a in range(3, 51):
    for b in range(a+1, 101):
        if b % a == 0:
            continue
        for c in range(b+1, 101):
            if c % a == 0 or c % b == 0:
                continue
            for d in range(c+1, 101):
                if d % a == 0 or d % b == 0 or d % c == 0:
                    continue
                A = [a, b, c, d]
                count += 1
                R, S1, S2 = compute_R_float(A)
                if R < min_R:
                    min_R = R
                    min_R_set = tuple(A)
                if R <= 0:
                    neg_count += 1
                    if neg_count <= 20:
                        neg_examples.append((tuple(A), R, S1))
                        # Verify with exact arithmetic
                        Re, _, _ = compute_R_exact(A)
                        print(f"  R<=0: {A}, R={float(Re):.8f}, S1={S1:.6f}")

        if count % 5000000 == 0:
            print(f"  ...{count/1e6:.1f}M quads, {neg_count} neg, "
                  f"min R={min_R:.6f} at {min_R_set}, {time.time()-t0:.0f}s")

elapsed = time.time() - t0
print(f"\nQuadruples checked: {count}")
print(f"R <= 0: {neg_count}")
print(f"Minimum R: {min_R:.8f} at {min_R_set}")
if min_R_set:
    Re, S1e, S2e = compute_R_exact(list(min_R_set))
    print(f"  Exact: R = {Re} = {float(Re):.10f}")
    print(f"  S1 = {S1e} = {float(S1e):.8f}")
    print(f"  2*S2 = {2*S2e} = {float(2*S2e):.8f}")
print(f"Time: {elapsed:.1f}s")

if neg_count > 0:
    print(f"\n{neg_count} quadruples with R <= 0:")
    for A, R, S1 in neg_examples[:10]:
        dense = "DENSE" if S1 > 2.0/A[0] else "sparse"
        print(f"  {A}: R={R:.6f}, S1={S1:.4f}, {dense}")
else:
    print("\nR > 0 FOR ALL PRIMITIVE QUADRUPLES with max <= 100!")

# ============================================
# TASK 2: R FOR DENSE SETS WITH k=5,6
# ============================================
print("\n" + "=" * 70)
print("TASK 2: R FOR DENSE SETS, k=5,6")
print("=" * 70)

for target_k in [5, 6]:
    t0 = time.time()
    count_k = 0
    neg_k = 0
    min_R_k = float('inf')
    min_R_k_set = None

    for a1 in range(3, 21):
        # Pool: elements not divisible by a1
        pool = [a1]
        for x in range(a1+1, 61):
            if x % a1 != 0:
                pool.append(x)

        for subset in combinations(pool[:30], target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            S1 = sum(1.0/x for x in A)
            if S1 <= 2.0/a1:
                continue  # sparse, skip

            count_k += 1
            R, _, _ = compute_R_float(A)
            if R < min_R_k:
                min_R_k = R
                min_R_k_set = tuple(A)
            if R <= 0:
                neg_k += 1
                if neg_k <= 10:
                    Re, _, _ = compute_R_exact(A)
                    print(f"  k={target_k} R<=0: {A}, R={float(Re):.8f}, S1={S1:.4f}")

    elapsed = time.time() - t0
    print(f"\n  k={target_k}: checked {count_k} dense sets, R<=0: {neg_k}, "
          f"min R={min_R_k:.6f} at {min_R_k_set}, {elapsed:.1f}s")

# ============================================
# TASK 3: FIND CRITICAL k0
# ============================================
print("\n" + "=" * 70)
print("TASK 3: FIND k0 WHERE R FIRST GOES NEGATIVE (DENSE SETS)")
print("=" * 70)

# For each k from 4 to 12, check if any dense set has R <= 0
# Use elements up to 40 for speed
for target_k in range(4, 13):
    t0 = time.time()
    count_k = 0
    neg_k = 0
    min_R_k = float('inf')
    min_R_k_set = None

    max_elem = min(40, 10 + 3 * target_k)  # scale search range with k
    for a1 in range(3, min(16, max_elem)):
        pool = [a1]
        for x in range(a1+1, max_elem + 1):
            if x % a1 != 0:
                pool.append(x)

        pool_lim = pool[:min(25, len(pool))]
        if len(pool_lim) < target_k:
            continue

        for subset in combinations(pool_lim, target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            S1 = sum(1.0/x for x in A)
            if S1 <= 2.0/a1:
                continue

            count_k += 1
            R, _, _ = compute_R_float(A)
            if R < min_R_k:
                min_R_k = R
                min_R_k_set = tuple(A)
            if R <= 0:
                neg_k += 1

    elapsed = time.time() - t0
    status = "ALL R>0" if neg_k == 0 else f"{neg_k} with R<=0"
    print(f"  k={target_k:2d}: {count_k:>8d} dense sets, {status}, "
          f"min R={min_R_k:.6f}" + (f" at {min_R_k_set}" if min_R_k_set else "")
          + f", {elapsed:.1f}s")
    if neg_k > 0 and min_R_k_set:
        Re, S1e, _ = compute_R_exact(list(min_R_k_set))
        print(f"         Exact min R = {float(Re):.8f}, S1 = {float(S1e):.6f}")

print("\nDONE.")
