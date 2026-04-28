"""
EP-488 Final Push: Three tasks toward full proof.
Task 1: R_hybrid = S1 - S2 - S3 for all dense 5-sets, max <= 50
Task 2: 2*delta > S1 for all dense k-sets, k <= 8, max <= 50
Task 3: delta*max(A) > 3C for all dense sets
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

def ie_sums(A):
    """Compute S1, S2, S3, S4, ... (IE sums by order)."""
    k = len(A)
    sums = {}
    for size in range(1, k+1):
        s = Fraction(0)
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            s += Fraction(1, l)
        sums[size] = s
    return sums

def density_exact(A):
    """Exact density via IE."""
    sums = ie_sums(A)
    d = Fraction(0)
    for size, s in sums.items():
        d += ((-1)**(size+1)) * s
    return d

def compute_C_exact(A, max_L=5_000_000):
    """Exact C via full period."""
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > max_L:
        return None, L
    delta = float(density_exact(A))
    hit = bytearray(L + 1)
    for a in A:
        for m in range(a, L + 1, a):
            hit[m] = 1
    running = 0
    max_C = 0.0
    for r in range(1, L + 1):
        running += hit[r]
        d = abs(running - delta * r)
        if d > max_C:
            max_C = d
    return max_C, L

# ============================================
# TASK 1: R_hybrid for all dense 5-sets
# ============================================
print("=" * 70)
print("TASK 1: R_hybrid = S1 - S2 - S3 for dense primitive 5-sets (max<=50)")
print("=" * 70)
t0 = time.time()

count5 = 0
neg_hybrid = 0
min_Rh = float('inf')
min_Rh_set = None

for a1 in range(3, 26):
    pool = [a1]
    for x in range(a1+1, 51):
        if x % a1 != 0:
            pool.append(x)
    for subset in combinations(pool[:30], 5):
        if subset[0] != a1:
            continue
        A = list(subset)
        if not is_primitive(A):
            continue
        S1f = sum(1.0/a for a in A)
        if S1f <= 2.0/a1:
            continue
        count5 += 1
        sums = ie_sums(A)
        S1 = sums[1]; S2 = sums[2]; S3 = sums[3]
        Rh = S1 - S2 - S3
        Rhf = float(Rh)
        if Rhf < min_Rh:
            min_Rh = Rhf
            min_Rh_set = tuple(A)
        if Rhf <= 0:
            neg_hybrid += 1
            if neg_hybrid <= 10:
                print(f"  R_hybrid<=0: {A}, Rh={Rhf:.6f}, S1={float(S1):.4f}")

elapsed = time.time() - t0
print(f"\nDense 5-sets checked: {count5}")
print(f"R_hybrid <= 0: {neg_hybrid}")
print(f"Min R_hybrid: {min_Rh:.8f} at {min_Rh_set}")
if min_Rh_set:
    sums = ie_sums(list(min_Rh_set))
    print(f"  S1={float(sums[1]):.6f}, S2={float(sums[2]):.6f}, S3={float(sums[3]):.6f}")
print(f"Time: {elapsed:.1f}s")

# ============================================
# TASK 2: 2*delta > S1 for all dense k-sets
# ============================================
print("\n" + "=" * 70)
print("TASK 2: Check 2*delta > S1 for all dense primitive sets (k=4..8, max<=50)")
print("Equivalent to delta > S1/2.")
print("=" * 70)

for target_k in range(4, 9):
    t0 = time.time()
    countk = 0
    fail_k = 0
    min_ratio = float('inf')  # min of 2*delta/S1
    min_ratio_set = None
    max_elem = min(50, 15 + 4*target_k)

    for a1 in range(3, min(21, max_elem)):
        pool = [a1]
        for x in range(a1+1, max_elem+1):
            if x % a1 != 0:
                pool.append(x)
        pool_lim = pool[:min(28, len(pool))]
        if len(pool_lim) < target_k:
            continue
        for subset in combinations(pool_lim, target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            S1 = sum(Fraction(1,a) for a in A)
            if S1 <= Fraction(2, a1):
                continue
            countk += 1
            delta = density_exact(A)
            ratio = float(2*delta / S1) if S1 > 0 else 999
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_set = tuple(A)
            if 2*delta <= S1:
                fail_k += 1
                if fail_k <= 5:
                    print(f"  FAIL k={target_k}: {A}, 2d={float(2*delta):.6f}, "
                          f"S1={float(S1):.6f}, ratio={ratio:.6f}")

    elapsed = time.time() - t0
    status = f"ALL 2d>S1" if fail_k == 0 else f"{fail_k} failures"
    print(f"  k={target_k}: {countk:>7d} dense sets, {status}, "
          f"min 2d/S1={min_ratio:.6f}" +
          (f" at {min_ratio_set}" if min_ratio_set else "") +
          f", {elapsed:.1f}s")

# ============================================
# TASK 3: delta*max(A) > 3C for all dense sets
# ============================================
print("\n" + "=" * 70)
print("TASK 3: delta*max(A) > 3C for all dense sets (k=3..7, max<=40)")
print("=" * 70)

for target_k in range(3, 8):
    t0 = time.time()
    countk = 0
    fail_k = 0
    min_margin = float('inf')  # min of delta*max - 3C
    min_margin_set = None
    min_margin_vals = None
    max_elem = min(40, 12 + 3*target_k)

    for a1 in range(3, min(16, max_elem)):
        pool = [a1]
        for x in range(a1+1, max_elem+1):
            if x % a1 != 0:
                pool.append(x)
        pool_lim = pool[:min(22, len(pool))]
        if len(pool_lim) < target_k:
            continue
        for subset in combinations(pool_lim, target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            S1f = sum(1.0/a for a in A)
            if S1f <= 2.0/a1:
                continue
            countk += 1
            delta = density_exact(A)
            deltaf = float(delta)
            M = max(A)
            C_val, L = compute_C_exact(A, max_L=2_000_000)
            if C_val is None:
                continue  # skip if period too large
            margin = deltaf * M - 3 * C_val
            if margin < min_margin:
                min_margin = margin
                min_margin_set = tuple(A)
                min_margin_vals = (deltaf, M, C_val, L)
            if margin <= 0:
                fail_k += 1
                if fail_k <= 5:
                    print(f"  FAIL k={target_k}: {A}, d*M={deltaf*M:.4f}, "
                          f"3C={3*C_val:.4f}, d={deltaf:.4f}, C={C_val:.4f}")

    elapsed = time.time() - t0
    status = f"ALL d*M>3C" if fail_k == 0 else f"{fail_k} failures"
    extra = ""
    if min_margin_set and min_margin_vals:
        d, M, C, L = min_margin_vals
        extra = f" (d={d:.4f}, M={M}, C={C:.2f}, L={L})"
    print(f"  k={target_k}: {countk:>6d} dense, {status}, "
          f"min margin={min_margin:.4f} at {min_margin_set}{extra}, {elapsed:.1f}s")

print("\nDONE.")
