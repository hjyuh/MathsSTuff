# EP-488: 5.2 Pro — The Cash-Flow Identity (D = 2m - n)
## April 7, 2026

## THE BREAKTHROUGH IDENTITY

For any layer j, the contribution decomposes as:

  2m·L(s) - n·L(t) = D·L(s) - n·(L(t) - L(s))

where D = 2m - n > n (always, since m > n).

INTERPRETATION:
- Every BANKED survivor (present at time n) earns D units of slack
- Every NEW survivor (appears between n and m) costs n units
- Since D > n, BANKED SURVIVORS ARE WORTH MORE THAN NEW SURVIVORS COST

## WHY COMPENSATION IS INEVITABLE

Child (bad compact, L_K(s) = 1):
  E_j = n·Δ_j - D    where Δ_j = L_j(t) - 1

  The child has 1 banked survivor (earning D) but Δ_j new survivors
  (each costing n). Since Δ_j ≤ 7 and D > n, the child excess is at
  most 7n - D = 7n - (2m-n) = 8n - 2m. This is small.

Parent (3-ancestor, evaluates deeper):
  S_i = D·L_i(s') - n·Δ_i    where Δ_i = L_i(t') - L_i(s')

  The parent has L_i(s') banked survivors (each earning D) and Δ_i
  new survivors (each costing n). Since L_i(s') ≥ 2 typically and
  D > n, the parent earns at least 2D while paying at most a few n.

COMPARISON: S_i ≥ E_j iff D·(L_i(s') + 1) ≥ n·(Δ_j + Δ_i)

Since D > n, this holds whenever L_i(s') + 1 ≥ Δ_j + Δ_i.
The child has Δ_j ≤ 7. The parent's Δ_i is typically small (1-3).
So we need L_i(s') ≥ Δ_j + Δ_i - 1 ≈ 8-10.

At s' ≥ 8 (which the parent always achieves in compact bad cases),
L_i(s') is typically 3-6 even with obstructions. So we need the
STRONGER bound D > n amplified by L_i(s')/1 ≈ 3-6× to carry it.

Actually: since D/n > 1, even L_i(s') = 2 with Δ_i = 1 gives
S_i = 2D - n > 2n - n = n, while E_j = n·Δ_j - D < 7n - n = 6n.
So we need 2D - n ≥ 7n - D, i.e. 3D ≥ 8n, i.e. m ≥ 11n/6 ≈ 1.83n.

For m < 1.83n, the cash-flow advantage alone isn't enough — you need
L_i(s') ≥ 3 or Δ_j to be small. But this is exactly the compact regime
where the 29-kernel classification constrains Δ_j.

## THE TIGHTEST CASE EXPLAINED

A = {2,9,15,25}, n = 124, m = 175, D = 2·175 - 124 = 226.

Child (a=25): L(4)=1 banked, Δ=2 new survivors
  E = 124·2 - 226·1 = 22

Parent (a=15): L(8)=3 banked, Δ=1 new survivor
  S = 226·3 - 124·1 = 554

Cash-flow: parent has 3 banked (earning 3×226=678) minus 1 new (costing 124).
Child has 1 banked (earning 226) but 2 new (costing 2×124=248).
The 3:1 ratio in banked survivors × the D > n amplifier = huge margin.

## THREE-WAY CONVERGENCE

| Model | Language | Same Insight |
|-------|----------|-------------|
| Codex B | 3-tax / upstream credit | Child pays Buchstab tax, parent overfunds |
| Codex A | Initial gap / forced dephasing | Parent evaluates past the survivor desert |
| 5.2 Pro | Cash-flow / D = 2m-n | Banked survivors worth more than new ones cost |

All three say: the child is FROZEN at n, the parent has already BANKED
survivors by n, and the coefficient structure (2m vs n, hence D > n)
makes banked survivors more valuable than new survivors.

## WHAT REMAINS

The cash-flow identity reduces compensation to:
  L_i(s') + 1 ≥ Δ_j + Δ_i (sufficient when D > n)

  or more precisely: D·(L_i(s') + 1) ≥ n·(Δ_j + Δ_i)

This needs:
1. A lower bound on L_i(s') (parent's banked survivors)
2. An upper bound on Δ_i (parent's new survivors)
3. The known bound Δ_j ≤ 7

The key sub-lemma is now: "In the compact regime, the 3-ancestor always
has L_i(s') ≥ 3 and Δ_i ≤ L_i(s')." This is an ACTIVE OBSTRUCTION
statement about small evaluation windows, not a kernel comparison.

## KILL COUNT: 61 (unchanged)
## PERCENTAGE: 84%
