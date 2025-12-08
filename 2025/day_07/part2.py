"""
Advent of Code 2025 - Day 7 - Part 2
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
    SPLITTER = "^"

    # Dictionary: {column: number_of_beams_at_that_column}
    beams = {lines[0].index(START): 1}

    splits = 0

    for row in lines[1:]:
        if SPLITTER not in row:
            continue  # Skip rows with no splitters

        # Snapshot the current beam state before modifying
        current_beams = list(beams.items())

        for col, count in current_beams:
            if row[col] == SPLITTER:
                splits += count  # Each beam at this position causes a split

                # Remove the beam from this column
                beams.pop(col)

                # Add beams to left and right
                beams[col - 1] = beams.get(col - 1, 0) + count
                beams[col + 1] = beams.get(col + 1, 0) + count

    return sum(beams.values())


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
