# Problem 686 — SIMPLE k=3 computation
# Paste this into CoCalc SageMath worksheet
# This version uses the most reliable SageMath methods

results = {}

for N in [4, 9, 16, 25, 49, 64, 81]:
    print(f"\n{'='*40}")
    print(f"N = {N}")
    print(f"{'='*40}")
    
    # The curve: X³ - X = N(Y³ - Y)
    # Homogeneous form: X³ - N*Y³ - X*Z² + N*Y*Z² = 0
    
    R.<X,Y,Z> = QQ[]
    cubic = X^3 - N*Y^3 - X*Z^2 + N*Y*Z^2
    
    # The point (1:1:1) is on the curve: 1-N-1+N=0 ✓
    P = [1, 1, 1]
    
    try:
        E, phi = EllipticCurve_from_cubic(cubic, P, morphism=True)
        print(f"  Weierstrass: {E.ainvs()}")
        print(f"  Conductor: {E.conductor()}")
        
        try:
            label = E.cremona_label()
            print(f"  Cremona label: {label}")
        except:
            print(f"  Cremona label: not in database")
        
        r = E.rank()
        print(f"  Rank: {r}")
        
        T = E.torsion_subgroup()
        print(f"  Torsion: {T.invariants()}")
        
        pts = E.integral_points()
        print(f"  Integral points: {pts}")
        
        # Map integral points back to original curve
        phi_inv = phi.inverse()
        print(f"  Mapping back to X³-X = N(Y³-Y):")
        for pt in pts:
            try:
                orig = phi_inv(pt)
                Xv = QQ(orig[0]/orig[2])
                Yv = QQ(orig[1]/orig[2])
                # Check admissibility: need X≥Y+3, Y≥3
                # (X=m+2, Y=n+2, so m≥n+3 means X≥Y+3, n≥1 means Y≥3)
                admissible = (Xv >= Yv + 3) and (Yv >= 3) and (Xv in ZZ) and (Yv in ZZ)
                m = int(Xv) - 2
                n = int(Yv) - 2
                print(f"    ({Xv}, {Yv}) → m={m}, n={n}", end="")
                if admissible:
                    print(f" *** ADMISSIBLE ***")
                    # Verify
                    lhs = (m+1)*(m+2)*(m+3)
                    rhs = N*(n+1)*(n+2)*(n+3)
                    print(f"    Verify: {lhs} = {N}*{(n+1)*(n+2)*(n+3)} = {rhs} {'✓' if lhs==rhs else '✗'}")
                else:
                    print(f" (not admissible)")
            except Exception as e:
                print(f"    Inverse map failed for {pt}: {e}")
        
        results[N] = {"rank": r, "integral_points": len(pts)}
        
    except Exception as e:
        print(f"  ERROR: {e}")
        results[N] = {"error": str(e)}

print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
for N in [4, 9, 16, 25, 49, 64, 81]:
    r = results.get(N, {})
    if "error" in r:
        print(f"  N={N:3d}: ERROR - {r['error'][:50]}")
    else:
        rescued = "rescued" if N in [9,16] else "STUCK"
        print(f"  N={N:3d}: rank={r['rank']}, integral_pts={r['integral_points']} [{rescued}]")
