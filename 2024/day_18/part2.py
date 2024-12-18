import time
from datetime import timedelta
from collections import deque as queue


# actual values
WIDTH, HEIGHT, BYTES = 71, 71, 1024

# test values
# WIDTH, HEIGHT, BYTES = 7, 7, 12

END_COORDINATES = (WIDTH - 1, HEIGHT - 1)


dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def shortest_path(grid):

    visited = set()
    q = queue()
    q.append((0, 0))

    while q:
        current_coordinate = q.popleft()
        visited.add(current_coordinate)

        if current_coordinate == END_COORDINATES:
            return True

        c_row, c_col = current_coordinate

        for i in range(0, 4):
            n_row, n_col = c_row + dRow[i], c_col + dCol[i]

            if (
                0 <= n_row < HEIGHT
                and 0 <= n_col < WIDTH
                and (n_row, n_col) not in visited
                and grid[n_row][n_col] != "#"
            ):
                q.append((n_row, n_col))
                visited.add((n_row, n_col))
    return False


def main():
    grid = [["."] * WIDTH for _ in range(HEIGHT)]
    with open("day_18/data.txt") as f:

        coordinates = [list(map(int, line.split(","))) for line in f.readlines()]

    for col, row in coordinates[:BYTES]:
        grid[row][col] = "#"
    for col, row in coordinates[BYTES:]:
        grid[row][col] = "#"
        if not shortest_path(grid):
            print(f"{col},{row}")
            break


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
