"""
Advent of Code 2025 - Day 11 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    # TODO: Implement solution
    result = None

    return result


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {{result}}")
    print(f"Time: {{elapsed:.6f}} seconds")


if __name__ == "__main__":
    main()
