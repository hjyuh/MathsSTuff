"""
Check 2*min G > S1 on LARGER primitive sets, including the 21-prime counter.
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

def check(A, mult=30):
    M = max(A)
    h_abs = max(5000, mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    mn = float('inf'); mx = 0; min_x = M
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < mn: mn = g; min_x = x
        if g > mx: mx = g
    S1 = sum(1.0/e for e in A)
    return mn, mx, S1, min_x

# Test known "hard" cases
print("TESTING HARD CASES")
print("=" * 70)

hard_sets = [
    # First k primes
    ([2,3,5,7], "first 4 primes"),
    ([2,3,5,7,11], "first 5 primes"),
    ([2,3,5,7,11,13], "first 6 primes"),
    ([2,3,5,7,11,13,17], "first 7 primes"),
    ([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73], "first 21 primes"),
    # Scaled
    ([4,6,10,14], "2*{2,3,5,7}"),
    ([4,6,10,14,22,26,34,38,46,58,62,74,82,86,94,106,118,122,134,142,146], "2*{first 21 primes}"),
    # Dense
    ([4,5,6,14], "dense 4"),
    ([4,6,9,10,14,15], "dense 6"),
    # Large k coprime
    ([2,3,5,7,11,13,17,19,23,29], "first 10 primes"),
    ([3,5,7,11,13,17,19,23,29,31,37,41], "odd primes 3-41"),
]

print(f"{'label':<30} {'k':>3} {'min G':>10} {'2*min G':>10} {'S1':>10} {'2mG>S1?':>8}")
print("-" * 80)

failed = []
for A, label in hard_sets:
    A = sorted(A)
    if not is_primitive(A): continue
    mn, mx, S1, min_x = check(A, mult=30)
    two_mn = 2*mn
    holds = two_mn > S1
    status = "YES" if holds else "NO"
    print(f"{label:<30} {len(A):>3} {mn:>10.6f} {two_mn:>10.6f} {S1:>10.6f} {status:>8}")
    if not holds:
        failed.append((A, two_mn, S1, mn, mx))
    sys.stdout.flush()

print()
if failed:
    print(f"FAILURES of 2*minG > S1:")
    for A, tm, S1, mn, mx in failed:
        ratio = mx/(2*mn) if mn > 0 else 999
        print(f"  {A}")
        print(f"    2*minG = {tm:.6f}, S1 = {S1:.6f}, deficit = {S1-tm:.6f}")
        print(f"    maxG = {mx:.6f}, ratio = {ratio:.6f}")
        print(f"    EP-488 status: ratio < 1 means {'HOLDS' if ratio < 1 else 'FAILS'}")

# Also systematically check all k up to 9
print("\n" + "=" * 70)
print("SYSTEMATIC: primitive sets with k up to 9, max <= 40")
print("=" * 70)
sys.stdout.flush()

total = 0
fails = 0
worst_deficit = 0
worst_set = None

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:16]
    for tk in range(2, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            mn, mx, S1, _ = check(A, mult=10)
            if 2*mn <= S1 + 1e-12:
                fails += 1
                deficit = S1 - 2*mn
                if deficit > worst_deficit:
                    worst_deficit = deficit
                    worst_set = (tuple(A), 2*mn, S1, mn, mx)

print(f"  Checked: {total}")
print(f"  Failures of 2*minG > S1: {fails}")
if worst_set:
    A, tm, S1, mn, mx = worst_set
    ratio = mx/(2*mn) if mn > 0 else 999
    print(f"  Worst: {list(A)}")
    print(f"    2*minG = {tm:.6f}, S1 = {S1:.6f}, deficit = {worst_deficit:.6f}")
    print(f"    maxG = {mx:.6f}, ratio = {ratio:.6f}")

print("\nDONE.")
