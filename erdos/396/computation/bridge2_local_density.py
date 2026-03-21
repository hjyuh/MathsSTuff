"""
Bridge 2 computation: Single-prime local carry-good density.

For each prime p and depth a, compute:
  G_{p,a} = { r in {0,...,p^a - 1} : for all 0 <= j <= n,
              if p | (r-j) then nu_p(r-j) <= kappa_p(r) }

where kappa_p(r) = number of carries when computing r+r in base p.

We want to see if |G_{p,a}| / p^a stabilizes as a grows.
"""

def base_p_digits(n, p, length):
    """Return base-p digits of n, padded to given length (LSB first)."""
    digits = []
    for _ in range(length):
        digits.append(n % p)
        n //= p
    return digits

def carry_count(r, p, a):
    """Number of carries when computing r + r in base p, using a digits."""
    digits = base_p_digits(r, p, a)
    carries = 0
    c = 0  # incoming carry
    for i in range(a):
        total = 2 * digits[i] + c
        if total >= p:
            carries += 1
            c = 1
        else:
            c = 0
    return carries

def p_adic_valuation(n, p):
    """Compute nu_p(n). Returns 0 if n == 0 is handled separately."""
    if n == 0:
        return float('inf')
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def compute_local_density(p, a, n_shifts):
    """
    Compute |G_{p,a}| / p^a for given prime p, depth a, and n+1 shifts (j=0,...,n_shifts).
    """
    total = p ** a
    good = 0
    
    for r in range(total):
        kappa = carry_count(r, p, a)
        is_good = True
        
        for j in range(n_shifts + 1):
            val = r - j
            if val < 0:
                val += total  # shouldn't matter for valuation check, but handle edge
            # Actually we need nu_p(r - j) where r-j is an actual integer
            # For r >= j: val = r - j
            # For r < j: in the actual problem K > X >> n, so K-j > 0 always.
            # For our local computation mod p^a, we use r - j (could be negative for small r)
            # In the real setting K >> n so K-j > 0. For local computation, 
            # we should think of r as representing K mod p^a where K is large.
            # So r - j mod p^a represents K - j mod p^a.
            # The valuation nu_p(K-j) is determined by (K-j) mod p^a as long as nu_p(K-j) < a.
            
            actual_val = r - j
            if actual_val < 0:
                actual_val += total  # wrap around mod p^a
            
            if actual_val % p == 0:  # p divides (r - j) mod p^a
                if actual_val == 0:
                    # nu_p = a (or more), which is >= a
                    # In reality K-j != 0 for large K, but mod p^a this means
                    # nu_p(K-j) >= a. We need nu_p(K-j) <= kappa.
                    # Since kappa < a always, this would FAIL.
                    # But this only happens when r ≡ j (mod p^a), i.e., 
                    # K ≡ j (mod p^a). For K in (X, 2X] this is ≤ 1 value.
                    # So we should mark this as BAD (conservative).
                    nu = a  # effectively infinite relative to kappa
                else:
                    nu = p_adic_valuation(actual_val, p)
                
                if nu > kappa:
                    is_good = False
                    break
        
        if is_good:
            good += 1
    
    return good, total, good / total

def main():
    primes = [2, 3, 5, 7, 11, 13]
    n_values = [1, 2, 3]  # test for n=1, 2, 3
    
    for n in n_values:
        print(f"\n{'='*70}")
        print(f"n = {n} (shifts j = 0, 1, ..., {n})")
        print(f"{'='*70}")
        
        for p in primes:
            print(f"\n  Prime p = {p}:")
            print(f"  {'a':>4} | {'|G_{p,a}|':>12} | {'p^a':>12} | {'density':>12} | {'ratio to prev':>14}")
            print(f"  {'-'*4}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*14}")
            
            prev_density = None
            max_a = min(12, 8 if p >= 7 else 10 if p >= 5 else 14)  # limit for large p
            
            # For p=2 we can go deeper, for large p we need to stop earlier
            if p >= 11:
                max_a = 6
            elif p >= 7:
                max_a = 7
            elif p >= 5:
                max_a = 8
            elif p >= 3:
                max_a = 10
            else:  # p = 2
                max_a = 16
            
            for a in range(1, max_a + 1):
                if p ** a > 5_000_000:  # safety limit
                    print(f"  {a:>4} | {'(too large)':>12}")
                    break
                    
                good, total, density = compute_local_density(p, a, n)
                
                ratio_str = ""
                if prev_density is not None and prev_density > 0:
                    ratio = density / prev_density
                    ratio_str = f"{ratio:.6f}"
                
                print(f"  {a:>4} | {good:>12} | {total:>12} | {density:>12.8f} | {ratio_str:>14}")
                prev_density = density

if __name__ == "__main__":
    main()
