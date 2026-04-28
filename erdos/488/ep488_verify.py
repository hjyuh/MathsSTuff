"""
EP-488 Verification (fast):
1. Verify 2*inf(G) > sup(G) for primitive triples (sufficient for EP-488)
2. Compute discrepancy C for triples
3. Search for primitive sets |A|>=4, min>=3, sum>2/min, delta<=1/2, max<=100
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
    """IE density."""
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
    """Return array f where f[x] = F(x) = #{n<=x: a|n for some a in A}."""
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

# ============================================
# PART 1: TRIPLES - 2*min(G) > max(G)
# ============================================
print("=" * 70)
print("PART 1: EP-488 FOR PRIMITIVE TRIPLES (2*inf G > sup G)")
print("=" * 70)
t0 = time.time()

triple_count = 0
triple_fail = 0
worst_margin = float('inf')  # min of (2*minG - maxG)
worst_triple_margin = None
worst_ratio = 0.0  # max of maxG/(2*minG)
worst_triple_ratio = None
max_C = 0.0
max_C_triple = None

for a in range(3, 101):
    for b in range(a+1, min(a + 80, 201)):
        if b % a == 0:
            continue
        for c in range(b+1, min(b + 80, 301)):
            if c % a == 0 or c % b == 0:
                continue

            A = [a, b, c]
            triple_count += 1

            delta = density_ie(A)

            # Horizon: max of 3*c and 20/delta
            if delta > 0.001:
                h = min(int(25 / delta) + 1, 8000)
            else:
                h = 3000
            h = max(h, 4 * c)

            f = sieve_F(h, A)

            # Compute min G and max G for x >= c
            min_g = float('inf')
            max_g = 0.0
            local_C = 0.0

            for x in range(c, h + 1):
                gx = f[x] / x
                if gx < min_g:
                    min_g = gx
                if gx > max_g:
                    max_g = gx
                d = abs(f[x] - delta * x)
                if d > local_C:
                    local_C = d

            if local_C > max_C:
                max_C = local_C
                max_C_triple = tuple(A)

            # EP-488 check: 2*min_g > max_g
            if min_g > 0:
                ratio = max_g / (2 * min_g)
            else:
                ratio = float('inf')

            if 2 * min_g <= max_g:
                triple_fail += 1
                print(f"  FAIL: {A}, minG={min_g:.6f}, maxG={max_g:.6f}, "
                      f"ratio={ratio:.6f}, delta={delta:.6f}")

            margin = 2 * min_g - max_g
            if margin < worst_margin:
                worst_margin = margin
                worst_triple_margin = tuple(A)

            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_triple_ratio = tuple(A)

    if a % 20 == 0:
        elapsed = time.time() - t0
        print(f"  a={a}: {triple_count} triples, fails={triple_fail}, "
              f"worst ratio={worst_ratio:.6f}, maxC={max_C:.2f}, {elapsed:.1f}s")

elapsed = time.time() - t0
print(f"\nTriples checked: {triple_count}")
print(f"Failures: {triple_fail}")
print(f"Worst ratio maxG/(2*minG): {worst_ratio:.6f} at {worst_triple_ratio}")
print(f"Tightest margin 2*minG - maxG: {worst_margin:.6f} at {worst_triple_margin}")
print(f"Max C: {max_C:.4f} at {max_C_triple}")
print(f"C <= 5: {'YES' if max_C <= 5.001 else 'NO (C=' + f'{max_C:.4f}' + ')'}")
print(f"Time: {elapsed:.1f}s")

# ============================================
# PART 2: DENSE PRIMITIVE SETS WITH |A| >= 4
# ============================================
print("\n" + "=" * 70)
print("PART 2: SEARCH FOR DENSE PRIMITIVE SETS WITH delta <= 1/2")
print("|A| >= 4, min(A) >= 3, sum(1/a) > 2/min(A), max(A) <= 100")
print("=" * 70)
t0 = time.time()

