"""Fast C computation using periodicity: C = max |D(r)| for r in [0, L)."""
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

def compute_C_periodic(A):
    """Exact C via full period. Only feasible when lcm(A) < ~10^6."""
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > 2_000_000:
        return None, L, None
    delta = 0.0
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            delta += ((-1)**(size+1)) / l

    hit = bytearray(L + 1)
    for a in A:
        for m in range(a, L + 1, a):
            hit[m] = 1
    running = 0
    max_pos = 0.0
    max_neg = 0.0
    for r in range(1, L + 1):
        running += hit[r]
        d = running - delta * r
        if d > max_pos:
            max_pos = d
        if d < max_neg:
            max_neg = d
    C = max(max_pos, -max_neg)
    return C, L, delta

def compute_C_sieve(A, horizon):
    """Approximate C via sieve up to horizon."""
    delta = 0.0
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            delta += ((-1)**(size+1)) / l
    hit = bytearray(horizon + 1)
    for a in A:
        for m in range(a, horizon + 1, a):
            hit[m] = 1
    running = 0
    C = 0.0
    for x in range(1, horizon + 1):
        running += hit[x]
        d = abs(running - delta * x)
        if d > C:
            C = d
    return C, delta

# ============================================
# PART 1: CONSECUTIVE TRIPLES (exact via period)
# ============================================
print("=" * 70)
print("PART 1: C FOR CONSECUTIVE TRIPLES {a, a+1, a+2}")
print("Exact when lcm < 2M, otherwise sieve approximation")
print("=" * 70)

for a in list(range(3, 52)) + [75, 100, 150, 200]:
    A = [a, a+1, a+2]
    if not is_primitive(A):
        continue
    C, L, delta = compute_C_periodic(A)
    if C is None:
        C, delta = compute_C_sieve(A, min(50000, 30*a))
        print(f"  a={a:4d}: C={C:.4f} (sieve), delta={delta:.6f}, L={L}")
    else:
        print(f"  a={a:4d}: C={C:.4f} (exact), delta={delta:.6f}, L={L}")

# ============================================
# PART 2: WORST-C TRIPLES (small a)
# ============================================
print("\n" + "=" * 70)
print("PART 2: WORST-C TRIPLES")
print("=" * 70)

worst_C = 0
worst_A = None
count = 0
t0 = time.time()
for a in range(3, 50):
    for b in range(a+1, min(a+100, 200)):
        if b % a == 0:
            continue
        for c in range(b+1, min(b+100, 300)):
            if c % a == 0 or c % b == 0:
                continue
            A = [a, b, c]
            count += 1
            C, L, delta = compute_C_periodic(A)
            if C is None:
                C, delta = compute_C_sieve(A, min(10000, 15*c))
            if C is not None and C > worst_C:
                worst_C = C
                worst_A = tuple(A)
                if C > 2.8:
                    print(f"  C={C:.4f} at {A}, delta={delta:.6f}, L={L}")
print(f"\nChecked {count} triples in {time.time()-t0:.1f}s")
print(f"Worst C: {worst_C:.4f} at {worst_A}")

# ============================================
# PART 3: DENSE k=4..7 SETS
# ============================================
print("\n" + "=" * 70)
print("PART 3: C FOR DENSE k=4..7 SETS")
print("=" * 70)

for target_k in [4, 5, 6, 7]:
    worst_Ck = 0
    worst_Ak = None
    countk = 0
    t0 = time.time()
    for a1 in range(3, 20):
        pool = [x for x in range(a1, 51) if x == a1 or x % a1 != 0]
        for subset in combinations(pool[:22], target_k):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            s = sum(1.0/x for x in A)
            if s <= 2.0/a1:
                continue
            countk += 1
            C, L, delta = compute_C_periodic(A)
            if C is None:
                C, delta = compute_C_sieve(A, min(5000, 10*max(A)))
            if C is not None and C > worst_Ck:
                worst_Ck = C
                worst_Ak = tuple(A)
    elapsed = time.time() - t0
    print(f"  k={target_k}: checked {countk}, worst C={worst_Ck:.4f} at {worst_Ak}, "
          f"{elapsed:.1f}s")

# ============================================
# PART 4: SYMMETRY IDENTITY CHECK
# ============================================
print("\n" + "=" * 70)
print("PART 4: SYMMETRY D(r)+D(L-r) in {0,-1}")
print("=" * 70)

for A in [[3,4,5], [3,5,7], [5,6,7], [4,5,6,14], [3,5,7,11], [3,4,5,7,11]]:
    A = sorted(A)
    if not is_primitive(A):
        print(f"  {A}: not primitive")
        continue
    delta = 0.0
    for size in range(1, len(A)+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            delta += ((-1)**(size+1)) / l
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > 500000:
        print(f"  {A}: L={L} too large")
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
    max_C = 0.0
    for r in range(1, L):
        dr = f[r] - delta * r
        dlr = f[L - r] - delta * (L - r)
        s = dr + dlr
        if abs(dr) > max_C:
            max_C = abs(dr)
        if abs(s) > 0.01 and abs(s + 1) > 0.01:
            violations += 1
            if violations <= 3:
                print(f"    VIOLATION at r={r}: D(r)={dr:.4f}, D(L-r)={dlr:.4f}, sum={s:.4f}")
    hit_at_Lr = "hit" if any((L-r) % a == 0 for a in A for r in [1]) else "?"
    print(f"  {A}: L={L}, C={max_C:.4f}, symmetry violations={violations}")

print("\nDONE.")
