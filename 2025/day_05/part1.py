"""
Advent of Code 2025 - Day 5 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    # Split input into two sections: ranges and ingredient IDs
    parts = [part.strip().split("\n") for part in data.split("\n\n")]

    ingredient_ranges = parts[0]
    ingredient_ids = parts[1]

    # Store ranges as (lower, upper) tuples for range checking
    allowed_ranges = set()

    result = 0

    # Parse each range string into a tuple of integers
    for ingredient_range in ingredient_ranges:
        ids = ingredient_range.split("-")
        allowed_ranges.add((int(ids[0]), int(ids[1])))

    # Count how many ingredient IDs fall within any allowed range
    for ingredient_id in ingredient_ids:
        if any(lower <= int(ingredient_id) <= upper for lower, upper in allowed_ranges):
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
