"""
EP-488 Final Push (fast float version).
Task 1: R_hybrid = S1 - S2 - S3 for dense 5-sets
Task 2: 2*delta > S1 for dense k-sets
Task 3: delta*max(A) > 3C for dense sets
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

def ie_sums_float(A):
    """Fast float IE sums by order."""
    k = len(A)
    sums = {}
    for size in range(1, k+1):
        s = 0.0
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            s += 1.0 / l
        sums[size] = s
    return sums

def density_float(A):
    sums = ie_sums_float(A)
    d = 0.0
    for size, s in sums.items():
        d += ((-1)**(size+1)) * s
    return d

def compute_C_exact(A, max_L=3_000_000):
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > max_L:
        return None, L
    delta = density_float(A)
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
# TASK 1: R_hybrid for dense 5-sets
# ============================================
print("=" * 70)
print("TASK 1: R_hybrid = S1 - S2 - S3 for dense 5-sets (max<=50)")
print("=" * 70)
t0 = time.time()
count5 = 0; neg5 = 0; min_Rh = 1e9; min_Rh_set = None

for a1 in range(3, 26):
    pool = [a1]
    for x in range(a1+1, 51):
        if x % a1 != 0:
            pool.append(x)
    pl = pool[:30]
    for subset in combinations(pl, 5):
        if subset[0] != a1: continue
        A = list(subset)
        if not is_primitive(A): continue
        S1 = sum(1.0/a for a in A)
        if S1 <= 2.0/a1: continue
        count5 += 1
        sums = ie_sums_float(A)
        Rh = sums[1] - sums[2] - sums[3]
        if Rh < min_Rh:
            min_Rh = Rh; min_Rh_set = tuple(A)
        if Rh <= 1e-10:
            neg5 += 1
            if neg5 <= 10:
                print(f"  Rh<=0: {A}, Rh={Rh:.8f}, S1={sums[1]:.4f}")
    if a1 % 5 == 0:
        print(f"  a1={a1}: {count5} sets, {neg5} neg, min={min_Rh:.6f}, {time.time()-t0:.1f}s")

print(f"\nDense 5-sets: {count5}, R_hybrid<=0: {neg5}")
print(f"Min R_hybrid: {min_Rh:.8f} at {min_Rh_set}")

# ============================================
# TASK 2: 2*delta > S1 for dense k-sets
# ============================================
print("\n" + "=" * 70)
print("TASK 2: 2*delta > S1 for dense k-sets (k=4..8, max<=45)")
print("=" * 70)

for tk in range(4, 9):
    t0 = time.time()
    ck = 0; fk = 0; mr = 1e9; ms = None
    me = min(45, 12 + 4*tk)
    for a1 in range(3, min(20, me)):
        pool = [a1]
        for x in range(a1+1, me+1):
            if x % a1 != 0: pool.append(x)
        pl = pool[:min(26, len(pool))]
        if len(pl) < tk: continue
        for subset in combinations(pl, tk):
            if subset[0] != a1: continue
            A = list(subset)
            if not is_primitive(A): continue
            S1 = sum(1.0/a for a in A)
            if S1 <= 2.0/a1: continue
            ck += 1
            delta = density_float(A)
            ratio = 2*delta/S1 if S1 > 0 else 999
            if ratio < mr:
                mr = ratio; ms = tuple(A)
            if 2*delta <= S1 + 1e-12:
                fk += 1
                if fk <= 5:
                    print(f"  FAIL k={tk}: {A}, 2d={2*delta:.6f}, S1={S1:.6f}, r={ratio:.6f}")
    el = time.time()-t0
    st = "ALL 2d>S1" if fk == 0 else f"{fk} FAILURES"
    print(f"  k={tk}: {ck:>7d} dense, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")

# ============================================
# TASK 3: delta*max > 3C for dense sets
# ============================================
print("\n" + "=" * 70)
print("TASK 3: delta*max(A) > 3C for dense sets (k=3..7, max<=35)")
print("=" * 70)

for tk in range(3, 8):
    t0 = time.time()
    ck = 0; fk = 0; mmarg = 1e9; mset = None; mvals = None
    me = min(35, 10 + 3*tk)
    for a1 in range(3, min(15, me)):
        pool = [a1]
        for x in range(a1+1, me+1):
            if x % a1 != 0: pool.append(x)
        pl = pool[:min(20, len(pool))]
        if len(pl) < tk: continue
        for subset in combinations(pl, tk):
            if subset[0] != a1: continue
            A = list(subset)
            if not is_primitive(A): continue
            S1 = sum(1.0/a for a in A)
            if S1 <= 2.0/a1: continue
            ck += 1
            delta = density_float(A)
            M = max(A)
            Cv, L = compute_C_exact(A, max_L=2_000_000)
            if Cv is None: continue
            marg = delta*M - 3*Cv
            if marg < mmarg:
                mmarg = marg; mset = tuple(A); mvals = (delta, M, Cv, L)
            if marg <= 0:
                fk += 1
                if fk <= 10:
                    print(f"  FAIL k={tk}: {A}, dM={delta*M:.4f}, 3C={3*Cv:.4f}, "
                          f"d={delta:.4f}, C={Cv:.2f}")
    el = time.time()-t0
    st = "ALL dM>3C" if fk == 0 else f"{fk} FAILURES"
    ex = ""
    if mset and mvals:
        d,M,C,L = mvals
        ex = f" (d={d:.4f},M={M},C={C:.2f})"
    print(f"  k={tk}: {ck:>6d} dense, {st}, min margin={mmarg:.4f} at {mset}{ex}, {el:.1f}s")

# ============================================
# BONUS: For ALL primitive sets (not just dense), check 2*delta > S1
# ============================================
print("\n" + "=" * 70)
print("BONUS: 2*delta > S1 for ALL primitive sets k=3..6, max<=30")
print("(including sparse)")
print("=" * 70)

for tk in range(3, 7):
    t0 = time.time()
    ck = 0; fk = 0; mr = 1e9; ms = None
    for a1 in range(2, 16):
        pool = [a1]
        for x in range(a1+1, 31):
            if x % a1 != 0: pool.append(x)
        pl = pool[:min(22, len(pool))]
        if len(pl) < tk: continue
        for subset in combinations(pl, tk):
            if subset[0] != a1: continue
            A = list(subset)
            if not is_primitive(A): continue
            ck += 1
            S1 = sum(1.0/a for a in A)
            delta = density_float(A)
            ratio = 2*delta/S1 if S1 > 0 else 999
            if ratio < mr:
                mr = ratio; ms = tuple(A)
            if 2*delta <= S1 + 1e-12:
                fk += 1
                if fk <= 5:
                    print(f"  FAIL k={tk}: {A}, 2d={2*delta:.6f}, S1={S1:.6f}")
    el = time.time()-t0
    st = "ALL 2d>S1" if fk == 0 else f"{fk} FAILURES"
    print(f"  k={tk}: {ck:>8d} sets, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")

print("\nDONE.")
