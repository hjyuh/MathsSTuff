"""Clean proof-oriented analysis of small-lcm subset count."""
from math import gcd, log2
from itertools import combinations

def lcm2(a, b):
    return a * b // gcd(a, b)

def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] % A[i] == 0:
                return False
    return True

def count_small_lcm(A):
    M = max(A)
    k = len(A)
    by_size = [0] * (k+1)
    for size in range(1, k+1):
        for combo in combinations(A, size):
            l = combo[0]
            for c in combo[1:]:
                l = lcm2(l, c)
            if l <= M:
                by_size[size] += 1
    return by_size

# PART 1: Tight cases analysis
print("TIGHT CASES: sets where count is closest to k(k+1)/2")
print("=" * 70)

worst_cases = []
for a1 in range(2, 12):
    pool = [x for x in range(a1+1, 40) if x % a1 != 0][:14]
    for tk in range(4, 10):
        if len(pool) < tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1] + list(sub)
            if not is_primitive(A): continue
            M = max(A)
            k = len(A)
            by_size = count_small_lcm(A)
            total = sum(by_size)
            bound = k*(k+1)//2
            gap = bound - total
            h = sum(1 for a in A if a <= M/2)
            worst_cases.append((gap, total, bound, tuple(A), by_size[:], h, k))

worst_cases.sort()
print(f"{'gap':>4} {'total':>5} {'bound':>5} k  h  {'breakdown':>30} {'set'}")
print("-" * 90)
for gap, total, bound, A, bs, h, k in worst_cases[:20]:
    bd = "+".join(str(bs[s]) for s in range(1, k+1) if bs[s]>0)
    sizes = "+".join(f"{bs[s]}@{s}" for s in range(1, k+1) if bs[s]>0)
    Astr = str(list(A))[:50]
    print(f"{gap:>4} {total:>5} {bound:>5} {k:>2} {h:>2}  {sizes:>30}  {Astr}")

# PART 2: The proof
print("\n" + "=" * 70)
print("PROOF OF N(A) <= k(k+1)/2")
print("=" * 70)

# Key observations from data:
# 1. Singletons: exactly k (all elements <= M)
# 2. Pairs with lcm <= M: at most C(h,2) where h = |A cap [1, M/2]|
#    BUT not all C(h,2) pairs qualify (coprime pairs in half can have lcm > M)
# 3. Triples with lcm <= M: very rare, only when elements share many factors
# 4. |S| >= 4: practically never has lcm <= M

# Let's verify: for |S| >= 3, max |S| with lcm <= M?
print("\nMax subset size with lcm <= max(A) (across all tested sets):")
max_size_seen = 0
max_size_ex = None
for gap, total, bound, A, bs, h, k in worst_cases:
    for s in range(k, 0, -1):
        if bs[s] > 0:
            if s > max_size_seen:
                max_size_seen = s
                max_size_ex = (A, s)
            break
print(f"  Max |S| with lcm <= M: {max_size_seen}")
if max_size_ex:
    print(f"  Example: A={max_size_ex[0]}, size={max_size_ex[1]}")

# Count triples and larger across all sets
total_triples_plus = 0
total_sets = 0
for gap, total, bound, A, bs, h, k in worst_cases:
    total_sets += 1
    total_triples_plus += sum(bs[s] for s in range(3, k+1))
print(f"\n  Total sets analyzed: {total_sets}")
print(f"  Total triples+ with lcm <= M: {total_triples_plus}")
print(f"  Average triples+ per set: {total_triples_plus/total_sets:.4f}")

# PART 3: The key inequality
print("\n" + "=" * 70)
print("THE KEY INEQUALITY: singletons + pairs + triples <= k(k+1)/2")
print("=" * 70)

# N(A) = k + P + T where P = pairs, T = triples+
# Need: k + P + T <= k(k+1)/2 = k + k(k-1)/2
# i.e., P + T <= k(k-1)/2

# P <= C(h,2) = h(h-1)/2 where h = elements <= M/2. And h <= k-1 (since a_k = M > M/2).
# So P <= (k-1)(k-2)/2.

# T: for a triple {a,b,c} <= M/2 with lcm <= M:
# lcm(a,b,c) = lcm(lcm(a,b), c). lcm(a,b) >= 2b (PDL). c <= M/2.
# lcm(lcm(a,b), c) >= 2*max(lcm(a,b), c) >= 2*lcm(a,b) >= 4b (if c divides lcm(a,b))
#                    OR >= 2c (if lcm(a,b) divides c ... impossible since c < lcm(a,b) >= 2b > b >= c? not necessarily)
# Actually c could be > b. Let a < b < c all <= M/2.
# lcm(a,b) >= 2b. If lcm(a,b) >= 2c: lcm(a,b,c) >= lcm(a,b) >= 2c >= 2*M/2 = M... wait = M. Need < M? No, need <= M. So lcm could = M.

# The constraint: lcm(a,b,c) <= M with a < b < c <= M/2.
# Since lcm(a,b) >= 2b >= 2(a+1): lcm(a,b) is at least 2(a+1).
# And lcm(a,b,c) >= lcm(a,b) >= 2b.
# Need lcm(a,b,c) <= M. Since c <= M/2 and lcm >= 2c: lcm(a,b,c) in [2c, M].

# For this to work: c must divide lcm(a,b) or share large gcd with it.
# In practice: very restrictive. The triple must have heavy shared factors.

