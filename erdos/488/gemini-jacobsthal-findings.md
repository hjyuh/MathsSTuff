# EP-488: Literature Findings — April 5, 2026
# From Gemini

## THE THREE KEY REFERENCES

1. Montgomery & Vaughan (1986). "On the distribution of reduced residues."
   Annals of Mathematics, 123(2), 311-333.
   → Tight bounds on moments of localized coprime counts
   → Proves Erdős's conjecture on second moment of gaps
   → THIS IS THE PAPER most likely to contain our lemma

2. Friedlander & Iwaniec (2010). Opera de Cribro.
   → Fundamental Lemma of Sieve Theory
   → Bypasses 2^ω(Q) barrier via sieving limit parameter
   → Local error bounded by function of ω(Q) and log y / log z

3. Hall & Tenenbaum (1988). Divisors. Chapter 5.
   → "The density of sets of multiples"
   → Explicitly analyzes primitive sequence local discrepancy
   → Fourier analysis on divisor distribution

## QUOTIENT-CORE CONSTRAINT HELPS
Gemini confirms: primitive set structure prevents Q from being worst-case.
The effective ω(Q) for localized sieve is smaller than theoretical max.

## ACTION: Send these references to GPT-5.2 Pro or GPT-5.4 Pro
Ask them to apply Montgomery-Vaughan or the Fundamental Lemma to prove
C^loc_Q(r) < r·ρ_Q/3 for quotient-cores.
