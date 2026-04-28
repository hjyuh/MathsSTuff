"""
Analyze the structure of subsets S with lcm(S) <= max(A).
For each primitive set: count by subset size, and analyze the elements involved.
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

def count_by_size(A):
    """Count subsets with lcm <= max(A), broken down by size."""
    M = max(A)
    k = len(A)
    counts = {}
    examples = {}
    for size in range(1, k+1):
        cnt = 0
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            if l <= M:
                cnt += 1
                if size not in examples:
                    examples[size] = combo
        counts[size] = cnt
    return counts, examples

# Detailed analysis for specific sets
print("DETAILED SUBSET ANALYSIS")
print("=" * 70)

test_sets = [
    [2, 3, 5, 7, 11, 13, 17, 19, 23],
    [4, 6, 10, 14, 22, 26, 34, 38, 46],
    [6, 10, 15, 35],
    [6, 10, 14, 15, 21, 22, 35],
    [4, 6, 9, 10, 14, 15, 21, 22, 25, 26],
    [3, 4, 5, 7, 11, 13, 17, 19, 23, 29],
    [2, 3, 5, 7, 11, 13, 17, 19],
    [4, 6, 10, 14, 22, 26, 34, 38],
]

for A in test_sets:
    A = sorted(A)
    if not is_primitive(A):
        print(f"\n{A}: NOT PRIMITIVE")
        continue
    k = len(A)
    M = max(A)
    counts, examples = count_by_size(A)
    total = sum(counts.values())
    bound = k*(k+1)//2

    # Count elements <= M/2
    half_count = sum(1 for a in A if a <= M/2)

    print(f"\nA = {A}")
    print(f"  k={k}, M={M}, M/2={M/2}, elements <= M/2: {half_count}")
    print(f"  Bound k(k+1)/2 = {bound}")
    print(f"  Total subsets with lcm <= M: {total}")
    print(f"  Breakdown by size:")
    for size in sorted(counts):
        if counts[size] > 0:
            max_possible = len(list(combinations(range(half_count), size))) if size <= half_count else 0
            ex = f"  e.g. {examples[size]}" if size in examples else ""
            print(f"    |S|={size}: {counts[size]}" + ex)
    print(f"  Passes: {'YES' if total <= bound else 'NO'}")

# ============================================
# KEY STRUCTURAL ANALYSIS
# ============================================
print("\n" + "=" * 70)
print("STRUCTURAL ANALYSIS: What determines the count?")
print("=" * 70)

# For each set, identify: how many elements <= M/2?
# All subsets with lcm <= M must have ALL elements <= M/2 (by lcm >= 2*max).
# So count <= 2^{half_count} - 1.
# But also: for pairs within [1, M/2], lcm >= 2*max(pair).
# If both elements <= M/2: lcm >= 2*(second element) which could be <= M.

# The count of pairs: C(half_count, 2) pairs, but not all have lcm <= M.
# A pair {a, b} with a < b <= M/2: lcm(a,b) >= 2b. Need 2b <= M, i.e., b <= M/2. Always true.
# So ALL pairs within A ∩ [1, M/2] have lcm <= M? Let's check.

print("\nClaim: for pairs {a,b} with a < b <= M/2 in primitive A: lcm(a,b) <= M always?")
print("lcm(a,b) >= 2b (by PDL). Need lcm(a,b) <= M. Since b <= M/2: 2b <= M. But lcm could be > 2b.")
print("Counterexample needed: lcm(a,b) > M with a,b <= M/2.")

# Check: for A with small M, is there a pair {a,b} <= M/2 with lcm > M?
violations = 0
for a1 in range(2, 10):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:12]
    for tk in range(4, 9):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A_test = [a1] + list(sub)
            if not is_primitive(A_test): continue
            M = max(A_test)
            half = [a for a in A_test if a <= M/2]
            for pair in combinations(half, 2):
                l = lcm2(pair[0], pair[1])
                if l > M:
                    violations += 1
                    if violations <= 5:
                        print(f"  PAIR VIOLATION: A={A_test}, pair={pair}, lcm={l}, M={M}")

print(f"  Pair violations (lcm > M for pair in A ∩ [1,M/2]): {violations}")

# So ALL pairs in A ∩ [1, M/2] have lcm <= M? Or do some exceed?

# For triples: how often does a triple in A ∩ [1, M/2] have lcm > M?
print("\nTriple analysis: triples in A ∩ [1, M/2] with lcm > M?")
triple_ok = 0
triple_fail = 0
for a1 in range(2, 8):
    pool = [x for x in range(a1+1, 30) if x % a1 != 0][:10]
    for tk in range(5, 9):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A_test = [a1] + list(sub)
            if not is_primitive(A_test): continue
            M = max(A_test)
            half = [a for a in A_test if a <= M/2]
            for trip in combinations(half, 3):
                l = lcm2(lcm2(trip[0], trip[1]), trip[2])
                if l > M:
                    triple_fail += 1
                    if triple_fail <= 5:
                        print(f"  TRIPLE > M: A={A_test}, triple={trip}, lcm={l}, M={M}")
                else:
                    triple_ok += 1

print(f"  Triples with lcm <= M: {triple_ok}")
print(f"  Triples with lcm > M: {triple_fail}")
print(f"  Fraction exceeding M: {triple_fail/(triple_ok+triple_fail):.4f}" if triple_ok+triple_fail > 0 else "")

# ============================================
# THE PROOF STRUCTURE
# ============================================
print("\n" + "=" * 70)
print("PROOF STRUCTURE")
print("=" * 70)

# Let h = |A ∩ [1, M/2]| = number of elements <= M/2.
# Singletons: k (all elements qualify)
# Pairs: need both elements <= M/2. At most C(h, 2) pairs.
#   But do ALL such pairs have lcm <= M? Check above.
# Triples+: need all elements <= M/2 AND lcm <= M.
#   Triples can have lcm > M even with all elements <= M/2.

# Count: N(A) = k + #{pairs in half with lcm<=M} + #{triples in half with lcm<=M} + ...

# The claim N(A) <= k(k+1)/2 = k + k(k-1)/2.
# If pairs contribute <= k(k-1)/2 and triples+ contribute 0: done.
# pairs in half: C(h, 2) = h(h-1)/2.
# Need h(h-1)/2 <= k(k-1)/2, i.e., h <= k. ALWAYS TRUE (h <= k).
# BUT: triples can contribute > 0.

# So: N(A) = k + (pairs with lcm<=M) + (triples+ with lcm<=M)
# <= k + C(h,2) + (triples+)
# <= k + k(k-1)/2 + (triples+)

# For N(A) <= k(k+1)/2 = k + k(k-1)/2: need triples+ contribution = 0?!
# But we saw triples CAN have lcm <= M. Example: {6,10,15,35}, lcm(6,10,15)=30<=35.

# So the bound k(k+1)/2 must account for triples by trading off with pairs.
# Key: not ALL C(h,2) pairs have lcm <= M. Some pairs have lcm > M.
# The pairs that exceed M free up room for the triples that sneak in.

# Quantify: how many pairs in half can have lcm > M?
print("\nHow many pairs {a,b} with a,b <= M/2 have lcm > M?")
# lcm(a,b) > M with a,b <= M/2. lcm = ab/gcd. Need ab/gcd > M.
# Since a,b <= M/2: ab <= M^2/4. gcd >= 1. So lcm <= M^2/4.
# lcm > M iff ab/gcd > M iff ab > M*gcd.
# With a <= M/2 and b <= M/2: ab <= M^2/4. Need M*gcd < M^2/4, i.e., gcd < M/4.
# For coprime pairs (gcd=1): lcm = ab. Need ab > M, i.e., a*b > M.
# With a >= 2 and b >= 3 (say): ab >= 6. M could be small.
# For A = {2,3,5,7}: M=7, M/2=3.5. Elements <= 3.5: {2,3}. Only 1 pair: {2,3}, lcm=6<=7. OK.
# For A = {3,5,7,11}: M=11. Half: {3,5}. Pair {3,5}: lcm=15>11. EXCEEDS!

print("Example: A={3,5,7,11}, M=11, half={3,5}, pair {3,5}: lcm=15>11 ✓ (exceeds)")
print("Example: A={2,3,5,7}, M=7, half={2,3}, pair {2,3}: lcm=6<=7 (ok)")
print("Example: A={6,10,15,35}, M=35, half={6,10,15}")
print("  Pairs: {6,10}:30<=35✓, {6,15}:30<=35✓, {10,15}:30<=35✓ = 3 pairs")
print("  Triple: {6,10,15}:30<=35✓ = 1 triple")
print("  Total: 4 singletons + 3 pairs + 1 triple = 8. Bound: 4*5/2 = 10. OK.")

# So the pair count can be LESS than C(h,2) when coprime pairs in the half exceed M.
# And the triple count is bounded by... what?

# Let's count more carefully for the worst cases found earlier.
print("\nWorst cases from systematic search (count closest to k(k+1)/2):")

worst_cases = []
for a1 in range(2, 10):
    pool = [x for x in range(a1+1, 30) if x % a1 != 0][:12]
    for tk in range(4, 9):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A_test = [a1] + list(sub)
            if not is_primitive(A_test): continue
            M = max(A_test)
            k = len(A_test)
            counts, _ = count_by_size(A_test)
            total = sum(counts.values())
            bound = k*(k+1)//2
            gap = bound - total
            worst_cases.append((gap, total, bound, tuple(A_test), dict(counts)))

worst_cases.sort()
print(f"  {'gap':>4} {'total':>6} {'bound':>6} {'set':>30} | breakdown")
for gap, total, bound, A, counts in worst_cases[:15]:
    bd = " + ".join(f"{counts.get(s,0)}@|S|={s}" for s in range(1, max(counts)+1) if counts.get(s,0)>0)
    Astr = str(list(A)) if len(str(list(A))) < 28 else str(list(A[:4]))[:-1] + f',...,{A[-1]}]'
    print(f"  {gap:>4} {total:>6} {bound:>6} {Astr:>30} | {bd}")

print("\nDONE.")
