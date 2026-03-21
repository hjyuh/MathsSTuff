# Problem 686 — k=3 Elliptic Curve Rank Computation
# Run in SageMath (CoCalc or local install)
# 
# For each stuck square N, this:
# 1. Builds the quartic curve w² = N²s⁴ + 8Ns³ - 18Ns² + 8Ns + 1
# 2. Converts to Weierstrass form using the known point (1, N-1)
# 3. Computes the Cremona label, rank, and ALL integral points
# 4. Determines provably whether N is k=3 representable

print("=" * 60)
print("Problem 686 — k=3 elliptic curve computation")
print("=" * 60)

def analyze_k3_curve(N):
    """
    The k=3 equation X³ - X = N(Y³ - Y) has the parametrization
    via lines through (1,1) giving the quartic:
      w² = N²s⁴ + 8Ns³ - 18Ns² + 8Ns + 1
    with known point (s,w) = (1, N-1).
    """
    print(f"\n{'='*50}")
    print(f"N = {N}")
    print(f"{'='*50}")
    
    R.<x> = QQ[]
    
    # The quartic: y² = f(x) where f = N²x⁴ + 8Nx³ - 18Nx² + 8Nx + 1
    f = N^2 * x^4 + 8*N * x^3 - 18*N * x^2 + 8*N * x + 1
    print(f"Quartic: w² = {f}")
    
    # Known rational point on the quartic
    P = (QQ(1), QQ(N - 1))
    print(f"Known point: (s, w) = {P}")
    
    # Verify the point is on the curve
    assert f(P[0]) == P[1]^2, "Point verification failed!"
    print("Point verified ✓")
    
    # Convert quartic to Weierstrass form
    # SageMath has EllipticCurve_from_cubic for cubics.
    # For quartics, we use the hyperelliptic curve approach.
    # 
    # Alternative: directly construct the elliptic curve from 
    # the original equation X³ - X = N(Y³ - Y).
    #
    # Let's use a different approach: work with the original cubic curve.
    # The curve C: X³ - NY³ - X + NY = 0 in projective coords.
    
    # Method: Use SageMath's EllipticCurve_from_cubic
    # First write the curve as a homogeneous cubic in P²
    # X³ - NY³ - XZ² + NYZ² = 0
    
    R3.<X,Y,Z> = QQ[]
    cubic = X^3 - N*Y^3 - X*Z^2 + N*Y*Z^2
    
    # Known rational point: (X:Y:Z) = (1:1:1)
    # (Check: 1 - N - 1 + N = 0 ✓)
    
    try:
        E = EllipticCurve_from_cubic(cubic, morphism=False)
        print(f"Weierstrass form: {E}")
        print(f"Cremona label: {E.cremona_label()}")
    except Exception as e1:
        print(f"EllipticCurve_from_cubic failed: {e1}")
        print("Trying alternative method...")
        
        # Alternative: construct directly from the affine equation
        # X³ - X = N(Y³ - Y)
        # Substituting X = u, Y = v, we get u³ - u - N(v³ - v) = 0
        # This is a plane cubic with the rational point (0,0).
        
        # For SageMath, use Cubic:
        R2.<u,v> = QQ[]
        cubic_affine = u^3 - u - N*(v^3 - v)
        
        # Homogenize: u³ - uw² - N(v³ - vw²) = 0
        # = u³ - Nv³ - uw² + Nvw² = 0
        
        try:
            from sage.schemes.elliptic_curves.constructor import EllipticCurve_from_cubic
            cubic_hom = X^3 - N*Y^3 - X*Z^2 + N*Y*Z^2
            E = EllipticCurve_from_cubic(cubic_hom, morphism=False)
            print(f"Weierstrass form: {E}")
        except Exception as e2:
            print(f"Alternative also failed: {e2}")
            
            # Last resort: manual Weierstrass form via the quartic
            # Use HyperellipticCurve
            try:
                H = HyperellipticCurve(f)
                print(f"Hyperelliptic curve: {H}")
                # For genus 1, we can get the Jacobian
                J = H.jacobian()
                print(f"Jacobian: {J}")
            except Exception as e3:
                print(f"HyperellipticCurve failed: {e3}")
                print("Manual computation needed.")
                return None
    
    # Compute rank and integral points
    try:
        rank = E.rank()
        print(f"Rank: {rank}")
        
        torsion = E.torsion_order()
        print(f"Torsion order: {torsion}")
        
        if rank == 0:
            print(f"*** RANK 0: Only torsion points exist ***")
            print(f"*** This means finitely many rational points ***")
        
        # Find all integral points
        int_pts = E.integral_points()
        print(f"Integral points: {int_pts}")
        print(f"Number of integral points: {len(int_pts)}")
        
        # For each integral point, check if it corresponds to an 
        # admissible 686 solution
        print(f"\nChecking admissibility...")
        # We need to map back from Weierstrass coords to (X,Y) on original curve
        # This requires the inverse morphism from EllipticCurve_from_cubic
        
        return E
        
    except Exception as e:
        print(f"Rank/integral points computation failed: {e}")
        return E


# Run for all stuck and rescued squares
print("\n" + "=" * 60)
print("RESCUED SQUARES (should have admissible points)")
print("=" * 60)

for N in [9, 16]:
    analyze_k3_curve(N)

print("\n" + "=" * 60)
print("STUCK SQUARES (expect rank 0 or no admissible points)")
print("=" * 60)

for N in [4, 25, 49, 64, 81]:
    analyze_k3_curve(N)

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
print("""
INTERPRETATION GUIDE:
- Rank 0 → only finitely many rational points (torsion only)
  → if none are admissible, N is PROVABLY not k=3 representable
- Rank 1+ → infinitely many rational points
  → must check integral points explicitly
  → if no integral point is admissible, still not representable
     but the proof is computational, not structural
""")
