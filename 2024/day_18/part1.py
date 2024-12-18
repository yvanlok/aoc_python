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
    q.append(((0, 0), 0))

    while q:
        current_coordinate, score = q.popleft()
        visited.add(current_coordinate)

        if current_coordinate == END_COORDINATES:
            return score

        c_row, c_col = current_coordinate

        for i in range(0, 4):
            n_row, n_col = c_row + dRow[i], c_col + dCol[i]

            if (
                0 <= n_row < HEIGHT
                and 0 <= n_col < WIDTH
                and (n_row, n_col) not in visited
                and grid[n_row][n_col] != "#"
            ):
                q.append(((n_row, n_col), score + 1))
                visited.add((n_row, n_col))


def main():
    grid = [["."] * WIDTH for _ in range(HEIGHT)]
    with open("day_18/data.txt") as f:
        for line in f.readlines()[:BYTES]:
            col, row = list(map(int, line.split(",")))
            grid[row][col] = "#"

    print(shortest_path(grid))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
