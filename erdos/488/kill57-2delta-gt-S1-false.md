# EP-488: Kill #57 — 2δ_A > S₁ is FALSE + Gemini Literature Results
## April 6, 2026

## KILL #57: 2δ_A > S₁ fails for large prime sets

A = {primes p ≤ 100}. This is primitive.
S₁ = Σ 1/p ≈ 2.10
δ_A = 1 - Π(1-1/p) ≈ 0.88
2δ_A ≈ 1.76 < 2.10 = S₁

The 830K+ verifications passed because they tested sets with S₁ < 2.
For S₁ ≥ 2, the inequality 2δ > S₁ fails.

CONSEQUENCE: Cannot use S₁ as middleman. The chain
"2G(x) > S₁ ≥ G(m)" breaks when S₁ ≥ 2.
Must compare G(m) to G(n) DIRECTLY, not through S₁.

## GEMINI LITERATURE RESULTS

### 1. Granville-Soundararajan reference (confirmed real):
"The spectrum of multiplicative functions" (Annals of Math, 2001)
- Converts discrete IE sums into continuous integral equations
- Uses Dickman/Buchstab function framework
- Proves oscillation contraction through integral equations

Secondary: GS (2003) "Distribution of values of L(1,χ_d)" (GAFA)
- Explicitly evaluates alternating fractional part sums via integration

### 2. Key technique: Fourier expansion of fractional parts
{t} = 1/2 - Σ sin(2πkt)/(πk)
Substituting into the IE alternating sum converts combinatorial
problem into exponential sum over multiples.

Reference: Montgomery & Vaughan (1977) "On the fractional parts of x/n"
- Integration of Fourier series forces massive cancellation in alternating signs

### 3. Logarithmic averaging is the right measure
Use (1/log 2) ∫_M^{2M} G(x) dx/x instead of (1/M) ∫_M^{2M} G(x) dx.
Under log averaging, fractional part errors decay as O(1/x²) inside
the integral, making GS Fourier techniques much more powerful.

### 4. The path forward (Gemini's recommendation):
- Drop S₁ as middleman entirely
- Compare G(m) to G(n) directly via logarithmic integrals
- Use GS framework to bound the alternating sum of fractional-part integrals
- The key: oscillation of G contracts under integration, not pointwise

## KILL COUNT: 57
## PERCENTAGE: 65%
