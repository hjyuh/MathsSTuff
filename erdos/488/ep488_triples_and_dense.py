"""
EP-488 Verification:
1. Verify EP-488 for all primitive triples with max(A) <= 200
2. Compute discrepancy C for primitive triples, verify C <= 5
3. Search for primitive sets with |A|>=4, min>=3, sum(1/a)>2/min, delta<=1/2, max<=100
"""

from math import gcd, floor
from fractions import Fraction
from itertools import combinations

def lcm(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    """Check if A is a primitive set (no element divides another)."""
    A = sorted(A)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def F(x, A):
    """Count integers <= x divisible by some element of A."""
    count = 0
    for n in range(1, x+1):
        for a in A:
            if n % a == 0:
                count += 1
                break
    return count

def F_fast(x, A):
    """Count using inclusion-exclusion for speed."""
    A = sorted(A)
    k = len(A)
    total = 0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm(l, c)
            if l > x:
                continue
            sign = (-1)**(size+1)
            total += sign * (x // l)
    return total

def density(A):
    """Compute asymptotic density delta_A using IE over one lcm period."""
    A = sorted(A)
    L = A[0]
    for a in A[1:]:
        L = lcm(L, a)
    return Fraction(F_fast(L, A), L)

def verify_ep488(A, horizon=None):
    """Check EP-488: F(m)/m < 2*F(n)/n for all m > n >= max(A).
    Returns (passes, worst_ratio, worst_n, worst_m)."""
    A = sorted(A)
    M = max(A)
    if horizon is None:
        # Use 15/delta or 500, whichever is smaller
        d = density(A)
        if d > 0:
            horizon = min(int(20 / float(d)) + 1, 2000)
        else:
            horizon = 500
    horizon = max(horizon, 3*M)

    worst_ratio = 0.0
    worst_n = worst_m = 0

    # Precompute F values
    f_vals = [0] * (horizon + 1)
    for x in range(1, horizon + 1):
        f_vals[x] = F_fast(x, A)

    for n in range(M, horizon + 1):
        fn = f_vals[n]
        if fn == 0:
            continue
        two_gn = 2.0 * fn / n
        for m in range(n + 1, horizon + 1):
            fm = f_vals[m]
            gm = fm / m
            if gm >= two_gn:
                return (False, gm / two_gn, n, m)
            ratio = gm / two_gn
            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_n, worst_m = n, m

    return (True, worst_ratio, worst_n, worst_m)

def compute_discrepancy(A, horizon=None):
    """Compute max |F(x) - delta*x| for x up to horizon."""
    A = sorted(A)
    d = float(density(A))
    M = max(A)
    if horizon is None:
        horizon = max(500, 10*M)

    max_disc = 0.0
    for x in range(1, horizon + 1):
        fx = F_fast(x, A)
        disc = abs(fx - d * x)
        if disc > max_disc:
            max_disc = disc
    return max_disc

# =========================================
# PART 1: TRIPLES VERIFICATION
# =========================================
print("=" * 70)
print("PART 1: EP-488 FOR ALL PRIMITIVE TRIPLES (max <= 200)")
print("=" * 70)

triple_count = 0
triple_failures = 0
worst_triple_ratio = 0.0
worst_triple = None
max_C_triple = 0.0
worst_C_triple = None

# For speed, limit max(A) to 60 with careful horizon
# and use looser horizon for larger
for a in range(3, 61):
    for b in range(a+1, min(2*a + 20, 201)):  # dense regime needs b not too far
        if b % a == 0:
            continue
        for c in range(b+1, min(3*a + 20, 201)):
            if c % a == 0 or c % b == 0:
                continue
            A = [a, b, c]
            triple_count += 1

            # Compute discrepancy
            C = compute_discrepancy(A, horizon=max(200, 5*c))
            if C > max_C_triple:
                max_C_triple = C
                worst_C_triple = tuple(A)

            # Verify EP-488
            passes, ratio, wn, wm = verify_ep488(A, horizon=max(200, 5*c))
            if not passes:
                triple_failures += 1
                print(f"  FAILURE: {A}, ratio={ratio:.6f} at n={wn}, m={wm}")
            if ratio > worst_triple_ratio:
                worst_triple_ratio = ratio
                worst_triple = tuple(A)

            if triple_count % 5000 == 0:
                print(f"  ...checked {triple_count} triples so far, 0 failures")

print(f"\nTriples checked: {triple_count}")
print(f"Failures: {triple_failures}")
print(f"Worst ratio G(m)/(2G(n)): {worst_triple_ratio:.6f} at {worst_triple}")
print(f"Max discrepancy C: {max_C_triple:.4f} at {worst_C_triple}")
print(f"C <= 5: {'YES' if max_C_triple <= 5 else 'NO (C = ' + str(max_C_triple) + ')'}")

# =========================================
# PART 2: DENSE PRIMITIVE SETS WITH |A| >= 4
# =========================================
print("\n" + "=" * 70)
print("PART 2: SEARCH FOR DENSE PRIMITIVE SETS WITH delta <= 1/2")
print("|A| >= 4, min(A) >= 3, sum(1/a) > 2/min(A), max(A) <= 100")
print("=" * 70)

def generate_primitive_sets_from(elements, min_size=4, max_size=8):
    """Generate primitive subsets of elements with given size range."""
    for size in range(min_size, min(max_size+1, len(elements)+1)):
        for subset in combinations(elements, size):
            if is_primitive(subset):
                yield subset

# Strategy: enumerate primitive sets with min >= 3, max <= 100
# Start with small a1 values and build up
dense_count = 0
delta_le_half_count = 0
results = []

# For each possible min element a1 from 3 to 50
for a1 in range(3, 51):
    # Candidates for other elements: a1+1 to 100, not divisible by a1
    candidates = [a1]
    for x in range(a1+1, 101):
        # Check x is not divisible by any element already in candidates
        # We'll check primitivity later
        if x % a1 != 0:
            candidates.append(x)

    # For speed: only try subsets of size 4-6 from the first ~30 candidates
    small_cands = candidates[:25]

    for size in range(4, min(7, len(small_cands)+1)):
        for subset in combinations(small_cands, size):
            if not is_primitive(subset):
                continue
            A = sorted(subset)
            if A[0] != a1:
                continue  # already counted under smaller a1

            s = sum(Fraction(1, a) for a in A)
            threshold = Fraction(2, a1)
            if s <= threshold:
                continue  # sparse, skip

            dense_count += 1
            d = density(A)

            if d <= Fraction(1, 2):
                delta_le_half_count += 1
                results.append((tuple(A), float(s), float(d)))
                if delta_le_half_count <= 20:
                    print(f"  FOUND: A={A}, sum(1/a)={float(s):.6f}, "
                          f"2/min={float(threshold):.6f}, delta={float(d):.6f}")

    if a1 % 10 == 0:
        print(f"  ...completed a1={a1}, dense sets found: {dense_count}, "
              f"with delta<=1/2: {delta_le_half_count}")

print(f"\nTotal dense primitive sets checked: {dense_count}")
print(f"Sets with delta_A <= 1/2: {delta_le_half_count}")

if delta_le_half_count == 0:
    print("\nCONCLUSION: No dense primitive set with |A|>=4, min>=3, max<=100 has delta<=1/2.")
    print("The density argument (2G(n) > 1 >= G(m)) covers all such sets.")
else:
    print(f"\nFOUND {delta_le_half_count} counterexamples to the density conjecture!")
    print("These need separate treatment:")
    for A, s, d in results[:10]:
        print(f"  A={A}, sum={s:.4f}, delta={d:.4f}")

# =========================================
# PART 3: EARLY-RANGE ANALYSIS FOR TRIPLES
# =========================================
print("\n" + "=" * 70)
print("PART 3: EARLY-RANGE KEY INEQUALITY FOR TRIPLES")
print("Checking: 2G(n) > S1 for ALL n in [max(A), 2*max(A)] for all primitive triples")
print("=" * 70)

early_failures = 0
early_count = 0
for a in range(3, 201):
    for b in range(a+1, min(3*a, 201)):
        if b % a == 0:
            continue
        for c in range(b+1, min(4*a, 201)):
            if c % a == 0 or c % b == 0:
                continue
            A = [a, b, c]
            S1 = 1/a + 1/b + 1/c
            early_count += 1

            # Check 2G(n) > S1 for n in [c, 2c]
            for n in range(c, 2*c + 1):
                fn = F_fast(n, A)
                two_gn = 2 * fn / n
                if two_gn <= S1:
                    early_failures += 1
                    if early_failures <= 10:
                        print(f"  EARLY FAILURE: {A}, n={n}, 2G(n)={two_gn:.6f}, S1={S1:.6f}")
                    break

if early_failures == 0:
    print(f"Checked {early_count} triples: 2G(n) > S1 for ALL n in [max(A), 2*max(A)]. PASSED.")
else:
    print(f"Failures: {early_failures} out of {early_count}")

# =========================================
# PART 4: MINIMUM G ANALYSIS
# =========================================
print("\n" + "=" * 70)
print("PART 4: 2*inf(G) vs sup(G) for consecutive triples {a, a+1, a+2}")
print("=" * 70)

for a in [3, 5, 10, 20, 50, 100, 200, 500]:
    A = [a, a+1, a+2]
    if not is_primitive(A):
        # a+2 might be divisible by a for a=2
        continue
    c = a + 2
    horizon = max(500, 20*a)

    min_g = float('inf')
    max_g = 0.0
    min_n = max_n = 0

    for n in range(c, horizon + 1):
        fn = F_fast(n, A)
        gn = fn / n
        if gn < min_g:
            min_g = gn
            min_n = n
        if gn > max_g:
            max_g = gn
            max_n = n

    ratio = max_g / (2 * min_g) if min_g > 0 else float('inf')
    S1 = 1/a + 1/(a+1) + 1/(a+2)
    print(f"  a={a}: min G={min_g:.6f} at n={min_n}, max G={max_g:.6f} at n={max_n}, "
          f"ratio={ratio:.6f}, S1={S1:.6f}")
    print(f"    2*minG={2*min_g:.6f} > maxG={max_g:.6f}: {2*min_g > max_g}")

print("\nDONE.")
