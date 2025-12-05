"""
Advent of Code 2025 - Day 5 - Part 2
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle by merging overlapping ranges and counting total IDs."""
    # Split input into sections (only need ranges for part 2)
    parts = [part.strip().split("\n") for part in data.split("\n\n")]

    ingredient_ranges = parts[0]

    ranges = []

    result = 0

    # Parse each range string into (lower, upper) tuples
    for ingredient_range in ingredient_ranges:
        lower, upper = ingredient_range.split("-")
        ranges.append((int(lower), int(upper)))

    # Sort by lower bound to enable merging adjacent/overlapping ranges
    ranges.sort()

    # Merge overlapping or adjacent ranges into non-overlapping intervals
    merged = []

    for lower, upper in ranges:
        # Check if current range overlaps or is adjacent to the last merged range
        if merged and lower <= merged[-1][1] + 1:
            # Extend the last merged range if current range reaches further
            merged[-1] = (merged[-1][0], max(merged[-1][1], upper))
        else:
            # No overlap - start a new merged range
            merged.append((lower, upper))

    # Sum up all unique IDs covered by the merged ranges
    result = sum(upper - lower + 1 for (lower, upper) in merged)

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
