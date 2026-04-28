"""
Where does min G occur for general primitive sets?
For consecutive k-tuples: at x = 2a-1.
For non-consecutive sets: does it move?
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

def find_minmax_G(A, horizon_mult=30):
    M = max(A)
    a = min(A)
    h_abs = max(5000, horizon_mult * M)
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    run = 0
    for x in range(1, M):
        run += hit[x]
    min_g = float('inf'); max_g = 0.0
    min_x = max_x = M
    for x in range(M, h_abs + 1):
        run += hit[x]
        g = run / x
        if g < min_g:
            min_g = g; min_x = x
        if g > max_g:
            max_g = g; max_x = x
    return min_g, min_x, max_g, max_x

# PART 1: consecutive k-tuples - baseline
print("CONSECUTIVE k-TUPLES (baseline):")
print(f"{'k':>3} {'a':>5} {'min_x':>8} {'2a-1':>6} {'match':>6}")
for k in [3, 4, 5, 6]:
    for a in [5, 10, 20, 50]:
        A = list(range(a, a+k))
        if not is_primitive(A): continue
        mn, mx_pos, _, _ = find_minmax_G(A)
        match = "YES" if mx_pos == 2*a-1 else "no"
        print(f"{k:>3} {a:>5} {mx_pos:>8} {2*a-1:>6} {match:>6}")
sys.stdout.flush()

# PART 2: Non-consecutive primitive sets
print("\nNON-CONSECUTIVE PRIMITIVE SETS: where is min G?")
print("=" * 70)

test_sets = [
    # Prime sets
    ([2, 3, 5, 7], "4 primes"),
    ([3, 5, 7, 11], "4 primes from 3"),
    ([5, 7, 11, 13], "4 primes from 5"),
    ([2, 3, 5, 7, 11, 13], "6 primes"),
    # Scaled
    ([4, 6, 10, 14], "2*{2,3,5,7}"),
    ([6, 9, 15, 21], "3*{2,3,5,7}"),
    # Dense non-coprime
    ([4, 6, 9, 10], ""),
    ([4, 6, 9, 10, 14, 15], ""),
    # Sparse
    ([5, 7, 9, 11, 13], ""),
    ([3, 5, 7, 11, 13, 17, 19], ""),
    # Skipping elements
    ([3, 5, 11, 13], "gap"),
    ([5, 6, 13, 14], ""),
    ([7, 8, 15, 16], ""),
]
print(f"{'set':<30} {'min(A)':>6} {'min_x':>8} {'2a-1':>6} {'min_x/a':>8} {'F(min_x)':>8} {'min_g':>10} {'k/(2a-1)':>10}")
for A, label in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        print(f"{str(A):<30} NOT PRIMITIVE")
        continue
    k = len(A)
    a = min(A)
    mn, mn_x, mx, mx_x = find_minmax_G(A)
    # F(min_x)
    h_abs = max(5000, 30*max(A))
    hit = bytearray(h_abs + 1)
    for e in A:
        for m in range(e, h_abs + 1, e):
            hit[m] = 1
    F_min_x = sum(hit[1:mn_x+1])
    k_over_2a1 = k/(2*a-1)
    print(f"{str(A):<30} {a:>6} {mn_x:>8} {2*a-1:>6} {mn_x/a:>8.3f} {F_min_x:>8} {mn:>10.6f} {k_over_2a1:>10.6f}")
sys.stdout.flush()

# PART 3: Systematic search — where does min G occur?
print("\n" + "=" * 70)
print("SYSTEMATIC: location of min G for primitive sets, k=4..8, max<=50")
print("=" * 70)

# For each k and each A, record:
# - min_x / a ratio (where is min relative to smallest element?)
# - min_x / (2a-1) ratio (is it near 2a-1?)
location_stats = {}  # k -> list of (min_x - (2a-1))/a
for tk in range(4, 9):
    location_stats[tk] = []
    min_at_2am1 = 0
    total = 0
    min_before_2am1 = 0
    min_after_2am1 = 0
    max_offset = 0
    max_offset_set = None
    for a1 in range(3, min(16, 51-tk+1)):
        pool = [x for x in range(a1+1, 51) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            total += 1
            mn, mn_x, _, _ = find_minmax_G(A, horizon_mult=20)
            target = 2*a1 - 1
            if mn_x == target:
                min_at_2am1 += 1
            elif mn_x < target:
                min_before_2am1 += 1
            else:
                min_after_2am1 += 1
            offset = mn_x - target
            location_stats[tk].append(offset / a1)
            if abs(offset) > max_offset:
                max_offset = abs(offset)
                max_offset_set = (tuple(A), mn_x, target, mn)
    print(f"\nk={tk}: {total} sets")
    print(f"  min_x == 2a-1: {min_at_2am1} ({100*min_at_2am1/total:.1f}%)")
    print(f"  min_x < 2a-1:  {min_before_2am1}")
    print(f"  min_x > 2a-1:  {min_after_2am1}")
    if max_offset_set:
        A, mn_x, target, mn = max_offset_set
        print(f"  Worst offset: A={list(A)}, min_x={mn_x}, 2a-1={target}, mn={mn:.6f}")
    sys.stdout.flush()

# PART 4: The h/k > (2a-1)/(2a+1) check
print("\n" + "=" * 70)
print("h/k vs (2a-1)/(2a+1): does the x=2a-1 bound work?")
print("=" * 70)

works_count = 0
fails_count = 0
fails_examples = []

for a1 in range(3, 16):
    pool = [x for x in range(a1+1, 51) if x % a1 != 0][:18]
    for tk in range(4, 9):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            k = len(A)
            a = min(A)
            # h = #{b in A : b <= 2a-1}
            h = sum(1 for b in A if b <= 2*a-1)
            threshold = (2*a-1)/(2*a+1)
            if h/k > threshold:
                works_count += 1
            else:
                fails_count += 1
                if len(fails_examples) < 10:
                    fails_examples.append((tuple(A), h, k, threshold, h/k))

print(f"  h/k > (2a-1)/(2a+1): {works_count} sets")
print(f"  h/k <= threshold:    {fails_count} sets")
if fails_examples:
    print(f"  Examples where x=2a-1 bound fails:")
    for A, h, k, thr, ratio in fails_examples:
        print(f"    {list(A)}: h={h}, k={k}, h/k={ratio:.4f}, threshold={thr:.4f}")
sys.stdout.flush()

# PART 5: For sets where x=2a-1 fails, check EP-488 still holds
print("\n" + "=" * 70)
print("For x=2a-1 failure cases: does EP-488 still hold?")
print("=" * 70)
for A, h, k, thr, ratio in fails_examples:
    A = list(A)
    mn, mn_x, mx, mx_x = find_minmax_G(A)
    r = mx/(2*mn) if mn > 0 else 999
    print(f"  {A}: min_x={mn_x} (vs 2a-1={2*min(A)-1}), mn={mn:.5f}, mx={mx:.5f}, ratio={r:.5f}")

print("\nDONE.")
