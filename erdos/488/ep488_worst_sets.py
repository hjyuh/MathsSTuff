"""
Find the TRUE worst cases for ratio(A), and understand their structure.
"""
from math import gcd
from itertools import combinations
import sys

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def full_analysis(A, mult=30):
    M = max(A); a = min(A); k = len(A)
    h = max(5000, mult * M)
    hit = bytearray(h + 1)
    for e in A:
        for m in range(e, h + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0
    min_x = max_x = M
    for x in range(M, h + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g; min_x = x
        if g > mx: mx = g; max_x = x
    S1 = sum(1.0/e for e in A)
    return {'min': mn, 'min_x': min_x, 'max': mx, 'max_x': max_x,
            'ratio': mx/(2*mn) if mn > 0 else 999, 'S1': S1, 'k': k, 'a': a, 'M': M}

# For each (a, k), find the MAXIMUM ratio across all primitive sets
print("MAX RATIO BY (a, k) — comparing consecutive vs best non-consecutive")
print("=" * 75)

for tk in [4, 5, 6, 7]:
    for a1 in [3, 5, 7, 10, 15, 20, 30]:
        # Consecutive
        B = list(range(a1, a1+tk))
        if not is_primitive(B): continue
        cons = full_analysis(B)
        cons_r = cons['ratio']

        # Search non-consecutive with same min, k
        pool = [x for x in range(a1+1, 3*a1 + 40) if x % a1 != 0][:25]
        if len(pool) < tk-1: continue
        best_nc = None
        best_r = 0
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            r_val = full_analysis(A, mult=15)['ratio']
            if r_val > best_r:
                best_r = r_val
                best_nc = A

        winner = "CONS" if cons_r >= best_r else "NON-CONS"
        print(f"  a={a1:>3} k={tk}: cons={cons_r:.5f}, best non-cons={best_r:.5f} "
              f"at {best_nc}, winner={winner}")
    sys.stdout.flush()

# The TRUE supremum across all primitive sets
print("\n" + "=" * 75)
print("GLOBAL SEARCH: highest ratio found across all primitive sets (max<=100)")
print("=" * 75)

worst_r = 0
worst_A = None
for a1 in range(3, 30):
    for tk in range(4, 10):
        pool = [x for x in range(a1+1, 101) if x % a1 != 0][:20]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            r_val = full_analysis(A, mult=15)['ratio']
            if r_val > worst_r:
                worst_r = r_val
                worst_A = A

# Also try large consecutive
for a in [50, 100, 200, 500, 1000]:
    for k in [2, 3, 4, 5, 6]:
        B = list(range(a, a+k))
        if not is_primitive(B): continue
        r_val = full_analysis(B, mult=15)['ratio']
        if r_val > worst_r:
            worst_r = r_val
            worst_A = B

print(f"  Global worst: ratio={worst_r:.6f} at A={worst_A}")
sys.stdout.flush()

# STRUCTURAL ANALYSIS: what does the "worst" non-consecutive set look like?
print("\n" + "=" * 75)
print("STRUCTURE OF THE WORST NON-CONSECUTIVE SETS")
print("=" * 75)

# From earlier: {9, 22, 23, 25, 26, 28, 29} was worst excess (0.111)
A = [9, 22, 23, 25, 26, 28, 29]
print(f"\nA = {A}")
r = full_analysis(A)
print(f"  k={r['k']}, a={r['a']}, M={r['M']}")
print(f"  min G = {r['min']:.6f} at x = {r['min_x']}")
print(f"  max G = {r['max']:.6f} at x = {r['max_x']}")
print(f"  ratio = {r['ratio']:.6f}")
print(f"  S1 = {r['S1']:.6f}")
print(f"  Structure: min(A) = 9, then elements in [22, 29] (all > 2a = 18)")
print(f"  Note: 'gap' between 9 and 22 means very few hits in [10, 21]")

# The pattern: a small min followed by a cluster of elements far away
# This creates a "dead zone" between min and the cluster where F barely grows
# So G drops to a very low value, then recovers when the cluster starts hitting
# The ratio max/(2*min) is larger than consecutive because min is pushed down

# Let me verify: at x in [10, 21], F only grows from multiples of 9 (which are 9, 18)
print(f"\n  F values in dead zone [9, 21]:")
hit = bytearray(200)
for e in A:
    for m in range(e, 200, e):
        hit[m] = 1
run = 0
for x in range(1, 22):
    run += hit[x]
    g = run/x if x >= 9 else 0
    marker = " <-- min zone" if 9 <= x <= 21 else ""
    print(f"    x={x:>3}: F={run}, G={g:.4f}{marker}" if 9 <= x <= 22 else "", end='')

# Try: ratio for the "bad" family {a, 2a+1, 2a+2, ..., 2a+k}
print("\n\nBAD FAMILY: {a, 2a+d, 2a+d+1, ..., 2a+d+k-1}")
for a in [5, 7, 9, 11]:
    for d in [4, 5, 6]:
        A = [a] + list(range(2*a+d, 2*a+d+5))
        if not is_primitive(A): continue
        r = full_analysis(A)
        cons = full_analysis(list(range(a, a+6)))
        print(f"  a={a}, d={d}: A={A}, ratio={r['ratio']:.4f}, cons={cons['ratio']:.4f}, "
              f"diff={r['ratio']-cons['ratio']:+.4f}")

print("\nDONE.")
