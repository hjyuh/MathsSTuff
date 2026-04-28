# EP-488 v26 — The Q_s(λ) Computation (Resolved)
## April 11, 2026

This note resolves the v26 “discrepancy”:

- the **universal** recursive coefficient `P_s` (uses `C*(s)` maxima at varying λ) makes
  `f(29/20)` blow up (~57k by `s<=200`),
- the **fixed-λ** recursive coefficient `Q_s(λ)` (uses the same λ throughout the recursion)
  gives a small value at `s<=200` (~1.09),
- but **the Q_s(λ) sum still diverges** as `s` grows: for `λ=29/20`, the partial sum crosses
  `λ` at `s=256`.

Code: `erdos/488/ep488_qs_lambda_v26.py`

---

## Definitions (v26)

For band `s>=4` (with `s=5` dead), define

- `t_s(λ) = floor((s+1)λ)`,
- `L_s(t) = #{1<=x<=t : x coprime to all primes <= s}` (equivalently: `spf(x) > s`, plus `x=1`),
- `c_s(λ) = max(0, (s+1)(L_s(t_s(λ)) - 2λ))`,
- geometric edges `(s→u,h)` with odd `h>=3` satisfying `2s/(u+1) < h < 2(s+1)/u`,
- “active at λ” iff `c_s(λ)>0` and `c_u(λ)>0`.

Then

`Q_s(λ) = c_s(λ) + Σ_{(s→u,h) active at λ} (h/2)·Q_u(λ)`.

The v26 sum tested is

`g_N(λ) = Σ_{active s<=N} Q_s(λ) · (2s+1)/(2 s^2 (s+1)^2)`.

---

## 1) The 7 test lambdas, computed exactly to N=200

These are the exact results from:

`python erdos/488/ep488_qs_lambda_v26.py`

| λ | active bands in [4,200]\{5} | g_200(λ) | g_200(λ) < λ? |
|---:|---:|---:|:---:|
| 29/20 = 1.45 | 194 | 1.091715808 | ✅ |
| 7/5 = 1.40 | 191 | 1.058374276 | ✅ |
| 3/2 = 1.50 | 183 | 0.868170819 | ✅ |
| 13/9 ≈ 1.444… | 193 | 1.096735105 | ✅ |
| 2 | 191 | 3.016088439 | ❌ |
| 5/2 | 192 | 4.639661637 | ❌ |
| 3 | 192 | 6.264564546 | ❌ |

So “g(λ) < λ on (1,10]” is already false at `N=200` for λ ≥ 2, under the literal v26 definition.

---

## 2) Tail behavior at λ = 29/20 (the fork is resolved)

For λ = 29/20, the partial sums are:

- `g_25 = 0.058534334`
- `g_50 = 0.174923570`
- `g_100 = 0.462837345`
- `g_150 = 0.768891343`
- `g_200 = 1.091715808`

However, pushing `N` higher shows the **fixed-λ recursion still grows**:

Running:

`python erdos/488/ep488_qs_lambda_v26.py --max-s 1000 --lambdas 29/20 --partials 200,256,300,500,1000`

gives:

- `g_256 = 1.455555613`  (FIRST `N` where `g_N >= 29/20`)
- `g_300 = 1.762631700`
- `g_500 = 3.206790527`
- `g_1000 = 7.096190459`

So **Codex B’s ~1.06 number was a truncation artifact** (it matches the `N<=200` regime).
The infinite-series claim “g(29/20) converges < 1.45” is false.

---

## 3) Q vs P magnitude (why the discrepancy existed at all)

At λ=29/20 and `s<=200`, `Q_s(λ)` is ~4% of the universal `P_s`:

| s | P_s | Q_s(29/20) | Q/P |
|---:|---:|---:|---:|
| 100 | ~184,534.22 | ~7,134.65 | ~0.039 |
| 150 | ~517,732.86 | ~20,325.49 | ~0.039 |
| 200 | ~1,015,670.18 | ~44,263.00 | ~0.044 |

This confirms the conceptual point: `P_s` stacks worst-case λ values across the recursion tree,
while `Q_s(λ)` “deflates” everything at a fixed λ. But the deflation is not strong enough to
make the global sum converge.

---

## Bottom line (v26)

- The fixed-λ recurrence `Q_s(λ)` is computable and does explain the huge P-vs-Q discrepancy at `s<=200`.
- But the v26 endgame statement “g(λ) < λ for all λ” is **false**:
  it fails for λ ≥ 2 already at `N=200`, and it fails at λ = 29/20 by `N=256`.

This means the uniform proof still needs a new structural ingredient beyond the raw recursive packages:
some arithmetic sparsity / witness-cost / CRT packing phenomenon that is not represented in `Q_s(λ)`.

