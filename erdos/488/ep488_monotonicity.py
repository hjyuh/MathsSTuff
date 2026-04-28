"""
Test monotonicity: for every primitive set A with min=a, |A|=k,
is ratio(A) <= ratio({a, a+1, ..., a+k-1})?
"""
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

def ratio(A, mult=30):
    M = max(A)
    h = max(5000, mult * M)
    hit = bytearray(h + 1)
    for e in A:
        for m in range(e, h + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0
    for x in range(M, h + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g
        if g > mx: mx = g
    return mx / (2*mn) if mn > 0 else 999

# Cache consecutive ratios
consecutive_cache = {}
def consecutive_ratio(a, k):
    if (a, k) not in consecutive_cache:
        B = list(range(a, a+k))
        if not is_primitive(B):
            return None
        consecutive_cache[(a, k)] = ratio(B)
    return consecutive_cache[(a, k)]

# SYSTEMATIC TEST
print("MONOTONICITY TEST: ratio(A) vs ratio(consecutive) for same min, |A|")
print("=" * 70)

violations = 0
total = 0
worst_excess = 0
worst_excess_pair = None

for a1 in range(3, 16):
    for tk in range(4, 9):
        cons_r = consecutive_ratio(a1, tk)
        if cons_r is None: continue
        pool = [x for x in range(a1+1, min(51, 8*a1)) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            A_r = ratio(A, mult=20)
            if A_r > cons_r + 1e-9:
                violations += 1
                excess = A_r - cons_r
                if excess > worst_excess:
                    worst_excess = excess
                    worst_excess_pair = (tuple(A), A_r, cons_r)
                if violations <= 10:
                    print(f"  VIOLATION: A={A}, ratio={A_r:.6f}, "
                          f"consecutive({a1},{tk})={cons_r:.6f}, excess={excess:.6f}")

print(f"\n  Checked: {total} primitive sets")
print(f"  Violations (A > consecutive): {violations}")
if worst_excess_pair:
    A, A_r, c_r = worst_excess_pair
    print(f"  Worst excess: A={list(A)}, ratio={A_r:.6f}, cons={c_r:.6f}, excess={worst_excess:.6f}")
sys.stdout.flush()

# KEY: is the monotonicity STRICT? i.e., ratio(A) < ratio(consecutive) always?
print("\n" + "=" * 70)
print("STRICT MONOTONICITY: is equality achieved?")
print("=" * 70)
# When does A achieve ratio = consecutive ratio?
strict_eq = 0
for a1 in range(3, 12):
    for tk in range(4, 8):
        cons_r = consecutive_ratio(a1, tk)
        if cons_r is None: continue
        pool = [x for x in range(a1+1, min(30, 5*a1)) if x % a1 != 0][:15]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            A_r = ratio(A, mult=15)
            if abs(A_r - cons_r) < 1e-9:
                strict_eq += 1

print(f"  Sets with ratio EXACTLY equal to consecutive: {strict_eq}")

# What are the sets closest to consecutive (largest ratio among non-consecutive)?
print("\nSets with largest ratio for each (a, k):")
for a in [3, 5, 10]:
    for k in [4, 5]:
        cons_r = consecutive_ratio(a, k)
        if cons_r is None: continue
        pool = [x for x in range(a+1, 40) if x % a != 0][:15]
        if len(pool) < k-1: continue
        candidates = []
        for sub in combinations(pool, k-1):
            A = [a] + list(sub)
            if not is_primitive(A): continue
            r = ratio(A, mult=15)
            candidates.append((r, tuple(A)))
        candidates.sort(reverse=True)
        print(f"\n  a={a}, k={k}, consecutive ratio={cons_r:.6f}")
        for r, A in candidates[:5]:
            print(f"    ratio={r:.6f}: {list(A)}")

print("\nDONE.")
