"""
Finite Z/8 spectral feasibility tests for Erdős Problem #38.

This script treats the residue-pattern bottleneck as a positive-definite
class-function problem on Z/8.  The scalar model is solved exactly enough by
active-set enumeration because the LP is only 6-dimensional:

    x = (w0, w1, w2, w3, w4, eta)

where wj >= 0, sum wj = 1, and

    rho(r) = w0
           + w1 cos(pi r/4)
           + w2 cos(pi r/2)
           + w3 cos(3 pi r/4)
           + w4 cos(pi r).

The main model tested here is:
    rho(1), rho(2), rho(4) >= eta
    rho(3) <= -eta

which is the cleanest scalar "odd + even" mod-8 feasibility test.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

import numpy as np
import sympy as sp


SQRT2 = math.sqrt(2.0)
S = 1.0 / SQRT2
TOL = 1e-9


@dataclass(frozen=True)
class LPResult:
    name: str
    eta: float
    weights: tuple[float, float, float, float, float]

    @property
    def delta(self) -> float:
        return (1.0 - self.eta) / 4.0


def rho_coeffs(r: int) -> np.ndarray:
    if r % 8 == 1:
        return np.array([1.0, S, 0.0, -S, -1.0])
    if r % 8 == 2:
        return np.array([1.0, 0.0, -1.0, 0.0, 1.0])
    if r % 8 == 3:
        return np.array([1.0, -S, 0.0, S, -1.0])
    if r % 8 == 4:
        return np.array([1.0, -1.0, 1.0, -1.0, 1.0])
    raise ValueError(f"Unsupported residue {r}")


def make_constraints(model: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    eq_a = np.array([[1.0, 1.0, 1.0, 1.0, 1.0, 0.0]])
    eq_b = np.array([1.0])

    ineq_a: list[np.ndarray] = []
    ineq_b: list[float] = []

    # Nonnegativity for weights and eta.
    for i in range(5):
        row = np.zeros(6)
        row[i] = -1.0
        ineq_a.append(row)
        ineq_b.append(0.0)
    row = np.zeros(6)
    row[5] = -1.0
    ineq_a.append(row)
    ineq_b.append(0.0)

    def add_rho_ge(r: int) -> None:
        row = np.zeros(6)
        row[:5] = -rho_coeffs(r)
        row[5] = 1.0
        ineq_a.append(row)
        ineq_b.append(0.0)

    def add_rho_le_neg_eta(r: int) -> None:
        row = np.zeros(6)
        row[:5] = rho_coeffs(r)
        row[5] = 1.0
        ineq_a.append(row)
        ineq_b.append(0.0)

    if model == "odd_only":
        add_rho_ge(1)
        add_rho_le_neg_eta(3)
    elif model == "odd_even_full":
        add_rho_ge(1)
        add_rho_ge(2)
        add_rho_ge(4)
        add_rho_le_neg_eta(3)
    elif model == "odd_even_no_r4":
        add_rho_ge(1)
        add_rho_ge(2)
        add_rho_le_neg_eta(3)
    else:
        raise ValueError(f"Unknown model {model}")

    return eq_a, eq_b, np.array(ineq_a), np.array(ineq_b)


def solve_lp(model: str) -> LPResult:
    eq_a, eq_b, ineq_a, ineq_b = make_constraints(model)
    n_vars = 6
    need = n_vars - len(eq_b)

    best_eta = -1.0
    best_x: np.ndarray | None = None

    for active in itertools.combinations(range(len(ineq_b)), need):
        a = np.vstack([eq_a, ineq_a[list(active)]])
        b = np.concatenate([eq_b, ineq_b[list(active)]])
        if np.linalg.matrix_rank(a) < n_vars:
            continue
        try:
            x = np.linalg.solve(a, b)
        except np.linalg.LinAlgError:
            continue
        if np.max(eq_a @ x - eq_b) > TOL or np.max(eq_b - eq_a @ x) > TOL:
            continue
        if np.max(ineq_a @ x - ineq_b) > TOL:
            continue
        eta = float(x[5])
        if eta > best_eta + 1e-8:
            best_eta = eta
            best_x = x

    if best_x is None:
        raise RuntimeError(f"No feasible solution found for {model}")

    weights = tuple(float(v) for v in best_x[:5])
    return LPResult(name=model, eta=float(best_x[5]), weights=weights)


def fmt_exact(value: float) -> str:
    return str(sp.nsimplify(value, [sp.sqrt(2)]))


def report(result: LPResult) -> None:
    names = ["w0", "w1", "w2", "w3", "w4"]
    print(f"MODEL {result.name}")
    print(f"  eta*   = {result.eta:.12f}  = {fmt_exact(result.eta)}")
    print(f"  delta* = {result.delta:.12f}  = {fmt_exact(result.delta)}")
    for name, value in zip(names, result.weights):
        print(f"  {name:<4} = {value:.12f}  = {fmt_exact(value)}")
    print()


def print_matrix_witness(target_eta: float = 1.0 / 3.0) -> None:
    print("2x2 MATRIX WITNESS (block-diagonal concentrated model)")
    print(f"  target eta = {target_eta:.12f} = {fmt_exact(target_eta)}")
    print("  Frequency matrices:")
    print("    M_1 = M_7 = (1/2) * [[1, 0], [0, 0]]")
    print("    M_4         =       [[0, 0], [0, 1]]")
    print("    all others  =       [[0, 0], [0, 0]]")
    print("  Resulting diagonal class functions:")
    print("    rho_OO(r) = cos(pi r / 4)")
    print("    rho_EE(r) = (-1)^r")
    print("    rho_OE(r) = 0")
    print("  Checks:")
    print(f"    rho_OO(1)=+1/sqrt(2), rho_OO(3)=-1/sqrt(2), so odd-family margin is {fmt_exact(1/SQRT2)}")
    print("    rho_EE(2)=rho_EE(4)=rho_EE(6)=1, so even-family margin is 1")
    print("    Therefore every target eta <= 1/sqrt(2) is feasible in the uncoupled 2x2 model.")
    print()


def main() -> None:
    for model in ("odd_only", "odd_even_full", "odd_even_no_r4"):
        report(solve_lp(model))
    print_matrix_witness()


if __name__ == "__main__":
    main()
