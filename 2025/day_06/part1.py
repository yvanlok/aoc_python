"""
Advent of Code 2025 - Day 6 - Part 1
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

    result = 0

    numbers = []

    operations = lines[-1].split()

    for line in lines[:-1]:
        numbers.append([int(num) for num in line.split()])

    for idx in range(0, len(operations)):
        if operations[idx] == "*":
            result += math.prod([row[idx] for row in numbers])
        else:
            result += sum([row[idx] for row in numbers])

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
