"""EP-488 Final Push v2: inline computation, no combinations overhead."""
from math import gcd
import time

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def S123_and_delta(A):
    """Compute S1, S2, S3, delta for a set A (inline, fast)."""
    k = len(A)
    S1 = sum(1.0/a for a in A)
    S2 = 0.0
    for i in range(k):
        for j in range(i+1, k):
            S2 += 1.0 / lcm2(A[i], A[j])
    S3 = 0.0
    for i in range(k):
        for j in range(i+1, k):
            lij = lcm2(A[i], A[j])
            for m in range(j+1, k):
                S3 += 1.0 / lcm2(lij, A[m])
    # Full IE density
    delta = S1 - S2 + S3
    if k >= 4:
        S4 = 0.0
        for i in range(k):
            for j in range(i+1, k):
                lij = lcm2(A[i], A[j])
                for m in range(j+1, k):
                    lijm = lcm2(lij, A[m])
                    for n in range(m+1, k):
                        S4 += 1.0 / lcm2(lijm, A[n])
        delta -= S4
        if k >= 5:
            S5 = 0.0
            for i in range(k):
                for j in range(i+1, k):
                    lij = lcm2(A[i], A[j])
                    for m in range(j+1, k):
                        lijm = lcm2(lij, A[m])
                        for n in range(m+1, k):
                            lijmn = lcm2(lijm, A[n])
                            for p in range(n+1, k):
                                S5 += 1.0 / lcm2(lijmn, A[p])
            delta += S5
            if k >= 6:
                S6 = 0.0
                for i in range(k):
                    for j in range(i+1, k):
                        lij = lcm2(A[i], A[j])
                        for m in range(j+1, k):
                            lijm = lcm2(lij, A[m])
                            for n in range(m+1, k):
                                lijmn = lcm2(lijm, A[n])
                                for p in range(n+1, k):
                                    lijmnp = lcm2(lijmn, A[p])
                                    for q in range(p+1, k):
                                        S6 += 1.0/lcm2(lijmnp, A[q])
                delta -= S6
                # Skip higher for k<=8
                if k >= 7:
                    # approximate: higher terms tiny
                    pass
    return S1, S2, S3, delta

# ============================================
# TASK 1: R_hybrid for dense 5-sets, max<=50
# ============================================
print("=" * 70)
print("TASK 1: R_hybrid = S1 - S2 - S3 for dense 5-sets (max<=50)")
print("=" * 70)
t0 = time.time()
c5 = 0; n5 = 0; mRh = 1e9; mRs = None

for a in range(3, 26):
    pool = [x for x in range(a+1, 51) if x % a != 0]
    np = len(pool)
    for ib in range(np):
        b = pool[ib]
        if b % a == 0: continue
        for ic in range(ib+1, np):
            c = pool[ic]
            if c % b == 0: continue
            for id_ in range(ic+1, np):
                d = pool[id_]
                if d % a == 0 or d % b == 0 or d % c == 0: continue
                for ie in range(id_+1, np):
                    e = pool[ie]
                    if e % a == 0 or e % b == 0 or e % c == 0 or e % d == 0: continue
                    A = [a, b, c, d, e]
                    S1 = 1.0/a + 1.0/b + 1.0/c + 1.0/d + 1.0/e
                    if S1 <= 2.0/a: continue
                    c5 += 1
                    # Compute S2
                    S2 = (1.0/lcm2(a,b) + 1.0/lcm2(a,c) + 1.0/lcm2(a,d) + 1.0/lcm2(a,e)
                         + 1.0/lcm2(b,c) + 1.0/lcm2(b,d) + 1.0/lcm2(b,e)
                         + 1.0/lcm2(c,d) + 1.0/lcm2(c,e) + 1.0/lcm2(d,e))
                    # Compute S3
                    lab=lcm2(a,b); lac=lcm2(a,c); lad=lcm2(a,d); lae=lcm2(a,e)
                    lbc=lcm2(b,c); lbd=lcm2(b,d); lbe=lcm2(b,e)
                    lcd=lcm2(c,d); lce=lcm2(c,e); lde=lcm2(d,e)
                    S3 = (1.0/lcm2(lab,c) + 1.0/lcm2(lab,d) + 1.0/lcm2(lab,e)
                        + 1.0/lcm2(lac,d) + 1.0/lcm2(lac,e)
                        + 1.0/lcm2(lad,e)
                        + 1.0/lcm2(lbc,d) + 1.0/lcm2(lbc,e)
                        + 1.0/lcm2(lbd,e)
                        + 1.0/lcm2(lcd,e))
                    Rh = S1 - S2 - S3
                    if Rh < mRh:
                        mRh = Rh; mRs = tuple(A)
                    if Rh <= 1e-10:
                        n5 += 1
                        if n5 <= 10:
                            print(f"  Rh<=0: {A}, Rh={Rh:.8f}")
    if a % 5 == 0:
        print(f"  a={a}: {c5} sets, {n5} neg, min={mRh:.6f}, {time.time()-t0:.1f}s")

