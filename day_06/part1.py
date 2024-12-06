with open("day_06/data.txt") as f:
    data = [list(line.strip()) for line in f]

GUARD_ARROWS = ["^", ">", "v", "<"]
visited = set()


def find_arrow(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in GUARD_ARROWS:
                return grid[row][col], (row, col)


while True:
    current_arrow, current_coords = find_arrow(data)
    current_row, current_col = current_coords
    visited.add(current_coords)

    if current_arrow == GUARD_ARROWS[0]:
        try:
            if data[current_row - 1][current_col] == ".":
                data[current_row][current_col] = "."
                data[current_row - 1][current_col] = GUARD_ARROWS[0]
            else:
                data[current_row][current_col] = GUARD_ARROWS[1]
        except IndexError:
            break
    elif current_arrow == GUARD_ARROWS[1]:
        try:
            if data[current_row][current_col + 1] == ".":
                data[current_row][current_col] = "."
                data[current_row][current_col + 1] = GUARD_ARROWS[1]
            else:
                data[current_row][current_col] = GUARD_ARROWS[2]
        except IndexError:
            break
    elif current_arrow == GUARD_ARROWS[2]:
        try:
            if data[current_row + 1][current_col] == ".":
                data[current_row][current_col] = "."
                data[current_row + 1][current_col] = GUARD_ARROWS[2]
            else:
                data[current_row][current_col] = GUARD_ARROWS[3]
        except IndexError:
            break
    elif current_arrow == GUARD_ARROWS[3]:
        try:
            if data[current_row][current_col - 1] == ".":
                data[current_row][current_col] = "."
                data[current_row][current_col - 1] = GUARD_ARROWS[3]
            else:
                data[current_row][current_col] = GUARD_ARROWS[0]
        except IndexError:
            break


print(len(visited))
