"""Find ALL primitive sets where a triple has lcm <= max(A). Extend search."""
from math import gcd
from itertools import combinations

def lcm2(a,b): return a*b//gcd(a,b)
def is_primitive(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j]%A[i]==0: return False
    return True

# Search for triples {a,b,c} in primitive A with lcm(a,b,c) <= max(A)
print("SEARCH: primitive sets with a triple having lcm <= max(A)")
print("=" * 60)

triple_examples = []
for a1 in range(2, 30):
    pool = [x for x in range(a1+1, 100) if x%a1!=0][:20]
    for tk in range(4, 8):
        if len(pool)<tk-1: continue
        for sub in combinations(pool, tk-1):
            A = [a1]+list(sub)
            if not is_primitive(A): continue
            M = max(A)
            half = [a for a in A if a<=M//2]
            if len(half)<3: continue
            for trip in combinations(half, 3):
                l = lcm2(lcm2(trip[0],trip[1]),trip[2])
                if l<=M:
                    triple_examples.append((tuple(A),trip,l,M))

print(f"Found {len(triple_examples)} triples with lcm <= max(A)")
# Deduplicate by triple
seen = set()
unique = []
for A,trip,l,M in triple_examples:
    if trip not in seen:
        seen.add(trip)
        unique.append((A,trip,l,M))
        if len(unique)<=20:
            print(f"  A={list(A)[:6]}{'...' if len(A)>6 else ''}, triple={trip}, lcm={l}, M={M}")

print(f"\nUnique triples: {len(unique)}")

# For each such triple, what's the gcd structure?
print("\nGCD structure of triples with lcm <= M:")
for A,trip,l,M in unique[:15]:
    a,b,c = trip
    g12=gcd(a,b); g13=gcd(a,c); g23=gcd(b,c)
    print(f"  {trip}: lcm={l}, gcds=({g12},{g13},{g23}), product={a*b*c}, lcm/max={l/c:.1f}")

# THE PROOF: count N(A) = k + P where P = pairs with lcm <= M
# Since triples are extremely rare (only when elements share many factors AND max(A) is large),
# the bound N(A) <= k + C(h,2) where h = |A cap [1, M/2]| should suffice.
# And h <= k-1, so C(h,2) <= (k-1)(k-2)/2 < k(k-1)/2.
# Total: k + (k-1)(k-2)/2 = k + k^2/2 - 3k/2 + 1 = k^2/2 - k/2 + 1 < k(k+1)/2 for k >= 2.

# Wait: k + (k-1)(k-2)/2 vs k(k+1)/2 = k + k(k-1)/2.
# Difference: k(k-1)/2 - (k-1)(k-2)/2 = (k-1)(k - (k-2))/2 = (k-1)*2/2 = k-1.
# So k + (k-1)(k-2)/2 = k(k+1)/2 - (k-1).
# This gives: singletons + all possible pairs in half = k(k+1)/2 - (k-1) <= k(k+1)/2. QED if no triples!

# But triples DO exist. Need to account for them.
# For the sets WITH triples: count total = k + P + T.
# Claim: when T > 0, some pairs are "knocked out" (lcm > M), freeing room.

# Check: for sets with triples, is the PAIR count reduced?
print("\nSets WITH triples: pair analysis")
for A,trip,l,M in unique[:10]:
    A = list(A)
    k = len(A)
    half = [a for a in A if a<=M//2]
    h = len(half)
    # Count pairs with lcm <= M
    pairs_ok = 0
    pairs_total = 0
    for p in combinations(half, 2):
        pairs_total += 1
        if lcm2(p[0],p[1]) <= M:
            pairs_ok += 1
    # Count triples with lcm <= M
    triples_ok = 0
    for t in combinations(half, 3):
        if lcm2(lcm2(t[0],t[1]),t[2]) <= M:
            triples_ok += 1
    total = k + pairs_ok + triples_ok
    bound = k*(k+1)//2
    print(f"  A={A[:5]}{'...' if k>5 else ''}: k={k}, h={h}, C(h,2)={h*(h-1)//2}, "
          f"pairs_ok={pairs_ok}, triples={triples_ok}, total={total}, bound={bound}, "
          f"gap={bound-total}")

# THE CLEAN PROOF
print("\n" + "=" * 60)
print("THE PROOF")
print("=" * 60)
print("""
THEOREM. For any primitive set A with |A| = k:
  N(A) := #{S subset A : lcm(S) <= max(A)} <= k + (k-1)(k-2)/2 + k-1 = k(k+1)/2.

PROOF.
Let M = max(A), h = |{a in A : a <= M/2}|. Note h <= k-1 (since a_k = M > M/2).

SINGLETONS: All k singletons have lcm = a_i <= M. Contribution: k.

SIZE >= 2 SUBSETS: By the Subset LCM Bound (lcm(S) >= 2*max(S) for |S|>=2),
any S with lcm(S) <= M must have max(S) <= M/2. So all elements of S are in
A_half := {a in A : a <= M/2}, which has h <= k-1 elements.

PAIRS: At most C(h,2) = h(h-1)/2 <= (k-1)(k-2)/2 pairs.

SIZE >= 3: For any such S with |S| >= 3 and lcm(S) <= M:
  All elements in A_half. lcm(S) >= 2*max(S) >= 2*third-largest.
  Moreover, by iterated Subset LCM Bound:
  lcm(S) >= lcm(any pair in S) >= 2*(second element of that pair).

  For each triple {a < b < c} in A_half with lcm <= M:
  lcm(a,b) >= 2b and lcm(a,b,c) >= lcm(a,b) >= 2b.
  But also lcm(a,b,c) is a multiple of c, so lcm >= c.
  And lcm(a,b,c) >= 2c IF c does not divide lcm(a,b) (by Subset LCM Bound applied
  to {lcm(a,b), c}). If c DOES divide lcm(a,b): then c | lcm(a,b), so
  lcm(a,b,c) = lcm(a,b) >= 2b.
  Need lcm(a,b,c) <= M and all of a,b,c <= M/2.

  For each fixed c: the number of pairs {a,b} with a < b < c and lcm(a,b,c) <= M
  is bounded by #{pairs in A_half below c}.

TOTAL BOUND (clean version):
  N(A) = k + #{size>=2 subsets of A_half with lcm <= M}
       <= k + #{all subsets of A_half of size >= 1} - h  [subtract singletons already counted]

  Wait, let me just bound: the number of subsets of A_half of ANY size with lcm <= M.
  There are 2^h - 1 non-empty subsets of A_half. We need to show at most
  k(k-1)/2 of them have lcm <= M.

  Each such subset S has lcm(S) | L where L = lcm(A_half). So the lcm of S is
  a divisor of L that is <= M.
  Number of divisors of L that are <= M: at most tau(L) (total divisors).
  And each divisor d can come from at most ONE maximal subset (all elements dividing d).
  So #{subsets with lcm <= M} <= #{divisors of L that are <= M} * 2^{longest chain}.

  This is getting complicated. Let me just prove the O(k^2) bound directly.
""")

# Direct O(k^2) bound:
print("CLEAN O(k^2) BOUND:")
print("  N(A) <= k + 2^h - 1  where h = |A_half| <= k-1.")
print("  For the strong bound: N(A) <= k + (k-1)k/2 = k(k+1)/2.")
print("  Equivalently: subsets of A_half of size >= 2 with lcm <= M: at most k(k-1)/2 - (k-1).")
print("")
print("  Pairs: C(h,2) <= (k-1)(k-2)/2.")
print("  Triples+: empirically 0 for max <= 40 (49K sets).")
print("  Triples can exist for larger max (e.g., {6,10,15,35}).")
print("")
print("  Even including ALL subsets of A_half (size >= 2):")
print("  2^h - 1 - h = 2^{k-1} - k (exponential, not polynomial).")
print("  This is too loose.")
print("")
print("  Better: for each d | L with d <= M, there is exactly one maximal subset")
print("  S_d = {a in A_half : a | d}. Every subset with lcm = d is a subset of S_d.")
print("  Number of subsets with lcm = d: 2^{|S_d|} - sum over proper divisors.")
print("  Total: sum over d <= M of (number of subsets with lcm = d).")
print("  Each S_d has |S_d| <= h. The number of d values <= M: at most M.")
print("")
print("  KEY INSIGHT: |S_d| = |{a in A : a | d}| is small for primitive A!")
print("  Since A is primitive (no a_i | a_j): the set {a in A : a | d} is an")
print("  antichain in [1,d] under divisibility. By Dilworth: max antichain in")
print("  divisors of d has size at most the width of the divisor lattice.")
print("  For d = p1^e1 * ... * pm^em: max antichain = C(e1+...+em, floor((e1+...+em)/2)).")
print("  For d <= M = max(A): d has at most log2(M) prime factors.")
print("  So |S_d| <= C(log2(M), log2(M)/2) ~ 2^{log2(M)} / sqrt(log2(M)).")
print("  This is polynomial in M but not directly in k.")

print("\nDONE.")
