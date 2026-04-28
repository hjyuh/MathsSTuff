"""
Test: does truncated Bonferroni at order floor(k/2)*2 give delta > S1/2?

The IE series: delta = S1 - S2 + S3 - S4 + ...
Bonferroni: truncate at even order = lower bound.

We need: S1 - S2 + S3 - S4 + ... > S1/2
i.e.:    S1/2 > S2 - S3 + S4 - S5 + ...

The alternating tail T = S2 - S3 + S4 - ... satisfies delta = S1 - T.
Need T < S1/2.

Check: for each pair (S_{2j-1}, S_{2j}), is S_{2j-1} >= S_{2j}?
If yes: the pairs (S3-S4), (S5-S6), etc. are all non-negative,
and T = S2 - (S3-S4) - (S5-S6) - ... <= S2.
So T < S1/2 iff S2 < S1/2 (which fails at k=5).

But more precisely: T = S2 - S3 + S4 - S5 + ...
= S2 - (S3 - S4) - (S5 - S6) - ...
Each (S_{2j+1} - S_{2j+2}) >= 0 (Bonferroni). So T <= S2.

But we need T < S1/2, not T < S2.

For k=5: T = S2 - S3 + S4 - S5. And delta = S1 - T.
Need T < S1/2.
T = S2 - S3 + S4 - S5 = (S2-S3) + (S4-S5).
Both (S2-S3) and (S4-S5) are... not necessarily non-negative by Bonferroni.
Actually Bonferroni says: S1-S2+S3 is an upper bound (order 3, upper).
So delta <= S1-S2+S3, i.e., S3 >= S4-S5+... (remaining terms).

Let me just compute everything.
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

def all_ie_sums(A):
    """Compute S1, S2, ..., Sk."""
    k = len(A)
    sums = []
    for size in range(1, k+1):
        s = 0.0
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            s += 1.0/l
        sums.append(s)
    return sums

def delta_from_sums(sums):
    d = 0.0
    for j, s in enumerate(sums):
        d += ((-1)**j) * s  # j=0: +S1, j=1: -S2, etc.
    return d

# Compute for all primitive sets k=3..8, max<=30
print("BONFERRONI SERIES ANALYSIS")
print("=" * 60)

for tk in range(3, 9):
    t0 = time.time()
    me = min(30, 6 + 3*tk)
    worst_ratio = 1e9  # min of 2*delta/S1
    worst_set = None
    worst_sums = None
    count = 0
    # Track: does S_{2j-1} >= S_{2j} always?
    pair_violations = 0
    # Track: does Bonferroni-2 give delta > S1/2?
    bonf2_fails = 0
    # Track: does Bonferroni-4 give delta > S1/2?
    bonf4_fails = 0

    for a1 in range(2, min(13, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:16]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            count += 1
            sums = all_ie_sums(A)
            S1 = sums[0]
            delta = delta_from_sums(sums)
            r = 2*delta/S1 if S1 > 0 else 999

            if r < worst_ratio:
                worst_ratio = r
                worst_set = tuple(A)
                worst_sums = list(sums)

            # Check S_{2j-1} >= S_{2j}
            for j in range(1, len(sums)//2 + 1):
                if 2*j-1 < len(sums) and 2*j < len(sums):
                    if sums[2*j-1] < sums[2*j] - 1e-15:  # S_{2j} > S_{2j+1} (0-indexed)
                        pair_violations += 1

            # Bonferroni-2: delta >= S1-S2 > S1/2 ?
            bonf2 = sums[0] - sums[1]  # S1-S2
            if bonf2 <= sums[0]/2 + 1e-15:
                bonf2_fails += 1

            # Bonferroni-4: delta >= S1-S2+S3-S4 > S1/2 ?
            if len(sums) >= 4:
                bonf4 = sums[0] - sums[1] + sums[2] - sums[3]
            else:
                bonf4 = sums[0] - sums[1] + (sums[2] if len(sums)>2 else 0)
            if bonf4 <= sums[0]/2 + 1e-15:
                bonf4_fails += 1

    el = time.time() - t0
    print(f"\n  k={tk}: {count} sets, worst 2d/S1={worst_ratio:.6f}, {el:.1f}s")
    print(f"    Bonferroni-2 fails (S1-S2 <= S1/2): {bonf2_fails}")
    print(f"    Bonferroni-4 fails (S1-S2+S3-S4 <= S1/2): {bonf4_fails}")
    print(f"    Pair violations (S_{{2j}} > S_{{2j+1}}): {pair_violations}")
    if worst_set and worst_sums:
        print(f"    Worst set: {worst_set}")
        print(f"    Sums: " + ", ".join(f"S{i+1}={s:.6f}" for i, s in enumerate(worst_sums)))
        # Show the alternating partial sums
        partial = 0.0
        half = worst_sums[0]/2
        print(f"    S1/2 = {half:.6f}")
        print(f"    Alternating tail T = S2-S3+S4-... :")
        T = 0.0
        for j in range(1, len(worst_sums)):
            T += ((-1)**(j+1)) * worst_sums[j]  # +S2, -S3, +S4, ...
            trunc = worst_sums[0] - T  # = Bonferroni truncation
            marker = " <-- LOWER BOUND" if j % 2 == 1 else " <-- upper bound"
            ok = "OK" if trunc > half else "FAIL"
            print(f"      After S{j+1}: T={T:.6f}, trunc={trunc:.6f} "
                  f"{'>' if trunc > half else '<='} S1/2={half:.6f} [{ok}]{marker}")

# KEY TEST: S_{j} >= S_{j+1} for all j? (sufficient for alternating convergence)
print("\n" + "=" * 60)
print("KEY TEST: S_j >= S_{j+1} for all j and all primitive sets?")
print("=" * 60)

for tk in range(3, 8):
    me = min(25, 5 + 3*tk)
    violations = {}
    count = 0
    for a1 in range(2, min(11, me)):
        pool = [x for x in range(a1+1, me+1) if x % a1 != 0][:14]
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            count += 1
            sums = all_ie_sums(A)
            for j in range(len(sums)-1):
                if sums[j] < sums[j+1] - 1e-15:
                    key = (j+1, j+2)
                    if key not in violations:
                        violations[key] = (tuple(A), sums[j], sums[j+1])
    if violations:
        print(f"  k={tk}: {count} sets, VIOLATIONS at:")
        for (j1,j2), (A, sj, sj1) in sorted(violations.items()):
            print(f"    S{j1} < S{j2}: {A}, S{j1}={sj:.6f}, S{j2}={sj1:.6f}")
    else:
        print(f"  k={tk}: {count} sets, S_j >= S_{{j+1}} ALWAYS ✓")

print("\nDONE.")
