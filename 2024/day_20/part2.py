import time
from datetime import timedelta
from collections import deque

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


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
    cheat_count = 0
    for i, pos_start in enumerate(path):
        # Only look at positions 100+ steps ahead
        for j, pos_end in enumerate(path[i + 100 :], start=100):
            dist = manhattan_distance(pos_start, pos_end)
            # Only consider positions reachable within 20 steps
            if dist <= 20:
                steps_saved = j - dist
                if steps_saved >= 100:
                    cheat_count += 1

    print(cheat_count)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
