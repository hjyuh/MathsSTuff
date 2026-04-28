"""
EP-488 Coprimality Probe
========================
Check whether Q_a^{ex} (minimal quotient-tail elements under divisibility)
is pairwise coprime across all primitive pair systems with F(s) >= 5.

If coprime in practice → Tao's EP-783 reduction closes EP-488.
If not → characterize the failures.

Usage: python ep488_coprimality_probe.py
"""

from math import gcd, lcm
from itertools import combinations
from collections import defaultdict

def quotient_tail(a, tail):
    """Compute q_a(t) = lcm(a,t)/a for each t in tail."""
    return [lcm(a, t) // a for t in tail]

def minimal_elements(elements):
    """Return minimal elements under divisibility (antichain)."""
    elements = sorted(set(elements))
    mins = []
    for e in elements:
        if not any(m != e and e % m == 0 for m in mins):
            mins.append(e)
    return mins

def F_value(a, b, tail, n):
    """Count integers in [1,n] divisible by at least one element of {a,b} ∪ tail."""
    ell = lcm(a, b)
    elements = [a, b] + list(tail)
    # Inclusion-exclusion (for small sets)
    from itertools import combinations
    total = 0
    for k in range(1, len(elements) + 1):
        for combo in combinations(elements, k):
            l = combo[0]
            for c in combo[1:]:
                l = lcm(l, c)
            if l > n:
                continue
            total += ((-1) ** (k + 1)) * (n // l)
    return total

def find_first_F5(a, b, tail, max_n=2000):
    """Find smallest n >= max(a,b,max(tail)) where F(n) = 5."""
    s = max(a, b, max(tail)) if tail else max(a, b)
    for n in range(s, max_n):
        if F_value(a, b, tail, n) >= 5:
            return n
    return None

def density(a, b, tail):
    """Compute asymptotic density delta = sum of 1/q for primitive set sieve."""
    ell = lcm(a, b)
    elements = [a, b] + list(tail)
    # Inclusion-exclusion for density
    total = 0.0
    for k in range(1, len(elements) + 1):
        for combo in combinations(elements, k):
            l = combo[0]
            for c in combo[1:]:
                l = lcm(l, c)
            total += ((-1) ** (k + 1)) / l
    return total

def check_coprimality(Q_ex):
    """Check all pairwise gcd's. Return list of non-coprime pairs."""
    failures = []
    for q1, q2 in combinations(Q_ex, 2):
        g = gcd(q1, q2)
        if g > 1:
            failures.append((q1, q2, g))
    return failures

def generate_primitive_pairs(max_ell=200, max_tail_elem=300, max_tail_size=6):
    """
    Generate primitive pairs (a, b, T) where:
    - lcm(a,b) = ell, a < b
    - T consists of elements > max(a,b), each not dividing any other
    - No element of {a,b} ∪ T divides any other
    - F(s) >= 5 for some s
    """
    systems = []
    
    for ell in range(2, max_ell + 1):
        # Find all pairs (a,b) with a < b, lcm(a,b) = ell
        for a in range(2, ell):
            if ell % a != 0:
                continue
            for b in range(a + 1, ell + 1):
                if lcm(a, b) != ell:
                    continue
                
                # a doesn't divide b, b doesn't divide a (primitivity)
                if b % a == 0 or a % b == 0:
                    continue
                
                # Generate small tails
                max_t = min(max_tail_elem, 5 * ell)
                candidates = []
                for t in range(max(a, b) + 1, max_t + 1):
                    # t not divisible by a or b, a and b not divisible by t
                    if t % a == 0 or t % b == 0:
                        continue
                    if a % t == 0 or b % t == 0:
                        continue
                    candidates.append(t)
                
                # Try small subsets of candidates as tails
                for size in range(2, min(max_tail_size + 1, len(candidates) + 1)):
                    for tail_combo in combinations(candidates[:30], size):  # limit search
                        tail = list(tail_combo)
                        
                        # Check primitivity within tail
                        primitive = True
                        for t1, t2 in combinations(tail, 2):
                            if t1 % t2 == 0 or t2 % t1 == 0:
                                primitive = False
                                break
                        if not primitive:
                            continue
                        
                        # Check F(s) >= 5
                        s = find_first_F5(a, b, tail, max_n=500)
                        if s is None:
                            continue
                        
                        systems.append((a, b, tail, s))
                        
                        if len(systems) >= 5000:
                            return systems
    
    return systems

def ratio_peak_y(a, b, tail, s, max_m=2000):
    """Find m > s that maximizes F(m)/m, return y = m // a."""
    best_ratio = 0
    best_m = s + 1
    for m in range(s + 1, max_m):
        f = F_value(a, b, tail, m)
        ratio = f / m
        if ratio > best_ratio:
            best_ratio = ratio
            best_m = m
    return best_m // a, best_m, best_ratio

def main():
    print("=" * 70)
    print("EP-488 COPRIMALITY PROBE")
    print("Checking pairwise coprimality of Q_a^{ex} across primitive systems")
    print("=" * 70)
    print()
    
    print("Generating primitive pair systems with F(s) >= 5...")
    systems = generate_primitive_pairs(max_ell=100, max_tail_elem=150, max_tail_size=4)
    print(f"Generated {len(systems)} systems.")
    print()
    
    coprime_count = 0
    non_coprime_count = 0
    non_coprime_examples = []
    
    stats = defaultdict(int)
    
    for i, (a, b, tail, s) in enumerate(systems):
        ell = lcm(a, b)
        
        # Compute quotient-tail for a
        Q_a = quotient_tail(a, tail)
        Q_a_ex = minimal_elements(Q_a)
        
        if len(Q_a_ex) < 2:
            stats['singleton_or_empty'] += 1
            coprime_count += 1
            continue
        
        # Check coprimality
        failures = check_coprimality(Q_a_ex)
        
        if failures:
            non_coprime_count += 1
            if len(non_coprime_examples) < 20:  # store first 20 examples
                non_coprime_examples.append({
                    'system': (a, b, tail),
                    'ell': ell,
                    's': s,
                    'Q_a_ex': Q_a_ex,
                    'Q_a_raw': Q_a,
                    'failures': failures,
                })
        else:
            coprime_count += 1
        
        stats[f'|Q_a_ex|={len(Q_a_ex)}'] += 1
    
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Total systems checked:     {len(systems)}")
    print(f"Q_a^ex pairwise coprime:   {coprime_count} ({100*coprime_count/max(1,len(systems)):.1f}%)")
    print(f"Q_a^ex NOT coprime:        {non_coprime_count} ({100*non_coprime_count/max(1,len(systems)):.1f}%)")
    print()
    
    print("Size distribution of Q_a^ex:")
    for key in sorted(stats.keys()):
        print(f"  {key}: {stats[key]}")
    print()
    
    if non_coprime_examples:
        print("=" * 70)
        print("NON-COPRIME EXAMPLES (first 20)")
        print("=" * 70)
        for ex in non_coprime_examples:
            a, b, tail = ex['system']
            print(f"\n  System: a={a}, b={b}, T={tail}")
            print(f"  ell={ex['ell']}, s={ex['s']}")
            print(f"  Q_a raw:     {ex['Q_a_raw']}")
            print(f"  Q_a^ex:      {ex['Q_a_ex']}")
            print(f"  Non-coprime pairs:")
            for q1, q2, g in ex['failures']:
                print(f"    gcd({q1}, {q2}) = {g}")
    else:
        print("*** ALL Q_a^ex ARE PAIRWISE COPRIME ***")
        print("*** TAO'S EP-783 REDUCTION APPLIES TO EP-488 ***")
    
    # For non-coprime cases, check if they matter for the refined condition
    if non_coprime_examples:
        print()
        print("=" * 70)
        print("CHECKING IF NON-COPRIME CASES AFFECT THE REFINED CONDITION")
        print("=" * 70)
        for ex in non_coprime_examples[:5]:
            a, b, tail = ex['system']
            s = ex['s']
            y, m_peak, peak_ratio = ratio_peak_y(a, b, tail, s)
            Q_a_ex = ex['Q_a_ex']
            active = [q for q in Q_a_ex if q <= y]
            
            delta = density(a, b, tail)
            alpha = 2 * F_value(a, b, tail, s) / s - delta
            
            tail_sum = sum(1/q for q in Q_a_ex if q > y)
            
            print(f"\n  System: a={a}, b={b}, T={tail}")
            print(f"  s={s}, m_peak={m_peak}, y={y}")
            print(f"  |Q_active| = {len(active)}, active = {active}")
            print(f"  tail_sum = {tail_sum:.6f}")
            print(f"  a*alpha(s) = {a*alpha:.6f}")
            print(f"  Margin = {a*alpha - tail_sum:.6f}")
            print(f"  Non-coprime pairs in Q_a^ex: {ex['failures']}")
            print(f"  Non-coprime pairs ACTIVE (q <= y): ", end="")
            active_failures = [(q1,q2,g) for q1,q2,g in ex['failures'] 
                              if q1 <= y and q2 <= y]
            print(active_failures if active_failures else "NONE")


if __name__ == '__main__':
    main()
