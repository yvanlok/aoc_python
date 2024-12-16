import time
from datetime import timedelta
import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N(0), E(1), S(2), W(3)


def valid_coordinate(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"


def main():
    with open("day_16/data.txt") as f:
        grid = [list(line.strip()) for line in f]

    # Find starting and ending positions
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                start = (row, col)
            elif grid[row][col] == "E":
                end = (row, col)

    heap = []
    heapq.heappush(heap, (0, start, 1))  # (score, coordinates, direction)
    visited = set()

    while heap:
        score, (curr_row, curr_col), curr_direction = heapq.heappop(heap)

        if ((curr_row, curr_col), curr_direction) in visited:
            continue
        visited.add(((curr_row, curr_col), curr_direction))

        if (curr_row, curr_col) == end:
            print(score)
            return

        for turn in [-1, 0, 1]:  # Turns of -90, 0, +90 degrees
            new_direction = (curr_direction + turn) % 4
            delta_row, delta_col = DIRECTIONS[new_direction]
            new_row = curr_row + delta_row
            new_col = curr_col + delta_col

            if valid_coordinate(grid, new_row, new_col):
                turn_cost = abs(turn) * 1000
                move_cost = 1  # Moving forward costs 1
                new_score = score + turn_cost + move_cost
                heapq.heappush(heap, (new_score, (new_row, new_col), new_direction))

    print("No path found")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
