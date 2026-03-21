# Full-state review for Problem 396

March 15, 2026

## Executive verdict

The project is in materially better shape than it was this morning, but the current prompt still overstates how close the proof is.

- Theorem 2 (one-carry automaticity) is correct.
- The mesoscopic carry analysis looks plausible, but it is only useful if written in a genuinely uniform dyadic form.
- The final gap is not just "positive density of smooth blocks". Even if you had that, you would still need an intersection theorem between the smooth-block set and the carry-good set.

So the proof is not yet "one missing standard citation" away. The last step is still a real analytic number theory problem.

## 1. Review of Theorem 2

Verdict: PASS.

A clean proof is as follows.

Assume `p > 2n`, `sqrt(K) < p <= sqrt(2K)`, and `p | (K-j)` for some `0 <= j <= n`. Write

`K = ap + j`,

with `0 <= j <= n < p/2`.

Because `p > sqrt(K)`, we have `p^2 > K`, hence `a < p`. Also `0 < K-j < p^2`, so

`nu_p(K-j) = 1`.

Now use `p <= sqrt(2K)`, i.e. `K >= p^2/2`. If `a <= (p-1)/2`, then since `j <= n <= (p-1)/2`,

`K = ap + j <= ((p-1)/2)p + (p-1)/2 = (p^2-1)/2 < p^2/2`,

contradiction. Hence `a >= (p+1)/2`, so `p < 2a < 2p`.

When doubling `K` in base `p`:

- the units digit contributes `2j < p`, so there is no carry from the units place;
- the top digit contributes `2a`, which lies in `[p+1, 2p-2]`, so there is exactly one carry.

Therefore `kappa_p(K) = 1 = nu_p(K-j)`, so the carry condition is automatic.

This is the right statement for the band `sqrt(K) < p <= sqrt(2K)`.

## 2. What the remaining gap actually is

There are two separate questions, and the current prompt merges them.

### A. Do smooth blocks have positive density?

For fixed `n`, is it true that

`#{K in [X,2X] : P^+(prod_{j=0}^n (K-j)) <= sqrt(2X)} >= c_n X`

for some `c_n > 0`?

I do not know a standard one-line citation for this exact consecutive-shift statement.

I did find a relevant recent primary source:

- Lilian Matthiesen and Mengdi Wang, "Smooth numbers are orthogonal to nilsequences," Algebra and Number Theory 19 (2025), Theorem 1.3 / Corollary 1.4. It proves asymptotic lower bounds for simultaneous smooth values of systems of shifted linear forms in a fairly large smoothness range.
  Link: https://arxiv.org/abs/2211.16892
  Journal PDF: https://msp.org/ant/2025/19-10/ant-v19-n10-p01-p.pdf

But there is an important caveat: the theorem as stated in the paper is for pairwise linearly independent forms in at least two variables. Your pattern `K, K-1, ..., K-n` is a one-variable parallel-shift system, so this is suggestive, not a drop-in theorem.

So my current assessment is:

- this smooth-block density question is not obviously standard;
- there is nearby modern machinery in the literature;
- I would not claim today that the exact `c_n X` theorem for consecutive shifts is already in hand.

### B. Even if smooth blocks have positive density, does that finish the proof?

No.

This is the bigger logical issue.

If the carry-good set has density `delta_1 > 0` in `[X,2X]` and the smooth-block set has density `delta_2 > 0` in `[X,2X]`, it does **not** follow that their intersection is nonempty. Two positive-density sets can be disjoint.

So the proof is not complete from:

- positive density of carry-good `K`, and
- positive density of smooth-block `K`

alone.

You need an actual interaction theorem, for example one of the following:

- a count of smooth blocks inside the carry-good residue set;
- a correlation / equidistribution result showing smooth blocks are not concentrated away from the carry-good set;
- a direct joint sieve that imposes both structures at once.

That is the main conceptual gap in the current proof structure.

## 3. Assessment of the current proof architecture

Here is the strongest version I am comfortable endorsing.

### Solid

- `P^+(prod(K-i)) <= max(2n, floor(sqrt(2K)))` is proved.
- The band `sqrt(K) < p <= sqrt(2K)` is automatic once a term `K-j` is divisible by `p`.
- The hard primes are indeed `p <= sqrt(K)`.
- The overall decomposition by prime ranges is correct and useful.

### Plausible but still needs full writeup

- The mesoscopic local bad densities `~ (n+1) 2^{-r} / p` by layer.
- Summability over layers.
- A dyadic version of the carry-good sieve.

I would not yet treat this as "finished" until the local conditions and the dyadic bookkeeping are written carefully enough that someone else can check them line by line.

### Still missing

- A theorem that produces enough `sqrt(X)`-smooth consecutive blocks in the specific structured environment created by the carry-good conditions.

That is the real last bridge.

## 4. Alternative direct sieve for the smoothness side

GPT's sieve idea is directionally good.

For primes `p > sqrt(2X)`, a prime can divide at most one of the shifts `K-j`, and each shift `K-j` can have at most one such prime divisor. So the large-prime obstruction is finite-depth in a way that resembles a Buchstab decomposition rather than a naive infinite Euler product.

For `n=0`, this is exactly the Dickman/Buchstab world and gives `rho(2) = 1 - log 2`.

For fixed `n >= 1`, I think a direct sieve / inclusion-exclusion over the forbidden residue classes

`K = j mod p`,  `p > sqrt(2X)`,  `0 <= j <= n`

is a plausible route to a positive-density constant `c_n`. The combinatorics should be more tractable than a fully general smooth-number theorem because there can be at most one large prime per shift.

But two cautions:

1. This is still nontrivial. It is not just `1 - (n+1) sum 1/p`; higher intersections matter, and one needs a controlled Buchstab-style expansion.
2. Even if this succeeds for the ambient integers, you still need to combine it with the carry-good constraints. That joint problem is harder than the pure smoothness count.

So I would treat the direct sieve as a promising research path, not as a completed reduction.

## 5. How close is this?

My score is **5/10**.

Why not lower:

- the large-prime structure is now genuinely understood;
- Theorem 2 is real progress;
- the computational side is strong and consistent with the theory;
- the remaining problem is sharper than before.

Why not higher:

- the current prompt conflates smooth-block density with intersection;
- the key final bridge is still unproved;
- I do not yet see a drop-in literature theorem that handles the consecutive-shift smoothness problem in exactly the form you need.

If you can prove either

- a positive lower bound for smooth blocks inside the carry-good set, or
- a direct joint sieve for carry + smoothness,

then the project jumps immediately into the 8/10 range.

## Bottom line

Theorem 2 passes.

The overall decomposition is right.

The remaining gap is still substantial and is best described as a **joint distribution problem** between carry-good residue constraints and tuple smoothness, not merely a missing smoothness-density citation.

Codex