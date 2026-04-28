"""
For the k=5 counterexamples where R < 0:
1. Does EP-488 still hold? Check 2*inf(G) > sup(G).
2. Does the sparse-mass lemma apply?
3. What mechanism saves EP-488?
"""
from math import gcd
from itertools import combinations

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
    for size in range(1, len(A)+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            total += ((-1)**(size+1)) / l
    return total

def compute_R(A):
    S1 = sum(1.0/a for a in A)
    S2 = sum(gcd(A[i],A[j])/(A[i]*A[j]) for i in range(len(A)) for j in range(i+1,len(A)))
    return S1 - 2*S2, S1, S2

def check_ep488(A, horizon=None):
    """Full EP-488 check via sieve."""
    M = max(A)
    delta = density_ie(A)
    if horizon is None:
        horizon = max(3000, int(50/delta)+1) if delta > 0 else 5000
    hit = bytearray(horizon + 1)
    for a in A:
        for m in range(a, horizon + 1, a):
            hit[m] = 1
    f = [0]*(horizon+1)
    running = 0
    for x in range(1, horizon+1):
        running += hit[x]
        f[x] = running

    min_g = float('inf')
    max_g = 0.0
    for x in range(M, horizon+1):
        gx = f[x]/x
        if gx < min_g: min_g = gx
        if gx > max_g: max_g = gx

    S1 = sum(1.0/a for a in A)
    passes = 2*min_g > max_g
    ratio = max_g/(2*min_g) if min_g > 0 else 999
    return passes, ratio, min_g, max_g, delta, S1

# The 4 counterexamples
print("=" * 70)
print("k=5 COUNTEREXAMPLES: DETAILED ANALYSIS")
print("=" * 70)

counter_examples = [
    [4, 6, 9, 10, 15],
    [4, 6, 10, 14, 15],
    [8, 12, 18, 20, 30],
    [8, 12, 20, 28, 30],
]

for A in counter_examples:
    print(f"\n  A = {A}")
    R, S1, S2 = compute_R(A)
    print(f"  R = S1-2S2 = {R:.6f} (NEGATIVE)")
    print(f"  S1 = {S1:.6f}, 2/min = {2.0/A[0]:.6f}")
    print(f"  Dense: {S1 > 2.0/A[0]}")

    passes, ratio, min_g, max_g, delta, _ = check_ep488(A)
    print(f"  delta = {delta:.6f}")
    print(f"  min G = {min_g:.6f}, max G = {max_g:.6f}")
    print(f"  2*minG = {2*min_g:.6f}")
    print(f"  EP-488 (2*minG > maxG): {'PASS' if passes else 'FAIL'}")
    print(f"  Ratio maxG/(2*minG) = {ratio:.6f}")

    # What mechanism saves it?
    print(f"  --- Mechanism analysis ---")
    # Check third-order IE: use Bonferroni 3rd order for tighter bounds
    # G(n) >= S1 - S2 + S3 (where S3 = sum of 1/lcm(triples))
    S3 = 0.0
    for combo in combinations(A, 3):
        l = combo[0]
        for c in combo[1:]:
            l = lcm2(l, c)
        S3 += 1.0/l
    print(f"  S3 (triple overlaps) = {S3:.6f}")
    print(f"  delta >= S1-S2+S3 = {S1-S2+S3:.6f} (3rd order lower)")
    print(f"  R3 = S1 - 2S2 + 2S3 = {S1-2*S2+2*S3:.6f} (improved?)")

# Now check: can we prove R > 0 for quadruples ANALYTICALLY?
print("\n" + "=" * 70)
print("ANALYTIC PROOF ATTEMPT: R > 0 FOR QUADRUPLES")
print("=" * 70)

# For coprime quadruples: R = S1(1-S1) + sum(1/a^2)
# S1 < 1 for all coprime quads with min >= 3 => R > 0

# For non-coprime: need tighter analysis
# Key: each non-coprime pair (a_i, a_j) has gcd ≤ min/p where p = smallest prime of min
# For min = a: gcd(a, a_j) divides a, and gcd < a => gcd ≤ a/p_min(a)
# So 1/lcm = gcd/(a·a_j) ≤ 1/(p_min(a)·a_j)

# Compute the bound using this for the tightest quadruples
print("\nTightest quadruples and their R:")
tight = [(40,60,90,100), (20,30,45,50), (12,18,20,45),
         (8,12,18,20), (24,36,40,45), (36,40,45,56)]
for A in tight:
    A = list(sorted(A))
    if not is_primitive(A):
        print(f"  {A}: not primitive")
        continue
    R, S1, S2 = compute_R(A)
    # Crude bound
    a,b,c,d = A
    crude = 1.0/a - 1.0/c - 2.0/d
    print(f"  {A}: R={R:.6f}, crude_bound={crude:.6f}, S1={S1:.6f}")

# Check: for ALL non-coprime quadruples with a=4, is R > 0?
print("\nAll primitive quadruples with a=4, max<=50:")
min_R_a4 = float('inf')
min_set_a4 = None
for b in range(5, 51):
    if b % 4 == 0: continue
    for c in range(b+1, 51):
        if c % 4 == 0 or c % b == 0: continue
        for d in range(c+1, 51):
            if d % 4 == 0 or d % b == 0 or d % c == 0: continue
            A = [4,b,c,d]
            R, _, _ = compute_R(A)
            if R < min_R_a4:
                min_R_a4 = R
                min_set_a4 = tuple(A)
print(f"  Min R = {min_R_a4:.6f} at {min_set_a4}")

print("\nAll primitive quadruples with a=6, max<=50:")
min_R_a6 = float('inf')
min_set_a6 = None
for b in range(7, 51):
    if b % 6 == 0: continue
    for c in range(b+1, 51):
        if c % 6 == 0 or c % b == 0: continue
        for d in range(c+1, 51):
            if d % 6 == 0 or d % b == 0 or d % c == 0: continue
            A = [6,b,c,d]
            R, _, _ = compute_R(A)
            if R < min_R_a6:
                min_R_a6 = R
                min_set_a6 = tuple(A)
print(f"  Min R = {min_R_a6:.6f} at {min_set_a6}")

# For the tightest overall: {40,60,90,100}
# Can we prove R > 0 for all quads where all elements share a common factor?
print("\nQuadruples of form {m*a, m*b, m*c, m*d} where {a,b,c,d} is primitive:")
print("  R is INVARIANT under scaling: R(mA) = R(A)/m (since S1 scales by 1/m, S2 by 1/m²)")
print("  Wait, S1(mA) = S1(A)/m. S2(mA) = S2(A)/m². R(mA) = S1(A)/m - 2S2(A)/m².")
print("  NOT simply related. Let me check:")
for m in [1, 2, 4, 5, 10]:
    A0 = [4, 6, 9, 10]
    A = [m*x for x in A0]
    if not is_primitive(A):
        print(f"  m={m}: {A} not primitive")
        continue
    R, S1, _ = compute_R(A)
    print(f"  m={m}: A={A}, R={R:.6f}, S1={S1:.6f}")

print("\nDONE.")
