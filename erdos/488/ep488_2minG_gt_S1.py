"""
CRITICAL TEST: is 2*min(G over [M, horizon]) > S1 for all primitive sets?
If yes, EP-488 follows: 2G(n) > S1 >= G(m) for all n >= M and all m > n.
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

def check(A, mult=30):
    """Compute min G over [M, mult*M] and S1. Return (2*min_G, S1, min_x)."""
    M = max(A)
    h_abs = max(5000, mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); min_x = M
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g; min_x = x
    S1 = sum(1.0/e for e in A)
    return 2*mn, S1, min_x, mn

print("TEST: 2*min(G over [M, 30M]) > S1 for all primitive sets?")
print("=" * 70)
sys.stdout.flush()

fail = 0
fail_examples = []
total = 0
worst_deficit = 0
worst_deficit_set = None

t0 = time.time()
for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 50) if x % a1 != 0][:16]
    for tk in range(2, 8):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            twoMin, S1, min_x, mn = check(A, mult=15)
            deficit = S1 - twoMin
            if twoMin <= S1 + 1e-12:
                fail += 1
                if deficit > worst_deficit:
                    worst_deficit = deficit
                    worst_deficit_set = (tuple(A), twoMin, S1, min_x, mn)
                if len(fail_examples) < 15:
                    fail_examples.append((tuple(A), twoMin, S1, min_x, mn))

elapsed = time.time() - t0
print(f"\nChecked {total} primitive sets in {elapsed:.1f}s")
print(f"Failures (2*min(G) <= S1): {fail}")
print(f"Fraction: {100*fail/total:.3f}%")
print(f"Worst deficit: {worst_deficit:.6f}")

if fail_examples:
    print(f"\nFailure examples:")
    for A, tm, S1, min_x, mn in fail_examples[:10]:
        print(f"  {list(A)}: 2*minG={tm:.5f}, S1={S1:.5f}, deficit={S1-tm:.5f}, min_x={min_x}, minG={mn:.5f}")

# Also compute worst RATIO
print("\n" + "=" * 70)
print("Compare: worst RATIO max G / (2 min G)")
print("=" * 70)

def full_ratio(A, mult=15):
    M = max(A)
    h_abs = max(5000, mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g
        if g > mx: mx = g
    return mx, mn, mx/(2*mn) if mn > 0 else 999

worst_r = 0
worst_r_set = None
for A, tm, S1, min_x, mn in fail_examples:
    mx, mn2, rv = full_ratio(list(A))
    if rv > worst_r:
        worst_r = rv; worst_r_set = A
    print(f"  {list(A)}: maxG={mx:.5f}, minG={mn2:.5f}, S1={S1:.5f}, ratio={rv:.5f}")
    print(f"    Note: ratio uses maxG (not S1). maxG < S1: {mx < S1}")

print(f"\n  Even when 2*minG <= S1, ratio = maxG/(2*minG) < 1 because maxG < S1.")

print("\nDONE.")
