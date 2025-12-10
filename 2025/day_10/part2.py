"""
Advent of Code 2025 - Day 10 - Part 2
"""

from time import perf_counter
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    result = 0

    for line in lines:

        parts = line.split()
        wiring_strs = parts[1:-1]
        joltage_str = parts[-1]

        wiring = []

        # Parse wiring as list of lists of integers
        for button in wiring_strs:
            button_indices = [int(x) for x in button[1:-1].split(",")]
            wiring.append(button_indices)

        # Parse joltages
        target = [int(x) for x in joltage_str[1:-1].split(",")]

        result += solve_lp(wiring, target)

    return result


def solve_lp(wiring, target):
    num_buttons = len(wiring)
    num_counters = len(target)

    # np matrix with column for each button, and row showing which counter it affects
    A = np.zeros((num_counters, num_buttons))

    for btn_idx, affected_counters in enumerate(wiring):
        for counter_idx in affected_counters:
            A[counter_idx, btn_idx] = 1

    # each button costs 1 - want to minimise
    c = np.ones(num_buttons)

    # sum of counters must be same as joltages
    constraints = LinearConstraint(A, target, target)

    # result must be positive
    bounds = Bounds(lb=0, ub=np.inf)

    # solve using scipy.milp
    result = milp(
        c, constraints=constraints, bounds=bounds, integrality=np.ones(num_buttons)
    )

    if result.success:
        return int(round(result.fun))
    else:
        return None


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
