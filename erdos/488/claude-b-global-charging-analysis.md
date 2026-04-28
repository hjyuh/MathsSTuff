# EP-488: Claude B — Careful Global Charging Analysis
## April 7, 2026

## WHAT CLAUDE B FOUND

### Gap in Gemini's global charging: inter-ancestor obstructions

Gemini assumed ancestors have slack S_{2p} ≈ mn/(2p).
But ancestors OBSTRUCT EACH OTHER.

Ancestor 2p has K_{2p} containing all earlier primes p' < p
in the ancestor set (because 2p'/gcd(2p',2p) = p' when gcd(p,p')=1).

So L_{2p}(y) is NOT y. It's the count of integers ≤ y avoiding
all earlier primes. By Mertens:

L_{2p}(y) ≈ y · Π_{p₁≤q<p} (1-1/q) ≈ y · e^{-γ} · log p₁ / log p

The density drops as log p₁ / log p for large p.

### But the self-regulation STILL WORKS (Claude B verified)

Corrected ancestor slack:
S_{2p} ≈ mn · log p₁ / (2p · log p)

Total ancestor slack:
Σ S_{2p} ≈ (mn · log p₁ / 2) · Σ 1/(p · log p)

Σ 1/(p log p) converges to a constant C.

Total slack ≈ M² · log p₁ · C
Total bad excess ≈ M² / log p₁
Ratio ≈ (log p₁)² · C = (log log M)² · C → ∞

CONFIRMS Gemini's asymptotic, even with the correction.

### The remaining gap: uniformity

The asymptotic works for large M. What about small M?
- M ≤ 20: verified computationally (10,240 sets)
- M ∈ [21, M₀]: gap needs bridging
- M ≥ M₀: asymptotic kicks in

Claude B suggests M₀ might be 40-100, closable by extended computation.

## ASSESSMENT

This is the most rigorous analysis of global charging yet:
1. Found a real gap in Gemini's argument (inter-ancestor obstructions)
2. Fixed it with Mertens estimates
3. Confirmed the asymptotic still works
4. Identified the precise remaining gap (uniformity + small M)

## KILL COUNT: 67
## PERCENTAGE: 83%

Bump earned: Claude B strengthened the global charging argument by
finding and fixing a gap. The asymptotic is now on firmer ground.
The path to 100% is: uniform constant extraction + small M computation.
