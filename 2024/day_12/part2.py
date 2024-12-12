import time
from datetime import timedelta
from collections import deque as queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def find_region_and_calculate(row, col, visited, grid):
    region_type = grid[row][col]
    region = set()

    # Collect region using BFS
    q = queue()
    q.append((row, col))
    visited.add((row, col))
    region.add((row, col))

    while q:
        current_row, current_col = q.popleft()
        for i in range(4):
            next_row = current_row + dRow[i]
            next_col = current_col + dCol[i]

            if (
                next_row < 0
                or next_col < 0
                or next_row >= len(grid)
                or next_col >= len(grid[0])
                or grid[next_row][next_col] != region_type
            ):
                continue
            elif (next_row, next_col) not in visited:
                q.append((next_row, next_col))
                visited.add((next_row, next_col))
                region.add((next_row, next_col))

    # Count corners
    area = len(region)
    seen = set()
    corners = 0

    for row, col in region:
        # Check each corner of the cell
        for dx, dy in [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]:
            corner = (row + dx, col + dy)
            if corner in seen:
                continue
            seen.add(corner)

            # Count adjacent cells that are part of the region
            adjacent = sum(
                (corner[0] + r, corner[1] + c) in region
                for r, c in [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]
            )

            if adjacent in (1, 3):
                corners += 1
            elif adjacent == 2:
                # Check if diagonal pattern
                pattern = [
                    (corner[0] - 0.5, corner[1] - 0.5) in region,
                    (corner[0] + 0.5, corner[1] + 0.5) in region,
                ]
                if pattern == [True, True] or pattern == [False, False]:
                    corners += 2

    return area, corners


def main():
    visited = set()
    total = 0

    with open("day_12/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited:
                area, corners = find_region_and_calculate(row, col, visited, grid)
                total += area * corners

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
