"""
Advent of Code 2025 - Day 9 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    tile_locations = [tuple(map(int, tile.split(","))) for tile in lines]

    max_area = 0

    for i in range(len(tile_locations)):
        for j in range(i, len(tile_locations)):
            x_distance = abs(tile_locations[i][0] - tile_locations[j][0]) + 1
            y_distance = abs(tile_locations[i][1] - tile_locations[j][1]) + 1

            max_area = max(max_area, x_distance * y_distance)

    result = max_area

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
