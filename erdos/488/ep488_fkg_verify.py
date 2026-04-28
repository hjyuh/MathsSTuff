"""
Verify FKG direction and test the key inequality delta >= 1-Pi vs delta <= 1-Pi.
Then prove the Bonferroni-4 bound via the subset-lcm lemma.
"""
from math import gcd, prod
from itertools import combinations

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def delta_exact(A):
    """Exact density via lcm period sieve."""
    L = A[0]
    for a in A[1:]:
        L = lcm2(L, a)
    if L > 5_000_000:
        return None
    hit = bytearray(L + 1)
    for a in A:
        for m in range(a, L + 1, a):
            hit[m] = 1
    return sum(hit) / L

def product_density(A):
    """1 - prod(1-1/a): the coprime/independent density."""
    p = 1.0
    for a in A:
        p *= (1 - 1.0/a)
    return 1 - p

# PART 1: FKG DIRECTION - verify delta <= 1-Pi for non-coprime
print("PART 1: FKG direction verification")
print("For non-coprime: delta <= 1-Pi(1-1/a) ?")
print("=" * 60)

test_sets = [
    [4, 6], [4, 6, 9], [4, 6, 9, 10], [4, 6, 9, 10, 14, 15],
    [6, 10, 15], [6, 10, 14, 15], [6, 10, 14, 15, 21, 22],
    [4, 6, 9, 10, 14, 15, 21, 22, 25, 26],
    [3, 5, 7], [2, 3, 5, 7],  # coprime sets for comparison
]

for A in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        print(f"  {A}: NOT PRIMITIVE")
        continue
    d = delta_exact(A)
    if d is None:
        print(f"  {A}: L too large")
        continue
    pd = product_density(A)
    cop = all(gcd(A[i],A[j])==1 for i in range(len(A)) for j in range(i+1,len(A)))
    direction = "delta = 1-Pi" if abs(d-pd)<1e-10 else ("delta < 1-Pi" if d < pd else "delta > 1-Pi")
    print(f"  {A}: delta={d:.6f}, 1-Pi={pd:.6f}, {direction}, "
          f"{'coprime' if cop else 'non-coprime'}")

# PART 2: The subset-lcm lemma
print("\n" + "=" * 60)
print("PART 2: lcm(S) >= 2*max(S) for all subsets S of primitive A, |S|>=2")
print("=" * 60)

violations = 0
total = 0
for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 26) if x % a1 != 0][:12]
    for tk in range(3, 7):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            # Check all subsets of size 2..k
            for sz in range(2, len(A)+1):
                for S in combinations(A, sz):
                    l = S[0]
                    for x in S[1:]:
                        l = lcm2(l, x)
                    mx = max(S)
                    total += 1
                    if l < 2*mx:
                        violations += 1
                        if violations <= 5:
                            print(f"  VIOLATION: A={A}, S={S}, lcm={l}, 2*max={2*mx}")

print(f"  Total subsets checked: {total}, violations: {violations}")

# PART 3: Can we prove Bonf-4 > S1/2 using lcm >= 2*max?
print("\n" + "=" * 60)
print("PART 3: Bonferroni-4 analysis using lcm >= 2*max")
print("=" * 60)

# For a primitive set with elements a1 < a2 < ... < ak:
# S_j <= sum_{l=j}^{k} C(l-1, j-1) / (2*a_l)
# because lcm(any j-subset with max = a_l) >= 2*a_l
#
# Then S2 - S3 + S4 <= sum_l [C(l-1,1) - C(l-1,2) + C(l-1,3)] / (2*a_l)
# = sum_l f(l) / (2*a_l)
# where f(l) = C(l-1,1) - C(l-1,2) + C(l-1,3)
#
# We need this <= S1/2 = sum_l 1/(2*a_l)
# i.e. sum_l (f(l)-1) / (2*a_l) <= 0
#
# f(l) for l=2,3,4: 1,1,1 (so f(l)-1 = 0)
# f(5) = 4-6+4 = 2, f(l)-1 = 1
# f(6) = 5-10+10 = 5, f(l)-1 = 4
# So for l >= 5: f(l)-1 > 0, contributing positively => bound FAILS

print("f(l) = C(l-1,1) - C(l-1,2) + C(l-1,3):")
for l in range(2, 12):
    c1 = l-1
    c2 = (l-1)*(l-2)//2 if l >= 3 else 0
    c3 = (l-1)*(l-2)*(l-3)//6 if l >= 4 else 0
    f = c1 - c2 + c3
    print(f"  l={l}: C({l-1},1)={c1}, C({l-1},2)={c2}, C({l-1},3)={c3}, f={f}")

print("\nf(l) grows cubically: the crude lcm >= 2*max bound is TOO WEAK for k >= 5.")
print("Need STRONGER lcm bounds for larger subsets.")

# PART 4: Better lcm bounds for j-subsets
print("\n" + "=" * 60)
print("PART 4: Actual lcm/max ratios for j-subsets of primitive sets")
print("=" * 60)

# For each j-subset, compute lcm(S)/max(S). The minimum over all subsets.
for tk in [4, 5, 6]:
    min_ratios = {}  # j -> min ratio
    for a1 in range(2, 10):
        pool = [x for x in range(a1+1, 20) if x % a1 != 0][:10]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            for sz in range(2, len(A)+1):
                for S in combinations(A, sz):
                    l = S[0]
                    for x in S[1:]:
                        l = lcm2(l, x)
                    mx = max(S)
                    r = l / mx
                    if sz not in min_ratios or r < min_ratios[sz][0]:
                        min_ratios[sz] = (r, S, A)

    print(f"\n  k={tk}: min lcm(S)/max(S) by subset size:")
    for sz in sorted(min_ratios):
        r, S, A = min_ratios[sz]
        print(f"    |S|={sz}: min ratio={r:.2f}, S={S}, A={A}")

print("\nDONE.")
