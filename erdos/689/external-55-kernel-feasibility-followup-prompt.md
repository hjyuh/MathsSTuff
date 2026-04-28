# Prompt for 5.5 Pro: prove or kill the kernel feasibility certificate

Created: 2026-04-25

We are working on Erdos Problem 689.  The current route is the robust
prime-difference / averaged GTZ / Kahn rounding route.

Please do not re-derive the whole framework.  Focus on the remaining
deterministic certificate.

## Current theorem stack

The route is:

\[
\text{finite-core kernel feasibility}
\Rightarrow
\text{GTZ first/second moments}
\Rightarrow
\text{large Kahn-eligible fractional matching}
\Rightarrow
\text{matching of almost all robust labels}
\Rightarrow
\text{pair-plus-singleton cleanup}
\Rightarrow
\text{EP689}.
\]

We are trying to prove the first implication's hypothesis: finite-core kernel
feasibility.

## Fixed robust setup

Use the parity-first baseline \(a_2\equiv 1\pmod 2\).  Choose a large fixed
set
\[
  S\subset\{7,11,13,\ldots\}
\]
and nonzero residues \(b_s\pmod s\).  Keep \(3\) at \(0\pmod 3\).  Let
\[
  W=\prod_{s\in S}s,
  \qquad
  H_S(x)=\#\{s\in S:x\equiv b_s\pmod s\}.
\]

A cleanup prime \(P>n/5\) is robust if
\[
  H_S(P)\ge 1,\qquad H_S(2P)\ge 2,\qquad H_S(4P)\ge 2.
\]
Robustness is a fixed condition \(P\bmod W\in\mathcal B\), with robust density
\[
  \delta_S=|\mathcal B|/\varphi(W).
\]
Assume \(S\) has been chosen so \(\delta_S>10/11\).

For
\[
  \beta\in(\delta_S^{-1}-3/5,\ 1/2),
\]
let
\[
  \mathcal R_\beta(n)=
  \{P\in(n/5,\beta n]:P\bmod W\in\mathcal B\}.
\]

The pair matching uses residual targets
\[
  A_1(n)=\{x\in A_S(n):v_2(x)=1\},
  \qquad
  A_2(n)=\{x\in A_S(n):v_2(x)\ge2\},
\]
with edges
\[
  x\in A_1(n),\quad y\in A_2(n),\quad |y-x|=2P,
  \qquad P\in\mathcal R_\beta(n).
\]

Matching almost all labels \(P\in\mathcal R_\beta(n)\) gives the required
pair-plus-singleton cleanup.

## The deterministic kernel lemma

Truncate the residual coefficient set to finite cores:
\[
  x=2a q,\qquad y=2bq',
\]
where \(a\in\mathcal C_1\) is odd, \(b\in\mathcal C_2\) is even, and
\(\gcd(a,b)=1\).

