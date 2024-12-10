import time
from datetime import timedelta
from collections import deque as queue

# Direction vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def isValid(row, col, expected_value, grid):
    # If cell lies out of bounds
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False

    # If cell is already visited or does not match the expected value
    if grid[row][col] != expected_value:
        return False

    return True


# Function to perform the BFS traversal
def BFS(grid, start_row, start_col):
    # Stores indices of the matrix cells
    q = queue()

    # Mark the starting cell as visited and push it into the queue
    q.append((start_row, start_col, 0))  # (row, col, current_value)

    score = 0

    # Iterate while the queue is not empty
    while q:
        x, y, current_value = q.popleft()

        # If we reached the value 9, increment the score
        if current_value == 9:
            score += 1
            continue

        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(adjx, adjy, current_value + 1, grid):
                q.append((adjx, adjy, current_value + 1))

    return score


def findTrailHeads(grid):
    trailHeads = list()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                trailHeads.append((row, col))
    return trailHeads


def main():
    with open("day_10/data.txt") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    trailHeads = findTrailHeads(grid)
    final_score = 0

    for trailHead in trailHeads:
        final_score += BFS(grid, trailHead[0], trailHead[1])
    print(final_score)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
