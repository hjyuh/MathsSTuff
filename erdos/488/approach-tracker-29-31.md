# EP-488: Approach Tracker Update — April 2, 2026

## Approaches 29-31

### #29 (Halving map / primitivity injection)
KILLED. Cross-stream collisions uncontrolled. lcm arithmetic was off by power of a.

### #30 (Hall/SDR on M_b(I) sets)  
KILLED. Strictly stronger than Window Lemma — fails where (W) holds.
Counterexample: a=41, k=2, b1=84, b2=112 share multiple 336 in window.

### #31 (Global W(x) ≥ W(0) = t)
KILLED GLOBALLY. Counterexample: a=331, k=2, t=330, x=217623, W(x)=329 < 330.
Also: a=503, k=2, t=502, x=503542, W(x)=499 < 502.

BUT: Failures occur FAR beyond first peak.
- a=331: m* = 4970, bad window at x = 217623 (44x past peak)
- The LOCAL version W(x) ≥ t for 0 ≤ x ≤ m* - 2ka SURVIVES all tests

### What survives
LOCAL pre-peak Window Lemma: W(x) ≥ t for x in the pre-peak range only.
This is sufficient for the first plateau lemma.
The pre-peak range has only finitely many active layers (j ≤ m*/(ka+1)),
making collisions sparse and classifiable.

## Total: 31 approaches, 2 theorems proved, 29 killed or restricted
