"""Fast version of two-regime check."""
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

def is_pairwise_coprime(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) > 1:
                return False
    return True

def check_minmax(A, mult=8):
    M = max(A)
    h_abs = max(3000, mult * M)
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
    return mn, mx, run/h_abs

# Q1: S1 >= 1 implies min G > 1/2?
print("Q1: S1 >= 1 implies min G > 1/2?")
print("=" * 60)
sys.stdout.flush()

t0 = time.time()
fail_Q1 = []
total = 0
min_minG = float('inf')
min_set = None

for a1 in range(2, 10):
    pool = [x for x in range(a1+1, 60) if x % a1 != 0][:20]
    for tk in range(3, 13):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 < 1: continue
            total += 1
            mn, mx, delta = check_minmax(A, mult=5)
            if mn < min_minG:
                min_minG = mn; min_set = tuple(A)
            if mn <= 0.5 + 1e-12:
                fail_Q1.append((tuple(A), mn, S1, mx, delta))

elapsed = time.time() - t0
print(f"  Checked {total} sets in {elapsed:.1f}s")
print(f"  Failures (min G <= 1/2): {len(fail_Q1)}")
print(f"  Minimum min G: {min_minG:.5f} at {list(min_set) if min_set else None}")
if fail_Q1:
    fail_Q1.sort(key=lambda x: x[1])
    print(f"  Worst failures:")
    for A, mn, S1, mx, delta in fail_Q1[:5]:
        print(f"    {list(A)}: minG={mn:.5f}, S1={S1:.4f}, delta={delta:.4f}, maxG={mx:.5f}")
sys.stdout.flush()

# Q2: non-coprime with S1 >= 1 and delta <= 1/2?
print("\nQ2: Non-coprime with S1 >= 1 AND delta <= 1/2?")
print("=" * 60)
sys.stdout.flush()
t0 = time.time()
found = []
total2 = 0
for a1 in range(2, 10):
    pool = [x for x in range(a1+1, 60) if x % a1 != 0][:20]
    for tk in range(3, 13):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            if is_pairwise_coprime(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 < 1: continue
            total2 += 1
            mn, mx, delta = check_minmax(A, mult=5)
            if delta <= 0.5 + 1e-12:
                found.append((tuple(A), S1, delta, mn, mx))
print(f"  Checked {total2} non-coprime sets with S1 >= 1 in {time.time()-t0:.1f}s")
print(f"  With delta <= 1/2: {len(found)}")
if found:
    found.sort(key=lambda x: x[2])
    for A, S1, delta, mn, mx in found[:10]:
        print(f"    {list(A)}: S1={S1:.4f}, delta={delta:.4f}, minG={mn:.4f}, maxG={mx:.4f}")
else:
    print("  NONE FOUND.")
sys.stdout.flush()

# Q3: S1 < 1 implies 2*min G > S1?
print("\nQ3: S1 < 1 implies 2*min G > S1?")
print("=" * 60)
sys.stdout.flush()
t0 = time.time()
fail3 = []
total3 = 0
worst_deficit = 0
worst_set = None
for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 60) if x % a1 != 0][:20]
    for tk in range(2, 12):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/e for e in A)
            if S1 >= 1: continue
            total3 += 1
            mn, mx, _ = check_minmax(A, mult=5)
            if 2*mn <= S1 + 1e-12:
                deficit = S1 - 2*mn
                fail3.append((tuple(A), mn, S1, mx, deficit))
                if deficit > worst_deficit:
                    worst_deficit = deficit; worst_set = (tuple(A), mn, S1, mx)

print(f"  Checked {total3} sets with S1 < 1 in {time.time()-t0:.1f}s")
print(f"  Failures (2*min G <= S1): {len(fail3)}")
print(f"  Worst deficit: {worst_deficit:.6f}")
if worst_set:
    A, mn, S1, mx = worst_set
    r = mx/(2*mn) if mn > 0 else 999
    print(f"  At {list(A)}: minG={mn:.4f}, S1={S1:.4f}, ratio={r:.4f}")

# Final assessment
print("\n" + "=" * 60)
print("FINAL")
print("=" * 60)
Q1 = len(fail_Q1) == 0
Q2 = len(found) == 0
Q3 = len(fail3) == 0
print(f"  Q1 (S1>=1 => min G > 1/2): {'HOLDS' if Q1 else 'FAILS'}")
print(f"  Q2 (no non-coprime w/ S1>=1 AND delta<=1/2): {'HOLDS' if Q2 else 'FAILS'}")
print(f"  Q3 (S1<1 => 2*min G > S1): {'HOLDS' if Q3 else 'FAILS'}")

print("\nDONE.")
