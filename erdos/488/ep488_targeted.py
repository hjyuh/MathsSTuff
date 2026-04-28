"""Targeted checks using itertools.combinations for speed."""
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

def compute_all(A):
    """Compute S1, S2, S3, delta (full IE) for small k."""
    k = len(A)
    S1 = sum(1.0/a for a in A)
    # S2: pairs
    S2 = 0.0
    for i in range(k):
        for j in range(i+1, k):
            S2 += 1.0/lcm2(A[i], A[j])
    # S3: triples
    S3 = 0.0
    for i in range(k):
        for j in range(i+1, k):
            lij = lcm2(A[i], A[j])
            for m in range(j+1, k):
                S3 += 1.0/lcm2(lij, A[m])
    # Full delta via sieve of one period (exact)
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L <= 5_000_000:
        hit = bytearray(L+1)
        for a in A:
            for m in range(a, L+1, a):
                hit[m] = 1
        fL = sum(hit)
        delta = fL / L
        # Also compute C
        run = 0; mx = 0.0
        for r in range(1, L+1):
            run += hit[r]
            d = abs(run - delta*r)
            if d > mx: mx = d
        C = mx
    else:
        # IE approximation for delta
        delta = S1 - S2 + S3
        if k >= 4:
            S4 = 0.0
            for c4 in combinations(range(k), 4):
                l = A[c4[0]]
                for idx in c4[1:]: l = lcm2(l, A[idx])
                S4 += 1.0/l
            delta -= S4
            if k >= 5:
                S5 = 0.0
                for c5 in combinations(range(k), 5):
                    l = A[c5[0]]
                    for idx in c5[1:]: l = lcm2(l, A[idx])
                    S5 += 1.0/l
                delta += S5
        C = None
    return S1, S2, S3, delta, C, L

# TASK 1: R_hybrid for dense 5-sets (smaller range for speed)
print("TASK 1: R_hybrid for dense 5-sets (max<=35)")
print("=" * 60)
t0 = time.time()
c=0; neg=0; mRh=1e9; mRs=None

for a1 in range(3, 18):
    pool = [x for x in range(a1+1, 36) if x % a1 != 0]
    for sub in combinations(pool[:20], 4):
        A = [a1] + list(sub)
        if not is_primitive(A): continue
        S1 = sum(1.0/x for x in A)
        if S1 <= 2.0/a1: continue
        c += 1
        s1,s2,s3,_,_,_ = compute_all(A)
        Rh = s1 - s2 - s3
        if Rh < mRh: mRh=Rh; mRs=tuple(A)
        if Rh <= 1e-10:
            neg += 1
            if neg <= 10: print(f"  Rh<=0: {A}, Rh={Rh:.8f}")

print(f"Dense 5-sets: {c}, Rh<=0: {neg}, min Rh={mRh:.8f} at {mRs}")
print(f"Time: {time.time()-t0:.1f}s")

# TASK 2: 2*delta > S1 for ALL primitive sets (the key question)
print(f"\nTASK 2: 2*delta > S1 for ALL primitive sets")
print("=" * 60)

for tk in range(3, 8):
    t0 = time.time()
    ck=0; fk=0; mr=1e9; ms=None
    me = min(30, 8+3*tk)
    for a1 in range(2, min(14, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0]
        pool = pool[:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1]+list(sub)
            if not is_primitive(A): continue
            ck += 1
            s1,s2,s3,delta,_,_ = compute_all(A)
            ratio = 2*delta/s1 if s1>0 else 999
            if ratio < mr: mr=ratio; ms=tuple(A)
            if 2*delta <= s1+1e-10:
                fk += 1
                if fk <= 5: print(f"  FAIL k={tk}: {A}, 2d/S1={ratio:.6f}")
    el = time.time()-t0
    st = "ALL 2d>S1" if fk==0 else f"{fk} FAIL"
    print(f"  k={tk}: {ck:>7d} sets, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")
    sys.stdout.flush()

# TASK 3: delta*M > 3C
print(f"\nTASK 3: delta*max(A) > 3C for dense sets (k=3..6, max<=25)")
print("=" * 60)

for tk in range(3, 7):
    t0 = time.time()
    ck=0; fk=0; mmarg=1e9; mset=None; mvals=None
    me = min(25, 7+3*tk)
    for a1 in range(3, min(12, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0]
        pool = pool[:16]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1]+list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/x for x in A)
            if S1 <= 2.0/a1: continue
            ck += 1
            s1,s2,s3,delta,Cv,L = compute_all(A)
            if Cv is None: continue
            M = max(A)
            marg = delta*M - 3*Cv
            if marg < mmarg:
                mmarg=marg; mset=tuple(A); mvals=(delta,M,Cv,L)
            if marg <= 0:
                fk += 1
                if fk <= 10:
                    print(f"  FAIL k={tk}: {A}, dM={delta*M:.4f}, 3C={3*Cv:.4f}, d={delta:.4f}, C={Cv:.2f}")
    el = time.time()-t0
    st = "ALL dM>3C" if fk==0 else f"{fk} FAIL"
    ex = ""
    if mvals: d,M,C,L=mvals; ex=f" (d={d:.4f},M={M},C={C:.2f},L={L})"
    print(f"  k={tk}: {ck:>6d} dense, {st}, min marg={mmarg:.4f} at {mset}{ex}, {el:.1f}s")
    sys.stdout.flush()

print("\nDONE.")
