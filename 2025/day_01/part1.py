"""
Advent of Code 2025 - Day 1 - Part 1
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
    num = 50

    for line in lines:
        direction = line[0]
        magnitude = int(line[1::])
        if direction == "L":
            num -= magnitude
        else:
            num += magnitude

        num = abs(num % 100)

        if num == 0:
            result += 1

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
