"""
Advent of Code 2025 - Day 7 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    START = "S"
    EMPTY = "."
    BEAM = "|"
    SPLITTER = "^"

    grid = [list(line.replace(START, BEAM)) for line in lines]

    result = 0

    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if grid[row_idx][col_idx] == BEAM:
                if row_idx + 1 < len(grid):
                    if grid[row_idx + 1][col_idx] == SPLITTER:
                        result += 1
                        grid[row_idx + 1][col_idx - 1] = BEAM
                        grid[row_idx + 1][col_idx + 1] = BEAM
                    elif grid[row_idx + 1][col_idx] == EMPTY:
                        grid[row_idx + 1][col_idx] = BEAM

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