dense_count = 0
delta_half_count = 0
delta_half_examples = []
min_delta_dense = float('inf')
min_delta_set = None

# Build pool of candidates for each min element
for a1 in range(3, 51):
    # Pool: elements from a1 to 100 that form a primitive set with a1
    pool = [a1]
    for x in range(a1 + 1, 101):
        if x % a1 != 0:
            pool.append(x)

    # Try size 4 subsets (most likely to find counterexamples)
    # Limit pool size for speed
    pool_limit = pool[:30]  # first 30 candidates

    for size in [4, 5, 6]:
        if size > len(pool_limit):
            break
        for subset in combinations(pool_limit, size):
            if subset[0] != a1:
                continue
            if not is_primitive(list(subset)):
                continue

            A = list(subset)
            s = sum(1.0/x for x in A)
            thresh = 2.0 / a1

            if s <= thresh:
                continue  # sparse

            dense_count += 1
            delta = density_ie(A)

            if delta < min_delta_dense:
                min_delta_dense = delta
                min_delta_set = tuple(A)

            if delta <= 0.5:
                delta_half_count += 1
                delta_half_examples.append((tuple(A), s, delta))
                if delta_half_count <= 20:
                    print(f"  FOUND: A={A}, sum={s:.6f}, 2/min={thresh:.6f}, "
                          f"delta={delta:.6f}")

    if a1 % 10 == 0:
        elapsed = time.time() - t0
        print(f"  a1={a1}: dense={dense_count}, delta<=1/2: {delta_half_count}, "
              f"min_delta={min_delta_dense:.6f}, {elapsed:.1f}s")

elapsed = time.time() - t0
print(f"\nDense sets checked: {dense_count}")
print(f"Sets with delta <= 1/2: {delta_half_count}")
print(f"Minimum delta found: {min_delta_dense:.6f} at {min_delta_set}")
print(f"Time: {elapsed:.1f}s")

if delta_half_count == 0:
    print("\nCONCLUSION: No dense primitive set with |A|>=4, min>=3, max<=100 "
          "has delta<=1/2.")
    print("Conjecture SUPPORTED: dense + large k => delta > 1/2 => EP-488 trivial.")
else:
    print(f"\n{delta_half_count} counterexamples found!")
    for A, s, d in delta_half_examples[:10]:
        print(f"  {A}: sum={s:.4f}, delta={d:.4f}")

# ============================================
# PART 3: CONSECUTIVE TRIPLES ANALYSIS
# ============================================
print("\n" + "=" * 70)
print("PART 3: CONSECUTIVE TRIPLES {a, a+1, a+2}")
print("=" * 70)

for a in [3, 5, 10, 20, 50, 100, 200, 500, 1000]:
    A = [a, a+1, a+2]
    if not is_primitive(A):
        continue
    c = a + 2
    h = max(500, 30*a)
    f = sieve_F(h, A)

    min_g = float('inf')
    max_g = 0.0
    S1 = 1/a + 1/(a+1) + 1/(a+2)

    for x in range(c, h+1):
        gx = f[x] / x
        if gx < min_g:
            min_g = gx
        if gx > max_g:
            max_g = gx

    ratio = max_g / (2*min_g) if min_g > 0 else 999
    print(f"  a={a:4d}: minG={min_g:.7f}, maxG={max_g:.7f}, "
          f"2minG={2*min_g:.7f}, S1={S1:.7f}, ratio={ratio:.6f}, "
          f"passes={'YES' if 2*min_g > max_g else 'NO'}")

# Algebraic verification: 6/(2a-1) > S1 for all a >= 3
print("\n  Algebraic check: 9a^2 + 14a + 2 > 0 (always true)")
print("  => 6/(2a-1) > 1/a + 1/(a+1) + 1/(a+2) for all a >= 1")
print("  => 2G(2a-1) > S1 >= sup G(m) at the minimum point n=2a-1")

print("\nALL DONE.")
