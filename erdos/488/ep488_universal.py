"""Confirm 2*delta > S1 universally for larger ranges."""
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
    k = len(A)
    d = 0.0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            d += ((-1)**(size+1)) / l
    return d

# Extended search: k=3..8, max up to 40
print("2*delta > S1: EXTENDED SEARCH (max<=40)")
print("=" * 60)

for tk in range(3, 9):
    t0 = time.time()
    ck=0; fk=0; mr=1e9; ms=None
    me = min(40, 8+4*tk)
    for a1 in range(2, min(16, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:20]
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
                    print(f"  FAIL k={tk}: {A}, 2d/S1={r:.6f}")
                    sys.stdout.flush()
    el = time.time()-t0
    st = "ALL 2d>S1" if fk==0 else f"{fk} FAIL"
    print(f"  k={tk}: {ck:>8d} sets, {st}, min 2d/S1={mr:.6f} at {ms}, {el:.1f}s")
    sys.stdout.flush()

# The worst case pattern: first k primes
print("\nWORST CASE PATTERN: first k primes")
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for k in range(2, 14):
    A = primes[:k]
    S1 = sum(1.0/p for p in A)
    delta = delta_ie(A)
    r = 2*delta/S1
    print(f"  k={k:2d}: {A}, S1={S1:.6f}, delta={delta:.6f}, 2d/S1={r:.6f}")
    sys.stdout.flush()

# Can we prove 2*delta > S1 analytically?
# delta = 1 - prod(1 - 1/a_i) for coprime sets
# S1 = sum(1/a_i)
# Need: 2(1 - prod(1-1/a)) > sum(1/a)
# i.e.: 2 - 2*prod(1-1/a) > sum(1/a)
# i.e.: 2 - sum(1/a) > 2*prod(1-1/a)

print("\nANALYTIC CHECK: for coprime sets, 2-S1 vs 2*prod(1-1/a)")
for k in range(2, 14):
    A = primes[:k]
    S1 = sum(1.0/p for p in A)
    prod_val = 1.0
    for p in A:
        prod_val *= (1 - 1.0/p)
    lhs = 2 - S1
    rhs = 2 * prod_val
    print(f"  k={k:2d}: 2-S1={lhs:.6f}, 2*prod={rhs:.6f}, "
          f"ratio={(2-S1)/rhs:.6f} (need>1 iff 2d>S1 when 2-S1>0)")
    sys.stdout.flush()

print("\nDONE.")
