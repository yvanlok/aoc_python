import time
from datetime import timedelta

# Constants
WALL = "#"
ROBOT = "@"
BOX = "O"
EMPTY = "."

DIRECTIONS = {
    "^": {"name": "up", "translation": (-1, 0)},
    "v": {"name": "down", "translation": (1, 0)},
    "<": {"name": "left", "translation": (0, -1)},
    ">": {"name": "right", "translation": (0, 1)},
}


def find_positions(grid, item):
    positions = []
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == item:
                positions.append((row_index, col_index))
    return positions


def shift_boxes_vertically(grid, start_row, col, delta_row):
    row = start_row
    # Move to the end of the box chain
    while grid[row][col] == BOX:
        row += delta_row
    if grid[row][col] == EMPTY:
        # Shift boxes
        current_row = row - delta_row
        while current_row != start_row - delta_row:
            grid[current_row + delta_row][col] = BOX
            current_row -= delta_row
        grid[start_row][col] = EMPTY
        return True
    elif grid[row][col] == WALL:
        return False
    return False


def shift_boxes_horizontally(grid, row, start_col, delta_col):
    col = start_col
    # Move to the end of the box chain
    while grid[row][col] == BOX:
        col += delta_col
    if grid[row][col] == EMPTY:
        # Shift boxes
        current_col = col - delta_col
        while current_col != start_col - delta_col:
            grid[row][current_col + delta_col] = BOX
            current_col -= delta_col
        grid[row][start_col] = EMPTY
        return True
    elif grid[row][col] == WALL:
        return False
    return False


def main():
    # Read the input data
    with open("day_15/data.txt") as f:
        content = f.read().strip()
        grid_str, steps = content.split("\n\n")
        grid = [list(line.strip()) for line in grid_str.split("\n")]
        steps = steps.replace("\n", "")

    # Find the robot's starting position
    robot_pos = find_positions(grid, ROBOT)[0]

    # Process each movement step
    for step in steps:
        delta_row, delta_col = DIRECTIONS[step]["translation"]
        row, col = robot_pos
        new_row, new_col = row + delta_row, col + delta_col

        if grid[new_row][new_col] == WALL:
            continue
        elif grid[new_row][new_col] == BOX:
            # Attempt to shift boxes
            moved = False
            if delta_row != 0:
                moved = shift_boxes_vertically(grid, new_row, new_col, delta_row)
            else:
                moved = shift_boxes_horizontally(grid, new_row, new_col, delta_col)
            if not moved:
                continue
            # Move the robot
            grid[row][col] = EMPTY
            grid[new_row][new_col] = ROBOT
            robot_pos = (new_row, new_col)
        else:
            # Move the robot
            grid[row][col] = EMPTY
            grid[new_row][new_col] = ROBOT
            robot_pos = (new_row, new_col)

    # Calculate the score
    box_positions = find_positions(grid, BOX)
    score = sum(row * 100 + col for row, col in box_positions)
    print(score)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
