# Review of the collapse argument

March 15, 2026

## Verdict

The first implication is correct, but the claimed collapse is **not currently valid**.

If `K` satisfies

`nu_p(K-j) <= kappa_p(K)`

for every prime `p > 2n` and every `0 <= j <= n` with `p | (K-j)`, then indeed

`P^+(\prod_{i=0}^n (K-i)) <= max(2n, floor(sqrt(2K))).`

So `full carry-goodness => sqrt(2K)-smoothness` is true.

What does **not** follow at present is that the full carry-good set has positive density, or even that current GPT layer heuristics are enough to prove nonemptiness. That is the actual missing step.

## Main gap

The argument fails at step (1):

> "GPT's layer analysis shows carry-good K has positive density via summable local obstructions + CRT/Euler product."

That statement is not established.

Summable local bad densities are **not enough by themselves** to conclude positive density of the global good set. The missing theorem is a rigorous local-to-global argument for the full carry condition.

## What is missing mathematically

1. For a fixed prime `p`, the event "K is good at p" is not obviously a fixed finite set of residue classes modulo `p^a` with `a` independent of `K`. The carry count `kappa_p(K)` depends on the full base-`p` expansion up to length about `log_p K`.
2. Because of that, the local condition varies with the dyadic interval `[M, 2M]`. A naive CRT/Euler-product argument is therefore not automatic.
3. Even if the local bad probabilities `q_p` were correct and summable, `sum q_p < infinity` alone does not prove the complement has positive lower density. One still needs genuine intersection control, not just a first-moment heuristic.
4. GPT's local counting has not yet been adversarially checked. The union over `j`, the higher-valuation spike cases `nu_p(K-j) >= 2`, and the claimed uniform asymptotic `q_p ~ 2^{-r}/p` are all still provisional.

## Correct part

The local implication itself is fine.

If `p > 2n`, `p > sqrt(2K)`, and `p | (K-j)`, then the two-digit argument gives `kappa_p(K) = 0`. So if `K` were fully carry-good at that prime, we would have `1 <= nu_p(K-j) <= kappa_p(K) = 0`, impossible. Hence no such `p` can occur.

So the `sqrt(2K)` smoothness bound is indeed a consequence of the **full** carry condition.

## But this does not collapse the proof

What you have shown is

`full carry-goodness for all p > 2n => smoothness bound.`

You have **not** shown

`current layer heuristics => positive-density set of fully carry-good K.`

So the smoothness condition has not been removed from the proof in any practical sense; it has only been reabsorbed into a stronger global carry theorem that is still unproved.

## Additional omission

Even after this discussion, the divisibility proof still has to handle the finitely many primes `p <= 2n` (or `p <= n`, depending on the formulation). Those are not a deep obstacle, but the statement "the entire proof reduces to carry-goodness for p > 2n" is not literally complete.

## Bottom line

- `carry-good => sqrt(2K)-smooth` is correct.
- `GPT layer analysis => positive-density full carry-good set` is **not** currently proved.
- Therefore Balog-Wooley/Granville is **not yet removable** from the proof strategy.

If a rigorous positive-density theorem for the full carry-good set is eventually proved, then yes: the external smoothness input would become redundant. But that stronger theorem is exactly what is still missing.

Codex