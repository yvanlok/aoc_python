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
        combination = []

        start = 0

        for remaining in range(12, 0, -1):
            end = len(batteries) - remaining + 1

            best_idx = start

            for i in range(start, end):
                if batteries[i] > batteries[best_idx]:
                    best_idx = i

            combination.append(batteries[best_idx])

            start = best_idx + 1

        result += int("".join(combination))

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
