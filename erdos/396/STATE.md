# STATE.md - Erdos Problem 396
## Last Updated: March 17, 2026

### Status: REDUCTIONS LARGELY COMPLETE; LIVE FRONTIER IS FIXED-SHIFT TWIN-SMOOTH CORRELATION

**Bottom line.** Problem 396 is not close to solved, but it is now sharply localized.
Most false routes have been closed cleanly. The current live theorem is a fixed-shift
smooth-pair statement in one arithmetic progression:

\[
\#\{X<n\le 2X:\ n\equiv a \pmod q,\ P^+(n)\le \sqrt{2X},\ P^+(n-1)\le \sqrt{2X}\}
\gg_q \frac{X}{q},
\]

or any polylog-loss lower bound strong enough for infinitude.

## Executive Verdict

### Closed or essentially closed

1. **Absolute-value Fourier / discrepancy route**
   - Blocked on average already at the top-block pair layer.
   - The obstruction survives block averaging.
   - This is now a barrier theorem, not an open lead.

2. **Fixed-r large-prime tail bounds**
   - Short-block tails: controlled for every fixed `r` under the structured reduction.
   - Long-block tails: controlled by standard fixed-r upper-bound sieve arguments.
   - Recombination of overlap tails: routine union-bound level.

3. **Large-prime overlap decomposition via `B_chi`**
   - Mathematically valid and diagnostically useful.
   - Not a viable proof strategy.
   - The surviving long-block theorem would require an averaged twisted Hardy-Littlewood
     prime-pair asymptotic in polylogarithmic intervals, which is beyond current technology.

### Still open / genuinely live

1. **Direct fixed-shift twin-smooth theorem (`n=1`)**
   - This is the first serious live checkpoint.
   - If it falls, the full program becomes much more believable.
   - If it fails, the whole route likely stops here.

2. **Lifting from `n=1` to the full parallel family**
   - Not yet addressed.
   - Should not be attacked until the fixed-shift case is understood.

## What Was Proved or Clarified

### A. Fourier barrier

- Local Fourier transform of the block congruence set was made explicit.
- Support-profile decomposition for the good set was corrected.
- The relevant large-spectrum question was reduced to one-base first moments.
- A block-average pair obstruction theorem was obtained:
  absolute-value Fourier already reaches main-term scale on the top-block pair layer.

**Conclusion:** absolute-value Fourier / Erdős-Turán discrepancy is closed as a route.

### B. Large-prime tails

- Pair short-block theorem (`r=2`) closes by divisor switching plus a fixed-modulus
  prime upper bound.
- The same switching argument extends through triples and then to all fixed `r`
  under the exact structured reduction.
- This yields fixed-r short-block and long-block upper bounds for the large-prime tails.

**Important correction:** these tail bounds do **not** imply the simultaneous
`sqrt(2X)`-smooth-shift lower bound needed by 396.

### C. Lower-bound sieve from current inputs is impossible

- One-shift smooth asymptotics plus `O(X/q)` overlap upper bounds do not force
  positivity of the simultaneous smooth set.
- An abstract countermodel shows that current inputs alone are compatible with
  complete extinction of the simultaneous smooth set.

**Conclusion:** a new positive-correlation theorem is genuinely required.

## The Current Mathematical Frontier

### Exact fixed-shift theorem now needed

For fixed residue class `a mod q`,

\[
\#\{X<n\le 2X:\ n\equiv a \pmod q,\ P^+(n)\le \sqrt{2X},\ P^+(n-1)\le \sqrt{2X}\}
\gg_q \frac{X}{q},
\]

or at minimum

\[
\gg_q \frac{X}{q(\log X)^A}
\]

for some fixed `A`.

This is the first live theorem with a realistic chance of determining whether
the method survives.

## Best Current Route

### Use the direct smooth-pair correlation route, not the prime-pair route

Define

\[
f_X(n):=1_{\{P^+(n)\le \sqrt{2X}\}}.
\]

Then the key object is

\[
C_\chi(X):=\sum_{X<n\le 2X} f_X(n)f_X(n-1)\chi(n),
\]

for Dirichlet characters `chi mod q`.

The prime-overlap decomposition

\[
C_\chi = T_\chi - A_{0,\chi} - A_{1,\chi} + B_\chi
\]

is exact, but the `B_\chi` long-block term leads to an unrealistically strong
prime-pair asymptotic. So the viable route is to study the smooth-pair correlation
directly.

## Step 1 Frontier: AP-Localized Logarithmic Theorem

The clean first target is the residue-class logarithmic average

\[
S_a(x):=
\frac{1}{\log \omega(x)}
\sum_{\substack{x/\omega(x)\le n\le x\\ n\equiv a \,(\mathrm{mod}\, q)}}
\frac{f_x(n)f_x(n+1)}{n},
\qquad
f_x(n):=1_{\{P^+(n)\le \sqrt{x}\}}.
\]

The right form is

\[
S_a(x)=c_{a,q}+o_q(1),
\]

where `c_{a,q}` is a new two-shift local profile.

### What survives from existing technology

- Scale-dependent families `f_x` are allowed in Teräväinen's framework.
- The short-interval AP lemma (Lemma 3.4) is already present for real-valued multiplicative functions.
- Minor-arc control plausibly survives the residue-class insertion.

### What is genuinely new

The first genuinely new theorem is a **residue-class major-arc recombination theorem**:
after inserting

\[
1_{n\equiv a \,(\mathrm{mod}\, q)}
=
\frac1q \sum_{b \,(\mathrm{mod}\, q)} e((n-a)b/q),
\]

the proof must identify the full Fourier profile of the residue-class constants,
not just the untwisted mode.

This is the first clear proof-level bottleneck.

## What 396 Actually Needs Beyond Step 1

Even if the logarithmic theorem is proved, 396 still needs stronger output:

1. **Almost-all-scales upgrade** for the moving-cutoff family.
2. **De-exceptionalization to every large dyadic scale**, or at least a polylog-loss
   lower bound sufficient for infinitude.

So the bottleneck hierarchy is:

1. first new theorem: AP-localized logarithmic twin-smooth theorem;
2. true endgame bottleneck: every-scale dyadic lower bound.

## Honest Probability / Feasibility Read

- Not close to a full solution.
- Much closer to the real barrier than before.
- The current method is no longer wandering: it is now waiting on one concrete
  smooth-correlation theorem and its upgrades.

## Current Ranking of Routes

1. **Direct fixed-shift smooth-pair correlation (`n=1`)**
   - Live.
   - Most credible.

2. **Lift from `n=1` to the full parallel family**
   - Future work only if `n=1` succeeds.

3. **Absolute-value Fourier**
   - Closed.

4. **Large-prime overlap asymptotics via prime pairs**
   - Diagnostically useful, but not viable.

## Immediate Next Move

Work inside Teräväinen's major-arc argument with the residue-class insertion and
identify the constant-producing term:

- derive the mode-by-mode major-arc contribution,
- determine the candidate Fourier coefficients of `c_{a,q}`,
- and decide whether a uniform positive lower bound for `c_{a,q}` is available
  without first proving an exact factorization formula.

That is the next serious checkpoint.
