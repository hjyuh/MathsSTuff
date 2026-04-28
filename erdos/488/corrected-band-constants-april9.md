# EP-488: CORRECTED Band Constants Table
## April 9, 2026

## CORRECT C*(s) with t ≤ 10(s+1) (the ONLY justified bound)

| s  | kernel           | C*(s) | best t | old C* | ratio |
|----|-----------------|-------|--------|--------|-------|
| 4  | {2,3}           | 1     | 7      | 1      | 1.0×  |
| 5  | {2,3,5}         | -2    | —      | -2     | DEAD  |
| 6  | {2,3,5}         | 4     | 19     | 4      | 1.0×  |
| 7  | {2,3,5,7}       | 2     | 19     | 2      | 1.0×  |
| 8  | {2,3,5,7}       | 16    | 73     | 10     | 1.6×  |
| 9  | {2,3,5,7}       | 34    | 73     | 26     | 1.3×  |
| 10 | {2,3,5,7}       | 68    | 109    | 38     | 1.8×  |
| 11 | {2,3,5,7,11}    | 86    | 113    | 50     | 1.7×  |
| 12 | {2,3,5,7,11}    | 112   | 113    | 81     | 1.4×  |
| 13 | {2,3,5,7,11,13} | 128   | 139    | ?      | —     |
| 14 | {2,3,5,7,11,13} | 157   | 139    | ?      | —     |
| 15 | {2,3,5,7,11,13} | 198   | 157    | ?      | —     |

Old values (from band assessment, t < (s+1)²/2) underestimate by 30-80%.
Correct values verified computationally with ep488_band_constants.py.

## KEY: s ≤ 7 constants are UNCHANGED. s ≥ 8 are LARGER.

For |A| = 6 proof: Codex B used C₈=16, C₁₀=68 (matching correct values).
The |A| = 6 proof is VALID with correct constants.

## LIVE DEPTHS: All s ≥ 4 except s = 5.

s = 5 is the ONLY dead zone. All odd depths s = 7, 9, 11, 13, 15 are LIVE.
