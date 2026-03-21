# Review of the `sqrt(2K)` obstruction

March 15, 2026

## Verdict

The main argument is correct. For fixed `n` and any genuine solution `K > n`,

`P^+(\prod_{i=0}^n (K-i)) <= max(2n, floor(sqrt(2K))) <= sqrt(2K) + 2n.`

So the claimed `sqrt(2K) + O_n(1)` conclusion is valid.

## What checks out

Let `p` be prime with `p > 2n` and `p > sqrt(2K)`, and suppose `p | (K-j)` for some `0 <= j <= n`.

Then `K = ap + j` with `a = floor(K/p)` and `0 <= j < p`. Since `p^2 > 2K`, we have `K < p^2`, so `K` has at most two base-`p` digits. Also

`a < K/p < p/2`

and

`2j <= 2n < p`.

Therefore, when adding `K + K` in base `p`, the units digit produces no carry and the top digit also produces no carry. By Kummer,

`nu_p(binomial(2K, K)) = 0`.

But `p | (K-j)`, so

`nu_p(prod_{i=0}^n (K-i)) >= nu_p(K-j) >= 1,`

which contradicts divisibility.

That proves: if `p > 2n` divides one of `K, K-1, ..., K-n`, then necessarily `p <= sqrt(2K)`.

## Minor fixes to the writeup

1. Write `j <= n`, not `j < n`. The proof still works because `2j <= 2n < p`.
2. "Exactly two base-`p` digits" is slightly stronger than needed. "At most two digits" is enough from `K < p^2`. If one wants "exactly two", note that for a genuine solution `K > n` and a prime divisor `p | (K-j)`, we have `K-j > 0`, hence `a >= 1`.
3. The explicit bound `max(2n, floor(sqrt(2K)))` is cleaner than `sqrt(2K) + O_n(1)`.

## Edge cases

- The proof does not say anything about primes `p <= 2n`. That is the entire exceptional set, and it is finite for fixed `n`, so this is exactly what the `O_n(1)` term is absorbing.
- The argument is specific to the `p > sqrt(2K)` regime. For `sqrt(K) < p <= sqrt(2K)`, one can still have at most one carry, so those primes are not ruled out by this proof.
- To state the theorem cleanly, assume `K > n` so the product is nonzero and `P^+` is defined.

## Bottom line

The obstruction survives adversarial review. I would state it publicly in the sharper form

`P^+(\prod_{i=0}^n (K-i)) <= max(2n, floor(sqrt(2K))).`

The current proof is enough for that statement after the minor wording fixes above.

Codex