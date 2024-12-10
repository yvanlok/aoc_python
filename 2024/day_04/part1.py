import time
from datetime import timedelta

from itertools import chain


# SLIGHT CHEATING THANKS CHATGPT
def extract_all_lines(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Extract horizontal lines (rows)
    horizontal = ["".join(row) for row in grid]

    # Extract vertical lines (columns)
    vertical = ["".join(grid[row][col] for row in range(rows)) for col in range(cols)]

    # Extract diagonal lines (top-left to bottom-right)
    diagonals_lr = []
    for d in range(-rows + 1, cols):  # Diagonals with variable starting points
        diagonals_lr.append(
            "".join(
                grid[r][c]
                for r, c in zip(range(rows), range(d, d + rows))
                if 0 <= c < cols
            )
        )

    # Extract diagonal lines (top-right to bottom-left)
    diagonals_rl = []
    for d in range(cols + rows - 1):
        diagonals_rl.append(
            "".join(
                grid[r][c]
                for r, c in zip(range(rows), range(d, d - rows, -1))
                if 0 <= c < cols
            )
        )

    # Combine all permutations
    all_lines = list(chain(horizontal, vertical, diagonals_lr, diagonals_rl))
    return all_lines


def main():

    with open("day_04/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    all_permutations = extract_all_lines(grid)

    total = sum(
        permutation.count("XMAS") + permutation.count("SAMX")
        for permutation in all_permutations
    )
    print(f"Total count: {total}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
