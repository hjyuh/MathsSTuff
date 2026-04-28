# EP-488: 5.4 Pro — t-Bound Kill + Odd Depths Live (v16 response)
## April 9, 2026

## TWO CONCRETE FAILURES IN v16's BAND TABLE

### Failure 1: Odd depths s=7,9 are LIVE (not dead zones)

A = {22,33,55,77,143,1143}, n=1143, m=2717.
Layer 5 (a=143): K={2,3,5,7}, s=7, t=19, L(7)=1, L(19)=5.
E = 1143·5 - 2·2717 = 281 > 0. FIRST BAD LAYER AT s=7.

A = {22,33,55,77,143,1429}, n=1429, m=1859.
Same layer 5: s=9, t=13, L(9)=1, L(13)=3.
E = 1429·3 - 2·1859 = 569 > 0. FIRST BAD LAYER AT s=9.

Live depths for j₀=5: {4, 6, 7, 8, 9, 10} — NOT just {4,6,8,10}.

### Failure 2: m/n < (s+1)/2 is FALSE

A = {22,33,55,77,143,1572}, n=1572, m=15720 (m = 10n).
Layer 5: s=10, t=109, L(10)=1, L(109)=26.
E = 1572·26 - 2·15720 = 9432 > 0.

v16 bound: E < 36a = 36·143 = 5148. VIOLATED (9432 > 5148).

The m/n = 10 >> (s+1)/2 = 5.5. The t = 109 >> (s+1)²/2 = 60.5.

## CORRECT UNIVERSAL t-BOUND

From convexity window ONLY:
  t = ⌊m/a⌋ ≤ 10M/(M/(s+1)) = 10(s+1)

So t ≤ 10s + 9. This is the ONLY justified bound.

## CORRECTED BAND CONSTANTS NEEDED

C_K(s) = max_{s < t ≤ 10s+9} ((s+1)L_K(t) - 2t)

These are LARGER than v16's table. The exact values need computation
with ep488_band_constants.py using the corrected t-range.

## WHAT SURVIVES

- |A| ≤ 6: PROVED (Codex B used conservative larger C values) ✓
- Layer-3-bad for ALL |A|: PROVED (doesn't use band constants) ✓
- All 40+ permanent results: unaffected ✓
- The self-regulation mechanism: intact ✓

## WHAT DIES

- v16's C*(s) table with t < (s+1)²/2: WRONG
- The "only even depths" claim: WRONG
- The "remaining 7%" framing based on those constants: TOO OPTIMISTIC

## PERCENTAGE: 91%

The proved results hold but the remaining gap is wider than v16/v17
claimed. The band constants need recomputation with t ≤ 10(s+1).
