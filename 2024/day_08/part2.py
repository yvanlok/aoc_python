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

    # get data
    with open("day_08/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    coords = findAntennas(grid, HEIGHT, WIDTH)

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            # check they aren't the same coordinate and they are the same antenna
            if (
                coords[i] != coords[j]
                and grid[coords[i][0]][coords[i][1]] == grid[coords[j][0]][coords[j][1]]
            ):

                # find gradient
                diff_row, diff_col = (
                    coords[i][0] - coords[j][0],
                    coords[i][1] - coords[j][1],
                )

                previous_1, previous_2 = coords[i], coords[j]

                # add current coordinates
                antinode_coords.add(previous_1)
                antinode_coords.add(previous_2)

                while True:
                    new_row1, new_col1 = (
                        previous_1[0] + diff_row,
                        previous_1[1] + diff_col,
                    )
                    new_row2, new_col2 = (
                        previous_2[0] - diff_row,
                        previous_2[1] - diff_col,
                    )

                    # infinite loop until both out of bounds
                    invalid_1 = False
                    invalid_2 = False

                    if 0 <= new_row1 < HEIGHT and 0 <= new_col1 < WIDTH:
                        previous_1 = (new_row1, new_col1)
                        antinode_coords.add(previous_1)
                    else:
                        invalid_1 = True
                    if 0 <= new_row2 < HEIGHT and 0 <= new_col2 < WIDTH:
                        previous_2 = (new_row2, new_col2)
                        antinode_coords.add(previous_2)
                    else:
                        invalid_2 = True

                    if invalid_1 and invalid_2:
                        break

            else:
                pass

    print("Antinode coordinates:", len(antinode_coords))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
