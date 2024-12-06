from copy import deepcopy

with open("day_06/data.txt") as f:
    data = [list(line.strip()) for line in f]

GUARD_ARROWS = ["^", ">", "v", "<"]
possible_coordinates = {
    (row, col)
    for row in range(len(data))
    for col in range(len(data[0]))
    if data[row][col] == "."
}


def find_arrow(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in GUARD_ARROWS:
                return grid[row][col], (row, col)


def possible_escape(grid):
    current_arrow, current_coords = find_arrow(grid)
    visited = set()

    while True:
        current_row, current_col = current_coords

        current_information = (current_arrow, current_coords)  # Convert to tuple
        if current_information in visited:
            return False, visited
        else:
            visited.add(current_information)

        if current_arrow == GUARD_ARROWS[0]:  # Up
            if current_row - 1 < 0:  # Escape out of bounds
                return True, visited
            if grid[current_row - 1][current_col] == ".":
                grid[current_row][current_col] = "."
                grid[current_row - 1][current_col] = current_arrow
                current_coords = (current_row - 1, current_col)
            else:
                current_arrow = GUARD_ARROWS[1]  # Turn right
        elif current_arrow == GUARD_ARROWS[1]:  # Right
            if current_col + 1 >= len(grid[0]):  # Escape out of bounds
                return True, visited
            if grid[current_row][current_col + 1] == ".":
                grid[current_row][current_col] = "."
                grid[current_row][current_col + 1] = current_arrow
                current_coords = (current_row, current_col + 1)
            else:
                current_arrow = GUARD_ARROWS[2]  # Turn down
        elif current_arrow == GUARD_ARROWS[2]:  # Down
            if current_row + 1 >= len(grid):  # Escape out of bounds
                return True, visited
            if grid[current_row + 1][current_col] == ".":
                grid[current_row][current_col] = "."
                grid[current_row + 1][current_col] = current_arrow
                current_coords = (current_row + 1, current_col)
            else:
                current_arrow = GUARD_ARROWS[3]  # Turn left
        elif current_arrow == GUARD_ARROWS[3]:  # Left
            if current_col - 1 < 0:  # Escape out of bounds
                return True, visited
            if grid[current_row][current_col - 1] == ".":
                grid[current_row][current_col] = "."
                grid[current_row][current_col - 1] = current_arrow
                current_coords = (current_row, current_col - 1)
            else:
                current_arrow = GUARD_ARROWS[0]  # Turn up


# Count positions that cause infinite loops
num_possible_positions = 0

for coord in possible_coordinates:
    mutated_grid = deepcopy(data)
    mutated_grid[coord[0]][coord[1]] = "O"  # Place the block

    escape_possible, _ = possible_escape(mutated_grid)

    if not escape_possible:
        num_possible_positions += 1

print("Number of positions causing an infinite loop:", num_possible_positions)
