"""
Test whether non-coprime primitive sets can have 2*delta < S1.
Focus on sets with many shared factors to minimize delta.
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

# Test sets with many shared factors (maximize overlap, minimize delta)
print("NON-COPRIME PRIMITIVE SETS: stress-testing 2delta > S1")
print("=" * 60)

# Sets built from multiples of 2 and 3
print("\n--- Sets with heavy factor-sharing ---")
test_sets = [
    [4, 6, 9, 10],
    [4, 6, 9, 10, 14, 15],
    [4, 6, 9, 10, 14, 15, 22, 25, 26],
    [6, 10, 14, 15, 21, 22, 25, 26],
    [6, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35],
    [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35],
    # Scaled versions (multiply by m)
    [8, 12, 18, 20, 28, 30],
    [12, 18, 20, 28, 30, 42, 44, 50],
    # Dense near min
    [4, 5, 6, 7, 9, 10, 11, 13],
    [3, 4, 5, 7, 8, 10, 11, 13, 16, 17],
    [3, 4, 5, 7, 8, 10, 11, 13, 16, 17, 19, 22, 23],
]

for A in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        print(f"  {A}: NOT PRIMITIVE")
        continue
    S1 = sum(1.0/a for a in A)
    delta = delta_ie(A)
    P = 1.0
    for a in A:
        P *= (1 - 1.0/a)
    ratio = 2*delta/S1
    coprime_delta = 1 - P
    print(f"  {A}: S1={S1:.4f}, delta={delta:.4f}, 1-P={coprime_delta:.4f}, "
          f"2d/S1={ratio:.4f}, k={len(A)}")

# Systematic search for worst non-coprime ratio
print("\n--- Systematic: worst 2d/S1 among non-coprime k=4..8, max<=40 ---")
for tk in range(4, 9):
    mr = 1e9; ms = None; ck = 0
    me = min(40, 8+4*tk)
    for a1 in range(3, min(16, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:20]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1]+list(sub)
            if not is_primitive(A): continue
            # Check if any pair is non-coprime
            has_noncoprime = False
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    if gcd(A[i], A[j]) > 1:
                        has_noncoprime = True
                        break
                if has_noncoprime: break
            if not has_noncoprime: continue  # skip fully coprime
            ck += 1
            S1 = sum(1.0/a for a in A)
            delta = delta_ie(A)
            r = 2*delta/S1
            if r < mr: mr = r; ms = tuple(A)
    if ms:
        S1 = sum(1.0/a for a in ms)
        delta = delta_ie(list(ms))
        print(f"  k={tk}: {ck} non-coprime sets, min 2d/S1={mr:.6f} at {ms}, "
              f"S1={S1:.4f}, delta={delta:.4f}")

# Key analytic question: for coprime vs non-coprime with same S1
print("\n--- Coprime vs non-coprime with similar S1 ---")
# Compare {2,3,5,7} (coprime, S1=1.176) with non-coprime sets of similar S1
target_S1 = 1.176
print(f"Target S1 ~ {target_S1}")
candidates = []
for a1 in range(3, 12):
    pool = [x for x in range(a1+1, 30) if x % a1 != 0][:15]
    for sub in combinations(pool, 3):
        A = [a1]+list(sub)
        if not is_primitive(A): continue
        S1 = sum(1.0/a for a in A)
        if abs(S1 - target_S1) < 0.05:
            delta = delta_ie(A)
            has_nc = any(gcd(A[i],A[j])>1 for i in range(4) for j in range(i+1,4))
            candidates.append((2*delta/S1, tuple(A), S1, delta, has_nc))
candidates.sort()
print(f"Found {len(candidates)} sets with S1 ~ {target_S1}:")
for r, A, S1, d, nc in candidates[:10]:
    print(f"  {A}: S1={S1:.4f}, delta={d:.4f}, 2d/S1={r:.4f}, "
          f"{'non-coprime' if nc else 'COPRIME'}")

# THE ACTUAL MERTENS-BASED PROOF
print("\n" + "=" * 60)
print("ANALYTIC PROOF: f(S) = 2 - 2e^{-S} - S > 0 for S < S_0")
print("=" * 60)
import math
# Find S_0 by bisection
lo, hi = 1.5, 1.7
for _ in range(50):
    mid = (lo+hi)/2
    if 2 - 2*math.exp(-mid) - mid > 0:
        lo = mid
    else:
        hi = mid
S0 = (lo+hi)/2
print(f"S_0 = {S0:.10f}")
print(f"f(S_0) = {2-2*math.exp(-S0)-S0:.2e}")
print(f"f(ln 2) = {2-2*math.exp(-math.log(2))-math.log(2):.6f} = 1 - ln 2 = {1-math.log(2):.6f}")
print(f"\nFor coprime A with S1 < {S0:.4f}: 2*delta > S1 PROVED.")
print(f"For S1 >= ln 2 = {math.log(2):.4f}: delta >= 1-e^(-S) > 1/2, so 2G > 1 > G(m).")
print(f"\nGap: non-coprime A with S1 in ({math.log(2):.3f}, {S0:.3f}) where coprime proof works")
print(f"but non-coprime delta could be < coprime delta.")

print("\nDONE.")
