import time
from datetime import timedelta
from collections import deque as queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def find_region_and_calculate(row, col, visited, grid):
    region_type = grid[row][col]
    area = 0
    perimeter = 0

    q = queue()
    q.append((row, col))
    visited.add((row, col))

    while q:
        current_row, current_col = q.popleft()
        area += 1

        for i in range(4):
            next_row = current_row + dRow[i]
            next_col = current_col + dCol[i]

            # Check if the neighboring cell is out of bounds or not part of the region
            if (
                next_row < 0
                or next_col < 0
                or next_row >= len(grid)
                or next_col >= len(grid[0])
                or grid[next_row][next_col] != region_type
            ):
                perimeter += 1
            elif (next_row, next_col) not in visited:
                q.append((next_row, next_col))
                visited.add((next_row, next_col))

    return area, perimeter


def main():
    visited = set()
    total = 0

    with open("day_12/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited:
                area, perimeter = find_region_and_calculate(row, col, visited, grid)
                total += area * perimeter

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
