"""
Compute discrepancy C(X) = max_{x<=X} |F(x) - delta*x| for sets of primes.
Q = odd primes <= 73 (20 primes)
Q_all = all primes <= 73 (21 primes)
"""
import time, sys

def sieve_F_primes(X, primes):
    """Sieve of Eratosthenes style: mark multiples of each prime."""
    hit = bytearray(X + 1)
    for p in primes:
        for m in range(p, X + 1, p):
            hit[m] = 1
    return hit

def compute_delta_product(primes):
    """Exact density for coprime set via product formula."""
    prod = 1.0
    for p in primes:
        prod *= (1.0 - 1.0/p)
    return 1.0 - prod

def compute_C_local(X, primes, delta):
    """Compute max |F(x) - delta*x| for x = 1..X."""
    hit = sieve_F_primes(X, primes)
    running = 0
    max_C = 0.0
    max_C_x = 0
    # Also track C at specific milestones
    milestones = {}
    targets = [100, 1000, 10000, 100000, 1000000, 10000000]
    for x in range(1, X + 1):
        running += hit[x]
        d = abs(running - delta * x)
        if d > max_C:
            max_C = d
            max_C_x = x
        if x in targets:
            milestones[x] = (max_C, max_C_x)
    return milestones, max_C, max_C_x

# Define prime sets
all_primes_73 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
odd_primes_73 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]

X_max = 10_000_000

# ============================================
# Q = odd primes <= 73 (20 primes)
# ============================================
print("=" * 70)
print(f"Q = odd primes <= 73: {odd_primes_73}")
print(f"|Q| = {len(odd_primes_73)}")
print("=" * 70)

delta_Q = compute_delta_product(odd_primes_73)
S1_Q = sum(1.0/p for p in odd_primes_73)
print(f"delta(Q) = 1 - prod(1-1/p) = {delta_Q:.12f}")
print(f"S1(Q) = {S1_Q:.6f}")
print(f"2*delta/S1 = {2*delta_Q/S1_Q:.6f}")
print(f"prod(1-1/p) = {1-delta_Q:.12f}")
sys.stdout.flush()

print(f"\nComputing C_local(X) for X up to {X_max:,}...")
t0 = time.time()
milestones_Q, final_C_Q, final_x_Q = compute_C_local(X_max, odd_primes_73, delta_Q)
elapsed = time.time() - t0
print(f"Done in {elapsed:.1f}s\n")

print(f"{'X':>12s} | {'C_local(X)':>12s} | {'at x':>10s} | {'C/sqrt(X)':>10s} | {'C/ln(X)':>10s} | {'C/X^0.33':>10s}")
print("-" * 78)
import math
for X in [100, 1000, 10000, 100000, 1000000, 10000000]:
    if X in milestones_Q:
        C, cx = milestones_Q[X]
        print(f"{X:>12,d} | {C:>12.4f} | {cx:>10,d} | {C/math.sqrt(X):>10.4f} | "
              f"{C/math.log(X):>10.4f} | {C/X**0.33:>10.4f}")
sys.stdout.flush()

# ============================================
# Q_all = all primes <= 73 (21 primes, includes 2)
# ============================================
print("\n" + "=" * 70)
print(f"Q_all = all primes <= 73: {all_primes_73}")
print(f"|Q_all| = {len(all_primes_73)}")
print("=" * 70)

delta_all = compute_delta_product(all_primes_73)
S1_all = sum(1.0/p for p in all_primes_73)
print(f"delta(Q_all) = {delta_all:.12f}")
print(f"S1(Q_all) = {S1_all:.6f}")
print(f"2*delta/S1 = {2*delta_all/S1_all:.6f}")
sys.stdout.flush()

print(f"\nComputing C_local(X) for X up to {X_max:,}...")
t0 = time.time()
milestones_all, final_C_all, final_x_all = compute_C_local(X_max, all_primes_73, delta_all)
elapsed = time.time() - t0
print(f"Done in {elapsed:.1f}s\n")

print(f"{'X':>12s} | {'C_local(X)':>12s} | {'at x':>10s} | {'C/sqrt(X)':>10s} | {'C/ln(X)':>10s} | {'C/X^0.33':>10s}")
print("-" * 78)
for X in [100, 1000, 10000, 100000, 1000000, 10000000]:
    if X in milestones_all:
        C, cx = milestones_all[X]
        print(f"{X:>12,d} | {C:>12.4f} | {cx:>10,d} | {C/math.sqrt(X):>10.4f} | "
              f"{C/math.log(X):>10.4f} | {C/X**0.33:>10.4f}")
sys.stdout.flush()

# ============================================
# GROWTH ANALYSIS
# ============================================
print("\n" + "=" * 70)
print("GROWTH ANALYSIS")
print("=" * 70)

print("\nFor Q (20 odd primes):")
vals_Q = [(X, milestones_Q[X][0]) for X in [100,1000,10000,100000,1000000,10000000] if X in milestones_Q]
for i in range(1, len(vals_Q)):
    X1, C1 = vals_Q[i-1]
    X2, C2 = vals_Q[i]
    if C1 > 0 and C2 > 0:
        log_ratio = math.log(C2/C1) / math.log(X2/X1)
        print(f"  X: {X1:>10,d} -> {X2:>10,d}, C: {C1:.2f} -> {C2:.2f}, "
              f"growth exponent: {log_ratio:.4f}")

print("\nFor Q_all (21 primes including 2):")
vals_all = [(X, milestones_all[X][0]) for X in [100,1000,10000,100000,1000000,10000000] if X in milestones_all]
for i in range(1, len(vals_all)):
    X1, C1 = vals_all[i-1]
    X2, C2 = vals_all[i]
    if C1 > 0 and C2 > 0:
        log_ratio = math.log(C2/C1) / math.log(X2/X1)
        print(f"  X: {X1:>10,d} -> {X2:>10,d}, C: {C1:.2f} -> {C2:.2f}, "
              f"growth exponent: {log_ratio:.4f}")

# Compare to 2^{k/2}
print(f"\n2^(k/2) for k=20: {2**10} = 1024")
print(f"2^(k/2) for k=21: {2**10 * math.sqrt(2):.0f} ~ 1448")
print(f"2^(k-1) for k=20: {2**19} = 524288")
print(f"2^(k-1) for k=21: {2**20} = 1048576")

# Also compute: what is C at x = max(Q)?
print(f"\nC at x = max(Q) = 73:")
hit_Q = sieve_F_primes(73, odd_primes_73)
F73 = sum(hit_Q[1:74])
C73 = abs(F73 - delta_Q * 73)
print(f"  F_Q(73) = {F73}, delta*73 = {delta_Q*73:.4f}, |F-delta*73| = {C73:.4f}")

hit_all = sieve_F_primes(73, all_primes_73)
F73_all = sum(hit_all[1:74])
C73_all = abs(F73_all - delta_all * 73)
print(f"  F_all(73) = {F73_all}, delta*73 = {delta_all*73:.4f}, |F-delta*73| = {C73_all:.4f}")

# And at x = 146 (max of A = {2p})
print(f"\nC at x = 146 (max of A = {{2p}}):")
hit146 = sieve_F_primes(146, odd_primes_73)
F146 = sum(hit146[1:147])
C146 = abs(F146 - delta_Q * 146)
print(f"  F_Q(146) = {F146}, delta*146 = {delta_Q*146:.4f}, |F-delta*146| = {C146:.4f}")

print("\nDONE.")
