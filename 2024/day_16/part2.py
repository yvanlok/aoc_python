import time
from datetime import timedelta
from collections import deque
import heapq

# Constants
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N(0), E(1), S(2), W(3)


def valid_coordinate(grid, row, col, height, width):
    return 0 <= row < height and 0 <= col < width and grid[row][col] != "#"


def main():
    with open("day_16/data.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    # Find starting and ending positions
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == "S":
                starting_coordinates = (row, col)
            elif grid[row][col] == "E":
                ending_coordinates = (row, col)

    q = []
    heapq.heappush(
        q, (0, starting_coordinates, 1, [starting_coordinates])
    )  # (score, coordinates, direction, tiles_visited)
    visited = {}
    scores = []

    while q:
        curr_score, (curr_row, curr_col), curr_direction, tiles_visited = heapq.heappop(
            q
        )

        state = ((curr_row, curr_col), curr_direction)

        # Check if this state has been reached with a lower score
        if state in visited:
            if curr_score > visited[state]:
                continue
            elif curr_score < visited[state]:
                visited[state] = curr_score
        else:
            visited[state] = curr_score

        if (curr_row, curr_col) == ending_coordinates:
            scores.append((curr_score, tiles_visited))
            continue  # No need to explore further from the end

        for turn in [-1, 0, 1]:  # Turns of -90, 0, +90 degrees
            new_direction = (curr_direction + turn) % 4
            delta_row, delta_col = DIRECTIONS[new_direction]
            new_row = curr_row + delta_row
            new_col = curr_col + delta_col

            if valid_coordinate(grid, new_row, new_col, HEIGHT, WIDTH):
                new_tiles_visited = tiles_visited + [(new_row, new_col)]
                score_modifier = abs(turn) * 1000 if turn != 0 else 0
                new_score = curr_score + score_modifier + 1  # Moving forward costs 1
                heapq.heappush(
                    q, (new_score, (new_row, new_col), new_direction, new_tiles_visited)
                )

    # Find the minimum score
    if scores:
        min_score = min(score for score, _ in scores)

        # Collect all tiles from paths with the minimum score
        best_tiles = set()
        for score, tiles in scores:
            if score == min_score:
                best_tiles.update(tiles)

        print(f"Number of tiles on any best path: {len(best_tiles)}")

    else:
        print("No path found")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
