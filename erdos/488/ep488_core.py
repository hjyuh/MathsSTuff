"""Ultra-fast: only float IE, no sieve. Focus on the key questions."""
from math import gcd
from itertools import combinations
import time, sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def delta_ie(A):
    """Full IE density (float)."""
    k = len(A)
    d = 0.0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            d += ((-1)**(size+1)) / l
    return d

# ============================================
# TASK 2 (most important): 2*delta > S1 for ALL primitive sets
# ============================================
print("TASK 2: 2*delta_A > S1 for ALL primitive sets?")
print("=" * 60)
sys.stdout.flush()

for tk in [3, 4, 5, 6, 7]:
    t0 = time.time()
    ck=0; fk=0; mr=1e9; ms=None
    me = min(25, 6+3*tk)
    for a1 in range(2, min(13, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:16]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1]+list(sub)
            if not is_primitive(A): continue
            ck += 1
            S1 = sum(1.0/x for x in A)
            delta = delta_ie(A)
            r = 2*delta/S1 if S1>0 else 999
            if r < mr: mr=r; ms=tuple(A)
            if 2*delta <= S1+1e-10:
                fk += 1
                if fk <= 3:
                    print(f"  FAIL k={tk}: {A}, 2d={2*delta:.6f}, S1={S1:.6f}, 2d/S1={r:.6f}")
                    sys.stdout.flush()
    el = time.time()-t0
    st = "ALL 2d>S1" if fk==0 else f"{fk} FAIL"
    print(f"  k={tk}: {ck:>7d} sets, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")
    sys.stdout.flush()

# TASK 1: R_hybrid for dense 5-sets (smaller range)
print(f"\nTASK 1: R_hybrid = S1-S2-S3 for dense 5-sets (max<=30)")
print("=" * 60)
sys.stdout.flush()

t0 = time.time()
c=0; neg=0; mRh=1e9; mRs=None
for a1 in range(3, 15):
    pool = [x for x in range(a1+1, 31) if x % a1 != 0][:16]
    for sub in combinations(pool, 4):
        A = [a1]+list(sub)
        if not is_primitive(A): continue
        S1 = sum(1.0/x for x in A)
        if S1 <= 2.0/a1: continue
        c += 1
        # S2
        S2 = sum(1.0/lcm2(A[i],A[j]) for i in range(5) for j in range(i+1,5))
        # S3
        S3 = 0.0
        for i in range(5):
            for j in range(i+1,5):
                lij = lcm2(A[i],A[j])
                for m in range(j+1,5):
                    S3 += 1.0/lcm2(lij, A[m])
        Rh = S1 - S2 - S3
        if Rh < mRh: mRh=Rh; mRs=tuple(A)
        if Rh <= 1e-10:
            neg += 1
            if neg <= 10: print(f"  Rh<=0: {A}, Rh={Rh:.8f}")
            sys.stdout.flush()
print(f"Dense 5-sets: {c}, Rh<=0: {neg}, min={mRh:.8f} at {mRs}, {time.time()-t0:.1f}s")
sys.stdout.flush()

print("\nDONE.")
