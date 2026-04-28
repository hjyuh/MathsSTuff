"""
Compute discrepancy C for primitive sets across a wide range.
Key questions:
1. Is C < 3 universal for dense primitive sets?
2. How does C scale with k and a?
3. What's the max C for consecutive triples {a, a+1, a+2}?
"""
from math import gcd
from itertools import combinations
import time

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def density_ie(A):
    total = 0.0
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            total += ((-1)**(size+1)) / l
    return total

def compute_C(A, horizon=None):
    """Compute discrepancy C = max |F(x) - delta*x| via sieve."""
    delta = density_ie(A)
    M = max(A)
    if horizon is None:
        horizon = max(2000, 30 * M)
    hit = bytearray(horizon + 1)
    for a in A:
        for m in range(a, horizon + 1, a):
            hit[m] = 1
    running = 0
    max_disc = 0.0
    for x in range(1, horizon + 1):
        running += hit[x]
        d = abs(running - delta * x)
        if d > max_disc:
            max_disc = d
    return max_disc, delta

# ============================================
# PART 1: CONSECUTIVE TRIPLES {a, a+1, a+2}
# ============================================
print("=" * 70)
print("PART 1: DISCREPANCY C FOR CONSECUTIVE TRIPLES {a, a+1, a+2}")
print("=" * 70)

for a in list(range(3, 30)) + [50, 100, 200, 300, 500, 750, 1000]:
    A = [a, a+1, a+2]
    if not is_primitive(A):
        continue
    h = max(3000, 50*a)
    C, delta = compute_C(A, horizon=h)
    print(f"  a={a:4d}: C={C:.4f}, delta={delta:.6f}, a*delta={a*delta:.4f}, "
          f"(a-1)*delta={(a-1)*delta:.4f}")

# ============================================
# PART 2: NON-CONSECUTIVE TRIPLES (WORST CASE SEARCH)
# ============================================
print("\n" + "=" * 70)
print("PART 2: WORST-C TRIPLES (non-consecutive)")
print("=" * 70)

worst_C = 0
worst_A = None
count = 0
for a in range(3, 80):
    for b in range(a+1, min(a+120, 300)):
        if b % a == 0:
            continue
        for c in range(b+1, min(b+120, 300)):
            if c % a == 0 or c % b == 0:
                continue
            A = [a, b, c]
            count += 1
            h = max(1000, 15*c)
            C, delta = compute_C(A, horizon=h)
            if C > worst_C:
                worst_C = C
                worst_A = tuple(A)
                if C > 2.5:
                    print(f"  NEW MAX: C={C:.4f} at {A}, delta={delta:.6f}")
    if a % 20 == 0:
        print(f"  ...a={a}, checked {count}, worst C={worst_C:.4f} at {worst_A}")

print(f"\nWorst triple C: {worst_C:.4f} at {worst_A}")

# ============================================
# PART 3: DENSE 4-ELEMENT SETS
# ============================================
print("\n" + "=" * 70)
print("PART 3: DISCREPANCY C FOR DENSE 4-ELEMENT SETS (max <= 60)")
print("=" * 70)

worst_C4 = 0
worst_A4 = None
count4 = 0
for a1 in range(3, 30):
    pool = [x for x in range(a1, 61) if x == a1 or x % a1 != 0]
    for subset in combinations(pool[:25], 4):
        if subset[0] != a1:
            continue
        A = list(subset)
        if not is_primitive(A):
            continue
        s = sum(1.0/x for x in A)
        if s <= 2.0/a1:
            continue
        count4 += 1
        h = max(1000, 20*max(A))
        C, delta = compute_C(A, horizon=h)
        if C > worst_C4:
            worst_C4 = C
            worst_A4 = tuple(A)
            if C > 2.5:
                print(f"  NEW MAX k=4: C={C:.4f} at {A}, delta={delta:.6f}")

print(f"\nDense 4-sets checked: {count4}")
print(f"Worst C: {worst_C4:.4f} at {worst_A4}")

# ============================================
# PART 4: DENSE 5,6,7-ELEMENT SETS
# ============================================
print("\n" + "=" * 70)
print("PART 4: DISCREPANCY C FOR DENSE 5,6,7-ELEMENT SETS (max <= 40)")
print("=" * 70)

for target_k in [5, 6, 7]:
    worst_Ck = 0
    worst_Ak = None
    countk = 0
    for a1 in range(3, 15):
        pool = [x for x in range(a1, 41) if x == a1 or x % a1 != 0]
        for subset in combinations(pool[:20], target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            s = sum(1.0/x for x in A)
            if s <= 2.0/a1:
                continue
            countk += 1
            h = max(800, 15*max(A))
            C, delta = compute_C(A, horizon=h)
            if C > worst_Ck:
                worst_Ck = C
                worst_Ak = tuple(A)
    print(f"  k={target_k}: checked {countk}, worst C={worst_Ck:.4f} at {worst_Ak}")

# ============================================
# PART 5: SYMMETRY IDENTITY VERIFICATION
# ============================================
print("\n" + "=" * 70)
print("PART 5: SYMMETRY IDENTITY D(r) + D(L-r) in {0, -1}")
print("=" * 70)

for A in [[3,4,5], [3,5,7], [4,5,6,14], [3,5,7,11]]:
    A = sorted(A)
    if not is_primitive(A):
        continue
    delta = density_ie(A)
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > 50000:
        print(f"  {A}: L={L} too large, skipping")
        continue
    hit = bytearray(L + 1)
    for a in A:
        for m in range(a, L + 1, a):
            hit[m] = 1
    f = [0] * (L + 1)
    running = 0
    for x in range(1, L + 1):
        running += hit[x]
        f[x] = running

    violations = 0
    max_d = 0.0
    for r in range(0, L + 1):
        dr = f[r] - delta * r
        if abs(dr) > max_d:
            max_d = abs(dr)
        if r > 0 and L - r >= 0 and L - r <= L:
            dlr = f[L - r] - delta * (L - r)
            s = dr + dlr
            expected = {0, -1}
            if abs(s - 0) > 0.001 and abs(s - (-1)) > 0.001:
                violations += 1

    print(f"  {A}: L={L}, max|D|={max_d:.4f}, symmetry violations={violations}")

print("\nDONE.")
