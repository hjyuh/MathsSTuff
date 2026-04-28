"""
For the dense primitive sets with delta <= 1/2 found in the search,
verify EP-488 directly: 2*inf(G) > sup(G).
Also check: does the IE comparison or discrepancy tail still work?
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

def density_ie(A):
    total = 0.0
    k = len(A)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            total += ((-1)**(size+1)) / l
    return total

def sieve_F(h, A):
    hit = bytearray(h + 1)
    for a in A:
        for m in range(a, h + 1, a):
            hit[m] = 1
    f = [0] * (h + 1)
    running = 0
    for x in range(1, h + 1):
        running += hit[x]
        f[x] = running
    return f

# Test specific examples from the search
test_sets = [
    [4, 5, 6, 14],
    [4, 5, 6, 17],
    [4, 5, 6, 22],
    [4, 5, 6, 34],
    [4, 5, 7, 26],
    [4, 5, 9, 11],
    [3, 5, 7, 11],
    [3, 7, 11, 13],
    [3, 8, 10, 14],  # might not be primitive
    [6, 10, 14, 15],
    [6, 10, 21, 25],
    [48, 60, 72, 75],  # min delta from search
]

print("=" * 80)
print("EP-488 CHECK FOR DENSE PRIMITIVE SETS WITH delta <= 1/2")
print("=" * 80)

for A in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        print(f"  {A}: NOT PRIMITIVE, skipping")
        continue

    s = sum(1.0/x for x in A)
    thresh = 2.0 / A[0]
    delta = density_ie(A)
    c = max(A)

    h = max(2000, 30*c)
    f = sieve_F(h, A)

    min_g = float('inf')
    max_g = 0.0
    min_n = max_n = 0

    for x in range(c, h+1):
        gx = f[x] / x
        if gx < min_g:
            min_g = gx
            min_n = x
        if gx > max_g:
            max_g = gx
            max_n = x

    passes = 2 * min_g > max_g
    ratio = max_g / (2*min_g) if min_g > 0 else 999

    # Compute discrepancy
    max_disc = 0.0
    for x in range(1, h+1):
        d = abs(f[x] - delta * x)
        if d > max_disc:
            max_disc = d

    print(f"\n  A={A}")
    print(f"    sum(1/a)={s:.6f}, 2/min={thresh:.6f}, dense={'YES' if s>thresh else 'NO'}")
    print(f"    delta={delta:.6f}, delta>1/2: {'YES' if delta>0.5 else 'NO'}")
    print(f"    minG={min_g:.6f} at n={min_n}, maxG={max_g:.6f} at n={max_n}")
    print(f"    2*minG={2*min_g:.6f}, ratio={ratio:.6f}")
    print(f"    EP-488 (2*minG > maxG): {'PASS' if passes else 'FAIL'}")
    print(f"    Discrepancy C={max_disc:.4f}")

# Now do a SYSTEMATIC check: for ALL dense primitive sets with min=3 or 4,
# max <= 40, |A| = 4, verify EP-488
print("\n" + "=" * 80)
print("SYSTEMATIC EP-488 CHECK FOR ALL DENSE 4-ELEMENT SETS, max <= 40")
print("=" * 80)

t0 = time.time()
checked = 0
failed = 0
worst_r = 0.0
worst_A = None

for a1 in range(3, 21):
    pool = [x for x in range(a1, 41) if x == a1 or x % a1 != 0]
    for subset in combinations(pool, 4):
        if subset[0] != a1:
            continue
        A = list(subset)
        if not is_primitive(A):
            continue
        s = sum(1.0/x for x in A)
        if s <= 2.0/a1:
            continue

        checked += 1
        c = max(A)
        delta = density_ie(A)
        h = max(1000, 20*c)
        f = sieve_F(h, A)

        min_g = float('inf')
        max_g = 0.0
        for x in range(c, h+1):
            gx = f[x] / x
            if gx < min_g:
                min_g = gx
            if gx > max_g:
                max_g = gx

        passes = 2 * min_g > max_g
        ratio = max_g / (2*min_g) if min_g > 0 else 999

        if not passes:
            failed += 1
            print(f"  FAIL: {A}, delta={delta:.4f}, minG={min_g:.6f}, maxG={max_g:.6f}")

        if ratio > worst_r:
            worst_r = ratio
            worst_A = tuple(A)

elapsed = time.time() - t0
print(f"\nChecked: {checked} dense primitive 4-sets")
print(f"Failures: {failed}")
print(f"Worst ratio: {worst_r:.6f} at {worst_A}")
print(f"Time: {elapsed:.1f}s")

# Also check size 5 and 6
print("\n" + "=" * 80)
print("SYSTEMATIC EP-488 CHECK FOR DENSE 5,6-ELEMENT SETS, max <= 30")
print("=" * 80)

for target_size in [5, 6]:
    t0 = time.time()
    checked = 0
    failed = 0
    worst_r = 0.0
    worst_A = None

    for a1 in range(3, 11):
        pool = [x for x in range(a1, 31) if x == a1 or x % a1 != 0]
        for subset in combinations(pool, target_size):
            if subset[0] != a1:
                continue
            A = list(subset)
            if not is_primitive(A):
                continue
            s = sum(1.0/x for x in A)
            if s <= 2.0/a1:
                continue

            checked += 1
            c = max(A)
            delta = density_ie(A)
            h = max(800, 15*c)
            f = sieve_F(h, A)

            min_g = float('inf')
            max_g = 0.0
            for x in range(c, h+1):
                gx = f[x] / x
                if gx < min_g:
                    min_g = gx
                if gx > max_g:
                    max_g = gx

            ratio = max_g / (2*min_g) if min_g > 0 else 999
            if 2*min_g <= max_g:
                failed += 1
                print(f"  FAIL |A|={target_size}: {A}, delta={delta:.4f}")
            if ratio > worst_r:
                worst_r = ratio
                worst_A = tuple(A)

    elapsed = time.time() - t0
    print(f"  |A|={target_size}: checked={checked}, fails={failed}, "
          f"worst={worst_r:.6f} at {worst_A}, {elapsed:.1f}s")

print("\nDONE.")