For a type
\[
  \tau=(a,r,b,r',\sigma,\pi),
\]
where
\[
  q\equiv r\pmod W,\quad q'\equiv r'\pmod W,\quad
  \pi\equiv \sigma(br'-ar)\pmod W,\quad \pi\in\mathcal B,
\]
define the polygon
\[
  \Omega_\tau=
  \{(u,v):0<u\le 1/(2a),\ 0<v\le 1/(2b),\
  1/5<\sigma(bv-au)\le \beta\}.
\]

We need bounded nonnegative kernels \(g_\tau\) on these polygons such that:

\[
  L_Z(\pi,t)=1
\]
for almost every \((\pi,t)\in\mathcal B\times(1/5,\beta]\), while
\[
  L_X(a,r,u)\le 1-2\gamma,\qquad
  L_Y(b,r',v)\le 1-2\gamma
\]
for some fixed \(\gamma>0\).

The explicit load equations are:

\[
  L_Z(\pi,t)=
  \sum_{\tau:\pi_\tau=\pi}
    {\kappa_\tau\over b_\tau}
    \int_{J_\tau(t)}
      g_\tau\!\left(u,{a_\tau u+\sigma_\tau t\over b_\tau}\right)\,du,
\]

\[
  L_X(a,r,u)=
  \sum_{\tau:a_\tau=a,\ r_\tau=r}
    \kappa_\tau\int_{V_\tau(u)}g_\tau(u,v)\,dv,
\]

\[
  L_Y(b,r',v)=
  \sum_{\tau:b_\tau=b,\ r'_\tau=r'}
    \kappa_\tau\int_{U_\tau(v)}g_\tau(u,v)\,du.
\]

Here \(\kappa_\tau>0\) is the fixed local GTZ density/singular-series factor
for the type, and obstructed types are discarded.

## Subagent findings to use

1. Kahn bridge:
   The averaged-nibble theorem should be stated as preprocessing to produce a
   Kahn-eligible fractional matching \(t_e\), not as a separate black box.
   It is enough to obtain:
   \[
     \sum_{e\ni v}t_e\le1,\qquad
     \sum_e t_e=(1-o(1))|Z|,\qquad
     \max_e t_e=o(1),
   \]
   because the hypergraph is linear, so pair co-loads are \(o(1)\), and
   Kahn rounds the fractional matching.

2. GTZ side:
   Assuming bounded feasible kernels, the first and second moments needed for
   the averaged route are finite-complexity GTZ systems:
   - edge totals: 2 variables, 3 forms \(q,q',\sigma(bq'-aq)\);
   - label second moments: 3 variables, 5 forms after parametrizing common \(P\);
   - side second moments: 3 variables, 5 forms.
   This avoids pointwise Hardy--Littlewood prime-pair estimates.

3. Skeptic pass:
   The likely failure modes are Hall-type cuts:
   - vanishing label intensity for some robust class \(\pi\);
   - residue reachability gaps for \(\pi\in\mathcal B\);
   - high-\(t\) bottleneck near \(\beta\);
   - coefficient-core bottlenecks from \(\gcd(a,b)=1\);
   - joint \(X,Y\) coupling cuts not visible from one-sided capacity checks.

4. Toy LP:
   A residue-free discretized model in the threshold-like case
   \[
     \beta=0.49,\qquad \rho=0.92
   \]
   failed badly for the one-pair core \((a,b)=(1,2)\), but richer cores
   succeeded with positive greedy slack:

   | core | greedy slack \(\gamma\) |
   |---|---:|
   | `{1,3}` by `{2,4}` | `0.04` |
   | `{1,3,5}` by `{2,4,6}` | `0.22` |
   | `{1,3,5,7}` by `{2,4,6,8}` | `0.30` |

   This is not proof, but it suggests endpoint geometry alone is not killing
   the kernel lemma once multiple coefficient types are available.

## What I need from you

Please attack the deterministic kernel-feasibility problem directly.

Deliver one of the following:

1. **A proof of feasibility.**
   Give a finite core, explicit kernels or entropic/dual potentials, and a
   quantified side slack \(\gamma>0\).  The proof must handle robust residue
   classes \(\pi\), not just the residue-free geometry.

2. **A compact Hall theorem plus verified hypotheses.**
   State the exact continuum or finite LP Hall condition and prove that the
   robust residue/coefficient model satisfies it.  In particular, check
   per-\(\pi\) reachability and the high-\(t\) endpoint.

3. **A probabilistic choice of \(S\) and residues \(b_s\) that makes the finite
   residue graph quasirandom enough.**
   If explicit residues are too hard, show that for a random fixed large \(S\)
   and random nonzero \(b_s\), with positive probability the robust set
   \(\mathcal B\) and residual residue sets have the expansion needed for the
   kernel LP.

4. **A genuine obstruction.**
   If the lemma is false as stated, identify the exact Hall cut or residue
   bottleneck and say how the EP689 route should be modified.

Please be precise about which parts are unconditional and which are only
heuristic.  The most valuable output is an exact theorem statement that, if
proved, would finish the current route to EP689.
