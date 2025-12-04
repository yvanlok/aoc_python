"""
Advent of Code 2025 - Day 4 - Part 2
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    # Track rolls as a set for O(1) lookup
    rolls = set()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "@":
                rolls.add((y, x))

    result = 0
    changed = True

    while changed:
        changed = False
        to_remove = []

        for y, x in rolls:
            count = sum(1 for dy, dx in NEIGHBORS if (y + dy, x + dx) in rolls)
            if count < 4:
                to_remove.append((y, x))

        if to_remove:
            changed = True
            result += len(to_remove)
            for pos in to_remove:
                rolls.discard(pos)

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
