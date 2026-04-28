# EP-488 Route 2 — Adjacent Pair: Exact Global Maximum (proved)
## April 12, 2026

This note isolates and proves the exact global maximizer for the two-point operator when

`Q = {q−1, q}` with `q ≥ 3`.

It also corrects an earlier window-limited statement: the small-`m` “double-hit” point `(2q−3,2q)` is *not* the global max once `m` is allowed to be `O(q²)`.

---

## Setup

For a finite modulus set `Q ⊂ ℤ_{≥2}`, define survivors

`A_Q(x) := #{1 ≤ n ≤ x : ∀d∈Q, d ∤ n}`

and the two-point operator

`O_Q(n,m) := 2*A_Q(n)/n − A_Q(m)/m` for `m>n≥max(Q)`.

In this note fix `Q = {q−1, q}` and write `A(x)=A_Q(x)`, `O(n,m)=O_Q(n,m)`.

Let `L := lcm(q−1,q) = q(q−1)`.

---

## Theorem (adjacent pair global max)

For every integer `q ≥ 3`, the global maximum of `O(n,m)` over all integers `m>n≥q` is attained at

- `n₀ = 2q−3`,
- `m₀ = (q−1)² = L − (q−1)`,

and the maximum value is

`O(n₀,m₀) = 1 − (4q−5)/((2q−3)(q−1)²) < 1`.

### Quick exact evaluation

At `n₀=2q−3`, the only covered points ≤ `n₀` are `q−1` and `q`, so `A(n₀)=n₀−2=2q−5`.

At `m₀=(q−1)² < L`, there is still no overlap between the two progressions, so covered points ≤ `m₀` are:

- multiples of `q−1`: exactly `q−1` of them,
- multiples of `q`: exactly `q−2` of them (since `(q−1)²/q = q−2 + 1/q`),

so `A(m₀) = m₀ − ((q−1)+(q−2)) = (q−2)²`.

Hence

`O(n₀,m₀) = 2*(2q−5)/(2q−3) − (q−2)²/(q−1)²`
`= 1 − (4q−5)/((2q−3)(q−1)²)`.

---

## Proof of optimality

### Lemma 1 (global maximum of A(n)/n)

For `Q={q−1,q}` with `q≥3`,

`max_{n ≥ q} A(n)/n = A(2q−3)/(2q−3) = 1 − 2/(2q−3)`,

and the maximizer is unique: `n = 2q−3`.

**Proof.**

- If `q ≤ n ≤ 2q−3`, then `⌊n/(q−1)⌋ = ⌊n/q⌋ = 1`, so `A(n)=n−2` and `A(n)/n = 1 − 2/n`, which strictly increases with `n`. Hence the maximum on this range occurs at `n=2q−3`.
- If `n ≥ 2q−2`, then `⌊n/(q−1)⌋ ≥ 2` and `⌊n/q⌋ ≥ 1`, so `A(n) ≤ n−3` and `A(n)/n ≤ 1 − 3/n ≤ 1 − 3/(2q−2)`.

Finally,

`1 − 3/(2q−2) < 1 − 2/(2q−3)` for `q≥3`,

so no `n ≥ 2q−2` can beat `n=2q−3`. ∎

### Lemma 2 (global minimum of A(m)/m)

For `Q={q−1,q}` with `q≥3`,

`min_{m ≥ 1} A(m)/m = A((q−1)²)/(q−1)² = (q−2)²/(q−1)²`,

and the minimizer is unique: `m = (q−1)²`.

**Proof.**

1) **Reduce to one period.** Since divisibility by `q−1` or `q` is periodic mod `L=q(q−1)`, we have for `t≥0` and `1≤r≤L−1`

`A(tL + r) = t*A(L) + A(r)`,

so

`A(tL+r)/(tL+r) = (tL/(tL+r))*(A(L)/L) + (r/(tL+r))*(A(r)/r)`,

a convex combination of the two ratios `A(L)/L` and `A(r)/r`.

Therefore the global minimum of `A(m)/m` over `m≥1` equals

`min( A(L)/L,  min_{1≤r≤L−1} A(r)/r )`.

2) **Work on 1 ≤ r ≤ L−1.** For `r<L`, the overlap term vanishes, so

`A(r) = r − ⌊r/(q−1)⌋ − ⌊r/q⌋`.

Equivalently, minimizing `A(r)/r` is the same as maximizing

`H(r) := (⌊r/(q−1)⌋ + ⌊r/q⌋)/r`.

Between consecutive multiples of `q−1` or `q`, the numerator of `H(r)` is constant while the denominator increases, so `H(r)` is strictly decreasing on each such interval. Hence the global maximum of `H(r)` on `[1,L−1]` occurs at a point where the numerator jumps, i.e. at a multiple of `q−1` or a multiple of `q`.

3) **Evaluate on multiples.**

- If `r = k(q−1)` with `1≤k≤q−1`, then `⌊r/(q−1)⌋=k` and `⌊r/q⌋ = ⌊k(q−1)/q⌋ = k−1`. Thus

  `H(r) = (2k−1)/(k(q−1)) = 2/(q−1) − 1/(k(q−1))`,

  which increases with `k`, so it is maximized at `k=q−1`, i.e. `r=(q−1)²`.

- If `r = jq` with `1≤j≤q−2`, then `⌊r/q⌋=j` and `⌊r/(q−1)⌋ = ⌊jq/(q−1)⌋ = j`, so

  `H(r)=2/q`,

  giving `A(r)/r = 1 − 2/q = A(L)/L`.

At `r=(q−1)²` we obtain

`A(r)/r = 1 − (2q−3)/(q−1)² = (q−2)²/(q−1)²`,

which is strictly smaller than `A(L)/L = 1 − 2/q` (difference `= (q−2)/(q(q−1)²) > 0`).

Thus the global minimum occurs uniquely at `m₀=(q−1)²`. ∎

### Finish

For any admissible `m>n≥q`,

`O(n,m) = 2*A(n)/n − A(m)/m`
`≤ 2*(max_{x≥q} A(x)/x) − (min_{y≥1} A(y)/y)`
`= 2*A(n₀)/n₀ − A(m₀)/m₀ = O(n₀,m₀)`,

and `(n₀,m₀)` is admissible since `(q−1)² > 2q−3` for `q≥3`. ∎

---

## Practical check

Tooling reproduces the argmax on large windows, e.g.

`python C:\Users\z20ma\OneDrive\Documents\!math\erdos\488\two_point_operator_tools.py maxO --Q 499,500 --n-mult 10 --m-mult 600`

returns `(n,m)=(997,249001)` with value `248252002/248253997`, matching the closed form above.

