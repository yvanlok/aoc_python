from dataclasses import dataclass
from typing import List, Set, Tuple, Dict, Optional
from copy import deepcopy
import time
from datetime import timedelta


@dataclass
class Position:
    row: int
    col: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.row + other.row, self.col + other.col)

    def is_valid(self, grid: List[List[str]]) -> bool:
        return 0 <= self.row < len(grid) and 0 <= self.col < len(grid[0])


class Guard:
    DIRECTIONS: Dict[str, Position] = {
        "^": Position(-1, 0),
        ">": Position(0, 1),
        "v": Position(1, 0),
        "<": Position(0, -1),
    }

    ROTATION = {"^": ">", ">": "v", "v": "<", "<": "^"}

    def __init__(self, symbol: str, pos: Position):
        self.symbol = symbol
        self.pos = pos

    def move(self, grid: List[List[str]]) -> Optional[bool]:
        next_pos = self.pos + self.DIRECTIONS[self.symbol]

        if not next_pos.is_valid(grid):
            return True  # Escape possible

        next_cell = grid[next_pos.row][next_pos.col]

        if next_cell == ".":
            grid[self.pos.row][self.pos.col] = "."
            grid[next_pos.row][next_pos.col] = self.symbol
            self.pos = next_pos
        else:
            self.symbol = self.ROTATION[self.symbol]
            grid[self.pos.row][self.pos.col] = self.symbol

        return False  # Escape not yet possible


def find_guard(grid: List[List[str]]) -> Optional[Guard]:
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell in Guard.DIRECTIONS:
                return Guard(cell, Position(row_index, col_index))
    return None


def possible_escape(grid: List[List[str]]) -> Tuple[bool, Set[Tuple[int, int]]]:
    guard = find_guard(grid)
    if not guard:
        return False, set()

    visited: Set[Tuple[str, int, int]] = set()

    while True:
        current_state = (guard.symbol, guard.pos.row, guard.pos.col)
        if current_state in visited:
            return False, set()
        visited.add(current_state)

        escaped = guard.move(grid)
        if escaped:
            return True, visited


def main():
    start_time = time.perf_counter()

    with open("day_06/data.txt") as f:
        data = [list(line.strip()) for line in f]

    possible_coordinates = [
        (row, col)
        for row in range(len(data))
        for col in range(len(data[0]))
        if data[row][col] == "."
    ]

    num_possible_positions = 0

    for coord in possible_coordinates:
        grid_copy = deepcopy(data)
        # Place obstacle only if it's not the guard's position
        if grid_copy[coord[0]][coord[1]] not in Guard.DIRECTIONS:
            grid_copy[coord[0]][coord[1]] = "O"
            escape_possible, _ = possible_escape(grid_copy)

            if not escape_possible:
                num_possible_positions += 1

    print(f"Number of positions causing an infinite loop: {num_possible_positions}")

    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")


if __name__ == "__main__":
    main()
