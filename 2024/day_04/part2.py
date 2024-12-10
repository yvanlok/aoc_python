import time
from datetime import timedelta

from itertools import chain


def main():

    with open("day_04/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    height = len(grid)
    width = len(grid[0])
    valid_permutations = ["MAS", "SAM"]
    count = 0

    for row in range(height - 2):
        for col in range(width - 2):

            diag_1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diag_2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]

            if diag_1 in valid_permutations and diag_2 in valid_permutations:
                count += 1

    print(count)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
