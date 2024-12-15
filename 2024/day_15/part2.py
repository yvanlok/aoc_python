import time
from datetime import timedelta
from collections import deque

# Constants
WALL = "#"
ROBOT = "@"
BOX_LEFT = "["
BOX_RIGHT = "]"
EMPTY = "."

DIRECTIONS = {
    "^": {"name": "up", "translation": (-1, 0)},
    "v": {"name": "down", "translation": (1, 0)},
    "<": {"name": "left", "translation": (0, -1)},
    ">": {"name": "right", "translation": (0, 1)},
}

BOX_CHARS = {BOX_LEFT, BOX_RIGHT}


def find_positions(grid, item):
    positions = []
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == item:
                positions.append((row_index, col_index))
    return positions


def shift_boxes_vertically(grid, start_row, start_col, delta_row):
    queue = deque()
    visited = set()
    queue.append((start_row, start_col))
    visited.add((start_row, start_col))

    # Include the other half of the box
    if grid[start_row][start_col] == BOX_LEFT:
        queue.append((start_row, start_col + 1))
        visited.add((start_row, start_col + 1))
    elif grid[start_row][start_col] == BOX_RIGHT:
        queue.append((start_row, start_col - 1))
        visited.add((start_row, start_col - 1))

    can_shift = True
    temp_queue = deque(queue)
    while temp_queue and can_shift:
        current_row, current_col = temp_queue.popleft()
        next_row = current_row + delta_row
        if grid[next_row][current_col] == WALL:
            can_shift = False
        elif grid[next_row][current_col] in BOX_CHARS:
            if (next_row, current_col) not in visited:
                temp_queue.append((next_row, current_col))
                visited.add((next_row, current_col))
            # Include the other half of the box
            if (
                grid[next_row][current_col] == BOX_LEFT
                and (next_row, current_col + 1) not in visited
            ):
                temp_queue.append((next_row, current_col + 1))
                visited.add((next_row, current_col + 1))
            elif (
                grid[next_row][current_col] == BOX_RIGHT
                and (next_row, current_col - 1) not in visited
            ):
                temp_queue.append((next_row, current_col - 1))
                visited.add((next_row, current_col - 1))

    if can_shift:
        sorted_positions = sorted(
            visited, key=lambda x: -x[0] if delta_row > 0 else x[0]
        )
        for current_row, current_col in sorted_positions:
            next_row = current_row + delta_row
            grid[next_row][current_col] = grid[current_row][current_col]
            grid[current_row][current_col] = EMPTY
    return can_shift


def shift_boxes_horizontally(grid, start_row, start_col, delta_col):
    current_col = start_col
    while grid[start_row][current_col + delta_col] in BOX_CHARS:
        current_col += delta_col
    next_col = current_col + delta_col
    if grid[start_row][next_col] == EMPTY:
        next_char = grid[start_row][start_col]
        for col in range(start_col, next_col, delta_col):
            grid[start_row][col + delta_col] = next_char
            next_char = BOX_RIGHT if next_char == BOX_LEFT else BOX_LEFT
        grid[start_row][start_col] = EMPTY
        return True
    return False


def main():
    with open("day_15/data.txt") as f:
        content = f.read().strip()
        grid_str, steps = content.split("\n\n")
        grid = [list(line.strip()) for line in grid_str.split("\n")]
        steps = steps.replace("\n", "")

    scaled_grid = []
    for row in grid:
        scaled_row = ""
        for tile in row:
            if tile == WALL:
                scaled_row += WALL * 2
            elif tile == "O":
                scaled_row += BOX_LEFT + BOX_RIGHT
            elif tile == EMPTY:
                scaled_row += EMPTY * 2
            elif tile == ROBOT:
                scaled_row += ROBOT + EMPTY
        scaled_grid.append(list(scaled_row))
    grid = scaled_grid

    robot_pos = find_positions(grid, ROBOT)[0]
    for step in steps:
        delta_row, delta_col = DIRECTIONS[step]["translation"]
        row, col = robot_pos
        new_row, new_col = row + delta_row, col + delta_col

        if grid[new_row][new_col] == WALL:
            continue
        elif grid[new_row][new_col] in BOX_CHARS:
            moved = False
            if delta_row != 0:
                moved = shift_boxes_vertically(grid, new_row, new_col, delta_row)
            else:
                moved = shift_boxes_horizontally(grid, new_row, new_col, delta_col)
            if not moved:
                continue
            grid[row][col] = EMPTY
            grid[new_row][new_col] = ROBOT
            robot_pos = (new_row, new_col)
        else:
            grid[row][col] = EMPTY
            grid[new_row][new_col] = ROBOT
            robot_pos = (new_row, new_col)

    score = sum((row * 100 + col) for row, col in find_positions(grid, BOX_LEFT))
    print(score)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
