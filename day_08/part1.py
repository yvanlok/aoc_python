import time
from datetime import timedelta


def findAntennas(grid, height, width):

    coords = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != ".":
                coords.append((row, col))

    return coords


def main():

    # use set to remove duplicates
    antinode_coords = set()
    with open("day_08/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    coords = findAntennas(grid, HEIGHT, WIDTH)

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            if (
                coords[i] != coords[j]
                and grid[coords[i][0]][coords[i][1]] == grid[coords[j][0]][coords[j][1]]
            ):
                diff_row, diff_col = (
                    coords[i][0] - coords[j][0],
                    coords[i][1] - coords[j][1],
                )

                new_row1, new_col1 = coords[i][0] + diff_row, coords[i][1] + diff_col
                new_row2, new_col2 = coords[j][0] - diff_row, coords[j][1] - diff_col

                if 0 <= new_row1 < HEIGHT and 0 <= new_col1 < WIDTH:
                    antinode_coords.add((new_row1, new_col1))
                if 0 <= new_row2 < HEIGHT and 0 <= new_col2 < WIDTH:
                    antinode_coords.add((new_row2, new_col2))

            else:
                pass

    print("Antinode coordinates:", len(antinode_coords))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
