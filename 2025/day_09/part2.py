"""
Advent of Code 2025 - Day 9 - Part 2
"""

from time import perf_counter
from shapely.geometry import Polygon


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")
    red_tiles = [tuple(map(int, tile.split(","))) for tile in lines]

    # Create polygon from red tiles
    polygon = Polygon(red_tiles)

    max_area = 0

    # Check all pairs of red tiles
    for i, (col_i, row_i) in enumerate(red_tiles):
        for col_j, row_j in red_tiles[i + 1 :]:
            # Create rectangle polygon
            min_col = min(col_i, col_j)
            max_col = max(col_i, col_j)
            min_row = min(row_i, row_j)
            max_row = max(row_i, row_j)

            rectangle = Polygon(
                [
                    (min_col, min_row),
                    (max_col, min_row),
                    (max_col, max_row),
                    (min_col, max_row),
                ]
            )

            # Check if rectangle is fully contained in the polygon
            if polygon.contains(rectangle):
                area = (max_col - min_col + 1) * (max_row - min_row + 1)
                max_area = max(max_area, area)

    return max_area


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