# Let's count exactly how many triples appear vs pairs for the tightest cases
print("\nTightest cases breakdown:")
for gap, total, bound, A, bs, h, k in worst_cases[:10]:
    P = bs[2] if 2 < len(bs) else 0
    T = sum(bs[s] for s in range(3, k+1))
    max_pairs = h*(h-1)//2 if h >= 2 else 0
    print(f"  A={list(A)[:6]}{'...' if k>6 else ''}: k={k}, h={h}, "
          f"pairs={P}/{max_pairs}, triples+={T}, P+T={P+T}, k(k-1)/2={k*(k-1)//2}")

# PART 4: Prove the weaker O(k^2) bound
print("\n" + "=" * 70)
print("PROOF OF N(A) <= k^2 (weaker but clean)")
print("=" * 70)

# Singletons: k
# Subsets of size >= 2 with lcm <= M: all elements must be <= M/2 (Subset LCM Bound).
# Let h = |A cap [1, M/2]|. Then h <= k-1.
# Total subsets of {elements <= M/2}: 2^h - 1 <= 2^{k-1} - 1.
# But by the PAIR bound: C(h,2) <= C(k-1, 2) = (k-1)(k-2)/2 < k^2/2 pairs.
# And triples+: much fewer.

# Actually, a clean bound:
# Subsets of size >= 2 with lcm <= M: they live in A cap [1, M/2], size h.
# For these h elements, EACH pair has lcm >= 2*max >= 2*(min+1) > 2*min.
# The number of such subsets is at most 2^h - 1 - h (subsets of size >= 2) + h (singletons re-added... no)

# Cleaner: total subsets with lcm <= M = (singletons = k) + (size>=2 subsets in half with lcm<=M)
# Size >= 2 subsets: at most 2^h - 1 - h (non-singleton subsets of half).
# But 2^h can be large. Need to use lcm constraint.

# For SIZE >= 2 subsets of h elements (all <= M/2):
# Each has lcm >= 2*max(S) >= 2*(second smallest + 1) (roughly).
# The number of DIVISORS of any integer <= M is at most M^epsilon for any epsilon.
# Since lcm(S) <= M: the lcm lives in [1, M]. The number of possible lcm values <= M.
# Each lcm value d can come from at most one "maximal" subset (the set of all a_i dividing d).
# So the number of subsets with lcm <= M is at most #{d <= M : d = lcm of some subset}.
# And #{d <= M : d is an lcm} <= M (trivially).

# But M can be much larger than k^2. So this doesn't give k^2.

# Better: use the STRUCTURE.
# Each subset S with lcm(S) <= M and |S| >= 2 has all elements <= M/2.
# These h elements have the property: every pair has lcm >= 2*second.
# For the pair {a_i, a_j} with a_i < a_j: lcm >= 2*a_j.
# So lcm(a_i, a_j) takes values in {2a_j, 3a_j, ..., M} (multiples of a_j... no, lcm is a_j * a_i/gcd).

# Key insight: for a fixed element a_j, how many elements a_i < a_j can pair with it
# to give lcm <= M? lcm(a_i, a_j) = a_i*a_j/gcd(a_i,a_j). Need <= M.
# a_i*a_j/gcd <= M => a_i/gcd <= M/a_j.
# Since gcd | a_i: a_i/gcd is an integer. And a_i/gcd <= M/a_j.
# Number of possible a_i: at most (number of multiples of gcd up to M*gcd/a_j) ... complicated.

# Simpler: a_i <= M*gcd/a_j = M*gcd(a_i,a_j)/a_j. Since gcd | a_j and gcd < a_j (primitive):
# gcd <= a_j/2 (PDL). So a_i <= M/(2) (already known).

# For each a_j <= M/2: the number of a_i < a_j with lcm(a_i,a_j) <= M:
# lcm = a_i*a_j/gcd <= M => a_i <= M*gcd/a_j.
# Since a_i < a_j and a_i >= min(A):
# count <= min(a_j - min(A), M*max_gcd/a_j).

# This is bounded by a_j (trivially). Summing over j: sum_{j} a_j <= h*M/2.
# Not useful.

# Let me just go with: N(A) = k + (pairs) + (triples+) <= k + C(h,2) + C(h,3)
# = k + h(h-1)/2 + h(h-1)(h-2)/6
# <= k + (k-1)(k-2)/2 + (k-1)(k-2)(k-3)/6
# = O(k^3)

# But actually triples+ with lcm <= M is MUCH less than C(h,3).

# From the data: triples+ is almost always 0. Let me check the max.
max_T = 0
max_T_set = None
for gap, total, bound, A, bs, h, k in worst_cases:
    T = sum(bs[s] for s in range(3, k+1))
    if T > max_T:
        max_T = T
        max_T_set = (A, bs, h, k)

print(f"\nMax triples+ count: {max_T}")
if max_T_set:
    A, bs, h, k = max_T_set
    print(f"  At: A={list(A)}, h={h}, k={k}")
    for s in range(1, k+1):
        if bs[s] > 0:
            print(f"    |S|={s}: {bs[s]}")

# Is max_T bounded by some function of k?
print("\nMax triples+ by k:")
by_k = {}
for gap, total, bound, A, bs, h, k in worst_cases:
    T = sum(bs[s] for s in range(3, k+1))
    if k not in by_k or T > by_k[k]:
        by_k[k] = T
for k in sorted(by_k):
    print(f"  k={k}: max triples+ = {by_k[k]}")

print("\nDONE.")
