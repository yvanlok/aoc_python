"""
Advent of Code 2025 - Day 4 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def adjacent_rolls(grid, y, x):

    count = 0

    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if j == y and i == x:
                continue
            if 0 <= j < len(grid) and 0 <= i < len(grid[0]):
                if grid[j][i] == "@":
                    count += 1
    return count


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")
    grid = [list(line) for line in lines]

    result = 0

    finished = False

    while not finished:
        to_remove = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "@":
                    rolls = adjacent_rolls(grid, y, x)
                    if rolls < 4:
                        result += 1
                        to_remove.append((y, x))
        if to_remove:
            for y, x in to_remove:
                grid[y][x] = "X"
        else:
            finished = True

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