print(f"\nTask 1: {c5} dense 5-sets, R_hybrid<=0: {n5}, min={mRh:.8f} at {mRs}")

# ============================================
# TASK 2: 2*delta > S1 for dense k-sets
# ============================================
print("\n" + "=" * 70)
print("TASK 2: 2*delta > S1 for dense sets (k=4..7, max<=40)")
print("=" * 70)

for tk in range(4, 8):
    t0 = time.time()
    ck = 0; fk = 0; mr = 1e9; ms = None
    me = min(40, 10 + 4*tk)
    for a1 in range(3, min(16, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0]
        pool = pool[:22]
        # Generate primitive tk-subsets including a1
        from itertools import combinations as comb
        for sub in comb(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/x for x in A)
            if S1 <= 2.0/a1: continue
            ck += 1
            _, _, _, delta = S123_and_delta(A)
            ratio = 2*delta/S1 if S1 > 0 else 999
            if ratio < mr:
                mr = ratio; ms = tuple(A)
            if 2*delta <= S1 + 1e-10:
                fk += 1
                if fk <= 5:
                    print(f"  FAIL k={tk}: {A}, 2d={2*delta:.6f}, S1={S1:.6f}")
    el = time.time()-t0
    st = "ALL 2d>S1" if fk == 0 else f"{fk} FAIL"
    print(f"  k={tk}: {ck:>7d} dense, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")

# ============================================
# TASK 3: delta*M > 3C for dense sets
# ============================================
print("\n" + "=" * 70)
print("TASK 3: delta*max(A) > 3C for dense sets (k=3..6, max<=30)")
print("=" * 70)

def compute_C(A, max_L=2_000_000):
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > max_L:
        return None, L
    _, _, _, delta = S123_and_delta(A)
    hit = bytearray(L+1)
    for a in A:
        for m in range(a, L+1, a):
            hit[m] = 1
    run = 0; mx = 0.0
    for r in range(1, L+1):
        run += hit[r]
        d = abs(run - delta*r)
        if d > mx: mx = d
    return mx, L

from itertools import combinations as comb
for tk in range(3, 7):
    t0 = time.time()
    ck=0; fk=0; mmarg=1e9; mset=None; mvals=None
    me = min(30, 8+3*tk)
    for a1 in range(3, min(13, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0]
        pool = pool[:18]
        if len(pool) < tk-1: continue
        for sub in comb(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/x for x in A)
            if S1 <= 2.0/a1: continue
            ck += 1
            _, _, _, delta = S123_and_delta(A)
            M = max(A)
            Cv, L = compute_C(A)
            if Cv is None: continue
            marg = delta*M - 3*Cv
            if marg < mmarg:
                mmarg = marg; mset=tuple(A); mvals=(delta,M,Cv,L)
            if marg <= 0:
                fk += 1
                if fk <= 10:
                    print(f"  FAIL k={tk}: {A}, dM={delta*M:.4f}, 3C={3*Cv:.4f}, d={delta:.4f}, C={Cv:.2f}")
    el = time.time()-t0
    st = "ALL dM>3C" if fk == 0 else f"{fk} FAIL"
    ex = ""
    if mvals:
        d,M,C,L = mvals
        ex = f" (d={d:.4f},M={M},C={C:.2f})"
    print(f"  k={tk}: {ck:>6d} dense, {st}, min marg={mmarg:.4f} at {mset}{ex}, {el:.1f}s")

# ============================================
# BONUS: 2*delta > S1 for ALL primitive sets including sparse
# ============================================
print("\n" + "=" * 70)
print("BONUS: 2*delta > S1 for ALL primitive sets (k=3..6, max<=25)")
print("=" * 70)

for tk in range(3, 7):
    t0 = time.time()
    ck=0; fk=0; mr=1e9; ms=None
    for a1 in range(2, 13):
        pool = [x for x in range(a1+1, 26) if x % a1 != 0]
        pool = pool[:18]
        if len(pool) < tk-1: continue
        for sub in comb(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            ck += 1
            S1 = sum(1.0/x for x in A)
            _, _, _, delta = S123_and_delta(A)
            ratio = 2*delta/S1 if S1 > 0 else 999
            if ratio < mr:
                mr = ratio; ms = tuple(A)
            if 2*delta <= S1 + 1e-10:
                fk += 1
                if fk <= 5:
                    print(f"  FAIL k={tk}: {A}, 2d/S1={ratio:.6f}")
    el = time.time()-t0
    st = "ALL 2d>S1" if fk == 0 else f"{fk} FAIL"
    print(f"  k={tk}: {ck:>8d} ALL prim, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")

print("\nDONE.")
