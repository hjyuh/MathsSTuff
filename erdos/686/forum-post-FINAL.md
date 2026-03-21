Following up with a small amount of computational data for Problem 686.

For `k=3`, writing `X = m+2` and `Y = n+2` gives

`X^3 - X = N(Y^3 - Y).`

Using SageMath's `EllipticCurve_from_cubic` with the rational point `(1:1:1)`, I obtained the following Weierstrass models:

| `N` | Cremona label | rank | torsion |
|---|---|---|---|
| `4` | `135a1` | `1` | trivial |
| `9` | `19440s1` | `2` | trivial |
| `16` | `9180a1` | `2` | trivial |
| `25` | `140400dd1` | `2` | trivial |
| `49` | `105840cu1` | `2` | trivial |
| `64` | `16380d1` | `2` | `Z/2Z` |
| `81` | conductor `797040` | `3` | trivial |

All seven curves have positive rank. On the original cubic, a direct search for `Y in [-50,500]` gives:

- `N=9`: admissible point `(X,Y) = (27,13)`, i.e. `(m,n) = (25,11)`.
- `N=16`: admissible point `(X,Y) = (15,6)`, i.e. `(m,n) = (13,4)`.
- `N=4`: the nontrivial point `(X,Y) = (3,2)`, but it is not admissible.
- `N in {25,49,64,81}`: only the 9 trivial points `{-1,0,1}^2`.

Important caveat: the birational map to the Weierstrass model does not preserve integrality in general. For example, the known `N=16` solution `(X,Y) = (15,6)` maps to a non-integral Weierstrass point. So integral points on the Weierstrass model do not by themselves prove non-representability on the original cubic.

For `k=5` and `N=4`, let

`F(t) = (t+1)(t+2)(t+3)(t+4)(t+5).`

Then `F(x) = 4F(y)` has no rational points at infinity, since this would require a rational root of `u^5 - 4`, which is irreducible over `Q`. A brute-force search for `|x|, |y| <= 10000` finds only the 25 trivial zero-product points `{-5,-4,-3,-2,-1}^2`, and no admissible solutions.

A congruence obstruction also cannot prove non-representability here. For every modulus `M`, the congruence

`F(m) ≡ 4F(n) (mod M)`

has admissible solutions with `m >= n+5`: for `M >= 5`, take `n = M-1` and `m = 3M-5`, so `F(n) ≡ F(m) ≡ 0 (mod M)` and `m-n = 2M-4 >= 6`; for `M <= 4`, the pair `(n,m) = (0,5)` already works.

For `N=4`, this leaves the following status:

| `k` | status | method |
|---|---|---|
| `2` | not representable | Tao |
| `3` | no admissible solution found for `Y <= 500` | direct search on `X^3-X = 4(Y^3-Y)`; `135a1` has rank `1` |
| `4` | not representable | natso26 |
| `5` | no admissible solution found for `|x|,|y| <= 10000` | direct search; no congruence obstruction exists |
| `6` | not representable | Vjeko |

AI disclosure: the computations were run in SageMath/CoCalc, and the draft of this comment was prepared with AI assistance (Claude, GPT, Codex). The computational claims above were checked by the author.
