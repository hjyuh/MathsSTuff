# Problem 686 — Map Weierstrass points back to original curve
# Paste into CoCalc SageMath worksheet
#
# Instead of using the morphism, we directly find ALL integer 
# points on X³ - X = N(Y³ - Y) by brute force over a range,
# then check admissibility.

for N in [4, 9, 16, 25, 49, 64, 81]:
    print(f"\n{'='*50}")
    print(f"N = {N} — all integer points on X³-X = N(Y³-Y)")
    print(f"{'='*50}")
    
    solutions = []
    admissible = []
    
    # Search Y from -50 to 500, solve for X
    for Y in range(-50, 501):
        rhs = N * (Y^3 - Y)
        # Need X³ - X = rhs, i.e. X³ - X - rhs = 0
        R.<x> = QQ[]
        poly = x^3 - x - rhs
        rts = poly.roots(ZZ)
        for (Xv, mult) in rts:
            solutions.append((ZZ(Xv), ZZ(Y)))
            # Admissibility: X = m+2, Y = n+2
            # Need m ≥ 0, n ≥ 0, m ≥ n+3
            # So X ≥ 2, Y ≥ 2, X ≥ Y+3
            m = ZZ(Xv) - 2
            n = ZZ(Y) - 2
            if m >= 0 and n >= 0 and m >= n + 3:
                admissible.append((ZZ(Xv), ZZ(Y), m, n))
    
    # Print all solutions (limit to reasonable display)
    print(f"  Total integer points found (Y in [-50,500]): {len(solutions)}")
    
    # Show small solutions
    small = [(X,Y) for (X,Y) in solutions if abs(X) <= 100 and abs(Y) <= 100]
    print(f"  Small solutions (|X|,|Y| ≤ 100):")
    for (X,Y) in sorted(small):
        tag = ""
        m, n = X-2, Y-2
        if m >= 0 and n >= 0 and m >= n+3:
            tag = " *** ADMISSIBLE: m={}, n={} ***".format(m, n)
        print(f"    (X={X}, Y={Y}){tag}")
    
    if admissible:
        print(f"\n  *** ADMISSIBLE SOLUTIONS FOUND: ***")
        for (X, Y, m, n) in admissible:
            lhs = (m+1)*(m+2)*(m+3)
            rhs_val = N*(n+1)*(n+2)*(n+3)
            print(f"    m={m}, n={n}: {lhs} = {N}*{(n+1)*(n+2)*(n+3)} = {rhs_val} {'✓' if lhs==rhs_val else '✗'}")
    else:
        print(f"\n  No admissible solutions in search range.")
        print(f"  (But the elliptic curve has rank ≥ 1, so there may be")
        print(f"   integer points with Y > 500 that we haven't checked.)")

print(f"\n{'='*50}")
print("KEY INSIGHT")
print(f"{'='*50}")
print("""
All 7 curves have positive Mordell-Weil rank (1-3).
All have many integral points (9-25).
For N=9,16: some integral points ARE admissible → rescued.
For N=4,25,49,64,81: need to check if ANY integral point 
(possibly with very large coordinates) is admissible.

The obstruction is NOT "the curve has no points."
The obstruction is "no point satisfies m ≥ n+3, both ≥ 0."
This is an ADMISSIBILITY constraint, not a genus/rank constraint.
""")
