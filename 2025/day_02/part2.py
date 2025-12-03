"""
Advent of Code 2025 - Day 2 - Part 1
"""

from time import perf_counter
from textwrap import wrap


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    num_ranges = data.split(",")
    result = 0
    for num_range in num_ranges:
        start, end = num_range.split("-")

        for num in range(int(start), int(end) + 1):
            num = str(num)

            for repeats in range(2, len(num) + 1):

                split_position = len(num) // repeats
                if len(num) % repeats == 0:
                    parts = wrap(num, split_position)
                    # check all parts are equal:
                    if len(set(parts)) == 1:
                        result += int(num)
                        break

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
