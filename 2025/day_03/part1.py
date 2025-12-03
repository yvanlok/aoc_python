"""
Advent of Code 2025 - Day 3 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    result = 0

    for batteries in lines:

        # compute max value (exclude last element) and first index where it occurs
        max_val = max(batteries[:-1])  # don't count last digit
        first_idx = batteries.index(max_val)

        optimal_combination = int(max_val + max(batteries[first_idx + 1 :]))

        result += optimal_combination

    return result


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
