"""
Advent of Code 2025 - Day 6 - Part 2
"""

from time import perf_counter
import math


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")
    grid = lines[:-1]
    ops_line = lines[-1]

    max_len = max(len(line) for line in lines)

    # Find indices where operators occur
    op_indices = [i for i, char in enumerate(ops_line) if char in "*+"]

    # Add the end of the line as the final boundary
    boundaries = op_indices + [max_len]

    result = 0

    for i in range(len(op_indices)):
        # start and end indices for current boundary
        start = boundaries[i]
        end = boundaries[i + 1]

        # current operator
        op = ops_line[start]

        nums = []

        # Iterate over columns within the boundaries
        for col in range(start, end):
            # Extract column characters
            col_chars = [line[col] for line in grid]
            # Join and strip to form number string
            num_str = "".join(col_chars).strip()

            if num_str:
                nums.append(int(num_str))

        if op == "*":
            val = math.prod(nums)
        else:
            val = sum(nums)

        result += val

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
