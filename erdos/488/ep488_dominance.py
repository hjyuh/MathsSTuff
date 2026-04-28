"""
Test the dominance claim: for every non-coprime primitive set A,
does there exist a coprime primitive set A' with S1(A') <= S1(A) and delta(A') <= delta(A)?

Equivalently: is 2*delta/S1 minimized by coprime sets?

Strategy: for each non-coprime primitive set, compute 2d/S1.
Compare with the WORST coprime set at similar S1.
"""
from math import gcd, log
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

def is_pairwise_coprime(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) > 1:
                return False
    return True

def delta_ie(A):
    k = len(A)
    d = 0.0
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            d += ((-1)**(size+1)) / l
    return d

# Collect ALL primitive sets with k=4..7, max<=35, compute (S1, delta, coprime?)
print("Collecting all primitive sets k=4..7, max<=35...")
print("=" * 60)

for tk in [4, 5, 6]:
    t0 = time.time()
    coprime_pts = []  # (S1, delta, set)
    noncoprime_pts = []
    me = min(35, 8 + 4*tk)

    for a1 in range(2, min(14, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:18]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            S1 = sum(1.0/a for a in A)
            delta = delta_ie(A)
            r = 2*delta/S1
            if is_pairwise_coprime(A):
                coprime_pts.append((S1, delta, r, tuple(A)))
            else:
                noncoprime_pts.append((S1, delta, r, tuple(A)))

    # Sort both by S1
    coprime_pts.sort()
    noncoprime_pts.sort()

    # For each non-coprime set, find the coprime set with closest S1 (from below)
    # and check if coprime delta <= non-coprime delta
    violations = 0
    worst_violation = None

    # Build sorted coprime S1 values for binary search
    coprime_S1 = [p[0] for p in coprime_pts]
    coprime_delta = [p[1] for p in coprime_pts]
    coprime_ratio = [p[2] for p in coprime_pts]

    import bisect
    for S1_nc, delta_nc, r_nc, A_nc in noncoprime_pts:
        # Find coprime sets with S1 <= S1_nc
        idx = bisect.bisect_right(coprime_S1, S1_nc + 1e-10) - 1
        if idx < 0:
            continue  # no coprime set with smaller S1

        # The claim: delta_nc >= delta of some coprime set with S1' <= S1_nc
        # Check: is there a coprime set with S1' <= S1_nc AND delta' <= delta_nc?
        found = False
        for i in range(max(0, idx-5), idx+1):
            if coprime_S1[i] <= S1_nc + 1e-10 and coprime_delta[i] <= delta_nc + 1e-10:
                found = True
                break
        # Also check: is 2*delta_nc/S1_nc >= min coprime ratio?
        # The WEAKER claim: non-coprime always has 2d/S1 >= coprime minimum
        min_coprime_r = min(coprime_ratio) if coprime_ratio else 999

        if not found and S1_nc > 0.5:  # only report for meaningful S1
            violations += 1
            if violations <= 5:
                # Find closest coprime
                closest = coprime_pts[idx] if idx >= 0 else None
                print(f"  VIOLATION k={tk}: NC={A_nc}, S1={S1_nc:.4f}, d={delta_nc:.4f}, "
                      f"r={r_nc:.4f}")
                if closest:
                    print(f"    Closest coprime: {closest[3]}, S1={closest[0]:.4f}, "
                          f"d={closest[1]:.4f}, r={closest[2]:.4f}")

    # Check the RATIO comparison: is min non-coprime ratio >= min coprime ratio?
    min_nc_r = min(r for _, _, r, _ in noncoprime_pts) if noncoprime_pts else 999
    min_c_r = min(r for _, _, r, _ in coprime_pts) if coprime_pts else 999

    el = time.time() - t0
    print(f"\n  k={tk}: {len(coprime_pts)} coprime, {len(noncoprime_pts)} non-coprime")
    print(f"  Min 2d/S1: coprime={min_c_r:.6f}, non-coprime={min_nc_r:.6f}")
    print(f"  Non-coprime ALWAYS >= coprime: {min_nc_r >= min_c_r - 1e-10}")
    print(f"  Dominance violations: {violations}")
    print(f"  Time: {el:.1f}s\n")

# DIRECT TEST: For fixed S1, which has lower delta: coprime or non-coprime?
print("=" * 60)
print("DIRECT TEST: For S1 ≈ 0.63, compare coprime vs non-coprime delta")
print("=" * 60)

target = 0.63
eps = 0.02
matches_c = []
matches_nc = []

for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 31) if x % a1 != 0][:16]
    for sub in combinations(pool, 3):
        A = [a1] + list(sub)
        if not is_primitive(A): continue
        S1 = sum(1.0/a for a in A)
        if abs(S1 - target) > eps: continue
        delta = delta_ie(A)
        if is_pairwise_coprime(A):
            matches_c.append((S1, delta, tuple(A)))
        else:
            matches_nc.append((S1, delta, tuple(A)))

matches_c.sort(key=lambda x: x[1])
matches_nc.sort(key=lambda x: x[1])

