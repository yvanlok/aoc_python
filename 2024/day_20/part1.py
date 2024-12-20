import time
from datetime import timedelta
from collections import deque

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def find_path(grid):
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == "S":
                start = (row, col)
            elif grid[row][col] == "E":
                end = (row, col)

    visited = set()
    q = deque()
    q.append((start, [start]))

    while q:
        curr_coordinates, path = q.popleft()
        c_row, c_col = curr_coordinates

        if curr_coordinates == end:
            return path
        else:
            for i in range(4):
                n_row, n_col = c_row + dRow[i], c_col + dCol[i]

                if (
                    0 <= n_row < HEIGHT
                    and 0 <= n_col < WIDTH
                    and (n_row, n_col) not in visited
                    and grid[n_row][n_col] != "#"
                ):
                    q.append(((n_row, n_col), path + [(n_row, n_col)]))
                    visited.add((n_row, n_col))

    return None  # Return None if no path is found


def main():
    with open("day_20/data.txt") as f:
        grid = [list(line.strip()) for line in f]

    path = find_path(grid)
    print(len(path))

    num_cheats = 0
    for idx, pos in enumerate(path):
        for i in range(4):
            n_row, n_col = pos[0] + dRow[i], pos[1] + dCol[i]

            if (
                0 <= n_row < len(grid)
                and 0 <= n_col < len(grid[0])
                and grid[n_row][n_col] == "#"
            ):
                n_row, n_col = n_row + dRow[i], n_col + dCol[i]
                if (
                    0 <= n_row < len(grid)
                    and 0 <= n_col < len(grid[0])
                    and grid[n_row][n_col] != "#"
                    and (n_row, n_col) in path
                ):
                    index = path.index((n_row, n_col))
                    if index - idx - 2 >= 100:
                        num_cheats += 1
    print(num_cheats)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
