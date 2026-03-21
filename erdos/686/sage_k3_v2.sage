# Problem 686 — k=3 computation (FIXED)
# Paste into CoCalc SageMath worksheet, run with Shift+Enter

results = {}

for N in [4, 9, 16, 25, 49, 64, 81]:
    print(f"\n{'='*40}")
    print(f"N = {N}")
    print(f"{'='*40}")
    
    R.<X,Y,Z> = QQ[]
    cubic = X^3 - N*Y^3 - X*Z^2 + N*Y*Z^2
    P = [1, 1, 1]
    
    try:
        # Don't unpack — just grab the return value
        result = EllipticCurve_from_cubic(cubic, P, morphism=True)
        
        # It might be a tuple of 2 or 3 things, or just an object
        if isinstance(result, tuple):
            if len(result) == 2:
                E, phi = result
            elif len(result) == 3:
                E, phi, phi_inv = result
            else:
                print(f"  Got tuple of length {len(result)}")
                E = result[0]
                phi = result[1]
        else:
            E = result
            phi = None
        
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
        print(f"  Number of integral points: {len(pts)}")
        
        results[N] = {"rank": r, "integral_points": len(pts), "pts": pts}
        
    except Exception as e:
        print(f"  ERROR: {e}")
        
        # Fallback: try without morphism
        try:
            print(f"  Trying without morphism...")
            E = EllipticCurve_from_cubic(cubic, P, morphism=False)
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
            
            results[N] = {"rank": r, "integral_points": len(pts), "pts": pts}
            
        except Exception as e2:
            print(f"  FALLBACK ERROR: {e2}")
            results[N] = {"error": str(e2)}

print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
for N in [4, 9, 16, 25, 49, 64, 81]:
    r = results.get(N, {})
    if "error" in r:
        print(f"  N={N:3d}: ERROR")
    else:
        tag = "RESCUED" if N in [9,16] else "STUCK"
        print(f"  N={N:3d}: rank={r['rank']}, integral_pts={r['integral_points']} [{tag}]")
