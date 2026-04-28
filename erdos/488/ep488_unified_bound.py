"""
KEY LEMMA: 2*min G > min(S1, 1) for all primitive sets.
This gives EP-488 since max G <= S1 and max G < 1 always.
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

def check(A, mult=20):
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
    S1 = sum(1.0/e for e in A)
    return mn, mx, S1

print("CHECK: 2*min G > min(S1, 1) for all primitive sets?")
print("=" * 70)

# First: test on the known hard cases
hard = [
    [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73],
    [4,6,10,14,22,26,34,38,46,58,62,74,82,86,94,106,118,122,134,142,146],
    [2,3,5,7,11,13,17,19,23,29,31],
    [3,5,7,11,13,17,19,23,29,31,37,41,43,47],
    [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67],
]

for A in hard:
    A = sorted(A)
    if not is_primitive(A): continue
    mn, mx, S1 = check(A, mult=15)
    bound = min(S1, 1.0)
    holds = 2*mn > bound
    print(f"  k={len(A)}, |A|<=100..146: 2*min G={2*mn:.5f}, min(S1,1)={bound:.5f}, "
          f"max G={mx:.5f}, 2mG>bnd: {'YES' if holds else 'NO'}")
sys.stdout.flush()

# Systematic test
print("\n" + "=" * 70)
print("SYSTEMATIC: all primitive sets k=2..9, max<=40")
print("=" * 70)

t0 = time.time()
total = 0
fail = 0
worst_deficit = 0
worst_set = None
worst_ratio_found = 0
worst_ratio_set = None

for a1 in range(2, 15):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:16]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            mn, mx, S1 = check(A, mult=10)
            bound = min(S1, 1.0)
            if 2*mn <= bound + 1e-12:
                fail += 1
                deficit = bound - 2*mn
                if deficit > worst_deficit:
                    worst_deficit = deficit
                    worst_set = (tuple(A), 2*mn, bound, mn, mx, S1)
            ratio_val = mx/(2*mn) if mn > 0 else 999
            if ratio_val > worst_ratio_found:
                worst_ratio_found = ratio_val
                worst_ratio_set = tuple(A)

elapsed = time.time() - t0
print(f"  Checked {total} primitive sets in {elapsed:.1f}s")
print(f"  Failures of 2*min G > min(S1, 1): {fail}")
print(f"  Worst ratio observed: {worst_ratio_found:.6f} at {worst_ratio_set}")

if worst_set:
    A, tm, bnd, mn, mx, S1 = worst_set
    print(f"\n  Worst deficit case:")
    print(f"    A = {list(A)}")
    print(f"    2*min G = {tm:.6f}")
    print(f"    min(S1, 1) = {bnd:.6f}")
    print(f"    deficit = {worst_deficit:.6f}")
    print(f"    min G = {mn:.6f}, max G = {mx:.6f}")
sys.stdout.flush()

# Now test with larger pool and k
print("\n" + "=" * 70)
print("EXTENDED: k up to 12, larger pool")
print("=" * 70)

total2 = 0
fail2 = 0
fail2_examples = []

for a1 in range(2, 10):
    pool = [x for x in range(a1+1, 30) if x % a1 != 0][:15]
    for tk in range(5, 13):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total2 += 1
            mn, mx, S1 = check(A, mult=5)
            bound = min(S1, 1.0)
            if 2*mn <= bound + 1e-12:
                fail2 += 1
                if len(fail2_examples) < 5:
                    fail2_examples.append((tuple(A), 2*mn, bound, mn, mx))

print(f"  Checked {total2} primitive sets")
print(f"  Failures: {fail2}")
if fail2_examples:
    for A, tm, bnd, mn, mx in fail2_examples:
        print(f"    {list(A)}: 2*mG={tm:.5f}, bnd={bnd:.5f}, mG={mn:.5f}, MG={mx:.5f}")

print("\nDONE.")