print(f"\nCoprime sets with S1 ≈ {target} (sorted by delta):")
for S1, d, A in matches_c[:8]:
    print(f"  {A}: S1={S1:.4f}, delta={d:.4f}, 2d/S1={2*d/S1:.4f}")

print(f"\nNon-coprime sets with S1 ≈ {target} (sorted by delta):")
for S1, d, A in matches_nc[:8]:
    print(f"  {A}: S1={S1:.4f}, delta={d:.4f}, 2d/S1={2*d/S1:.4f}")

if matches_c and matches_nc:
    min_c = min(d for _, d, _ in matches_c)
    min_nc = min(d for _, d, _ in matches_nc)
    print(f"\nMin delta: coprime={min_c:.6f}, non-coprime={min_nc:.6f}")
    print(f"Coprime has LOWER delta: {min_c < min_nc}")

# THEORETICAL ANALYSIS
print("\n" + "=" * 60)
print("THEORETICAL: for {a,b} coprime vs {a,b} with gcd>1")
print("=" * 60)

# Compare {p, q} coprime vs {a, b} non-coprime, same 1/a+1/b
# Coprime: delta = 1/a + 1/b - 1/(ab)
# Non-coprime (gcd=g>1): delta = 1/a + 1/b - g/(ab) = 1/a + 1/b - 1/lcm
# Since gcd > 1: 1/lcm > 1/(ab). So delta_nc < delta_c!

print("For pairs with same {1/a, 1/b}:")
print("  Coprime: delta = 1/a + 1/b - 1/(ab)")
print("  Non-coprime (gcd=g): delta = 1/a + 1/b - g/(ab)")
print("  Since g > 1 for non-coprime: delta_nc < delta_c")
print("  => Non-coprime pairs have LOWER delta for same S1!")
print("")

# But pairs have same S1 = 1/a+1/b. So non-coprime has LOWER delta.
# This DISPROVES the dominance claim for pairs!

# Wait: the claim is about different elements. For the SAME S1, can we find
# coprime and non-coprime with the same S1?
print("PAIR COMPARISON: same S1, different coprimality")
# {3, 5}: S1=1/3+1/5=8/15, delta = 8/15-1/15 = 7/15, coprime
# {4, 6}: S1=1/4+1/6=5/12, delta = 5/12-2/24 = 5/12-1/12 = 4/12 = 1/3
# Different S1. Let's find same S1:
# {a,b} coprime with S1 = s vs {c,d} non-coprime with S1 = s
# Example: {5, 12}: coprime, S1 = 1/5+1/12 = 17/60, delta = 17/60-1/60 = 16/60
# {4, 15}: coprime, S1 = 1/4+1/15 = 19/60, delta = 19/60-1/60 = 18/60
# {6, 10}: non-coprime(gcd=2), S1 = 1/6+1/10 = 4/15, delta = 4/15-1/30 = 7/30

# Hard to match S1 exactly. Let me try triples.
print("\nTRIPLE COMPARISON: matched S1")
# {3, 7, 11}: coprime, S1 = 1/3+1/7+1/11 = 0.524, delta = ?
# {4, 6, 35}: non-coprime?, S1 = 1/4+1/6+1/35 = 0.446... different

# Let me just check: for the SAME set of elements, coprime vs non-coprime is irrelevant
# (it's determined by the elements). The question is about DIFFERENT sets.

# The CORRECT formulation: among all primitive k-sets with S1 = s,
# which minimizes delta?

# For k=2: delta = S1 - S2. S2 = gcd/(a*b). For coprime: S2 = 1/(ab).
# For non-coprime: S2 = g/(ab) > 1/(ab). So delta_nc = S1 - g/(ab) < S1 - 1/(ab) = delta_c.
# Non-coprime has LOWER delta. => Coprime has HIGHER delta.
# => The dominance claim "non-coprime has higher delta" is FALSE for pairs!

print("\nCONCLUSION FOR PAIRS:")
print("  For pairs with same S1: coprime has HIGHER delta (OPPOSITE of claim)")
print("  delta = S1 - 1/lcm. Coprime: lcm = ab (largest). Non-coprime: lcm < ab.")
print("  Larger lcm => smaller S2 => higher delta.")
print("  So coprime maximizes delta, non-coprime minimizes it.")
print("")

# But the computation showed coprime sets have the WORST (smallest) 2d/S1 ratio!
# This seems contradictory. Let me check...

print("RESOLUTION: The worst 2d/S1 sets are coprime NOT because coprime has")
print("lower delta, but because coprime sets can achieve HIGHER S1 values.")
print("The first k primes pack the most reciprocal sum for given max element.")
print("Non-coprime sets with same max have lower S1 (blocked by divisibility).")
print("")
print("The correct statement: for FIXED S1, coprime has HIGHER delta,")
print("which means HIGHER 2d/S1. So coprime is the BEST case, not worst!")
print("The worst 2d/S1 comes from coprime sets at HIGH S1 values,")
print("not from non-coprime sets at the same S1.")

print("\nDONE.")
